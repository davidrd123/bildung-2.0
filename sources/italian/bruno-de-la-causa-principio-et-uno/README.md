# Bruno - De la causa, principio et uno - Source-Local Scaffold

This is a source-local scaffold for Giordano Bruno's *De la causa, principio et
uno*. It is for calibration, translation, and encounter notes before deciding
whether to promote the work into a fuller campaign.

This is not yet a `texts/` project, not a critical edition, and not a
diplomatic transcription of the 1584 print. The authority copy here is the
local Liber Liber e-text, based on Giovanni Aquilecchia's 1973 Einaudi edition.

## Source

- Incoming source: `sources/italian/INCOMING/De la causa, principio et uno - Giordano Bruno.txt`
- Local authority copy: `source/full/de-la-causa-principio-et-uno-liberliber.txt`
- Edition basis named by the e-text: Giovanni Aquilecchia, Einaudi, 1973
- Liber Liber reliability index: `1`
- Original-language status: Italian source text, with Latin title and early
  modern Italian forms retained

The original incoming file remains the outer source witness. The `source/full/`
copy is included so this scaffold can be worked locally without mutating the
incoming drop.

## Structure

- `source/full/` keeps the complete e-text.
- `source/raw/` contains a first line-normalized split by natural textual units.
- `source/sections.yaml` records the split boundaries and source line spans.
- `parts/` holds bounded translation and commentary batches.
- `encounters/` is reserved for reflective encounter notes if a batch earns one.
- `journal.md` records calibration decisions and cross-batch patterns.
- `glossary.yaml` tracks terms under pressure without prematurely settling them.

## Split Logic

The first split follows the text's own front matter and dialogue structure:

1. Liber Liber metadata and table of contents
2. Title page and proemial epistle
3. Arguments of the five dialogues
4. `Ai principi de l'universo`
5. Dialogues one through five

The split files are line-normalized working files. They do not preserve every
blank separator line from the full source, and they should not be treated as a
page-critical witness.

## Current Calibration

The first calibration batch is:

- `parts/001-proemial-epistle-opening-calibration.md`

Its purpose is to test the translation register, identify terms under pressure,
and decide whether Bruno should be pursued with an Erkenntnisproblem-style
journal discipline rather than a thin source cleanup workflow.

## Current Limits

- No page images or 1584 print witness have been checked.
- No handles, dossiers, or stable glossary entries have been promoted.
- The current terminology is deliberately open, especially `causa`,
  `principio`, and `uno`.
- Historical name normalization has not been settled.

