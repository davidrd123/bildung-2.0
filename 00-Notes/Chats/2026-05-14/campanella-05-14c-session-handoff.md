# Session `campanella-05-14c` — Handoff Notes

Written at the end of the session, before context compaction. Captures what was done, current mental state, open threads, and re-entry pointers for the next session.

## Session Framing

- **Session name:** `campanella-05-14c` (the third of three on 2026-05-14: `erk-vol02-5-13a` and `erk-vol02-05-14b` preceding)
- **How it started:** A factual question — "how well does Tesseract deal with two-column layout?" — pointed at the IA Campanella scan in `~/Downloads/`. No initial scope to build anything.
- **How it ended:** A full bounded source-extraction campaign for Campanella's *Metaphysica* (1638), with two verified-Latin encounter notes anchoring the Cassirer Vol. 2 Part 018 `intrinsecatio` citation, plus the apparatus to pick it up cold.
- **Layer:** Pure **substrate** work in `sources/latin/` (per the memory entry on substrate vs. engagement that surfaced near the end of session). The encounter notes brush against close-reading-for-translation but are not yet engagement-with-argument; the bridge would be the open `reading/erk-vol2-campanella-crosswalk.md` re-entry item, which would tie findings back to `texts/erkenntnisproblem-vol2/parts/018-...`.
- **Parallel context:** David's other agents committed work into the same branch during the session (a Funktionszusammenhang fix for Spinoza Part 028, Gassendi parts 020-021, a Spinoza Opera scaffold, a Leibniz chapter opening in Vol. 2, a separate handoff log `erk-vol02-05-14b-session-handoff.md`). My commits interleaved with theirs cleanly — no conflicts — but the experience was that several scoped sub-projects can advance concurrently in this repo and the commit log will weave them together.

## What Was Done (Chronological)

1. **Tesseract two-column analysis.** Started as a generic technical answer; sharpened when David pointed at the actual scan. Ran Tesseract on `thomcampanellsty00camp_0114.jp2` (printed page 102). Found: column detection mostly OK, but the *long-s* problem is the dominant character error, plus marginalia/header misplacement. The IA package ships an ABBYY OCR (`_abbyy.gz`) that is materially better and carries per-block typing and per-word `wordFromDictionary` flags. Pivoted the conversation from "should we tune Tesseract" to "use the ABBYY artifact as substrate."

2. **Witness choice.** ABBYY XML over hOCR flat text — the XML preserves block structure (Text/Picture/Separator/Table), per-character coordinates, per-character `suspicious` flags, per-word `wordFromDictionary` flags. The hOCR is a lossy projection of the same OCR pass. Decision recorded in `sources/latin/campanella-metaphysica/source/witnesses.yaml`.

3. **Scaffold mirrored from Gassendi.** Created `sources/latin/campanella-metaphysica/` with same subdir layout as the Gassendi campaign. Copied IA binaries into gitignored dirs (PDF, JP2 dir, ABBYY .gz, hOCR text). Title-page identification done by streaming the ABBYY XML for the first few leaves rather than re-OCRing — confirmed Paris 1638 Burellius edition.

4. **Built three-script ABBYY pipeline.**
   - `extract_abbyy_page.py` — stream-parses `_abbyy.gz`, emits one page as block-typed text. Block classifier (BODY / HEADER / MARGINALIA) uses bbox geometry; fallible at line-wrap-into-margin but documented.
   - `build_lexicon.py` — scrapes ~31.5k words ABBYY's Latin dict recognized across all 972 leaves (~11 s). The clever move: use ABBYY's own dictionary validation as the corpus-specific oracle.
   - `normalize_extract.py` — long-s repair with two-tier ranking. Tier 1: exact lexicon hit, prefer most `f→s` swaps. Tier 2: stem-prefix match (4-8 char), prefer longest stem, then fewest swaps. The longest-stem tiebreaker is what makes the algorithm robust against `praeficit → praesicit` over-corrections while still catching `intrinsecatio` (8-char stem `intrinse` matches in-lexicon `intrinseca`).

