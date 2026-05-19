# Cassirer — *Philosophie der symbolischen Formen* — Localized Source Scaffold

Ernst Cassirer, *Philosophie der symbolischen Formen* I-III.

## What This Is

A localized German source scaffold for Cassirer's three
*Philosophie der symbolischen Formen* volumes.

It exists so chats, future agents, and web/search surfaces can touch the
actual German directly without opening a full `texts/` campaign or leaning only
on chat-level summaries about "symbolic forms."

This is **not** yet a live Cassirer subproject and **not** a promoted
symbolic-forms apparatus. It is a source-localization and substrate move only.

## Substrate Status

The May 2026 substrate/engagement distinction changes the practical threshold
for this scaffold. Unpacking PSF inside `sources/` is legitimate
**substrate-building**, not a quiet promotion to `texts/`.

The current target is a **direct all-volume searchable substrate**:

1. whole-volume search through `source/full/*.txt`
2. direct volume folders with chapter/back-matter files immediately inside
3. verified normalized tranches where earlier reading pressure already forced
   closer work

The introduction and chapter V of Volume I remain the strongest already-active
anchors, but they are no longer the boundary of the substrate. Future readers,
agents, and web-facing search/export layers should be able to locate and engage
any part of PSF I-III at will, while still seeing which surfaces are rough
extraction and which have been checked more closely.

What this licenses:

- whole-volume indexing for PSF I-III inside `sources/german/`
- direct chapter-file browsing inside per-volume folders
- web/search-facing metadata for full text, chapter files, and normalized
  priority surfaces
- verified normalized tranches where later reading tasks need them
- compact method notes that point future sessions back to the German

What it still does not license:

- promotion to `texts/cassirer-philosophie-der-symbolischen-formen/`
- a stable PSF glossary
- repo-wide import of `symbolic form` as controlling vocabulary
- treating Volumes II-III as engagement-active because their search substrate
  now exists

## Why Here

- Not only in `sources/modern/incoming/` — because these are German primary
  texts and belong on the source-language side once the source is physically on
  disk.
- Not yet `texts/cassirer-philosophie-der-symbolischen-formen/` — because no
  engagement layer has been earned for them. Substrate volume alone is not the
  promotion test.
- Not a full `texts/` campaign even though bounded rough and normalized layers
  exist — because the present need is chapter-scale substrate for guided
  reading and search, not a sustained engagement project.

Current pressure toward these texts is real but still bounded. The repo already
holds:

- the later language / symbolic-forms bridge as real reserve pressure in
  `texts/erkenntnisproblem-vol1/journal.md`
- the same bridge as plausible but still provisional in
  `texts/erkenntnisproblem-vol1/reading/2026-04-08-earned-distillation-from-ferrari-and-gonzalez-rios.md`
- `Zeitmauer` pressure that remains Cassirer-historical rather than fully
  symbolic-formal in `texts/zeitmauer/threads/cassirer-pressure-on-zeitmauer.md`
- the April 17 bounded `Substanzbegriff` survey, which made the currently
  source-earned Cassirer center much clearer without yet licensing a
  symbolic-forms opening

## Current Working Bias

The three volumes are now equally searchable as substrate, but they are **not**
equally live as engagement.

Current probe order:

1. `vol1-die-sprache`
   - because the clearest reserve pressure is the later language /
     symbolic-forms bridge; within Volume I, the introduction and chapter V
     remain priority anchors
2. `vol3-phaenomenologie-der-erkenntnis`
   - because current repo pressure around anti-psychologism, representation,
     objectivation, and modern physics may eventually need direct contact here
3. `vol2-das-mythische-denken`
   - held as searchable substrate; real, but not the first surface currently
     being demanded

So this scaffold is deliberately asymmetrical: all three volumes are localized
and split for search, while Volume I remains the first honest probe surface.

## Source

Local authority copies (gitignored):

- `source/local/philosophie-der-symbolischen-formen-1-die-sprache.pdf`
- `source/local/philosophie-der-symbolischen-formen-2-das-mythische-denken.pdf`
- `source/local/philosophie-der-symbolischen-formen-3-phaenomenologie-der-erkenntnis.pdf`

Working extracted full text:

- `source/full/vol1-die-sprache.txt`
- `source/full/vol2-das-mythische-denken.txt`
- `source/full/vol3-phaenomenologie-der-erkenntnis.txt`

The PDF remains authoritative whenever extracted text and source image
disagree.

## Structure

