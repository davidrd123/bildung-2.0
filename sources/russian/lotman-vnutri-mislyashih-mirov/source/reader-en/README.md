# Reader-En Pass

Status: access layer for English reading, discussion, and audiobook/TTS
preparation. This is not the critical apparatus.

## Purpose

`reader-en` gives the book an English reading surface comparable to the
chapter-scale source shelves used for Langer and other modern sources. It lets a
web chat or reading session take one chapter at a time, discuss it, revise the
English for comprehension, and later prepare audio-friendly text.

The drafts here do not settle Russian terminology. They do not seed the
glossary, create handles, or open thread dossiers by themselves.

## File Convention

Use the same sequence and slug as `source/sections.yaml`:

```text
005-part-i-01-tri-funktsii-teksta.md
006-part-i-02-avtokommunikatsiya.md
013-part-ii-02-ponyatie-granitsy.md
```

Track pass state in `manifest.yaml`. Use `drafted` for reader files that exist,
`pending` for planned reader chapters, and `skip` for front matter, indexes, or
other material not useful as reading chapters.

Each file should begin with:

```text
# English Reader Draft: <section title>

Status: reader draft; not quotation-grade.
Source: ../raw/<source-file>.txt
Checked source: <checked file or "none beyond local spot checks">
Use: discussion and audiobook/TTS preparation.
Apparatus boundary: glossary, handles, and threads require separate checked
encounters.
```

## Translation Pass Shape

1. Translate in source order, paragraph by paragraph.
2. Keep the argument audible: split long Russian sentences when English would
   otherwise become hard to hear.
3. Preserve technical recurrence even when the English is a little less smooth.
4. Do not add commentary inside the reading flow.
5. Use `[source check]` only for OCR or scan uncertainties that would materially
   affect the reading.
6. Put source issues, term pressure, and possible encounter candidates at the
   end under `Pass Notes`.

## Audio Bias

The reader draft should already be close to listenable English:

- no page headers or page numbers in the main flow
- no dense footnote apparatus in the main flow
- headings kept short and speakable
- paragraph breaks preserved for pacing
- formulas and variables rendered in words when needed for audio clarity

A later `source/tts/` layer may strip metadata and pass notes, but `reader-en`
should remain the editable translation draft.

## Apparatus Boundary

Broad reader translation is allowed. Apparatus promotion is not automatic.

Use this rule:

> Reader text can travel widely through the book; conceptual apparatus must stay
> earned by checked encounters.

If a reader chapter exposes serious pressure, make a journal note or create a
new encounter packet against a checked source range. Only that checked encounter
can justify glossary updates, thread dossiers, or handles.
