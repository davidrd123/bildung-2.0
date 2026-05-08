#!/usr/bin/env python3

from __future__ import annotations

import re
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "sources/modern/hoffmeyer-biosemiotics/source"
RAW_DIR = SOURCE_DIR / "raw"
NORMALIZED_DIR = SOURCE_DIR / "normalized"
PDF_AUTHORITY = ROOT / (
    "sources/modern/incoming/books/"
    "Biosemiotics_ An Examination into the Signs of Life and the -- Jesper Hoffmeyer.pdf"
)

# This is a first-pass generator. Several normalized files also have manual
# page-level OCR repairs; regenerating this directory should be followed by a
# diff review before replacing the current text.

STRUCTURAL_FILES = {
    "000-title-pages-and-publisher-matter.txt",
    "001-contents.txt",
    "053-back-cover-blurbs-and-scan-noise.txt",
}

PROSE_SECTIONS = [
    (2, "raw/002-preface.txt", 1411),
    (10, "raw/010-on-biosemiotics.txt", 2189),
    (11, "raw/011-surfaces-within-surfaces.txt", 3108),
    (12, "raw/012-sign-and-cause.txt", 4399),
    (13, "raw/013-code-duality.txt", 6277),
    (14, "raw/014-the-semiotics-of-heredity.txt", 8918),
    (15, "raw/015-the-semiotic-niche.txt", 12219),
    (16, "raw/016-endosemiotics.txt", 15063),
    (17, "raw/017-from-animal-to-human.txt", 17846),
    (18, "raw/018-perspectives.txt", 20435),
    (19, "raw/019-biosemiotic-technology.txt", 22143),
    (50, "raw/050-postscript-short-historical-notes.txt", 22903),
    (51, "raw/051-literature.txt", 23603),
    (52, "raw/052-index.txt", 25426),
]

RUNNING_HEADERS = {
    "THE BIOSEMIOTIC APPROACH",
    "THE SEMIOTICS OF NATURE",
    "BIOSEMIOTICS AND THE HUMAN BEING",
    "FROM ANIMAL TO HUMAN",
    "PERSPECTIVES",
    "BIOSEMIOTIC TECHNOLOGY",
    "ENDOSEMIOTICS",
    "LITERATURE",
    "INDEX",
}

TECH_WORDS = {
    "acetabularia",
    "biosemiotic",
    "biosemiotics",
    "cytosemiotics",
    "endosemiotic",
    "endosemiotics",
    "epigenesis",
    "epigenetic",
    "immunodepressant",
    "psychoneuroimmunological",
    "psychoneuroimmunology",
    "semethic",
    "semiosphere",
    "semiosis",
    "signification",
    "zoosemiotics",
}

DIRECT_FIXES = {
    "Forthe": "For the",
    "couldbesaidtobe": "could be said to be",
    "ofinformation": "of information",
    "oflife": "of life",
    "ofbiosemiotics": "of biosemiotics",
    "oflifeare": "of life are",
    "amore": "a more",
    "one- -dimensional": "one-dimensional",
    "adeep-drawn": "a deep-drawn",
    "seIf": "self",
    "described asa": "described as a",
    "iis a spherelike": "is a sphere like",
    "Itpermeates": "It permeates",
    "orbiosphere": "or biosphere",
    "iinnermost": "innermost",
    "The Collected Papers ofCharles": "The Collected Papers of Charles",
    "oneenveloping. another": "one enveloping another",
    "essentialone": "essential one",
    "thesurrounding": "the surrounding",
    "bystrangers": "by strangers",
    "pickedup": "picked up",
    "ofinterfaces": "of interfaces",
    "in itselfasign": "in itself a sign",
    "ice.,": "i.e.,",
    "processes oflife": "processes of life",
    "th life onEarth": "the life on Earth",
    "does ot": "does not",
    "trafhic": "traffic",
    "Semioitiker": "Semiotiker",
    "repettoire": "repertoire",
    "hormoneproducing": "hormone-producing",
    "aseverywhere": "as everywhere",
    "sepcifications": "specifications",
    "organioe": "organism",
    "gees may": "genes may",
    "interpretantiscalled": "interpretant is called",
    "especiallyinpaleontology": "especially in paleontology",
    "appointed chee essential one": "appointed the essential one",
    "The semiosphere iis a spherelike the atmosphere, hydrosphere, orbiosphere. Itpermeates these spheres from their iinnermost to outermost reaches": "The semiosphere is a sphere like the atmosphere, hydrosphere, or biosphere. It permeates these spheres from their innermost to outermost reaches",
    "mediates liaves co contact with the surrounding world via its manifold": "mediates all our contact with the surrounding world via its manifold",
    "these, let us just mention fe invisible surface that sie (1979, 45) referred": "Among these, let us just mention the invisible surface that Sebeok (1979, 45) referred",
    "Sebeok\n(Se\n1985 (1976), 3).": "(Sebeok 1985 (1976), 3).",
    "Sebeok\n(Se\n1985 (1976), 3)": "(Sebeok 1985 (1976), 3)",
    "((Sebeok 1985 (1976), 3).": "(Sebeok 1985 (1976), 3).",
    "appointed chee essential one": "appointed the essential one",
    "The skin, then, mediates liaves co contact with the surrounding world via its manifold\n\nAmong these": "The skin, then, mediates all our contact with the surrounding world via its manifold surfaces.\n\nAmong these",
    "The skin, then, mediates liaves co contact with the surrounding world via its manifold\n\nthese, let us just mention fe invisible surface that sie (1979, 45) referred": "The skin, then, mediates all our contact with the surrounding world via its manifold surfaces. Among these, let us just mention the invisible surface that Sebeok (1979, 45) referred",
}


