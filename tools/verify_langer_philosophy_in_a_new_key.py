#!/usr/bin/env python3

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CLEANED_DIR = ROOT / "sources/modern/langer-philosophy-in-a-new-key/source/cleaned"


EXPECTED_CLEANED_FILES = [
    "000-title-pages-and-publisher-matter.txt",
    "001-preface-to-the-second-edition.txt",
    "002-preface-to-the-first-edition.txt",
    "003-contents.txt",
    "010-the-new-key.txt",
    "011-symbolic-transformation.txt",
    "012-the-logic-of-signs-and-symbols.txt",
    "013-discursive-forms-and-presentational-forms.txt",
    "014-language.txt",
    "015-life-symbols-the-roots-of-sacrament.txt",
    "016-life-symbols-the-roots-of-myth.txt",
    "017-on-significance-in-music.txt",
    "018-the-genesis-of-artistic-import.txt",
    "019-the-fabric-of-meaning.txt",
    "030-acknowledgments.txt",
    "031-index.txt",
]


EXPECTED_KINDLE_GAP_WITNESSES = [
    "source/page-images/kindle-gap/2026-05-04-185135-p76-p77-gap-start.png",
    "source/page-images/kindle-gap/2026-05-04-185146-p77-p78-gap-end.png",
    "source/page-images/kindle-gap/2026-05-04-185225-p78-overlap.png",
]


EXPECTED_PAGE_RANGES = {
    "010-the-new-key.txt": (1, 20),
    "011-symbolic-transformation.txt": (20, 42),
    "012-the-logic-of-signs-and-symbols.txt": (42, 63),
    "013-discursive-forms-and-presentational-forms.txt": (63, 83),
    "014-language.txt": (83, 116),
    "015-life-symbols-the-roots-of-sacrament.txt": (116, 138),
    "016-life-symbols-the-roots-of-myth.txt": (138, 165),
    "017-on-significance-in-music.txt": (165, 199),
    "018-the-genesis-of-artistic-import.txt": (199, 216),
    "019-the-fabric-of-meaning.txt": (216, 239),
    "030-acknowledgments.txt": (240, 242),
    "031-index.txt": (243, 248),
}


EXPECTED_FOOTNOTE_RANGES = {
    "010-the-new-key.txt": (1, 22),
    "011-symbolic-transformation.txt": (1, 19),
    "012-the-logic-of-signs-and-symbols.txt": (1, 14),
    "013-discursive-forms-and-presentational-forms.txt": (1, 18),
    "014-language.txt": (1, 53),
    "015-life-symbols-the-roots-of-sacrament.txt": (1, 26),
    "016-life-symbols-the-roots-of-myth.txt": (1, 35),
    "017-on-significance-in-music.txt": (1, 80),
    "018-the-genesis-of-artistic-import.txt": (1, 17),
    "019-the-fabric-of-meaning.txt": (1, 19),
}


KNOWN_GARBAGE_PATTERNS = [
    r"\\",
    r"»",
    r"«",
    r"b«",
    r"\bH2SO\b",
    r"language9",
    r"symbol15",
    r"L\.esttitlique",
    r"Papal",
    r"MATTHESON'",
    r"\bMOKE\b",
    r"LATIF ISRAEL",
    r"\bHOn\b",
    r"\bISOn\b",
    r"\bIll\b",
    r"\b2!6\b",
    r"\bcury\b",
    r"\btO\b",
    r"\btor\b",
    r"half -",
    r"Les jeux sont fait\b",
]


REQUIRED_MANIFEST_SNIPPETS = [
    "Printed pp. 76-77 are absent from the supplied PDF but have been word-checked against supplied Kindle screenshots",
    "User accepted this Kindle proof as good for the current corpus state on 2026-05-05",
    "As of 2026-05-05, the pp. 76-77 Kindle screenshot proof is accepted as good for the current corpus",
    "Kindle screenshots do not show printed page numbers",
    "Capture target for an alternate/Kindle witness: locate `Preface to the Second Edition`",
    "Capture target for an alternate/Kindle witness: chapter 5, \"Language\"",
    "note 38 absent from the scan",
    "raw witness normalized only",
    "Local artifact search found no alternate Langer PDF, DjVu, EPUB, archive, or book-scan witness",
]


