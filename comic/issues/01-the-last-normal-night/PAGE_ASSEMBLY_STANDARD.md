# EP1 Controlled Page Assembly Standard

This file defines the production method for final EP1 page art after exploratory full-page generations proved too willing to alter panel count, geography, signage and story beats.

## Core rule

**The scripted page layout is authoritative. Generated art fills panels; generated art does not decide the page structure.**

Final page master:

- 2063 × 3150 px
- 300 DPI target
- 6.875 × 10.5 in full-bleed working canvas
- trim 6.625 × 10.25 in

## Workflow

1. Use `script.md` for story, action, dialogue, SFX and panel count.
2. Use `focus-regions.json` as the starting geometry for panel rectangles and Rack mobile focus order.
3. Use `layouts/*.svg` as fixed page templates.
4. Generate or source each panel independently when full-page generation cannot preserve the scripted layout.
5. Place each approved panel into the fixed SVG/page geometry.
6. Add all lettering, UI, clocks, phone messages, captions and signage during layout — not in generated art.
7. Export the flattened page master at 2063 × 3150.
8. Recheck Rack focus regions against the final faces, balloons and action before publication.

## Visual continuity priority

1. Real CDA geography and user-supplied references
2. `comic/reference/CDA_LOCATION_LOCK.md`
3. EP1 protagonist/truck/white-sedan/doorway visual locks
4. `art-prompts.md`
5. Generated environment boards as mood only

If generated art conflicts with real CDA geography, the real reference wins.

## Forbidden drift in final masters

- wrong panel count
- multiple scripted pages merged into one
- noncanonical `11:59` license plates
- invented major CDA geography
- relocated resort, marina, Tubbs Hill, McEuen Park or major downtown streets
- generated story text replacing final lettering
- white sedan highlighted as overtly supernatural before the script calls for it
- portal/fantasy effects before the midnight rupture

## Page batch strategy

### Pages 1–4
Opening normality / first silence. Existing images remain concept references until rebuilt or assembled to match exact script geometry.

### Pages 5–8
First controlled-assembly validation batch. These pages prove the workflow because their panel structures are straightforward and their anomalies are subtle.

### Pages 9–13
11:59 convergence and reality-proximity escalation.

### Pages 14–15
One deliberate double-page rupture spread.

### Pages 16–24
Altered-CDA aftermath, Frequency Three intrusion, doorway choice and WELCOME HOME handoff.

## Approval rule

A page is not production-final merely because the art looks good. It must pass all of the following:

- correct panel count and order
- correct story beat
- consistent protagonist
- consistent truck / white sedan when present
- CDA geography plausible under the location lock
- lettering-safe space available
- no premature reveal
- Rack focus order still works

Only then should the page be moved into the final `pages/` publishing set.
