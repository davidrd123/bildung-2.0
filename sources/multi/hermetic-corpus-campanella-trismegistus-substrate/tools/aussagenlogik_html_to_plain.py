#!/usr/bin/env python3
"""Extract the WordPress entry text from archived Aussagenlogik pages."""

from __future__ import annotations

import argparse
import re
from html.parser import HTMLParser
from pathlib import Path


BLOCK_TAGS = {
    "blockquote",
    "br",
    "center",
    "div",
    "h1",
    "h2",
    "h3",
    "h4",
    "li",
    "p",
    "table",
    "td",
    "th",
    "tr",
}


class EntryTextParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.in_entry = False
        self.entry_depth = 0
        self.done = False
        self.chunks: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if self.done:
            return

        attr_map = {key: value or "" for key, value in attrs}
        classes = set(attr_map.get("class", "").split())
        if not self.in_entry and tag == "div" and "entrytext" in classes:
            self.in_entry = True
            self.entry_depth = 1
            return

        if self.in_entry:
            if tag == "div":
                self.entry_depth += 1
            if tag in BLOCK_TAGS:
                self.chunks.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if not self.in_entry or self.done:
            return

        if tag in BLOCK_TAGS:
            self.chunks.append("\n")
        if tag == "div":
            self.entry_depth -= 1
            if self.entry_depth == 0:
                self.in_entry = False
                self.done = True

    def handle_data(self, data: str) -> None:
        if self.in_entry and not self.done:
            self.chunks.append(data)


def normalize(text: str) -> str:
    lines = []
    for line in text.splitlines():
        cleaned = re.sub(r"\s+", " ", line).strip()
        if cleaned:
            lines.append(cleaned)
    return "\n".join(lines).strip() + "\n"


def convert(input_path: Path, output_path: Path, title: str) -> None:
    parser = EntryTextParser()
    parser.feed(input_path.read_text(encoding="utf-8", errors="replace"))
    body = normalize("".join(parser.chunks))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        f"# {title}\n\nSource HTML: `{input_path.name}`\n\n{body}",
        encoding="utf-8",
    )


def main() -> None:
    argparser = argparse.ArgumentParser()
    argparser.add_argument("input", type=Path)
    argparser.add_argument("output", type=Path)
    argparser.add_argument("--title", required=True)
    args = argparser.parse_args()
    convert(args.input, args.output, args.title)


if __name__ == "__main__":
    main()
