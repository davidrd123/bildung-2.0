#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import re
import subprocess
import textwrap


PDF_REL = (
    "books/Escolios a un texto implícito II -- Nicolás Gómez Dávila -- "
    "Colección de autores nacionales, II.pdf"
)
OUTPUT_REL = "texts/escolios-ii/source/aphorisms.yaml"

SKIP_EXACT = {
    "!",
    "NICOLAS GOMEZ DAVILA",
    "ESCOLIOS A UN",
    "TEXTO IMPLICITO II",
}
SKIP_PREFIXES = (
    "SUBDIRECCION DE COMUNICACIONES CULTURALES",
    "DIVISION DE PUBLICACIONES",
    "BIBLIOTECA COLOMBIANA DE CULTURA",
    "COLECCION AUTORES NACIONALES",
    "398.96",
    "G633e Gómez Dávila, Nicolás",
    "Escolios a un texto implícito II",
    "Bogotá, Instituto Colombiano",
    "de Cultura, 1977.",
    "2v. 508 p.",
    "(Colección Autores",
    "1. Escolios.",
    "LOS DERECHOS DE ESTA EDICION",
    "POR EL INSTITUTO COLOMBIANO",
    "IMPRESO EN EDITORIAL ANDES",
)
PRINTED_PAGE_RE = re.compile(r"^[0-9 ]+$")


def repo_root() -> Path:
    return Path(__file__).resolve().parents[3]


def wrap_block(text: str, width: int = 76) -> list[str]:
    return textwrap.wrap(
        text,
        width=width,
        break_long_words=False,
        break_on_hyphens=False,
    )


