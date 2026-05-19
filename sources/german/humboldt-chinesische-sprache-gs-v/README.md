# Humboldt - Chinese Language Writings - GS V

Wilhelm von Humboldt, *Gesammelte Schriften*, Band V, Erste Abteilung:
*Werke V*, edited by Albert Leitzmann. Berlin: B. Behr's Verlag, 1906.

## What This Is

A German source-language landing zone for the GS V witness that contains
Humboldt's Chinese-language essays Cassirer cites in PSF I:

- *Lettre a Monsieur Abel-Remusat, sur la nature des formes grammaticales en
  general, et sur le genie de la langue Chinoise en particulier*
- *Ueber den grammatischen Bau der Chinesischen Sprache*

The same GS V volume also contains *Grundzuege des allgemeinen Sprachtypus*,
so this shelf now covers that short theoretical support as well.

This is not a promoted Humboldt campaign. It is a source scaffold for
Cassirer-facing substrate work where non-Indo-European language form,
grammatical categories, and the form-of-language question become active.

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
- `source/local/gesammelteschrif05humbuoft_scandata.xml`
- `source/local/gesammelteschrif05humbuoft_files.xml`
- `source/local/gesammelteschrif05humbuoft_meta.xml`

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
- `source/raw/020-grammatischer-bau-der-chinesischen-sprache-pdf-319-334.txt`
- `source/raw/030-grundzuege-des-allgemeinen-sprachtypus-pdf-373-485.txt`

The raw text is OCR/PDF-derived and uncorrected. Use page images and hOCR
before quoting or normalizing.

One boundary caveat: *Grundzuege* begins on the same PDF page as the tail of
the preceding American-languages fragment. The raw extract starts at PDF page
373 to preserve the title page; that first page therefore includes a small
amount of preceding material before the *Grundzuege* title.

## Why Here

- `sources/german/` is the right layer for the GS V German/French primary
  witness.
- Cassirer cites the Abel-Remusat letter and the German Chinese grammar essay
  together at PSF I p. 106.
- *Grundzuege des allgemeinen Sprachtypus* is cited at PSF I p. 102 and lives
  in the same GS V witness.
- Keeping these texts together makes the Chinese-language pressure visible
  without folding it into the singular *Verschiedenheit* or Kawi shelves.

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

1. Use this shelf for the GS V Chinese-language pair and *Grundzuege* support
   only.
2. Check raw extracts against JP2/hOCR before quotation, translation, or
   synthesis.
3. Pull smaller normalized tranches only when Cassirer PSF I chapter I pressure
   demands them.
4. Keep the non-Indo-European language-form angle distinct from the Kawi and
   singular/plural *Verschiedenheit* lines.
