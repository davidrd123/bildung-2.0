#!/usr/bin/env python3

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PDF_AUTHORITY = ROOT / (
    "sources/modern/incoming/books/"
    "Philosophie der Mathematik und Naturwissenschaft, 8_ Auflage -- Herrmann Weyl.pdf"
)
SOURCE_DIR = ROOT / "sources/modern/weyl-philosophie-der-mathematik-und-naturwissenschaft/source"
FULL_PATH = SOURCE_DIR / "full/text-layer.txt"
TEXT_LAYER_DIR = SOURCE_DIR / "text-layer/pages"
PAGES_PATH = SOURCE_DIR / "pages.yaml"
IMAGE_MANIFEST_PATH = SOURCE_DIR / "page-images.yaml"
DEFAULT_PAGE_COUNT = 407


def yaml_quote(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def run(cmd: list[str]) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def page_count() -> tuple[int, list[str]]:
    try:
        proc = run(["pdfinfo", str(PDF_AUTHORITY)])
    except (FileNotFoundError, subprocess.CalledProcessError):
        return DEFAULT_PAGE_COUNT, ["pdfinfo unavailable; using known page count"]

    warnings = [
        line.strip()
        for line in proc.stderr.decode("utf-8", errors="replace").splitlines()
        if line.strip()
    ]
    for line in proc.stdout.decode("utf-8", errors="replace").splitlines():
        if line.startswith("Pages:"):
            return int(line.split(":", 1)[1].strip()), warnings
    return DEFAULT_PAGE_COUNT, warnings + ["pdfinfo did not report page count; using known page count"]


def split_pdf_text(expected_pages: int) -> tuple[list[str], list[str]]:
    try:
        proc = run(["pdftotext", "-layout", str(PDF_AUTHORITY), "-"])
    except FileNotFoundError as exc:
        raise SystemExit("pdftotext is required to regenerate this scaffold") from exc

    warnings = [
        line.strip()
        for line in proc.stderr.decode("utf-8", errors="replace").splitlines()
        if line.strip()
    ]
    text = (
        proc.stdout.decode("utf-8", errors="replace")
        .replace("\x08", "")
        .replace("\xad", "")
    )
    pages = text.split("\f")
    if len(pages) == expected_pages + 1 and not pages[-1].strip():
        pages = pages[:-1]
    if len(pages) < expected_pages:
        pages.extend([""] * (expected_pages - len(pages)))
    if len(pages) > expected_pages:
        warnings.append(
            f"pdftotext returned {len(pages)} pages for {expected_pages} PDF pages; keeping first {expected_pages}"
        )
        pages = pages[:expected_pages]
    return pages, warnings


def write_text_layer() -> None:
    expected_pages, pdf_warnings = page_count()
    pages, text_warnings = split_pdf_text(expected_pages)

    FULL_PATH.parent.mkdir(parents=True, exist_ok=True)
    TEXT_LAYER_DIR.mkdir(parents=True, exist_ok=True)

    full_chunks = []
    page_entries = []
    for page_number, page in enumerate(pages, 1):
        page = page.rstrip()
        nonblank_lines = [line for line in page.splitlines() if line.strip()]
        rel_text_file = None
        if nonblank_lines:
            text_path = TEXT_LAYER_DIR / f"page-{page_number:04d}.txt"
            text_path.write_text(page + "\n", encoding="utf-8")
            rel_text_file = text_path.relative_to(SOURCE_DIR).as_posix()

        full_chunks.extend([f"===== PDF page {page_number:04d} =====", page, ""])
        page_entries.append(
            {
                "page": page_number,
                "text_file": rel_text_file,
                "has_text_layer": bool(nonblank_lines),
                "char_count": len(page),
                "nonblank_line_count": len(nonblank_lines),
            }
        )

    FULL_PATH.write_text("\n".join(full_chunks).rstrip() + "\n", encoding="utf-8")
    write_pages_manifest(expected_pages, pdf_warnings + text_warnings, page_entries)


def write_pages_manifest(
    expected_pages: int,
    warnings: list[str],
    page_entries: list[dict[str, object]],
) -> None:
    warnings = list(dict.fromkeys(warnings))
    lines = [
        "book:",
        '  title: "Philosophie der Mathematik und Naturwissenschaft"',
        '  author: "Hermann Weyl"',
        '  edition: "8. Auflage"',
        f'  source_pdf: "{PDF_AUTHORITY.relative_to(ROOT).as_posix()}"',
        f'  extracted_full_text: "{FULL_PATH.relative_to(SOURCE_DIR).as_posix()}"',
        f"  pdf_page_count: {expected_pages}",
        "  extraction_notes:",
        '    - "The embedded text layer covers only the publisher/title pages; the body is image-only."',
        '    - "Use source/page-images/ for direct page inspection and OCR input."',
        '    - "source/full/, source/page-images/, and source/ocr/ are local generated outputs and gitignored."',
    ]
    if warnings:
        lines.append("  extraction_warnings:")
        for warning in warnings:
            lines.append(f"    - {yaml_quote(warning)}")
    lines.append("pages:")
    for entry in page_entries:
        text_file = entry["text_file"]
        text_repr = "null" if text_file is None else yaml_quote(str(text_file))
        has_text = "true" if entry["has_text_layer"] else "false"
        lines.extend(
            [
                f'  - pdf_page: {entry["page"]}',
                f"    text_layer_file: {text_repr}",
                f"    has_text_layer: {has_text}",
                f'    char_count: {entry["char_count"]}',
                f'    nonblank_line_count: {entry["nonblank_line_count"]}',
            ]
        )
    PAGES_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_image_manifest(first: int, last: int, dpi: int, image_format: str) -> None:
    ext = "jpg" if image_format == "jpeg" else "png"
    rel_dir = f"page-images/{ext}-{dpi}"
    lines = [
        "image_set:",
        f'  source_pdf: "{PDF_AUTHORITY.relative_to(ROOT).as_posix()}"',
        f"  first_pdf_page: {first}",
        f"  last_pdf_page: {last}",
        f"  dpi: {dpi}",
        f'  format: "{image_format}"',
        f'  directory: "{rel_dir}"',
        f'  filename_pattern: "page-%04d.{ext}"',
        "  notes:",
        '    - "Generated page images are local-only and gitignored."',
        '    - "Use these as the visual authority for OCR correction and direct inspection."',
    ]
    IMAGE_MANIFEST_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def extract_page_images(first: int, last: int, dpi: int, image_format: str, overwrite: bool) -> None:
    expected_pages, _ = page_count()
    first = max(1, first)
    last = min(expected_pages, last)
    if first > last:
        raise SystemExit(f"invalid image page range: {first}-{last}")

    ext = "jpg" if image_format == "jpeg" else "png"
    out_dir = SOURCE_DIR / f"page-images/{ext}-{dpi}"
    out_dir.mkdir(parents=True, exist_ok=True)

    for page_number in range(first, last + 1):
        out_file = out_dir / f"page-{page_number:04d}.{ext}"
        if out_file.exists() and not overwrite:
            continue
        prefix = out_dir / f"page-{page_number:04d}"
        cmd = [
            "pdftoppm",
            "-singlefile",
            "-f",
            str(page_number),
            "-l",
            str(page_number),
            "-r",
            str(dpi),
        ]
        if image_format == "jpeg":
            cmd.extend(["-jpeg", "-jpegopt", "quality=90"])
        else:
            cmd.append("-png")
        cmd.extend([str(PDF_AUTHORITY), str(prefix)])
        try:
            run(cmd)
        except FileNotFoundError as exc:
            raise SystemExit("pdftoppm is required to extract page images") from exc

    write_image_manifest(first, last, dpi, image_format)


def available_tesseract_languages() -> set[str]:
    try:
        proc = run(["tesseract", "--list-langs"])
    except (FileNotFoundError, subprocess.CalledProcessError):
        return set()
    return {
        line.strip()
        for line in proc.stdout.decode("utf-8", errors="replace").splitlines()
        if line.strip() and not line.startswith("List of available languages")
    }


def run_ocr(first: int, last: int, dpi: int, image_format: str, lang: str, overwrite: bool) -> None:
    languages = available_tesseract_languages()
    if lang not in languages:
        available = ", ".join(sorted(languages)) or "none"
        raise SystemExit(f"tesseract language '{lang}' is unavailable; installed languages: {available}")

    expected_pages, _ = page_count()
    first = max(1, first)
    last = min(expected_pages, last)
    ext = "jpg" if image_format == "jpeg" else "png"
    image_dir = SOURCE_DIR / f"page-images/{ext}-{dpi}"
    ocr_dir = SOURCE_DIR / f"ocr/tesseract-{lang}/pages"
    ocr_dir.mkdir(parents=True, exist_ok=True)

    for page_number in range(first, last + 1):
        image_path = image_dir / f"page-{page_number:04d}.{ext}"
        if not image_path.exists():
            raise SystemExit(f"missing image for OCR: {image_path}")
        out_base = ocr_dir / f"page-{page_number:04d}"
        out_file = out_base.with_suffix(".txt")
        if out_file.exists() and not overwrite:
            continue
        try:
            run(["tesseract", str(image_path), str(out_base), "-l", lang])
        except FileNotFoundError as exc:
            raise SystemExit("tesseract is required to run OCR") from exc


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skip-text", action="store_true", help="do not refresh embedded text-layer files")
    parser.add_argument("--images", action="store_true", help="extract page images for direct inspection")
    parser.add_argument("--ocr", action="store_true", help="run tesseract OCR over extracted page images")
    parser.add_argument("--first", type=int, default=1, help="first PDF page for image/OCR work")
    parser.add_argument("--last", type=int, default=DEFAULT_PAGE_COUNT, help="last PDF page for image/OCR work")
    parser.add_argument("--dpi", type=int, default=200, help="page image resolution")
    parser.add_argument("--format", choices=["jpeg", "png"], default="jpeg", help="page image format")
    parser.add_argument("--ocr-lang", default="deu", help="tesseract OCR language")
    parser.add_argument("--overwrite", action="store_true", help="overwrite generated images/OCR outputs")
    args = parser.parse_args()

    if not args.skip_text:
        write_text_layer()
    if args.images:
        extract_page_images(args.first, args.last, args.dpi, args.format, args.overwrite)
    if args.ocr:
        run_ocr(args.first, args.last, args.dpi, args.format, args.ocr_lang, args.overwrite)


if __name__ == "__main__":
    main()
