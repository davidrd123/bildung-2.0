# Sequential Run Review Standard

This is the reviewer-side companion to `sequential-run-standard.md`. Use it before declaring any tranche of `part-iii-NNN-*` (or other numeric sequential) parts acceptable.

The lesson from the `part-iii-003` through `part-iii-027` tranche is simple: structural review is not content review. The tranche passed every format check (file sizes 37-43 lines, sequential numbering, scratch file populated, apparatus untouched as instructed, filename arc tracing Liber XIV end-to-end) and still produced selected-Latin-disguised-as-transcription plus summary-disguised-as-translation. Reading the diff at structural level was not enough. Reading the files against the extracts was.

## What Failed Last Time

The tranche was approved on the basis of:

- file count (25)
- file size (tight, ~40 lines each)
- filename architecture (Liber XIV end-to-end, then Liber XVI opening)
- format compliance (`## Latin` / `## English` / `## Note` structure present)
- methodology compliance (apparatus untouched, scratch used as instructed)

None of those checks opened a file and read the Latin against the normalized extract. None then read the English against the Latin. They were all surface-level. The actual content failure was visible in any single file: `## Latin` sections carried selected, cleaned argument skeletons rather than complete body transcription, and `## English` sections began with paraphrase signals like *"Campanella first lets the Aristotelian argument state itself"* and proceeded to digest rather than translate.

The reviewer mistake was treating the producer's report ("Done. I... marked it complete.") and the structural diff as sufficient evidence. They are necessary, never sufficient.

## First Gate: Latin Completeness

Check the Latin before judging the English. If the `## Latin` section is not a complete-enough working transcription of the leaf's body text, the file is not a translated sequential part, even if the English summary is useful.

For at least one sampled file in every tranche, open the normalized extract and compare it block by block against `## Latin`.

The Latin passes only if:

- all substantive `[BODY]` blocks from the normalized extract are represented, unless the file explicitly marks a local omission
- the represented Latin follows the extract order
- headings are included when they identify section structure
- running headers, page numbers, and non-substantive marginalia are excluded
- substantive marginalia are either included or explicitly noted as excluded
- OCR uncertainty is visible with `[?]`, not silently normalized into confidence
- the section heading says `Latin excerpts` if the file intentionally selects rather than transcribes

The Latin fails if:

- a dense extract is reduced to a few clean thesis paragraphs
- examples, objections, citations, or transitions disappear without a marker
- the English translates claims that are not actually present in the Latin section
- the file gives the impression of complete transcription while only carrying the argument skeleton

When the Latin fails, stop there. Do not proceed to "but the English is useful." The file is a summary artifact, not a translated sequential part.

## Mandatory Spot-Check

Before approving any tranche, sample at least 3 files — one near the beginning, one near the middle, one near the end. For each:

1. Open the normalized extract for the same leaf.
2. Compare the extract's `[BODY]` blocks against the part's `## Latin` section. Is the Latin body text represented in order, or has it been condensed into selected excerpts?
3. If the normalized extract is damaged or ambiguous, open the raw extract too and check whether the part visibly marks the uncertainty.
4. Only after the Latin passes, read the `## English` section. Does each substantive Latin paragraph have a corresponding English paragraph?

If any sampled file fails, the tranche is provisional until audited file-by-file. Do not absorb apparatus until the audit completes.

## Per-File Checklist

For each sampled file, the checks mirror `sequential-run-standard.md`'s fidelity check:

- [ ] `## Latin` contains the body argument in sequence, not a selected quotation bank
- [ ] `## Latin` has been checked against the normalized extract, not only against itself
- [ ] Substantive `[BODY]` blocks are represented or visibly marked as omitted/damaged
- [ ] Running headers and non-substantive marginalia are excluded
- [ ] Each substantive Latin paragraph has a corresponding English paragraph
- [ ] English order matches Latin order (a reader could reconstruct one from the other)
- [ ] No paraphrase signals appear inside `## English`: "Campanella argues...", "his reply is...", "the leaf shows...", "the key move is...", "this means..."
- [ ] Synthesis is in `## Note`, not in `## English`
- [ ] Hard readings are marked `[?]`, not silently smoothed
- [ ] If the file is selected Latin, the header reads `Latin excerpts`, not `Latin`

## Paraphrase Signal Quick-Grep

Run this grep against any tranche before approval as a smoke test, not as a verdict:

```sh
rg -l '^(Campanella |His reply|The leaf|This leaf|The objections|Campanella argues|Campanella answers|The key move|This means|The passage shows)' \
  sources/latin/campanella-metaphysica/parts/part-iii-*.md
```

If matches appear inside `## English` sections, the tranche has summarization disguised as translation. The signals belong in `## Note`. A clean tranche should return zero hits inside `## English` blocks. (Hits inside `## Note` are fine.) A clean grep does not prove the Latin is complete or the English is faithful; it only removes one obvious warning sign.

## Failure Modes to Watch For

These are the patterns that produced the false-positive review in the part-iii-003-027 tranche. Treat each as a reason for *more* spot-checking, not less:

- **Format compliance hiding content failure** — file structure correct, content is summary
- **Quantitative success hiding qualitative failure** — many parts produced, each a digest
- **Architecture visibility hiding content emptiness** — filenames trace a clean argument structure, but the files don't carry the Latin
- **Clean Latin hiding incompleteness** — the Latin looks corrected and authoritative, but only selected sentences survived from the extract
- **English built from the extract rather than from the Latin section** — the translation summarizes things noticed while reading, but not actually transcribed in the part
- **"Goal completed" framing satisfying methodology rather than content** — agent hit phase gates without delivering substrate
- **Uniform per-file size as a signal of summarization** — when 25 files all land at 37-43 lines, suspect a target-length compression rather than per-leaf material driving the size
- **Quantitative briefs raising failure odds** — when the brief emphasized a quantity floor ("at least N parts"), be *more* suspicious of fidelity, not less. Quantity targets pressure summarization

## What to Do When a Tranche Fails Review

- Name the suspect file range explicitly (e.g., `part-iii-003` through `part-iii-027`)
- Add a Redo Flag entry to `sequential-run-standard.md` against the range
- Do not absorb substantive apparatus from failed parts. A journal entry naming the failure and redo scope is allowed and usually desirable; glossary, page-map, README, and crosswalk uptake from the failed contents should wait until redo
- Keep raw/normalized extracts. Those are still good — only the part files need rework
- Propose a redo brief that names the specific failures: Latin completeness gaps first, then per-file translation gaps, paraphrase signals, and condensed English

## Review Report Shape

A passing review must report:

- Specific filenames sampled
- Normalized extract paths checked
- Latin/English excerpts quoted from each sampled file (so the reader can verify the check happened)
- A brief statement on whether the part's Latin represented the normalized extract's body blocks completely, partially, or only selectively
- Grep results for paraphrase signals
- Verdict: clean / provisional / redo

If files were sampled and the report doesn't quote specific extract/Latin/English content from them, the review was structural and the verdict is not earned.

## Scope

This document applies to sequential page-order parts (`part-iii-NNN-*`, `001-*`, and any future numeric sequence). It does **not** apply to:

- `pilot-*` files (different shape; encounter-candidate work)
- `encounters/` files (citation-grade; have their own apparatus expectations)
- Reading notes in `reading/` (synthesis, not translation)

For those, see the corresponding methodology in `parts/README.md` and the parent `README.md`.
