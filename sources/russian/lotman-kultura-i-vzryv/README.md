# Lotman - *Культура и взрыв* - Cleanup Scaffold

Ю. М. Лотман, *Культура и взрыв* (Москва: Гнозис; Издательская группа
«Прогресс», 1992).

## What This Is

A source-language cleanup scaffold for producing a page-image-proofed Russian
text of *Культура и взрыв*.

The target is clean text suitable for downstream audiobook/script generation,
not an English translation and not a critical edition. The cleaned corpus should
preserve page markers, headings, footnotes, contents, and publication matter
while correcting OCR damage against page images.

## Status

- Canonical local source: `source/local/lotman-kultura-i-vzryv.djvu`.
- The local DjVu is intentionally gitignored.
- Raw OCR has been extracted into `source/raw/pages/NNN.txt`.
- Chapter-scale raw OCR splits have been generated under `source/raw/`.
- Page images have been rendered to `source/page-images/pages/NNN.png`.
- Rendered page images are intentionally gitignored proof aids.
- The OCR layer is useful as a scaffold but has visible Russian OCR damage.
- Page-image-proofed cleaned text has been completed under `source/cleaned/`
  for all mapped sections, scans 001-273.
- See `source/cleaned/cleanup-manifest.md`,
  `source/cleaned/page-proof-manifest.md`, and `journal.md` for proof status
  and cleanup decisions.

## Structure

```text
source/
  local/                 # gitignored DjVu authority
  raw/
    pages/               # page-level OCR, with [scan page NNN] markers
    000-*.txt            # section-level OCR splits
    full-ocr.txt         # combined OCR dump
    metadata.yaml        # extraction metadata
  page-images/           # gitignored rendered PNG page images
  cleaned/               # target page-proofed Russian text and ledgers
  sections.yaml          # section map from scan pages to printed pages
journal.md               # local state and decisions
```

## How To Use

- Use `source/page-images/pages/NNN.png` as the visual authority.
- Use `source/raw/pages/NNN.txt` as the page OCR scaffold.
- Use `source/sections.yaml` to work section by section.
- Write checked text under `source/cleaned/`.
- Update `source/cleaned/page-proof-manifest.md` as each page range is proved.

Regenerate the raw scaffold and local images with:

```bash
python3 tools/extract_lotman_kultura_pages.py --images
```

The generated raw text is tracked. The DjVu and rendered images are local proof
artifacts and should remain out of git.
