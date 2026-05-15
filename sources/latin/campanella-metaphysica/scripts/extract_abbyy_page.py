#!/usr/bin/env python3
"""Extract one page from the IA-shipped ABBYY XML, preserving block structure.

The IA Campanella package ships an ABBYY FineReader XML stream (gzipped) with
per-character coordinates, block typing (Text / Picture / Separator / Table),
and per-character confidence. This script stream-parses the file and emits one
page as a block-tagged text dump, so downstream passes (long-s repair,
marginalia separation, header filtering) can work against structure rather
than against a flat-text projection.

Block-tagging heuristic:
  - blockType="Text" with a narrow width AND positioned in the right margin
    is treated as MARGINALIA.
  - blockType="Text" whose first line sits above the typical body-text band
    is treated as HEADER (running header / page number).
  - Everything else with blockType="Text" is treated as BODY.

We deliberately keep the heuristic conservative; the goal here is to make the
structure visible, not to make policy decisions about what to filter.
"""

from __future__ import annotations

import argparse
import gzip
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterator

NS = "{http://www.abbyy.com/FineReader_xml/FineReader10-schema-v1.xml}"

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ABBYY_GZ = PROJECT_ROOT / "source" / "local" / "thomcampanellsty00camp_abbyy.gz"


@dataclass
class Block:
    block_type: str
    role: str  # "BODY" | "MARGINALIA" | "HEADER" | "OTHER"
    l: int
    t: int
    r: int
    b: int
    lines: list[str] = field(default_factory=list)
    suspicious_chars: int = 0
    total_chars: int = 0
    out_of_dict_words: int = 0
    total_words: int = 0


def iter_pages(stream) -> Iterator[tuple[int, ET.Element]]:
    """Yield (zero_based_leaf_index, page_element) pairs as we stream."""
    leaf_index = -1
    for event, elem in ET.iterparse(stream, events=("end",)):
        if elem.tag != NS + "page":
            continue
        leaf_index += 1
        yield leaf_index, elem
        elem.clear()


def classify_block(block: ET.Element, page_width: int, page_height: int) -> str:
    block_type = block.attrib.get("blockType", "")
    if block_type != "Text":
        return "OTHER"

    try:
        l = int(block.attrib["l"])
        t = int(block.attrib["t"])
        r = int(block.attrib["r"])
        b = int(block.attrib["b"])
    except (KeyError, ValueError):
        return "OTHER"

    width = r - l
    height = b - t

    # HEADER: block sits in the top ~6% of the page and is short.
    if t < page_height * 0.06 and height < page_height * 0.05:
        return "HEADER"

    # MARGINALIA: narrow block in the outer margins. The 1638 print uses both
    # margins for marginalia, so check both sides.
    narrow = width < page_width * 0.22
    in_right_margin = l > page_width * 0.70
    in_left_margin = r < page_width * 0.30
    if narrow and (in_right_margin or in_left_margin):
        return "MARGINALIA"

    return "BODY"


def extract_block_text(block: ET.Element) -> tuple[list[str], int, int, int, int]:
    """Return (lines, suspicious_chars, total_chars, ood_words, total_words)."""
    lines = []
    susp = 0
    total_c = 0
    ood = 0
    total_w = 0

    for line in block.iter(NS + "line"):
        for fmt in line.iter(NS + "formatting"):
            pass  # iter order is unstable across versions; we use charParams below
        line_chars = []
        word_in_dict = None
        for cp in line.iter(NS + "charParams"):
            ch = cp.text or " "
            line_chars.append(ch)
            total_c += 1
            if cp.attrib.get("suspicious") == "1":
                susp += 1
            if cp.attrib.get("wordFirst") == "1":
                total_w += 1
                if cp.attrib.get("wordFromDictionary") == "0":
                    ood += 1
        if line_chars:
            lines.append("".join(line_chars).rstrip())

    return lines, susp, total_c, ood, total_w


