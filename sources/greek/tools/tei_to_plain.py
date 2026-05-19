#!/usr/bin/env python3
"""Create plain-text search surfaces from Perseus/First1K TEI files."""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from xml.etree import ElementTree as ET

TEI_NS = {"tei": "http://www.tei-c.org/ns/1.0"}
XML_NS = "{http://www.w3.org/XML/1998/namespace}"


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def normalized_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def element_text(element: ET.Element) -> str:
    chunks: list[str] = []

    def walk(node: ET.Element) -> None:
        name = local_name(node.tag)
        if name == "milestone":
            unit = node.attrib.get("unit")
            n = node.attrib.get("n")
            if n and unit in {"section", "page"}:
                chunks.append(f" [{n}] ")
        elif node.text:
            chunks.append(node.text)

        for child in node:
            child_name = local_name(child.tag)
            if child_name not in {"note", "bibl"}:
                walk(child)
            if child.tail:
                chunks.append(child.tail)

    walk(element)
    return normalized_text("".join(chunks))


def first_title(root: ET.Element) -> str:
    for title in root.findall(".//tei:titleStmt/tei:title", TEI_NS):
        text = normalized_text("".join(title.itertext()))
        if text:
            return text
    return "Untitled"


def edition_urn(root: ET.Element) -> str:
    edition = root.find(".//tei:div[@type='edition']", TEI_NS)
    if edition is not None:
        n = edition.attrib.get("n")
        if n:
            return n
    return ""


def child_textpart_divs(element: ET.Element) -> list[ET.Element]:
    return [
        child
        for child in list(element)
        if local_name(child.tag) == "div" and child.attrib.get("type") == "textpart"
    ]


def write_sections(
    element: ET.Element,
    out: list[str],
    ancestors: list[tuple[str, str]],
) -> None:
    subtype = element.attrib.get("subtype", "")
    n = element.attrib.get("n", "")
    next_ancestors = ancestors
    children = child_textpart_divs(element)

    if children:
        out.append("")
        label = " ".join(part for part in (subtype.title(), n) if part)
        out.append(f"## {label or 'Textpart'}")
        if subtype and n:
            next_ancestors = ancestors + [(subtype, n)]
    else:
        context = " ".join(f"{kind} {value}" for kind, value in ancestors)
        unit = subtype or "section"
        label = f"{context} {unit} {n}".strip()
        out.append("")
        out.append(f"### {label}")
        text = element_text(element)
        if text:
            out.append(text)

    for child in children:
        write_sections(child, out, next_ancestors)


def convert_file(input_path: Path, output_path: Path) -> None:
    root = ET.parse(input_path).getroot()
    body = root.find(".//tei:body", TEI_NS)
    if body is None:
        raise ValueError(f"No TEI body found in {input_path}")
    text_root = root.find(".//tei:div[@type='edition']", TEI_NS)
    if text_root is None:
        text_root = body

    out: list[str] = [f"# {first_title(root)}"]
    urn = edition_urn(root)
    if urn:
        out.append("")
        out.append(f"CTS edition: `{urn}`")
    out.append("")
    out.append(f"Source TEI: `{input_path.name}`")

    for div in child_textpart_divs(text_root):
        write_sections(div, out, [])

    output_path.write_text("\n".join(out).strip() + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_dir", type=Path)
    parser.add_argument("output_dir", type=Path)
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    for input_path in sorted(args.input_dir.glob("*.xml")):
        stem = input_path.name.removesuffix(".xml")
        output_path = args.output_dir / f"{stem}.txt"
        convert_file(input_path, output_path)


if __name__ == "__main__":
    main()
