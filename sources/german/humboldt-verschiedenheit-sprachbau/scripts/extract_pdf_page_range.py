#!/usr/bin/env python3
"""Extract a page range from the local Humboldt PDF with pdftotext."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PDF = (
    PROJECT_ROOT
    / "source"
    / "local"
    / "ueber-die-verschiedenheit-des-menschlichen-sprachbaues-band1-1876.pdf"
)


def project_path(path: Path) -> Path:
    if path.is_absolute():
        return path
    return PROJECT_ROOT / path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pdf", type=Path, default=DEFAULT_PDF)
    parser.add_argument("--start", type=int, required=True, help="First PDF page, 1-based.")
    parser.add_argument("--end", type=int, required=True, help="Last PDF page, 1-based.")
    parser.add_argument(
        "--mode",
        choices=["layout", "plain", "raw"],
        default="layout",
        help="pdftotext extraction mode.",
    )
    parser.add_argument("--output", type=Path, help="Output path relative to this source root.")
    args = parser.parse_args()

    pdf = project_path(args.pdf)
    if args.start < 1 or args.end < args.start:
        parser.error("--start must be >= 1 and --end must be >= --start")
    if not pdf.exists():
        parser.error(f"PDF not found: {pdf}")

    command = ["pdftotext", "-enc", "UTF-8"]
    if args.mode == "layout":
        command.append("-layout")
    elif args.mode == "raw":
        command.append("-raw")
    command.extend(["-f", str(args.start), "-l", str(args.end), str(pdf), "-"])

    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
    except FileNotFoundError:
        print("pdftotext is not available on PATH", file=sys.stderr)
        return 127
    except subprocess.CalledProcessError as exc:
        sys.stderr.write(exc.stderr)
        return exc.returncode

    if args.output:
        output = project_path(args.output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(result.stdout, encoding="utf-8")
    else:
        sys.stdout.write(result.stdout)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
