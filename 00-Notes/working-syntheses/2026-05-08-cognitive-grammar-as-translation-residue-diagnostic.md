# Cognitive Grammar as Translation-Residue Diagnostic

**Status**: working synthesis; source-visible probe ledger  
**Date**: 2026-05-08  
**Trigger**: May 8 OpenAI DeepResearch bridge notes plus the earlier chat thread on cognitive grammar, translation residue, and LLM interpretability.

## Working Claim

The useful move is not to import Cognitive Grammar as a master frame. It is to
use a small part of its vocabulary as a diagnostic for translation residue:
where the English is lexically plausible but loses the source's construal of a
scene.

This makes the chat claim "grammar carries meaning" source-visible. The test is
local: can the construal vocabulary name losses already visible in the repo's
translation decisions, and can it generate probes that fail in informative ways?

Key constraint from the May 8 bridge notes: philosopher-facing claims should be
turned into retrieval, probing, intervention, and failure criteria, not left as
analogical gloss. See `00-Notes/DeepResearch/2026-05-08/bridge-openai-v2.md`.

## Diagnostic Vocabulary

Use only as much as the passage earns:

- **Profiling**: what the expression makes figure against a background.
- **Figure / ground**: which entity is foregrounded as moving, acting, or being
  located, and which functions as reference field.
- **Trajector / landmark**: asymmetric relational construal; reversing the
  relation changes the scene.
- **Scope**: how wide the relevant scene is; inside-body, organism-world,
  earth-history, or cosmic frame.
- **Sequential vs summary scanning**: whether the relation is presented as a
  linear process or as a configured whole.
- **Image schema**: path, circle, container, boundary, force, station, house,
  weaving, clock.

## Passage Ledger

### 1. Uexküll: `Funktionskreis` as Role Circuit

- Source locus: `sources/german/uexkuell-theoretische-biologie/encounters/02-funktionskreis.md` lines 31-56 and 73-104.
- Source phrase: `aus den allgemeinen Wirkungen der Außenwelt bestimmte Reize auswählt`, `diese beeinflussen ihrerseits die Reize`, `Wirkwelt und Merkwelt bilden ... Umwelt`.
- Current translation: "selects from the general effects of the outer world certain stimuli"; "these in their turn influence the stimuli"; "Wirkwelt and Merkwelt form a coherent whole ... Umwelt."
- What English loses: `environment` would profile a surrounding container. The source profiles reciprocal role-formation: selected stimuli, steering, effects, feedback, Merkwelt, Wirkwelt, Umwelt.
- Construal type: circle schema; trajector/landmark relation is distributed across animal, marked stimulus, steering, and effected world.
- Residue kind: lexical, grammatical, conceptual.
- Rival reading: `functional circle` may still sound too static; `circuit` might better preserve feedback but loses the source's circular-world imagery.
- Possible LLM probe: compare answers to `Umwelt` left untranslated, `environment`, and `organism-bound functional world`; check whether the model preserves reciprocal roles or describes a neutral surrounding.

### 2. Uexküll: Planfulness Outside the Body

- Source locus: `sources/german/uexkuell-theoretische-biologie/encounters/02b-funktionskreis-undrafted.md` lines 27-48 and 54-74.
- Source phrase: `den außerhalb des Körpers in der Umwelt verlaufenden Teil`, `biologisches Gefüge`, `Wo ein Fuß ist, da ist auch ein Weg`.
- Current translation: "the part of the circle that runs outside the body, in the Umwelt"; "biological fabric"; "where there is a foot, there is also a path."
- What English loses: a smooth `external environment` phrasing hides that the outside is still inside the functional circle. `A path exists for a foot` is not enough; the German construes paired affordance as rule-bound fit.
- Construal type: scope expansion; figure/ground shift from body-contained organism to organism-world circuit; path schema.
- Residue kind: grammatical and conceptual, with lexical pressure around `Umwelt`, `Gefüge`, `Planmäßigkeit`.
- Rival reading: the foot/path line could be treated as teleological overstatement rather than a biological construal claim.
- Possible LLM probe: ask whether a passage says "organisms adapt to available paths" or "path and foot are co-articulated within one functional circle." The second is closer; the first smooths into adaptation.

