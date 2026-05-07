#!/usr/bin/env python3

from __future__ import annotations

import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PDF_AUTHORITY = ROOT / (
    "sources/modern/incoming/books/"
    "What Is Intelligence__ Lessons from AI About Evolution, -- Aguera y Arcas, Blaise -- 2025.pdf"
)
SOURCE_DIR = ROOT / "sources/modern/aguera-y-arcas-what-is-intelligence/source"
FULL_PATH = SOURCE_DIR / "full/what-is-intelligence.txt"
RAW_DIR = SOURCE_DIR / "raw"
SECTIONS_PATH = SOURCE_DIR / "sections.yaml"


SECTIONS = [
    {
        "seq": 0,
        "slug": "title-pages-and-copyright",
        "title": "Title pages and copyright",
        "kind": "front-matter",
        "printed_page_start": None,
        "start_line": 1,
        "file": "raw/000-title-pages-and-copyright.txt",
    },
    {
        "seq": 1,
        "slug": "note-on-the-e-book",
        "title": "A note on the e-book",
        "kind": "front-matter",
        "printed_page_start": None,
        "start_line": 10,
        "file": "raw/001-note-on-the-e-book.txt",
    },
    {
        "seq": 2,
        "slug": "contents",
        "title": "Contents",
        "kind": "front-matter",
        "printed_page_start": None,
        "start_line": 17,
        "file": "raw/002-contents.txt",
    },
    {
        "seq": 3,
        "slug": "foreword-by-benjamin-bratton",
        "title": "Foreword by Benjamin Bratton",
        "kind": "front-matter",
        "printed_page_start": None,
        "start_line": 142,
        "file": "raw/003-foreword-by-benjamin-bratton.txt",
    },
    {
        "seq": 4,
        "slug": "preface",
        "title": "Preface",
        "kind": "front-matter",
        "printed_page_start": None,
        "start_line": 172,
        "file": "raw/004-preface.txt",
    },
    {
        "seq": 5,
        "slug": "introduction",
        "title": "Introduction",
        "kind": "front-matter",
        "printed_page_start": None,
        "start_line": 438,
        "file": "raw/005-introduction.txt",
    },
    {
        "seq": 10,
        "slug": "origins",
        "title": "1. Origins",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 767,
        "file": "raw/010-origins.txt",
    },
    {
        "seq": 11,
        "slug": "survival",
        "title": "2. Survival",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 2555,
        "file": "raw/011-survival.txt",
    },
    {
        "seq": 12,
        "slug": "interlude-the-prehistory-of-computing",
        "title": "Interlude: The Prehistory of Computing",
        "kind": "interlude",
        "printed_page_start": None,
        "start_line": 3490,
        "file": "raw/012-interlude-the-prehistory-of-computing.txt",
    },
    {
        "seq": 13,
        "slug": "cybernetics",
        "title": "3. Cybernetics",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 3900,
        "file": "raw/013-cybernetics.txt",
    },
    {
        "seq": 14,
        "slug": "learning",
        "title": "4. Learning",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 4887,
        "file": "raw/014-learning.txt",
    },
    {
        "seq": 15,
        "slug": "other-minds",
        "title": "5. Other Minds",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 5957,
        "file": "raw/015-other-minds.txt",
    },
    {
        "seq": 16,
        "slug": "many-worlds",
        "title": "6. Many Worlds",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 6886,
        "file": "raw/016-many-worlds.txt",
    },
    {
        "seq": 17,
        "slug": "ourselves",
        "title": "7. Ourselves",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 8173,
        "file": "raw/017-ourselves.txt",
    },
    {
        "seq": 18,
        "slug": "transformers",
        "title": "8. Transformers",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 9200,
        "file": "raw/018-transformers.txt",
    },
    {
        "seq": 19,
        "slug": "generality",
        "title": "9. Generality",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 10481,
        "file": "raw/019-generality.txt",
    },
    {
        "seq": 20,
        "slug": "interlude-no-perfect-heroes-or-villains",
        "title": "Interlude: No Perfect Heroes or Villains",
        "kind": "interlude",
        "printed_page_start": None,
        "start_line": 12294,
        "file": "raw/020-interlude-no-perfect-heroes-or-villains.txt",
    },
    {
        "seq": 21,
        "slug": "evolutionary-transition",
        "title": "10. Evolutionary Transition",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 12397,
        "file": "raw/021-evolutionary-transition.txt",
    },
    {
        "seq": 50,
        "slug": "acknowledgments",
        "title": "Acknowledgments",
        "kind": "back-matter",
        "printed_page_start": None,
        "start_line": 14168,
        "file": "raw/050-acknowledgments.txt",
    },
    {
        "seq": 51,
        "slug": "about-the-author",
        "title": "About the Author",
        "kind": "back-matter",
        "printed_page_start": None,
        "start_line": 14278,
        "file": "raw/051-about-the-author.txt",
    },
    {
        "seq": 52,
        "slug": "the-antikythera-book-series",
        "title": "The Antikythera Book Series",
        "kind": "back-matter",
        "printed_page_start": None,
        "start_line": 14292,
        "file": "raw/052-the-antikythera-book-series.txt",
    },
    {
        "seq": 53,
        "slug": "glossary",
        "title": "Glossary",
        "kind": "back-matter",
        "printed_page_start": None,
        "start_line": 14363,
        "file": "raw/053-glossary.txt",
    },
    {
        "seq": 54,
        "slug": "bibliography",
        "title": "Bibliography",
        "kind": "back-matter",
        "printed_page_start": None,
        "start_line": 15002,
        "file": "raw/054-bibliography.txt",
    },
    {
        "seq": 55,
        "slug": "notes",
        "title": "Notes",
        "kind": "back-matter",
        "printed_page_start": None,
        "start_line": 16711,
        "file": "raw/055-notes.txt",
    },
]


