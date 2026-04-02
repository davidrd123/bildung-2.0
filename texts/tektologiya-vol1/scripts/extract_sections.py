#!/usr/bin/env python3
"""Extract Bogdanov's volume-1 front matter and main-text leaf units from the FB2."""

from __future__ import annotations

import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "books" / "Bogdanov" / "Тектология (всеобщая организационная наука) -- 1989.fb2"
OUTLINE_TARGET = ROOT / "texts" / "tektologiya-vol1" / "source" / "outline.yaml"
FRONT_TARGET = ROOT / "texts" / "tektologiya-vol1" / "source" / "front-matter.yaml"
SECTIONS_TARGET = ROOT / "texts" / "tektologiya-vol1" / "source" / "sections.yaml"

NONBREAKING_SPACE = "\xa0"

TRANSLIT = {
    "а": "a",
    "б": "b",
    "в": "v",
    "г": "g",
    "д": "d",
    "е": "e",
    "ё": "e",
    "ж": "zh",
    "з": "z",
    "и": "i",
    "й": "i",
    "к": "k",
    "л": "l",
    "м": "m",
    "н": "n",
    "о": "o",
    "п": "p",
    "р": "r",
    "с": "s",
    "т": "t",
    "у": "u",
    "ф": "f",
    "х": "kh",
    "ц": "ts",
    "ч": "ch",
    "ш": "sh",
    "щ": "shch",
    "ъ": "",
    "ы": "y",
    "ь": "",
    "э": "e",
    "ю": "iu",
    "я": "ia",
}


def tag_name(elem: ET.Element) -> str:
    return elem.tag.rsplit("}", 1)[-1]


def yaml_quote(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def transliterate(text: str) -> str:
    pieces: list[str] = []
    for char in text.lower():
        pieces.append(TRANSLIT.get(char, char))
    return "".join(pieces)


def slugify(text: str) -> str:
    base = transliterate(text)
    base = re.sub(r"[^a-z0-9]+", "-", base)
    return base.strip("-") or "item"


def alpha_token(index: int) -> str:
    return chr(ord("a") + index - 1)


def normalize_text(text: str) -> str:
    text = text.replace(NONBREAKING_SPACE, " ")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r" ?\n ?", "\n", text)
    return text.strip()


def title_parts(section: ET.Element) -> list[str]:
    parts: list[str] = []
    for child in section:
        if tag_name(child) != "title":
            continue
        for part in child:
            if tag_name(part) != "p":
                continue
            text = normalize_text("".join(part.itertext()))
            if text:
                parts.append(text)
    return parts


def title_text(section: ET.Element) -> str:
    return " / ".join(title_parts(section))


def parse_label_and_title(text: str) -> tuple[str | None, str]:
    patterns = [
        r"^(§\s*\d+\.?)\s*(.+)$",
        r"^([0-9]+\.?)\s*(.+)$",
        r"^([A-Za-zА-Яа-яIVX]+\.?)\s*(.+)$",
    ]
    for pattern in patterns:
        match = re.match(pattern, text)
        if match:
            return match.group(1), match.group(2).strip()
    return None, text.strip()


def collect_blocks(section: ET.Element) -> list[str]:
    blocks: list[str] = []
    for child in section:
        name = tag_name(child)
        if name in {"title", "section"}:
            continue
        if name in {"p", "subtitle"}:
            text = normalize_text("".join(child.itertext()))
            if text:
                blocks.append(text)
            continue
        if name in {"cite", "epigraph"}:
            nested = []
            for part in child.iter():
                if tag_name(part) == "p":
                    text = normalize_text("".join(part.itertext()))
                    if text:
                        nested.append(text)
            if nested:
                blocks.append("\n".join(nested))
            continue
        if name == "poem":
            poem_lines: list[str] = []
            for part in child:
                part_name = tag_name(part)
                if part_name == "title":
                    title = " / ".join(
                        normalize_text("".join(p.itertext()))
                        for p in part
                        if tag_name(p) == "p"
                    ).strip(" /")
                    if title:
                        poem_lines.append(title)
                        poem_lines.append("")
                elif part_name == "stanza":
                    stanza_lines = []
                    for v in part:
                        if tag_name(v) == "v":
                            text = normalize_text("".join(v.itertext()))
                            if text:
                                stanza_lines.append(text)
                    if stanza_lines:
                        poem_lines.extend(stanza_lines)
                        poem_lines.append("")
            if poem_lines:
                while poem_lines and poem_lines[-1] == "":
                    poem_lines.pop()
                blocks.append("\n".join(poem_lines))
            continue

    return blocks


def child_sections(section: ET.Element) -> list[ET.Element]:
    return [child for child in section if tag_name(child) == "section"]


