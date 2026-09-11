# EP1 Visual Asset Manifest

This manifest classifies uploaded/generated visual assets for **Episode 1 — The Last Normal Night**.

The purpose is to prevent rejected concept art from quietly becoming canon and to make clear which files are safe to reuse during final panel production.

## Status labels

- **LOCKED REFERENCE** — approved continuity/reference source. May guide final art directly, subject to written canon rules.
- **WORKING PAGE** — current assembled/generated page candidate in `pages/`; useful for sequence review but not automatically production-final.
- **CANDIDATE** — page candidate awaiting full QA/approval.
- **USEFUL CONCEPT** — good for mood, lighting, framing, texture, palette, or isolated details, but not authoritative for story or geography.
- **REJECTED STORY ART** — may be retained for lessons/style only; must not be used as a final comic page or as story canon.
- **UNCLASSIFIED** — uploaded asset whose exact intended production role is not sufficiently documented yet.

## Authority order

1. `script.md`
2. `PAGE_ASSEMBLY_STANDARD.md`
3. `focus-regions.json`
4. `../../reference/CDA_LOCATION_LOCK.md`
5. approved character / truck / sedan / doorway references
6. real-world user-supplied CDA photo/map references
7. generated mood/reference boards
8. working page candidates
9. rejected page concepts

If any image conflicts with written canon or real CDA geography, the written canon / real reference wins.

---

## Page-file naming convention

All EP1 page-art PNGs now live in `pages/`.

- `pXX.png` — current working page for that story page; still requires `PAGE_ART_QA.md` approval before publication.
- `pXX-candidate.png` — candidate page awaiting approval.
- `pXX-legacy-concept.png` — earlier page concept retained for reference only.
- `pXX-rejected-concept.png` — explicitly rejected story art; never publish as canon.
- `pXX-concept-a.png`, `pXX-concept-b.png`, etc. — exploratory concepts retained for visual reference.

Reference boards, CDA geography references, track artwork and mood images remain outside `pages/` because they are not comic-page masters.

---

## Current working page sequence

The September 11 generation batch has been normalized to:

- `pages/p09.png`
- `pages/p10.png`
- `pages/p11.png`
- `pages/p12.png`
- `pages/p13.png`
- `pages/p14.png`
- `pages/p15.png`
- `pages/p16.png`
- `pages/p17.png`
- `pages/p18.png`

**Status:** WORKING PAGE / QA REQUIRED  
**Rule:** These files are the current visual sequence for review, but their clean filename does not itself make them production-final. Every page still has to pass the locked script, panel count, reveal order, continuity, CDA geography, lettering, print geometry and Rack-focus checks.

Pages 14–15 must ultimately satisfy the canonical single-composition rupture-spread requirement, including the 4050 × 3150 spread master.

---

## Current Page 07–08 gate

### `pages/p07-candidate.png`
**Status:** CANDIDATE / QA REQUIRED  
**Role:** newer Page 07 candidate.  
**Must match:** four-panel convenience-store recognition sequence in `storyboards/p07-storyboard.svg` and `layouts/p07.svg`.

### `pages/p08-candidate.png`
**Status:** CANDIDATE / QA REQUIRED  
**Role:** Page 08 candidate.  
**Must match:** empty Sherman → unnaturally flat lake → NO SERVICE → transient WELCOME BACK sequence in `storyboards/p08-storyboard.svg` and `layouts/p08.svg`.

---

## Locked / primary references

### `2026-09-10__16-56-12__EchoStory-Continuity-Reference-Board__file_000000005aec81fd9c62aed2beaa38ae.png`
**Status:** LOCKED REFERENCE WITH CAVEATS  
**Role:** protagonist, truck, recurring white sedan, doorway geometry, overall palette / visual continuity language.  
**Caveats:** generated `11:59` truck plate is not canonical; exact CDA geography shown in the board is not authoritative.

