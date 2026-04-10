# bildung-2.0

A reconstruction project for whole knowing. Recovering buried texts, reconnecting severed lineages of thought, and building a practice of translation, decryption, commentary, and cross-domain synthesis that forms the reader rather than merely informs them.

## What this is

Six translation and decryption subprojects, two completed source campaigns, a growing shelf of modern concept encounters, and a cross-project synthesis layer — all governed by one method: slow encounter with opaque sources, deferred structure, and the principle that the texts teach the method.

The post-war Anglosphere inherited institutional power while losing contact with deeper traditions that shaped the question of what a human being is for. Important texts were buried, mistranslated, undertranslated, or rendered inaccessible. This project recovers them through disciplined re-articulation — not just foreign-language translation, but any work that makes an opaque source legible without flattening it.

## Subprojects

| Project | Author | Language | Status |
|---------|--------|----------|--------|
| **Erkenntnisproblem Vol. I** | Ernst Cassirer | German → English | **Complete.** 149 parts, full review apparatus. First English working translation of this volume. |
| **An der Zeitmauer** | Ernst Jünger | German → English | **Complete.** 59 parts through §186. First English working translation. Handle/evidence pilot, 5 thread dossiers. |
| **Tektologiya Vol. 1** | Alexander Bogdanov | Russian → English | 27 parts. First pass through main text complete. Demand-led. |
| **Escolios I** | Nicolás Gómez Dávila | Spanish → English | 17 section files. Selective second-pass mode. |
| **Escolios II** | Nicolás Gómez Dávila | Spanish → English | 56 section files. Active batching. |
| **Exegesis** | Philip K. Dick | English → English | 75 passes, 10 thread dossiers. Same-language decryption of a recursive archive. |

"Translation" here is broader than foreign-language transfer. The Exegesis is English throughout, but its recursive, spiraling structure is as opaque as any cross-linguistic barrier. The governing problem is opacity, not foreignness.

## Source campaigns

| Campaign | Source | Status |
|----------|--------|--------|
| **Uexküll** | *Theoretische Biologie* (1928) | Complete. 5 encounters + glossary. Bounded source campaign under `sources/german/`. |
| **Anders** | *Die Antiquiertheit des Menschen* Band I | Complete. Under `sources/german/`. |
| **Modern concepts** | Rosen, von Foerster, McCulloch, Montévil/Mossio, Eilenberg-MacLane, Freedman | 6 encounters under `sources/modern/`. Demand-led. |

## How it works

### Two layers

| Layer | Location | Character |
|-------|----------|-----------|
| **Living** | `00-Notes/` | Exploratory, freely revised, overlapping. Chats, distillations, experiments, cross-project synthesis. |
| **Crystallized** | `patterns/` | Stable, referenceable, canonical. Charter and handle schema. Deliberately thin. |

The living layer feeds the crystallized layer. The crystallized layer constrains the living layer. Neither replaces the other. Promotion from living to crystallized requires that the material survive contestation, reuse, and contact with the source — not just that it sounds good.

### Translation apparatus

Each subproject carries its own:
- **Parts** — translated tranches with German/Spanish/Russian source and English draft
- **Journal** — tranche-by-tranche findings and decisions ("what this clarified / decision for now")
- **Glossary** — terms under pressure, with `open`, `tentative`, and `stable` statuses
- **Handles and evidence chains** — machine-readable pointers connecting terms, passages, and threads (piloted in Zeitmauer)

### Cross-project synthesis

- **Threads** — named intellectual connections tracked across subprojects (Goethe/Leibniz split, cybernetics braided river, predecided world, action-conditioned real, and others)
- **Thread dossiers** — standalone notes with evidence paths, rival readings, and weakening evidence
- **Experiments** — bounded cross-text collision tests with explicit success/failure conditions and independent verification runs

### Methodological guardrails

- **Evidence before framework** — do not propose abstractions the textual evidence has not earned
- **Deferred structure** — terms with `status: open` are methodological discipline, not unfinished business
- **The Schuon limit** — expansion without absorption is not progress
- **Watch the Goethe/Leibniz balance** — the default LLM instinct is Leibnizian (clean taxonomy, explicit schema). This project needs both halves: patient accumulation and morphological intuition alongside formal structure
- **Do not reference what you have not encountered** — if a concept appears in synthesis prose without having been through primary encounter, it is floating on secondhand knowledge

Full guardrails in [`CLAUDE.md`](CLAUDE.md). Project charter in [`patterns/charter.md`](patterns/charter.md).

## Repository structure

```
bildung-2.0/
├── 00-Notes/              # Living intellectual workspace
│   ├── right-now.md       # Standing snapshot: what is proven, current, next
│   ├── process.md         # Workflow, authority order, ingestion
│   ├── Chats/             # Exported conversations
│   ├── distillations/     # Filtered notes from chats and research
│   ├── DeepResearch/      # Question sets, audits, and external pressure tests
│   ├── experiments/       # Cross-text collision experiments with results
│   ├── cross-project/     # Workspace-level synthesis notes
│   └── threads/           # Thread dossiers
├── patterns/              # Crystallized architectural decisions
│   ├── charter.md         # Purpose, scope, method, limits
│   └── handle-schema.md   # Handle grammar and relation vocabulary
├── texts/                 # Translation and decryption subprojects
│   ├── erkenntnisproblem-vol1/
│   ├── zeitmauer/
│   ├── tektologiya-vol1/
│   ├── escolios/
│   ├── escolios-ii/
│   └── exegesis/
├── sources/               # Source-language encounters and campaigns
│   ├── german/            # Uexküll, Anders
│   ├── french/            # La Rochefoucauld, Valéry
│   ├── modern/            # Modern concept encounters (Rosen, von Foerster, etc.)
│   └── ...
├── sessions/              # Session logs
├── tools/                 # Scripts and utilities
├── CLAUDE.md              # Agent guardrails
└── AGENTS.md              # Agent conventions
```

## Current state

As of April 2026:

- Two major German translation volumes complete (Erkenntnisproblem, Zeitmauer)
- Active forward work in Escolios II
- Six cross-project experiments completed with independent verification
- A retrieval layer (qmd) tested at BM25 level with authority-separated collections
- Secondary source encounters beginning (Cassirer Festschrift 1936, Hamburg 1956)
- The project's primary-work center is shifting from translation toward cross-project synthesis, deployment of earned material on modern questions, and selective secondary encounter

See [`00-Notes/right-now.md`](00-Notes/right-now.md) for the current standing state.

## Built with

This project is a human-LLM collaboration. Translation, commentary, cross-project synthesis, experiment design, and architectural decisions are produced through extended working sessions between a human reader and frontier language models (primarily Claude). The guardrails in `CLAUDE.md` exist because the collaboration's default failure mode is expansion without absorption — the same failure mode the project studies in the texts themselves.

## Working motto

Recover what was buried. Reconnect what was severed. Build forms that can change the reader.
