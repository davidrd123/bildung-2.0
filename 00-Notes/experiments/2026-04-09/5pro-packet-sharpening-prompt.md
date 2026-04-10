# 5 Pro Task: Sharpen Live Experiment Options into Runnable Packets

This prompt is addressed to **5 Pro after the coding-agent context pass**.
The intermediate coding agent's job is to assemble the right slices and then pass this task through; it should not answer the task itself unless explicitly asked to do so.

## Context

You have the project's experiment queue (`live-options.md`), the best completed experiments as models, and earned material from two completed translation volumes (Erkenntnisproblem Vol. I and Zeitmauer).

Important setup:

- a coding-agent prepass is managing the full input budget, up to `160k` tokens
- that prepass will not just attach files, but select the most relevant slices from those files
- your job is therefore **not** broad corpus exploration for its own sake
- your job is to take the curated context, judge whether it is sufficient, identify only the minimal missing additions if needed, and turn the candidate experiments into runnable packets

You may still have access to larger anchor files, but the selected slices should be treated as the primary work surface.

## What the experiments so far established

Three cross-project experiments (01-03) plus three verification runs (03a, 03b, 03c) tested whether Cassirer's completed Erkenntnisproblem and Jünger's completed Zeitmauer produce real structural contact at the passage level. They do. The core finding:

- Cassirer's limit is methodological and enabling — he shows where lawful cognition becomes possible by renouncing substance in favor of relation and law
- Jünger's limit is historical-threshold and standpoint-shifting — he shows where inherited order-regimes become provincial before a threshold they cannot contain
- These are not two instances of one structure; they are two boundary-markers facing different directions

The experiments also produced three informative negatives (different tempting bridges that fail), German-residue findings, and a method lesson: packet design matters as much as the result; same-packet convergence is evidence; diversified negatives are stronger evidence than elegant agreement.

## Your task

For each of the four near-term experiment candidates in `live-options.md`, do the following:

### 1. Assess and refine the selected passages

Do not stay at the category level ("Cassirer passages where reification happens"). Work from the selected slices first and decide whether they already give enough evidence to build a runnable packet.

For each experiment:

- name the actual part files
- name the actual line ranges or section markers
- name the actual German phrases that should be loaded
- say whether the current selected slices are already sufficient
- if not, name only the **minimal** extra passages that should be added by the coding-agent pass

### 2. Design the packet

For each experiment, produce a packet in the same format as `experiment-02-limit-of-orderable.md`:

- Cassirer side: specific units with source file paths, status notes (glossary entry vs. pressure candidate vs. passage)
- Jünger side: specific units with source file paths
- One narrow question
- Method constraints (scale matching, what to exclude, how many items)
- If the current selected context is too broad, say what should be removed
- If the current selected context is too thin, say what minimal additions are needed

### 3. Name the decoy or expected negative

For each experiment, identify one specific tempting bridge that should fail — a pairing that looks plausible but that the earned material suggests won't hold. This is as important as the positive packet. State why you expect it to fail.

### 4. Assess difficulty

For each experiment, say whether it's:

- **Ready to run now** — all materials on disk, packet is tight, question is clear
- **Needs one preparatory step** — materials exist but need extraction or narrowing first
- **Needs material the project doesn't yet have** — requires new encounter or translation

### 5. Improve or combine if warranted

If any of the four experiments can be improved or combined, say so. But don't combine just for elegance — only if the materials genuinely overlap enough that a combined run would be more honest than two separate ones.

## Constraints

- Stay inside the earned material. Do not introduce authors, frameworks, or concepts not already in these files.
- Do not design experiments that require encountering new sources first.
- The point is to make the existing speculative queue *runnable*, not to expand it.
- Assume the coding-agent pass is responsible for budget discipline. Help it by preferring precise slices over whole-file expansion.
- If the curated context already contains enough evidence, do **not** ask for more just because more context exists.
- If a proposed experiment turns out to be less promising once you look at the actual passages, say so honestly. Dropping one from the queue is a useful result.
- Prefer small, tight packets (3-5 units per side) over comprehensive inventories.
- Each packet should include the specific German phrases to attend to, following the format of `packet-03b-independent-german-threshold.md`.

## Source pool the coding-agent pass may draw from

In the actual run, you should expect a curated subset of these materials plus selected slices from them. Use the selected slices as primary evidence; treat the broader list below as the source pool for minimal additions or corrections.

### Experiment models and queue
- `00-Notes/experiments/live-options.md`
- `00-Notes/experiments/2026-04-09/experiment-02-limit-of-orderable.md`
- `00-Notes/experiments/2026-04-09/experiment-03-passage-threshold-test.md`
- `00-Notes/experiments/2026-04-09/experiment-03c-second-independent-subagent.md`

### Erkenntnisproblem earned surfaces / slice sources
- `texts/erkenntnisproblem-vol1/reading/2026-04-08-earned-distillation-from-volume-i.md`
- `texts/erkenntnisproblem-vol1/source/glossary.yaml`
- `texts/erkenntnisproblem-vol1/reading/close-reading-ledger.md`
- `texts/erkenntnisproblem-vol1/journal.md`
- `00-Notes/DeepResearch/2026-04-09/opus_task03.md` (glossary audit)

