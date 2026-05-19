# Humboldt - *Ueber das vergleichende Sprachstudium* - GS IV

Wilhelm von Humboldt, *Gesammelte Schriften*, Band IV, Erste Abteilung:
*Werke IV*, edited by Albert Leitzmann. Berlin: B. Behr's Verlag, 1905.

## What This Is

A German source-language landing zone for *Ueber das vergleichende
Sprachstudium in Beziehung auf die verschiedenen Epochen der
Sprachentwicklung* in the GS IV witness.

This shelf exists because Cassirer cites this academy-address comparative
language frame at PSF I pp. 100 and 102. It completes the immediate short
Humboldt support set alongside GS V *Grundzuege* and GS VI/1 *Dualis*.

This is not a promoted Humboldt campaign. It is a source scaffold for
Cassirer-facing substrate work.

## Source

Primary local authority copy, gitignored:

- `source/local/gesammelteschrif04humbuoft.pdf`

Internet Archive item:

- `gesammelteschrif04humbuoft`
- `https://archive.org/details/gesammelteschrif04humbuoft`

Local sidecars landed, gitignored:

- `source/local/gesammelteschrif04humbuoft_djvu.txt`
- `source/local/gesammelteschrif04humbuoft_hocr_pageindex.json`
- `source/local/gesammelteschrif04humbuoft_hocr_pageindex.json.gz`
- `source/local/gesammelteschrif04humbuoft_hocr_searchtext.txt`
- `source/local/gesammelteschrif04humbuoft_hocr_searchtext.txt.gz`
- `source/local/gesammelteschrif04humbuoft_page_numbers.json`
- `source/local/gesammelteschrif04humbuoft_scandata.xml`
- `source/local/gesammelteschrif04humbuoft_files.xml`
- `source/local/gesammelteschrif04humbuoft_meta.xml`

Page-image witness, gitignored:

- `source/local/gesammelteschrif04humbuoft_orig_jp2.tar`
- extracted to `source/page-images/jp2/gesammelteschrif04humbuoft_orig_jp2/`
- 500 JP2 files
- filename pattern `gesammelteschrif04humbuoft_orig_0000.jp2` through
  `gesammelteschrif04humbuoft_orig_0499.jp2`
- no detected gaps in the filename sequence

IA metadata reports `imagecount=460`, but the original JP2 tar landed locally
with 500 files. The landed page-image sequence is what this shelf records.

## Current Splits

Tracked full text:

- `source/full/gesammelte-schriften-iv.txt`

Tracked raw extract:

- `source/raw/010-ueber-das-vergleichende-sprachstudium-pdf-011-044.txt`

The raw extract covers PDF pages 11-44, corresponding to printed pages 1-34.
PDF page 45 opens *Ueber die Aufgabe des Geschichtschreibers*, confirming the
right boundary. The IA page-number JSON is imperfect at the opening; it begins
useful numbering inside this range at leaf 13 / printed page 2.

The raw text is OCR/PDF-derived and uncorrected. Use page images and hOCR
before quoting or normalizing.

## Why Here

- `sources/german/` is the right layer: this is a German primary source.
- This is a GS IV witness, not the GS V Chinese-language shelf and not the
  GS VI/1 Dualis/plural *Verschiedenheiten* shelf.
- The shelf supports Cassirer's PSF I citations to the comparative-language
  address at PSF I pp. 100 and 102.

## Structure

```text
source/
  local/                 # PDF and IA sidecars; gitignored
  page-images/jp2/       # original JP2 page-image witness; gitignored
  full/                  # whole-volume PDF text extraction
  raw/                   # uncorrected bounded extracts
  normalized/            # future checked tranches only
  witnesses.yaml
  page-map.yaml
  sections.yaml
scripts/
  extract_pdf_page_range.py
  inspect_jp2_sequence.py
```

## Next Honest Moves

1. Check the raw extract against JP2/hOCR before quotation, translation, or
   synthesis.
2. Use this shelf only for the GS IV comparative-language address unless later
   Cassirer pressure demands another GS IV text.
3. Keep this short support distinct from *Grundzuege*, *Dualis*, Kawi, and the
   singular/plural *Verschiedenheit* shelves.
