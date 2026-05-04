#!/usr/bin/env python3

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

import split_peirce_essential_volume_1 as split_source


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "sources/modern/peirce-essential-peirce-volume-1/source"
RAW_DIR = SOURCE_DIR / "raw"
CLEANED_DIR = SOURCE_DIR / "cleaned"
FULL_CLEANED_PATH = SOURCE_DIR / "full/essential-peirce-volume-1.cleaned.txt"


@dataclass(frozen=True)
class CleanedSection:
    seq: int
    title: str
    source_file: str
    cleaned_file: str
    pdf_range: str
    printed_range: str
    page_markers: int
    suspicious_count: int


HEADER_RE = re.compile(
    r"^(?:"
    r"(?:[ivxlcdm]+|\d+)\s+I\s+.+"
    r"|.+\s+I\s+(?:[ivxlcdm]+|\d+)"
    r")$",
    re.IGNORECASE,
)
PAGE_MARKER_RE = re.compile(r"^\[(?:page|pdf page) [^\]]+\]$")
STANDALONE_PAGE_RE = re.compile(r"^\d+$")
FOOTNOTE_RE = re.compile(r"^\d+\.\s+")
SUSPICIOUS_RE = re.compile(
    r"(?:\b[Oo] f\b|\b[A-Z] [a-z]{2,}\b|¡|¥|Alsopublished|thefour|"
    r"papersin|CP\d+\.\d|W\d+\d|indispensible|interprétant|m yself|"
    r"\bfo r\b|\bM an\b|\bN ew\b|\bH is\b|\bT h)"
)


