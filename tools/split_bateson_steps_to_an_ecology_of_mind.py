#!/usr/bin/env python3

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TXT_WITNESS = ROOT / (
    "sources/modern/incoming/books/Steps to an Ecology of Mind - Gregory Bateson.txt"
)
SOURCE_DIR = ROOT / "sources/modern/bateson-steps-to-an-ecology-of-mind/source"
FULL_PATH = SOURCE_DIR / "full/steps-to-an-ecology-of-mind.txt"
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
        "slug": "preface-1987",
        "title": "Preface, 1987",
        "kind": "front-matter",
        "printed_page_start": None,
        "start_line": 140,
        "file": "raw/001-preface-1987.txt",
    },
    {
        "seq": 2,
        "slug": "preface-1971",
        "title": "Preface, 1971",
        "kind": "front-matter",
        "printed_page_start": None,
        "start_line": 169,
        "file": "raw/002-preface-1971.txt",
    },
    {
        "seq": 3,
        "slug": "foreword-1999",
        "title": "Foreword by Mary Catherine Bateson, 1999",
        "kind": "front-matter",
        "printed_page_start": None,
        "start_line": 204,
        "file": "raw/003-foreword-1999.txt",
    },
    {
        "seq": 4,
        "slug": "foreword-1971",
        "title": "Foreword, 1971",
        "kind": "front-matter",
        "printed_page_start": None,
        "start_line": 326,
        "file": "raw/004-foreword-1971.txt",
    },
    {
        "seq": 5,
        "slug": "introduction-the-science-of-mind-and-order",
        "title": "Introduction: The Science of Mind and Order",
        "kind": "front-matter",
        "printed_page_start": None,
        "start_line": 404,
        "file": "raw/005-introduction-the-science-of-mind-and-order.txt",
    },
    {
        "seq": 10,
        "slug": "part-one-metalogues",
        "title": "Part I: Metalogues",
        "kind": "part",
        "printed_page_start": None,
        "start_line": 561,
        "file": "raw/010-part-one-metalogues.txt",
    },
    {
        "seq": 11,
        "slug": "metalogue-why-do-things-get-in-a-muddle",
        "title": "Metalogue: Why Do Things Get in a Muddle?",
        "kind": "essay",
        "printed_page_start": None,
        "start_line": 574,
        "file": "raw/011-metalogue-why-do-things-get-in-a-muddle.txt",
    },
    {
        "seq": 12,
        "slug": "metalogue-why-do-frenchmen",
        "title": "Metalogue: Why Do Frenchmen?",
        "kind": "essay",
        "printed_page_start": None,
        "start_line": 1099,
        "file": "raw/012-metalogue-why-do-frenchmen.txt",
    },
    {
        "seq": 13,
        "slug": "metalogue-about-games-and-being-serious",
        "title": "Metalogue: About Games and Being Serious",
        "kind": "essay",
        "printed_page_start": None,
        "start_line": 1516,
        "file": "raw/013-metalogue-about-games-and-being-serious.txt",
    },
    {
        "seq": 14,
        "slug": "metalogue-how-much-do-you-know",
        "title": "Metalogue: How Much Do You Know?",
        "kind": "essay",
        "printed_page_start": None,
        "start_line": 2091,
        "file": "raw/014-metalogue-how-much-do-you-know.txt",
    },
    {
        "seq": 15,
        "slug": "metalogue-why-do-things-have-outlines",
        "title": "Metalogue: Why Do Things Have Outlines?",
        "kind": "essay",
        "printed_page_start": None,
        "start_line": 2530,
        "file": "raw/015-metalogue-why-do-things-have-outlines.txt",
    },
    {
        "seq": 16,
        "slug": "metalogue-why-a-swan",
        "title": "Metalogue: Why a Swan?",
        "kind": "essay",
        "printed_page_start": None,
        "start_line": 3039,
        "file": "raw/016-metalogue-why-a-swan.txt",
    },
    {
        "seq": 17,
        "slug": "metalogue-what-is-an-instinct",
        "title": "Metalogue: What Is an Instinct?",
        "kind": "essay",
        "printed_page_start": None,
        "start_line": 3468,
        "file": "raw/017-metalogue-what-is-an-instinct.txt",
    },
    {
        "seq": 20,
        "slug": "part-two-form-and-pattern-in-anthropology",
        "title": "Part II: Form and Pattern in Anthropology",
        "kind": "part",
        "printed_page_start": None,
        "start_line": 5875,
        "file": "raw/020-part-two-form-and-pattern-in-anthropology.txt",
    },
    {
        "seq": 21,
        "slug": "culture-contact-and-schismogenesis",
        "title": "Culture Contact and Schismogenesis",
        "kind": "essay",
        "printed_page_start": None,
        "start_line": 5879,
        "file": "raw/021-culture-contact-and-schismogenesis.txt",
    },
    {
        "seq": 22,
        "slug": "experiments-in-thinking-about-observed-ethnological-material",
        "title": "Experiments in Thinking About Observed Ethnological Material",
        "kind": "essay",
        "printed_page_start": None,
        "start_line": 5982,
        "file": "raw/022-experiments-in-thinking-about-observed-ethnological-material.txt",
    },
    {
        "seq": 23,
        "slug": "morale-and-national-character",
        "title": "Morale and National Character",
        "kind": "essay",
        "printed_page_start": None,
        "start_line": 6093,
        "file": "raw/023-morale-and-national-character.txt",
    },
    {
        "seq": 24,
        "slug": "bali-the-value-system-of-a-steady-state",
        "title": "Bali: The Value System of a Steady State",
        "kind": "essay",
        "printed_page_start": None,
        "start_line": 6315,
        "file": "raw/024-bali-the-value-system-of-a-steady-state.txt",
    },
    {
        "seq": 25,
        "slug": "style-grace-and-information-in-primitive-art",
        "title": "Style, Grace, and Information in Primitive Art",
        "kind": "essay",
        "printed_page_start": None,
        "start_line": 6496,
        "file": "raw/025-style-grace-and-information-in-primitive-art.txt",
    },
    {
        "seq": 26,
        "slug": "comment-on-part-two",
        "title": "Comment on Part II",
        "kind": "comment",
        "printed_page_start": None,
        "start_line": 6926,
        "file": "raw/026-comment-on-part-two.txt",
    },
    {
        "seq": 30,
        "slug": "part-three-form-and-pathology-in-relationship",
        "title": "Part III: Form and Pathology in Relationship",
        "kind": "part",
        "printed_page_start": None,
        "start_line": 7064,
        "file": "raw/030-part-three-form-and-pathology-in-relationship.txt",
    },
    {
        "seq": 31,
        "slug": "social-planning-and-the-concept-of-deutero-learning",
        "title": "Social Planning and the Concept of Deutero-Learning",
        "kind": "essay",
        "printed_page_start": None,
        "start_line": 7068,
        "file": "raw/031-social-planning-and-the-concept-of-deutero-learning.txt",
    },
    {
        "seq": 32,
        "slug": "a-theory-of-play-and-fantasy",
        "title": "A Theory of Play and Fantasy",
        "kind": "essay",
        "printed_page_start": None,
        "start_line": 7169,
        "file": "raw/032-a-theory-of-play-and-fantasy.txt",
    },
    {
        "seq": 33,
        "slug": "epidemiology-of-a-schizophrenia",
        "title": "Epidemiology of a Schizophrenia",
        "kind": "essay",
        "printed_page_start": None,
        "start_line": 7316,
        "file": "raw/033-epidemiology-of-a-schizophrenia.txt",
    },
    {
        "seq": 34,
        "slug": "toward-a-theory-of-schizophrenia",
        "title": "Toward a Theory of Schizophrenia",
        "kind": "essay",
        "printed_page_start": None,
        "start_line": 7383,
        "file": "raw/034-toward-a-theory-of-schizophrenia.txt",
    },
    {
        "seq": 35,
        "slug": "the-group-dynamics-of-schizophrenia",
        "title": "The Group Dynamics of Schizophrenia",
        "kind": "essay",
        "printed_page_start": None,
        "start_line": 7656,
        "file": "raw/035-the-group-dynamics-of-schizophrenia.txt",
    },
    {
        "seq": 36,
        "slug": "minimal-requirements-for-a-theory-of-schizophrenia",
        "title": "Minimal Requirements for a Theory of Schizophrenia",
        "kind": "essay",
        "printed_page_start": None,
        "start_line": 7863,
        "file": "raw/036-minimal-requirements-for-a-theory-of-schizophrenia.txt",
    },
    {
        "seq": 37,
        "slug": "double-bind-1969",
        "title": "Double Bind, 1969",
        "kind": "essay",
        "printed_page_start": None,
        "start_line": 8186,
        "file": "raw/037-double-bind-1969.txt",
    },
    {
        "seq": 38,
        "slug": "the-logical-categories-of-learning-and-communication",
        "title": "The Logical Categories of Learning and Communication",
        "kind": "essay",
        "printed_page_start": None,
        "start_line": 8330,
        "file": "raw/038-the-logical-categories-of-learning-and-communication.txt",
    },
    {
        "seq": 39,
        "slug": "the-cybernetics-of-self-a-theory-of-alcoholism",
        "title": "The Cybernetics of Self: A Theory of Alcoholism",
        "kind": "essay",
        "printed_page_start": None,
        "start_line": 8787,
        "file": "raw/039-the-cybernetics-of-self-a-theory-of-alcoholism.txt",
    },
    {
        "seq": 40,
        "slug": "comment-on-part-three",
        "title": "Comment on Part III",
        "kind": "comment",
        "printed_page_start": None,
        "start_line": 9184,
        "file": "raw/040-comment-on-part-three.txt",
    },
    {
        "seq": 50,
        "slug": "part-four-biology-and-evolution",
        "title": "Part IV: Biology and Evolution",
        "kind": "part",
        "printed_page_start": None,
        "start_line": 9426,
        "file": "raw/050-part-four-biology-and-evolution.txt",
    },
    {
        "seq": 51,
        "slug": "on-empty-headedness-among-biologists-and-state-boards-of-education",
        "title": "On Empty-Headedness Among Biologists and State Boards of Education",
        "kind": "essay",
        "printed_page_start": None,
        "start_line": 9430,
        "file": "raw/051-on-empty-headedness-among-biologists-and-state-boards-of-education.txt",
    },
    {
        "seq": 52,
        "slug": "the-role-of-somatic-change-in-evolution",
        "title": "The Role of Somatic Change in Evolution",
        "kind": "essay",
        "printed_page_start": None,
        "start_line": 9471,
        "file": "raw/052-the-role-of-somatic-change-in-evolution.txt",
    },
    {
        "seq": 53,
        "slug": "problems-in-cetacean-and-other-mammalian-communication",
        "title": "Problems in Cetacean and Other Mammalian Communication",
        "kind": "essay",
        "printed_page_start": None,
        "start_line": 9640,
        "file": "raw/053-problems-in-cetacean-and-other-mammalian-communication.txt",
    },
    {
        "seq": 54,
        "slug": "a-re-examination-of-batesons-rule",
        "title": "A Re-examination of Bateson's Rule",
        "kind": "essay",
        "printed_page_start": None,
        "start_line": 9811,
        "file": "raw/054-a-re-examination-of-batesons-rule.txt",
    },
    {
        "seq": 55,
        "slug": "comment-on-part-four",
        "title": "Comment on Part IV",
        "kind": "comment",
        "printed_page_start": None,
        "start_line": 10062,
        "file": "raw/055-comment-on-part-four.txt",
    },
    {
        "seq": 60,
        "slug": "part-five-epistemology-and-ecology",
        "title": "Part V: Epistemology and Ecology",
        "kind": "part",
        "printed_page_start": None,
        "start_line": 10150,
        "file": "raw/060-part-five-epistemology-and-ecology.txt",
    },
    {
        "seq": 61,
        "slug": "cybernetic-explanation",
        "title": "Cybernetic Explanation",
        "kind": "essay",
        "printed_page_start": None,
        "start_line": 10154,
        "file": "raw/061-cybernetic-explanation.txt",
    },
    {
        "seq": 62,
        "slug": "redundancy-and-coding",
        "title": "Redundancy and Coding",
        "kind": "essay",
        "printed_page_start": None,
        "start_line": 10273,
        "file": "raw/062-redundancy-and-coding.txt",
    },
    {
        "seq": 63,
        "slug": "conscious-purpose-versus-nature",
        "title": "Conscious Purpose versus Nature",
        "kind": "essay",
        "printed_page_start": None,
        "start_line": 10424,
        "file": "raw/063-conscious-purpose-versus-nature.txt",
    },
    {
        "seq": 64,
        "slug": "effects-of-conscious-purpose-on-human-adaptation",
        "title": "Effects of Conscious Purpose on Human Adaptation",
        "kind": "essay",
        "printed_page_start": None,
        "start_line": 10589,
        "file": "raw/064-effects-of-conscious-purpose-on-human-adaptation.txt",
    },
    {
        "seq": 65,
        "slug": "form-substance-and-difference",
        "title": "Form, Substance, and Difference",
        "kind": "essay",
        "printed_page_start": None,
        "start_line": 10684,
        "file": "raw/065-form-substance-and-difference.txt",
    },
    {
        "seq": 66,
        "slug": "comment-on-part-five",
        "title": "Comment on Part V",
        "kind": "comment",
        "printed_page_start": None,
        "start_line": 10871,
        "file": "raw/066-comment-on-part-five.txt",
    },
    {
        "seq": 70,
        "slug": "part-six-crisis-in-the-ecology-of-mind",
        "title": "Part VI: Crisis in the Ecology of Mind",
        "kind": "part",
        "printed_page_start": None,
        "start_line": 10923,
        "file": "raw/070-part-six-crisis-in-the-ecology-of-mind.txt",
    },
    {
        "seq": 71,
        "slug": "from-versailles-to-cybernetics",
        "title": "From Versailles to Cybernetics",
        "kind": "essay",
        "printed_page_start": None,
        "start_line": 10927,
        "file": "raw/071-from-versailles-to-cybernetics.txt",
    },
    {
        "seq": 72,
        "slug": "pathologies-of-epistemology",
        "title": "Pathologies of Epistemology",
        "kind": "essay",
        "printed_page_start": None,
        "start_line": 11020,
        "file": "raw/072-pathologies-of-epistemology.txt",
    },
    {
        "seq": 73,
        "slug": "the-roots-of-ecological-crisis",
        "title": "The Roots of Ecological Crisis",
        "kind": "essay",
        "printed_page_start": None,
        "start_line": 11135,
        "file": "raw/073-the-roots-of-ecological-crisis.txt",
    },
    {
        "seq": 74,
        "slug": "ecology-and-flexibility-in-urban-civilization",
        "title": "Ecology and Flexibility in Urban Civilization",
        "kind": "essay",
        "printed_page_start": None,
        "start_line": 11238,
        "file": "raw/074-ecology-and-flexibility-in-urban-civilization.txt",
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
        '  title: "Steps to an Ecology of Mind"',
        '  author: "Gregory Bateson"',
        f'  source_text_witness: "{TXT_WITNESS.relative_to(ROOT).as_posix()}"',
        f'  extracted_full_text: "{FULL_PATH.relative_to(SOURCE_DIR).as_posix()}"',
        "  extraction_notes:",
        '    - "Generated from the local TXT witness on the incoming shelf."',
        '    - "Control characters and soft hyphens were removed during extraction."',
        '    - "The witness heading for The Roots of Ecological Crisis appears as The Boots of Ecological Crisis; metadata follows the contents listing."',
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
