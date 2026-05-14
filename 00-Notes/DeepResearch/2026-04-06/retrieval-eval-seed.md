# Retrieval Evaluation Seed

**Status**: living-layer method note
**Date**: 2026-04-06
**Purpose**: seed the Phase 1 evaluation set for retrieval benchmarking

## How to use this

For each query:

- run lexical search first
- compare dense and hybrid retrieval against the same expected anchors
- record top 5 hits
- mark whether the expected anchor appears
- use `Test focus` to say what the query is actually testing
- note whether the first relevant result is in the right authority layer
- note whether widening to `living-notes` helped
- note whether widening to `chats` was actually necessary

## Query set

| Query | Query class | Test focus | Expected anchor(s) | Failure labels | Notes |
| --- | --- | --- | --- | --- | --- |
| `predecided world` | thread retrieval | thread retrieval; exact term | `texts/zeitmauer/threads/predecided-world.md`; `sources/german/anders-antiquiertheit-des-menschen-band1/journal.md`; `sources/german/uexkuell-theoretische-biologie/journal.md` | `missing-dossier`; `omnibus-note-dominance` | should be an easy baseline |
| `time-crisis` | thread retrieval | thread retrieval; exact term | `texts/zeitmauer/threads/time-crisis.md`; `texts/zeitmauer/journal.md` | `corpus-shape`; `derived-index-dominance` | tests dossier retrieval without letting handles dominate |
| `Goethe/Leibniz split` | thread retrieval | thread retrieval; synthesis | `texts/zeitmauer/threads/goethe-leibniz-frame.md`; `00-Notes/cross-domain-synthesis-threads.md` | `omnibus-note-dominance`; `missing-dossier` | tests thread vs omnibus-note competition |
| `Planmäßigkeit as Naturkraft` | exact term | exact term; cross-language | `sources/german/uexkuell-theoretische-biologie/encounters/04-fuegung.md`; `sources/german/uexkuell-theoretische-biologie/journal.md`; `sources/german/uexkuell-theoretische-biologie/glossary.yaml` | `translation-bottleneck`; `model-smoothing` | tests whether the compressed repo phrase reaches the explicit rule-binding force passage |
| `planfulness outside the body` | source-close phrase | source-close phrase; cross-language | `sources/german/uexkuell-theoretische-biologie/encounters/02b-funktionskreis-undrafted.md` | `cross-language-miss`; `chunking` | should hit Uexküll directly |
| `leading and accompanying properties` | source-close phrase | source-close phrase; exact term | `sources/german/uexkuell-theoretische-biologie/encounters/02b-funktionskreis-undrafted.md` | `chunking`; `model-smoothing` | distinction-heavy local phrase |
| `switch standpoints` | source-close phrase | source-close phrase; exact phrase | `sources/german/uexkuell-theoretische-biologie/encounters/02b-funktionskreis-undrafted.md` | `model-smoothing`; `query-too-short` | anti-psychologism test |
| `animal's soul` | source-close phrase | source-close phrase; false friend | `sources/german/uexkuell-theoretische-biologie/encounters/02b-funktionskreis-undrafted.md` | `translation-bottleneck`; `model-smoothing` | should retrieve the same passage by a different local phrase |
| `translation resistance as evidence` | synthesis | synthesis; method | `sources/german/uexkuell-theoretische-biologie/journal.md`; `00-Notes/process.md`; `patterns/charter.md` | `query-too-abstract`; `living-note-noise` | tests repo-method retrieval rather than one text |
| `world already structured before neutral description` | synthesis | synthesis; cross-project | `sources/german/uexkuell-theoretische-biologie/journal.md`; `00-Notes/cross-domain-synthesis-threads.md`; `texts/zeitmauer/journal.md` | `query-too-abstract`; `model-smoothing` | tests abstract cross-project phrasing |
| `where is empathy methodologically blocked?` | synthesis | synthesis; source-close phrase | `sources/german/uexkuell-theoretische-biologie/encounters/02b-funktionskreis-undrafted.md`; `sources/german/uexkuell-theoretische-biologie/encounters/03-merkzeichen-und-umwelten.md` | `model-smoothing`; `query-too-abstract` | tests abstract paraphrase of the anti-psychologism line |
| `constitutive fit rather than adaptation` | synthesis | synthesis; false friend | `sources/german/uexkuell-theoretische-biologie/encounters/04-fuegung.md`; `sources/german/uexkuell-theoretische-biologie/encounters/05-welt-und-umwelt.md` | `false-friend`; `model-smoothing` | tests whether the model can find fit-language without exact repo wording |
| `Vorentscheidung` | cross-language | exact term; cross-language | `sources/german/anders-antiquiertheit-des-menschen-band1/encounters/01-preface-and-introduction.md`; `sources/german/anders-antiquiertheit-des-menschen-band1/glossary.yaml`; `sources/german/anders-antiquiertheit-des-menschen-band1/journal.md`; `texts/zeitmauer/threads/predecided-world.md` | `cross-language-miss`; `missing-glossary-cue` | tests German term to source anchor and cross-project thread |
| `Umwelt` | cross-language | exact term; cross-language | `sources/german/uexkuell-theoretische-biologie/glossary.yaml`; `sources/german/uexkuell-theoretische-biologie/encounters/02-funktionskreis.md`; `sources/german/uexkuell-theoretische-biologie/encounters/05-welt-und-umwelt.md` | `commentary-noise`; `model-smoothing` | tests term retrieval vs commentary noise |
| `what says the world is cut in advance by plan and naming?` | synthesis | synthesis; cross-language | `texts/zeitmauer/threads/predecided-world.md`; `texts/zeitmauer/journal.md`; `00-Notes/cross-domain-synthesis-threads.md`; `sources/german/anders-antiquiertheit-des-menschen-band1/encounters/03-phantom-und-matrize.md` | `query-too-abstract`; `missing-dossier` | tests multi-author paraphrase |
| `cassirer pressure on zeitmauer` | thread retrieval | thread retrieval; exact term | `texts/zeitmauer/threads/cassirer-pressure-on-zeitmauer.md`; `texts/zeitmauer/journal.md` | `omnibus-note-dominance`; `missing-dossier` | tests a named pressure dossier |
| `mumford bridge` | thread retrieval | thread retrieval; exact term | `texts/zeitmauer/threads/mumford-bridge.md`; `00-Notes/cross-domain-synthesis-threads.md` | `omnibus-note-dominance`; `missing-dossier` | tests another named thread surface |
| `thread:predecided-world` | exact term | exact handle; thread retrieval | `texts/zeitmauer/threads/predecided-world.md` | `derived-index-dominance`; `corpus-shape` | handle-like query should still land on the dossier by default |
| `Siderische Einteilungen` | exact term | exact term; source-title phrase | `texts/zeitmauer/parts/46-siderische-einteilungen.md`; `texts/zeitmauer/journal.md` | `missing-unit`; `derived-index-dominance` | tests a recurring title phrase now that selected part files are in the seed corpus |
| `source-role taxonomy` | method retrieval | exact term; synthesis | `00-Notes/right-now.md`; `00-Notes/process.md` | `living-note-noise`; `query-too-abstract` | tests retrieval of a living method cue |
| `Gerüst` | exact term | exact term; false friend | `sources/german/uexkuell-theoretische-biologie/encounters/01-prefaces.md`; `sources/german/uexkuell-theoretische-biologie/glossary.yaml` | `false-friend`; `translation-bottleneck` | tests scaffold/framework pressure |
| `Fügung` | exact term | exact term; false friend | `sources/german/uexkuell-theoretische-biologie/encounters/04-fuegung.md`; `sources/german/uexkuell-theoretische-biologie/glossary.yaml`; `sources/german/uexkuell-theoretische-biologie/encounters/05-welt-und-umwelt.md` | `false-friend`; `model-smoothing` | tests the fittedness/adaptation pressure term |
| `Merkwelt` | exact term | exact term; cross-language | `sources/german/uexkuell-theoretische-biologie/encounters/03-merkzeichen-und-umwelten.md`; `sources/german/uexkuell-theoretische-biologie/glossary.yaml` | `translation-bottleneck`; `chunking` | tests perceptual-world vocabulary |
| `Funktionskreis` | exact term | exact term; source-close phrase | `sources/german/uexkuell-theoretische-biologie/encounters/02-funktionskreis.md`; `sources/german/uexkuell-theoretische-biologie/encounters/05-welt-und-umwelt.md`; `sources/german/uexkuell-theoretische-biologie/glossary.yaml` | `commentary-noise`; `chunking` | core Uexküll source term |
| `Einpassung` | exact term | exact term; false friend | `sources/german/uexkuell-theoretische-biologie/encounters/05-welt-und-umwelt.md`; `sources/german/uexkuell-theoretische-biologie/glossary.yaml` | `false-friend`; `translation-bottleneck` | tests fit vs adaptation |
| `Umwelttunnel` | exact term | exact term; cross-language | `sources/german/uexkuell-theoretische-biologie/encounters/05-welt-und-umwelt.md`; `sources/german/uexkuell-theoretische-biologie/glossary.yaml` | `cross-language-miss`; `missing-glossary-cue` | tests a rare source term |
| `prometheisches Gefälle` | exact term | exact term; cross-language | `sources/german/anders-antiquiertheit-des-menschen-band1/encounters/01-preface-and-introduction.md`; `sources/german/anders-antiquiertheit-des-menschen-band1/glossary.yaml`; `sources/german/anders-antiquiertheit-des-menschen-band1/journal.md` | `translation-bottleneck`; `chunking` | tests Anders's asymmetry term; Encounter 01 is the primary anchor |
| `Weltphantom` | exact term | exact term; cross-language | `sources/german/anders-antiquiertheit-des-menschen-band1/encounters/01-preface-and-introduction.md`; `sources/german/anders-antiquiertheit-des-menschen-band1/encounters/03-phantom-und-matrize.md`; `sources/german/anders-antiquiertheit-des-menschen-band1/glossary.yaml` | `cross-language-miss`; `commentary-noise` | tests world-phantom vocabulary |
| `Matrize` | exact term | exact term; false friend | `sources/german/anders-antiquiertheit-des-menschen-band1/encounters/03-phantom-und-matrize.md`; `sources/german/anders-antiquiertheit-des-menschen-band1/glossary.yaml` | `false-friend`; `model-smoothing` | tests matrix/matrice ambiguity |
| `Massenmensch` | exact term | exact term; source-close phrase | `sources/german/anders-antiquiertheit-des-menschen-band1/encounters/03-phantom-und-matrize.md`; `sources/german/anders-antiquiertheit-des-menschen-band1/glossary.yaml`; `sources/german/anders-antiquiertheit-des-menschen-band1/journal.md` | `translation-bottleneck`; `chunking` | tests mass-human vocabulary |
| `Apokalypseblindheit` | exact term | exact term; cross-language | `sources/german/anders-antiquiertheit-des-menschen-band1/encounters/05-apokalypseblindheit.md`; `sources/german/anders-antiquiertheit-des-menschen-band1/glossary.yaml`; `sources/german/anders-antiquiertheit-des-menschen-band1/journal.md` | `cross-language-miss`; `model-smoothing` | tests a rare Anders term |
| `Sein ohne Zeit` | exact term | exact title phrase | `sources/german/anders-antiquiertheit-des-menschen-band1/encounters/04-sein-ohne-zeit.md`; `sources/german/anders-antiquiertheit-des-menschen-band1/journal.md` | `chunking`; `missing-unit` | tests encounter title retrieval |
| `scaffold not framework` | false friend | false friend; source-close phrase | `sources/german/uexkuell-theoretische-biologie/encounters/01-prefaces.md`; `sources/german/uexkuell-theoretische-biologie/glossary.yaml` | `false-friend`; `model-smoothing` | English paraphrase of `Gerüst` decision |
| `beetle path does not belong to mineralogy` | source-close phrase | source-close phrase | `sources/german/uexkuell-theoretische-biologie/encounters/02b-funktionskreis-undrafted.md` | `chunking`; `model-smoothing` | vivid local phrase should be easy for lexical and hybrid |
| `functional circle as invariant world weave` | source-close phrase | source-close phrase; synthesis | `sources/german/uexkuell-theoretische-biologie/encounters/05-welt-und-umwelt.md` | `query-too-abstract`; `model-smoothing` | tests paraphrase of the Funktionskreis/world-weave line |
| `bomb as apparatus predecision` | source-close phrase | source-close phrase; synthesis | `sources/german/anders-antiquiertheit-des-menschen-band1/encounters/01-preface-and-introduction.md`; `sources/german/anders-antiquiertheit-des-menschen-band1/journal.md` | `query-too-abstract`; `model-smoothing` | tests Anders preface apparatus line |
| `mass-hermit` | source-close phrase | source-close phrase; false friend | `sources/german/anders-antiquiertheit-des-menschen-band1/encounters/03-phantom-und-matrize.md`; `sources/german/anders-antiquiertheit-des-menschen-band1/journal.md` | `translation-bottleneck`; `chunking` | tests English rendering of mass solitude |
| `shame before things` | synthesis | synthesis; source-close phrase | `sources/german/anders-antiquiertheit-des-menschen-band1/encounters/02-prometheische-scham.md`; `sources/german/anders-antiquiertheit-des-menschen-band1/journal.md` | `query-too-abstract`; `model-smoothing` | paraphrases Promethean shame |
| `being without time` | cross-language | cross-language; title phrase | `sources/german/anders-antiquiertheit-des-menschen-band1/encounters/04-sein-ohne-zeit.md` | `cross-language-miss`; `chunking` | English query to German title |
| `monstrous size ethics` | synthesis | synthesis; source-close phrase | `sources/german/anders-antiquiertheit-des-menschen-band1/encounters/05-apokalypseblindheit.md`; `sources/german/anders-antiquiertheit-des-menschen-band1/journal.md` | `query-too-abstract`; `model-smoothing` | tests apocalypse ethics formulation |
| `predecision` | cross-language | cross-language; translated term | `sources/german/anders-antiquiertheit-des-menschen-band1/encounters/01-preface-and-introduction.md`; `sources/german/anders-antiquiertheit-des-menschen-band1/glossary.yaml`; `texts/zeitmauer/threads/predecided-world.md` | `cross-language-miss`; `false-friend` | English to `Vorentscheidung` and thread |
| `phantom matrix` | cross-language | cross-language; false friend | `sources/german/anders-antiquiertheit-des-menschen-band1/encounters/03-phantom-und-matrize.md`; `sources/german/anders-antiquiertheit-des-menschen-band1/glossary.yaml` | `false-friend`; `model-smoothing` | English query for `Phantom` and `Matrize` |
| `world phantom` | cross-language | cross-language; translated term | `sources/german/anders-antiquiertheit-des-menschen-band1/encounters/03-phantom-und-matrize.md`; `sources/german/anders-antiquiertheit-des-menschen-band1/glossary.yaml` | `cross-language-miss`; `commentary-noise` | English phrase for `Weltphantom` |
| `fittedness` | false friend | false friend; translated term | `sources/german/uexkuell-theoretische-biologie/encounters/04-fuegung.md`; `sources/german/uexkuell-theoretische-biologie/encounters/05-welt-und-umwelt.md`; `sources/german/uexkuell-theoretische-biologie/glossary.yaml` | `false-friend`; `model-smoothing` | English pressure term for `Fügung` and `Einpassung` |
| `perceptual world` | cross-language | cross-language; translated term | `sources/german/uexkuell-theoretische-biologie/encounters/03-merkzeichen-und-umwelten.md`; `sources/german/uexkuell-theoretische-biologie/glossary.yaml` | `cross-language-miss`; `translation-bottleneck` | English query for `Merkwelt` |
| `Planmäßigkeit purposiveness` | false friend | false friend; exact term | `sources/german/uexkuell-theoretische-biologie/encounters/01-prefaces.md`; `sources/german/uexkuell-theoretische-biologie/encounters/04-fuegung.md`; `sources/german/uexkuell-theoretische-biologie/glossary.yaml` | `false-friend`; `model-smoothing` | tests whether purposiveness smooths the term wrongly |
| `environment not Umwelt` | false friend | false friend; cross-language | `sources/german/uexkuell-theoretische-biologie/encounters/05-welt-und-umwelt.md`; `sources/german/uexkuell-theoretische-biologie/glossary.yaml` | `false-friend`; `model-smoothing` | should find the caution against flattening Umwelt |
| `where does apparatus decide the world before choice` | synthesis | synthesis; cross-project | `sources/german/anders-antiquiertheit-des-menschen-band1/encounters/01-preface-and-introduction.md`; `sources/german/anders-antiquiertheit-des-menschen-band1/encounters/03-phantom-und-matrize.md`; `texts/zeitmauer/threads/predecided-world.md` | `query-too-abstract`; `model-smoothing` | bridge query across Anders and Zeitmauer |
| `what treats translation as decryption rather than transfer` | synthesis | synthesis; method | `patterns/charter.md`; `00-Notes/process.md`; `00-Notes/DeepResearch/2026-05-08/bridge-openai.md` | `query-too-abstract`; `living-note-noise` | tests charter/process retrieval |
| `what says source terms should remain open` | method retrieval | synthesis; exact method | `00-Notes/process.md`; `sources/german/uexkuell-theoretische-biologie/glossary.yaml`; `sources/german/uexkuell-theoretische-biologie/journal.md` | `query-too-abstract`; `missing-glossary-cue` | tests open-term discipline |
| `where do plan and freedom collide` | synthesis | synthesis; thread retrieval | `texts/zeitmauer/threads/predecided-world.md`; `texts/zeitmauer/journal.md` | `query-too-abstract`; `model-smoothing` | paraphrase for `zm:25:plan-freedom` through the dossier |
| `where is modern media an apparatus-world` | synthesis | synthesis; source-close phrase | `sources/german/anders-antiquiertheit-des-menschen-band1/encounters/03-phantom-und-matrize.md`; `sources/german/anders-antiquiertheit-des-menschen-band1/journal.md` | `query-too-abstract`; `model-smoothing` | tests media/apparatus-world retrieval |
| `what connects Uexküll and Anders to Jünger predecided world` | synthesis | synthesis; cross-project | `texts/zeitmauer/threads/predecided-world.md`; `sources/german/uexkuell-theoretische-biologie/journal.md`; `sources/german/anders-antiquiertheit-des-menschen-band1/journal.md` | `query-too-abstract`; `omnibus-note-dominance` | bridge query using all three local anchors |
| `Funktionskreis reciprocal roles not environment` | construal | role circuit vs surrounding container | `sources/german/uexkuell-theoretische-biologie/encounters/02-funktionskreis.md`; `00-Notes/working-syntheses/2026-05-08-cognitive-grammar-as-translation-residue-diagnostic.md` | `environment-flattening`; `role-loss` | tests whether `Umwelt` retrieval keeps the reciprocal `Merkwelt` / `Wirkwelt` structure visible |
| `foot path mouth food weapon enemy Umwelt answers` | construal | co-articulated affordance | `sources/german/uexkuell-theoretische-biologie/encounters/02b-funktionskreis-undrafted.md`; `00-Notes/working-syntheses/2026-05-08-cognitive-grammar-as-translation-residue-diagnostic.md` | `adaptation-smoothing`; `model-smoothing` | tests whether fit is smoothed into adaptation |
| `beetle stone does not belong to mineralogy construal` | construal | object reprofiled by functional circle | `sources/german/uexkuell-theoretische-biologie/encounters/02b-funktionskreis-undrafted.md`; `00-Notes/working-syntheses/2026-05-08-cognitive-grammar-as-translation-residue-diagnostic.md` | `objectivist-reversion`; `chunking` | tests leading/accompanying properties and circuit-relative objecthood |
| `Merkzeichen become Merkmale of the world` | construal | morphological chain from attention to world | `sources/german/uexkuell-theoretische-biologie/encounters/03-merkzeichen-und-umwelten.md`; `sources/german/uexkuell-theoretische-biologie/glossary.yaml`; `00-Notes/working-syntheses/2026-05-08-cognitive-grammar-as-translation-residue-diagnostic.md` | `morphology-loss`; `translation-bottleneck` | tests whether retrieval keeps the `Merk-` family intact |
| `nicht das einfache Wort sondern erst der Satz Beziehungsausdruck` | construal | sentence-whole before lexical atom | `00-Notes/method/cassirer-psf-i-ch5-relation-expression.md`; `sources/german/cassirer-philosophie-der-symbolischen-formen/source/normalized/0151-kapitel-v-280-293-satz-und-beziehungsausdruck.txt`; `00-Notes/working-syntheses/2026-05-08-cognitive-grammar-as-translation-residue-diagnostic.md` | `word-first-reversal`; `living-note-noise` | tests Cassirer/Humboldt as relation-expression surface |
| `Verhältniswörtchen ist reine Verknüpfung Da- Dort-sein` | construal | predication vs being-residue | `00-Notes/method/cassirer-psf-i-ch5-relation-expression.md`; `sources/german/cassirer-philosophie-der-symbolischen-formen/source/normalized/0152-kapitel-v-293-295-kopula-und-praedikative-synthesis.txt`; `00-Notes/working-syntheses/2026-05-08-cognitive-grammar-as-translation-residue-diagnostic.md` | `pure-logic-flattening`; `query-too-abstract` | tests `ist` as relation-word rather than merely logic |
| `Gewebe menschlicher An- Absichten Durchschuss weft-thread` | construal | textile schema as structural | `texts/zeitmauer/parts/05-messbare-und-schicksalszeit.md`; `texts/zeitmauer/second-pass-messbare-und-schicksalszeit.md`; `00-Notes/working-syntheses/2026-05-08-cognitive-grammar-as-translation-residue-diagnostic.md` | `decorative-metaphor`; `translation-bottleneck` | tests whether textile language retrieves the fate/planning passage |
| `webt Schicksalszeit messbaren Zeit Unfälle` | construal | fateful/measurable time contrast | `texts/zeitmauer/parts/07-messbare-und-schicksalszeit.md`; `texts/zeitmauer/threads/time-crisis.md`; `00-Notes/working-syntheses/2026-05-08-cognitive-grammar-as-translation-residue-diagnostic.md` | `decorative-metaphor`; `model-smoothing` | tests whether `webt Schicksalszeit` is treated structurally |
| `Neue Uhren Zeitwille Haus zu Haus Hauptzeit Stationen` | construal | station-time vs smooth path | `texts/zeitmauer/parts/46-siderische-einteilungen.md`; `texts/zeitmauer/journal.md`; `00-Notes/working-syntheses/2026-05-08-cognitive-grammar-as-translation-residue-diagnostic.md` | `stage-smoothing`; `query-too-abstract` | tests `Uhren`, `Haus`, `Stationen`, and qualitative time |
| `Sheets-Johnstone rejects embodied image schemata insideness` | construal | image-schema caution | `sources/modern/hoffmeyer-biosemiotics/source/cleaned/017-from-animal-to-human.txt`; `00-Notes/working-syntheses/2026-05-08-cognitive-grammar-as-translation-residue-diagnostic.md` | `confirmation-bias`; `model-smoothing` | tests the anti-Cartesian caution inside the image-schema lane |

