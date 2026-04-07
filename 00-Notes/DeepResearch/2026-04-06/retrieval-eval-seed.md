# Retrieval Evaluation Seed

**Status**: living-layer method note
**Date**: 2026-04-06
**Purpose**: seed the Phase 1 evaluation set for retrieval benchmarking

## How to use this

For each query:

- run lexical search first
- record top 5 hits
- mark whether the expected anchor appears
- note whether the first relevant result is in the right authority layer
- note whether widening to `living-notes` helped
- note whether widening to `chats` was actually necessary

## Query set

| Query | Query class | Expected anchor(s) | Notes |
| --- | --- | --- | --- |
| `predecided world` | repo-native | `texts/zeitmauer/threads/predecided-world.md`; `sources/german/anders-antiquiertheit-des-menschen-band1/journal.md`; `sources/german/uexkuell-theoretische-biologie/journal.md` | should be an easy baseline |
| `time-crisis` | repo-native | `texts/zeitmauer/threads/time-crisis.md`; `texts/zeitmauer/journal.md` | tests dossier retrieval |
| `Goethe/Leibniz split` | repo-native | `texts/zeitmauer/threads/goethe-leibniz-frame.md`; `00-Notes/cross-domain-synthesis-threads.md` | tests thread vs omnibus-note competition |
| `planfulness outside the body` | source-close English | `sources/german/uexkuell-theoretische-biologie/encounters/02b-funktionskreis-undrafted.md` | should hit Uexküll directly |
| `leading and accompanying properties` | source-close English | `sources/german/uexkuell-theoretische-biologie/encounters/02b-funktionskreis-undrafted.md` | distinction-heavy local phrase |
| `switch standpoints` | source-close English | `sources/german/uexkuell-theoretische-biologie/encounters/02b-funktionskreis-undrafted.md` | anti-psychologism test |
| `animal's soul` | source-close English | `sources/german/uexkuell-theoretische-biologie/encounters/02b-funktionskreis-undrafted.md` | should retrieve the same passage by a different local phrase |
| `translation resistance as evidence` | natural-language synthesis | `sources/german/uexkuell-theoretische-biologie/journal.md`; `00-Notes/process.md`; `patterns/charter.md` | tests repo-method retrieval rather than one text |
| `world already structured before neutral description` | natural-language synthesis | `sources/german/uexkuell-theoretische-biologie/journal.md`; `00-Notes/cross-domain-synthesis-threads.md`; `texts/zeitmauer/journal.md` | tests abstract cross-project phrasing |
| `where is empathy methodologically blocked?` | natural-language synthesis | `sources/german/uexkuell-theoretische-biologie/encounters/02b-funktionskreis-undrafted.md`; `sources/german/uexkuell-theoretische-biologie/encounters/03-merkzeichen-und-umwelten.md` | tests abstract paraphrase of the anti-psychologism line |
| `constitutive fit rather than adaptation` | natural-language synthesis | `sources/german/uexkuell-theoretische-biologie/encounters/04-fuegung.md`; `sources/german/uexkuell-theoretische-biologie/encounters/05-welt-und-umwelt.md` | tests whether the model can find fit-language without exact repo wording |
| `Vorentscheidung` | cross-language | `sources/german/anders-antiquiertheit-des-menschen-band1/glossary.yaml`; `sources/german/anders-antiquiertheit-des-menschen-band1/journal.md`; `texts/zeitmauer/threads/predecided-world.md` | tests German term to cross-project thread |
| `Umwelt` | cross-language | `sources/german/uexkuell-theoretische-biologie/glossary.yaml`; `sources/german/uexkuell-theoretische-biologie/encounters/02-funktionskreis.md`; `encounters/05-welt-und-umwelt.md` | tests term retrieval vs commentary noise |
| `what says the world is cut in advance by plan and naming?` | cross-language synthesis | `texts/zeitmauer/journal.md`; `00-Notes/cross-domain-synthesis-threads.md`; `sources/german/anders-antiquiertheit-des-menschen-band1/encounters/03-phantom-und-matrize.md` | tests multi-author paraphrase |

## Minimal scoring rubric

For each query, record:

- `top5_anchor`: yes / no
- `top1_relevant`: yes / no
- `right_layer_first`: yes / no
- `living_needed`: yes / no
- `chats_needed`: yes / no
- `notes`: one sentence on failure mode

## Failure-type labels

Use one or more of these:

- `query-too-abstract`
- `needs-repo-phrase`
- `chat-noise`
- `omnibus-note-dominance`
- `missing-dossier`
- `missing-unit`
- `cross-language-miss`
- `model-smoothing`

## Current hypothesis

Likely strong:

- repo-native queries
- source-close English queries

Likely weak:

- abstract natural-language synthesis questions
- cross-language paraphrases without an exact lexical bridge

That is what the next benchmark phase should test, not generic retrieval quality in the abstract.