### 3. Uexküll: Leading vs Accompanying Properties

- Source locus: `sources/german/uexkuell-theoretische-biologie/encounters/02b-funktionskreis-undrafted.md` lines 89-104 and 110-123.
- Source phrase: `Der Stein ... ist nur ein Käferweg und gehört nicht in die Mineralogie`; `leitende` / `begleitende Eigenschaften`; `Einfügung ... in den Funktionskreis`.
- Current translation: "The stone a beetle climbs is only a beetle-path and does not belong to mineralogy"; "leading / accompanying properties"; "insertion ... into the functional circle."
- What English loses: `properties` sounds object-intrinsic. Uexküll is recutting the object by circuit-relative guidance: the same stone is not the same object under the beetle's path relation.
- Construal type: profiling and scope; mineralogical object is backgrounded, path-function is profiled.
- Residue kind: lexical and conceptual.
- Rival reading: this may be only methodological abstraction, not an ontological claim about the stone.
- Possible LLM probe: present the beetle-stone sentence and ask whether mineral properties are false, irrelevant, or backgrounded by a different functional construal.

### 4. Uexküll: `Merkzeichen` Becoming `Merkmale`

- Source locus: `sources/german/uexkuell-theoretische-biologie/encounters/03-merkzeichen-und-umwelten.md` lines 93-107 and 113-130.
- Source phrase: `Merkzeichen unserer Aufmerksamkeit werden zu Merkmalen der Welt`.
- Current translation: "the Merkzeichen of our attention become the Merkmale of the world."
- What English loses: `signs` and `features` would sever the morphological bridge. The German carries a transformation from inner marked attention to outer marked world.
- Construal type: trajector/landmark plus profiling; attention's marks are reprofiled as world-marks.
- Residue kind: lexical, grammatical, conceptual.
- Rival reading: the line may be a terminological proposal for measurement psychology rather than a general theory of world-formation.
- Possible LLM probe: compare `inner signs become external features` with `marks of attention become marks of the world`; check whether the model preserves the same `Merk-` chain.

### 5. Uexküll: `Merkding`, `Wirkding`, `Gegengefüge`

- Source locus: `sources/german/uexkuell-theoretische-biologie/encounters/04-fuegung.md` lines 101-115 and 121-137.
- Source phrase: `merkmaltragende Eigenschaften`, `wirkmaltragende Eigenschaften`, `Gegengefüge`, `subjektives Bindungsmittel`.
- Current translation: "merkmal-bearing properties"; "wirkmal-bearing properties"; "Gegengefüge"; "subjective binding medium."
- What English loses: `object parts` would flatten the subject-centered recutting. The passage profiles the object as reorganized by marking and effecting.
- Construal type: figure/ground and profiling; the object is not simply divided, but crystallized around the subject as center.
- Residue kind: lexical, grammatical, conceptual.
- Rival reading: `crystallizes all objects over again` might overstate if read metaphysically; it may be a methodological diagram of Umwelt analysis.
- Possible LLM probe: ask the model to diagram object, Merkding, Wirkding, and Gegengefüge; failure mode is treating them as ordinary physical parts.

### 6. Cassirer/Humboldt: Sentence Before Word

- Source locus: `sources/german/cassirer-philosophie-der-symbolischen-formen/source/normalized/0151-kapitel-v-280-293-satz-und-beziehungsausdruck.txt` lines 29-62.
- Source phrase: `nicht das einfache Wort, sondern erst der Satz`; `die Wörter gehen ... aus dem Ganzen der Rede hervor`; `Bestimmungen ... der Beziehung`.
- Working translation: "not the simple word, but only the sentence"; "words emerge from the whole of speech"; "determinations that serve the expression of relation."
- What English loses: a word-first translation workflow silently reverses the claim. Relation is not an add-on after lexical selection; it is the unit from which words become meaningful.
- Construal type: scope and summary scanning; the sentence-whole profiles relation before isolated terms.
- Residue kind: grammatical and conceptual.
- Rival reading: Cassirer is describing language genesis, not necessarily prescribing translation method.
- Possible LLM probe: give the same sentence with shuffled clauses and ask which translation preserves relation before word choice.

### 7. Cassirer: Parataxis, Hypotaxis, and Perspective

