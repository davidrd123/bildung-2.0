#!/usr/bin/env python3

from __future__ import annotations

import subprocess
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PDF_AUTHORITY = ROOT / (
    "sources/modern/incoming/books/peirce/"
    "The Essential Peirce, Volume 1 Selected Philosophical.pdf"
)
SOURCE_DIR = ROOT / "sources/modern/peirce-essential-peirce-volume-1/source"
FULL_PATH = SOURCE_DIR / "full/essential-peirce-volume-1.txt"
RAW_DIR = SOURCE_DIR / "raw"
SECTIONS_PATH = SOURCE_DIR / "sections.yaml"


@dataclass(frozen=True)
class Section:
    seq: int
    slug: str
    title: str
    kind: str
    pdf_start: int
    pdf_end: int
    printed_start: str | None
    printed_end: str | None

    @property
    def filename(self) -> str:
        return f"{self.seq:03d}-{self.slug}.txt"


SECTIONS = [
    Section(0, "title-pages-and-publisher-matter", "Title pages, publisher matter, and contents", "front-matter", 1, 8, None, None),
    Section(1, "chronology", "Chronology", "front-matter", 9, 10, "ix", "x"),
    Section(2, "foreword", "Foreword", "front-matter", 11, 17, "xi", "xvii"),
    Section(3, "introduction", "Introduction", "front-matter", 19, 41, "xix", "xli"),
    Section(10, "on-a-new-list-of-categories-1867", "1. On a New List of Categories (1867)", "essay", 45, 54, "1", "10"),
    Section(11, "questions-concerning-certain-faculties-claimed-for-man-1868", "2. Questions Concerning Certain Faculties Claimed for Man (1868)", "essay", 55, 71, "11", "27"),
    Section(12, "some-consequences-of-four-incapacities-1868", "3. Some Consequences of Four Incapacities (1868)", "essay", 72, 99, "28", "55"),
    Section(13, "grounds-of-validity-of-the-laws-of-logic-1869", "4. Grounds of Validity of the Laws of Logic (1869)", "essay", 100, 126, "56", "82"),
    Section(14, "frasers-the-works-of-george-berkeley-1871", "5. Fraser's The Works of George Berkeley (1871)", "essay", 127, 149, "83", "105"),
    Section(15, "on-a-new-class-of-observations-suggested-by-the-principles-of-logic-1877", "6. On a New Class of Observations, suggested by the principles of Logic (1877)", "essay", 150, 152, "106", "108"),
    Section(16, "the-fixation-of-belief-1877", "7. The Fixation of Belief (1877)", "essay", 153, 167, "109", "123"),
    Section(17, "how-to-make-our-ideas-clear-1878", "8. How to Make Our Ideas Clear (1878)", "essay", 168, 185, "124", "141"),
    Section(18, "the-doctrine-of-chances-1878", "9. The Doctrine of Chances (1878)", "essay", 186, 198, "142", "154"),
    Section(19, "the-probability-of-induction-1878", "10. The Probability of Induction (1878)", "essay", 199, 213, "155", "169"),
    Section(20, "the-order-of-nature-1878", "11. The Order of Nature (1878)", "essay", 214, 229, "170", "185"),
    Section(21, "deduction-induction-and-hypothesis-1878", "12. Deduction, Induction, and Hypothesis (1878)", "essay", 230, 243, "186", "199"),
    Section(22, "from-on-the-algebra-of-logic-1880", "13. [from] On the Algebra of Logic (1880)", "essay", 244, 253, "200", "209"),
    Section(23, "introductory-lecture-on-the-study-of-logic-1882", "14. Introductory Lecture on the Study of Logic (1882)", "essay", 254, 258, "210", "214"),
    Section(24, "design-and-chance-1883-84", "15. Design and Chance (1883-84)", "essay", 259, 268, "215", "224"),
    Section(25, "from-on-the-algebra-of-logic-a-contribution-to-the-philosophy-of-notation-1885", "16. [from] On the Algebra of Logic: A Contribution to the Philosophy of Notation (1885)", "essay", 269, 272, "225", "228"),
    Section(26, "an-american-plato-review-of-royces-religious-aspect-of-philosophy-1885", "17. An American Plato: Review of Royce's Religious Aspect of Philosophy (1885)", "essay", 273, 285, "229", "241"),
    Section(27, "one-two-three-kantian-categories-1886", "18. One, Two, Three: Kantian Categories (1886)", "essay", 286, 288, "242", "244"),
    Section(28, "a-guess-at-the-riddle-1887-88", "19. A Guess at the Riddle (1887-88)", "essay", 289, 323, "245", "279"),
    Section(29, "trichotomie-1888", "20. Trichotomie (1888)", "essay", 324, 328, "280", "284"),
    Section(30, "the-architecture-of-theories-1891", "21. The Architecture of Theories (1891)", "essay", 329, 341, "285", "297"),
    Section(31, "the-doctrine-of-necessity-examined-1892", "22. The Doctrine of Necessity Examined (1892)", "essay", 342, 355, "298", "311"),
    Section(32, "the-law-of-mind-1892", "23. The Law of Mind (1892)", "essay", 356, 377, "312", "333"),
    Section(33, "mans-glassy-essence-1892", "24. Man's Glassy Essence (1892)", "essay", 378, 395, "334", "351"),
    Section(34, "evolutionary-love-1893", "25. Evolutionary Love (1893)", "essay", 396, 416, "352", "372"),
    Section(50, "notes", "Notes", "back-matter", 417, 432, "373", "388"),
    Section(51, "index", "Index", "back-matter", 433, 443, "389", "399"),
]


