# Peirce — *The Essential Peirce, Volume 1* — Text Scaffold

Charles S. Peirce, *The Essential Peirce, Volume 1: Selected Philosophical
Writings (1867-1893)*, edited by Nathan Houser and Christian Kloesel.

## What This Is

A split, page-referenceable scaffold of *The Essential Peirce, Volume 1* for
bounded source contact and lightweight agent work.

This exists so the volume can be touched directly in essay-scale pieces without
loading the full PDF or relying on the larger Peirce intake dump.

This is **not** a live Peirce campaign, **not** a critical edition, and **not**
a license to import Peircean vocabulary into the project as if it had already
been tested.

## Status

- The authority source remains the PDF in `sources/modern/incoming/books/peirce/`.
- The tracked text scaffold is generated from the PDF text layer with
  `pdftotext -raw`.
- The higher-quality correction path is image-grounded: render pages to `/tmp`,
  read the images directly, and save corrected page transcripts under
  `source/page-transcripts/`.
- The full intake pile under `sources/modern/incoming/books/peirce/` remains the
  raw source shelf.
- The curated extract shelf under `sources/modern/incoming/peirce/` remains the
  small first-pressure surface.
- This directory is the tracked whole-volume scaffold for Volume 1 only.
- `encounters/` and `journal.md` hold bounded source-local notes when a
  specific Peirce surface becomes useful. They do not promote this scaffold
  into a live Peirce campaign.

## Source

Authority PDF:

- `sources/modern/incoming/books/peirce/The Essential Peirce, Volume 1 Selected Philosophical.pdf`

Generated full text:

- `source/full/essential-peirce-volume-1.txt`
- `source/full/essential-peirce-volume-1.cleaned.txt`

Split browsing files:

- `source/raw/*.txt`
- `source/cleaned/*.txt`

Image-grounded transcript layer:

- `source/page-transcripts/*.txt`
- `source/page-transcripts/transcription-manifest.md`
- `source/image-grounded-cleaned/*.txt`

Manifests:

- `source/cleaned/cleanup-manifest.md`
- `source/cleaned/page-proof-manifest.md`
- `source/cleaned/ocr-uncertainties.md`

Section map:

- `source/sections.yaml`

Generation scripts:

- `tools/split_peirce_essential_volume_1.py`
- `tools/clean_peirce_essential_volume_1.py`

## Structure

```text
source/
  full/
    essential-peirce-volume-1.txt
    essential-peirce-volume-1.cleaned.txt
  raw/
    000-title-pages-and-publisher-matter.txt
    001-chronology.txt
    002-foreword.txt
    003-introduction.txt
    010-on-a-new-list-of-categories-1867.txt
    ...
    034-evolutionary-love-1893.txt
    050-notes.txt
    051-index.txt
  cleaned/
    cleanup-manifest.md
    page-proof-manifest.md
    ocr-uncertainties.md
    *.txt
  image-grounded-cleaned/
    README.md
    010-on-a-new-list-of-categories-1867.txt
  page-transcripts/
    README.md
    transcription-manifest.md
    045.txt
    046.txt
    ...
  sections.yaml
encounters/
  README.md
  01-illustrations-018-021-probability-induction-hypothesis.md
journal.md
```

## Workflow

The splitter extracts each PDF page with `pdftotext -raw`, preserves page
markers, and writes section files from fixed PDF ranges derived from the table
of contents.

The cleaner removes running heads, repairs line-break hyphenation, applies
conservative OCR cleanup, writes a cleaned full text, and updates the manifests.

Page images are intentionally not tracked. For the image-grounded pass, render
them to `/tmp/peirce_ep1_pages_300/` and treat the page image, not the OCR text
layer, as the authority. Existing raw and cleaned text may be used as drafts,
but corrected transcripts should be saved per page in `source/page-transcripts/`.
Completed image-grounded batches may then be assembled under
`source/image-grounded-cleaned/`.

## How To Use

- Use `source/cleaned/*.txt` for normal reading and bounded source checks.
- Use `source/raw/*.txt` when you need to inspect the direct PDF text-layer
  witness.
- Use `source/page-transcripts/*.txt` for pages that have been directly read
  from images.
- Use `source/image-grounded-cleaned/*.txt` for completed sections assembled
  from image-grounded page transcripts.
- Use the PDF whenever punctuation, notation, editorial symbols, or quotation
  accuracy matters.
- If a passage begins to matter beyond a local check, record that pressure in a
  separate encounter note rather than expanding this scaffold into a Peirce
  project by drift.
