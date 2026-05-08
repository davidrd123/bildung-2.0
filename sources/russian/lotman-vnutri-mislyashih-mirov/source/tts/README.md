# TTS Layer

Status: access layer. All current `reader-en` drafts have audio-ready exports.

`source/tts/` is reserved for audiobook-ready derivatives of
`source/reader-en/` drafts. A TTS file should not become the editable
translation draft and should not seed apparatus decisions.

Expected use:

- remove reader metadata and pass notes
- keep only speakable headings and reading text
- use English filenames so audiobook sections are legible in players and file
  browsers
- expand compact notation, letter-number variables, and schematic labels where
  they would otherwise read poorly in speech
- optionally smooth sentence rhythm for listening without changing the reader
  draft's interpretive decisions

Apparatus boundary: glossary, handles, threads, and encounter claims require
checked source-facing work outside this directory.

Regenerate exports from the repo root with:

```bash
python3 tools/export_lotman_tts.py
```

Track exports in `manifest.yaml`.
