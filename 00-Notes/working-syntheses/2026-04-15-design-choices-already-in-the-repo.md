# 2026-04-15 — Design choices already in the repo

**Status:** Working synthesis, not an earned distillation. This note does not add new architecture. Its job is only to name design choices that are already embodied in the repo but are still mostly visible as practice, scattered rules, or local file conventions.

**Purpose:** give the project one place to point when it needs to say "these were not accidents; they were choices," without importing the larger conversation-only vocabulary around field/temperature, biosemiotics, or genre claims.

**Inputs:**

- `patterns/handle-schema.md`
- `00-Notes/process.md`
- `texts/zeitmauer/source/glossary.yaml`
- `texts/zeitmauer/source/handles.yaml`
- `texts/erkenntnisproblem-vol1/reading/close-reading-ledger.md`
- `00-Notes/experiments/2026-04-09/packet-04-reification-detection.md`
- `00-Notes/experiments/2026-04-09/experiment-04-reification-detection.md`
- `00-Notes/experiments/2026-04-13/packet-01-umwelt-planfulness-outside-the-body.md`
- `00-Notes/experiments/2026-04-13/experiment-01-umwelt-planfulness-outside-the-body.md`

## Core claim

The repo already contains a set of design choices that matter structurally.

Most of them are not hidden, exactly. They are written down somewhere. But they usually appear as:

- one sentence in `handle-schema.md`
- a local convention inside a glossary
- a recurring format inside experiments
- a habit in one subproject rather than a named cross-repo choice

This note just gathers them.

## 1. Text authority over graph authority

This is the clearest architectural choice the repo has made:

> "text files remain the authority; handles are derived structure that makes the authority navigable"  
> [patterns/handle-schema.md](/Users/daviddickinson/Projects/Lora/bildung-2.0/patterns/handle-schema.md:3)

This is not a storage detail. It determines the whole shape of the repo:

- canonical meaning lives in source-bound text files
- handles, YAML, and derived indexes exist to point back into those files
- structure is downstream of the encounter, not upstream of it

This choice is also visible locally in the `Zeitmauer` handle pilot:

> "Canonical authority remains: `sections.yaml`, `glossary.yaml`, `parts/`, `threads/`, and `journal.md`."  
> [texts/zeitmauer/source/handles.yaml](/Users/daviddickinson/Projects/Lora/bildung-2.0/texts/zeitmauer/source/handles.yaml:2)

## 2. Open terms are positive data, not incomplete cleanup

This choice appears in two linked places.

At the lifecycle level:

> "`open` is not a lesser status than `stable`."  
> [patterns/handle-schema.md](/Users/daviddickinson/Projects/Lora/bildung-2.0/patterns/handle-schema.md:160)

At the glossary level:

- `preferred: null`
- explicit alternatives preserved
- `status: open`

The Uexküll glossary is the clearest surface:

- `Umwelt` — [sources/german/uexkuell-theoretische-biologie/glossary.yaml](/Users/daviddickinson/Projects/Lora/bildung-2.0/sources/german/uexkuell-theoretische-biologie/glossary.yaml:5)
- `Merkwelt` — [sources/german/uexkuell-theoretische-biologie/glossary.yaml](/Users/daviddickinson/Projects/Lora/bildung-2.0/sources/german/uexkuell-theoretische-biologie/glossary.yaml:37)
- `Wirkwelt` — [sources/german/uexkuell-theoretische-biologie/glossary.yaml](/Users/daviddickinson/Projects/Lora/bildung-2.0/sources/german/uexkuell-theoretische-biologie/glossary.yaml:49)

The same move is also live in `Zeitmauer`:

- `an der Zeitmauer` — [texts/zeitmauer/source/glossary.yaml](/Users/daviddickinson/Projects/Lora/bildung-2.0/texts/zeitmauer/source/glossary.yaml:5)
- `Bruchstelle` — [texts/zeitmauer/source/glossary.yaml](/Users/daviddickinson/Projects/Lora/bildung-2.0/texts/zeitmauer/source/glossary.yaml:172)

