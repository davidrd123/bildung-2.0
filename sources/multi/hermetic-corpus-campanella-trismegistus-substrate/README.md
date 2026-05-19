# Hermetic Corpus - Campanella Trismegistus Substrate Shelf

**Status:** Live bounded substrate shelf. This is not a full Hermetica
campaign.

## Why This Exists

This shelf supports the Campanella *Metaphysica* Liber XV leaves where Mercury
Trismegistus becomes load-bearing, especially leaves 0829-0830.

The pressure is narrow but strong:

- `Asclepius` is the direct citation pressure. Leaf 0829 cites `Ascl. 4`, and
  leaf 0830 turns on the statue-making passage.
- Ficino's Latin `Pimander` is the likely Renaissance transmission layer for
  the Corpus Hermeticum material Campanella could actually have been reading.
- The Greek Corpus Hermeticum remains the critical spine for Poimandres,
  Nous/Logos/Anthropos, and monad/regeneration passages.
- The Stobaean Hermetica carry the decan, zodiacal, and `Kore Kosmou` pressure
  behind the pantomorphic material.
- Patrizi is recorded as a near-contemporary reception witness, but is held at
  the edge so this does not become a general Renaissance Hermetica project.

## Contents

- `source/manifest.yaml` - source records, pressure notes, URLs, and local
  acquisition paths.
- `extracts/` - bounded working extracts keyed to the Campanella leaf pressure.
- `source/greek/tei/` - tracked First1KGreek `tlg1286` TEI witnesses from
  Scott's 1924 *Hermetica*.
- `source/greek/plain/` - generated plain-text search surfaces from that TEI.
- `source/latin/plain/` - tracked plain-text search surfaces generated from
  the 1505 Ficino/Asclepius Wayback transcriptions.
- `source/local/` - ignored local HTML/OCR witnesses for private work.
- `source/pdf/` - ignored local PDFs and scan witnesses.

Local acquisitions currently include:

- First1KGreek `tlg1286` TEI and generated plain text for CH I-XIV, XVI-XVIII,
  Scott's Latin Asclepius witness, and Stobaei Hermetica fragments.
- Bibliotheca Augustana Greek Corpus Hermeticum I-XII HTML.
- Wayback copies and generated plain text for the 1505 Ficino `Pimander` I-XIV
  and Latin `Asclepius` transcriptions from Aussagenlogik.
- Internet Archive PDFs/OCR for Scott's *Hermetica* vol. I, the 1505 Stephanus
  Ficino/Asclepius volume, and the 1481 Ficino `Pimander` witness.
- A private local Nock-Festugiere vol. II PDF and text extraction for
  `Asclepius` / CH XIII-XVIII citation checks.
- Wachsmuth-Hense Stobaeus OCR and PDFs from Internet Archive.
- Matheson Trust Poimandres PDF for CH I.
- ONB IIIF manifest for Patrizi's 1591 *Nova de universis philosophia*.

## Use Discipline

Search `source/greek/plain/`, `source/latin/plain/`, and ignored
`source/local/` for discovery, but cite through `source/manifest.yaml` and
confirm exact claims against the critical Nock-Festugiere volumes when the
reading matters. The First1KGreek witness is Scott 1924, useful for grep-level
substrate work but not the citation authority. The Bude volumes are treated as
the reference spine, not as tracked open text.

Keep this shelf to the Schuon-sized limit: the working core is Asclepius,
Ficino's Pimander, Greek CH, Stobaean Hermetica, and Patrizi as a bounded
reception witness. Cicero, Augustine, Iamblichus, Plato, Hesiod, and technical
astrology remain comparative or reserve supports unless a leaf forces them into
the primary substrate.

The working extraction layer is controlled by `extracts/pressure-map.yaml`.
Add a new extract only when it answers a named Campanella phrase or a direct
verification gap in the existing extracts.

## Gaps

- Nock-Festugiere vol. II is now present locally under ignored `source/pdf/`
  with a private text extraction under `source/local/critical/`. Vols. I and
  III-IV remain library/borrowing acquisitions if the Greek CH or Stobaean
  pressure needs citation-critical verification.
- PerseusDL has no Hermetic corpus surface in the checked canonical Greek tree.
- First1KGreek `tlg1286` uses Walter Scott's 1924 edition, not
  Nock-Festugiere. This is adequate for search but needs Bude verification for
  citation-critical use.
- The Stobaeus OCR and First1KGreek fragment surface are useful for discovery,
  but fragment mapping still needs to be checked against Nock-Festugiere
  volumes III-IV.
- Patrizi is recorded by stable scan/IIIF surfaces, and the ONB IIIF manifest
  is local, but no full Patrizi text extraction is part of the shelf yet.
