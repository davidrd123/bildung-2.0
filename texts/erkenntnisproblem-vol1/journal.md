# Translation Journal

## 2026-04-01 - Scaffold

Set up a dedicated `erkenntnisproblem-vol1` project rather than forcing Cassirer into the `escolios` or `zeitmauer` shape.

Reasons:

- the OCR is usable enough for page-range intake but not clean enough for blind translation
- the work is structured by prefaces, books, chapters, and sub-arguments rather than numbered units
- the conceptual vocabulary is broad and recursive enough to require a dedicated glossary from the start
- the up-front cost should go into page mapping and tooling, not hand-cleaning all 636 pages before the first translated tranche

Initial structure:

- reproducible page-range extractor
- conservative normalizer for line-wrap and page-noise cleanup
- outline and page-map files
- glossary for recurring epistemological terms
- calibration batch under `parts/`

## 2026-04-01 - Intake Method

Current bias:

- clean the container ahead of time, not the whole contents
- trust the PDF text layer only as a draft source, never as final authority
- preserve paragraph boundaries unless the PDF clearly indicates otherwise
- keep `Wissenschaft` and related terms under pressure rather than flattening them early into modern academic English

Decision for now:

- use a hybrid workflow
- do mechanical normalization ahead of time
- do semantic cleanup just in time against the PDF for the tranche being translated

## 2026-04-01 - Calibration Batch

The first batch should cover:

- the 1906 preface
- the retained 1910 preface headed `Zur zweiten Auflage`
- the opening of the introduction

Why this batch:

- the prefaces state the method explicitly
- the introduction immediately pressures the core lexicon: `Erkenntnis`, `Gegenstand`, `Begriff`, `Wissenschaft`, `Erfahrung`
- it is small enough to expose OCR failure modes without committing to a full-book cleanup pass

## 2026-04-01 - Scan Correction Notes

The title page identifies this copy as the twelfth revised edition, but the prefatory revision note it carries is still headed `Zur zweiten Auflage`.

Decision for now:

- describe the bound volume as the 1911 twelfth revised edition
- describe the retained revision preface by its actual heading

## 2026-04-01 - First Draft Tranche

Completed a first draft of:

- the 1906 preface
- the retained 1910 preface headed `Zur zweiten Auflage`
- the opening four printed pages of the introduction

What this tranche clarified:

- `pdftotext -raw` is the right default extractor for this scan
- the first preface page still requires manual correction against the page image
- `Wissenschaft` can remain provisionally `science` in these pages, though the broader pressure on the term remains open
- `Vorstellung` should stay near `representation`
- `Geist` cannot be globally fixed yet; this tranche pressures both `mind` and `spirit`

Decision for now:

- keep the generated normalized files as mechanical artifacts
- keep the corrected tranche text in the batch file itself until a clearer cleaned-source convention emerges
