#!/usr/bin/env python3

from __future__ import annotations

import re
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "sources/modern/weyl-philosophie-der-mathematik-und-naturwissenschaft/source"
SECTIONS_PATH = SOURCE_DIR / "sections.yaml"
OCR_DIR = SOURCE_DIR / "ocr/tesseract-deu/pages"
CLEANED_DIR = SOURCE_DIR / "cleaned"
MANUALLY_CURATED_SECTIONS = {
    "front-contents",
    "math-03-geometrie",
    "science-01-raum-und-zeit",
    "appendix-c-quantenphysik-und-kausalitaet",
    "appendix-d-chemische-valenz",
    "appendix-e-physik-und-biologie",
    "appendix-f-physische-welt",
}


LETTER_CONTINUATION = re.compile(r"^[A-Za-zÄÖÜäöüß]")
RUNNING_HEAD_LEFT = re.compile(r"^[\dilI]+\s*\|\s+\S")
RUNNING_HEAD_RIGHT = re.compile(r"^.+\|\s*[\dilI]+$")
PAGE_NUMBER_ONLY = re.compile(r"^\d+$")


def read_sections() -> dict:
    with SECTIONS_PATH.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def clean_line(line: str) -> str:
    line = line.replace("\xad", "")
    line = line.replace("Kekul&", "Kekulé")
    line = line.replace("Kekule&", "Kekulé")
    line = line.replace("Kekules", "Kekulés")
    line = re.sub(r"\bKekule\b", "Kekulé", line)
    line = line.replace("muB", "muß")
    line = line.replace("groB", "groß")
    line = line.replace("daB", "daß")
    line = line.replace("1äßt", "läßt")
    line = line.replace("8.83", "S. 83")
    line = line.replace("KoNTINUUM", "KONTINUUM")
    line = line.replace("Unendlichklene", "Unendlichkleine")
    line = line.replace("GEOMETRRE", "GEOMETRIE")
    line = line.replace("Subjet", "Subjekt")
    line = line.replace("Koefhzienten", "Koeffizienten")
    line = line.replace("Werstanden", "verstanden")
    line = line.replace("„ ", "„").replace(" “", "“")
    line = line.replace(" .", ".").replace(" ,", ",")
    line = re.sub(r"(?<=[a-zäöü])B(?=[a-zäöü])", "ß", line)
    return re.sub(r"[ \t]+", " ", line).strip()


def strip_running_head(lines: list[str]) -> list[str]:
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    if not lines:
        return lines
    first = lines[0].strip()
    if RUNNING_HEAD_LEFT.match(first) or RUNNING_HEAD_RIGHT.match(first) or PAGE_NUMBER_ONLY.match(first):
        return lines[1:]
    return lines


def remove_running_heads(lines: list[str]) -> list[str]:
    return [
        line
        for line in lines
        if not (RUNNING_HEAD_LEFT.match(line) or RUNNING_HEAD_RIGHT.match(line))
    ]


def dehyphenate(lines: list[str]) -> list[str]:
    cleaned: list[str] = []
    index = 0
    while index < len(lines):
        line = lines[index]
        while (
            line.endswith("-")
            and index + 1 < len(lines)
            and lines[index + 1]
            and should_join_hyphen(line, lines[index + 1])
        ):
            line = line[:-1] + lines[index + 1].lstrip()
            index += 1
        cleaned.append(line)
        index += 1
    return cleaned


def should_join_hyphen(line: str, next_line: str) -> bool:
    if not LETTER_CONTINUATION.match(next_line):
        return False
    token = line.rsplit(" ", 1)[-1][:-1]
    letters = re.sub(r"[^A-Za-zÄÖÜäöüß]", "", token)
    if len(letters) <= 1:
        return False
    return True


