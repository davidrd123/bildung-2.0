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
    030-editorischer-bericht.txt
    031-abkuerzungen.txt
    020-zweiter-teil-das-system-der-relationsbegriffe-und-das-problem-der-wirklichkeit.txt
    023-subjektivitaet-und-objektivitaet-der-relationsbegriffe.txt
    0241-viii-i.txt
    0242-viii-ii.txt
    0211-v-i.txt
    0212-v-ii.txt
    0213-v-iii.txt
    0221-vi-i.txt
    0222-vi-ii.txt
    0223-vi-iii.txt
    0224-vi-iv.txt
    0141-iv-i.txt
    0142-iv-ii.txt
    0143-iv-iii.txt
    0144-iv-iv.txt
    0145-iv-v.txt
    0146-iv-vi.txt
    0147-iv-vii.txt
    0148-iv-viii.txt
    0149-iv-ix.txt
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
- chapter V also breaks cleanly into `I.` / `II.` / `III.` in the OCR witness (`333` / `354` / `371` / chapter VI on `379`) and is now surfaced at subsection scale in the normalized layer
- chapter VI also breaks cleanly into `I.` / `II.` / `III.` / `IV.` in the OCR witness (`379` / `400` / `409` / `422`; chapter VII on `430`) and is now surfaced at subsection scale in the normalized layer
- chapter VIII also breaks cleanly into `I.` / `II.` in the OCR witness (`453` / `474`), with the chapter ending before the colophon on `480`; it is now surfaced at subsection scale in the normalized layer
- the prose back matter (`Editorischer Bericht`) and the abbreviation list can be normalized at working level with straightforward seam repair; the two registers still require a separate two-column reconstruction pass
- back matter kept separate

That granularity is enough for bounded German forays and for handing exact loci to chats or future agents without pretending the text has already been fully opened.

## Normalized Tranche

The extracted `full/` and `raw/` text came from a noisy PDF substrate, not from a clean EPUB. That means the extracted German is useful for locating pressure zones, but not yet trustworthy enough for direct lexical work or stable quoting.

The current first-pass `normalized/` layer therefore stays deliberately small:

- `001-vorwort.txt`
- `011-zur-theorie-der-begriffsbildung.txt`
- `030-editorischer-bericht.txt`
  - normalized prose back matter surface for the editorial report
  - page furniture removed, but no critical restoration beyond obvious split-noise repair
- `031-abkuerzungen.txt`
  - normalized working list of Cassirer's abbreviations as paired entries
  - reconstructed from the raw seam across `030` and `031`
- `020-zweiter-teil-das-system-der-relationsbegriffe-und-das-problem-der-wirklichkeit.txt`
  - normalized anchor for the second-part entry surface
- `023-subjektivitaet-und-objektivitaet-der-relationsbegriffe.txt`
  - rebuilt from the OCR page band `430`–`452`, clipped before chapter VIII on `453`
  - working-level normalization of the chapter-scale relations / pragmatism / objectivity / continuity argument of chapter VII; no reliable internal Roman-numeral subheads appear before chapter VIII
- `0241-viii-i.txt`
  - rebuilt from the OCR page band `453`–`473`, clipped before `II.` on `474`
  - working-level normalization of the Platon / Aristoteles / Leibniz / Gestaltqualität / physiologischer Zirkel tranche of chapter VIII
- `0242-viii-ii.txt`
  - rebuilt from the OCR page band `474`–`479`, clipped before the colophon on `480`
  - working-level normalization of the fundierte Inhalte / Empirismus-Nativismus / Raum / kategoriale Akte close of chapter VIII
- `0211-v-i.txt`
  - rebuilt from the OCR page band `333`–`353`, clipped before `II.` on `354`
  - working-level normalization of the opening induction tranche
- `0212-v-ii.txt`
  - rebuilt from the OCR page band `354`–`370`, clipped before `III.` on `371`
  - working-level normalization of the core induction / isolation / superposition / Mach tranche
- `0213-v-iii.txt`
  - rebuilt from the OCR page band `371`–`378`, clipped before chapter VI on `379`
  - working-level normalization of the invariance / transcendental-philosophy / `a priori` close of chapter V
- `0221-vi-i.txt`
  - rebuilt from the OCR page band `379`–`399`, clipped before `II.` on `400`
  - working-level normalization of the opening objectivity / subjectivity / representation / reality tranche of chapter VI
- `0222-vi-ii.txt`
  - rebuilt from the OCR page band `400`–`409`, clipped before `III.` on `409`
  - working-level normalization of the Raum / Projektion / Selektion / Apperzeption tranche of chapter VI
- `0223-vi-iii.txt`
  - rebuilt from the OCR page band `409`–`421`, clipped before `IV.` on `422`
  - working-level normalization of the Transzendenz / Immanenz / kritischer Idealismus / Fechner tranche of chapter VI
- `0224-vi-iv.txt`
  - rebuilt from the OCR page band `422`–`429`, clipped before chapter VII on `430`
  - working-level normalization of the Zeichentheorie / Relativität / Planck close of chapter VI
- `0141-iv-i.txt`
- `0142-iv-ii.txt`
- `0143-iv-iii.txt`
- `0144-iv-iv.txt`
  - cleaned against the local PDF and the page-level OCR witness
  - includes one conservative bracketed restoration at the clipped closing contrast
- `0145-iv-v.txt`
  - rebuilt from the OCR page band and cleaned back against the local PDF at working level
  - usable for source-near reading, but still not a full scholarly normalization of every Greek or citation form
