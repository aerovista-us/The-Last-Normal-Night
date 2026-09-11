# EP1 — The Last Normal Night

## Production status

**Stage:** Full script complete; visual reference lock approved; fixed layouts + storyboard/lettering proofs complete for all 24 story pages and the 14–15 rupture spread. Final panel-art replacement, lettering, QA and export are next.

**Story pages:** 24  
**Print trim:** 6.625 × 10.25 in  
**Full-bleed master:** 6.875 × 10.5 in / 2063 × 3150 px @ 300 DPI  
**Rupture spread master:** 4050 × 3150 px @ 300 DPI  
**Rack reader format:** 2063 × 3150  
**Optional motion moments:** 1

## Canonical files

- `script.md` — full page-by-page and panel-by-panel production script
- `art-prompts.md` — cover, inside-front, 24 story-page, back-cover, and optional motion prompts
- `focus-regions.json` — authored Rack Panel Focus reading map
- `PAGE_ASSEMBLY_STANDARD.md` — authoritative controlled-assembly workflow
- `PAGE_ART_QA.md` — acceptance/rejection log for generated page concepts
- `panel-prompts-p05-p08.md` — controlled panel prompts for the first anomaly batch
- `layouts/` — fixed SVG production geometry for all story pages + rupture spread
- `storyboards/` — storyboard/lettering proofs for all 24 story pages + rupture spread
- `storyboards/README.md` — storyboard index and final-art production order
- `../../reference/CDA_LOCATION_LOCK.md` — geographic continuity rules for real vs fractured Coeur d'Alene

## Visual reference lock

Approved working references exist for:

1. protagonist
2. truck exterior/interior
3. recurring white sedan
4. doorway geometry
5. normal CDA environment
6. fractured CDA environment
7. real-world CDA geography and street/landmark references

The real-world reference images are authoritative for geography. Generated environment boards are mood/lighting aids when their layout is approximate.

### Geographic rule

The fractured world remains the same Coeur d'Alene. Major geography, lake position, Tubbs Hill, downtown grid, Sherman Avenue, McEuen Park, resort/marina relationship, shoreline and major landmark placement stay coherent.

Wrongness comes first from controlled contradictions inside the real place, not from casually rearranging the city.

## Page-art QA status

Early generated page concepts are **exploratory only unless explicitly approved in `PAGE_ART_QA.md`**.

Useful visual discoveries so far:

- protagonist appearance
- dark wet-street palette
- practical North Idaho atmosphere
- strong noir lighting direction
- recurring white-sedan visual language

Known generation failures that must not enter final masters:

- wrong scripted panel counts/layouts
- protagonist driving when script says walking
- invented figures, notes or horror beats
- noncanonical `11:59` license plates
- altered CDA geography
- generated story text baked into artwork
- multiple scripted pages blended together

### Current QA state

- Pages 1–4: old concept art remains reference only; **canonical layouts/storyboards now complete**
- Page 5: concept pass rejected as final; canonical layout/storyboard complete
- Page 6: concept pass rejected as final; canonical layout/storyboard complete
- Page 7: concept pass rejected as final; canonical layout/storyboard complete
- Pages 8–13: fixed layouts + storyboard/lettering proofs complete
- Pages 14–15: 4050 × 3150 rupture spread layout + storyboard complete
- Pages 16–24: fixed layouts + storyboard/lettering proofs complete
- **All 24 story pages are now preflighted for final art production**

## Controlled storyboard gate

Every final page has now passed the structural storyboard gate. Each proof locks:

- panel count
- action/read order
- temporary dialogue/caption/UI placement
- negative space
- Rack focus compatibility
- reveal order

Final panel art is generated/sourced textless and placed into locked page geometry. Final lettering happens during assembly.

## Planned asset folders

```text
covers/
pages/
motion/
```

## Planned published asset order

```text
00-cover-front.png
01-inside-front.png
02-p01.png
03-p02.png
...
25-p24.png
26-cover-back.png
```

Optional motion insertion after story Page 15:

```text
motion/motion-01-midnight-rupture.mp4
motion/motion-01-midnight-rupture-poster.jpg
```

## Story exit state

The protagonist has refused the doorway back, the doorway closes, morning arrives from the wrong side, his phone returns to full signal, and the world identifies him with:

**WELCOME HOME**

Issue 2 begins from that exact state.

## Current production gate

**Next:** prove final-art assembly on Page 07.

Use:

- `storyboards/p07-storyboard.svg`
- `layouts/p07.svg`
- `panel-prompts-p05-p08.md`
- protagonist / CDA visual references

Build four textless plates, place into the locked page geometry, add final lettering, QA against `script.md` and `focus-regions.json`, then export the 2063 × 3150 master.

Once Page 07 passes as the visual-quality benchmark, proceed Page 08 → Page 24, then rebuild Pages 01–06 from their locked storyboards before publication.
