#!/usr/bin/env python3
from __future__ import annotations

import re
import shutil
import unicodedata
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "sources" / "german" / "kant-kritik-der-urteilskraft" / "source"
FULL_TEXT = BASE / "full" / "kritik-der-urteilskraft.txt"
RAW_DIR = BASE / "raw"
SECTIONS_YAML = BASE / "sections.yaml"

ROMAN_INTRO = {"I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"}
PLAIN_BODY_HEADINGS = {
    "Der Kritik der Urteilskraft",
    "Erster Teil",
    "Zweiter Teil",
    "Erster Abschnitt",
    "Zweiter Abschnitt",
    "Erstes Buch",
    "Zweites Buch",
    "Erste Abteilung",
    "Zweite Abteilung",
    "Anhang",
}
SUPPLEMENTARY_STOP_HEADINGS = {
    "Erstes Moment",
    "Zweites Moment",
    "Drittes Moment",
    "Viertes Moment",
    "A",
    "B",
}


@dataclass
class Section:
    seq: int
    start_line: int
    end_line: int
    kind: str
    slug: str
    title: str
    file: str
    parent: str | None = None

    @property
    def length(self) -> int:
        return self.end_line - self.start_line + 1


def slugify(text: str, limit: int = 72) -> str:
    text = text.replace("§", " ")
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-{2,}", "-", text).strip("-")
    if len(text) > limit:
        text = text[:limit].rstrip("-")
    return text or "section"


def classify_heading(line: str) -> str:
    stripped = line.strip()
    if stripped == "Vorrede":
        return "preface"
    if stripped == "Einleitung":
        return "introduction"
    if stripped in ROMAN_INTRO:
        return "introduction"
    if stripped == "Der Kritik der Urteilskraft":
        return "title"
    if stripped in {"Erster Teil", "Zweiter Teil"}:
        return "part"
    if stripped in {"Erster Abschnitt", "Zweiter Abschnitt", "Erstes Buch", "Zweites Buch", "Erste Abteilung", "Zweite Abteilung", "Anhang"}:
        return "division"
    if stripped.startswith("§ Anhang.") or stripped.startswith("§ Allgemeine Anmerkung") or stripped.startswith("§ Deduktion"):
        return "appendix"
    if re.match(r"^§+\s*\d+\.?$", stripped):
        return "section"
    return "section"


def collect_title(lines: list[str], start_idx: int, kind: str) -> str:
    start_line = lines[start_idx].strip()
    if kind == "introduction":
        if start_line == "Einleitung":
            collected: list[str] = []
            for line in lines[start_idx : start_idx + 12]:
                stripped = line.strip()
                if stripped:
                    collected.append(stripped)
                if len(collected) >= 3:
                    break
            return " ".join(collected)
        collected = []
        for line in lines[start_idx : start_idx + 8]:
            stripped = line.strip()
            if stripped:
                collected.append(stripped)
            if len(collected) >= 2:
                break
        return " ".join(collected)

    if kind == "title":
        return start_line

    if kind == "part":
        collected = []
        for offset, line in enumerate(lines[start_idx : start_idx + 24]):
            stripped = line.strip()
            if offset > 0 and (line.startswith("§ ") or stripped in PLAIN_BODY_HEADINGS or stripped in SUPPLEMENTARY_STOP_HEADINGS):
                break
            if stripped:
                collected.append(stripped)
            if len(collected) >= 4:
                break
        return " ".join(collected)

    if kind == "division":
        collected = []
        for offset, line in enumerate(lines[start_idx : start_idx + 18]):
            stripped = line.strip()
            if offset > 0 and (line.startswith("§ ") or stripped in PLAIN_BODY_HEADINGS or stripped in SUPPLEMENTARY_STOP_HEADINGS):
                break
            if stripped:
                collected.append(stripped)
            if len(collected) >= 2:
                break
        return " ".join(collected)

    if kind in {"section", "appendix", "preface"}:
        collected = []
        for line in lines[start_idx : start_idx + 16]:
            stripped = line.strip()
            if stripped:
                collected.append(stripped)
            if len(collected) >= 2:
                break
        return " ".join(collected)

    collected = []
    seen_any = False
    for line in lines[start_idx:]:
        stripped = line.strip()
        if stripped:
            collected.append(stripped)
            seen_any = True
            continue
        if seen_any:
            break
    return " ".join(collected)


