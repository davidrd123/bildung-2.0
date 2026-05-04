# TTS Layer

Status: access layer. One audio-ready Lotman chapter has been exported.

`source/tts/` is reserved for audiobook-ready derivatives of
`source/reader-en/` drafts. A TTS file should not become the editable
translation draft and should not seed apparatus decisions.

Expected use:

- remove reader metadata and pass notes
- keep only speakable headings and reading text
- expand formulas, abbreviations, and letter-number variables where needed
- smooth sentence rhythm for listening without changing the reader draft's
  interpretive decisions

Apparatus boundary: glossary, handles, threads, and encounter claims require
checked source-facing work outside this directory.

Track exports in `manifest.yaml`.
