# Orbis EE route diagnostic report

Project: CyberKitty2077. Credentials are intentionally excluded.

## GPT Image EE

- Model: `gpt-image-2`
- Free `GET https://api.orbiorbi.com/v1/models`: success; model present.
- Generation: `POST https://api.orbiorbi.com/v1/images/generations`
- Body: `{"model":"gpt-image-2","prompt":"Generate one simple solid blue square centered on a white background.","n":1}`
- Header: `Authorization: Bearer <route-specific key>` plus JSON Content-Type.
- Timeout:600seconds; actual failures returned in about1second.
- Six separate requests returned HTTP403, error type/code `upstream_error`.
- All six usage entries show USD0 charged; no output image returned.
- Latest request ID: `202611061655411231027158268d9d6eTU21kpv`.
- First GPT Image2 request ID: `202611061654497161162988268d9d6WqaiEp85`.

Please verify upstream route availability. Authentication/model discovery succeeds while the documented minimal generation request fails. Also confirm whether this specific EE route accepts reference images: provide the supported endpoint, exact request fields, MIME formats, size/count limits, and an example. Its documentation currently exposes only text prompt fields, and its input listing says Text despite a generic editing badge.

## Previous Nano Banana EE test

The native Gemini `generateContent` route also returned upstream403 using the documented body. Both Python urllib and the exact cURL example were tried. The model was present in the free model list.

Nano Banana request ID: `202611061645311398454408268d9d6iHpwxyhO`.

Documentation reviewed:
- https://orbiorbi.com/api/developer-docs/published/gpt-image-2-ee
- https://orbiorbi.com/api/developer-docs/published/nano-banana-2-1-line02

This report is prepared for provider support. It has not been sent to anyone.
