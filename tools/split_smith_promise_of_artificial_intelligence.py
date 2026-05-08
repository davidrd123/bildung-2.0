#!/usr/bin/env python3

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TXT_WITNESS = ROOT / (
    "sources/modern/incoming/books/The Promise of Artificial Intel - Brian Cantwell Smith.txt"
)
SOURCE_DIR = ROOT / "sources/modern/smith-promise-of-artificial-intelligence/source"
FULL_PATH = SOURCE_DIR / "full/promise-of-artificial-intelligence.txt"
RAW_DIR = SOURCE_DIR / "raw"
SECTIONS_PATH = SOURCE_DIR / "sections.yaml"


SECTIONS = [
    {
        "seq": 0,
        "slug": "title-pages-and-contents",
        "title": "Title pages and contents",
        "kind": "front-matter",
        "printed_page_start": None,
        "start_line": 1,
        "file": "raw/000-title-pages-and-contents.txt",
    },
    {
        "seq": 1,
        "slug": "preface",
        "title": "Preface",
        "kind": "front-matter",
        "printed_page_start": None,
        "start_line": 111,
        "file": "raw/001-preface.txt",
    },
    {
        "seq": 2,
        "slug": "introduction",
        "title": "Introduction",
        "kind": "front-matter",
        "printed_page_start": None,
        "start_line": 140,
        "file": "raw/002-introduction.txt",
    },
    {
        "seq": 10,
        "slug": "background",
        "title": "1. Background",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 201,
        "file": "raw/010-background.txt",
    },
    {
        "seq": 11,
        "slug": "history",
        "title": "2. History",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 238,
        "file": "raw/011-history.txt",
    },
    {
        "seq": 12,
        "slug": "failure",
        "title": "3. Failure",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 381,
        "file": "raw/012-failure.txt",
    },
    {
        "seq": 13,
        "slug": "transition",
        "title": "4. Transition",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 578,
        "file": "raw/013-transition.txt",
    },
    {
        "seq": 14,
        "slug": "machine-learning",
        "title": "5. Machine Learning",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 604,
        "file": "raw/014-machine-learning.txt",
    },
    {
        "seq": 15,
        "slug": "assessment",
        "title": "6. Assessment",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 719,
        "file": "raw/015-assessment.txt",
    },
    {
        "seq": 16,
        "slug": "epistemological-challenges",
        "title": "7. Epistemological Challenges",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 844,
        "file": "raw/016-epistemological-challenges.txt",
    },
    {
        "seq": 17,
        "slug": "objects",
        "title": "8. Objects",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 939,
        "file": "raw/017-objects.txt",
    },
    {
        "seq": 18,
        "slug": "world",
        "title": "9. World",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 1074,
        "file": "raw/018-world.txt",
    },
    {
        "seq": 19,
        "slug": "reckoning-and-judgment",
        "title": "10. Reckoning and Judgment",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 1141,
        "file": "raw/019-reckoning-and-judgment.txt",
    },
    {
        "seq": 20,
        "slug": "discussion",
        "title": "11. Discussion",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 1224,
        "file": "raw/020-discussion.txt",
    },
    {
        "seq": 21,
        "slug": "application",
        "title": "12. Application",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 1350,
        "file": "raw/021-application.txt",
    },
    {
        "seq": 22,
        "slug": "conclusion",
        "title": "13. Conclusion",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 1447,
        "file": "raw/022-conclusion.txt",
    },
    {
        "seq": 50,
        "slug": "references",
        "title": "References",
        "kind": "back-matter",
        "printed_page_start": None,
        "start_line": 1485,
        "file": "raw/050-references.txt",
    },
    {
        "seq": 51,
        "slug": "index",
        "title": "Index",
        "kind": "back-matter",
        "printed_page_start": None,
        "start_line": 1589,
        "file": "raw/051-index.txt",
    },
]


def load_witness() -> list[str]:
    cleaned = (
        TXT_WITNESS.read_text(encoding="utf-8")
        .replace("\x08", "")
        .replace("\xad", "")
        .replace("\f", "")
    )
    FULL_PATH.parent.mkdir(parents=True, exist_ok=True)
    FULL_PATH.write_text(cleaned, encoding="utf-8")
    return cleaned.splitlines()


def split_sections(lines: list[str]) -> None:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    rendered_sections: list[dict[str, object]] = []

    for i, section in enumerate(SECTIONS):
        start = int(section["start_line"])
        end = len(lines) if i == len(SECTIONS) - 1 else int(SECTIONS[i + 1]["start_line"]) - 1
        content = "\n".join(lines[start - 1 : end]).strip() + "\n"

        rel_path = Path(str(section["file"]))
        out_path = SOURCE_DIR / rel_path
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(content, encoding="utf-8")

        rendered = dict(section)
        rendered["end_line"] = end
        rendered["line_count"] = end - start + 1
        rendered_sections.append(rendered)

    book_lines = [
        "book:",
        '  title: "The Promise of Artificial Intelligence: Reckoning and Judgment"',
        '  author: "Brian Cantwell Smith"',
        f'  source_text_witness: "{TXT_WITNESS.relative_to(ROOT).as_posix()}"',
        f'  extracted_full_text: "{FULL_PATH.relative_to(SOURCE_DIR).as_posix()}"',
        "sections:",
    ]

    for section in rendered_sections:
        printed = section["printed_page_start"]
        printed_repr = "null" if printed is None else f'"{printed}"'
        book_lines.extend(
            [
                f'  - seq: {section["seq"]}',
                f'    slug: "{section["slug"]}"',
                f'    title: "{section["title"]}"',
                f'    kind: "{section["kind"]}"',
                f'    file: "{section["file"]}"',
                f'    start_line: {section["start_line"]}',
                f'    end_line: {section["end_line"]}',
                f'    line_count: {section["line_count"]}',
                f"    printed_page_start: {printed_repr}",
            ]
        )

    SECTIONS_PATH.write_text("\n".join(book_lines) + "\n", encoding="utf-8")


def main() -> None:
    lines = load_witness()
    split_sections(lines)


if __name__ == "__main__":
    main()
