# Freedman et al.: Compression Is All You Need

**Source**: Vitaly Aksenov, Eve Bodnia, Michael H. Freedman, and Michael Mulligan, "Compression Is All You Need: Modeling Mathematics" (2026 preprint). This encounter reads the Abstract, Introduction, Section 3 ("Interpreting Data from MathLib"), and Section 5 ("Application and Outlook"). The theorem proofs in Section 2 are used only at the level of headline claim, not closely verified line by line.
**Status**: open
**Triggered by**: `esc:4` / `evidence:aphorism:4:pointilliste` in escolios, the handle schema, and the April 1 session assessment that kept the wrapped/unwrapped and PageRank questions while discarding the inflated formalism

## Overview

The paper makes one strong claim and two weaker ones.

- **Strong claim**: human mathematics (HM) is characterized by compressibility through nested definitions, lemmas, and theorems; formal mathematics (FM) as a whole is vastly larger and not uniformly compressible.
- **Intermediate claim**: the growth behavior of MathLib, used as a proxy for HM, looks more like an abelian compression regime than a non-abelian one.
- **Speculative claim**: compression measures plus a PageRank-style refinement could quantify mathematical interest and guide AI exploration.

For this project, the paper is useful less as a theorem about the handle system than as a disciplined language for one familiar observation: brevity is not simplicity, and a small wrapped surface can carry enormous unwrapped depth. The paper helps where the repo wants a *diagnostic question* ("which handles are load-bearing?"), not where it wants a ready-made metaphysics ("the repo is literally `A_n`").

---

## Passage 1: HM versus FM through compression

### Formal (Freedman et al.)

The paper distinguishes:

- **FM**: the totality of valid formal deductions
- **HM**: the tiny subset humans discover, value, and can navigate

Its thesis is that HM is marked by compressibility through hierarchically nested macros: definitions, lemmas, theorems, notation. In the abelian model `A_n`, sparse macros can yield exponential expansion of expressivity; in the free non-abelian model `F_n`, comparably sparse macros do not buy much.

The opening paradigm is place notation: with logarithmically many macros (`10`, `100`, `1000`, ...), one gets exponential increase in reach.

### Prose

Not all mathematics is equally inhabitable by finite minds. The mathematics humans actually work in is the region where definitions buy leverage. A short surface string can open into a huge body of structure because the definitions stack cleanly and can be reused. The paper's guiding picture is not "math is true because it compresses," but "human mathematical practice settles where compression is possible."

This is why the paper keeps returning to **wrapped** versus **unwrapped** size. Wrapped length is what the statement or definition looks like when left folded. Unwrapped length is what appears when the whole dependency chain is expanded back down toward primitives.

### Project register

This is the genuinely relevant line for `bildung-2.0`:

- a handle, glossary term, or thread can be short in wrapped form while carrying a large unwrapped field of passages, evidence, and reread pressure
- the real test is whether the compression buys reusable leverage, not whether the token is elegant

What does **not** yet follow:

- that the handle graph is literally the same mathematical object as the paper's monoid model
- that `open` status is formally a non-abelian obstruction
- that every cycle in the repo is therefore mathematically vindicated

The paper gives a strong transfer heuristic for *why concise handles can be real*. It does not automatically ratify every formal analogy chat prose built on top of that.

---

## Passage 2: MathLib, wrapped/unwrapped length, and the missing macro set

### Formal (Freedman et al.)

MathLib is treated as a proxy for HM. The paper constructs a dependency DAG from Lean declarations and defines:

- **unwrapped length**: total count of primitives after recursively expanding all references
- **wrapped length**: token count of the declaration as written
- **depth**: longest path to primitives in the dependency graph

The reported findings are:

- unwrapped length grows exponentially with depth
- wrapped length stays roughly constant across depths
- unwrapped length grows exponentially with wrapped length

But the authors also say they do **not** identify the true macro set of HM. Treating all non-primitives as macros is only a rough proxy. Abbreviations, trivial specializations, and library artifacts can fake compression.

### Prose

This is the most useful part of the paper for the repo, because it includes its own brake. The paper is not only saying "look, the graph compresses"; it is also saying "the hard problem is identifying which declarations are doing the real compressive work." The owner’s manual is missing. Some short things are genuine landmarks. Others are just wrappers.

That distinction matters because otherwise every short, well-connected node looks profound. The paper explicitly warns against that by noting that naive proxies can be gamed.

### Project register

This maps cleanly onto several repo pressures:

- a **load-bearing term** is not just a short label; it is one whose evidence chain and reuse justify the compression
- a **dead macro** would be a handle or term whose wrapped form exists but whose unwrapped field is thin, arbitrary, or not actually reused
- a **translation note** can also compress well or badly: some short notes carry a whole reread criterion, others merely rename a difficulty

This is probably the best repo-level takeaway from the paper:

> compressed objects need falsifiable tests for whether they really carry the domain they claim to wrap.

That fits the repo's existing promotion gates in `patterns/handle-schema.md` much better than the louder April 2 chat rhetoric.

---

