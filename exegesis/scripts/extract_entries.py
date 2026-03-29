#!/usr/bin/env python3
"""
Extract bracketed entries and letters from the Exegesis ebook text.
Produces source/entries.yaml with one record per entry.

Usage:
    python3 exegesis/scripts/extract_entries.py
"""

import re
import yaml
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
SOURCE_FILE = PROJECT_ROOT / "books" / "The Exegesis of Philip K. Dick - Dick, Philip K_.txt"
OUTPUT_FILE = Path(__file__).resolve().parent.parent / "source" / "entries.yaml"

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
    9: "Early 1979",
    11: "Early 1979",
    8: "Early 1979",
    6: "1979",
    10: "1979",
    13: "1979-1980",
    39: "1979-1980",
    41: "1980",
    42: "1980",
    43: "1980",
    44: "1980",
    45: "1980",
    46: "1980",
    47: "1980",
    48: "1980",
    49: "1980-1981",
    82: "1981",
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


def extract_first_line(lines, start_idx, max_chars=120):
    """Get first non-empty content line after the entry marker."""
    for i in range(start_idx, min(start_idx + 10, len(lines))):
        line = lines[i].strip()
        # Skip empty lines and the entry marker itself
        if not line or ENTRY_RE.match(line) or LETTER_RE.match(line):
            # But entry markers sometimes have content on the same line
            if ENTRY_RE.match(line):
                rest = ENTRY_RE.sub("", line).strip()
                if rest:
                    return rest[:max_chars]
            continue
        if line:
            return line[:max_chars]
    return ""


def main():
    print(f"Reading: {SOURCE_FILE}")
    text = SOURCE_FILE.read_text(encoding="utf-8")
    lines = text.split("\n")
    print(f"Total lines: {len(lines)}")

    entries = []
    current_folder = None
    current_part = None
    letter_context = {}  # line_number -> letter info

    # First pass: find all letters (they appear just before their entry)
    for i, line in enumerate(lines):
        m = LETTER_RE.match(line.strip())
        if m:
            letter_context[i] = {
                "recipient": m.group(1).strip(),
                "date": m.group(2).strip().rstrip("*"),
            }

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

            # Check if preceded by a letter heading (within 10 lines)
            letter_info = None
            for lookback in range(max(0, i - 10), i):
                if lookback in letter_context:
                    letter_info = letter_context[lookback]
                    break

            entry = {
                "id": f"{folder}:{page_str}",
                "folder": folder,
                "page": page_str,
                "line": i + 1,  # 1-indexed
                "part": current_part,
                "date_approx": FOLDER_DATES.get(folder, "unknown"),
                "type": "letter" if letter_info else "entry",
                "first_line": extract_first_line(lines, i),
            }

            if letter_info:
                entry["recipient"] = letter_info["recipient"]
                entry["letter_date"] = letter_info["date"]

            entries.append(entry)

    print(f"Extracted {len(entries)} entries")
    print(f"  Letters: {sum(1 for e in entries if e['type'] == 'letter')}")
    print(f"  Journal entries: {sum(1 for e in entries if e['type'] == 'entry')}")
    print(f"  Folders represented: {len(set(e['folder'] for e in entries))}")

    # Write YAML
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    header = (
        "# The Exegesis of Philip K. Dick — Entry Index\n"
        "# Extracted from the 2011 Jackson/Lethem abridgement.\n"
        "# Archival IDs follow the [folder:page] scheme from Paul Williams's numbering.\n"
        "#\n"
        f"# Total entries: {len(entries)}\n"
        f"# Letters: {sum(1 for e in entries if e['type'] == 'letter')}\n"
        f"# Journal entries: {sum(1 for e in entries if e['type'] == 'entry')}\n\n"
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
