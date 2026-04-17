from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "sources/german/cassirer-philosophie-der-symbolischen-formen/source/full/vol1-die-sprache.txt"
RAW_DIR = ROOT / "sources/german/cassirer-philosophie-der-symbolischen-formen/source/raw"


# 1-based inclusive line ranges from the current pdftotext extraction.
# These are intentionally rough navigational surfaces, not a verified edition.
RANGES = [
    ("000-front-matter-and-inhaltsuebersicht.txt", 1, 136),
    ("001-vorwort.txt", 137, 322),
    ("010-einleitung-und-problemstellung.txt", 323, 2159),
    ("011-kapitel-i-das-sprachproblem-in-der-geschichte-der-philosophie.txt", 2160, 4870),
    ("012-kapitel-ii-die-sprache-in-der-phase-des-sinnlichen-ausdrucks.txt", 4871, 5815),
    ("013-kapitel-iii-die-sprache-in-der-phase-des-anschaulichen-ausdrucks.txt", 5816, 9861),
    ("014-kapitel-iv-die-sprache-als-ausdruck-des-begrifflichen-denkens.txt", 9862, 11003),
    ("015-kapitel-v-die-sprache-und-der-ausdruck-der-reinen-beziehungsformen.txt", 11004, 11822),
    ("030-editorischer-bericht-und-back-matter.txt", 11823, None),
]


def main() -> None:
    lines = SOURCE.read_text(encoding="utf-8").splitlines()
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    for filename, start, end in RANGES:
        start_idx = start - 1
        end_idx = len(lines) if end is None else end
        block = "\n".join(lines[start_idx:end_idx]).strip() + "\n"
        (RAW_DIR / filename).write_text(block, encoding="utf-8")


if __name__ == "__main__":
    main()
