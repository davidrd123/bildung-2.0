# Goal Shape: Kultura Reader-En Translation Pass

## Objective

Produce a complete English `reader-en` access layer for Yuri Lotman's *Culture
and Explosion* from the page-image-proofed Russian source. The output should be
clean, speakable English suitable for discussion and later TTS export, while
preserving Lotman's conceptual recurrence and keeping glossary, handle, and
thread claims out of the translation layer unless a separate checked encounter
earns them.

Recommended `/goal` wording:

```text
Produce a full English reader-en pass for sources/russian/lotman-kultura-i-vzryv from source/cleaned, section by section. For every main chapter, create a reader-en markdown draft with the standard metadata header, clean paragraph-by-paragraph English, no page markers in the main reading flow, and a Pass Notes section for source issues, term pressure, encounter candidates, and TTS cleanup notes. Keep the cleaned Russian as authority; use page images only when the cleaned source appears doubtful. Update source/reader-en/manifest.yaml and journal.md after each batch. Do not create glossary entries, handles, thread dossiers, or a TTS export until the reader-en layer is complete or a separate checked encounter explicitly earns them.
```

## Scope

Inputs:

- `source/cleaned/*.txt` as the translation authority
- `source/sections.yaml` for ordering, titles, scan ranges, and printed pages
- `source/cleaned/page-proof-manifest.md` for source decisions already made
- `source/page-images/pages/NNN.png` only when the cleaned Russian itself needs
  verification

Outputs:

- `source/reader-en/001-*.md` through `020-*.md`
- updated `source/reader-en/manifest.yaml`
- chronological batch entries in `journal.md`

Out of scope for this goal:

- TTS export generation
- glossary promotion
- handle creation
- thread dossiers
- broad Lotman comparison notes beyond compact `Pass Notes`

## Definition Of Done

- Main chapters `001` through `020` have reader-en markdown files.
- Manifest entries for `001` through `020` are marked `drafted`; front matter
  and back matter remain `skip` unless deliberately translated later.
- Each reader file begins with the standard metadata header and identifies its
  cleaned source, scan range, and printed page range.
- The main reading flow contains only the translated chapter text: no page
  markers, no source apparatus, no commentary, and no unresolved OCR residue.
- Technical recurrence is kept consistent enough for listening: system,
  language, outside-language reality, translation, boundary, explosion,
  unpredictability, text, culture, dynamics.
- Substantive authorial footnotes are translated where they affect the argument;
  citation-only footnotes are either kept compact or summarized in `Pass Notes`.
- Each reader file ends with `## Pass Notes` covering source status, term
  pressure, possible checked-encounter candidates, and TTS cleanup candidates.
- `journal.md` records each completed batch, including files drafted, source
  ranges, notable translation decisions, and the next continuation point.

## Work Loop

1. Read the next cleaned source file and its row in `source/sections.yaml`.
2. Draft the reader-en file in source order, paragraph by paragraph.
3. Translate for the ear without flattening technical recurrence.
4. Check page images only if the cleaned source creates a real doubt.
5. Add `Pass Notes`.
6. Mark the manifest row `drafted`.
7. Add a compact journal batch entry.

## Suggested Milestones

1. Calibration: `001-postanovka-problemy` and
   `002-sistema-s-odnim-yazykom`.
2. Early conceptual arc: `003` through `007`.
3. Long cultural-type chapters: `008`, then `009`, then `010` as separate
   large batches.
4. Explosion and unpredictability core: `011` through `014`.
5. Late semiotic/art chapters: `015` through `020`.
6. Whole-layer audit: manifest completeness, missing pass notes, `[source
   check]` residues, TTS hazards, and journal continuity.
