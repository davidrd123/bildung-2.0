#!/usr/bin/env python3
"""Extract sections 1-186 from Jünger's ebook text into YAML.

The source file includes later editorial matter. This script keeps only the
main numbered sections and writes a structured source file for translation.
"""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "books" / "An der Zeitmauer_ Mit Adnoten v - Ernst Jnger;.txt"
TARGET = ROOT / "zeitmauer" / "source" / "sections.yaml"
SECTION_RE = re.compile(r"^\s*(\d{1,3})\s*$")

PARTS = [
    (1, 3, "fremde-voegel", "Fremde Vögel", "Strange Birds"),
    (
        4,
        31,
        "messbare-und-schicksalszeit",
        "Meßbare und Schicksalszeit",
        "Measurable Time and Fateful Time",
    ),
    (32, 84, "humane-einteilungen", "Humane Einteilungen", "Human Divisions"),
    (
        85,
        166,
        "siderische-einteilungen",
        "Siderische Einteilungen",
        "Sidereal Divisions",
    ),
    (167, 186, "urgrund-und-person", "Urgrund und Person", "Primal Ground and Person"),
]


def yaml_quote(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def normalize_lines(lines: list[str]) -> list[str]:
    trimmed = [line.rstrip() for line in lines]

    while trimmed and not trimmed[0].strip():
        trimmed.pop(0)
    while trimmed and not trimmed[-1].strip():
        trimmed.pop()

    normalized: list[str] = []
    saw_blank = False

    for line in trimmed:
        if line.strip():
            normalized.append(line)
            saw_blank = False
        elif normalized and not saw_blank:
            normalized.append("")
            saw_blank = True

    while normalized and not normalized[-1].strip():
        normalized.pop()

    return normalized


def part_for(section_id: int) -> tuple[str, str, str]:
    for start, end, slug, title_de, title_en in PARTS:
        if start <= section_id <= end:
            return slug, title_de, title_en
    raise ValueError(f"no part mapping for section {section_id}")


def main() -> None:
    lines = SOURCE.read_text(encoding="utf-8").splitlines()

    starts: list[tuple[int, int]] = []
    for index, line in enumerate(lines):
        match = SECTION_RE.match(line)
        if not match:
            continue

        section_id = int(match.group(1))
        if 1 <= section_id <= 186:
            starts.append((section_id, index))

    expected = list(range(1, 187))
    found = [section_id for section_id, _ in starts]
    if found != expected:
        raise SystemExit(
            f"expected numbered sections 1-186 exactly once; found {len(found)} markers"
        )

    entries: list[dict[str, str | int]] = []
    for pos, (section_id, start_index) in enumerate(starts):
        if pos + 1 < len(starts):
            end_index = starts[pos + 1][1]
        else:
            end_index = next(
                (
                    idx
                    for idx in range(start_index + 1, len(lines))
                    if lines[idx].strip() == "Zurück"
                ),
                len(lines),
            )

        body = normalize_lines(lines[start_index + 1 : end_index])
        if not body:
            raise SystemExit(f"section {section_id} was empty after normalization")

        part_slug, part_title_de, part_title_en = part_for(section_id)
        entries.append(
            {
                "id": section_id,
                "label": f"§{section_id}",
                "part_slug": part_slug,
                "part_title_de": part_title_de,
                "part_title_en": part_title_en,
                "de": "\n".join(body),
            }
        )

    output: list[str] = [
        "# Extracted from `books/An der Zeitmauer_ Mit Adnoten v - Ernst Jnger;.txt`.",
        "# Main text only: sections 1-186. Editorial adnotes excluded.",
        "",
    ]

    for entry in entries:
        output.append(f"- id: {entry['id']}")
        output.append(f"  label: {yaml_quote(entry['label'])}")
        output.append(f"  part_slug: {yaml_quote(entry['part_slug'])}")
        output.append(f"  part_title_de: {yaml_quote(entry['part_title_de'])}")
        output.append(f"  part_title_en: {yaml_quote(entry['part_title_en'])}")
        output.append("  de: |-")
        for line in str(entry["de"]).splitlines():
            output.append(f"    {line}" if line else "")
        output.append("")

    TARGET.write_text("\n".join(output), encoding="utf-8")
    print(f"wrote {len(entries)} sections to {TARGET}")


if __name__ == "__main__":
    main()
