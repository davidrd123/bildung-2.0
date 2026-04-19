#!/usr/bin/env python3

from __future__ import annotations

import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PDF_PATH = ROOT / (
    "sources/modern/incoming/books/"
    "Language Machines_ Cultural AI and the End of Remainder -- "
    "Leif Weatherby -- Posthumanities, 2025.pdf"
)
SOURCE_DIR = ROOT / "sources/modern/weatherby-language-machines/source"
FULL_PATH = SOURCE_DIR / "full/language-machines.txt"
RAW_DIR = SOURCE_DIR / "raw"
SECTIONS_PATH = SOURCE_DIR / "sections.yaml"


SECTIONS = [
    {
        "seq": 0,
        "slug": "front-matter-and-contents",
        "title": "Front matter and contents",
        "kind": "front-matter",
        "printed_page_start": None,
        "start_line": 1,
        "file": "raw/000-front-matter-and-contents.txt",
    },
    {
        "seq": 1,
        "slug": "acknowledgments",
        "title": "Acknowledgments",
        "kind": "acknowledgments",
        "printed_page_start": "vii",
        "start_line": 124,
        "file": "raw/001-acknowledgments.txt",
    },
    {
        "seq": 10,
        "slug": "introduction-ai-between-cognition-and-culture",
        "title": "Introduction: AI between Cognition and Culture",
        "kind": "introduction",
        "printed_page_start": "1",
        "start_line": 161,
        "file": "raw/010-introduction-ai-between-cognition-and-culture.txt",
    },
    {
        "seq": 11,
        "slug": "how-the-humanities-lost-language",
        "title": "1. How the Humanities Lost Language: Syntax, Statistics, and Structure",
        "kind": "chapter",
        "printed_page_start": "41",
        "start_line": 1731,
        "file": "raw/011-how-the-humanities-lost-language.txt",
    },
    {
        "seq": 12,
        "slug": "the-eliza-effect-goes-global",
        "title": "2. The Eliza Effect Goes Global: Intelligence as Simulacrum",
        "kind": "chapter",
        "printed_page_start": "79",
        "start_line": 3236,
        "file": "raw/012-the-eliza-effect-goes-global.txt",
    },
    {
        "seq": 13,
        "slug": "the-semiological-surround",
        "title": "3. The Semiological Surround, or How Language Is the Medium of Computation",
        "kind": "chapter",
        "printed_page_start": "101",
        "start_line": 4054,
        "file": "raw/013-the-semiological-surround.txt",
    },
    {
        "seq": 14,
        "slug": "large-literary-machines",
        "title": "4. Large Literary Machines",
        "kind": "chapter",
        "printed_page_start": "123",
        "start_line": 4901,
        "file": "raw/014-large-literary-machines.txt",
    },
    {
        "seq": 15,
        "slug": "computational-meaning",
        "title": "5. Computational Meaning: For a General Poetics",
        "kind": "chapter",
        "printed_page_start": "139",
        "start_line": 5556,
        "file": "raw/015-computational-meaning.txt",
    },
    {
        "seq": 16,
        "slug": "poetic-ideology",
        "title": "6. Poetic Ideology: The Packaged Semantics of Generative Culture",
        "kind": "chapter",
        "printed_page_start": "173",
        "start_line": 6844,
        "file": "raw/016-poetic-ideology.txt",
    },
    {
        "seq": 17,
        "slug": "conclusion-language-as-a-service",
        "title": "Conclusion: Language as a Service, or the Return of Rhetoric",
        "kind": "conclusion",
        "printed_page_start": "195",
        "start_line": 7700,
        "file": "raw/017-conclusion-language-as-a-service.txt",
    },
    {
        "seq": 30,
        "slug": "notes",
        "title": "Notes",
        "kind": "back-matter",
        "printed_page_start": "213",
        "start_line": 8406,
        "file": "raw/030-notes.txt",
    },
    {
        "seq": 31,
        "slug": "bibliography",
        "title": "Bibliography",
        "kind": "back-matter",
        "printed_page_start": "233",
        "start_line": 9328,
        "file": "raw/031-bibliography.txt",
    },
    {
        "seq": 32,
        "slug": "index",
        "title": "Index",
        "kind": "back-matter",
        "printed_page_start": "249",
        "start_line": 10068,
        "file": "raw/032-index.txt",
    },
]


def run_pdftotext() -> None:
    FULL_PATH.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ["pdftotext", "-layout", str(PDF_PATH), str(FULL_PATH)],
        check=True,
    )
    cleaned = (
        FULL_PATH.read_text(encoding="utf-8")
        .replace("\x08", "")
        .replace("\xad", "")
    )
    FULL_PATH.write_text(cleaned, encoding="utf-8")


def split_sections() -> None:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    lines = FULL_PATH.read_text(encoding="utf-8").splitlines()

    rendered_sections = []
    for idx, section in enumerate(SECTIONS):
        start = section["start_line"]
        end = (
            SECTIONS[idx + 1]["start_line"] - 1
            if idx + 1 < len(SECTIONS)
            else len(lines)
        )
        body = "\n".join(lines[start - 1 : end]).rstrip() + "\n"
        (SOURCE_DIR / section["file"]).write_text(body, encoding="utf-8")

        rendered_sections.append(
            {
                **section,
                "end_line": end,
                "line_count": end - start + 1,
            }
        )

    section_lines = [
        'book:',
        '  title: "Language Machines: Cultural AI and the End of Remainder Humanism"',
        '  author: "Leif Weatherby"',
        (
            "  source_pdf: "
            '"sources/modern/incoming/books/Language Machines_ Cultural AI and the End '
            'of Remainder -- Leif Weatherby -- Posthumanities, 2025.pdf"'
        ),
        '  extracted_full_text: "source/full/language-machines.txt"',
        'sections:',
    ]

    for section in rendered_sections:
        page = section["printed_page_start"]
        page_text = "null" if page is None else f'"{page}"'
        section_lines.extend(
            [
                f'  - seq: {section["seq"]}',
                f'    slug: "{section["slug"]}"',
                f'    title: "{section["title"]}"',
                f'    kind: "{section["kind"]}"',
                f'    file: "{section["file"]}"',
                f"    start_line: {section['start_line']}",
                f"    end_line: {section['end_line']}",
                f"    line_count: {section['line_count']}",
                f"    printed_page_start: {page_text}",
            ]
        )

    SECTIONS_PATH.write_text("\n".join(section_lines) + "\n", encoding="utf-8")


def main() -> None:
    if not PDF_PATH.exists():
        raise FileNotFoundError(PDF_PATH)
    run_pdftotext()
    split_sections()


if __name__ == "__main__":
    main()
