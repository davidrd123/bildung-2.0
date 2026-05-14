# TTS Layer

Status: access layer for audiobook input preparation.

`source/tts/` contains audio-ready derivatives of the English working
translation in `parts/`. These files are intended as input to the Alexandria
audiobook pipeline, where later steps can handle speaker chunking, performance
instructions, and pronunciation cleanup.

## What the TTS pass does

- Keeps only the speakable `## Working Translation` body from each source part.
- Adds one compact section heading from the part title.
- Strips translation pressure, calibration notes, and source-facing apparatus.
- Strips Markdown emphasis markers around book titles and foreign terms.
- Converts dialogue labels into `[[speaker: Name]]` markers and preserves
  Bruno's argument sequence.
- Excludes Liber Liber metadata and the duplicated proemial calibration draft.

## What it does NOT do

The TTS layer is not the editable translation draft. It should not settle
terminology, seed glossary entries, create encounters, or replace source-facing
review. It also does not yet perform detailed pronunciation normalization for
Italian, Latin, or proper names.

The `[[speaker: Name]]` markers are structural cues for downstream audiobook
script generation, not voice assignments and not text meant to be read aloud
verbatim.

## Source Boundary

Current exports derive from the source-local `parts/` working translations, not
from a checked page-image or critical-edition witness. Keep substantive
translation corrections in `parts/` first, then regenerate this layer.

Regenerate exports from the repo root with:

```bash
python3 tools/export_bruno_de_la_causa_tts.py
```

Track exports in `manifest.yaml`.
