# Context Packages for `Erkenntnisproblem`

Purpose: define what to load at session start so a human or LLM begins from the right compression layer for the task at hand.

This file is not a replacement for direct reading of the parts. It is a session-start manifest.

## Core rules

### 1. Use `kernel + overlay`, not bulk preload

- load the same small kernel for any `Erkenntnisproblem` work
- then add a task-specific overlay
- do not load the whole translated run by default

### 2. Keep authority and retrieval distinct

Truth surfaces:

- `texts/erkenntnisproblem-vol1/parts/*.md`
- `texts/erkenntnisproblem-vol1/source/glossary.yaml`
- `texts/erkenntnisproblem-vol1/source/cusanus-generative-chain.yaml`
- `texts/erkenntnisproblem-vol1/source/bruno-generative-chain.yaml`
- `texts/erkenntnisproblem-vol1/journal.md`

Retrieval surfaces:

- `texts/erkenntnisproblem-vol1/reading/close-reading-ledger.md`
- dated notes in `texts/erkenntnisproblem-vol1/reading/`
- scratch notes in `texts/erkenntnisproblem-vol1/reading/`

Use retrieval surfaces to get oriented quickly; go back to truth surfaces whenever a claim or pressure needs verification.

### 3. Prefer slices over full files when context is tight

Priority order under pressure:

1. active parts
2. recent journal entries touching those parts
3. chapter-local ledger entries
4. active glossary slice
5. structured chain files
6. older dated notes

### 4. Write exclusion rules explicitly

Do not load by default:

- the entire `parts/` run
- the full journal unless the task is explicitly whole-run or apparatus-audit
- multiple large primary texts from different subprojects at once
- secondary sources before the primary pressure has been named

## Artifact roles

### Parts

The parts are the translation surface and the nearest local authority for what Cassirer is doing.

### Journal

The journal is the decision surface. It records what a tranche clarified and what the project chose not to do yet.

### Close-reading ledger

The ledger is the sentence-scale pressure surface. It catches gains that are too local for the journal and too important to lose.

### Chain files

The chain files preserve staged conceptual movement when a chapter becomes too dense to recover from prose notes alone.

### Scratch notes

Scratch notes are anti-compaction devices. Use them during whole-run or multi-part rereads whenever the rate of internal correction is high enough that memory will flatten it.

## Packages

### Package 1: Cold-start kernel

Use when:

- any session touches `texts/erkenntnisproblem-vol1/`

Load order:

1. `patterns/charter.md`
2. `CLAUDE.md`
3. `00-Notes/process.md`
4. `00-Notes/right-now.md`
5. recent `journal.md` tail relevant to the active chapter

Kernel add-on:

- add `patterns/handle-schema.md` whenever the session is touching handles, thread dossiers, or any structure that might widen ontology

Why:

- this gives purpose, guardrails, workflow, current state, and the current edge

Avoid:

- starting from the translated parts alone
- starting from a secondary source alone

### Package 2: Translation continuation

Use when:

- translating the next tranche in sequence

Load on top of Package 1:

1. `texts/erkenntnisproblem-vol1/source/glossary.yaml`
2. `texts/erkenntnisproblem-vol1/reading/close-reading-ledger.md`
3. last `3-5` journal entries touching the active stretch
4. previous `2-3` parts for continuity of register and argument
5. `texts/erkenntnisproblem-vol1/source/page-map.yaml`

Why:

- keeps term discipline stable
- carries over sentence-scale gains
- preserves the most recent `Decision for now`

Avoid:

- loading the whole chapter history unless a real continuity problem appears

### Package 3: Bounded reread / second pass

Use when:

- revisiting translated material to tighten English, test local argument-pressure, or check whether a conceptual movement still reads as staged

Load on top of Package 1:

1. target parts only
2. matching journal entries
3. matching ledger entries
4. active glossary slice
5. relevant chain file, if one exists
6. one secondary-source working note only if it bears directly on the same pressure

Glossary note:

- if the active glossary slice is thin or empty, treat that as a real state of the apparatus rather than a prompt to promote terms prematurely

