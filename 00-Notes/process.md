# Process

How material flows through `bildung-2.0`: from conversation to synthesis to crystallized architecture.

## Standing State

`right-now.md` is the standing snapshot for cold starts: what is proven, what is current, what is next, and what decision is live.

`process.md` is not the standing snapshot. It describes workflow, authority, and upkeep.

## Two Layers

| Layer | Location | Character | Changes when... |
|-------|----------|-----------|-----------------|
| **Living** | `00-Notes/` | Exploratory, overlapping, freely revised | A new conversation produces new threads or revises existing ones |
| **Crystallized** | `patterns/` | Stable, referenceable, canonical | The intellectual work forces a structural revision |

The living layer feeds the crystallized layer. The crystallized layer constrains and organizes the living layer. Neither replaces the other.

## Authority

When different layers disagree, use this precedence:

1. `patterns/charter.md` — purpose, scope, and layer split
2. `patterns/handle-schema.md` — handle grammar, relation vocabulary, shared maturity language
3. Subproject canonical files — `texts/*/source/*.yaml`, translation/commentary files, journals, and thread dossiers
4. Derived indexes such as `texts/*/source/handles.yaml` — navigational structure that must resolve back to canonical files
5. Living synthesis notes in `00-Notes/` — exploratory unless crystallized elsewhere

If a living note proposes something that the canonical layer does not yet support, treat it as a proposal, not as settled architecture.

## Ingestion

### 1. Chat export

Conversations that do real conceptual work get exported to `00-Notes/Chats/`. Naming convention: `YYYY-MM-DD_HH-MM-SS_<platform>_<short-title>.md`.

Not every conversation is worth exporting. The test: did it produce a new thread, revise an existing one, or force an architectural change?

### 2. Distillation

Read the chat and extract into synthesis notes. What to look for:

- **New threads** — a figure, concept, or connection not yet tracked
- **Thread advances** — an existing thread that moved: got sharper, connected to something new, or got challenged
- **Architectural implications** — something that changes what the repo needs structurally (a new object type, a new relation, a lifecycle change)
- **Corrections** — something a prior note got wrong or overstated
- **Subproject triggers** — a reference, term, or passage that should feed into escolios, zeitmauer, exegesis, or sources

Distillation targets (not all needed every time):

| Target | File(s) |
|--------|---------|
| Intellectual genealogy | `cross-domain-synthesis-threads.md` |
| Project purpose / telos | `higher-purpose-distillation.md` |
| Vault intersection | `symbiotic-vault-intersection.md` |
| Genealogy → architecture | `genealogy-to-instrument.md` |
| New standalone thread | New file in `00-Notes/` |

### 3. Crystallization

When a synthesis note converges on something stable enough to reference without re-reading the exploration, extract it into `patterns/`:

- A relation type that keeps recurring → `patterns/relations.md`
- An object lifecycle that's settled → `patterns/objects.md`
- A convention for agent work → `patterns/agent-conventions.md`
- A frame definition → `patterns/frames/`

The test for crystallization: would a future session need to re-derive this from scratch, or can it just read the pattern?

## Threads in Flight

Living list. Updated as threads advance or stall.

### Intellectual Threads

| Thread | Status | Home | Last active |
|--------|--------|------|-------------|
| Goethe/Leibniz split | Active — central diagnostic | `cross-domain-synthesis-threads.md` | 2026-03-31 |
| Cybernetics braided river | Active — genealogy mapped, tributaries identified | `cross-domain-synthesis-threads.md` | 2026-03-29 |
| The Cassirer node | Active — connects all three texts | `cross-domain-synthesis-threads.md` | 2026-03-29 |
| Barrett constructed categories | Active — epistemological ground for the translation / decryption method | `cross-domain-synthesis-threads.md` | 2026-03-30 |
| Schuon limit | Placed — names the honest boundary of textual recovery | `cross-domain-synthesis-threads.md` | 2026-03-31 |
| Rosen: models vs. simulations | Placed — maps onto close/free split | `cross-domain-synthesis-threads.md` | 2026-03-29 |
| Practice queue (source encounter + decryption) | Active — revised around practical coupling to live work and generalized opacity | `cross-domain-synthesis-threads.md` | 2026-04-01 |
| Anders bridge | Active — source campaign complete; bridge clarified | `cross-domain-synthesis-threads.md` | 2026-04-02 |
| Predecided world | Active — Uexküll/Cassirer/Anders/Jünger world-cut connector | `cross-domain-synthesis-threads.md` | 2026-04-02 |
| Empirical morphogenesis line | Active — Levin corpus linked to the braided river | `cross-domain-synthesis-threads.md` | 2026-04-01 |
| Action-conditioned real | Active — von Foerster + late Zeitmauer + Cassirer + Dick | `cross-domain-synthesis-threads.md` | 2026-04-02 |
| Whitehead decryption | Seeded — identified as target, not started | `cross-domain-synthesis-threads.md` | 2026-03-29 |
| Symbiotic-Vault convergence | Active — structural isomorphisms mapped | `symbiotic-vault-intersection.md` | 2026-03-31 |
| The instrument (rotating hierarchy) | Active — architecture sketched, not built | `higher-purpose-distillation.md`, `genealogy-to-instrument.md` | 2026-03-31 |

### Architectural Threads

| Thread | Status | Home | Next move |
|--------|--------|------|-----------|
| Project charter | **Done** | `patterns/charter.md` | — |
| Frame layer | Missing — frames exist in practice, not as objects | `genealogy-to-instrument.md` §1 | Define frame format, seed 2-3 frames |
| Cross-project atomic layer | Missing — atomic candidates in prose only | `genealogy-to-instrument.md` §2 | Pick format, extract highest-value atoms |
| Relation vocabulary | Missing — types identified, not codified | `genealogy-to-instrument.md` §3 | Write `patterns/relations.md` |
| Object lifecycles | Missing — statuses exist per-project, not unified | `genealogy-to-instrument.md` §4-7 | Write `patterns/objects.md` |
| Agent-memory conventions | Missing | `genealogy-to-instrument.md` §5 | Write `patterns/agent-conventions.md` |
| Dynamic view layer | Missing — the instrument frontier | `genealogy-to-instrument.md` §6 | Design spike after handles stabilize |
| Process doc | **Done** | `00-Notes/process.md` | Keep threads-in-flight current |

### Subproject Status

| Project | Progress | Current edge |
|---------|----------|-------------|
| `texts/erkenntnisproblem-vol1/` | 45 parts; section IV closed; harmonization pass done | Skepticism chapter, Part 46 from broken Montaigne sentence |
| `texts/zeitmauer/` | 44 parts (§§123+) | Siderische Einteilungen; handle pilot live, thread extraction growing |
| `texts/tektologiya-vol1/` | 10 parts | Progressive selection / structural crisis |
| `texts/escolios/` | §§1-108 translated (8 section files) | Continuing sequential batches |
| `texts/escolios-ii/` | 2 section files; extraction pipeline building | History-and-ruin opening; aphorisms.yaml restructuring |
| `texts/exegesis/` | 17 passes (folders 02-04, 14-19, 23-30, 38); 3 thread dossiers | Stable; no recent pushes |
| `sources/` | Uexküll complete (5 encounters); Anders Band I complete (5 encounters); modern sources growing | Next source move should be demand-led rather than queue-filling by default |

## Maintenance

This doc should be updated:
- When standing state changes materially (update `right-now.md`)
- After any chat distillation (update threads-in-flight)
- After any crystallization into `patterns/` (update architectural threads)
- After subproject work sessions (update subproject status)

It does not need to capture everything. It needs to capture enough that any session can pick up where the last one left off.
