#!/usr/bin/env python3
"""Build a readable normalized layer from the Snell OCR split files.

This is intentionally conservative. It removes extraction furniture, joins
wrapped prose, applies only high-confidence OCR repairs, and records suspect
counts for the manual pass. Greek quotations remain a manual repair target.
"""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "sources/modern/snell-die-entdeckung-des-geistes/source"
RAW_DIR = SOURCE_DIR / "raw"
NORMALIZED_DIR = SOURCE_DIR / "normalized"
MANIFEST_PATH = NORMALIZED_DIR / "manifest.yaml"


HIGH_CONFIDENCE_REPAIRS: tuple[tuple[str, str], ...] = (
    ("Phüanthropie", "Philanthropie"),
    ("Phüanthrop", "Philanthrop"),
    ("Phüologe", "Philologe"),
    ("Phüologie", "Philologie"),
    ("Phüol", "Philol"),
    ("phüologisch", "philologisch"),
    ("phüosoph", "philosoph"),
    ("Phüosoph", "Philosoph"),
    ("Phü", "Phil"),
    ("phü", "phil"),
    ("BÜder", "Bilder"),
    ("BÜd", "Bild"),
    ("Büd", "Bild"),
    ("Büder", "Bilder"),
    ("büd", "bild"),
    ("ausgebüdet", "ausgebildet"),
    ("gebüdet", "gebildet"),
    ("WeiterbÜdungen", "Weiterbildungen"),
    ("Teü", "Teil"),
    ("teüs", "teils"),
    ("zuteÜ", "zuteil"),
    ("aufteÜen", "aufteilen"),
    ("weÜ", "weil"),
    ("weü", "weil"),
    ("WÜlen", "Willen"),
    ("wül", "will"),
    ("BereitwÜligkeit", "Bereitwilligkeit"),
    ("Rndar", "Pindar"),
    ("Kallünachos", "Kallimachos"),
    ("Archüochos", "Archilochos"),
    ("Vergü", "Vergil"),
    ("Piaton", "Platon"),
    ("Thaies", "Thales"),
    ("Sökrates", "Sokrates"),
    ("AchÜl", "Achill"),
    ("griechbchen", "griechischen"),
    ("griechbche", "griechische"),
    ("Bewußtsems", "Bewußtseins"),
    ("funktioneile", "funktionelle"),
    ("einfaöh", "einfach"),
    ("Umecht", "Unrecht"),
    ("Häuptstück", "Hauptstück"),
    ("hÜflos", "hilflos"),
    ("hüft", "hilft"),
    ("schÜdert", "schildert"),
    ("schüdert", "schildert"),
    ("freÜich", "freilich"),
    ("freüich", "freilich"),
    ("Zivüisation", "Zivilisation"),
    ("MÜieu", "Milieu"),
    ("MiÜeus", "Milieus"),
    ("stabÜ", "stabil"),
    ("SchÜd", "Schild"),
    ("Schüd", "Schild"),
    ("Archü.", "Archil."),
    ("Hüflosigkeit", "Hilflosigkeit"),
    ("hüflose", "hilflose"),
    ("hüflosen", "hilflosen"),
    ("Hufe im Streit", "Hilfe im Streit"),
    ("Unheü", "Unheil"),
    ("unheü", "unheil"),
    ("beüegt", "beilegt"),
    ("Haupstadt", "Hauptstadt"),
    ("Dir Gefühl", "Ihr Gefühl"),
    ("Müde npaör", "Milde npaör"),
    ("Wohlwollen und Müde", "Wohlwollen und Milde"),
    ("gut es als Trost", "gilt es als Trost"),
    ("gut durchaus", "gilt durchaus"),
    ("gut übrigens", "gilt übrigens"),
)

FOOTER_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(r"©\s*2011,\s*1975,\s*Vandenhoeck", re.I),
    re.compile(r"ISBN\s+Print:", re.I),
)

PAGE_NUMBER_RE = re.compile(r"^\s*\d+\s*$")
ROMAN_RE = re.compile(r"^\s*[IVXLCDM]+\s*$")


def is_footer(line: str) -> bool:
    return any(pattern.search(line) for pattern in FOOTER_PATTERNS)


