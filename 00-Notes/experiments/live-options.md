# Live Options

Purpose: keep a running list of experiment ideas that have real promise but have not yet been run, plus a record of which speculative prompts are not yet earned.

Status: living-layer queue. This is not a result note and not a standing architecture file.

## Current Completed Chain

Completed so far:

- `experiment-01-glossary-collision.md`
- `experiment-02-limit-of-orderable.md`
- `experiment-03-passage-threshold-test.md`
- `experiment-03a-german-source-check.md`
- `experiment-03b-independent-subagent-check.md`
- `experiment-03c-second-independent-subagent.md`

What that chain established:

- packet construction matters as much as the result
- same-packet convergence is useful evidence
- diversified negatives are stronger evidence than repeated elegant agreement
- German residue often shows where English creates false parallels
- a higher-resolution packet index has still **not** earned its entrance

## Near-Term Candidates

These are the next experiments most clearly indicated by the current work.
They remain the first-priority queue.

### 1. Reification-detection test

Question:

- can Cassirer's reification pressure discriminate between productive and hardened uses of ordering terms in `Zeitmauer`

Likely materials:

- Cassirer passages where methodological gains harden into metaphysical guarantees
- `Zeitmauer` terms under pressure:
  - `Weltplan`
  - `Urgrund`
  - possibly `Schöpfungsplan`

Success condition:

- one or two clear discriminating cases
- one clear non-case where the term stays productive rather than reified

Failure condition:

- the Cassirer packet only redescribes everything as suspicious depth-language

Why it is promising:

- grounded in earned `Erkenntnisproblem` work
- directly pressures live `Zeitmauer` vocabulary
- falsifiable and narrow

### 2. Shaped-gap completion test

Question:

- can a structural gap clearly marked in one source be illuminated by material from another source without collapsing into decoration or analogy

Control requirement:

- include one plausible decoy completion that should fail

Success condition:

- the candidate completion survives return to both sources
- the decoy is rejected for a specific reason

Failure condition:

- every candidate looks suggestive, and no rejection is discriminating

Why it is promising:

- this is the strongest concrete form of the "shaped absence" idea
- Experiments 01-03 already act as prototypes for it

### 3. Translation-residue clustering

Question:

- do recorded close-reading losses cluster around specific kinds of German reasoning-pressure, or are they mainly local quirks

Likely materials:

- `texts/erkenntnisproblem-vol1/reading/close-reading-ledger.md`
- relevant `Zeitmauer` journal pressure points
- a bounded set of translation-resistance examples

Success condition:

- one or two recurring residue types become visible

Failure condition:

- the examples refuse meaningful grouping

Why it is promising:

- grounded in actual translation work
- could improve both future translation and future packet construction

### 4. Inverse-Bayle / self-critique test

Question:

- when given Cassirer-style reification cases, can an LLM detect analogous overreach or loss of warrant in its own constituting outputs

Success condition:

- the model can identify at least some cases where its own constructive output outran the source support

Failure condition:

- it keeps constituting without a real Baylean dissolving move

Why it is promising:

- directly tied to the completed `Erkenntnisproblem` run
- relevant to how these experiments themselves are being conducted

## Deployment Candidates

These are not next by default.

They become live when a modern question actually demands outward deployment of earned material rather than another inward-facing comparison. Movement from the near-term queue into this section is demand-driven, not count-driven.

### 5. Chain-of-thought as discursive adequacy test

Question:

- does the Cusanus `ratio` / `intellectus` structure predict which tasks benefit from chain-of-thought prompting and which do not

Likely materials:

- the earned Cusanus run in `Erkenntnisproblem`
- close-reading notes on discursive ordering, suspension, and the limit of serial reasoning
- a bounded set of modern task examples where chain-of-thought helps, fails, or adds nothing

Success condition:

- the historical framework produces a discriminating prediction rather than merely redescribing “hard tasks need more steps”

Failure condition:

- the framework maps trivially onto existing prompt folklore without adding explanatory precision

Why it is promising:

- it would use earned philosophical material on a live modern question
- it is outward-facing without requiring a full theory of LLM cognition

### 6. Constitutive vs. indicative in LLM outputs

Question:

- can the constitutive / indicative distinction discriminate between different kinds of LLM output more sharply than current labels like retrieval, generation, or creativity

Likely materials:

- Hamburg's exposition of the constitutive / indicative distinction
- relevant Festschrift material already encountered
- a bounded set of LLM outputs from project work or comparable controlled examples

Success condition:

- the distinction cuts LLM behavior at a joint that current vocabulary does not capture well

Failure condition:

- the distinction collapses trivially into categories the project already has

Why it is promising:

- it directly tests whether the philosophical vocabulary does new work on a modern phenomenon
- it keeps the deployment question bounded instead of leaping to “new symbolic form”

## Design Principle, Not Standalone Experiment

### Loop-structured experiments

This is not one experiment but a default pattern for higher-risk probes:

1. constituting pass
2. critique pass
3. source-language check
4. independent rerun

This pattern is already what made `03 -> 03a -> 03b -> 03c` trustworthy.

## Hold For Later

These are productive prompts, not yet experiment-ready.

### LLM as new symbolic form

Why held:

- would require direct encounter with the relevant `Philosophy of Symbolic Forms` material, not just `Erkenntnisproblem` and secondary exposition
- Hamburg and Festschrift encounters are moving this closer to readiness faster than expected
- revisit after the reification-detection test and at least one deployment candidate

### Formal perception

Why held:

- interesting hypothesis, but current repo methods do not really test it
- if the deployment candidates start producing discriminating results on modern questions, revisit

### Goethe / Leibniz reunification as dual operations

Why held:

- still too close to a large synthetic thesis rather than a bounded experiment
- should return only if repeated deployment results begin to demand it, not because a quota of successful small experiments has been reached

## Infrastructure Guardrail

Do not build new packet-construction infrastructure unless repeated hand-curated runs show a real bottleneck that the current checklist cannot resolve.

For now:

- packet design by hand is still adequate
- the control surface should be improved before the tooling surface is expanded

## Update Rule

When a new experiment idea appears:

- add it here first
- classify it as `near-term`, `design principle`, or `hold for later`
- give it a narrow question, likely materials, and success/failure conditions

If it cannot be stated that concretely, it is still a prompt, not yet an experiment.
