# Das Erkenntnisproblem II - Translation Project

Ernst Cassirer, *Das Erkenntnisproblem in der Philosophie und Wissenschaft der neueren Zeit*, vol. 2, third edition, Berlin 1922.

## Scope

This project tracks a working English translation and source-facing apparatus for volume 2 of Cassirer's *Erkenntnisproblem*.

- Local source PDF: `source/pdf/daserkenntnispro02cassuoft.pdf` (gitignored)
- Local JP2 scans: `source/page-images/jp2/` (gitignored)
- Translation scope: volume 2 main text, from Book IV through Book VIII, ending before the name and subject index unless later work needs index consultation
- Author-given scope from Cassirer's 1906 preface: English empiricism, then idealism from Leibniz and natural science from Newton, converging in critical philosophy

## Vol. 1 Carry-Forward

The volume 1 workflow remains the model, but not every artifact should be copied prematurely.

Carry forward:

- paragraph-cluster units rather than aphorism-style sections
- raw extraction, conservative normalization, and active-tranche PDF correction
- source-bound journal entries with `What this tranche clarified` and `Decision for now`
- journal entries that name the tranche's structural center and routing decision
- post-translation opening paragraphs that name what the tranche actually showed
- explicit re-entry hooks when a first pass exposes unresolved source pressure
- a close-reading ledger for sentence- and paragraph-scale findings
- glossary entries only for terms under repeated structural pressure; the file starts empty
- periodic quality audits before a long forward run silently changes standards

Do not carry forward:

- mature Vol. 1 term confidence as if it were already proven in Vol. 2
- structured chain files before a chapter actually forces them
- cross-project analogies before local Vol. 2 pressure has been named
- a viewer/export layer before the first few parts settle the part format

## Structure

```text
source/
  outline.yaml          # high-level map from the table of contents
  page-map.yaml         # trusted PDF/printed-page/scan anchors
  glossary.yaml         # locally earned Vol. 2 terms; intentionally empty at preflight
  raw/                  # page-range extracts from the PDF text layer
  normalized/           # lightly normalized working text, still to be verified
  pdf/                  # local source PDF, ignored
  page-images/jp2/      # local page scans, ignored
reading/
  close-reading-ledger.md
  context-packages.md
  preflight-audit.md
parts/
  README.md
journal.md
review-checklist.md
session-ledger.yaml
scripts/
  extract_page_range.py
  normalize_pages.py
```

## Working Method

1. Extract a small PDF page range into `source/raw/`.
2. Normalize conservatively into `source/normalized/`.
3. Correct the German against the PDF or JP2 scan for the active tranche only.
4. Translate in small batches.
5. Write the part's opening finding paragraph after the translation pass.
6. Leave re-entry hooks for unresolved pressure instead of silently compressing it away.
7. Record unstable recurring terms in `source/glossary.yaml` only after repeated local pressure earns an entry.
8. Record local source findings in `reading/close-reading-ledger.md` when they are too important to lose but too local for the journal.
9. Record source-bound drift, decisions, and review findings in `journal.md`.

Correctness comes before speed. Do not start an open-ended forward run until
the part form has shown that it can preserve source evidence under review:
corrected German, substantive quoted footnotes, draft English, opening finding,
routing decision, and re-entry hooks all need to be present. Only after several
consecutive tranches pass that gate without substantive correction should a
future agent treat "continue forward" as a safe standing goal.

Additional reviewers or sub-agents can help catch structural omissions and
pressure points, but they do not satisfy the correctness gate by themselves.
Source-level details still need direct verification against the German, Latin,
French, PDF, or scan. A positive outside review is useful evidence, not final
authority.

For journal entries, use Zeitmauer as a method source rather than a template.
The useful habit is routing: name what the tranche clarified, name the
structural center if one passage or move carries the load, say where the
pressure belongs next, and leave re-entry hooks when the first pass exposed
something unresolved. Use `What to expect next` only at chapter, book, or other
real boundaries where a forward-looking expectation can later be tested.

Cross-project material should follow a hybrid rule. Cassirer-internal
cross-domain movement belongs in the journal because it is part of Vol. 2's
argument. External project resonances should enter only as contact candidates;
promote them to a `threads/` dossier if they become anchored and recurrent, or
keep them in `reading/` as nonbinding notes if they remain speculative.

The starting calibration is deliberately small: the Book IV divider and the opening Bacon pages. This should settle page alignment, extraction quality, part format, and the first layer of Vol. 2 vocabulary before the run widens.

## Current Source State

- PDF has 856 pages and an extractable text layer.
- JP2 import has 860 files; the sequence skips `_0857.jp2`.
- PDF page `21` is the Book IV divider.
- PDF page `23` is printed page `3`, the opening of Bacon.
- `source/glossary.yaml` is intentionally empty until Vol. 2 passages earn entries.

Because PDF and JP2 counts differ, always use `source/page-map.yaml` for scan/PDF/printed-page alignment instead of assuming one fixed offset.
