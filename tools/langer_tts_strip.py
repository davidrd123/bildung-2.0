#!/usr/bin/env python3
"""
Strip a Langer cleaned chapter file into TTS-ready text.

Removes:
- [page XX] markers (including mid-word splits)
- [footnote N] blocks (the footnote text paragraphs)
- Inline footnote reference numbers (trailing superscript-style digits)
- ALL CAPS chapter-opening words (normalizes to sentence case)

Keeps:
- All of Langer's prose
- Quotation blocks
- Chapter title
"""

import re
import sys
from pathlib import Path


def strip_to_tts(text: str) -> str:
    # 1. Fix mid-word/mid-sentence page breaks.
    # First handle mid-word: "com[page 65]plex" -> "complex"
    # Then mid-sentence: "requires\n\n[page 66]\n\nus to" -> "requires us to"
    # Strategy: replace [page XX] with empty, then fix resulting double-newlines
    # that were caused by page markers appearing between continuation lines.

    # Replace page markers that appear mid-line (no newline before/after in context)
    text = re.sub(r'\[page \d+\]', '', text)

    # 2. Remove footnote blocks BEFORE joining, so they don't block the join.
    # Footnotes appear as "[footnote N] text..." paragraphs
    lines = text.split('\n')
    out_lines = []
    in_footnote = False
    for line in lines:
        if re.match(r'\[footnote[ \w]*\]', line, re.IGNORECASE):
            in_footnote = True
            continue
        if in_footnote:
            if line.strip() == '':
                in_footnote = False
            continue
        out_lines.append(line)
    text = '\n'.join(out_lines)

    # Now fix cases where stripping page markers/footnotes left a broken paragraph:
    # Heuristic: if a line ends without sentence-ending punctuation and the next
    # non-blank line starts with lowercase, join them.
    lines = text.split('\n')
    joined = []
    i = 0
    while i < len(lines):
        line = lines[i]
        # Check if this line ends mid-sentence (no terminal punctuation)
        # and is followed by blank line(s) then a lowercase continuation
        if (line.strip() and
            not re.search(r'[.!?:"\'\)]\s*$', line.strip()) and
            not line.strip().startswith('"')):
            # Look ahead past blank lines
            j = i + 1
            while j < len(lines) and lines[j].strip() == '':
                j += 1
            if j < len(lines) and lines[j].strip():
                first_char = lines[j].strip()[0]
                if first_char.islower():
                    # This is a continuation - join
                    joined.append(line.rstrip() + ' ' + lines[j].strip())
                    i = j + 1
                    continue
        joined.append(line)
        i += 1
    text = '\n'.join(joined)

    # 3. Remove inline footnote reference numbers.
    # These appear as " 7 " or " 11 " after sentence-ending punctuation, mid-paragraph.
    # Also after words directly (e.g., "language 9 is").
    # Be careful not to strip legitimate numbers like "(4.0311)" or "59,049"
    # Pattern A: after sentence-ending punct + space + number + space before next sentence
    text = re.sub(r'(?<=[\.\"\'\)\?\!]) (\d{1,2})(?= [A-Z])', '', text)
    # Pattern B: after a word + space + small number (1-18) + space + lowercase (mid-sentence ref)
    text = re.sub(r'(?<=[a-z]) (\d{1,2})(?= [a-z])', '', text)
    # Pattern C: at end of line
    text = re.sub(r'(?<=[\.\"\'\)\?\!]) (\d{1,2})(?=\s*$)', '', text, flags=re.MULTILINE)

    # 4. Normalize ALL CAPS opening (e.g., "THE LOGICAL THEORY" -> "The logical theory")
    # Find the first line that starts with multiple ALL CAPS words (the chapter opening)
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if line.strip():
            match = re.match(r'^([A-Z]{2,}(?:\s+[A-Z]{2,})+)', line)
            if match:
                caps_part = match.group(1)
                # First word capitalized, rest lowercase
                fixed = caps_part[0] + caps_part[1:].lower()
                lines[i] = fixed + line[len(caps_part):]
                break
    text = '\n'.join(lines)

    # 5. Collapse multiple blank lines to max 2
    text = re.sub(r'\n{3,}', '\n\n', text)

    # 6. Strip leading/trailing whitespace
    text = text.strip() + '\n'

    return text


def main():
    if len(sys.argv) < 3:
        print("Usage: langer_tts_strip.py <input_cleaned_file> <output_tts_file>")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])

    if not input_path.exists():
        print(f"Error: {input_path} does not exist")
        sys.exit(1)

    text = input_path.read_text(encoding='utf-8')

    # Strip the "4." prefix from "4. Discursive and Presentational Forms" -> chapter number word
    # Convert "4." to "Four." for spoken form
    number_words = {
        '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five',
        '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine', '10': 'Ten',
        '11': 'Eleven', '12': 'Twelve'
    }
    # Match chapter number at start: "4. Title"
    m = re.match(r'^(\[page \d+\]\s*)*(\d+)\.\s*', text)
    if m:
        num = m.group(2)
        word = number_words.get(num, num)
        text = text[m.end():]
        # Get title (next line or rest of first line)
        title_match = re.match(r'([^\n]+)', text.strip())
        if title_match:
            title = title_match.group(1).strip()
            text = text[title_match.end():].lstrip('\n')
            text = f"{word}. {title}\n\n{text}"

    result = strip_to_tts(text)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(result, encoding='utf-8')
    print(f"Written TTS file: {output_path}")
    print(f"  Lines: {len(result.splitlines())}")
    print(f"  Size: {len(result)} bytes")


if __name__ == '__main__':
    main()