- Source locus: `sources/german/cassirer-philosophie-der-symbolischen-formen/source/normalized/0151-kapitel-v-280-293-satz-und-beziehungsausdruck.txt` lines 284-328 and 331-367.
- Source phrase: `keine perspektivische Unterscheidung zwischen Vorder- und Hintergrund`; relation grasped by detours through `Substanz` and `Eigenschaft`.
- Working translation: "no perspectival distinction between foreground and background"; pure relation is grasped only by way of substance and property.
- What English loses: adding polished subordination can fake a relation-organ the source says may not yet be present. Smooth connectives can become interpretive violence.
- Construal type: figure/ground, foreground/background, sequential vs hierarchical relation.
- Residue kind: grammatical and conceptual.
- Rival reading: Cassirer's developmental language may be historically dated; use the passage as a warning about relation-media, not as a hierarchy of languages.
- Possible LLM probe: ask for two translations of a paratactic sentence, one preserving parataxis and one adding logical subordination; then ask what each construes.

### 8. Cassirer: Copula as Pure Linkage, with Locative Residue

- Source locus: `sources/german/cassirer-philosophie-der-symbolischen-formen/source/normalized/0152-kapitel-v-293-295-kopula-und-praedikative-synthesis.txt` lines 1-76.
- Source phrase: `Ausdruck der reinen Verknüpfung`; `Verhältniswörtchen ist`; `Da- oder Dort-sein`.
- Working translation: "`is` as expression of pure linkage"; "`is` as relation-word"; existence here or there.
- What English loses: English `is` looks like a universal predicative tool, but Cassirer stresses the history of existential, local, temporal, and bodily residues inside being-language.
- Construal type: relation schema; locative and temporal profiling hidden inside predication.
- Residue kind: lexical, grammatical, conceptual.
- Rival reading: this is a broad linguistic-philosophical claim and should not be used to overread every `sein` in German sources.
- Possible LLM probe: compare prompts that translate `ist` as predication, existence, location, and event-state; check whether the model notices the construal shift.

### 9. Zeitmauer: Fate as Weft in the Fabric of Planning

- Source locus: `texts/zeitmauer/parts/05-messbare-und-schicksalszeit.md` lines 76 and 92-104.
- Source phrase: `Gewebe menschlicher An- und Absichten`; `eines Durchschusses bedarf`.
- Current translation: "this fabric of human views and intentions"; "does not require a weft-thread."
- What English loses: if `Durchschuss` is rendered as generic `addition` or `supplement`, the textile model disappears. Jünger is construing planning as a fabric that is structurally weak without a cross-thread from fate.
- Construal type: weaving schema; force/stability through cross-directional insertion.
- Residue kind: lexical and conceptual.
- Rival reading: the textile may be a local metaphor rather than a system-level model; recurrence across the time-crisis thread is what keeps it load-bearing.
- Possible LLM probe: ask whether the passage uses textile language ornamentally or to explain why plans need cross-binding by fate; test against nearby `weaves fateful time`.

### 10. Zeitmauer: Tragedy Weaves `Schicksalszeit`

- Source locus: `texts/zeitmauer/parts/07-messbare-und-schicksalszeit.md` lines 25 and 41-52.
- Source phrase: `webt Schicksalszeit`; `In der messbaren Zeit ... nur Unfaelle`.
- Current translation: "weaving fateful time"; "In measurable time ... only accidents."
- What English loses: `fate happens in tragedy` is too propositional. The German makes tragedy an activity that weaves a time-order not available to measurable time.
- Construal type: weaving schema; domain contrast between fateful time and measurable time.
- Residue kind: lexical and conceptual.
- Rival reading: `weaves` may be literary register rather than technical construal; the counterweight is its recurrence beside `Durchschuss`, `Einschuss`, and the textile journal notes.
- Possible LLM probe: ask for the inferential difference between "tragedy represents fate" and "tragedy weaves fateful time."

### 11. Zeitmauer: Clocks, Houses, Stations

