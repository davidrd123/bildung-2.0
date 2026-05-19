# Humboldt - *Ueber die Kawi-Sprache auf der Insel Java* - Band II

Wilhelm von Humboldt, *Ueber die Kawi-Sprache auf der Insel Java, nebst
einer Einleitung ueber die Verschiedenheit des menschlichen Sprachbaues und
ihren Einfluss auf die geistige Entwickelung des Menschengeschlechts*.
Zweiter Band. Edited posthumously by J. C. Eduard Buschmann. Berlin:
Druckerei der Koeniglichen Akademie der Wissenschaften, 1838.

## What This Is

A German source-language landing zone for Band II of Humboldt's
*Kawi-Sprache*.

This is **not** the Pott 1876 *Verschiedenheit* shelf and should not be
collapsed into it. The Pott shelf at
`sources/german/humboldt-verschiedenheit-sprachbau/` holds a later edition of
the singular *Verschiedenheit* text plus Pott apparatus. This shelf holds the
Buschmann-edited 1838 Kawi volume.

This is **not** yet a live Humboldt campaign. It is a source scaffold for
substrate use: PDF/OCR/page-image witnesses, a page map, and rough raw splits
at the volume's natural seams. Targeted working tranches now mark the main
Cassirer-facing Kawi surfaces: the Kawi opening, `actuale Sein`, the Drittes
Buch Stammverwandtschaft method opening, Raumverba, Tagalog `sa`, and the
section 23 close on the concept of Kawi.

## Why Here

- `sources/german/` is the right layer: this is a German primary source.
- The volume is distinct from the 1876 Pott *Verschiedenheit* witness already
  landed.
- The volume is the practical next Humboldt source for Cassirer-side work:
  it contains the concrete comparative-linguistic Kawi and Malay material
  missing from a merely theoretical *Ergon/Energeia* extraction.

## Source

Primary local authority copy, gitignored:

- `source/local/berdiekawisprac01buscgoog_text.pdf`

Original local intake path:

- `/Users/daviddickinson/Downloads/berdiekawisprac01buscgoog_text.pdf`

Internet Archive identifier from metadata:

- `berdiekawisprac01buscgoog`
- `https://archive.org/details/berdiekawisprac01buscgoog`

Local sidecars landed, gitignored:

- `source/local/berdiekawisprac01buscgoog_hocr.html`
- `source/local/berdiekawisprac01buscgoog_hocr_pageindex.json`
- `source/local/berdiekawisprac01buscgoog_hocr_pageindex.json.gz`
- `source/local/berdiekawisprac01buscgoog_hocr_searchtext.txt`
- `source/local/berdiekawisprac01buscgoog_hocr_searchtext.txt.gz`
- `source/local/berdiekawisprac01buscgoog_page_numbers.json`

Page-image witness:

- local source: `/Users/daviddickinson/Downloads/berdiekawisprac01buscgoog_tif.zip`
- extracted to `source/page-images/tif/berdiekawisprac01buscgoog_tif/`
- 609 TIF files
- filename pattern `berdiekawisprac01buscgoog_0001.tif` through
  `berdiekawisprac01buscgoog_0609.tif`
- no JP2 tar is available locally for this item

Observed but not imported:

- `/Users/daviddickinson/Downloads/berdiekawisprac01buscgoog.pdf`
  scan-only Google PDF; superseded for this shelf by the text PDF plus TIFs.
- Internet Archive "Full text" HTML download; redundant with the hOCR/search
  text sidecars for current source work.

## Current Splits

Tracked full OCR text:

- `source/full/kawi-sprache-band2.txt`

Tracked raw splits:

- `source/raw/000-front-matter-and-inhaltsuebersicht-pdf-001-041.txt`
- `source/raw/010-zweites-buch-ueber-die-kawi-sprache-pdf-042-246.txt`
- `source/raw/020-drittes-buch-erster-abschnitt-stammverwandtschaft-pdf-248-336.txt`
- `source/raw/030-drittes-buch-zweiter-abschnitt-westlicher-zweig-pdf-337-485.txt`
- `source/raw/040-beilagen-schrift-und-polynesische-alphabete-pdf-486-582.txt`
- `source/raw/050-javanisches-alphabet-tafeln-pdf-583-609.txt`

Tracked targeted raw tranches:

- `source/raw/011-kawi-book-opening-pdf-042-047.txt`
- `source/raw/012-verbum-actuale-sein-pdf-122-124.txt`
- `source/raw/021-drittes-buch-stammverwandtschaft-method-opening-pdf-250-264.txt`
- `source/raw/022-drittes-buch-wortvergleichung-method-pdf-270-283.txt`
- `source/raw/023-feststellung-des-begriffs-des-kawi-pdf-231-246.txt`
- `source/raw/024-drittes-buch-pronomen-und-zahlwort-pdf-316-336.txt`

Tracked normalized working excerpts:

- `source/normalized/011a-kawi-language-opening-pdf-044.txt`
- `source/normalized/012a-verbum-actuale-sein-pdf-122-124.txt`
- `source/normalized/021a-stammverwandtschaft-method-opening-pdf-250-254.txt`
- `source/normalized/023a-feststellung-des-begriffs-des-kawi-opening-pdf-231-237.txt`
- `source/normalized/020a-raumverba-praepositionen-pdf-207-209.txt`
- `source/normalized/030a-tagalisch-sa-ortsbegriff-pdf-402-403.txt`

The raw text is OCR-derived and uncorrected. Use page images and hOCR before
promoting any passage.

## Structure

```text
source/
  local/                 # PDFs and IA sidecars; gitignored
  page-images/tif/       # extracted TIF page-image witness; gitignored
  full/                  # whole OCR text extracted from text PDF
  raw/                   # rough split OCR by book / appendix
  normalized/            # checked working tranches only
  witnesses.yaml
  page-map.yaml
  sections.yaml
scripts/
  extract_pdf_page_range.py
  inspect_tif_sequence.py
```

## Next Honest Moves

1. Use this shelf as the Kawi Vol. II source, not the Pott
   *Verschiedenheit* shelf.
2. Use the targeted raw and normalized tranches as local Kawi working
   surfaces: the Kawi opening, the `actuale Sein` verb passage, the
   Drittes Buch Stammverwandtschaft method and comparison passages, the
   `Raumverba`/preposition passage, the `Feststellung des Begriffs des Kawi`
   close, and the Tagalog `sa` place-concept passage.
3. Check Cassirer PSF I references against this volume before writing
   stronger claims about exact page pressure.
4. Normalize only the local tranche needed for a Cassirer/Humboldt move.
5. If page-level philology matters, inspect the TIF or hOCR witness before
   trusting the text-PDF extraction.