def render_blocks(blocks: list[Block], show_stats: bool) -> str:
    out: list[str] = []
    for blk in blocks:
        header = f"[{blk.role}]  blockType={blk.block_type}  bbox=({blk.l},{blk.t},{blk.r},{blk.b})"
        if show_stats and blk.total_chars:
            sp = 100.0 * blk.suspicious_chars / blk.total_chars
            if blk.total_words:
                dp = 100.0 * blk.out_of_dict_words / blk.total_words
                header += (
                    f"  suspicious={blk.suspicious_chars}/{blk.total_chars} ({sp:.1f}%)"
                    f"  out_of_dict={blk.out_of_dict_words}/{blk.total_words} ({dp:.1f}%)"
                )
            else:
                header += f"  suspicious={blk.suspicious_chars}/{blk.total_chars} ({sp:.1f}%)"
        out.append(header)
        out.extend(blk.lines)
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    src = parser.add_mutually_exclusive_group(required=True)
    src.add_argument(
        "--jp2-leaf",
        type=int,
        help="zero-based JP2 leaf index (matches IA jp2 filename suffix, e.g. 114 for _0114.jp2)",
    )
    src.add_argument(
        "--printed-page",
        type=int,
        help="printed page number; resolved via known_alignments in page-map.yaml (not yet implemented)",
    )
    parser.add_argument(
        "--abbyy",
        type=Path,
        default=DEFAULT_ABBYY_GZ,
        help="path to the gzipped ABBYY XML",
    )
    parser.add_argument(
        "--output",
        type=str,
        help="output file path; relative to campaign root",
    )
    parser.add_argument(
        "--stats",
        action="store_true",
        default=True,
        help="emit suspicious-char and out-of-dictionary stats per block (default on)",
    )
    parser.add_argument(
        "--no-stats",
        dest="stats",
        action="store_false",
        help="suppress per-block stats",
    )
    args = parser.parse_args()

    if args.printed_page is not None:
        sys.exit("printed-page resolution not yet implemented; pass --jp2-leaf for now")

    if not args.abbyy.exists():
        sys.exit(f"missing ABBYY XML: {args.abbyy}")

    target_leaf = args.jp2_leaf
    found = False

    with gzip.open(args.abbyy, "rb") as stream:
        for leaf_index, page in iter_pages(stream):
            if leaf_index != target_leaf:
                continue
            found = True
            page_width = int(page.attrib.get("width", "0"))
            page_height = int(page.attrib.get("height", "0"))

            blocks: list[Block] = []
            for block_el in page.iter(NS + "block"):
                bt = block_el.attrib.get("blockType", "")
                if bt != "Text":
                    continue
                role = classify_block(block_el, page_width, page_height)
                try:
                    coords = (
                        int(block_el.attrib["l"]),
                        int(block_el.attrib["t"]),
                        int(block_el.attrib["r"]),
                        int(block_el.attrib["b"]),
                    )
                except (KeyError, ValueError):
                    continue
                lines, susp, tot, ood, tw = extract_block_text(block_el)
                if not lines:
                    continue
                blocks.append(
                    Block(
                        block_type=bt,
                        role=role,
                        l=coords[0],
                        t=coords[1],
                        r=coords[2],
                        b=coords[3],
                        lines=lines,
                        suspicious_chars=susp,
                        total_chars=tot,
                        out_of_dict_words=ood,
                        total_words=tw,
                    )
                )

            preface = (
                f"# Campanella Metaphysica 1638 — jp2 leaf {leaf_index:04d}\n"
                f"# page dimensions: {page_width} x {page_height}\n"
                f"# block count: {len(blocks)}\n"
                "\n"
            )
            body = render_blocks(blocks, args.stats)
            output = preface + body

            if args.output:
                out_path = Path(args.output)
                if not out_path.is_absolute():
                    out_path = PROJECT_ROOT / out_path
                out_path.parent.mkdir(parents=True, exist_ok=True)
                out_path.write_text(output, encoding="utf-8")
                print(f"wrote leaf {leaf_index:04d} extraction to {out_path}")
            else:
                sys.stdout.write(output)
            break

    if not found:
        sys.exit(f"jp2 leaf {target_leaf} not found in ABBYY stream")


if __name__ == "__main__":
    main()
