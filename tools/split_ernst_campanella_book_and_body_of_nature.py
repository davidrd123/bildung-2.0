#!/usr/bin/env python3

from __future__ import annotations

import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PDF_PATH = ROOT / (
    "sources/modern/incoming/books/"
    "Tommaso Campanella - The Book and the Body of Nature -- Germana Ernst.pdf"
)
SOURCE_DIR = ROOT / "sources/modern/ernst-campanella-book-and-body-of-nature/source"
FULL_PATH = SOURCE_DIR / "full/campanella-book-and-body-of-nature.txt"
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
        "slug": "preface",
        "title": "Preface",
        "kind": "preface",
        "printed_page_start": "vii",
        "start_line": 173,
        "file": "raw/001-preface.txt",
    },
    {
        "seq": 10,
        "slug": "telesius-me-delectavit",
        "title": "1. Telesius me delectavit",
        "kind": "chapter",
        "printed_page_start": "1",
        "start_line": 244,
        "file": "raw/010-telesius-me-delectavit.txt",
    },
    {
        "seq": 11,
        "slug": "from-naples-to-padua",
        "title": "2. From Naples to Padua: Encounters, Conflicts, Trials",
        "kind": "chapter",
        "printed_page_start": "15",
        "start_line": 921,
        "file": "raw/011-from-naples-to-padua.txt",
    },
    {
        "seq": 12,
        "slug": "the-palace-of-atlas",
        "title": "3. The Palace of Atlas",
        "kind": "chapter",
        "printed_page_start": "33",
        "start_line": 1759,
        "file": "raw/012-the-palace-of-atlas.txt",
    },
    {
        "seq": 13,
        "slug": "back-to-naples-and-calabria",
        "title": "4. Back to Naples and Calabria",
        "kind": "chapter",
        "printed_page_start": "45",
        "start_line": 2349,
        "file": "raw/013-back-to-naples-and-calabria.txt",
    },
    {
        "seq": 14,
        "slug": "the-conspiracy",
        "title": "5. The Conspiracy",
        "kind": "chapter",
        "printed_page_start": "67",
        "start_line": 3337,
        "file": "raw/014-the-conspiracy.txt",
    },
    {
        "seq": 15,
        "slug": "prophecy-politics-and-utopia",
        "title": "6. Prophecy, Politics and Utopia",
        "kind": "chapter",
        "printed_page_start": "85",
        "start_line": 4192,
        "file": "raw/015-prophecy-politics-and-utopia.txt",
    },
    {
        "seq": 16,
        "slug": "in-the-cave-of-polyphemus",
        "title": "7. In the Cave of Polyphemus",
        "kind": "chapter",
        "printed_page_start": "105",
        "start_line": 5116,
        "file": "raw/016-in-the-cave-of-polyphemus.txt",
    },
    {
        "seq": 17,
        "slug": "christian-unity",
        "title": "8. Christian Unity",
        "kind": "chapter",
        "printed_page_start": "137",
        "start_line": 6605,
        "file": "raw/017-christian-unity.txt",
    },
    {
        "seq": 18,
        "slug": "new-heavens",
        "title": "9. New Heavens",
        "kind": "chapter",
        "printed_page_start": "159",
        "start_line": 7628,
        "file": "raw/018-new-heavens.txt",
    },
    {
        "seq": 19,
        "slug": "the-new-encyclopedia-of-knowledge",
        "title": "10. The New Encyclopedia of Knowledge",
        "kind": "chapter",
        "printed_page_start": "181",
        "start_line": 8666,
        "file": "raw/019-the-new-encyclopedia-of-knowledge.txt",
    },
    {
        "seq": 20,
        "slug": "the-disappointment-of-liberty",
        "title": "11. The Disappointment of Liberty",
        "kind": "chapter",
        "printed_page_start": "215",
        "start_line": 10260,
        "file": "raw/020-the-disappointment-of-liberty.txt",
    },
    {
        "seq": 21,
        "slug": "the-paris-years",
        "title": "12. The Paris Years",
        "kind": "chapter",
        "printed_page_start": "243",
        "start_line": 11523,
        "file": "raw/021-the-paris-years.txt",
    },
    {
        "seq": 30,
        "slug": "list-of-abbreviations",
        "title": "List of Abbreviations",
        "kind": "back-matter",
        "printed_page_start": "267",
        "start_line": 12634,
        "file": "raw/030-list-of-abbreviations.txt",
    },
    {
        "seq": 31,
        "slug": "index-of-names",
        "title": "Index of Names",
        "kind": "back-matter",
        "printed_page_start": "271",
        "start_line": 12767,
        "file": "raw/031-index-of-names.txt",
    },
    {
        "seq": 32,
        "slug": "subject-index",
        "title": "Subject Index",
        "kind": "back-matter",
        "printed_page_start": "279",
        "start_line": 13123,
        "file": "raw/032-subject-index.txt",
    },
]


def run_pdftotext() -> list[str]:
    FULL_PATH.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ["pdftotext", "-layout", str(PDF_PATH), str(FULL_PATH)],
        check=True,
    )
    cleaned = (
        FULL_PATH.read_text(encoding="utf-8")
        .replace("\x08", "")
        .replace("\xad", "")
        .replace("\f", "")
    )
    FULL_PATH.write_text(cleaned, encoding="utf-8")
    return cleaned.splitlines()


def split_sections(lines: list[str]) -> None:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    rendered_sections: list[dict[str, object]] = []

    for index, section in enumerate(SECTIONS):
        start = section["start_line"]
        end = (
            SECTIONS[index + 1]["start_line"] - 1
            if index + 1 < len(SECTIONS)
            else len(lines)
        )
        content = "\n".join(lines[start - 1 : end]).strip() + "\n"
        out_path = SOURCE_DIR / section["file"]
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(content, encoding="utf-8")

        rendered_sections.append(
            {
                **section,
                "end_line": end,
                "line_count": end - start + 1,
            }
        )

    section_lines = [
        "book:",
        '  title: "Tommaso Campanella: The Book and the Body of Nature"',
        '  author: "Germana Ernst"',
        '  translator: "David L. Marshall"',
        f'  source_pdf: "{PDF_PATH.relative_to(ROOT).as_posix()}"',
        f'  extracted_full_text: "{FULL_PATH.relative_to(SOURCE_DIR).as_posix()}"',
        "sections:",
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
                f'    start_line: {section["start_line"]}',
                f'    end_line: {section["end_line"]}',
                f'    line_count: {section["line_count"]}',
                f"    printed_page_start: {page_text}",
            ]
        )

    SECTIONS_PATH.write_text("\n".join(section_lines) + "\n", encoding="utf-8")


def main() -> None:
    if not PDF_PATH.exists():
        raise FileNotFoundError(PDF_PATH)
    split_sections(run_pdftotext())


if __name__ == "__main__":
    main()
