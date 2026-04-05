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
  cusanus-generative-chain.yaml  # first-pass transformation chain for Parts 06-16
  raw/                  # page-range extracts from the PDF text layer
  normalized/           # lightly normalized working text, still to be verified
reading/
  close-reading-ledger.md  # sentence- and paragraph-scale findings that arise directly from close translation
parts/
  01-prefaces-and-introduction.md
journal.md              # process notes, drift in term choices, cleanup rules
interpretive-notes.md   # project-side analogies and method extrapolations
review-checklist.md     # periodic quality and maintenance prompts
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
6. Record paragraph-scale translation findings in `reading/close-reading-ledger.md` when they are too important to lose but too local for the journal.
7. Keep source-bound workflow drift in `journal.md` and exploratory cross-project notes in `interpretive-notes.md`.

The split between note files is intentional:

- `reading/close-reading-ledger.md` catches sentence- and paragraph-level gains from slow translation before they either disappear or get overpromoted
- `journal.md` stays source-bound and workflow-bound
- `interpretive-notes.md` holds exploratory analogies, external comparisons, and project-side method extrapolations

## Ongoing Maintenance

- Run a harmonization pass after each major chapter arc, or once a cluster of glossary decisions has clearly stabilized.
- Revisit earlier parts against the current glossary, especially where open terms like `Geist`, `Wissenschaft`, and `Vorstellung` were translated before later pressure emerged.
- Expand glossary notes whenever an entry lists renderings but still underdescribes what the term is doing philosophically in the translated material.
- Build structured transformation chains only where the text itself forces them; the current first-pass example is the Cusanus chapter in `source/cusanus-generative-chain.yaml`.
- Recheck viewer and PDF stitching whenever a tranche ends mid-sentence or when export-facing headings and paragraph alignment change.
- Keep source-bound judgments in `journal.md`; move comparative or project-side extrapolations to `interpretive-notes.md`.
- Treat `source/viewer-index.json` and the export script as the authoritative current status rather than hardcoding moving progress counts here.

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
