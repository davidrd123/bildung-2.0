# Humboldt - *Ueber die Verschiedenheit des menschlichen Sprachbaues* - Source Landing Zone

Wilhelm von Humboldt, *Ueber die Verschiedenheit des menschlichen Sprachbaues
und ihren Einfluss auf die geistige Entwickelung des Menschengeschlechts*.
Edited with explanatory notes and excursuses, and with A. F. Pott's
introductory essay *Wilhelm von Humboldt und die Sprachwissenschaft*. Erster
Band. Berlin: S. Calvary & Co., 1876.

## What This Is

A German source-language landing zone for the 1876 Pott edition of Humboldt's
major Sprachbau text.

This is **not** yet a live Humboldt encounter, **not** a checked working text,
and **not** a promoted subproject. It exists so the PDF and incoming page
images have a stable home before extraction, page mapping, and any bounded
source work begin.

## Why Here

- Not `texts/` - no glossary, journal, encounters, or translation/commentary
  apparatus has been earned.
- Not `sources/modern/` - this is a German primary source.
- `sources/german/` is the right layer for a source-near Humboldt witness that
  can later support Cassirer, Chomsky, Lotman, and translation-method probes.

## Source

Local authority copy, gitignored:

- `source/local/ueber-die-verschiedenheit-des-menschlichen-sprachbaues-band1-1876.pdf`

Original local intake path:

- `/Users/daviddickinson/Downloads/berdieverschiede01humb.pdf`

Archive identifier from PDF metadata:

- `https://archive.org/details/berdieverschiede01humb`

PDF metadata at intake:

- 436 PDF pages
- 28,587,608 bytes
- Internet Archive PDF generated 2022-09-10

Original JP2 tar landed from local path:

- `/Users/daviddickinson/Downloads/berdieverschiede01humb_orig_jp2.tar`
- extracted to `source/page-images/jp2/`
- 438 JP2 files
- filename prefix `berdieverschiede01humb_orig_`
- zero-based sequence `0000` through `0437`, no detected gaps

Volume 2 local witnesses, gitignored:

- `source/local/berdieverschiede02humb.pdf`
- `source/local/berdieverschiede02humb_hocr.html`
- `source/local/berdieverschiede02humb_hocr_pageindex.json`
- `source/local/berdieverschiede02humb_hocr_searchtext.txt`
- `source/local/berdieverschiede02humb_page_numbers.json`
- original JP2 tar: `/Users/daviddickinson/Downloads/berdieverschiede02humb_orig_jp2.tar`
- extracted to `source/page-images/jp2/`
- 558 JP2 files
- filename prefix `berdieverschiede02humb_orig_`
- zero-based sequence `0000` through `0557`, no detected gaps

Important limit: this is **Band I**. Do not treat it as a complete Humboldt
corpus or complete source surface until the companion volume situation is
checked.

## Initial Structural Finding

First page-map pass: Band I appears to contain the edition title matter and
A. F. Pott's long introduction, *Wilhelm von Humboldt und die
Sprachwissenschaft*, not the running body of Humboldt's own Sprachbau text.

Verified anchors:

- PDF page 8 / JP2 `0008`: Pott title page.
- PDF page 9 / JP2 `0009`: edition title page for Humboldt's Sprachbau work.
- PDF page 11 / JP2 `0011`: Pott introduction title page.
- PDF page 13 / JP2 `0013`: Pott introduction opening, printed page `I`.
- PDF page 431 / JP2 `0431`: Pott introduction close, printed page
  `CCCCXXI`, headed `Schluss`.

Do not promote raw Humboldt text from this witness until the companion volume
is located. This Band I witness is still valuable for Pott's reception,
apparatus, and edition framing.

Companion candidate located, not yet landed:

- Internet Archive identifier `berdieverschiede02humb`
- `https://archive.org/details/berdieverschiede02humb`
- Theological Commons record: `https://commons.ptsem.edu/id/berdieverschiede02humb`
- Reported as Volume 2 of the same 1876 S. Calvary & Co. edition.
- Now landed locally and treated as the primary Humboldt text witness.

Volume 2 starts Humboldt's running text at PDF/JP2 leaf `0007`, printed page
`1`, with Section 1 on the Malay peoples. Section 2 begins at PDF/JP2 leaf
`0025`, printed page `19`.

First raw extract promoted:

- `source/raw/001-band2-section-01-malayischer-stamm-pdf-007-024.txt`
- witness: Volume 2 PDF text layer
- PDF/JP2 leaves: `0007-0024`
- printed pages: `1-18`
- status: raw, unnormalized

Second raw extract promoted for the core theoretical passage:

- `source/raw/008-band2-section-08-form-der-sprachen-pdf-060-068.txt`
- witness: Volume 2 PDF text layer
- PDF/JP2 leaves: `0060-0068`
- printed pages: `54-62`
- status: raw, unnormalized
- note: contains the `Ergon` / `Energeia` formulation.

Targeted raw tranche promoted for the familiar theoretical node:

- `source/raw/008a-ergon-energeia-pdf-061-062.txt`
- witness: Volume 2 PDF text layer
- PDF/JP2 leaves: `0061-0062`
- printed pages: `55-56`
- status: raw, unnormalized
- note: begins with the setup that language is something continually passing
  away and includes the `Werk (Ergon)` / `Thaetigkeit (Energeia)` formulation.

## Structure

```text
source/
  local/
    ueber-die-verschiedenheit-des-menschlichen-sprachbaues-band1-1876.pdf
    # future IA OCR/metadata sidecars; gitignored
  page-images/
    jp2/                 # incoming page images; gitignored
  full/                  # future whole-text extraction
  raw/                   # future split OCR / extraction files
  normalized/            # future checked working tranches
  witnesses.yaml         # local witness inventory and source preference notes
  page-map.yaml          # placeholder for PDF leaf / printed-page mapping
  sections.yaml          # bounded extraction map
  README.md              # local source-layer notes
scripts/
  inspect_jp2_sequence.py
  extract_pdf_page_range.py
  ocr_jp2_page.py
```

## Next Honest Moves

After the initial mapping:

1. Land the companion volume candidate `berdieverschiede02humb`.
2. Use Band I for Pott's introduction only unless a later check proves
   otherwise.
3. Continue mapping Volume 2 sections before bulk splitting.
4. Check the targeted `Ergon` / `Energeia` raw tranche against JP2/HOCR before
   quotation, translation, or Chomsky comparison.
5. Extract a whole text into `source/full/` only after choosing the best OCR
   witness.
6. Split into `source/raw/` at the edition's natural seams.
7. Normalize only the bounded tranches that are actually needed for source-near
   work.

The original JP2s are visual witnesses, but they are full camera-frame images
of the open book, not cropped OCR-ready page images. Use IA OCR sidecars or a
cropped/rotated image workflow before promoting OCR text.
