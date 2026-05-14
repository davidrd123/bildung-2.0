# 2026-05-13 - Lessons from Volume I for the opening of Volume II

Purpose: record the apparatus-level findings Volume I earned, so they remain available to Volume II as *evidence* rather than as inherited prescription. The Vol. 2 scaffold (`texts/erkenntnisproblem-vol2/README.md`, `reading/context-packages.md`, `review-checklist.md`) operationalizes most of these already. This note is the source-side anchor for why those prescriptions exist, so the lessons survive future scaffold edits.

This note is local to `erkenntnisproblem-vol1`. It is not a Vol. 2 plan and not a second volume retrospective. It is written from a re-reading of primary surfaces — selected parts, the close-reading ledger, the glossary, both chain files, the synthesis notes — not only from retrospective summaries.

Inputs primarily consulted:

- `parts/01-prefaces-and-introduction.md` (calibration tranche, part-file form at startup)
- `parts/78-bruno-interval-pure-quantity-and-leibniz.md` (mid-volume part-file form)
- `parts/90-kepler-force-as-function-and-the-arithmetic-of-forces.md` (post-repair late-zone)
- `parts/149-bayle-ethical-reason-the-psychological-motive-of-skepsis-and-the-limits-of-critique.md` (volume close)
- `reading/close-reading-ledger.md` (sentence-scale evidence layer)
- `source/glossary.yaml` (49 entries, status fields)
- `source/cusanus-generative-chain.yaml`, `source/bruno-generative-chain.yaml` (structured-chain schema)
- `reading/2026-04-08-earned-distillation-from-volume-i.md`
- `reading/2026-04-08-whole-run-parts-journal-ledger-scratch-note.md`
- `reading/2026-04-08-volume-i-close-review.md`
- `reading/2026-04-08-artifact-integrity-audit.md`
- `reading/2026-04-09-journal-second-pass-document-regimes.md`
- `reading/2026-04-10-four-surprises-from-encountering-volume-i.md`

## 1. The part-file form itself mutated across phases

The parts directory is not uniform. Three distinct shapes appear:

- **Calibration form (Part 01):** `## Scope` → `**German (corrected)**` → `**Draft**` → short `**Notes**`. Notes are 2–4 lines of specific translation choices (`geistige Kulturmächte` → `powers of intellectual culture`; `Wissenschaft` → `science` for now). No commentary surface is needed yet.
- **Mid-volume form (Parts 63–81, visible in Part 78):** adds a separate `**Working Commentary**` code block between the English and Notes. This was introduced precisely to keep interpretive trace *out of* the English block. Part 78's Working Commentary numbers five interpretive points; the English itself remains translation, not paraphrase.
- **Closure form (Part 149):** returns to Notes-only. But the English is visibly compressed — an embedded Montaigne quote on the `natural man` ("Wilde heißen wir jene, wie wir die Früchte wild nennen…") is present in the German block and absent in the English draft, which jumps to "Bayle is far removed from such a Rousseauesque basic Stimmung."

The Working Commentary surface was *invented* to solve a specific drift between Parts 82 and 94 (the gloss-creep zone) — an additional structural answer beyond the close-reading ledger. The chain files are another such answer. Each surface is downstream of a specific failure the work encountered.

Vol. 2 implication: do not pre-commit to one part-file form. Start with the calibration form, since that is what calibration material can sustain. The Working Commentary block, if needed, is earned later in response to specific pressure; the same is true of any other interpretive surface.

## 2. Two failure modes, not one: gloss-creep and late-run compression

The artifact integrity audit names the gloss-creep zone (Parts 82–94). I had earlier collapsed all late-run debt into "gloss." Primary reading shows two distinct failure modes:

- **Gloss-creep** is paraphrase replacing translation. The English block exists but no longer renders Cassirer's prose — it summarizes the argument. This is what the Parts 82–149 repair pass corrected.
- **Late-run compression** is *elision*. The English exists at draft-translation grade for what it includes, but quotational and intermediate material drops out. Part 149 is the cleanest example: the Bayle close's English preserves Cassirer's argumentative spine but omits a five-line Montaigne quotation and shortens transitional connective tissue. The argument survives; the texture doesn't.

