#!/usr/bin/env python3
"""Inspect the extracted IA TIF sequence for Kawi Band II."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DIR = ROOT / "source/page-images/tif/berdiekawisprac01buscgoog_tif"
PATTERN = re.compile(r"berdiekawisprac01buscgoog_(\d{4})\.tif$")


def main() -> int:
    files = sorted(DEFAULT_DIR.glob("*.tif"))
    numbers = []
    unmatched = []
    for path in files:
        match = PATTERN.search(path.name)
        if match:
            numbers.append(int(match.group(1)))
        else:
            unmatched.append(path.name)

    if numbers:
        expected = set(range(min(numbers), max(numbers) + 1))
        gaps = sorted(expected - set(numbers))
        print(f"count={len(numbers)}")
        print(f"min={min(numbers)}")
        print(f"max={max(numbers)}")
        print(f"gaps={gaps}")
    else:
        print("count=0")

    if unmatched:
        print(f"unmatched={unmatched}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