Typical examples:

- late Cusanus reread: `Parts 12-15` + Cusanus chain
- late Bruno reread: `Parts 76-79` + Bruno chain

Why:

- second-pass work depends on earlier local decisions and sentence-scale findings
- the chain files stop the reread from degrading into isolated sentence cleanup

Avoid:

- full-book preload
- multiple secondary sources competing for authority

### Package 4: Whole-run probe

Use when:

- reading a long run to recover arc, pressure, and weak points

Load on top of Package 1:

1. `texts/erkenntnisproblem-vol1/reading/2026-04-08-whole-run-parts-journal-ledger-scratch-note.md`
2. `texts/erkenntnisproblem-vol1/reading/close-reading-ledger.md`
3. structural and recent journal entries
4. the parts themselves only as they are read in sequence

Process rule:

- externalize noticing as you go
- do not trust working memory to preserve the internal rate of correction across a long run

Why:

- whole-run reading loses resolution fastest in late Bruno and other high-correction stretches

Avoid:

- loading all parts at once
- producing a polished summary before writing a scratch note

### Package 5: Secondary-source encounter

Use when:

- reading Ferrari, Bast, Gonzalez Rios, or another companion source against live primary work

Load on top of Package 1:

1. the specific secondary source
2. the primary parts under pressure
3. matching journal entries
4. matching ledger entries if the issue is translation or local argument-motion
5. any existing working note on that source

Why:

- secondary work should sharpen, sort, or pressure-test what is already visible in the primary material

Avoid:

- reading the secondary source as transfer authority
- widening glossary or structure from secondary evidence alone

### Package 6: Cross-project question transfer

Use when:

- a live question from another subproject appears to bear on `Erkenntnisproblem`, or vice versa

Load:

1. `CLAUDE.md`
2. `00-Notes/cross-domain-synthesis-threads.md`
3. relevant journal entries from both projects
4. relevant ledger entries or chain nodes
5. active glossary slices only if the question is terminological

Why:

- cross-project contact should happen at the level of pressure and question, not concept-mapping

Avoid:

- loading large primary prose bodies from both projects together
- comparing by author-mapping before the local problem-structure is clear
- answering the cross-project question before both sides have earned it from direct reading

### Package 7: Volume I high-level integration

Use when:

- writing a high-level synthesis of completed Volume I
- preparing a bounded cross-volume handoff
- checking what is mature enough for controlled cross-project comparison

Load on top of Package 1:

1. `texts/erkenntnisproblem-vol1/reading/2026-04-08-volume-i-close-review.md`
2. `texts/erkenntnisproblem-vol1/reading/2026-04-08-earned-distillation-from-volume-i.md`
3. `texts/erkenntnisproblem-vol1/reading/2026-04-08-whole-run-parts-journal-ledger-scratch-note.md`
4. `texts/erkenntnisproblem-vol1/reading/2026-04-08-artifact-integrity-audit.md`
5. `texts/erkenntnisproblem-vol1/journal.md`

Optional bounded check:

- `texts/erkenntnisproblem-vol1/interpretive-notes.md` only after the source-bound synthesis is already written, and only to test whether a comparison remains at the level of problem-structure rather than author-mapping

Suggested output shape:

1. main intellectual arc
2. major internal transitions
3. strongest findings now earned
4. live unresolved pressures and debts
5. what is mature enough for cross-project comparison, and what should remain local

Why:

- these files are now the smallest trustworthy set for a source-bound whole-volume integration
- they preserve both argument arc and honesty about the late-run debt map

Avoid:

- starting from all `parts/*.md`
- using `interpretive-notes.md` as a primary authority surface
- exporting cross-project analogies before the local synthesis is stable

## Current use notes

- the Cusanus line already has a stable structured chain
- the Bruno line now has a first structured chain and should be used for late-Bruno rereads instead of reconstructing the sequence from journal prose each time
- the exact-science threshold after Bruno still needs a bounded reread note of its own once the `Leonardo -> Kepler` passage settles
