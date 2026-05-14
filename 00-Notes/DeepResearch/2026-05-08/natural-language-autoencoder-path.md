# Natural Language Autoencoder Path

**Status**: living-layer method note  
**Date**: 2026-05-08  
**Purpose**: translate the NLA lead into a repo-native round-trip test before
attempting an actual activation-level NLA pilot

## External Lead

Anthropic's Natural Language Autoencoder work is useful here because it changes
the standard for an explanation. The explanation is not good because it is
fluent. It is good when it preserves enough information for a reconstructor to
recover the original activation direction from the explanation alone.

Working formula:

```text
activation -> natural-language explanation -> reconstructed activation
```

The released code and checkpoints make actual activation-level experiments
possible, but that is not the first repo-native move. The first move is to test
the same discipline on the project's own interpretive objects.

Sources:

- Anthropic overview: <https://www.anthropic.com/research/natural-language-autoencoders>
- Released code: <https://github.com/kitft/natural_language_autoencoders>

## Translation Into Repo Method

For this repo, the immediate analogue is:

```text
source bundle -> compact natural-language latent -> reconstructed source obligations
```

The natural-language latent is not a generic summary. It is a compressed carrier
of obligations. A good latent should preserve:

- source terms that must remain visible
- unsettled translation pressure
- core anchors or handles
- claims the source supports
- claims the source does not support
- weakening evidence or rival readings
- downstream tests the claim should survive

The reconstruction step gets only the latent and must recover what a competent
agent should inspect next: files, handles, terms, limits, and likely failure
modes. If it cannot do that, the latent was too smooth.

This is closer to the project than ordinary embeddings because the output is
readable, contestable, and explicitly answerable to source pressure.

## Score Rubric

Each round trip gets a small scorecard. The point is not numeric precision; the
point is to locate what the compression lost.

| Axis | Good result | Failure signal |
| --- | --- | --- |
| Anchor recovery | reconstructs the file, handle, or encounter family to inspect | finds only a broad theme |
| Term pressure | keeps source terms and unsettled English visible | replaces pressure terms with fluent paraphrase |
| Distinction recovery | preserves the local distinction the note was built to protect | collapses false friends or rival concepts |
| Negative constraint | remembers what the source does not license | turns a warning into a positive theory |
| Weakening path | names what would count against the claim | makes the claim unfalsifiable |
| Hallucination check | adds no unsupported source obligations | invents anchors, sections, or claims |

## Probe 1: Predecided World

Source bundle:

- `texts/zeitmauer/threads/predecided-world.md`
- `texts/zeitmauer/threads/time-crisis.md`
- `sources/german/anders-antiquiertheit-des-menschen-band1/glossary.yaml`
- `sources/german/uexkuell-theoretische-biologie/glossary.yaml`

Compact latent:

> The local "predecided world" thread says Jünger's time wall is also a
> world-cut: plan, measure, naming, display, experiment, and technical mediation
> pre-shape the field in which action and judgment occur. It should be read with
> Uexkuell's warning that there is no neutral world before access, and Anders's
> `Vorentscheidung`, where apparatuses are not mere means but decisions already
> made over us. The claim weakens if later Jünger treats planning and technique
> as neutral tools whose danger lies only in misuse.

Reconstruction from latent:

- inspect `thread:predecided-world` before broad synthesis
- recover `thread:time-crisis` as the larger pressure field
- expect Jünger handles around plan, naming, technique, built form, display,
  experiment, descent, and worker apparatus
- inspect Anders `Vorentscheidung` and `Weltphantom`, not only generic
  technology critique
- inspect Uexkuell `Umwelt`, `Merkwelt`, `Wirkwelt`, and `Fügung` as the
  non-neutral-access pressure
- do not claim Jünger has simply become Uexkuell or Anders

Score:

| Axis | Result |
| --- | --- |
| Anchor recovery | strong: the dossier and cross-project source campaigns are recoverable |
| Term pressure | strong: `Vorentscheidung` and `Umwelt` remain visible |
| Distinction recovery | good: neutral-tool reading is separated from prior world-cut |
| Negative constraint | good: no direct identity between Jünger, Uexkuell, and Anders |
| Weakening path | strong: later neutral-instrument evidence would count against it |
| Hallucination check | acceptable: latent points to families, not invented sections |

Loss:

The latent does not preserve enough of the fine-grained Jünger handle path by
itself. It recovers the dossier, but not the full sequence from `zm:25` through
`zm:177`. If this were an agent-memory object, it should carry either the
handle family or a pointer to the dossier's useful path.

## Probe 2: Anders Disproportion and Predecision

Source bundle:

- `sources/german/anders-antiquiertheit-des-menschen-band1/glossary.yaml`
- `sources/german/anders-antiquiertheit-des-menschen-band1/journal.md`
- `sources/german/anders-antiquiertheit-des-menschen-band1/encounters/01-preface-and-introduction.md`

Compact latent:

> The first Anders queue makes `prometheisches Gefälle` and `Vorentscheidung`
> structurally real. `prometheisches Gefälle` names the widening asynchrony
> between what humans make and what they can imagine, feel, answer for, or
> bodily inhabit. `Vorentscheidung` names apparatuses as decisions made before
> local choice begins, not merely background influence or bias. Keep
> `prometheisches Gefälle`, `Weltphantom`, and `Apokalypseblindheit` visibly
> open; let `predecision` stand only provisionally.

