# Langer PNK Cleanup Manifest

- PDF authority: `sources/modern/incoming/books/Philosophy in a New Key, Suzanne K. Langer.pdf`
- Extraction: `pdftotext` default text layer for prose; `pdftotext -layout` for the two-column index; then local cleanup script.
- Page markers: printed page numbers recovered from PDF running headers as `[page N]`.
- Index note: PDF pages 250-255 are the printed index pages 243-248; badly garbled index spans on printed pages 247-248 were checked against rendered page images.
- Witness mismatch: the raw scaffold has a separate second-edition preface; the current PDF does not. That one file is retained from the raw text witness and marked below.

| seq | cleaned file | source | page markers | page gaps | suspicious OCR items |
| ---: | --- | --- | ---: | --- | ---: |
| 0 | `cleaned/000-title-pages-and-publisher-matter.txt` | pdf page-image proof | 0 | - | 0 |
| 1 | `cleaned/001-preface-to-the-second-edition.txt` | raw-witness-only | 0 | - | 4 |
| 2 | `cleaned/002-preface-to-the-first-edition.txt` | pdf | 0 | - | 5 |
| 3 | `cleaned/003-contents.txt` | pdf | 0 | - | 0 |
| 10 | `cleaned/010-the-new-key.txt` | pdf | 19 | - | 26 |
| 11 | `cleaned/011-symbolic-transformation.txt` | pdf | 23 | - | 28 |
| 12 | `cleaned/012-the-logic-of-signs-and-symbols.txt` | pdf | 22 | - | 18 |
| 13 | `cleaned/013-discursive-forms-and-presentational-forms.txt` | pdf + raw gap fill for missing PDF pages 76-77 | 21 | - | 19 |
| 14 | `cleaned/014-language.txt` | pdf | 34 | - | 40 |
| 15 | `cleaned/015-life-symbols-the-roots-of-sacrament.txt` | pdf | 23 | - | 21 |
| 16 | `cleaned/016-life-symbols-the-roots-of-myth.txt` | pdf | 28 | - | 27 |
| 17 | `cleaned/017-on-significance-in-music.txt` | pdf | 35 | - | 55 |
| 18 | `cleaned/018-the-genesis-of-artistic-import.txt` | pdf | 18 | - | 27 |
| 19 | `cleaned/019-the-fabric-of-meaning.txt` | pdf | 24 | - | 20 |
| 30 | `cleaned/030-acknowledgments.txt` | pdf page-image proof with inferred logical pages 240-242 | 3 | - | 15 |
| 31 | `cleaned/031-index.txt` | pdf-layout + page-image repair for index pp. 247-248 | 6 | - | 2 |