### Erkenntnisproblem parts — likely reification and method-pressure loci
- `texts/erkenntnisproblem-vol1/parts/76-bruno-minimum-measure-and-the-irrational.md`
- `texts/erkenntnisproblem-vol1/parts/77-bruno-minimum-synthesis-and-boundary.md`
- `texts/erkenntnisproblem-vol1/parts/78-bruno-interval-pure-quantity-and-leibniz.md`
- `texts/erkenntnisproblem-vol1/parts/79-bruno-method-limit-and-exact-science-opening.md`
- `texts/erkenntnisproblem-vol1/parts/101-galilei-from-substance-to-function-and-phenomenal-knowledge.md`
- `texts/erkenntnisproblem-vol1/parts/110-descartes-the-new-organon-and-the-problem-of-necessity.md`
- `texts/erkenntnisproblem-vol1/parts/111-descartes-method-metaphysics-and-the-universal-mathematics.md`
- `texts/erkenntnisproblem-vol1/parts/112-descartes-relational-logic-and-the-analytic-method.md`
- `texts/erkenntnisproblem-vol1/parts/113-descartes-analytic-geometry-and-extension-as-common-measure.md`
- `texts/erkenntnisproblem-vol1/parts/114-descartes-space-magnitude-and-the-foundation-of-physics.md`
- `texts/erkenntnisproblem-vol1/parts/115-descartes-extension-as-innate-idea-and-the-concept-of-substance.md`
- `texts/erkenntnisproblem-vol1/parts/138-burthogge-retrospective-and-malebranche-psychological-opening.md`
- `texts/erkenntnisproblem-vol1/parts/139-malebranche-self-knowledge-occasionalism-and-the-end-of-absolute-matter.md`
- `texts/erkenntnisproblem-vol1/parts/140-malebranche-force-relativism-and-the-concept-of-relation.md`
- `texts/erkenntnisproblem-vol1/parts/141-malebranche-relation-divine-law-and-psychological-idealism.md`
- `texts/erkenntnisproblem-vol1/parts/142-malebranche-critique-of-the-ontological-proof-and-idea-vs-perception.md`
- `texts/erkenntnisproblem-vol1/parts/143-malebranche-idea-infinity-and-intelligible-extension.md`
- `texts/erkenntnisproblem-vol1/parts/144-malebranche-eternal-truths-and-arnaulds-objection.md`
- `texts/erkenntnisproblem-vol1/parts/147-bayle-historical-critique-reason-and-revelation.md`
- `texts/erkenntnisproblem-vol1/parts/148-bayle-antinomies-of-the-infinite-and-the-fate-of-theoretical-reason.md`
- `texts/erkenntnisproblem-vol1/parts/149-bayle-ethical-reason-the-psychological-motive-of-skepsis-and-the-limits-of-critique.md`

### Zeitmauer earned surfaces / slice sources
- `texts/zeitmauer/source/glossary.yaml`
- `texts/zeitmauer/source-bound-high-level-integration.md`
- `texts/zeitmauer/threads/cassirer-pressure-on-zeitmauer.md`
- `texts/zeitmauer/threads/time-crisis.md`
- `texts/zeitmauer/threads/predecided-world.md`
- `texts/zeitmauer/journal.md`

### Zeitmauer parts — likely target loci
- `texts/zeitmauer/parts/16-humane-einteilungen.md`
- `texts/zeitmauer/parts/17-humane-einteilungen.md`
- `texts/zeitmauer/parts/37-siderische-einteilungen.md`
- `texts/zeitmauer/parts/38-siderische-einteilungen.md`
- `texts/zeitmauer/parts/49-siderische-einteilungen.md`
- `texts/zeitmauer/parts/50-siderische-einteilungen.md`
- `texts/zeitmauer/parts/51-siderische-einteilungen.md`
- `texts/zeitmauer/parts/56-urgrund-und-person.md`
- `texts/zeitmauer/parts/57-urgrund-und-person.md`
- `texts/zeitmauer/parts/58-urgrund-und-person.md`
- `texts/zeitmauer/parts/59-urgrund-und-person.md`

## Output format

For each experiment, return:

1. **Experiment name and question** (one sentence)
2. **Cassirer packet** (file paths, line ranges or section markers, German phrases to attend to, status of each unit, and whether the currently selected slices are sufficient)
3. **Jünger packet** (same format)
4. **Expected negative / decoy** (what bridge should fail and why)
5. **Method constraints** (scale matching, exclusions, number of items, and what to remove or minimally add if the current context is mis-sized)
6. **Difficulty assessment** (ready / needs prep / needs new material)
7. **Any improvements** to the original `live-options.md` description

Then at the end:

8. **Cross-experiment notes** — any overlaps, combinations, or sequencing recommendations across the four experiments
9. **Coding-agent guidance** — if you need any additional slices beyond the curated context, list them as a minimal addendum in priority order
