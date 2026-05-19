# Source Notes

This source layer holds local witnesses and rough extraction surfaces for
Humboldt's *Kawi-Sprache*, Band II.

## Witness Policy

- `source/local/berdiekawisprac01buscgoog_text.pdf` is the working text PDF.
- `source/page-images/tif/` is the visual witness. It replaces the JP2 role
  used in the Pott *Verschiedenheit* shelf because no JP2 tar is available
  locally for this IA item.
- hOCR and page-number sidecars are locating aids. They are useful for
  alignment, but they do not by themselves make a passage normalized.
- `source/full/` and `source/raw/` are OCR surfaces. They are searchable and
  useful for substrate work, but remain uncorrected. Smaller targeted files in
  `source/raw/` are navigational working tranches, not normalized passages.
- `source/normalized/` should contain only checked tranches that earned use
  in an actual reading or cross-text move.

## Current Local Artifacts

All files under `source/local/` and `source/page-images/` are gitignored.
The tracked authority surface is the metadata plus `full/` and `raw/`.
