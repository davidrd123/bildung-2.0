#!/usr/bin/env python3

from __future__ import annotations

import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EPUB_PATH = ROOT / (
    "sources/modern/incoming/books/"
    "The Origins of Knowledge and Imagination -- Jacob Bronowski.epub"
)
SOURCE_DIR = ROOT / "sources/modern/bronowski-origins-knowledge-imagination/source"
FULL_PATH = SOURCE_DIR / "full/origins-of-knowledge-and-imagination.txt"
RAW_DIR = SOURCE_DIR / "raw"
SECTIONS_PATH = SOURCE_DIR / "sections.yaml"


SECTIONS = [
    {
        "seq": 0,
        "slug": "front-matter-and-contents",
        "title": "Front matter and contents",
        "kind": "front-matter",
        "printed_page_start": None,
        "file": "raw/000-front-matter-and-contents.txt",
        "marker": None,
    },
    {
        "seq": 10,
        "slug": "foreword",
        "title": "Foreword, by S. E. Luria",
        "kind": "foreword",
        "printed_page_start": "ix",
        "file": "raw/010-foreword.txt",
        "marker": ("FOREWORD",),
    },
    {
        "seq": 11,
        "slug": "the-mind-as-an-instrument-for-understanding",
        "title": "1. The Mind as an Instrument for Understanding",
        "kind": "chapter",
        "printed_page_start": "1",
        "file": "raw/011-the-mind-as-an-instrument-for-understanding.txt",
        "marker": ("1", "The Mind as an Instrument for Understanding"),
    },
    {
        "seq": 12,
        "slug": "the-evolution-and-power-of-symbolic-language",
        "title": "2. The Evolution and Power of Symbolic Language",
        "kind": "chapter",
        "printed_page_start": "20",
        "file": "raw/012-the-evolution-and-power-of-symbolic-language.txt",
        "marker": ("2", "The Evolution and Power of Symbolic Language"),
    },
    {
        "seq": 13,
        "slug": "knowledge-as-algorithm-and-as-metaphor",
        "title": "3. Knowledge as Algorithm and as Metaphor",
        "kind": "chapter",
        "printed_page_start": "41",
        "file": "raw/013-knowledge-as-algorithm-and-as-metaphor.txt",
        "marker": ("3", "Knowledge as Algorithm and as Metaphor"),
    },
    {
        "seq": 14,
        "slug": "the-laws-of-nature-and-the-nature-of-laws",
        "title": "4. The Laws of Nature and the Nature of Laws",
        "kind": "chapter",
        "printed_page_start": "67",
        "file": "raw/014-the-laws-of-nature-and-the-nature-of-laws.txt",
        "marker": ("4", "The Laws of Nature and the Nature of Laws"),
    },
    {
        "seq": 15,
        "slug": "error-progress-and-the-concept-of-time",
        "title": "5. Error, Progress, and the Concept of Time",
        "kind": "chapter",
        "printed_page_start": "86",
        "file": "raw/015-error-progress-and-the-concept-of-time.txt",
        "marker": ("5", "Error, Progress, and the Concept of Time"),
    },
    {
        "seq": 16,
        "slug": "law-and-individual-responsibility",
        "title": "6. Law and Individual Responsibility",
        "kind": "chapter",
        "printed_page_start": "108",
        "file": "raw/016-law-and-individual-responsibility.txt",
        "marker": ("6", "Law and Individual Responsibility"),
    },
    {
        "seq": 30,
        "slug": "index",
        "title": "Index",
        "kind": "back-matter",
        "printed_page_start": None,
        "file": "raw/030-index.txt",
        "marker": ("INDEX",),
    },
    {
        "seq": 40,
        "slug": "footnotes",
        "title": "Footnotes",
        "kind": "back-matter",
        "printed_page_start": None,
        "file": "raw/040-footnotes.txt",
        "marker": ("1. See F. S. C. Northrop",),
        "prefix": True,
    },
]


def yaml_value(value: object) -> str:
    if value is None:
        return "null"
    return json.dumps(value, ensure_ascii=False)