def find_body_start(lines: list[str]) -> int:
    for idx, line in enumerate(lines, start=1):
        if idx > 200 and line.strip() == "Vorrede":
            return idx
    raise RuntimeError("Could not find body start (Vorrede).")


def build_sections(lines: list[str]) -> list[Section]:
    body_start = find_body_start(lines)

    intro_start = next(
        idx for idx, line in enumerate(lines, start=1) if idx > body_start and line.strip() == "Einleitung"
    )
    actual_body_start = next(
        idx for idx, line in enumerate(lines, start=1) if idx > intro_start and line.strip() == "Der Kritik der Urteilskraft"
    )

    starts: list[tuple[int, str]] = [(1, "front"), (body_start, "preface"), (intro_start, "introduction")]

    for idx, line in enumerate(lines, start=1):
        stripped = line.strip()
        if intro_start < idx < actual_body_start and stripped in ROMAN_INTRO and stripped != "I":
            starts.append((idx, "introduction"))

    for idx, line in enumerate(lines, start=1):
        stripped = line.strip()
        if idx >= actual_body_start and (line.startswith("§ ") or stripped in PLAIN_BODY_HEADINGS):
            starts.append((idx, classify_heading(line)))

    deduped: list[tuple[int, str]] = []
    seen: set[int] = set()
    for start, kind in sorted(starts):
        if start in seen:
            continue
        deduped.append((start, kind))
        seen.add(start)

    provisional: list[dict[str, object]] = []
    for i, (start, kind) in enumerate(deduped):
        end = deduped[i + 1][0] - 1 if i + 1 < len(deduped) else len(lines)
        title = "Front matter and Inhaltsübersicht" if kind == "front" else collect_title(lines, start - 1, kind)
        slug = slugify(title)
        provisional.append(
            {
                "start": start,
                "end": end,
                "kind": kind,
                "title": title,
                "slug": slug,
            }
        )

    current_part: str | None = None
    current_division: str | None = None
    sections: list[Section] = []

    for seq, item in enumerate(provisional):
        kind = item["kind"]  # type: ignore[index]
        slug = item["slug"]  # type: ignore[index]

        parent = None
        if kind == "part":
            current_part = slug
            current_division = None
        elif kind == "division":
            parent = current_part
            current_division = slug
        elif kind == "moment":
            parent = current_division or current_part
        elif kind == "section":
            parent = current_division or current_part
        elif kind == "appendix":
            parent = current_division or current_part

        filename = f"raw/{seq:03d}-{slug}.txt"
        sections.append(
            Section(
                seq=seq,
                start_line=item["start"],  # type: ignore[arg-type]
                end_line=item["end"],  # type: ignore[arg-type]
                kind=kind,  # type: ignore[arg-type]
                slug=slug,  # type: ignore[arg-type]
                title=item["title"],  # type: ignore[arg-type]
                file=filename,
                parent=parent,
            )
        )

    return sections


def write_sections(lines: list[str], sections: list[Section]) -> None:
    if RAW_DIR.exists():
        shutil.rmtree(RAW_DIR)
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    for section in sections:
        chunk = "\n".join(lines[section.start_line - 1 : section.end_line]).rstrip() + "\n"
        (BASE / section.file).write_text(chunk, encoding="utf-8")


def quote_yaml(text: str) -> str:
    escaped = text.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def write_sections_yaml(sections: list[Section]) -> None:
    lines = [
        "# Kritik der Urteilskraft — lightweight sections map",
        "# Generated by tools/split_kant_urteilskraft.py from the current full-text scaffold.",
        "# This is a navigational split for localized source forays, not yet a live encounter apparatus.",
        "",
        "sections:",
    ]
    for section in sections:
        lines.extend(
            [
                f"  - seq: {section.seq:03d}",
                f"    file: {section.file}",
                f"    kind: {section.kind}",
                f"    slug: {section.slug}",
                f"    title: {quote_yaml(section.title)}",
            ]
        )
        if section.parent:
            lines.append(f"    parent: {section.parent}")
        lines.extend(
            [
                f"    start_line: {section.start_line}",
                f"    end_line: {section.end_line}",
                f"    length: {section.length}",
            ]
        )
    SECTIONS_YAML.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    text = FULL_TEXT.read_text(encoding="utf-8")
    lines = text.splitlines()
    sections = build_sections(lines)
    write_sections(lines, sections)
    write_sections_yaml(sections)
    print(f"Wrote {len(sections)} sections to {RAW_DIR}")
    print(f"Wrote section map to {SECTIONS_YAML}")


if __name__ == "__main__":
    main()
