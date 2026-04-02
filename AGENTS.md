# Repo Agent Notes

This file is a thin operator sheet for agents working in `bildung-2.0`.

It is not the charter. It is not the process doc. Read those first and treat
them as the real source of purpose and workflow.

## Start Here

Read these in order before doing substantial work:

1. `patterns/charter.md`
2. `00-Notes/process.md`
3. `patterns/handle-schema.md`
4. `00-Notes/right-now.md`

Then read the local files for the subproject you are actually touching.

## Authority Order

When layers disagree, use this precedence:

1. `patterns/charter.md`
2. `patterns/handle-schema.md`
3. Canonical subproject files:
   - `texts/*/source/*.yaml`
   - translation/commentary files in `texts/*/parts/`
   - `texts/*/journal.md`
   - `texts/*/threads/*.md`
4. Derived indexes such as `texts/*/source/handles.yaml` and `ui-index.json`
5. Living notes in `00-Notes/`

Derived structure must resolve back to canonical files.

## What This Repo Is For

`bildung-2.0` is a reconstruction project for whole knowing.

Your job is not to optimize the system in the abstract. Your job is to help the
repo recover, translate, decrypt, comment on, and synthesize difficult source
material without flattening it.

## Operating Rules

- Text files remain the authority. Handles, viewers, and exported indexes are
  instruments built on top of them.
- Translation and commentary come before infrastructure unless the current text
  work clearly forces an architectural change.
- Keep the glossary lean. `open` and `tentative` are methodological states, not
  failures to finish.
- Do not prematurely settle major terms because the English looks neat.
- Do not let the viewer, handle system, or architecture become the project.
- The texts teach the method. Record patterns discovered through the material;
  do not invent frameworks ahead of the evidence.

## Review Discipline

When reviewing or continuing work:

- If you notice a cross-batch pattern, write it into the relevant journal.
- If a review surfaces a possible diagram, map, or illustration, mark it with
  `[visual candidate]` in the journal.
- If a term gains real pressure across sections, add evidence before you add
  confidence.
- If a thread becomes structurally real, give it a handle and a dossier rather
  than leaving it only in conversation context.

If you noticed it and it matters beyond the current batch, write it down.

## Update Discipline

After meaningful work, update only what the material actually earned:

- translation batch file
- relevant `journal.md`
- relevant `glossary.yaml`
- relevant `threads/*.md`
- `handles.yaml` only when a new anchor, note, evidence item, or relation is
  justified

If you change exported or derived data:

1. run the export script
2. verify sequentially, not in parallel with the export
3. confirm alignment and the specific new handles or relations you added

For `texts/zeitmauer/`, that usually means:

- `python3 texts/zeitmauer/scripts/export_ui_index.py`
- validate YAML / JSON shape after export

## Current Working Bias

The repo's most structurally advanced proving ground is `texts/zeitmauer/`.
Default to keeping architecture in service of that live translation work, not
the other way around.

## Do Not Do By Default

- Do not widen ontology because it feels elegant.
- Do not create new object types unless repeated material pressure forces them.
- Do not promote terms to stable on agent fluency alone.
- Do not treat living notes in `00-Notes/` as settled architecture.
- Do not erase ambiguity that the source is still using productively.

## If You Need More Context

Read the local subproject docs and journals next, not more meta-docs by
default. The shortest path back into useful work is usually:

- the latest batch file
- the local journal
- the local glossary
- the active thread dossiers
