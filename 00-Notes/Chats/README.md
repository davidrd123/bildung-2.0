# Chats (Hot Layer) — Local Standards

This directory holds **chat exports** as a working register.

These files are not primary sources. They are not authority. They are a place where hypotheses, failure modes, and method pressure become visible at conversational speed.

If this README conflicts with higher-order repo docs, it loses. See:

- `patterns/charter.md`
- `00-Notes/process.md`

## Dates and filenames

- Folder dates (e.g. `2026-04-20/`) are **export dates** by default, not necessarily the date the conversation happened.
- Filenames are kept close to the exporter’s naming (for traceability).
- If a file is re-exported / continued, prefer keeping it in the later export folder and adding a short note in `sift-notes.md` describing the continuity.

## What belongs here

- Raw chat exports (`.md`) and Claude Code transcripts (`.jsonl` + cleaned `.md`).
- Minimal, disciplined re-entry surfaces that help future you *not reread the whole file* to know whether it’s worth rereading.

## What does *not* belong here

- Promotions into `patterns/` or into live subproject artifacts (`texts/**`) based on chat fluency alone.
- “Settled claims” about texts that were not actually encountered.

## Standard outputs for a day-folder

Not every folder will have all of these yet, but this is the target shape:

1. `sift-notes.md`
   Atelier complement: portable phrases, exemplar moments, cross-connections, “why this matters,” and explicit quarantine warnings.
   This is allowed to decay.

2. `extractions/*actual-questions*.md`
   Folder-level extraction: the actual question stack, what survives, what should evaporate, and the next bounded move (if any).
   This is the “cold layer” re-entry surface.

3. `extractions/*dossier*.md` (optional, but preferred for large/high-value files)
   Line-anchored barrier note: a navigable index into a long chat with concrete anchors, capturing exactly where key moves happen.
   Not method canon. Not source authority.

## Line anchors and integrity

- Prefer line anchors against the exported files (use `nl -ba` locally).
- Avoid editing exported chat files unless necessary (deduping repeated re-export content is the main exception).
- If you do edit an exported file, note it at the top of `sift-notes.md` for that folder so future line anchors aren’t silently invalidated.

## Provenance discipline (what to trust)

Chat content is treated as **untrusted by default** in these cases:

- “I cloned / read / searched / found” claims that aren’t corroborated by actual file contact or diffs.
- Web links and literature maps inside the chat (treat as pointers; re-run under explicit provenance before using).
- Voice-theatre (HERO/PROTEUS/HERMES) used as an evidence substitute.

Chat content is treated as **more trustworthy** when:

- It quotes a passage that you can verify against an on-disk source file.
- It performs a correction under pressure (e.g., a lexical or provenance slip corrected by direct text contact).
- It explicitly names a failure mode that is itself visible in the transcript (shape drift, ontology upgrades under citation, inherited-authority laundering, etc.).

## Promotion boundary

Chats are a register for:

- generating hypotheses
- catching failure modes
- staging guardrail tests

Promotion into anything that gets cited as authority requires:

- direct source contact (resistant text)
- evidence handles / line-anchors
- explicit “what remains open” and “what was not read”

If a chat produced something valuable, prefer:

- extracting the value as a bounded working note, or
- leaving it here with explicit quarantine language

Do not let “beautiful narrative shape” outrank the repo’s “slow encounter” work.

