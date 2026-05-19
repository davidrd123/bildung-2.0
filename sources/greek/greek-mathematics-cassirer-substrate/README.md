# Greek Mathematics Cassirer Substrate

**Status:** Cassirer substrate shelf. This is a search surface for the Greek
mathematical tradition Cassirer pressures; it is not a full ancient mathematics
campaign.

## Why This Exists

Cassirer repeatedly uses Greek mathematics as a model for construction,
relation, deduction, and scientific objectivity. Euclid is the first pressure
point. Proclus matters because Cassirer's philosophical account of Greek
geometry often runs through ancient commentary on Euclid. Archimedes,
Apollonius, and Ptolemy support the later Galilei/Kepler/mathematical-physics
line.

## Source Shape

- `source/tei/` contains TEI XML fetched directly from PerseusDL or
  OpenGreekAndLatin/First1KGreek.
- `source/plain/` contains generated plain-text search surfaces.
- `source/ocr/` contains Internet Archive OCR for Proclus on Euclid Book I.
- `source/manifest.yaml` records CTS URNs, source URLs, and edition notes.
- `source/checksums.sha256` records the local file checksums.

Proclus is OCR-only here. Use it for discovery and search, then verify any
citation-sensitive passage against the scan or a critical edition.
