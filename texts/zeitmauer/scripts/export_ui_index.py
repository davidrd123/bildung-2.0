#!/usr/bin/env python3
"""Export a small JSON index for the first dynamic Zeitmauer view.

This reads the canonical section source plus the derived handle and glossary
layers, then emits a UI-oriented JSON file. The goal is not to replace the
authority of the text files, but to give the future HTML layer and agents a
single concrete object to navigate.
"""

from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[3]
PROJECT_ROOT = ROOT / "texts" / "zeitmauer"
SECTIONS_PATH = PROJECT_ROOT / "source" / "sections.yaml"
GLOSSARY_PATH = PROJECT_ROOT / "source" / "glossary.yaml"
HANDLES_PATH = PROJECT_ROOT / "source" / "handles.yaml"
TARGET_PATH = PROJECT_ROOT / "source" / "ui-index.json"
PARTS_DIR = PROJECT_ROOT / "parts"

SECTION_HEADER_RE = re.compile(r"^## §(\d+)\s*$", re.MULTILINE)
DRAFT_BLOCK_RE = re.compile(r"\*\*Draft\*\*\s+```text\n(.*?)\n```", re.DOTALL)
TITLE_RE = re.compile(r"^#\s+(.+)$", re.MULTILINE)


def load_yaml(path: Path) -> object:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def build_section_lookup(sections: list[dict[str, object]]) -> dict[int, dict[str, object]]:
    return {int(section["id"]): section for section in sections}


def build_glossary_lookup(glossary: list[dict[str, object]]) -> dict[str, dict[str, object]]:
    lookup: dict[str, dict[str, object]] = {}
    for entry in glossary:
        handle = entry.get("handle")
        if handle:
            lookup[str(handle)] = entry
    return lookup


def repo_relative(path: Path) -> str:
    return str(path.relative_to(ROOT))


def normalize_project_file(raw_path: str | None) -> str | None:
    if not raw_path:
        return None
    return repo_relative((PROJECT_ROOT / raw_path).resolve())


def split_paragraphs(text: str) -> list[str]:
    return [paragraph.strip() for paragraph in re.split(r"\n\s*\n", text) if paragraph.strip()]


