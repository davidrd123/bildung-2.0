# Das Erkenntnisproblem I - Translation Project

Ernst Cassirer, *Das Erkenntnisproblem in der Philosophie und Wissenschaft der neueren Zeit*, vol. 1 (12th revised edition, 1911)

## Scope

This project tracks a working English translation of volume 1 of Cassirer's *Erkenntnisproblem*.

- Source PDF: `../../books/Erkenntnisproblem/Vol1/daserkenntnispro01cass.pdf`
- Source OCR/search text: `../../books/Erkenntnisproblem/Vol1/daserkenntnispro01cass_hocr_searchtext.txt`
- Translation scope for this subproject: front matter, introduction, and the main body of volume 1

## Why This Is Not `escolios` or `zeitmauer`

This material is neither aphoristic nor section-numbered prose. It is architectonic philosophical exposition with heavy conceptual recurrence and long argumentative paragraphs. For that reason the workflow here is:

- one primary draft translation
- paragraph-cluster units rather than aphorisms or numbered sections
- light mechanical cleanup ahead of time
- semantic cleanup against the PDF only for the tranche currently being translated
- glossary pressure notes for recurring terms that are broader than ordinary English equivalents

## Structure

```text
source/
  outline.yaml          # high-level map of books, chapters, and tranche boundaries
  page-map.yaml         # trusted PDF/printed-page anchors for current work
  glossary.yaml         # recurring term decisions and unresolved pressure points
  raw/                  # page-range extracts from the PDF text layer
  normalized/           # lightly normalized working text, still to be verified
parts/
  01-prefaces-and-introduction.md
journal.md              # process notes, drift in term choices, cleanup rules
scripts/
  extract_page_range.py # raw PDF text extraction by page range
  normalize_pages.py    # conservative cleanup of raw extracts
```

## Working Method

1. Extract a page range from the PDF into `source/raw/`.
2. Run light normalization into `source/normalized/`.
3. Correct the German against the PDF for the active tranche only.
4. Translate in small batches.
5. Record unstable terms in `source/glossary.yaml`.
6. Keep methodological drift and cross-project notes in `journal.md`.

## Calibration Tranche

The starting tranche is deliberately small:

- 1906 preface
- retained 1910 preface headed `Zur zweiten Auflage`
- opening pages of the introduction

That batch should settle sentence strategy, paragraph handling, and the first layer of load-bearing vocabulary before any broader pass through the body of the book.

## Extraction

```bash
python3 texts/erkenntnisproblem-vol1/scripts/extract_page_range.py --start 25 --end 28 --output source/raw/example.txt
python3 texts/erkenntnisproblem-vol1/scripts/normalize_pages.py --input source/raw/example.txt --output source/normalized/example.txt --start-page 25
```

The extractor defaults to `pdftotext -raw`, which currently preserves reading order better than the plain mode on this scan. The normalization step is intentionally conservative. It should reduce clerical noise, not silently emend the text.
