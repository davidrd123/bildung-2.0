# Aristotle Core Cassirer Substrate

**Status:** Cassirer substrate shelf. This is not an Aristotle campaign and
not an attempt to unpack all Aristotle.

## Why This Exists

Cassirer's Greek pressure needs Aristotle as infrastructure for categories,
substance, predication, perception, demonstration, physics, and cosmology. The
use is broad enough to require a local source shelf, but still too diffuse to
justify a full translation or commentary project.

This pack keeps a bounded core searchable in Greek:

- `Categories`
- `De interpretatione`
- `Analytica Priora` / `Analytica Posteriora`
- `Metaphysics`
- `De anima`
- `De sensu et sensibilibus`
- `Physics`
- `De caelo`
- `Topica`
- `Sophistical Refutations`

## Source Shape

- `source/tei/` contains TEI XML fetched directly from PerseusDL or
  OpenGreekAndLatin/First1KGreek.
- `source/plain/` contains generated plain-text search surfaces.
- `source/manifest.yaml` records CTS URNs, source URLs, and edition notes.
- `source/checksums.sha256` records the local file checksums.

Use the TEI for citation-sensitive work. Use the generated plain text for
searching and quick cross-reference while reading Cassirer.
