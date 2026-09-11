# The Last Normal Night — Comprehensive Handoff

**Date:** 2026-09-11  
**Project:** EchoStory — The Last Normal Night  
**Canonical repository:** `aerovista-us/The-Last-Normal-Night`  
**Public site / player:** `https://lastnormalnight.aerovista.us/`

---

# 1. Executive status

The project has moved well beyond concept stage.

## Album / EchoStory

- The 10-track story arc is canonically defined.
- Lyrics and Suno style files exist for all 10 tracks.
- Track artwork PNGs exist in all 10 track folders.
- Real MP3 audio is committed for Tracks 1–3.
- Tracks 4–10 do not currently have committed MP3s.
- The root web player is built for all 10 chapters and should automatically recognize audio as the expected files appear.

## Comic

- The comic is defined as a **10-issue mature limited series**, one issue per album track.
- Issue #1 / Track 1 is a 24-story-page adaptation.
- EP1 has a complete panel-by-panel script.
- All 24 EP1 story pages have fixed SVG layouts.
- All 24 EP1 story pages have storyboard / lettering proofs.
- Pages 14–15 are designed as one deliberate 4050 × 3150 rupture spread.
- Rack Panel Focus geometry has been authored.
- CDA geographic continuity rules are locked.
- A controlled page-assembly standard exists specifically to stop generative art from changing the story.
- **No final `pages/` publishing folder is currently committed in the repo.** Final flattened page masters still need to be assembled and approved.

## Current visual-production reality

The written story and storyboards are strong. The weak point has been free-form full-page image generation.

The generator repeatedly drifted into:

- incorrect page beats
- lifestyle / “normal day” montages
- wrong panel counts
- premature or repeated motifs
- invented characters and subplots
- `Time Circuit` or `The Signal` branding instead of EchoStory
- baked-in generated lettering
- altered CDA geography

Therefore the controlling production rule is now:

> **Generated art fills a locked panel. Generated art does not decide the page.**

The current session produced useful visual ideas, but anything generated after Page 8 must be treated as **concept/reference only unless it is rebuilt against the canonical storyboard and explicitly approved**.

---

# 2. Source-of-truth hierarchy

## Global story / music canon

1. `docs/STORY_BIBLE.md` — reveal order, discoveries, decisions, consequences, handoffs
2. `docs/CONTINUITY.md` — motif meanings and sonic continuity
3. `docs/RULES.md` — fracture rules and character constraints
4. `README.md` — project overview / track sequence
5. per-track `lyrics.md` and `style.md`

## Comic canon

1. `comic/issues/01-the-last-normal-night/script.md`
2. `comic/issues/01-the-last-normal-night/PAGE_ASSEMBLY_STANDARD.md`
3. `comic/issues/01-the-last-normal-night/focus-regions.json`
4. `comic/reference/CDA_LOCATION_LOCK.md`
5. `comic/issues/01-the-last-normal-night/layouts/*.svg`
6. `comic/issues/01-the-last-normal-night/storyboards/*.svg`
7. approved protagonist / truck / sedan / doorway references
8. real user-supplied CDA location references
9. generated mood/reference boards
10. rejected experimental page art

If an attractive generated image contradicts the script, story bible, continuity ledger, or real CDA geography, **the generated image loses**.

---

# 3. Canonical story spine

## Core premise

An ordinary night in Coeur d’Alene slips at midnight. The protagonist crosses into a CDA that is almost correct but wrong. A doorway back appears almost immediately. He refuses it.

That choice is the center of the story.

The deeper question becomes:

> **Which world was home in the first place — and which version of him made that decision before?**

## Three acts

### Act I — The Crossing / Tracks 1–3

**Emotion:** comfort → unease → fear → curiosity

1. **The Last Normal Night — The Crossing**  
   Reality splits. He refuses the doorway back. Phone says `WELCOME HOME`.
