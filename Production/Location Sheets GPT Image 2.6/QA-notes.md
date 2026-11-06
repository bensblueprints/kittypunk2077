# Location sheets — QA notes

All 20 Higgsfield GPT Image 2.6 PNGs are saved and measured at **3840 × 2160**. Hashes match their generation receipts. These are **review drafts**. Initial reviewer passes do not approve final layouts, clean plates or scenes.

The 16 earlier drafts and the prompt export remain preserved. No additional generation or paid corrections are included in this QA handoff. **Never use Higgsfield for videos.**

[Open the gallery](index.html) · [Generation manifest](generation-manifest.json) · [Machine-readable QA](QA-notes.json)

<a id="loc01"></a>

## LOC01 — Resistance warehouse exterior

[Open full sheet](<LOC01-resistance-warehouse-exterior-gpt26-v001.png>). Initial QA result: **draft-corrections**. Final production approval: **pending**.

- **annotation_required_before_blocking · 6 OVERHEAD PLAN:** Roof/site view does not clearly identify south cargo/staff and north service-bay door footprints. A/B/C arrows correspond to south front, north wall and southeast hero, but no arrow represents panel 9's southward apron-to-street reverse. Suggested correction: Annotate door footprints. Use an explicit legend such as A hero southeast looking northwest, B north looking south, C at south loading apron looking south to street. Keep the rendered architecture.
- **minor_state_note · 9 REVERSE WIDE:** Reverse appears under/inside the loading threshold whereas front facade views have a closed shutter. Suggested correction: When extracting plates, label open/closed shutter state explicitly; do not treat these as simultaneous door states.

Recommendation: Keep as review draft; annotation and state clarification are sufficient. No full rerender or extra generation retry recommended.

<a id="loc02"></a>

## LOC02 — Resistance warehouse lounge

[Open full sheet](<LOC02-resistance-warehouse-lounge-gpt26-v001.png>). Initial QA result: **draft-corrections**. Final production approval: **pending**.

- **required_before_reverse_dialogue_plates · 3 SOUTH / REVERSE WALL; 6 OVERHEAD PLAN:** Panel3 shows a high plain outside-style couch back rather than a clear seat/front view from the TV side. The top-down sofa geometry remains ambiguous about which edge is the open seat, despite putting the emblem on the southern edge. Suggested correction: Use hero/north anchors, but derive a true front seating view before reverse dialogue. Mark the seat-facing edge NORTH and outside back SOUTH explicitly in the authoritative furniture plan. Do not assume the current reverse is a verified front-couch master.
- **required_geometry_lock_before_coverage · 3 SOUTH / REVERSE WALL; 5 WEST / ENTRY SIDE; 6 OVERHEAD PLAN:** South and west panels show substantially the same entry-wall arrangement. In a view facing south the opening on viewer-left reads southeast, while the plan fixes the opening at southwest on the west side. Suggested correction: Keep one southwest west-side passage. A true south-wall view must not mirror it to the southeast; resolve with a clean south elevation when making plates.

Recommendation: Useful improved hero/TV reference, still a review draft for reverse coverage. Preserve this result; no extra generation retry requested under the current batch budget.

<a id="loc03"></a>

## LOC03 — Hacking operations

[Open full sheet](<LOC03-hacking-operations-gpt26-v001.png>). Initial QA result: **draft-corrections**. Final production approval: **pending**.

- **minor_annotation_before_blocking · 6 OVERHEAD PLAN; 1 HERO:** Camera A is north of the worktable looking north, but hero includes that table in the foreground. That A position cannot produce the shown hero composition. Suggested correction: Move the hero camera marker south of the worktable and state its northward bearing. Give B/C explicit position-plus-direction labels.
- **viewpoint_needs_blocking_confirmation · 9 SECOND WIDE (DESK TO WAREHOUSE):** Second wide shows the fronts of the north-wall monitors while also presenting itself as the desk-to-south-warehouse reverse. It works as an oblique overview but is not a verified opposite-angle camera plate. Suggested correction: Retain as an oblique overview. Derive the true southward reverse from the approved plan if the edit needs matching reverses; do not use its label alone as camera authority.

