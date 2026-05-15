# Campanella — Metaphysica (1638)

This is a bounded Latin source campaign for Tommaso Campanella's *Universalis philosophiae seu Metaphysicarum rerum, iuxta propria dogmata, partes tres, libri III* (Paris, 1638, ed. Burellius).

It exists first to ground and transclude the Campanella material in `texts/erkenntnisproblem-vol2`, especially the Spinoza chapter (Part 018), where Cassirer cites Campanella's account of intuitive cognition as `intrinsecatio, per quam unum fit aliud` — the soul's becoming-one with its object. It is not yet a sequential translation campaign.

## Source Decision

- Single witness: the Internet Archive scan with item identifier `thomcampanellsty00camp` (972 JP2 leaves).
- Three derived artifacts ship with the IA package, in decreasing lossiness:
  - `source/local/thomcampanellsty00camp_abbyy.gz` — full ABBYY FineReader XML with per-character coordinates, block typing, and confidence scores (~88 MB compressed). **Primary OCR witness.**
  - `source/local/thomcampanellsty00camp_hocr_searchtext.txt` — flat text projection of the same OCR (~5.6 MB). Useful for quick grepping; lossy.
  - `source/pdf/campanella-metaphysica-1638-ia.pdf` — searchable PDF for spot navigation.

Unlike the Gassendi campaign, fresh Tesseract on the JP2s is **not** the OCR baseline here. The IA-supplied ABBYY OCR is materially better on early-modern Latin print (long-s aside) and ships with structural metadata Tesseract cannot reproduce. Tesseract may be useful as a stress-witness on isolated glyphs.

## Local Binary Policy

Local binaries are deliberately untracked:

- `source/pdf/`
- `source/page-images/`
- `source/local/` (ABBYY XML and hOCR flat text live here)

The tracked files in this folder should be maps, corrected extracts, translation encounters, glossary entries, journals, and scripts.

## Structure

- `journal.md` — chronological session log; most recent entry at top. Read this to find out what state the campaign is currently in.
- `glossary.yaml` — working glossary of key Latin terms and their Cassirer-side German correspondents; entries marked `status: open` are deliberately unsettled.
- `source/witnesses.yaml` records the IA witness and its three derived artifacts.
- `source/page-map.yaml` records known page correspondences and Vol. 2 anchors.
- `source/raw/` keeps raw ABBYY extraction outputs (per page, structured by block type).
- `source/normalized/` keeps corrected working extracts; long-s repair is the dominant pass.
- `encounters/` keeps source-grounding passages and translation notes. **These are the load-bearing artifacts of the campaign** — each contains verified Latin against the JP2, working translation, and observations.
- `parts/` is reserved for longer sequential translation chunks if the campaign grows.
- `reading/` keeps crosswalks back to `texts/erkenntnisproblem-vol2`.
- `scripts/` keeps local extraction helpers.

## Quickstart for New Agents

A fresh clone of the repo will not have the IA-package binaries (PDF, JP2s, ABBYY XML, hOCR text) — they are gitignored. Before any extraction script will run, those need to be in place and the lexicon needs to be built.

1. **Fetch the IA package.** Search Internet Archive for item identifier `thomcampanellsty00camp`. Download the JP2 zip, the `_abbyy.gz`, the `_hocr_searchtext.txt`, and the `.pdf`.
2. **Copy into the gitignored source dirs** (paths recorded in `source/witnesses.yaml`):
   ```sh
   cp thomcampanellsty00camp.pdf            source/pdf/campanella-metaphysica-1638-ia.pdf
   cp thomcampanellsty00camp_abbyy.gz       source/local/
   cp thomcampanellsty00camp_hocr_searchtext.txt  source/local/
   cp -R thomcampanellsty00camp_jp2/.       source/page-images/jp2/
   ```
3. **Build the lexicon once** (one-time, ~11 s, produces a ~1.4 MB file under `source/local/`):
   ```sh
   python3 scripts/build_lexicon.py
   ```
4. **Extract a page and normalize it** (per anchor):
   ```sh
   python3 scripts/extract_abbyy_page.py --jp2-leaf 906 --output source/raw/intrinsecatio-jp2-0906-abbyy.txt
   python3 scripts/normalize_extract.py  source/raw/intrinsecatio-jp2-0906-abbyy.txt
   ```

To find what work has been done and what is open, read in this order: this README → `journal.md` (chronological, most recent at top) → `source/page-map.yaml` (anchors with extract paths) → the `encounters/` directory. The journal lists open re-entry items in rough priority order; the encounters are the load-bearing artifacts.

## OCR Pipeline

The ABBYY XML is stream-parsed page by page; for each page, blocks are emitted in geometric reading order with their `blockType` preserved, so marginalia, body columns, and running headers can be separated downstream. The script preserves per-character confidence and dictionary-membership flags as inline markers for evaluation passes.

The normalization pass applies long-s repair using the corpus-derived lexicon, with two-tier ranking that prefers exact-lexicon matches with the most `f→s` swaps, falling back to stem-prefix matches (4-8 char) with the longest stem. This catches `intrinsecatio` (stem `intrinse`) and `Cognoscere` (stem `cogno`) while preserving real f-words like `praeficit` and `forma`. Typical body-block OOD-rate reduction is 6-7 percentage points; the residue is mostly æ-glyph drops, joined words, and ligature errors that are not long-s damage.

## Known OCR Issues

- **Long-s read as `f`**. Systematic across the corpus. The substitution `ſ → s` is not a blind regex — real word-final `f`'s must be preserved. Use lexicon validation (`wordFromDictionary` flag from ABBYY plus a Latin lemma list).
- **Marginalia interleaved with body**. ABBYY's `blockType` lets us separate them; the flat hOCR text does not.
- **Running headers mid-page**. Detectable by position; filter at extraction.
- **Hyphenation at line ends**. ABBYY preserves these with `wordFromDictionary` cues; reassemble across line boundaries before lexicon checks.

## Current Priority

The first anchor is Cassirer's Vol. 2 Part 018 (Spinoza, Renaissance background) citation of Campanella's account of intuitive cognition as `intrinsecatio, per quam unum fit aliud`. The corresponding Latin passage location is not yet identified — extracting and grepping the full ABBYY text is the next step.