def is_running_header(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return False
    if PAGE_NUMBER_RE.match(stripped):
        return True

    # Examples:
    #   14                  I Die Auffassung des Menschen bei Homer
    #   IV Das Erwachen der Persönlichkeit in der frühgriechischen Lyrik        57
    if re.match(r"^\d+\s{2,}\S", line):
        return True
    if re.match(r"^\s*[IVXLCDM]+\s+.+\s+\d+\s*$", line):
        return True
    if re.match(r"^\s*\S.+\s{2,}\d+\s*$", line) and len(stripped) < 90:
        return True
    return False


def repair_text(text: str) -> tuple[str, dict[str, int]]:
    counts: dict[str, int] = {}
    text = text.replace("\x08", "").replace("\xad", "").replace("\f", "\n\n")
    for old, new in HIGH_CONFIDENCE_REPAIRS:
        count = text.count(old)
        if count:
            counts[old] = count
            text = text.replace(old, new)
    return text, counts


def looks_like_greek_noise(line: str) -> bool:
    if not line.strip():
        return False
    greek_chars = sum(1 for char in line if "\u0370" <= char <= "\u03ff")
    noise_tokens = len(re.findall(r"[#&\\]|[A-Za-z][<>]|[A-Z]{2,}", line))
    return greek_chars > 0 and noise_tokens > 1


def looks_like_ocr_noise(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return False
    if re.search(r"[#&][A-Za-z0-9]+", stripped):
        return True
    if re.search(r"\b[a-zA-Z]*[üÜ][a-zA-Z]*\b", stripped) and re.search(
        r"Phü|phü|Büd|Teü|weü|gebü", stripped
    ):
        return True
    if stripped.count("|") >= 2:
        return True
    return False


def normalize_lines(text: str) -> tuple[list[str], int, int]:
    paragraphs: list[str] = []
    current: list[str] = []
    suspect_greek = 0
    suspect_ocr = 0

    def flush() -> None:
        if current:
            paragraphs.append(" ".join(current).strip())
            current.clear()

    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        stripped = line.strip()
        if is_footer(line) or is_running_header(line):
            flush()
            continue
        if not stripped:
            flush()
            continue

        if looks_like_greek_noise(stripped):
            suspect_greek += 1
        if looks_like_ocr_noise(stripped):
            suspect_ocr += 1

        if not current:
            current.append(stripped)
            continue

        previous = current[-1]
        if previous.endswith("-") and stripped[:1].islower():
            current[-1] = previous[:-1] + stripped
        else:
            current.append(stripped)

    flush()
    return paragraphs, suspect_greek, suspect_ocr


def normalize_file(path: Path) -> dict[str, object]:
    text, repair_counts = repair_text(path.read_text(encoding="utf-8"))
    paragraphs, suspect_greek, suspect_ocr = normalize_lines(text)
    output_path = NORMALIZED_DIR / path.name
    normalized_text = "\n\n".join(paragraphs).strip()
    normalized_text, post_join_repairs = repair_text(normalized_text)
    for old, count in post_join_repairs.items():
        repair_counts[old] = repair_counts.get(old, 0) + count
    output_path.write_text(normalized_text + "\n", encoding="utf-8")
    return {
        "raw_file": f"raw/{path.name}",
        "normalized_file": f"normalized/{path.name}",
        "raw_lines": len(path.read_text(encoding="utf-8").splitlines()),
        "normalized_paragraphs": len(paragraphs),
        "suspect_greek_lines": suspect_greek,
        "suspect_ocr_lines": suspect_ocr,
        "repairs": repair_counts,
    }


def yaml_scalar(value: object) -> str:
    if isinstance(value, int):
        return str(value)
    text = str(value)
    return '"' + text.replace("\\", "\\\\").replace('"', '\\"') + '"'


def write_manifest(entries: list[dict[str, object]]) -> None:
    lines = [
        "status: machine-normalized-ocr-base",
        "source_quality: conservative automated cleanup from source/raw split files",
        "generated_by: tools/normalize_snell_ocr.py",
        "manual_pass_required: true",
        "notes:",
        "  - Removes page furniture, form feeds, wrapped-line breaks, and selected high-confidence OCR errors.",
        "  - Does not repair Greek quotations or citation-sensitive passages.",
        "  - Use source/raw and the PDF or scan witness for verification.",
        "files:",
    ]
    for entry in entries:
        lines.append(f"  - raw_file: {yaml_scalar(entry['raw_file'])}")
        for key in (
            "normalized_file",
            "raw_lines",
            "normalized_paragraphs",
            "suspect_greek_lines",
            "suspect_ocr_lines",
        ):
            lines.append(f"    {key}: {yaml_scalar(entry[key])}")
        repairs = entry["repairs"]
        if repairs:
            lines.append("    repairs:")
            assert isinstance(repairs, dict)
            for old, count in sorted(repairs.items()):
                lines.append(f"      {yaml_scalar(old)}: {count}")
        else:
            lines.append("    repairs: {}")
    MANIFEST_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    NORMALIZED_DIR.mkdir(parents=True, exist_ok=True)
    entries = [normalize_file(path) for path in sorted(RAW_DIR.glob("*.txt"))]
    write_manifest(entries)


if __name__ == "__main__":
    main()
