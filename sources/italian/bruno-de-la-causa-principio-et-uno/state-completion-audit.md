# Completion Audit and Promotion State

Date: 2026-05-08

## Objective Restated

Produce a complete source-local Bruno translation campaign for
`sources/italian/bruno-de-la-causa-principio-et-uno`, using the local Italian
Liber Liber/Aquilecchia source as authority. The campaign must translate the
full work in bounded source-span batches, preserve the structure and conceptual
pressure of the source, maintain an Erkenntnisproblem-style journal and open
glossary, and finish with a clear note on promotion readiness.

## Prompt-to-Artifact Checklist

Source-local campaign exists:

- Evidence: `README.md`, `source/sections.yaml`, `source/full/`,
  `source/raw/`, `parts/`, `journal.md`, `glossary.yaml`.
- Status: complete.

Local Italian Liber Liber/Aquilecchia source used as authority:

- Evidence: `README.md`; `source/full/de-la-causa-principio-et-uno-liberliber.txt`;
  `parts/000-liberliber-metadata-and-toc.md`.
- Status: complete.

All `source/sections.yaml` sections have corresponding handled parts:

- `000` metadata and table of contents: `parts/000-liberliber-metadata-and-toc.md`
- `001` title and proemial epistle: `parts/001-title-and-proemial-epistle.md`
- `002` arguments: `parts/002-argomenti.md`
- `003` verse front matter: `parts/003-ai-principi-de-l-universo.md`
- `004` Dialogue One: `parts/004a-*`, `parts/004b-*`, `parts/004c-*`
- `005` Dialogue Two: `parts/005a-*`, `parts/005b-*`, `parts/005c-*`
- `006` Dialogue Three: `parts/006a-*`, `parts/006b-*`, `parts/006c-*`, `parts/006d-*`
- `007` Dialogue Four: `parts/007a-*`, `parts/007b-*`, `parts/007c-*`, `parts/007d-*`
- `008` Dialogue Five: `parts/008a-*`, `parts/008b-*`, `parts/008c-*`
- Status: complete. Gaps inside raw-line spans are blank separator lines.

Each batch includes source span, working English translation, and translation
pressure notes:

- Evidence: `rg "^Source span:" parts`, `rg "^## Working Translation$" parts`,
  and `rg "^## Translation Pressure$" parts` all return entries for the part
  files.
- Status: complete.

Front matter, arguments, poems, and dialogues are handled:

- Evidence: parts `001`, `002`, `003`, and `004` through `008`.
- Status: complete.

Journal maintained with major interpretive and term decisions:

- Evidence: `journal.md` includes scaffold, calibration, front matter, Dialogues
  1-5, metadata, source issues, Latin note, diagrams note, and next-state notes.
- Status: complete.

Glossary maintained as lean/open rather than prematurely stable:

- Evidence: `glossary.yaml` includes open entries for `causa`, `principio`,
  `uno`, `sustanza`, `materia`, `forma`, `anima`, `contemplazione`, `atto`,
  `potenza`, `ente`, `soggetto`, `intelletto_universale`, `anima_del_mondo`,
  `complicato`, `esplicato`, `contrazione`, `cusano`, and related terms.
- Status: complete.

Key terms not flattened:

- Evidence: glossary entries remain `open`; translations preserve repeated
  terms such as cause/principle/one, act/potency, matter/form, soul/life/spirit,
  complication/explication.
- Status: complete.

Verification:

- `git diff --check sources/italian/bruno-de-la-causa-principio-et-uno` passed
  with no output.
- `rg` checks confirm source-span, working-translation, and translation-pressure
  sections across the part files.
- Status: complete for mechanical checks.

## Remaining Risks

This is a complete source-local working translation campaign, not a finished
critical edition.

Known risks:

- The Latin verse in `003-ai-principi-de-l-universo.md` is provisional and needs
  a dedicated Latin check.
- The plain-text source has likely joined-word artifacts such as
  `efficiente,etè`, `partietescrementi`, and `Orcoetavaro`.
- The fifth dialogue refers to `Figura 1`, `Figura 2`, and `Figura 3`, but the
  local text does not include the actual diagrams.
- Name normalization is not settled: Mauvissiero/Mauvissiere, Michel di
  Castelnovo, Alessandro Dicsono Arelio, Polihimnio/Poliinnia.
- The translation has had one full drafting pass, not a second proofread against
  another witness or page images.

## Promotion State

Ready to promote as a draft source-local translation base: yes.

Ready to promote as a polished canonical `texts/` project without further work:
no.

Recommended next step before canonical promotion: run a second pass against the
Italian source, check the Latin, recover or reconstruct the three figures, and
decide editorial policy for names and source artifacts. After that, this can
become a full `texts/` project with batch files, journal, glossary, and eventual
handle work.

