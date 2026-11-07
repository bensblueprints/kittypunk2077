# CyberKitty 2077 / Kitty Punk 2077 — production inventory

This README is the production handoff for the existing Desktop reference pack. It adds an inventory and dependency order; it does not replace the original `README.txt`. Snapshot generated from files currently present on disk. A file existing is not the same as an approved asset.

Start with the [complete production checklist](production-checklist.md) and [voice audition player](Voices/listen.html).

Open the [current location gallery](<Location Sheets GPT Image 2.6/index.html>) to browse all 20 new sheets and their QA notes. The [earlier review gallery](location-review.html) remains historical. The Phase 2 table below covers newer characters, dogs, HQ, props, clean settings and opening frames.


## Current production organization

Pilot priority: **Season 1, Episode 1 — 24 scenes, exactly 20:00.** [District lore and future businesses](district-lore-and-businesses.md) records the latest user canon; future district character generation is deferred. [Current asset index](asset-index.json) distinguishes files, review status and revisions. [Next asset manifest](<Next Assets/generation-manifest.json>) covers the latest pass. [Organization audit](organization-audit.json) records cleanup and backup scope. Earlier dated snapshots below remain historical.

## Current master and status

<!-- PHASE2_LIVE_STATUS:START -->
### Phase 2 — current local snapshot

Snapshot UTC: `2026-11-06T20:15:11.492763+00:00`. Counts below come from saved local files; revisions and final approval remain governed by their receipts, QA and current manifests.

| Collection | Saved unique assets / planned | PNG versions | Status |
|---|---:|---:|---|
| [Character Masters](<Phase 2/Character Masters/>) | 6/6 | 7 | Saved review drafts; approval not inferred |
| [Dog Masters](<Phase 2/Dog Masters/>) | 5/5 | 5 | Saved review drafts; approval not inferred |
| [Goodboy HQ](<Phase 2/Goodboy HQ/>) | 10/10 | 15 | Saved review drafts; approval not inferred |
| [Props](<Phase 2/Props/>) | 12/12 | 15 | Saved review drafts; approval not inferred |
| [Setting Plates](<Phase 2/Setting Plates/>) | 4/4 | 4 | Saved review drafts; approval not inferred |
| [Opening Frames](<Phase 2/Opening Frames/>) | 28/28 | 34 | Saved review drafts; approval not inferred |

Character Masters contains **six identities total: five cats plus Barkington**, with historical versions kept separately. Barkington v002 is the current cape-corrected reference. The five new Dog Masters are **Viper, Frost, Stone, Velvet and Domino**. Fetch and Muzzle already had usable multiview sheets; see the [dog audit](<Phase 2/dog-sheet-audit.md>).

The named dog library is **Barkington plus seven others: Fetch, Muzzle, Viper, Frost, Stone, Velvet, Domino**. It is an expanded supporting/future library. This does not assign which four are Barkington’s initial cronies. The hero crew remains exactly **Trixie / CatGirl (female, 19), Byte, Ghost, Onyx and Neon (four boys, ages 15–19)**.

HQ and prop revisions are distinct versions, not new asset types. The four clean setting plates and 28 planned opening frames are still production reference work; saved frames are not animated or finished scenes. Resolve per-file continuity notes and final review before promotion.

**Provider policy:** Higgsfield is for still images only. Never use Higgsfield for speech, other audio or video. All character/narrator/radio voice generation uses the user’s ElevenLabs account only. This documentation update authorizes no new generation.

**Voices:** 22 distinct ElevenLabs review recordings: seven auditions, two requested-line versions, one narrator trial and 12 exact Scene 02–04 dialogue takes. [Listen to all review recordings](Voices/listen.html) or [the opening dialogue](<Voices/Opening Scenes/listen.html>). The 12 takes total 36.502 seconds and 629 text characters, with provider timings and receipts. Their settled cost was 139 included credits; the saved 29,711 remaining balance is a historical check, not a live balance. No take is final-approved.

Current company canon is **Goodboy Global**. Preserve historical sources, old recordings and exact transcripts. Current selected voices are Trixie/Emma, Byte/Northern Terry, Ghost/Austin—Upbeat, Neon/Ryan, Onyx/Harry, NIP7/Daniel, Barkington/Brian and WOOF7/Eric. Countdown Casey is the separate recurring radio host; narrator Austin remains a trial. Jerry B. is selected for Guard A and Hugo for Guard B; see the [supporting cast selections](Voices/supporting-cast-selections.md). New selections are not auditioned recordings.

Current Phase 2 completion, spending and external synchronization must be read from current receipts. Earlier location-only sync totals do not establish that these new files have been uploaded.
<!-- PHASE2_LIVE_STATUS:END -->

- **Location generation complete:** All **20 Higgsfield GPT Image 2.6** reference-guided sheets are saved at verified **3840 × 2160**, High / 4K / 16:9, generated one at a time. **All remain review drafts; final production approval is pending.** Browse the [new gallery](<Location Sheets GPT Image 2.6/index.html>), [QA report](<Location Sheets GPT Image 2.6/QA-notes.md>) and [generation manifest](<Location Sheets GPT Image 2.6/generation-manifest.json>). The 19-image remaining batch was authorized up to 81 credits; receipts quote 80.75 credits, not independently verified final billing. **Never use Higgsfield for videos.**

