#!/usr/bin/env python3
"""Build and query a local OpenAI embedding JSONL index.

Requires OPENAI_API_KEY. Generated embeddings are local derived artifacts and
should stay out of git.
"""

from __future__ import annotations

import argparse
import json
import os
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

from retrieval_common import (
    compact_text,
    cosine,
    expected_anchor_hit,
    filter_rows,
    parse_eval_seed,
    read_jsonl,
    write_jsonl,
)


EMBEDDINGS_URL = "https://api.openai.com/v1/embeddings"


def request_embeddings(
    inputs: list[str],
    model: str,
    dimensions: int | None,
    api_key: str,
    retries: int = 4,
) -> list[list[float]]:
    payload: dict[str, Any] = {
        "model": model,
        "input": inputs,
        "encoding_format": "float",
    }
    if dimensions:
        payload["dimensions"] = dimensions

    body = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        EMBEDDINGS_URL,
        data=body,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    for attempt in range(retries):
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                data = json.loads(response.read().decode("utf-8"))
            return [item["embedding"] for item in sorted(data["data"], key=lambda row: row["index"])]
        except urllib.error.HTTPError as error:
            message = error.read().decode("utf-8", errors="replace")
            if error.code not in {429, 500, 502, 503, 504} or attempt == retries - 1:
                raise RuntimeError(f"OpenAI embeddings request failed: {error.code} {message}") from error
        except urllib.error.URLError as error:
            if attempt == retries - 1:
                raise RuntimeError(f"OpenAI embeddings request failed: {error}") from error
        time.sleep(2**attempt)

    raise RuntimeError("OpenAI embeddings request failed")


def embedding_input(row: dict[str, Any]) -> str:
    return "\n".join(
        [
            f"Title: {row.get('title', '')}",
            f"Path: {row.get('path', '')}",
            f"Collection: {row.get('collection', '')}",
            f"Authority layer: {row.get('authority_layer', '')}",
            f"Heading: {row.get('heading', '')}",
            "",
            row.get("text", ""),
        ]
    )


def load_existing(path: Path, model: str, dimensions: int | None) -> dict[str, dict[str, Any]]:
    if not path.exists():
        return {}
    rows = read_jsonl(path)
    existing: dict[str, dict[str, Any]] = {}
    for row in rows:
        if row.get("model") == model and row.get("dimensions") == dimensions:
            existing[row["chunk_id"]] = row
    return existing


def embed_corpus(args: argparse.Namespace) -> None:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise SystemExit("OPENAI_API_KEY is not set")

    corpus_path = Path(args.corpus)
    output_path = Path(args.output)
    corpus = read_jsonl(corpus_path)
    existing = load_existing(output_path, args.model, args.dimensions)
    embedded: dict[str, dict[str, Any]] = {}
    for row in corpus:
        old = existing.get(row["chunk_id"])
        if (
            not old
            or old.get("chunk_hash") != row.get("chunk_hash")
            or old.get("source_hash") != row.get("source_hash")
        ):
            continue
        refreshed = {
            key: row[key]
            for key in [
                "chunk_id",
                "path",
                "collection",
                "authority_layer",
                "project",
                "title",
                "heading",
                "chunk_index",
                "chunk_hash",
                "source_hash",
                "word_count",
                "handles",
                "text",
            ]
            if key in row
        }
        refreshed["model"] = args.model
        refreshed["dimensions"] = args.dimensions
        refreshed["embedding"] = old["embedding"]
        embedded[row["chunk_id"]] = refreshed

    pending = [row for row in corpus if row["chunk_id"] not in embedded]
    for start in range(0, len(pending), args.batch_size):
        batch = pending[start : start + args.batch_size]
        vectors = request_embeddings(
            [embedding_input(row) for row in batch],
            model=args.model,
            dimensions=args.dimensions,
            api_key=api_key,
        )
        for row, vector in zip(batch, vectors):
            record = {
                key: row[key]
                for key in [
                    "chunk_id",
                    "path",
                    "collection",
                    "authority_layer",
                    "project",
                    "title",
                    "heading",
                    "chunk_index",
                    "chunk_hash",
                    "source_hash",
                    "word_count",
                    "handles",
                    "text",
                ]
                if key in row
            }
            record["model"] = args.model
            record["dimensions"] = args.dimensions
            record["embedding"] = vector
            embedded[row["chunk_id"]] = record
        print(f"embedded {min(start + len(batch), len(pending))}/{len(pending)} pending chunks")

    ordered = [embedded[row["chunk_id"]] for row in corpus if row["chunk_id"] in embedded]
    write_jsonl(output_path, ordered)
    print(f"wrote {len(ordered)} embeddings to {output_path.as_posix()}")