Recommendation: Strong usable operations design. Main counts and anchors pass; plan-camera and reverse-label corrections remain. No regeneration retry requested.

<a id="loc04"></a>

## LOC04 — Engineering workshop

[Open full sheet](<LOC04-engineering-workshop-gpt26-v001.png>). Initial QA result: **pass**. Final production approval: **pending**.

- **minor_annotation_before_blocking · 3, 5, 6:** Both south-opening and west-passage views show a similar operations area beyond the workshop; the local plan stops at the bay boundary and does not resolve their relationship to the warehouse-wide operations layout. Suggested correction: When joining LOC03 and LOC04 for a walk-through, annotate the shared warehouse plan and choose matching passage directions. This is not a reason to rerender this sheet.

Recommendation: Usable workshop design reference. Preserve the successful fixed equipment layout. No regeneration retry requested.

<a id="loc05"></a>

## LOC05 — District 7 streets and alleys

[Open full sheet](<LOC05-district-7-streets-and-alleys-gpt26-v001.png>). Initial QA result: **draft-corrections**. Final production approval: **pending**.

- **minor_annotation_before_blocking · 2, 3, 6:** Plan camera markers and legend all point north, including B at the north end. The legend says C SOUTH but still shows an upward/N arrow. The north-approach image is another north-looking view, while the reverse view flips storefront/tree sides. Labels and bearings cannot currently define a reliable reverse setup. Suggested correction: Choose the actual north-looking and south-looking plates, label them by camera position plus viewing direction, and redraw B/C bearings. Do not treat all arrows as valid.
- **required_geometry_lock_before_coverage · 4, 6, 9:** The plan places 7-Catleven south of the east alley, but the east-looking alley view shows its frontage on the left/north side. The alley-mouth reverse also places the store across/right rather than presenting the expected corner relationship from the mapped alley. Suggested correction: Lock the store and alley corner with LOC06 before any continuous street-to-alley move. Retain the main-street design and establish one coherent east-alley corner for scene plates; do not use panel 9 as proven geographic coverage.

Recommendation: Useful empty District7 street design and textures. Alley/store corner and camera annotations remain drafts. No regeneration retry requested.

<a id="loc06"></a>

## LOC06 — 7-Catleven exterior

[Open full sheet](<LOC06-7-catleven-exterior-gpt26-v001.png>). Initial QA result: **pass**. Final production approval: **pending**.

- **minor_annotation_before_blocking · 6; cross-set LOC05/LOC07:** The LOC06 local map correctly makes the storefront south-facing with an east-side alley. LOC05 instead embeds the shop facing west on its north-south street. Interior glimpses and the decorative cutaway should also not supersede LOC07 interior blocking. Suggested correction: Declare whether local storefront axes rotate within the district map or place this shop on an east-west cross street. Use LOC07 as interior authority before an uninterrupted entrance shot; keep LOC06 exterior architecture.

Recommendation: Usable exterior design with strong repeated facade identity. Resolve cross-set street mapping as an annotation, without an automatic image retry.

<a id="loc07"></a>

## LOC07 — 7-Catleven interior and freezer

[Open full sheet](<LOC07-7-catleven-interior-and-freezer-gpt26-v001.png>). Initial QA result: **pass**. Final production approval: **pending**.

- **minor_annotation_before_blocking · 6:** Camera C at the north/rear end points north although the rear-to-entrance coverage looks south. Suggested correction: Turn C south to match panel 9 before using the map for blocking.
- **minor_prop_continuity_before_closeups · 1, 5; cross-set LOC06 south glazing:** The salmon pair and notice appear in the same near-front freezer bay in the hero but adjacent bays in the straight freezer view. Interior entrance views also retain the exterior-style pink cat neon on viewer-right, whereas the same east-side window would appear viewer-left when looking south from inside. Suggested correction: Use the straight WEST freezer view as the authoritative pair/notice placement for inserts; lock the entrance window graphics to the LOC06 east window for matching inside/outside views.

Recommendation: Usable and clear store interior reference. Essential two-pack shortage story content is present. Correct camera annotation and lock small prop/window details when making scene plates; no retry requested.

<a id="loc08"></a>

