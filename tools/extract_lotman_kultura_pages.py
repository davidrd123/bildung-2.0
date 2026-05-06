#!/usr/bin/env python3

from __future__ import annotations

import argparse
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BOOK_DIR = ROOT / "sources/russian/lotman-kultura-i-vzryv"
SOURCE_DIR = BOOK_DIR / "source"
DJVU_AUTHORITY = SOURCE_DIR / "local/lotman-kultura-i-vzryv.djvu"
RAW_DIR = SOURCE_DIR / "raw"
RAW_PAGES_DIR = RAW_DIR / "pages"
IMAGE_PAGES_DIR = SOURCE_DIR / "page-images/pages"

SECTION_RANGES = [
    ("000-front-matter.txt", 1, 7),
    ("001-postanovka-problemy.txt", 8, 12),
    ("002-sistema-s-odnim-yazykom.txt", 13, 17),
    ("003-postepennyy-progress.txt", 18, 25),
    ("004-preryvnoe-i-nepreryvnoe.txt", 26, 35),
    ("005-semanticheskoe-peresechenie-kak-smyslovoy-vzryv.txt", 36, 44),
    ("006-myslyashchiy-trostnik.txt", 45, 52),
    ("007-mir-sobstvennykh-imen.txt", 53, 64),
    ("008-durak-i-sumasshedshiy.txt", 65, 104),
    ("009-tekst-v-tekste-vstavnaya-glava.txt", 105, 123),
    ("010-perevernutyy-obraz.txt", 124, 176),
    ("011-logika-vzryva.txt", 177, 190),
    ("012-moment-nepredskazuemosti.txt", 191, 205),
    ("013-vnutrennie-struktury-i-vneshnie-vliyaniya.txt", 206, 215),
    ("014-dve-formy-dinamiki.txt", 216, 219),
    ("015-son-semioticheskoe-okno.txt", 220, 227),
    ("016-ya-i-ya.txt", 228, 232),
    ("017-fenomen-iskusstva.txt", 233, 248),
    ("018-konets-kak-zvuchno-eto-slovo.txt", 249, 257),
    ("019-perspektivy.txt", 258, 266),
    ("020-vmesto-vyvodov.txt", 267, 271),
    ("021-contents-and-colophon.txt", 272, 273),
]


def run(command: list[str], **kwargs) -> subprocess.CompletedProcess:
    return subprocess.run(command, check=True, text=True, **kwargs)


def page_count() -> int:
    result = run(["djvused", "-e", "n", str(DJVU_AUTHORITY)], capture_output=True)
    return int(result.stdout.strip())


def page_size(page: int) -> str:
    result = run(
        ["djvused", "-e", f"select {page}; size", str(DJVU_AUTHORITY)],
        capture_output=True,
    )
    return result.stdout.strip()


def extract_page_text(page: int) -> str:
    result = run(
        ["djvutxt", f"--page={page}", str(DJVU_AUTHORITY)],
        capture_output=True,
    )
    text = result.stdout.replace("\r\n", "\n").replace("\r", "\n").strip()
    return f"[scan page {page:03d}]\n\n{text}\n"


def write_raw_pages(count: int) -> dict[int, str]:
    RAW_PAGES_DIR.mkdir(parents=True, exist_ok=True)
    page_texts: dict[int, str] = {}
    full_parts: list[str] = []

    for page in range(1, count + 1):
        page_text = extract_page_text(page)
        page_texts[page] = page_text
        (RAW_PAGES_DIR / f"{page:03d}.txt").write_text(page_text, encoding="utf-8")
        full_parts.append(page_text)

    (RAW_DIR / "full-ocr.txt").write_text("\n".join(full_parts), encoding="utf-8")
    return page_texts


def write_raw_sections(page_texts: dict[int, str]) -> None:
    for filename, first_page, last_page in SECTION_RANGES:
        section_text = "\n".join(
            page_texts[page] for page in range(first_page, last_page + 1)
        )
        (RAW_DIR / filename).write_text(section_text, encoding="utf-8")


def render_page_png(page: int) -> None:
    IMAGE_PAGES_DIR.mkdir(parents=True, exist_ok=True)
    target = IMAGE_PAGES_DIR / f"{page:03d}.png"

    with tempfile.TemporaryDirectory(prefix="lotman-kultura-page-") as tmpdir:
        pnm_path = Path(tmpdir) / f"{page:03d}.pnm"
        run(
            [
                "ddjvu",
                "-format=pnm",
                f"-page={page}",
                str(DJVU_AUTHORITY),
                str(pnm_path),
            ],
            capture_output=True,
        )
        with target.open("wb") as png:
            subprocess.run(["pnmtopng", str(pnm_path)], check=True, stdout=png)


def render_images(count: int) -> None:
    for page in range(1, count + 1):
        render_page_png(page)


def write_metadata(count: int) -> None:
    first_size = page_size(1)
    last_size = page_size(count)
    metadata = f"""# Lotman Kultura i vzryv raw extraction metadata.
---
authority:
  file: "../local/lotman-kultura-i-vzryv.djvu"
  format: "DjVu bundled scan with hidden OCR text"
  page_count: {count}
  first_page_size: "{first_size}"
  last_page_size: "{last_size}"
extraction:
  generated_by: "tools/extract_lotman_kultura_pages.py"
  raw_pages: "pages/NNN.txt"
  raw_sections: "NNN-section-slug.txt"
  combined_ocr: "full-ocr.txt"
  page_markers: "[scan page NNN]"
image_rendering:
  generated_by: "tools/extract_lotman_kultura_pages.py --images"
  output: "../page-images/pages/NNN.png"
  status: "local gitignored proof aid"
"""
    (RAW_DIR / "metadata.yaml").write_text(metadata, encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Extract raw page OCR and optional PNG proof images for Lotman Kultura i vzryv."
    )
    parser.add_argument(
        "--images",
        action="store_true",
        help="Also render all DjVu pages to gitignored PNG proof images.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not DJVU_AUTHORITY.exists():
        raise FileNotFoundError(DJVU_AUTHORITY)

    count = page_count()
    page_texts = write_raw_pages(count)
    write_raw_sections(page_texts)
    write_metadata(count)

    if args.images:
        render_images(count)

    image_note = " and rendered PNG page images" if args.images else ""
    print(f"Extracted {count} OCR pages{image_note} for {BOOK_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
