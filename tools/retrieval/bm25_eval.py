#!/usr/bin/env python3
"""Run dependency-free BM25 search over a retrieval corpus."""

from __future__ import annotations

import argparse
import math
from collections import Counter
from pathlib import Path
from typing import Any

from retrieval_common import (
    compact_text,
    expected_anchor_hit,
    filter_rows,
    parse_eval_seed,
    read_jsonl,
    tokenize,
)


class BM25:
    def __init__(self, rows: list[dict[str, Any]], k1: float = 1.5, b: float = 0.75):
        self.rows = rows
        self.k1 = k1
        self.b = b
        self.doc_terms: list[Counter[str]] = []
        self.doc_lengths: list[int] = []
        self.df: Counter[str] = Counter()

        for row in rows:
            terms = Counter(tokenize(searchable_text(row)))
            self.doc_terms.append(terms)
            length = sum(terms.values())
            self.doc_lengths.append(length)
            self.df.update(terms.keys())

        self.avgdl = sum(self.doc_lengths) / len(self.doc_lengths) if rows else 0.0

    def search(self, query: str, top_k: int = 5) -> list[dict[str, Any]]:
        query_terms = tokenize(query)
        scores: list[tuple[float, int]] = []
        total_docs = len(self.rows)
        for index, terms in enumerate(self.doc_terms):
            score = 0.0
            doc_length = self.doc_lengths[index] or 1
            for term in query_terms:
                freq = terms.get(term, 0)
                if not freq:
                    continue
                idf = math.log(1 + (total_docs - self.df[term] + 0.5) / (self.df[term] + 0.5))
                denom = freq + self.k1 * (1 - self.b + self.b * doc_length / self.avgdl)
                score += idf * (freq * (self.k1 + 1)) / denom
            if score > 0:
                scores.append((score, index))

        hits: list[dict[str, Any]] = []
        for score, index in sorted(scores, reverse=True)[:top_k]:
            row = dict(self.rows[index])
            row["score"] = score
            hits.append(row)
        return hits


def searchable_text(row: dict[str, Any]) -> str:
    return "\n".join(
        [
            row.get("title", ""),
            row.get("heading", ""),
            row.get("path", ""),
            " ".join(row.get("handles", [])),
            row.get("text", ""),
        ]
    )


def render_hits(hits: list[dict[str, Any]]) -> str:
    lines: list[str] = []
    for rank, hit in enumerate(hits, start=1):
        lines.append(
            f"{rank}. `{hit['path']}#{hit['chunk_index']}` "
            f"({hit['collection']}, score={hit['score']:.3f})"
        )
        lines.append(f"   - {hit.get('heading', '')}")
        lines.append(f"   - {compact_text(hit.get('text', ''))}")
    return "\n".join(lines)


def run_eval(index: BM25, eval_path: Path, top_k: int) -> str:
    cases = parse_eval_seed(eval_path)
    lines = [
        "# BM25 Retrieval Baseline",
        "",
        f"Eval seed: `{eval_path.as_posix()}`",
        f"Top K: `{top_k}`",
        "",
    ]
    anchor_hits = 0
    for case in cases:
        hits = index.search(case["query"], top_k=top_k)
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
                f"- top{top_k}_anchor: `{'yes' if hit else 'no'}`",
                "",
                render_hits(hits) if hits else "_No hits._",
                "",
            ]
        )
    lines.insert(4, f"Anchor hits: `{anchor_hits}/{len(cases)}`")
    lines.insert(5, "")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus", default="var/retrieval/seed-corpus.jsonl")
    parser.add_argument("--query")
    parser.add_argument("--eval", dest="eval_path")
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--collection", action="append")
    parser.add_argument("--authority-layer", action="append")
    parser.add_argument("--output")
    args = parser.parse_args()

    rows = filter_rows(
        read_jsonl(Path(args.corpus)),
        collections=args.collection,
        authority_layers=args.authority_layer,
    )
    if not rows:
        raise SystemExit("no corpus rows after filtering")
    index = BM25(rows)

    if args.query:
        result = render_hits(index.search(args.query, top_k=args.top_k))
    elif args.eval_path:
        result = run_eval(index, Path(args.eval_path), args.top_k)
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
