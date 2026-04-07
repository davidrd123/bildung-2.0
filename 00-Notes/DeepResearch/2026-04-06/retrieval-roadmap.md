# Retrieval Roadmap

**Status**: living-layer method note
**Date**: 2026-04-06
**Purpose**: turn the qmd experiment into a concrete retrieval plan for `bildung-2.0`

## Core question

The retrieval question is not only "which model is best?" but "where are we willing to collapse structure?"

In this repo, collapse happens at least at four levels:

- the index unit
- the collection boundary
- the retrieval model
- the promotion boundary

That means retrieval design is primarily an editorial problem and only secondarily a model problem.

## Baseline from the qmd experiment

What already helped:

- authority-separated collections
- narrowing `canonical-texts` to authority-bearing files
- splitting `living-notes` from `chats`
- treating BM25 as the first-pass retriever rather than defaulting to dense search

What the experiment showed:

- repo-native queries already retrieve well with lexical search
- source-close English queries can retrieve source-facing material
- abstracted synthesis questions degrade much faster
- chat isolation materially improves signal
- query expansion alone does not solve the abstraction gap
- partial semantic retrieval is promising but not yet decisive
- embedding should be treated as offline maintenance, not background work during live querying

## Current retrieval surface

The current local qmd setup should remain a derived layer, not a repo layer.

Working collection shape:

- `canonical-patterns`
- `canonical-texts`
- `sources`
- `living-notes`
- `chats`
- `sessions`

The important practical rule is:

- search `canonical-patterns` + `canonical-texts` + `sources` first
- widen to `living-notes` second
- widen to `chats` only when needed

## Phase 1: Lexical Baseline + Evaluation Set

### Goal

Establish what the existing corpus can already retrieve before changing models.

### Deliverables

- stable local retrieval config
- a small evaluation set of real repo questions
- a record of expected anchors for each query
- a note on which failures come from query wording versus corpus shape

### Query classes

The evaluation set should include both query modes the repo actually uses.

1. Repo-native queries

- `predecided world`
- `Planmäßigkeit as Naturkraft`
- `time-crisis`
- `Goethe/Leibniz split`

2. Source-close English queries

- `planfulness outside the body`
- `leading and accompanying properties`
- `switch standpoints`
- `animal's soul`

3. Natural-language synthesis questions

- `what treats translation resistance as evidence rather than error?`
- `what in the repo says the world is already structured before neutral description?`
- `where is empathy methodologically blocked?`
- `what says adaptation is not the right frame for fit?`

4. Cross-language pressure queries

- English query with German target
- German term with English anchor
- paraphrase that should reach an existing term or thread without exact lexical overlap

### Success criteria

Measure each query by:

- whether at least one expected anchor appears in the top 5
- whether the highest-ranked relevant result is in the right authority layer
- whether widening to `living-notes` adds signal or only noise
- whether widening to `chats` is actually necessary
- whether the query only works when phrased in repo-native language

### What counts as a Phase 1 failure

- a query only works after hand-rephrasing into exact repo wording
- a giant omnibus note dominates the hits and obscures the real anchor
- the relevant material exists but only in `chats`
- the relevant material exists but is not yet unitized in a retrievable form

## Phase 2: Hybrid Multilingual Benchmark

### Goal

Test whether a hybrid multilingual model improves recall on the Phase 1 failures without flooding the top hits with smoothed analogies.

### Candidate

- `BGE-M3` or equivalent hybrid multilingual family

Reason:

- dense + sparse + multi-vector behavior in one family
- easier benchmark path than jumping straight to a heavier late-interaction stack

### Evaluation rule

Run the exact same evaluation set from Phase 1.

Do not judge the model by generic benchmark claims.
Judge it by whether it improves the actual Phase 1 misses:

- English query to German anchor
- abstract synthesis prompt to source-facing anchor
- cross-project echo where exact phrasing differs

### Success criteria

- improved recall on known misses
- no collapse of crucial distinctions into generic semantic neighbors
- no strong increase in chat-heavy or theory-heavy noise

### Failure condition

If hybrid retrieval mostly returns nearby-sounding but weakly grounded notes, the model is widening recall by over-smoothing.

## Phase 3: Late Interaction / Reranker

### Goal

Handle the failures that remain specifically phrase-sensitive, distinction-sensitive, or term-family-sensitive after Phase 2.

### Candidate uses

- second-stage reranking over the top 50-100 candidates
- precision retrieval for difficult conceptual probes

### Why this phase is conditional

Late interaction is architecturally closer to the repo's needs than single-vector dense retrieval, but it is not the first question.

It is only justified if Phase 2 still misses:

- term-family pressure
- local distinctions where one phrase matters
- English queries that should reach German anchors but still do not

### Success criteria

- better ranking of source-facing anchors for distinction-heavy queries
- improved phrase sensitivity without a large noise penalty
- enough gain to justify the extra infrastructure

## Corpus-shape work that matters regardless of model

These are improvements to the corpus itself, not retrieval tricks.

1. Thread dossiers

This remains the highest-value improvement.

The repo has more named threads than standalone dossiers. Files like `cross-domain-synthesis-threads.md` are carrying too much retrieval load.

Priority:

- promote the top few repeatedly used threads into their own dossiers
- keep them small and anchor-heavy

2. Unit shape from existing structure

Do not create a giant hand-authored retrieval layer.

Prefer existing units:

- part files
- encounter files
- glossary entries
- thread dossiers
- evidence handles
- journal entries

Only generate finer slices if evaluation shows a specific retrieval failure that existing units cannot solve.

3. Keep authority explicit

Any retrieval system should preserve the widening order:

- canonical
- source campaigns
- living notes
- chats

## Practical next step

The cheapest next move is not a model install.

It is to build the Phase 1 evaluation set:

- `10-20` real queries
- expected anchors
- top-5 lexical results
- notes on why each miss failed

Only after that should the repo benchmark a hybrid multilingual model.

## Working thesis

For `bildung-2.0`, retrieval should be built in this order:

1. corpus shape
2. collection shape
3. evaluation discipline
4. lexical baseline
5. hybrid multilingual benchmark
6. late interaction or reranking if the benchmark proves it is needed

That order keeps retrieval answerable to the texts rather than turning retrieval itself into a new authoring project.