## LOC08 — District 7 market

[Open full sheet](<LOC08-district-7-market-gpt26-v001.png>). Initial QA result: **draft-corrections**. Final production approval: **pending**.

- **required_geometry_lock_before_coverage · EAST:** The panel labeled from east looking west repeats a hero-like view with lantern stalls on the left and the tower vista ahead. A true west-looking view should put the north stalls on the right and reveal the west plaza, as the successful REVERSE WIDE does. The east stair is present but this panel does not establish trustworthy street orientation. Suggested correction: Use PLAN plus HERO/REVERSE as the geographic authority, and derive a later east-end/stair plate from them. Keep the northeast stair relationship when joining LOC20.
- **minor_annotation_before_blocking · SOUTH:** The panel labeled from south looking north shows the south shuttered shop row and its billboard. It is a south-wall elevation viewed from the north, rather than the stated camera-side convention. Suggested correction: Relabel this panel SOUTH SHOP ROW / VIEW SOUTH, or otherwise give the actual camera side and bearing.

Recommendation: Strong usable hero, reverse, plan and material references; preserve this market identity. Directional east coverage remains draft and south label needs correction. No automatic retry requested.

<a id="loc09"></a>

## LOC09 — District 7 rally stage and plaza

[Open full sheet](<LOC09-district-7-rally-stage-and-plaza-gpt26-v001.png>). Initial QA result: **draft-corrections**. Final production approval: **pending**.

- **required_geometry_lock_before_coverage · ROOFTOP OVERLOOK, PLAN:** The rooftop view faces north toward the stage with the tree on the left. It therefore reads as a south-side rooftop, not camera B on the north building looking south; from B the stage building could not appear across the plaza. Suggested correction: Keep the hero and site plan as authority. Do not use this roof view as the specified north/northeast perch; derive the eventual roof scene plate from an agreed joint LOC08/09/20 plan.
- **required_geometry_lock_before_coverage · EAST; cross-set LOC08:** The market connection view puts the red-lantern stalls on the right while looking down the market toward the towers. For the established east-looking market axis, the north lantern row should be left. The plaza plan depicts the lantern edge along its east boundary without clearly showing the east-west street continuation. Suggested correction: Annotate the market mouth and north-row continuation on the shared site plan and use LOC08 hero/reverse as authority for market-facing scene plates.
- **minor_coverage_annotation · SOUTH, cardinal labels:** SOUTH is a tight shuttered-shop elevation rather than the requested stage POV across the audience space with west steps. Cardinal labels generally describe facade/content rather than the final camera-side convention. Suggested correction: Treat the shop image as material/elevation reference; label actual viewpoint bearings before blocking. A later stage-POV scene plate must include the open audience area.

Recommendation: Usable rally stage design and plaza hero. Rooftop and market-connection coverage are drafts, not geographically verified scene plates. No regeneration retry requested.

<a id="loc10"></a>

## LOC10 — Steak & Bone exterior and security

[Open full sheet](<LOC10-steak-bone-exterior-and-security-gpt26-v001.png>). Initial QA result: **draft-corrections**. Final production approval: **pending**.

- **required_geometry_lock_before_coverage · REVERSE WIDE, PLAN B:** The reverse shows the restaurant facade across a street from a foreground rooftop railing. That is an opposite-building surveillance perch, not the mapped camera B on the restaurant northwest roof; the restaurant cannot see its own whole south facade across the lane from that position. Suggested correction: Keep the exterior design. Either document a separate opposite-roof camera position, or derive a later south-looking plate from the restaurant roof that looks down on its own arrival lane. Do not use this panel as proven camera B coverage.
- **minor_annotation_before_blocking · PLAN:** The overhead is primarily a roof plan. The north service-door footprint and guard/scanner pedestrian route are not clearly marked even though their views are present. Suggested correction: Annotate those ground-level access points and lock the west stair landing before planning the infiltration path.

Recommendation: Strong usable restaurant exterior and security fixture reference; rooftop surveillance geography remains draft. Preserve successful facade and material design. No regeneration retry requested.

<a id="loc11"></a>

## LOC11 — Steak & Bone service corridors

