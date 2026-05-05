# Langer PNK Cleanup Manifest

- PDF authority: `sources/modern/incoming/books/Philosophy in a New Key, Suzanne K. Langer.pdf`
- Extraction: `pdftotext` default text layer for prose; `pdftotext -layout` for the two-column index; then local cleanup script.
- Page markers: printed page numbers recovered from PDF running headers as `[page N]`.
- Publisher matter: the catalog page at PDF p. 249 is intentionally retained because it is present in the supplied PDF and has been page-image proofed.
- Index note: PDF pages 250-255 are the printed index pages 243-248; the full index has now been checked against rendered page images, linearized from the original two-column layout, and stripped of repeated `INDEX` running headers after page markers.
- Witness mismatch: the raw scaffold from `sources/modern/incoming/books/Philosophy in a New Key - Susanne Langer.txt` has a separate second-edition preface and has the text used to fill the supplied-PDF pp. 76-77 gap under a different running pagination; the current PDF does not include those page images. The pp. 76-77 gap has been OCR-normalized from the raw text witness, word-checked against supplied Kindle screenshots, and accepted for this corpus on 2026-05-05. The second-edition preface remains raw-witness-only.
- Proof status: `page-proof-manifest.md` is the authoritative current proof ledger. The suspicious OCR counts below are legacy first-pass mechanical counts, not an active open-issue list.
- Mechanical verification: run `python3 tools/verify_langer_philosophy_in_a_new_key.py` from the repo root after editing cleaned files. This checks page-marker coverage, chapter footnote continuity, known OCR garbage patterns, and the presence of documented blocker notes.

| seq | cleaned file | source | page markers | page gaps | suspicious OCR items |
| ---: | --- | --- | ---: | --- | ---: |
| 0 | `cleaned/000-title-pages-and-publisher-matter.txt` | pdf page-image proof | 0 | - | 0 |
| 1 | `cleaned/001-preface-to-the-second-edition.txt` | raw-witness-only, normalized | 0 | not in supplied PDF | 0 |
| 2 | `cleaned/002-preface-to-the-first-edition.txt` | pdf page-image proof | 0 | - | 5 |
| 3 | `cleaned/003-contents.txt` | pdf page-image proof | 0 | - | 0 |
| 10 | `cleaned/010-the-new-key.txt` | pdf page-image proof | 20 | - | 26 |
| 11 | `cleaned/011-symbolic-transformation.txt` | pdf | 23 | - | 28 |
| 12 | `cleaned/012-the-logic-of-signs-and-symbols.txt` | pdf | 22 | - | 18 |
| 13 | `cleaned/013-discursive-forms-and-presentational-forms.txt` | pdf + Kindle-checked raw gap fill for missing PDF pages 76-77 | 21 | - | 19 |
| 14 | `cleaned/014-language.txt` | pdf | 34 | - | 40 |
| 15 | `cleaned/015-life-symbols-the-roots-of-sacrament.txt` | pdf | 23 | - | 21 |
| 16 | `cleaned/016-life-symbols-the-roots-of-myth.txt` | pdf | 28 | - | 27 |
| 17 | `cleaned/017-on-significance-in-music.txt` | pdf | 35 | - | 55 |
| 18 | `cleaned/018-the-genesis-of-artistic-import.txt` | pdf | 18 | - | 27 |
| 19 | `cleaned/019-the-fabric-of-meaning.txt` | pdf | 24 | - | 20 |
| 30 | `cleaned/030-acknowledgments.txt` | pdf page-image proof with inferred logical pages 240-242 | 3 | - | 15 |
| 31 | `cleaned/031-index.txt` | pdf page-image proof, full index linearized | 6 | - | 2 |
