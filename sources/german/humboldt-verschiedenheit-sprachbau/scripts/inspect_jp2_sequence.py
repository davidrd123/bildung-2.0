#!/usr/bin/env python3
"""Inspect landed JP2 page-image files for count, prefixes, and gaps."""

from __future__ import annotations

import argparse
import re
from collections import defaultdict
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JP2_DIR = PROJECT_ROOT / "source" / "page-images" / "jp2"
NUMBERED_STEM = re.compile(r"^(?P<prefix>.*?)(?P<number>\d+)$")


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(PROJECT_ROOT))
    except ValueError:
        return str(path)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--jp2-dir",
        type=Path,
        default=DEFAULT_JP2_DIR,
        help="JP2 directory to inspect. Defaults to source/page-images/jp2.",
    )
    args = parser.parse_args()

    jp2_dir = args.jp2_dir
    if not jp2_dir.is_absolute():
        jp2_dir = PROJECT_ROOT / jp2_dir

    files = sorted(jp2_dir.rglob("*.jp2"))
    print(f"directory: {rel(jp2_dir)}")
    print(f"jp2_files: {len(files)}")

    if not files:
        return 0

    print("first_files:")
    for path in files[:5]:
        print(f"  - {rel(path)}")
    print("last_files:")
    for path in files[-5:]:
        print(f"  - {rel(path)}")

    groups: dict[str, list[int]] = defaultdict(list)
    unparsed: list[Path] = []
    for path in files:
        match = NUMBERED_STEM.match(path.stem)
        if not match:
            unparsed.append(path)
            continue
        groups[match.group("prefix")].append(int(match.group("number")))

    if groups:
        print("numbered_prefixes:")
    for prefix, numbers in sorted(groups.items(), key=lambda item: len(item[1]), reverse=True):
        numbers = sorted(numbers)
        expected = set(range(numbers[0], numbers[-1] + 1))
        gaps = sorted(expected.difference(numbers))
        print(f"  - prefix: {prefix!r}")
        print(f"    count: {len(numbers)}")
        print(f"    min_index: {numbers[0]}")
        print(f"    max_index: {numbers[-1]}")
        print(f"    gaps: {gaps[:25]}")
        if len(gaps) > 25:
            print(f"    gaps_omitted: {len(gaps) - 25}")

    if unparsed:
        print("unparsed_files:")
        for path in unparsed[:25]:
            print(f"  - {rel(path)}")
        if len(unparsed) > 25:
            print(f"  - ... {len(unparsed) - 25} more")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
