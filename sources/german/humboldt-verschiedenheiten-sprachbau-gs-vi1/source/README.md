# Source Notes

This source layer holds local witnesses and extraction surfaces for Humboldt's
GS VI/1 texts currently needed by the Cassirer PSF I Humboldt map: *Ueber den
Dualis*, the plural *Verschiedenheiten* essay, and *Ueber die Verwandtschaft
der Ortsadverbien mit dem Pronomen in einigen Sprachen*.

## Witness Policy

- `source/local/gesammelteschrif06humbuoft.pdf` is the working text PDF.
- `source/page-images/jp2/` is the visual witness from the original JP2 tar.
- hOCR, page-index, search-text, and page-number sidecars are locating aids.
- `source/full/` and `source/raw/` are OCR/PDF text surfaces. They are
  searchable and useful for substrate work, but remain uncorrected.
- `source/normalized/` contains checked tranches that earned use in an actual
  reading or cross-text move.

## Current Local Artifacts

All files under `source/local/` and `source/page-images/` are gitignored.
The tracked authority surface is the metadata plus `full/`, `raw/`, and the
checked working tranches under `normalized/`.