Both correlate with the high-cognitive-load late stretches. They are not the same failure and they need different responses. Gloss-creep is detectable by comparing English against German sentence-by-sentence (it shows up as paraphrase). Compression is detectable only by comparing *length and quotational density* against the corrected German block at full density. The artifact integrity audit's "main-prose full density" standard is calibrated to the second failure, not the first.

Vol. 2 implication: the review-checklist's quality-zone check needs both signals. "Is this still translation, not gloss?" *and* "Is the quotational and connective texture present, or has the English compressed it out?" The second question is easier to skip because compressed English still reads fluently.

## 3. The chain-file schema crystallizes deferred-structure discipline into YAML

Both `cusanus-generative-chain.yaml` and `bruno-generative-chain.yaml` use the same six-field node schema:

- `position`: what the stage claims or presupposes
- `internal_pressure`: where it fails on its own terms
- `operation`: the transformation Cassirer attributes
- `yield`: what new resource becomes available
- `generated_problem`: what the new stage still cannot handle
- `conditions_of_application`: when this concept is doing valid work *and when it should not be detached into a free template*

The last field is the load-bearing one. It is the deferred-structure discipline made first-class in the schema — every node tells future users where the concept's authority ends. The earned-distillation prose form has no equivalent self-limiting field, which is part of why that form grooved into a template while the chain schema did not.

Both chains carry `status: "first-pass"` and `purpose:` statements naming their scope. The point of view is "this is a working representation, not a settled framework."

Vol. 2 implication: if a Vol. 2 chapter forces a chain file (the default is no chain), the schema is portable, but the *only* reason to use it is when prose notes can no longer carry the rate of internal correction. Cusanus and Bruno earned chains out of 149 parts. The threshold is high.

## 4. Glossary thinness in the late run reflects where pressure was being carried

The Vol. 1 glossary has 49 entries. Several load-bearing late terms — `Minimum`, `Grenze`, `Intervall`, `Bruchstelle`-adjacent vocabulary — have no glossary entry. They are carried in the Bruno chain file's `anchor_terms` field on the relevant nodes. The journal-second-pass note states this directly: "the deepest late pressures were often being carried as structures, relations, and method-lines rather than as stable lexical handles."

The glossary entries themselves show the discipline at item-level. Terms with `status: open` and `preferred: null` include `Erkenntnis`, `Rechenmarken`, `ratio`, `leidender Verstand`, `tätiger Verstand`, `Phantasma`, `quidditas`, `Wissenschaft`, `Geist`, `Geisteswissenschaften`. These stayed unsettled through the full 149-part run. Open status is not pending work; it is a recorded judgment that English equivalents would falsify the term.

Vol. 1's glossary is also overwhelmingly Renaissance-vocabulary: `docta ignorantia`, `conjectura`, `similitudo`, `assimilatio`, `complicatio`, `explicatio`, `coincidentia oppositorum`, `non aliud`, `scientia infinita`, `Ars oppositorum`, `perennis philosophia`. Most of this does not transfer to Vol. 2. Bacon's `prerogativae instantiarum`, `experientia literata`; Hobbes's `ratiocinatio`; Spinoza's `attributum`, `conatus`; Leibniz's `vis viva`, `perceptio`, `petites perceptions`; Wolff's distinctions; Newton's `vis insita` — these are the Vol. 2 candidate field. Different vocabulary, similar discipline.

Vol. 2 implication: start with an empty glossary. Pressure-led promotions are local. A smaller Vol. 2 glossary carried by Vol. 2 chain files (if any earn them) is not a less complete apparatus; it is the same discipline applied to different material.

## 5. The tranche-summary paragraph is the sharpest prose surface

