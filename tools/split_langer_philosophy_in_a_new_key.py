#!/usr/bin/env python3

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TXT_WITNESS = ROOT / (
    "sources/modern/incoming/books/Philosophy in a New Key - Susanne Langer.txt"
)
PDF_AUTHORITY = ROOT / (
    "sources/modern/incoming/books/Philosophy in a New Key - Susanne Langer.pdf"
)
SOURCE_DIR = ROOT / "sources/modern/langer-philosophy-in-a-new-key/source"
FULL_PATH = SOURCE_DIR / "full/philosophy-in-a-new-key.txt"
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
        "slug": "preface-to-the-second-edition",
        "title": "Preface to the Second Edition",
        "kind": "preface",
        "printed_page_start": "v",
        "start_line": 96,
        "file": "raw/001-preface-to-the-second-edition.txt",
    },
    {
        "seq": 2,
        "slug": "preface-to-the-first-edition",
        "title": "Preface to the First Edition",
        "kind": "preface",
        "printed_page_start": "vii",
        "start_line": 191,
        "file": "raw/002-preface-to-the-first-edition.txt",
    },
    {
        "seq": 3,
        "slug": "contents",
        "title": "Contents",
        "kind": "front-matter",
        "printed_page_start": "xii",
        "start_line": 318,
        "file": "raw/003-contents.txt",
    },
    {
        "seq": 10,
        "slug": "the-new-key",
        "title": "1. The New Key",
        "kind": "chapter",
        "printed_page_start": "15",
        "start_line": 623,
        "file": "raw/010-the-new-key.txt",
    },
    {
        "seq": 11,
        "slug": "symbolic-transformation",
        "title": "2. Symbolic Transformation",
        "kind": "chapter",
        "printed_page_start": "33",
        "start_line": 1545,
        "file": "raw/011-symbolic-transformation.txt",
    },
    {
        "seq": 12,
        "slug": "the-logic-of-signs-and-symbols",
        "title": "3. The Logic of Signs and Symbols",
        "kind": "chapter",
        "printed_page_start": "54",
        "start_line": 2698,
        "file": "raw/012-the-logic-of-signs-and-symbols.txt",
    },
    {
        "seq": 13,
        "slug": "discursive-forms-and-presentational-forms",
        "title": "4. Discursive Forms and Presentational Forms",
        "kind": "chapter",
        "printed_page_start": "75",
        "start_line": 3735,
        "file": "raw/013-discursive-forms-and-presentational-forms.txt",
    },
    {
        "seq": 14,
        "slug": "language",
        "title": "5. Language",
        "kind": "chapter",
        "printed_page_start": "94",
        "start_line": 4857,
        "file": "raw/014-language.txt",
    },
    {
        "seq": 15,
        "slug": "life-symbols-the-roots-of-sacrament",
        "title": "6. Life-Symbols: The Roots of Sacrament",
        "kind": "chapter",
        "printed_page_start": "127",
        "start_line": 6539,
        "file": "raw/015-life-symbols-the-roots-of-sacrament.txt",
    },
    {
        "seq": 16,
        "slug": "life-symbols-the-roots-of-myth",
        "title": "7. Life-Symbols: The Roots of Myth",
        "kind": "chapter",
        "printed_page_start": "148",
        "start_line": 7665,
        "file": "raw/016-life-symbols-the-roots-of-myth.txt",
    },
    {
        "seq": 17,
        "slug": "on-significance-in-music",
        "title": "8. On Significance in Music",
        "kind": "chapter",
        "printed_page_start": "174",
        "start_line": 9029,
        "file": "raw/017-on-significance-in-music.txt",
    },
    {
        "seq": 18,
        "slug": "the-genesis-of-artistic-import",
        "title": "9. The Genesis of Artistic Import",
        "kind": "chapter",
        "printed_page_start": "208",
        "start_line": 10885,
        "file": "raw/018-the-genesis-of-artistic-import.txt",
    },
    {
        "seq": 19,
        "slug": "the-fabric-of-meaning",
        "title": "10. The Fabric of Meaning",
        "kind": "chapter",
        "printed_page_start": "224",
        "start_line": 11742,
        "file": "raw/019-the-fabric-of-meaning.txt",
    },
    {
        "seq": 30,
        "slug": "acknowledgments",
        "title": "Acknowledgments",
        "kind": "back-matter",
        "printed_page_start": "247",
        "start_line": 12932,
        "file": "raw/030-acknowledgments.txt",
    },
    {
        "seq": 31,
        "slug": "index",
        "title": "Index",
        "kind": "back-matter",
        "printed_page_start": "251",
        "start_line": 13161,
        "file": "raw/031-index.txt",
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
        '  title: "Philosophy in a New Key: A Study in the Symbolism of Reason, Rite, and Art"',
        '  author: "Susanne K. Langer"',
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
