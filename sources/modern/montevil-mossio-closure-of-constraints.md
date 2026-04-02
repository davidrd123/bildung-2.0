# Montévil & Mossio: Closure of Constraints

**Source**: Maël Montévil & Matteo Mossio, "Biological organisation as closure of constraints," *J. Theor. Biol.* 372 (2015), pp. 179-191
**Status**: open
**Triggered by**: the Rosen encounter's open question on anti-computability; Bogdanov's activities-resistances and boundary analysis; Uexküll's Funktionskreis as constraint-structure

## Overview

This paper works within Rosen's framework while judging his characterization of closure too abstract for biological application. Montévil & Mossio present themselves as "directly inspired by" and "consistent with" Rosen, but they ground the concept differently: the entities that close are *constraints* (not abstract efficient causes), and they operate at *specific time scales* (not in a scale-free algebraic formulation). The result is a version of closure concrete enough to apply to actual biology while remaining formally precise. They do not frame their work as settling the Rosen dispute about computability — they reformulate the concept so that the dispute becomes less central.

The key innovation is the constraint/process distinction. Processes are the thermodynamic flow — chemical reactions, energy transfers, physical changes. Constraints are entities that act on processes while being conserved at the relevant time scale. Closure occurs when constraints mutually depend on each other: each one's existence is maintained by processes that are constrained by other constraints in the set.

---

## Passage 1: Constraints versus Processes

### Formal (Montévil & Mossio, §2-3)

> "What do we mean by constraints? In contrast to fundamental physical equations and their underlying symmetries, constraints are contingent causes, exerted by specific structures or dynamics, which reduce the degrees of freedom of the system on which they act."
>
> **Definition 1 (Constraint)**: Given a process A → B, C is a constraint on A → B, at a specific time scale τ, if and only if:
> I/ The situations A → B and A_C → B_C are different (asymmetric) — the constraint makes a causal difference.
> II/ A constraint, while it changes the way a process behaves, is not altered by (is conserved through) that process at the scale at which the latter takes place.

The vascular system constrains blood flow (channels it to every cell) without being consumed by the flow at the time scale of circulation. An enzyme constrains a chemical reaction (accelerates it by orders of magnitude) without being consumed at the time scale of catalysis.

### Prose

There are two causal regimes in biological systems, not one. *Processes* are the thermodynamic flow — reactions, transfers, changes of state. They consume inputs and produce outputs. *Constraints* are structures that channel processes without being consumed by them at the relevant time scale. The vascular system doesn't participate in the blood's chemistry; it shapes where the blood goes. The enzyme doesn't become part of the product; it shapes how fast the reaction occurs.

The crucial qualifier is *at the relevant time scale*. Enzymes do degrade — but at longer time scales than catalysis. Vasculature does change — but at longer time scales than circulation. A constraint is not eternal. It is *locally conserved* relative to the process it constrains. This time-scale relativity is what Rosen's formulation lacked.

### Relation to Rosen

Rosen defines closure through "efficient causes" — but Montévil & Mossio judge this too abstract to identify concretely. What entities in a cell are the efficient causes? At what level of description? Their answer: the entities are *constraints* (specific structures that channel processes), and the level of description is set by the *time scale* at which the constraint is conserved. They see this as grounding Rosen's insight rather than replacing it — making closure empirically applicable without claiming to have settled the broader dispute about computability.

### Bogdanov register

Bogdanov's activities-resistances framework has surface overlap but may differ at depth. Both treat boundaries as productive rather than merely restrictive — Bogdanov's drop/atmosphere surface is simultaneously a zone of construction and destruction, and Montévil & Mossio's constraints channel processes without merely blocking them. But the two frameworks ground their claims differently. Bogdanov's constraints are organizational: activities meeting resistances at boundaries, with the distinction being symmetric and viewpoint-relative. Montévil & Mossio's constraints constitute a distinct causal regime *grounded in* thermodynamic openness but not themselves thermodynamic flows — they are specific structures that channel dynamics while being conserved at the relevant time scale, with the distinction being asymmetric. The overlap (productive boundaries, mutual dependence) is real. Whether the organizational and thermodynamic senses of "constraint" are the same concept at different levels of formalization or genuinely different concepts with a family resemblance is an open question that would require sitting with both sources carefully. The hypothesis is worth testing but should not be asserted as a finding.

