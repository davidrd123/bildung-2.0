# Embedding Prototype for the Bridge Note

**Status**: living-layer method note  
**Date**: 2026-05-08  
**Purpose**: record the first local retrieval setup and the initial result against the April retrieval eval seed

## Setup

The prototype is intentionally a derived tool layer, not a new authority layer.
It lives under `tools/retrieval/` and writes generated local artifacts under
`var/retrieval/`, which is ignored by git.

Repository pieces:

- `tools/retrieval/config.seed.json` — small authority-separated seed corpus
- `tools/retrieval/build_corpus.py` — builds JSONL chunks from existing files
- `tools/retrieval/bm25_eval.py` — dependency-free BM25 control
- `tools/retrieval/openai_vector.py` — OpenAI embedding build/search/eval
- `tools/retrieval/hybrid_search.py` — reciprocal-rank fusion over BM25 + embeddings

Generated local pieces:

- `var/retrieval/seed-corpus.jsonl`
- `var/retrieval/seed-openai-embeddings.jsonl`
- `var/retrieval/*-eval.md`

## Seed Corpus

The first corpus is deliberately small and pressure-led:

| Collection | Authority layer | Chunks |
| --- | --- | ---: |
| `canonical-patterns` | `canonical-patterns` | 23 |
| `zeitmauer-dossiers` | `canonical-texts` | 166 |
| `zeitmauer-handles` | `derived-indexes` | 52 |
| `uexkuell-source-campaign` | `sources` | 94 |
| `anders-source-campaign` | `sources` | 84 |
| `living-method-notes` | `living-notes` | 104 |

Total: 523 chunks after expanding the eval seed.

## Initial Eval

Eval set: `00-Notes/DeepResearch/2026-04-06/retrieval-eval-seed.md`

| Retriever | Scope | Top-5 anchor hits |
| --- | --- | ---: |
| BM25 | all seed layers | 14 / 15 |
| OpenAI `text-embedding-3-small` | all seed layers | 10 / 15 |
| Hybrid BM25 + OpenAI | all seed layers | 14 / 15 |
| BM25 | excluding `derived-indexes` | 15 / 15 |
| OpenAI `text-embedding-3-small` | excluding `derived-indexes` | 10 / 15 |
| Hybrid BM25 + OpenAI | excluding `derived-indexes` | 15 / 15 |

## What This Shows

The first result confirms the retrieval roadmap rather than replacing it.

- BM25 remains the control surface. It is strong on repo-native terms and exact
  source-close phrases.
- Dense OpenAI embeddings are useful, but not as a flat default. They miss some
  short distinction-heavy queries, including `switch standpoints`, and can let
  broad method notes outrank the source-facing anchor.
- Hybrid search is the practical default for now: lexical control plus semantic
  recall, with authority filters available.
- `texts/zeitmauer/source/handles.yaml` is valuable, but should stay a separate
  `derived-indexes` collection. When included flatly, it can dominate dossier
  retrieval for handle-heavy queries such as `time-crisis`.

## Current Judgment

The right next retrieval interface is not dense-only search. It is:

1. BM25 first, as the auditable baseline.
2. OpenAI embeddings as a sidecar for semantic recall.
3. Hybrid rank fusion when the user wants a practical search result.
4. Explicit authority-layer widening rather than one flattened corpus.

This keeps retrieval answerable to the texts and preserves the project rule that
derived structure must resolve back to canonical files.

## Expanded Eval Pass

After the practical-path decision, `retrieval-eval-seed.md` was expanded from
15 to 53 queries. The table now classifies each query by `Query class`,
`Test focus`, expected anchors, and likely failure labels. The query set covers:

- exact terms
- source-close phrases
- cross-language retrieval
- thread retrieval
- synthesis questions
- false-friend pressure

Full top-5 outputs are generated locally under `var/retrieval/`:

- `expanded-bm25-living-eval.md`
- `expanded-openai-living-eval.md`
- `expanded-hybrid-living-eval.md`
- `expanded-hybrid-with-derived-eval.md`

Results:

| Retriever | Scope | Top-5 anchor hits |
| --- | --- | ---: |
| BM25 | `living`, excluding `derived-indexes` | 51 / 53 |
| OpenAI `text-embedding-3-small` | `living`, excluding `derived-indexes` | 48 / 53 |
| Hybrid BM25 + OpenAI | `living`, excluding `derived-indexes` | 53 / 53 |
| Hybrid BM25 + OpenAI | `living`, including `derived-indexes` | 51 / 53 |

Actual misses:

| Retriever | Miss | Failure labels |
| --- | --- | --- |
| BM25 | `prometheisches Gefälle` | `translation-bottleneck`, `chunking` |
| BM25 | `what connects Uexküll and Anders to Jünger predecided world` | `query-too-abstract`, `omnibus-note-dominance` |
| OpenAI dense | `switch standpoints` | `model-smoothing`, `query-too-short` |
| OpenAI dense | `world already structured before neutral description` | `query-too-abstract`, `model-smoothing` |
| OpenAI dense | `where is empathy methodologically blocked?` | `model-smoothing`, `query-too-abstract` |
| OpenAI dense | `Vorentscheidung` | `cross-language-miss`, `missing-glossary-cue` |
| OpenAI dense | `what says the world is cut in advance by plan and naming?` | `query-too-abstract`, `missing-dossier` |
| Hybrid with derived indexes | `time-crisis` | `corpus-shape`, `derived-index-dominance` |
| Hybrid with derived indexes | `Siderische Einteilungen` | `missing-unit`, `derived-index-dominance` |

The important result is not that hybrid "wins" abstractly. The result is that
the hybrid path works only when authority layers stay explicit. Including
`derived-indexes` by default makes handle traces compete with dossiers and
source anchors. Therefore `hybrid_search.py` now defaults to `--scope living`
with derived indexes excluded, and exposes `--include-derived` only for queries
where handle traces are explicitly desired.
