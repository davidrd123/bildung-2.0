#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


DEFAULT_SOURCE_DIR = Path("/Users/daviddickinson/Downloads/$b44030")
DEFAULT_OUTPUT_DIR = Path(
    "sources/german/wind-das-experiment-und-die-metaphysik/source"
)
LAST_TEXT_PAGE = 136


@dataclass(frozen=True)
class Item:
    seq: int
    file: str
    kind: str
    slug: str
    title: str
    start_page: int
    start_line: int
    parent: str | None = None


ITEMS: list[Item] = [
    Item(0, "raw/000-front-matter.txt", "front", "front-matter", "Front matter (title pages and imprint)", 1, 2),
    Item(1, "raw/001-epigraph-schlegel.txt", "epigraph", "epigraph-schlegel", "Friedrich Schlegel epigraph", 7, 3),
    Item(2, "raw/002-vorwort.txt", "preface", "vorwort", "Vorwort", 9, 1),
    Item(3, "raw/003-contents.txt", "toc", "contents", "Inhaltsverzeichnis", 15, 1),
    Item(4, "raw/004-part-i-theorie-des-experiments.txt", "part", "part-i-theorie-des-experiments", "Erster Teil — Theorie des Experiments", 17, 1),
    Item(5, "raw/005-part-i-s01-zirkel-der-physikalischen-forschung.txt", "section", "part-i-s01-zirkel-der-physikalischen-forschung", "§ 1. Der Zirkel der physikalischen Forschung.", 17, 3, "part-i-theorie-des-experiments"),
    Item(6, "raw/006-part-i-s02-elemente-der-messung.txt", "section", "part-i-s02-elemente-der-messung", "§ 2. Die Elemente der Messung und der Sinn des Exaktheitsanspruchs.", 20, 6, "part-i-theorie-des-experiments"),
    Item(7, "raw/007-part-i-s03-praktische-geometrie.txt", "section", "part-i-s03-praktische-geometrie", "§ 3. Einsteins Begriff der „praktischen Geometrie“.", 23, 11, "part-i-theorie-des-experiments"),
    Item(8, "raw/008-part-i-s04-konventionelle-willkuer.txt", "section", "part-i-s04-konventionelle-willkuer", "§ 4. Poincarés Prinzip der „konventionellen Willkür“.", 26, 8, "part-i-theorie-des-experiments"),
    Item(9, "raw/009-part-i-s05-aufgabe-des-experiments.txt", "section", "part-i-s05-aufgabe-des-experiments", "§ 5. Die Aufgabe des Experiments.", 28, 12, "part-i-theorie-des-experiments"),
    Item(10, "raw/010-part-i-s06-transformation-und-verkoerperung.txt", "section", "part-i-s06-transformation-und-verkoerperung", "§ 6. Transformation und Verkörperung.", 32, 7, "part-i-theorie-des-experiments"),
    Item(11, "raw/011-part-i-s07-eignungsurteile.txt", "section", "part-i-s07-eignungsurteile", "§ 7. Die „Eignungsurteile“.", 38, 15, "part-i-theorie-des-experiments"),
    Item(12, "raw/012-part-i-s08-wirkliche-und-indifferente-hypothesen.txt", "section", "part-i-s08-wirkliche-und-indifferente-hypothesen", "§ 8. Wirkliche und indifferente Hypothesen.", 40, 7, "part-i-theorie-des-experiments"),
    Item(13, "raw/013-part-i-s09-zyklische-progression.txt", "section", "part-i-s09-zyklische-progression", "§ 9. Die zyklische Progression und ihre methodischen Grundlagen.", 42, 16, "part-i-theorie-des-experiments"),
    Item(14, "raw/014-part-i-s10-metaphysik-und-empirie.txt", "section", "part-i-s10-metaphysik-und-empirie", "§ 10. Metaphysik und Empirie.", 47, 18, "part-i-theorie-des-experiments"),
    Item(15, "raw/015-part-i-s11-transzendentalphilosophie-und-experimentelle-methode.txt", "section", "part-i-s11-transzendentalphilosophie-und-experimentelle-methode", "§ 11. Transzendentalphilosophie und experimentelle Methode.", 55, 10, "part-i-theorie-des-experiments"),
    Item(16, "raw/016-part-ii-experimentelle-reduktion-der-kosmologischen-antinomien.txt", "part", "part-ii-experimentelle-reduktion-der-kosmologischen-antinomien", "Zweiter Teil — Die „experimentelle Reduktion“ der kosmologischen Antinomien", 61, 1),
    Item(17, "raw/017-part-ii-s12-empirische-kriterien-der-metaphysik.txt", "section", "part-ii-s12-empirische-kriterien-der-metaphysik", "§ 12. Die empirischen Kriterien der Metaphysik.", 61, 8, "part-ii-experimentelle-reduktion-der-kosmologischen-antinomien"),
    Item(18, "raw/018-part-ii-ch1-antinomie-des-weltbegriffs.txt", "chapter", "part-ii-ch1-antinomie-des-weltbegriffs", "1. Kapitel — Die Antinomie des Weltbegriffs", 68, 3, "part-ii-experimentelle-reduktion-der-kosmologischen-antinomien"),
    Item(19, "raw/019-part-ii-ch1-s13-praezisierung-der-ersten-antinomie.txt", "section", "part-ii-ch1-s13-praezisierung-der-ersten-antinomie", "§ 13. Präzisierung der Frage der ersten Antinomie. (Zurückweisung des Russellschen Einwands.)", 68, 4, "part-ii-ch1-antinomie-des-weltbegriffs"),
    Item(20, "raw/020-part-ii-ch1-s14-mathematische-antinomie-des-euklidischen-raumes.txt", "section", "part-ii-ch1-s14-mathematische-antinomie-des-euklidischen-raumes", "§ 14. Die mathematische Antinomie des Euklidischen Raumes.", 73, 30, "part-ii-ch1-antinomie-des-weltbegriffs"),
    Item(21, "raw/021-part-ii-ch1-s15-physikalische-antinomie-des-newtonschen-systems.txt", "section", "part-ii-ch1-s15-physikalische-antinomie-des-newtonschen-systems", "§ 15. Die physikalische Antinomie des Newtonschen Systems.", 75, 35, "part-ii-ch1-antinomie-des-weltbegriffs"),
    Item(22, "raw/022-part-ii-ch1-s16-zwangslaeufigkeit-der-newtonschen-antinomie.txt", "section", "part-ii-ch1-s16-zwangslaeufigkeit-der-newtonschen-antinomie", "§ 16. Die Zwangsläufigkeit der Newtonschen Antinomie gemäß der Kantischen Lehre.", 78, 27, "part-ii-ch1-antinomie-des-weltbegriffs"),
    Item(23, "raw/023-part-ii-ch1-s17-kants-interpretation-des-absoluten-raumes.txt", "section", "part-ii-ch1-s17-kants-interpretation-des-absoluten-raumes", "§ 17. Kants Interpretation des absoluten Raumes.", 80, 29, "part-ii-ch1-antinomie-des-weltbegriffs"),
    Item(24, "raw/024-part-ii-ch1-s18-methodische-folgerung.txt", "section", "part-ii-ch1-s18-methodische-folgerung", "§ 18. Methodische Folgerung.", 83, 37, "part-ii-ch1-antinomie-des-weltbegriffs"),
    Item(25, "raw/025-part-ii-ch1-s19-mathematische-loesung-der-euklidischen-antinomie.txt", "section", "part-ii-ch1-s19-mathematische-loesung-der-euklidischen-antinomie", "§ 19. Die mathematische Lösung der euklidischen Antinomie.", 85, 14, "part-ii-ch1-antinomie-des-weltbegriffs"),
    Item(26, "raw/026-part-ii-ch1-s20-physikalische-loesung-der-newtonschen-antinomie.txt", "section", "part-ii-ch1-s20-physikalische-loesung-der-newtonschen-antinomie", "§ 20. Die physikalische Lösung der Newtonschen Antinomie.", 87, 31, "part-ii-ch1-antinomie-des-weltbegriffs"),
    Item(27, "raw/027-part-ii-ch1-s21-prinzip-der-inneren-grenzsetzung.txt", "section", "part-ii-ch1-s21-prinzip-der-inneren-grenzsetzung", "§ 21. Das Prinzip der inneren Grenzsetzung.", 91, 30, "part-ii-ch1-antinomie-des-weltbegriffs"),
    Item(28, "raw/028-part-ii-ch2-antinomie-des-atombegriffs.txt", "chapter", "part-ii-ch2-antinomie-des-atombegriffs", "2. Kapitel — Die Antinomie des Atombegriffs", 93, 3, "part-ii-experimentelle-reduktion-der-kosmologischen-antinomien"),
    Item(29, "raw/029-part-ii-ch2-s22-innere-grenze-des-teilungsvollzuges.txt", "section", "part-ii-ch2-s22-innere-grenze-des-teilungsvollzuges", "§ 22. Die „innere Grenze“ des Teilungsvollzuges.", 93, 4, "part-ii-ch2-antinomie-des-atombegriffs"),
    Item(30, "raw/030-part-ii-ch2-s23-zwei-formen-der-unsicherheit.txt", "section", "part-ii-ch2-s23-zwei-formen-der-unsicherheit", "§ 23. Zwei Formen der „Unsicherheit“.", 94, 15, "part-ii-ch2-antinomie-des-atombegriffs"),
    Item(31, "raw/031-part-ii-ch3-kausalitaet-und-freiheit.txt", "chapter", "part-ii-ch3-kausalitaet-und-freiheit", "3. Kapitel — Kausalität und Freiheit", 99, 2, "part-ii-experimentelle-reduktion-der-kosmologischen-antinomien"),
    Item(32, "raw/032-part-ii-ch3-s24-heterogenitaet-und-notwendigkeit.txt", "section", "part-ii-ch3-s24-heterogenitaet-und-notwendigkeit", "§ 24. Heterogeneität und Notwendigkeit in der Verbindung von Ursache und Wirkung.", 99, 3, "part-ii-ch3-kausalitaet-und-freiheit"),
    Item(33, "raw/033-part-ii-ch3-s25-zeitverhaeltnis-der-dynamischen-verknuepfung.txt", "section", "part-ii-ch3-s25-zeitverhaeltnis-der-dynamischen-verknuepfung", "§ 25. Das Zeitverhältnis der dynamischen Verknüpfung.", 103, 3, "part-ii-ch3-kausalitaet-und-freiheit"),
    Item(34, "raw/034-part-ii-ch3-s26-spielraum-der-gegenwart.txt", "section", "part-ii-ch3-s26-spielraum-der-gegenwart", "§ 26. Der „Spielraum“ der Gegenwart.", 108, 28, "part-ii-ch3-kausalitaet-und-freiheit"),
    Item(35, "raw/035-part-ii-ch3-s27-linearer-und-konfiguraler-zeitablauf.txt", "section", "part-ii-ch3-s27-linearer-und-konfiguraler-zeitablauf", "§ 27. Linearer und konfiguraler Zeitablauf.", 110, 23, "part-ii-ch3-kausalitaet-und-freiheit"),
    Item(36, "raw/036-part-ii-ch3-s28-innere-grenzsetzung-und-indetermination.txt", "section", "part-ii-ch3-s28-innere-grenzsetzung-und-indetermination", "§ 28. Innere Grenzsetzung und Indetermination.", 113, 3, "part-ii-ch3-kausalitaet-und-freiheit"),
    Item(37, "raw/037-part-ii-ch3-s29-konstanz-und-emergenz.txt", "section", "part-ii-ch3-s29-konstanz-und-emergenz", "§ 29. Konstanz und Emergenz.", 116, 3, "part-ii-ch3-kausalitaet-und-freiheit"),
    Item(38, "raw/038-part-ii-ch3-s30-zeitanfang-und-ende.txt", "section", "part-ii-ch3-s30-zeitanfang-und-ende", "§ 30. Zeitanfang und -ende.", 121, 30, "part-ii-ch3-kausalitaet-und-freiheit"),
    Item(39, "raw/039-part-ii-ch3-s31-freiheit-unter-der-bedingung-des-naturgesetzes.txt", "section", "part-ii-ch3-s31-freiheit-unter-der-bedingung-des-naturgesetzes", "§ 31. Die Freiheit unter der Bedingung des Naturgesetzes.", 125, 10, "part-ii-ch3-kausalitaet-und-freiheit"),
    Item(40, "raw/040-part-ii-ch4-modalitaet-des-geschehens.txt", "chapter", "part-ii-ch4-modalitaet-des-geschehens", "4. Kapitel — Die Modalität des Geschehens", 132, 3, "part-ii-experimentelle-reduktion-der-kosmologischen-antinomien"),
    Item(41, "raw/041-part-ii-ch4-s32-mass-des-zufalls.txt", "section", "part-ii-ch4-s32-mass-des-zufalls", "§ 32. Das Maß des Zufalls als Objekt der Sinndeutung.", 132, 4, "part-ii-ch4-modalitaet-des-geschehens"),
]