2. **The Wrong Side of Morning — Exploration**  
   Daylight proves this is a different history, not simply the future.
3. **Frequency Three — The Voice**  
   An older version of his own voice communicates through the truck radio, but messages arrive out of sequence.

### Act II — The Fracture / Tracks 4–7

**Emotion:** curiosity → pursuit → dread → recognition

4. **The Man in My Shadow — The Doppelgänger**  
   Another physical version of him exists and drops an impossible duplicate object.
5. **The Lake Remembers — The Constant**  
   The lake persists across realities and behaves like a memory boundary.
6. **Don’t Answer Yourself — The Rules**  
   Older-him reveals survival rules; his own voice calls from behind him.
7. **I Already Did This — The Fracture**  
   Déjà vu becomes memory and evidence implies this sequence has happened before.

### Act III — The Return / Tracks 8–10

**Emotion:** recognition → betrayal → choice → acceptance

8. **Welcome Back — The Reveal**  
   The strange world may have been home first.
9. **The Door Was Never for Me — The Confrontation**  
   The doorway was primarily an entrance, not an exit; he chooses a third option.
10. **Midnight Knows My Name — The Choice**  
   Older-him appears physically; the protagonist rejects simple repetition and breaks the repeating choice.

---

# 4. Locked motifs and what they mean

Do not use motifs as decoration. Their appearances carry mechanics.

## 11:59

Threshold marker: reality preparing to split. Use sparingly.

## Frequency Three

Communication across displaced time / reality. Messages can arrive out of order.

## Wooden-flute growl / waveform

Two realities are close enough to touch. It is never random atmosphere.

## The lake

Cross-reality constant and memory boundary. City details may change; the lake persists.

## White car / sedan

Quiet continuity clue. Do not explain early or make it overtly supernatural.

## Truck

The protagonist’s moving anchor and safest familiar physical space.

## Phone signal

- no signal = displaced / between states
- signal return = a reality has recognized / indexed him

`WELCOME BACK` and `WELCOME HOME` are therefore mechanical story signals, not decorative texts.

## Moon halo

Quiet confirmation that he remains displaced.

## Wrong reflection / shadow

Identity overlap. Do not turn it into generic ghost imagery.

---

# 5. Character rules

## Protagonist

- practical, grounded North Idaho adult
- curious before heroic
- notices physical details
- initially rejects supernatural explanations
- adapts when evidence becomes undeniable
- **must make active decisions**
- defining behavior: refuses false binaries

## Older-him

- knows more than the protagonist
- knows less than he pretends
- is genuinely trying to prevent something
- manipulates because he believes the outcome justifies it
- can be wrong because his memory belongs to another sequence
- is experienced, **not omniscient**

## Other him / double

Do not collapse the Track 4 double into older-him. Multiple concurrent versions must remain possible.

---

# 6. Music production status

All track folders exist under `tracks/`.

| # | Track | Lyrics | Suno style | Artwork | MP3 |
|---|---|---|---|---|---|
| 1 | The Last Normal Night | yes | yes | yes | **yes** |
| 2 | The Wrong Side of Morning | yes | yes | yes | **yes** |
| 3 | Frequency Three | yes | yes | yes | **yes** |
| 4 | The Man in My Shadow | yes | yes | yes | no |
| 5 | The Lake Remembers | yes | yes | yes | no |
| 6 | Don’t Answer Yourself | yes | yes | yes | no |
| 7 | I Already Did This | yes | yes | yes | no |
| 8 | Welcome Back | yes | yes | yes | no |
| 9 | The Door Was Never for Me | yes | yes | yes | no |
| 10 | Midnight Knows My Name | yes | yes | yes | no |

## Verified committed audio

- Track 1: `01-the-last-normal-night.mp3` — 7,428,070 bytes
- Track 2: `02-the-wrong-side-of-morning.mp3` — 7,567,705 bytes
- Track 3: `03-frequency-three.mp3` — 8,334,963 bytes

