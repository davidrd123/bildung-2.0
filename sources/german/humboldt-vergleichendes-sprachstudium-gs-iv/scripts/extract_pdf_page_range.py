#!/usr/bin/env python3
"""Extract a page range from the local GS IV PDF with pdftotext."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PDF = ROOT / "source/local/gesammelteschrif04humbuoft.pdf"


def root_path(path: Path) -> Path:
    if path.is_absolute():
        return path
    return ROOT / path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pdf", type=Path, default=DEFAULT_PDF)
    parser.add_argument("--start", type=int, required=True)
    parser.add_argument("--end", type=int, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    pdf = root_path(args.pdf)
    if args.start < 1 or args.end < args.start:
        parser.error("--start must be >= 1 and --end must be >= --start")
    if not pdf.exists():
        parser.error(f"PDF not found: {pdf}")

    command = [
        "pdftotext",
        "-layout",
        "-f",
        str(args.start),
        "-l",
        str(args.end),
        str(pdf),
        "-",
    ]
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
    except FileNotFoundError:
        print("pdftotext is not available on PATH", file=sys.stderr)
        return 127
    except subprocess.CalledProcessError as exc:
        sys.stderr.write(exc.stderr)
        return exc.returncode

    if args.output:
        output = root_path(args.output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(result.stdout, encoding="utf-8")
    else:
        sys.stdout.write(result.stdout)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