def pdftotext(pdf_path: Path) -> str:
    result = subprocess.run(
        ["pdftotext", str(pdf_path), "-"],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout


def clean_page(raw_page: str) -> tuple[list[str], str | None]:
    cleaned: list[str] = []
    printed_page: str | None = None

    for raw in raw_page.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line == "!—":
            line = "—"
        if line in SKIP_EXACT:
            continue
        if PRINTED_PAGE_RE.fullmatch(line):
            digits = re.sub(r"\s+", "", line)
            if digits:
                printed_page = digits
            continue
        if any(line.startswith(prefix) for prefix in SKIP_PREFIXES):
            continue
        cleaned.append(line)

    return cleaned, printed_page


def join_line(buffer: list[str], line: str) -> None:
    if not buffer:
        buffer.append(line)
        return

    previous = buffer[-1]
    if previous.endswith("-") and line and line[0].islower():
        buffer[-1] = previous[:-1] + line
        return

    buffer.append(line)


def normalize_text(text: str) -> str:
    value = text.strip()
    # Repair obvious inline line-break hyphenation from OCR/PDF extraction.
    value = re.sub(
        r"\b([A-Za-zÁÉÍÓÚáéíóúÑñÜü]{2,})-\s+([a-záéíóúñü])",
        r"\1\2",
        value,
    )
    # Fix simple digit-for-letter OCR noise inside words.
    value = re.sub(r"(?<=[A-Za-zÁÉÍÓÚáéíóúÑñÜü])1(?=[A-Za-zÁÉÍÓÚáéíóúÑñÜü])", "l", value)
    value = re.sub(r"\bE1\b", "El", value)
    # Strip stray apostrophes inserted ahead of lowercase words.
    value = re.sub(r"(?<=\s)'(?=[a-záéíóúñü])", "", value)
    # Remove spacing glitches around punctuation.
    value = re.sub(r"\s+([,.;:])", r"\1", value)
    value = re.sub(r"([,.;:]){2,}", r"\1", value)
    # Drop obvious separator noise while keeping real emphatic punctuation intact.
    value = re.sub(r"\s+!{2,}(?=\s|$)", "", value)
    value = value.replace("!—", "—")
    # Drop dangling OCR separators at entry ends.
    value = re.sub(r"\s+-$", "", value)
    # Fix recurrent witness-specific OCR seams that survive the generic cleanup.
    replacements = {
        "seresindeleblemente": "seres indeleblemente",
        "conciste": "consiste",
        "periódico-envilece": "periódico envilece",
        "al que. no": "al que no",
        "no,es": "no es",
        "aficionado,a": "aficionado a",
        "ideas:que": "ideas que",
        "del. cambio.": "del cambio.",
        "a, sentirse": "a sentirse",
        "a, envejecer": "a envejecer",
        "creer, en Dios": "creer en Dios",
        "no, tiene": "no tiene",
        "La,objetividad": "La objetividad",
        "uña imaginación": "una imaginación",
        "co-. mo": "como",
        "estructuras feudales América": "estructuras feudales en América",
        "feudalismo,\\": "feudalismo,",
        "codi-¡ cia": "codicia",
        "de' la": "de la",
        "anda mar de poetas": "anda mal de poetas",
        "textos=": "textos",
        "enjambre humanó": "enjambre humano",
        "inte ligencias": "inteligencias",
        "hue lias": "huellas",
        "La' literatura": "La literatura",
        "no es' el": "no es el",
    }
    for old, new in replacements.items():
        value = value.replace(old, new)
    value = re.sub(r"\.(\d{2,4})$", ".", value)
    value = re.sub(r"\s+\d+'\d+$", "", value)
    return value.strip()


def detect_issues(text_value: str) -> list[str]:
    issues: list[str] = []
    if "  " in text_value:
        issues.append("double-space")
    if re.search(r"(?:\b\w\s+){6,}", text_value):
        issues.append("spaced-letter-ocr")
    if re.search(r"\b\w+-\s+[a-záéíóúñü]", text_value):
        issues.append("inline-hyphenation")
    if re.search(
        r"(?<=[A-Za-zÁÉÍÓÚáéíóúÑñÜü])\d(?=[A-Za-zÁÉÍÓÚáéíóúÑñÜü])|\.\d{2,4}$|\d+'\d+$",
        text_value,
    ):
        issues.append("digit-in-word")
    if re.search(r"!{2,}|!—", text_value):
        issues.append("separator-noise")
    return issues


def extract_entries(text: str) -> list[dict[str, object]]:
    pages = text.split("\f")
    page_payloads: list[tuple[int, list[str], str | None]] = []

    for pdf_page, raw_page in enumerate(pages, start=1):
        lines, printed_page = clean_page(raw_page)
        if lines:
            page_payloads.append((pdf_page, lines, printed_page))

    body_pages = [
        payload
        for payload in page_payloads
        if any(line.startswith("—") for line in payload[1])
    ]
    if not body_pages:
        raise RuntimeError("No aphorism pages detected in Spanish PDF extraction.")

    first_body_page = body_pages[0][0]
    last_body_page = body_pages[-1][0]

    entries: list[dict[str, object]] = []
    current_lines: list[str] = []
    current_page: int | None = None
    current_printed: str | None = None

    for pdf_page, lines, printed_page in page_payloads:
        if pdf_page < first_body_page or pdf_page > last_body_page:
            continue

        for line in lines:
            if line.startswith("—"):
                if current_lines:
                    text_value = normalize_text(" ".join(current_lines))
                    entry: dict[str, object] = {
                        "id": len(entries) + 1,
                        "pdf_page": current_page,
                        "es": text_value,
                    }
                    if current_printed:
                        entry["print_page"] = current_printed
                    issues = detect_issues(text_value)
                    if issues:
                        entry["issues"] = issues
                    entries.append(entry)

                current_lines = [re.sub(r"^—\s*", "", line)]
                current_page = pdf_page
                current_printed = printed_page
                continue

            if current_lines:
                join_line(current_lines, line)

    if current_lines:
        text_value = normalize_text(" ".join(current_lines))
        entry = {
            "id": len(entries) + 1,
            "pdf_page": current_page,
            "es": text_value,
        }
        if current_printed:
            entry["print_page"] = current_printed
        issues = detect_issues(text_value)
        if issues:
            entry["issues"] = issues
        entries.append(entry)

    return entries


def write_yaml(entries: list[dict[str, object]], out_path: Path) -> None:
    header = [
        "# Escolios a un texto implicito II — Spanish PDF extraction",
        "# Primary source extracted from the 1977 Bogotá volume II PDF.",
        "# Body pages detected from the first to the last page carrying aphorism starts.",
        "# `pdf_page` is the scan page index; `print_page` is present when recoverable.",
        "# Compare against `aphorisms.it.yaml` for the secondary Italian witness.",
        "",
    ]
    chunks = ["\n".join(header)]

    for entry in entries:
        chunks.append(f"- id: {entry['id']}\n")
        chunks.append(f"  pdf_page: {entry['pdf_page']}\n")
        if "print_page" in entry:
            chunks.append(f"  print_page: {entry['print_page']}\n")
        if "issues" in entry:
            issues = ", ".join(entry["issues"])  # type: ignore[arg-type]
            chunks.append(f"  issues: [{issues}]\n")
        chunks.append("  es: >\n")
        for line in wrap_block(str(entry["es"]).strip()):
            chunks.append(f"    {line}\n")
        chunks.append("\n")

    out_path.write_text("".join(chunks))


def main() -> None:
    root = repo_root()
    pdf_path = root / PDF_REL
    out_path = root / OUTPUT_REL
    text = pdftotext(pdf_path)
    entries = extract_entries(text)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    write_yaml(entries, out_path)
    flagged = sum(1 for entry in entries if "issues" in entry)
    print(
        f"Wrote {len(entries)} aphorisms to {out_path.relative_to(root)} "
        f"({flagged} flagged for OCR cleanup review)."
    )


if __name__ == "__main__":
    main()
