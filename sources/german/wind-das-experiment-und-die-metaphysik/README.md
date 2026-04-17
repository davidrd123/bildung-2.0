# Wind — *Das Experiment und die Metaphysik* — Text-Only Scaffold

Edgar Wind, *Das Experiment und die Metaphysik: Zur Auflösung der kosmologischen Antinomien* (Tübingen: J. C. B. Mohr / Paul Siebeck, 1934).

## What This Is

A split, navigable German source scaffold for passage-level browsing in chats and lightweight agent work.

This exists for the same reason as the Grothendieck and Lotman scaffolds already in the repo: so a conversation can read a bounded section of the book without loading the entire OCR dump at once.

This is **not** a live encounter, **not** a source-critical working text, and **not** a promoted subproject. It is a localized browsing surface only.

## Source

The scaffold was generated from a local page-level OCR dump:

- `/Users/daviddickinson/Downloads/$b44030/`
  - 140 page files (`UCAL_$B44030_00000001.txt` … `UCAL_$B44030_00000140.txt`)
  - the book text itself ends on page 136
  - pages 137–140 are blank / library-artifact residue and are not part of the scaffolded text

No page-image PDF or EPUB witness is currently vendored into the repo. The split therefore rests on OCR only.

## Why Here

- Not `texts/` — no glossary, journal, or encounter dossiers have been earned.
- Not `sources/modern/` — this is a German primary text, not a modern concept encounter.
- `sources/german/` is the least misleading place for a source-language scaffold that may later support bounded source work.

## Structure

```text
source/
  raw/                   # 42 split OCR-derived files
  sections.yaml          # sequence, title, kind, parent, page-line span
```

Current granularity:

- front matter
- Schlegel epigraph
- `Vorwort`
- `Inhaltsverzeichnis`
- Part I container + `§§ 1–11`
- Part II container + `§ 12`
- chapter containers for the four antinomy chapters
- `§§ 13–32`

Not yet created:

- `source/normalized/`
- `journal.md`
- `glossary.yaml`
- `encounters/`

## Status and Limits

- The raw files are OCR-derived and lightly cleaned for browsing:
  - top-of-page running headers and bottom-of-page footer residue were stripped where possible
  - obvious blank interstitial pages and late library-slip pages were excluded
- The text is good enough for orientation, browsing, and exploratory web chat.
- It is **not** yet good enough for fine lexical work, quotation discipline, or glossary building without a better witness.
- The two figures named in the book survive only as textual references (`Fig. 1.` / `Fig. 2.`); the image content itself is not extracted here.

## How To Use

- Read `source/raw/*.txt` when you want section-scale access.
- Use `source/sections.yaml` when you need reading order, titles, parents, and original page-line spans.
- Treat this as a browsing aid, not as an authority surface.

If later work shows that Wind is exerting real pressure on the repo, the next honest move would be a checked working text for whichever bounded axis wakes first. Until then, this scaffold is just navigational infrastructure.
