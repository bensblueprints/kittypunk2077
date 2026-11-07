from database import ClosingConnection
import os, json, sqlite3, secrets, time, re
from pathlib import Path
from functools import wraps
from flask import Flask, request, session, redirect, render_template, abort, send_from_directory, g
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.middleware.proxy_fix import ProxyFix
ROOT=Path(__file__).parent
app=Flask(__name__)
app.config.update(SECRET_KEY=os.environ['SECRET_KEY'],SESSION_COOKIE_SECURE=os.environ.get('COOKIE_SECURE','1')=='1',SESSION_COOKIE_HTTPONLY=True,SESSION_COOKIE_SAMESITE='Lax',MAX_CONTENT_LENGTH=16384,PERMANENT_SESSION_LIFETIME=86400,TRUSTED_HOSTS=[os.environ.get('SITE_HOST','localhost'),'localhost','127.0.0.1'])
app.wsgi_app=ProxyFix(app.wsgi_app,x_for=1,x_proto=1)
DB=os.environ.get('DATABASE',str(ROOT/'data/site.sqlite3'))
def db():
 c=sqlite3.connect(DB,timeout=20,factory=ClosingConnection);c.row_factory=sqlite3.Row;return c
with db() as c:
 c.executescript('CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY,email TEXT UNIQUE,password TEXT,staff INTEGER DEFAULT 0,created INTEGER); CREATE TABLE IF NOT EXISTS sessions(token TEXT PRIMARY KEY,user_id INTEGER,expires INTEGER); CREATE TABLE IF NOT EXISTS attempts(ip TEXT,at INTEGER);')
 if not c.execute('SELECT 1 FROM users WHERE staff=1').fetchone():
  c.execute('INSERT INTO users(email,password,staff,created) VALUES(?,?,1,?)',('producer',generate_password_hash(os.environ['ADMIN_PASSWORD']),int(time.time())))
catalog=json.loads((ROOT/'catalog.json').read_text('utf-8'))
audio=json.loads((ROOT/'audio.json').read_text('utf-8'))
episodes=json.loads((ROOT/'episodes.json').read_text('utf-8'))
pilot=json.loads((ROOT/'pilot.json').read_text('utf-8'))
voices=json.loads((ROOT/'voices.json').read_text('utf-8'))
frames=json.loads((ROOT/'frames.json').read_text('utf-8'))
asset_ids={x['id'] for x in catalog+frames};audio_ids={x['id'] for x in audio}
@app.before_request
def before():
 g.user=None
 if session.get('token'):
  with db() as c:g.user=c.execute('SELECT users.* FROM sessions JOIN users ON users.id=sessions.user_id WHERE token=? AND expires>?',(session['token'],time.time())).fetchone()
 if 'csrf' not in session:session['csrf']=secrets.token_urlsafe(24)
 if request.method=='POST' and not secrets.compare_digest(request.form.get('csrf',''),session['csrf']):abort(400)
@app.after_request
def headers(r):
 r.headers['X-Content-Type-Options']='nosniff';r.headers['X-Frame-Options']='DENY';r.headers['Referrer-Policy']='same-origin'
 r.headers['Content-Security-Policy']="default-src 'self'; img-src 'self'; media-src 'self'; style-src 'self'; script-src 'self'; frame-ancestors 'none'; form-action 'self'; base-uri 'self'"
 if request.path.startswith(('/studio','/library','/account','/login','/signup')):r.headers['Cache-Control']='private, no-store'
 return r
def staff(fn):
 @wraps(fn)
 def wrapped(*a,**kw):
  if not g.user:return redirect('/login?studio=1')
  if not g.user['staff']:abort(403)
  return fn(*a,**kw)
 return wrapped
@app.route('/')
def home():return render_template('home.html')
@app.route('/generation-input/<token>/<filename>')
def generation_input(token,filename):
 if not re.fullmatch(r'[a-f0-9]{64}',token):abort(404)
 folder=Path(DB).parent/'wan-inputs'/token
 try:manifest=json.loads((folder/'manifest.json').read_text('utf-8'))
 except (OSError,ValueError):abort(404)
 if time.time()>manifest.get('expires',0) or filename not in manifest.get('files',[]):abort(404)
 response=send_from_directory(folder,filename,conditional=True)
 response.headers['Cache-Control']='private, no-store'
 response.headers['X-Robots-Tag']='noindex, nofollow, noarchive'
 return response
@app.route('/health')
def health():
 with db() as c:c.execute('SELECT 1').fetchone()
 return {'status':'ok','catalog_count':len(catalog)}
