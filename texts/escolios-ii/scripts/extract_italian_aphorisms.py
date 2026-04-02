#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import re
import textwrap


BOOK_REL = "books/Escolios a un texto implicito II - Nicolas Gomez Davila.txt"
OUTPUT_REL = "texts/escolios-ii/source/aphorisms.it.yaml"
BODY_START_LINE = 392
BODY_END_LINE = 14325
TRUNCATED_OPENING_RE = re.compile(r"^[a-zà-öø-ÿ]")


def repo_root() -> Path:
    return Path(__file__).resolve().parents[3]


def wrap_block(text: str, width: int = 76) -> list[str]:
    return textwrap.wrap(
        text,
        width=width,
        break_long_words=False,
        break_on_hyphens=False,
    )


def extract_blocks(lines: list[str]) -> list[dict[str, object]]:
    blocks: list[dict[str, object]] = []
    current: list[str] = []
    current_start: int | None = None

    for lineno, raw in enumerate(lines, start=BODY_START_LINE):
        stripped = raw.strip()
        if stripped:
            if not current:
                current_start = lineno
            current.append(stripped)
            continue

        if current:
            text = " ".join(current)
            entry: dict[str, object] = {
                "id": len(blocks) + 1,
                "line_start": current_start,
                "it": text,
            }
            if TRUNCATED_OPENING_RE.match(text):
                entry["issues"] = ["truncated-opening"]
            blocks.append(entry)
            current = []
            current_start = None

    if current:
        text = " ".join(current)
        entry = {
            "id": len(blocks) + 1,
            "line_start": current_start,
            "it": text,
        }
        if TRUNCATED_OPENING_RE.match(text):
            entry["issues"] = ["truncated-opening"]
        blocks.append(entry)

    return blocks


def write_yaml(entries: list[dict[str, object]], out_path: Path) -> None:
    header = [
        "# Escolios a un texto implicito II — Italian witness extraction",
        "# Extracted from the corrected volume II text export.",
        f"# Main aphorism body: lines {BODY_START_LINE}-{BODY_END_LINE}.",
        "# Endnotes begin at line 14326; postface begins at line 14442.",
        "# `it` preserves the available Italian witness, including inline note markers.",
        "",
    ]
    chunks = ["\n".join(header)]

    for entry in entries:
        chunks.append(f"- id: {entry['id']}\n")
        chunks.append(f"  line_start: {entry['line_start']}\n")
        if "issues" in entry:
            issues = ", ".join(entry["issues"])  # type: ignore[arg-type]
            chunks.append(f"  issues: [{issues}]\n")
        chunks.append("  it: >\n")
        for line in wrap_block(str(entry["it"]).strip()):
            chunks.append(f"    {line}\n")
        chunks.append("\n")

    out_path.write_text("".join(chunks))


def main() -> None:
    root = repo_root()
    book_path = root / BOOK_REL
    out_path = root / OUTPUT_REL
    lines = book_path.read_text().splitlines()
    body = lines[BODY_START_LINE - 1 : BODY_END_LINE]
    entries = extract_blocks(body)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    write_yaml(entries, out_path)
    flagged = sum(1 for entry in entries if "issues" in entry)
    print(
        f"Wrote {len(entries)} aphorisms to {out_path.relative_to(root)} "
        f"({flagged} flagged with truncated openings)."
    )


if __name__ == "__main__":
    main()
