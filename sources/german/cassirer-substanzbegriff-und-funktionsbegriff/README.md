# Cassirer — *Substanzbegriff und Funktionsbegriff* — Localized Source Scaffold

Ernst Cassirer, *Substanzbegriff und Funktionsbegriff: Untersuchungen über die Grundfragen der Erkenntniskritik*.

## What This Is

A localized German source scaffold for narrow forays into Cassirer's 1910 systematic companion to *Das Erkenntnisproblem*. It exists so that conversational instances, web chats, and future agents can read specific source passages directly in German without leaning on the combined English *Substance and Function and Einstein's Theory of Relativity* volume.

This is **not** yet a live Cassirer encounter and **not** a promoted subproject. It is a source-localization move only.

## Why Here

- Not only in `sources/modern/incoming/` — because this is a German primary text and belongs on the source-language side.
- Not yet `texts/cassirer-substanzbegriff-und-funktionsbegriff/` — because no glossary, journal, or encounter dossiers have been earned for it.
- Not the combined English volume — because that volume is useful for reception history, but this scaffold is for source-near German probing.

Current pressure toward this text is distributed across existing repo surfaces rather than concentrated in one dedicated source note, especially:

- `texts/erkenntnisproblem-vol1/parts/01-prefaces-and-introduction.md`
- `texts/erkenntnisproblem-vol1/parts/04-introduction-continued.md`
- `texts/zeitmauer/threads/cassirer-pressure-on-zeitmauer.md`
- `sources/modern/eilenberg-maclane-natural-equivalences.md`
- `sources/modern/incoming/ferrari/2012-erkenntnisproblem-working-extract.md`

## Source

Canonical working text:

- `source/full/substanzbegriff-und-funktionsbegriff.txt`
  - extracted locally from the standalone German PDF in `~/Downloads/`
  - current extraction reflects the Felix Meiner / Hamburger Ausgabe text as present in that PDF

Local authority copy (gitignored):

- `source/local/substanzbegriff-und-funktionsbegriff.pdf`
  - local working PDF for visual checking
  - authoritative over the extracted `.txt` whenever they disagree

Additional external support source, not vendored into the repo:

- `~/Downloads/33433089905909/`
  - page-by-page OCR dump with 486 page files, usable later if a page map becomes necessary

## Structure

```text
source/
  full/
    substanzbegriff-und-funktionsbegriff.txt
  local/
    substanzbegriff-und-funktionsbegriff.pdf   # gitignored authority copy
  normalized/
    001-vorwort.txt
    011-zur-theorie-der-begriffsbildung.txt
    0141-iv-i.txt
    0142-iv-ii.txt
    0143-iv-iii.txt
    0144-iv-iv.txt
  raw/
    000-front-matter-and-inhaltsubersicht.txt
    001-vorwort.txt
    010-erster-teil-dingbegriffe-und-relationsbegriffe.txt
    011-zur-theorie-der-begriffsbildung.txt
    012-die-zahlbegriffe.txt
    013-der-raumbegriff-und-die-geometrie.txt
    014-die-naturwissenschaftliche-begriffsbildung.txt
    0141-iv-i.txt
    0142-iv-ii.txt
    ...
    0149-iv-ix.txt
    020-zweiter-teil-das-system-der-relationsbegriffe-und-das-problem-der-wirklichkeit.txt
    021-zum-problem-der-induktion.txt
    022-der-begriff-der-wirklichkeit.txt
    023-subjektivitaet-und-objektivitaet-der-relationsbegriffe.txt
    024-zur-psychologie-der-relationen.txt
    030-editorischer-bericht.txt
    031-abkuerzungen.txt
    032-schriftenregister.txt
    033-personenregister.txt
  sections.yaml
```

## Split Logic

This is a lightweight navigational split, not yet a scholarly edition.

The current segmentation is:

- front matter and Inhaltsübersicht
- Vorwort
- both major parts as short container files
- chapter-scale files for the eight main chapters
- chapter IV additionally split into Roman-numeral subsection files (`0141`–`0149`) because its science / function line is already under local pressure and the chapter-scale file was too blunt
- back matter kept separate

That granularity is enough for bounded German forays and for handing exact loci to chats or future agents without pretending the text has already been fully opened.

## Normalized Tranche

The extracted `full/` and `raw/` text came from a noisy PDF substrate, not from a clean EPUB. That means the extracted German is useful for locating pressure zones, but not yet trustworthy enough for direct lexical work or stable quoting.

The current first-pass `normalized/` layer therefore stays deliberately small:

- `001-vorwort.txt`
- `011-zur-theorie-der-begriffsbildung.txt`
- `0141-iv-i.txt`
- `0142-iv-ii.txt`
- `0143-iv-iii.txt`
- `0144-iv-iv.txt`
  - cleaned against the local PDF and the page-level OCR witness
  - includes one conservative bracketed restoration at the clipped closing contrast

These files were checked against the local PDF or against the page-level OCR witness anchored back to the local PDF and then lightly cleaned for working use. They should be preferred over the corresponding `raw/` files when doing close source-near reading. The rest of the book remains intake text only.

## Status

- 2026-04-15: standalone German PDF identified as the correct source surface.
- 2026-04-15: full text localized and split into chapter-scale files.
- 2026-04-15: chapter IV additionally surfaced at subsection scale (`0141`–`0149`).
- 2026-04-15: local PDF copied into `source/local/` and gitignored.
- 2026-04-15: first verified `normalized/` tranche written for `Vorwort` and `Zur Theorie der Begriffsbildung`.
- 2026-04-15: first science/function tranche normalized for `Kapitel IV — I.` and `Kapitel IV — II.`.
- 2026-04-15: method-history continuation normalized for `Kapitel IV — III.`.
- 2026-04-15: historical substance-turn normalized for `Kapitel IV — IV.` with one conservative bracketed restoration at the clipped ending.

Nothing here licenses a Cassirer campaign by itself. This scaffold only makes source-near probing cheaper if the pressure toward `Substanzbegriff und Funktionsbegriff` keeps holding.

## Reproducibility

The split is generated by:

- `tools/split_substanzbegriff.py`

If the full text changes, rerun the splitter rather than editing the split files by hand.
