# Tektologiya Visuals

This folder is the local home for Tektologiya's earned `[visual candidate]`
work.

For now it is intentionally smaller than `texts/zeitmauer/visuals/`. The first
job here is not image generation but curation: selecting which diagrams would
actually help a reader grasp the architecture of volume `1`.

## Current contents

- `packet-01-volume-1-architecture.md` — the first curated packet of
  architectural diagrams, drafted directly from journal candidates
- `plates/01-volume-1-arc.svg` and `plates/02-mechanism-split.svg` — the first
  rendered SVG plates from packet `01`
- `keepers/` — first prompt-only Gemini keepers for the volume arc and
  mechanism split

## Rule

Visual work begins from review-noted candidates in the journal, not from
arbitrary prompting.

The packet notes here are derived exploratory artifacts. They do not replace
the journal, the glossary, or the translation batches.

Repo policy:

- `visuals/out/` is local scratch for raw Gemini runs and compare metadata
- `keepers/` is the curated layer worth carrying in git
- `plates/raster-ref/` is temporary conversion material, not a durable asset layer

## Later use

If image generation is resumed, mirror the lighter workflow already tested in
[`texts/zeitmauer/visuals/README.md`](../../zeitmauer/visuals/README.md)
and keep provenance tied back to the originating `[visual candidate]` lines.

For Tektologiya so far, the strongest lever is a highly specific prompt rather
than the SVG anchor. Use the SVGs as fallback control surfaces when branching
logic or stage order starts drifting, not as the default starting point.