RAW_ONLY_EXCEPTION_SNIPPETS = {
    "001-preface-to-the-second-edition.txt": [
        "Preface to the Second Edition",
        "Les jeux sont faits.",
    ],
    "013-discursive-forms-and-presentational-forms.txt": [
        "[page 76]",
        "[page 77]",
        "symbols—qualities, lines, rhythms—may",
        "Rogues' Gallery",
    ],
    "014-language.txt": [
        "[footnote 38] Ibid., p. 437.",
    ],
}


def collect_page_markers(text: str) -> list[int]:
    return [int(match) for match in re.findall(r"\[page (\d+)\]", text)]


def collect_exact_footnotes(text: str) -> list[int]:
    return [
        int(match)
        for match in re.findall(r"(?m)^\[footnote (\d+)\]", text)
    ]


def expected_range(start: int, end: int) -> list[int]:
    return list(range(start, end + 1))


def check_sequence(
    path: Path,
    actual: list[int],
    expected_start: int,
    expected_end: int,
    label: str,
    errors: list[str],
) -> None:
    expected = expected_range(expected_start, expected_end)
    actual_unique = sorted(set(actual))
    if actual_unique != expected:
        errors.append(
            f"{path.name}: {label} expected {expected_start}-{expected_end}, "
            f"found {actual_unique[:5]}...{actual_unique[-5:] if actual_unique else []}"
        )
    duplicates = sorted({item for item in actual if actual.count(item) > 1})
    if duplicates:
        errors.append(f"{path.name}: duplicate {label}: {duplicates}")