[Open full sheet](<LOC11-steak-bone-service-corridors-gpt26-v001.png>). Initial QA result: **draft_requires_geometry_correction**. Final production approval: **pending**.

Observed strengths: Nine labeled panels including plan, ceiling and materials; No visible occupants, animals or robots; Kitchen swing door and hatch, trolley alcove, burgundy service door, camera, red alarm and utility finishes present; Plan has north arrow and A/B look arrows.

- **major · Layout / continuity:** Both wides read as a straight corridor with opposite end doors. The plan depicts an L-shaped corridor; the reverse from its northern dining door could not see the west exterior exit directly as rendered.
- **major · Layout / continuity:** Hero places the exterior double exit on the same side wall as the kitchen door/hatch, while the plan and WEST elevation place it at the west end. Burgundy dining door appears at the far east end in the hero rather than around the northward turn.
- **minor · Layout / continuity:** The trolley alcove appears near the kitchen-side wall in the hero, while its intended position is the south wall as shown by the SOUTH panel and plan.

Recommendation: Retain material and prop design; rebuild hero and reverse from the L-shaped plan and lock all door/alcove positions before camera blocking.

<a id="loc12"></a>

## LOC12 — Steak & Bone private dining room

[Open full sheet](<LOC12-steak-bone-private-dining-room-gpt26-v001.png>). Initial QA result: **draft_requires_geometry_correction**. Final production approval: **pending**.

Observed strengths: Nine panels and unoccupied set; Gold chandelier, burgundy seating, black/gold marble, east windows, north Steak & Bone sign and west sideboard present; Two tumblers and two plates; no money bag or story action; North arrow and A/B camera arrows present with sensible diagonal directions.

- **major · Layout / continuity:** Plan places the service door at the southwest corner, but SOUTH and REVERSE WIDE show it at screen-left beside the east window wall: the southeast corner.
- **major · Layout / continuity:** Plan places the long table east-west with opposing seats north/south. Hero and reverse instead show the long table running toward the north/south walls, with seats west/east. Table and booth orientation do not match the plan.
- **minor · Layout / continuity:** Door has no narrow frosted-glass strip, unlike the adjoining LOC11 burgundy service-door design; cross-set doorway continuity needs reconciliation.

Recommendation: Keep the strong luxury material design; lock southwest service door and table/booth axis consistently across plan, south elevation and wides before shooting.

<a id="loc13"></a>

## LOC13 — WOOF7 news studio

[Open full sheet](<LOC13-woof7-news-studio-gpt26-v001.png>). Initial QA result: **draft_requires_door_continuity_correction**. Final production approval: **pending**.

Observed strengths: Nine panels, empty chair and unmanned equipment; no cast or CRT shell; North WOOF7/world map, curved desk, east control booth, west vertical display, two cameras and ceiling grid present; North arrow and distinct A/B positions point toward their corresponding hero/reverse views; Control booth switches from hero right to reverse left correctly.

- **major · Layout / continuity:** Plan and brief put the rear exit at southwest. SOUTH and REVERSE WIDE show that exit at screen-left beside the east control-booth wall, which is southeast. Move the exit consistently to the west side or deliberately revise the plan.
- **minor · Layout / continuity:** Screen brief is internally mixed: design section permits quiet WOOF7/blue graphics, while final instruction says keep screens blank. Image follows the graphic version; confirm graphics policy before using as a clean compositing plate.

Recommendation: Strong studio design; resolve south exit location, then verify west newsroom-door position against the plan at production blocking stage.

<a id="loc14"></a>

## LOC14 — NIP7 investigative newsroom

[Open full sheet](<LOC14-nip7-investigative-newsroom-gpt26-v001.png>). Initial QA result: **draft_requires_exit_location_correction**. Final production approval: **pending**.

Observed strengths: Nine labeled panels; empty studio with no presenters, portraits, bribe image or CRT frame; One two-seat anchor desk, west two-seat editing bench, east glass/noticeboard, north NIP7 map, one tripod camera; Resourceful brick/wood/acoustic-panel design clearly distinct from WOOF7; Plan has north arrow and two distinct camera marks with opposing diagonal arrows.

