#!/usr/bin/env python3
"""Extract a page range from the local Kawi Band II text PDF."""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PDF = ROOT / "source/local/berdiekawisprac01buscgoog_text.pdf"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("start", type=int, help="First PDF page, 1-based.")
    parser.add_argument("end", type=int, help="Last PDF page, inclusive.")
    parser.add_argument("output", type=Path, help="Output text path.")
    parser.add_argument("--pdf", type=Path, default=DEFAULT_PDF)
    parser.add_argument("--layout", action="store_true", default=True)
    args = parser.parse_args()

    args.output.parent.mkdir(parents=True, exist_ok=True)
    command = [
        "pdftotext",
        "-layout",
        "-f",
        str(args.start),
        "-l",
        str(args.end),
        str(args.pdf),
        str(args.output),
    ]
    subprocess.run(command, check=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