REPLACEMENTS = {
    "C H R O N O L O G Y": "CHRONOLOGY",
    "F O R E W O R D": "FOREWORD",
    "I N T R O D U C T I O N": "INTRODUCTION",
    "T h e": "The",
    "t h e": "the",
    "T h is": "This",
    "T h at": "That",
    "T h ese": "These",
    "T h ere": "There",
    "T h ey": "They",
    "H is": "His",
    "H e": "He",
    "H arvard": "Harvard",
    "H ilary": "Hilary",
    "H ookw ay": "Hookway",
    "W illiam": "William",
    "W hitehead": "Whitehead",
    "W hite": "White",
    "W orld": "World",
    "W ho": "Who",
    "W hat": "What",
    "W e": "We",
    "W ith": "With",
    "w ith": "with",
    "w hich": "which",
    "w hile": "while",
    "w hen": "when",
    "w here": "where",
    "w ere": "were",
    "w as": "was",
    "w ould": "would",
    "w ork": "work",
    "w orld": "world",
    "w ritings": "writings",
    "w riting": "writing",
    "grow n": "grown",
    "know n": "known",
    "show n": "shown",
    "ow n": "own",
    "N ew": "New",
    "N ot": "Not",
    "N o": "No",
    "M assachusetts": "Massachusetts",
    "M ax": "Max",
    "M ost": "Most",
    "M an": "Man",
    "A m erican": "American",
    "A merica": "America",
    "A lfred": "Alfred",
    "A ristotle": "Aristotle",
    "A s": "As",
    "F o r": "For",
    "fo r": "for",
    "o f": "of",
    "O f": "Of",
    "m any": "many",
    "m ore": "more",
    "m ight": "might",
    "m ind": "mind",
    "m anuscript": "manuscript",
    "m anuscripts": "manuscripts",
    "m athem": "mathem",
    "P eirce": "Peirce",
    "P eirce’s": "Peirce’s",
    "P u rely": "Purely",
    "Peirce Js": "Peirce's",
    "Peirce J s": "Peirce's",
    "ofBelief": "of Belief",
    "ofDoubt": "of Doubt",
    "ofScience": "of Science",
    "ofthe": "of the",
    "oftheir": "of their",
    "ofone": "of one",
    "ofa": "of a",
    "tofind": "to find",
    "tofalse": "to false",
    "nofurther": "no further",
    "soformed": "so formed",
    "sofar": "so far",
    "sofrom": "so from",
    "fromanything": "from anything",
    "Thispaper": "This paper",
    "thispaper": "this paper",
    "thefirst": "the first",
    "Searchfor": "Search for",
    "Appleton 5 r": "Appleton's",
    "¿zj": "as",
    "¿zi": "at",
    "# 5*": "as",
    "cuiiuilmfetf1 riba* rthf* Ar iluwntinu,« *Rii* vVih^r J": "concluded that the latter practice is in itself licentious. But when I",
    "Ae develops": "he develops",
    "earliestformulation": "earliest formulation",
    "thegoodly": "the goodly",
    "Hefurther": "He further",
    "discussesfour": "discusses four",
    "tofix": "to fix",
    "some thing": "something",
    "twofundamental": "two fundamental",
    "nof act": "no fact",
    "w ill": "will",
    "G ilbert": "Gilbert",
    "na ture": "nature",
    "perma nency": "permanency",
    "whole some": "wholesome",
    "appel lation": "appellation",
    "re corded": "recorded",
    "con ception": "conception",
    "con ceptions": "conceptions",
    "con clusion": "conclusion",
    "con clusions": "conclusions",
    "con sciousness": "consciousness",
    "con sequence": "consequence",
    "con sequent": "consequent",
    "con sequently": "consequently",
    "con tinuity": "continuity",
    "con tinued": "continued",
    "con nected": "connected",
    "pre mise": "premise",
    "prem ises": "premises",
    "T o ": "To ",
    "every thing": "everything",
    "any thing": "anything",
    "manythings": "many things",
    "every body": "everybody",
    "remem bered": "remembered",
    "defec tive": "defective",
    "manipulat ing": "manipulating",
    "regard ing": "regarding",
    "demon strates": "demonstrates",
    "circum stances": "circumstances",
    "sub jects": "subjects",
    "infer ence": "inference",
    "infer ences": "inferences",
    "constitu tional": "constitutional",
    "particu lar": "particular",
    "formu lated": "formulated",
    "con fess": "confess",
    "dissatisfac tion": "dissatisfaction",
    "hypothe sis": "hypothesis",
    "proposi tion": "proposition",
    "proposi tions": "propositions",
    "deter mined": "determined",
    "arbi trary": "arbitrary",
    "priestridden": "priest-ridden",
    "primafacie": "prima facie",
    "interprétant": "interpretant",
    "interprétants": "interpretants",
    "m yself": "myself",
    "A lso": "Also",
    "Alsopublished": "Also published",
    "thefour": "the four",
    "papersin": "papers in",
    "and Sciences 7 (1868)1287-98": "and Sciences 7 (1868): 287-98",
    "¡¥2": "W2",
    "W21193-2n": "W2:193-211",
    "CP5.264-317": "CP 5.264-317",
    "CP5.264": "CP 5.264",
    "CP5": "CP 5",
    "CP6": "CP 6",
    "W2111": "W2:111",
    "W3142": "W3:142",
    "W4i": "W4:",
    "W5i": "W5:",
    "M S": "MS",
    "N E M": "NEM",
    "H P P L S": "HPPLS",
}

KEEP_HYPHEN_PREFIXES = {
    "anti",
    "co",
    "cross",
    "first",
    "half",
    "low",
    "many",
    "multi",
    "non",
    "one",
    "post",
    "pre",
    "pseudo",
    "re",
    "second",
    "self",
    "semi",
    "single",
    "three",
    "two",
    "well",
}


def normalize_text(text: str) -> str:
    text = text.replace("\u00ad", "")
    for old, new in REPLACEMENTS.items():
        text = text.replace(old, new)
    text = re.sub(r"([A-Z])\s+\.\s+([A-Z])\s+\.", r"\1. \2.", text)
    text = re.sub(r"\s+([,.;:?!])", r"\1", text)
    text = re.sub(r"([“‘])\s+", r"\1", text)
    text = re.sub(r"\s+([”’])", r"\1", text)
    return text


def dehyphenate(lines: list[str]) -> list[str]:
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        if i + 1 < len(lines):
            nxt = lines[i + 1].lstrip()
            if line.endswith("-") and nxt and nxt[0].islower():
                prefix = line[:-1].split()[-1].lower()
                if prefix in KEEP_HYPHEN_PREFIXES:
                    lines[i + 1] = f"{line}{nxt}"
                else:
                    lines[i + 1] = f"{line[:-1]}{nxt}"
                i += 1
                continue
        out.append(line)
        i += 1
    return out


