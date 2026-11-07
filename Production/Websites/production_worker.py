from database import ClosingConnection
"""One durable production worker. Persist task IDs; never retry uncertain submissions."""
import os,json,time,sqlite3,urllib.request,urllib.error,urllib.parse,uuid,shutil,subprocess
from pathlib import Path
from production import init_tables
ROOT=Path(__file__).parent;DB=os.environ.get('DATABASE',str(ROOT/'data/site.sqlite3'));DATA=Path(DB).parent
OUT=DATA/'generated';OUT.mkdir(parents=True,exist_ok=True)
DEEPSEEK_MODEL=os.environ.get('ORBIS_DEEPSEEK_MODEL','deepseek-v4.1-flash')
def connect():
 c=sqlite3.connect(DB,timeout=30,factory=ClosingConnection);c.row_factory=sqlite3.Row;return c
init_tables(connect)
def update(ident,**values):
 values['updated']=time.time()
 with connect() as c:c.execute('UPDATE production_jobs SET '+','.join(k+'=?' for k in values)+' WHERE id=?',(*values.values(),ident))
def secret(provider):return os.environ.get({'wan':'ORBIS_WAN_API_KEY','elevenlabs':'ELEVENLABS_API_KEY','deepseek':'ORBIS_DEEPSEEK_API_KEY'}[provider],'')
def call(url,provider,payload=None,timeout=180):
 key=secret(provider)
 if not key:raise ValueError('Missing server credential for '+provider)
 headers={'Content-Type':'application/json'};headers.update({'xi-api-key':key} if provider=='elevenlabs' else {'Authorization':'Bearer '+key})
 req=urllib.request.Request(url,data=None if payload is None else json.dumps(payload).encode(),headers=headers)
 try:
  with urllib.request.urlopen(req,timeout=timeout) as r:return r.read(),dict(r.headers)
 except urllib.error.HTTPError as e:
  message=e.read().decode('utf-8','replace').replace(key,'[redacted]')[:350]
  raise ValueError('Provider HTTP '+str(e.code)+': '+message) from None
def jcall(*args,**kwargs):return json.loads(call(*args,**kwargs)[0])
def stage(paths):
 token=uuid.uuid4().hex+uuid.uuid4().hex;folder=DATA/'wan-inputs'/token;folder.mkdir(parents=True)
 files=[]
 for i,value in enumerate(paths):
  path=(ROOT/value).resolve()
  if not path.is_relative_to(ROOT.resolve()) or not path.is_file():raise ValueError('Missing prepared reference')
  name=f'input-{i}'+path.suffix;shutil.copy2(path,folder/name);files.append(name)
 (folder/'manifest.json').write_text(json.dumps({'expires':int(time.time())+86400,'files':files}))
 base='https://'+os.environ['SITE_HOST']+'/generation-input/'+token+'/'
 return [base+n for n in files]
def revise(payload):
 result=jcall('https://api.orbiorbi.com/v1/chat/completions','deepseek',{'model':DEEPSEEK_MODEL,'messages':[{'role':'system','content':'Revise an animation prompt using the producer correction. Return ONLY the revised prompt, maximum 2900 characters. Preserve all cast identities, five-cat limit, set continuity, camera shot length, gameplay strictly inside physical TV glass, and offscreen versus onscreen speakers. Do not invent visual inspection findings; you only have text. Do not change safety or API settings. Do not output JSON or commentary.'},{'role':'user','content':payload['prompt']}],'max_tokens':1300})
 text=result['choices'][0]['message']['content'].strip()
 if not text or len(text)>3000:raise ValueError('DeepSeek revision exceeded WAN prompt limit; no video submitted')
 payload['original_prompt']=payload['prompt'];payload['prompt']=text;payload['deepseek_usage']=result.get('usage',{});return payload
