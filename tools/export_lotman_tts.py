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

TTS_FILENAMES = {
    "002-ivanov-semisfera-i-istoriya.md": "002-front-ivanov-semiosphere-and-history.md",
    "003-intro-01-vvodnye-zamechaniya.md": "003-intro-01-introductory-remarks.md",
    "004-intro-02-posle-sossyura.md": "004-intro-02-after-saussure.md",
    "005-part-i-01-tri-funktsii-teksta.md": "005-part-i-01-three-functions-of-the-text.md",
    "006-part-i-02-avtokommunikatsiya.md": "006-part-i-02-autocommunication.md",
    "007-part-i-03-ritorika-smysloporozhdeniya.md": "007-part-i-03-rhetoric-of-meaning-generation.md",
    "008-part-i-04-ikonicheskaya-ritorika.md": "008-part-i-04-iconic-rhetoric.md",
    "009-part-i-05-tekst-v-protsesse-dvizheniya.md": "009-part-i-05-text-in-motion-author-audience-design-text.md",
    "010-part-i-06-simvol-gen-syuzheta.md": "010-part-i-06-symbol-as-plot-gene.md",
    "011-part-i-07-simvol-v-sisteme-kultury.md": "011-part-i-07-symbol-in-the-system-of-culture.md",
    "012-part-ii-01-semioticheskoe-prostranstvo.md": "012-part-ii-01-semiotic-space.md",
    "013-part-ii-02-ponyatie-granitsy.md": "013-part-ii-02-the-concept-of-boundary.md",
    "014-part-ii-03-mekhanizmy-dialoga.md": "014-part-ii-03-mechanisms-of-dialogue.md",
    "015-part-ii-04-semiosfera-i-problema-syuzheta.md": "015-part-ii-04-semiosphere-and-the-problem-of-plot.md",
    "017-part-ii-05-01-geograficheskoe-prostranstvo.md": "017-part-ii-05-01-geographical-space.md",
    "018-part-ii-05-02-puteshestvie-ulissa.md": "018-part-ii-05-02-ulysses-journey.md",
    "019-part-ii-05-03-dom-v-mastere-i-margarite.md": "019-part-ii-05-03-the-house-in-the-master-and-margarita.md",
    "020-part-ii-05-04-simvolika-peterburga.md": "020-part-ii-05-04-symbolism-of-petersburg.md",
    "021-part-ii-06-nekotorye-itogi.md": "021-part-ii-06-some-conclusions.md",
    "022-part-iii-01-problema-istoricheskogo-fakta.md": "022-part-iii-01-the-problem-of-the-historical-fact.md",
    "023-part-iii-02-istoricheskie-zakonomernosti-i-struktura-teksta.md": "023-part-iii-02-historical-laws-and-the-structure-of-text.md",
    "024-part-iii-03-alternativnyy-variant-bespismennaya-kultura.md": "024-part-iii-03-alternative-case-non-written-culture.md",
    "025-part-iii-04-o-roli-tipologicheskikh-simvolov.md": "025-part-iii-04-role-of-typological-symbols.md",
    "026-part-iii-05-vozmozhna-li-istoricheskaya-nauka.md": "026-part-iii-05-is-historical-science-possible.md",
    "027-back-matter-conclusion.md": "027-conclusion.md",
    "029-appendix-01-umberto-eco.md": "029-appendix-01-umberto-eco.md",
    "030-appendix-02-gasparov-lotman-i-marksizm.md": "030-appendix-02-gasparov-lotman-and-marxism.md",
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


def tts_filename_for(path: Path) -> str:
    try:
        return TTS_FILENAMES[path.name]
    except KeyError as exc:
        raise ValueError(f"no TTS filename mapping for {path.name}") from exc


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


def remove_stale_tts_files(expected_filenames: set[str]) -> None:
    for path in TTS_DIR.glob("*.md"):
        if path.name != "README.md" and path.name not in expected_filenames:
            path.unlink()


def build_manifest(exports: list[tuple[int, str, str]]) -> str:
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

    for seq, source_filename, tts_filename in exports:
        lines.extend(
            [
                f"  - seq: {seq}",
                f'    source_reader: "../reader-en/{source_filename}"',
                f'    tts_file: "{tts_filename}"',
                "    status: exported",
                '    note: "metadata and pass notes stripped; speech hazards normalized; generated from reader-en"',
            ]
        )

    return "\n".join(lines) + "\n"


def main() -> int:
    TTS_DIR.mkdir(parents=True, exist_ok=True)

    sources = reader_files()
    expected_filenames = {tts_filename_for(source_path) for source_path in sources}
    remove_stale_tts_files(expected_filenames)

    exports: list[tuple[int, str, str]] = []
    for source_path in sources:
        text = source_path.read_text(encoding="utf-8")
        tts_text = strip_reader_to_tts(text, source_path.name)
        tts_filename = tts_filename_for(source_path)
        target_path = TTS_DIR / tts_filename
        target_path.write_text(tts_text, encoding="utf-8")
        exports.append((seq_for(source_path), source_path.name, tts_filename))

    (TTS_DIR / "manifest.yaml").write_text(build_manifest(exports), encoding="utf-8")
    print(f"Wrote {len(exports)} TTS files to {TTS_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
