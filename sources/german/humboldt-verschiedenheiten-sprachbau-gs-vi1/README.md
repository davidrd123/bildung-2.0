# Humboldt - GS VI/1: *Dualis*, Plural *Verschiedenheiten*, and *Ortsadverbien*

Wilhelm von Humboldt, *Gesammelte Schriften*, Band VI, Erste Abteilung:
*Werke VI*, Erste Haelfte, edited by Albert Leitzmann. Berlin: B. Behr's
Verlag, 1907.

## What This Is

A German source-language landing zone for GS VI/1 Humboldt materials that
Cassirer cites in PSF I, currently:

- *Ueber den Dualis*
- *Ueber die Verschiedenheiten des menschlichen Sprachbaues*
- *Ueber die Verwandtschaft der Ortsadverbien mit dem Pronomen in einigen
  Sprachen*

This shelf exists to keep the plural *Verschiedenheiten* essay separate from
the singular *Ueber die Verschiedenheit des menschlichen Sprachbaues* shelf at
`sources/german/humboldt-verschiedenheit-sprachbau/`.

Cassirer's PSF I Schriftenregister cites both titles. They should not be
collapsed.

## Source

Primary local authority copy, gitignored:

- `source/local/gesammelteschrif06humbuoft.pdf`

Internet Archive item:

- `gesammelteschrif06humbuoft`
- `https://archive.org/details/gesammelteschrif06humbuoft`

Local sidecars landed, gitignored:

- `source/local/gesammelteschrif06humbuoft_djvu.txt`
- `source/local/gesammelteschrif06humbuoft_hocr_pageindex.json`
- `source/local/gesammelteschrif06humbuoft_hocr_pageindex.json.gz`
- `source/local/gesammelteschrif06humbuoft_hocr_searchtext.txt`
- `source/local/gesammelteschrif06humbuoft_hocr_searchtext.txt.gz`
- `source/local/gesammelteschrif06humbuoft_page_numbers.json`
- `source/local/gesammelteschrif06humbuoft_files.xml`
- `source/local/gesammelteschrif06humbuoft_meta.xml`

Page-image witness, gitignored:

- `source/local/gesammelteschrif06humbuoft_orig_jp2.tar`
- extracted to `source/page-images/jp2/gesammelteschrif06humbuoft_orig_jp2/`
- 368 JP2 files
- filename pattern `gesammelteschrif06humbuoft_orig_0000.jp2` through
  `gesammelteschrif06humbuoft_orig_0367.jp2`
- no detected gaps in the filename sequence

## Current Splits

Tracked full text:

- `source/full/gesammelte-schriften-vi1.txt`

Tracked raw extracts:

- `source/raw/005-ueber-den-dualis-pdf-014-040.txt`
- `source/raw/010-ueber-die-verschiedenheiten-pdf-121-313.txt`
- `source/raw/020-ueber-die-verwandtschaft-ortsadverbien-pronomen-pdf-314-340.txt`

The Dualis raw extract covers PDF pages 14-40, corresponding to printed pages
4-30. PDF page 41 opens the Sanskrit word-separation memoir, confirming the
right boundary. The IA page-number JSON is sparse at the beginning of the
Dualis range, so this range is bounded by PDF/text inspection.

The plural *Verschiedenheiten* raw extract covers PDF pages 121-313,
corresponding to the plural essay opening through the page before *Ueber die
Verwandtschaft der Ortsadverbien mit dem Pronomen in einigen Sprachen* begins.
Printed pages are 111-303.

The *Ortsadverbien* raw extract covers PDF pages 314-340, corresponding to
printed pages 304-330. PDF page 341 opens Leitzmann's
*Bemerkungen zur Entstehungsgeschichte der einzelnen Aufsaetze*, confirming the
right boundary.

The raw text is OCR/PDF-derived and uncorrected. Use page images and hOCR
before quoting or normalizing.

## Why Here

- `sources/german/` is the right layer: this is a German primary source.
- This is a GS VI/1 witness, not the 1876 Pott witness and not the 1838 Kawi
  witness.
- The shelf supports Cassirer's PSF I citations to *Ueber den Dualis* at PSF I
  pp. 168, 196 f., 206, and 213.
- The shelf supports Cassirer's PSF I citations to the plural essay at PSF I
  pp. 100 f., 206, and 257.
- The shelf supports Cassirer's PSF I citations to *Ueber die Verwandtschaft
  der Ortsadverbien mit dem Pronomen in einigen Sprachen* at PSF I pp. 153,
  164, 166, 213, 216, and 225.

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

1. Use this shelf for the GS VI/1 texts Cassirer actually cites: Dualis,
   plural *Verschiedenheiten*, and *Ortsadverbien*.
2. Check raw extracts against JP2/hOCR before any quotation, translation, or
   synthesis.
3. Pull smaller targeted tranches only when Cassirer's PSF I page pressure
   demands them.
4. Keep the singular/plural title distinction visible in downstream notes.