### `ep1.visual-reference.png`
**Status:** LOCKED REFERENCE WITH CAVEATS  
**Role:** consolidated EP1 visual-language reference.  
**Caveats:** use only for appearance / mood / palette / object continuity; geography remains governed by real CDA references and `CDA_LOCATION_LOCK.md`.

### `wp1.vis-ref.png`
**Status:** LOCKED REFERENCE WITH CAVEATS  
**Role:** supporting visual continuity reference.  
**Caveats:** same as above; do not treat invented text, signage, geography, or timing motifs as canon.

### `cda.off.streets.png`
**Status:** USEFUL LOCATION REFERENCE / NOT AUTHORITATIVE ALONE  
**Role:** helps reason about CDA street relationships and wrong-world possibilities.  
**Rule:** use alongside the user-supplied real CDA photo/map set; do not let it override real geography.

### `if-tubbs-was-island.png`
**Status:** USEFUL CONCEPT / NONCANON GEOGRAPHY  
**Role:** visual thought experiment for altered-world feeling.  
**Rule:** Tubbs Hill / shoreline placement must remain geographically coherent in EP1; this image must not redefine the real city map.

---

## Environment / mood concepts

### `2026-09-10__19-23-52__EchoStory-The-Last-Normal-Night__file_00000000928881fd8eb33578f77ff645.png`
**Status:** USEFUL CONCEPT  
**Role:** early EP1 mood / branding / atmosphere reference.

### `2026-09-10__19-30-37__Moonlit-Lakeside-Town-Reflections__file_00000000a43c8230a403848b7670b888.png`
**Status:** USEFUL CONCEPT  
**Role:** lake reflections, moonlit atmosphere, cold-night palette.

### `2026-09-10__19-32-34__Uncanny-Moonlit-Lakeside-Town__file_00000000509c81f78c8b2d089f59c42c.png`
**Status:** USEFUL CONCEPT / REJECTED GEOGRAPHY  
**Role:** fractured-reality mood only.  
**Reason for geography rejection:** generated city layout drifted too far from actual CDA.

### `2026-09-10__19-35-11__Cinematic-Coeur-dAlene-Location-Reference-Board__file_000000009e4081fda2e98c2108c8ae47.png`
**Status:** USEFUL CONCEPT  
**Role:** location-language board and composition aid.  
**Rule:** real CDA references remain authoritative.

### `2026-09-10__20-00-11__EchoStory-Coeur-dAlene-After-Dark__file_00000000b2b481fd8548d7552a4794e2.png`
**Status:** USEFUL CONCEPT  
**Role:** normal-night lighting / wet-street / noir treatment.  
**Rule:** mood source only where generated geography differs from real CDA.

### `2026-09-10__20-00-24__EchoStory-Fractured-Coeur-dAlene-at-Night__file_000000003e708230892c3bef98f40ec0.png`
**Status:** USEFUL CONCEPT / REJECTED GEOGRAPHY  
**Role:** fractured-night lighting and uncanny mood.  
**Reason for geography rejection:** town arrangement changed too much; fractured CDA must remain recognizable as the same city.

### `2026-09-10__20-58-21__Rainy-Noir-in-Downtown-Coeur-dAlene__file_00000000706481fdb43883c8c8ec1289.png`
**Status:** USEFUL CONCEPT  
**Role:** wet-street noir lighting, protagonist scale, night contrast.

### `2026-09-10__21-01-40__Rainy-Lakeside-Mystery__file_00000000bbec81fdaa4852d0305d3a1e.png`
**Status:** USEFUL CONCEPT  
**Role:** lake / street / mystery atmosphere.

### `2026-09-10__21-01-42__Moose-Mug-Rainy-Lakeside-Night__file_00000000683c82309af8f598a7113737.png`
**Status:** USEFUL CONCEPT  
**Role:** grounded local-bar / storefront night mood.

### `2026-09-10__21-02-04__Rainy-Lakeside-Nightfall__file_00000000e1ec81fda0870c76f82c5096.png`
**Status:** USEFUL CONCEPT  
**Role:** rainy nightfall palette / lakeside lighting.

