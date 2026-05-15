# Journal

## 2026-05-14 — Scaffold, ABBYY Pipeline, and Two Encounters

Set up the bounded Latin source campaign for Campanella's *Universalis philosophiae seu Metaphysicarum rerum* (Paris 1638, ed. Burellius, IA item `thomcampanellsty00camp`) under `sources/latin/`. The campaign is for grounding the Cassirer Vol. 2 Part 018 citation of `intrinsecatio, per quam unum fit aliud` into the Spinoza chapter's Renaissance background, not a sequential translation project yet.

### Source decision

Single digital witness, three derived artifacts of decreasing lossiness:

- ABBYY FineReader XML (`source/local/thomcampanellsty00camp_abbyy.gz`, 88 MB) — **primary OCR witness.** Carries per-block typing (Text/Picture/Separator/Table), per-character coordinates and confidence, and per-word `wordFromDictionary` flags. Materially better than fresh Tesseract on this 1638 long-s print.
- hOCR flat-text projection of the same OCR (`source/local/thomcampanellsty00camp_hocr_searchtext.txt`, 5.6 MB) — useful for grep-level navigation; lossy.
- IA-shipped PDF (`source/pdf/campanella-metaphysica-1638-ia.pdf`, 125 MB) — useful for visual navigation.

Tesseract is **not** the OCR baseline for this campaign. The IA-shipped ABBYY OCR is materially better and ships with structural metadata Tesseract cannot reproduce.

### Pipeline built

Three scripts under `scripts/`:

- `extract_abbyy_page.py` — stream-parses the gzipped ABBYY XML, emits one page as block-typed text with per-block suspicious-char and out-of-dictionary stats. ~1-2 s per page.
- `build_lexicon.py` — scrapes every word ABBYY's own Latin dictionary recognized (`wordFromDictionary="1"`) across all 972 leaves; produces ~31.5k unique forms in ~11 s. Output is gitignored at `source/local/abbyy-lexicon.txt`.
- `normalize_extract.py` — long-s repair plus line-end hyphen reassembly. Two-tier ranking: exact-lexicon match with preference for *most* `f→s` swaps; then stem-prefix (4-8 char) match with preference for *longest* stem and *fewest* swaps. Catches `intrinsecatio` (stem `intrinse`) and `Cognoscere` (stem `cogno`) while preserving `praeficit` and `forma`. Reduces body-block OOD rate by ~6-7 percentage points on the two pages tested.

### Two encounters opened

- **Encounter 001 — Intrinsecatio and the modality of beatitude** (`encounters/001-intrinsecatio-cap-ii-art-i.md`). Pars III, Lib. XVII, Cap. II, Art. I (printed page 244, jp2 leaf 0906). The Cassirer-anchor passage. Verified Latin against direct JP2 crops of both columns — caught two OCR-cleanup errors (`sicuti → sicut`; `tinctas → tincta`) that the latter case produces a chiasmus the OCR-only reading obscured. Recorded the continuation Cassirer strips (`Sic Anima, quoniam in hac vita non fit Deus...` plus the *Mahomet* polemic about taking the eating-metaphor of paradise literally), the Latin-German lexical bridge, and the cross-volume distribution of the `intrinsec*` family.

- **Encounter 002 — Four-register contemplative ascent** (`encounters/002-four-register-ascent-lib-x-cap-i.md`). Pars II, Lib. X, Cap. I (printed page 549, jp2 leaf 0617). The only `intrinsecatur & extrinsecatur` coordinate pair in the volume, naming God's simultaneous immanence and transcendence into all things. Structurally mirrors encounter 001: the mind's *intrinsecatio* into God in beatitude reflects God's *intrinsecatur & extrinsecatur* into creation at the Mathematical register. The ascent climaxes in *intuitus, comprehensio, fruitio* — the same vocabulary the leaf-906 beatitude chapter uses.

### Working finding

The intrinsec family is volume-spanning (115 hits across 92 leaves). The substantive noun `intrinsecatio` is a single-occurrence nominalization at the Cassirer-anchor passage; verb and adjective forms develop the concept across a conceptual arc: gustatory phenomenology (leaf 23) → physical infusion of forms (leaf 210) → epistemological doctrine of sapientia (leaf 438) → God's immanence/transcendence (leaf 617) → cognitive form of beatitude (leaf 906). Cassirer's German paraphrase takes the climax phrase and abstracts it from this developmental chain, isolating the *form* (intuitive cognition as inner becoming-one) from the *substance* (the bodily figure of taste, the Christian-Platonist double-movement, the eschatological deferral).

The Spinoza connection Cassirer draws sits on the formal endpoint alone. The deeper Bruno / Cusanus / Aquinas connection would sit at leaf 617's metaphysical register and at the gustatio foundation on leaf 23.

### Re-entry

Three primary-contact targets remain, each grounded in passages already identified by the cross-volume grep:

1. **Leaf 23 `gustus` passage** — the foundational use where intrinsecation enters as taste's mode of operation ("this sense alone is intrinsecated into the object"). Without this, the conceptual chain in encounters 001/002 starts mid-air.
2. **Leaf 438 epistemology passage** — "[the fool] nesciret se illa cogniturum non mensura entis, & veri, sed mensura sui." Where intrinsecation becomes the criterion for *sapientia* against ordinary cognition. Connects directly to the `Cognoscere est fieri rem cognitam` claim from encounter 001.
3. **Crosswalk back to Cassirer Vol. 2 Part 018** — read what Cassirer is *doing* in the German prose immediately around the Campanella citation and write `reading/erk-vol2-campanella-crosswalk.md` (matching the Gassendi pattern).

### Smaller pipeline items still open

- The printed-page number on a leaf is sometimes not captured as its own block by ABBYY (we saw this on leaf 906). A small extractor improvement would also surface short-text Picture/Separator-typed blocks near the page top.
- ABBYY occasionally false-segments the last word or two of a body line at the right edge as a narrow "marginalia"-style block. We saw this on leaf 906 with the trailing "rem cognitam." A merge-narrow-blocks-back-into-body pass would help.
- The `ideare imaginanti convenit verius omnia` line in encounter 002 wants its own probe. The grammar is dense and the rendering is provisional.

### Meta-note on documentation timing

Most of the apparatus in this campaign (the journal you are reading, the glossary, the Quickstart section in the README) was written **after** the substantive findings were already in place. That is the opposite of how it should normally go: documentation captured live as work happens is reliable; documentation reconstructed from artifacts has to take on faith what mattered to the agent who did the work.

For Campanella specifically, the encounters were written with verification discipline live — so they are reliable. But the prioritization among re-entry items, the choice of which passages were "central" versus "peripheral", and the working-glossary entries reflect a single agent's view at the end of one session. A fresh agent picking up should treat this journal as a guide to *what was emphasized*, not as the only plausible ordering of the work. The encounter notes themselves remain the load-bearing artifacts.
