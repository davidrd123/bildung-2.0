# Right Now

Last updated: 2026-04-09 (late)

## Proven

- The repo has a usable layer split: `patterns/charter.md` states purpose, `00-Notes/process.md` states workflow, `patterns/handle-schema.md` states reference grammar.
- The handle/evidence/thread pilot is real in `texts/zeitmauer/source/handles.yaml` through `§§1-186` (the full book). Evidence chains for `term:schicksalszeit`, `term:hinzutretende`, `term:da-sein-so-sein`, `term:weltplan`, and `term:erdgeschichtlich` are machine-readable. `thread:time-crisis` and `thread:predecided-world` now have workable traversals, and `zeitmauer` remains the strongest canonical implementation of the handle layer.
- Zeitmauer is now a completed translation run: 59 parts through §186, the end of the book. Second-pass reread memo for the closing section (Urgrund und Person) confirms the unit is reread-stable. Commentary probe (Schöttker, Koslowski) confirmed rather than revised.
- Symbiotic-Vault interoperability is concrete at the handle layer through loose-coupled `vault:*` and `b2:*` references.
- The architecture designed for three subprojects is now silently supporting five, plus two completed bounded source campaigns and a modern-sources directory. The layer split, journals, and glossaries are carrying the load without needing more ontology.
- CLAUDE.md guardrails are in place, broadcasting the Goethe/Leibniz balance, deferred structure, evidence-before-framework, and opacity-not-foreignness principles to every agent session.
- The practice queue has been reframed from "translation" to "source encounter and decryption" — governing problem is opacity, not foreignness.
- Erkenntnisproblem Volume I is now a completed, source-backed node: 149 parts through printed page 601, with an earned distillation, whole-run scratch note, close-reading ledger, glossary (49 entries), session ledger, and a cross-project review batch (Tasks 01-04). The completed run gives the repo a trustworthy local authority surface for Cassirer's historical epistemology of lawful cognition.
- A Cassirer-pressure note for Zeitmauer is now filed at `texts/zeitmauer/threads/cassirer-pressure-on-zeitmauer.md`, giving four operational constraints and honest negatives for cross-project use.
- The Uexküll source campaign is complete (5 encounters) with a 02b candidate (3 undrafted passages from pp. 102-103) filed but not yet reviewed.
- A qmd retrieval experiment confirmed that BM25 over authority-separated collections works for repo-native queries. Retrieval roadmap and eval seed are filed.
- The source-role taxonomy (primary / source-language commentary / continued primary work / thinker-on-thinker) is in living-layer use as a reading filter, with provisional source-role tags for the April 6 DeepResearch batch.

## Current

- **Erkenntnisproblem** Volume I is complete. 149 parts, the English layer repaired, the review apparatus filed. The next legitimate moves are: bounded late German repair (Parts 142-149), opening Volume II, or bounded cross-volume synthesis. No further forward translation inside Volume I.
- **Zeitmauer** is now complete: 59 parts through §186, the end of the book. Handle pilot through the full text, 5 thread dossiers, Cassirer-pressure note, second-pass reread memo for the closing arc. The next legitimate moves are: bounded review/repair, a whole-book integration pass, cross-project synthesis, or rest.
- **Tektologiya** has 27 part files on disk: the first pass through volume-1 main text is complete through `1.1-5.4`, the selective front-matter pass is complete through `front.10`, and the glossary carries a compact stable core of organizational vocabulary. Its next value is likely demand-led, not linear.
- **Escolios I** remains in selective second-pass mode: 17 section files, minimal handle layer, load-bearing reread bias.
- **Escolios II** has 51 section files on disk. The Spanish extraction has stabilized for honest batching.
- **Exegesis** first pass complete at 75 passes, second-pass knot syntheses underway.
- **Sources**: Uexküll complete, Anders Band I complete, modern-source shelf active but demand-led. Acquisition list filed with tiered priorities.

## Next

- Both major German translation lines are now complete (Erkenntnisproblem Vol. I, Zeitmauer). The project's primary-work center has shifted.
- Active forward translation continues in Escolios II (steady batching) and potentially Tektologiya (demand-led).
- Decide what "next" means for two completed volumes: whole-book integration? Cross-project synthesis? Open Erkenntnisproblem Vol. II? Or let both rest while the other subprojects catch up?
- Keep crystallizing only what the work forces.

## Live Question

- Two completed volumes now sit side by side. Is there a cross-volume integration pass that's earned, or should they stay independent nodes?
- The source-role commentary test (read Schöttker or Ferrari before next return) has now been partly run on the Zeitmauer side (Schöttker/Koslowski probe during the Urgrund und Person reread). What did it teach?
- The glossary audit flagged five missed promotions (Relation, Unendliches, Kraft, Gesetz, Potenz) and one homeless pattern (reification) in erk. Zeitmauer's glossary was never audited at the same level. Should it be?
- What does Tektologiya need to earn its next move? Is it still demand-led, or has the completion of two other volumes changed the demand?

## Do Not Do Yet

- Do not build a dashboard.
- Do not merge ontologies with Symbiotic-Vault.
- Do not build the dynamic view layer before handle practice stabilizes beyond one strong pilot.
- Do not promote anything to `stable` on agent fluency alone.
- Do not let reserve vocabulary quietly pre-earn a framework.
- Do not open Volume II as an escape from late Volume I repair if the Bayle tail still needs German density work.
- Do not launch a cross-volume Cassirer-Jünger synthesis before each volume has its own honest integration pass.
- Do not expand the retrieval stack (BGE-M3, ColBERT, reranking) before the BM25 baseline has a proper evaluation set.