def normalize_full_text() -> None:
    text = (
        FULL_PATH.read_text(encoding="utf-8")
        .replace("\r\n", "\n")
        .replace("\r", "\n")
        .replace("\x08", "")
        .replace("\xad", "")
    )
    FULL_PATH.write_text(text, encoding="utf-8")


def run_calibre() -> None:
    FULL_PATH.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [
            "ebook-convert",
            str(EPUB_PATH),
            str(FULL_PATH),
            "--txt-output-formatting",
            "plain",
        ],
        check=True,
    )
    normalize_full_text()


def line_matches(line: str, marker: str, prefix: bool) -> bool:
    stripped = line.strip()
    return stripped.startswith(marker) if prefix else stripped == marker


def next_nonblank(lines: list[str], start: int) -> tuple[int, str] | None:
    for idx in range(start, len(lines)):
        text = lines[idx].strip()
        if text:
            return idx, text
    return None


def find_marker(lines: list[str], marker: tuple[str, ...], prefix: bool = False) -> int:
    for idx, line in enumerate(lines):
        if not line_matches(line, marker[0], prefix):
            continue
        cursor = idx + 1
        matched = True
        for expected in marker[1:]:
            found = next_nonblank(lines, cursor)
            if found is None or found[1] != expected:
                matched = False
                break
            cursor = found[0] + 1
        if matched:
            return idx + 1
    raise ValueError(f"Could not find section marker: {marker!r}")


def resolve_sections(lines: list[str]) -> list[dict[str, object]]:
    resolved = []
    for section in SECTIONS:
        marker = section["marker"]
        if marker is None:
            start_line = 1
        else:
            start_line = find_marker(
                lines,
                marker,
                bool(section.get("prefix", False)),
            )
        cleaned = {key: value for key, value in section.items() if key not in {"marker", "prefix"}}
        cleaned["start_line"] = start_line
        resolved.append(cleaned)

    for idx, section in enumerate(resolved):
        next_start = (
            resolved[idx + 1]["start_line"]
            if idx + 1 < len(resolved)
            else len(lines) + 1
        )
        section["end_line"] = int(next_start) - 1
        section["line_count"] = int(section["end_line"]) - int(section["start_line"]) + 1
    return resolved


def split_sections(sections: list[dict[str, object]], lines: list[str]) -> None:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    for section in sections:
        start = int(section["start_line"])
        end = int(section["end_line"])
        body = "\n".join(lines[start - 1 : end]).rstrip() + "\n"
        (SOURCE_DIR / str(section["file"])).write_text(body, encoding="utf-8")


def calibre_version() -> str:
    result = subprocess.run(
        ["ebook-convert", "--version"],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip().splitlines()[0]


def write_sections_yaml(sections: list[dict[str, object]]) -> None:
    tool = calibre_version()
    yaml_lines = [
        "book:",
        '  title: "The Origins of Knowledge and Imagination"',
        '  author: "Jacob Bronowski"',
        '  source_epub: "sources/modern/incoming/books/The Origins of Knowledge and Imagination -- Jacob Bronowski.epub"',
        '  extracted_full_text: "source/full/origins-of-knowledge-and-imagination.txt"',
        f"  extraction_tool: {yaml_value(tool)}",
        "sections:",
    ]

    for section in sections:
        yaml_lines.extend(
            [
                f'  - seq: {section["seq"]}',
                f'    slug: {yaml_value(section["slug"])}',
                f'    title: {yaml_value(section["title"])}',
                f'    kind: {yaml_value(section["kind"])}',
                f'    file: {yaml_value(section["file"])}',
                f'    start_line: {section["start_line"]}',
                f'    end_line: {section["end_line"]}',
                f'    line_count: {section["line_count"]}',
                f'    printed_page_start: {yaml_value(section["printed_page_start"])}',
            ]
        )

    SECTIONS_PATH.write_text("\n".join(yaml_lines) + "\n", encoding="utf-8")


def main() -> None:
    if not EPUB_PATH.exists():
        raise FileNotFoundError(EPUB_PATH)
    run_calibre()
    lines = FULL_PATH.read_text(encoding="utf-8").splitlines()
    sections = resolve_sections(lines)
    split_sections(sections, lines)
    write_sections_yaml(sections)


if __name__ == "__main__":
    main()
