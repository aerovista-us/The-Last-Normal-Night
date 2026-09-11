# EP1 Controlled Panel Prompts — Pages 5–8

Use these prompts with the fixed templates in `layouts/`.

All panel art is generated **without final text**. Dialogue, captions, SFX, clocks, phone UI and signs are added during layout.

## Shared visual anchor

Mature prestige graphic-novel realism; grounded North Idaho atmosphere; textured ink linework with painterly digital color; cold blue-black night; wet asphalt; selective warm amber streetlights; believable adult anatomy; subtle psychological dread; no superhero gloss; no cyberpunk; no fantasy portal effects; no readable generated text.

**Protagonist:** early-to-mid 30s, dark short hair, short stubble, tired observant eyes, charcoal work jacket over faded black hoodie, dark jeans, worn boots.

**White sedan:** older white sedan, dented left rear quarter panel, one slightly dimmer tail light. Treat as ordinary unless the script says otherwise.

**CDA geography:** real-location references and `comic/reference/CDA_LOCATION_LOCK.md` override generated location invention.

---

# PAGE 05 — Streetlight / Signal
Template: `layouts/p05.svg`

## P05.1 — Streetlight ahead
**Target crop:** 1897 × 725 px

Quiet real-CDA sidewalk at night after rain, protagonist walking toward one normal amber streetlight, light visibly on, damp pavement and ordinary storefront/residential transition, no other people near him, no anomaly yet, calm realistic composition, protagonist small-to-medium in frame with room above/around him for later lettering if needed.

## P05.2 — Light shuts off
**Target crop:** 1897 × 630 px

Same sidewalk, same streetlight, same camera axis and protagonist continuity one beat later; protagonist directly beneath the lamp, lamp now dark, his face and shoulders fall into cooler shadow while surrounding distant lights remain normal; subtle electrical-failure feeling, no sparks, no supernatural glow.

## P05.3 — Light returns / phone signal
**Target crop:** 1897 × 630 px

Same location moments later; protagonist several steps beyond the lamp, same streetlight glowing behind him again, protagonist looking down at phone with screen visible but blank/unreadable for later signal-bar lettering, expression annoyed and puzzled rather than frightened; realistic wet reflections.

## P05.4 — Empty sidewalk / whisper
**Target crop:** 1897 × 535 px

Over protagonist’s shoulder as he turns back toward the same empty sidewalk, no visible speaker, no figure, no shadow-creature, no movement; illuminated streetlight in distance and ordinary CDA streetscape, the unsettling element is only the complete absence of anyone who could have whispered.

---

# PAGE 06 — Road Stretch / White Car Repeat
Template: `layouts/p06.svg`

## P06.1 — Sherman feels stretched
**Target crop:** 1897 × 630 px

Recognizable Sherman Avenue at night using real CDA storefront scale and street geometry; protagonist walking toward lake direction; perspective should feel only subtly too long, as though one familiar block takes a little more distance than it should, without changing major landmarks or inventing a fantasy city.

## P06.2 — White sedan passes
**Target crop:** 908 × 756 px

Street-level three-quarter view as the older white sedan passes protagonist from the same direction as traffic, left rear quarter-panel dent and slightly dimmer tail light visible but not emphasized; protagonist notices only casually; realistic local traffic and wet street.

## P06.3 — Same sedan repeats
**Target crop:** 908 × 756 px

Two blocks later, same protagonist and same older white sedan again passing from the same direction, identical dent and dim tail light; compose so readers can recognize the repeat without any visual magic effect; protagonist now looking directly at it with mild disbelief.

## P06.4 — Digital sign 11:58 plate
**Target crop:** 908 × 1260 px

Portrait composition of protagonist looking toward a plausible downtown digital clock/sign surface; leave the display completely blank and high contrast for final `11:58` lettering; recognizable wet CDA street context behind; no 11:59 anywhere else.

## P06.5 — Digital sign reverses
**Target crop:** 908 × 1260 px

Nearly matching angle moments later, same display surface and environment; leave display blank for final `11:57` lettering; protagonist in edge of frame looking back, confused; no glitch effects, only the impossible backward time value that will be added in layout.

---

# PAGE 07 — Clerk Recognition
Template: `layouts/p07.svg`

## P07.1 — Convenience store establishing
**Target crop:** 1897 × 756 px

Small realistic late-night convenience store in central CDA, fluorescent interior, modest shelves and counter, protagonist entering to buy water or gum, young clerk behind counter; nothing visually supernatural, believable local store rather than stylized horror set; leave sign surfaces unreadable or generic.

## P07.2 — Clerk recognizes him
**Target crop:** 908 × 851 px

Medium close shot of young clerk looking up at protagonist with immediate recognition and quiet relief, not menace; fluorescent light; protagonist partially foregrounded; reserve clean balloon space but generate no speech text.

## P07.3 — Good what?
**Target crop:** 908 × 851 px

Medium shot of protagonist paused with card/cash in hand, eyebrows slightly raised, confused by being recognized; clerk soft-focus opposite; grounded adult body language, not horror performance; clean upper area for dialogue balloon.

## P07.4 — Clerk smiles
**Target crop:** 1897 × 1039 px

Wide two-character counter shot; clerk gives a normal almost relieved smile while protagonist studies him uneasily; store remains mundane and believable; emotional wrongness comes from familiarity that should not exist, not from scary lighting or a sinister grin.

---

# PAGE 08 — WELCOME BACK Flash
Template: `layouts/p08.svg`

## P08.1 — Empty Sherman
**Target crop:** 1897 × 693 px

Recognizable Sherman Avenue at night after protagonist exits store, lamps on and storefronts lit but street strangely empty—no moving cars, no pedestrians, no insects around lamps; preserve real CDA street scale and lake direction; unsettling because normal activity is absent.

## P08.2 — Lake unnaturally flat
**Target crop:** 1897 × 693 px

Grounded view toward Lake Coeur d’Alene from a recognizable downtown/waterfront approach; same shoreline orientation and landmark relationships as real references; water almost perfectly flat and still despite normal night conditions, no fantasy glow, no portal, no altered shoreline.

## P08.3 — Phone no service
**Target crop:** 908 × 1260 px

Portrait close-up over protagonist’s shoulder holding phone against dark wet street background; phone screen clean/blank with controlled dark UI area for final `NO SERVICE` lettering; his thumb near screen, face partially visible and concerned; no generated text.

## P08.4 — Welcome Back flash
**Target crop:** 908 × 1260 px

Tighter portrait composition of same phone and hand one instant later; reserve a clean notification area for final `WELCOME BACK` typesetting with no sender/app icon; protagonist’s thumb reaching for the screen, expression startled in partial background; generate no readable words and no supernatural graphics.

---

# Assembly notes

- Use the same approved protagonist face/reference across all panels.
- Whenever two panels intentionally repeat a location, match lens height, light placement and architecture closely enough that the difference is readable.
- Phone and digital-sign text is added only after art placement.
- Crop/extend art to the locked panel rectangles rather than reshaping the page template around generated art.
- For Rack Panel Focus, retain primary faces/actions inside the normalized regions already defined in `focus-regions.json`.