### `ep1.same-streets.different-tomorrow.png`
**Status:** USEFUL CONCEPT  
**Role:** visual thesis / mood reference for familiar-place-wrongness.  
**Rule:** do not treat any generated story details as canonical unless separately supported by `script.md`.

---

## Retained page concepts

### `pages/p01-concept-a.png`
**Status:** USEFUL CONCEPT / NOT FINAL  
**Role:** early opening-page concept.  
**Rule:** final Page 01 must follow `storyboards/p01-storyboard.svg` and `layouts/p01.svg`.

### `pages/p01-concept-b.png`
**Status:** USEFUL CONCEPT / NOT FINAL  
**Role:** alternate opening-page concept.  
**Rule:** same as above.

### `pages/p03-spread-concept.png`
**Status:** USEFUL CONCEPT / NOT FINAL  
**Role:** early multi-panel/spread exploration.  
**Rule:** must not override the locked page-by-page layout or the canonical Pages 14–15 rupture spread.

### `pages/p09-legacy-concept.png`
**Status:** LEGACY CONCEPT / NOT FINAL

### `pages/p10-legacy-concept.png`
**Status:** LEGACY CONCEPT / NOT FINAL

### `pages/p11-legacy-concept.png`
**Status:** LEGACY CONCEPT / NOT FINAL  
**Note:** restored from the original valid historical blob after a prior move produced a corrupt 2-byte file.

### `pages/p13-legacy-concept.png`
**Status:** LEGACY CONCEPT / NOT FINAL

---

## Page-art concepts rejected as finals

### `pages/p05-rejected-concept.png`
**Status:** REJECTED STORY ART / PAGE 05 CONCEPT  
**Useful:** palette, protagonist facial direction, anomaly rhythm.  
**Rejected because:** protagonist drives instead of walks; lettering baked into art; visible figure appears where script requires an empty sidewalk; invented location detail.

### `pages/p06-rejected-concept.png`
**Status:** REJECTED STORY ART / PAGE 06 CONCEPT  
**Useful:** lighting mood.  
**Rejected because:** seven panels instead of five; driving instead of walking Sherman; premature `11:59`; invented hooded figure; wrong route; missing `11:58 → 11:57`; generated text baked in.

### `pages/p07-rejected-concept.png`
**Status:** REJECTED STORY ART / PAGE 07 CONCEPT  
**Useful:** noir palette, sedan rendering quality, protagonist facial direction.  
**Rejected because:** seven panels instead of four; convenience-store scene omitted; invented note subplot; invented hooded woman; wrong character action; generated text baked in.

---

## Unclassified / needs explicit role confirmation before reuse

Any newly uploaded PNG/JPG not listed above should initially be treated as **UNCLASSIFIED** until its intended role is documented.

Do not promote an unclassified image into a final page simply because it looks polished.

---

## Duplicate-file cleanup

The duplicate page-art binaries previously scattered at repository root and the issue root have been removed from those duplicate locations. Page-art copies now live under `pages/` with role-explicit names.

Reference and mood images intentionally remain outside `pages/`.

---

## Final-art rule

A clean filename is not an approval state. No current uploaded PNG is automatically a publishable EP1 page.

A final page master must:

1. match the locked storyboard and panel count
2. preserve the exact scripted action and reveal order
3. use approved art / controlled assembly as required
4. preserve protagonist / vehicle / doorway continuity
5. preserve real CDA geography where applicable
6. contain clean final lettering added during layout where required
7. pass `PAGE_ART_QA.md`
8. export at **2063 × 3150 px** (or **4050 × 3150 px** for the Pages 14–15 spread master)
9. remain compatible with `focus-regions.json`

## Current production target

QA Pages 07–08 candidates, then review the normalized working sequence `p09.png` through `p18.png` against the script, storyboards, layouts, continuity rules, print geometry and Rack focus regions before promoting any page to production-final.