These replaced earlier accidental 2-byte placeholder files.

## Suno rule

Every Suno-facing prompt must be self-contained. Suno does not know what “Track 1” or “the previous track” means.

### Known cleanup still worth doing

Track 2 currently contains non-standalone Suno wording:

- style prompt says `Continue Track 1’s musical DNA...`
- lyric header says `Track 1 groove slightly wrong`

Before regenerating Track 2, rewrite those phrases into explicit sonic ingredients.

Track 3 style was already corrected into a fully standalone Suno prompt.

## Optional standardization gap

`brief.md` exists for Tracks 2–3, but not consistently for every track. The story bible carries the needed canon, so this is not blocking, but adding briefs for Tracks 1 and 4–10 would make the track folders more uniform.

---

# 7. Web player / landing page

Root file: `index.html`

CNAME:

`lastnormalnight.aerovista.us`

The player currently exposes all 10 tracks and includes:

- full 10-track playlist
- Act I / II / III grouping
- dynamic track title / chapter / description
- previous / next
- ±10 second seek
- scrubber
- volume
- keyboard controls
- local MP3 fallback
- auto-advance behavior
- expected static file paths for Tracks 1–10

## Current audio state

Tracks 1–3 should be available from the committed MP3 paths. Tracks 4–10 are awaiting audio.

## Player hardening TODO

The current availability approach was designed around file presence. Earlier 2-byte placeholder MP3s proved that “file exists” is not enough.

A future player pass should reject implausibly small audio payloads or rely on successful audio metadata / can-play validation before marking a track ready.

Do not claim that this size-aware hardening is already implemented.

---

# 8. Album artwork and merch

## Album / track artwork

Track artwork is committed as a PNG in every track folder, Tracks 1–10.

These images are part of the visual language that the comic series should echo without copying blindly.

## Clothing / swag

A clothing line, hoodie, T-shirt and swag direction was explored in the conversation.

**Current repo status:** no merch source package was verified during this handoff audit.

Treat merch as concept-stage / conversation-stage until dedicated assets and production files are committed. A clean future structure would be:

```text
merch/
  artwork/
  mockups/
  print-files/
  prompts/
```

---

# 9. Comic series format

Canonical series concept:

- **10 issues**
- one issue per album track
- target **24–28 story pages per issue**
- roughly **250–280 pages** collected
- mature prestige horror / sci-fi noir
- grimy, grounded, physical North Idaho atmosphere
- adult language allowed
- violence only when earned
- psychological / identity / existential horror over gore

The music describes how the world feels. The comic shows what physically changed.

---

# 10. Canonical comic page size

## Standard page

- trim: **6.625 × 10.25 in**
- bleed: **0.125 in** each side
- working canvas: **6.875 × 10.5 in**
- master: **2063 × 3150 px @ 300 DPI**
- trim-only pixel reference: **1988 × 3075 px**

## Safe area

- top / bottom / outside: 0.25 in minimum
- binding side: 0.375 in

## Double-page spread

- trim: **13.25 × 10.25 in**
- full bleed: **13.5 × 10.5 in**
- master: **4050 × 3150 px @ 300 DPI**

Critical faces, clues, doorway geometry, or lettering must not sit on the center fold.

## Lettering rule

Final story text, signs, clocks, phone messages, radio readouts and credits are added during layout. Do not trust generated text for production masters.

---

# 11. CDA location lock

The fractured world is the **same Coeur d’Alene**, not a fantasy replacement city.

Keep coherent:

- lake position and shoreline
- Tubbs Hill
- downtown grid
- Sherman Avenue
- McEuen Park
- resort / marina relationship
- waterfront approaches
- major street orientation
- recognizable landmark massing

The audience should recognize the place first and notice the contradiction second.

> **One wrong detail in a real place is stronger than a completely fictional skyline.**