Reconstruction from latent:

- inspect Anders Encounter 01 and the journal entry "Encounter 01 worked"
- recover glossary handles `term:prometheisches-gefaelle` and
  `term:vorentscheidung`
- keep `Weltphantom` and `Apokalypseblindheit` near the same campaign arc
- avoid translating `prometheisches Gefälle` as only "gap"
- avoid reducing `Vorentscheidung` to bias, influence, or prior conditioning
- expect the campaign to connect shame, media, worldlessness, and apocalypse as
  surfaces of one product-world disproportion

Score:

| Axis | Result |
| --- | --- |
| Anchor recovery | strong: source campaign, encounter, journal, and glossary are recoverable |
| Term pressure | strong: the German terms and provisional English are preserved |
| Distinction recovery | strong: asynchrony and predecision are not flattened into generic AI-risk terms |
| Negative constraint | strong: bias/influence readings are explicitly rejected |
| Weakening path | moderate: the latent says what not to flatten, but less clearly what later evidence would weaken the campaign |
| Hallucination check | good: no new Anders claim is introduced |

Loss:

The latent compresses the five-encounter campaign into one arc and risks making
the unity sound more settled than the source campaign warrants. A stronger
version should carry the bounded-campaign status: Anders is live and major, but
not yet promoted to a full `texts/` project.

## Probe 3: Bridge Claims and Falsification

Source bundle:

- `00-Notes/DeepResearch/2026-05-08/bridge-openai.md`
- `00-Notes/DeepResearch/2026-05-08/bridge-openai-retrieval-probes.md`
- `00-Notes/process.md`
- `00-Notes/DeepResearch/2026-05-08/embedding-prototype.md`

Compact latent:

> The OpenAI bridge survives best as procedure, not analogy. Philosophical
> terms can discipline interpretability only when they generate failure-prone
> tests: retrieve source anchors before synthesis, separate critical horizons
> from mechanistic claims, and make feature explanations survive revision,
> counterevidence, or intervention. Retrieval is not the intelligence layer; it
> is a falsification aid that shows whether bridge language still points back to
> source obligations or has smoothed them away.

Reconstruction from latent:

- inspect `bridge-openai.md` for the larger research survey
- inspect `bridge-openai-retrieval-probes.md`, especially probes 4 and 5
- inspect `embedding-prototype.md` for the practical result that BM25/hybrid
  retrieval is a corpus-discipline tool, not a dense semantic oracle
- recover `process.md` as the local norm for adversarial/contestable work
- avoid saying Cassirer, Uexkuell, Anders, or Hoffmeyer explain model internals
  without an intervening experiment
- ask what would break the bridge claim before asking what analogy sounds good

Score:

| Axis | Result |
| --- | --- |
| Anchor recovery | strong: all relevant notes are recoverable |
| Term pressure | moderate: method terms survive, but source-language pressure is indirect |
| Distinction recovery | strong: critical constraint is separated from mechanistic explanation |
| Negative constraint | strong: analogy is blocked unless it becomes a test |
| Weakening path | strong: intervention, counterevidence, and failed retrieval can break claims |
| Hallucination check | good: no model-internal fact is asserted |

Loss:

The latent is methodologically clean but source-thin. It should not replace the
source-facing probes. It is a gate for later synthesis, not itself evidence for
any particular interpretability claim.

## Current Judgment

This path is better than more retrieval work as the next conceptual branch, but
it is not a substitute for actual NLA. It is the intermediate discipline that
should make an actual NLA pilot interpretable.

Working sequence:

1. Use repo-native natural-language latents to test whether notes preserve
   source obligations under compression.
2. Once the rubric is stable, run a small actual NLA pilot on open-model
   activations for selected passages.
3. Compare NLA explanations against repo latents.
4. Treat disagreements as the research object: model-internal smoothing,
   source-term loss, false-friend collapse, or unexpected preservation.

## Actual NLA Pilot Criteria

Do not start by training an NLA. The first real pilot should use released
checkpoints and a small passage set.

Candidate passage set:

- Uexkuell: `Umwelt`, `Merkwelt`, `Wirkwelt`, `Fügung`
- Anders: `prometheisches Gefälle`, `Vorentscheidung`, `Weltphantom`
- Zeitmauer: `predecided-world` handle path
- Bridge note: falsification-before-analogy passages

Pilot question:

Can an open model's NLA explanation preserve the same distinctions the repo
latent preserves, or does it translate them into fluent generic themes?

Expected useful failures:

- `Umwelt` becomes generic "environment"
- `Fügung` becomes generic "fit"
- `Vorentscheidung` becomes "bias" or "prior context"
- `prometheisches Gefälle` becomes a generic responsibility gap
- bridge discipline becomes an analogy instead of a test protocol

Engineering note:

The released NLA path requires model checkpoint downloads, activation capture,
and GPU-oriented inference infrastructure. It should be a bounded experiment,
not a new repo dependency, until the small round-trip protocol proves that the
comparison will answer a real project question.