- **Pilot master:** Season 1 Episode 1, **The Great Salmon Shortage**, 24 scenes, exactly **20:00 / 1,200 seconds**. Use the [working script with Trixie](pilot-working-24-scenes-trixie.txt); the [original supplied master](pilot-master-24-scenes.txt) is retained. See also [machine-readable scene index](pilot-24-scene-index.json).
- **Earlier 18-scene draft is superseded.** `work/pilot.json`, its shot IDs and `work/pilot_voice_lines.json` are legacy development material. Do not generate from them or merge their scene numbering into this master.
- **Locations:** **20/20 current sheets generated**, zero queued or missing, zero final production approvals. The **16 earlier drafts remain preserved** separately, giving 36 PNG versions across the two collections. The original prompt export and ZIP remain unchanged as provenance. Use [current location registry](location-registry.json) and [generation progress](location-generation-progress.json).
- **Earlier combined Trixie crew sheet:** [TRIXIE / AKA CATGIRL crew sheet](Characters/Trixie/trixie-catgirl-crew-character-sheet-v001.png) revised with the user-approved built-in image editor, native1536x1024. All five identities visually checked; original preserved. Prompt/result metadata sits beside the image.
- **Characters:** 21 registry entries, including a crowd ensemble and later-season proposals. See [character prompts](character-prompts.json). No entry is declared fully production-approved merely because an old reference exists.
- **Story expansion:** [three-season proposed bible](story-bible-proposed.json) has 24 episode outlines. Later-season arcs and backstories are PROPOSED. Its Episode 1 development title/summary does not override the new 24-scene master.
- **Recovered references:** 31 nonblank originals were copied into `Recovered References`; the recovery manifest records hashes. Exclude known black/corrupt active references when generating.
- **Historical Orbis test:** the failed route was **GPT Image EE / `gpt-image-2`**. Free model check passed. Six exact minimal generation requests returned HTTP 403 `upstream_error`; no Orbis image was returned. All six show USD0 charged in provider usage logs. Earlier Nano Banana attempts also failed upstream. The new client uses Python `urllib`, saves base64/URL images, allows 600 seconds and does not auto-retry. Four offline checks pass. Listed rate: **$0.04/request**, total test budget: **$5**. Reference-image input is not documented for this route and remains unconfirmed. See [integration and evidence](Integration/README.md).
- **Hugging Face:** [bensblueprints/cyberkitty-2077-assets](https://huggingface.co/datasets/bensblueprints/cyberkitty-2077-assets) remains **private**. The historical completed location snapshot has **514 asset/document paths verified against local hashes**, including all 20 new 4K PNGs. Desktop Production Pack v01 has **291 files verified**, excluding its own sync receipt. See [HF receipt](hf-sync.json) and [Desktop receipt](local-sync.json); private links require authorized sign-in.
- **Historical location-only Boardly snapshot:** board **133**, production list **633** contained **26 cards**, including all 20 locations and production dependencies. Six full project files were saved; refreshed versions include the latest route and sync status. Location approvals remain open. See [sync receipt](boardly-sync.json).
- No API keys, tokens or authorization headers belong in this package.

## Production order — all locations first

1. All 20 location sheets are saved; reconcile remaining geometry/QA and use the current clean plates. Later user authorization permits Phase 2 opening stills; final location and scene approvals remain separate.
2. Lock character identity masters, standing turnarounds, costumes, expressions, paws and recurring props. Repair or reject contradictory/black references.
3. Use the eight confirmed role voices and review the 12 exact opening takes; complete remaining **ElevenLabs** casting and dialogue from the **24-scene** master. Crew voice direction: youthful **15–19**; NIP7 presenter: **British**; corporate dogs: **older**. Voice IDs and reusable settings must be recorded.
4. Build scene stills/storyboard panels using approved empty sets, characters and props; record blocking, eyelines, screen direction and exact wardrobe.
5. Build an animatic with approved dialogue and scene timings; then use a separately selected video route, edit, composite exact graphics, mix audio and verify the final 20:00 cut. **Never use Higgsfield for videos.**
6. Archive approved versions and synchronize the manifest, private dataset and Boardly only after their respective operations succeed.

## Canon and layout rules

- The five heroes are **Trixie (aka CatGirl), Byte, Ghost, Onyx, Neon**. Trixie is the girl leader; the other four are boys. The old name Catman remains only in historical sources and paths; “Bite” is a transcript alias. No dogs substitute for crew members.
- Canonical couch rear view, screen left to right: **Neon / Onyx / Trixie / Byte / Ghost**. Preserve the uploaded rusty CRT, its **two knobs on the right**, the dusty console **above the TV**, patched brown couch, **banner left of TV**, **window right of TV**. Keep the CRT blank in source plates and composite content later.
- **7-Catleven** is the latest script/storefront spelling. The game title appears as **Grand Theft Kitty VI** in the master and “6” in some art; approve one graphic treatment without changing the story. Console naming likewise varies CatStation 5 / Cat Station 5; match the approved prop art.
- **Goodboy Global** is the user-confirmed company name for active story text and all new artwork. The working pilot is normalized; the original master, historical audio/transcripts and image-generation metadata remain preserved.
- **WOOF7** is the dog network and **NIP7** the independent cat outlet. Imported broadcast graphics with another channel name must be checked before reuse.
- Barkington is the approved black-and-tan **Doberman**, with canine paws; Muzzle is a **Husky with lit cybernetic muzzle and uncovered eyes**, never a cat, wolf, or glasses-only replacement.
- Photographing cash proves an undisclosed payment, not the salmon conspiracy. The routing records/physical stock later establish diversion. Preserve refrigeration while stopping discriminatory dispatch.
- Districts deprived: **7–12**. Districts receiving preferential shipments: **1–6**.
- Every room has one fixed floor plan. Door positions, windows, desk and couch orientation, screen side, props, lighting and connecting corridors persist across angles. Unseen angles in new sheets are proposed completion, not recovered historical facts.
- Extract the relevant subject/panel from multi-panel references for later work; do not let a model paint an entire reference grid inside the scene. Generic external image links in the master are illustrative, not identity authorities.
- News text, maps, receipts, prices, logos and newspaper body copy are separate exact graphics. Composite them into blank screens/signs instead of relying on tiny generated text.

## Pilot — 24-scene timeline

| Scene | Title | Time | Seconds | Location IDs |
| --- | --- | --- | --- | --- |
| 01 | Just One More Mission | 00:00–01:10 | 70 | LOC01, LOC02, LOC19 |
| 02 | The Interruption | 01:10–02:00 | 50 | LOC02, LOC13 |
| 03 | Barkington's Emergency Broadcast | 02:00–03:05 | 65 | LOC02, LOC13 |
| 04 | The Trip to 7-Catleven | 03:05–04:00 | 55 | LOC01, LOC05, LOC06 |
| 05 | Three Times the Price | 04:00–05:00 | 60 | LOC07 |
| 06 | Word Spreads | 05:00–05:45 | 45 | LOC08 |
| 07 | The District 7 Rally | 05:45–06:50 | 65 | LOC09 |
| 08 | The Cats Are Waking Up | 06:50–07:30 | 40 | LOC05 |
| 09 | Follow the Money | 07:30–08:40 | 70 | LOC03 |
| 10 | Operation Bonehead | 08:40–09:45 | 65 | LOC04 |
| 11 | Steak & Bone Surveillance | 09:45–11:00 | 75 | LOC10 |
| 12 | The Bone Distraction | 11:00–11:45 | 45 | LOC10 |
| 13 | Inside the Restaurant | 11:45–12:35 | 50 | LOC11 |
| 14 | The Secret Dinner | 12:35–13:35 | 60 | LOC12 |
| 15 | The Payoff Photograph | 13:35–14:20 | 45 | LOC12 |
| 16 | Get the Hell Out | 14:20–15:10 | 50 | LOC10, LOC11 |
| 17 | The Leak | 15:10–16:00 | 50 | LOC03, LOC14, LOC18 |
| 18 | Victory? Not Quite | 16:00–16:35 | 35 | LOC05, LOC08 |
| 19 | Follow the Fish | 16:35–17:10 | 35 | LOC03 |
| 20 | Salmon Headquarters | 17:10–17:45 | 35 | LOC15 |
| 21 | The Great Salmon Heist | 17:45–18:30 | 45 | LOC16, LOC17 |
| 22 | Shut It Down | 18:30–19:05 | 35 | LOC15, LOC17 |
| 23 | Salmon for Everyone | 19:05–19:30 | 25 | LOC08, LOC14, LOC20 |
| 24 | Back to the Game | 19:30–20:00 | 30 | LOC02, LOC19 |

Acts: 1 = 00:00–05:00; 2 = 05:00–11:00; 3 = 11:00–16:00; 4 = 16:00–20:00. The master reserves no separate credit duration beyond 20:00; resolve credit placement in the animatic without silently extending runtime.

## Location registry — every room and area

Each LOC entry is one reference sheet covering its listed set. Interior sheets require hero wide, four walls, ceiling/floor, fixed props, overhead plan and reverse wide. Exteriors use four directional coverages, roof/sky and ground details. All sets are empty of characters. A sheet is not a substitute for full-resolution individual shooting plates.

| ID | Set / rooms | Scenes | Sheet file | Current status |
| --- | --- | --- | --- | --- |
| LOC01 | Resistance warehouse exterior — South cargo entrance and staff door; North service wall; East workshop side; West window side; Loading apron and roof | 1, 4 | Location Sheets GPT Image 2.6/LOC01-resistance-warehouse-exterior-gpt26-v001.png | generated_review_required; QA recorded |
| LOC02 | Resistance warehouse lounge — TV wall; Couch and console area; Window side; Entry passage; Reverse wall | 1, 2, 3, 24 | Location Sheets GPT Image 2.6/LOC02-resistance-warehouse-lounge-gpt26-v001.png | generated_review_required; QA recorded |
| LOC03 | Hacking operations — Five-position operations desk; Server rack ends; Central worktable; Open warehouse access | 9, 17, 19 | Location Sheets GPT Image 2.6/LOC03-hacking-operations-gpt26-v001.png | generated_review_required; QA recorded |
| LOC04 | Engineering workshop — Workbench; Parts storage; Equipment locker; Operations passage | 10 | Location Sheets GPT Image 2.6/LOC04-engineering-workshop-gpt26-v001.png | generated_review_required; QA recorded |
| LOC05 | District 7 streets and alleys — Main pedestrian street; East side alley; Shopfronts; Utility/fire-escape edge | 4, 8, 18 | Location Sheets GPT Image 2.6/LOC05-district-7-streets-and-alleys-gpt26-v001.png | generated_review_required; QA recorded |
| LOC06 | 7-Catleven exterior — South storefront; Side alley; Rear service wall; Sidewalk and entry | 4 | Location Sheets GPT Image 2.6/LOC06-7-catleven-exterior-gpt26-v001.png | generated_review_required; QA recorded |
| LOC07 | 7-Catleven interior and freezer — West freezer bank; East cashier counter; Two snack aisles; Rear service door; South entry | 5 | Location Sheets GPT Image 2.6/LOC07-7-catleven-interior-and-freezer-gpt26-v001.png | generated_review_required; QA recorded |
| LOC08 | District 7 market — Market square; Fish stalls; Public billboard; Truck delivery stopping area | 6, 18, 23 | Location Sheets GPT Image 2.6/LOC08-district-7-market-gpt26-v001.png | generated_review_required; QA recorded |
| LOC09 | District 7 rally stage and plaza — Temporary raised stage; Crowd plaza; Access lanes; Projection backdrop | 7 | Location Sheets GPT Image 2.6/LOC09-district-7-rally-stage-and-plaza-gpt26-v001.png | generated_review_required; QA recorded |
| LOC10 | Steak & Bone exterior and security — Main entrance; Guard positions; Service entry; Service alley; Restaurant surveillance roof | 11, 12, 16 | Location Sheets GPT Image 2.6/LOC10-steak-bone-exterior-and-security-gpt26-v001.png | generated_review_required; QA recorded |
| LOC11 | Steak & Bone service corridors — Service entry corridor; Dining access turn; Robot patrol route; Service exit | 13, 16 | Location Sheets GPT Image 2.6/LOC11-steak-bone-service-corridors-gpt26-v001.png | generated_review_required; QA recorded |
| LOC12 | Steak & Bone private dining room — Private dining table; Window/view wall; Service door; Hidden surveillance angle | 14, 15 | Location Sheets GPT Image 2.6/LOC12-steak-bone-private-dining-room-gpt26-v001.png | generated_review_required; QA recorded |
| LOC13 | WOOF7 news studio — Anchor desk; Broadcast backdrop; Camera lane; Control/screen graphics area | 2, 3 | Location Sheets GPT Image 2.6/LOC13-woof7-news-studio-gpt26-v001.png | generated_review_required; QA recorded |
| LOC14 | NIP7 investigative newsroom — Presenter desk; Evidence display; Newsroom backdrop; Camera lane | 17, 23 | Location Sheets GPT Image 2.6/LOC14-nip7-investigative-newsroom-gpt26-v001.png | generated_review_required; QA recorded |
| LOC15 | Salmon facility exterior and loading — Guarded vehicle gate; Four loading bays; Staff/service door; Cold utility enclosure; Loading yard | 20, 22 | Location Sheets GPT Image 2.6/LOC15-salmon-facility-exterior-and-loading-gpt26-v001.png | generated_review_required; QA recorded |
| LOC16 | Salmon cold store and processing hall — Processing conveyors; Cold A and Cold B rooms; Mezzanine access stair; West wash/mechanical wall; Loading shutter | 21 | Location Sheets GPT Image 2.6/LOC16-salmon-cold-store-and-processing-hall-gpt26-v001.png | generated_review_required; QA recorded |
| LOC17 | Salmon routing control room — East mezzanine control room; West observation glass; Routing desks; Server rack wall; Separate cooling control | 21, 22 | Location Sheets GPT Image 2.6/LOC17-salmon-routing-control-room-gpt26-v001.png | generated_review_required; QA recorded |
| LOC18 | Catnip Times pressroom — Editorial desk; Rotary press; Paper/ink storage; Freight loading door | 17 | Location Sheets GPT Image 2.6/LOC18-catnip-times-pressroom-gpt26-v001.png | generated_review_required; QA recorded |
| LOC19 | Game world: Great Dog National Bank — Bank facade and steps; Game street/plaza; Opposite storefront; Open east/west street exits | 1, 24 | Location Sheets GPT Image 2.6/LOC19-game-world-great-dog-national-bank-gpt26-v001.png | generated_review_required; QA recorded |
| LOC20 | District 7 market rooftop overlook — Low roof above market; North market parapet; Southwest access hut; HVAC and rail edges | 23 | Location Sheets GPT Image 2.6/LOC20-district-7-market-rooftop-overlook-gpt26-v001.png | generated_review_required; QA recorded |

### Location props and physical continuity

| Set | Required fixed/hero props |
| --- | --- |
| LOC01 | cargo shutter, staff door, utility meters, crate stack, drain, resistance stencil |
| LOC02 | rusty CRT with two right knobs, CatStation 5 above CRT, five-seat patched couch, five controllers, blankets, snack bowl, cans, District 7 crew banner, media cases |
| LOC03 | five blank monitors, five chairs, server racks, HackPad, data drive, cable trays, evidence uploads, routing map |
| LOC04 | bone decoys, remote control, drone, 3D printer, solder tools, robot bench arm, tool rig, parts bins |
| LOC05 | street lamps, graffiti, signs, utility box, posters, banners, newspaper stand |
| LOC06 | 7-Catleven lightbox, green/orange/red fascia, sliding glass doors, District 7 pole sign, pink cat neon |
| LOC07 | exactly two salmon packs, blank notice panel, price labels, handheld scanner, receipt, register, shop cap/apron |
| LOC08 | closed/open fish stalls, crate podium, price-history display, refrigerated truck, salmon cartons, vendor scales |
| LOC09 | microphone, stand, PA speakers, projector, price chart, banners, stage crates, cables |
| LOC10 | Steak & Bone sign, valet frontage, limousine, CCTV, guard radio, bone decoys, alarm lamp, surveillance camera |
| LOC11 | security camera, service robot, push-bar door, access reader, tray cart, alarm light |
| LOC12 | two dining chairs, table setting, wine glasses, cash bag, banknotes, Barkington ring, recorder, camera |
| LOC13 | blank display wall, news desk, studio camera, teleprompter, broadcast lectern or seated source composition, WOOF7 ident |
| LOC14 | blank evidence screen, news desk, microphone, camera, teleprompter, NIP7 ident |
| LOC15 | refrigerated trucks, sealed salmon crates, CCTV, guard booth, bollards, D1-6 and D7-12 destination overlays, fish neon |
| LOC16 | salmon stockpile, insulated doors, sealed crates, pallet jack, conveyors, parked robot arms, refrigeration gauges, blue cooling pipes |
| LOC17 | routing screen, shipping manifests, data drive, dispatch-stop control, independent refrigeration indicator, two chairs, keyboards |
| LOC18 | blank newspaper template, paper rolls, press rollers, bundled papers, ink tins, trolley, pinboards |
| LOC19 | bank wordmark, dog medallion, game money bag, getaway car, game HUD layers, bank doors |
| LOC20 | railing, roof drain, utility box, crate, tarpaulin, HVAC units, predawn market view |

### Required completion for every location

- Nine-panel location sheet: hero wide, north/south/east/west coverage, overhead plan with camera markers, ceiling/floor, fixed props/materials, reverse wide.
- Separate clean full-resolution 16:9 hero and reverse plates, without grid labels.
- Four separate wall/directional coverage plates.
- Annotated overhead layout with fixed door/window/prop coordinates and screen axis.
- Lighting/material palette and day/night variants only when script needs them.
- Blank screens and signage areas plus separate exact typography overlays.
- QC record, source references, prompt, model/version, dimensions and file hash.

**Current QA:** All 20 new images are verified at 3840 × 2160. Detailed findings and recommendations are in the [QA report](<Location Sheets GPT Image 2.6/QA-notes.md>). Initial review is complete; corrections, clean plates and final location approvals remain open. Older 1672 × 941 drafts are preserved as historical versions.

### Per-sheet QA queue

All rows refer to the new GPT Image 2.6 sheets. Full findings are preserved in QA-notes.json.

| Sheet | Initial QA / required next step |
| --- | --- |
| LOC01 | Keep as review draft; annotation and state clarification are sufficient. No full rerender or extra generation retry recommended. |
| LOC02 | Useful improved hero/TV reference, still a review draft for reverse coverage. Preserve this result; no extra generation retry requested under the current batch budget. |
| LOC03 | Strong usable operations design. Main counts and anchors pass; plan-camera and reverse-label corrections remain. No regeneration retry requested. |
| LOC04 | Usable workshop design reference. Preserve the successful fixed equipment layout. No regeneration retry requested. |
| LOC05 | Useful empty District7 street design and textures. Alley/store corner and camera annotations remain drafts. No regeneration retry requested. |
| LOC06 | Usable exterior design with strong repeated facade identity. Resolve cross-set street mapping as an annotation, without an automatic image retry. |
| LOC07 | Usable and clear store interior reference. Essential two-pack shortage story content is present. Correct camera annotation and lock small prop/window details when making scene plates; no retry requested. |
| LOC08 | Strong usable hero, reverse, plan and material references; preserve this market identity. Directional east coverage remains draft and south label needs correction. No automatic retry requested. |
| LOC09 | Usable rally stage design and plaza hero. Rooftop and market-connection coverage are drafts, not geographically verified scene plates. No regeneration retry requested. |
| LOC10 | Strong usable restaurant exterior and security fixture reference; rooftop surveillance geography remains draft. Preserve successful facade and material design. No regeneration retry requested. |
| LOC11 | Retain material and prop design; rebuild hero and reverse from the L-shaped plan and lock all door/alcove positions before camera blocking. |
| LOC12 | Keep the strong luxury material design; lock southwest service door and table/booth axis consistently across plan, south elevation and wides before shooting. |
| LOC13 | Strong studio design; resolve south exit location, then verify west newsroom-door position against the plan at production blocking stage. |
| LOC14 | Keep design and desk arrangement. Align the single exit wall/corner across plan, SOUTH and reverse before scene blocking. |
| LOC15 | Retain industrial design and dock assignment; correct booth side and plan/view labels before production blocking. |
| LOC16 | Stockpile reveal is successful. Lock personnel door and arm positions, correct A arrow, and choose whether reverse remains a south-facing architecture plate. |
| LOC17 | Keep functional control design and cooling/dispatch separation. Reconcile southwest door and northeast shelf across all views before filming. |
| LOC18 | Core pressroom geography is useful. Correct cupboard and trolley sides; use a clean newspaper overlay for close-up inserts. |
| LOC19 | Useful coherent empty game set. Correct B position/arrow and swap north/south captions before treating plan as camera guide. |
| LOC20 | Use plan as provisional roof master, rebuild the named elevations and hero/reverse from it, and explicitly match the same LOC08 stall/billboard/stair geometry before scene 23. |

## Character inventory — all 21 entries

P0 = pilot dependency; P1 = later-season/council development. Existing reference means a design source exists, not that all view deliverables are ready. The crowd row is six proposed repeatable civilians, not one individual. Keep every one separately identifiable.

| Asset ID | Priority | Character / species | Identity and role | Source/design status |
| --- | --- | --- | --- | --- |
| CHAR_TRIXIE | P0 | Trixie / White long-haired cat | White long-haired cat; Blue; Black circuit/scar motif with small pink points on cheek; lock its side from face reference, do not mirror. Pink nose.; Black cyber jacket with pink neon cat patch; cyan/magenta accents. Dossier hood and goggles treated as wardrobe state. Role: Master hacker / infiltrator | Established identity from supplied artwork; prompt repairs only. |
| CHAR_BYTE | P0 | Byte / Orange tabby cat | Orange tabby cat; Round black sunglasses, white muzzle, orange tabby striping; Orange-and-black tech jacket; gold/orange paw-print headphones around neck; tac boots Role: Analyst / planner | Established identity from supplied artwork; prompt repairs only. |
| CHAR_GHOST | P0 | Ghost / Grey tabby cat | Grey tabby cat; Green AR visor, dark hood, pale muzzle and striped tail; Dark stealth suit with green light accents Role: Stealth / recon | Established identity from supplied artwork; prompt repairs only. |
| CHAR_ONYX | P0 | Onyx / Black cat | Black cat; Yellow-gold; Black fur and magenta paw headphones; Hooded black protective outfit and magenta accents Role: Security / protection | Established identity from supplied artwork; prompt repairs only. |
| CHAR_NEON | P0 | Neon / Grey tabby cat | Grey tabby cat; Blue/cyan visor, patterned blue scarf, white muzzle, striped tail; Blue-accented engineer equipment and tool rig Role: Engineer / gear specialist | Established identity from supplied artwork; prompt repairs only. |
| CHAR_CHAIRMAN_BARKINGTON | P0 | Chairman Barkington / Doberman Pinscher | Doberman Pinscher; Black-and-tan, upright ears, long canine muzzle, purple reflective sunglasses; Black gold-trim suit, deep red tie, grey fur collar, black cape with red lining, gold watch/ring; cigar scene-dependent Role: Chairman / CEO / Supreme Leader | Established identity from supplied artwork; prompt repairs only. |
| CHAR_GENERAL_FETCH | P1 | General Fetch / Rottweiler | Rottweiler; Black-and-tan, broad square muzzle, folded ears, visible cheek scar; Black tactical armor with gold trim, Goodboy shoulder crest, utility belt, combat boots Role: Head of security / enforcement | Established identity from supplied artwork; prompt repairs only. |
| CHAR_DR_MUZZLE | P1 | Dr Muzzle / Siberian Husky | Siberian Husky; Bright blue, visible without glasses; Black/grey-and-white fur, upright ears, permanent custom cyberpunk muzzle covering lower snout with cyan vents and magenta circular modules; White lab coat with gold trim, dark underlayer, cyan equipment accents Role: R&D / implant program | Established identity from supplied artwork; prompt repairs only. |
| CHAR_VIPER | P1 | Viper / German Shepherd | German Shepherd; Tan and black coat, upright ears, long muzzle; Black corporate uniform/coat with gold trim Role: Operations / supply chain | Established identity from supplied artwork; prompt repairs only. |
| CHAR_FROST | P1 | Frost / American Pit Bull | American Pit Bull; Grey coat, broad muzzle, short ears; Dark gold-trim suit and white shirt with dark tie Role: Intelligence / surveillance | Established identity from supplied artwork; prompt repairs only. |
| CHAR_STONE | P1 | Stone / English Bulldog | English Bulldog; Stocky, wrinkled tan-and-white face, folded ears, heavy jowls; Dark gold-trim suit, white shirt and gold tie Role: Finance / resources | Established identity from supplied artwork; prompt repairs only. |
| CHAR_VELVET | P1 | Velvet / Afghan Hound | Afghan Hound; Long silky golden coat, narrow muzzle, dark sunglasses; Black gold-trim corporate suit; group scene shows red tie/accent Role: Public relations / media | Established identity from supplied artwork; prompt repairs only. |
| CHAR_DOMINO | P1 | Domino / Dalmatian | Dalmatian; White coat with distinct black spots; floppy ears; Black gold-trim corporate/military suit Role: Enforcement / special ops | Established identity from supplied artwork; prompt repairs only. |
| CHAR_WOOF7_ANCHOR | P0 | WOOF7 Anchor / Shiba Inu dog | Orange-tan Shiba Inu with cream muzzle/cheeks and upright ears; rectangular black eyeglasses; dark pinstripe suit, white shirt, deep red tie, small gold paw lapel pin. Match the left seated Shiba in restaurant reference, not the right Doberman or inset altered Shiba. Canine paws. Role: Corporate TV anchor | Existing supporting character visible in imported scene; unseen full-body details are proposed. |
| CHAR_NIP7_ANCHOR | P0 | NIP7 Anchor / Hairless Sphynx cat | Pink hairless Sphynx with prominent forehead wrinkles, very large upright ears, gold/olive eyes as depicted, black rectangular eyeglasses and coiled earpiece; navy pinstripe suit, white shirt, burgundy tie and small paw pin. Match the main newscaster only, never the dogs in the inset. Role: Independent investigative newscaster | Existing supporting character visible in imported scene; unseen full-body details are proposed. |
| CHAR_SEVEN_CATLEVEN_CLERK | P0 | Seven Catleven Clerk / Tabby-and-white cat | Small tabby-and-white shop cat with white muzzle/chest, dark striped forehead, black shop cap, orange collar/shirt and dark green apron. Match cashier behind counter in store image; do not borrow the five crew costumes. Paw hands. Role: Neighbourhood shop clerk | Existing supporting character visible in imported scene; unseen full-body details are proposed. |
| CHAR_DOG_GUARD_A | P0 | Dog Guard A / Rottweiler dog | Proposed recurring guard based on the restaurant security extras: sturdy black-and-tan Rottweiler, broad muzzle, folded ears, black sunglasses, plain black suit, white shirt and black tie; coiled earpiece, canine paw hands. Give a subtle silver rectangular badge on wearer-left lapel. No gold command armor or red captain tie. Role: Recurring security guard | Proposed separate identity derived from visible generic security extras; not General Fetch. |
| CHAR_DOG_GUARD_B | P0 | Dog Guard B / Rottweiler dog | Proposed second recurring guard based on restaurant extras: leaner black-and-tan Rottweiler, narrower muzzle than Guard A, folded ears, black sunglasses, plain black suit and narrow black tie; coiled earpiece, canine paw hands. Small silver circular badge on wearer-left lapel. Keep separate face and build from Guard A and General Fetch. Role: Recurring security guard | Proposed separate identity derived from visible generic security extras; not General Fetch. |
| CHAR_CAT_CIVILIAN_CROWD | P0 | Cat Civilian Crowd / Cats only | Proposed District7 civilian ensemble: exactly six distinct adult cats, one cream shorthair, one brown mackerel tabby, one calico, one grey shorthair, one ginger-and-white cat, one black-and-white tuxedo. Modest repaired everyday jackets and work clothes; individually consistent stripe/patch maps. No crew signature visors, magenta headphones or branded hacker jackets. All upright anthropomorphic cats with feline paws and tails. Role: District7 citizens | Proposed reusable background cast; sheet is style reference only, not identity reference. |
| CHAR_HUMAN_AI_AVATAR | P1 | Human AI Avatar / Nonphysical human-created AI | Proposed representation: a clean cyan-white vertical circular interface ring made of seven evenly spaced small segments, centred on a dark screen, tiny warm amber central light, no animal face or body. Projected glyphs remain abstract; its repeated design is identical in every screen shot. Role: Later-season system antagonist | Proposed visual design; reference sets screen/material palette only. Not yet canon. |
| CHAR_RETURNING_HUMAN_COMMANDER | P1 | Returning Human Commander / Human | Proposed adult human mission commander around50, practical unglamorous silver-grey short hair, weathered face, dark slate pressure suit with ivory shoulder panels, plain rectangular mission patch and scuffed boots. Neutral presentation, no weapon in reference master, no recognizable actor likeness. Human hands, not paws. Keep helmet separate, fully visible face. Role: Season3 final-cliffhanger returning human | Proposed character design; existing city reference sets world lighting/material realism only. No established human portrait exists. |

### Canonical character sources

| Asset ID | Reference files and authority |
| --- | --- |
| CHAR_TRIXIE | C:\Users\DELL\Desktop\CyberKitty 2077\Assets\Characters\Catman\Reference Images\ref-headshot.png — Clean face identity reference; low-resolution derivative, do not infer new microdetail.; C:\Users\DELL\Desktop\CyberKitty 2077\Assets\Character Sheets\kitty-punk-2077-character-sheets.png — Identity/outfit authority: select only the panel labelled CATMAN when this is a group sheet. |
| CHAR_BYTE | C:\Users\DELL\Desktop\CyberKitty 2077\Assets\Characters\Byte\Reference Images\ref-headshot.png — Clean face identity reference; low-resolution derivative, do not infer new microdetail.; C:\Users\DELL\Desktop\CyberKitty 2077\Assets\Character Sheets\kitty-punk-2077-character-dossiers.png — Identity/outfit authority: select only the panel labelled BYTE when this is a group sheet. |
| CHAR_GHOST | C:\Users\DELL\Desktop\CyberKitty 2077\Assets\Characters\Ghost\Reference Images\ref-headshot.png — Clean face identity reference; low-resolution derivative, do not infer new microdetail.; C:\Users\DELL\Desktop\CyberKitty 2077\Assets\Character Sheets\kitty-punk-2077-character-dossiers.png — Identity/outfit authority: select only the panel labelled GHOST when this is a group sheet. |
| CHAR_ONYX | E:\MovedFromC\Documents\Codex\2026-11-06\https-chatgpt-com-share-6aedf171-aae8-2\outputs\Recovered References\Onyx\portrait.png — Recovered intact portrait, face/wardrobe reference. Ignore sheet labels and borders.; C:\Users\DELL\Desktop\CyberKitty 2077\Assets\Character Sheets\kitty-punk-2077-character-dossiers.png — Identity/outfit authority: select only the panel labelled ONYX when this is a group sheet. |
| CHAR_NEON | E:\MovedFromC\Documents\Codex\2026-11-06\https-chatgpt-com-share-6aedf171-aae8-2\outputs\Recovered References\Neon\portrait.png — Recovered intact portrait, face/wardrobe reference. Ignore sheet labels and borders.; C:\Users\DELL\Desktop\CyberKitty 2077\Assets\Character Sheets\kitty-punk-2077-character-dossiers.png — Identity/outfit authority: select only the panel labelled NEON when this is a group sheet. |
| CHAR_CHAIRMAN_BARKINGTON | C:\Users\DELL\Desktop\CyberKitty 2077\Assets\Character Sheets\character-sheet-01-chairman-barkington.png — Identity/outfit authority: select only the panel labelled CHAIRMAN BARKINGTON when this is a group sheet. |
| CHAR_GENERAL_FETCH | C:\Users\DELL\Desktop\CyberKitty 2077\Assets\Character Sheets\character-sheet-02-general-fetch.png — Identity/outfit authority: select only the panel labelled GENERAL FETCH when this is a group sheet. |
| CHAR_DR_MUZZLE | E:\MovedFromC\Documents\Codex\2026-11-06\https-chatgpt-com-share-6aedf171-aae8-2\outputs\Recovered References\Dr Muzzle\portrait.png — Recovered intact portrait, face/wardrobe reference. Ignore sheet labels and borders.; C:\Users\DELL\Desktop\CyberKitty 2077\Assets\Character Sheets\character-sheet-03-dr-muzzle.png — Identity/outfit authority: select only the panel labelled DR MUZZLE when this is a group sheet. |
| CHAR_VIPER | C:\Users\DELL\Desktop\CyberKitty 2077\Assets\Character Sheets\The Dogs\file_00000000ffc081f59db0af84291190f4.webp — Identity/outfit authority: select only the panel labelled VIPER when this is a group sheet. |
| CHAR_FROST | C:\Users\DELL\Desktop\CyberKitty 2077\Assets\Character Sheets\The Dogs\file_00000000ffc081f59db0af84291190f4.webp — Identity/outfit authority: select only the panel labelled FROST when this is a group sheet. |
| CHAR_STONE | C:\Users\DELL\Desktop\CyberKitty 2077\Assets\Character Sheets\The Dogs\file_00000000ffc081f59db0af84291190f4.webp — Identity/outfit authority: select only the panel labelled STONE when this is a group sheet. |
| CHAR_VELVET | C:\Users\DELL\Desktop\CyberKitty 2077\Assets\Character Sheets\The Dogs\file_00000000ffc081f59db0af84291190f4.webp — Identity/outfit authority: select only the panel labelled VELVET when this is a group sheet. |
| CHAR_DOMINO | C:\Users\DELL\Desktop\CyberKitty 2077\Assets\Character Sheets\The Dogs\file_00000000ffc081f59db0af84291190f4.webp — Identity/outfit authority: select only the panel labelled DOMINO when this is a group sheet. |
| CHAR_WOOF7_ANCHOR | E:\MovedFromC\Documents\Codex\2026-11-06\https-chatgpt-com-share-6aedf171-aae8-2\outputs\Imported References\steak-and-bone-meeting.png — Visual authority for the specified subject only; do not copy other characters, text, background or inset pictures. |
| CHAR_NIP7_ANCHOR | E:\MovedFromC\Documents\Codex\2026-11-06\https-chatgpt-com-share-6aedf171-aae8-2\outputs\Imported References\nip7-investigation.png — Visual authority for the specified subject only; do not copy other characters, text, background or inset pictures. |
| CHAR_SEVEN_CATLEVEN_CLERK | E:\MovedFromC\Documents\Codex\2026-11-06\https-chatgpt-com-share-6aedf171-aae8-2\outputs\Imported References\7-catleven-exterior.png — Visual authority for the specified subject only; do not copy other characters, text, background or inset pictures. |
| CHAR_DOG_GUARD_A | E:\MovedFromC\Documents\Codex\2026-11-06\https-chatgpt-com-share-6aedf171-aae8-2\outputs\Imported References\steak-and-bone-meeting.png — Visual authority for the specified subject only; do not copy other characters, text, background or inset pictures. |
| CHAR_DOG_GUARD_B | E:\MovedFromC\Documents\Codex\2026-11-06\https-chatgpt-com-share-6aedf171-aae8-2\outputs\Imported References\steak-and-bone-meeting.png — Visual authority for the specified subject only; do not copy other characters, text, background or inset pictures. |
| CHAR_CAT_CIVILIAN_CROWD | C:\Users\DELL\Desktop\CyberKitty 2077\Assets\Character Sheets\kitty-punk-2077-character-dossiers.png — Visual authority for the specified subject only; do not copy other characters, text, background or inset pictures. |
| CHAR_HUMAN_AI_AVATAR | C:\Users\DELL\Desktop\CyberKitty 2077\Assets\Locations\Goodboy Global HQ\Reference Images\location-sheet-02-goodboy-global-hq.png — Visual authority for the specified subject only; do not copy other characters, text, background or inset pictures. |
| CHAR_RETURNING_HUMAN_COMMANDER | C:\Users\DELL\Desktop\CyberKitty 2077\Assets\Locations\Neko-Tokyo District 7\Reference Images\location-shot-pack-neko-tokyo-district-7.png — Visual authority for the specified subject only; do not copy other characters, text, background or inset pictures. |

### Required outputs for each recurring character

- `CHAR_<ID>_identity_front_v001.png`: clean head/shoulders, neutral lighting, no text or inset panels.
- `CHAR_<ID>_standing_front_v001.png`, `_threequarter`, `_left`, `_right`, `_back`: full body standing, same scale/outfit and visible feet/tail; no seated-only master.
- `CHAR_<ID>_head_turnaround_v001.png`: front/three-quarter/profile/back with locked muzzle, ears, markings and scar side.
- `CHAR_<ID>_expressions_v001.png`: neutral, amused, annoyed, worried, angry, surprised, determined; preserve facial identity.
- `CHAR_<ID>_paws_v001.png`: open, pointing, gripping controller, operating device; canine/feline furred anatomy, no human fingers. Human commander is the explicit human exception.
- `CHAR_<ID>_costume_gear_v001.png`: front/back layers, equipment close-ups, left/right placement, approved hood/visor states; damage/wetness variants only when a shot requires them.
- `CHAR_<ID>_scale_v001.png`: crew/council height comparison and silhouette checks. Five-cat crew sheet contains exactly five; council sheet contains exactly the eight named dogs.
- `CHAR_<ID>_voice.json`: selected ElevenLabs voice ID, authorized source, model, settings, pronunciation, age/accent direction and audition approval. Never store service credentials.
- `CHAR_<ID>_qc.json`: accepted reference hashes, rejected conflicts and visual checks. Human AI uses stable screen-icon states rather than body turnarounds. Crowd entry expands to six individual mini-masters.

**Additional pilot gaps beyond the 21 entries:** `CHAR_KITTEN_01` is the speaking kitten in scene 08 and needs a consistent design/voice; `PROP_SERVICE_ROBOT_01` is the moving restaurant robot in scene 13 and needs front/side/back and idle/movement references. Background shoppers and vendors can derive from the six-civilian roster with individually locked wardrobe. Factory/security extras must not silently turn into named council members.

## P0 prop, graphic and evidence inventory

| Asset IDs | Scenes | Create / repair / lock |
| --- | --- | --- |
| PROP_CRT; PROP_CATSTATION5; PROP_CONTROLLER_A–E | 01–03,24 | Exact CRT front/side/back, two right knobs; console top/side/front, controller front/back/grip; console stays above CRT; cable paths and couch layout fixed. |
| PROP_COUCH; PROP_BLANKETS; PROP_SNACKS | 01–03,24 | Couch front/back/side/overhead; wear map, cushions, blankets, bowl and cans with fixed positions. |
| GAME_GTKVI_COVER; GAME_GTKVI_BANK; GAME_GTKVI_CAR; GAME_GTKVI_HUD | 01,24 | Cover/front/spine; bank environment; game avatar and getaway car; loading screen, frozen state and HUD separate. Game figures never redefine real crew identities. |
| GFX_INTERRUPTION; GFX_CORPORATE_IDENT; GFX_SHORTAGE_MAP | 02,03,24 | Clean 16:9 bulletin layouts, lower thirds and districts7–12 map; final corporate name pending; exact typography applied in post. |
| PROP_SALMON_PACK; GFX_PRICE_NOTICE; GFX_PRICE_HISTORY; PROP_RECEIPT | 05,06,07 | Two sealed packs in freezer, previous $10/current $30 comparison, dated price evidence predating broadcast, receipt/scan display; keep one consistent timestamp logic. |
| PROP_SCANNER; PROP_HACKPAD; PROP_DATA_DRIVE | 05,09,17,19,21,22 | Front/back/side devices, blank screens, ports, paw interaction pose and carry state; no random device swaps. |
| PROP_PROJECTOR; GFX_BILLBOARD_CHART; PROP_RALLY_MIC; PROP_PA | 06,07 | Projector and public display/chart, microphone/stand, speakers/cables, stage/banners and crowd chant layout. |
| GFX_GRAFFITI; PROP_RALLY_BANNERS | 07,08,18 | Repeatable resistance marks; readable slogans and positions; no unexpected character portraits. |
| GFX_MEETING_INVITE; GFX_ENCRYPTED_MESSAGE; GFX_RESTAURANT_MAP | 09 | Evidence screens with exact sender/date/time and map tying the meeting to Steak & Bone; add readable text after rendering. |
| PROP_BONE_DECOY_01; PROP_BONE_REMOTE | 10,12,16 | Nonlethal rolling/squeaking bone: front/back/side, wheels, emitter, inactive/active states, last-decoy continuity; not a real injurious trap. |
| PROP_CAMERA; PROP_RECORDER; GFX_CAMERA_VIEWFINDER | 11,15 | Same lens/body/strap and recording device; empty viewfinder overlay and definitive payoff image captured from the actual dining-room setup. |
| PROP_LIMO; PROP_GUARD_RADIO; PROP_CCTV | 11–16 | Corporate limousine multi-view, guard earpieces/radio, security camera housing/POV, patrol path and alarm light. |
| PROP_SERVICE_ROBOT_01 | 13 | Repeatable service robot geometry, tray and wheels; empty-set route, idle/pass/turn reference, silent robot mechanical SFX; no spoken robot line in the current pilot. |
| PROP_DINING_TABLE; PROP_TABLEWARE; PROP_CASH_BAG; PROP_BANKNOTES | 14,15 | Table/chair placement; fixed plates/glasses; bag closed/open, cash contents, transfer hand-off frames with furred dog paws. |
| GFX_PAYOFF_PHOTO; GFX_AUDIO_WAVEFORM; GFX_UPLOAD | 15,17 | Preserve exact Barkington and Shiba identities/outfits and table direction; photo proves exchange, never substitute a wolf. Store uncropped evidence image and compositing crop. |
| GFX_NIP7_LEAK; GFX_NIP7_ROUTES; GFX_WOOF7_IDENT | 03,17,23 | Channel identities, blank/source presenter plates, accurate lower thirds, separately verified evidence inset and final shipment report. |
| GFX_CATNIP_TIMES_PAYMENT; GFX_CATNIP_TIMES_ROUTES; GFX_DAILY_BONE | 17,18,23; P1 Daily Bone | Front-page mastheads, exact headline/body copy, correct payoff photo; Daily Bone is broader universe prop and can follow pilot P0 work. |
| GFX_SHIPPING_DB; GFX_ROUTE_MAP; PROP_MANIFEST; GFX_CRATE_LABEL | 19–22 | Matching batch IDs, original allocations, signed routing overrides, districts1–6 vs7–12, timestamps and truck labels. Same evidence across monitor/paper/news. |
| PROP_SALMON_CARTON; PROP_SALMON_PALLET; PROP_REEFER_TRUCK | 20–23 | Sealed carton all sides, consistent fish logo/lot labels, pallet stack layouts, refrigerated truck exterior/interior and loading-door states. |
| PROP_DISPATCH_SWITCH; PROP_COOLING_CONTROL; GFX_COOLING_STATUS | 21,22 | Physically separate dispatch shutdown and active cold-chain systems; never show refrigeration disabled or salmon spoiled. |
| GFX_PUBLIC_DATA_RELEASE; GFX_REDIRECTED_ROUTES | 22,23 | Exact before/after dispatch visualization and readable publication confirmation, no invented evidence beyond master. |
| PROP_NEWS_BUNDLE; PROP_FISH_STALL; PROP_VENDOR_SCALE | 18,23 | Same newspaper editions, closed/empty and reopened/supplied stall states, crate unloading states, safe food-handling props. |
| GFX_SERIES_TITLE; GFX_CREDITS; GFX_END_BLACK | 24 | Final title/credit styling and timing; fitting credits into 20:00 remains an editorial decision. |

## P1 follow-on inventory

- Eight-dog boardroom sheet and exact eight-seat assignment: Barkington, Fetch, Muzzle, Viper, Frost, Stone, Velvet, Domino; fix obsolete muzzle-free Muzzle and remove any ninth dog.
- Muzzle lab, controlled-implant props and later reveal states; keep cybernetic muzzle silhouette unchanged.
- Public council/hearing room, neighborhood clinic/shelter, utilities/substation, monorail/checkpoint coverage, human archive, welfare center, beacon chamber and public landing pad for the PROPOSED later seasons. These are outside the 20 pilot-location IDs and must receive new IDs rather than being silently substituted for pilot rooms.
- Human AI icon/state library, limited-access interface screens, scout drone and returning-human ship/commander references, after later-season story approval.
- Daily Bone newspaper, corporate director offices and additional city districts only when a specific later episode requires them.

## Voice, audio and sound deliverables

**Current selected casting:** Trixie/Emma; Byte/Northern Terry; Ghost/Austin—Upbeat; Neon/Ryan; Onyx/Harry; NIP7/Daniel; Barkington/Brian; WOOF7/Eric. Account access is confirmed. Trixie is female19; the four boys remain15–19. Voice selection does not approve final takes. Countdown Casey remains the separate recurring car-radio host.

**Pending assignments / trials:** Austin—Deep, Raspy and Authentic remains the opening-narrator trial, distinct from Ghost. Jerry B. and Hugo remain separate unassigned dogs; Jerry B. is explicitly not Commander/Barkington. Guards, kitten and civilians still need casting. Ryan and Harry are now assigned to Neon and Onyx.

Latest requested Trixie recording: [Emma — salmon factory v002](<Voices/Requested Lines/trixie-salmon-factory-emma-v002.mp3>), **7.52 seconds**. Austin’s [opening narration trial](Voices/Narration/kitty-punks-opening-austin-v001.mp3) is **30.00 seconds**. Their pilot placement is unassigned; the 24-scene, 20:00 master is unchanged. Both earlier Lauren recordings remain preserved as superseded casting.

Use the [current casting overview](Voices/casting-overview.md), [casting pack](Voices/voice-casting-pack.md), [voice registry](Voices/voice-casting-registry.json), and [listening gallery](Voices/listen.html). The gallery accounts for **22 distinct review recordings across both listening pages**: seven original auditions, two requested-line versions, one narrator trial and 12 exact Scene 02–04 dialogue takes, excluding mirrored copies. Voice selection does not imply approval of a take as final dialogue.

The original pilot plan remains **17 voices**:11 individual principal/supporting voices including the kitten plus six proposed civilians. It excludes narrator/radio additions. The21-entry registry and silent service robot are unchanged. All eight principal/supporting role choices are selected; final performances, guards/kitten/civilians and Scene01 exact game banter remain unfinished. Austin’s decade-of-hacking claim needs chronology review against crew ages15–19 before placement.

ElevenLabs is the requested source. Current recording receipts identify their actual voices and settings. The earlier baseline audit of 17 local MP3 references remains historical and does not establish approved casting. The historical account check found three custom slots full; recheck live usage before a full batch.

| Group / asset IDs | Direction / output |
| --- | --- |
| VOICE_TRIXIE; VOICE_BYTE; VOICE_GHOST; VOICE_ONYX; VOICE_NEON | Youthful 15–19 direction, five clearly distinct voices. Trixie confident/impatient; Byte dry and precise; Ghost quiet and quick; Onyx grounded and protective; Neon bright, curious and fast. Preserve chosen accent/voice between scenes. |
| VOICE_BARKINGTON; VOICE_WOOF7; VOICE_GUARD_A; VOICE_GUARD_B | Older dog voices. Barkington polished authority; anchor practiced news cadence; guards distinct builds/voices. Avoid using the same stock voice for all dogs. |
| VOICE_NIP7 | British voice, clear investigative delivery; same Sphynx identity and measured reporting in both leak and confirmed-routes reports. |
| VOICE_CLERK; VOICE_CITIZEN; VOICE_KITTEN; VOICE_CROWD | Cast only lines actually in the 24-scene script. Distinct kitten line in scene08; crowd chant and nonverbal reactions recorded as controlled layers. |
| VOICE_FETCH; VOICE_MUZZLE; VOICE_DIRECTORS; VOICE_AI; VOICE_HUMAN | P1 later-season auditions; new IDs/settings remain provisional until selected. |
| SFX_ROOM; SFX_CITY; SFX_STORE; SFX_FACTORY; SFX_NEWS | Loopable room tone, rain/neon electric hum, shop freezer hum, cold-store machinery, studio beds; clean ends for editing. |
| SFX_CONTROLLERS; SFX_CRT; SFX_GAME; SFX_BONE; SFX_CAMERA | Controller clicks, CRT power/flicker, original game sirens/gunfire/engine, squeak/roll, shutter/recorder. Keep speech intelligible. |
| SFX_PAWS; SFX_CLOTH; SFX_DOORS; SFX_TRUCK; SFX_PRESS | Species-appropriate footsteps, outfit movement, service doors, brakes/refrigeration, newspaper press; match action timing. |
| MUSIC_OPEN; MUSIC_INVESTIGATION; MUSIC_INFILTRATION; MUSIC_HEIST; MUSIC_RETURN | Original or licensed cues and stems; recurring motif; controlled transitions and room for comedy silence. |

Render dialogue as one named speaker per file where possible: `S01E01_SC##_SH##_CHAR_LINE##_v001.wav`, plus transcript and timing sidecar. Export consistent edit-quality WAV when available; retain original downloaded format. Check pronunciation (Trixie, Byte, Neko-Tokyo, 7-Catleven, Barkington, WOOF7, NIP7), missing words, clipped starts/ends, accent drift and emotional continuity. Record model/version/settings and the approved voice ID, never a secret. Align generated motion to approved dialogue, not the reverse.

## Scene generation and verification

- Nothing in this README authorizes skipping the all-location-first production order. New scenes begin only when their location, cast and prop dependencies are ready.
- Each shot manifest records scene/shot ID, master time range, source reference hashes, character IDs, exact costume/gear state, location ID, camera position/height/lens, screen axis, blocking, action, dialogue file, sound, start/end state, prompt, model/version and output hashes.
- Use one clearly defined action/camera move per short clip. Keep actor count low in speaking coverage; use clean reactions and wide establishes to assemble conversation.
- Composite title text, captions, maps, newspapers, receipts and screen UI from exact graphics. Preserve TV perspective, reflection and CRT curvature.
- Check every visible face, species, paws, fur pattern, gear color and seat order; count the crew; verify Muzzle stays muzzled; compare each reverse angle to the approved plan.
- Reject object teleportation, extra limbs, swapped glasses/visors, changed scar side, duplicated actors, walking through fixtures, door moves and cold-store shutdown.
- Review animatic duration before paying for clips. The quoted $0.08/sec and $120 expected full-pilot estimate in the source are historical planning assumptions, not verified provider pricing or a spending authorization. The historical Orbis test cap was $5. The 81-credit location authorization is historical. The user subsequently authorized 500 additional Higgsfield image credits for Phase 2; use the current budget ledger and job receipts for commitments and actual billing, without treating authorization as spend. Higgsfield remains still-images-only; speech uses the user’s ElevenLabs account.
- Keep review and approved folders distinct. An approved still may be reused as a start frame; a reviewed sheet is not automatically a final cinematic plate.

## Files and versioning

- `pilot-master-24-scenes.txt`: supplied narrative/timing authority.
- `pilot-24-scene-index.json`: parsed 24 scenes and location crosswalk.
- `location-registry.json`: 20 location IDs, rooms, scenes, props, required outputs and on-disk status.
- `character-prompts.json`: 21 character entries with identity references and reusable prompts.
- `story-bible-proposed.json`: broader three-season development draft; pilot master above takes precedence.
- `Location Sheets v01/`: generated review PNGs, prompt manifests and QA notes.
- `Imported References/`: user-supplied incoming stills, retained as references.
- `Recovered References/`: verified copies of intact originals replacing corrupt reference inputs non-destructively.
- `Orbis Test/`: sanitized request/response records and test outputs only; no credentials.
- Use immutable versions (`v001`, `v002`) and record supersession. Never overwrite the original `README.txt`, source sheets or approved assets without an explicit replacement decision.
- Synchronize **Boardly board 133** and the **private** Hugging Face dataset from accepted manifests; record completion receipts and actual upload/status results. Do not mark pending external work complete in documentation.


Current location snapshot UTC: 2026-11-06T18:49:14.931317+00:00. All 20 new images and initial QA are complete; final approval remains pending. External synchronization outcomes are recorded in their receipts.


## Current pilot production desk

S01E01 production map v003: 24 scenes, 145 continuous shots, 222 dialogue cues, 2,082 words; editorial runtime 20:00. Timings for unrecorded lines remain estimates.

- [Pilot timeline](https://kittypunk.144.76.78.158.sslip.io/studio/episodes/1/1)
- [Current voice IDs and exports](https://kittypunk.144.76.78.158.sslip.io/studio/voices)
- Local map: Seasons/Season 01/Episode 01 - The Great Salmon Shortage/Production Map
- Approved Barkington voice: Matthew Schmitz; Brian archived.
- Approval policy: active manifests use approved replacements; superseded files move to Archive.
- Gameplay is always inside the existing television casing. Approved gaming dialogue remains unchanged.