def run_job(job):
 ident=job['id'];p=json.loads(job['payload'])
 if job['provider']=='wan':
  if p.get('refine'):p=revise(p);update(ident,payload=json.dumps(p))
  api={k:p[k] for k in ['model','prompt','duration_sec','resolution','aspect_ratio']}
  # Prefer the proven source image-host URL. Never submit platform file IDs.
  if p.get('input_images'):api['input_images']=p['input_images']
  elif p.get('source_images'):api['input_images']=stage(p['source_images'])
  if p.get('input_audios'):api['input_audios']=p['input_audios']
  elif p.get('source_audio'):api['input_audios']=stage(p['source_audio'])
  before=jcall('https://api.orbiorbi.com/v1/models','wan',timeout=30)
  if not any(x.get('id')=='wan-3.0-prime' for x in before.get('data',[])):raise ValueError('WAN model absent from route; no video submitted')
  result=jcall('https://api.orbiorbi.com/v1/tasks','wan',api)
  taskid=result.get('task_id') or result.get('id')
  if not taskid:raise RuntimeError('Submission returned no task ID; inspect provider console before retrying')
  update(ident,task_id=taskid,status=result.get('status','queued'))
 else:
  subscription=jcall('https://api.elevenlabs.io/v1/user/subscription','elevenlabs',timeout=30)
  if subscription.get('character_limit',0)-subscription.get('character_count',0)<len(p['text'])*3+1000:raise ValueError('Insufficient included ElevenLabs credit headroom')
  settings={'stability':.5,'similarity_boost':.75,'style':.15,'use_speaker_boost':True}
  if p.get('role_id')=='trixie':settings.update(stability=.35,similarity_boost=.8,style=.55)
  if p.get('role_id')=='chairman_barkington':settings.update(stability=.4,style=.65,speed=.9)
  content,headers=call('https://api.elevenlabs.io/v1/text-to-speech/'+urllib.parse.quote(p['voice_id'],safe='')+'?output_format=mp3_44100_128','elevenlabs',{'text':p['text'],'model_id':p['model_id'],'voice_settings':settings})
  file=OUT/(ident+'.mp3');file.write_bytes(content)
  subprocess.run(['ffmpeg','-v','error','-i',str(file),'-f','null','-'],check=True,capture_output=True)
  update(ident,status='completed',output=file.name)
  register_review(job,file,'audio')
def register_review(job,file,kind):
 rel=file.relative_to(ROOT).as_posix()
 with connect() as c:c.execute('INSERT OR IGNORE INTO review_versions(id,scene,label,kind,file,created) VALUES(?,?,?,?,?,?)',(job['id'],job['scene'],job['subject']+' Â· '+job['id'][:8],kind,rel,time.time()))
def poll(job):
 result=jcall('https://api.orbiorbi.com/v1/tasks/'+urllib.parse.quote(job['task_id'],safe=''),'wan',timeout=30)
 status=result.get('status')
 if status=='failed':update(job['id'],status='failed',error=json.dumps(result.get('error',{}),ensure_ascii=False)[:800]);return
 if status!='completed':update(job['id'],status=status if status in ['queued','in_progress'] else 'in_progress');return
 url=result.get('metadata',{}).get('url');parsed=urllib.parse.urlsplit(url or '')
 if parsed.scheme not in ['https','http'] or not parsed.hostname or parsed.username:raise ValueError('Invalid video result URL')
 file=OUT/(job['id']+'.mp4');raw=OUT/(job['id']+'-raw.mp4')
 if not raw.exists():
  with urllib.request.urlopen(url,timeout=300) as r,raw.with_suffix('.partial').open('wb') as f:shutil.copyfileobj(r,f)
  raw.with_suffix('.partial').replace(raw)
 p=json.loads(job['payload']);inputs=['ffmpeg','-v','error','-i',str(raw)]
 audios=p.get('source_audio',[])
 if audios:
  inputs+=['-i',str(ROOT/audios[0]),'-map','0:v:0','-map','1:a:0','-c:a','aac','-b:a','192k']
 else:inputs+=['-an']
 inputs+=['-t',str(p.get('edit_duration',p.get('duration_sec',30))),'-c:v','copy','-movflags','+faststart','-y',str(file)]
 subprocess.run(inputs,check=True,capture_output=True);update(job['id'],status='completed',output=file.name,error=None);register_review(job,file,'shot')
def main():
 # A crash between POST and persisted task ID is uncertain, never auto-resubmit.
 with connect() as c:c.execute("UPDATE production_jobs SET status='submission_unknown',error='Worker restarted during submission; check provider records before retrying' WHERE status='submitting' AND task_id IS NULL")
 lastpoll=0
 while True:
  with connect() as c:
   c.execute('BEGIN IMMEDIATE');job=c.execute("SELECT * FROM production_jobs WHERE status='queued_local' ORDER BY created LIMIT 1").fetchone()
   if job:c.execute("UPDATE production_jobs SET status='submitting',updated=? WHERE id=?",(time.time(),job['id']))
  if job:
   try:run_job(job)
   except ValueError as e:update(job['id'],status='failed',error=str(e)[:800])
   except Exception:update(job['id'],status='submission_unknown',error='Transport or save outcome uncertain. Check provider records; no automatic retry.')
  if time.time()-lastpoll>=300:
   with connect() as c:jobs=c.execute("SELECT * FROM production_jobs WHERE provider='wan' AND task_id IS NOT NULL AND status IN ('queued','in_progress')").fetchall()
   for pending in jobs:
    try:poll(pending)
    except Exception:update(pending['id'],error='Status/download check did not complete; same task will be checked again, no new generation.')
   lastpoll=time.time()
  time.sleep(2)
if __name__=='__main__':main()
