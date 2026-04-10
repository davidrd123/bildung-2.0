# DeepResearch

This folder holds question sets, external-audit materials, and pressure tests for the repo.

It is not the primary workspace for ordinary translation sessions.

If a note has become an explicit bounded experiment run against earned material, it should usually live under `../experiments/` rather than here.

## Current Layout

- `2026-04-02/` — earlier DeepResearch runs and outputs. Left as-is.
- `2026-04-04/productive-generative.md` — the active, translation-phase prompt surface.
- `2026-04-04/exploratory-hard-questions.md` — bounded prompts for mining chats into real open questions and sending them to a harder model without treating the result as authority.
- `2026-04-04/peirce-gpt5pro-queue.md` — paste-ready GPT-5 Pro questions for the April 4 Peirce chat, ordered by priority.
- `2026-04-04/punishing/` — harder audit prompts for protocol pressure, overclaim checks, and method hardening.
- `2026-04-06/README.md` — post-processed intake surface for the April 6 source-role research set. Use this if the task is deciding whether an item is source-language commentary, continued primary work pressure, or thinker-on-thinker encounter.
- `2026-04-07/README.md` — router for the April 7 Warburg / Mythos review cluster. Start here for what survived, what stayed as prompt, and where the archived review surface now lives.

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

If the work is:

- route the April 6 bibliography set by source role
- choose between the `5Pro`, `Opus`, and raw `DR` variants
- prepare a later agent or feature pass to pick up the category-2 / category-4 distinction cleanly

start with `2026-04-06/README.md`.

If the work is:

- recover what actually survived from the April 7 Warburg / Mythos cluster
- decide whether the live object is the session-ledger test, the Mythos source note, or the weaker method-pressure note
- reconstruct the older multi-pass review surface only if needed

start with `2026-04-07/README.md`.

The default should be the productive surface, not the punishing one.
