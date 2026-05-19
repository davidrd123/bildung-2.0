# Source Layout

This directory holds the local witness and future extraction layers for
Humboldt's *Ueber die Verschiedenheit des menschlichen Sprachbaues*.

## Local Witnesses

- `local/` - gitignored local PDF witness.
- `page-images/jp2/` - gitignored incoming page-image witness.

The PDF and page images are authority surfaces for checking extraction and OCR.
They are not tracked in git.

Internet Archive sidecars should also stay in `local/`: `HOCR`, `CHOCR`,
`FULL TEXT`, `OCR SEARCH TEXT`, `OCR PAGE INDEX`, and `PAGE NUMBERS JSON`.
Record landed sidecars in `witnesses.yaml` before using them as evidence.

## Future Text Layers

- `full/` - whole-text extraction, once there is a chosen OCR or PDF text
  witness.
- `raw/` - split browsing files, preserving edition seams as much as practical.
- `normalized/` - checked working tranches only where bounded source work
  requires them.

No text extraction has been promoted here yet.

## Working Pattern

- Use original JP2 images as the preferred visual witness once they land.
- Use PDF text and IA full/search text for locating, not as settled copy.
- Use HOCR/CHOCR only after inspecting their page alignment against images.
- Add page anchors to `page-map.yaml` before making raw or normalized tranches.