ROMAN_VALUES = [
    (1000, "m"),
    (900, "cm"),
    (500, "d"),
    (400, "cd"),
    (100, "c"),
    (90, "xc"),
    (50, "l"),
    (40, "xl"),
    (10, "x"),
    (9, "ix"),
    (5, "v"),
    (4, "iv"),
    (1, "i"),
]


def to_roman(number: int) -> str:
    out: list[str] = []
    for value, numeral in ROMAN_VALUES:
        while number >= value:
            out.append(numeral)
            number -= value
    return "".join(out)


def page_marker(pdf_page: int) -> str:
    if 9 <= pdf_page <= 41:
        return f"[page {to_roman(pdf_page)}]"
    if pdf_page >= 45:
        return f"[page {pdf_page - 44}]"
    return f"[pdf page {pdf_page:03d}]"


def extract_pdf_page(pdf_page: int) -> str:
    result = subprocess.run(
        [
            "pdftotext",
            "-raw",
            "-f",
            str(pdf_page),
            "-l",
            str(pdf_page),
            str(PDF_AUTHORITY),
            "-",
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.replace("\x0c", "").replace("\x00", "").strip()


def extract_section(section: Section) -> str:
    pages: list[str] = []
    for pdf_page in range(section.pdf_start, section.pdf_end + 1):
        text = extract_pdf_page(pdf_page)
        if not text:
            continue
        pages.append(f"{page_marker(pdf_page)}\n\n{text.strip()}")
    return "\n\n".join(pages).strip() + "\n"


def write_sections() -> None:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    FULL_PATH.parent.mkdir(parents=True, exist_ok=True)
    full_parts: list[str] = []

    for section in SECTIONS:
        text = extract_section(section)
        out_path = RAW_DIR / section.filename
        out_path.write_text(text, encoding="utf-8")
        full_parts.append(text)

    FULL_PATH.write_text("\n\n".join(part.strip() for part in full_parts) + "\n", encoding="utf-8")


def write_sections_yaml() -> None:
    lines = [
        "book:",
        '  title: "The Essential Peirce, Volume 1: Selected Philosophical Writings (1867-1893)"',
        '  author: "Charles S. Peirce"',
        '  editors: "Nathan Houser and Christian Kloesel"',
        f'  source_pdf: "{PDF_AUTHORITY.relative_to(ROOT).as_posix()}"',
        f'  extracted_full_text: "{FULL_PATH.relative_to(SOURCE_DIR).as_posix()}"',
        "  extraction_mode: \"pdftotext -raw\"",
        "  skipped_pdf_pages:",
        "    - 18",
        "    - 42",
        "    - 43",
        "    - 44",
        "sections:",
    ]
    for section in SECTIONS:
        printed_start = "null" if section.printed_start is None else f'"{section.printed_start}"'
        printed_end = "null" if section.printed_end is None else f'"{section.printed_end}"'
        lines.extend(
            [
                f"  - seq: {section.seq}",
                f'    slug: "{section.slug}"',
                f'    title: "{section.title}"',
                f'    kind: "{section.kind}"',
                f'    file: "raw/{section.filename}"',
                f"    pdf_page_start: {section.pdf_start}",
                f"    pdf_page_end: {section.pdf_end}",
                f"    printed_page_start: {printed_start}",
                f"    printed_page_end: {printed_end}",
            ]
        )
    SECTIONS_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    if not PDF_AUTHORITY.exists():
        raise SystemExit(f"Missing authority PDF: {PDF_AUTHORITY}")
    write_sections()
    write_sections_yaml()


if __name__ == "__main__":
    main()