def clean_page(text: str) -> str:
    text = text.replace("\f", "")
    raw_lines = [clean_line(line) for line in text.splitlines()]
    lines = strip_running_head(raw_lines)

    compacted: list[str] = []
    previous_blank = False
    for line in lines:
        blank = not line
        if blank and previous_blank:
            continue
        compacted.append(line)
        previous_blank = blank

    lines = dehyphenate(compacted)
    lines = [clean_line(line) for line in lines]
    lines = remove_running_heads(lines)
    cleaned = "\n".join(lines).strip()
    cleaned = cleaned.replace(
        "Vergangenheit von den gleichen Prinzipien\n"
        "Fig. 7. Das Hyperboloid von de aus verstanden, werden muß\n"
        "Sitter mit dem Einflußgebit p Wie im Falle des Entropiegeund den Weltlinien der Sterne. setzes.",
        "von den gleichen Prinzipien\n"
        "aus verstanden werden muß\n"
        "wie im Falle des Entropiegesetzes.\n\n"
        "Fig. 7. Das Hyperboloid von de Sitter mit dem Einflußgebiet D und den Weltlinien der Sterne.",
    )
    cleaned = cleaned.replace(
        "Vergangenheit von den gleichen Prinzipien\n"
        "Fig. 7. Das Hyperboloid von de aus ‚verstanden, werden muß\n"
        "Sitter mit dem Einflußgebit p Wie im Falle des Entropiegeund den Weltlinien der Sterne. setzes.",
        "von den gleichen Prinzipien\n"
        "aus verstanden werden muß\n"
        "wie im Falle des Entropiegesetzes.\n\n"
        "Fig. 7. Das Hyperboloid von de Sitter mit dem Einflußgebiet D und den Weltlinien der Sterne.",
    )
    return cleaned


def printed_page_for(section: dict, pdf_page: int) -> int | None:
    printed_start = section.get("printed_page_start")
    printed_end = section.get("printed_page_end")
    if printed_start is None or printed_end is None:
        return None
    return int(printed_start) + (pdf_page - int(section["pdf_page_start"]))


def page_anchor(section: dict, pdf_page: int) -> str:
    printed = printed_page_for(section, pdf_page)
    if printed is None:
        return f"[[pdf-page:{pdf_page:04d} printed-page:n/a]]"
    return f"[[pdf-page:{pdf_page:04d} printed-page:{printed}]]"


def section_filename(index: int, section: dict) -> str:
    return f"{index:03d}-{section['id']}.txt"


def build_section(index: int, section: dict) -> str:
    pdf_start = int(section["pdf_page_start"])
    pdf_end = int(section["pdf_page_end"])
    printed_start = section.get("printed_page_start")
    printed_end = section.get("printed_page_end")

    header = [
        f"# {section['title']}",
        "",
        f"Section ID: {section['id']}",
        f"Kind: {section['kind']}",
        f"PDF pages: {pdf_start}-{pdf_end}",
        f"Printed pages: {printed_start if printed_start is not None else 'n/a'}-{printed_end if printed_end is not None else 'n/a'}",
        "Status: OCR-derived cleaned draft; page images remain the authority.",
        "",
    ]

    chunks = header
    for pdf_page in range(pdf_start, pdf_end + 1):
        ocr_path = OCR_DIR / f"page-{pdf_page:04d}.txt"
        if not ocr_path.exists():
            raise SystemExit(f"missing OCR page: {ocr_path}")
        page_text = clean_page(ocr_path.read_text(encoding="utf-8"))
        chunks.append(page_anchor(section, pdf_page))
        chunks.append("")
        chunks.append(page_text if page_text else "[blank page]")
        chunks.append("")

    return "\n".join(chunks).rstrip() + "\n"


def main() -> None:
    data = read_sections()
    CLEANED_DIR.mkdir(parents=True, exist_ok=True)

    for index, section in enumerate(data["sections"]):
        filename = section_filename(index, section)
        rel_path = f"cleaned/{filename}"
        section["cleaned_file"] = rel_path
        target = CLEANED_DIR / filename
        if section["id"] in MANUALLY_CURATED_SECTIONS and target.exists():
            continue
        target.write_text(build_section(index, section), encoding="utf-8")

    data["book"]["status"] = "OCR-derived cleaned draft split by visual contents map"
    data["book"]["cleaned_directory"] = "cleaned"
    SECTIONS_PATH.write_text(
        yaml.safe_dump(data, allow_unicode=True, sort_keys=False, width=1200),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