@app.route('/signup',methods=['GET','POST'])
@app.route('/login',methods=['GET','POST'])
def auth():
 signup=request.path=='/signup';error='';studio=request.args.get('studio')=='1'
 if request.method=='POST':
  with db() as c:
   now=int(time.time());c.execute('DELETE FROM attempts WHERE at<?',(now-900,))
   if c.execute('SELECT COUNT(*) FROM attempts WHERE ip=?',(request.remote_addr,)).fetchone()[0]>=15:abort(429)
   c.execute('INSERT INTO attempts VALUES(?,?)',(request.remote_addr,now))
  email=request.form.get('email','').strip().lower();password=request.form.get('password','')
  if len(email)>254 or len(password)>128:error='Please use a shorter email or password.'
  elif signup and (not re.fullmatch(r'[^\s@]+@[^\s@]+\.[^\s@]+',email) or len(password)<12):error='Enter a valid email and a password of at least 12 characters.'
  elif signup:
   try:
    with db() as c:c.execute('INSERT INTO users(email,password,created) VALUES(?,?,?)',(email,generate_password_hash(password),int(time.time())))
   except sqlite3.IntegrityError:error='Unable to create this account. Try signing in.'
  if not error:
   with db() as c:user=c.execute('SELECT * FROM users WHERE email=?',(email,)).fetchone()
   if user and check_password_hash(user['password'],password):
    token=secrets.token_urlsafe(32)
    with db() as c:
     c.execute('DELETE FROM sessions WHERE expires<?',(time.time(),));c.execute('INSERT INTO sessions VALUES(?,?,?)',(token,user['id'],int(time.time())+86400))
    session.clear();session['token']=token;session.permanent=True
    return redirect('/studio' if user['staff'] else '/watch')
   error='Email or password was not recognized.'
 return render_template('auth.html',signup=signup,error=error,studio=studio)
@app.post('/logout')
def logout():
 with db() as c:c.execute('DELETE FROM sessions WHERE token=?',(session.get('token',''),))
 session.clear();return redirect('/')
@app.route('/watch')
def watch():
 if not g.user:return redirect('/signup')
 return render_template('watch.html')
@app.route('/studio')
@staff
def studio():
 q=request.args.get('q','').lower();cat=request.args.get('category','All');group=request.args.get('group','All')
 rows=[x for x in catalog if (cat=='All' or x['category']==cat) and (group=='All' or x['group']==group) and q in (x['title']+' '+x['file']+' '+(x['voice'] or '')).lower()]
 return render_template('studio.html',items=rows,total=len(catalog),q=q,cat=cat,group=group,groups=sorted({x['group'] for x in catalog}))
@app.route('/studio/audio')
@staff
def audio_page():return render_template('audio.html',clips=audio)
@app.route('/studio/episodes')
@staff
def episodes_page():return render_template('episodes.html',episodes=episodes)
@app.route('/studio/episodes/1/1')
@staff
def pilot_page():return render_template('pilot.html',pilot=pilot)
@app.route('/studio/voices')
@staff
def voices_page():return render_template('voices.html',voices=voices)
@app.route('/studio/downloads/<name>')
@staff
def production_download(name):
 if name not in {'voice-registry.json','voice-registry.csv','shot-timeline-v004.csv','dialogue-cue-sheet-v004.csv','full-timed-script-v004.txt','pilot-production-map-v004.json','validation-v003.json','scene-shot-references.csv'}:abort(404)
 return send_from_directory(ROOT/'downloads',name,as_attachment=True)
@app.route('/library/<ident>.<ext>')
@staff
def library(ident,ext):
 if not ((ident in asset_ids and ext in ['jpg','webp']) or (ident in audio_ids and ext=='mp3')):abort(404)
 return send_from_directory(ROOT/'library',ident+'.'+ext,conditional=True)
@app.route('/account',methods=['GET','POST'])
def account():
 if not g.user:return redirect('/login')
 error='';message=''
 if request.method=='POST':
  if not check_password_hash(g.user['password'],request.form.get('current','')):error='Current password is incorrect.'
  elif request.form.get('action')=='delete' and not g.user['staff']:
   with db() as c:c.execute('DELETE FROM sessions WHERE user_id=?',(g.user['id'],));c.execute('DELETE FROM users WHERE id=?',(g.user['id'],))
   session.clear();return redirect('/')
  elif 12<=len(request.form.get('new',''))<=128:
   with db() as c:c.execute('UPDATE users SET password=? WHERE id=?',(generate_password_hash(request.form['new']),g.user['id']));c.execute('DELETE FROM sessions WHERE user_id=? AND token<>?',(g.user['id'],session['token']))
   message='Password updated. Other sessions have been signed out.'
  else:error='Use a new password of 12â€“128 characters.'
 return render_template('account.html',error=error,message=message)
@app.route('/privacy')
def privacy():return render_template('privacy.html')
@app.errorhandler(403)
@app.errorhandler(404)
@app.errorhandler(429)
@app.errorhandler(400)
def error(e):return render_template('error.html',code=e.code),e.code

from production import register
register(app,db,staff,ROOT,DB)
