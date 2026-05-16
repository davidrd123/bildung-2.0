# Campanella — Metaphysica (1638)

This is a bounded Latin source campaign for the work catalogued as Tommaso Campanella's *Universalis philosophiae seu Metaphysicarum rerum, iuxta propria dogmata, partes tres, libri 18* (Paris, 1638, ed. Burellius).

It exists first to make Campanella's *Metaphysica* usable as a source-near reading substrate for `texts/erkenntnisproblem-vol2`, especially the Spinoza chapter (Part 018), where Cassirer cites Campanella's account of intuitive cognition as `intrinsecatio, per quam unum fit aliud` — the soul's becoming-one with its object.

The operating model is closer to Gassendi than to a one-off encounter: transcribe the Latin accurately from the witness, normalize OCR damage transparently, translate in bounded slices, and keep enough apparatus that later chats can address the source directly. This does **not** by itself promote Campanella to `texts/`; it remains `sources/` substrate unless separate engagement work begins producing structural reading notes about Campanella's argument as such.

The long horizon may become closer to the Lotman workflow: page-order transcription and translation of the text rather than only concept-driven slices. The first slices were conceptual pilots around `intrinsecatio`; page-order work now exists in two lanes, a small Part I trial and a Part III reconnaissance sequence. Use smaller page units where the Latin or OCR requires slower verification. Numeric `NNN-*` part filenames are reserved for literal page-order work, with local prefixes such as `part-iii-NNN-*` when a non-contiguous region gets its own sequential run.

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
- `encounters/` keeps citation-grade or concept-anchor passages tied to Cassirer or to a specific crosswalk question. These are deep grounding files, not the only valid output form.
- `parts/` keeps bounded transcription-and-translation slices when the task is making Campanella readable for chat-paced source work. Current non-sequential concept-chain work uses descriptive `pilot-*` filenames; numeric `NNN-*` filenames are reserved for literal page-order transcription/translation.
- `reading/` keeps crosswalks back to `texts/erkenntnisproblem-vol2` and secondary triage notes, such as the Ernst chapter 10 map.
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

To find what work has been done and what is open, read in this order: this README → `journal.md` (chronological, most recent at top) → `source/page-map.yaml` (anchors with extract paths) → `parts/` and `encounters/`. The journal lists open re-entry items in rough priority order; `parts/` and `encounters/` are the load-bearing text artifacts.

## OCR Pipeline

The ABBYY XML is stream-parsed page by page; for each page, blocks are emitted in geometric reading order with their `blockType` preserved, so marginalia, body columns, and running headers can be separated downstream. The script preserves per-character confidence and dictionary-membership flags as inline markers for evaluation passes.

The normalization pass applies long-s repair using the corpus-derived lexicon, with two-tier ranking that prefers exact-lexicon matches with the most `f→s` swaps, falling back to stem-prefix matches (4-8 char) with the longest stem. This catches `intrinsecatio` (stem `intrinse`) and `Cognoscere` (stem `cogno`) while preserving real f-words like `praeficit` and `forma`. Typical body-block OOD-rate reduction is 6-7 percentage points; the residue is mostly æ-glyph drops, joined words, and ligature errors that are not long-s damage.

## Known OCR Issues

- **Long-s read as `f`**. Systematic across the corpus. The substitution `ſ → s` is not a blind regex — real word-final `f`'s must be preserved. Use lexicon validation (`wordFromDictionary` flag from ABBYY plus a Latin lemma list).
- **Marginalia interleaved with body**. ABBYY's `blockType` lets us separate them; the flat hOCR text does not.
- **Running headers mid-page**. Detectable by position; filter at extraction.
- **Hyphenation at line ends**. ABBYY preserves these with `wordFromDictionary` cues; reassemble across line boundaries before lexicon checks.

## Current Priority

The first anchor is now located and opened as `encounters/001-intrinsecatio-cap-ii-art-i.md`: Cassirer's Vol. 2 Part 018 citation of `intrinsecatio, per quam unum fit aliud` corresponds to Pars III, Liber XVII, Caput II, Articulus I, printed page 244 / JP2 leaf 0906.

Current pickup should follow the Gassendi distinction between substrate-building and engagement:

- Build accurate Latin + working English substrate in `parts/` when the goal is making a passage or short run chat-addressable.
- Use `encounters/` for citation-grade anchors that need a fuller local-context file.
- Keep the distinction between concept-chain pilots and eventual literal page-order transcription visible.
- Keep `journal.md`, `glossary.yaml`, and `source/page-map.yaml` in lockstep after each meaningful slice.
- If continuing the Part III reconnaissance, start with `reading/part-iii-structural-survey.md` and the local sequence in `parts/part-iii-001-*` / `parts/part-iii-002-*`. The next continuation is `part-iii-003-*` at leaf 795, `Liber XIV, Caput III`, on Platonic arguments for immortality.
- If continuing the intrinsecation/sapientia chain, leaf 438 is now opened as `parts/pilot-sapientia-mensura-entis-veri.md`; the next local continuation is leaf 439 `ART. VI` on grades of primalities outside God.
- If following the self-knowledge/Cassirer/Descartes signal, the leaf-85/86 ninth-dubitation response and the leaf-86/87 tenth-dubitation response are now opened; the next local continuation is leaf 87 lower half, `Responsio ad Undecimam Dubitationem`.
- If following the Cassirer Vol. 1 self-consciousness signal, `P. II, Lib. VI, Cap. VI, Art. 9` is now opened at leaf 402 in `parts/pilot-part-ii-intellectione-abdita-per-essentiam.md`; `reading/cassirer-vol1-self-consciousness-crosswalk.md` keeps leaf 85/86 as a pilot and says any encounter-grade treatment should probably be a composite self-consciousness dossier.
- If following the Part II primalities signal, the direct triad is now opened at leaves 449-450; the later Ernst harmony/providence pages remain separate targets.
- If absorbing the Campanella substrate back into Cassirer, the Vol. 2 Part 018 crosswalk now exists at `reading/cassirer-vol2-part018-intrinsecation-crosswalk.md`; Cassirer's Part II p. 78 quote on essential love of God and participated divinity having `saporem` is now opened at leaf 444 in `parts/pilot-part-ii-essential-love-sapor.md`. The current artifact decision is to keep hardening the crosswalk rather than create a composite Vol. 2 dossier until additional listed Vol. 2 Campanella footnote loci are opened and need integration with the already opened leaves.
- If switching to page order, a first numeric trial now exists at `parts/001-leaf-0023-art-iii-animal-odor-touch-weight.md`; the next sequential continuation would be leaf 24 section `9`, hearing. Numeric page-order work should follow local argument boundaries across page breaks, not stop mechanically at physical leaf edges.