---

## Passage 2: Dependence Between Constraints

### Formal (Montévil & Mossio, §4)

> "Constraints are typically subject to degradation at *longer* time scales, and must be replaced or repaired. When the replacement or repair of a constraint depends (also) on the action of another constraint, a relationship of dependence is established between the two."
>
> **Definition 2 (Dependence between constraints)**: C₁ depends on C₂ if: (1) C₁ is a constraint at scale τ₁; (2) there is a process at scale τ₂, constrained by C₂, that produces aspects of C₁ relevant for its role as a constraint at scale τ₁.

The enzyme constrains a reaction (at τ₁). But the enzyme itself is produced by ribosomes reading mRNA (at τ₂). The ribosomes and mRNA are themselves constraints on the translation process. So the enzyme *depends on* the ribosome/mRNA constraint. The dependence is between constraints, not between processes — and it operates across time scales.

### Prose

Constraints break down. They are conserved at the time scale of the process they constrain, but they degrade at longer time scales. When the repair or replacement of one constraint depends on the action of another constraint, the two are in a relationship of *dependence*. This dependence is not a thermodynamic exchange — no energy or matter flows between the constraints at the relevant time scale. It is an organizational relationship: one constraint's continued existence requires processes that are shaped by another constraint.

The paper distinguishes *slow dependence* (τ₂ > τ₁: the generative constraint operates at a longer time scale than the dependent) from *fast dependence* (τ₁ > τ₂: the generative constraint operates at a shorter time scale). Organizational closure requires both kinds jointly.

### Diagrammatic

```
Slow dependence (τ₂ > τ₁):         Fast dependence (τ₁ > τ₂):

scale                               scale
  τ₂  :  A₂ ——C₂——→ C₁                τ₁  :  A₁ ——C₁——→ B
        :                                    :
  τ₁  :  A₁ ——C₁——→ B                 τ₂  :  A₂ ——C₂——→ C₁
        :                                    :

C₂ generates C₁ from above.         C₂ generates C₁ from below.
The producer is slower               The producer is faster
than the product's action.           than the product's action.
```

---

## Passage 3: Closure

### Formal (Montévil & Mossio, §5)

> **Definition 4 (Closure)**: A set of constraints C realizes overall closure if, for each constraint C_i belonging to C:
> 1. C_i depends directly on at least one other constraint belonging to C (C_i is dependent);
> 2. There is at least one other constraint belonging to C which depends directly on C_i (C_i is generative).
>
> The authors then add: the set realizes *strict* closure (which they use as the default sense of "closure") if it additionally *cannot be split into two non-empty subsets each of which realizes overall closure independently*. This non-splitting condition is what individuates the system — it says the closure picks out one organism, not two independent ones happening to coexist.

Every constraint in the closed set is both *dependent* (its existence requires processes constrained by others) and *generative* (it constrains processes that maintain others). No constraint is a free rider; no constraint is a dead end. And the set cannot be decomposed into smaller closed sets — the closure is irreducibly *this* system, not a collection of independent subsystems. The non-splitting condition is what connects closure to biological boundaries: it is a formal criterion for where one organism ends and another begins.

### Prose

Closure is the mutual dependence of a set of constraints. Each constraint in the set is both produced by and productive of other constraints in the set. The set as a whole is self-maintaining — not because any single constraint is self-producing (that would be circular in a trivial sense), but because the *network* of dependencies loops back through all its members.

This is Rosen's closure reformulated. The difference: Rosen talks about "efficient causes" closing on themselves in an abstract category. Montévil & Mossio talk about *specific constraints at specific time scales* whose mutual dependence forms a closed network. The organizational insight is the same. The machinery for identifying it in actual biology is new.

### What this adds to the Rosen encounter

