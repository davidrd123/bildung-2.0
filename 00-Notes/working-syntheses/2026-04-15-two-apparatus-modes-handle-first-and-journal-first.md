# 2026-04-15 — Two apparatus modes: handle-first and journal-first

**Status:** Working synthesis, not a final architectural statement. This note names a difference already visible in the repo's strongest proving grounds.

**Purpose:** explain why `Zeitmauer` and `Erkenntnisproblem` currently generate different secondary apparatus shapes, and why that should not be mistaken for inconsistency.

**Inputs:**

- `texts/zeitmauer/README.md`
- `texts/zeitmauer/source/glossary.yaml`
- `texts/zeitmauer/source/handles.yaml`
- `texts/erkenntnisproblem-vol1/README.md`
- `texts/erkenntnisproblem-vol1/reading/close-reading-ledger.md`
- `00-Notes/process.md`

## Core distinction

The repo currently has two strong apparatus modes:

- **handle-first**
- **journal/ledger-first**

Both are real. Both are already on disk. Neither should be treated as the one true format for all projects.

## 1. `Zeitmauer` as handle-first

`Zeitmauer` is the strongest handle-first pilot.

Its README already emphasizes:

- numbered section units
- glossary-driven term tracking
- thread dossiers
- a viewer backed by exported index data  
  [texts/zeitmauer/README.md](/Users/daviddickinson/Projects/Lora/bildung-2.0/texts/zeitmauer/README.md:22)

In practice, this means:

- sections are stable navigational units
- evidence chains are serialized directly into glossary entries
- threads are explicit dossiers
- handles can already serve as a real retrieval and traversal surface

The result is a project where the relational layer is not just derived navigation. It is already part of the active reading instrument.

## 2. `Erkenntnisproblem` as journal/ledger-first

`Erkenntnisproblem` is the strongest journal/ledger-first pilot.

Its README emphasizes:

- paragraph-cluster units
- glossary pressure
- a close-reading ledger
- a journal
- interpretive notes kept separate from source-bound notes  
  [texts/erkenntnisproblem-vol1/README.md](/Users/daviddickinson/Projects/Lora/bildung-2.0/texts/erkenntnisproblem-vol1/README.md:22)

In practice, this means:

- the key unit is often a paragraph-scale finding, not a stable numbered section
- reasoning gets preserved in prose trace before it is serialized into handle grammar
- the ledger's `Current downstream use` field makes later reuse visible inside the same trace surface  
  [texts/erkenntnisproblem-vol1/reading/close-reading-ledger.md](/Users/daviddickinson/Projects/Lora/bildung-2.0/texts/erkenntnisproblem-vol1/reading/close-reading-ledger.md:23)

The result is a project where prose trace remains the main secondary instrument.

## 3. Why the difference is legitimate

`process.md` already gives the underlying rationale:

- different projects have different textual grain
- the standard should be discoverability, not uniformity  
  [00-Notes/process.md](/Users/daviddickinson/Projects/Lora/bildung-2.0/00-Notes/process.md:170)

That means:

- Jünger's numbered prose and recurring term structure reward handle-first serialization
- Cassirer's long architectonic argument rewards slower prose trace and downstream-use logging

So the difference is not drift.

It is local fit.

## 4. What each mode is good at

**Handle-first** is strongest when:

- the source has stable local anchors
- recurrence and cross-linking matter early
- evidence chains can be serialized without losing too much pressure
- traversal is already part of the reading task

**Journal/ledger-first** is strongest when:

- the source pressure lives at sentence or paragraph scale
- the reasoning path matters as much as the local term
- serialization too early would lose argumentative shape
- later reuse needs to be tracked in prose before it hardens

## 5. What this does not mean

- not that every project must choose one mode permanently
- not that the repo has two incompatible architectures
- not that `Erkenntnisproblem` is anti-handle or `Zeitmauer` is anti-prose
- not that a later convergence is impossible

It means only that the repo is already allowing apparatus to be shaped by the text rather than by a demand for format symmetry.

## Working judgment

This distinction is already one of the repo's real design choices, even though it has mostly been living as practice rather than as named rationale.

The next honest move is not to unify the two modes.

The next honest move is to keep making the difference legible enough that future work can choose deliberately rather than by accident.

## Use rule

Use this note when the repo starts sounding inconsistent because one subproject has richer handles and another has richer prose trace.

Do not use it as a mandate that every new project must be classified in advance. Its job is only to explain the two strongest current modes already on disk.
