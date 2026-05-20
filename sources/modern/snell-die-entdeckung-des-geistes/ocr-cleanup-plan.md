# Snell OCR Cleanup Plan

**Status:** Active cleanup plan. This lines up the heroic pass; it does not
pretend the current OCR is clean.

## Problem

The current Snell scaffold is useful for chapter-scale access, but the OCR is
not reliable enough for close work. The visible problems are:

- page furniture and copyright footer lines embedded in chapters
- form-feed page breaks
- line-wrapped prose and line-break hyphenation
- German OCR substitutions that affect meaning, such as `Phüologe`
- Greek quotations rendered into mixed Latin, symbol, and HTML-like garbage
- scaffold drift: the README still names a `source/full/` text and a local
  splitter location that are not present inside this source folder

## Layers

Use three layers rather than trying to make the raw OCR carry every job:

1. `source/raw/`: extraction witness. Keep as-is except for a deliberate
   re-extraction.
2. `source/normalized/`: generated readable base from
   `tools/normalize_snell_ocr.py`.
3. future checked files: manual chapter repairs, only when a chapter earns
   close-reading pressure.

The normalized layer is a base camp, not the summit.

## Heroic Pass Sequence

### Phase 0 — Automated base

Run:

```bash
python3 tools/normalize_snell_ocr.py
```

This regenerates `source/normalized/*.txt` and
`source/normalized/manifest.yaml`.

### Phase 1 — PSF II overlap first

Clean the chapters that actually matter for the live Cassirer/Snell seam:

1. `011-die-auffassung-des-menschen-bei-homer`
2. `012-der-glaube-an-die-olympischen-goetter`
3. `013-die-welt-der-goetter-bei-hesiod`
4. `014-das-erwachen-der-persoenlichkeit-in-der-fruehgriechischen-lyrik`
5. `016-mythos-und-wirklichkeit-in-der-griechischen-tragoedie`
6. `018-menschliches-und-goettliches-wissen`
7. `019-zur-entstehung-des-geschichtlichen-bewusstseins`
8. `015-pindars-hymnos-auf-zeus`
9. `020-mahnung-zur-tugend`

This order follows
`../../../00-Notes/working-syntheses/2026-05-19-snell-psf-ii-intersection-and-gaps.md`.

### Phase 2 — Greek repair

Do not infer Greek from the Snell OCR. Restore Greek passages from the Greek
substrate shelves where possible:

- Homer / Homeric Hymns / Hesiod / Pindar / tragedy:
  `../../greek/mythic-greek-cassirer-snell-substrate/`
- Plato myths:
  `../../greek/plato-dialogue-pack-cassirer-substrate/`
- Presocratic and mystical surfaces:
  `../../greek/presocratic-atomist-doxography-cassirer-substrate/`

If a Greek passage cannot be restored confidently, mark it explicitly as an
unresolved Greek OCR repair rather than smoothing it into plausible nonsense.

### Phase 3 — Back matter

Clean `030-anmerkungen` and `031-indices` after the chapters they support.
The notes and index are valuable, but they are most useful once the referenced
chapter surfaces are readable.

### Phase 4 — Non-PSF II Snell

Clean the remaining chapters on demand:

- `017` Aristophanes
- `021-022` comparison / scientific concept formation
- `023-027` path symbol, humanity, Callimachus, Arcadia, theory/practice
- `028` afterword

## Checks

Before treating a chapter as clean:

- run `rg "Phü|phü|Büd|Teü|weü|#|&[A-Za-z]"` against the chapter
- inspect the chapter's `manifest.yaml` suspect counts
- compare the opening, one middle page, and the close against a PDF or scan
- verify that Greek quotations are restored from a source witness or left
  visibly unresolved

## Current Judgment

The current best working surface is `source/normalized/`, but the authority
for exact reading remains the scan/PDF. Until the source PDF is restored to the
checkout or a stable scan witness is recorded, this should remain a cleanup
campaign rather than a normalized source campaign.
