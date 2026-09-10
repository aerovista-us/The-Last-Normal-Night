# EchoStory: The Last Normal Night
## Comic Production Specification

This file defines the canonical physical and digital page format for the EchoStory comic series. All issue scripts, page layouts, image prompts, splash pages, covers, and collected-edition assets should reference this specification.

---

# Canonical Page Size

## Standard interior page

**US comic trim size:** 6.625 × 10.25 inches

This is the final visible page size after trimming.

### Full-bleed working canvas

Add **0.125 inch bleed on all four sides**.

**Working canvas:** 6.875 × 10.5 inches

At 300 DPI this is approximately:

**2063 × 3150 pixels**

Use this full-bleed canvas for painted artwork, generated artwork, textures, and any image intended to reach the edge of the printed page.

### Trim-size pixel reference

At 300 DPI:

**1988 × 3075 pixels**

Do not use the trim-size canvas for edge-to-edge art; use the full-bleed canvas instead.

---

# Safe Area

Keep all critical text, faces, speech balloons, captions, logos, and essential story information inside the safe area.

Recommended minimum safe margins from the trim edge:

- Top: 0.25 in
- Bottom: 0.25 in
- Outside edge: 0.25 in
- Inside / binding edge: 0.375 in

The larger inside margin protects the collected graphic novel edition if perfect binding is used later.

Nonessential atmospheric art may extend through the trim and into the bleed.

---

# Double-Page Spreads

A two-page spread uses two standard pages side by side.

## Trimmed spread

**13.25 × 10.25 inches**

## Full-bleed spread canvas

**13.5 × 10.5 inches**

At 300 DPI:

**4050 × 3150 pixels**

Do not place faces, lettering, doorway edges, clues, or other critical visual information directly across the center gutter.

For important spread compositions, treat roughly **0.375 inch on either side of the center fold** as a caution zone.

---

# Cover Format

Individual issue covers should use the same base trim proportion as the interior unless a printer-specific template later overrides it.

## Front cover art working size

**6.875 × 10.5 inches including bleed**

**2063 × 3150 px at 300 DPI**

Keep issue title, EchoStory branding, issue number, and major faces or symbols inside the safe area.

Full wraparound covers will require a printer-specific spine width once final page count and paper stock are known. Do not permanently bake a spine width into artwork before printer specifications are selected.

---

# Resolution and Color

## Artwork

- Target resolution: **300 DPI minimum at final print size**
- Painted / generated art: 300 DPI final
- Line art may be retained at higher resolution when available
- Avoid enlarging small raster art beyond its native useful resolution

## Lettering and logos

Prefer vector lettering and vector logos whenever possible.

Do not rely on AI-generated text for final speech balloons, captions, signs that carry story information, credits, page numbers, or cover typography. Generate the image composition first and add final typography during layout.

## Color workflow

AI-generated and digital concept art may begin in RGB.

Master working art can remain RGB during illustration and compositing, but print-ready files should be converted using the selected printer's required CMYK profile during prepress.

Do not perform destructive CMYK conversion early in the art-development process.

---

# Digital Edition

The digital edition should preserve the same page composition and aspect ratio as print.

Recommended master digital page:

**2063 × 3150 px**

Smaller distribution versions may be derived from the master.

Never compose the print and digital editions independently unless a later platform specifically requires guided-view panel crops.

---

# AI Image Generation Standard

When generating a complete comic page, prompts should explicitly state:

**"Vertical US comic page composition, 6.625 × 10.25 inch trim proportion, full-bleed artwork with 0.125 inch bleed, compose all critical characters and story information safely inside the trim area."**

Because image-generation tools may not output the exact print dimensions, generate at the closest available vertical aspect ratio and crop / extend into the canonical **6.875 × 10.5 inch full-bleed canvas** during layout.

For individual panels, generate at sufficient resolution for the panel's final physical size rather than forcing every panel to full-page dimensions.

Final lettering should be added after the artwork is placed on the page.

---

# Page Script Header Standard

Every scripted comic page should begin with a production header similar to:

```text
PAGE 07 — 6.625 × 10.25 in trim
FULL-BLEED CANVAS: 6.875 × 10.5 in / 2063 × 3150 px @ 300 DPI
PANELS: 5
BLEED: Yes / No
SPECIAL: none
```

For a splash:

```text
PAGE 14 — FULL-PAGE SPLASH
TRIM: 6.625 × 10.25 in
CANVAS: 6.875 × 10.5 in / 2063 × 3150 px @ 300 DPI
BLEED: full bleed
```

For a spread:

```text
PAGES 14–15 — DOUBLE-PAGE SPREAD
TRIM: 13.25 × 10.25 in
CANVAS: 13.5 × 10.5 in / 4050 × 3150 px @ 300 DPI
BLEED: full bleed
GUTTER CAUTION: keep critical content away from center fold
```

---

# Layout Philosophy

EchoStory should not feel like a conventional dense superhero comic.

Use negative space, large atmospheric panels, occasional silent pages, full-page splashes, and controlled cinematic pacing.

Typical pages may use **3–6 panels**, but panel count should follow story tension rather than a rigid grid.

Recommended uses:

- 1 panel: revelation, rupture, dread, major environment
- 2–3 panels: slow cinematic tension
- 4–5 panels: normal dialogue / investigation
- 6–8 panels: fractured memory, radio timing, escalating unease
- irregular repeated grids: primarily Issue #7, where the comic itself begins malfunctioning

The page size is fixed. The storytelling rhythm is not.

---

# Canonical Production Rule

Unless a future printer requires a different template, all EchoStory comic development should assume:

**6.625 × 10.25 in trim**  
**6.875 × 10.5 in full bleed**  
**2063 × 3150 px at 300 DPI**

Every full page script and every page-level image prompt should include these dimensions.