def extract_pdf_text() -> tuple[list[str], list[int | None]]:
    try:
        proc = subprocess.run(
            ["pdftotext", str(PDF_AUTHORITY), "-"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    except FileNotFoundError as exc:
        raise SystemExit("pdftotext is required to regenerate this scaffold") from exc

    text = (
        proc.stdout.decode("utf-8", errors="replace")
        .replace("\x08", "")
        .replace("\xad", "")
    )
    pages = text.split("\f")
    if pages and not pages[0].strip():
        pages = pages[1:]

    lines: list[str] = []
    pdf_pages: list[int | None] = []
    for pageno, page in enumerate(pages, 1):
        page_lines = []
        for line in page.splitlines():
            line = line.rstrip()
            if line.strip() == "OceanofPDF.com":
                continue
            page_lines.append(line)

        while page_lines and not page_lines[0].strip():
            page_lines.pop(0)
        while page_lines and not page_lines[-1].strip():
            page_lines.pop()
        if not page_lines:
            continue

        if lines:
            lines.append("")
            pdf_pages.append(None)
        for line in page_lines:
            lines.append(line)
            pdf_pages.append(pageno)

    FULL_PATH.parent.mkdir(parents=True, exist_ok=True)
    FULL_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return lines, pdf_pages


def split_sections(lines: list[str], pdf_pages: list[int | None]) -> None:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    rendered_sections: list[dict[str, object]] = []

    for i, section in enumerate(SECTIONS):
        start = int(section["start_line"])
        end = len(lines) if i == len(SECTIONS) - 1 else int(SECTIONS[i + 1]["start_line"]) - 1
        content = "\n".join(lines[start - 1 : end]) + "\n"

        rel_path = Path(str(section["file"]))
        out_path = SOURCE_DIR / rel_path
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(content, encoding="utf-8")

        rendered = dict(section)
        rendered["end_line"] = end
        rendered["line_count"] = end - start + 1
        rendered["pdf_page_start"] = pdf_pages[start - 1]
        rendered_sections.append(rendered)

    book_lines = [
        "book:",
        '  title: "What Is Intelligence?: Lessons from AI About Evolution, Computing, and Minds"',
        '  author: "Blaise Agüera y Arcas"',
        f'  source_pdf: "{PDF_AUTHORITY.relative_to(ROOT).as_posix()}"',
        f'  extracted_full_text: "{FULL_PATH.relative_to(SOURCE_DIR).as_posix()}"',
        "  extraction_notes:",
        '    - "Generated with pdftotext from the local PDF witness."',
        '    - "Repeated source footer lines were removed during extraction."',
        "sections:",
    ]

    for section in rendered_sections:
        printed = section["printed_page_start"]
        printed_repr = "null" if printed is None else f'"{printed}"'
        pdf_page = section["pdf_page_start"]
        pdf_page_repr = "null" if pdf_page is None else str(pdf_page)
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
                f"    pdf_page_start: {pdf_page_repr}",
            ]
        )

    SECTIONS_PATH.write_text("\n".join(book_lines) + "\n", encoding="utf-8")


def main() -> None:
    lines, pdf_pages = extract_pdf_text()
    split_sections(lines, pdf_pages)


if __name__ == "__main__":
    main()
