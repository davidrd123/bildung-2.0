# Context Packages for `Erkenntnisproblem` Vol. 2

Purpose: define what to load at session start so a human or LLM begins from the right compression layer for the task at hand.

This file is not a replacement for direct reading of the parts. It is a session-start manifest.

## Core Rules

### 1. Use `kernel + overlay`, not bulk preload

- load the same small kernel for any Vol. 2 work
- then add a task-specific overlay
- do not load all Vol. 1 review files by default

### 2. Keep authority and retrieval distinct

Truth surfaces:

- `texts/erkenntnisproblem-vol2/parts/*.md`
- `texts/erkenntnisproblem-vol2/source/glossary.yaml`
- `texts/erkenntnisproblem-vol2/source/page-map.yaml`
- `texts/erkenntnisproblem-vol2/journal.md`

Retrieval surfaces:

- `texts/erkenntnisproblem-vol2/reading/close-reading-ledger.md`
- dated notes in `texts/erkenntnisproblem-vol2/reading/`
- Vol. 1 integration notes, only when the Vol. 2 question actually calls for them

Use retrieval surfaces to orient quickly; return to truth surfaces whenever a claim or pressure needs verification.

### 3. Prefer slices over full files

Priority order under pressure:

1. active Vol. 2 part
2. recent Vol. 2 journal entries touching that part
3. chapter-local ledger entries
4. active glossary slice
5. page-map anchors
6. bounded Vol. 1 carry-forward notes

### 4. Write exclusion rules explicitly

Do not load by default:

- all Vol. 1 parts
- the full Vol. 1 journal
- multiple large primary texts from other subprojects
- secondary sources before primary pressure has been named
- `interpretive-notes.md` from Vol. 1 as an authority surface

## Packages

### Package 1: Cold-Start Kernel

Use when any session touches `texts/erkenntnisproblem-vol2/`.

Load order:

1. `patterns/charter.md`
2. `00-Notes/process.md`
3. `00-Notes/right-now.md`
4. `texts/erkenntnisproblem-vol2/README.md`
5. recent `journal.md` tail relevant to the active chapter

Add `patterns/handle-schema.md` only when touching handles, threads, or anything that might widen ontology.

### Package 2: Translation Continuation

Load on top of Package 1:

1. `texts/erkenntnisproblem-vol2/source/glossary.yaml`
2. `texts/erkenntnisproblem-vol2/reading/close-reading-ledger.md`
3. last `3-5` journal entries touching the active stretch
4. previous `2-3` parts for continuity
5. `texts/erkenntnisproblem-vol2/source/page-map.yaml`

### Package 3: Vol. 1 Carry-Forward Check

Use only when a Vol. 2 passage creates a real cross-volume pressure.

Load:

1. `texts/erkenntnisproblem-vol1/reading/2026-04-08-earned-distillation-from-volume-i.md`
2. `texts/erkenntnisproblem-vol1/reading/2026-04-10-four-surprises-from-encountering-volume-i.md`
3. only the specific Vol. 1 part, ledger entry, or glossary slice needed for verification

Avoid using Vol. 1 to predict Vol. 2. Use it to test a pressure already encountered in Vol. 2.

For apparatus setup rather than interpretive carry-forward, use `texts/erkenntnisproblem-vol1/reading/2026-05-13-lessons-for-vol-2.md` as a hypothesis checklist and verify its claims against the named Vol. 1 artifacts.

### Package 4: Preflight / Apparatus Audit

Use when checking whether the setup is ready for forward translation.

Load:

1. `texts/erkenntnisproblem-vol2/reading/preflight-audit.md`
2. `texts/erkenntnisproblem-vol2/README.md`
3. `texts/erkenntnisproblem-vol2/source/page-map.yaml`
4. `texts/erkenntnisproblem-vol2/source/outline.yaml`
5. `texts/erkenntnisproblem-vol2/review-checklist.md`
6. `texts/erkenntnisproblem-vol1/reading/2026-05-13-lessons-for-vol-2.md`

Suggested output shape:

1. source status
2. alignment status
3. apparatus readiness
4. specific risks before first translation batch
5. go/no-go recommendation

### Package 5: Method Comparison / Apparatus Drift

Use only when the Vol. 2 working method itself is under review.

Start with the distilled Vol. 2 record:

1. `texts/erkenntnisproblem-vol2/reading/preflight-audit.md`
2. `texts/erkenntnisproblem-vol2/README.md`
3. `texts/erkenntnisproblem-vol2/review-checklist.md`

Then verify against primary method surfaces as needed:

1. `texts/zeitmauer/journal.md`
2. `texts/zeitmauer/source-bound-high-level-integration.md`
3. `texts/zeitmauer/second-pass-messbare-und-schicksalszeit.md`
4. `texts/zeitmauer/second-pass-urgrund-und-person.md`
5. `texts/zeitmauer/source/handles.yaml`

Do not load Zeitmauer by default for translation continuation. Its role here is
to help audit routing discipline, glossary evidence, second-pass memo use, and
the threshold for promoting a pressure into a thread.