5. **First commit** (`7a8c266`) — scaffold + pipeline + pilot page-102 extraction + intrinsecatio anchor located on jp2 leaf 0906.

6. **Encounter 001 written: `intrinsecatio` and the modality of beatitude.** Pars III Lib XVII Cap II Art I, printed page 244. Critical: I verified the Latin against direct JP2 crops, NOT just the OCR-cleaned text. The verification caught two OCR-cleanup errors I would have shipped silently: `sicuti → sicut` (twice) and `tinctas → tincta`. The second is philosophically substantive — `tincta` as feminine ablative singular modifying `luce` produces a chiasmus (light tinted by things, then light shows things) that the wrong agreement obscured. **This was the session's single most important methodological moment.** Without the JP2 crop check, I would have written a "verified" encounter on a hallucinated Latin reading.

7. **Mahomet discovery.** When checking the continuation of the intrinsecatio sentence against the JP2, I read three more lines of body text and found `unde deceptus est Mahometes` — Campanella using the medieval polemical move about Muslims taking the eating-metaphor of paradise literally, in order to argue that the bodily metaphor of *gustatio* is the *correct* figure for beatific cognition. This is the theological/eschatological frame Cassirer's secularizing extraction strips out.

8. **Distribution trace.** David picked "trace intrinsecatio across the volume" from the offered next-steps menu. Grepped ABBYY OCR for `intrinsec*` family — 115 hits across 92 leaves. The noun `intrinsecatio` is a single-occurrence nominalization; verb/adjective forms develop the concept across a five-step conceptual arc (gustus → physical infusion → sapientia → divine immanence → cognitive form of beatitude). Recorded in encounter 001 as a Distribution section.

9. **Encounter 002 written: four-register contemplative ascent.** Pars II Lib X Cap I, printed page 549. The only `intrinsecatur & extrinsecatur` coordinate pair in the volume — at the *Mathematical* register of a four-world cosmological diagram. Discovery: encounter 002 is the *structural mirror* of encounter 001. God intrinsecates AND extrinsecates into creation (enc-002); the mind intrinsecates into God in beatitude (enc-001). Each is a movement of becoming-one-with that doesn't cancel the difference. This is the Christian-Platonist double-movement Cusanus/Aquinas/Bruno frame Cassirer's Spinoza-prefiguration reading wants but doesn't reach for.

10. **Second commit** (`ca866d0`) — encounter 002 + cross-link from encounter 001.

11. **Pickup-readiness audit.** David asked: "do you have enough documentation that another agent could come in and pick back up?" Honest audit found two gaps relative to Gassendi: no `journal.md`, no `glossary.yaml`, plus the rebuild-dependencies for `source/local/abbyy-lexicon.txt` weren't called out in the README.

12. **Documentation backfill** (`ba44555`) — wrote journal.md (single 2026-05-14 entry consolidating session findings + meta-note on documenting-from-behind), glossary.yaml (10 open entries), README Quickstart for New Agents section.

## Mental State / Working Observations

- **The session inverted my usual scope discipline.** It opened as a five-minute factual answer about Tesseract and ended as a full substrate campaign. The escalation was driven by the material, not by me pushing scope. Each step had clear motivation; in retrospect the trajectory was reasonable. But "this started as a question and is now a campaign" was true throughout the last hour.

- **JP2 verification is non-optional.** Twice I would have published wrong Latin if I hadn't cropped the page image. Once was a small grammar slip (`sicuti` vs `sicut`); once was philosophically substantive (the chiasmus). The encounter README now records this discipline. Future encounters in this campaign must follow it.