def remove_running_header(lines: list[str], marker: str) -> list[str]:
    stripped = [line.strip() for line in lines if line.strip()]
    if not stripped:
        return []

    while stripped and HEADER_RE.match(stripped[0]) and len(stripped[0]) < 96:
        stripped.pop(0)

    if marker.startswith("[page ") and stripped and STANDALONE_PAGE_RE.match(stripped[0]):
        stripped.pop(0)

    return stripped


def unwrap_lines(lines: list[str]) -> str:
    paragraphs: list[str] = []
    current = ""
    for raw in lines:
        line = normalize_text(raw.strip())
        if not line:
            if current:
                paragraphs.append(current.strip())
                current = ""
            continue
        if PAGE_MARKER_RE.match(line):
            if current:
                paragraphs.append(current.strip())
                current = ""
            paragraphs.append(line)
            continue
        if FOOTNOTE_RE.match(line) and current:
            paragraphs.append(current.strip())
            current = line
            continue
        if current:
            current = f"{current} {line}"
        else:
            current = line
    if current:
        paragraphs.append(current.strip())
    return "\n\n".join(paragraphs)


def split_pages(raw_text: str) -> list[tuple[str, list[str]]]:
    pages: list[tuple[str, list[str]]] = []
    marker: str | None = None
    lines: list[str] = []
    for line in raw_text.splitlines():
        if PAGE_MARKER_RE.match(line.strip()):
            if marker is not None:
                pages.append((marker, lines))
            marker = line.strip()
            lines = []
        else:
            lines.append(line)
    if marker is not None:
        pages.append((marker, lines))
    return pages


def clean_section(section: split_source.Section) -> tuple[str, int, int]:
    raw_path = RAW_DIR / section.filename
    raw_text = raw_path.read_text(encoding="utf-8")
    page_chunks: list[str] = []
    marker_count = 0

    for marker, raw_lines in split_pages(raw_text):
        marker_count += 1
        lines = remove_running_header(raw_lines, marker)
        lines = dehyphenate(lines)
        page_body = normalize_text(unwrap_lines([marker, *lines]))
        page_chunks.append(page_body)

    body = "\n\n".join(chunk.strip() for chunk in page_chunks if chunk.strip())
    cleaned = f"{section.title}\n\n{body}\n"
    suspicious_count = len(SUSPICIOUS_RE.findall(cleaned))
    return cleaned, marker_count, suspicious_count


def format_range(start: str | None, end: str | None) -> str:
    if start is None and end is None:
        return "-"
    if start == end:
        return str(start)
    return f"{start}-{end}"


