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

## Exploratory Weaving

Exploratory weaving is legitimate in the living layer.

By `weaving` this project means:

- associative cross-links
- personal or practice-level engagement
- tentative frame-reads
- speculative syntheses
- language that is trying to find a shape before the shape is fully earned

This is not contamination by itself. The living layer exists partly to make this possible.

Contamination begins when exploratory material crosses into canonical language without passing through resistance. In practice that means:

- no clear source trigger
- no distinction between `survey`, `verification`, and `analytical` mode
- no weakening evidence or rival reading where one is needed
- reuse alone making a claim feel settled

The rule is simple:

- weave freely in `00-Notes/`
- mark the mode when it matters
- keep the source pressure visible
- promote only what survives contestation, reuse, and contact with the material

Exploratory weaving is therefore a protected activity in the living layer and a controlled substance in the crystallized layer.

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

When a distillation surfaces a claim that matters but is not yet a repo
finding, keep it visible without overpromoting it:

- `promoted claims` for what current evidence licenses
- `held below promotion` for what remains live but unearned

This preserves pressure without quietly converting conversation residue into
framework.

### 3. Crystallization

When a synthesis note converges on something stable enough to reference without re-reading the exploration, extract it into `patterns/`:

- A relation type that keeps recurring → `patterns/relations.md`
- An object lifecycle that's settled → `patterns/objects.md`
- A convention for agent work → `patterns/agent-conventions.md`
- A frame definition → `patterns/frames/` only after repeated frame-reads have survived reuse and shown their blind spots

The test for crystallization: would a future session need to re-derive this from scratch, or can it just read the pattern?

## Adversarial Practice

The project's default failure mode is absorbing critique as better prose rather than harder tests. This section exists to counter that. It adds friction, not architecture.

### For translation batches

After each batch, note one passage where the rendering might be *wrong*, not just improvable. Classify the difficulty:

| Type | Meaning | What resolves it |
|------|---------|-----------------|
| **lexical** | dictionary, usage, or period-specific meaning problem | a better lexicon, a native speaker, a parallel passage |
| **contextual** | depends on surrounding argument not yet translated | later sections may settle it |
| **edition** | variant readings, textual corruption, or editorial choices | critical apparatus, rival editions |
| **residual** | genuine resistance to single rendering after the above are exhausted | this is the real `open` |

These types can be mixed — a term may be partly contextual and partly residual. A term with `status: open` should say which types of difficulty keep it open. If the difficulty is primarily lexical or edition, the right move is research, not patience.

### For thread dossiers and cross-project claims

Each thread dossier or cross-project note that makes a developmental or structural claim should include:

- **Rival reading** — at least one alternative interpretation of the same evidence that the project does not currently hold. Not a strawman. A reading a competent scholar in the relevant field might actually advance.
- **Weakening evidence** — what specific passages, facts, or counter-examples would weaken the thread's organizing claim? If nothing would weaken it, the claim is unfalsifiable, not strong.

These belong as sections in the dossier itself, not as separate files.

### Retrieval-visible cues

When close reading yields a clearly earned distinction that later search would likely miss, record that distinction once in the nearest existing artifact.

Prefer local additions over new structures. Good forms include:

- a false-friend warning in a glossary entry
- a `do not confuse with` line in a thread dossier
- a short bridge phrase in an encounter note
- a thread pointer or alternate phrasing in a journal entry

Keep these cues compact. They are not a new metadata layer. They are a way of making source-earned distinctions easier to find later without flattening them into a retrieval ontology.

### For the handle layer

`challenges` is an active relation type (see `patterns/handle-schema.md`). Use it when:

- a passage puts a glossary term's current rendering under pressure
- a later section contradicts the developmental arc of a thread
- a cross-project resonance breaks down on closer inspection
- a modern-source retranslation produces a reading that does not fit the source

Evidence handles can carry negative evidence: `evidence:term:schicksalszeit:zm:22 challenges term:schicksalszeit` means §22 puts the current rendering under pressure rather than confirming it.

### For the project as a whole