- `0146-iv-vi.txt`
  - rebuilt from the OCR page band `245`–`268`, clipped before the true `VII.` start on `269`
  - heavy footnote / header debris removed and the main argument normalized to working level against the OCR witness and local PDF
- `0147-iv-vii.txt`
  - rebuilt from the OCR page band `269`–`289`, clipped before the true `VIII.` start on `290`
  - working-level normalization of the Energetik / measure / quality tranche; the opening Greek witness form remains provisional rather than fully normalized
- `0148-iv-viii.txt`
  - rebuilt from the OCR page band `290`–`311`, clipped before the true `IX.` start on `312`
  - working-level normalization of the chemistry / atom / valence / periodic-system tranche; footnote bodies remain omitted and a few citation markers stay schematic rather than critically restored
- `0149-iv-ix.txt`
  - rebuilt from the OCR page band `312`–`330`, clipped before `Zweiter Teil` on `331`
  - working-level normalization of the Rickert / concept / singularity / method close of chapter IV; long footnote bodies remain omitted and a few reference markers stay schematic

These files were checked against the local PDF or against the page-level OCR witness anchored back to the local PDF and then lightly cleaned for working use. They should be preferred over the corresponding `raw/` files when doing close source-near reading. The rest of the book remains intake text only.

## Status

- 2026-04-15: standalone German PDF identified as the correct source surface.
- 2026-04-15: full text localized and split into chapter-scale files.
- 2026-04-15: chapter IV additionally surfaced at subsection scale (`0141`–`0149`).
- 2026-04-15: second-part entry anchor normalized and chapter V subsection boundaries pinned from the OCR witness (`I./II./III.` at `333/354/371`, chapter VI on `379`).
- 2026-04-15: `Kapitel V — II.` normalized at working level from the OCR witness and raw intake text, clipped before the true `III.` start on `371`.
- 2026-04-15: `Kapitel V — III.` normalized at working level from the OCR witness and raw intake text, clipped before chapter VI on `379`.
- 2026-04-15: `Kapitel VI — I.` normalized at working level from the OCR witness and raw intake text, clipped before the true `II.` start on `400`.
- 2026-04-15: chapter VI subsection map corrected from the OCR witness: `IV.` begins on `422`, with chapter VII on `430`.
- 2026-04-15: `Kapitel VI — II.` normalized at working level from the OCR witness and raw intake text, clipped before the true `III.` start on `409`.
- 2026-04-15: `Kapitel VI — III.` normalized at working level from the OCR witness and raw intake text, clipped before the true `IV.` start on `422`.
- 2026-04-15: `Kapitel VI — IV.` normalized at working level from the OCR witness and raw intake text, clipped before chapter VII on `430`.
- 2026-04-15: chapter VII checked against the OCR witness and kept at chapter scale; no reliable internal Roman-numeral subheads appear before chapter VIII on `453`.
- 2026-04-15: `Siebentes Kapitel — Subjektivität und Objektivität der Relationsbegriffe` normalized at working level from the OCR witness and raw intake text, clipped before `Achtes Kapitel` on `453`.
- 2026-04-15: chapter VIII checked against the OCR witness and split only into `I.` and `II.` (`453/474`); no later substantive chapter follows before the colophon on `480`.
- 2026-04-15: `Achtes Kapitel — I.` normalized at working level from the OCR witness and raw intake text, clipped before `II.` on `474`.
- 2026-04-15: `Achtes Kapitel — II.` normalized at working level from the OCR witness and raw intake text, clipped before the colophon on `480`.
- 2026-04-15: `Editorischer Bericht` normalized at working level from raw back matter, with page furniture removed.
- 2026-04-15: `Abkürzungen` normalized at working level as a paired list, reconstructed from the raw seam across `030` and `031`.
- 2026-04-15: `Schriftenregister` and `Personenregister` deliberately left below normalization for now; both require a dedicated two-column reconstruction pass rather than simple OCR cleanup.
- 2026-04-15: local PDF copied into `source/local/` and gitignored.
- 2026-04-15: first verified `normalized/` tranche written for `Vorwort` and `Zur Theorie der Begriffsbildung`.
- 2026-04-15: first science/function tranche normalized for `Kapitel IV — I.` and `Kapitel IV — II.`.
- 2026-04-15: method-history continuation normalized for `Kapitel IV — III.`.
- 2026-04-15: historical substance-turn normalized for `Kapitel IV — IV.` with one conservative bracketed restoration at the clipped ending.
- 2026-04-15: continuation through `Kapitel IV — V.` normalized at working level from the OCR witness and local PDF.
- 2026-04-15: `Kapitel IV — VI.` normalized at working level after rechecking the true `VI./VII.` boundary in the OCR witness.
- 2026-04-15: `Kapitel IV — VII.` normalized at working level after pinning the true `VII./VIII.` boundary in the OCR witness.
- 2026-04-15: `Kapitel IV — VIII.` normalized at working level after pinning the true `VIII./IX.` boundary in the OCR witness.
- 2026-04-15: `Kapitel IV — IX.` normalized at working level after pinning the `IX./Zweiter Teil` boundary in the OCR witness.

Nothing here licenses a Cassirer campaign by itself. This scaffold only makes source-near probing cheaper if the pressure toward `Substanzbegriff und Funktionsbegriff` keeps holding.

## Reproducibility

The split is generated by:

- `tools/split_substanzbegriff.py`

If the full text changes, rerun the splitter rather than editing the split files by hand.
