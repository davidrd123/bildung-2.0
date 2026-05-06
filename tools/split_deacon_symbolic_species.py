#!/usr/bin/env python3

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TXT_WITNESS = ROOT / (
    "sources/modern/incoming/books/The Symbolic Species - Terrence W. Deacon.txt"
)
SOURCE_DIR = ROOT / "sources/modern/deacon-symbolic-species/source"
FULL_PATH = SOURCE_DIR / "full/symbolic-species.txt"
RAW_DIR = SOURCE_DIR / "raw"
SECTIONS_PATH = SOURCE_DIR / "sections.yaml"


SECTIONS = [
    {
        "seq": 0,
        "slug": "title-pages-acknowledgments-and-contents",
        "title": "Title pages, acknowledgments, and contents",
        "kind": "front-matter",
        "printed_page_start": None,
        "start_line": 1,
        "file": "raw/000-title-pages-acknowledgments-and-contents.txt",
    },
    {
        "seq": 1,
        "slug": "preface",
        "title": "Preface",
        "kind": "front-matter",
        "printed_page_start": None,
        "start_line": 401,
        "file": "raw/001-preface.txt",
    },
    {
        "seq": 10,
        "slug": "part-one-language",
        "title": "Part One: Language",
        "kind": "part",
        "printed_page_start": None,
        "start_line": 454,
        "file": "raw/010-part-one-language.txt",
    },
    {
        "seq": 11,
        "slug": "the-human-paradox",
        "title": "1. The Human Paradox",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 464,
        "file": "raw/011-the-human-paradox.txt",
    },
    {
        "seq": 12,
        "slug": "a-loss-for-words",
        "title": "2. A Loss for Words",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 621,
        "file": "raw/012-a-loss-for-words.txt",
    },
    {
        "seq": 13,
        "slug": "symbols-arent-simple",
        "title": "3. Symbols Aren't Simple",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 756,
        "file": "raw/013-symbols-arent-simple.txt",
    },
    {
        "seq": 14,
        "slug": "outside-the-brain",
        "title": "4. Outside the Brain",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 933,
        "file": "raw/014-outside-the-brain.txt",
    },
    {
        "seq": 20,
        "slug": "part-two-brain",
        "title": "Part Two: Brain",
        "kind": "part",
        "printed_page_start": None,
        "start_line": 1157,
        "file": "raw/020-part-two-brain.txt",
    },
    {
        "seq": 21,
        "slug": "the-size-of-intelligence",
        "title": "5. The Size of Intelligence",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 1167,
        "file": "raw/021-the-size-of-intelligence.txt",
    },
    {
        "seq": 22,
        "slug": "growing-apart",
        "title": "6. Growing Apart",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 1294,
        "file": "raw/022-growing-apart.txt",
    },
    {
        "seq": 23,
        "slug": "a-darwinian-electrician",
        "title": "7. A Darwinian Electrician",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 1469,
        "file": "raw/023-a-darwinian-electrician.txt",
    },
    {
        "seq": 24,
        "slug": "the-talking-brain",
        "title": "8. The Talking Brain",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 1673,
        "file": "raw/024-the-talking-brain.txt",
    },
    {
        "seq": 25,
        "slug": "symbol-minds",
        "title": "9. Symbol Minds",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 1861,
        "file": "raw/025-symbol-minds.txt",
    },
    {
        "seq": 26,
        "slug": "locating-language",
        "title": "10. Locating Language",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 1999,
        "file": "raw/026-locating-language.txt",
    },
    {
        "seq": 30,
        "slug": "part-three-co-evolution",
        "title": "Part Three: Co-Evolution",
        "kind": "part",
        "printed_page_start": None,
        "start_line": 2235,
        "file": "raw/030-part-three-co-evolution.txt",
    },
    {
        "seq": 31,
        "slug": "and-the-word-became-flesh",
        "title": "11. And the Word Became Flesh",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 2245,
        "file": "raw/031-and-the-word-became-flesh.txt",
    },
    {
        "seq": 32,
        "slug": "symbolic-origins",
        "title": "12. Symbolic Origins",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 2534,
        "file": "raw/032-symbolic-origins.txt",
    },
    {
        "seq": 33,
        "slug": "a-serendipitous-mind",
        "title": "13. A Serendipitous Mind",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 2750,
        "file": "raw/033-a-serendipitous-mind.txt",
    },
    {
        "seq": 34,
        "slug": "such-stuff-as-dreams-are-made-on",
        "title": "14. Such Stuff as Dreams Are Made On",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 2897,
        "file": "raw/034-such-stuff-as-dreams-are-made-on.txt",
    },
    {
        "seq": 50,
        "slug": "notes",
        "title": "Notes",
        "kind": "back-matter",
        "printed_page_start": None,
        "start_line": 3078,
        "file": "raw/050-notes.txt",
    },
    {
        "seq": 51,
        "slug": "additional-readings",
        "title": "Additional Readings",
        "kind": "back-matter",
        "printed_page_start": None,
        "start_line": 3457,
        "file": "raw/051-additional-readings.txt",
    },
    {
        "seq": 52,
        "slug": "bibliography",
        "title": "Bibliography",
        "kind": "back-matter",
        "printed_page_start": None,
        "start_line": 3520,
        "file": "raw/052-bibliography.txt",
    },
    {
        "seq": 53,
        "slug": "index",
        "title": "Index",
        "kind": "back-matter",
        "printed_page_start": None,
        "start_line": 4335,
        "file": "raw/053-index.txt",
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
        '  title: "The Symbolic Species: The Co-Evolution of Language and the Brain"',
        '  author: "Terrence W. Deacon"',
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
