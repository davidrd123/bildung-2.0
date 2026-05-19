#!/usr/bin/env python3

from __future__ import annotations

import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EPUB_PATH = ROOT / (
    "sources/modern/incoming/books/"
    "Cartesian Linguistics _ A Chapter in the History of -- "
    "Noam Chomsky & James McGilvray & Noam Chomsky -- 1966.epub"
)
SOURCE_DIR = ROOT / "sources/modern/chomsky-cartesian-linguistics/source"
FULL_PATH = SOURCE_DIR / "full/cartesian-linguistics.txt"
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
        "slug": "introduction-to-the-third-edition",
        "title": "Introduction to the third edition",
        "kind": "introduction",
        "printed_page_start": "1",
        "file": "raw/010-introduction-to-the-third-edition.txt",
        "marker": ("Introduction to the third edition", "James McGilvray"),
    },
    {
        "seq": 20,
        "slug": "cartesian-linguistics-title-acknowledgments",
        "title": "Cartesian Linguistics: title, acknowledgments, and epigraph",
        "kind": "front-matter",
        "printed_page_start": "53",
        "file": "raw/020-cartesian-linguistics-title-acknowledgments.txt",
        "marker": (
            "Cartesian Linguistics",
            "A Chapter in the History of Rationalist Thought",
            "Noam Chomsky",
        ),
    },
    {
        "seq": 21,
        "slug": "introduction",
        "title": "Introduction",
        "kind": "chapter",
        "printed_page_start": "57",
        "file": "raw/021-introduction.txt",
        "marker": ("Introduction", "Whitehead’s often quoted remark"),
        "prefix": True,
    },
    {
        "seq": 22,
        "slug": "creative-aspect-of-language-use",
        "title": "Creative aspect of language use",
        "kind": "chapter",
        "printed_page_start": "59",
        "file": "raw/022-creative-aspect-of-language-use.txt",
        "marker": ("Creative aspect of language use", "Although Descartes makes"),
        "prefix": True,
    },
    {
        "seq": 23,
        "slug": "deep-and-surface-structure",
        "title": "Deep and surface structure",
        "kind": "chapter",
        "printed_page_start": "78",
        "file": "raw/023-deep-and-surface-structure.txt",
        "marker": ("Deep and surface structure", "We have observed"),
        "prefix": True,
    },
    {
        "seq": 24,
        "slug": "description-and-explanation-in-linguistics",
        "title": "Description and explanation in linguistics",
        "kind": "chapter",
        "printed_page_start": "93",
        "file": "raw/024-description-and-explanation-in-linguistics.txt",
        "marker": ("Description and explanation in linguistics", "Within the framework"),
        "prefix": True,
    },
    {
        "seq": 25,
        "slug": "acquisition-and-use-of-language",
        "title": "Acquisition and use of language",
        "kind": "chapter",
        "printed_page_start": "98",
        "file": "raw/025-acquisition-and-use-of-language.txt",
        "marker": ("Acquisition and use of language", "We have so far"),
        "prefix": True,
    },
    {
        "seq": 26,
        "slug": "summary",
        "title": "Summary",
        "kind": "chapter",
        "printed_page_start": "108",
        "file": "raw/026-summary.txt",
        "marker": ("Summary", "Returning to the remark"),
        "prefix": True,
    },
    {
        "seq": 30,
        "slug": "notes",
        "title": "Notes",
        "kind": "back-matter",
        "printed_page_start": "109",
        "file": "raw/030-notes.txt",
        "marker": ("Notes", "INTRODUCTION TO THE THIRD EDITION"),
    },
    {
        "seq": 31,
        "slug": "bibliography",
        "title": "Bibliography",
        "kind": "back-matter",
        "printed_page_start": "147",
        "file": "raw/031-bibliography.txt",
        "marker": ("Bibliography", "Aarslef, H."),
        "prefix": True,
    },
    {
        "seq": 32,
        "slug": "index",
        "title": "Index",
        "kind": "back-matter",
        "printed_page_start": "154",
        "file": "raw/032-index.txt",
        "marker": ("Index", "accommodation of linguistics"),
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


def calibre_version() -> str:
    result = subprocess.run(
        ["ebook-convert", "--version"],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip().splitlines()[0]


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
            if found is None:
                matched = False
                break
            found_prefix = prefix and expected == marker[-1]
            if not line_matches(found[1], expected, found_prefix):
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


def write_sections_yaml(sections: list[dict[str, object]]) -> None:
    yaml_lines = [
        "book:",
        '  title: "Cartesian Linguistics: A Chapter in the History of Rationalist Thought"',
        '  author: "Noam Chomsky"',
        '  editor: "James McGilvray"',
        (
            '  source_epub: "sources/modern/incoming/books/Cartesian Linguistics _ '
            "A Chapter in the History of -- Noam Chomsky & James McGilvray & "
            'Noam Chomsky -- 1966.epub"'
        ),
        '  extracted_full_text: "source/full/cartesian-linguistics.txt"',
        f"  extraction_tool: {yaml_value(calibre_version())}",
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