def load_pages(source_dir: Path) -> dict[int, list[str]]:
    pages: dict[int, list[str]] = {}
    for page in range(1, LAST_TEXT_PAGE + 1):
        path = source_dir / f"UCAL_$B44030_{page:08d}.txt"
        pages[page] = path.read_text(encoding="utf-8", errors="ignore").splitlines()
    return pages


def is_page_number(line: str) -> bool:
    return bool(re.fullmatch(r"[IVXLCDM]+|\d+", line.strip()))


def normalize_header(line: str) -> str:
    normalized = line.strip()
    normalized = re.sub(r"^k\.\s*", "", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"^§\s*\d+\.?\s*", "", normalized)
    normalized = (
        normalized.replace(",,", " ")
        .replace("„", " ")
        .replace("“", " ")
        .replace('"', " ")
        .replace("—", " ")
        .replace("-", " ")
        .replace("'", " ")
        .replace(".", " ")
        .replace(",", " ")
        .replace("(", " ")
        .replace(")", " ")
    )
    normalized = re.sub(r"\s+", " ", normalized)
    normalized = normalized.strip()
    return normalized.casefold()


def build_header_titles() -> set[str]:
    titles = {
        "Vorwort",
        "Inhaltsverzeichnis",
        "Erster Teil — Theorie des Experiments",
        "Zweiter Teil — Die „experimentelle Reduktion“ der kosmologischen Antinomien",
        "Theorie des Experiments.",
        "Die „experimentelle Reduktion“ der kosmologischen Antinomien.",
        "Die experimentelle Reduktion der kosmologischen Antinomien.",
        "Wind, Experiment.",
        *[item.title for item in ITEMS if item.kind in {"section", "chapter"}],
    }
    normalized_titles: set[str] = set()
    for title in titles:
        normalized = normalize_header(title)
        normalized_titles.add(normalized)
        if " (" in title:
            normalized_titles.add(normalize_header(title.split(" (", 1)[0]))
    return normalized_titles


