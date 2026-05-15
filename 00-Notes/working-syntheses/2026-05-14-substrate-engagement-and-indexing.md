# 2026-05-14 — Substrate vs. Engagement: Indexing as the Underlying Discipline

**Status:** Earned working synthesis. Captures methodological clarifications that have been building across several sessions and that crystallized in session `erk-vol02-05-14b` while discussing the Gassendi Disquisitio campaign's growth past its original anchor.

**Purpose:** Make the substrate/engagement distinction and the indexing rationale durably retrievable. This is not new doctrine — it's the operational discipline the project has been using, named more sharply.

**Provenance:** Discussion in session `erk-vol02-05-14b` (this session), building on:
- `2026-05-14-meta-conversation-markers-erk-vol02-5-13a.md` — particularly the "Re-entry hooks as Anti-Compression" thread and the "negative archaeology" framing
- The Cassirer-as-secondary discussion earlier in this session, where the user pointed out that primary-source contact is "going from low resolution to high resolution" — the same activity, deeper
- The Gassendi README revisions in commits `45177cf` and `a10d424` that operationalize this for one campaign

## The indexing pain point

The underlying motivation for the project's apparatus discipline is this: **chatting with a primary source at chapter pace requires indexes into the source**. Raw text is not navigable in conversation. Even cleaned, well-paginated text doesn't give you the affordances you need to say "go to the part about X" and have the AI find it fast.

What makes a source actually usable in dialogue is layered:

- **Corrected text** — OCR cleaned, ligatures restored, scan boundaries verified. Without this, the AI is fighting noise rather than reading the source.
- **Page-map** — where each passage sits in the physical witness. Without this, you can't verify a claim against the scan.
- **Glossary terms** — recurring vocabulary tracked across tranches, with cross-references to where each term shifts. Without this, the AI has to re-derive a term's working meaning each turn.
- **Journal entries with structural notes** — what each tranche clarified, what the routing decision was, what to expect next. Without this, the AI cannot orient between the current passage and the surrounding argument.
- **Encounter files** — citation-grade ground for specific passages with the surrounding-argument context the citation alone doesn't carry.
- **Parts files** — sequential tranches showing how an argument moves, named by their structural function (`Instantia IX -- fieri/esse and the sunlight analogy`) rather than just by page.

Each layer makes a different kind of question fast. Without glossaries, "how does Gassendi use `realitas objectiva` differently in Meditation III vs. V?" is hours of re-reading. With them, it's one lookup. Without structural part-titles, "show me where the ontological argument is rebutted" is grep through OCR. With them, it's `parts/061-dubitatio-ii-existence-perfection-and-the-triangle-analogy.md`.

The apparatus is, in other words, **an index**. The translation is part of the apparatus, not the deliverable.

## Substrate vs. engagement

This indexing framing clarifies the project's `sources/` vs `texts/` distinction, which had been operating implicitly:

