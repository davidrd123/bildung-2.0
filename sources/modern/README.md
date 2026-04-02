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

All encounters carry `status: open` until a translation session reaches for the concept and the encounter changes how the passage is read. Confirmation that the concept "fits" is not enough. The encounter must teach something unexpected.

## Queue

Concepts referenced in project prose but not yet encountered. Ordered by anchor density (most connections to live translation work first). An entry moves from queue to encounter file only when triggered by live work.

| Concept | Key source | Anchors | Triggered by |
|---------|-----------|---------|-------------|
| Observer-dependent reality | von Foerster, "On Constructing a Reality" (1973) | `zm:6`–`zm:9` (Hinzutretende chain) | Zeitmauer glossary |
| Autopoiesis | Maturana & Varela, "Autopoiesis" (1973) | exegesis (VALIS as living information), zeitmauer (time wall as threshold) | Agüera y Arcas hierarchy |
| Compression | Freedman et al., "Compression Is All You Need" (2026) | `esc:4` (pointillism), handle schema | Prior conversation |
| Local/global failure | Spivak or Bredon on sheaf theory | `esc:2` (symmetric injustices), close/free residue | Cross-domain synthesis |
| Active inference | Friston, "The Free Energy Principle" (2010) | exegesis (recursive model-revision) | Exegesis second pass |
| Closure of constraints | Montévil & Mossio (2015) | `zm:1`, `zm:11`, autonomy theory | Rosen encounter correction |

## Current Encounters

| File | Concept | Status |
|------|---------|--------|
| `rosen-closure-efficient-causation.md` | Closure to efficient causation | open (headline theorem corrected; organizational insight stable, anti-machine proof disputed) |

## Sketches

Interactive HTML demonstrations live in `sketches/`. Each one shows the shape of one concept's claim — what breaks when you cut a link, what changes when you toggle a parameter. They are drawings, not simulations.

| File | Demonstrates |
|------|-------------|
| `sketches/rosen-mr-system.html` | (M,R)-system: three-node cycle, click to sever |
