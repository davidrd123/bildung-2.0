#!/usr/bin/env python3
from __future__ import annotations

import re
import shutil
import unicodedata
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INCOMING = ROOT / "sources" / "japanese" / "incoming" / "Treasury of the True Dharma Eye - Dogen.txt"
BASE = ROOT / "sources" / "japanese" / "dogen-shobogenzo-tanahashi-en" / "source"
FULL_TEXT = BASE / "full" / "treasury-of-the-true-dharma-eye-tanahashi.txt"
RAW_DIR = BASE / "raw"
SECTIONS_YAML = BASE / "sections.yaml"


MAIN_PERIOD_HEADINGS = {
    "WANDERING PERIOD",
    "KOSHO MONASTERY PERIOD",
    "MONASTERY CONSTRUCTION PERIOD",
    "DAIBUTSU MONASTERY PERIOD",
    "EIHEI MONASTERY PERIOD",
    "FASCICLES NOT DATED BY DOGEN",
}

END_MATTER = {
    "AFTERWORD": "afterword",
    "APPENDIX 1": "appendix",
    "APPENDIX 2": "appendix",
    "APPENDIX 3": "appendix",
    "APPENDIX 4": "appendix",
    "APPENDIX 5": "appendix",
    "APPENDIX 6": "appendix",
    "APPENDIX 7": "appendix",
    "APPENDIX 8": "appendix",
    "GLOSSARY": "glossary",
    "SELECTED BIBLIOGRAPHY": "bibliography",
    "CREDITS": "credits",
}

