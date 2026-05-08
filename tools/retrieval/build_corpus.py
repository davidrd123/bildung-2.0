#!/usr/bin/env python3
"""Build a small authority-separated retrieval corpus JSONL."""

from __future__ import annotations

import argparse
import glob
import hashlib
import json
import re
from pathlib import Path
from typing import Any

from retrieval_common import HANDLE_RE, infer_project, markdown_title, write_jsonl


def split_markdown_sections(text: str, fallback_heading: str) -> list[tuple[str, str]]:
    sections: list[tuple[str, str]] = []
    heading = fallback_heading
    current: list[str] = []

    for line in text.replace("\r\n", "\n").splitlines():
        match = re.match(r"^(#{1,4})\s+(.+?)\s*$", line)
        if match:
            if "\n".join(current).strip():
                sections.append((heading, "\n".join(current).strip()))
            heading = match.group(2).strip()
            current = [line]
        else:
            current.append(line)

    if "\n".join(current).strip():
        sections.append((heading, "\n".join(current).strip()))
    return sections or [(fallback_heading, text.strip())]


def word_windows(text: str, target_words: int, overlap_words: int) -> list[str]:
    words = text.split()
    if len(words) <= target_words:
        return [" ".join(words)]

    windows: list[str] = []
    start = 0
    step = max(1, target_words - overlap_words)
    while start < len(words):
        end = min(len(words), start + target_words)
        windows.append(" ".join(words[start:end]))
        if end == len(words):
            break
        start += step
    return windows


def expand_files(root: Path, includes: list[str]) -> list[Path]:
    files: list[Path] = []
    seen: set[Path] = set()
    for pattern in includes:
        for match in sorted(glob.glob(str(root / pattern), recursive=True)):
            path = Path(match)
            if path.is_file() and path not in seen:
                files.append(path)
                seen.add(path)
    return files


def build_rows(root: Path, config: dict[str, Any]) -> list[dict[str, Any]]:
    chunking = config.get("chunking", {})
    target_words = int(chunking.get("target_words", 380))
    overlap_words = int(chunking.get("overlap_words", 60))
    min_words = int(chunking.get("min_words", 40))

    rows: list[dict[str, Any]] = []
    seen_paths: set[str] = set()

    for collection in config["collections"]:
        collection_name = collection["name"]
        authority_layer = collection["authority_layer"]
        for path in expand_files(root, collection.get("include", [])):
            rel_path = path.relative_to(root).as_posix()
            if rel_path in seen_paths:
                continue
            seen_paths.add(rel_path)

            text = path.read_text(encoding="utf-8", errors="replace")
            source_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()
            title = markdown_title(text, path.stem.replace("-", " "))
            file_rows: list[dict[str, Any]] = []

            for heading, section_text in split_markdown_sections(text, title):
                for window in word_windows(section_text, target_words, overlap_words):
                    word_count = len(window.split())
                    if word_count < min_words:
                        continue
                    chunk_hash = hashlib.sha256(
                        f"{rel_path}\n{heading}\n{window}".encode("utf-8")
                    ).hexdigest()
                    file_rows.append(
                        {
                            "path": rel_path,
                            "collection": collection_name,
                            "authority_layer": authority_layer,
                            "project": infer_project(rel_path),
                            "title": title,
                            "heading": heading,
                            "source_hash": source_hash,
                            "chunk_hash": chunk_hash,
                            "word_count": word_count,
                            "char_count": len(window),
                            "handles": sorted(set(HANDLE_RE.findall(window))),
                            "text": window,
                        }
                    )

            for index, row in enumerate(file_rows):
                row["chunk_index"] = index
                row["chunk_count"] = len(file_rows)
                row["chunk_id"] = f"{rel_path}#c{index:03d}"
                rows.append(row)

    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", default="tools/retrieval/config.seed.json")
    parser.add_argument("--output", default="var/retrieval/seed-corpus.jsonl")
    args = parser.parse_args()

    root = Path.cwd()
    config = json.loads((root / args.config).read_text(encoding="utf-8"))
    rows = build_rows(root, config)
    write_jsonl(root / args.output, rows)

    collections: dict[str, int] = {}
    for row in rows:
        collections[row["collection"]] = collections.get(row["collection"], 0) + 1

    print(f"wrote {len(rows)} chunks to {args.output}")
    for name, count in sorted(collections.items()):
        print(f"{name}: {count}")


if __name__ == "__main__":
    main()
