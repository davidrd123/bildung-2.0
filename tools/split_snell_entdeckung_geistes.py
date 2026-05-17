#!/usr/bin/env python3

from __future__ import annotations

import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PDF_PATH = ROOT / (
    "sources/modern/incoming/books/"
    "Die Entdeckung des Geistes _ Studien zur Entstehung des -- "
    "Bruno Snell -- 2nd, 2009.pdf"
)
SOURCE_DIR = ROOT / "sources/modern/snell-die-entdeckung-des-geistes/source"
FULL_PATH = SOURCE_DIR / "full/die-entdeckung-des-geistes.txt"
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
        "seq": 10,
        "slug": "einfuehrung",
        "title": "Einführung",
        "kind": "introduction",
        "printed_page_start": "7",
        "start_line": 98,
        "file": "raw/010-einfuehrung.txt",
    },
    {
        "seq": 11,
        "slug": "die-auffassung-des-menschen-bei-homer",
        "title": "I. Die Auffassung des Menschen bei Homer",
        "kind": "chapter",
        "printed_page_start": "13",
        "start_line": 393,
        "file": "raw/011-die-auffassung-des-menschen-bei-homer.txt",
    },
    {
        "seq": 12,
        "slug": "der-glaube-an-die-olympischen-goetter",
        "title": "II. Der Glaube an die olympischen Götter",
        "kind": "chapter",
        "printed_page_start": "30",
        "start_line": 1232,
        "file": "raw/012-der-glaube-an-die-olympischen-goetter.txt",
    },
    {
        "seq": 13,
        "slug": "die-welt-der-goetter-bei-hesiod",
        "title": "III. Die Welt der Götter bei Hesiod",
        "kind": "chapter",
        "printed_page_start": "45",
        "start_line": 1961,
        "file": "raw/013-die-welt-der-goetter-bei-hesiod.txt",
    },
    {
        "seq": 14,
        "slug": "das-erwachen-der-persoenlichkeit-in-der-fruehgriechischen-lyrik",
        "title": "IV. Das Erwachen der Persönlichkeit in der frühgriechischen Lyrik",
        "kind": "chapter",
        "printed_page_start": "56",
        "start_line": 2505,
        "file": "raw/014-das-erwachen-der-persoenlichkeit-in-der-fruehgriechischen-lyrik.txt",
    },
    {
        "seq": 15,
        "slug": "pindars-hymnos-auf-zeus",
        "title": "V. Pindars Hymnos auf Zeus",
        "kind": "chapter",
        "printed_page_start": "82",
        "start_line": 3863,
        "file": "raw/015-pindars-hymnos-auf-zeus.txt",
    },
    {
        "seq": 16,
        "slug": "mythos-und-wirklichkeit-in-der-griechischen-tragoedie",
        "title": "VI. Mythos und Wirklichkeit in der griechischen Tragödie",
        "kind": "chapter",
        "printed_page_start": "95",
        "start_line": 4519,
        "file": "raw/016-mythos-und-wirklichkeit-in-der-griechischen-tragoedie.txt",
    },
    {
        "seq": 17,
        "slug": "aristophanes-und-die-aesthetik",
        "title": "VII. Aristophanes und die Ästhetik",
        "kind": "chapter",
        "printed_page_start": "111",
        "start_line": 5287,
        "file": "raw/017-aristophanes-und-die-aesthetik.txt",
    },
    {
        "seq": 18,
        "slug": "menschliches-und-goettliches-wissen",
        "title": "VIII. Menschliches und göttliches Wissen",
        "kind": "chapter",
        "printed_page_start": "127",
        "start_line": 6083,
        "file": "raw/018-menschliches-und-goettliches-wissen.txt",
    },
    {
        "seq": 19,
        "slug": "zur-entstehung-des-geschichtlichen-bewusstseins",
        "title": "IX. Zur Entstehung des geschichtlichen Bewußtseins",
        "kind": "chapter",
        "printed_page_start": "139",
        "start_line": 6652,
        "file": "raw/019-zur-entstehung-des-geschichtlichen-bewusstseins.txt",
    },
    {
        "seq": 20,
        "slug": "mahnung-zur-tugend",
        "title": "X. Mahnung zur Tugend. Ein kurzes Kapitel aus der griechischen Ethik",
        "kind": "chapter",
        "printed_page_start": "151",
        "start_line": 7206,
        "file": "raw/020-mahnung-zur-tugend.txt",
    },
    {
        "seq": 21,
        "slug": "gleichnis-vergleich-metapher-analogie",
        "title": "XI. Gleichnis, Vergleich, Metapher, Analogie. Der Weg vom mythischen zum logischen Denken",
        "kind": "chapter",
        "printed_page_start": "178",
        "start_line": 8547,
        "file": "raw/021-gleichnis-vergleich-metapher-analogie.txt",
    },
    {
        "seq": 22,
        "slug": "die-naturwissenschaftliche-begriffsbildung-im-griechischen",
        "title": "XII. Die naturwissenschaftliche Begriffsbildung im Griechischen",
        "kind": "chapter",
        "printed_page_start": "205",
        "start_line": 9875,
        "file": "raw/022-die-naturwissenschaftliche-begriffsbildung-im-griechischen.txt",
    },
    {
        "seq": 23,
        "slug": "das-symbol-des-weges",
        "title": "XIII. Das Symbol des Weges",
        "kind": "chapter",
        "printed_page_start": "219",
        "start_line": 10550,
        "file": "raw/023-das-symbol-des-weges.txt",
    },
    {
        "seq": 24,
        "slug": "die-entdeckung-der-menschlichkeit",
        "title": "XIV. Die Entdeckung der Menschlichkeit und unsere Stellung zu den Griechen",
        "kind": "chapter",
        "printed_page_start": "231",
        "start_line": 11141,
        "file": "raw/024-die-entdeckung-der-menschlichkeit.txt",
    },
    {
        "seq": 25,
        "slug": "ueber-das-spielerische-bei-kallimachos",
        "title": "XV. Über das Spielerische bei Kallimachos",
        "kind": "chapter",
        "printed_page_start": "244",
        "start_line": 11769,
        "file": "raw/025-ueber-das-spielerische-bei-kallimachos.txt",
    },
    {
        "seq": 26,
        "slug": "arkadien",
        "title": "XVI. Arkadien. Die Entdeckung einer geistigen Landschaft",
        "kind": "chapter",
        "printed_page_start": "257",
        "start_line": 12381,
        "file": "raw/026-arkadien.txt",
    },
    {
        "seq": 27,
        "slug": "theorie-und-praxis",
        "title": "XVII. Theorie und Praxis",
        "kind": "chapter",
        "printed_page_start": "275",
        "start_line": 13271,
        "file": "raw/027-theorie-und-praxis.txt",
    },
    {
        "seq": 28,
        "slug": "nachwort-1974",
        "title": "XVIII. Nachwort 1974",
        "kind": "afterword",
        "printed_page_start": "283",
        "start_line": 13655,
        "file": "raw/028-nachwort-1974.txt",
    },
    {
        "seq": 30,
        "slug": "anmerkungen",
        "title": "Anmerkungen",
        "kind": "back-matter",
        "printed_page_start": "293",
        "start_line": 14097,
        "file": "raw/030-anmerkungen.txt",
    },
    {
        "seq": 31,
        "slug": "indices",
        "title": "Indices",
        "kind": "back-matter",
        "printed_page_start": "324",
        "start_line": 15925,
        "file": "raw/031-indices.txt",
    },
]


