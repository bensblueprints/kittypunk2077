"""Orbis GPT Image EE route; Python stdlib HTTP, no SDK or automatic retries."""
from pathlib import Path
import argparse, base64, datetime, hashlib, json, os, sys, urllib.error, urllib.parse, urllib.request

ROOT = Path(__file__).resolve().parents[1]
MODEL = 'gpt-image-2'
BASE = 'https://api.orbiorbi.com'
DOC = 'https://orbiorbi.com/api/developer-docs/published/gpt-image-2-ee'
MINIMAL_PROMPT = 'Generate one simple solid blue square centered on a white background.'

def load_env(path=None):
    path = Path(path) if path else ROOT / '.env'
    if path.exists():
        for line in path.read_text(encoding='utf-8-sig').splitlines():
            if line.strip() and not line.lstrip().startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                os.environ.setdefault(key.strip(), value.strip().strip('\"\''))

def request(path, payload=None):
    key = os.environ.get('ORBIS_API_KEY')
    if not key:
        raise RuntimeError('Set ORBIS_API_KEY in the environment or project .env.')
    req = urllib.request.Request(BASE + path,
        data=None if payload is None else json.dumps(payload).encode('utf-8'),
        headers={'Authorization': 'Bearer ' + key, 'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=600 if payload else 120) as response:
            return json.load(response)
    except urllib.error.HTTPError as exc:
        body = exc.read().decode('utf-8', errors='replace').replace(key, '[REDACTED]')
        raise RuntimeError(f'HTTP {exc.code}: {body[:2000]}') from None
    except (TimeoutError, urllib.error.URLError):
        raise RuntimeError('Request did not complete. Check usage logs before retrying; a timeout does not establish whether it was billed.') from None

def check():
    data = request('/v1/models')
    found = any(isinstance(item, dict) and item.get('id') == MODEL for item in data.get('data', []))
    if not found:
        raise RuntimeError('Authenticated, but gpt-image-2 is missing. Use a key from GPT Image EE; no generation submitted.')
    return {'route_verified': True, 'model': MODEL}

def extension(content):
    if content.startswith(b'\x89PNG\r\n\x1a\n'): return 'png'
    if content.startswith(b'\xff\xd8\xff'): return 'jpg'
    if content[:4] == b'RIFF' and content[8:12] == b'WEBP': return 'webp'
    if content[:3] == b'GIF': return 'gif'
    return 'bin'

def save_images(result, out, stamp):
    items = result.get('data') or []
    if not items:
        raise RuntimeError('Response data contains no images; inspect saved response before retrying.')
    saved = []
    for i, item in enumerate(items):
        if item.get('b64_json'):
            content = base64.b64decode(item['b64_json'], validate=True)
            transport = 'base64'
        elif item.get('url'):
            # Separate request: never send the Orbis bearer key to an image host.
            url = item['url']
            if urllib.parse.urlparse(url).scheme not in {'https', 'http'}:
                raise RuntimeError('Unsupported image download URL scheme.')
            with urllib.request.urlopen(url, timeout=120) as response:
                content = response.read()
            transport = 'url'
        else:
            raise RuntimeError('Image object has neither b64_json nor url.')
        if not content:
            raise RuntimeError('Returned image is empty.')
        path = Path(out) / f'{stamp}-image-{i}.{extension(content)}'
        path.write_bytes(content)
        saved.append({'path': str(path.resolve()), 'bytes': len(content),
            'sha256': hashlib.sha256(content).hexdigest(), 'transport': transport})
    return saved

def generate(prompt, out):
    out = Path(out); out.mkdir(parents=True, exist_ok=True)
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    payload = {'model': MODEL, 'prompt': prompt, 'n': 1}
    (out / f'{stamp}-request.json').write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding='utf-8')
    receipt = {'model': MODEL, 'documentation': DOC, 'submitted_requests': 1,
        'timeout_seconds': 600, 'actual_charge_usd': None, 'images': []}
    try:
        result = request('/v1/images/generations', payload)
        raw_dir = ROOT / 'work' / 'orbis-responses'; raw_dir.mkdir(parents=True, exist_ok=True)
        raw_path = raw_dir / f'{stamp}.json'
        raw_path.write_text(json.dumps(result), encoding='utf-8')
        receipt['raw_response_saved_locally'] = str(raw_path)
        receipt['images'] = save_images(result, out, stamp)
        receipt['status'] = 'images_saved'
    except Exception as exc:
        receipt['status'] = 'failed_or_unconfirmed'
        receipt['error'] = str(exc)
        raise
    finally:
        (out / f'{stamp}-receipt.json').write_text(json.dumps(receipt, indent=2, ensure_ascii=False), encoding='utf-8')
    return receipt

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['check', 'minimal', 'generate'])
    parser.add_argument('--env-file')
    parser.add_argument('--prompt-file')
    parser.add_argument('--out', default=str(ROOT / 'outputs' / 'GPT Image 2 Test'))
    args = parser.parse_args(); load_env(args.env_file)
    verified = check()
    if args.command == 'check':
        print(json.dumps(verified)); return
    if args.command == 'generate' and not args.prompt_file:
        parser.error('--prompt-file is required for generate')
    prompt = MINIMAL_PROMPT if args.command == 'minimal' else Path(args.prompt_file).read_text(encoding='utf-8')
    print(json.dumps(generate(prompt, args.out), indent=2, ensure_ascii=False))

if __name__ == '__main__':
    try: main()
    except Exception as exc:
        print(str(exc), file=sys.stderr); sys.exit(1)
