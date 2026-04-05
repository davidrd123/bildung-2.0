# Sources — Modern Concept Encounters

## What This Is

The same encounter discipline as the original-language sources, applied to modern concepts that the project already references but has not yet subjected to primary reading. If a concept appears in synthesis prose without having been through close encounter, it is floating on secondhand knowledge. This directory is where it earns its keep — or doesn't.

## How Entries Are Triggered

By the same rule as the classical sources: follow references encountered in the live translation/reading work. The difference is temporal direction. Classical encounters go backward (an escolio quotes Seneca → follow it back). Modern encounters go forward (a Zeitmauer passage echoes autopoiesis → sit with the primary source).

An encounter goes here only if it anchors into specific passages or handles in the live projects. If it doesn't illuminate something you're translating, it doesn't go in.

## Format

Each encounter renders the concept in multiple registers where possible:

- **Formal** — the original source passage
- **Prose** — close paraphrase preserving the argument
- **Poetic** — the concept rendered in the voice of the texts being translated
- **Diagrammatic** — shape, if applicable
- **Computational sketch** — runnable demonstration (in `sketches/`), not simulation
- **Mathematical** — categorical or algebraic version, if applicable
- **Residue matrix** — what survives and what's lost between registers
- **Anchors** — specific handles/passages in zeitmauer, escolios, exegesis

Not every encounter needs every register. The residue matrix is where the actual thinking happens.

## Status

All encounters carry `status: open` until a translation session reaches for the concept and the encounter changes how the passage is read. Confirmation that the concept "fits" is not enough. The encounter must teach something unexpected. After that first validation, an encounter may still remain `open` if its wider transfer range or unresolved claims are still under test.

## Queue

Concepts referenced in project prose but not yet encountered. Ordered by anchor density (most connections to live translation work first). An entry moves from queue to encounter file only when triggered by live work.

| Concept | Key source | Anchors | Triggered by |
|---------|-----------|---------|-------------|
| Closure of constraints | Montévil & Mossio (2015) | `zm:1`, `zm:11`, Rosen correction, Bogdanov boundary | Rosen encounter correction |
| Natural equivalences | Eilenberg & Mac Lane (1945), Introduction + §1 | Erkenntnisproblem (Substanzbegriff → Funktionsbegriff), handle schema relations | Cassirer genealogy |
| Organization as theoretical principle | Mossio, Montévil & Longo (2016) | Erkenntnisproblem (Kant → Goethe → Cuvier genealogy), braided river | Erkenntnisproblem Skepticism chapter |
| Autopoiesis | Maturana & Varela, "Autopoiesis" (1973) | exegesis (VALIS as living information), zeitmauer (time wall as threshold) | Agüera y Arcas hierarchy |
| Compression | Freedman et al., "Compression Is All You Need" (2026) | `esc:4` (pointillism), handle schema | Prior conversation |
| Local/global failure | Spivak or Bredon on sheaf theory | `esc:2` (symmetric injustices), close/free residue | Cross-domain synthesis |
| Active inference | Friston, "The Free Energy Principle" (2010) | exegesis (recursive model-revision) | Exegesis second pass |
| Emergence of meaning from constraint | Deacon, *Incomplete Nature: How Mind Emerged from Matter* (2012) | Erkenntnisproblem (constitutive forms vs. substrate-independent organization), Uexküll (symbolless constitution — tick Umwelt as test case), Bogdanov (organizational invariants without constituting subject), von Foerster (recursive computation, undifferentiated encoding) | **Trigger conditions**: (1) Uexküll encounter reaches a point where the symbolless-constitution problem forces a decision about whether Cassirer's "symbolic form" is the genus or one species of constitution; or (2) Bogdanov translation surfaces an organizational pattern that needs the meaning/mechanism bridge more than the activities-resistances framework can supply; or (3) the information-theory / formal-systems register gap identified in the 2026-04-03 reading sessions becomes a direct obstacle to cross-project work rather than a noted absence. Deacon is a bridge text: he responds to the Shannon/Turing pressure (syntax without semantics doing constitutive work) but is not the pressure in its most exact form. Does not close the formal-systems gap by himself. |
| Negative prehension / concrescence | Whitehead, *Process and Reality* Part III (via Sherburne key) | Bogdanov deingression (Tekt 3.a.5-7), `zm:6` Hinzutretende (supplementary phase), Erkenntnisproblem (Cassirer as near-contemporary process-thinker) | **Trigger conditions**: (1) Tektologiya translation reaches a point where Bogdanov's boundary grammar needs a vocabulary for how exclusion is productive beyond activities-resistances; or (2) Erkenntnisproblem reaches Kant and needs Whitehead's explicit revision of the categories; or (3) a zeitmauer passage forces the Hinzutretende beyond interpretation into the question of how novelty enters an occasion. Do not encounter speculatively — PR is 500 pages and has consumed careers. Use Sherburne as guide, PR as source, selective passages only. |

## Current Encounters

| File | Concept | Status |
|------|---------|--------|
| `rosen-closure-efficient-causation.md` | Closure to efficient causation | open (headline theorem corrected; organizational insight stable, anti-machine proof disputed) |
| `von-foerster-constructing-reality.md` | Observer-dependent reality, recursive cognition, cognitive closure | open (first pressure confirmed in Erkenntnisproblem Part 45; changed the read of Montaigne's organ-conditioned knowledge passage; broader validation still pending) |
| `mcculloch-heterarchy-of-values.md` | Heterarchy of values, diadrome, toroidal anti-hierarchy | open (primary reading complete; anti-hierarchy/topology claim source-secure; no translation-session validation yet) |
| `montevil-mossio-closure-of-constraints.md` | Closure of constraints, constraint/process distinction, time-scale relativity | open (grounds Rosen; bridges to Bogdanov boundary analysis; time-scale parameter τ as genuine contribution) |
| `eilenberg-maclane-natural-equivalences.md` | Natural equivalences, functors, categories, commutativity as criterion | open (Introduction only; Substanzbegriff → Funktionsbegriff formalized; commutativity as residue-detection; all project parallels marked as transfer heuristics) |

## Sketches

Interactive HTML demonstrations live in `sketches/`. Each one shows the shape of one concept's claim — what breaks when you cut a link, what changes when you toggle a parameter. They are drawings, not simulations.

| File | Demonstrates |
|------|-------------|
| `sketches/rosen-mr-system.html` | (M,R)-system: three-node cycle, click to sever |
