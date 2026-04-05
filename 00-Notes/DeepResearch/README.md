# DeepResearch

This folder holds question sets, external-audit materials, and pressure tests for the repo.

It is not the primary workspace for ordinary translation sessions.

## Current Layout

- `2026-04-02/` — earlier DeepResearch runs and outputs. Left as-is.
- `2026-04-04/productive-generative.md` — the active, translation-phase prompt surface.
- `2026-04-04/exploratory-hard-questions.md` — bounded prompts for mining chats into real open questions and sending them to a harder model without treating the result as authority.
- `2026-04-04/peirce-gpt5pro-queue.md` — paste-ready GPT-5 Pro questions for the April 4 Peirce chat, ordered by priority.
- `2026-04-04/punishing/` — harder audit prompts for protocol pressure, overclaim checks, and method hardening.

## Use

If the work is:

- translate the next batch
- settle glossary pressure
- extract journal-worthy observations
- choose the next source-bound move

start with `2026-04-04/productive-generative.md`.

If the work is:

- mine a chat for the real open questions inside it
- send one of those questions to a stronger model for harder thought
- keep exploratory inquiry alive without letting it harden into method or architecture

use `2026-04-04/exploratory-hard-questions.md`.

If the work is specifically:

- run the April 4 Peirce chat through GPT-5 Pro
- use a ranked queue instead of reconstructing prompts each time

use `2026-04-04/peirce-gpt5pro-queue.md`.

If the work is:

- test whether a protocol is overbuilt
- stress a frame or genealogy
- audit model-loop fluency
- pressure the project's purpose claims

use `2026-04-04/punishing/`.

The default should be the productive surface, not the punishing one.