def yaml_quote(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


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
    lines = FULL_PATH.read_text(encoding="utf-8").split("\n")
    if lines and lines[-1] == "":
        lines.pop()

    rendered_sections = []
    for idx, section in enumerate(SECTIONS):
        start = section["start_line"]
        end = (
            SECTIONS[idx + 1]["start_line"] - 1
            if idx + 1 < len(SECTIONS)
            else len(lines)
        )
        body = "\n".join(lines[start - 1 : end]).rstrip("\n") + "\n"
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
        '  title: "Die Entdeckung des Geistes: Studien zur Entstehung des europäischen Denkens bei den Griechen"',
        '  author: "Bruno Snell"',
        '  edition_note: "9. Auflage; source filename records 2nd, 2009"',
        (
            "  source_pdf: "
            + yaml_quote(
                "sources/modern/incoming/books/"
                "Die Entdeckung des Geistes _ Studien zur Entstehung des -- "
                "Bruno Snell -- 2nd, 2009.pdf"
            )
        ),
        '  extracted_full_text: "source/full/die-entdeckung-des-geistes.txt"',
        "sections:",
    ]

    for section in rendered_sections:
        page = section["printed_page_start"]
        page_text = "null" if page is None else yaml_quote(page)
        section_lines.extend(
            [
                f'  - seq: {section["seq"]}',
                f'    slug: "{section["slug"]}"',
                f'    title: {yaml_quote(section["title"])}',
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
