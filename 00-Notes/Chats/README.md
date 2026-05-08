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

Not every folder will have all of these, and some folders may have none. A chat that is purely exploratory — no source contact, no methodological payload — may legitimately earn no artifacts. When outputs are produced, this is the target shape:

1. `sift-notes.md`
   Atelier complement: portable phrases, exemplar moments, cross-connections, “why this matters,” and explicit quarantine warnings.
   Two-valenced: allowed to decay if not returned to, and also available for unpacking when a later encounter pulls on a specific entry (see *Unpacking generative material* below).

2. `extractions/*actual-questions*.md`
   Folder-level extraction: the actual question stack, what survives, what should evaporate, and the next bounded move (if any).
   This is the “cold layer” re-entry surface.

3. `extractions/*dossier*.md` (optional, but preferred for large/high-value files)
   Line-anchored barrier note: a navigable index into a long chat with concrete anchors, capturing exactly where key moves happen.
   Not method canon. Not source authority.

## Current model assignment

The three outputs have different model temperaments attached in current practice:

- `extractions/*actual-questions*.md` and `extractions/*dossier*.md` — GPT-5.2 / Codex-temperament. Detail-patient, literalist, refuses to smooth gaps. Suited to line-anchoring and strict promotion-audit.
- `sift-notes.md` — Claude-Opus-temperament. Synthesis-drive, cross-weave, textural. Suited to noticing exemplar patterns, portable phrases, and corpus-weave across days.

This is current practice, not a permanent rule. What matters is the role each artifact plays; the model assignment is the current tuning of role-to-temperament. Running the same model on both passes risks pass-2 becoming a gloss on pass-1 rather than an independent reading.

## Unpacking generative material

`sift-notes.md` is a staging register for generative material — vocabulary emergence, portable phrases, candidate atelier entries, exemplar patterns. Material in it has two forward paths:

- **Decay.** Entries not returned to fade. Sift-notes is not an archive.
- **Graduation.** When later pressure (a new encounter, a recurring question, source-contact in a campaign) pulls on a sift-notes entry, it may migrate to a more specific shape:
    - `00-Notes/atelier/curio.md` — conceptual distinctions, phrases that do work in conversation without earning promotion.
    - `00-Notes/atelier/sparks/` — single-image compressions.
    - `00-Notes/atelier/pairings/` — two-thinker or two-text staging.
    - `00-Notes/atelier/ghost-books/` — unwritten-book intuitions.
    - `00-Notes/working-syntheses/` — dated working material that wants cross-source tracking.

Graduation is pressure-driven, not scheduled. Most sift-notes entries won't migrate, and that is correct.

(`00-Notes/atelier/encounters/` is currently at seed status per its own README and is not a stable destination for sift-notes material. Route to the canonical buckets only.)

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

## Shape check

If a folder's `sift-notes.md` is materially shorter than its `extractions/*dossier*.md`, either the chat was thin (sift correctly has less to say) or pass-2 hasn't actually been run and the sift is a restatement of the dossier. Distinguish by checking whether the sift contains portable phrases, exemplar patterns, or cross-connections that the dossier doesn't.

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

## Against grooving

The three-artifact target shape is descriptive, not a template to follow. Each chat's material should shape the specific form of its `sift-notes.md` — section headings, emphasis, what gets preserved as portable vs. what gets merely indexed. If two consecutive days' sift-notes share identical scaffolding (same headers, same emphasis pattern), the form has started grooving and something needs to change — either the shape of the sift, or the sift should not be written at all for that day.

This README is subject to the same discipline. If future sessions find it prescribing form rather than describing role, the README should be revised rather than defended.

