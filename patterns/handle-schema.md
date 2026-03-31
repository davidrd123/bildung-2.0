# Handle Schema

Stable IDs for everything in the repo that the UI, notes, commentary, and agents need to point at. The principle: text files remain the authority; handles are derived structure that makes the authority navigable.

## Design Constraints

1. **Human-readable.** A handle should be parseable at a glance in a markdown note.
2. **Stable.** Once assigned, a handle doesn't change. Content can be revised; the handle persists.
3. **Cross-project.** The same handle grammar works for escolios, zeitmauer, exegesis, and sources.
4. **Composable.** Chunk handles nest inside section handles. Note handles attach to any anchor.
5. **Greppable.** Every handle is a single token with no whitespace, usable in YAML, markdown, and URLs.

## Handle Types

### Section handles

The primary unit. One per numbered section, aphorism, or entry.

| Project | Format | Example | Source field |
|---------|--------|---------|-------------|
| zeitmauer | `zm:{id}` | `zm:14` | `sections.yaml` id |
| escolios | `esc:{id}` | `esc:42` | `aphorisms.yaml` id |
| exegesis | `exg:{source_id}` | `exg:4:1` | `entries.yaml` source_id |
| sources | `src:{lang}:{file-stem}` | `src:greek:diogenes-laertius-vii-165` | filename in `sources/{lang}/` |

### Chunk handles

Sub-section units. Paragraphs within a section, or named passages.

Format: `{section_handle}:p{n}` for paragraphs (numbered from 1 in the German/Spanish/English source).

Examples:
- `zm:14:p1` — first paragraph of Zeitmauer §14
- `zm:14:p3` — the paragraph about augury and the Trajanic frieze
- `esc:42:p1` — first paragraph (usually the only one) of escolio 42
- `exg:4:1:p2` — second paragraph of Exegesis entry 4:1

Named passages (for passages that acquire significance through commentary):
- `zm:14:abdichtung` — the "sealing toward the side of fate" passage
- `zm:11:schachtgaenge` — the "abandoned mine-shafts" image
- `esc:2:ahorcados` — the "two rows of hanged men" image

Named passages are created only when commentary or cross-reference demands it. They supplement, not replace, paragraph numbering.

### Term handles

Glossary entries and cross-project concepts.

Format: `term:{normalized-key}`

Examples:
- `term:schicksalszeit` — glossary entry in zeitmauer
- `term:bruchstelle` — glossary entry in zeitmauer
- `term:hinzutretende` — glossary entry in zeitmauer
- `term:bildung` — cross-project concept
- `term:residue` — cross-project concept (from the Barrett/sheaf thread)
- `term:rotating-hierarchy` — cross-project concept

Term handles point to the glossary YAML entry in their home project, or to a cross-project concept file once promoted to that level.

### Note handles

Commentary, translation notes, and journal observations attached to specific anchors.

Format: `note:{section_handle}:{slug}`

Examples:
- `note:zm:14:abdichtung` — note on the "sealing" metaphor in §14
- `note:zm:11:bildender-kraft` — note on `formative power` in §11
- `note:esc:2:method` — note on §2's claim about symmetric injustices

Unanchored notes (journal-level, not attached to a specific passage):
- `note:journal:mumford-bridge` — the Mumford bridge-text journal entry
- `note:journal:schuon-limit` — the Schuon tradition-vs-traditionalism note

### Thread handles

Cross-cutting themes that span sections and projects.

Format: `thread:{slug}`

Examples:
- `thread:time-crisis` — measurable vs. fateful time across zeitmauer
- `thread:technique-and-modernity` — technology critique across all three projects
- `thread:transmission-chain` — the project's own meta-theme
- `thread:commentary-as-form` — commentary's equal status to translation
- `thread:goethe-leibniz` — the formalism/perception split
- `thread:zebra-valis` — exegesis thread (already exists as `exegesis/threads/zebra-valis.md`)
- `thread:black-iron-prison` — exegesis thread

### Evidence handles

Records of where a term or claim was tested, confirmed, or pressured.

Format: `evidence:{term_handle}:{section_handle}`

Examples:
- `evidence:term:schicksalszeit:zm:4` — §4 first exercises `fateful time` in context
- `evidence:term:schicksalszeit:zm:9` — §9 puts it under load with church-year analogy
- `evidence:term:schicksalszeit:zm:13` — §13 confirms it via `Schicksalsuhr`
- `evidence:term:hinzutretende:zm:6` — §6 introduces the concept
- `evidence:term:hinzutretende:zm:7` — §7 makes it structural (banking metaphor)
- `evidence:term:hinzutretende:zm:9` — §9 extends it to the priestly role

Evidence handles make the glossary's evidence chain machine-readable. The chain for `term:schicksalszeit` can be reconstructed by collecting all `evidence:term:schicksalszeit:*` handles.

### Frame handles

Perspective lenses for cross-project reading. (Not yet implemented in the repo; anticipated from `genealogy-to-instrument.md`.)

Format: `frame:{slug}`