HEADER_TITLES = build_header_titles()


def is_running_header(line: str) -> bool:
    normalized = normalize_header(line)
    if not normalized:
        return False
    if normalized in HEADER_TITLES:
        return True
    return any(
        len(normalized) >= 12 and (title.startswith(normalized) or normalized.startswith(title))
        for title in HEADER_TITLES
    )


def strip_page_prefix(lines: list[str]) -> list[str]:
    out = list(lines)
    while out and not out[0].strip():
        out.pop(0)

    if len(out) >= 2 and is_page_number(out[0]) and is_running_header(out[1]):
        out = out[2:]
    elif len(out) >= 2 and is_running_header(out[0]) and is_page_number(out[1]):
        out = out[2:]
    else:
        if out and is_page_number(out[0]):
            out.pop(0)
        if out and is_running_header(out[0]):
            out.pop(0)
        if out and is_page_number(out[0]):
            out.pop(0)

    while out and not out[0].strip():
        out.pop(0)
    while out and out[0].strip() in {"...", ".", "-", "—"}:
        out.pop(0)
        while out and not out[0].strip():
            out.pop(0)
    return out


def strip_page_suffix(lines: list[str]) -> list[str]:
    out = list(lines)
    while out and not out[-1].strip():
        out.pop()
    while out and (
        out[-1].strip() in {"...", ".", "-", "—"}
        or is_page_number(out[-1])
        or normalize_header(out[-1]) == normalize_header("Wind, Experiment.")
    ):
        out.pop()
        while out and not out[-1].strip():
            out.pop()
    footer = normalize_header("Wind, Experiment.")
    for index in range(len(out) - 1, max(-1, len(out) - 6), -1):
        if normalize_header(out[index]) == footer:
            del out[index]
            break
    while out and (
        out[-1].strip() in {"...", ".", "-", "—"} or is_page_number(out[-1])
    ):
        out.pop()
        while out and not out[-1].strip():
            out.pop()
    return out


