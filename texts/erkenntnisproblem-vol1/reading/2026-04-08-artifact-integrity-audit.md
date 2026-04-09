# 2026-04-08 Artifact Integrity Audit

This note fixes the status of the recent `Erkenntnisproblem` artifacts after the English layer drifted from translation toward gloss.

It is a routing and honesty note, not a second journal.

## Current Edge

- The canonical working edge in the current tree is Part `133`, ending at printed `532-535` / PDF `556-559`.
- Parts `132-133` are fully integrated into the local trace (`page-map.yaml`, `journal.md`, `close-reading-ledger.md`, `session-ledger.yaml`), even though they are still untracked in git.
- The next real pickup is printed `536-539` / PDF `560-563`, starting fresh from the end of Part `133`.

## Source-Backed and Aligned

- `source/raw/*.txt` through `134`:
  direct extraction windows for the active run
- `source/normalized/*.txt` through `134`:
  cleaned source windows aligned with the active run
- `parts/*.md` German corrected blocks through `133`:
  source-backed working text for the tranche files, but not always full-page transcription in the late run; some recent parts compress the body text into corrected working excerpts
- `source/page-map.yaml` through `133`:
  aligned with the current working edge and parse-clean
- `source/viewer-index.json`:
  derived export parses cleanly and currently serializes `133` parts and `49` glossary entries

## Translation Layer Status

- Parts `80-81`:
  `English (draft)` is still translation-shaped working English and remains provisionally acceptable as draft translation
- Parts `82-133`:
  `English (gloss)` is not a faithful translation layer and should be treated as interpretive English only
- `Working Commentary` blocks:
  interpretive guidance, not translation

The practical boundary is therefore:

- `80-81` = draft translation
- `82-133` = gloss

## Derived but Current

- `journal.md` through Part `133`:
  current cross-batch notebook for findings actually earned from the text
- `reading/close-reading-ledger.md` through Part `133`:
  local holding surface for tranche findings
- `session-ledger.yaml` through Part `133`:
  valid re-entry surface for continuation
- `interpretive-notes.md`:
  explicitly nonbinding review/extrapolation surface; useful prompts, not source authority

## Not Canonical

- Raw extraction spillover beyond the active edge is not canonical unless it is normalized, turned into a part, and integrated into the trace.
- The interrupted `135-139` raw windows were only scratch from an aborted continuation and should not be treated as the next edge.

## Decision for Now

- Resume primary work from Part `133`, not from any stray raw window.
- If forward work resumes, re-extract printed `536-539` / PDF `560-563` fresh.
- If translation fidelity becomes the priority, the repair boundary starts at Part `82`, where the English layer stopped behaving like translation and became gloss.
- If source completeness becomes the priority, late parts from roughly `124-133` should also be rechecked for compressed German working excerpts against the normalized windows.
