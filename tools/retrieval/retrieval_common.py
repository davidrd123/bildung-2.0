#!/usr/bin/env python3
"""Shared helpers for the lightweight retrieval prototype.

The scripts in this directory are intentionally dependency-free. They produce
derived local artifacts from repo text files; they do not define canonical
objects for the project.
"""

from __future__ import annotations

import json
import math
import re
from pathlib import Path
from typing import Any, Iterable


TOKEN_RE = re.compile(r"[\w]+", re.UNICODE)
HANDLE_RE = re.compile(
    r"\b(?:zm|esc|exg|src|term|thread|note|evidence|frame):[A-Za-z0-9_.:-]+"
)


def tokenize(text: str) -> list[str]:
    return [token.lower() for token in TOKEN_RE.findall(text)]


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def filter_rows(
    rows: list[dict[str, Any]],
    collections: list[str] | None = None,
    authority_layers: list[str] | None = None,
) -> list[dict[str, Any]]:
    collection_set = set(collections or [])
    layer_set = set(authority_layers or [])
    return [
        row
        for row in rows
        if (not collection_set or row.get("collection") in collection_set)
        and (not layer_set or row.get("authority_layer") in layer_set)
    ]


def write_jsonl(path: Path, rows: Iterable[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True))
            handle.write("\n")


def infer_project(path: str) -> str:
    parts = Path(path).parts
    if len(parts) >= 2 and parts[0] == "patterns":
        return "patterns"
    if len(parts) >= 2 and parts[0] == "00-Notes":
        return "00-Notes"
    if len(parts) >= 2 and parts[0] == "texts":
        return parts[1]
    if len(parts) >= 3 and parts[0] == "sources":
        return parts[2]
    return parts[0] if parts else "unknown"


def markdown_title(text: str, fallback: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip() or fallback
    return fallback


def markdown_table_cells(line: str) -> list[str]:
    stripped = line.strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        return []
    return [cell.strip() for cell in stripped[1:-1].split("|")]


DEFAULT_SCOPE = "living"

SCOPE_LAYERS: dict[str, list[str]] = {
    "canonical": ["canonical-patterns", "canonical-texts", "sources"],
    "sources": ["sources"],
    "living": ["canonical-patterns", "canonical-texts", "sources", "living-notes"],
    "all": ["canonical-patterns", "canonical-texts", "sources", "living-notes"],
}

DERIVED_LAYERS = ["derived-indexes"]


def scope_authority_layers(scope: str, include_derived: bool = False) -> list[str]:
    if scope not in SCOPE_LAYERS:
        known = ", ".join(sorted(SCOPE_LAYERS))
        raise ValueError(f"unknown scope {scope!r}; expected one of: {known}")
    layers = list(SCOPE_LAYERS[scope])
    if include_derived:
        layers.extend(layer for layer in DERIVED_LAYERS if layer not in layers)
    return layers


def parse_eval_seed(path: Path) -> list[dict[str, Any]]:
    """Parse the retrieval-eval-seed markdown table into query cases.

    Supports the original four-column table and the richer six-column table
    used by the expanded benchmark.
    """
    cases: list[dict[str, Any]] = []
    in_table = False
    headers: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        cells = markdown_table_cells(line)
        if not cells:
            if in_table:
                break
            continue
        if "Query" in cells and "Expected anchor(s)" in cells:
            in_table = True
            headers = cells
            continue
        if not in_table or set(cells[0]) <= {"-"}:
            continue

        row = {
            header: cells[index] if index < len(cells) else ""
            for index, header in enumerate(headers)
        }
        query_match = re.search(r"`([^`]+)`", row.get("Query", ""))
        if not query_match:
            continue
        expected = re.findall(r"`([^`]+)`", row.get("Expected anchor(s)", ""))
        failure_labels = re.findall(r"`([^`]+)`", row.get("Failure labels", ""))
        cases.append(
            {
                "query": query_match.group(1),
                "query_class": row.get("Query class", ""),
                "test_focus": row.get("Test focus", row.get("Query class", "")),
                "expected_anchors": expected,
                "failure_labels": failure_labels,
                "notes": row.get("Notes", ""),
            }
        )
    return cases


def hit_matches_anchor(hit: dict[str, Any], anchor: str) -> bool:
    path = hit.get("path", "")
    text = hit.get("text", "")
    heading = hit.get("heading", "")
    title = hit.get("title", "")
    return (
        anchor == path
        or anchor in path
        or anchor in heading
        or anchor in title
        or anchor in text
    )


def expected_anchor_hit(hits: list[dict[str, Any]], anchors: list[str]) -> bool:
    return any(hit_matches_anchor(hit, anchor) for hit in hits for anchor in anchors)


def cosine(left: list[float], right: list[float]) -> float:
    dot = 0.0
    left_norm = 0.0
    right_norm = 0.0
    for a, b in zip(left, right):
        dot += a * b
        left_norm += a * a
        right_norm += b * b
    if not left_norm or not right_norm:
        return 0.0
    return dot / (math.sqrt(left_norm) * math.sqrt(right_norm))


def compact_text(text: str, limit: int = 180) -> str:
    compacted = re.sub(r"\s+", " ", text).strip()
    if len(compacted) <= limit:
        return compacted
    return compacted[: limit - 3].rstrip() + "..."
