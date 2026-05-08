#!/usr/bin/env python3
"""Hybrid retrieval with BM25 plus OpenAI vector reciprocal-rank fusion."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

from bm25_eval import BM25
from openai_vector import query_embedding, search_vectors
from retrieval_common import (
    DEFAULT_SCOPE,
    compact_text,
    expected_anchor_hit,
    filter_rows,
    parse_eval_seed,
    read_jsonl,
    scope_authority_layers,
)


def fuse(
    bm25_hits: list[dict[str, Any]],
    vector_hits: list[dict[str, Any]],
    rrf_k: int,
    bm25_weight: float,
    vector_weight: float,
) -> list[dict[str, Any]]:
    fused: dict[str, dict[str, Any]] = {}

    for rank, hit in enumerate(bm25_hits, start=1):
        chunk_id = hit["chunk_id"]
        row = fused.setdefault(chunk_id, dict(hit))
        if "fused_initialized" not in row:
            row["score"] = 0.0
            row["fused_initialized"] = True
        row["bm25_rank"] = rank
        row["bm25_score"] = hit["score"]
        row["vector_rank"] = None
        row["vector_score"] = None
        row["score"] = row.get("score", 0.0) + bm25_weight / (rrf_k + rank)

    for rank, hit in enumerate(vector_hits, start=1):
        chunk_id = hit["chunk_id"]
        row = fused.setdefault(chunk_id, dict(hit))
        if "fused_initialized" not in row:
            row["score"] = 0.0
            row["fused_initialized"] = True
        row["vector_rank"] = rank
        row["vector_score"] = hit["score"]
        row.setdefault("bm25_rank", None)
        row.setdefault("bm25_score", None)
        row["score"] = row.get("score", 0.0) + vector_weight / (rrf_k + rank)

    return sorted(fused.values(), key=lambda row: row["score"], reverse=True)


def hybrid_search(args: argparse.Namespace, query: str) -> list[dict[str, Any]]:
    authority_layers = resolve_authority_layers(args)
    corpus_rows = filter_rows(
        read_jsonl(Path(args.corpus)),
        collections=args.collection,
        authority_layers=authority_layers,
    )
    vector_rows = filter_rows(
        read_jsonl(Path(args.index)),
        collections=args.collection,
        authority_layers=authority_layers,
    )
    if not corpus_rows or not vector_rows:
        raise SystemExit("no rows after filtering")

    bm25 = BM25(corpus_rows)
    bm25_hits = bm25.search(query, top_k=args.candidate_k)
    vector = query_embedding(query, args.model, args.dimensions)
    vector_hits = search_vectors(vector_rows, vector, args.candidate_k)
    return fuse(
        bm25_hits,
        vector_hits,
        rrf_k=args.rrf_k,
        bm25_weight=args.bm25_weight,
        vector_weight=args.vector_weight,
    )[: args.top_k]


def resolve_authority_layers(args: argparse.Namespace) -> list[str] | None:
    if args.authority_layer:
        return args.authority_layer
    return scope_authority_layers(args.scope, include_derived=args.include_derived)


def render_hits(hits: list[dict[str, Any]]) -> str:
    lines: list[str] = []
    for rank, hit in enumerate(hits, start=1):
        vector_score = hit.get("vector_score")
        vector_text = "none" if vector_score is None else f"{vector_score:.4f}"
        bm25_score = hit.get("bm25_score")
        bm25_text = "none" if bm25_score is None else f"{bm25_score:.3f}"
        lines.append(
            f"{rank}. `{hit['path']}#{hit['chunk_index']}` ({hit['collection']}, "
            f"rrf={hit['score']:.5f}, bm25_rank={hit.get('bm25_rank')}, "
            f"bm25={bm25_text}, vector_rank={hit.get('vector_rank')}, vector={vector_text})"
        )
        lines.append(f"   - {hit.get('heading', '')}")
        lines.append(f"   - {compact_text(hit.get('text', ''))}")
    return "\n".join(lines)


def run_eval(args: argparse.Namespace) -> str:
    cases = parse_eval_seed(Path(args.eval_path))
    authority_layers = resolve_authority_layers(args)
    lines = [
        "# Hybrid Retrieval Eval",
        "",
        f"Corpus: `{args.corpus}`",
        f"Index: `{args.index}`",
        f"Model: `{args.model}`",
        f"Top K: `{args.top_k}`",
        f"Candidate K: `{args.candidate_k}`",
        f"RRF K: `{args.rrf_k}`",
        f"Weights: `bm25={args.bm25_weight}`, `vector={args.vector_weight}`",
        f"Scope: `{args.scope}`",
        f"Include derived: `{'yes' if args.include_derived else 'no'}`",
        f"Collections: `{', '.join(args.collection or ['all'])}`",
        f"Authority layers: `{', '.join(authority_layers or ['all'])}`",
        "",
    ]
    anchor_hits = 0
    for case in cases:
        hits = hybrid_search(args, case["query"])
        hit = expected_anchor_hit(hits, case["expected_anchors"])
        anchor_hits += int(hit)
        lines.extend(
            [
                f"## `{case['query']}`",
                "",
                f"- class: `{case['query_class']}`",
                f"- test_focus: `{case.get('test_focus', '')}`",
                f"- expected: {', '.join(f'`{anchor}`' for anchor in case['expected_anchors'])}",
                f"- failure_labels: {', '.join(f'`{label}`' for label in case.get('failure_labels', [])) or '`none`'}",
                f"- top{args.top_k}_anchor: `{'yes' if hit else 'no'}`",
                "",
                render_hits(hits) if hits else "_No hits._",
                "",
            ]
        )
    lines.insert(11, f"Anchor hits: `{anchor_hits}/{len(cases)}`")
    lines.insert(12, "")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus", default="var/retrieval/seed-corpus.jsonl")
    parser.add_argument("--index", default="var/retrieval/seed-openai-embeddings.jsonl")
    parser.add_argument("--model", default="text-embedding-3-small")
    parser.add_argument("--dimensions", type=int)
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--candidate-k", type=int, default=50)
    parser.add_argument("--rrf-k", type=int, default=60)
    parser.add_argument("--bm25-weight", type=float, default=2.0)
    parser.add_argument("--vector-weight", type=float, default=1.0)
    parser.add_argument(
        "--scope",
        choices=["canonical", "sources", "living", "all"],
        default=DEFAULT_SCOPE,
        help="authority-layer preset; default excludes derived indexes",
    )
    parser.add_argument(
        "--include-derived",
        action="store_true",
        help="include derived-indexes such as handles.yaml in the selected scope",
    )
    parser.add_argument("--collection", action="append")
    parser.add_argument("--authority-layer", action="append")
    parser.add_argument("--query")
    parser.add_argument("--eval", dest="eval_path")
    parser.add_argument("--output")
    args = parser.parse_args()

    if args.query:
        result = render_hits(hybrid_search(args, args.query))
    elif args.eval_path:
        result = run_eval(args)
    else:
        raise SystemExit("provide --query or --eval")

    if args.output:
        output = Path(args.output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(result + "\n", encoding="utf-8")
        print(f"wrote {args.output}")
    else:
        print(result)


if __name__ == "__main__":
    main()
