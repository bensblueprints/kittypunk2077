"""CyberKitty ElevenLabs client using Python's standard HTTP library."""
from pathlib import Path
import base64, datetime, json, os, urllib.request, urllib.error
from orbis_gpt_image2 import load_env, ROOT
BASE='https://api.elevenlabs.io'

def api(path, payload=None):
    key=os.environ.get('ELEVENLABS_API_KEY')
    if not key: raise RuntimeError('ELEVENLABS_API_KEY is not set.')
    request=urllib.request.Request(BASE+path,data=None if payload is None else json.dumps(payload).encode('utf-8'),headers={'xi-api-key':key,'Content-Type':'application/json'})
    try:
        with urllib.request.urlopen(request,timeout=180) as response:return json.load(response)
    except urllib.error.HTTPError as exc:
        body=exc.read().decode('utf-8','replace').replace(key,'[REDACTED]')
        raise RuntimeError(f'ElevenLabs HTTP{exc.code}: {body[:1500]}') from None

def inspect():
    (ROOT/'work').mkdir(exist_ok=True)
    subscription=api('/v1/user/subscription')
    voices=api('/v2/voices?page_size=100')
    summary={k:subscription.get(k) for k in ['tier','status','character_count','character_limit','voice_slots_used','voice_limit','max_credit_limit_extension']}
    summary['remaining_included_credits']=max(0,subscription.get('character_limit',0)-subscription.get('character_count',0))
    summary['voices']=[{k:v.get(k) for k in ['voice_id','name','category','description','labels','preview_url']} for v in voices.get('voices',[])]
    summary['has_more_voices']=voices.get('has_more')
    (ROOT/'work'/'elevenlabs-account.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
    return summary

def design(role_id, description, text):
    if not 20<=len(description)<=1000:raise ValueError('Voice description must contain20–1000characters.')
    if not 100<=len(text)<=1000:raise ValueError('Preview text must contain100–1000characters.')
    # Keep auditions within included credits; never rely on account overage settings.
    subscription=api('/v1/user/subscription')
    remaining=subscription.get('character_limit',0)-subscription.get('character_count',0)
    if remaining < max(1000,len(text)*3):raise RuntimeError('Insufficient included-credit headroom for this audition; no request sent.')
    payload={'voice_description':description,'text':text,'auto_generate_text':False,'model_id':'eleven_ttv_v3','stream_previews':False}
    result=api('/v1/text-to-voice/design?output_format=mp3_44100_128',payload)
    folder=ROOT/'outputs'/'Voices'/'Auditions'/role_id;folder.mkdir(parents=True,exist_ok=True)
    records=[]
    stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    for i,preview in enumerate(result.get('previews',[]),1):
        data=base64.b64decode(preview['audio_base_64'],validate=True)
        if not data:raise RuntimeError('Empty audio preview received.')
        path=folder/f'{role_id}-option-{i}-{stamp}.mp3';path.write_bytes(data)
        records.append({'option':i,'generated_voice_id':preview.get('generated_voice_id'),'file':str(path),'media_type':preview.get('media_type'),'duration_secs':preview.get('duration_secs')})
    after=api('/v1/user/subscription')
    receipt={'role_id':role_id,'voice_description':description,'preview_text':result.get('text',text),'model_id':'eleven_ttv_v3','previews':records,'credits_before':subscription.get('character_count'),'credits_after':after.get('character_count'),'selected_voice_id':None,'status':'auditions_generated_not_selected'}
    (folder/'audition-receipt.json').write_text(json.dumps(receipt,indent=2,ensure_ascii=False),encoding='utf-8')
    return receipt

def speak(role_id, option, voice_id, text, model='eleven_multilingual_v2', settings=None):
    subscription=api('/v1/user/subscription')
    remaining=subscription.get('character_limit',0)-subscription.get('character_count',0)
    if remaining < max(1000,len(text)*3):raise RuntimeError('Insufficient included-credit headroom; no request submitted.')
    key=os.environ['ELEVENLABS_API_KEY']
    payload={'text':text,'model_id':model,'voice_settings':settings or {'stability':0.5,'similarity_boost':0.75,'style':0.15,'use_speaker_boost':True}}
    req=urllib.request.Request(BASE+f'/v1/text-to-speech/{voice_id}?output_format=mp3_44100_128',data=json.dumps(payload).encode('utf-8'),headers={'xi-api-key':key,'Content-Type':'application/json','Accept':'audio/mpeg'})
    try:
        with urllib.request.urlopen(req,timeout=180) as response:
            content=response.read();request_id=response.headers.get('request-id')
    except urllib.error.HTTPError as exc:
        body=exc.read().decode('utf-8','replace').replace(key,'[REDACTED]')
        raise RuntimeError(f'ElevenLabs HTTP{exc.code}: {body[:1500]}') from None
    if not content:raise RuntimeError('Empty speech response.')
    folder=ROOT/'outputs'/'Voices'/'Auditions'/role_id;folder.mkdir(parents=True,exist_ok=True)
    path=folder/f'{role_id}-{option}.mp3';path.write_bytes(content)
    after=api('/v1/user/subscription')
    receipt={'role_id':role_id,'option':option,'candidate_voice_id':voice_id,'text':text,'model':model,'settings':payload['voice_settings'],'file':str(path),'request_id':request_id,'credits_before':subscription.get('character_count'),'credits_after':after.get('character_count'),'status':'audition_only_not_approved'}
    (folder/f'{role_id}-{option}.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
    return receipt

if __name__=='__main__':
    load_env();result=inspect()
    print(json.dumps({k:v for k,v in result.items() if k!='voices'},indent=2))
    print(json.dumps({'voice_count_returned':len(result['voices']),'custom_voices':[{'name':v['name'],'category':v['category']} for v in result['voices'] if v['category']!='premade']},indent=2))