def load_dictionary() -> set[str]:
    words_path = Path("/usr/share/dict/words")
    if not words_path.exists():
        return set(TECH_WORDS)

    words = {
        line.strip().lower()
        for line in words_path.read_text(encoding="utf-8", errors="ignore").splitlines()
        if line.strip()
    }
    words.update(TECH_WORDS)
    return words


DICTIONARY = load_dictionary()


def apply_direct_fixes(text: str) -> str:
    for old, new in DIRECT_FIXES.items():
        text = text.replace(old, new)
    return text


def collapse_space(line: str) -> str:
    return re.sub(r"[ \t]+", " ", line).strip()


def is_probable_noise(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return False

    if re.fullmatch(r"\d+\s+[A-Z][A-Z\s]{5,}", stripped):
        return True

    if stripped in RUNNING_HEADERS:
        return True

    if re.fullmatch(r"[0-9]+", stripped):
        return True

    if re.fullmatch(r"[IVXLCDMivxlcdm]+", stripped):
        return True

    if re.fullmatch(r"[0-9IVXLCDMivxlcdm\W_]+", stripped):
        return True

    if stripped in {"v.", "ite)", "a", "Ll", "See"}:
        return True

    if len(stripped) <= 5 and not re.fullmatch(r"[A-Z][a-z]+", stripped):
        alpha = sum(ch.isalpha() for ch in stripped)
        if alpha <= 3:
            return True

    alpha = sum(ch.isalpha() for ch in stripped)
    if alpha == 0:
        return True

    if stripped == stripped.upper() and alpha > 0 and len(stripped) <= 40:
        return True

    # OCR garbage tends to have lots of punctuation/digits with very little letter content.
    if len(stripped) >= 8 and alpha / len(stripped) < 0.45:
        return True

    return False


def is_heading_block(block: list[str]) -> bool:
    if not block:
        return False

    if len(block) <= 2:
        return all(
            len(line) <= 80
            and not line.endswith((".", "?", "!", ":", ";"))
            for line in block
        )

    return False


def is_heading_line(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return False
    if len(stripped) > 90:
        return False
    if stripped.endswith((".", "?", "!", ":", ";")):
        return False
    if stripped == stripped.upper():
        return True
    return bool(re.fullmatch(r"[A-Z][A-Za-z0-9'’\-,:;() ]+", stripped))


def is_footnote_line(line: str) -> bool:
    return bool(re.match(r"^\d+\s", line))


def compress_soft_breaks(lines: list[str]) -> list[str]:
    compressed: list[str] = []
    total = len(lines)

    for i, line in enumerate(lines):
        if line:
            compressed.append(line)
            continue

        prev = next((item for item in reversed(compressed) if item), "")
        next_line = ""
        for j in range(i + 1, total):
            if lines[j]:
                next_line = lines[j]
                break

        if not prev or not next_line:
            if compressed and compressed[-1] != "":
                compressed.append("")
            continue

        if is_heading_line(prev) or is_heading_line(next_line):
            if compressed and compressed[-1] != "":
                compressed.append("")
            continue

        if is_footnote_line(next_line):
            if compressed and compressed[-1] != "":
                compressed.append("")
            continue

        if (
            prev.endswith("-")
            or prev.endswith((",", ";", ":"))
            or not prev.endswith((".", "?", "!", "”", '"'))
            or next_line[:1].islower()
            or next_line[:1] in "([“\"'"
        ):
            continue

        if compressed and compressed[-1] != "":
            compressed.append("")

    return compressed


def smart_join(lines: list[str]) -> str:
    if not lines:
        return ""

    result = lines[0]
    for next_line in lines[1:]:
        if not next_line:
            continue

        if result.endswith("-"):
            left_match = re.search(r"([A-Za-z]+)-$", result)
            right_match = re.match(r"([A-Za-z]+)(.*)$", next_line)
            if left_match and right_match:
                merged = (left_match.group(1) + right_match.group(1)).lower()
                if merged in DICTIONARY:
                    result = result[:-1] + next_line
                    continue

        if result.endswith(("/", "(", "[", '"', "'")):
            result += next_line
            continue

        if next_line.startswith((",", ".", ";", ":", ")", "]")):
            result += next_line
            continue

        result += " " + next_line

    result = re.sub(r"\s+([,.;:!?])", r"\1", result)
    result = re.sub(r"\(\s+", "(", result)
    result = re.sub(r"\s+\)", ")", result)
    return result.strip()


def repair_inline_breaks(text: str) -> str:
    hyphen_pattern = re.compile(r"\b([A-Za-z]+)- ([A-Za-z]+)\b")
    repaired_lines: list[str] = []

    for raw_line in text.splitlines():
        line = re.sub(r"\s*[|<>_{}~\\]+\s*", " ", raw_line)
        line = re.sub(r"[ \t]{2,}", " ", line).strip()

        while True:
            changed = False

            def repl(match: re.Match[str]) -> str:
                nonlocal changed
                left, right = match.group(1), match.group(2)
                merged = (left + right).lower()
                changed = True
                if merged in DICTIONARY:
                    return left + right
                return left + "-" + right

            line = hyphen_pattern.sub(repl, line)
            if not changed:
                break

        line = re.sub(r"\s+([,.;:!?])", r"\1", line)
        line = re.sub(r"\(\s+", "(", line)
        line = re.sub(r"\s+\)", ")", line)
        repaired_lines.append(line)

    return "\n".join(repaired_lines).strip()


def postprocess_file(name: str, text: str) -> str:
    text = apply_direct_fixes(text)

    if name == "010-on-biosemiotics.txt":
        text = re.sub(
            r"John Deely accepts my use of the word semiosphere and suggests “signosphere as a term more appropriate for the narrower designation of semiosphere in Lotman’s sense, leaving the broader coinage and usage to Hoftmeyet’s.*?Not Reductionist",
            "John Deely accepts my use of the word semiosphere and suggests “signosphere as a term more appropriate for the narrower designation of semiosphere in Lotman’s sense, leaving the broader coinage and usage to Hoffmeyer’s credit” (Deely 2001, 629).\n\nNot Reductionist",
            text,
            count=1,
            flags=re.S,
        )
        text = re.sub(
            r"\(Hoffmeyer 1993; 1996; Kawade 1996\)\..*",
            "(Hoffmeyer 1993; 1996; Kawade 1996).",
            text,
            count=1,
            flags=re.S,
        )

    if name == "013-code-duality.txt":
        text = re.sub(
            r"was nothing like the uncontested theory in biology.*?domains of the genetic and the somatic\.",
            "was nothing like the uncontested theory in biology that it is today — and there was indeed no really compelling biological evidence for its truth (Ruse 1979). Religious forces in the United States, in particular, were capable of successfully fighting Darwinism for a considerable portion of the early twentieth century — and, especially in paleontology, the eventual conversion to Darwinism became a long, drawn-out affair. Similarly, the animosity against religion was a frequent component in Darwinian rhetoric and Weismann himself was a dedicated materialist with an aversion to the spiritualist and vitalist overtones present in much neo-Lamarckian theorizing of the time (Depew and Weber 1995). Dusty as these conflicts may seem today, there is no doubt that fires are still smoldering within their ashes. For to the modern mind, Darwinism stands for rationality, materialism, and clear separation of science from ideology or religion — whereas Lamarckism brings associations of irrationalism and religious interference in scientific matters. Thus, still today, critical reconsiderations of Darwinism automatically call forth a suspicion that it is, in fact, not just the specific postulates of Darwinism, but scientific rationality as such, that is being rejected. The old conflicts between science and the Church are not so easily forgotten. Here, however, we must nevertheless venture to have a closer look at this whole complex of ideas. For we are going to argue that Weismann’s doctrine is based on a specific semiotic trick that is characteristic of living systems in general — a trick which Weismann himself could not have uncovered, because it presupposes a knowledge about the molecular semiotic dynamics of life processes that had not yet been discovered in his time. And yet, while the inner core of Weismannism will be in a certain sense confirmed by this reformulated understanding, it is one which in no way supports the aggressive transmission-genetic reduction of evolutionary biology that Weismannism otherwise seems to justify. On the contrary, it appears that the Weismann doctrine depends on a duality between analogue and digital representations that opens the door to a sophisticated interaction between the domains of the genetic and the somatic.",
            text,
            count=1,
            flags=re.S,
        )
        text = re.sub(
            r"In the next chapter, we shall have a closer look at such genetic semiotics\..*",
            "In the next chapter, we shall have a closer look at such genetic semiotics.",
            text,
            count=1,
            flags=re.S,
        )

    if name == "019-biosemiotic-technology.txt":
        text = re.sub(
            r"Thus, in preindustrial peasant societies, nearly all energy consumption was\s+of biological origin and was directly or indirectly provided on the basis of the\s+This not only meant.*?photosynthetic processes of plants\.",
            "Thus, in preindustrial peasant societies, nearly all energy consumption was of biological origin and was directly or indirectly provided on the basis of the photosynthetic processes of plants.\n\n1 This not only meant more work for cultivators, but also meant the introduction of draught animals — and thus the requirement for additional cultivated land to feed the animals. Consequently, not only was the workload dramatically increased in the process, but the ownership of land, as well as new needs for collaboration and planning, introduced a social stratification unseen in egalitarian slash-and-burn farming groups — and, in fact, established the perfect conditions for a propertied class to eventually arise. In the schools of my childhood, this process of loss was portrayed as a significant progress for civilization under the emblem of state formation.",
            text,
            count=1,
            flags=re.S,
        )

    text = re.sub(r"\s+([,.;:!?])", r"\1", text)
    text = re.sub(r"\(\s+", "(", text)
    text = re.sub(r"\s+\)", ")", text)
    return text.strip()


def normalize_structural(text: str) -> str:
    lines = [collapse_space(line) for line in apply_direct_fixes(text).splitlines()]
    kept: list[str] = []
    previous_blank = True
    for line in lines:
        if not line:
            if not previous_blank:
                kept.append("")
            previous_blank = True
            continue

        if is_probable_noise(line):
            continue

        kept.append(line)
        previous_blank = False

    return postprocess_file("", repair_inline_breaks("\n".join(kept).strip())) + "\n"


def normalize_prose(text: str) -> str:
    lines = [collapse_space(line) for line in apply_direct_fixes(text).splitlines()]
    lines = compress_soft_breaks(lines)

    filtered: list[str] = []
    previous_blank = True
    for line in lines:
        if not line:
            if not previous_blank:
                filtered.append("")
            previous_blank = True
            continue

        if is_probable_noise(line):
            continue

        filtered.append(line)
        previous_blank = False

    blocks: list[list[str]] = []
    block: list[str] = []
    for line in filtered:
        if not line:
            if block:
                blocks.append(block)
                block = []
            continue
        block.append(line)
    if block:
        blocks.append(block)

    rendered: list[str] = []
    for block in blocks:
        if block and is_heading_line(block[0]) and len(block) > 1:
            split_at = 0
            while split_at < len(block) and is_heading_line(block[split_at]):
                split_at += 1

            if 0 < split_at < len(block):
                heading = block[:split_at]
                body = block[split_at:]
                rendered.extend(heading)
                rendered.append("")
                rendered.append(smart_join(body))
                rendered.append("")
                continue

        if is_heading_block(block):
            rendered.extend(block)
        else:
            rendered.append(smart_join(block))
        rendered.append("")

    return postprocess_file("", repair_inline_breaks("\n".join(rendered).strip())) + "\n"


def main() -> None:
    NORMALIZED_DIR.mkdir(parents=True, exist_ok=True)

    with tempfile.NamedTemporaryFile(suffix=".txt") as tmp:
        subprocess.run(
            ["pdftotext", str(PDF_AUTHORITY), tmp.name],
            check=True,
        )
        prose_lines = apply_direct_fixes(
            Path(tmp.name).read_text(encoding="utf-8", errors="ignore").replace("\f", "\n")
        ).splitlines()

    prose_sections: dict[str, str] = {}
    for i, (_, rel_path, start) in enumerate(PROSE_SECTIONS):
        end = len(prose_lines) if i == len(PROSE_SECTIONS) - 1 else PROSE_SECTIONS[i + 1][2] - 1
        prose_sections[Path(rel_path).name] = "\n".join(prose_lines[start - 1 : end]).strip() + "\n"

    for raw_path in sorted(RAW_DIR.glob("*.txt")):
        if raw_path.name in STRUCTURAL_FILES:
            text = raw_path.read_text(encoding="utf-8")
            normalized = normalize_structural(text)
        elif raw_path.name in prose_sections:
            text = prose_sections[raw_path.name]
            if raw_path.name in {"051-literature.txt", "052-index.txt"}:
                normalized = normalize_structural(text)
            else:
                normalized = normalize_prose(text)
        else:
            text = raw_path.read_text(encoding="utf-8")
            normalized = normalize_prose(text)

        normalized = postprocess_file(raw_path.name, normalized)
        out_path = NORMALIZED_DIR / raw_path.name
        out_path.write_text(normalized, encoding="utf-8")


if __name__ == "__main__":
    main()