The test for whether the adversarial practice is working: could the current batch, dossier, or glossary decision survive being read by a hostile but competent specialist in the relevant field? Not "would they agree" — would they find enough rigor to engage with?

This is not a publication standard. It is a contestability standard. The work does not need to be sent out. It needs to be *sendable*.

## Secondary Trace Diagnostic (2026-04-05)

The current repo does not have one secondary-trace format. It has at least two, and that is not a defect by itself.

- `texts/erkenntnisproblem-vol1/` is currently the richest **prose** trace environment: tranche notes, close-reading ledger, distillation notes, journal, glossary pressure, and the Cusanus chain.
- `texts/zeitmauer/` is currently the richest **relational** trace environment: `source/handles.yaml` carries section handles, anchor handles, translation-note handles, evidence chains, thread links, and journal-note links through the translated range.

In practice that means the `Zeitmauer` work is already generating secondary traces in the handle layer itself, not in a separate `reading/` directory: the handles are not just navigation there, but a real retrieval and evidence surface.

So the right contrast is not `rich` versus `thin`, but different media shaped by different textual grain.

- Cassirer's pressure often needs sentence- or paragraph-scale prose traces.
- Jünger's pressure often needs recurrence, drift, and section-to-thread retrieval.

The practical standard is therefore not uniformity of format but discoverability:

- can a cold start reconstruct why a local decision was made?
- can a modern-source / primary-text contact be found from both sides without rereading whole journals?
- can the trace medium used by one subproject point cleanly into the trace medium used by another?

Current working judgment:

- do not force all subprojects into a `reading/` layer
- do not treat `handles.yaml` as mere derived navigation where it is already functioning as a real secondary-trace surface
- do make cross-project and modern-source contact traces lighter and more routine, because that is still the weakest interoperability point

## Threads in Flight

Living list. Updated as threads advance or stall.

### Intellectual Threads

| Thread | Status | Home | Last active |
|--------|--------|------|-------------|
| Goethe/Leibniz split | Active — central diagnostic | `cross-domain-synthesis-threads.md` | 2026-03-31 |
| Cybernetics braided river | Active — genealogy mapped, tributaries identified | `cross-domain-synthesis-threads.md` | 2026-03-29 |
| The Cassirer node | Active — connects all three texts and now has denser local apparatus inside Cassirer work | `cross-domain-synthesis-threads.md` | 2026-04-04 |
| Barrett constructed categories | Active — epistemological ground for the translation / decryption method | `cross-domain-synthesis-threads.md` | 2026-03-30 |
| Schuon limit | Placed — names the honest boundary of textual recovery | `cross-domain-synthesis-threads.md` | 2026-03-31 |
| Rosen: models vs. simulations | Placed — maps onto close/free split | `cross-domain-synthesis-threads.md` | 2026-03-29 |
| Practice queue (source encounter + decryption) | Active — revised around practical coupling to live work and generalized opacity | `cross-domain-synthesis-threads.md`, `00-Notes/Chats/2026-04-06/extractions/2026-04-06_actual-questions-from-planmaessigkeit-uexkuell-chat.md` | 2026-04-06 |
| Anders bridge | Placed — Band I campaign complete; bridge clarified and available for demand-led reuse | `cross-domain-synthesis-threads.md` | 2026-04-02 |
| Tektologiya as demand-led instrument | Active — bounded reuse rule clarified; visual packet and Rosen encounter now define the next honest tests | `distillations/2026-04-08-earned-distillation-from-opus-on-tektologiya-instrument-pressure.md`, `cross-domain-synthesis-threads.md` | 2026-04-08 |
| Predecided world | Active — Uexküll/Cassirer/Anders/Jünger world-cut connector | `cross-domain-synthesis-threads.md` | 2026-04-02 |
| Empirical morphogenesis line | Active — Levin corpus linked to the braided river | `cross-domain-synthesis-threads.md` | 2026-04-01 |
| Action-conditioned real | Active — von Foerster + late Zeitmauer + Cassirer + Dick | `cross-domain-synthesis-threads.md` | 2026-04-02 |
| Peirce reserve | Seeded — architecture-level convergences noted; no primary encounter campaign yet | `distillations/2026-04-04-earned-distillation-from-peirce-thinking-methods-chat.md` | 2026-04-04 |
| Whitehead decryption | Seeded — identified as target, not started | `cross-domain-synthesis-threads.md` | 2026-03-29 |
| Symbiotic-Vault convergence | Active — structural isomorphisms mapped | `symbiotic-vault-intersection.md` | 2026-03-31 |
| The instrument (rotating hierarchy) | Active — architecture sketched, not built | `higher-purpose-distillation.md`, `genealogy-to-instrument.md` | 2026-03-31 |

