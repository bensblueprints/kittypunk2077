# GPT Image 2 EE route — implementation summary

Source: https://orbiorbi.com/api/developer-docs/published/gpt-image-2-ee

Use a key issued for the GPT Image EE route. Authenticate with the Bearer header, reading ORBIS_API_KEY from the environment. Check GET /v1/models before generation and require gpt-image-2 to be present.

Submit a synchronous JSON POST to https://api.orbiorbi.com/v1/images/generations with model set to gpt-image-2, a text prompt, and n set to1. The documented timeout is600seconds. Each execution submits a potentially billable request; inspect usage logs after a timeout before trying again.

Read images from the response data array. Decode b64_json when present; otherwise download the supplied URL without forwarding the Orbis key. Save bytes promptly and identify the extension from the file signature. Reject empty results. A response JSON file alone is not a saved image.

The route-specific documentation does not define a reference-image input or edit endpoint. Support remains unconfirmed.
