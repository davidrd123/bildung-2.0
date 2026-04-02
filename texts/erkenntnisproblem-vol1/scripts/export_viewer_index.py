#!/usr/bin/env python3
"""Export a JSON index for the Erkenntnisproblem translation viewer.

Reads the markdown parts files and glossary, extracting aligned German/English
paragraph pairs for each tranche. The output is a single JSON file consumed
by the HTML viewer.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
PARTS_DIR = ROOT / "parts"
GLOSSARY_PATH = ROOT / "source" / "glossary.yaml"
TARGET_PATH = ROOT / "source" / "viewer-index.json"


def extract_blocks(md_text: str) -> list[dict]:
    """Extract German/English block pairs from a part file.

    Each pair is a section within the file delimited by ## headings,
    containing **German (corrected)** and an English draft code block.
    """
    sections = re.split(r"^## ", md_text, flags=re.MULTILINE)
    results = []

    for section in sections:
        if not section.strip():
            continue

        heading = section.split("\n", 1)[0].strip()

        de_blocks = re.findall(
            r"\*\*German(?:\s+\([^)]*\))?\*\*\s+```text\n(.*?)\n```",
            section,
            re.DOTALL,
        )
        en_blocks = re.findall(
            r"\*\*(?:Draft|English(?:\s+\([^)]*\))?)\*\*\s+```text\n(.*?)\n```",
            section,
            re.DOTALL,
        )

        if not de_blocks and not en_blocks:
            continue

        de_text = "\n\n".join(de_blocks).strip()
        en_text = "\n\n".join(en_blocks).strip()

        # Strip bare structural headings (chapter markers, section numbers,
        # continuation titles) that appear in one language but not the other
        # and throw off paragraph alignment.
        structural_re = re.compile(
            r"^(?:"
            r"Introduction|Einleitung\.?"                       # intro heading
            r"|(?:Erstes|Zweites|Drittes) Kapitel\.?"           # chapter markers (DE)
            r"|Chapter (?:One|Two|Three)\.?"                    # chapter markers (EN)
            r"|Nikolaus Cusanus\.?"                             # chapter title (DE)
            r"|Nicholas of Cusa\.?"                             # chapter title (EN)
            r"|Der Humanismus und der Kampf der Platonischen und Aristotelischen Philosophie\.?"
            r"|Humanism and the Conflict of Platonic and Aristotelian Philosophy\.?"
            r"|Der Skepticismus\.?"
            r"|Skepticism\.?"
            r"|Die Naturphilosophie\.?"
            r"|Natural Philosophy\.?"
            r"|Die Entstehung der exakten Wissenschaft\.?"
            r"|The Emergence of Exact Science\.?"
            r"|Die Erneuerung der Platonischen Philosophie\.?"
            r"|The Renewal of Platonic Philosophy\.?"
            r"|Die Reform der Aristotelischen Psychologie\.?"
            r"|The Reform of Aristotelian Psychology\.?"
            r"|Descartes\.?"
            r"|Die Fortbildung der Cartesischen Philosophie\.?"
            r"|The Development of Cartesian Philosophy\.?"
            r"|Die Auflösung der scholastischen Logik\.?"
            r"|The Dissolution of Scholastic Logic\.?"
            r"|[IVXLC]+\.?"                                    # roman numeral section markers
            r")\s*$",
            re.MULTILINE,
        )
        de_text = structural_re.sub("", de_text).strip()
        en_text = structural_re.sub("", en_text).strip()

        de_paras = [p.strip() for p in re.split(r"\n\n+", de_text) if p.strip()] if de_text else []
        en_paras = [p.strip() for p in re.split(r"\n\n+", en_text) if p.strip()] if en_text else []

        results.append({
            "heading": heading,
            "de": de_text,
            "en": en_text,
            "de_paragraphs": de_paras,
            "en_paragraphs": en_paras,
        })

    return results


def load_glossary() -> list[dict]:
    if not GLOSSARY_PATH.exists():
        return []
    with GLOSSARY_PATH.open("r", encoding="utf-8") as f:
        entries = yaml.safe_load(f) or []
    return [
        {
            "term": e.get("term", ""),
            "preferred": e.get("preferred"),
            "alternatives": e.get("alternatives", []),
            "status": e.get("status", "unknown"),
            "notes": e.get("notes", ""),
        }
        for e in entries
    ]


def main():
    parts = sorted(PARTS_DIR.glob("*.md"))
    all_parts = []

    for part_path in parts:
        md = part_path.read_text(encoding="utf-8")

        title_match = re.match(r"^#\s+(.+)$", md, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else part_path.stem

        scope_match = re.search(
            r"printed pages?\s+`([^`]+)`.*?PDF pages?\s+`([^`]+)`",
            md,
            re.DOTALL,
        )
        scope = ""
        if scope_match:
            scope = f"pp. {scope_match.group(1)} (PDF {scope_match.group(2)})"

        sections = extract_blocks(md)
        if sections:
            all_parts.append({
                "file": part_path.name,
                "title": title,
                "scope": scope,
                "sections": sections,
            })

    glossary = load_glossary()

    index = {
        "project": "erkenntnisproblem-vol1",
        "title": "Das Erkenntnisproblem I",
        "author": "Ernst Cassirer",
        "parts": all_parts,
        "glossary": glossary,
    }

    TARGET_PATH.parent.mkdir(parents=True, exist_ok=True)
    with TARGET_PATH.open("w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=2)

    total_sections = sum(len(p["sections"]) for p in all_parts)
    print(f"Exported {len(all_parts)} parts, {total_sections} sections, {len(glossary)} glossary terms")
    print(f"  → {TARGET_PATH}")


if __name__ == "__main__":
    main()