- **major · Layout / continuity:** Exit location does not agree: brief specifies south wall near southwest; plan appears to put it on the west wall near southwest; SOUTH and REVERSE WIDE place it on the left/east end of the south wall, adjacent to the control-room side.

Recommendation: Keep design and desk arrangement. Align the single exit wall/corner across plan, SOUTH and reverse before scene blocking.

<a id="loc15"></a>

## LOC15 — Salmon facility exterior and loading

[Open full sheet](<LOC15-salmon-facility-exterior-and-loading-gpt26-v001.png>). Initial QA result: **draft_requires_gate_and_camera_corrections**. Final production approval: **pending**.

Observed strengths: Nine panels, no visible cast; parked refrigerated trucks are allowed; Four ordered docks, two trucks at bays 1/2, fish sign over 1/2 and dispatch glazing over 3/4; D1-6 versus D7-12 separation and canine emblem present; company wordmark omitted; East coolant enclosure separate from loading; west stairs/service door and blank board present.

- **major · Layout / continuity:** Guard booth is east/right of south gate in the north-up plan, but right of the gate in the south-facing SOUTH and reverse renders, placing it west in those views. This violates the explicit no-mirroring requirement.
- **major · Layout / continuity:** Directional labels disagree with rendered views and the specified exterior convention. NORTH shows the north facade viewed from south; SOUTH says looking north but depicts the south gate from inside looking south.
- **moderate · Layout / continuity:** Plan camera B is drawn near the southeast portion of the yard rather than the requested northeast reverse position. Camera icons lack clearly readable look arrows; verify against the reverse plate.
- **minor · Layout / continuity:** Extra Kitty Punk 2077 wordmark appears in the header despite title/short-label-only instruction.

Recommendation: Retain industrial design and dock assignment; correct booth side and plan/view labels before production blocking.

<a id="loc16"></a>

## LOC16 — Salmon cold store and processing hall

[Open full sheet](<LOC16-salmon-cold-store-and-processing-hall-gpt26-v001.png>). Initial QA result: **draft_requires_continuity_correction**. Final production approval: **pending**.

Observed strengths: Nine panels and no cast; fixed industrial arms are permitted by this specific brief; Hero and north view clearly reveal deep salmon-carton stockpiles through both open cold doors; Cyan active refrigeration, two conveyor lines, clear center aisle, east elevated control room and west wash stations; North arrow and A/B plan marks present; company name omitted.

- **major · Layout / continuity:** Personnel door is southwest in plan but appears left of the shutter in SOUTH/reverse views, placing it southeast.
- **major · Layout / continuity:** Yellow arms are near the north/cold-door ends of the conveyors in HERO, but near the south/shutter ends in REVERSE. Their mounting positions move between views.
- **moderate · Layout / continuity:** Camera A's triangular pointer appears to point southwest out of the room, opposite the hero's required northeast look direction; use an explicit arrow.
- **prompt_conflict · Layout / continuity:** Final brief asks BOTH hero and reverse to reveal north cold-room stockpiles, while the defined reverse camera looks south at the loading shutter. The image reveals stock in the hero only; resolve this incompatible requirement before requesting correction.

Recommendation: Stockpile reveal is successful. Lock personnel door and arm positions, correct A arrow, and choose whether reverse remains a south-facing architecture plate.

<a id="loc17"></a>

## LOC17 — Salmon routing control room

[Open full sheet](<LOC17-salmon-routing-control-room-gpt26-v001.png>). Initial QA result: **draft_requires_door_and_shelf_continuity_correction**. Final production approval: **pending**.

Observed strengths: Nine panels and empty control room; Three north racks, independent COLD ON indicator and separate DISPATCH stop prop; East routing groups 1-6 and 7-12, two desk/chair stations, west glass overlooking processing rather than city or duplicate control room; Plan north arrow and readable A/B viewing cones point northeast/southwest.

- **major · Layout / continuity:** Single entry door moves: plan specifies south wall at southwest; HERO places it along the west glass wall; SOUTH and REVERSE show it on the east/left side of the south wall, away from the west-glass corner.
- **moderate · Layout / continuity:** Document shelf is northeast in plan but on the right/south end of the EAST elevation, so its corner is mirrored.
- **minor · Layout / continuity:** Extra Kitty Punk 2077 header wordmark beyond requested title and short labels.

