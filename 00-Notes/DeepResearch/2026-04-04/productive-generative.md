# Productive / Generative

These are the only prompts in this folder meant for normal use during a translation-first phase.

Use one prompt at a time.

The standard is simple:

- closer contact with the text
- clearer glossary pressure
- better journal capture
- cleaner next moves

If a prompt does not help with one of those, it is probably overhead.

---

## Prompt A — Batch Translation Review: Where Is The Real Pressure?

I am giving you a current translation batch and its immediate supporting files.

Do **not** rewrite this prompt, discuss prompt design, or generalize to the whole project. Answer the work directly.

The question is narrow:

Where, in this batch, is the translation under real pressure, and what is the smallest honest next move for each pressure point?

Important constraints:

- Stay close to the attached text.
- Prefer identifying real instability over offering polished rewrites.
- Classify pressure as `lexical`, `contextual`, `edition`, or `residual`.
- If a passage is workable as-is, say so and move on.
- Do not promote broad cross-project theory unless the batch itself forces it.

Files to attach:

- current `parts/*.md` file
- relevant `source/*.yaml`
- local `journal.md`
- local `source/glossary.yaml`

Tasks:

1. Identify the `3-7` passages under the most real pressure.
2. For each passage:
   - quote or cite the passage
   - classify the pressure type
   - say what is unstable
   - say what the smallest next move is
3. Identify which pressure points should update the glossary now.
4. Identify which pressure points should wait for later context.
5. Name one passage that looks better than the translator may realize and should probably be left alone.

Structure the answer with these exact headings:

- `Highest-Pressure Passages`
- `Glossary Updates Needed Now`
- `What Should Wait For More Context`
- `One Passage To Leave Alone`

---

## Prompt B — Glossary Pressure Only: What Actually Needs To Change?

I am giving you a local glossary and the current translated batch or tranche.

Do **not** rewrite this prompt, suggest ontology work, or generalize beyond the local project. Answer the glossary question directly.

The question is narrow:

Which glossary entries are actually under new pressure from this batch, and what is the smallest honest update for each?

Important constraints:

- Work only at glossary level.
- Distinguish between `new evidence`, `status change`, and `no change`.
- If an entry should remain `open`, say why without trying to force resolution.
- Do not invent cross-project concepts.

Files to attach:

- local `source/glossary.yaml`
- current `parts/*.md` file
- local `journal.md` if relevant

Tasks:

1. Identify glossary entries touched by this batch.
2. For each touched entry, decide:
   - `no change`
   - `notes update`
   - `alternatives update`
   - `status change`
3. Quote the exact evidence from the batch that justifies the update.
4. Identify one term that may look settled but should remain open.
5. Identify one term that may now be stable enough to stop worrying over for the moment.

Structure the answer with these exact headings:

- `Entries With No Change`
- `Entries Needing Notes Updates`
- `Entries Needing Status Review`
- `One Term That Should Stay Open`
- `One Term You Can Stop Circling For Now`

---

## Prompt C — Journal Extraction: What Is Worth Preserving Beyond The Batch?

I am giving you a current batch and its local support files.

Do **not** rewrite this prompt, discuss prompt design, or produce grand synthesis. Answer the journal question directly.

The question is narrow:

What, from this work session, is worth preserving in the journal because it matters beyond the current batch?

Important constraints:

- Prefer cross-batch observations over sentence-by-sentence comments.
- Do not restate ordinary translation labor.
- If nothing rises above the batch, say that.
- Keep the output small and durable.

Files to attach:

- current `parts/*.md` file
- local `journal.md`
- local `source/glossary.yaml`
- any review note or working scratch note from the session

Tasks:

1. Identify `0-3` observations worth preserving in the journal.
2. For each one, say:
   - why it matters beyond this batch
   - whether it is about method, terminology, structure, or drift
   - the smallest durable journal wording
3. Identify anything that feels interesting but does **not** belong in the journal yet.

Structure the answer with these exact headings:

- `Journal-Worthy Observations`
- `What Is Interesting But Not Yet Journal-Worthy`

Under `Journal-Worthy Observations`, use this mini-format for each item:

- `Why It Matters`
- `Type`
- `Suggested Journal Wording`

---

## Prompt D — Next Move Selector: What Is The Most Productive Thing To Do Now?

I am giving you the current local state of a translation project.

Do **not** rewrite this prompt, propose large architecture, or discuss future platforms. Answer the work-planning question directly.

The question is narrow:

Given the attached files, what is the single most productive next move right now?

Important constraints:

- Choose one next move, not five.
- Optimize for momentum plus honesty.
- Prefer source-bound work over meta-work unless the attached state clearly blocks further translation.
- If the bottleneck is unresolved terminology, say so.
- If the bottleneck is fatigue with a passage, say what kind of move would unblock it.

Files to attach:

- local `README.md`
- current `parts/*.md` file
- local `journal.md`
- local `source/glossary.yaml`
- any active `reading/` or `thread` note if relevant

Tasks:

1. Name the single best next move.
2. Explain why it beats the most plausible alternatives.
3. State what concrete output should exist after that move.
4. State one thing that should explicitly **not** be done yet.

Structure the answer with these exact headings:

- `Best Next Move`
- `Why This Beats The Alternatives`
- `What Should Exist Afterward`
- `What Not To Do Yet`
