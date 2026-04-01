#!/usr/bin/env python3
"""Conservatively normalize extracted page text for working use.

This script is intentionally narrow:
- remove obvious page-number noise
- drop simple running headers when paired with a page number
- join wrapped lines within paragraphs
- preserve paragraph breaks
- keep page anchors when requested

It is not allowed to silently fix OCR misunderstandings in the underlying text.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
PROJECT_ROOT = REPO_ROOT / "texts" / "erkenntnisproblem-vol1"
PAGE_NUMBER_RE = re.compile(r"^(?:[IVXLCDM]+|\d+)$")


def resolve_path(raw_path: str) -> Path:
    path = Path(raw_path)
    return path if path.is_absolute() else PROJECT_ROOT / path


def looks_like_short_header(line: str) -> bool:
    stripped = line.strip()
    if not stripped or len(stripped) > 60:
        return False
    if stripped.endswith("."):
        return True
    return stripped.istitle() and len(stripped.split()) <= 6


def is_combined_header_line(line: str) -> bool:
    stripped = " ".join(line.strip().split())
    if not stripped:
        return False

    parts = stripped.split()
    if len(parts) < 2:
        return False

    if PAGE_NUMBER_RE.match(parts[0]) and looks_like_short_header(" ".join(parts[1:])):
        return True

    tail_number = parts[-1]
    head_text = " ".join(parts[:-1]).lstrip("-— ").strip()
    if PAGE_NUMBER_RE.match(tail_number) and looks_like_short_header(head_text):
        return True

    return False


def trim_edges(lines: list[str]) -> list[str]:
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    return lines


def strip_page_noise(lines: list[str]) -> list[str]:
    lines = trim_edges(lines)
    if len(lines) >= 2 and PAGE_NUMBER_RE.match(lines[0].strip()) and looks_like_short_header(lines[1]):
        lines = lines[2:]
    elif len(lines) >= 2 and looks_like_short_header(lines[0]) and PAGE_NUMBER_RE.match(lines[1].strip()):
        lines = lines[2:]
    elif lines and PAGE_NUMBER_RE.match(lines[0].strip()):
        lines = lines[1:]

    lines = trim_edges(lines)
    if lines and is_combined_header_line(lines[0]):
        lines = lines[1:]
    lines = trim_edges(lines)
    if lines and PAGE_NUMBER_RE.match(lines[-1].strip()):
        lines = lines[:-1]
    return trim_edges(lines)


def join_wrapped_lines(lines: list[str]) -> list[str]:
    paragraphs: list[str] = []
    current: list[str] = []

    def flush() -> None:
        if current:
            paragraphs.append(" ".join(current))
            current.clear()

    for raw_line in lines:
        line = " ".join(raw_line.split())
        if not line:
            flush()
            continue

        if not current:
            current.append(line)
            continue

        previous = current[-1]
        if previous.endswith("-") and len(previous) >= 2 and previous[-2].isalpha() and line[0].isalpha():
            current[-1] = previous[:-1] + line
        else:
            current.append(line)

    flush()
    return paragraphs


def normalize(text: str, start_page: int | None) -> str:
    raw_pages = text.split("\f")
    output: list[str] = []

    for index, raw_page in enumerate(raw_pages):
        lines = raw_page.splitlines()
        lines = strip_page_noise(lines)
        if not lines:
            continue

        if start_page is not None:
            output.append(f"[[pdf-page-{start_page + index}]]")

        output.extend(join_wrapped_lines(lines))
        output.append("")

    while output and not output[-1]:
        output.pop()
    return "\n".join(output) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="input text file")
    parser.add_argument("--output", required=True, help="output text file")
    parser.add_argument(
        "--start-page",
        type=int,
        help="first PDF page number; if set, page markers are emitted",
    )
    args = parser.parse_args()

    input_path = resolve_path(args.input)
    output_path = resolve_path(args.output)

    if not input_path.exists():
        raise SystemExit(f"missing input: {input_path}")

    text = input_path.read_text(encoding="utf-8")
    normalized = normalize(text, args.start_page)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(normalized, encoding="utf-8")

    try:
        label = output_path.relative_to(REPO_ROOT)
    except ValueError:
        label = output_path
    print(f"wrote normalized text to {label}")


if __name__ == "__main__":
    main()