APPENDIX_TITLES = {
    "APPENDIX 1": "Appendix 1: Recommending Zazen to All People",
    "APPENDIX 2": "Appendix 2: Dogen's Life and Teaching",
    "APPENDIX 3": "Appendix 3: Dogen's Editions of the Book",
    "APPENDIX 4": "Appendix 4: Lineage of Chinese Zen Ancestors",
    "APPENDIX 5": "Appendix 5: Maps Related to the Text",
    "APPENDIX 6": "Appendix 6: Eihei-ji Presumed Original Layout",
    "APPENDIX 7": "Appendix 7: Monks' Hall",
    "APPENDIX 8": "Appendix 8: Time System",
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
    fascicle: str | None = None

    @property
    def length(self) -> int:
        return self.end_line - self.start_line + 1


def slugify(text: str, limit: int = 72) -> str:
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-{2,}", "-", text).strip("-")
    if len(text) > limit:
        text = text[:limit].rstrip("-")
    return text or "section"


def quote_yaml(text: str) -> str:
    escaped = text.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def find_line(lines: list[str], needle: str, after: int = 0) -> int:
    normalized_needle = needle.replace("’", "'")
    for idx, line in enumerate(lines, start=1):
        if idx > after and line.strip().replace("’", "'") == normalized_needle:
            return idx
    raise RuntimeError(f"Could not find heading: {needle}")


def previous_heading_line(lines: list[str], heading_line: int, heading: str) -> int:
    for idx in range(heading_line - 1, max(heading_line - 12, 0), -1):
        if lines[idx - 1].strip() == heading:
            return idx
    return heading_line


def next_nonempty(lines: list[str], start_line: int) -> tuple[int, str]:
    for idx in range(start_line + 1, len(lines) + 1):
        stripped = lines[idx - 1].strip()
        if stripped:
            return idx, stripped
    raise RuntimeError(f"No nonempty line after {start_line}")


def is_fascicle_number(text: str) -> bool:
    return bool(re.fullmatch(r"\d{1,3}[AB]?", text))


def collect_toc_titles(lines: list[str]) -> dict[str, str]:
    contents_start = find_line(lines, "CONTENTS")
    appendix_start = find_line(lines, "1. Recommending Zazen to All People · Dogen", after=contents_start)
    titles: dict[str, str] = {}
    for line in lines[contents_start - 1 : appendix_start - 1]:
        stripped = line.strip()
        match = re.fullmatch(r"(\d{1,3})([ab])?\.\s+(.+)", stripped)
        if not match:
            continue
        label = match.group(1)
        if match.group(2):
            label = f"{label}{match.group(2).upper()}"
        titles[label] = match.group(3)
    return titles


def titlecase_heading(text: str) -> str:
    small_words = {"a", "an", "and", "as", "at", "by", "for", "from", "in", "of", "on", "the", "to", "with"}
    words = [word[:1].upper() + word[1:].lower() for word in text.split()]
    for idx, word in enumerate(words):
        if idx > 0 and word.lower() in small_words:
            words[idx] = word.lower()
    return " ".join(words).replace("’S", "’s")


def find_main_fascicles(
    lines: list[str], start_line: int, end_line: int, toc_titles: dict[str, str]
) -> list[dict[str, str | int]]:
    fascicles: list[dict[str, str | int]] = []
    for idx in range(start_line, end_line + 1):
        label = lines[idx - 1].strip()
        if not is_fascicle_number(label):
            continue
        title_line, title = next_nonempty(lines, idx)
        if title_line - idx > 6:
            continue
        if title.upper() != title:
            continue
        display_title = toc_titles.get(label, titlecase_heading(title))
        fascicles.append(
            {
                "start": idx,
                "kind": "fascicle",
                "title": f"{label}. {display_title}",
                "slug": f"{label.lower()}-{slugify(display_title)}",
                "fascicle": label,
            }
        )
    return fascicles


def build_sections(lines: list[str]) -> list[Section]:
    preface_heading = find_line(lines, "PREFACE AND ACKNOWLEDGMENTS")
    preface_start = previous_heading_line(lines, preface_heading, "VOLUME ONE")
    notes_start = find_line(lines, "NOTES TO THE READER", after=preface_start)
    editor_intro_start = find_line(lines, "EDITOR'S INTRODUCTION", after=notes_start)
    life_map_start = find_line(lines, "TEXTS IN RELATION TO DOGEN'S LIFE AND TRANSLATION CREDITS", after=editor_intro_start)
    main_start = find_line(lines, "WANDERING PERIOD", after=life_map_start + 1000)
    afterword_start = find_line(lines, "AFTERWORD", after=main_start)
    toc_titles = collect_toc_titles(lines)

    starts: list[dict[str, str | int | None]] = [
        {
            "start": 1,
            "kind": "front",
            "title": "Front Matter and Contents",
            "slug": "front-matter-and-contents",
            "parent": None,
            "fascicle": None,
        },
        {
            "start": preface_start,
            "kind": "preface",
            "title": "Preface and Acknowledgments",
            "slug": "preface-and-acknowledgments",
            "parent": None,
            "fascicle": None,
        },
        {
            "start": notes_start,
            "kind": "notes",
            "title": "Notes to the Reader",
            "slug": "notes-to-the-reader",
            "parent": None,
            "fascicle": None,
        },
        {
            "start": editor_intro_start,
            "kind": "introduction",
            "title": "Editor's Introduction",
            "slug": "editors-introduction",
            "parent": None,
            "fascicle": None,
        },
        {
            "start": life_map_start,
            "kind": "source-apparatus",
            "title": "Texts in Relation to Dogen's Life and Translation Credits",
            "slug": "texts-in-relation-to-dogens-life-and-translation-credits",
            "parent": None,
            "fascicle": None,
        },
    ]

    for idx in range(main_start, afterword_start):
        stripped = lines[idx - 1].strip()
        if stripped == "VOLUME TWO":
            starts.append(
                {
                    "start": idx,
                    "kind": "volume",
                    "title": "Volume Two",
                    "slug": "volume-two",
                    "parent": None,
                    "fascicle": None,
                }
            )
        elif stripped in MAIN_PERIOD_HEADINGS:
            starts.append(
                {
                    "start": idx,
                    "kind": "period",
                    "title": stripped.title(),
                    "slug": slugify(stripped),
                    "parent": None,
                    "fascicle": None,
                }
            )

    starts.extend(find_main_fascicles(lines, main_start, afterword_start - 1, toc_titles))

    for idx in range(afterword_start, len(lines) + 1):
        stripped = lines[idx - 1].strip()
        if stripped not in END_MATTER:
            continue
        title = APPENDIX_TITLES.get(stripped, stripped.title())
        starts.append(
            {
                "start": idx,
                "kind": END_MATTER[stripped],
                "title": title,
                "slug": slugify(title),
                "parent": None,
                "fascicle": None,
            }
        )

    deduped: list[dict[str, str | int | None]] = []
    seen: set[int] = set()
    for item in sorted(starts, key=lambda item: int(item["start"])):
        start = int(item["start"])
        if start in seen:
            continue
        deduped.append(item)
        seen.add(start)

    current_volume: str | None = "volume-one"
    current_period: str | None = None
    sections: list[Section] = []
    for seq, item in enumerate(deduped):
        start = int(item["start"])
        end = int(deduped[seq + 1]["start"]) - 1 if seq + 1 < len(deduped) else len(lines)
        kind = str(item["kind"])
        slug = str(item["slug"])
        title = str(item["title"])

        parent: str | None = None
        if kind == "volume":
            current_volume = slug
            current_period = None
        elif kind == "period":
            parent = current_volume
            current_period = slug
        elif kind == "fascicle":
            parent = current_period or current_volume

        filename = f"raw/{seq:03d}-{slug}.txt"
        sections.append(
            Section(
                seq=seq,
                start_line=start,
                end_line=end,
                kind=kind,
                slug=slug,
                title=title,
                file=filename,
                parent=parent,
                fascicle=item["fascicle"] if item["fascicle"] else None,  # type: ignore[arg-type]
            )
        )
    return sections


def write_full_text(lines: list[str]) -> None:
    FULL_TEXT.parent.mkdir(parents=True, exist_ok=True)
    FULL_TEXT.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_raw_sections(lines: list[str], sections: list[Section]) -> None:
    if RAW_DIR.exists():
        shutil.rmtree(RAW_DIR)
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    for section in sections:
        chunk = "\n".join(lines[section.start_line - 1 : section.end_line]) + "\n"
        (BASE / section.file).write_text(chunk, encoding="utf-8")


def write_sections_yaml(sections: list[Section]) -> None:
    output = [
        "# Treasury of the True Dharma Eye — lightweight sections map",
        "# Generated by tools/split_dogen_tanahashi.py from the current incoming text scaffold.",
        "# This is a navigational split of the Tanahashi English translation, not a Japanese source witness.",
        "",
        "sections:",
    ]
    for section in sections:
        output.extend(
            [
                f"  - seq: {section.seq:03d}",
                f"    file: {section.file}",
                f"    kind: {section.kind}",
                f"    slug: {section.slug}",
                f"    title: {quote_yaml(section.title)}",
            ]
        )
        if section.fascicle:
            output.append(f"    fascicle: {quote_yaml(section.fascicle)}")
        if section.parent:
            output.append(f"    parent: {section.parent}")
        output.extend(
            [
                f"    start_line: {section.start_line}",
                f"    end_line: {section.end_line}",
                f"    length: {section.length}",
            ]
        )
    SECTIONS_YAML.write_text("\n".join(output) + "\n", encoding="utf-8")


def main() -> None:
    lines = INCOMING.read_text(encoding="utf-8").splitlines()
    sections = build_sections(lines)
    write_full_text(lines)
    write_raw_sections(lines, sections)
    write_sections_yaml(sections)
    print(f"Wrote full text to {FULL_TEXT}")
    print(f"Wrote {len(sections)} split files to {RAW_DIR}")
    print(f"Wrote section map to {SECTIONS_YAML}")


if __name__ == "__main__":
    main()
