# The Rack Integration Rules
## EchoStory / The Last Normal Night
## Canonical publishing rules for comic production + Rack deployment

This document defines the rules for how **The Last Normal Night** comic series should be produced, prepared, and published for **The Rack**.

These rules exist so that:
- comic production stays consistent
- print and digital outputs share one canonical source
- page-level scripts can flow directly into The Rack reader
- mobile panel reading works intentionally, not accidentally
- publishing stays simple and repeatable

---

## 1. Core principle

**Build for print first. Publish to The Rack second.**

The print-ready comic page is the master asset.

The Rack is a publishing/delivery layer for finished pages, covers, and optional motion moments.  
It is **not** the master source for scripts, prompts, continuity, or working production files.

---

## 2. Repo separation rule

### Production repo
The canonical production source remains in:

- `aerovista-us/The-Last-Normal-Night`

This repo holds:
- story bible
- continuity
- character rules
- comic scripts
- page prompts
- page layouts
- focus region definitions
- issue production files
- album/music canon

### Publishing repo
The Rack remains the publishing/delivery system:

- `aerovista-us/the-rack`

This repo holds:
- `rack.json`
- finished published page images
- optional motion clips
- issue covers
- issue-level metadata
- public reader experience

**Do not move source comic development into The Rack repo.**

---

## 3. Canonical page size rule

All comic issues must use the locked production spec.

### Standard single page
- **Trim size:** 6.625 × 10.25 in
- **Full bleed size:** 6.875 × 10.5 in
- **Full-bleed canvas at 300 DPI:** 2063 × 3150 px
- **Trim-only reference at 300 DPI:** 1988 × 3075 px

### Bleed / safe rules
- **Bleed:** 0.125 in on all sides
- **General safe area:** 0.25 in
- **Binding-side safe area:** 0.375 in

### Standard spread
- **Double-page spread full bleed:** 13.5 × 10.5 in
- **Spread canvas at 300 DPI:** 4050 × 3150 px

### Mandatory rule
Every full script page, layout page, and page prompt must explicitly include:
- trim size
- canvas size
- bleed status
- page type
- panel count

---

## 4. Print-first asset rule

The canonical visual master is the **finished full comic page**, not panel crops.

That means:
- generate or assemble the full page at production size
- add lettering during layout
- preserve full page composition
- export a final flattened page image for publication

The same finished page is then used for:
- print
- archive/master delivery
- The Rack normal reading
- The Rack panel-focus reading

---

## 5. Rack format rule

Every EchoStory issue published to The Rack must explicitly declare page format in the book object.

Use:

```json
"format": {
  "width": 2063,
  "height": 3150
}
