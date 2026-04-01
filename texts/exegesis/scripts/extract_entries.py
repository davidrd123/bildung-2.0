#!/usr/bin/env python3
"""
Extract bracketed entries and letters from the Exegesis ebook text.
Produces source/entries.yaml with one record per entry.

Usage:
    python3 texts/exegesis/scripts/extract_entries.py
"""

import re
import yaml
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
SOURCE_FILE = REPO_ROOT / "books" / "The Exegesis of Philip K. Dick - Dick, Philip K_.txt"
OUTPUT_FILE = Path(__file__).resolve().parent.parent / "source" / "entries.yaml"

# Canonical counts for the current ebook source. If the source text changes,
# regenerate intentionally and update these after reviewing the diff.
EXPECTED_INDEX = {
    "total_entries": 1009,
    "letters": 21,
    "journal_entries": 988,
    "folders": 75,
    "missing_previews": 26,
}

# Folder date ranges from the published edition's chronological markers
FOLDER_DATES = {
    4: "1974-1976",
    23: "Late 1976",
    24: "Late 1976",
    25: "Late 1976 - Early 1977",
    26: "Early 1977",
    27: "Early 1977",
    34: "1977",
    33: "1977",
    35: "1977",
    36: "1977",
    31: "1977",
    32: "1977",
    50: "Late 1977",
    28: "February 1978",
    29: "1978",
    30: "1978",
    14: "1978",
    15: "1978",
    16: "1978-1979",
    38: "1979",
    18: "1979",
    2: "1979",
    3: "1979",
    19: "1979",
    20: "1979",
    21: "1979",
    22: "1979",
    9: "December 1978",
    11: "December 1979",
    8: "Early 1979",
    6: "Early 1979",
    10: "Early 1979",
    13: "Early 1979",
    39: "March 1979",
    41: "Spring 1979",
    42: "Spring 1979",
    43: "Spring 1979",
    44: "Spring 1979 - January 1980",
    45: "Spring 1979 - January 1980",
    46: "Spring 1979 - January 1980",
    47: "October-November 1979",
    48: "Spring 1979 - January 1980",
    49: "January 1980",
    82: "January-April 1980",
    83: "1981",
    58: "1981",
    1: "1981",
    87: "1981",
    88: "1981",
    85: "1981",
    89: "1981",
    59: "1981",
    60: "1981",
    75: "1981",
    76: "1981",
    84: "1981",
    90: "1981",
    77: "1981",
    78: "1981",
    79: "1981",
    80: "June 1981",
    91: "1981",
    81: "1981-1982",
    62: "1982",
    63: "1982",
    64: "1982",
    56: "1982",
    55: "1982",
    73: "1982",
    53: "1982",
    54: "1982",
    57: "1982",
}

# Patterns
ENTRY_RE = re.compile(r"^\[(\d+\*?):([^\]]+)\]")
# Footnote superscripts appear as digits glued to names/dates, e.g.:
#   "Letter to Peter Fitting,3 June 28, 1974"
LETTER_RE = re.compile(r"^Letter to (.+?),\d*\s*(.+?)$")
FOLDER_RE = re.compile(r"^Folder (\d+\*?)$")
PART_RE = re.compile(r"^PART (ONE|TWO|THREE|FOUR)$")
PREVIEW_FOOTNOTE_RE = re.compile(r"^\d{1,2}\s+")
PREVIEW_UNAVAILABLE = "[preview unavailable in ebook text]"


def clean_preview_text(text):
    """Trim obvious ebook footnote artifacts from preview text."""
    cleaned = re.sub(r"\s+", " ", text.strip())
    if not cleaned:
        return ""
    if cleaned.isdigit():
        return ""
    cleaned = PREVIEW_FOOTNOTE_RE.sub("", cleaned)
    return cleaned.strip()


def extract_first_line(lines, start_idx, max_chars=120):
    """Get first non-empty content line after the entry marker."""
    for i in range(start_idx, min(start_idx + 20, len(lines))):
        line = lines[i].strip()
        if i > start_idx and (ENTRY_RE.match(line) or LETTER_RE.match(line)):
            break
        # Skip empty lines and the entry marker itself
        if not line or ENTRY_RE.match(line) or LETTER_RE.match(line):
            # But entry markers sometimes have content on the same line
            if ENTRY_RE.match(line):
                rest = clean_preview_text(ENTRY_RE.sub("", line).strip())
                if rest:
                    return rest[:max_chars]
            continue
        cleaned = clean_preview_text(line)
        if cleaned:
            return cleaned[:max_chars]
    return PREVIEW_UNAVAILABLE