def emit_front_matter(entries: list[dict[str, str]]) -> str:
    lines = [
        "# Extracted from `books/Bogdanov/Тектология (всеобщая организационная наука) -- 1989.fb2`.",
        "# Front matter from the first body only. Notes and comments remain separate.",
        "",
    ]
    for entry in entries:
        lines.append(f"- id: {yaml_quote(entry['id'])}")
        lines.append(f"  slug: {yaml_quote(entry['slug'])}")
        lines.append(f"  title_ru: {yaml_quote(entry['title_ru'])}")
        lines.append("  ru: |-")
        for block in entry["ru"].split("\n\n"):
            for line in block.splitlines():
                lines.append(f"    {line}" if line else "")
            lines.append("")
        if lines[-1] == "":
            lines.pop()
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def emit_sections(entries: list[dict[str, str]]) -> str:
    lines = [
        "# Extracted from `books/Bogdanov/Тектология (всеобщая организационная наука) -- 1989.fb2`.",
        "# Leaf units from `Том 1` only. Front matter, notes, and comments are split out separately.",
        "",
    ]
    for entry in entries:
        lines.append(f"- id: {yaml_quote(entry['id'])}")
        lines.append(f"  label: {yaml_quote(entry['label'])}")
        lines.append(f"  chapter_index: {entry['chapter_index']}")
        lines.append(f"  chapter_slug: {yaml_quote(entry['chapter_slug'])}")
        lines.append(f"  chapter_title_ru: {yaml_quote(entry['chapter_title_ru'])}")
        if entry.get("chapter_subtitle_ru"):
            lines.append(f"  chapter_subtitle_ru: {yaml_quote(entry['chapter_subtitle_ru'])}")
        if entry.get("group_slug"):
            lines.append(f"  group_slug: {yaml_quote(entry['group_slug'])}")
        if entry.get("group_label"):
            lines.append(f"  group_label: {yaml_quote(entry['group_label'])}")
        if entry.get("group_title_ru"):
            lines.append(f"  group_title_ru: {yaml_quote(entry['group_title_ru'])}")
        lines.append(f"  section_title_ru: {yaml_quote(entry['section_title_ru'])}")
        lines.append("  ru: |-")
        for line in entry["ru"].splitlines():
            lines.append(f"    {line}" if line else "")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def emit_outline(
    front_entries: list[dict[str, str]],
    chapters: list[dict[str, object]],
) -> str:
    lines = [
        "# High-level outline for Bogdanov volume 1, derived from the FB2 hierarchy.",
        "",
        "metadata:",
        '  work_ru: "Всеобщая организационная наука (тектология)"',
        '  author: "Александр Александрович Богданов"',
        "  volume: 1",
        '  edition_note: "1989 reprint; main text headed `Часть 1`, third revised and expanded edition."',
        f"  source_fb2: {yaml_quote('../../books/Bogdanov/Тектология (всеобщая организационная наука) -- 1989.fb2')}",
        f"  source_facsimile: {yaml_quote('../../books/Bogdanov/Тектология_ Всеобщая организационная наука кн_1.djvu')}",
        "  auxiliary_bodies:",
        '    - "Примечания"',
        '    - "Комментарии"',
        "",
        "front_matter:",
    ]

    for entry in front_entries:
        lines.append(f"  - id: {yaml_quote(entry['id'])}")
        lines.append(f"    slug: {yaml_quote(entry['slug'])}")
        lines.append(f"    title_ru: {yaml_quote(entry['title_ru'])}")

    lines.extend(["", "main_text:", '  title_ru: "Том 1"', "  chapters:"])

    for chapter in chapters:
        lines.append(f"    - chapter_index: {chapter['chapter_index']}")
        lines.append(f"      slug: {yaml_quote(chapter['slug'])}")
        lines.append(f"      title_ru: {yaml_quote(chapter['title_ru'])}")
        if chapter.get("subtitle_ru"):
            lines.append(f"      subtitle_ru: {yaml_quote(chapter['subtitle_ru'])}")
        if chapter.get("groups"):
            lines.append("      groups:")
            for group in chapter["groups"]:
                lines.append(f"        - slug: {yaml_quote(group['slug'])}")
                if group.get("label"):
                    lines.append(f"          label: {yaml_quote(group['label'])}")
                lines.append(f"          title_ru: {yaml_quote(group['title_ru'])}")
                lines.append("          units:")
                for unit in group["units"]:
                    lines.append(f"            - {yaml_quote(unit)}")
        if chapter.get("units"):
            lines.append("      units:")
            for unit in chapter["units"]:
                lines.append(f"        - {yaml_quote(unit)}")

    return "\n".join(lines).rstrip() + "\n"


def extract_front_matter(front_sections: list[ET.Element]) -> list[dict[str, str]]:
    entries: list[dict[str, str]] = []
    for index, section in enumerate(front_sections, start=1):
        title = title_text(section)
        blocks = collect_blocks(section)
        if not title or not blocks:
            raise SystemExit(f"front matter entry {index} was incomplete")
        entries.append(
            {
                "id": f"front.{index:02d}",
                "slug": slugify(title),
                "title_ru": title,
                "ru": "\n\n".join(blocks),
            }
        )
    return entries