Good altered-world contradictions include:

- one building where an empty lot should be
- one missing building
- an older facade with impossible history
- a road subtly too long
- a sign pointing wrong
- one landmark renamed but still in the correct place
- a clock disagreeing with nearby time
- mathematically strange traffic / pedestrian behavior

Do not casually relocate Tubbs Hill, the lake, resort, marina, McEuen Park, or downtown streets.

---

# 12. Locked / working visual references

## Protagonist

Working reference is strong enough to preserve:

- early-30s appearance
- practical dark layers
- rough dark hair
- stubble
- grounded, tired but observant expression
- believable adult rather than superhero anatomy

## Truck

Treat the dark, worn older pickup as the physical anchor.

Important:

- generated `11:59` license plate is **not canon**
- generated badges are not story-critical
- interior wear / cracked plastic / stains / radio / spare-key area should stay consistent

## White sedan

Recurring older white sedan.

Key visual continuity:

- recognizable left-rear damage / dent
- one dimmer rear light
- ordinary enough to be ignored at first

## Doorway

- precise rectangular geometry
- cold white perimeter
- should feel physically impossible because it is too exact
- not a swirling fantasy portal

## CDA references

Real user-supplied map, aerial, street, resort, marina, park, storefront and road references override generated environment boards.

### Page 7 current location decision

The latest working choice for Page 7 is the **real CDA Corner Store** reference supplied by the user, including its authentic exterior / store interior language.

Do **not** return to the accidental Fleet Feet exterior + convenience-store interior mismatch.

The clerk scene must remain mundane. The only wrong thing is that the clerk recognizes him.

---

# 13. EP1 story-page map — canonical

EP1 has exactly **24 story pages**.

## Pages 1–4 — Normality starts to fail

### Page 1
Normal CDA opening. Establish place, mood and protagonist.

### Page 2
Adult social normality / bar life. Nothing supernatural should dominate.

### Page 3
Truck / town texture; seed the recurring white sedan quietly.

### Page 4
First dismissible anomaly: dog barks, then the world becomes too still.

## Pages 5–8 — Dismissible becomes personal

### Page 5
Streetlight tracks him: on → off directly above → on behind. Phone bars shift `1 → 5 → none`. Unseen whisper: `Don’t go home.`

### Page 6
Sherman feels subtly stretched. Same dented white sedan passes twice from the same direction. Digital display reverses `11:58 → 11:57`. **Do not use 11:59 yet.**

### Page 7
Convenience-store / CDA Corner Store recognition scene.

- protagonist buys water / gum
- clerk recognizes him immediately: `You picked a good one.`
- protagonist: `Good what?`
- clerk, almost relieved rather than sinister: `Have a good night.`

### Page 8
He exits to an unnaturally empty Sherman. Lake is impossibly flat. Phone says `NO SERVICE`. A notification flashes: `WELCOME BACK`, then disappears. `What the fuck was that?`

## Pages 9–13 — Synchronization and threshold

### Page 9
White sedan idles ahead. Dent / dim tail light confirms same car. First traffic signal turns red, then every signal clicks red toward the lake. Sedan disappears without being shown leaving. Protagonist: `Nope.`

### Page 10
First true **11:59 convergence**:

1. truck clock = 11:59
2. phone = 11:59
3. store clock = 11:59
4. municipal / bank sign = 11:59
5. reaction: `Okay.` / `That’s not funny.`

### Page 11
Time refuses to progress:

- dashboard still 11:59
- phone still 11:59
- engine revs, clock unchanged
- rearview reflection subtly misaligns
- passenger glass creaks
- pressure fills the cab

Caption: `Eleven fifty-nine.`

### Page 12
Reality proximity becomes physical:

- truck stopped in empty intersection
- shadow points in impossible direction
- first wooden-flute growl appears as a thin pressure/waveform distortion through glass, puddles, dashboard plastic and lake reflection
- protagonist: `What the hell—`

