#!/usr/bin/env python3

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROJECT_DIR = ROOT / "sources/italian/bruno-de-la-causa-principio-et-uno"
PARTS_DIR = PROJECT_DIR / "parts"
TTS_DIR = PROJECT_DIR / "source/tts"

SPEAKERS = (
    "Dicsono Arelio",
    "Elitropio",
    "Filoteo",
    "Gervasio",
    "Polihimnio",
    "Armesso",
    "Teofilo",
)
SPEAKER_RE = re.compile(
    rf"^({'|'.join(re.escape(speaker) for speaker in SPEAKERS)})\.\s*(.*)$"
)

SKIPPED_PARTS = {
    "000-liberliber-metadata-and-toc.md": (
        "metadata",
        "Liber Liber apparatus; not authored Bruno text",
    ),
    "001-proemial-epistle-opening-calibration.md": (
        "superseded",
        "partial calibration fragment duplicated by 001-title-and-proemial-epistle.md",
    ),
}

PARTS = [
    "001-title-and-proemial-epistle.md",
    "002-argomenti.md",
    "003-ai-principi-de-l-universo.md",
    "004a-dialogo-primo-opening-and-cena-defense.md",
    "004b-dialogo-primo-correction-and-university-satire.md",
    "004c-dialogo-primo-pedants-and-interlocutors.md",
    "005a-dialogo-secondo-cause-principle-and-universal-intellect.md",
    "005b-dialogo-secondo-world-soul-and-life-in-all-things.md",
    "005c-dialogo-secondo-form-substance-and-whole-in-each-part.md",
    "006a-dialogo-terzo-pedant-prelude.md",
    "006b-dialogo-terzo-matter-as-subject.md",
    "006c-dialogo-terzo-plural-methods-and-matter-as-potency.md",
    "006d-dialogo-terzo-absolute-act-potency-and-the-one.md",
    "007a-dialogo-quarto-matter-female-and-appetite-prelude.md",
    "007b-dialogo-quarto-one-matter-corporeal-incorporeal.md",
    "007c-dialogo-quarto-matter-contains-forms.md",
    "007d-dialogo-quarto-appetite-of-matter.md",
    "008a-dialogo-quinto-one-infinite-immobile.md",
    "008b-dialogo-quinto-summary-and-ascent-to-unity.md",
    "008c-dialogo-quinto-contraries-and-final-one.md",
]


def seq_for(filename: str) -> str:
    match = re.match(r"^(\d+[a-z]?)-", filename)
    if not match:
        raise ValueError(f"cannot infer sequence from {filename}")
    return match.group(1)


def title_for(text: str, filename: str) -> str:
    first_line = text.splitlines()[0].strip()
    match = re.match(r"# Part \S+: (.+)", first_line)
    if not match:
        raise ValueError(f"{filename}: cannot infer part title")
    return match.group(1).strip()


def working_translation_for(text: str, filename: str) -> str:
    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")

    try:
        start = next(i for i, line in enumerate(lines) if line == "## Working Translation")
    except StopIteration as exc:
        raise ValueError(f"{filename}: no Working Translation boundary") from exc

    end = next(
        (i for i, line in enumerate(lines[start + 1 :], start + 1) if line.startswith("## ")),
        len(lines),
    )

    body = "\n".join(lines[start + 1 : end]).strip()
    if not body:
        raise ValueError(f"{filename}: empty Working Translation body")
    return normalize_for_speech(body)


def normalize_for_speech(text: str) -> str:
    text = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"\1", text)
    text = text.replace("*", "")
    text = mark_dialogue_speakers(text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return "\n".join(line.rstrip() for line in text.splitlines()).strip()


def mark_dialogue_speakers(text: str) -> str:
    lines: list[str] = []
    for line in text.splitlines():
        match = SPEAKER_RE.match(line)
        if not match:
            lines.append(line)
            continue

        lines.append(f"[[speaker: {match.group(1)}]]")
        if match.group(2):
            lines.append(match.group(2))

    return "\n".join(lines)


def strip_part_to_tts(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    title = title_for(text, path.name)
    body = working_translation_for(text, path.name)
    return f"# {title}\n\n{body}\n"


def remove_stale_tts_files(expected_filenames: set[str]) -> None:
    for path in TTS_DIR.glob("*.md"):
        if path.name != "README.md" and path.name not in expected_filenames:
            path.unlink()


def build_manifest(exports: list[tuple[str, str, str]]) -> str:
    lines = [
        "# TTS export manifest.",
        "# Access layer only; generated from source-local translation parts.",
        "---",
        "pass:",
        "  name: bruno-de-la-causa-tts",
        "  status: active",
        '  purpose: "Audio-ready derivatives of source-local English working translations"',
        '  source_parts: "../../parts"',
        '  generated_by: "tools/export_bruno_de_la_causa_tts.py"',
        '  cleanup_rule: "keep Working Translation only; add speakable heading; strip source apparatus and Markdown emphasis; convert dialogue labels to [[speaker: Name]] markers"',
        '  apparatus_boundary: "tts exports do not seed glossary, handles, threads, or encounter claims"',
        "exports:",
    ]

    for seq, source_part, tts_file in exports:
        lines.extend(
            [
                f'  - seq: "{seq}"',
                f'    source_part: "../../parts/{source_part}"',
                f'    tts_file: "{tts_file}"',
                "    status: exported",
                '    note: "Working Translation body exported; apparatus stripped; dialogue labels converted to speaker markers"',
            ]
        )

    lines.append("omitted:")
    for source_part, (status, note) in sorted(SKIPPED_PARTS.items()):
        lines.extend(
            [
                f'  - source_part: "../../parts/{source_part}"',
                f"    status: {status}",
                f'    note: "{note}"',
            ]
        )

    return "\n".join(lines) + "\n"


def main() -> int:
    TTS_DIR.mkdir(parents=True, exist_ok=True)

    source_paths = [PARTS_DIR / filename for filename in PARTS]
    missing = [str(path) for path in source_paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing source parts: " + ", ".join(missing))

    expected_filenames = {path.name for path in source_paths}
    remove_stale_tts_files(expected_filenames)

    exports: list[tuple[str, str, str]] = []
    for source_path in source_paths:
        tts_text = strip_part_to_tts(source_path)
        target_path = TTS_DIR / source_path.name
        target_path.write_text(tts_text, encoding="utf-8")
        exports.append((seq_for(source_path.name), source_path.name, target_path.name))

    (TTS_DIR / "manifest.yaml").write_text(build_manifest(exports), encoding="utf-8")
    print(f"Wrote {len(exports)} TTS files to {TTS_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