- **`sources/` builds navigable substrate** for primary-source reading. The work is *indexing* a source so that future conversations can chat with it efficiently. Substrate includes: corrected text, glossary, page-map, witnesses.yaml, encounter notes, parts files (if the source's argument warrants sequential walk-through), translation-process journal entries.
- **`texts/` does engagement-with-argument**. The work is *producing structural findings* about what the source's argument is doing: bounded reading notes ("Hobbes's self-created principles harden into absolute powers"), close-reading ledger entries that track how concepts shift across the work, journal entries that synthesize the argument's shape rather than the translation's process.

A source can have an arbitrarily large substrate (62 parts is fine) without having earned `texts/` status — because the engagement layer is a different kind of work, not a more advanced quantity of the substrate work.

This makes promotion to `texts/` **conditional on engagement, not on volume**. The operational test: does the campaign have at least one bounded reading note producing a structural finding about the source's own argument, plus close-reading ledger entries tracking conceptual shifts? Either both exist or they don't. If they don't, the campaign is substrate-only regardless of its scale.

## Two registers of substrate-building

Substrate-building itself can be calibrated to the reading task. Looking at the project's current Latin and modern source campaigns:

- **Light scaffold** (Lotman style). One README explaining what the scaffold is and isn't. Encounter files when specific pressure calls for them. No glossary expansion, no parts/. Used for sources where the reading mode is "browse a chapter and chat about it" — the AI can read the chapter directly, and what's needed is just enough apparatus to navigate. Examples: `sources/russian/lotman-vnutri-mislyashih-mirov/`, `sources/modern/ernst-campanella-book-and-body-of-nature/`.
- **Thick substrate** (Gassendi style). Sequential parts following the source's own argument structure, growing glossary, daily journal of translation work, page-map with multiple witness anchors. Used for sources where the reading mode is "walk through the argument tranche by tranche" — the AI needs the corrected Latin and glossary loaded to engage productively. Examples: `sources/latin/gassendi-disquisitio-metaphysica/`.

Both are legitimate substrate-building. The choice between them depends on whether the source needs to be navigable at passage scale (light) or argument scale (thick).

This also explains the encounter-vs-parts proportion question that came up earlier. The Gassendi campaign has 1 encounter and 62 parts. That looks inverted compared to the original intent (encounters as the rare deep-grounding format, parts as the rare grow-into format). But under the substrate framing, **the parts are doing argument-context indexing for the thick-substrate mode**, while the encounter remains a citation-grade index for the one passage Cassirer foregrounded. They are not in tension; they index different reading needs.

## Why this matters for the project's broader methodology

Three discipline implications that follow from naming the substrate/engagement cut:

1. **Volume of substrate is not overreach.** The Schuon-limit guardrail ("expansion without absorption is not progress") applies to *engagement* artifacts: bounded notes, syntheses, reading notes that try to draw too much from too little textual contact. It does not apply to substrate building, because substrate IS the absorption infrastructure. The Gassendi campaign growing to 62 parts is appropriate if and only if it produces text the next reading move can use — which it does.

2. **Cassirer-as-secondary is the same activity at higher resolution.** Earlier in this session the discussion was: "the activity is chapter-pace guided reading; following Cassirer's citations downward to the primary source is the same activity at higher resolution." That's true, but it also means primary-source contact requires substrate. A source not yet indexed is not yet readable at chapter pace. So opening a primary-source campaign is opening the indexing work that enables high-resolution reading. The substrate-building is the resolution-raising mechanism itself.

3. **The encounter format is not a lesser substrate.** Encounters do focused, citation-grade indexing for one passage with surrounding context. They are appropriate when the reading task is "chat about this one passage Cassirer cited." They become inappropriate only when sustained walk-through of the source is the actual reading task — at which point parts/ is needed. Sister campaigns (Campanella, Spinoza Opera) can stay at encounter-only indefinitely if guided reading of those sources doesn't grow past single-passage scale.

## Operational consequences (now operative across the project)

- **Gassendi stays in `sources/latin/`** despite its scale. The README (commits `45177cf` and `a10d424`) frames promotion as conditional on engagement work that has not been done. Substrate may remain indefinitely.
- **Lotman's "Text-Only Scaffold" framing is the model** for light-substrate campaigns. The `sources/modern/ernst-campanella-book-and-body-of-nature/` scaffold built earlier this session follows this model.
- **Spinoza Opera and Campanella Metaphysica campaigns** sit at one-encounter-or-fewer right now. Whether they grow into thick-substrate Gassendi-style campaigns or stay at light-scaffold Lotman-style is determined by the reading task, not by intrinsic priority.
- **Promotion to `texts/` requires bounded reading notes**, not high translation volume. The Hobbes self-created-principles note and the Spinoza absolute-order-and-anthropomorphism note in `texts/erkenntnisproblem-vol2/reading/` are markers of what engagement looks like. If any `sources/` campaign produces equivalent artifacts about its source's own argument, the promotion question becomes earnable.

## Re-entry

Use this note when:

- A `sources/` campaign is growing and the substrate/engagement question surfaces. Apply the operational test (do bounded reading notes exist?) rather than counting parts.
- A new source is being opened. Decide between light scaffold (Lotman model) and thick substrate (Gassendi model) based on the reading task, not based on importance.
- The encounter-vs-parts proportion looks "inverted" in a campaign. Check whether the parts are doing argument-context indexing for sustained reading, or whether they have started doing engagement work that should be relocated to a `texts/` project.
- Volume of work in `sources/` triggers Schuon-limit concerns. Distinguish substrate-volume (appropriate) from engagement-volume (which should be in `texts/` and is what the limit actually warns against).

Do not use this note as:

- Authority on which campaigns should grow. The reading task drives that, not the apparatus.
- A reason to promote campaigns to `texts/` prophylactically. Promotion is earned by engagement artifacts, not by substrate scale.
- A prescription that all sources need thick substrate. Most can stay at light scaffold or encounter-only.