- **The "documenting from behind" trap is real.** The journal entry, glossary, and Quickstart were all written after the substantive work. I flagged this in the journal's final section, but the right pattern next time is: open the journal first, append in small chunks live, write the encounter, append more, etc. What I did this session was substrate-building at scale with backfilled apparatus — fine as a one-time exception but not a model.

- **The lexicon trick was the most satisfying piece of engineering.** Using ABBYY's `wordFromDictionary` flag as a corpus-derived validator means no external Latin dictionary dependency, and the validator is exactly aligned with the OCR's own confidence — words ABBYY confidently knows are Latin AND words ABBYY confidently mis-OCRs (like `effe` for `esse`) both fall out cleanly. The longest-stem tiebreaker handles the inflection sparsity problem without bloating the dictionary.

- **Parallel commits worked smoothly but felt unfamiliar.** David and his other agents pushed three commits to the same branch during my session. No conflicts because the work was scoped to non-overlapping files. But I noticed that the encounter 001 file I was editing had been touched by a parallel agent — the diff showed my own pre-commit additions appearing in HEAD. Took me a moment to reconstruct what had happened (David committed my work himself, didn't wait for me). This is fine, but worth knowing: in this repo, what I think of as "my work" can be committed by other agents while I'm still iterating on it.

- **Substrate vs. engagement is a clarifying frame.** The memory entry surfaced near the end of the session. Everything in this session lives in `sources/`, which means it builds navigable substrate. The encounter notes are substrate that happens to also contain close-reading findings, but they don't engage with Cassirer's argument — they just record what Cassirer's citation points to and what's adjacent. Engagement would happen if I (or a future agent) wrote `reading/erk-vol2-campanella-crosswalk.md` and tied findings into the Vol. 2 Part 018 reading layer.

## Open Threads / Re-Entry Pointers

These are also in `sources/latin/campanella-metaphysica/journal.md`, but here in rough working priority:

1. **`reading/erk-vol2-campanella-crosswalk.md`** — the engagement bridge. Substrate work is done; the next step is to read Cassirer Vol. 2 Part 018 around the Campanella citation and write the equivalent of `sources/latin/gassendi-disquisitio-metaphysica/reading/erk-vol2-gassendi-crosswalk.md`. This is what turns the substrate into engagement.

2. **Leaf-23 `gustus` encounter** — the bodily phenomenology that funds the entire intrinsecation doctrine ("this sense alone is intrinsecated into the object, and the object entirely into it"). Both encounters 001 and 002 flag this as their conceptual floor. Without it the chain starts mid-air.

3. **Leaf-438 epistemology passage** — where intrinsecation becomes the criterion for *sapientia* against ordinary cognition. Directly relevant to the `Cognoscere est fieri rem cognitam` claim from encounter 001.

4. **Pipeline polish (lower priority)** — the extractor mis-tags right-edge line-wrap as marginalia; a merge-narrow-blocks-back-into-body pass would fix it. Also, printed-page numbers aren't always captured as their own block; widening the HEADER classifier to short-text Picture/Separator blocks near the page top would help.

## Files Worth Looking At First Next Time

- `sources/latin/campanella-metaphysica/journal.md` — chronological state, re-entry list
- `sources/latin/campanella-metaphysica/encounters/001-intrinsecatio-cap-ii-art-i.md` — load-bearing, with Distribution section
- `sources/latin/campanella-metaphysica/encounters/002-four-register-ascent-lib-x-cap-i.md` — load-bearing, mirrors 001
- `sources/latin/campanella-metaphysica/glossary.yaml` — open-status terminology
- `sources/latin/campanella-metaphysica/source/page-map.yaml` — anchors and known leaf alignments

## Commits This Session

- `7a8c266` — scaffold + pipeline + intrinsecatio anchor (initial commit)
- `ca866d0` — encounter 002 + cross-link
- `ba44555` — documentation backfill (journal, glossary, README Quickstart)

Plus the three interleaved parallel commits from David and his other agents: `7e87ef5`, `8694af0`, `1603072`, `439dd5a`.
