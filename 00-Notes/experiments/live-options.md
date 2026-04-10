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
- `experiment-04-reification-detection.md`
- `experiment-05-bruno-shaped-gap-completion.md`
- `experiment-06-translation-residue-clustering.md`

What that chain established:

- packet construction matters as much as the result
- same-packet convergence is useful evidence
- diversified negatives are stronger evidence than repeated elegant agreement
- German residue often shows where English creates false parallels
- a higher-resolution packet index has still **not** earned its entrance

## Near-Term Candidates

These are the next experiments most clearly indicated by the current work.
They remain the first-priority queue.

### 1. Inverse-Bayle / self-critique test

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

### 2. Chain-of-thought as discursive adequacy test

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

### 3. Constitutive vs. indicative in LLM outputs

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
- the reification-detection test is now complete; revisit after at least one deployment candidate

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
