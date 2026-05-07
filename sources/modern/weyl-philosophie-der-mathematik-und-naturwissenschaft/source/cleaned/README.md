# Cleaned Text Layer

This directory contains a chapter-split German working text for Hermann Weyl's
*Philosophie der Mathematik und Naturwissenschaft*.

## Source Method

- `source/page-images/jpg-200/page-*.jpg` is the visual authority.
- `source/ocr/tesseract-deu/pages/page-*.txt` is the ignored draft OCR layer.
- `tools/build_weyl_cleaned_text.py` generated these files from the German OCR
  draft and the visually inspected `source/sections.yaml` map.
- `004-front-contents.txt` is a manually curated visual transcription because
  OCR turned the contents dot leaders into unusable noise; the generator
  preserves that file if it already exists.
- `016-appendix-c-quantenphysik-und-kausalitaet.txt` has manual visual
  corrections for the projection/gitter formulas around printed pages 327-329;
  the generator preserves that file if it already exists.
- `017-appendix-d-chemische-valenz.txt` has manual visual corrections for
  spin, valence, invariant, and benzene-resonance notation around printed pages
  341-349; the generator preserves that file if it already exists.
- Every cleaned file preserves page anchors of the form
  `[[pdf-page:0000 printed-page:0]]`.

## Current Quality

This is a usable cleaned working layer, not a critical edition.

The prose OCR is generally strong. The largest remaining risks are formulas,
tables, Greek/math symbols, and pages where figures interrupt the body text.
Those passages should be checked against the page images before quotation or
translation.

Visual spot checks were made against:

- title/front matter and contents: PDF pages 1, 2, 6, 8, 10, 11, 12, 14, 16
- major section starts: PDF pages 17, 48, 92, 126, 178, 211, 280, 304, 325,
  342, 355, 369, 396, 402
- risk pages: PDF pages 20, 21, 48, 126, 211, 240, 280, 325, 342,
  349, 369, 407

Known patterns to re-check in close reading:

- logical notation: OCR can confuse `Π`, `Σ`, `∃`, and ordinary Latin letters
- mathematical formulas: OCR can flatten superscripts/subscripts and signs
- figure-heavy pages: captions are usually usable, but diagram labels can leak
  into prose
- accented names: common cases such as `Kekulé` were normalized, but not all
  names have been exhaustively checked
