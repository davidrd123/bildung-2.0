# Q Set 01 — Protocol and Frame Audit (Direct Prompts for GPT-5.4 Pro)

Use one prompt at a time.

Paste the prompt body itself into GPT-5.4 Pro along with the listed core documents.

These prompts were written after auditing the 2026-04-02 `DeepResearch` returns. The aim here is stricter contestability, not more elevated self-description.

---

## Prompt-design audit before reuse

What worked well in the older prompts:

- asking for direct substantive answers rather than prompt commentary
- forcing an outside-facing or adversarial stance
- rewarding deflation over prestige
- requiring explicit sections and concrete judgments

What was misleading or should not be templated forward unchanged:

1. **Comparison-heavy framing can oversteer the answer.**

   Prompts that require "most embarrassing comparison," "most clarifying comparison," or fixed resemblance scores produce useful outside readings, but they push the model toward classification theater. That is good for external description and bad for protocol audit.

2. **Some prompts preload the diagnosis they are supposed to test.**

   Examples from earlier sets:

   - calling a self-critique "suspiciously clean"
   - saying a split is "load-bearing" before asking whether it holds
   - asking what traditions have "already achieved the reunion"
   - implying the project is "most clearly not asking itself" a certain question

   These are good provocations but bad audit prompts. They smuggle a preferred adversarial frame into the question.

3. **Role pressure can become performative.**

   Asking for a "hostile critic" is useful. Asking for "the harshest possible takedown" or for the model to "attack" something can reward rhetoric over discrimination.

4. **False precision is easy to induce.**

   Numerical resemblance scores and overly tidy matrices can create the feel of rigor without adding real contestability.

5. **Prestige or novelty pressure distorts protocol review.**

   Prompts that push toward deciding whether the project is "truly novel" or "already an instrument" bias the model toward a status verdict. For protocol audit, the real question is narrower: what is earned, what is anticipated, and what is currently misleading.

The prompts below are designed to avoid those distortions.

---

## Prompt A — Protocol Audit: Earned vs Anticipated Architecture

I am giving you core documents from a project called `bildung-2.0`.

Do **not** rewrite this prompt, suggest alternative prompts, or discuss prompt design. Answer the request directly.

Read the documents as a competent but unsympathetic reviewer of method. Your job is not to admire the project and not to dismiss it. Your job is to determine which parts of the protocol are genuinely earned by repeated practice, which parts are only reserved or anticipated, and which parts may already be distorting inquiry.

Important constraints:

- Do not generate new architecture.
- Do not reward elegant self-description.
- Prefer demotion over promotion when the evidence is ambiguous.
- If a claim looks plausible but under-supported, classify it as under-supported.
- Distinguish clearly between what the documents say and what the current practice actually demonstrates.

Core documents to attach:

- `patterns/charter.md`
- `patterns/handle-schema.md`
- `00-Notes/process.md`
- `AGENTS.md`
- `texts/zeitmauer/threads/goethe-leibniz-frame.md`
- `texts/erkenntnisproblem-vol1/reading/2026-04-04-earned-distillation-from-cusanus-generative-chains-chat.md`
- `00-Notes/2026-04-04-earned-distillation-from-peirce-thinking-methods-chat.md`

Tasks:

1. Sort the protocol into three buckets:
   - `Earned by repeated practice`
   - `Reserved but not yet earned`
   - `Currently misleading or overbuilt`
2. For every item you place in `Currently misleading or overbuilt`, quote or cite the exact document feature that makes it misleading.
3. Identify one way the current protocol may be protecting itself from criticism by naming the criticism in advance rather than exposing itself to it.
4. Identify one way the protocol may be underbuilt rather than overbuilt.
5. Say whether the chat → distillation → promotion pipeline currently looks like a real filtration mechanism or a grooved ritual that can make unearned material feel earned.
6. Name the smallest defensible repo change that would make the protocol more honest.
7. Name the smallest defensible repo change that would make the protocol more contestable.

Structure your answer under these exact headings:

- `Earned By Practice`
- `Reserved But Not Yet Earned`
- `Currently Misleading Or Overbuilt`
- `Where The Protocol Protects Itself`
- `Where The Protocol Is Still Underbuilt`
- `Chat To Distillation Pipeline`
- `Smallest Honest Change`
- `Smallest Contestability Change`

In `Currently Misleading Or Overbuilt`, each point must include:

- the claim or structure
- why it is premature or distorting
- what evidence would be needed to earn it

Do not end with inspiration or summary rhetoric. End with one sentence beginning exactly:

`The protocol is strongest where ...`

---

## Prompt B — Frame Audit: Reserved Namespace or Real Layer?

I am giving you a small set of files from `bildung-2.0`.

Do **not** rewrite this prompt, propose better prompts, or discuss prompt engineering. Answer the substance directly.

The question is narrow:

Has this project earned a real frame layer, or has it only earned a reserved namespace and a few experimental frame-like dossiers?

Important constraints:

- Do not invent new frames.
- Do not reward vocabulary that redescribes the same thing more elegantly.
- Treat repeated use as more important than conceptual beauty.
- If a frame yields insight but has not yet shown its blind spots, count that against promotion.

Files to attach:

- `patterns/handle-schema.md`
- `00-Notes/process.md`
- `texts/zeitmauer/threads/goethe-leibniz-frame.md`
- `00-Notes/2026-04-04-earned-distillation-from-peirce-thinking-methods-chat.md`

Tasks:

1. Decide whether the current state is best described as:
   - `No frame layer yet`
   - `Reserved frame namespace with experimental uses`
   - `A genuinely earned frame layer`
2. Defend the choice using only the attached documents.
3. Identify what the current frame-like materials actually prove.
4. Identify what they do **not** yet prove.
5. Say whether the present language in the documents is overstating or understating frame maturity.
6. Recommend the smallest defensible wording change if any current wording is still misleading.

Structure the answer with these exact headings:

- `Current Best Description`
- `What The Existing Materials Actually Prove`
- `What They Do Not Yet Prove`
- `Where The Language Overstates`
- `Where The Language Understates`
- `Smallest Wording Fix`

Do not generalize to the whole project beyond what these files support.