Recommendation: Keep functional control design and cooling/dispatch separation. Reconcile southwest door and northeast shelf across all views before filming.

<a id="loc18"></a>

## LOC18 — Catnip Times pressroom

[Open full sheet](<LOC18-catnip-times-pressroom-gpt26-v001.png>). Initial QA result: **draft_requires_cupboard_and_prop_correction**. Final production approval: **pending**.

Observed strengths: Nine panels and empty pressroom; Single north-south press, two south feed rolls, north windows/sign/editor desk, centered south freight doors; East reels/inks and west two pinboards/four pigeonhole shelves present; North-up plan and A northeast/B southwest arrows largely agree with the wides.

- **major · Layout / continuity:** Store cupboard is northeast in the plan, but EAST elevation shows its door at the screen-right/south end of the east wall. Fix this mirrored corner.
- **moderate · Layout / continuity:** Trolley is on the east/right side of south freight doors in plan, but on screen-right/west in the south-facing SOUTH elevation.
- **minor · Layout / continuity:** Newspaper prop contains simulated dense article lines/tiny lettering below masthead rather than clean blank column blocks; replace with exact typography during prop finishing.

Recommendation: Core pressroom geography is useful. Correct cupboard and trolley sides; use a clean newspaper overlay for close-up inserts.

<a id="loc19"></a>

## LOC19 — Game world: Great Dog National Bank

[Open full sheet](<LOC19-game-world-great-dog-national-bank-gpt26-v001.png>). Initial QA result: **draft_requires_plan_and_direction_labels**. Final production approval: **pending**.

Observed strengths: Nine panels; empty game-world exterior with no CRT, HUD, weapons or playable characters; Bank north, opposite storefront south, open east/west street, gold door/sign/medallion and consistent main facades; GAME WORLD label clear; readable bank title and three-step entrance; Hero A is southwest looking northeast; reverse visually looks from bank toward opposite storefront.

- **major · Layout / continuity:** Plan B is at the south side and points north toward the bank. Actual reverse is from north/bank steps looking south. Move B to bank steps and reverse its arrow.
- **moderate · Layout / continuity:** NORTH/SOUTH panel labels use target-wall naming instead of specified exterior camera-side convention. NORTH shows bank from south; SOUTH shows storefront from north. East/west side labels are consistent.

Recommendation: Useful coherent empty game set. Correct B position/arrow and swap north/south captions before treating plan as camera guide.

<a id="loc20"></a>

## LOC20 — District 7 market rooftop overlook

[Open full sheet](<LOC20-district-7-market-rooftop-overlook-gpt26-v001.png>). Initial QA result: **draft_requires_roof_and_market_geography_correction**. Final production approval: **pending**.

Observed strengths: Nine panels and empty roof; no helipad, aircraft or cast; Plan has northeast hut with south-facing door, west HVAC pair/planters, east rail/spool, and clear central staging area; Plan A northwest looking southeast and B southwest looking northeast are clearly marked; Wet rooftop materials and nocturnal neon atmosphere fit the district.

- **major · Layout / continuity:** Hut moves to screen-left/northwest in SOUTH view looking north, although plan fixes it northeast. EAST view largely repeats a north-facing hut view instead of looking west from the east edge.
- **major · Layout / continuity:** HERO shows lantern fish stalls across the street from the roof. Plan and SOUTH elevation place those stalls directly beneath this north-row roof. The hero therefore reverses the market-side relationship; the opposite south-row shuttered shops and fixed billboard are not established.
- **major · Layout / continuity:** REVERSE looking northeast puts pipe railing and cable spool at foreground left, although plan fixes them east/right. WEST view also relocates hut/HVAC relative to the north/east corners.
- **moderate · Layout / continuity:** No clear matching view of LOC08's western street mouth/rally connection or opposite billboard. Market cross-set geography cannot yet be approved from this sheet.

Recommendation: Use plan as provisional roof master, rebuild the named elevations and hero/reverse from it, and explicitly match the same LOC08 stall/billboard/stair geometry before scene 23.