def load_translation_drafts() -> dict[int, dict[str, str]]:
    drafts: dict[int, dict[str, str]] = {}

    for path in sorted(PARTS_DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        matches = list(SECTION_HEADER_RE.finditer(text))

        for index, match in enumerate(matches):
            section_id = int(match.group(1))
            start = match.end()
            end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
            body = text[start:end]

            draft_match = DRAFT_BLOCK_RE.search(body)
            if not draft_match:
                continue

            drafts[section_id] = {
                "en": draft_match.group(1).strip(),
                "draft_file": repo_relative(path),
            }

    return drafts


def load_markdown_doc(path: Path) -> dict[str, str]:
    content = path.read_text(encoding="utf-8")
    title_match = TITLE_RE.search(content)
    return {
        "title": title_match.group(1).strip() if title_match else path.stem,
        "content": content,
    }


def main() -> None:
    sections = load_yaml(SECTIONS_PATH)
    glossary = load_yaml(GLOSSARY_PATH)
    handles = load_yaml(HANDLES_PATH)
    translation_drafts = load_translation_drafts()

    if not isinstance(sections, list):
        raise SystemExit(f"expected list in {SECTIONS_PATH}")
    if not isinstance(glossary, list):
        raise SystemExit(f"expected list in {GLOSSARY_PATH}")
    if not isinstance(handles, dict):
        raise SystemExit(f"expected mapping in {HANDLES_PATH}")

    section_lookup = build_section_lookup(sections)
    glossary_lookup = build_glossary_lookup(glossary)

    exported_sections: list[dict[str, object]] = []
    for item in handles.get("sections", []):
        if not isinstance(item, dict):
            continue
        section_id = int(item["id"])
        source = section_lookup.get(section_id)
        if source is None:
            raise SystemExit(f"missing section {section_id} in {SECTIONS_PATH}")
        draft = translation_drafts.get(section_id)
        if draft is None:
            raise SystemExit(f"missing translation draft for section {section_id} in {PARTS_DIR}")
        de_paragraphs = split_paragraphs(str(source["de"]))
        en_paragraphs = split_paragraphs(str(draft["en"]))

        exported_sections.append(
            {
                "handle": item["handle"],
                "id": section_id,
                "label": source["label"],
                "part_slug": source["part_slug"],
                "part_title_de": source["part_title_de"],
                "part_title_en": source["part_title_en"],
                "de": source["de"],
                "en": draft["en"],
                "de_paragraphs": de_paragraphs,
                "en_paragraphs": en_paragraphs,
                "paragraph_alignment": {
                    "de_count": len(de_paragraphs),
                    "en_count": len(en_paragraphs),
                    "aligned": len(de_paragraphs) == len(en_paragraphs),
                    "row_count": max(len(de_paragraphs), len(en_paragraphs)),
                },
                "source_file": normalize_project_file(str(item["source"])),
                "draft_file": draft["draft_file"],
            }
        )

    exported_terms: list[dict[str, object]] = []
    evidence_by_term: dict[str, list[str]] = defaultdict(list)
    for entry in glossary:
        if not isinstance(entry, dict):
            continue
        term_handle = entry.get("handle")
        if not term_handle:
            continue

        evidence_handles = [str(value) for value in entry.get("evidence", [])]
        evidence_by_term[str(term_handle)].extend(evidence_handles)

        exported_terms.append(
            {
                "handle": term_handle,
                "term": entry["term"],
                "kind": entry["kind"],
                "preferred": entry.get("preferred"),
                "alternatives": entry.get("alternatives", []),
                "status": entry["status"],
                "notes": entry.get("notes", ""),
                "evidence": evidence_handles,
            }
        )

    exported_chunks = []
    for item in handles.get("chunks", []):
        if not isinstance(item, dict):
            continue
        exported_chunks.append(
            {
                **item,
                "file": normalize_project_file(str(item.get("file"))),
            }
        )

    exported_notes = []
    for item in handles.get("notes", []):
        if not isinstance(item, dict):
            continue
        exported_notes.append(
            {
                **item,
                "file": normalize_project_file(str(item.get("file"))),
            }
        )

    exported_threads = []
    for item in handles.get("threads", []):
        if not isinstance(item, dict):
            continue
        resolved_file = normalize_project_file(str(item.get("file")))
        doc = load_markdown_doc(ROOT / resolved_file) if resolved_file else {
            "title": str(item["handle"]),
            "content": "",
        }
        exported_threads.append(
            {
                **item,
                "file": resolved_file,
                "title": doc["title"],
                "content": doc["content"],
            }
        )

    evidence_items = []
    for item in handles.get("evidence", []):
        if not isinstance(item, dict):
            continue
        glossary_entry = glossary_lookup.get(str(item["term"]))
        evidence_items.append(
            {
                "handle": item["handle"],
                "term": item["term"],
                "term_label": glossary_entry["term"] if glossary_entry else None,
                "anchor": item["anchor"],
                "file": normalize_project_file(str(item.get("file"))),
                "relation": item["relation"],
                "note": item["note"],
            }
        )

    relations_by_from: dict[str, list[dict[str, object]]] = defaultdict(list)
    for relation in handles.get("relations", []):
        if not isinstance(relation, dict):
            continue
        relations_by_from[str(relation["from"])].append(relation)

    chunk_items = exported_chunks
    note_items = exported_notes
    thread_items = exported_threads
    relation_items = handles.get("relations", [])

    sections_by_part: dict[str, list[str]] = defaultdict(list)
    for section in exported_sections:
        sections_by_part[str(section["part_slug"])].append(str(section["handle"]))

    by_handle: dict[str, dict[str, object]] = {}
    for index, item in enumerate(exported_sections):
        by_handle[str(item["handle"])] = {"kind": "section", "index": index}
    for index, item in enumerate(exported_terms):
        by_handle[str(item["handle"])] = {"kind": "term", "index": index}
    for index, item in enumerate(chunk_items):
        if isinstance(item, dict) and item.get("handle"):
            by_handle[str(item["handle"])] = {"kind": "chunk", "index": index}
    for index, item in enumerate(note_items):
        if isinstance(item, dict) and item.get("handle"):
            by_handle[str(item["handle"])] = {"kind": "note", "index": index}
    for index, item in enumerate(thread_items):
        if isinstance(item, dict) and item.get("handle"):
            by_handle[str(item["handle"])] = {"kind": "thread", "index": index}
    for index, item in enumerate(evidence_items):
        by_handle[str(item["handle"])] = {"kind": "evidence", "index": index}

    payload = {
        "project": handles.get("project", "zeitmauer"),
        "scope": handles.get("scope"),
        "source_files": {
            "sections": str(SECTIONS_PATH.relative_to(ROOT)),
            "glossary": str(GLOSSARY_PATH.relative_to(ROOT)),
            "handles": str(HANDLES_PATH.relative_to(ROOT)),
        },
        "counts": {
            "sections": len(exported_sections),
            "terms": len(exported_terms),
            "chunks": len(chunk_items),
            "notes": len(note_items),
            "threads": len(thread_items),
            "evidence": len(evidence_items),
            "relations": len(relation_items),
        },
        "sections": exported_sections,
        "glossary": exported_terms,
        "chunks": chunk_items,
        "notes": note_items,
        "threads": thread_items,
        "evidence": evidence_items,
        "relations": relation_items,
        "indexes": {
            "section_handles": [item["handle"] for item in exported_sections],
            "term_handles": [item["handle"] for item in exported_terms],
            "chunk_handles": [
                item["handle"]
                for item in chunk_items
                if isinstance(item, dict) and item.get("handle")
            ],
            "note_handles": [
                item["handle"]
                for item in note_items
                if isinstance(item, dict) and item.get("handle")
            ],
            "thread_handles": [
                item["handle"]
                for item in thread_items
                if isinstance(item, dict) and item.get("handle")
            ],
            "evidence_handles": [item["handle"] for item in evidence_items],
            "sections_by_part": dict(sorted(sections_by_part.items())),
            "by_handle": dict(sorted(by_handle.items())),
            "evidence_by_term": dict(sorted(evidence_by_term.items())),
            "relations_by_from": dict(sorted(relations_by_from.items())),
        },
    }

    TARGET_PATH.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"wrote UI index to {TARGET_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