No rupture yet.

### Page 13
Involuntary countdown:

`10 → 9/8 → 7/6 → 5 → 4/3 → 2`

An unseen source says:

`One.`

Do not reveal the speaker.

## Pages 14–15 — Midnight rupture

One continuous full-bleed 4050 × 3150 composition.

CDA remains recognizable but misregisters against itself by inches / seconds:

- hard vertical white tear
- truck in two almost-identical positions
- doubled signage
- reflections from different moments
- lake reflects a sky not above it
- protagonist left of center, bracing rather than flying

**No dialogue. Absolute silence is the point.**

## Pages 16–19 — The altered world indexes him

### Page 16
He wakes beside the truck. Same intersection, mountains and concrete. Street is subtly wrong. One impossible building / one older facade / odd skyline spacing. Faint moon ring.

`Opened my eyes.`  
`Same damn street.`  
`Almost.`

### Page 17
Closed storefront reflections may contain indistinct watchers, but they remain plausibly human. Truck engine starts **before the key enters**. Key remains visibly in his hand. Radio wakes by itself to `03` / Frequency Three.

`No.`  
`RRRRMM`  
`KSSSSHHH`

### Page 18
Static / breathing waveform. Older-sounding familiar male voice:

`You finally made it.`

Protagonist:

`Who is this?`

Radio cuts out. No second answer.

### Page 19
He drives through altered-history CDA: new building in old empty lot, collapsed familiar business, wrong year flickers too fast to read. Instead of running, he laughs once.

`Shit.`  
`Of course.`

`I should’ve run.`  
`Instead I laughed.`

## Pages 20–24 — The doorway and the choice

### Page 20
Electrical tear opens behind him, widens into canonical rectangular doorway. Through it is the exact old-world night: friends, bar, truck, warm neon, movement, life.

Caption:

`Home.`

### Page 21
He approaches the threshold. Warm old-world light falls across his boots. Familiar friend laughs. His old truck is visible. One foot could cross.

Caption:

`All I had to do was walk back through.`

### Page 22
One step. Two. He stops. Looks at altered CDA, then at the old world. He deliberately steps **sideways** away from the threshold.

`Nah.`

This must read as a decision, not paralysis.

### Page 23
Doorway shivers and collapses inward to a line, then disappears. Wind returns. Dawn begins from the wrong direction.

`TCHK`

Quietly:

`I ain’t going back.`

### Page 24
Full-page end splash.

Wrong-side morning. Familiar-but-wrong CDA. Fading moon halo. Phone vibrates.

Signal: `FULL`

One message, no sender:

`WELCOME HOME`

Protagonist, small:

`Figures.`

**END ISSUE #1**

---

# 14. EP1 production assets already complete

Under `comic/issues/01-the-last-normal-night/`:

- `script.md` — complete
- `art-prompts.md` — complete prompt deck
- `focus-regions.json` — authored Rack focus map
- `PAGE_ASSEMBLY_STANDARD.md` — controlled assembly workflow
- `PAGE_ART_QA.md` — rejection / acceptance rules
- `ASSET_MANIFEST.md` — asset status and authority rules
- `layouts/` — all story pages + rupture spread
- `storyboards/` — all 24 pages + rupture spread
- `storyboards/README.md` — production index

The storyboard index marks every story page **READY FOR ART**, with Pages 14–15 **READY FOR SPREAD ART**.

---

# 15. Current final-art status — very important

## Repository reality

As of this handoff audit, `comic/issues/01-the-last-normal-night/pages/` does **not** exist in the repository.

Therefore:

> **There are currently no repo-verified final flattened EP1 story-page masters.**

Do not confuse storyboard completeness with final comic art completion.

## Page 7

The user has been manually refining a Page 7 candidate, including restoring missing header / footer and text from an earlier version and correcting the location to CDA Corner Store.