def collapse_blank_runs(lines: Iterable[str]) -> list[str]:
    collapsed: list[str] = []
    blank = False
    for raw in lines:
        line = raw.rstrip()
        if line:
            collapsed.append(line)
            blank = False
        elif not blank:
            collapsed.append("")
            blank = True
    while collapsed and not collapsed[0]:
        collapsed.pop(0)
    while collapsed and not collapsed[-1]:
        collapsed.pop()
    return collapsed


def last_nonblank_line(lines: list[str]) -> int:
    for index in range(len(lines), 0, -1):
        if lines[index - 1].strip():
            return index
    return 0


def slice_item_lines(
    pages: dict[int, list[str]],
    item: Item,
    next_item: Item | None,
) -> list[str]:
    if next_item is None:
        end_page = LAST_TEXT_PAGE
        end_line = len(pages[LAST_TEXT_PAGE]) + 1
    else:
        end_page = next_item.start_page
        end_line = next_item.start_line

    collected: list[str] = []
    for page in range(item.start_page, end_page + 1):
        page_lines = pages[page]
        start_idx = item.start_line - 1 if page == item.start_page else 0
        end_idx = end_line - 1 if page == end_page else len(page_lines)
        chunk = page_lines[start_idx:end_idx]
        if page != item.start_page:
            chunk = strip_page_prefix(chunk)
        if page != end_page:
            chunk = strip_page_suffix(chunk)
        collected.extend(chunk)

    cleaned = collapse_blank_runs(collected)
    if item.slug == "part-ii-ch3-s29-konstanz-und-emergenz" and cleaned:
        cleaned[0] = "§ 29. Konstanz und Emergenz."
    return cleaned