The Rosen encounter's open question asked: "Does Rosen's proof against machines hold?" Montévil & Mossio don't directly answer this — they reframe the problem. Their account grounds closure in identifiable entities (constraints) at specific time scales, making the concept empirically applicable regardless of the computability question. The non-computability dispute becomes less central because the framework no longer depends on it.

The Rosen encounter should be updated with a cross-reference to this paper as a grounding companion, not a replacement.

---

## Passage 4: Constraints and Symmetry

### Formal (Montévil & Mossio, §2)

> "In this paper, we base the theoretical and formal characterisation of closure on the concept of *symmetry*... In very general terms, symmetries refer to transformations that do not change the relevant aspects of an object: symmetries and invariants (of energy, momentum, electrical charges, etc.) are therefore complementary concepts, both mathematically and physically."
>
> "The theoretical characterisation of closure as a specific kind of symmetry provides, we submit, a principle for understanding the *stabilisation* of biological phenomena... biological systems can be understood in terms of 'extended critical transitions', which mean that they form coherent structures, whose proper symmetries are inherently unstable."

### Prose

Constraints exhibit symmetry — they are conserved (invariant) relative to the processes they constrain at the relevant time scale. The vascular system exhibits spatial symmetry with respect to blood flow: blood circulates, the vasculature stays put (at the circulation time scale). The enzyme exhibits chemical symmetry with respect to catalysis: substrate transforms, the enzyme configuration is conserved. The constraint is not *identical* with the symmetry; it is the entity whose conservation at τ constitutes the symmetry. But biological symmetries are *inherently unstable* — they degrade, they must be actively maintained, and they may change unpredictably over evolutionary time. This is what makes biology different from physics: in physics, symmetries are the stable ground on which change is described. In biology, the symmetries themselves are contingent, historical, and subject to variation.

Closure is what stabilizes inherently unstable symmetries. The constraints maintain each other. No single constraint is stable on its own (it degrades). The closed set is stable because each member's degradation is compensated by processes constrained by other members.

### Cusan register

This is the *complicatio/explicatio* structure at the biological level. Each constraint is a local *complicatio* — an enfolded invariant that channels the thermodynamic flow. The set of constraints in closure is the *complicatio* of the whole organism — the generating principle from which all the organism's processes are *explicatio*, unfolded. But unlike Cusa's mathematical *complicatio* (the point that generates the line), biological *complicatio* is inherently unstable. It must be actively maintained. The organism is not a mathematical form that simply unfolds; it is a form that must continually *produce the conditions of its own unfolding*.

This is where Montévil & Mossio go beyond both Rosen and Cusa. Rosen has the closure but not the instability. Cusa has the generating principle but not the contingency. Montévil & Mossio have both: a closure that is real (the constraints genuinely maintain each other) and precarious (the symmetries are inherently unstable, historical, subject to variation). That precariousness is what makes biology biology rather than mathematics.

---

## Residue Matrix

| Direction | What survives | What's lost |
|-----------|--------------|-------------|
| Montévil & Mossio → Rosen | The closure concept. The mutual dependence. The organizational insight. | The elegance. The three-node diagram. The impossible-to-simulate claim. |
| Rosen → Montévil & Mossio | The *felt* irreducibility — "what you hold after dissection is not what you killed." | Rosen's poetic force doesn't survive the formalization into constraint/process/time-scale. |
| Montévil & Mossio → Bogdanov | The time-scale parameter and the asymmetry between constraint and process. | Bogdanov's insistence on reversibility (activity and resistance are always relative). Whether the thermodynamic asymmetry and the organizational symmetry are compatible or conflicting is untested. |
| Bogdanov → Montévil & Mossio | The universality claim — that organizational analysis applies to all complexes, not just biological ones. The productive-boundary insight (drop/atmosphere). | Bogdanov's philosophical breadth. Montévil & Mossio are strictly biological. Whether the overlap is deep or superficial is an open question. |
| Montévil & Mossio → Cusa | The generating principle (*complicatio*) made biological: constraint-networks as unstable invariants that must be actively maintained. | Everything Cusan: the theological horizon, the mathematical form, the positive epistemic status. |
| Montévil & Mossio → Uexküll | The Funktionskreis as a constraint-circuit: sensory and motor surfaces constrain the organism's engagement with the world. | Uexküll's subject-relative plurality (many Umwelten). Montévil & Mossio work with one organism at a time. |

