#!/usr/bin/env python3
"""Inspect landed JP2 files for count and filename sequence gaps."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DIR = ROOT / "source/page-images/jp2/gesammelteschrif05humbuoft_orig_jp2"
NUMBER_RE = re.compile(r"_(\d+)\.jp2$")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--jp2-dir", type=Path, default=DEFAULT_DIR)
    args = parser.parse_args()

    jp2_dir = args.jp2_dir if args.jp2_dir.is_absolute() else ROOT / args.jp2_dir
    files = sorted(jp2_dir.glob("*.jp2"))
    numbers: list[int] = []
    for path in files:
        match = NUMBER_RE.search(path.name)
        if match:
            numbers.append(int(match.group(1)))

    print(f"directory={jp2_dir.relative_to(ROOT)}")
    print(f"count={len(files)}")
    if numbers:
        numbers.sort()
        gaps = sorted(set(range(numbers[0], numbers[-1] + 1)).difference(numbers))
        print(f"min={numbers[0]}")
        print(f"max={numbers[-1]}")
        print(f"gaps={gaps}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
