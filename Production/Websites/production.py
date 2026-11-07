"""Private producer review history and durable, explicitly submitted generation jobs."""
import json,os,sqlite3,time,uuid,re
from pathlib import Path
from flask import request,render_template,redirect,abort,g,send_from_directory,session

ACTIVE=('queued_local','submitting','queued','in_progress','submission_unknown')
def init_tables(connect):
 with connect() as c:
  c.executescript('''CREATE TABLE IF NOT EXISTS production_jobs(
   id TEXT PRIMARY KEY,provider TEXT,subject TEXT,scene INTEGER,payload TEXT,status TEXT,
   task_id TEXT,error TEXT,output TEXT,created REAL,updated REAL,owner INTEGER,estimate REAL);
  CREATE TABLE IF NOT EXISTS review_versions(
   id TEXT PRIMARY KEY,scene INTEGER,label TEXT,kind TEXT,file TEXT,created REAL,status TEXT DEFAULT 'pending');
  CREATE TABLE IF NOT EXISTS review_events(
   id INTEGER PRIMARY KEY,version_id TEXT,decision TEXT,feedback TEXT,owner INTEGER,created REAL);
  CREATE TABLE IF NOT EXISTS provider_checks(provider TEXT PRIMARY KEY,result TEXT,checked REAL);
  ''')

