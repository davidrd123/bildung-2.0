# Cassirer — *Philosophie der symbolischen Formen* — Localized Source Scaffold

Ernst Cassirer, *Philosophie der symbolischen Formen* I-III.

## What This Is

A localized German source scaffold for narrow forays into Cassirer's three
*Philosophie der symbolischen Formen* volumes.

It exists so that chats, future agents, and bounded source checks can touch the
actual German directly without opening a full `texts/` campaign or leaning only
on chat-level summaries about "symbolic forms."

This is **not** yet a live Cassirer subproject and **not** a promoted symbolic-
forms apparatus. It is a source-localization move only.

## Why Here

- Not only in `sources/modern/incoming/` — because these are German primary
  texts and belong on the source-language side once the source is physically on
  disk.
- Not yet `texts/cassirer-philosophie-der-symbolischen-formen/` — because no
  glossary, journal, encounter dossiers, or thread apparatus have been earned
  for them.
- Not yet a full `texts/` campaign even though a bounded `raw/` and partial
  `normalized/` layer now exist — because the present need is still localized
  probing, not sustained close reading.

Current pressure toward these texts is real but still bounded. The repo already
holds:

- the later language / symbolic-forms bridge as real reserve pressure in
  `texts/erkenntnisproblem-vol1/journal.md`
- the same bridge as plausible but still provisional in
  `texts/erkenntnisproblem-vol1/reading/2026-04-08-earned-distillation-from-ferrari-and-gonzalez-rios.md`
- `Zeitmauer` pressure that remains Cassirer-historical rather than fully
  symbolic-formal in `texts/zeitmauer/threads/cassirer-pressure-on-zeitmauer.md`
- the April 17 bounded `Substanzbegriff` survey, which made the currently
  source-earned Cassirer center much clearer without yet licensing a symbolic-
  forms opening

## Current Working Bias

The three volumes are **not** equally live.

Current probe order:

1. `vol1-die-sprache.txt`
   - because the most clearly earned reserve pressure is the later
     language / symbolic-forms bridge
2. `vol3-phaenomenologie-der-erkenntnis.txt`
   - because current repo pressure around anti-psychologism, representation,
     objectivation, and modern physics may eventually need direct contact here
3. `vol2-das-mythische-denken.txt`
   - held for now; real, but not the first surface currently being demanded

So this scaffold is deliberately asymmetrical: all three volumes are localized,
but Volume I is the first honest probe surface.

## Source

Local authority copies (gitignored):

- `source/local/philosophie-der-symbolischen-formen-1-die-sprache.pdf`
- `source/local/philosophie-der-symbolischen-formen-2-das-mythische-denken.pdf`
- `source/local/philosophie-der-symbolischen-formen-3-phaenomenologie-der-erkenntnis.pdf`

Working extracted text:

- `source/full/vol1-die-sprache.txt`
- `source/full/vol2-das-mythische-denken.txt`
- `source/full/vol3-phaenomenologie-der-erkenntnis.txt`

The PDF remains authoritative whenever the extracted text and the source image
disagree.

The extraction quality is materially better than the earlier `Substanzbegriff`
PDF intake. These files are already usable for bounded orientation and rough
German probing, but not yet a substitute for a verified normalized layer.

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
    000-front-matter-and-inhaltsuebersicht.txt
    001-vorwort.txt
    010-einleitung-und-problemstellung.txt
    011-kapitel-i-das-sprachproblem-in-der-geschichte-der-philosophie.txt
    012-kapitel-ii-die-sprache-in-der-phase-des-sinnlichen-ausdrucks.txt
    013-kapitel-iii-die-sprache-in-der-phase-des-anschaulichen-ausdrucks.txt
    014-kapitel-iv-die-sprache-als-ausdruck-des-begrifflichen-denkens.txt
    015-kapitel-v-die-sprache-und-der-ausdruck-der-reinen-beziehungsformen.txt
    030-editorischer-bericht-und-back-matter.txt
  sections.yaml
```

## How To Use This

Use this scaffold for:

- bounded source checks against live repo pressure
- direct German forays when chat pressure begins reaching for symbolic forms
- testing whether a symbolic-forms claim is actually on the page or only in
  later reception / chat synthesis

Do **not** use this scaffold yet for:

- a stable symbolic-forms glossary
- a symbolic-forms encounter dossier
- importing `symbolic form` as controlling authority into current
  `Erkenntnisproblem`, `Zeitmauer`, Uexkuell, Anders, or Dick work
- general claims about all three volumes based on one bounded check

## Why The Section Map Exists

`source/sections.yaml` is a chapter map, not yet a split apparatus.

It exists so later work can say:

- "check Volume I, chapter III"
- "probe Volume III, chapter V, section III"
- "hold Volume II entirely below activation for now"

without reopening the tables of contents each time.

If pressure strengthens, the next honest move is:

1. extend the verified Volume I tranche only if current work keeps pressing it
2. leave Volumes II-III localized until they are actually needed
3. only then decide whether a broader `normalized/` layer is warranted

The current rough chapter files for Volume I were generated by:

- `tools/split_cassirer_symbolic_forms_vol1.py`

They are navigational surfaces only, not yet verified working texts.

## Present Status

What has been earned:

- the source substrate is on disk
- the texts are localized in the repo
- the first probe order is clear
- later agents now have an exact German surface to consult
- Volume I now has rough chapter files suitable for bounded direct forays
- a first bounded read of the introduction and chapter I confirms that Volume I
  is the correct first probe surface
- the first verified working surfaces now exist at
  - `source/normalized/0101-einleitung-i-begriff-und-systematik-1-7.txt`
    - scope: printed pages `1-7` of Intro I
  - `source/normalized/0102-einleitung-i-begriff-und-systematik-8-16.txt`
    - scope: the remainder of Intro I through the transition to section II
  - `source/normalized/0115-kapitel-i-v-wilhelm-von-humboldt.txt`
    - scope: the bounded Humboldt surface inside chapter I
  - `source/normalized/0151-kapitel-v-280-293-satz-und-beziehungsausdruck.txt`
    - scope: chapter V opening through sentence-before-word,
      isolating/flexional language, parataxis/hypotaxis, and the
      late emergence of explicit relation-expression
  - `source/normalized/0152-kapitel-v-293-295-kopula-und-praedikative-synthesis.txt`
    - scope: the Kant / Urteil / Kopula block and the cross-language
      emergence of pure predicative synthesis as a late achievement
  - `source/normalized/0153-kapitel-v-295-300-seinsbegriff-und-sprachlicher-ausdruck.txt`
    - scope: the broader Seinsgeschichte block through the end of
      chapter V, including Eleatics / Plato / Fichte, the
      indogermanic witness, and the Locke / Kant / Herder return
  - status: working-level normalization against the local PDF
  - footnote bodies omitted; page furniture removed

Chapter V is therefore now available as three bounded working
surfaces rather than as raw-only chapter mass.

What has **not** been earned:

- a symbolic-forms campaign
- a journal
- encounters
- a full verified `normalized/` layer for Volume I
- any repo-wide symbolic-forms vocabulary import
- any claim that the recent chat pressure is now source-secured