## Passage 3: Compression, interest, and PageRank

### Formal (Freedman et al.)

The paper proposes:

- `T0` ("taste"): reductive compression, roughly the ratio of unwrapped to wrapped size for the full element
- `I0` ("interest"): deductive compression, roughly the ratio of proof size to statement size after compression
- `I1`: a PageRank-style refinement over the dependency graph, biased toward high-compression nodes

The idea is to give AI agents a sense of direction: stay in the compressible regions of mathematics, and identify elements that are not only compressed themselves but support other high-value elements.

### Prose

The proposal is half-diagnostic and half-aspirational. The diagnostic part is strong: dependency structure can reveal which nodes are carrying disproportionate weight in a mathematical corpus. The aspirational part is weaker: "interestingness" is easy to game, and the paper itself notes that bizarre metamathematical constructions can score very highly without being central mathematics.

So PageRank is useful here not as a judge of value, but as a way to ask where the weight is flowing.

### Project register

This is exactly where the paper becomes useful for retrieval and review:

- a weighted in-degree / PageRank-style pass over handles might reveal which terms, notes, or sections are truly load-bearing
- this would be a **derived diagnostic**, not a promotion mechanism
- it could help identify where the repo's wrapped structure is doing real work and where it is only decorative

The paper does **not** justify:

- promoting handles because a graph metric likes them
- treating numerical centrality as intellectual authority
- replacing journal judgment or source pressure with ranking

The right use is subordinate and local: let the metric ask a question the human then checks against the texts.

---

## Residue matrix

| Direction | What survives | What's lost |
|---|---|---|
| Freedman -> repo | brevity vs. depth; the distinction between genuine and fake compression; load-bearing-node diagnostics | the formal monoid machinery as a direct description of historical or translational material |
| Repo -> Freedman | the importance of resistance, residue, and non-neutral unwrapping; why some expansions destroy the object they explain | the paper's clean dependence on recursively expandable formal objects |
| Freedman -> escolios | the pointillist touch can be short without being simple; a fragment can wrap a much larger implicit field | the metric itself; aphoristic compression is not a Lean DAG |
| Freedman -> handle schema | handles as macros; PageRank as a possible diagnostic of support structure | any automatic warrant for statuses like `open`, `tentative`, or `stable` |
| Freedman -> translation method | the question "what is really load-bearing here?" | the lived sentence-level pressure that cannot be reduced to graph size |

### What no single register captures

The paper gives a mathematical account of compression under clean recursive expansion. The project's hardest cases are often exactly where expansion is **not** clean: open terms, non-commuting translations, historical vocabulary whose force changes with register, and passages where unwrapping alters the thing itself. That is why the Rosen bridge about the non-neutrality of unwrapping remains important. Freedman sharpens one axis of the problem, not the whole field.

---

## Anchors

These are transfer heuristics, not identities.

- `esc:4` / `evidence:aphorism:4:pointilliste` — Gómez Dávila's pointillist claim: short touches can carry a much larger picture than their local surface suggests.
- `texts/escolios/journal.md` — especially the "Compression Reaching Its Limit" notes and the repeated observation that very short aphorisms often leave little gap between close and free versions while medium-length ones open a larger interpretive field.
- `patterns/handle-schema.md` — the macro-set reading of handles is now source-backed enough to use as a heuristic, not as a theorem.
- `sessions/2026-04-01-escolios-cassirer-sprint.md` — prior editorial judgment kept wrapped-length constancy, macro-set reading, and PageRank as the only parts that seemed worth retaining.
- `sources/modern/rosen-closure-efficient-causation.md` — the bridge claim that full unwrapping is sometimes non-neutral and can destroy the explanatory object.

## Open questions (status: open)

### Does the paper justify treating the handle schema as a macro set?

Partly, as a heuristic. It supports the thought that short labels can wrap large structured fields and that some handles are load-bearing while others are decorative. But the repo is not a formal proof DAG, and handles are not recursively expandable definitions in the paper's strict sense. **Working assessment: heuristic yes, identity no (80% confidence).**

### Does `open` status correspond to a non-abelian obstruction?

Not from this encounter. That was chat inflation. `Open` in this repo means the material resists resolution despite rich evidence. The paper's `A_n` / `F_n` contrast concerns compressibility properties of macro sets in formal mathematical settings. The resemblance is interesting but not yet earned as a direct formal translation. **Working assessment: not established (20% confidence).**

### Is PageRank over the handle graph worth trying?

Probably, but only as a derived diagnostic. The paper gives a good reason to ask which nodes support other high-value nodes. It also gives a reason not to trust the output naively, because centrality and interest can be gamed. **Working assessment: worth a bounded experiment later; should not become a value metric.**

### What did the encounter actually teach that the chat did not?

Two things. First, the true payload is narrower than the April 2 chat made it sound: wrapped/unwrapped length, the missing macro-set problem, and PageRank as a diagnostic are the real yields. Second, the paper itself already contains the caution the chat lacked: not every short, connected object is a genuine macro, and identifying the right macro set is a central unsolved problem. That warning is directly useful for this repo.