def write_manifests(rows: list[CleanedSection]) -> None:
    cleanup_lines = [
        "# Essential Peirce Volume 1 Cleanup Manifest",
        "",
        f"- PDF authority: `{split_source.PDF_AUTHORITY.relative_to(ROOT).as_posix()}`",
        "- Extraction: `pdftotext -raw` per page, then section splitting by observed PDF ranges.",
        "- Page markers: printed roman and arabic pages are preserved as `[page N]`; unnumbered front matter uses `[pdf page NNN]`.",
        "- PDF page offset: printed page 1 begins at PDF page 45, so printed arabic page = PDF page - 44.",
        "- Image proofing: page images are generated outside git under `/tmp/peirce_ep1_pages/`.",
        "- Status: this is a clean source scaffold, not a critical edition and not a live Peirce encounter campaign.",
        "",
        "| seq | cleaned file | PDF pages | printed pages | page markers | suspicious OCR items |",
        "| ---: | --- | ---: | --- | ---: | ---: |",
    ]
    for row in rows:
        cleanup_lines.append(
            f"| {row.seq} | `cleaned/{row.cleaned_file}` | {row.pdf_range} | "
            f"{row.printed_range} | {row.page_markers} | {row.suspicious_count} |"
        )
    (CLEANED_DIR / "cleanup-manifest.md").write_text("\n".join(cleanup_lines) + "\n", encoding="utf-8")

    proof_lines = [
        "# Essential Peirce Volume 1 Page Proof Manifest",
        "",
        f"Authority: `{split_source.PDF_AUTHORITY.relative_to(ROOT).as_posix()}`",
        "",
        "Rendered images target: `/tmp/peirce_ep1_pages/peirce-ep1-NNN.png` at 180 dpi.",
        "",
        "## Scope Notes",
        "",
        "- PDF pages 001-008 contain unnumbered title, publisher, epigraph, and contents pages.",
        "- PDF pages 009-041 map directly to printed roman pages ix-xli.",
        "- PDF pages 018, 042, and 044 are blank and skipped.",
        "- PDF page 043 is a duplicate half-title divider and is skipped from the text scaffold.",
        "- Printed page 1 starts at PDF page 045.",
        "- Printed pages 1-399 map to PDF pages 045-443.",
        "",
        "## Completed Spot Checks",
        "",
        "- PDF page 007: contents page and first table-of-contents section boundaries verified against rendered image.",
        "- PDF page 045 / printed page 1: first Peirce item starts correctly and page mapping is confirmed.",
        "- PDF page 163 / printed page 119: visually repaired a severe OCR break in `016-the-fixation-of-belief-1877.txt`.",
        "- PDF page 417 / printed page 373: notes section start verified against rendered image.",
        "- PDF page 433 / printed page 389: index section start verified against rendered image.",
        "",
        "## Proof Status",
        "",
        "| cleaned file | PDF / printed range | status | notes |",
        "| --- | --- | --- | --- |",
    ]
    for row in rows:
        proof_lines.append(
            f"| `cleaned/{row.cleaned_file}` | PDF {row.pdf_range}; printed {row.printed_range} | generated, pending visual proof | Text layer extracted with `pdftotext -raw`; use rendered page images for uncertain passages. |"
        )
    (CLEANED_DIR / "page-proof-manifest.md").write_text("\n".join(proof_lines) + "\n", encoding="utf-8")


def write_uncertainties(rows: list[CleanedSection]) -> None:
    lines = [
        "# Essential Peirce Volume 1 OCR Uncertainties",
        "",
        "This file records automated suspicious-pattern hits from the generated cleaned text.",
        "It is a triage surface for later page-image proofing, not a claim that every listed hit is wrong.",
        "",
    ]
    for row in rows:
        if row.suspicious_count == 0:
            continue
        path = CLEANED_DIR / row.cleaned_file
        text = path.read_text(encoding="utf-8")
        hits = []
        for match in SUSPICIOUS_RE.finditer(text):
            start = max(0, match.start() - 60)
            end = min(len(text), match.end() + 80)
            snippet = re.sub(r"\s+", " ", text[start:end]).strip()
            hits.append(snippet)
            if len(hits) >= 8:
                break
        lines.append(f"## {row.cleaned_file}")
        lines.append("")
        lines.append(f"- Suspicious pattern count: {row.suspicious_count}")
        for hit in hits:
            lines.append(f"- `{hit}`")
        lines.append("")
    (CLEANED_DIR / "ocr-uncertainties.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    if not RAW_DIR.exists() or not any(RAW_DIR.glob("*.txt")):
        split_source.main()

    CLEANED_DIR.mkdir(parents=True, exist_ok=True)
    full_parts: list[str] = []
    rows: list[CleanedSection] = []

    for section in split_source.SECTIONS:
        cleaned, marker_count, suspicious_count = clean_section(section)
        cleaned_path = CLEANED_DIR / section.filename
        cleaned_path.write_text(cleaned, encoding="utf-8")
        full_parts.append(cleaned.strip())
        rows.append(
            CleanedSection(
                seq=section.seq,
                title=section.title,
                source_file=section.filename,
                cleaned_file=section.filename,
                pdf_range=f"{section.pdf_start}-{section.pdf_end}",
                printed_range=format_range(section.printed_start, section.printed_end),
                page_markers=marker_count,
                suspicious_count=suspicious_count,
            )
        )

    FULL_CLEANED_PATH.write_text("\n\n".join(full_parts) + "\n", encoding="utf-8")
    write_manifests(rows)
    write_uncertainties(rows)


if __name__ == "__main__":
    main()
