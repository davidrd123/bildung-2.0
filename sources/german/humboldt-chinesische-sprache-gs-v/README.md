# Humboldt - Chinese Grammar And Sprachtypus - GS V

Wilhelm von Humboldt, *Gesammelte Schriften*, Band V, Erste Abteilung:
*Werke V*, edited by Albert Leitzmann. Berlin: B. Behr's Verlag, 1906.

## What This Is

A German source-language landing zone for the GS V Humboldt pieces Cassirer
uses around the chapter I Humboldt/Kant/form cluster in PSF I:

- *Lettre a Monsieur Abel-Remusat, sur la nature des formes grammaticales en
  general, et sur le genie de la langue Chinoise en particulier*
- *Ueber den grammatischen Bau der Chinesischen Sprache*
- *Grundzuege des allgemeinen Sprachtypus*

The shelf name foregrounds the Chinese-language pair, but the same GS V witness
also carries *Grundzuege*, so that support text is landed here too.

## Source

Primary local authority copy, gitignored:

- `source/local/gesammelteschrif05humbuoft.pdf`

Internet Archive item:

- `gesammelteschrif05humbuoft`
- `https://archive.org/details/gesammelteschrif05humbuoft`

Local sidecars landed, gitignored:

- `source/local/gesammelteschrif05humbuoft_djvu.txt`
- `source/local/gesammelteschrif05humbuoft_hocr_pageindex.json`
- `source/local/gesammelteschrif05humbuoft_hocr_pageindex.json.gz`
- `source/local/gesammelteschrif05humbuoft_hocr_searchtext.txt`
- `source/local/gesammelteschrif05humbuoft_hocr_searchtext.txt.gz`
- `source/local/gesammelteschrif05humbuoft_page_numbers.json`
- `source/local/gesammelteschrif05humbuoft_files.xml`
- `source/local/gesammelteschrif05humbuoft_meta.xml`
- `source/local/gesammelteschrif05humbuoft_scandata.xml`

Page-image witness, gitignored:

- `source/local/gesammelteschrif05humbuoft_orig_jp2.tar`
- extracted to `source/page-images/jp2/gesammelteschrif05humbuoft_orig_jp2/`
- 506 JP2 files
- filename pattern `gesammelteschrif05humbuoft_orig_0000.jp2` through
  `gesammelteschrif05humbuoft_orig_0505.jp2`
- no detected gaps in the filename sequence

## Current Splits

Tracked full text:

- `source/full/gesammelte-schriften-v.txt`

Tracked raw extracts:

- `source/raw/010-lettre-a-abel-remusat-pdf-264-318.txt`
- `source/raw/020-grammatischer-bau-der-chinesischen-sprache-pdf-319-335.txt`
- `source/raw/030-grundzuege-des-allgemeinen-sprachtypus-pdf-374-485.txt`

The raw extracts are OCR/PDF-derived and uncorrected. Use page images and hOCR
before quoting or normalizing.

## Why Here

- `sources/german/` is the right layer: these are Humboldt primary-source
  surfaces used by Cassirer.
- This is a GS V witness, distinct from the GS VI/1 plural
  *Verschiedenheiten* shelf and from the Pott 1876 singular
  *Verschiedenheit* shelf.
- The Chinese-grammar pair supports Cassirer's PSF I p. 106 citation cluster.
- *Grundzuege* supports Cassirer's PSF I p. 102 chapter I form/Kant cluster.

## Structure

```text
source/
  local/                 # PDF and IA sidecars; gitignored
  page-images/jp2/       # original JP2 page-image witness; gitignored
  full/                  # whole-volume PDF/OCR text extraction
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

1. Check the Chinese-grammar extracts against JP2/hOCR before quotation,
   translation, or synthesis.
2. Use the PSF I chapter I Humboldt section when making the Cassirer-facing
   move; these extracts are the direct source pressure for that chapter cluster.
3. Keep this GS V witness distinct from Kawi, singular *Verschiedenheit*, and
   plural *Verschiedenheiten* shelves.
