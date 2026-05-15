#!/usr/bin/env python3
"""Scrape the ABBYY-validated Latin lexicon from the IA-shipped XML.

ABBYY FineReader tags each character with a `wordFromDictionary` flag indicating
whether the surrounding word was recognized by its Latin dictionary. By
collecting every distinct word with that flag set across all 972 leaves of the
Campanella volume, we get a corpus-specific Latin lexicon usable as a validator
for the long-s repair pass.

The output is one word per line, lowercased, ASCII-normalized, sorted. It is
stable across runs and lives under `source/local/` (gitignored).
"""

from __future__ import annotations

import argparse
import gzip
import sys
import unicodedata
import xml.etree.ElementTree as ET
from pathlib import Path

NS = "{http://www.abbyy.com/FineReader_xml/FineReader10-schema-v1.xml}"
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ABBYY = PROJECT_ROOT / "source" / "local" / "thomcampanellsty00camp_abbyy.gz"
DEFAULT_OUT = PROJECT_ROOT / "source" / "local" / "abbyy-lexicon.txt"


def normalize_token(token: str) -> str:
    """Lowercase + strip accents + drop non-letters for lexicon storage."""
    decomposed = unicodedata.normalize("NFKD", token.lower())
    return "".join(c for c in decomposed if c.isalpha() and ord(c) < 128)


def scrape(xml_gz: Path, progress_every: int = 50) -> set[str]:
    lex: set[str] = set()
    pages = 0
    in_dict_words = 0
    total_words = 0

    with gzip.open(xml_gz, "rb") as stream:
        for event, elem in ET.iterparse(stream, events=("end",)):
            if elem.tag != NS + "page":
                continue
            pages += 1

            # Walk charParams inside this page, grouping by wordFirst markers
            chars: list[str] = []
            in_dict = False
            had_word = False

            for cp in elem.iter(NS + "charParams"):
                if cp.attrib.get("wordFirst") == "1":
                    if had_word:
                        total_words += 1
                        if in_dict:
                            tok = normalize_token("".join(chars))
                            if tok and len(tok) > 1:
                                lex.add(tok)
                                in_dict_words += 1
                    chars = []
                    had_word = True
                    in_dict = cp.attrib.get("wordFromDictionary") == "1"
                ch = cp.text or ""
                chars.append(ch)

            if had_word:
                total_words += 1
                if in_dict:
                    tok = normalize_token("".join(chars))
                    if tok and len(tok) > 1:
                        lex.add(tok)
                        in_dict_words += 1

            elem.clear()
            if pages % progress_every == 0:
                print(
                    f"  ... {pages} pages, {total_words} words seen, "
                    f"{in_dict_words} in-dict, {len(lex)} unique",
                    file=sys.stderr,
                )

    print(
        f"done: {pages} pages, {total_words} words, "
        f"{in_dict_words} in-dict, {len(lex)} unique lexicon entries",
        file=sys.stderr,
    )
    return lex


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--abbyy", type=Path, default=DEFAULT_ABBYY)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    if not args.abbyy.exists():
        sys.exit(f"missing ABBYY XML: {args.abbyy}")

    lex = scrape(args.abbyy)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n".join(sorted(lex)) + "\n", encoding="utf-8")
    print(f"wrote {len(lex)} unique words to {args.output}")


if __name__ == "__main__":
    main()
