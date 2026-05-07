#!/usr/bin/env python3

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TXT_WITNESS = ROOT / (
    "sources/modern/incoming/books/Order Out of Chaos - Ilya Prigogine,Isabelle Stenger.txt"
)
SOURCE_DIR = ROOT / "sources/modern/prigogine-stengers-order-out-of-chaos/source"
FULL_PATH = SOURCE_DIR / "full/order-out-of-chaos.txt"
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
        "slug": "foreword-science-and-change",
        "title": "Foreword: Science and Change",
        "kind": "front-matter",
        "printed_page_start": None,
        "start_line": 297,
        "file": "raw/001-foreword-science-and-change.txt",
    },
    {
        "seq": 2,
        "slug": "preface-mans-new-dialogue-with-nature",
        "title": "Preface: Man's New Dialogue with Nature",
        "kind": "front-matter",
        "printed_page_start": None,
        "start_line": 509,
        "file": "raw/002-preface-mans-new-dialogue-with-nature.txt",
    },
    {
        "seq": 3,
        "slug": "introduction-the-challenge-to-science",
        "title": "Introduction: The Challenge to Science",
        "kind": "front-matter",
        "printed_page_start": None,
        "start_line": 549,
        "file": "raw/003-introduction-the-challenge-to-science.txt",
    },
    {
        "seq": 10,
        "slug": "book-one-the-delusion-of-the-universal",
        "title": "Book One: The Delusion of the Universal",
        "kind": "part",
        "printed_page_start": None,
        "start_line": 741,
        "file": "raw/010-book-one-the-delusion-of-the-universal.txt",
    },
    {
        "seq": 11,
        "slug": "the-triumph-of-reason",
        "title": "Chapter I: The Triumph of Reason",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 753,
        "file": "raw/011-the-triumph-of-reason.txt",
    },
    {
        "seq": 12,
        "slug": "the-identification-of-the-real",
        "title": "Chapter II: The Identification of the Real",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 1070,
        "file": "raw/012-the-identification-of-the-real.txt",
    },
    {
        "seq": 13,
        "slug": "the-two-cultures",
        "title": "Chapter III: The Two Cultures",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 1257,
        "file": "raw/013-the-two-cultures.txt",
    },
    {
        "seq": 20,
        "slug": "book-two-the-science-of-complexity",
        "title": "Book Two: The Science of Complexity",
        "kind": "part",
        "printed_page_start": None,
        "start_line": 1464,
        "file": "raw/020-book-two-the-science-of-complexity.txt",
    },
    {
        "seq": 21,
        "slug": "energy-and-the-industrial-age",
        "title": "Chapter IV: Energy and the Industrial Age",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 1476,
        "file": "raw/021-energy-and-the-industrial-age.txt",
    },
    {
        "seq": 22,
        "slug": "the-three-stages-of-thermodynamics",
        "title": "Chapter V: The Three Stages of Thermodynamics",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 1744,
        "file": "raw/022-the-three-stages-of-thermodynamics.txt",
    },
    {
        "seq": 23,
        "slug": "order-through-fluctuations",
        "title": "Chapter VI: Order Through Fluctuations",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 2197,
        "file": "raw/023-order-through-fluctuations.txt",
    },
    {
        "seq": 30,
        "slug": "book-three-from-being-to-becoming",
        "title": "Book Three: From Being to Becoming",
        "kind": "part",
        "printed_page_start": None,
        "start_line": 2474,
        "file": "raw/030-book-three-from-being-to-becoming.txt",
    },
    {
        "seq": 31,
        "slug": "rediscovering-time",
        "title": "Chapter VII: Rediscovering Time",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 2486,
        "file": "raw/031-rediscovering-time.txt",
    },
    {
        "seq": 32,
        "slug": "the-clash-of-doctrines",
        "title": "Chapter VIII: The Clash of Doctrines",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 2679,
        "file": "raw/032-the-clash-of-doctrines.txt",
    },
    {
        "seq": 33,
        "slug": "irreversibility-the-entropy-barrier",
        "title": "Chapter IX: Irreversibility--the Entropy Barrier",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 2927,
        "file": "raw/033-irreversibility-the-entropy-barrier.txt",
    },
    {
        "seq": 40,
        "slug": "conclusion-from-earth-to-heaven",
        "title": "Conclusion: From Earth to Heaven--the Reenchantment of Nature",
        "kind": "back-matter",
        "printed_page_start": None,
        "start_line": 3317,
        "file": "raw/040-conclusion-from-earth-to-heaven.txt",
    },
    {
        "seq": 50,
        "slug": "notes",
        "title": "Notes",
        "kind": "back-matter",
        "printed_page_start": None,
        "start_line": 3616,
        "file": "raw/050-notes.txt",
    },
    {
        "seq": 51,
        "slug": "index",
        "title": "Index",
        "kind": "back-matter",
        "printed_page_start": None,
        "start_line": 4111,
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
        content = "\n".join(lines[start - 1 : end]) + "\n"

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
        '  title: "Order Out of Chaos: Man\'s New Dialogue with Nature"',
        '  author: "Ilya Prigogine and Isabelle Stengers"',
        f'  source_text_witness: "{TXT_WITNESS.relative_to(ROOT).as_posix()}"',
        f'  extracted_full_text: "{FULL_PATH.relative_to(SOURCE_DIR).as_posix()}"',
        "  extraction_notes:",
        '    - "Generated from the local TXT witness on the incoming shelf."',
        '    - "Control characters and soft hyphens were removed during extraction."',
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
