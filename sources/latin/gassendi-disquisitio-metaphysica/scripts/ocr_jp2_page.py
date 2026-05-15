#!/usr/bin/env python3
"""OCR one preferred JP2 page with Tesseract.

The defaults are tuned for the version2 historical Antiqua scan. Use Fraktur or
plain Latin passes as secondary witnesses when a glyph remains ambiguous.
"""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[4]
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JP2_DIR = PROJECT_ROOT / "source" / "page-images" / "jp2"
DEFAULT_PREFIX = "ned-kbn-all-00004327-001"


def resolve_output(raw_path: str) -> Path:
    path = Path(raw_path)
    return path if path.is_absolute() else PROJECT_ROOT / path


def image_from_index(index: int) -> Path:
    return DEFAULT_JP2_DIR / f"{DEFAULT_PREFIX}_{index:04d}.jp2"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--page-index", type=int, help="zero-padded JP2 index, for example 138")
    source.add_argument("--image", type=Path, help="explicit JP2 image path")
    parser.add_argument("--output", type=str, help="output file path; relative to campaign root")
    parser.add_argument("--lang", default="script/Latin", help="Tesseract language")
    parser.add_argument("--psm", default="4", help="Tesseract page segmentation mode")
    parser.add_argument(
        "--format",
        choices=["txt", "hocr", "tsv"],
        default="txt",
        help="Tesseract output format",
    )
    parser.add_argument(
        "--no-preserve-spaces",
        action="store_true",
        help="omit preserve_interword_spaces=1",
    )
    args = parser.parse_args()

    image = args.image if args.image else image_from_index(args.page_index)
    if not image.exists():
        raise SystemExit(f"missing JP2 image: {image}")

    command = ["tesseract", str(image), "stdout", "--oem", "1", "--psm", args.psm, "-l", args.lang]
    if not args.no_preserve_spaces:
        command.extend(["-c", "preserve_interword_spaces=1"])
    if args.format != "txt":
        command.append(args.format)
    result = subprocess.run(command, capture_output=True, text=True, check=True)

    if args.output:
        output_path = resolve_output(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(result.stdout, encoding="utf-8")
        try:
            label = output_path.relative_to(REPO_ROOT)
        except ValueError:
            label = output_path
        print(f"wrote OCR for {image.name} to {label}")
        return

    print(result.stdout, end="")


if __name__ == "__main__":
    main()