- Source locus: `texts/zeitmauer/parts/46-siderische-einteilungen.md` lines 17-27 and 33-50.
- Source phrase: `Neue Uhren`; `Zeitwille`; `von Haus zu Haus`; `Hauptzeit auf den Stationen`.
- Current translation: "New clocks"; "time-will"; "from house to house"; "the main time is spent at the stations."
- What English loses: `periods` and `stages` would flatten the station/house contrast. The passage opposes continuous transit to qualitative dwelling.
- Construal type: clock schema, path schema, station/house container schema; sequential vs qualitative scanning.
- Residue kind: lexical, grammatical, conceptual.
- Rival reading: the astrological house-language may be comparative imagery rather than the governing ontology of the section.
- Possible LLM probe: ask whether the passage construes evolution as smooth transit, punctuated stations, or house-to-house reconfiguration; check if a model notices that `new clocks` revise the past.

### 12. Hoffmeyer / Sheets-Johnstone: Image Schema Under Pressure

- Source locus: `sources/modern/hoffmeyer-biosemiotics/source/cleaned/017-from-animal-to-human.txt` lines 441-461.
- Source phrase: Sheets-Johnstone rejects "embodied image schemata"; `insideness` is a corporeally constituted basic category.
- Diagnostic paraphrase: body is not a container for preconceptual schemas; corporeal-kinetic forms are already conceptually load-bearing.
- What English loses: this is already English, so the residue is not translation loss but framework loss. A Lakoff/Johnson-friendly paraphrase can miss the anti-Cartesian objection inside Sheets-Johnstone's critique.
- Construal type: container schema under challenge; body-as-source, not body-as-container.
- Residue kind: conceptual.
- Rival reading: Hoffmeyer is reporting Sheets-Johnstone sympathetically; this should be used as a caution, not as the repo's settled position on image schemas.
- Possible LLM probe: ask whether `insideness` is a preconceptual schema, a corporeal concept, or a metaphorical abstraction; expected answer should preserve the critique of "embodied" as cosmetic if it keeps body and concept apart.

## Behavioral Probe Seed

Use these only after the ledger has been read. The point is not model judgment in
general, but whether a model preserves the construal difference.

| Probe | Source-preserving prompt | Smoothed prompt | Adversarial paraphrase | Expected construal difference | Failure label |
| --- | --- | --- | --- | --- | --- |
| `Umwelt` role circuit | Explain `Funktionskreis`, `Merkwelt`, `Wirkwelt`, and `Umwelt` from the passage. | Explain the animal's environment. | The organism adapts to external surroundings. | Preserves reciprocal role-formation rather than container surroundings. | `role-loss`, `environment-flattening` |
| Foot/path fit | What does "where there is a foot, there is also a path" do in the functional-circle argument? | Why do organisms find paths in nature? | This is a poetic statement about adaptation. | Co-articulated fit, not simple adaptation. | `adaptation-smoothing` |
| Beetle-stone | Why does the stone "not belong to mineralogy" here? | What properties of the stone matter to the beetle? | Mineralogy is irrelevant because the beetle is ignorant. | Object is reprofiled by functional circle, not by mental ignorance. | `objectivist-reversion` |
| `Merkzeichen` chain | Track `Merkzeichen` to `Merkmale` without translating the morpheme away. | Inner signs become outer features. | Uexküll means subjective sensations create objective facts. | Preserves mark-chain and lawfulness without subjectivist collapse. | `morphology-loss`, `subjectivism` |
| Cassirer sentence-whole | Why does Cassirer/Humboldt start from sentence rather than word? | Summarize his theory of vocabulary. | Words are combined into sentences. | Relation-whole precedes isolated word. | `word-first-reversal` |
| Cassirer copula | How can `is` carry locative or temporal residue? | Explain predication. | `Is` is just a logical connector. | Relation-word has historical/local residues. | `pure-logic-flattening` |
| Jünger textile | Why does `Durchschuss` matter here? | What supplement do plans need? | Fate is an emotional addition to planning. | Cross-thread stabilizes the fabric of planning. | `decorative-metaphor` |
| Jünger station-time | Contrast `Fahrt`, `Stationen`, and `Haus zu Haus`. | Explain stages of evolution. | Evolution is a journey with milestones. | Qualitative dwelling replaces smooth transit. | `stage-smoothing` |
| Time wall naming | Why is naming dangerous beyond the `Zeitmauer`? | Why is the future hard to describe? | The author is warning against bad predictions. | Names have spell-like risk at a boundary of historical language. | `forecast-flattening` |
| Sheets-Johnstone | Why does she reject "embodied image schemata"? | Summarize image schema theory. | She says image schemas are embodied. | Body is not a container for detachable schemas. | `confirmation-bias` |

