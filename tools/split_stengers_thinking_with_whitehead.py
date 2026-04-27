#!/usr/bin/env python3

from __future__ import annotations

import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PDF_PATH = ROOT / (
    "sources/modern/incoming/books/"
    "Thinking with Whitehead a free and wild creation of concepts -- Isabelle Stengers.pdf"
)
SOURCE_DIR = ROOT / "sources/modern/stengers-thinking-with-whitehead/source"
FULL_PATH = SOURCE_DIR / "full/thinking-with-whitehead.txt"
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
        "slug": "foreword-what-is-given-in-experience",
        "title": "Foreword: What Is Given in Experience?",
        "kind": "foreword",
        "printed_page_start": "ix",
        "start_line": 133,
        "file": "raw/001-foreword-what-is-given-in-experience.txt",
    },
    {
        "seq": 2,
        "slug": "abbreviations-and-references",
        "title": "Abbreviations and References",
        "kind": "front-matter",
        "printed_page_start": "xvii",
        "start_line": 436,
        "file": "raw/002-abbreviations-and-references.txt",
    },
    {
        "seq": 10,
        "slug": "introduction-whitehead-today",
        "title": "Introduction: Whitehead Today?",
        "kind": "introduction",
        "printed_page_start": "1",
        "start_line": 529,
        "file": "raw/010-introduction-whitehead-today.txt",
    },
    {
        "seq": 20,
        "slug": "part-one-from-the-philosophy-of-nature-to-metaphysics",
        "title": "Part One: From the Philosophy of Nature to Metaphysics",
        "kind": "part",
        "printed_page_start": None,
        "start_line": 1759,
        "file": "raw/020-part-one-from-the-philosophy-of-nature-to-metaphysics.txt",
    },
    {
        "seq": 21,
        "slug": "the-mathematician-and-the-sunset",
        "title": "1. The Mathematician and the Sunset",
        "kind": "chapter",
        "printed_page_start": "31",
        "start_line": 1770,
        "file": "raw/021-the-mathematician-and-the-sunset.txt",
    },
    {
        "seq": 22,
        "slug": "events-and-passage",
        "title": "2. Events and Passage",
        "kind": "chapter",
        "printed_page_start": "42",
        "start_line": 2266,
        "file": "raw/022-events-and-passage.txt",
    },
    {
        "seq": 23,
        "slug": "the-foothold-of-the-mind",
        "title": "3. The Foothold of the Mind",
        "kind": "chapter",
        "printed_page_start": "58",
        "start_line": 2973,
        "file": "raw/023-the-foothold-of-the-mind.txt",
    },
    {
        "seq": 24,
        "slug": "there-it-is-again",
        "title": "4. There It Is Again",
        "kind": "chapter",
        "printed_page_start": "73",
        "start_line": 3643,
        "file": "raw/024-there-it-is-again.txt",
    },
    {
        "seq": 25,
        "slug": "attention-to-objects",
        "title": "5. Attention to Objects",
        "kind": "chapter",
        "printed_page_start": "85",
        "start_line": 4173,
        "file": "raw/025-attention-to-objects.txt",
    },
    {
        "seq": 26,
        "slug": "the-ingression-of-scientific-objects",
        "title": "6. The Ingression of Scientific Objects",
        "kind": "chapter",
        "printed_page_start": "94",
        "start_line": 4560,
        "file": "raw/026-the-ingression-of-scientific-objects.txt",
    },
    {
        "seq": 27,
        "slug": "interlude-a-pragmatics-of-concepts",
        "title": "7. Interlude: A Pragmatics of Concepts",
        "kind": "chapter",
        "printed_page_start": "105",
        "start_line": 5024,
        "file": "raw/027-interlude-a-pragmatics-of-concepts.txt",
    },
    {
        "seq": 28,
        "slug": "science-and-the-modern-world-a-strange-book",
        "title": "8. Science and the Modern World: A Strange Book",
        "kind": "chapter",
        "printed_page_start": "114",
        "start_line": 5431,
        "file": "raw/028-science-and-the-modern-world-a-strange-book.txt",
    },
    {
        "seq": 29,
        "slug": "a-new-epoch",
        "title": "9. A New Epoch?",
        "kind": "chapter",
        "printed_page_start": "123",
        "start_line": 5824,
        "file": "raw/029-a-new-epoch.txt",
    },
    {
        "seq": 30,
        "slug": "from-the-concept-of-nature-to-the-order-of-nature",
        "title": "10. From the Concept of Nature to the Order of Nature",
        "kind": "chapter",
        "printed_page_start": "142",
        "start_line": 6680,
        "file": "raw/030-from-the-concept-of-nature-to-the-order-of-nature.txt",
    },
    {
        "seq": 31,
        "slug": "scientific-objects-and-the-test-of-the-organism",
        "title": "11. Scientific Objects and the Test of the Organism",
        "kind": "chapter",
        "printed_page_start": "165",
        "start_line": 7718,
        "file": "raw/031-scientific-objects-and-the-test-of-the-organism.txt",
    },
    {
        "seq": 32,
        "slug": "the-event-from-its-own-standpoint",
        "title": "12. The Event from Its Own Standpoint?",
        "kind": "chapter",
        "printed_page_start": "185",
        "start_line": 8620,
        "file": "raw/032-the-event-from-its-own-standpoint.txt",
    },
    {
        "seq": 33,
        "slug": "entry-into-metaphysics",
        "title": "13. Entry into Metaphysics",
        "kind": "chapter",
        "printed_page_start": "201",
        "start_line": 9321,
        "file": "raw/033-entry-into-metaphysics.txt",
    },
    {
        "seq": 34,
        "slug": "the-great-refusal",
        "title": "14. The Great Refusal",
        "kind": "chapter",
        "printed_page_start": "218",
        "start_line": 10071,
        "file": "raw/034-the-great-refusal.txt",
    },
    {
        "seq": 40,
        "slug": "part-two-cosmology",
        "title": "Part Two: Cosmology",
        "kind": "part",
        "printed_page_start": None,
        "start_line": 10652,
        "file": "raw/040-part-two-cosmology.txt",
    },
    {
        "seq": 41,
        "slug": "hic-circuli-hic-saltus",
        "title": "15. Hic Circuli, Hic Saltus",
        "kind": "chapter",
        "printed_page_start": "233",
        "start_line": 10663,
        "file": "raw/041-hic-circuli-hic-saltus.txt",
    },
    {
        "seq": 42,
        "slug": "thinking-under-the-constraint-of-creativity",
        "title": "16. Thinking under the Constraint of Creativity",
        "kind": "chapter",
        "printed_page_start": "254",
        "start_line": 11613,
        "file": "raw/042-thinking-under-the-constraint-of-creativity.txt",
    },
    {
        "seq": 43,
        "slug": "the-risks-of-speculative-interpretation",
        "title": "17. The Risks of Speculative Interpretation",
        "kind": "chapter",
        "printed_page_start": "277",
        "start_line": 12622,
        "file": "raw/043-the-risks-of-speculative-interpretation.txt",
    },
    {
        "seq": 44,
        "slug": "feeling-ones-world",
        "title": "18. Feeling One's World",
        "kind": "chapter",
        "printed_page_start": "294",
        "start_line": 13373,
        "file": "raw/044-feeling-ones-world.txt",
    },
    {
        "seq": 45,
        "slug": "justifying-life",
        "title": "19. Justifying Life?",
        "kind": "chapter",
        "printed_page_start": "312",
        "start_line": 14178,
        "file": "raw/045-justifying-life.txt",
    },
    {
        "seq": 46,
        "slug": "the-adventure-of-the-senses",
        "title": "20. The Adventure of the Senses",
        "kind": "chapter",
        "printed_page_start": "336",
        "start_line": 15262,
        "file": "raw/046-the-adventure-of-the-senses.txt",
    },
    {
        "seq": 47,
        "slug": "actuality-between-physics-and-the-divine",
        "title": "21. Actuality between Physics and the Divine",
        "kind": "chapter",
        "printed_page_start": "364",
        "start_line": 16540,
        "file": "raw/047-actuality-between-physics-and-the-divine.txt",
    },
    {
        "seq": 48,
        "slug": "and-they-became-souls",
        "title": "22. And They Became Souls",
        "kind": "chapter",
        "printed_page_start": "392",
        "start_line": 17790,
        "file": "raw/048-and-they-became-souls.txt",
    },
    {
        "seq": 49,
        "slug": "modes-of-existence-modes-of-thought",
        "title": "23. Modes of Existence, Modes of Thought",
        "kind": "chapter",
        "printed_page_start": "423",
        "start_line": 19206,
        "file": "raw/049-modes-of-existence-modes-of-thought.txt",
    },
    {
        "seq": 50,
        "slug": "god-and-the-world",
        "title": "24. God and the World",
        "kind": "chapter",
        "printed_page_start": "449",
        "start_line": 20397,
        "file": "raw/050-god-and-the-world.txt",
    },
    {
        "seq": 51,
        "slug": "an-adventure-of-ideas",
        "title": "25. An Adventure of Ideas",
        "kind": "chapter",
        "printed_page_start": "479",
        "start_line": 21753,
        "file": "raw/051-an-adventure-of-ideas.txt",
    },
    {
        "seq": 60,
        "slug": "conclusion-word-of-a-dragon-word-of-trance",
        "title": "Conclusion: Word of a Dragon, Word of Trance",
        "kind": "conclusion",
        "printed_page_start": "503",
        "start_line": 22789,
        "file": "raw/060-conclusion-word-of-a-dragon-word-of-trance.txt",
    },
    {
        "seq": 61,
        "slug": "index",
        "title": "Index",
        "kind": "back-matter",
        "printed_page_start": "521",
        "start_line": 23548,
        "file": "raw/061-index.txt",
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
        '  title: "Thinking with Whitehead: A Free and Wild Creation of Concepts"',
        '  author: "Isabelle Stengers"',
        '  translator: "Michael Chase"',
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
