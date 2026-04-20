#!/usr/bin/env python3

from __future__ import annotations

import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PDF_PATH = ROOT / (
    "sources/modern/incoming/books/"
    "An Artificial History of Natural Intelligence _ Thinking -- David W_ Bates.pdf"
)
SOURCE_DIR = ROOT / "sources/modern/bates-artificial-history/source"
FULL_PATH = SOURCE_DIR / "full/artificial-history-of-natural-intelligence.txt"
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
        "slug": "autonomy-and-automaticity",
        "title": "1. Autonomy and Automaticity: On the Contemporary Question of Intelligence",
        "kind": "chapter",
        "printed_page_start": "2",
        "start_line": 155,
        "file": "raw/001-autonomy-and-automaticity.txt",
    },
    {
        "seq": 2,
        "slug": "integration-and-interruption",
        "title": "2. Integration and Interruption: The Cartesian Thinking Machine",
        "kind": "chapter",
        "printed_page_start": "16",
        "start_line": 655,
        "file": "raw/002-integration-and-interruption.txt",
    },
    {
        "seq": 3,
        "slug": "spiritual-automata",
        "title": "3. Spiritual Automata: From Hobbes to Spinoza",
        "kind": "chapter",
        "printed_page_start": "33",
        "start_line": 1380,
        "file": "raw/003-spiritual-automata.txt",
    },
    {
        "seq": 4,
        "slug": "spiritual-automata-revisited",
        "title": "4. Spiritual Automata Revisited: Leibniz and Automatic Harmony",
        "kind": "chapter",
        "printed_page_start": "49",
        "start_line": 2064,
        "file": "raw/004-spiritual-automata-revisited.txt",
    },
    {
        "seq": 5,
        "slug": "humes-enlightened-nervous-system",
        "title": "5. Hume's Enlightened Nervous System",
        "kind": "chapter",
        "printed_page_start": "65",
        "start_line": 2744,
        "file": "raw/005-humes-enlightened-nervous-system.txt",
    },
    {
        "seq": 6,
        "slug": "machinery-of-cognition-first-critique",
        "title": "6. The Machinery of Cognition in the First Critique",
        "kind": "chapter",
        "printed_page_start": "80",
        "start_line": 3280,
        "file": "raw/006-machinery-of-cognition-first-critique.txt",
    },
    {
        "seq": 7,
        "slug": "pathology-of-spontaneity",
        "title": "7. The Pathology of Spontaneity: The Critique of Judgment and Beyond",
        "kind": "chapter",
        "printed_page_start": "95",
        "start_line": 3937,
        "file": "raw/007-pathology-of-spontaneity.txt",
    },
    {
        "seq": 8,
        "slug": "babbage-lovelace-and-the-unexpected",
        "title": "8. Babbage, Lovelace, and the Unexpected",
        "kind": "chapter",
        "printed_page_start": "108",
        "start_line": 4415,
        "file": "raw/008-babbage-lovelace-and-the-unexpected.txt",
    },
    {
        "seq": 9,
        "slug": "psychophysics",
        "title": "9. Psychophysics: On the Physio-Technology of Automatic Reason",
        "kind": "chapter",
        "printed_page_start": "116",
        "start_line": 4747,
        "file": "raw/009-psychophysics.txt",
    },
    {
        "seq": 10,
        "slug": "singularities-of-the-thermodynamic-mind",
        "title": "10. Singularities of the Thermodynamic Mind",
        "kind": "chapter",
        "printed_page_start": "125",
        "start_line": 5128,
        "file": "raw/010-singularities-of-the-thermodynamic-mind.txt",
    },
    {
        "seq": 11,
        "slug": "the-dynamic-brain",
        "title": "11. The Dynamic Brain",
        "kind": "chapter",
        "printed_page_start": "131",
        "start_line": 5371,
        "file": "raw/011-the-dynamic-brain.txt",
    },
    {
        "seq": 12,
        "slug": "prehistoric-humans-and-the-technical-evolution-of-reason",
        "title": "12. Prehistoric Humans and the Technical Evolution of Reason",
        "kind": "chapter",
        "printed_page_start": "141",
        "start_line": 5733,
        "file": "raw/012-prehistoric-humans-and-the-technical-evolution-of-reason.txt",
    },
    {
        "seq": 13,
        "slug": "creative-life-and-the-emergence-of-technical-intelligence",
        "title": "13. Creative Life and the Emergence of Technical Intelligence",
        "kind": "chapter",
        "printed_page_start": "152",
        "start_line": 6175,
        "file": "raw/013-creative-life-and-the-emergence-of-technical-intelligence.txt",
    },
    {
        "seq": 14,
        "slug": "technology-is-not-the-liberation-of-the-human-but-its-transformation",
        "title": "14. Technology Is Not the Liberation of the Human but Its Transformation . . .",
        "kind": "chapter",
        "printed_page_start": "162",
        "start_line": 6525,
        "file": "raw/014-technology-is-not-the-liberation-of-the-human-but-its-transformation.txt",
    },
    {
        "seq": 15,
        "slug": "techniques-of-insight",
        "title": "15. Techniques of Insight",
        "kind": "chapter",
        "printed_page_start": "164",
        "start_line": 6555,
        "file": "raw/015-techniques-of-insight.txt",
    },
    {
        "seq": 16,
        "slug": "brains-in-crisis-psychic-emergencies",
        "title": "16. Brains in Crisis, Psychic Emergencies",
        "kind": "chapter",
        "printed_page_start": "181",
        "start_line": 7293,
        "file": "raw/016-brains-in-crisis-psychic-emergencies.txt",
    },
    {
        "seq": 17,
        "slug": "bio-technicity-in-von-uexkuell",
        "title": "17. Bio-Technicity in Von Uexkull",
        "kind": "chapter",
        "printed_page_start": "188",
        "start_line": 7567,
        "file": "raw/017-bio-technicity-in-von-uexkuell.txt",
    },
    {
        "seq": 18,
        "slug": "lotka-on-the-evolution-of-technical-humanity",
        "title": "18. Lotka on the Evolution of Technical Humanity",
        "kind": "chapter",
        "printed_page_start": "194",
        "start_line": 7812,
        "file": "raw/018-lotka-on-the-evolution-of-technical-humanity.txt",
    },
    {
        "seq": 19,
        "slug": "thinking-machines",
        "title": "19. Thinking Machines",
        "kind": "chapter",
        "printed_page_start": "201",
        "start_line": 8111,
        "file": "raw/019-thinking-machines.txt",
    },
    {
        "seq": 20,
        "slug": "a-typology-of-machines",
        "title": "20. A Typology of Machines",
        "kind": "chapter",
        "printed_page_start": "205",
        "start_line": 8272,
        "file": "raw/020-a-typology-of-machines.txt",
    },
    {
        "seq": 21,
        "slug": "philosophical-anthropology-the-human-as-technical-exteriorization",
        "title": "21. Philosophical Anthropology: The Human as Technical Exteriorization",
        "kind": "chapter",
        "printed_page_start": "209",
        "start_line": 8430,
        "file": "raw/021-philosophical-anthropology-the-human-as-technical-exteriorization.txt",
    },
    {
        "seq": 22,
        "slug": "wittgenstein-on-the-immateriality-of-thinking",
        "title": "22. Wittgenstein on the Immateriality of Thinking",
        "kind": "chapter",
        "printed_page_start": "228",
        "start_line": 9210,
        "file": "raw/022-wittgenstein-on-the-immateriality-of-thinking.txt",
    },
    {
        "seq": 23,
        "slug": "cybernetic-machines-and-organisms",
        "title": "23. Cybernetic Machines and Organisms",
        "kind": "chapter",
        "printed_page_start": "234",
        "start_line": 9441,
        "file": "raw/023-cybernetic-machines-and-organisms.txt",
    },
    {
        "seq": 24,
        "slug": "automatic-plasticity-and-the-pathological-machine",
        "title": "24. Automatic Plasticity and the Pathological Machine",
        "kind": "chapter",
        "printed_page_start": "245",
        "start_line": 9932,
        "file": "raw/024-automatic-plasticity-and-the-pathological-machine.txt",
    },
    {
        "seq": 25,
        "slug": "turing-and-the-spirit-of-error",
        "title": "25. Turing and the Spirit of Error",
        "kind": "chapter",
        "printed_page_start": "260",
        "start_line": 10576,
        "file": "raw/025-turing-and-the-spirit-of-error.txt",
    },
    {
        "seq": 26,
        "slug": "epistemologies-of-the-exosomatic",
        "title": "26. Epistemologies of the Exosomatic",
        "kind": "chapter",
        "printed_page_start": "289",
        "start_line": 11893,
        "file": "raw/026-epistemologies-of-the-exosomatic.txt",
    },
    {
        "seq": 27,
        "slug": "leroi-gourhan-on-the-technical-origin-of-the-exteriorized-mind",
        "title": "27. Leroi-Gourhan on the Technical Origin of the Exteriorized Mind",
        "kind": "chapter",
        "printed_page_start": "311",
        "start_line": 12855,
        "file": "raw/027-leroi-gourhan-on-the-technical-origin-of-the-exteriorized-mind.txt",
    },
    {
        "seq": 28,
        "slug": "technogenesis-in-the-networked-age",
        "title": "28. Technogenesis in the Networked Age",
        "kind": "chapter",
        "printed_page_start": "328",
        "start_line": 13573,
        "file": "raw/028-technogenesis-in-the-networked-age.txt",
    },
    {
        "seq": 29,
        "slug": "failures-of-anticipation",
        "title": "29. Failures of Anticipation: The Future of Intelligence in the Era of Machine Learning",
        "kind": "chapter",
        "printed_page_start": "345",
        "start_line": 14317,
        "file": "raw/029-failures-of-anticipation.txt",
    },
    {
        "seq": 50,
        "slug": "acknowledgments",
        "title": "Acknowledgments",
        "kind": "acknowledgments",
        "printed_page_start": "353",
        "start_line": 14657,
        "file": "raw/050-acknowledgments.txt",
    },
    {
        "seq": 51,
        "slug": "notes",
        "title": "Notes",
        "kind": "back-matter",
        "printed_page_start": "355",
        "start_line": 14692,
        "file": "raw/051-notes.txt",
    },
    {
        "seq": 52,
        "slug": "index",
        "title": "Index",
        "kind": "back-matter",
        "printed_page_start": "391",
        "start_line": 16623,
        "file": "raw/052-index.txt",
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
        "book:",
        '  title: "An Artificial History of Natural Intelligence"',
        '  author: "David W. Bates"',
        (
            "  source_pdf: "
            '"sources/modern/incoming/books/An Artificial History of Natural Intelligence _ Thinking -- David W_ Bates.pdf"'
        ),
        '  extracted_full_text: "source/full/artificial-history-of-natural-intelligence.txt"',
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