## Paired query tests

For selected high-pressure terms, run paired A/B queries with the source-language term retained versus translated into smoother English.

Suggested pairs:

- `Planmäßigkeit` vs `planfulness`
- `Umwelt` vs `environment`
- `Fügung` vs `fittedness`
- `Merkwelt` vs `perceptual world`

The question is not which query gets more hits. The question is whether keeping the source term intact retrieves stronger anchors with less conceptual smoothing.

## Minimal scoring rubric

For each query, record:

- `top5_anchor`: yes / no
- `top1_relevant`: yes / no
- `right_layer_first`: yes / no
- `living_needed`: yes / no
- `chats_needed`: yes / no
- `failure_labels`: use the table's labels when a miss occurs, then revise if
  the actual miss has a different cause
- `notes`: one sentence on failure mode

## Failure-type labels

Use one or more of these:

- `chunking`
- `commentary-noise`
- `corpus-shape`
- `cross-language-miss`
- `derived-index-dominance`
- `false-friend`
- `living-note-noise`
- `missing-dossier`
- `missing-glossary-cue`
- `missing-unit`
- `model-smoothing`
- `query-too-abstract`
- `needs-repo-phrase`
- `query-too-short`
- `chat-noise`
- `translation-bottleneck`
- `omnibus-note-dominance`
- `adaptation-smoothing`
- `confirmation-bias`
- `decorative-metaphor`
- `environment-flattening`
- `morphology-loss`
- `objectivist-reversion`
- `pure-logic-flattening`
- `role-loss`
- `stage-smoothing`
- `word-first-reversal`

## Current hypothesis

Likely strong:

- exact terms
- source-close phrases
- named thread retrieval when derived indexes are excluded

Likely weak:

- abstract synthesis questions
- false-friend paraphrases
- cross-language paraphrases without an exact lexical bridge
- dense-only retrieval on short distinction-heavy phrases

That is what the next benchmark phase should test, not generic retrieval quality in the abstract.
