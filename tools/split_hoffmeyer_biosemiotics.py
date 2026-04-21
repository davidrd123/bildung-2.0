#!/usr/bin/env python3

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TXT_WITNESS = ROOT / (
    "sources/modern/incoming/books/"
    "Biosemiotics_ An Examination into the Signs of Life and the -- Jesper Hoffmeyer.txt"
)
PDF_AUTHORITY = ROOT / (
    "sources/modern/incoming/books/"
    "Biosemiotics_ An Examination into the Signs of Life and the -- Jesper Hoffmeyer.pdf"
)
SOURCE_DIR = ROOT / "sources/modern/hoffmeyer-biosemiotics/source"
FULL_PATH = SOURCE_DIR / "full/biosemiotics.txt"
RAW_DIR = SOURCE_DIR / "raw"
SECTIONS_PATH = SOURCE_DIR / "sections.yaml"


SECTIONS = [
    {
        "seq": 0,
        "slug": "title-pages-and-publisher-matter",
        "title": "Title pages and publisher matter",
        "kind": "front-matter",
        "printed_page_start": None,
        "start_line": 1,
        "file": "raw/000-title-pages-and-publisher-matter.txt",
    },
    {
        "seq": 1,
        "slug": "contents",
        "title": "Contents",
        "kind": "front-matter",
        "printed_page_start": None,
        "start_line": 98,
        "file": "raw/001-contents.txt",
    },
    {
        "seq": 2,
        "slug": "preface",
        "title": "Preface",
        "kind": "preface",
        "printed_page_start": None,
        "start_line": 430,
        "file": "raw/002-preface.txt",
    },
    {
        "seq": 10,
        "slug": "on-biosemiotics",
        "title": "1. On Biosemiotics",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 793,
        "file": "raw/010-on-biosemiotics.txt",
    },
    {
        "seq": 11,
        "slug": "surfaces-within-surfaces",
        "title": "2. Surfaces within Surfaces",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 1510,
        "file": "raw/011-surfaces-within-surfaces.txt",
    },
    {
        "seq": 12,
        "slug": "sign-and-cause",
        "title": "3. Sign and Cause",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 2546,
        "file": "raw/012-sign-and-cause.txt",
    },
    {
        "seq": 13,
        "slug": "code-duality",
        "title": "4. Code-Duality",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 4050,
        "file": "raw/013-code-duality.txt",
    },
    {
        "seq": 14,
        "slug": "the-semiotics-of-heredity",
        "title": "5. The Semiotics of Heredity",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 5980,
        "file": "raw/014-the-semiotics-of-heredity.txt",
    },
    {
        "seq": 15,
        "slug": "the-semiotic-niche",
        "title": "6. The Semiotic Niche",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 8521,
        "file": "raw/015-the-semiotic-niche.txt",
    },
    {
        "seq": 16,
        "slug": "endosemiotics",
        "title": "7. Endosemiotics",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 10682,
        "file": "raw/016-endosemiotics.txt",
    },
    {
        "seq": 17,
        "slug": "from-animal-to-human",
        "title": "8. From Animal to Human",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 13059,
        "file": "raw/017-from-animal-to-human.txt",
    },
    {
        "seq": 18,
        "slug": "perspectives",
        "title": "9. Perspectives",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 15290,
        "file": "raw/018-perspectives.txt",
    },
    {
        "seq": 19,
        "slug": "biosemiotic-technology",
        "title": "10. Biosemiotic Technology",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 16502,
        "file": "raw/019-biosemiotic-technology.txt",
    },
    {
        "seq": 50,
        "slug": "postscript-short-historical-notes",
        "title": "Postscript: Short Historical Notes",
        "kind": "back-matter",
        "printed_page_start": None,
        "start_line": 17138,
        "file": "raw/050-postscript-short-historical-notes.txt",
    },
    {
        "seq": 51,
        "slug": "literature",
        "title": "Literature",
        "kind": "back-matter",
        "printed_page_start": None,
        "start_line": 17746,
        "file": "raw/051-literature.txt",
    },
    {
        "seq": 52,
        "slug": "index",
        "title": "Index",
        "kind": "back-matter",
        "printed_page_start": None,
        "start_line": 19018,
        "file": "raw/052-index.txt",
    },
    {
        "seq": 53,
        "slug": "back-cover-blurbs-and-scan-noise",
        "title": "Back-cover blurbs and scan noise",
        "kind": "back-matter",
        "printed_page_start": None,
        "start_line": 19920,
        "file": "raw/053-back-cover-blurbs-and-scan-noise.txt",
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
        start = section["start_line"]
        end = len(lines) if i == len(SECTIONS) - 1 else SECTIONS[i + 1]["start_line"] - 1
        content = "\n".join(lines[start - 1 : end]).strip() + "\n"

        rel_path = Path(section["file"])
        out_path = SOURCE_DIR / rel_path
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(content, encoding="utf-8")

        rendered = dict(section)
        rendered["end_line"] = end
        rendered["line_count"] = end - start + 1
        rendered_sections.append(rendered)

    book_lines = [
        "book:",
        '  title: "Biosemiotics: An Examination into the Signs of Life and the Life of Signs"',
        '  author: "Jesper Hoffmeyer"',
        f'  source_pdf: "{PDF_AUTHORITY.relative_to(ROOT).as_posix()}"',
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
