# Anders, Die Antiquiertheit des Menschen, Band I — Source Campaign

Günther Anders, *Die Antiquiertheit des Menschen. Band I: Über die Seele im Zeitalter der zweiten industriellen Revolution*

## What This Is

A bounded source-layer campaign around a small set of decisive passages from Anders's Band I.

This is more than a single `sources/` encounter, because the work needs its own line map, glossary pressure, and journal. It is less than a full `texts/` project, because the repo has not yet earned a sequential whole-book translation lane here.

## Why Here

Anders is already structurally active in the repo's genealogy:

- apparatus-world as human milieu rather than neutral toolset
- the human being's inferiority before its own technical products
- media phantoms and the manufactured mass human
- worldlessness as a lived historical condition
- apocalyptic incapacity as a failure of imagination, feeling, and responsibility

The immediate task is to recover the passages that put real pressure on those claims, not to build a larger Anders apparatus ahead of the evidence.

## Source

- `../../../books/Die Antiquiertheit des Menschen - Gunther Anders.txt`

This source is an EPUB-derived TXT and is clean enough to work from directly. The campaign therefore uses line anchors rather than a PDF page map. Raw and normalized local tranches should be created only when a specific encounter is actually worked.

## Structure

```text
source/
  line-map.yaml         # encounter anchors into the raw TXT source
encounters/
  01-preface-and-introduction.md
  02-prometheische-scham.md
  03-phantom-und-matrize.md
  04-sein-ohne-zeit.md
  05-apokalypseblindheit.md
glossary.yaml           # unstable terms under pressure
journal.md              # source-bound drift, not wider synthesis
```

## Working Hypothesis

These passages matter because they are where Anders most clearly forces the repo's existing threads:

- devices are not mere means but world-shaping predecisions
- `prometheische Scham` names a specifically modern shame before self-made things
- `Phantom` and `Matrize` turn media from channels into makers of reality
- `Sein ohne Zeit` gives a phenomenology of worldlessness and stalled action
- `Apokalypseblindheit` names a limit of imagination and responsibility at civilizational scale

## Encounter Queue

1. `01-preface-and-introduction.md`
   Lines `65-199`.
   The later preface, apparatus-world introduction, `prometheisches Gefälle`, and the methodological defense of overstatement.

2. `02-prometheische-scham.md`
   Lines `255-368`.
   The naming of `prometheische Scham`, the made/born contrast, and the first defense against objections.

3. `03-phantom-und-matrize.md`
   Main lines `1052-1121`, with a later confirmatory return to `§27`.
   `Phantom` / `Matrize`, the thesis that no medium is merely a means, and the distributed production of the mass human.

4. `04-sein-ohne-zeit.md`
   Lines `2177-2227`.
   Worldlessness, the negative parable, and waiting as the misreading of mere continued existence.

5. `05-apokalypseblindheit.md`
   Lines `2315-2401`.
   The bomb opening, overstatement as truth practice, and the first full pressure on `Apokalypseblindheit`.

## Promotion Trigger

Promote this campaign out of `sources/` only if the work starts to demand:

- sustained sequential translation beyond these anchor passages
- local tranche files dense enough to require their own raw/normalized workflow
- recurring journal drift that exceeds source-bound note-taking
- a glossary larger than a bounded campaign can honestly carry
- stable cross-project reuse strong enough to justify a standing `texts/` subproject

## First-Pass Assessment

The initial five-encounter queue is now complete.

What it earned:

- `Vorentscheidung` can stand provisionally as `predecision`, but only provisionally. The stronger singular claim still matters.
- `prometheische Scham`, `prometheisches Gefaelle`, `Weltphantom`, `Phantom / Matrize`, `Sein ohne Zeit`, `Massenmensch`, and `Apokalypseblindheit` all proved structurally real and remain genuinely open.
- The Beckett and bomb essays did not break the line opened by the first two encounters; they intensified it.
- The bounded campaign form held. A clean TXT source plus line-anchored encounter dossiers was enough to carry the first pass without spawning unnecessary workflow.

Promotion decision:

Stay under `sources/` for now.

What has not yet been earned:

- no full `texts/` promotion
- no local tranche-extraction machinery by default
- no standing cross-project dossier beyond the current source-bound notes

Best next routes from here:

- let existing cross-project notes point to this campaign explicitly when Anders is invoked
- return to specific later sections only when a live thread demands them
- reconsider promotion only if later work starts pulling on these terms more often than this bounded form can hold
