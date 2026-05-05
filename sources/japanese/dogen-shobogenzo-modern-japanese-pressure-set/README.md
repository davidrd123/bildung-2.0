# Dogen - *Shobogenzo* - Modern Japanese Pressure Set

Bounded source-language scaffold from the repo-local, gitignored
`Shobo Gendaigoyaku` PDFs.

## What This Is

This directory collects the small Dogen pressure set currently relevant to the
repo: modern Japanese renderings of the fascicles most likely to matter for
`Uji`, translation/decryption practice, formation, embodied knowing, worldhood,
language, and transmission.

It is **modern Japanese**, not original/classical Dogen. It is also **not** a
full Dogen campaign and **not** a complete import of the twelve-volume PDF set.
The point is to make the pressure-bearing modernizations available for
source-near comparison without pretending the whole corpus has opened.

## Included Fascicles

```text
source/raw/
  001-bendowa.txt          # practice-realization frame
  002-genjo-koan.txt       # actualization / self-world relation
  003-uji.txt              # being-time anchor
  004-sansuigyo.txt        # mountains, waters, worldhood
  005-gyoji-1.txt          # continuous practice, part one
  006-gyoji-2.txt          # continuous practice, part two
  007-shinjin-gakudo.txt   # body-and-mind study
  008-dotoku.txt           # expression / language
  009-zenki.txt            # undivided activity
  010-katto.txt            # twining vines / transmission entanglement
```

Use `source/sections.yaml` for the PDF source path, English witness pointer,
line count, and reason each fascicle was admitted to the set.

## Extraction

The PDF authority shelf is:

```text
sources/japanese/incoming/shobo-gendaigoyaku/
  Vol01/
  Vol02/
  ...
  Vol12/
```

The whole `sources/japanese/incoming/` directory is gitignored. These PDFs are
kept there so local machines can sync the source payload without putting it in
Git or depending on a `Downloads` path.

The parallel bilingual witness shelf is:

```text
sources/japanese/incoming/eng-jap-shobo/
  Vol. 1/
  Vol. 2/
  Vol. 3/
  Vol. 4/
```

These PDFs place Japanese text and the Nishijima/Cross English translation on
facing columns. They are useful as a phrase-level translation witness, not as
the source authority. `source/sections.yaml` records them as
`parallel_witness_pdf` where this partial set covers the pressure fascicle:
`Bendowa`, `Genjo-koan`, `Uji`, `Sansuigyo`, `Gyoji` 1/2, and `Dotoku`.
`Shinjin-gakudo`, `Zenki`, and `Katto` have no matching bilingual PDF in this
local set.

Each file was extracted directly from its PDF with:

```bash
pdftotext -raw <source-pdf> <target-txt>
```

The raw extraction preserves the PDF text layer as-is. It has not been cleaned,
normalized, line-wrapped, or checked against classical Japanese.

## Relation To Other Dogen Scaffolds

- `sources/japanese/dogen-shobogenzo-uji/` remains the single-fascicle Uji pilot
  that already existed before this pressure set. It now contains a separate
  `source/original/020-uji.txt` original/classical layer; its
  `source/modern-japanese-raw/` file remains the raw modern Japanese witness.
- `sources/japanese/dogen-shobogenzo-tanahashi-en/` is the English Tanahashi
  translation witness, split for comparison and navigation.
- This pressure set is the bounded modern-Japanese companion to both.

## Status

- 2026-05-05: extracted 10 raw files from the local PDFs.
- 2026-05-05: wrote `source/sections.yaml` with pressure roles and English
  witness links.
- 2026-05-05: added repo-local pointers to the partial bilingual
  Japanese/English PDF witness set where available.
- 2026-05-05: linked Uji to the separate original/classical text layer in the
  single-fascicle Uji scaffold.

Next honest move, if needed: choose one pressure question and read one fascicle
against `Uji`. Do not widen to the full Dogen corpus unless a later source
problem actually forces it.
