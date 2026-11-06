# Orbis GPT Image 2 integration

Active route: GPT Image EE, model `gpt-image-2`. This replaces Nano Banana as the selected production route. The Python implementation uses the existing standard-library HTTP stack (`urllib`), with no SDK. It checks `/v1/models`, submits the documented `model`, `prompt`, `n: 1` body to `/v1/images/generations`, saves base64 or downloaded image bytes using their actual format, and writes sanitized receipts.

The generation timeout is 600 seconds as the route document specifies. This is a maximum wait, not a delay. Image downloads allow 120 seconds and never receive the Orbis bearer key. Requests never retry automatically. After a timeout, check usage logs before resubmitting.

## Current result

Authentication and model access pass. Six minimal generation requests, including the user's five-request retry batch, each returned HTTP 403 `upstream_error`. No image was returned. The listed price is USD0.04/request; the first batch budget remains USD5. All six failed GPT Image2 requests were checked in Orbis usage logs: USD0 charged.

This route's published input fields contain no reference-image parameter or edit endpoint. Reference support is **unconfirmed**. The route UI lists Text as the only input; a generic Image editing badge does not establish an image-upload contract. The client does not invent fields or submit character images to unsupported endpoints. A provider article about the general model does not establish this EE route's input contract.

## Installed project use

The client is installed in `C:\Users\DELL\Desktop\CyberKitty 2077\Tools\orbis_gpt_image2.py`. The project-root `.env` contains credentials and is excluded by `.gitignore`. Existing environment variables take precedence. Do not publish `.env`.

From the project folder:

```powershell
python -X utf8 Tools/orbis_gpt_image2.py check
python -X utf8 Tools/orbis_gpt_image2.py minimal --out "Outputs/Orbis Tests"
python -X utf8 Tools/orbis_gpt_image2.py generate --prompt-file "path/to/prompt.txt" --out "Outputs/Generated"
```

Each `minimal` or `generate` command submits one potentially billable request after a free model check. For a downloaded client outside the installed project, pass `--env-file` with the local `.env` path or set the environment variables explicitly.

The four offline tests validate the exact endpoint/body, base64 saving, downloads without authentication headers, image signatures, invalid data and wrong-route detection. They do not establish live provider availability.

Source: https://orbiorbi.com/api/developer-docs/published/gpt-image-2-ee
