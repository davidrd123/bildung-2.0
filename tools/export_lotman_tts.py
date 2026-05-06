#!/usr/bin/env python3

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "sources/russian/lotman-vnutri-mislyashih-mirov/source"
READER_DIR = SOURCE_DIR / "reader-en"
TTS_DIR = SOURCE_DIR / "tts"

NUMBER_WORDS = {
    "1": "one",
    "2": "two",
    "3": "three",
}


def reader_files() -> list[Path]:
    return sorted(
        path
        for path in READER_DIR.glob("*.md")
        if path.name != "README.md"
    )


def seq_for(path: Path) -> int:
    match = re.match(r"^(\d+)-", path.name)
    if not match:
        raise ValueError(f"cannot infer sequence from {path.name}")
    return int(match.group(1))


def strip_reader_to_tts(text: str, source_name: str) -> str:
    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")

    try:
        body_start = next(i for i, line in enumerate(lines) if line.startswith("## "))
    except StopIteration as exc:
        raise ValueError(f"{source_name}: no speakable heading found") from exc

    try:
        pass_notes = next(i for i, line in enumerate(lines) if line == "## Pass Notes")
    except StopIteration as exc:
        raise ValueError(f"{source_name}: no Pass Notes boundary found") from exc

    if pass_notes <= body_start:
        raise ValueError(f"{source_name}: Pass Notes appears before body")

    body = lines[body_start:pass_notes]
    while body and not body[-1].strip():
        body.pop()

    if body and body[0].startswith("## "):
        body[0] = "# " + body[0][3:]

    tts_text = "\n".join(line.rstrip() for line in body).strip()
    return normalize_for_speech(tts_text) + "\n"


def expand_letter_number(match: re.Match[str]) -> str:
    letter = match.group(1)
    number = match.group(2)
    return f"{letter} {NUMBER_WORDS[number]}"


def normalize_for_speech(text: str) -> str:
    """Expand compact notation that reads poorly in raw TTS."""
    replacements = {
        '"I - HE"': '"I to he"',
        '"I - I"': '"I to I"',
        '"I - he/she"': '"I to he or she"',
        '"I - you"': '"I to you"',
        '"HE"': '"he"',
        "Author - Audience, Design - Text": "Author and Audience, Design and Text",
        "Theme - Devices of Expressiveness - Text": (
            "Theme, Devices of Expressiveness, and Text"
        ),
        "context,\nmessage,\naddresser to addressee,\ncontact,\ncode.": (
            "context; message; addresser to addressee; contact; code."
        ),
        "context,\nshift of context,\nmessage 1 becomes message 2,\ncode 1 becomes code 2.": (
            "context; shift of context; message one becomes message two; "
            "code one becomes code two."
        ),
    }

    for source, target in replacements.items():
        text = text.replace(source, target)

    text = re.sub(r'"I\s+-\s+HE"', '"I to he"', text)
    text = re.sub(r'"I\s+-\s+I"', '"I to I"', text)
    text = re.sub(r'"I\s+-\s+he/she"', '"I to he or she"', text)
    text = re.sub(r'"I\s+-\s+you"', '"I to you"', text)
    text = re.sub(r'"I\s+-\s+HE([,.;:])"', r'"I to he\1"', text)
    text = re.sub(r'"I\s+-\s+I([,.;:])"', r'"I to I\1"', text)
    text = re.sub(r'"I\s+-\s+he/she([,.;:])"', r'"I to he or she\1"', text)
    text = re.sub(r'"I\s+-\s+you([,.;:])"', r'"I to you\1"', text)
    text = re.sub(r"\bmessage 1\b", "message one", text)
    text = re.sub(r"\bmessage 2\b", "message two", text)
    text = re.sub(r"\bcode 1\b", "code one", text)
    text = re.sub(r"\bcode 2\b", "code two", text)
    text = re.sub(r"\b([TLKk])([123])\b", expand_letter_number, text)
    text = re.sub(r"\b([Tk])n\b", r"\1 n", text)
    text = text.replace(
        'formed by communicative systems of the "I to he" and "I to I" types. Incidentally,',
        'formed by communicative systems of the "I to he" and "I to I" types.\n'
        "Incidentally,",
    )

    return text


def build_manifest(exports: list[tuple[int, str]]) -> str:
    lines = [
        "# TTS export manifest.",
        "# Access layer only; generated from reader-en drafts.",
        "---",
        "pass:",
        "  name: lotman-vnutri-tts",
        "  status: active",
        '  purpose: "Audio-ready derivatives of reader-en drafts"',
        '  source_reader_manifest: "../reader-en/manifest.yaml"',
        '  generated_by: "tools/export_lotman_tts.py"',
        '  cleanup_rule: "strip reader metadata and Pass Notes; preserve speakable headings and reading text; expand compact notation and schematic labels for speech"',
        '  apparatus_boundary: "tts exports do not seed glossary, handles, threads, or encounter claims"',
        "exports:",
    ]

    for seq, filename in exports:
        lines.extend(
            [
                f"  - seq: {seq}",
                f'    source_reader: "../reader-en/{filename}"',
                f'    tts_file: "{filename}"',
                "    status: exported",
                '    note: "metadata and pass notes stripped; speech hazards normalized; generated from reader-en"',
            ]
        )

    return "\n".join(lines) + "\n"


def main() -> int:
    TTS_DIR.mkdir(parents=True, exist_ok=True)

    exports: list[tuple[int, str]] = []
    for source_path in reader_files():
        text = source_path.read_text(encoding="utf-8")
        tts_text = strip_reader_to_tts(text, source_path.name)
        target_path = TTS_DIR / source_path.name
        target_path.write_text(tts_text, encoding="utf-8")
        exports.append((seq_for(source_path), source_path.name))

    (TTS_DIR / "manifest.yaml").write_text(build_manifest(exports), encoding="utf-8")
    print(f"Wrote {len(exports)} TTS files to {TTS_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
