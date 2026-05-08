#!/usr/bin/env python3

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TXT_WITNESS = ROOT / (
    "sources/modern/incoming/books/Incomplete Nature_ How Mind Eme - Deacon W_.txt"
)
SOURCE_DIR = ROOT / "sources/modern/deacon-incomplete-nature/source"
FULL_PATH = SOURCE_DIR / "full/incomplete-nature.txt"
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
        "slug": "acknowledgments",
        "title": "Acknowledgments",
        "kind": "front-matter",
        "printed_page_start": None,
        "start_line": 581,
        "file": "raw/001-acknowledgments.txt",
    },
    {
        "seq": 10,
        "slug": "absence",
        "title": "0. Absence",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 599,
        "file": "raw/010-absence.txt",
    },
    {
        "seq": 11,
        "slug": "w-holes",
        "title": "1. (W)holes",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 745,
        "file": "raw/011-w-holes.txt",
    },
    {
        "seq": 12,
        "slug": "homunculi",
        "title": "2. Homunculi",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 969,
        "file": "raw/012-homunculi.txt",
    },
    {
        "seq": 13,
        "slug": "golems",
        "title": "3. Golems",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 1277,
        "file": "raw/013-golems.txt",
    },
    {
        "seq": 14,
        "slug": "teleonomy",
        "title": "4. Teleonomy",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 1519,
        "file": "raw/014-teleonomy.txt",
    },
    {
        "seq": 15,
        "slug": "emergence",
        "title": "5. Emergence",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 1801,
        "file": "raw/015-emergence.txt",
    },
    {
        "seq": 16,
        "slug": "constraint",
        "title": "6. Constraint",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 2107,
        "file": "raw/016-constraint.txt",
    },
    {
        "seq": 17,
        "slug": "homeodynamics",
        "title": "7. Homeodynamics",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 2273,
        "file": "raw/017-homeodynamics.txt",
    },
    {
        "seq": 18,
        "slug": "morphodynamics",
        "title": "8. Morphodynamics",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 2483,
        "file": "raw/018-morphodynamics.txt",
    },
    {
        "seq": 19,
        "slug": "teleodynamics",
        "title": "9. Teleodynamics",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 2721,
        "file": "raw/019-teleodynamics.txt",
    },
    {
        "seq": 20,
        "slug": "autogenesis",
        "title": "10. Autogenesis",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 2935,
        "file": "raw/020-autogenesis.txt",
    },
    {
        "seq": 21,
        "slug": "work",
        "title": "11. Work",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 3243,
        "file": "raw/021-work.txt",
    },
    {
        "seq": 22,
        "slug": "information",
        "title": "12. Information",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 3547,
        "file": "raw/022-information.txt",
    },
    {
        "seq": 23,
        "slug": "significance",
        "title": "13. Significance",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 3757,
        "file": "raw/023-significance.txt",
    },
    {
        "seq": 24,
        "slug": "evolution",
        "title": "14. Evolution",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 3987,
        "file": "raw/024-evolution.txt",
    },
    {
        "seq": 25,
        "slug": "self",
        "title": "15. Self",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 4301,
        "file": "raw/025-self.txt",
    },
    {
        "seq": 26,
        "slug": "sentience",
        "title": "16. Sentience",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 4485,
        "file": "raw/026-sentience.txt",
    },
    {
        "seq": 27,
        "slug": "consciousness",
        "title": "17. Consciousness",
        "kind": "chapter",
        "printed_page_start": None,
        "start_line": 4671,
        "file": "raw/027-consciousness.txt",
    },
    {
        "seq": 28,
        "slug": "epilogue",
        "title": "Epilogue",
        "kind": "back-matter",
        "printed_page_start": None,
        "start_line": 4893,
        "file": "raw/028-epilogue.txt",
    },
    {
        "seq": 50,
        "slug": "glossary",
        "title": "Glossary",
        "kind": "back-matter",
        "printed_page_start": None,
        "start_line": 4959,
        "file": "raw/050-glossary.txt",
    },
    {
        "seq": 51,
        "slug": "notes",
        "title": "Notes",
        "kind": "back-matter",
        "printed_page_start": None,
        "start_line": 5075,
        "file": "raw/051-notes.txt",
    },
    {
        "seq": 52,
        "slug": "references",
        "title": "References",
        "kind": "back-matter",
        "printed_page_start": None,
        "start_line": 5499,
        "file": "raw/052-references.txt",
    },
    {
        "seq": 53,
        "slug": "index",
        "title": "Index",
        "kind": "back-matter",
        "printed_page_start": None,
        "start_line": 5951,
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
        '  title: "Incomplete Nature: How Mind Emerged from Matter"',
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
