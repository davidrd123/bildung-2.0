# Snell Normalized OCR Layer

**Status:** Machine-normalized base for a manual cleanup pass. This is more
readable than `source/raw/`, but it is not citation-grade.

## What This Is

The files in this directory are generated from `source/raw/*.txt` by:

- `tools/normalize_snell_ocr.py`

The script performs conservative cleanup:

- removes form feeds, page numbers, running headers, copyright footer lines,
  and ISBN footer lines
- joins line-wrapped prose into paragraphs
- dehyphenates obvious line-break hyphenation
- applies a small set of high-confidence OCR repairs, such as `Phüologe` to
  `Philologe`
- writes `manifest.yaml` with paragraph counts, repair counts, and suspect OCR
  counts by file

## What This Is Not

This layer does not repair Greek quotations. The Greek in the OCR is often
corrupt enough that it should be restored from a Greek source witness rather
than guessed from the German OCR.

This layer also does not certify punctuation, italics, page transitions, note
references, or exact quotation. Use it for reading and search; use a PDF or
scan witness for citation-grade verification.

## Manual Pass Order

The first manual pass should follow the PSF II pressure map rather than the
book's full sequence:

1. `011` Homer
2. `012` Olympian gods
3. `013` Hesiod
4. `014` early lyric
5. `016` tragedy
6. `018` human/divine knowledge
7. `019` historical consciousness
8. `015` Pindar and `020` ethics

The later chapters can wait unless a specific Snell-side task needs them:
`017` Aristophanes, `021-022` concept formation, `023-027` symbol/humanism /
Callimachus / Arcadia / theory-practice.

## Completion Gate

A chapter is clean enough for ordinary working use when:

- page furniture is gone
- line-break hyphenation is repaired
- German OCR corruptions that affect sense are corrected
- Greek quotations are either repaired from a Greek witness or marked as
  unresolved
- notes and index references remain searchable
- a quick comparison against the scan/PDF passes for the chapter opening, one
  middle page, and the chapter close
