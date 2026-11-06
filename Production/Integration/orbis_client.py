"""Orbis Nano Banana EE route. Native Gemini synchronous HTTP, no SDK.

Use check first; generate submits exactly once and never auto-retries.
"""
from pathlib import Path
import os,json,urllib.request,urllib.error,base64,argparse,hashlib,datetime

ROOT=Path(__file__).resolve().parents[1]
MODEL='gemini-nano-banana-2.1'
BASE='https://api.orbiorbi.com'
DOC='https://orbiorbi.com/api/developer-docs/published/nano-banana-2-1-line02'
MINIMAL_PROMPT='一只橘猫坐在窗台上，午后阳光，胶片质感'

def load_env(path=ROOT/'.env'):
    if path.exists():
        for line in path.read_text(encoding='utf-8-sig').splitlines():
            if line.strip() and not line.lstrip().startswith('#') and '=' in line:
                k,v=line.split('=',1)
                os.environ.setdefault(k.strip(),v.strip().strip('\"\''))

def request(path,payload=None,timeout=180):
    key=os.environ.get('ORBIS_API_KEY')
    if not key: raise RuntimeError('Set ORBIS_API_KEY in the local .env or environment.')
    req=urllib.request.Request(BASE+path,data=None if payload is None else json.dumps(payload,ensure_ascii=False).encode(),headers={'Authorization':'Bearer '+key,'Content-Type':'application/json','User-Agent':'CyberKitty-production/1.0'})
    try:
        with urllib.request.urlopen(req,timeout=max(120,timeout)) as res: return json.load(res)
    except urllib.error.HTTPError as e:
        raw=e.read().decode('utf-8','replace').replace(key,'[REDACTED]')
        safe_dir=ROOT/'work';safe_dir.mkdir(exist_ok=True)
        (safe_dir/'orbis-last-error.json').write_text(json.dumps({'status':e.code,'response':raw[:5000]},ensure_ascii=False,indent=2),encoding='utf-8')
        if e.code==401: raise RuntimeError('Orbis returned 401: invalid key or wrong route.') from None
        raise RuntimeError(f'Orbis HTTP {e.code}. Sanitized details saved in work/orbis-last-error.json. No automatic retry sent.') from None
    except (TimeoutError,urllib.error.URLError):
        raise RuntimeError('Request did not complete. Check Orbis usage logs before retrying to avoid duplicate charges.') from None

def check():
    data=request('/v1/models')
    rows=data.get('data',[]) if isinstance(data,dict) else []
    match=[x for x in rows if isinstance(x,dict) and x.get('id')==MODEL]
    if not match: raise RuntimeError('Key authenticated but target model is absent: do not generate on this route.')
    return {'route_verified':True,'model':MODEL,'matched_model':match[0]}

def generate(prompt,out_dir):
    out=Path(out_dir);out.mkdir(parents=True,exist_ok=True)
    stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    payload={'contents':[{'role':'user','parts':[{'text':prompt}]}],'generationConfig':{'responseModalities':['TEXT','IMAGE']}}
    (out/f'{stamp}-request.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2),encoding='utf-8')
    data=request(f'/v1beta/models/{MODEL}:generateContent',payload,180)
    files=[];notes=[];finish=[]
    for ci,candidate in enumerate(data.get('candidates',[])):
        finish.append(candidate.get('finishReason'))
        for pi,part in enumerate(candidate.get('content',{}).get('parts',[])):
            if 'text' in part: notes.append(part['text'])
            im=part.get('inlineData')
            if not im: continue
            ext={'image/png':'png','image/jpeg':'jpg','image/webp':'webp'}.get(im.get('mimeType'))
            if ext is None: raise RuntimeError('Unsupported image MIME returned; no guessed extension used.')
            blob=base64.b64decode(im['data'],validate=True)
            path=out/f'{stamp}-image-{ci}-{pi}.{ext}'
            path.write_bytes(blob)
            files.append({'path':str(path),'mime':im['mimeType'],'bytes':len(blob),'sha256':hashlib.sha256(blob).hexdigest()})
    receipt={'model':MODEL,'documentation':DOC,'finish_reasons':finish,'images':files,'text':notes,'usageMetadata':data.get('usageMetadata'),'submitted_requests':1,'actual_usd':None,'cost_note':'Provider bills per request. Actual charge must be read from Orbis usage; token counts are not a dollar price.'}
    (out/f'{stamp}-receipt.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2),encoding='utf-8')
    if not files: raise RuntimeError('Orbis returned no inline image. Receipt saved; no automatic retry sent.')
    return receipt

if __name__=='__main__':
    load_env()
    parser=argparse.ArgumentParser();parser.add_argument('command',choices=['check','minimal','generate']);parser.add_argument('--prompt-file');parser.add_argument('--out',default=str(ROOT/'outputs'/'Orbis Test'))
    args=parser.parse_args()
    if args.command=='check': result=check()
    else:
        check()
        if args.command=='generate' and not args.prompt_file: parser.error('--prompt-file required')
        prompt=MINIMAL_PROMPT if args.command=='minimal' else Path(args.prompt_file).read_text(encoding='utf-8')
        result=generate(prompt,args.out)
    print(json.dumps(result,ensure_ascii=False,indent=2))
