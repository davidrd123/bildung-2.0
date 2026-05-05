# TTS Layer

Status: access layer for audiobook input preparation.

`source/tts/` contains audio-ready text derived from `source/image-grounded-cleaned/`
(preferred) or `source/cleaned/` (fallback). These files serve as input to the
Alexandria audiobook pipeline, where Gemini handles speaker chunking and
instruction generation.

## What the TTS pass does

- Strips page markers (`[pdf page XXX]`, `[page N]`)
- Strips editorial headnotes (publication history, cross-references)
- Marks footnotes as `[Footnote: ...]` for downstream handling
- Strips bare scholarly cross-references (W2:49, CP1:545, etc.)
- Preserves all of Peirce's prose and argument structure
- Expands section markers and compact notation for speech (`§1.` -> `Section 1.`,
  `∴` -> `Therefore`, `P'` -> `P prime`, `P^iv` -> `P four`)
- Does NOT split sentences, simplify vocabulary, or add reading instructions

## What it does NOT do

Sentence pacing, speaker assignment, and audio direction are handled downstream
by Alexandria/Gemini. The TTS file is clean prose input, not a production script.

## Apparatus boundary

TTS files do not seed glossary, encounters, handles, or threads. They are access
aids only.

## Source preference

Use `image-grounded-cleaned` when available (page-image verified). Fall back to
`cleaned` for chapters not yet image-grounded.

Track exports in `manifest.yaml`.
