# Uexküll Cognitive Grammar Probe Results

**Status**: first smoke-test run  
**Date**: 2026-05-08  
**Probe pack**: `00-Notes/working-syntheses/2026-05-08-uexkuell-cognitive-grammar-probe-pack.json`  
**Runner**: `tools/retrieval/run_prompt_probe.py`  
**Raw output**: `var/retrieval/uexkuell-cg-probe-gpt-4.1-mini.jsonl`  
**Model**: `gpt-4.1-mini` via OpenAI chat completions, `temperature=0`, `max_tokens=420`

## Scope

This run tests only the first four Uexküll rows from
`2026-05-08-cognitive-grammar-as-translation-residue-diagnostic.md`:

1. `Funktionskreis` / `Merkwelt` / `Wirkwelt` / `Umwelt`
2. planfulness outside the body, with foot/path, mouth/food, weapon/enemy
3. beetle-stone, leading properties, accompanying properties
4. `Merkzeichen` becoming `Merkmale`

Each case used three prompt forms:

- source-preserving prompt
- smoothed-English prompt
- adversarial paraphrase

The expected construal differences and failure labels were kept in the probe
pack but not shown to the model.

## Score Key

- `preserved`: answer keeps the expected construal visible.
- `partial`: answer avoids the main failure but drops part of the construal.
- `failed`: answer falls into one of the named failure labels.

## Results

| Probe | Prompt form | Score | Failure labels | Note |
| --- | --- | --- | --- | --- |
| `uex-01-role-circuit` | source-preserving | preserved | none | Keeps stimulus selection, effects, feedback, `Merkwelt`, `Wirkwelt`, and `Umwelt` inside a closed loop. |
| `uex-01-role-circuit` | smoothed-English | preserved | none | The word `environment` does not flatten the answer because the model reintroduces the functional circle and source terms. |
| `uex-01-role-circuit` | adversarial paraphrase | preserved | none | Rejects the adaptation/environment paraphrase as oversimplified and names the missing closed circuit. |
| `uex-02-foot-path` | source-preserving | preserved | none | Treats foot/path as a coordinated relation inside the planful `Umwelt`, not a passive background. |
| `uex-02-foot-path` | smoothed-English | partial | none | Preserves planful relation, but drifts toward organism `needs and functions`; not yet a clean failure. |
| `uex-02-foot-path` | adversarial paraphrase | preserved | none | Directly says adaptation alone is misleading and misses the functional circle. |
| `uex-03-beetle-stone` | source-preserving | partial | none | Gets leading/accompanying properties but speaks mainly of context and use; the functional-circle recutting is muted. |
| `uex-03-beetle-stone` | smoothed-English | partial | none | Correctly names form and hardness, but the prompt lets the answer stay at "what matters to the beetle" without reconstructing the circuit. |
| `uex-03-beetle-stone` | adversarial paraphrase | preserved | none | Rejects the beetle-ignorance reading and keeps leading properties in view. |
| `uex-04-merkzeichen` | source-preserving | preserved | none | Keeps the `Merk-` chain visible and tracks attention-marks becoming world-marks. |
| `uex-04-merkzeichen` | smoothed-English | partial | none | Reintroduces `Merkzeichen` and `Merkmale`, but still leans on inner signs / external features. |
| `uex-04-merkzeichen` | adversarial paraphrase | partial | `morphology-loss` | Rejects "subjective sensations create objective facts," but wrongly glosses `Merkzeichen` as subjective sensations and `Merkmale` as objective features. |

## What Preserved Construal

The model preserved construal best when either:

- the prompt kept the source terms visible, or
- the adversarial paraphrase asked for assessment rather than completion.

In those cases it usually noticed that `environment`, `adaptation`, `resources`,
and `ignorance` were too smooth. The strongest success was `uex-01`: all three
prompt forms retained the reciprocal circuit.

## What Erased or Weakened Construal

The weak spots are not full collapses, but they matter:

- `uex-03` can shrink into "properties relevant to the beetle" unless the prompt
  forces insertion into the `Funktionskreis`.
- `uex-04` is vulnerable to the familiar inner/outer split. Even while rejecting
  subjectivism, the model can gloss `Merkzeichen` as subjective sensations and
  `Merkmale` as objective features, which severs the morphology the passage is
  trying to preserve.
- The smoothed-English prompts are not yet hard enough, because the same source
  excerpt still exposes `Umwelt`, `Merkwelt`, `Wirkwelt`, `Merkzeichen`, and
  `Merkmale`.

## Failure-Label Coverage

| Failure label | Tested by | Observed? | Note |
| --- | --- | --- | --- |
| `environment-flattening` | `uex-01`, `uex-02` | no hard failure | The model kept the circle/Umwelt relation even when the prompt said `environment`. |
| `role-loss` | `uex-01`, `uex-04` | no hard failure | The role circuit survived; the `Merkzeichen` case weakened but did not fully lose the relation. |
| `adaptation-smoothing` | `uex-02` | no hard failure | The adversarial adaptation paraphrase was explicitly rejected. |
| `objectivist-reversion` | `uex-03` | no hard failure | The beetle-ignorance paraphrase was rejected; the smoothed prompt still muted the functional-circle recutting. |
| `morphology-loss` | `uex-04` | partial | `uex-04-adversarial` preserved the anti-subjectivist point but wrongly treated `Merkzeichen` as subjective sensations. |

## Judgment

This is strong enough to justify a repeatable Uexküll benchmark, but not strong
enough to claim the benchmark is finished.

The next version should create true A/B passage variants:

- source-preserving excerpt with `Umwelt`, `Funktionskreis`, `Merkzeichen`, and
  `Merkmale` retained
- smoothed excerpt where those terms are translated away
- adversarial paraphrase with no source terms visible

Then score whether the model can recover the construal without lexical crutches.
Only after that should this move to a broader Zeitmauer textile/station-time
lane.
