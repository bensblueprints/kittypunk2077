# KittyPunk2077 self-hosted website

Public free-account watch site and private production gallery, built for Linux/Docker. The pilot is in production; only the existing concept teaser is playable publicly. The studio contains 98 reference images, 12 opening dialogue takes and the 24-episode development plan.

Every episode targets 20:00. Later outlines are proposals, not completed scripts. The 12 voice takes cover Scenes 2–4 and total about 36.5 seconds; a complete soundtrack has not been made.

## Deployment

Copy this directory to `/opt/kittypunk2077`. Create a private `.env` containing random `SECRET_KEY`, random `ADMIN_PASSWORD`, `SITE_HOST`, and `COOKIE_SECURE=1`. Never commit or share that file. Create `data/` owned by UID 10001, then run `docker compose -p kittypunk2077 up -d --build`. Proxy HTTPS to loopback port 3460. The initial staff username is `producer`; change its password in Account after first login.

The SQLite database in `data/` is persistent. Back it up with SQLite's backup API, not by copying a live file. The container runs without root or Linux capabilities, with memory and CPU limits. Signup uses scrypt password hashes, server-side sessions, CSRF tokens and rate limits. The production image, audio and gallery routes all require a staff account. Email verification and automated password reset are not enabled; this limitation is disclosed on signup. No marketing email is sent.

## Operations

Health: `/health`. Logs: `docker compose -p kittypunk2077 logs --tail 100`. Restart: `docker compose -p kittypunk2077 restart`. Stop only this stack: `docker compose -p kittypunk2077 down` (preserves `data/`). To reset a forgotten producer password, use an administrative Python command inside this container to update the hash and revoke that account's sessions. Do not delete the database.

When a domain is purchased, update SITE_HOST and nginx, obtain its certificate, then recreate the web container. Keep the generated private access file outside this source directory and all source/asset backups.

Security implementation follows [Flask's official guidance](https://flask.palletsprojects.com/en/stable/web-security/). Functional checks cover signup, login, account deletion, password changes, staff-only assets, CSRF, filtering and video byte-range playback.
