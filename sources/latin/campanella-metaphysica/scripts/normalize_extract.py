#!/usr/bin/env python3
"""Apply long-s repair and hyphen reassembly to a raw ABBYY extract.

Reads a raw extract produced by `extract_abbyy_page.py`, walks block by block,
reassembles line-end hyphenation, and repairs the systematic long-s OCR
artifact (ABBYY rendered glyph 'long s' as 'f' throughout). The repair is
lexicon-validated using the ABBYY-derived lexicon built by `build_lexicon.py`.

Algorithm per word:
  1. Find all positions of 'f' or 'F' in the token.
  2. Skip the word-final position (long-s was never used word-finally).
  3. Enumerate all 2^n subsets of swappable positions.
  4. For each variant, check the normalized form against the lexicon.
  5. Of all variants in the lexicon, prefer the one with the MOST swaps.
  6. If none in the lexicon, return the original (conservative).

The "most swaps" preference implements the printing convention: any 'f' that
could be a long-s should be, unless that produces a non-word.

Output is written to source/normalized/ with a per-block stats footer.
"""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from itertools import combinations
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_LEXICON = PROJECT_ROOT / "source" / "local" / "abbyy-lexicon.txt"

BLOCK_HEADER_RE = re.compile(r"^\[(HEADER|BODY|MARGINALIA|OTHER)\]\s+blockType=")
COMMENT_RE = re.compile(r"^#")
WORD_RE = re.compile(r"[A-Za-zæÆœŒàáâãäåèéêëìíîïòóôõöùúûüçñÀÁÂÃÄÅÈÉÊËÌÍÎÏÒÓÔÕÖÙÚÛÜÇÑ]+")
MAX_F_FOR_SEARCH = 6


def normalize_token(token: str) -> str:
    decomposed = unicodedata.normalize("NFKD", token.lower())
    return "".join(c for c in decomposed if c.isalpha() and ord(c) < 128)


def load_lexicon(path: Path) -> tuple[set[str], set[str]]:
    """Return (full-word set, 4-6 char prefix set).

    The prefix set lets us match inflected forms whose nominative is in the
    lexicon: a candidate `stupido` (dative) shares the prefix `stupi` with the
    in-lexicon `stupidus`, so its 4-char prefix `stup` matches. This broadens
    recall substantially given the sparse coverage of inflected forms.
    """
    words = {line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()}
    stems: set[str] = set()
    for w in words:
        for n in (4, 5, 6, 7, 8):
            if len(w) > n:
                stems.add(w[:n])
    return words, stems


def longest_stem_match(token: str, stems: set[str]) -> int:
    """Return the length of the longest 4-8-char prefix of token that is in stems, or 0."""
    for n in (8, 7, 6, 5, 4):
        if len(token) >= n and token[:n] in stems:
            return n
    return 0


def in_lexicon(token: str, words: set[str], stems: set[str]) -> bool:
    if token in words:
        return True
    return longest_stem_match(token, stems) > 0


def repair_word(word: str, words: set[str], stems: set[str]) -> tuple[str, bool]:
    """Return (repaired_word, was_repaired)."""
    f_positions = [i for i, c in enumerate(word) if c in ("f", "F")]
    if not f_positions:
        return word, False

    last = len(word) - 1
    swappable = [i for i in f_positions if i != last]
    if not swappable:
        return word, False
    if len(swappable) > MAX_F_FOR_SEARCH:
        return word, False

    # Two-tier ranking:
    #   Tier 1 — variants whose lowercased form is in the exact word set.
    #            Among these, prefer MOST swaps. (Long-s should always be
    #            repaired when the repaired form is a known Latin word.)
    #   Tier 2 — variants matching only by stem prefix (4-8 chars).
    #            Among these, prefer LONGEST stem; tiebreak by FEWEST swaps.
    #            The longest-stem rule discriminates ambiguous swaps: e.g.
    #            `intrinsecatio` matches the 8-char stem `intrinse` while
    #            `intrinfecatio` matches only the 6-char `intrin`, so the
    #            former wins; `praesicit` (stem `praes`) loses to `praeficit`
    #            (stem `praefic`) which has a longer match.
    exact_variant: str | None = None
    exact_swaps = -1
    stem_variant: str | None = None
    stem_len = -1
    stem_swaps = -1

    for r in range(len(swappable) + 1):
        for subset in combinations(swappable, r):
            chars = list(word)
            for pos in subset:
                chars[pos] = "S" if chars[pos] == "F" else "s"
            cand = "".join(chars)
            cand_norm = normalize_token(cand)
            if not cand_norm:
                continue
            if cand_norm in words:
                if r > exact_swaps:
                    exact_variant = cand
                    exact_swaps = r
            else:
                ln = longest_stem_match(cand_norm, stems)
                if ln == 0:
                    continue
                if (ln > stem_len) or (ln == stem_len and (stem_swaps == -1 or r < stem_swaps)):
                    stem_variant = cand
                    stem_len = ln
                    stem_swaps = r

    chosen = exact_variant if exact_variant is not None else stem_variant
    if chosen is None:
        return word, False
    return chosen, chosen != word


def repair_text(text: str, words: set[str], stems: set[str]) -> tuple[str, int, int]:
    """Return (repaired_text, words_examined, words_repaired)."""
    words_examined = 0
    words_repaired = 0

    def sub(match: re.Match) -> str:
        nonlocal words_examined, words_repaired
        words_examined += 1
        word = match.group(0)
        new_word, changed = repair_word(word, words, stems)
        if changed:
            words_repaired += 1
        return new_word

    return WORD_RE.sub(sub, text), words_examined, words_repaired