def validate_entries(entries):
    """Fail fast if extraction drifted or obvious preview junk leaked through."""
    unique_ids = set()
    for entry in entries:
        entry_id = entry["id"]
        if entry_id in unique_ids:
            raise ValueError(f"Duplicate entry id detected: {entry_id}")
        unique_ids.add(entry_id)

        if entry["part"] is None:
            raise ValueError(f"Missing part metadata for {entry_id}")

        preview = entry["first_line"]
        if preview.isdigit():
            raise ValueError(f"Digit-only preview leaked through for {entry_id}: {preview!r}")

        if entry["type"] == "letter":
            if "recipient" not in entry or "letter_date" not in entry:
                raise ValueError(f"Incomplete letter metadata for {entry_id}")

    letters = sum(1 for e in entries if e["type"] == "letter")
    journal_entries = sum(1 for e in entries if e["type"] == "entry")
    folders = len(set(e["folder"] for e in entries))
    missing_previews = sum(1 for e in entries if e["first_line"] == PREVIEW_UNAVAILABLE)

    actual = {
        "total_entries": len(entries),
        "letters": letters,
        "journal_entries": journal_entries,
        "folders": folders,
        "missing_previews": missing_previews,
    }

    if actual != EXPECTED_INDEX:
        raise ValueError(
            "Extracted corpus stats changed. "
            f"Expected {EXPECTED_INDEX}, got {actual}. Review the source text and update intentionally."
        )

    return actual


def main():
    print(f"Reading: {SOURCE_FILE}")
    text = SOURCE_FILE.read_text(encoding="utf-8")
    lines = text.split("\n")
    print(f"Total lines: {len(lines)}")

    entries = []
    current_folder = None
    current_part = None
    letter_context = {}  # line_number -> letter info
    source_id_counts = {}
    source_id_seen = {}

    # First pass: find all letters (they appear just before their entry)
    for i, line in enumerate(lines):
        stripped = line.strip()

        m = LETTER_RE.match(stripped)
        if m:
            letter_context[i] = {
                "recipient": m.group(1).strip(),
                "date": m.group(2).strip().rstrip("*"),
            }

        em = ENTRY_RE.match(stripped)
        if em:
            source_id = f"{em.group(1).rstrip('*')}:{em.group(2).strip()}"
            source_id_counts[source_id] = source_id_counts.get(source_id, 0) + 1

    # Second pass: extract entries
    for i, line in enumerate(lines):
        stripped = line.strip()

        # Track current part
        pm = PART_RE.match(stripped)
        if pm:
            part_names = {"ONE": 1, "TWO": 2, "THREE": 3, "FOUR": 4}
            current_part = part_names.get(pm.group(1))
            continue

        # Track current folder
        fm = FOLDER_RE.match(stripped)
        if fm:
            folder_num = fm.group(1).rstrip("*")
            current_folder = int(folder_num)
            continue

        # Match entry markers
        em = ENTRY_RE.match(stripped)
        if em:
            folder_str = em.group(1).rstrip("*")
            page_str = em.group(2).strip()
            folder = int(folder_str)
            source_id = f"{folder}:{page_str}"

            occurrence = source_id_seen.get(source_id, 0) + 1
            source_id_seen[source_id] = occurrence

            entry_id = source_id
            if source_id_counts[source_id] > 1:
                entry_id = f"{source_id}#{occurrence}"

            # Check if preceded by a letter heading (within 10 lines)
            letter_info = None
            for lookback in range(max(0, i - 10), i):
                if lookback in letter_context:
                    letter_info = letter_context[lookback]
                    break

            entry = {
                "id": entry_id,
                "source_id": source_id,
                "folder": folder,
                "page": page_str,
                "line": i + 1,  # 1-indexed
                "part": current_part,
                "date_approx": FOLDER_DATES.get(folder, "unknown"),
                "type": "letter" if letter_info else "entry",
                "first_line": extract_first_line(lines, i),
            }

            if source_id_counts[source_id] > 1:
                entry["occurrence"] = occurrence

            if letter_info:
                entry["recipient"] = letter_info["recipient"]
                entry["letter_date"] = letter_info["date"]

            entries.append(entry)

    stats = validate_entries(entries)

    print(f"Extracted {stats['total_entries']} entries")
    print(f"  Letters: {stats['letters']}")
    print(f"  Journal entries: {stats['journal_entries']}")
    print(f"  Folders represented: {stats['folders']}")
    print("Validation: OK")

    # Write YAML
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    header = (
        "# The Exegesis of Philip K. Dick — Entry Index\n"
        "# Extracted from the 2011 Jackson/Lethem abridgement.\n"
        "# source_id preserves the printed [folder:page] scheme from Paul Williams's numbering.\n"
        "# When the ebook repeats a printed ID, id receives a #n suffix and occurrence records the repeat order.\n"
        "#\n"
        f"# Total entries: {stats['total_entries']}\n"
        f"# Letters: {stats['letters']}\n"
        f"# Journal entries: {stats['journal_entries']}\n\n"
    )

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(header)
        yaml.dump(
            entries,
            f,
            default_flow_style=False,
            allow_unicode=True,
            sort_keys=False,
            width=120,
        )

    print(f"Written to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