## Retrieval-Eval Query Additions

These are the construal-specific queries worth adding to the retrieval seed:

| Query | Expected anchor | Test focus | Failure labels |
| --- | --- | --- | --- |
| `Funktionskreis reciprocal roles not environment` | Uexküll encounter 02 | role circuit vs surrounding container | `environment-flattening`, `role-loss` |
| `foot path mouth food weapon enemy Umwelt answers` | Uexküll encounter 02b | co-articulated affordance | `adaptation-smoothing` |
| `beetle stone does not belong to mineralogy construal` | Uexküll encounter 02b | object reprofiled by functional circle | `objectivist-reversion` |
| `Merkzeichen become Merkmale of the world` | Uexküll encounter 03 | morphological chain | `morphology-loss` |
| `nicht das einfache Wort sondern erst der Satz Beziehungsausdruck` | PSF I ch. V method note / source | sentence-whole before lexical atom | `word-first-reversal` |
| `Verhältniswörtchen ist reine Verknüpfung Da- Dort-sein` | PSF I ch. V method note / source | predication vs being-residue | `pure-logic-flattening` |
| `Gewebe menschlicher An- Absichten Durchschuss weft-thread` | Zeitmauer part 05 | textile schema as structural | `decorative-metaphor` |
| `webt Schicksalszeit messbaren Zeit Unfälle` | Zeitmauer part 07 | fateful/measurable time contrast | `decorative-metaphor` |
| `Neue Uhren Zeitwille Haus zu Haus Hauptzeit Stationen` | Zeitmauer part 46 | station-time vs smooth path | `stage-smoothing` |
| `Sheets-Johnstone rejects embodied image schemata insideness` | Hoffmeyer cleaned ch. 17 | image-schema caution | `confirmation-bias` |

## What This Licenses

- A small working ledger for translation residue as construal loss.
- A behavioral benchmark seed before any mechanistic interpretability work.
- Retrieval evaluation queries that test grammar/construal, not only terms.

## What This Does Not License

- No new `frame:*` object.
- No promotion of Cognitive Grammar into `patterns/`.
- No claim that Langacker, Fillmore, Lakoff, Talmy, or Goldberg settle the repo's method.
- No SAE or activation work until one passage-family has a behavioral probe that fails usefully.

## Current Judgment

The strongest first probe is Uexküll. The `Merk* / Wirk* /
Funktionskreis / Umwelt` family already forces the exact issue: English can be
fluent while losing the construal. Cassirer supplies the methodological warrant
that relation can be carried by grammar and syntax rather than by isolated
terms. Zeitmauer shows that images like weaving, houses, clocks, stations, and
walls can be structural rather than decorative. Hoffmeyer/Sheets-Johnstone keeps
the image-schema lane honest by warning that "embodied" can itself become a
cosmetic abstraction.

## Follow-on Probe Run

The first Uexküll-only smoke test is now recorded in:

- `00-Notes/working-syntheses/2026-05-08-uexkuell-cognitive-grammar-probe-pack.json`
- `00-Notes/working-syntheses/2026-05-08-uexkuell-cognitive-grammar-probe-results.md`

Result: strong enough to justify a repeatable Uexküll benchmark, but not yet
strong enough to move straight to mechanistic interpretability. The next version
needs true A/B passage variants where source terms are retained in one excerpt
and smoothed away in the other.

The harder A/B run is recorded in:

- `00-Notes/working-syntheses/2026-05-08-uexkuell-cognitive-grammar-ab-probe-pack.json`
- `00-Notes/working-syntheses/2026-05-08-uexkuell-cognitive-grammar-ab-probe-results.md`

Result: role-circuit and foot/path construals survive source-term removal, but
the `Merkzeichen -> Merkmale` chain fails even with source terms visible because
the model slides toward an inner-subjective / outer-objective schema. The next
bounded step is a scoring rubric for the fragile Uexküll cases before moving
the method to Zeitmauer.