def reassemble_hyphens(lines: list[str]) -> list[str]:
    """Join lines where the previous line ends in '-' or '¬'."""
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        # Look for line-end hyphenation
        stripped = line.rstrip()
        while i + 1 < len(lines) and (stripped.endswith("-") or stripped.endswith("¬")):
            head = stripped[:-1]
            next_line = lines[i + 1]
            # split next line at first whitespace to grab the joined fragment
            j = 0
            while j < len(next_line) and next_line[j].isspace():
                j += 1
            k = j
            while k < len(next_line) and not next_line[k].isspace():
                k += 1
            fragment = next_line[j:k]
            rest = next_line[k:].lstrip()
            stripped = head + fragment
            lines[i + 1] = rest
            if not rest:
                i += 1
            else:
                break
        out.append(stripped)
        i += 1
    return out


def out_of_dict_rate(text: str, words: set[str], stems: set[str]) -> tuple[int, int, float]:
    total = 0
    ood = 0
    for match in WORD_RE.finditer(text):
        token = normalize_token(match.group(0))
        if not token or len(token) <= 1:
            continue
        total += 1
        if not in_lexicon(token, words, stems):
            ood += 1
    rate = (ood / total * 100.0) if total else 0.0
    return ood, total, rate


def process_blocks(input_text: str, words: set[str], stems: set[str], keep_marginalia: bool) -> str:
    lines = input_text.splitlines()
    out: list[str] = []
    block_role: str | None = None
    block_lines: list[str] = []
    block_count = 0
    overall_ood_pre = 0
    overall_total_pre = 0
    overall_ood_post = 0
    overall_total_post = 0

    def flush_block() -> None:
        nonlocal overall_ood_pre, overall_total_pre, overall_ood_post, overall_total_post
        nonlocal block_count
        if block_role is None:
            return

        block_count += 1
        if block_role in ("BODY",) or (keep_marginalia and block_role == "MARGINALIA"):
            joined = reassemble_hyphens(block_lines[:])
            joined_text = "\n".join(joined)
            ood_pre, tot_pre, rate_pre = out_of_dict_rate(joined_text, words, stems)
            repaired_text, examined, repaired = repair_text(joined_text, words, stems)
            ood_post, tot_post, rate_post = out_of_dict_rate(repaired_text, words, stems)

            overall_ood_pre += ood_pre
            overall_total_pre += tot_pre
            overall_ood_post += ood_post
            overall_total_post += tot_post

            out.append(
                f"[{block_role}] words={tot_pre}  "
                f"pre-repair-OOD={ood_pre} ({rate_pre:.1f}%)  "
                f"post-repair-OOD={ood_post} ({rate_post:.1f}%)  "
                f"repaired={repaired}"
            )
            out.append(repaired_text)
            out.append("")
        elif block_role == "HEADER":
            # Keep headers as a one-line note, do not repair
            joined = " ".join(line.strip() for line in block_lines if line.strip())
            out.append(f"[{block_role}] {joined}")
            out.append("")
        elif block_role == "MARGINALIA":
            out.append(f"[{block_role}] (dropped: --no-marginalia)")
            out.append("")

    for line in lines:
        if COMMENT_RE.match(line):
            out.append(line)
            continue
        m = BLOCK_HEADER_RE.match(line)
        if m:
            flush_block()
            block_role = m.group(1)
            block_lines = []
            continue
        if block_role is not None:
            block_lines.append(line)

    flush_block()

    rate_pre = (overall_ood_pre / overall_total_pre * 100.0) if overall_total_pre else 0.0
    rate_post = (overall_ood_post / overall_total_post * 100.0) if overall_total_post else 0.0
    summary = (
        "\n# === overall ===\n"
        f"# body words: {overall_total_pre}\n"
        f"# pre-repair OOD:  {overall_ood_pre} ({rate_pre:.2f}%)\n"
        f"# post-repair OOD: {overall_ood_post} ({rate_post:.2f}%)\n"
        f"# OOD-rate reduction: {rate_pre - rate_post:.2f} percentage points\n"
    )
    return "\n".join(out) + summary


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="raw extract file (from extract_abbyy_page.py)")
    parser.add_argument("--output", type=Path, help="output path (default: derive from input)")
    parser.add_argument("--lexicon", type=Path, default=DEFAULT_LEXICON)
    parser.add_argument(
        "--no-marginalia",
        action="store_true",
        help="drop marginalia blocks from output (default: keep)",
    )
    args = parser.parse_args()

    if not args.input.exists():
        sys.exit(f"missing input: {args.input}")
    if not args.lexicon.exists():
        sys.exit(f"missing lexicon: {args.lexicon}  (run build_lexicon.py first)")

    words, stems = load_lexicon(args.lexicon)
    raw = args.input.read_text(encoding="utf-8")
    out = process_blocks(raw, words, stems, keep_marginalia=not args.no_marginalia)

    if args.output:
        out_path = args.output if args.output.is_absolute() else PROJECT_ROOT / args.output
    else:
        rel = args.input.relative_to(PROJECT_ROOT)
        out_path = PROJECT_ROOT / "source" / "normalized" / rel.name.replace(".txt", ".normalized.txt")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(out, encoding="utf-8")
    print(f"wrote normalized extract to {out_path}")

    # Echo summary line for convenience
    for line in out.splitlines()[-5:]:
        if line.startswith("# "):
            print(line)


if __name__ == "__main__":
    main()