Working judgment: visually promising / likely closest to first final page.

**Status until uploaded and QA’d:** candidate, not repo-final.

## Page 8

A Page 8 candidate from the current conversation followed the intended arc more closely than the later generations.

**Status until uploaded and QA’d:** candidate, not repo-final.

## Pages 9–16

Multiple free-form generations were attempted.

Problems included:

- normal-day / productivity montages instead of story beats
- wrong panel counts
- scenes happening at home instead of the street / truck
- reused `WELCOME BACK` at the wrong time
- `Time Circuit` branding
- `The Signal` branding
- invented narration
- invented entities / shadow figures
- combined multi-page boards instead of actual pages

One later Pages 9–16 sequence board finally captured much of the correct **arc**:

white sedan → 11:59 → pressure → countdown → rupture → altered CDA

but it is still only an **arc-control / visual reference board**, not final page art.

**Final status:** reject all current Pages 9–16 generated page outputs as publishable masters. Rebuild from canonical storyboards.

## Pages 17–24

A later sequence board drifted into a cassette / `THE SIGNAL` plot that does not exist in canon.

**Final status:** reject as story canon and publishable art.

### Hard branding rule

The project is:

**EchoStory — The Last Normal Night**

Do not allow image generation to rename it:

- not `Time Circuit`
- not `The Signal`
- not `A Coeur d’Alene Story` as replacement title

Those were generation errors, not canon revisions.

---

# 16. What we learned about image generation

The image model has repeatedly anchored to prior visual themes and then rewritten story content even when given explicit page instructions.

## Do not resume with whole-page free-form generation

For final production use this pipeline:

1. open canonical storyboard
2. identify exact panel rectangle
3. generate **one textless panel plate at a time**
4. use locked protagonist / object / location references
5. reject extra characters, text, effects, symbols or plot beats
6. place plate into `layouts/pXX.svg`
7. add final lettering manually / programmatically during page assembly
8. compare to `script.md`
9. compare to `focus-regions.json`
10. export 2063 × 3150 final master

Only Pages 14–15 should be generated / painted as a unified spread composition.

## Panel prompt rule

A final-art prompt should describe only the requested panel:

- subject
- action
- framing
- real location reference
- lighting / style
- continuity objects
- explicit exclusions

Do **not** ask the image model to understand the full page arc while also composing the finished layout.

## Text rule

Keep generated panel art textless whenever story text matters.

Add:

- dialogue
- captions
- clocks
- phone screens
- radio display
- signs with story meaning
- page headers / footers
- issue branding

after the artwork is placed.

---

# 17. Page 7 visual benchmark

Page 7 remains the best page to establish the final production style because its story wrongness is almost entirely social.

## Required panels

1. real / plausible CDA Corner Store establishing shot; protagonist buys water or gum
2. young clerk recognizes him immediately
3. protagonist pauses: `Good what?`
4. normal two-shot; clerk seems almost relieved: `Have a good night.`

## Forbidden Page 7 additions

- portal
- shadow figure
- white-sedan subplot
- note
- surveillance character
- supernatural lighting
- sinister grin
- generated horror glitching

The location is ordinary. The recognition is wrong.

Once Page 7 is fully assembled and approved, its typography, header/footer, gutters, color treatment and character rendering should become the EP1 page-style benchmark.

---

# 18. Recommended next production sequence

## Phase A — recover current good work

1. Upload / commit the user-edited Page 7 candidate if it is not already in the repo.
2. Upload / commit the Page 8 candidate if it is being kept.
3. QA each against:
   - `script.md`
   - storyboard
   - layout
   - CDA location lock
   - focus regions
4. Update `ASSET_MANIFEST.md` with explicit status: candidate / approved / rejected.
5. Create the final `pages/` directory only when the first page genuinely passes QA.

## Phase B — rebuild Page 9 properly

Do not use the incorrect full-page generated versions.

Generate / source five textless plates:

- P09.1 sedan idling ahead
- P09.2 dent / dim tail-light confirmation
- P09.3 first signal turns red
- P09.4 signals cascade red toward lake
- P09.5 same street, sedan gone; protagonist stops / turns back toward truck

Assemble into `layouts/p09.svg`, then letter:

- `CLICK`
- `CLICK. CLICK. CLICK. CLICK.`
- `Nope.`

## Phase C — Pages 10–13

Continue the same controlled method:

- P10 — 11:59 convergence
- P11 — time stuck / pressure
- P12 — impossible shadow / wooden-flute proximity
- P13 — involuntary countdown

These pages must be especially strict because reveal order matters.

## Phase D — Pages 14–15 rupture

Create one 4050 × 3150 spread master.

The rupture should distort timing/alignment **without replacing CDA with fantasy architecture**.

## Phase E — Pages 16–24

Proceed sequentially from the existing storyboards:

altered CDA → truck self-start → Frequency Three → altered history → doorway → return temptation → sideways choice → collapse → `WELCOME HOME`.

## Phase F — rebuild Pages 1–6

After the Page 7–24 visual pipeline is stable, return to Pages 1–6 and rebuild them from their locked storyboards rather than relying on early concept pages.

## Phase G — final QA / Rack

- full issue read in order
- compare every page against script
- check character / truck / sedan / doorway continuity
- verify CDA geography
- verify motif timing
- confirm page dimensions / safe areas
- confirm Rack focus crops
- export publishing set
- copy **finished pages only** to `aerovista-us/the-rack`

---

# 19. Rack publishing rules

Production repo remains:

`aerovista-us/The-Last-Normal-Night`

Publishing repo remains:

`aerovista-us/the-rack`

**Build for print first. Publish to The Rack second.**

The Rack is not the source of truth for scripts, prompts, or continuity.

Final Rack assets should be flattened full page masters at **2063 × 3150**.

Rack focus regions provide guided/mobile reading without replacing the full print page as the canonical asset.

The optional motion insert belongs after story Page 15 and before Page 16:

```text
motion/motion-01-midnight-rupture.mp4
motion/motion-01-midnight-rupture-poster.jpg
```

The motion beat should end before showing the post-rupture world; Page 16 owns that reveal.

---

# 20. EP1 publishing order

Recommended sequence:

```text
00-cover-front.png
01-inside-front.png
02-p01.png
03-p02.png
...
15-p14.png
16-p15.png
motion/motion-01-midnight-rupture.mp4   # optional
17-p16.png
...
25-p24.png
26-cover-back.png
```

Story count remains 24 pages. Covers and inside-front matter do not change the story count.

---

# 21. QA checklist for every final page

A page is not final just because it looks impressive.

Before approval verify:

- [ ] exact scripted panel count
- [ ] exact action / story beat
- [ ] reveal order preserved
- [ ] protagonist face / age / clothing continuity
- [ ] truck continuity where present
- [ ] white sedan continuity where present
- [ ] doorway geometry continuity where present
- [ ] real CDA geography plausible
- [ ] no invented character / note / subplot
- [ ] no premature 11:59 / Frequency Three / doorway / wooden-flute motif
- [ ] no generated story text accepted accidentally
- [ ] lettering-safe negative space
- [ ] page header/footer/branding consistent
- [ ] EchoStory branding correct
- [ ] 2063 × 3150 master exported
- [ ] safe area respected
- [ ] Rack focus regions still center faces / action / lettering correctly

For Pages 14–15 also verify 4050 × 3150 spread master and gutter caution.

---

# 22. Known cleanup / risk list

## Music

- Tracks 4–10 still need final MP3 audio uploads.
- Track 2 Suno-facing references to `Track 1` should be rewritten into standalone wording before future generation.
- Optional: add missing `brief.md` files for consistency.

## Player

- implement stronger MP3 validity detection so tiny placeholders cannot appear `ready`