def register(app,connect,staff,root,dbpath):
 init_tables(connect)
 data=Path(dbpath).parent
 def configs():return json.loads((root/'generation-shots.json').read_text())
 def lines():return {l['id']:dict(l,scene=s['number']) for s in json.loads((root/'pilot.json').read_text())['scenes'] for l in s['lines']}
 def casting():return {v['role_id']:v for v in json.loads((root/'voices.json').read_text())}
 seeds=root/'review-seeds.json'
 if seeds.exists():
  with connect() as c:
   for x in json.loads(seeds.read_text()):c.execute('INSERT OR IGNORE INTO review_versions(id,scene,label,kind,file,created) VALUES(?,?,?,?,?,?)',(x['id'],x['scene'],x['label'],x['kind'],x['file'],time.time()))
 jobs_seed=root/'generation-job-seeds.json'
 if jobs_seed.exists():
  with connect() as c:
   owner=c.execute('SELECT id FROM users WHERE staff=1 LIMIT 1').fetchone()[0]
   for x in json.loads(jobs_seed.read_text()):
    c.execute('INSERT OR IGNORE INTO production_jobs VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)',(x['id'],x['provider'],x['subject'],x['scene'],json.dumps(x['payload']),x['status'],x.get('task_id'),x.get('error'),None,x['created'],time.time(),owner,x['estimate']))
 balance_seed=root/'provider-balance-snapshot.json'
 if balance_seed.exists():
  with connect() as c:
   for x in json.loads(balance_seed.read_text()):
    existing=c.execute('SELECT checked FROM provider_checks WHERE provider=?',(x['provider'],)).fetchone()
    if not existing or existing['checked']<x['checked']:c.execute('INSERT OR REPLACE INTO provider_checks VALUES(?,?,?)',(x['provider'],x['result'],x['checked']))

 @app.get('/studio/review')
 @staff
 def review_page():
  with connect() as c:
   versions=[dict(x) for x in c.execute("SELECT * FROM review_versions WHERE status != 'archived' ORDER BY scene,created DESC")]
   events=[dict(x) for x in c.execute('SELECT e.*,u.email FROM review_events e LEFT JOIN users u ON u.id=e.owner ORDER BY e.id DESC')]
  return render_template('review.html',versions=versions,events=events,scenes=json.loads((root/'pilot.json').read_text())['scenes'])

 @app.post('/studio/review/<version>')
 @staff
 def review_submit(version):
  decision=request.form.get('decision');feedback=request.form.get('feedback','').strip()
  if decision not in ['approved','regenerate'] or len(feedback)>4000:abort(400)
  if decision=='regenerate' and not feedback:return redirect('/studio/review?message=Add+what+needs+fixing#'+version)
  with connect() as c:
   c.execute('BEGIN IMMEDIATE')
   review=c.execute('SELECT * FROM review_versions WHERE id=?',(version,)).fetchone()
   if not review:abort(404)
   if review['status']=='archived':abort(409)
   c.execute('INSERT INTO review_events(version_id,decision,feedback,owner,created) VALUES(?,?,?,?,?)',(version,decision,feedback,g.user['id'],time.time()))
   c.execute('UPDATE review_versions SET status=? WHERE id=?',(decision,version))
  message='Review saved'
  if decision=='regenerate' and review['kind']=='shot':
   match=re.match(r'(S[0-9]+-P[0-9]+)',review['label']);subject=match.group(1) if match else None
   config=configs().get(subject)
   if config and os.environ.get('ORBIS_WAN_API_KEY'):
    payload=dict(config);payload['refine']=bool(os.environ.get('ORBIS_DEEPSEEK_API_KEY'))
    payload['prompt']+='\nProducer correction for this version: '+feedback
    payload['source_review']=version;payload['producer_feedback']=feedback
    estimate=payload['duration_sec']*{'480p':.275,'720p':.55,'1080p':1.1}[payload['resolution']]
    if len(payload['prompt'])<=3000 or payload['refine']:
     with connect() as c:
      c.execute('BEGIN IMMEDIATE')
      active=c.execute('SELECT id FROM production_jobs WHERE provider=? AND subject=? AND status IN (?,?,?,?,?)',('wan',subject,*ACTIVE)).fetchone()
      if active:message+='; a shot job is already active, so no duplicate was created'
      else:
       ident=uuid.uuid4().hex;now=time.time()
       c.execute('INSERT INTO production_jobs VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)',(ident,'wan',subject,review['scene'],json.dumps(payload),'queued_local',None,None,None,now,now,g.user['id'],estimate))
       message+='; corrected shot queued as a new version'
    else:message+='; correction exceeds the prompt limit, shorten it in the generation desk'
   else:message+='; use the generation desk to prepare this retry'
  from urllib.parse import quote
  return redirect('/studio/review?message='+quote(message)+'#'+version)

 @app.get('/studio/review-media/<version>')
 @staff
 def review_media(version):
  with connect() as c:r=c.execute('SELECT file FROM review_versions WHERE id=?',(version,)).fetchone()
  if not r:abort(404)
  p=Path(r['file'])
  if p.is_absolute() or '..' in p.parts:abort(404)
  return send_from_directory(root,p.as_posix(),conditional=True)

 @app.get('/studio/generate')
 @staff
 def generation_page():
  with connect() as c:jobs=[dict(x) for x in c.execute('SELECT id,provider,subject,scene,status,error,output,created,estimate,task_id FROM production_jobs ORDER BY created DESC LIMIT 1000')];checks=[dict(x) for x in c.execute('SELECT * FROM provider_checks')]
  history=json.loads((root/'generation-history.json').read_text()) if (root/'generation-history.json').exists() else []
  live={j['task_id'] for j in jobs};history=[j for j in history if j.get('task_id') not in live]
  return render_template('generate.html',history=history,deepseek_ready=bool(os.environ.get('ORBIS_DEEPSEEK_API_KEY')),jobs=jobs,shots=configs(),lines=list(lines().values()),voices=list(casting().values()),wan_ready=bool(os.environ.get('ORBIS_WAN_API_KEY')),eleven_ready=bool(os.environ.get('ELEVENLABS_API_KEY')),checks=checks)

 @app.post('/studio/generate')
 @staff
 def generation_submit():
  provider=request.form.get('provider');subject=request.form.get('subject','');notes=request.form.get('notes','').strip();estimate=0
  if len(notes)>1800:abort(400)
  if provider=='wan':
   if not os.environ.get('ORBIS_WAN_API_KEY'):abort(400)
   config=configs().get(subject)
   if not config:abort(400)
   payload=dict(config);scene=config['scene'];res=request.form.get('resolution','1080p')
   if res not in ['480p','720p','1080p']:abort(400)
   duration=int(config['duration_sec']);estimate=duration*{'480p':.275,'720p':.55,'1080p':1.1}[res]
   payload['refine']=request.form.get('refine')=='1';payload['resolution']=res;payload['prompt']=config['prompt']+('\nCorrection requested by producer: '+notes if notes else '')
   if len(payload['prompt'])>3000:return redirect('/studio/generate?message=Correction+is+too+long+for+WAN')
   try:cap=float(request.form.get('cost_cap','50'))
   except ValueError:abort(400)
   if not 0<cap<=1000 or estimate>cap:return redirect('/studio/generate?message=Job+exceeds+your+cost+cap')
  elif provider=='elevenlabs':
   if not os.environ.get('ELEVENLABS_API_KEY'):abort(400)
   line=lines().get(subject)
   if not line:abort(400)
   voice=casting().get(request.form.get('voice_role') or line['role_id'])
   if not voice:abort(400)
   text=request.form.get('text','').strip() or line['text']
   if not 1<=len(text)<=5000:abort(400)
   scene=line['scene'];payload={'text':text,'voice_id':voice['voice_id'],'voice_name':voice['voice_name'],'role_id':line['role_id'],'model_id':'eleven_multilingual_v2','notes':notes};estimate=len(text)
  else:abort(400)
  with connect() as c:
   c.execute('BEGIN IMMEDIATE')
   active=c.execute('SELECT id FROM production_jobs WHERE provider=? AND subject=? AND status IN (?,?,?,?,?)',(provider,subject,*ACTIVE)).fetchone()
   if active:return redirect('/studio/generate?message=This+item+already+has+an+active+job')
   ident=uuid.uuid4().hex;now=time.time()
   c.execute('INSERT INTO production_jobs VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)',(ident,provider,subject,scene,json.dumps(payload),'queued_local',None,None,None,now,now,g.user['id'],estimate))
  return redirect('/studio/generate?message=Job+queued')

 @app.post('/studio/jobs/<ident>/retry')
 @staff
 def job_retry(ident):
  with connect() as c:
   c.execute('BEGIN IMMEDIATE');r=c.execute('SELECT * FROM production_jobs WHERE id=?',(ident,)).fetchone()
   if not r or r['status']!='failed':abort(400)
   active=c.execute('SELECT id FROM production_jobs WHERE provider=? AND subject=? AND status IN (?,?,?,?,?)',(r['provider'],r['subject'],*ACTIVE)).fetchone()
   if active:return redirect('/studio/generate?message=Already+running')
   new=uuid.uuid4().hex;now=time.time()
   c.execute('INSERT INTO production_jobs VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)',(new,r['provider'],r['subject'],r['scene'],r['payload'],'queued_local',None,None,None,now,now,g.user['id'],r['estimate']))
  return redirect('/studio/generate?message=Retry+queued+as+a+new+version')

 @app.get('/studio/job-media/<ident>')
 @staff
 def job_media(ident):
  with connect() as c:r=c.execute('SELECT output FROM production_jobs WHERE id=?',(ident,)).fetchone()
  if not r or not r['output']:abort(404)
  return send_from_directory(data/'generated',Path(r['output']).name,conditional=True)

 @app.post('/studio/providers/check')
 @staff
 def provider_check():
  import urllib.request
  provider=request.form.get('provider')
  if provider=='wan':url='https://api.orbiorbi.com/v1/models';headers={'Authorization':'Bearer '+os.environ.get('ORBIS_WAN_API_KEY','')}
  elif provider=='deepseek':url='https://api.orbiorbi.com/v1/models';headers={'Authorization':'Bearer '+os.environ.get('ORBIS_DEEPSEEK_API_KEY','')}
  elif provider=='elevenlabs':url='https://api.elevenlabs.io/v1/user/subscription';headers={'xi-api-key':os.environ.get('ELEVENLABS_API_KEY','')}
  else:abort(400)
  try:
   with urllib.request.urlopen(urllib.request.Request(url,headers=headers),timeout=15) as r:result=json.load(r)
   if provider=='wan':message='WAN route ready' if any(x.get('id')=='wan-3.0-prime' for x in result.get('data',[])) else 'Key works, but WAN model is absent on this route'
   elif provider=='deepseek':message='DeepSeek text route ready' if any(x.get('id')==os.environ.get('ORBIS_DEEPSEEK_MODEL','deepseek-v4.1-flash') for x in result.get('data',[])) else 'DeepSeek model missing from route'
   else:message='Included credits remaining: '+str(result.get('character_limit',0)-result.get('character_count',0))
  except Exception:message='Connection check failed; verify server credential and route'
  with connect() as c:c.execute('INSERT OR REPLACE INTO provider_checks VALUES(?,?,?)',(provider,message,time.time()))
  return redirect('/studio/generate')
