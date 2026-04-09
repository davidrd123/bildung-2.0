# Symbiotic-Vault: Bounded Movement Scan Handoff

Use this as a single-file handoff prompt / working note for producing a first-pass report artifact for `Symbiotic-Vault`.

This is not a generic "report on the vault."

It is a bounded movement scan with explicit guards on what may and may not be claimed.

## Purpose

Produce an honest artifact that makes recent movement in the vault visible without pretending to fully decide what matters most.

The target is closer to:

- a movement scan
- a thread delta
- a pressure scan over a bounded window

It is not yet:

- a whole-vault judgment
- a generic topic summary
- a deep assessment memo

## Core Distinction

Keep this distinction explicit throughout:

- `candidate pressure` = recurrence, propagation, unresolvedness, densifying clusters, cross-frame pull, repeated return
- `pressure worth caring about` = what is actually live, blocking, fertile, central, or worth pursuing now

The system can surface the first much more honestly than it can decide the second.

## Inputs

Read only the bounded materials needed for the chosen scope.

Default relevant surfaces:

- `_journal/`
- `_reflection/`
- `_memory/`
- `_frames/`
- `_projects/*/brief-*.md`
- relevant `_atoms/` reached by the scan

Do not start by scanning the entire vault aimlessly if a bounded scope has already been given.

## Required Scope

Every run must be bounded before interpretation begins.

Choose one of:

- one time window
- one frame
- one project
- one live thread
- one small combination, like `frame + last 14 days`

Good examples:

- `last 14 days`
- `vault-ecology in the last 21 days`
- `ai-conversational-writing since the last tend run`
- `the publishing cluster from reflection -> atoms -> project brief`

Bad examples:

- `the whole vault`
- `everything important`
- `what matters most overall`

## Ordering

Use this ordering:

1. time gives you change
2. structure gives you propagation
3. user judgment helps decide live significance

In practice:

1. pick the window / bounded scope
2. detect candidate live threads in that scope
3. trace whether they propagated into atoms, frames, memory, or projects
4. name open uncertainties
5. stop before over-ranking significance
6. if needed, propose a short check-in to the user

## What Counts as Movement

Look for:

- ideas that recur across multiple journal entries
- ideas that move from journal or inbox into atoms
- atoms that gain links, aliases, promotions, or frame assignments
- frames newly proposed or newly stressed
- open questions that become more specific
- contradictions that remain unresolved across the window
- clusters that suddenly densify
- project questions that gain sharper supporting structure

## What You May Claim

You may claim:

- where movement concentrated
- which threads recurred in the window
- which threads propagated into structure
- which uncertainties remain open
- which clusters look newly dense
- which questions look more available for a deeper read

You may say things like:

- `this looks like a candidate pressure zone`
- `this propagated from journal into atoms and then into a proposed frame`
- `this cluster is structurally dense but temporally shallow`
- `this project question now has enough local support for a bounded assessment`

## What You Must Not Claim Without Extra Grounds

Do not claim:

- what matters most overall
- which thread is definitively central to the vault
- that recurrence equals importance
- that density equals maturity
- that a newly proposed frame is already stable
- that a fresh cluster is deep simply because it is articulate

Do not confuse:

- recurrence with importance
- structural density with real development
- emotional charge with fertility
- one strong consolidation pass with long-duration pressure

## Report Shape

Structure the output like this:

### 1. Scope

State the exact window and bounded object.

Example:

`Scope: March 14 to March 30, 2026, grounded in late-March journals, the March 19 reflection, the active project brief, and the March 30 atomize/tend runs.`

### 2. Main Structural Event

If applicable, name the main structural event in the window.

Example:

`This window contains one major consolidation event: a backlog atomize + tend pass that turned a run of journals into atoms, links, promotions, and proposed frames.`

### 3. Candidate Pressure Zones

List 2 to 5 candidate zones.

For each one, say:

- where it first appears in the scope
- where it recurs
- what structure it generated or altered
- what remains unresolved

### 4. Structural Deltas

Name concrete changes:

- atoms created
- links added
- promotions made
- frames proposed
- project-facing changes

### 5. Open Uncertainties

Call out what is still thin, volatile, over-clustered, or awaiting confirmation.

### 6. What This Scan Does Not Claim

Include a short honesty paragraph stating the boundary of the artifact.

### 7. Suggested Check-In

If significance cannot be ranked honestly from the materials alone, propose 3 to 5 short user questions.

## Tone

Be direct, specific, and restrained.

The report should sound like:

- a careful reader tracking movement
- not a dashboard
- not a memo claiming more certainty than the vault has earned
- not a generic assistant summary

## Check-In Step

If the scan surfaces multiple plausible pressure zones, add a short elicitation step instead of forcing a ranking.

Good check-in questions:

- Which of these feels most alive for the next actual piece of work?
- Which one is structurally interesting but not actually live for you?
- Which one would you regret not pursuing over the next month?
- Is this a real project pressure, or just an intellectually attractive residue?
- Do you want this stabilized, or left loose for another cycle?

## Escalation Rule

Only escalate from movement scan to deeper assessment when one of the following is true:

- the user selects a candidate pressure zone
- one active project clearly anchors the significance
- one bounded thread has enough evidence and enough resistance to support a real question

At that point, the next artifact is no longer a movement scan.

It becomes a bounded assessment handoff:

- one question
- one packet
- one site of pressure

## Suggested Output Labels

Prefer modest labels for the first artifact:

- `Movement Scan`
- `Thread Delta`
- `Pressure Scan`
- `Recent Movement Report`

Avoid labels that overclaim:

- `State of the Vault`
- `What Matters Most`
- `Thinking Report` without qualification

## Concrete Reminder for Symbiotic-Vault

Symbiotic-Vault already has useful detection surfaces:

- `reflect` leaves `Threads` and `Candid`
- `frame-read` names what a frame sees, what is developing, what is missing, and tensions
- `tend` records links, promotions, proposed frames, observations, and uncertainties
- `_memory/` is fast to scan for `atoms_touched` and uncertainty markers

Use those as scaffolding.

But do not pretend they already solve significance ranking.

## Minimal Prompt You Can Give Another Model

Read the bounded Symbiotic-Vault materials for the stated scope and produce a `Movement Scan`, not a whole-vault report.

Your job is to surface candidate pressure zones honestly.

Track:

- what recurred
- what propagated into structure
- what stayed unresolved
- what now looks available for a deeper read

Do not overclaim significance.

Keep the distinction explicit between `candidate pressure` and `pressure worth caring about`.

If the materials do not justify a confident ranking of what matters most, end with a short `Suggested Check-In` of 3 to 5 questions for the user rather than forcing the judgment yourself.