The choice is:

- unresolvedness can be a better state than false resolution
- failed English candidates are part of the record
- a term can stay live for a long time without being treated as backlog

## 3. Promotion follows evidence density and reuse, not rhetorical fluency

This is explicit in the handle schema:

- promotion gates are given per object type
- agents have no direct path to `stable` by prose force alone  
  [patterns/handle-schema.md](/Users/daviddickinson/Projects/Lora/bildung-2.0/patterns/handle-schema.md:166), [patterns/handle-schema.md](/Users/daviddickinson/Projects/Lora/bildung-2.0/patterns/handle-schema.md:203)

This matters because it turns maturity into a design choice rather than a social impression.

The repo does not ask:

- does this sound right?
- has this been reused enough that it feels settled?

It asks:

- did the evidence chain thicken?
- did later use survive without re-deriving the claim?
- is there still an equally live rival?

## 4. Relations are a repertoire of moves, not an ontology that must be complete

The handle schema names eleven relation types, including one explicitly reserved-but-unused slot:

- `echoes`
- `extends`
- `translates`
- `retranslates`
- `detranslates`
- `residue-of`
- `crystallizes`
- `pressures`
- `parallels`
- `challenges`
- `grounds`  
  [patterns/handle-schema.md](/Users/daviddickinson/Projects/Lora/bildung-2.0/patterns/handle-schema.md:135)

Two choices are embedded here:

1. the relation set is intentionally compact and ergonomic
2. the grammar is allowed to reserve a move before it is frequently used

`detranslates` is the cleanest example:

- present in the schema
- not yet exercised  
  [patterns/handle-schema.md](/Users/daviddickinson/Projects/Lora/bildung-2.0/patterns/handle-schema.md:140)

The choice is not "represent everything."

The choice is:

- keep a small repertoire
- only add or stabilize moves that materially improve reading and replay

## 5. Evidence is tracked as a chain, not just cited as background

The evidence-handle format makes term pressure reconstructable:

- `evidence:term:schicksalszeit:zm:4`
- `evidence:term:hinzutretende:zm:6`  
  [patterns/handle-schema.md](/Users/daviddickinson/Projects/Lora/bildung-2.0/patterns/handle-schema.md:86)

In practice, this means glossary pressure is not just explained in prose. It is serialized into handles and chains:

- `Schicksalszeit` evidence list — [texts/zeitmauer/source/glossary.yaml](/Users/daviddickinson/Projects/Lora/bildung-2.0/texts/zeitmauer/source/glossary.yaml:76)
- `Weltplan` evidence list — [texts/zeitmauer/source/glossary.yaml](/Users/daviddickinson/Projects/Lora/bildung-2.0/texts/zeitmauer/source/glossary.yaml:153)

The choice is:

- pressure should be replayable from explicit loci
- later decisions should be able to point back into the term's testing history

## 6. Forward provenance is treated as real trace, not as a side effect

The `Erkenntnisproblem` close-reading ledger tracks:

- passage base
- finding
- current downstream use  
  [texts/erkenntnisproblem-vol1/reading/close-reading-ledger.md](/Users/daviddickinson/Projects/Lora/bildung-2.0/texts/erkenntnisproblem-vol1/reading/close-reading-ledger.md:23)

That last field is the distinctive move.

The ledger does not only ask:

- where did this finding come from?

It also asks:

- where has it since gone?

This is already a real trace discipline on disk, even though it has not yet been written up as a repo-level design choice.

## 7. Different texts are allowed different secondary-trace media

The repo has already chosen not to force one trace format across all subprojects.

`process.md` says this explicitly in the secondary-trace diagnostic:

- `Erkenntnisproblem` is currently the richest prose-trace environment
- `Zeitmauer` is currently the richest relational-trace environment
- the right standard is discoverability, not uniformity  
  [00-Notes/process.md](/Users/daviddickinson/Projects/Lora/bildung-2.0/00-Notes/process.md:170)

