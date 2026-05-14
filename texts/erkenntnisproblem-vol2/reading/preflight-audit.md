# Vol. 2 Preflight Audit

Date: 2026-05-13

## Source Assets

- PDF imported locally at `source/pdf/daserkenntnispro02cassuoft.pdf` and gitignored.
- JP2 page scans imported locally at `source/page-images/jp2/` and gitignored.
- PDF has 856 pages and an extractable text layer.
- JP2 folder has 860 files and skips `_0857.jp2`.
- PDF page 21 is the Book IV divider.
- PDF page 23 is printed page 3, opening `Erstes Kapitel. Bacon.`

The PDF text layer is good enough for first-pass extraction, but the German used in part files should still be corrected against the active PDF or JP2 pages.

## Vol. 1 Lessons To Carry Forward

Vol. 1 proved that the apparatus works when it remains source-bound and tranche-local. The useful unit is a paragraph cluster with corrected German, draft English, and short notes about what the passage clarified.

The 2026-05-13 Vol. 1 lessons note is useful, but it was evaluated as a hypothesis checklist rather than imported as authority. Its strongest claims are supported by the Vol. 1 artifact-integrity audit, journal second-pass note, context package, and reading-file inventory:

- apparatus mutation was earned in motion, not designed up front
- gloss-creep appeared under high-load forward translation and became visible only after a run had accumulated
- late glossary thinness was sometimes evidence that pressure was structural rather than lexical
- repeated reading-note templates can become their own misleading groove
- `journal.md` changed jobs across phases instead of remaining a single-purpose log

The main Vol. 1 failure mode was late-run quality drift: the English became smoother while some German blocks became less dense than the source warranted. Vol. 2 should start with the rule that main prose is preserved at full density in the active tranche, while footnotes and page spillover can be handled selectively and explicitly. The roughly ten-part audit cadence is justified by Vol. 1 because drift was delayed, not obvious tranche by tranche.

The glossary should remain lean and begins empty. This is not a wholesale adoption of the Vol. 1 lessons note; it follows from treating `source/glossary.yaml` as a truth surface. Candidate terms can be named as watchpoints here, but they should not become glossary entries until repeated Vol. 2 evidence clarifies their function.

The context system should stay layered:

- canonical source and translation files first
- close-reading ledger for local findings too important to lose
- journal for tranche-level decisions and cross-batch pressure
- structured chains or viewer/export data only when repeated work forces them

The updated Vol. 1 lessons note adds two setup refinements that this preflight accepts:

- the part-file opening paragraph is a high-value prose surface and should be retained in Vol. 2
- the Vol. 2 scope is author-given in Cassirer's 1906 preface: English empiricism, then idealism from Leibniz and natural science from Newton, converging in critical philosophy

The later user reflection adds a third refinement: first-pass translation should be allowed to leave hooks for re-entry at higher resolution. The failure in the late Vol. 1 run was not only that compression happened, but that compression and unresolved source-pressure were not always marked clearly enough while the work moved toward completion.

The first Bacon pass added a fourth refinement. The project should not optimize
for forward motion before it has earned correctness. Bacon's own restraint on
the understanding is the local methodological analogue: the agent must restrain
the impulse to move through pages until the part gate preserves evidence. In
practice, substantive Latin or French footnote quotations are part of the
evidence layer. They should be translated in the draft-footnote layer unless
they are purely bibliographic, or explicitly routed as deferred work with a
reason.

## Zeitmauer Lessons For Vol. 2

`texts/zeitmauer/` was reviewed as a method comparison, not as an apparatus to
copy wholesale. Its strongest lesson is that the journal can be a routing
surface, not only a clarification log. A batch entry can record where pressure
should go next: stay in the journal, add glossary evidence, generate a bounded
reading note, become a thread dossier, mark a visual candidate, or wait.

Adopt these habits lightly:

- name the tranche's structural center when a passage, contrast, or move is load-bearing
- make routing decisions explicit, including negative decisions such as "no glossary entry yet"
- treat `open` as evidence-backed rather than merely unresolved
- use second-pass memos only after a closed unit has accumulated pressure that needs resolution
- mark `[visual candidate]` only when a structure in the material earns it
- use `What to expect next` only at chapter, book, or part boundaries where the expectation can later be tested

The cross-project rule for Vol. 2 should be hybrid. Cassirer's own cross-domain
movement among empiricism, idealism, mathematical natural science, and critique
belongs in the journal because it is source-bound. External resonances with
other repo projects should enter the journal only as brief contact candidates.
If they become anchored and recurrent, create a `threads/` dossier; if they
remain speculative, keep them in `reading/` as nonbinding notes.