### What no single register captures

The time-scale parameter τ is the paper's genuine contribution. It is what makes closure empirically identifiable rather than merely algebraically stated. Neither Rosen, nor Bogdanov, nor Cusa, nor Uexküll has an explicit time-scale parameter in their formulations of organizational closure, self-production, or functional circuitry. Montévil & Mossio show that without it, you cannot distinguish constraints from processes, and without that distinction, closure is too abstract to use.

**Project extrapolation** (not a finding from the paper, but a repo-side inference): the glossary's maturity statuses (seed → tentative → stable → open) may be *time-scale-relative* in an analogous sense. A term is "stable" when it is conserved across the time scale of batch-level translation. It may still degrade at the time scale of a full-book arc review. The maturity lifecycle is a constraint system, and the glossary's health is a form of organizational closure — each term's stability depends on the evidence produced by translating passages that exercise other terms.

---

## Anchors

- `sources/modern/rosen-closure-efficient-causation.md` — direct correction. The Rosen encounter's open question on anti-computability is resolved here: the organizational insight is preserved, the non-computability claim is replaced by empirical identifiability.
- `zm:1`, `zm:11` — the waxwing passage and *bildende Kraft*. The organism's self-shaping capacity may be structurally adjacent to closure of constraints, but the parallel needs testing against the actual passages rather than being asserted as identity.
- Bogdanov `parts/04-structural-mechanisms-i.md` — the drop/atmosphere boundary in 3.a.4 may be a constraint/process interface (cohesion channeling evaporation/deposition). Transfer heuristic, not established finding — see open question on Bogdanov above.
- Uexküll `encounters/02-funktionskreis.md` — the Funktionskreis as a possible constraint-circuit. The structural adjacency (closed loop, organism/world coupling) is real; whether it maps onto Montévil & Mossio's specific formalism is untested.
- Erkenntnisproblem interpretive notes, "The similitudo/assimilatio Turn" — *assimilatio* (active self-measurement) may be constraint-like in that the mind channels experience through its own organizational forms. But calling it "a constraint on the cognitive process" in Montévil & Mossio's technical sense outruns what this encounter has earned. Transfer heuristic only.

## Open Questions (status: open)

### Does the time-scale parameter settle the Rosen dispute?

Partially. Montévil & Mossio preserve Rosen's organizational insight while dropping the non-computability claim. But they don't directly address the computational question — they reformulate closure in terms that make it empirically identifiable regardless of whether it's computable. The dispute about simulation becomes moot because the concept no longer depends on it. **Working assessment: this is the better formulation for the project's purposes (90% confidence). Update the Rosen encounter's open questions accordingly.**

### Is the constraint/process distinction the same as Bogdanov's activity/resistance distinction?

Adjacent but not identical. Bogdanov's distinction is symmetric (any activity is a resistance from another viewpoint). Montévil & Mossio's is asymmetric (the constraint is conserved; the process is not — at the relevant time scale). The asymmetry is grounded in thermodynamics. Bogdanov's symmetry is grounded in the universality of the organizational point of view. Both are useful. The Montévil & Mossio version is more precise for biology; the Bogdanov version is more general. **Working assessment: complementary tools, not competing claims. The project should hold both.**

### Does "inherently unstable symmetries" connect to Jünger's time wall?

Speculatively. Jünger's argument is that historical categories (the naming regime, the political vocabulary, the temporal frame) are breaking down — they are constraints on civilizational experience that are degrading at the current time scale. If the time wall is a constraint-boundary at which the symmetries of historical time lose their stabilization, then Montévil & Mossio's framework offers a formal vocabulary for what Jünger describes phenomenologically. But this is speculative and should not be asserted as a finding. **Status: marked for testing against zeitmauer §§109+ when translation resumes.**
