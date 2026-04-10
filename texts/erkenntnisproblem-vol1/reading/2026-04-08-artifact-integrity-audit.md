# 2026-04-08 Artifact Integrity Audit

This note fixes the status of the completed `Erkenntnisproblem` Volume I artifacts after the English layer drifted from translation toward gloss during the late run.

It is a routing and honesty note, not a second journal.

## Closure State

- Volume I is structurally complete through printed page `601`
- the advertisement pages after printed `601` were not used
- the canonical working run now ends at Part `149`
- the final source windows run through `source/raw/150-*` and `source/normalized/150-*`

## Source-Backed and Aligned

- `source/raw/*.txt` through `150`:
  direct extraction windows for the completed run
- `source/normalized/*.txt` through `150`:
  cleaned source windows aligned with the completed run
- `parts/*.md` through `149`:
  source-backed working tranche files for the whole volume
- `source/page-map.yaml` through `149`:
  aligned with the completed run and parse-clean
- `source/viewer-index.json`:
  derived export parses cleanly and currently serializes `149` parts and `49` glossary entries

## Quality Zones

The English and German layers do not have the same boundary behavior.

### Working standard for the German layer

For Volume I, the meaningful completeness standard is `main-prose full density`, not raw line-count equality and not naive character-ratio comparison against the whole normalized source window.

That means:

- the corrected German should carry Cassirer's own running prose for the tranche
- load-bearing quotations and formulas should be retained where they do argumentative work
- long documentary footnotes, original-language apparatus, and source-window spillover into the next heading do not by themselves have to be mirrored at equal density inside the part file

Low visible line counts are therefore not direct evidence of a thin tranche. In practice, late and early outliers alike can be pulled down by:

- long inline footnote quotations in the normalized window
- source windows that include the opening of the next section or chapter
- more compact paragraphing in the part file even when the prose spine is present

Representative low-ratio parts manually rechecked under this stricter standard include `9`, `11`, `28`, `43`, and `54`. They read as footnote- or spillover-heavy windows rather than as missing-prose failures.

### English layer

- Parts `1-62`:
  full draft-translation zone
- Parts `63-81`:
  still translation-grade, but with `Working Commentary` separated from the English block
- Parts `82-149`:
  repaired draft-translation zone; the English layer again behaves as working translation

There is no remaining English-gloss zone in Volume I. The whole English layer is now back at draft-translation status, though the late run remains working translation rather than publication-finished prose.

### German layer

- Parts `1-81`:
  strongest corrected-source zone; these are closest to full corrected tranche bodies
- Parts `82-133`:
  now close again to full corrected-source bodies; the late Descartes, Pascal, and logic-opening runs have been locally restored through the Geulincx opening
- Parts `134-149`:
  no longer behave like a single late-compression band; the remaining debt is pocketed
- Parts `134-138`:
  largely recovered; `136` is comparatively thin, but that now appears to be driven mainly by the long Burthogge footnote quotation rather than a missing prose bridge
- Parts `139-142`:
  source-backed and usable, but still thinner than early full-body standard
- Parts `143-144`:
  no longer a broken local pocket, but still the thinnest citation-heavy pair in the Malebranche / Arnauld run; `144` remains the weaker tranche
- Part `145`:
  materially improved; no longer the first local priority
- Parts `146-149`:
  materially recovered; `147` and `149` are no longer the primary German-completeness problem

## Derived but Current

- `journal.md` through Part `149`:
  current cross-batch notebook for findings actually earned from the text
- `reading/close-reading-ledger.md` through Part `149`:
  local holding surface for tranche findings
- `session-ledger.yaml` through Part `149`:
  valid re-entry surface for post-volume continuation
- `interpretive-notes.md`:
  explicitly nonbinding review/extrapolation surface; useful prompts, not source authority

## What Is Trustworthy

With the English repair completed, the working scaffold remains reliable for:

- argument sequence
- tranche boundaries
- section anchors
- re-entry and continuation
- cross-batch pressure tracking

In practice, that means the following can be treated as working-complete for Volume I:

- source windows
- part structure
- journal
- close-reading ledger
- session ledger
- page-map

## What Is Not Complete

- Parts `134-149` still contain local German completeness debt, but it now appears mostly as uneven density rather than missing argumentative bridges
- Parts `139-144` remain thinner than the early full-body standard, with `144` still the weakest local tranche
- Part `136` no longer looks structurally broken; its low density is largely footnote-driven
- the late-run English remains working draft translation, not polished publication prose

Under the `main-prose full density` standard, the remaining uncertainty is narrower than the visible line gradient suggests. What still varies across the volume is mostly:

- density of citation and documentary apparatus
- paragraph compactness inside the part files
- how much chapter-edge spillover the source window contains

That unevenness should not be mistaken for a uniform loss of Cassirer's main prose.

## Decision for Now

- There is no further forward translation inside Volume I.
- If German source-completeness continues, reopen Part `144` or Part `136` only if the goal is near-full tranche density rather than argument-complete usability.
- Otherwise the local German repair pass can stop here; the remaining late-run debt is now selective thinness, not a broken reconstruction surface.
- If primary work continues, it should do so in Volume II rather than by pretending Volume I remains open.
