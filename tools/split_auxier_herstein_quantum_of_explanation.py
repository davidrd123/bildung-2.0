#!/usr/bin/env python3

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TXT_WITNESS = ROOT / (
    "sources/modern/incoming/books/"
    "The Quantum of Explanation - Auxier, Randall E.; Herstein, G.txt"
)
SOURCE_DIR = ROOT / "sources/modern/auxier-herstein-quantum-of-explanation/source"
FULL_PATH = SOURCE_DIR / "full/quantum-of-explanation.txt"
RAW_DIR = SOURCE_DIR / "raw"
SECTIONS_PATH = SOURCE_DIR / "sections.yaml"


SECTIONS = [
    {
        "seq": 0,
        "slug": "title-pages-and-contents",
        "title": "Title pages and contents",
        "kind": "front-matter",
        "start_line": 1,
        "file": "raw/000-title-pages-and-contents.txt",
    },
    {
        "seq": 1,
        "slug": "preface",
        "title": "Preface",
        "kind": "front-matter",
        "start_line": 169,
        "file": "raw/001-preface.txt",
    },
    {
        "seq": 2,
        "slug": "acknowledgements",
        "title": "Acknowledgements",
        "kind": "front-matter",
        "start_line": 214,
        "file": "raw/002-acknowledgements.txt",
    },
    {
        "seq": 10,
        "slug": "introduction",
        "title": "Introduction",
        "kind": "introduction",
        "start_line": 229,
        "file": "raw/010-introduction.txt",
    },
    {
        "seq": 11,
        "slug": "reading-whitehead",
        "title": "1. Reading Whitehead",
        "kind": "chapter",
        "start_line": 510,
        "file": "raw/011-reading-whitehead.txt",
    },
    {
        "seq": 12,
        "slug": "whiteheads-radical-empiricism",
        "title": "2. Whitehead's Radical Empiricism",
        "kind": "chapter",
        "start_line": 667,
        "file": "raw/012-whiteheads-radical-empiricism.txt",
    },
    {
        "seq": 13,
        "slug": "the-logic-in-metaphysics",
        "title": "3. The Logic in Metaphysics",
        "kind": "chapter",
        "start_line": 777,
        "file": "raw/013-the-logic-in-metaphysics.txt",
    },
    {
        "seq": 14,
        "slug": "the-quantum-of-explanation",
        "title": "4. The Quantum of Explanation",
        "kind": "chapter",
        "start_line": 991,
        "file": "raw/014-the-quantum-of-explanation.txt",
    },
    {
        "seq": 15,
        "slug": "extensive-connectedness-the-metaphysics-in-logic",
        "title": "5. Extensive Connectedness (The Metaphysics in Logic)",
        "kind": "chapter",
        "start_line": 1166,
        "file": "raw/015-extensive-connectedness-the-metaphysics-in-logic.txt",
    },
    {
        "seq": 16,
        "slug": "the-principle-of-relativity",
        "title": "6. The Principle of Relativity",
        "kind": "chapter",
        "start_line": 1354,
        "file": "raw/016-the-principle-of-relativity.txt",
    },
    {
        "seq": 17,
        "slug": "genetic-and-coordinate-division-and-divisibility",
        "title": "7. Genetic and Coordinate Division and Divisibility",
        "kind": "chapter",
        "start_line": 1497,
        "file": "raw/017-genetic-and-coordinate-division-and-divisibility.txt",
    },
    {
        "seq": 18,
        "slug": "the-problem-of-possibility",
        "title": "8. The Problem of Possibility",
        "kind": "chapter",
        "start_line": 1848,
        "file": "raw/018-the-problem-of-possibility.txt",
    },
    {
        "seq": 19,
        "slug": "the-algebra-of-negative-prehension",
        "title": "9. The Algebra of Negative Prehension",
        "kind": "chapter",
        "start_line": 2168,
        "file": "raw/019-the-algebra-of-negative-prehension.txt",
    },
    {
        "seq": 20,
        "slug": "the-nature-of-naturalism",
        "title": "10. The Nature of Naturalism",
        "kind": "chapter",
        "start_line": 2383,
        "file": "raw/020-the-nature-of-naturalism.txt",
    },
    {
        "seq": 21,
        "slug": "synoptic-pluralism-and-the-problem-of-whiteheadian-theology",
        "title": "11. Synoptic Pluralism and the Problem of Whiteheadian Theology",
        "kind": "chapter",
        "start_line": 2706,
        "file": "raw/021-synoptic-pluralism-and-the-problem-of-whiteheadian-theology.txt",
    },
    {
        "seq": 22,
        "slug": "possibility-and-god",
        "title": "12. Possibility and God",
        "kind": "chapter",
        "start_line": 2923,
        "file": "raw/022-possibility-and-god.txt",
    },
    {
        "seq": 23,
        "slug": "gods-mortal-soul",
        "title": "13. God's Mortal Soul",
        "kind": "chapter",
        "start_line": 3176,
        "file": "raw/023-gods-mortal-soul.txt",
    },
    {
        "seq": 90,
        "slug": "notes",
        "title": "Notes",
        "kind": "back-matter",
        "start_line": 3434,
        "file": "raw/090-notes.txt",
    },
    {
        "seq": 91,
        "slug": "index",
        "title": "Index",
        "kind": "back-matter",
        "start_line": 5062,
        "file": "raw/091-index.txt",
    },
]


def yaml_quote(value: object) -> str:
    if value is None:
        return "null"
    return '"' + str(value).replace("\\", "\\\\").replace('"', '\\"') + '"'


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

    for index, section in enumerate(SECTIONS):
        start = int(section["start_line"])
        end = (
            int(SECTIONS[index + 1]["start_line"]) - 1
            if index + 1 < len(SECTIONS)
            else len(lines)
        )
        content = "\n".join(lines[start - 1 : end]).strip() + "\n"
        out_path = SOURCE_DIR / str(section["file"])
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(content, encoding="utf-8")

        rendered_sections.append(
            {
                **section,
                "end_line": end,
                "line_count": end - start + 1,
                "printed_page_start": None,
            }
        )

    section_lines = [
        "book:",
        '  title: "The Quantum of Explanation: Whitehead\'s Radical Empiricism"',
        '  author: "Randall E. Auxier and Gary L. Herstein"',
        f"  source_text_witness: {yaml_quote(TXT_WITNESS.relative_to(ROOT).as_posix())}",
        f"  extracted_full_text: {yaml_quote(FULL_PATH.relative_to(SOURCE_DIR).as_posix())}",
        "sections:",
    ]

    for section in rendered_sections:
        section_lines.extend(
            [
                f'  - seq: {section["seq"]}',
                f'    slug: {yaml_quote(section["slug"])}',
                f'    title: {yaml_quote(section["title"])}',
                f'    kind: {yaml_quote(section["kind"])}',
                f'    file: {yaml_quote(section["file"])}',
                f'    start_line: {section["start_line"]}',
                f'    end_line: {section["end_line"]}',
                f'    line_count: {section["line_count"]}',
                f'    printed_page_start: {yaml_quote(section["printed_page_start"])}',
            ]
        )

    SECTIONS_PATH.write_text("\n".join(section_lines) + "\n", encoding="utf-8")


def main() -> None:
    split_sections(load_witness())


if __name__ == "__main__":
    main()
