# Dogen - *Treasury of the True Dharma Eye* - Tanahashi English Scaffold

Eihei Dogen, *Treasury of the True Dharma Eye: Zen Master Dogen's Shobo Genzo*,
edited by Kazuaki Tanahashi (Shambhala, 2012).

## What This Is

A lightweight English translation scaffold for navigation and bounded comparison.
It splits the incoming Tanahashi text into fascicle-scale files, plus front matter,
period containers, appendixes, glossary, bibliography, and credits.

This is **not** a Japanese source witness and **not** a live Dogen campaign. The
Japanese source-language pilot currently remains:

- `sources/japanese/dogen-shobogenzo-uji/`

Use this scaffold when an English translation witness is helpful beside the
modern Japanese `Uji` extraction or later source-language fascicle work.

## Source

Incoming text:

- `sources/japanese/incoming/Treasury of the True Dharma Eye - Dogen.txt`

The full normalized copy is stored at:

- `source/full/treasury-of-the-true-dharma-eye-tanahashi.txt`

## Structure

```text
source/
  full/
    treasury-of-the-true-dharma-eye-tanahashi.txt
  raw/
    000-front-matter-and-contents.txt
    001-preface-and-acknowledgments.txt
    002-notes-to-the-reader.txt
    003-editors-introduction.txt
    004-texts-in-relation-to-dogens-life-and-translation-credits.txt
    005-wandering-period.txt
    006-1-on-the-endeavor-of-the-way.txt
    ...
    018-12-the-time-being.txt
    ...
    037-31a-continuous-practice-part-one.txt
    038-31b-continuous-practice-part-two.txt
    ...
    120-credits.txt
  sections.yaml
```

## Split Logic

This is a navigational split, not a scholarly edition.

The segmentation preserves:

- front matter and contents
- preface, reader notes, editor introduction
- the life/translation-credit apparatus as one large source-apparatus file
- period containers (`Wandering Period`, `Kosho Monastery Period`, etc.)
- the full numbered fascicle sequence, with `31A` and `31B` kept as distinct
  split files
- afterword, appendixes, glossary, selected bibliography, and credits

`sections.yaml` records sequence, file, kind, slug, title, optional fascicle
number, parent, and original incoming-text line range.

## Status

- 2026-05-05: scaffold created from the incoming Tanahashi English text.
- 2026-05-05: 121 split files generated and `sections.yaml` verified for
  sequential line coverage.

Nothing here promotes Dogen into a full repo subproject. The immediate useful
role is bounded comparison against the already-localized `Uji` material.

## Reproducibility

Regenerate the split with:

```bash
python3 tools/split_dogen_tanahashi.py
```

If the incoming text changes, rerun the splitter rather than editing generated
raw files by hand.