Examples:
- `frame:transmission-chain`
- `frame:time-crisis`
- `frame:whole-knowing`
- `frame:goethe-leibniz`
- `frame:technique-and-modernity`
- `frame:commentary-as-form`
- `frame:symbolic-form-rupture`

## Relation Types

A compact vocabulary for how handles connect. Used in notes, future graph layer, and agent output.

| Relation | Meaning | Example |
|----------|---------|---------|
| `echoes` | structural resonance, not causal | `zm:1:p1 echoes zm:7:p2` (waxwing and banking metaphor) |
| `extends` | builds on, develops further | `zm:13 extends zm:9` (fate-clock develops church-year argument) |
| `translates` | same idea, different domain | `term:hinzutretende translates vault:agent-role` |
| `retranslates` | same idea, updated framework | `note:journal:mumford-bridge retranslates zm:15` |
| `detranslates` | same idea, older/less-differentiated frame | (not yet exercised) |
| `residue-of` | what doesn't survive translation between two frames | `term:bruchstelle residue-of [fracture-point, fault-line, break-point]` |
| `crystallizes` | makes latent pattern explicit | `thread:time-crisis crystallizes [zm:4, zm:9, zm:13]` |
| `pressures` | creates unresolved tension | `zm:11:bildender-kraft pressures term:bildung` |
| `parallels` | independent convergence | `esc:112 parallels zm:10` (knowledge vs. interpretation) |
| `challenges` | contradiction or counter-evidence | (reserved) |
| `grounds` | provides foundation or justification | `evidence:term:schicksalszeit:zm:9 grounds term:schicksalszeit` |

## Maturity Statuses

Shared across all handle types that have lifecycle.

| Status | Meaning | Promotion criterion |
|--------|---------|-------------------|
| `seed` | First appearance, untested | Exists in source, a note, or a newly introduced handle |
| `tentative` | Exercised, provisional choice holding | Tested across 2+ sections/contexts or one coherent traversal path |
| `stable` | Confirmed by sustained use, unlikely to change | Survives repeated use across a full part, repeated traversal, or multiple projects without an equally live rival |
| `open` | Genuinely undecided, multiple live alternatives | Evidence or traversal is rich, but the alternatives remain genuinely live |
| `archived` | Superseded or no longer active | Replaced by a better formulation |

`open` is not a lesser status than `stable`. It is a positive determination that the material resists resolution. An `open` term with a rich evidence chain is more valuable than a `stable` term with a thin one.

### Promotion Gates

These are criteria, not metrics. They exist to make promotion legible, not mechanical.

| Object | `seed → tentative` | `tentative → stable` | `any → open` |
|--------|-------------------|---------------------|--------------|
| `term:*` | Exercised across 2+ sections/contexts | Evidence chain survives a full part or cross-project reuse; no equally live rival | Evidence is rich but 2+ alternatives remain equally supported |
| `thread:*` | Traversal path links 3+ grounded handles | Later rereading uses the thread without re-deriving its organizing claim | Recurrence is real but the organizing interpretation is still under pressure |
| `frame:*` | At least one frame-read yields non-obvious connections | Repeated frame-reads across distinct anchors/projects continue to illuminate | Frame produces insight but also systematic blind spots |

Promotion follows evidence density and reuse, not rhetorical force.

## Implementation Notes

### Phase 1: Convention only

Handles used as plain strings in markdown notes, YAML comments, and journal entries. No tooling required. Humans and agents use them by convention.

Example in a journal entry:
```
The banking metaphor in `zm:7` echoes `zm:1` (waxwing). Both are Jünger's method:
analogy that becomes argument. See `thread:time-crisis`.
The `term:hinzutretende` evidence chain now runs `zm:6` → `zm:7` → `zm:9`.
```

### Phase 2: YAML index

A machine-readable index mapping handles to file locations, statuses, and relations. Generated from the existing YAML sources and batch files. This is the structured extraction layer from the stack in `higher-purpose-distillation.md`.

### Phase 3: Dynamic view

The HTML instrument reads the index and renders navigable, layered views. Handles become clickable links. Evidence chains become visual. Threads become traversable paths. This is where the Symbiotic-Vault intersection becomes concrete — shared handle grammar means the two systems can cross-reference.

### Phase 4: Agent integration

Agents read and write against handles, not loose prose. An agent can say "I found that `zm:22` echoes `esc:145`" and the claim is verifiable, linkable, and persistent. Agent memory entries use handles for `atoms_touched` (borrowing the Vault convention).

## Agent Authority Boundary

Agents may create `seed` handles, propose relations, and suggest promotions.

Agents do not have a direct path to `stable` by prose fluency alone. Promotion is grounded by evidence handles, traversal reuse, and canonical-source updates. If the chain is not there, the proposal stays `seed`, `tentative`, or `open`.

## Interoperability with Symbiotic-Vault

The Vault uses its own ID scheme (atom filenames, frame filenames). Cross-system references use a namespace prefix:

- `vault:atom:agentic-cowriting-as-performative-form`
- `vault:frame:writing-practice`
- `b2:zm:14` (bildung-2.0 handle as seen from the Vault)

This is loose coupling. Neither system needs to import the other's ontology. They just need to be able to *point at* each other's objects with stable, resolvable identifiers.
