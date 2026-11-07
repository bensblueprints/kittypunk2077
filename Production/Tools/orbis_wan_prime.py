"""Orbis Wan3.0Prime official-A route; Python standard HTTP, no SDK.
Submit once, persist ID, query the documented task endpoint, download without credentials.
"""
from pathlib import Path
import argparse, datetime, hashlib, json, os, urllib.request, urllib.error, urllib.parse
MODEL='wan-3.0-prime'
BASE='https://api.orbiorbi.com'
DOC='https://orbiorbi.com/api/developer-docs/published/openplane-wan-3-0-prime-official-a'
MINIMAL={'model':MODEL,'prompt':'一只小船漂过平静湖面，镜头缓慢拉远，清晨自然光。','duration_sec':2,'resolution':'480p','aspect_ratio':'16:9'}
PRICES={'480p':.275,'720p':.55,'1080p':1.1}

def load_env(path):
 for line in Path(path).read_text('utf-8-sig').splitlines():
  if line.strip() and not line.lstrip().startswith('#') and '=' in line:
   k,v=line.split('=',1);os.environ.setdefault(k.strip(),v.strip().strip('\"\''))

def save(path,obj):
 path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
 tmp=path.with_suffix(path.suffix+'.tmp');tmp.write_text(json.dumps(obj,ensure_ascii=False,indent=2),'utf-8');tmp.replace(path)

def request(path,payload=None):
 key=os.environ.get('ORBIS_API_KEY')
 if not key:raise RuntimeError('ORBIS_API_KEY missing')
 req=urllib.request.Request(BASE+path,data=None if payload is None else json.dumps(payload,ensure_ascii=False).encode('utf-8'),headers={'Authorization':'Bearer '+key,'Content-Type':'application/json'})
 try:
  with urllib.request.urlopen(req,timeout=180 if payload is not None else 30) as res:return json.load(res)
 except urllib.error.HTTPError as exc:
  msg=exc.read().decode('utf-8','replace').replace(key,'[redacted]')
  raise RuntimeError(f'HTTP {exc.code}: {msg[:1200]}') from None
 except (TimeoutError,urllib.error.URLError) as exc:
  raise RuntimeError('Transport did not complete; do not resubmit a POST. Check task records first.') from None

def validate(p):
 allowed={'model','prompt','resolution','aspect_ratio','duration_sec','input_images','input_audios','input_videos'}
 if set(p)-allowed:raise ValueError('Unsupported route fields: '+','.join(sorted(set(p)-allowed)))
 if p.get('model')!=MODEL:raise ValueError('Wrong route model')
 if not isinstance(p.get('prompt'),str) or not 1<=len(p['prompt'])<=3000:raise ValueError('Prompt must be 1–3000 characters')
 if type(p.get('duration_sec')) is not int or not 2<=p['duration_sec']<=30:raise ValueError('Duration must be integer 2–30')
 if p.get('resolution') not in PRICES:raise ValueError('Resolution must be 480p,720p,1080p')
 if p.get('aspect_ratio') not in ['adaptive','16:9','4:3','1:1','3:4','9:16']:raise ValueError('Invalid aspect ratio')
 total=0
 for field,cap in [('input_images',10),('input_audios',5),('input_videos',5)]:
  items=p.get(field,[])
  if not isinstance(items,list) or len(items)>cap:raise ValueError(f'{field} exceeds {cap}')
  for url in items:
   if not isinstance(url,str):raise ValueError('Reference must be a public direct URL')
   parsed=urllib.parse.urlsplit(url)
   if parsed.scheme not in ['http','https'] or not parsed.netloc or parsed.username or parsed.password:raise ValueError('Reference must be a public direct HTTP(S) URL without credentials')
  total+=len(items)
 if total>15:raise ValueError('Mixed references exceed 15')
 return {'estimated_cny':round(PRICES[p['resolution']]*p['duration_sec'],3),'reference_total':total}

def check():
 data=request('/v1/models');ids=[x.get('id') for x in data.get('data',[]) if isinstance(x,dict)]
 if MODEL not in ids:raise RuntimeError('Key authenticated, but wan-3.0-prime is missing; no generation submitted. Use the official-A route key.')
 return {'model':MODEL,'route_access_verified':True}

def submit(folder,payload):
 folder=Path(folder);folder.mkdir(parents=True,exist_ok=True);receipt=folder/'receipt.json'
 if receipt.exists():raise RuntimeError('Receipt exists; query it. Never resubmit automatically.')
 quote=validate(payload);verified=check()
 save(folder/'request.json',payload)
 state={'model':MODEL,'documentation':DOC,'status':'submission_started','created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'post_requests':1,'auto_retries':0,**quote,**verified}
 save(receipt,state)
 try:
  result=request('/v1/tasks',payload);save(folder/'submitted.json',result)
  ident=result.get('task_id') or result.get('id')
  if not ident:raise RuntimeError('No task ID returned; inspect submitted.json and console before retrying')
  state.update(task_id=str(ident),status=result.get('status','queued'));save(receipt,state)
 except Exception as exc:
  state.update(status='submission_failed_or_unknown',error=str(exc));save(receipt,state);raise
 return {k:state[k] for k in ['task_id','status','estimated_cny']}

def poll(folder):
 folder=Path(folder);state=json.loads((folder/'receipt.json').read_text('utf-8'));ident=state.get('task_id')
 if not ident:raise RuntimeError('No task ID to query; check console; do not resubmit')
 result=request('/v1/tasks/'+urllib.parse.quote(ident,safe=''));save(folder/'task.json',result)
 state.update(status=result.get('status'),progress=result.get('progress'),last_polled_utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
 if state['status']=='failed':state['error']=result.get('error',{}).get('message','Task failed')
 save(folder/'receipt.json',state)
 return {k:state.get(k) for k in ['task_id','status','progress','error'] if state.get(k) is not None}

def download(folder):
 folder=Path(folder);task=json.loads((folder/'task.json').read_text('utf-8'))
 if task.get('status')!='completed':raise RuntimeError('Task is not completed')
 url=task.get('metadata',{}).get('url')
 if not url or urllib.parse.urlsplit(url).scheme not in ['https','http']:raise RuntimeError('Missing or invalid metadata.url')
 path=folder/'output.mp4';temp=folder/'output.mp4.partial'
 # No Orbis Authorization header is sent to the media download host.
 with urllib.request.urlopen(url,timeout=300) as response,temp.open('wb') as f:
  while block:=response.read(1024*1024):f.write(block)
 if temp.stat().st_size==0:raise RuntimeError('Downloaded file is empty')
 temp.replace(path);state=json.loads((folder/'receipt.json').read_text('utf-8'));state.update(downloaded_file=str(path.resolve()),bytes=path.stat().st_size,sha256=hashlib.sha256(path.read_bytes()).hexdigest());save(folder/'receipt.json',state)
 return {'saved':str(path.resolve()),'bytes':path.stat().st_size}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('action',choices=['check','submit-minimal','submit','poll','download']);ap.add_argument('--env',default='.env');ap.add_argument('--out',default='outputs/Wan Orbis Route Test');ap.add_argument('--request');args=ap.parse_args();load_env(args.env)
 if args.action=='check':result=check()
 elif args.action.startswith('submit'):result=submit(args.out,MINIMAL if args.action=='submit-minimal' else json.loads(Path(args.request).read_text('utf-8-sig')))
 elif args.action=='poll':result=poll(args.out)
 else:result=download(args.out)
 print(json.dumps(result,ensure_ascii=False))
if __name__=='__main__':main()