So the choice is:

- textual grain determines trace medium
- prose and relational surfaces are both legitimate
- forcing symmetry across projects would lose local fit

This is one reason the repo currently has both:

- a handle-first proving ground
- a journal/ledger-first proving ground

without treating that difference as drift.

## 8. The experiment layer is a bounded method, not just miscellaneous notes

The experiment folder already contains a real discipline:

- packet separate from result
- explicit baseline to beat
- clear output contract
- non-goals
- rerunnable structure

Examples:

- packet/result pair for `Umwelt` replay  
  [packet-01-umwelt-planfulness-outside-the-body.md](/Users/daviddickinson/Projects/Lora/bildung-2.0/00-Notes/experiments/2026-04-13/packet-01-umwelt-planfulness-outside-the-body.md:1), [experiment-01-umwelt-planfulness-outside-the-body.md](/Users/daviddickinson/Projects/Lora/bildung-2.0/00-Notes/experiments/2026-04-13/experiment-01-umwelt-planfulness-outside-the-body.md:1)
- packet/result pair for reification detection  
  [packet-04-reification-detection.md](/Users/daviddickinson/Projects/Lora/bildung-2.0/00-Notes/experiments/2026-04-09/packet-04-reification-detection.md:1), [experiment-04-reification-detection.md](/Users/daviddickinson/Projects/Lora/bildung-2.0/00-Notes/experiments/2026-04-09/experiment-04-reification-detection.md:1)

The choice is:

- experiments are bounded
- success/failure conditions are declared in advance
- results do not silently rewrite the packet that generated them

That is already a methodology, even if it has not yet been collected as one.

## 9. Interoperability is loose coupling, not ontology merger

The handle schema already says:

- `vault:` and `b2:` namespace prefixes are enough
- neither system needs to import the other's ontology
- they only need stable identifiers that can point across systems  
  [patterns/handle-schema.md](/Users/daviddickinson/Projects/Lora/bildung-2.0/patterns/handle-schema.md:209)

That is a real design philosophy, not just a naming trick.

It means:

- interoperability happens through reference
- the systems stay sovereign
- shared work does not require conceptual unification

## 10. The repo now has more than two note states

The repo began with a broad living/crystallized split:

- `00-Notes/`
- `patterns/`  
  [00-Notes/process.md](/Users/daviddickinson/Projects/Lora/bildung-2.0/00-Notes/process.md:9)

It has since effectively grown a more articulated filtration chain:

- chat exports
- extractions
- experiments
- working syntheses
- distillations
- patterns

That split is visible in the directory structure and recent cleanup, even if `process.md` still states the simpler two-layer model.

The choice already being made in practice is:

- not all living notes do the same job
- some living notes are for recovery
- some are for testing
- some are for explicit non-authoritative synthesis

That probably should remain practice for now, but it is still a real choice.

## What this note is not doing

It is **not** trying to promote the conversation-only layer into repo design.

Still outside this note:

- translation as reasoning engine
- field / pressure / temperature as settled repo vocabulary
- overflow vs pitch
- biosemiotics / Schelling framing
- "genre without a name"
- "continuing interrupted trajectories"

Those may matter later. But they are not needed to explain the choices the repo has already made.

## Working judgment

The repo already has a more explicit design philosophy than its top-level prose currently admits.

The missing piece is not more architecture.

The missing piece is one level of explanation:

- why these choices were made
- what alternative they quietly reject
- what kind of work each choice protects

This note is only a first gather. It is not yet the final rationale.

## Use rule

Use this note when the repo starts sounding as if its current structure "just grew" or when conversation starts adding fresh architecture before the existing design choices have even been named.

Do not use it as authority for new vocabulary, new object types, or a stronger pattern layer. Its job is only to make already-embodied choices visible as choices.