def main() -> int:
    errors: list[str] = []

    if not CLEANED_DIR.is_dir():
        print(f"Missing cleaned directory: {CLEANED_DIR}", file=sys.stderr)
        return 1

    for witness in EXPECTED_KINDLE_GAP_WITNESSES:
        witness_path = ROOT / "sources/modern/langer-philosophy-in-a-new-key" / witness
        if not witness_path.exists():
            errors.append(f"missing Kindle gap witness image: {witness}")
        elif witness_path.stat().st_size == 0:
            errors.append(f"empty Kindle gap witness image: {witness}")

    all_txt_paths = sorted(CLEANED_DIR.glob("*.txt"))
    all_text = {path.name: path.read_text(encoding="utf-8") for path in all_txt_paths}
    actual_cleaned_files = sorted(all_text)
    expected_cleaned_files = sorted(EXPECTED_CLEANED_FILES)
    if actual_cleaned_files != expected_cleaned_files:
        missing = sorted(set(expected_cleaned_files) - set(actual_cleaned_files))
        extra = sorted(set(actual_cleaned_files) - set(expected_cleaned_files))
        errors.append(f"cleaned file set mismatch; missing={missing}, extra={extra}")

    for filename in sorted(set(EXPECTED_PAGE_RANGES) | set(EXPECTED_FOOTNOTE_RANGES)):
        if filename not in all_text:
            errors.append(f"missing required cleaned file: {filename}")

    global_pages: set[int] = set()
    for filename, (start, end) in EXPECTED_PAGE_RANGES.items():
        text = all_text.get(filename, "")
        markers = collect_page_markers(text)
        check_sequence(CLEANED_DIR / filename, markers, start, end, "page markers", errors)
        global_pages.update(markers)

    expected_global_pages = set(range(1, 249))
    if global_pages != expected_global_pages:
        missing = sorted(expected_global_pages - global_pages)
        extra = sorted(global_pages - expected_global_pages)
        errors.append(f"global page marker coverage mismatch; missing={missing}, extra={extra}")

    for filename, (start, end) in EXPECTED_FOOTNOTE_RANGES.items():
        text = all_text.get(filename, "")
        notes = collect_exact_footnotes(text)
        check_sequence(CLEANED_DIR / filename, notes, start, end, "footnotes", errors)

    index_text = all_text.get("031-index.txt", "")
    index_titles = len(re.findall(r"(?m)^INDEX$", index_text))
    if index_titles != 1:
        errors.append(f"031-index.txt: expected one INDEX title, found {index_titles}")

    for filename, snippets in RAW_ONLY_EXCEPTION_SNIPPETS.items():
        text = all_text.get(filename)
        if text is None:
            errors.append(f"missing raw-only exception file: {filename}")
            continue
        for snippet in snippets:
            if snippet not in text:
                errors.append(f"{filename}: missing expected raw-only exception text: {snippet}")

    line_hyphen_re = re.compile(r"[A-Za-z]-\s*$")
    garbage_res = [re.compile(pattern) for pattern in KNOWN_GARBAGE_PATTERNS]
    for filename, text in all_text.items():
        for line_no, line in enumerate(text.splitlines(), start=1):
            if line_hyphen_re.search(line):
                errors.append(f"{filename}:{line_no}: line-ending word hyphen: {line}")
            for garbage_re in garbage_res:
                if garbage_re.search(line):
                    errors.append(
                        f"{filename}:{line_no}: known OCR garbage "
                        f"{garbage_re.pattern!r}: {line}"
                    )

    manifest_path = CLEANED_DIR / "page-proof-manifest.md"
    if not manifest_path.exists():
        errors.append("missing page-proof-manifest.md")
    else:
        manifest_text = manifest_path.read_text(encoding="utf-8")
        for filename in EXPECTED_CLEANED_FILES:
            if f"`{filename}`" not in manifest_text:
                errors.append(f"page-proof-manifest.md missing cleaned file row: {filename}")
        for snippet in REQUIRED_MANIFEST_SNIPPETS:
            if snippet not in manifest_text:
                errors.append(f"page-proof-manifest.md missing required note: {snippet}")

    cleanup_manifest_path = CLEANED_DIR / "cleanup-manifest.md"
    if not cleanup_manifest_path.exists():
        errors.append("missing cleanup-manifest.md")
    else:
        cleanup_text = cleanup_manifest_path.read_text(encoding="utf-8")
        for filename in EXPECTED_CLEANED_FILES:
            if f"`cleaned/{filename}`" not in cleanup_text:
                errors.append(f"cleanup-manifest.md missing cleaned file row: {filename}")

    audit_path = CLEANED_DIR / "completion-audit.md"
    if not audit_path.exists():
        errors.append("missing completion-audit.md")
    else:
        audit_text = audit_path.read_text(encoding="utf-8")
        if "Do not mark the active goal complete yet" not in audit_text:
            errors.append("completion-audit.md does not preserve the non-complete verdict")
        for snippet in [
            "pp. 76-77 are alternate-witness word-proofed",
            "accepted for this corpus on 2026-05-05",
            "remaining deferred items are the second-edition preface and p. 105 footnote 38",
            "For the second-edition preface, locate `Preface to the Second Edition`",
            "Kindle footnote-38 witness",
            "footnote 38",
            "Local artifact search found no alternate Langer PDF, DjVu, EPUB, archive, or book-scan witness",
        ]:
            if snippet not in audit_text:
                errors.append(f"completion-audit.md missing required blocker note: {snippet}")

    if errors:
        print("Langer PNK cleaned verification failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Langer PNK cleaned verification passed.")
    print(f"- checked {len(all_txt_paths)} cleaned text files")
    print("- cleaned file set is complete and covered by manifests")
    print("- page markers cover 1-248 with expected file-local ranges")
    print("- chapter footnotes are contiguous with expected ranges")
    print("- no known OCR garbage or line-ending word hyphen scars found")
    print("- raw-only/alternate-witness exception text is present and documented")
    print(f"- checked {len(EXPECTED_KINDLE_GAP_WITNESSES)} copied Kindle gap witness images")
    print("- proof manifest and completion audit preserve documented blockers")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