def extract_main_text(volume_section: ET.Element) -> tuple[list[dict[str, str]], list[dict[str, object]]]:
    entries: list[dict[str, str]] = []
    chapters_out: list[dict[str, object]] = []
    chapters = child_sections(volume_section)

    for chapter_index, chapter in enumerate(chapters, start=1):
        chapter_parts = title_parts(chapter)
        if not chapter_parts:
            raise SystemExit(f"chapter {chapter_index} has no title")
        chapter_title = chapter_parts[0]
        chapter_subtitle = chapter_parts[1] if len(chapter_parts) > 1 else None
        chapter_slug = slugify(chapter_title)
        chapter_units: list[str] = []
        chapter_groups: list[dict[str, object]] = []

        for child_index, child in enumerate(child_sections(chapter), start=1):
            nested = child_sections(child)
            child_title = title_text(child)
            label, bare_title = parse_label_and_title(child_title)
            group_token = alpha_token(child_index)

            if nested:
                group_slug = slugify(bare_title)
                group_units: list[str] = []
                for nested_index, leaf in enumerate(nested, start=1):
                    leaf_title = title_text(leaf)
                    leaf_label, leaf_bare_title = parse_label_and_title(leaf_title)
                    leaf_blocks = collect_blocks(leaf)
                    if not leaf_blocks:
                        raise SystemExit(f"empty leaf section under chapter {chapter_index}: {leaf_title}")
                    unit_id = f"{chapter_index}.{group_token}.{nested_index}"
                    group_units.append(unit_id)
                    entries.append(
                        {
                            "id": unit_id,
                            "label": leaf_label or str(nested_index),
                            "chapter_index": chapter_index,
                            "chapter_slug": chapter_slug,
                            "chapter_title_ru": chapter_title,
                            "chapter_subtitle_ru": chapter_subtitle or "",
                            "group_slug": group_slug,
                            "group_label": label or "",
                            "group_title_ru": bare_title,
                            "section_title_ru": leaf_bare_title,
                            "ru": "\n\n".join(leaf_blocks),
                        }
                    )
                chapter_groups.append(
                    {
                        "slug": group_slug,
                        "label": label or "",
                        "title_ru": bare_title,
                        "units": group_units,
                    }
                )
                chapter_units.extend(group_units)
                continue

            leaf_blocks = collect_blocks(child)
            if not leaf_blocks:
                raise SystemExit(f"empty leaf section under chapter {chapter_index}: {child_title}")

            if label and re.match(r"^[A-Za-zА-Яа-яIVX]+\.?$", label):
                unit_id = f"{chapter_index}.{group_token}"
                group_slug = slugify(bare_title)
                entries.append(
                    {
                        "id": unit_id,
                        "label": label,
                        "chapter_index": chapter_index,
                        "chapter_slug": chapter_slug,
                        "chapter_title_ru": chapter_title,
                        "chapter_subtitle_ru": chapter_subtitle or "",
                        "group_slug": group_slug,
                        "group_label": label,
                        "group_title_ru": bare_title,
                        "section_title_ru": bare_title,
                        "ru": "\n\n".join(leaf_blocks),
                    }
                )
                chapter_groups.append(
                    {
                        "slug": group_slug,
                        "label": label,
                        "title_ru": bare_title,
                        "units": [unit_id],
                    }
                )
                chapter_units.append(unit_id)
            else:
                unit_id = f"{chapter_index}.{child_index}"
                entries.append(
                    {
                        "id": unit_id,
                        "label": label or str(child_index),
                        "chapter_index": chapter_index,
                        "chapter_slug": chapter_slug,
                        "chapter_title_ru": chapter_title,
                        "chapter_subtitle_ru": chapter_subtitle or "",
                        "group_slug": "",
                        "group_label": "",
                        "group_title_ru": "",
                        "section_title_ru": bare_title,
                        "ru": "\n\n".join(leaf_blocks),
                    }
                )
                chapter_units.append(unit_id)

        chapter_record: dict[str, object] = {
            "chapter_index": chapter_index,
            "slug": chapter_slug,
            "title_ru": chapter_title,
        }
        if chapter_subtitle:
            chapter_record["subtitle_ru"] = chapter_subtitle
        if chapter_groups:
            chapter_record["groups"] = chapter_groups
        else:
            chapter_record["units"] = chapter_units
        chapters_out.append(chapter_record)

    return entries, chapters_out


def main() -> None:
    root = ET.parse(SOURCE).getroot()
    bodies = [child for child in root if tag_name(child) == "body"]
    if len(bodies) < 3:
        raise SystemExit("expected main text, notes, and comments bodies in the FB2")

    main_body = bodies[0]
    top_sections = child_sections(main_body)
    if len(top_sections) < 11:
        raise SystemExit("unexpected top-level structure in FB2 main body")

    volume_section = top_sections[10]
    if title_text(volume_section) != "Том 1":
        raise SystemExit("expected `Том 1` as the eleventh top-level section")

    front_entries = extract_front_matter(top_sections[:10])
    section_entries, chapters = extract_main_text(volume_section)

    FRONT_TARGET.write_text(emit_front_matter(front_entries), encoding="utf-8")
    SECTIONS_TARGET.write_text(emit_sections(section_entries), encoding="utf-8")
    OUTLINE_TARGET.write_text(emit_outline(front_entries, chapters), encoding="utf-8")

    print(
        f"wrote {len(front_entries)} front-matter entries and {len(section_entries)} main-text units"
    )


if __name__ == "__main__":
    main()
