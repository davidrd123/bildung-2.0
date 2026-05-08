# Reader-En Pass

Status: access layer for English reading, discussion, and audiobook/TTS
preparation. This is not the critical apparatus.

## Purpose

`reader-en` gives *Культура и взрыв* an English reading surface comparable to
the `reader-en` pass for `../lotman-vnutri-mislyashih-mirov`. It should support
chapter-scale reading sessions, revision for comprehension, and a later
audio-friendly export.

The source for this pass is the page-image-proofed Russian text in
`../cleaned/`, not raw OCR. The cleaned Russian remains the authority for page
markers, source formatting, and later checks against the DjVu page images.

The drafts here do not settle Russian terminology. They do not seed the
glossary, create handles, or open thread dossiers by themselves.

## File Convention

Use the same sequence and slug as `source/sections.yaml`:

```text
001-postanovka-problemy.md
008-durak-i-sumasshedshiy.md
020-vmesto-vyvodov.md
```

Track pass state in `manifest.yaml`. Use `drafted` for reader files that exist,
`pending` for planned reader chapters, and `skip` for front matter, contents, or
other material not useful as reading chapters.

Each file should begin with:

```text
# English Reader Draft: <section title>

Status: reader draft; not quotation-grade.
Source: ../cleaned/<source-file>.txt
Checked source: page-image-proofed cleaned Russian, scans <NNN-NNN>, printed
pages <N-N>.
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
5. Use `[source check]` only for source uncertainties that materially affect the
   reading; if the cleaned Russian itself seems wrong, check the page image and
   record the decision in pass notes.
6. Put source issues, term pressure, and possible encounter candidates at the
   end under `Pass Notes`.

## Audio Bias

The reader draft should already be close to listenable English:

- no page headers or page numbers in the main flow
- no dense citation apparatus in the main flow
- headings kept short and speakable
- paragraph breaks preserved for pacing
- formulas, diagram labels, and variables rendered in words when needed for
  audio clarity
- substantive authorial footnotes translated only where they affect the
  argument; citation-only notes can be summarized in `Pass Notes`

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
