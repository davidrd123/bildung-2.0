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

## 2026-04-01 - Second Introduction Tranche

Completed a second draft tranche of the introduction:

- printed pages `5-8`
- PDF pages `29-32`

What this tranche clarified:

- `Rechenmarken` should remain open in the glossary; `reckoning-marks` works better than `counters` for now, but should not be treated as settled
- the historical inquiry is now stated more sharply as complement and touchstone to the analysis of given science
- Cassirer explicitly limits psychological analysis: it can complete critique of knowledge, but not replace critical analysis of scientific principles

Decision for now:

- continue the introduction in similarly sized tranches until the opening methodological arc is complete
- keep long English sentences by default, but prefer semicolons or light restructuring where the argumentative relation would otherwise blur

## 2026-04-01 - Third Introduction Tranche

Completed a third draft tranche of the introduction:

- printed pages `9-12`
- PDF pages `33-36`

What this tranche clarified:

- the broken `Geist` clause does in fact push the local English toward `mind`: Cassirer rejects the model of `Geist` as a finished substance that merely appropriates a ready-made reality
- `Geisteswissenschaften` now needs its own glossary entry; `human sciences` is the current working rendering, but it remains open
- the introduction now states explicitly that philosophy and science must be read not in terms of external `influence`, but as coequal symptoms of one intellectual development
- exact science emerges here as the first domain in which the unity of the concept of knowledge receives effective vindication

Decision for now:

- continue until the introduction's opening methodological arc is complete, then harmonize `Parts 01-03` before moving into `Nikolaus Cusanus`

## 2026-04-01 - Fourth Introduction Tranche

Completed a fourth draft tranche of the introduction:

- printed pages `13-16`
- PDF pages `37-40`

What this tranche clarified:

- Kant appears here not simply as culmination but as a new beginning; the introduction explicitly turns from `completion` to `problem-generation`
- the transcendental method is defended not as a denial of history, but as the condition under which history becomes intelligible rather than chaotic
- the coupling of substantive analysis of present science with the historical tracing of its becoming is now stated directly as a reciprocal relation
- the concept of `Wissenschaftsgeschichte` already carries, for Cassirer, the thought of an enduring logical structure across changing concept-systems

Decision for now:

- continue the introduction beyond this point before harmonizing, since the argument is still unfolding continuously

## 2026-04-01 - Introduction Endpoint Correction

The running sequence shows that the earlier OCR-derived page map for the introduction was wrong.

Verified now:

- printed pages `17-18` correspond to PDF pages `41-42`
- PDF page `43` is the unnumbered divider `Erstes Buch / Die Renaissance des Erkenntnisproblems`
- PDF page `44` is blank
- `Nikolaus Cusanus` therefore opens immediately after the divider sequence

Decision for now:

- treat the introduction as ending on printed page `18`
- begin the next prose tranche with `Nikolaus Cusanus`
