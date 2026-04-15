#!/usr/bin/env python3

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "sources/german/cassirer-substanzbegriff-und-funktionsbegriff/source"
FULL = BASE / "full/substanzbegriff-und-funktionsbegriff.txt"
RAW = BASE / "raw"
SECTIONS = BASE / "sections.yaml"


def slugify(text: str) -> str:
    text = text.lower()
    replacements = {
        "ä": "ae",
        "ö": "oe",
        "ü": "ue",
        "ß": "ss",
    }
    for src, dst in replacements.items():
        text = text.replace(src, dst)
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def find_after(lines: list[str], pattern: str, start: int) -> int:
    regex = re.compile(pattern)
    for i in range(start, len(lines)):
        if regex.match(lines[i]):
            return i
    raise ValueError(f"pattern not found after {start}: {pattern}")


def body_title(lines: list[str], idx: int) -> str | None:
    for i in range(idx, min(idx + 8, len(lines))):
        candidate = lines[i].strip()
        if not candidate:
            continue
        if candidate.startswith("\x0c"):
            continue
        if re.fullmatch(r"\[?[IVXLCDM]+\]?[-–]?[0-9 ]*", candidate):
            continue
        if re.fullmatch(r"[A-ZÄÖÜ .0-9-]{4,}", candidate):
            continue
        return candidate
    return None


def main() -> None:
    text = FULL.read_text()
    lines = text.splitlines()

    starts: list[dict[str, object]] = []

    def add(id_: str, kind: str, title: str, pattern: str | None, parent: str | None = None) -> None:
        if not starts:
            idx = 0 if pattern is None else find_after(lines, pattern, 0)
        else:
            start_at = int(starts[-1]["start_line"]) + 1
            idx = start_at if pattern is None else find_after(lines, pattern, start_at)
        starts.append(
            {
                "id": id_,
                "kind": kind,
                "title": title,
                "parent": parent,
                "start_line": idx + 1,
            }
        )

    add("000", "front-matter", "Front matter and Inhaltsübersicht", r"^Ernst Cassirer$")
    add("001", "preface", "Vorwort", r"^VORWORT$")
    add("010", "part", "Erster Teil. Dingbegriffe und Relationsbegriffe", r"^ERSTER TEIL\.$")
    add("011", "chapter", "Zur Theorie der Begriffsbildung", r"^ERSTES KAPITEL\.$", "010")
    add("012", "chapter", "Die Zahlbegriffe", r"^ZWEITES KAPITEL\.$", "010")
    add("013", "chapter", "Der Raumbegriff und die Geometrie", r"^DRITTES KAPITEL\.$", "010")
    add("014", "chapter", "Die naturwissenschaftliche Begriffsbildung", r"^VIERTES KAPITEL\.$", "010")
    add(
        "020",
        "part",
        "Zweiter Teil. Das System der Relationsbegriffe und das Problem der Wirklichkeit",
        r"^ZWEITER TEIL\.$",
    )
    add("021", "chapter", "Zum Problem der Induktion", r"^FÜNFTES KAPITEL\.$", "020")
    add("022", "chapter", "Der Begriff der Wirklichkeit", r"^SECHSTES KAPITEL\.$", "020")
    add(
        "023",
        "chapter",
        "Subjektivität und Objektivität der Relationsbegriffe",
        r"^SIEBENTES KAPITEL\.$",
        "020",
    )
    add("024", "chapter", "Zur Psychologie der Relationen", r"^ACHTES KAPITEL\.$", "020")
    add("030", "back-matter", "Editorischer Bericht", r"^Editorischer Bericht$")
    add("031", "back-matter", "Abkürzungen", r"^Abkürzungen$")
    add("032", "back-matter", "Schriftenregister", r"^Schriftenregister$")
    add("033", "back-matter", "Personenregister", r"^Personenregister$")

    sections: list[dict[str, object]] = []
    for i, entry in enumerate(starts):
        start = int(entry["start_line"])
        end = (int(starts[i + 1]["start_line"]) - 1) if i + 1 < len(starts) else len(lines)
        body = lines[start - 1 : end]
        title = str(entry["title"])
        path = f"source/raw/{entry['id']}-{slugify(title)}.txt"
        (RAW / Path(path).name).write_text("\n".join(body).rstrip() + "\n")
        sections.append(
            {
                **entry,
                "path": path,
                "end_line": end,
                "length": end - start + 1,
            }
        )

    # Chapter IV is too large to serve as a single bounded probing surface.
    # Expose its internal I–IX divisions as additional subsection files while
    # keeping the chapter-level file as the broader container.
    chapter_iv = next(section for section in sections if section["id"] == "014")
    chapter_start = int(chapter_iv["start_line"])
    chapter_end = int(chapter_iv["end_line"])
    chapter_body = lines[chapter_start - 1 : chapter_end]

    roman_markers = ["II.", "III.", "IV.", "V.", "VI.", "VII.", "VIII.", "IX."]
    subsection_starts: list[tuple[str, int]] = [("I", chapter_start)]
    for marker in roman_markers:
        for offset, line in enumerate(chapter_body, start=chapter_start):
            if line.strip() == marker:
                subsection_starts.append((marker.rstrip("."), offset))
                break
        else:
            raise ValueError(f"chapter IV subsection marker not found: {marker}")

    subsection_id_map = {
        "I": "0141",
        "II": "0142",
        "III": "0143",
        "IV": "0144",
        "V": "0145",
        "VI": "0146",
        "VII": "0147",
        "VIII": "0148",
        "IX": "0149",
    }
    for idx, (roman, start) in enumerate(subsection_starts):
        end = subsection_starts[idx + 1][1] - 1 if idx + 1 < len(subsection_starts) else chapter_end
        body = lines[start - 1 : end]
        path = f"source/raw/{subsection_id_map[roman]}-iv-{roman.lower()}.txt"
        (RAW / Path(path).name).write_text("\n".join(body).rstrip() + "\n")
        sections.append(
            {
                "id": subsection_id_map[roman],
                "title": f"Kapitel IV — {roman}.",
                "kind": "subsection",
                "parent": "014",
                "path": path,
                "start_line": start,
                "end_line": end,
                "length": end - start + 1,
            }
        )

    with SECTIONS.open("w") as f:
        f.write("sections:\n")
        for section in sections:
            f.write(f"  - id: '{section['id']}'\n")
            f.write(f"    title: \"{str(section['title']).replace('\\', '\\\\').replace('"', '\\"')}\"\n")
            f.write(f"    kind: {section['kind']}\n")
            parent = section.get("parent")
            if parent:
                f.write(f"    parent: '{parent}'\n")
            f.write(f"    path: {section['path']}\n")
            f.write(f"    start_line: {section['start_line']}\n")
            f.write(f"    end_line: {section['end_line']}\n")
            f.write(f"    length: {section['length']}\n")


if __name__ == "__main__":
    main()
