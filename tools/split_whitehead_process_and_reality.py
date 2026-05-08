#!/usr/bin/env python3

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TXT_WITNESS = ROOT / (
    "sources/modern/incoming/books/"
    "Process and Reality (Gifford Le - Alfred North Whitehead.txt"
)
SOURCE_DIR = ROOT / "sources/modern/whitehead-process-and-reality/source"
FULL_PATH = SOURCE_DIR / "full/process-and-reality.txt"
RAW_DIR = SOURCE_DIR / "raw"
SECTIONS_PATH = SOURCE_DIR / "sections.yaml"


SECTIONS = [
    {
        "seq": 0,
        "slug": "title-pages-and-publication-matter",
        "title": "Title pages and publication matter",
        "kind": "front-matter",
        "start_line": 1,
        "file": "raw/000-title-pages-and-publication-matter.txt",
    },
    {
        "seq": 1,
        "slug": "editors-preface",
        "title": "Editors' Preface",
        "kind": "front-matter",
        "start_line": 118,
        "file": "raw/001-editors-preface.txt",
    },
    {
        "seq": 2,
        "slug": "preface",
        "title": "Preface",
        "kind": "front-matter",
        "start_line": 199,
        "file": "raw/002-preface.txt",
    },
    {
        "seq": 3,
        "slug": "contents",
        "title": "Contents",
        "kind": "front-matter",
        "start_line": 266,
        "file": "raw/003-contents.txt",
    },
    {
        "seq": 10,
        "slug": "part-one-the-speculative-scheme",
        "title": "Part I: The Speculative Scheme",
        "kind": "part",
        "start_line": 1413,
        "file": "raw/010-part-one-the-speculative-scheme.txt",
    },
    {
        "seq": 11,
        "slug": "part-one-chapter-one-speculative-philosophy",
        "title": "Part I, Chapter I: Speculative Philosophy",
        "kind": "chapter",
        "start_line": 1419,
        "file": "raw/011-part-one-chapter-one-speculative-philosophy.txt",
    },
    {
        "seq": 12,
        "slug": "part-one-chapter-two-the-categoreal-scheme",
        "title": "Part I, Chapter II: The Categoreal Scheme",
        "kind": "chapter",
        "start_line": 1585,
        "file": "raw/012-part-one-chapter-two-the-categoreal-scheme.txt",
    },
    {
        "seq": 13,
        "slug": "part-one-chapter-three-some-derivative-notions",
        "title": "Part I, Chapter III: Some Derivative Notions",
        "kind": "chapter",
        "start_line": 1805,
        "file": "raw/013-part-one-chapter-three-some-derivative-notions.txt",
    },
    {
        "seq": 20,
        "slug": "part-two-discussions-and-applications",
        "title": "Part II: Discussions and Applications",
        "kind": "part",
        "start_line": 1869,
        "file": "raw/020-part-two-discussions-and-applications.txt",
    },
    {
        "seq": 21,
        "slug": "part-two-chapter-one-fact-and-form",
        "title": "Part II, Chapter I: Fact and Form",
        "kind": "chapter",
        "start_line": 1875,
        "file": "raw/021-part-two-chapter-one-fact-and-form.txt",
    },
    {
        "seq": 22,
        "slug": "part-two-chapter-two-the-extensive-continuum",
        "title": "Part II, Chapter II: The Extensive Continuum",
        "kind": "chapter",
        "start_line": 2083,
        "file": "raw/022-part-two-chapter-two-the-extensive-continuum.txt",
    },
    {
        "seq": 23,
        "slug": "part-two-chapter-three-the-order-of-nature",
        "title": "Part II, Chapter III: The Order of Nature",
        "kind": "chapter",
        "start_line": 2285,
        "file": "raw/023-part-two-chapter-three-the-order-of-nature.txt",
    },
    {
        "seq": 24,
        "slug": "part-two-chapter-four-organisms-and-environment",
        "title": "Part II, Chapter IV: Organisms and Environment",
        "kind": "chapter",
        "start_line": 2597,
        "file": "raw/024-part-two-chapter-four-organisms-and-environment.txt",
    },
    {
        "seq": 25,
        "slug": "part-two-chapter-five-locke-and-hume",
        "title": "Part II, Chapter V: Locke and Hume",
        "kind": "chapter",
        "start_line": 2821,
        "file": "raw/025-part-two-chapter-five-locke-and-hume.txt",
    },
    {
        "seq": 26,
        "slug": "part-two-chapter-six-from-descartes-to-kant",
        "title": "Part II, Chapter VI: From Descartes to Kant",
        "kind": "chapter",
        "start_line": 3007,
        "file": "raw/026-part-two-chapter-six-from-descartes-to-kant.txt",
    },
    {
        "seq": 27,
        "slug": "part-two-chapter-seven-the-subjectivist-principle",
        "title": "Part II, Chapter VII: The Subjectivist Principle",
        "kind": "chapter",
        "start_line": 3111,
        "file": "raw/027-part-two-chapter-seven-the-subjectivist-principle.txt",
    },
    {
        "seq": 28,
        "slug": "part-two-chapter-eight-symbolic-reference",
        "title": "Part II, Chapter VIII: Symbolic Reference",
        "kind": "chapter",
        "start_line": 3205,
        "file": "raw/028-part-two-chapter-eight-symbolic-reference.txt",
    },
    {
        "seq": 29,
        "slug": "part-two-chapter-nine-the-propositions",
        "title": "Part II, Chapter IX: The Propositions",
        "kind": "chapter",
        "start_line": 3331,
        "file": "raw/029-part-two-chapter-nine-the-propositions.txt",
    },
    {
        "seq": 30,
        "slug": "part-two-chapter-ten-process",
        "title": "Part II, Chapter X: Process",
        "kind": "chapter",
        "start_line": 3567,
        "file": "raw/030-part-two-chapter-ten-process.txt",
    },
    {
        "seq": 40,
        "slug": "part-three-the-theory-of-prehensions",
        "title": "Part III: The Theory of Prehensions",
        "kind": "part",
        "start_line": 3661,
        "file": "raw/040-part-three-the-theory-of-prehensions.txt",
    },
    {
        "seq": 41,
        "slug": "part-three-chapter-one-the-theory-of-feelings",
        "title": "Part III, Chapter I: The Theory of Feelings",
        "kind": "chapter",
        "start_line": 3667,
        "file": "raw/041-part-three-chapter-one-the-theory-of-feelings.txt",
    },
    {
        "seq": 42,
        "slug": "part-three-chapter-two-the-primary-feelings",
        "title": "Part III, Chapter II: The Primary Feelings",
        "kind": "chapter",
        "start_line": 3871,
        "file": "raw/042-part-three-chapter-two-the-primary-feelings.txt",
    },
    {
        "seq": 43,
        "slug": "part-three-chapter-three-the-transmission-of-feelings",
        "title": "Part III, Chapter III: The Transmission of Feelings",
        "kind": "chapter",
        "start_line": 3963,
        "file": "raw/043-part-three-chapter-three-the-transmission-of-feelings.txt",
    },
    {
        "seq": 44,
        "slug": "part-three-chapter-four-propositions-and-feelings",
        "title": "Part III, Chapter IV: Propositions and Feelings",
        "kind": "chapter",
        "start_line": 4081,
        "file": "raw/044-part-three-chapter-four-propositions-and-feelings.txt",
    },
    {
        "seq": 45,
        "slug": "part-three-chapter-five-the-higher-phases-of-experience",
        "title": "Part III, Chapter V: The Higher Phases of Experience",
        "kind": "chapter",
        "start_line": 4187,
        "file": "raw/045-part-three-chapter-five-the-higher-phases-of-experience.txt",
    },
    {
        "seq": 50,
        "slug": "part-four-the-theory-of-extension",
        "title": "Part IV: The Theory of Extension",
        "kind": "part",
        "start_line": 4349,
        "file": "raw/050-part-four-the-theory-of-extension.txt",
    },
    {
        "seq": 51,
        "slug": "part-four-chapter-one-coordinate-division",
        "title": "Part IV, Chapter I: Coordinate Division",
        "kind": "chapter",
        "start_line": 4355,
        "file": "raw/051-part-four-chapter-one-coordinate-division.txt",
    },
    {
        "seq": 52,
        "slug": "part-four-chapter-two-extensive-connection",
        "title": "Part IV, Chapter II: Extensive Connection",
        "kind": "chapter",
        "start_line": 4497,
        "file": "raw/052-part-four-chapter-two-extensive-connection.txt",
    },
    {
        "seq": 53,
        "slug": "part-four-chapter-three-flat-loci",
        "title": "Part IV, Chapter III: Flat Loci",
        "kind": "chapter",
        "start_line": 4691,
        "file": "raw/053-part-four-chapter-three-flat-loci.txt",
    },
    {
        "seq": 54,
        "slug": "part-four-chapter-four-strains",
        "title": "Part IV, Chapter IV: Strains",
        "kind": "chapter",
        "start_line": 4855,
        "file": "raw/054-part-four-chapter-four-strains.txt",
    },
    {
        "seq": 55,
        "slug": "part-four-chapter-five-measurement",
        "title": "Part IV, Chapter V: Measurement",
        "kind": "chapter",
        "start_line": 4959,
        "file": "raw/055-part-four-chapter-five-measurement.txt",
    },
    {
        "seq": 60,
        "slug": "part-five-final-interpretation",
        "title": "Part V: Final Interpretation",
        "kind": "part",
        "start_line": 5087,
        "file": "raw/060-part-five-final-interpretation.txt",
    },
    {
        "seq": 61,
        "slug": "part-five-chapter-one-the-ideal-opposites",
        "title": "Part V, Chapter I: The Ideal Opposites",
        "kind": "chapter",
        "start_line": 5093,
        "file": "raw/061-part-five-chapter-one-the-ideal-opposites.txt",
    },
    {
        "seq": 62,
        "slug": "part-five-chapter-two-god-and-the-world",
        "title": "Part V, Chapter II: God and the World",
        "kind": "chapter",
        "start_line": 5149,
        "file": "raw/062-part-five-chapter-two-god-and-the-world.txt",
    },
    {
        "seq": 90,
        "slug": "index",
        "title": "Index",
        "kind": "back-matter",
        "start_line": 5281,
        "file": "raw/090-index.txt",
    },
    {
        "seq": 91,
        "slug": "editors-notes",
        "title": "Editors' Notes",
        "kind": "back-matter",
        "start_line": 6948,
        "file": "raw/091-editors-notes.txt",
    },
]


PAGE_RE = re.compile(r"\[([ivxlcdm]+|\d+)\]", re.IGNORECASE)


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


def printed_page_start(content: str) -> str | None:
    match = PAGE_RE.search(content)
    return match.group(1) if match else None


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
                "printed_page_start": printed_page_start(content),
            }
        )

    section_lines = [
        "book:",
        '  title: "Process and Reality: An Essay in Cosmology"',
        '  author: "Alfred North Whitehead"',
        '  editors: "David Ray Griffin and Donald W. Sherburne"',
        '  edition: "Corrected edition"',
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