def write_sections_yaml(
    output_dir: Path,
    pages: dict[int, list[str]],
    rendered: list[tuple[Item, list[str], Item | None]],
) -> None:
    lines = [
        "# Wind — Das Experiment und die Metaphysik — sections map",
        "# Generated by tools/split_wind_experiment.py from the UCAL page-level OCR dump.",
        "# Use for navigation and browsing, not for fine lexical work without scan checks.",
        "# 'kind' values:",
        "#   front/epigraph/preface/toc = opening material",
        "#   part = major division heading",
        "#   chapter = chapter heading container inside Part II",
        "#   section = numbered § section",
        "---",
        "sections:",
    ]

    for item, rendered_lines, next_item in rendered:
        if next_item is None:
            end_page = LAST_TEXT_PAGE
            end_line = len(pages[LAST_TEXT_PAGE])
        elif next_item.start_page == item.start_page:
            end_page = item.start_page
            end_line = next_item.start_line - 1
        else:
            end_page = next_item.start_page
            end_line = next_item.start_line - 1

        if next_item is not None and next_item.start_page != item.start_page and next_item.start_line == 1:
            end_page = next_item.start_page - 1
            while end_page > item.start_page and last_nonblank_line(pages[end_page]) == 0:
                end_page -= 1
            end_line = last_nonblank_line(pages[end_page])

        lines.extend(
            [
                f"- seq: {item.seq}",
                f"  file: {item.file}",
                f"  kind: {item.kind}",
                f"  slug: {item.slug}",
                f"  title: {quote_yaml(item.title)}",
            ]
        )
        if item.parent:
            lines.append(f"  parent: {item.parent}")
        lines.extend(
            [
                f"  start_page: {item.start_page}",
                f"  start_line: {item.start_line}",
                f"  end_page: {end_page}",
                f"  end_line: {end_line}",
                f"  length: {len(rendered_lines)}",
            ]
        )

    (output_dir / "sections.yaml").write_text("\n".join(lines) + "\n", encoding="utf-8")


def quote_yaml(text: str) -> str:
    escaped = text.replace('"', '\\"')
    return f'"{escaped}"'


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-dir", type=Path, default=DEFAULT_SOURCE_DIR)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    args = parser.parse_args()

    pages = load_pages(args.source_dir)

    raw_dir = args.output_dir / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)

    rendered: list[tuple[Item, list[str], Item | None]] = []
    for index, item in enumerate(ITEMS):
        next_item = ITEMS[index + 1] if index + 1 < len(ITEMS) else None
        lines = slice_item_lines(pages, item, next_item)
        (args.output_dir / item.file).write_text("\n".join(lines) + "\n", encoding="utf-8")
        rendered.append((item, lines, next_item))

    write_sections_yaml(args.output_dir, pages, rendered)


if __name__ == "__main__":
    main()
