#!/usr/bin/env python3
"""OCR one JP2 page image with Tesseract."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JP2_DIR = PROJECT_ROOT / "source" / "page-images" / "jp2"


def project_path(path: Path) -> Path:
    if path.is_absolute():
        return path
    return PROJECT_ROOT / path


def find_page_image(jp2_dir: Path, page_index: int, prefix: str | None) -> Path:
    suffix = f"{page_index:04d}.jp2"
    if prefix:
        candidate = jp2_dir / f"{prefix}{suffix}"
        if candidate.exists():
            return candidate
        raise FileNotFoundError(candidate)

    matches = sorted(jp2_dir.rglob(f"*{suffix}"))
    if len(matches) == 1:
        return matches[0]
    if not matches:
        raise FileNotFoundError(f"no JP2 ending in {suffix} under {jp2_dir}")
    raise RuntimeError(f"multiple JP2 files ending in {suffix}; pass --prefix or --image")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--image", type=Path, help="Explicit JP2 image path.")
    parser.add_argument("--jp2-dir", type=Path, default=DEFAULT_JP2_DIR)
    parser.add_argument("--page-index", type=int, help="Zero-based physical leaf index.")
    parser.add_argument("--prefix", help="Filename prefix before the zero-padded page index.")
    parser.add_argument("--lang", default="frk+deu", help="Tesseract language code.")
    parser.add_argument("--psm", default="4", help="Tesseract page segmentation mode.")
    parser.add_argument("--output", type=Path, help="Output path relative to this source root.")
    parser.add_argument("--format", choices=["txt", "hocr", "tsv"], default="txt")
    args = parser.parse_args()

    if args.image:
        image = project_path(args.image)
    else:
        if args.page_index is None:
            parser.error("pass --image or --page-index")
        jp2_dir = project_path(args.jp2_dir)
        try:
            image = find_page_image(jp2_dir, args.page_index, args.prefix)
        except (FileNotFoundError, RuntimeError) as exc:
            parser.error(str(exc))

    if not image.exists():
        parser.error(f"image not found: {image}")

    command = [
        "tesseract",
        str(image),
        "stdout",
        "--oem",
        "1",
        "--psm",
        args.psm,
        "-l",
        args.lang,
        "-c",
        "preserve_interword_spaces=1",
    ]
    if args.format != "txt":
        command.append(args.format)

    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
    except FileNotFoundError:
        print("tesseract is not available on PATH", file=sys.stderr)
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