def search_vectors(rows: list[dict[str, Any]], query_vector: list[float], top_k: int) -> list[dict[str, Any]]:
    scored: list[dict[str, Any]] = []
    for row in rows:
        hit = dict(row)
        hit["score"] = cosine(query_vector, row["embedding"])
        scored.append(hit)
    return sorted(scored, key=lambda row: row["score"], reverse=True)[:top_k]


def render_hits(hits: list[dict[str, Any]]) -> str:
    lines: list[str] = []
    for rank, hit in enumerate(hits, start=1):
        lines.append(
            f"{rank}. `{hit['path']}#{hit['chunk_index']}` "
            f"({hit['collection']}, cosine={hit['score']:.4f})"
        )
        lines.append(f"   - {hit.get('heading', '')}")
        lines.append(f"   - {compact_text(hit.get('text', ''))}")
    return "\n".join(lines)


def query_embedding(query: str, model: str, dimensions: int | None) -> list[float]:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise SystemExit("OPENAI_API_KEY is not set")
    return request_embeddings([query], model=model, dimensions=dimensions, api_key=api_key)[0]


def search_index(args: argparse.Namespace) -> str:
    rows = filter_rows(
        read_jsonl(Path(args.index)),
        collections=args.collection,
        authority_layers=args.authority_layer,
    )
    if not rows:
        raise SystemExit("no index rows after filtering")
    query_vector = query_embedding(args.query, args.model, args.dimensions)
    return render_hits(search_vectors(rows, query_vector, args.top_k))


def eval_index(args: argparse.Namespace) -> str:
    rows = filter_rows(
        read_jsonl(Path(args.index)),
        collections=args.collection,
        authority_layers=args.authority_layer,
    )
    if not rows:
        raise SystemExit("no index rows after filtering")
    cases = parse_eval_seed(Path(args.eval_path))
    lines = [
        "# OpenAI Embedding Retrieval Eval",
        "",
        f"Index: `{args.index}`",
        f"Model: `{args.model}`",
        f"Dimensions: `{args.dimensions or 'default'}`",
        f"Top K: `{args.top_k}`",
        f"Collections: `{', '.join(args.collection or ['all'])}`",
        f"Authority layers: `{', '.join(args.authority_layer or ['all'])}`",
        "",
    ]
    anchor_hits = 0
    for case in cases:
        vector = query_embedding(case["query"], args.model, args.dimensions)
        hits = search_vectors(rows, vector, args.top_k)
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
    lines.insert(6, f"Anchor hits: `{anchor_hits}/{len(cases)}`")
    lines.insert(7, "")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", default="text-embedding-3-small")
    parser.add_argument("--dimensions", type=int)
    subparsers = parser.add_subparsers(dest="command", required=True)

    embed_parser = subparsers.add_parser("embed", help="embed corpus chunks")
    embed_parser.add_argument("--corpus", default="var/retrieval/seed-corpus.jsonl")
    embed_parser.add_argument("--output", default="var/retrieval/seed-openai-embeddings.jsonl")
    embed_parser.add_argument("--batch-size", type=int, default=64)

    search_parser = subparsers.add_parser("search", help="search an embedding index")
    search_parser.add_argument("query")
    search_parser.add_argument("--index", default="var/retrieval/seed-openai-embeddings.jsonl")
    search_parser.add_argument("--top-k", type=int, default=5)
    search_parser.add_argument("--collection", action="append")
    search_parser.add_argument("--authority-layer", action="append")

    eval_parser = subparsers.add_parser("eval", help="run the eval seed against an embedding index")
    eval_parser.add_argument("--index", default="var/retrieval/seed-openai-embeddings.jsonl")
    eval_parser.add_argument("--eval", dest="eval_path", default="00-Notes/DeepResearch/2026-04-06/retrieval-eval-seed.md")
    eval_parser.add_argument("--top-k", type=int, default=5)
    eval_parser.add_argument("--collection", action="append")
    eval_parser.add_argument("--authority-layer", action="append")
    eval_parser.add_argument("--output")

    args = parser.parse_args()
    if args.command == "embed":
        embed_corpus(args)
    elif args.command == "search":
        print(search_index(args))
    elif args.command == "eval":
        result = eval_index(args)
        if args.output:
            output = Path(args.output)
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_text(result + "\n", encoding="utf-8")
            print(f"wrote {args.output}")
        else:
            print(result)


if __name__ == "__main__":
    main()