```text
source/
  full/
    vol1-die-sprache.txt
    vol2-das-mythische-denken.txt
    vol3-phaenomenologie-der-erkenntnis.txt
  local/
    philosophie-der-symbolischen-formen-1-die-sprache.pdf
    philosophie-der-symbolischen-formen-2-das-mythische-denken.pdf
    philosophie-der-symbolischen-formen-3-phaenomenologie-der-erkenntnis.pdf
  normalized/
    0101-einleitung-i-begriff-und-systematik-1-7.txt
    0102-einleitung-i-begriff-und-systematik-8-16.txt
    0115-kapitel-i-v-wilhelm-von-humboldt.txt
    0151-kapitel-v-280-293-satz-und-beziehungsausdruck.txt
    0152-kapitel-v-293-295-kopula-und-praedikative-synthesis.txt
    0153-kapitel-v-295-300-seinsbegriff-und-sprachlicher-ausdruck.txt
  raw/
    ... earlier Volume I rough split, retained as prior substrate
  vol1-die-sprache/
    000-front-matter-and-inhaltsuebersicht.txt
    001-vorwort.txt
    010-einleitung-und-problemstellung.txt
    ...
  vol2-das-mythische-denken/
    000-front-matter-and-inhaltsuebersicht.txt
    001-vorwort.txt
    010-einleitung-problem-einer-philosophie-der-mythologie.txt
    ...
  vol3-phaenomenologie-der-erkenntnis/
    000-front-matter-and-inhaltsuebersicht.txt
    001-vorrede.txt
    010-einleitung.txt
    ...
  search-surfaces.yaml
  sections.yaml
```

The direct `vol*` folders are the default search and browsing surfaces. Their
files were generated from the full text by:

- `tools/split_cassirer_symbolic_forms.py`

They are navigational and search surfaces, not verified working texts.

## How To Use This

Use this scaffold for:

- bounded source checks against live repo pressure
- all-volume PSF search and guided-reading substrate
- direct German forays when chat pressure begins reaching for symbolic forms
- testing whether a symbolic-forms claim is actually on the page or only in
  later reception / chat synthesis
- web-facing discovery where a reader needs direct chapter files

Do **not** use this scaffold yet for:

- a stable symbolic-forms glossary
- a symbolic-forms encounter dossier
- importing `symbolic form` as controlling authority into current
  `Erkenntnisproblem`, `Zeitmauer`, Uexkuell, Anders, or Dick work
- general claims about the whole trilogy based on one bounded check

## Web/Search Use

`source/search-surfaces.yaml` is the web-facing finding aid for PSF I-III.

It distinguishes:

- whole-volume files, useful for broad search
- direct chapter/back-matter files, useful for navigation and exploratory
  engagement
- normalized priority tranches, useful when a passage needs closer citation
  discipline

The direct chapter files are valid search surfaces. They are not yet verified
working texts. A web layer should expose that distinction rather than hiding
it.

## Why The Section Map Exists

`source/sections.yaml` is a chapter map and status map.

It exists so later work can say:

- "check Volume I, chapter III"
- "probe Volume III, chapter V, section III"
- "hold Volume II below engagement activation for now"

without reopening the tables of contents each time.

If pressure strengthens, the next honest move is:

1. keep the PSF I-III substrate searchable
2. extend verified normalization only where future engagement needs citation
   discipline
3. keep Volumes II-III substrate-available but engagement-held until actually
   needed
4. only then decide whether a broader normalized layer is warranted

## Present Status

What has been earned:

- the source substrate is on disk
- the texts are localized in the repo
- all three volumes have direct chapter/back-matter search folders
- the web-facing search surface index is tracked at
  `source/search-surfaces.yaml`
- Volume I has priority anchors in the introduction and chapter V
- a first bounded read of the introduction and chapter I confirms that Volume I
  is the correct first probe surface
- the first verified working surfaces now exist at
  - `source/normalized/0101-einleitung-i-begriff-und-systematik-1-7.txt`
  - `source/normalized/0102-einleitung-i-begriff-und-systematik-8-16.txt`
  - `source/normalized/0115-kapitel-i-v-wilhelm-von-humboldt.txt`
  - `source/normalized/0151-kapitel-v-280-293-satz-und-beziehungsausdruck.txt`
  - `source/normalized/0152-kapitel-v-293-295-kopula-und-praedikative-synthesis.txt`
  - `source/normalized/0153-kapitel-v-295-300-seinsbegriff-und-sprachlicher-ausdruck.txt`

What has **not** been earned:

- a symbolic-forms campaign
- a journal
- encounters
- a full verified `normalized/` layer
- any repo-wide symbolic-forms vocabulary import
- any claim that recent chat pressure is now source-secured
