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

Local support witness (gitignored):

- `source/local/experiment-and-metaphysics-translation-cyril-edwards.pdf`
  - local English translation for continuity of reading and secondary seam-checking
  - useful for catching omissions or OCR breakage
  - not authoritative for German wording, punctuation, or lexical pressure

No page-image PDF or EPUB witness is currently vendored into the repo. The split therefore rests on OCR only.

## Why Here

- Not `texts/` — no glossary, journal, or encounter dossiers have been earned.
- Not `sources/modern/` — this is a German primary text, not a modern concept encounter.
- `sources/german/` is the least misleading place for a source-language scaffold that may later support bounded source work.

## Structure

```text
source/
  local/                 # gitignored support witness
  raw/                   # 42 split OCR-derived files
  normalized/            # cautious working tranche (currently §§ 12–32)
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

- `journal.md`
- `glossary.yaml`
- `encounters/`

## Normalized Tranche

The current bounded `normalized/` layer stays deliberately selective:

- `017-part-ii-s12-empirische-kriterien-der-metaphysik.txt`
  - continuity-checked against the local English translation
  - intrusive note lines moved out of the prose body and obvious page-seam noise repaired conservatively
- `019-part-ii-ch1-s13-praezisierung-der-ersten-antinomie.txt`
- `020-part-ii-ch1-s14-mathematische-antinomie-des-euklidischen-raumes.txt`
- `021-part-ii-ch1-s15-physikalische-antinomie-des-newtonschen-systems.txt`
- `022-part-ii-ch1-s16-zwangslaeufigkeit-der-newtonschen-antinomie.txt`
- `023-part-ii-ch1-s17-kants-interpretation-des-absoluten-raumes.txt`
- `024-part-ii-ch1-s18-methodische-folgerung.txt`
- `025-part-ii-ch1-s19-mathematische-loesung-der-euklidischen-antinomie.txt`
- `026-part-ii-ch1-s20-physikalische-loesung-der-newtonschen-antinomie.txt`
- `027-part-ii-ch1-s21-prinzip-der-inneren-grenzsetzung.txt`
- `029-part-ii-ch2-s22-innere-grenze-des-teilungsvollzuges.txt`
- `030-part-ii-ch2-s23-zwei-formen-der-unsicherheit.txt`
- `032-part-ii-ch3-s24-heterogenitaet-und-notwendigkeit.txt`
- `033-part-ii-ch3-s25-zeitverhaeltnis-der-dynamischen-verknuepfung.txt`
- `034-part-ii-ch3-s26-spielraum-der-gegenwart.txt`
- `035-part-ii-ch3-s27-linearer-und-konfiguraler-zeitablauf.txt`
- `036-part-ii-ch3-s28-innere-grenzsetzung-und-indetermination.txt`
- `037-part-ii-ch3-s29-konstanz-und-emergenz.txt`
- `038-part-ii-ch3-s30-zeitanfang-und-ende.txt`
- `039-part-ii-ch3-s31-freiheit-unter-der-bedingung-des-naturgesetzes.txt`
- `041-part-ii-ch4-s32-mass-des-zufalls.txt`
  - same bounded repair standard
  - together they normalize the full first world-concept chapter (`§§ 13–21`), the full atom-concept chapter (`§§ 22–23`), the full causality/freedom chapter (`§§ 24–31`), and the final modality section (`§ 32`)
  - at the current scaffold granularity this reaches the end of the source section run
  - a small number of formula / note restorations (`§ 15`, `§ 20`, the chapter-III figure labels / spilled notes in `§§ 25–26`, `§ 28`, and a handful of OCR seam repairs in `§ 32`) are supported only by the English witness or by OCR seam repair and should be treated as provisional rather than source-critical

This layer is still below source-critical confidence. It is a cautious German working surface for bounded reading, not a quoting authority.

## Status and Limits

- The raw files are OCR-derived and lightly cleaned for browsing:
  - top-of-page running headers and bottom-of-page footer residue were stripped where possible
  - obvious blank interstitial pages and late library-slip pages were excluded
- The first-pass `normalized/` tranche is continuity-checked against the local English translation, but only at the level of section seams / note placement / obvious OCR damage.
- The text is good enough for orientation, browsing, and exploratory web chat.
- It is **not** yet good enough for fine lexical work, quotation discipline, or glossary building without a better witness.
- The local English translation can help detect dropped lines or bad seams, but it cannot substitute for a checked German witness when lexical precision matters.
- The two figures named in the book survive only as textual references (`Fig. 1.` / `Fig. 2.`); the image content itself is not extracted here.

## How To Use

- Read `source/raw/*.txt` when you want section-scale access.
- Use `source/sections.yaml` when you need reading order, titles, parents, and original page-line spans.
- Treat this as a browsing aid, not as an authority surface.

If later work shows that Wind is exerting real pressure on the repo, the next honest move would be a checked working text for whichever bounded axis wakes first. Until then, this scaffold is just navigational infrastructure.