Each part file opens with a short prose paragraph *before* `## Scope`. It is written by the translator, not by Cassirer, and it states what the tranche shows. Part 78's opener: "Cassirer now makes the correction to Bruno's minimum-doctrine explicit. Once `Minimum` and `Grenze` are no longer treated as the same kind of quantity, a higher and purer category of quantity has to be admitted…" Part 90's opener: "Cassirer now gives the Kepler force-line its methodological center. Cause no longer means an inner driver hidden behind motion, but a system of mathematically determinable conditions."

The whole-run scratch note calls these "often the sharpest prose in the project because they name pressure without pretending to settle it." Primary reading confirms this. The form is short (3–5 sentences), names the argumentative action, and stops. It is neither summary nor gloss — it diagnoses what the tranche permits or blocks.

Vol. 2 implication: keep this opening paragraph as a deliberate surface. Write it *after* the translation is drafted, not before, because it is supposed to record what the tranche actually showed. Resist the urge to write it as a preview; that turns it into a planning artifact rather than a finding.

## 6. Closure changes the journal's job

The journal-second-pass note records five regimes the journal moved through (startup protocol → tranche discovery → apparatus-mutation → high-frequency pressure → post-completion repair). The completion entry does not end the journal; it changes its job. After completion the journal stops recording forward discovery and starts tracking "honest repair boundary," English/German quality zones, and audit synchronization.

The April 8 burst of dated `reading/` notes (six files in one day, four of them named `earned-distillation-from-X.md`) is the post-completion regime visible as filename density. That form *worked* once or twice for genuinely earned synthesis (the volume-I distillation; the Ferrari/Gonzalez-Rios contact) but multiplied into a template. The four-surprises note (2026-04-10) deliberately did not use the form; that is the correct corrective.

The `"What this tranche clarified / Decision for now"` journal form, by contrast, did not groove. It carried the work for 149 parts because its template was at the right scale: a header pattern, not a content pattern. Every entry's clarified-and-decided content was shaped by its tranche.

Vol. 2 implication: the tranche-and-decision journal form transfers cleanly. The dated `reading/` note pattern should be earned individually and named for its content, not generated from a default template. If Vol. 2 ever produces a closure-distillation, model it on the four-surprises note, not on the earned-distillation series.

## 7. Cassirer wrote Vol. 2's scope in the 1906 preface

Part 01 contains Cassirer's own statement of Vol. 2's plan, in the 1906 preface (line 41 of the part file): "The second volume will begin with English empiricism and then trace, in a twofold direction, the development of idealism from Leibniz onward and the progress of natural science from Newton onward; both streams unite in critical philosophy, with whose exposition the work is to reach its conclusion."

The 1910 preface adds that the Gassendi section was substantially reworked in Vol. 2. This pre-figures one early Vol. 2 stretch as a deliberately revised Cassirer rather than a first-pass exposition.

Vol. 2 implication: scope is author-given. The volume covers Bacon and English empiricism, then idealism (Leibniz, Wolff) running alongside natural science (Newton), converging in Kant. The Vol. 2 README's scope statement aligns with this. Do not redesign scope; track Cassirer's own twofold-then-converging plan.

## What this note is not

- not a Vol. 2 plan
- not a comprehensive Vol. 1 retrospective (the April 8 distillation, the whole-run scratch note, and the four-surprises note serve those purposes at different scales)
- not a substitute for the prescriptions in `texts/erkenntnisproblem-vol2/README.md` or `texts/erkenntnisproblem-vol2/review-checklist.md`; this is their source-side anchor

## Use rule

Use this note when:

- a Vol. 2 setup decision needs justification from Vol. 1 evidence rather than from Vol. 1 prescription
- the Vol. 2 scaffold is being edited and the original rationale for a restraint needs to be visible
- a future agent (human or LLM) is tempted to import a Vol. 1 surface wholesale and needs to see why each was earned locally

Do not use this note when:

- writing a Vol. 1 high-level synthesis (use the April 8 distillation instead)
- the question is what Vol. 1 established philosophically (use the four-surprises note and the close-reading ledger)
- working forward in Vol. 2 translation (use Vol. 2's own surfaces and the README's working method)
