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
- Parts `134-141`:
  uneven recovery zone; several tranche bodies become fuller again, but the recovery is not uniform
- Parts `142-149`:
  renewed late compression, strongest in the Bayle close; still source-backed, but no longer at the earlier full-body standard

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

- Parts `134-141` remain usable but uneven; they may still need targeted German re-expansion
- Parts `142-149` reopen the German density problem, with the Bayle close as the thinnest local stretch
- Parts `142-149` are now the clearest remaining local priority if German completeness work resumes
- the late-run English remains working draft translation, not polished publication prose

## Decision for Now

- There is no further forward translation inside Volume I.
- If German source-completeness continues, begin with the renewed thin tail in Parts `142-149`.
- After that, recheck the uneven middle band in Parts `134-141` as needed.
- If primary work continues, it should do so in Volume II rather than by pretending Volume I remains open.
