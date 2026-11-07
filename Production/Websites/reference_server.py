from flask import Flask, abort, send_from_directory
from pathlib import Path
import json, re, time
app = Flask(__name__)
ROOT = Path('/app/data/wan-inputs')
@app.route('/health')
def health(): return {'status': 'ok'}
@app.route('/generation-input/<token>/<filename>')
def reference(token, filename):
    if not re.fullmatch(r'[a-f0-9]{64}', token): abort(404)
    if not re.fullmatch(r'[A-Za-z0-9_.-]+', filename) or Path(filename).suffix.lower() not in {'.jpg','.jpeg','.png','.wav','.mp3','.mp4'}: abort(404)
    folder = ROOT / token
    try: manifest = json.loads((folder / 'manifest.json').read_text('utf-8'))
    except (OSError, ValueError): abort(404)
    if time.time() > manifest.get('expires', 0) or filename not in manifest.get('files', []): abort(404)
    path = folder / filename
    if path.is_symlink() or not path.is_file(): abort(404)
    response = send_from_directory(folder, filename, conditional=True)
    response.headers['Cache-Control'] = 'private, no-store'
    response.headers['X-Robots-Tag'] = 'noindex, nofollow, noarchive'
    return response
