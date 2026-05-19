# PSF Direct Volume-Folder Substrate

**Status:** Working substrate decision. This records a scope adjustment, not a
promotion of PSF into a `texts/` campaign.

## Trigger

The May 2026 substrate/engagement clarification makes it legitimate to unpack
Cassirer's localized *Philosophie der symbolischen Formen* volumes inside
`sources/german/` without treating that work as a full symbolic-forms project.

The earlier two-chapter framing was too narrow for the actual use case. The
follow-up correction was also concrete: web readers and agents need the text
files directly inside volume folders, split by chapter, so they can search and
engage without knowing an internal raw/normalized staging convention.

## Current Scope

The justified substrate target is **all localized PSF volumes as direct
chapter-folder substrate**:

- whole-volume search through `source/full/*.txt`
- direct chapter/back-matter files in:
  - `source/vol1-die-sprache/`
  - `source/vol2-das-mythische-denken/`
  - `source/vol3-phaenomenologie-der-erkenntnis/`
- web/search metadata through `source/search-surfaces.yaml`
- closer normalized tranches where the reading task has already forced them

The introduction and chapter V remain priority anchors because they already
carry the current repo pressure:

1. **Einleitung und Problemstellung**, especially section I, where Cassirer
   defines symbolic form, objectivation, functional unity, and the move from
   critique of reason toward critique of culture.
2. **Kapitel V**, where relation-expression becomes a language-medium problem:
   sentence before word, parataxis/hypotaxis, relation words, copula, and the
   history of `sein` as more than pure predicative linkage.

But these are now anchors inside an all-volume substrate, not the boundary of
the search surface.

Existing anchors:

- [cassirer-psf-i-intro-symbolic-form-and-objectivation.md](/Users/daviddickinson/Projects/Lora/bildung-2.0/00-Notes/method/cassirer-psf-i-intro-symbolic-form-and-objectivation.md:1)
- [cassirer-psf-i-ch5-relation-expression.md](/Users/daviddickinson/Projects/Lora/bildung-2.0/00-Notes/method/cassirer-psf-i-ch5-relation-expression.md:1)
- [README.md](/Users/daviddickinson/Projects/Lora/bildung-2.0/sources/german/cassirer-philosophie-der-symbolischen-formen/README.md:1)
- [search-surfaces.yaml](/Users/daviddickinson/Projects/Lora/bildung-2.0/sources/german/cassirer-philosophie-der-symbolischen-formen/source/search-surfaces.yaml:1)

## Why This Is Legitimate Now

The substrate note clarified that source work does not promote itself by
volume. `sources/` can build corrected, navigable, chapter-scale apparatus so
future conversations can locate the source's argument quickly. Promotion to
`texts/` requires engagement artifacts: bounded reading notes that make
structural findings about the argument, close-reading ledger entries, and a
journal that synthesizes what the work is doing rather than only where the
source has been indexed.

PSF has not earned that engagement layer. But it has earned enough pressure to
justify all-volume substrate because current and future repo questions need to
be able to search and re-enter the texts without treating a few favorite
passages as the whole work.

## Web/Search Requirement

For web-facing use, the source must be searchable at multiple resolutions:

- full-volume phrase search
- direct chapter-level browsing and engagement
- normalized citation surfaces where they exist

This is why the new search-surface index is part of the substrate. A web layer
or agent should be able to ask "where is Cassirer discussing X in PSF?" and
land on a volume folder or chapter surface immediately, while still seeing
whether the passage is rough extraction or normalized working text.

## Guardrails

This licenses:

- full PSF I-III search substrate
- metadata for web/export/search use
- normalized tranches as needed by later reading tasks
- compact source-facing method notes

It does not license:

- a stable PSF glossary
- engagement activation of PSF II or PSF III by substrate availability
- treating `symbolic form` as repo-wide master vocabulary
- promoting the source scaffold to `texts/`

## Next Honest Move

Keep PSF I-III searchable as a whole and by direct chapter file. Extend
normalization only where future use needs more than rough search and
navigation. Do not treat Volumes II or III as engagement-active unless a
specific reading task forces them.
