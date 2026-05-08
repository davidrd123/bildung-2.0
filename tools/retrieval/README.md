# Retrieval Prototype

This is a small derived retrieval setup for `bildung-2.0`. It exists to test
whether embeddings improve actual repo questions without collapsing authority
layers or smoothing difficult distinctions.

## Design

- Keep source text, journals, glossaries, and handles as the authority.
- Build local JSONL indexes from existing files.
- Search in authority-aware collections rather than one flattened corpus.
- Treat BM25 as the control before judging semantic retrieval.
- Keep generated corpora and embeddings under `var/retrieval/`, which is ignored.

## Seed Corpus

Build the initial corpus:

```bash
python3 tools/retrieval/build_corpus.py
```

The seed config is `tools/retrieval/config.seed.json`. It currently indexes:

- `patterns/*.md`
- `texts/zeitmauer` thread and journal surfaces
- `texts/zeitmauer/source/handles.yaml` as a separate derived-index collection
- Uexküll and Anders source-campaign notes
- selected living method notes, including the retrieval roadmap and bridge note

## Lexical Control

Run the Phase 1 eval seed against BM25:

```bash
python3 tools/retrieval/bm25_eval.py \
  --eval 00-Notes/DeepResearch/2026-04-06/retrieval-eval-seed.md \
  --output var/retrieval/seed-bm25-eval.md
```

Ad hoc lexical search:

```bash
python3 tools/retrieval/bm25_eval.py --query "translation resistance as evidence"
```

Restrict a search to source-campaign material:

```bash
python3 tools/retrieval/bm25_eval.py \
  --query "switch standpoints" \
  --authority-layer sources
```

## OpenAI Embeddings

Requires `OPENAI_API_KEY`.

Build local embeddings:

```bash
python3 tools/retrieval/openai_vector.py embed
```

Search:

```bash
python3 tools/retrieval/openai_vector.py search "world already structured before neutral description"
```

Source-layer-only search:

```bash
python3 tools/retrieval/openai_vector.py search \
  "where is empathy methodologically blocked?" \
  --authority-layer sources
```

Run the same eval seed:

```bash
python3 tools/retrieval/openai_vector.py eval \
  --output var/retrieval/seed-openai-eval.md
```

Default model: `text-embedding-3-small`. Use `--model text-embedding-3-large`
only when the small model has a documented failure worth testing.

## Hybrid Search

Use reciprocal-rank fusion when you want semantic recall without giving up the
lexical control. This is the normal practical interface. By default it searches
the `living` scope, excludes derived indexes such as `handles.yaml`, and uses a
lexical-biased weight of `bm25=2`, `vector=1`.

```bash
python3 tools/retrieval/hybrid_search.py \
  --query "switch standpoints"
```

Scope presets:

- `--scope canonical` searches canonical patterns, canonical text surfaces, and source campaigns.
- `--scope sources` searches source campaigns only.
- `--scope living` adds selected living method notes. This is the default.
- `--scope all` searches all non-derived layers in the seed corpus.
- `--include-derived` adds derived indexes to whichever scope is selected.

Evaluate the same seed:

```bash
python3 tools/retrieval/hybrid_search.py \
  --eval 00-Notes/DeepResearch/2026-04-06/retrieval-eval-seed.md \
  --output var/retrieval/seed-hybrid-eval.md
```

Include derived indexes when you explicitly want handle traces:

```bash
python3 tools/retrieval/hybrid_search.py \
  --eval 00-Notes/DeepResearch/2026-04-06/retrieval-eval-seed.md \
  --include-derived \
  --output var/retrieval/seed-hybrid-with-derived-eval.md
```

## Bridge Workflow

For bridge-style research questions, retrieve anchors before synthesis:

```bash
python3 tools/retrieval/hybrid_search.py \
  --query "what connects Uexküll and Anders to Jünger predecided world"
```

Use the returned paths and snippets as the citation surface for any later
interpretive answer. Dense-only results are useful diagnostics, but they should
not be treated as evidence unless the hit resolves back to a repo anchor.