## Vol. 1 Findings That Matter For Vol. 2

The carry-forward thesis from Vol. 1 is not a list of figures but a problem shape: knowing moves from substantial or ontological pictures toward relation, rule, function, and exact science. Repeated failure occurs when method, condition, relation, or concept is treated as a thing, power, or content.

For Vol. 2, this means Bacon should be read as a test of whether empirical method can produce lawful cognition rather than merely collect observations. Gassendi and Hobbes should then be checked for how they bind sense, definition, calculation, and objectivity. The later empiricism and Newton-to-Kant arc should not be pre-read through Kant, but the path toward critical objectivity is the live question.

No further Vol. 1 repair is required before beginning Vol. 2. If a future audit wants a stricter complete Vol. 1 body, the known pockets to revisit are around part `144` and possibly `136`; that is not a blocker for Vol. 2.

## Setup Decisions

- Keep the PDF and JP2 scans local and ignored, because they are source assets, not repo text.
- Track source alignment in `source/page-map.yaml`, not in conversation memory.
- Use the Vol. 1 extraction-normalization workflow, adapted to Vol. 2 paths.
- Start with a deliberately small Bacon calibration batch before widening the run.
- Do not create chain files, viewer exports, or a large term ontology until actual Vol. 2 passages force them.
- Keep `source/glossary.yaml` empty until a term has repeated local evidence.
- Run a quality-zone check after roughly ten parts, because Vol. 1 gloss-creep was delayed rather than immediately obvious.
- Give future reading notes content-bearing names; do not recreate the Vol. 1 `earned-distillation-from-*` pattern by habit.
- Use re-entry hooks in part files to mark unresolved pressure without forcing premature resolution.
- Treat repeated hooks naming the same primary source or justification problem as the threshold for a bounded `reading/` note.
- Use the journal as a routing surface: structural center, routing decision, re-entry hooks, and decision for now are the minimum useful habits.
- Do not create `threads/`, handle layers, or second-pass memo layers until repeated local evidence earns them.
- Do not permit open-ended forward translation until multiple tranches pass the correctness gate: corrected German, substantive footnotes, draft English, opening finding, routing decision, and hooks.

## First Calibration Target

Initial tranche:

- PDF pages: `21-26`
- printed pages: divider, blank, `3-6`
- scan files: `_0021.jp2` through `_0026.jp2`
- source locus: Book IV divider and the opening of Bacon, section I, `Die Kritik des Verstandes`

What this tranche should test:

- whether PDF extraction keeps usable paragraph boundaries
- whether normalization handles running headers and page numbers without deleting real prose
- whether scan/PDF/printed-page alignment holds beyond the first opening pages
- how to render `Verstand`, `Erfahrung`, `Experiment`, `Natur`, `Begriff`, and `Methode` in the opening empiricism frame
- whether the part template can carry a post-translation finding paragraph and re-entry hooks without becoming a checklist

Candidate term watchpoints, not glossary entries:

- Bacon: `experientia`, `prerogativae instantiarum`, `Form`, `Interpretation der Natur`, `Idole`
- Hobbes: `ratiocinatio`, definition, reckoning, word/concept relation
- Spinoza and Leibniz: `attributum`, `vis viva`, `perceptio`, symbolic knowledge
- Later empiricism and Kant: objectivity, representation, self-consciousness, synthesis, thing in itself

## Calibration Result

Generated files:

- `source/raw/001-book-iv-bacon-opening-pdf-21-26.txt`
- `source/normalized/001-book-iv-bacon-opening-pdf-21-26.txt`

The raw extraction preserves the Book IV divider, blank page, and Bacon opening. The normalized extraction is usable as a starting point, but it must not be treated as corrected German. It contains predictable PDF text-layer defects, including joined words, damaged characters, and OCR noise in Latin footnotes.

Spot checks:

- JP2 `_0021` confirms the Book IV divider.
- JP2 `_0022` is blank.
- JP2 `_0023` opens Bacon on printed page `3`.
- JP2 `_0026` confirms the continuation on printed page `6`.

Normalization note:

- blank PDF page `22` is omitted from the normalized text because it has no content; `source/page-map.yaml` remains the authority for blank-page alignment.

## Go Criteria

Vol. 2 is ready to begin when:

- `source/outline.yaml`, `source/page-map.yaml`, and `source/glossary.yaml` parse cleanly
- a small raw extraction and normalized extraction exist for PDF pages `21-26`
- the normalized text is spot-checked against PDF page `23` and JP2 `_0023`
- the first part file uses the settled status/template shape from `parts/README.md`
