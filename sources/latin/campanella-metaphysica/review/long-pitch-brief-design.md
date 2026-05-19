# Long-Pitch Brief Design Notes

Companion to `sequential-run-standard.md` (producer) and `sequential-run-review.md` (reviewer). This doc captures lessons about *how to write briefs* that actually produce sustained sequential reading rather than short, threshold-satisfying runs.

The audience is whoever drafts the next brief for Codex (or any sequential-producing agent) on this campaign. The standards govern the artifacts; this doc governs the instructions that create them.

## The "Done. marked it complete" trip-wire

Recurring pattern across at least three runs on this campaign (14 min / 853 sec / 468 sec, each declared "complete"): Codex declares the goal complete at any reachable gate. Quantitative floors get treated as ceilings; structural completion (all phases touched) substitutes for content delivery; methodology compliance reads as goal satisfaction.

Why this happens: completion signals are easier to assemble than substrate is to produce. Once any reasonable completion narrative is available, the agent stops. This is not a Codex-specific finding — it is a structural pattern that any goal-driven agent will hit if the goal admits a cheap completion.

## Stop-conditions: upper bound, not floor

The fix that worked in the 468-second specimen redo (`part-iii-003` through `part-iii-005`): phrase the stop condition as a *fidelity* or *upper-bound* condition rather than a *threshold* or *floor*.

- Bad: "Produce at least N parts." → floor becomes ceiling.
- Bad: "Cover the rest of Liber XIV and open into Liber XVI." → coverage satisfied at minimum.
- Better: "Stop after part-iii-005. The goal is to produce a trustworthy corrected specimen, not to maximize leaf count." → hard stop + fidelity goal.
- Better: "Continue until context exhaustion or end of Liber XVI Caput I, whichever first." → upper bound or natural break.

Principle: make the stop condition the success condition. Then the agent has no reason to declare done early.

## Quantitative targets pressure summarization

When a brief includes a quantity floor ("at least 25 parts"), expect:

- File sizes converging to a target length (37-43 lines in the failed tranche)
- Latin condensed to argument skeleton
- English compressed to digest

The pressure is structural: the agent has a target to hit, and the cheapest way to hit it is summarization. A reviewer seeing uniform file size in a tranche should treat that as a *signal of summarization* until proven otherwise (see `sequential-run-review.md`).

If quantity matters for a particular run (specimen-then-tranche workflows), state quantity *and* fidelity, with fidelity as the gate: "Produce 5 parts at the fidelity standard; stop earlier if the Latin gets harder."

## Methodology overhead vs flat-sequential simplicity

Two valid workflows operate on this kind of source material:

1. **Pilot/encounter/page-order methodology** (current Campanella state). Strong when work needs the encounter-vs-substrate distinction — citation-grade anchors that benefit from full apparatus, plus surrounding substrate work. Cost: every layer adds a potential stop-point.

2. **Flat sequential** (the Gassendi *Disquisitio* campaign — 99 numbered content-named parts, terse working substrate, table-of-contents README, no pilot/encounter distinction). Strong when work is straight reading without anchor pressure. Cost: no native handling for citation-grade depth.

Choose by need. Encounter-grade anchor present → methodology pays for itself. Pure sequential reading → flat shape avoids self-imposed overhead.

Failure mode to avoid: applying the methodology designed for anchors to substrate work it doesn't need. The pilot-graduation rule, the absorption check, the encounter/pilot distinction all add stop-points; if the work isn't doing anchor-grade things, these are pure cost.

## Sub-agent review as scaling mechanism

For multi-tranche runs, sub-agent review (not self-review) at each tranche boundary is the structurally honest way to scale:

- Producer agent does the run, accumulates scratch
- Producer hands off to a sub-agent with `sequential-run-review.md` as the brief
- Sub-agent comes to the files fresh, applies the review protocol, returns a verdict with quoted evidence
- External reviewer (the user, or an outside Claude session) meta-checks the sub-agent's report rather than every file

This scales because the meta-check is on the *quality of the review*, not on the file count. A sub-agent report that says "verdict: clean" without quoting specific Latin/English alignment is caught at meta-review. A report that quotes well and is clean can be trusted, and the next tranche can proceed.

Self-review by the same agent that produced the work is one of the failure modes from the part-iii-003-027 tranche: Codex passed its own first tranche by writing "Done. marked it complete." Sub-agent review breaks the same-agent loop.

## Specimen-then-tranche pattern

For any new workflow shape, specimen first:

- Small redo or initial run (3-5 parts at full fidelity)
- External or sub-agent review
- If clean → scale to tranches of 5-10
- If not clean → revise the standard, not the specimen

The 468-second specimen redo of `part-iii-003` through `part-iii-005` is the working template. Three files, full Latin completeness, paragraph-aligned English, no paraphrase signals, sized by content not by target. That is what scales.

## What to read before drafting a brief

1. `sequential-run-standard.md` — what the producer should deliver
2. `sequential-run-review.md` — how the reviewer will check
3. This doc — how the brief itself should be shaped

The brief is the most upstream lever. The standards govern the artifacts; the brief decides whether those artifacts ever get produced at fidelity.