### Architectural Threads

| Thread | Status | Home | Next move |
|--------|--------|------|-----------|
| Project charter | **Done** | `patterns/charter.md` | — |
| Handle schema | **Done** | `patterns/handle-schema.md` | Extend only under live pilot pressure; keep strongest implementation local to `texts/zeitmauer/` until a second pilot is earned |
| Frame layer | Reserved in schema, experimental in practice — not yet earned as a crystallized object layer | `genealogy-to-instrument.md` §1 | Keep frame use in living dossiers; crystallize only after repeated frame-reads across anchors/projects |
| Cross-project atomic layer | Missing — atomic candidates in prose only | `genealogy-to-instrument.md` §2 | Pick format, extract highest-value atoms |
| Relation vocabulary | Partial — compact types exist in `patterns/handle-schema.md` and the `zeitmauer` pilot; a separate crystallized doc is not yet earned | `genealogy-to-instrument.md` §3 | Keep using the compact vocabulary in live work; split into `patterns/relations.md` only if cross-project reuse forces it |
| Object lifecycles | Missing — statuses exist per-project, not unified | `genealogy-to-instrument.md` §4-7 | Write `patterns/objects.md` |
| Agent-memory conventions | Missing | `genealogy-to-instrument.md` §5 | Write `patterns/agent-conventions.md` |
| Dynamic view layer | Missing — the instrument frontier | `genealogy-to-instrument.md` §6 | Design spike after handles stabilize |
| Process doc | **Done** | `00-Notes/process.md` | Keep threads-in-flight current |

### Subproject Status

| Project | Progress | Current edge |
|---------|----------|-------------|
| `texts/erkenntnisproblem-vol1/` | 55 parts; Book II `Naturphilosophie` active; close-reading ledger live; Cusanus second-pass map added | Part 56 from the broken sentence on bodily processes in Paracelsus; keep the Cusanus apparatus local unless later pressure forces promotion |
| `texts/zeitmauer/` | 52 parts (`§§1-156`); handle pilot live through the translated range; thread extraction and visuals growing | Late `Siderische Einteilungen`; protean-power / new-type / decadence-scale run active; keep extending the pilot through live translation rather than widening by symmetry |
| `texts/tektologiya-vol1/` | 27 parts; volume-1 main text complete; selective front-matter pass through `front.10`; packet `01` on disk with first two plates | Keep extending packet `01` without turning it into a synthesis sprawl; keep Bogdanov's cross-project use demand-led |
| `texts/escolios/` | Volume I first pass complete: 17 section files, `§§1-499`, minimal handle layer, selective second pass | Thicken only the load-bearing aphorisms when later work forces it |
| `texts/escolios-ii/` | 32 real section files; Spanish source stabilized enough for ongoing batching; Italian witness secondary | Keep batching from the cleaned Spanish source; repair extractor only where live reading exposes exact lies |
| `texts/exegesis/` | 75 passes; first pass complete; second-pass knot syntheses and 10 thread files | Use the new knot structure to bridge the archive into workspace-level method without restarting a second first pass |
| `sources/` | Uexküll complete; Anders Band I complete; modern source shelf present and growing | Next source move should stay demand-led rather than queue-filling by default |

## Maintenance

This doc should be updated:
- When standing state changes materially (update `right-now.md`)
- After any chat distillation (update threads-in-flight)
- After any crystallization into `patterns/` (update architectural threads)
- After subproject work sessions (update subproject status)

It does not need to capture everything. It needs to capture enough that any session can pick up where the last one left off.