## Visual assets

- real user-supplied CDA location references should eventually be organized into dedicated folders such as:

```text
comic/reference/real-cda/
comic/reference/character/
comic/reference/vehicles/
comic/reference/doorway/
```

- several generated images currently sit at repo root / issue root with timestamp-heavy names
- duplicate binaries should eventually be cleaned up
- update `ASSET_MANIFEST.md` whenever a new page image is uploaded

## Comic finals

- no repo-verified `pages/` master set yet
- Page 7 / Page 8 candidates need upload + QA before calling them final
- Pages 9 onward must be rebuilt from storyboards, not promoted from recent sequence boards

## Merch

- merch concepts exist in conversation history but no verified production-ready repo package was found in this audit

---

# 23. Do-not-do list for the next session

Do not:

- redesign the story from generated art
- call recent 9–24 contact sheets final pages
- use `Time Circuit` branding
- use `The Signal` as this comic’s title
- invent a cassette storyline
- add a ghost / monster simply to make a panel scary
- move major CDA geography
- show 11:59 before the script allows it
- turn wooden-flute effects into random horror atmosphere
- turn the doorway into a swirling magic portal
- bake critical lettering into generated art
- let a good-looking page override the canonical panel count
- skip the protagonist’s active choices

---

# 24. Exact resume instructions for a new thread

When reopening this project, start by reading in this order:

1. `README.md`
2. `docs/STORY_BIBLE.md`
3. `docs/CONTINUITY.md`
4. `docs/RULES.md`
5. `docs/COMIC_SERIES_OUTLINE.md`
6. `docs/COMIC_PRODUCTION_SPEC.md`
7. `docs/Rack-Integration-Rules.MD`
8. this handoff
9. `comic/issues/01-the-last-normal-night/README.md`
10. `comic/issues/01-the-last-normal-night/script.md`
11. `comic/issues/01-the-last-normal-night/PAGE_ASSEMBLY_STANDARD.md`
12. `comic/issues/01-the-last-normal-night/PAGE_ART_QA.md`
13. `comic/issues/01-the-last-normal-night/ASSET_MANIFEST.md`
14. `comic/reference/CDA_LOCATION_LOCK.md`
15. target page storyboard + target page layout

Then inspect whether user-edited Page 7 and Page 8 have been committed.

### If Page 7 / Page 8 are present and pass QA

Resume at **Page 9 controlled assembly**.

### If they are not present

Ask the user to upload the versions they are keeping before recreating them.

### Critical resume instruction

**Do not resume by asking an image model to create Page 9 as a complete page from scratch.**

Generate P09.1–P09.5 as separate textless plates, assemble them in the locked layout, then letter the page.

That is the current safest path to a finished issue.

---

# 25. Definition of EP1 complete

EP1 is complete only when:

1. all 24 final story page masters exist
2. Pages 14–15 derive from one approved 4050 × 3150 rupture composition
3. front / inside-front / back cover assets exist
4. final lettering is clean and human-controlled
5. every page passes story / continuity / geography QA
6. Rack focus regions have been checked against final art
7. the complete issue reads correctly in sequence
8. the print-ready archive is preserved in this repo
9. finished publishing assets are deployed to The Rack
10. the issue still ends exactly on:

**WELCOME HOME**

with the protagonist having **chosen to stay**.

---

# 26. Bottom line

The project is not stuck on story development.

The album canon is established. The 10-track narrative exists. The first three audio tracks are in place. Track art is in place. The comic series architecture is established. EP1 is fully scripted, laid out, storyboarded and Rack-preflighted.

The remaining EP1 bottleneck is **disciplined final illustration / assembly**, not writing.

The correct next move is to turn the locked storyboards into finished pages without allowing generative art to rewrite them.

**Resume point:** recover / approve Page 7 and Page 8, then build Page 9 from five controlled textless panel plates.
