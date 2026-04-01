#!/usr/bin/env python3
"""Extract a PDF page range from Cassirer's volume into plain text."""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
PROJECT_ROOT = REPO_ROOT / "texts" / "erkenntnisproblem-vol1"
DEFAULT_PDF = (
    REPO_ROOT
    / "books"
    / "Erkenntnisproblem"
    / "Vol1"
    / "daserkenntnispro01cass.pdf"
)


def resolve_output(raw_path: str) -> Path:
    path = Path(raw_path)
    return path if path.is_absolute() else PROJECT_ROOT / path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start", type=int, required=True, help="first PDF page")
    parser.add_argument("--end", type=int, required=True, help="last PDF page")
    parser.add_argument(
        "--pdf",
        type=Path,
        default=DEFAULT_PDF,
        help="path to the source PDF",
    )
    parser.add_argument(
        "--output",
        type=str,
        help="output file path; relative paths are resolved from the project root",
    )
    parser.add_argument(
        "--mode",
        choices=["raw", "plain", "layout"],
        default="raw",
        help="`pdftotext` extraction mode; `raw` is the default because it preserves reading order better on this scan",
    )
    args = parser.parse_args()

    if args.start < 1 or args.end < args.start:
        raise SystemExit("invalid page range")
    if not args.pdf.exists():
        raise SystemExit(f"missing PDF: {args.pdf}")

    command = ["pdftotext"]
    if args.mode == "raw":
        command.append("-raw")
    elif args.mode == "layout":
        command.append("-layout")

    command.extend(
        [
            "-f",
            str(args.start),
            "-l",
            str(args.end),
            str(args.pdf),
            "-",
        ]
    )
    result = subprocess.run(command, capture_output=True, text=True, check=True)

    if args.output:
        output_path = resolve_output(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(result.stdout, encoding="utf-8")
        try:
            label = output_path.relative_to(REPO_ROOT)
        except ValueError:
            label = output_path
        print(f"wrote PDF pages {args.start}-{args.end} ({args.mode}) to {label}")
        return

    print(result.stdout, end="")


if __name__ == "__main__":
    main()
