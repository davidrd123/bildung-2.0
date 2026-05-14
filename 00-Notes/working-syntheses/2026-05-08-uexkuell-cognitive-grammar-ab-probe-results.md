# Uexküll Cognitive Grammar A/B Probe Results

**Status**: harder A/B probe run  
**Date**: 2026-05-08  
**Probe pack**: `00-Notes/working-syntheses/2026-05-08-uexkuell-cognitive-grammar-ab-probe-pack.json`  
**Runner**: `tools/retrieval/run_prompt_probe.py`  
**Raw output**: `var/retrieval/uexkuell-cg-ab-probe-gpt-4.1-mini.jsonl`  
**Model**: `gpt-4.1-mini` via OpenAI chat completions, `temperature=0`, `max_tokens=420`

## Purpose

The first smoke test showed that source terms in the excerpt were acting as
lexical crutches. This A/B run tests the same four Uexküll cases with:

- source terms retained
- source terms translated away inside a smoothed excerpt
- adversarial paraphrase with no source terms visible

The question is whether the model can preserve construal from structure alone.

## Score Key

- `preserved`: answer keeps the expected construal visible.
- `partial`: answer avoids the main false paraphrase but drops part of the construal.
- `failed`: answer falls into one of the named failure labels.

## Results

| Probe | Condition | Score | Failure labels | Note |
| --- | --- | --- | --- | --- |
| `uex-ab-01-role-circuit` | source terms retained | preserved | none | Keeps closed circuit, selected stimuli, effects, feedback, `Merkwelt`, `Wirkwelt`, and `Umwelt`. |
| `uex-ab-01-role-circuit` | terms translated away | preserved | none | Still recovers reciprocal loop from structure alone: responses affect environment, which shapes future stimuli. |
| `uex-ab-01-role-circuit` | adversarial no terms | preserved | none | Rejects the passive input/adaptation construal and names missing mutual feedback. |
| `uex-ab-02-foot-path` | source terms retained | preserved | none | Treats foot/path, mouth/food, weapon/enemy as correspondences inside a planful biological circle. |
| `uex-ab-02-foot-path` | terms translated away | preserved | none | Keeps co-constitution and planful relation even without `Umwelt` or `Funktionskreis`. |
| `uex-ab-02-foot-path` | adversarial no terms | preserved | none | Rejects mere adaptation to external resources and names the lost organism-counterpart relation. |
| `uex-ab-03-beetle-stone` | source terms retained | partial | `role-loss` | Gets leading/accompanying properties, but the object-reprofiling by the circuit is muted. |
| `uex-ab-03-beetle-stone` | terms translated away | partial | `role-loss` | Keeps functional role, form, and hardness, but stays near "significance for the beetle" rather than circuit insertion. |
| `uex-ab-03-beetle-stone` | adversarial no terms | preserved | none | Rejects beetle-ignorance and recovers selective sensitivity to relevant features. |
| `uex-ab-04-merk-chain` | source terms retained | failed | `morphology-loss`, `role-loss` | Despite visible `Merk-`, it recasts the movement as subjective inner markers representing objective outer features. |
| `uex-ab-04-merk-chain` | terms translated away | failed | `morphology-loss`, `role-loss` | The smoothed excerpt collapses into inner signs defining attributed external features. |
| `uex-ab-04-merk-chain` | adversarial no terms | partial | `morphology-loss` | It notices the paraphrase overstates subjective creation, but preserves only thresholding, not the mark-chain. |

## Failure-Label Coverage

| Failure label | Tested by | Observed? | Note |
| --- | --- | --- | --- |
| `environment-flattening` | `uex-ab-01`, `uex-ab-02` | no | Reciprocal organism-world structure survived term removal. |
| `adaptation-smoothing` | `uex-ab-01`, `uex-ab-02` | no | The model consistently rejected mere adaptation in adversarial prompts. |
| `objectivist-reversion` | `uex-ab-03` | no hard failure | Beetle-ignorance was rejected; the weaker issue was loss of circuit insertion. |
| `role-loss` | `uex-ab-03`, `uex-ab-04` | yes | `uex-ab-03` weakens the functional circle; `uex-ab-04` loses the role of the shared `Merk-` chain. |
| `morphology-loss` | `uex-ab-04` | yes | The model repeatedly turns `Merkzeichen` / `Merkmale` into inner subjective signs versus external objective features. |

## What the A/B Run Shows

The strongest finding is negative and useful: `Merkzeichen -> Merkmale` is the
hard case. Even with the source terms retained, the model slides toward the
familiar subject/object schema. That means the relevant residue is not only a
lexical problem. The morphology helps the human reader, but the model still
needs a prompt or scoring rubric that protects the mark-chain from being
reinterpreted as mental representation of objective features.

The role-circuit and foot/path cases are more robust. Their construal survived
the smoothed excerpts because the reciprocal loop and counterpart structure
were still explicit in the English.

The beetle-stone case sits between them. The model rejects the crude ignorance
paraphrase, but it does not naturally recover the stronger claim: the stone is
reprofiled by insertion into a functional circle, not merely considered under
"properties relevant to the beetle."

## Benchmark Judgment

This is now strong enough to become a repeatable Uexküll benchmark with two
subtests:

1. **Robust relation tests**: role circuit and foot/path. These check whether a
   model preserves reciprocal organism-world construal without source terms.
2. **Fragile residue tests**: beetle-stone and `Merkzeichen -> Merkmale`. These
   are the useful failure probes.

Do not move straight to Zeitmauer as a benchmark suite yet. The next bounded
step should be a scoring rubric for the fragile Uexküll cases, especially:

- whether the answer mentions insertion into a functional circle
- whether `Merkzeichen` and `Merkmale` are kept as one mark-family
- whether the answer avoids inner-subjective versus outer-objective flattening

Once that rubric can be applied consistently, the Zeitmauer textile/station
lane is the right next domain.
