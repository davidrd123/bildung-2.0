# Journal

## 2026-05-13 - Vol. 2 Preflight Opened

Vol. 2 source assets are now local under `source/pdf/` and `source/page-images/jp2/`, both gitignored. The PDF has an extractable text layer, so the first workflow should reuse the Vol. 1 `pdftotext` path before introducing OCR.

What this setup clarified:

- the Vol. 1 apparatus should be carried forward by role, not copied wholesale
- the first Vol. 2 task is page/source calibration, not interpretation
- the strongest Vol. 1 lesson is the need to track quality zones before a long forward run drifts in density or translation standard
- Vol. 2 begins immediately after the Vol. 1 Bayle/Newton/Voltaire bridge, with Bacon's empirical program as the first test of the completed Vol. 1 line about constructive lawful cognition

Decision for now:

- start with a small Bacon calibration batch
- keep the inherited glossary terms provisional
- build structured chain files only after a Vol. 2 chapter has shown sustained internal movement
- do not activate cross-volume synthesis until at least the Bacon/Gassendi/Hobbes opening arc has its own local notes

## 2026-05-13 - Bacon Opening Begun

Created `parts/001-bacon-opening-and-the-critique-of-understanding.md` from PDF pages `23-26` / printed pages `3-6`. The PDF text layer was corrected against the JP2 page scans for the active tranche; the biggest OCR corrections were joined words, damaged characters, and false readings such as `Schwanke` for `Schranke`, `Naturlelire` for `Naturlehre`, and `Tlineinwandere` for `hineinwandere`.

What this tranche clarified:

- Bacon enters as a change in philosophical affect and posture: nature is no longer primarily the harmonious order that answers reason, but a resisting power to be mastered and made to testify.
- The first contrast is not experience versus speculation in general. It is experiment as lawful mediation between subject and object in Leonardo/Kepler versus experiment as coercive technical procedure in Bacon.
- Bacon's critique of understanding begins negatively: restrict the understanding's creative powers and trace psychological sources of error before identifying any positive ground of truth.

Structural center:

- The load-bearing passage is Cassirer's contrast between Leonardo/Kepler, for whom experiment reveals necessary connections and `Vernunftgründe` in experience, and Bacon, for whom nature must be forced by repeated `Folterungen` to give answer.

Routing decision:

- Keep the new pressures in the part notes and close-reading ledger for now. `Geist/geistig`, `Verstand`, `Experiment`, `Erfahrung`, `Wesenheiten`, `Regnum hominis`, and `Idole` are watchpoints, not glossary entries yet.
- Correct the initial Latin-footnote compression: substantive Latin quotations now receive English translations in the draft-footnote layer; only bibliographic footnotes remain citation-only.
- No thread or Bacon source dossier yet. The `Redargutio philosophiarum` tower/descent image becomes a reading-note candidate only if the next tranches keep returning to it.

Re-entry hooks:

- The tranche ends mid-sentence at `Was er positiv leistet, ist`; the next part should complete the positive side of Bacon's achievement before widening the frame.
- Watch whether `Verstandeskritik` remains psychological-error critique or begins to move toward a more systematic account of objectivity.
- Watch whether `Geist/geistig` stays safely renderable as `mind` / `intellectual` in the Bacon register or begins to need a glossary entry.

Decision for now:

- Continue with the next Bacon tranche from PDF page `27` / printed page `7`.
- Leave `source/glossary.yaml` empty.
- Keep the part format, but treat Part 001 as a correctness calibration rather than evidence that forward speed is safe yet.

## 2026-05-13 - Correctness Gate Before Forward Motion

The first review of Part 001 surfaced the exact failure mode the Vol. 2 setup was meant to prevent: forward motion can quietly compress evidence. The Latin footnote quotations were preserved in the German/source block but initially reduced to source identifications in the English layer. That is now corrected in Part 001.

What this clarified:

- Substantive footnote quotations are part of the source argument, not optional apparatus.
- A deferral can be valid, but only when named and routed; silent compression is not a permissible speed tradeoff.
- Bacon's own warning against unrestrained intellectual flight supplies the right local analogy for the method: restrain the impulse to move forward until the evidential apparatus is sound.

Routing decision:

- Update the checklist and part template so quoted footnotes must be translated unless they are bibliographic-only or explicitly deferred with a hook.
- Do not treat open-ended forward translation as safe until several tranches pass the correctness gate without substantive review corrections.

Decision for now:

- Part 002 can continue only after Part 001's translated footnotes and the updated gate are verified.

Verification result:

- Part 001's substantive Latin footnotes were checked against the Latin. One correction was made: `theologus mente captus` is now rendered as `theologian out of his mind`, matching both the Latin idiom and Cassirer's German `tolle Theologe`.
- Footnotes 2 and 5 were judged adequate for draft status; their remaining awkwardness is literal register rather than a sense error.
- Opus's review caught the structural issues but not this Latin idiom error. That is now part of the method lesson: outside review can widen attention, but source-language verification remains a separate responsibility.
- Part 002 is now ready to begin under the correctness gate.

## 2026-05-13 - Bacon Experience And Method

Created `parts/002-bacon-idols-experience-and-method.md` from PDF pages `27-30` / printed pages `7-10`, ending before `II. Die Formenlehre` begins on printed page `11`. The PDF text layer was again useful but scrambled the page 8 handoff between main text and footnotes; the corrected German was checked against JP2/Tesseract output.

What this tranche clarified:

- Bacon's positive achievement is not the general return to empirical observation, which Cassirer treats as already prepared by Vives, Ramus, Valla, and Francesco Pico.
- The real achievement is the distinction between passive, accidental `Erfahrung` and consciously ordered experiment. Experience becomes scientific only when the empirical and rational faculties become mutually corrective.
- Cassirer is already turning the gain into a problem: if experiment discloses only the rule of empirical recurrence within appearances, Bacon's method will come into tension with Bacon's later physics and metaphysics.

Structural center:

- The load-bearing passage is the double meaning of `Erfahrung`: mere nighttime groping versus the true order of experience that first lights a lamp, then uses it to guide the way toward axioms and new experiments.

Routing decision:

- Keep `Erfahrung`, `Experiment`, `Methode`, `Sinn`, `Empfindung`, `Vorstellungen`, `Geist/geistig`, and `Idole` as watchpoints. `Erfahrung` and `Experiment` now have repeated pressure, but wait for the forms-doctrine transition before creating glossary entries.
- The mirror imagery has now recurred across Part 001 and Part 002. If it recurs again in the forms-doctrine passage, create a bounded Bacon source note rather than a glossary entry.

Re-entry hooks:

- Continue from PDF page `31` / printed page `11`, completing the sentence `Diese Folgerung aber steht...`.
- Watch the method/physics tension: Cassirer is likely to show that Bacon's methodological conception points toward lawful recurrence, while his forms doctrine pulls back toward metaphysical `Wesenheiten`.

Decision for now:

- Part 002 passes the correctness gate for draft status, including substantive Latin footnotes.
- Do not authorize open-ended forward translation yet; one more correctness-gated tranche should test the transition into `II. Die Formenlehre`.

Verification result:

- The check-over caught one source-level German correction: the page scan reads old dative singular `Verstande`, not `Verstände`, in `dem menschlichen Verstande als solchem`.
- The Latin footnotes are adequate for draft status after one local tightening: `certa ratione` now follows Cassirer's `rationelle Methode` as `sure rational method`, not the flatter `sure reason`.
- This confirms the gate is still doing real work. Part 002 can be used as a controlled draft, but it is not yet evidence that open-ended forward translation is safe.

## 2026-05-13 - Bacon Forms And Substantial Induction

Created `parts/003-bacon-forms-and-substantial-induction.md` from PDF pages `31-37` / printed pages `11-17`, stopping after the Harvey/Lord Chancellor judgment. The final paragraph beginning `Wieder aber gilt es...` on printed page `17` is deliberately reserved for Part 004 because it opens the next explanatory movement rather than closing this one.

What this tranche clarified:

- The contradiction opened at the end of Part 002 is now explicit: Bacon's method can discipline sense and understanding, but Bacon's physics asks it to reach absolute forms and self-subsisting qualities.
- Cassirer opposes Descartes and Bacon through the kind of analysis each performs. Descartes moves toward mathematical and physical relation-concepts; Bacon moves toward simple natures, substantial qualities, and forms.
- Baconian induction rests on a finite picture of nature: the phenomena can be surveyed, counted, and exhausted, and facts can be collected before theory determines their form.

Structural center:

- The load-bearing contrast is between modern empirical science, where theory helps determine what counts as a fact, and Bacon's separation of observation from theory, where facts are treated as already available material from which forms can later be distilled.

Routing decision:

- Promote `Erfahrung`, `Experiment`, `Form`, and `Induktion` to open glossary entries. The first two were waiting for this forms-doctrine transition; the latter two now carry the section's central pressure.
- Keep `Tatsache`, `Geschichte der Phänomene`, `Denkart`, and `Wesenheit` as watchpoints. They are important here but should not all be promoted at once.

Re-entry hooks:

- Part 004 should begin on printed page `17` with `Wieder aber gilt es...`, not on printed page `18`, because the page-17 paragraph reframes the defects of Bacon's procedure from the ground-conception of his philosophy.
- Watch whether `Tatsache` recurs as a theoretical problem. If it does, it deserves a glossary entry: Cassirer is already saying a fact is not simply given.
- Watch whether the Baconian "negative instance" becomes a recurring self-reversal, with Bacon's own methodological language turned against Bacon.

Decision for now:

- Part 003 passes the first draft gate, but it should get the same check-over Part 002 received before Part 004 is treated as authorized.
- The glossary is no longer empty, but every entry is `open`; no term has earned a settled preferred rendering beyond local draft use.

Verification result:

- Part 003 needed no source-level German correction after checking the corrected block against the page scans and Tesseract output. The earlier OCR errors (`Schwert`, split `Verhältnisbegriffe`, `Lieb ig`, `läßti`, etc.) are confined to extraction layers, not the corrected part.
- Footnote 3 was tightened: Bacon's list of superinduced simple natures now reads as `yellowness, heaviness, ductility, fixedness, fluidity, solubility`, matching the conceptual list better than the first draft's mixed `yellow, weight...`.
- The English draft was locally smoothed where literalness obscured the claim: `Konstatierung` is now `ascertainment`, and `trägt er es zusammen` is `gathers it from everywhere`.
- Part 003 now counts as a checked draft pass, but still not enough by itself to authorize open-ended speed.

## 2026-05-14 - Bacon Ideas, Idols, And Ground Concepts

Created `parts/004-bacon-ideas-idols-and-ground-concepts.md` from PDF pages `37-41` / printed pages `17-21`, beginning with the paragraph held over from Part 003 and stopping before the `philosophia prima` paragraph on printed page `21`.

What this tranche clarified:

- Cassirer now turns Bacon's idol-critique against Bacon's own form-concept. The form is not a secure divine idea behind things; it is a logical commonality projected outward and treated as an objective source.
- The key pressure is the relation of the `Allgemeine` to the `Besondere`: Bacon claims to reject empty abstractions, but still needs universal simple natures before the particular can be known.
- Bacon's failure is no longer only that he collects facts too loosely. He lacks a scientific rule for defining the simple natures and for grounding physical concepts theoretically.

Structural center:

- The load-bearing passage is the `idola fori` reversal: Bacon's physics falls into the same language-error that his theory of knowledge criticizes, because linguistically separated properties become opposed force-entities in the marrow of things.

Routing decision:

- Add `Idole / Ideen` as an open glossary entry and update `Form` to include the idolic-projection pressure.
- Keep `Allgemeine / Besondere`, `Grundbegriffe`, and `idola fori` as watchpoints for Part 005. They are central here, but Part 005's `philosophia prima` may change the routing.
- Do not promote `Tatsache` yet; it did not recur as the central issue in this tranche.

Re-entry hooks:

- Part 005 should begin on printed page `21` with `Freilich kennt auch Bacon...`, where Cassirer turns to Bacon's `erste Philosophie`.
- Watch whether `philosophia prima` is a genuine alternative route to grounding concepts or another version of the same failure.
- Watch whether `Allgemeine / Besondere` becomes the broader name for the Bacon chapter's problem.

Decision for now:

- Part 004 passes the check-over for controlled draft status. This is another clean correctness-gated tranche, but not yet a reason to switch into open-ended forward motion.

Verification result:

- No source-level German correction was needed after checking PDF text and scan/Tesseract surfaces for the active pages.
- The awkward source phrase `nach der Form ... fragen` was left un-emended; the English renders its sense as `inquire into`.
- The pass tightened English and Latin-facing choices around `Sinn`, `wenn anders`, `Kräftewesen`, `natura naturans`, and Latin `Rari`.
- A follow-up review added three nonblocking refinements: `Selbsttätigkeit` now renders as `self-activity`, the `Formbegriff` idol sentence keeps the German emphasis, and the `works` / `creatures` variation is marked as a source-layer difference.

## 2026-05-14 - Bacon Philosophia Prima And Rhetorical Generality

Created `parts/005-bacon-philosophia-prima-and-rhetorical-generality.md` from PDF pages `41-44` / printed pages `21-24`, beginning with `Freilich kennt auch Bacon...` and stopping before Bacon's definition of physics begins at `Deutlich tritt diese Stellung...`.

What this tranche clarified:

- Bacon's `philosophia prima` is not a successful alternate route around the forms problem. It names a universal foundational science, but the execution reduces it to a loose sequence of analogies and cross-disciplinary maxims.
- The pressure from Part 004 on `Allgemeine / Besondere` continues, but it now takes a sharper form: because thing-like qualities already occupy the place of the universal, general truths and axioms lose their theoretical function and wither into rhetorical commonplaces.
- Cassirer preserves the double judgment on Bacon. Bacon is genuinely the herald of the new valuation of physical and empirical being, but he cannot reach the mastery of the particular because he lacks the conceptual instruments of the new science.

Structural center:

- The load-bearing sentence is: `Der Platz, der dem "Allgemeinen" im Ganzen der Erkenntnis zukommt, ist durch die dinglichen "Qualitäten" ausgefüllt.` This explains why Bacon's first philosophy can only collect analogies rather than ground concepts.

Routing decision:

- Do not add a new glossary entry yet. `Allgemeine / Besondere`, `Grundbegriffe`, and `philosophia prima` are stronger ledger watchpoints, but Part 005 mainly deepens the already-open `Form` problem.
- Keep `Tatsache` in the ledger. It recurs in a Bacon example about contagious disease, not as the fact/theory issue from Part 003.
- The self-reversal pattern is now stronger: Part 003's `negative Instanz`, Part 004's `idola fori`, and Part 005's failed `philosophia prima` all show Cassirer testing Bacon by Bacon's own stated ideals.

Re-entry hooks:

- Part 006 should begin on printed page `24` with `Deutlich tritt diese Stellung...`, where Cassirer turns to Bacon's definition of physics.
- Watch whether Bacon's motion theory produces a third or fourth instance of the self-reversal pattern; if it does, create a bounded reading note rather than a glossary entry.
- Watch whether `Bewegung` becomes the next term-pressure center.

Decision for now:

- Part 005 passes the check-over for controlled draft status. It is now another clean correctness-gated tranche, but I would still define the reusable `/goal` workflow before authorizing open-ended forward motion.

Verification result:

- No word-level German correction was needed after checking PDF text and scan/Tesseract surfaces for the active pages.
- The boundary was confirmed: Part 005 stops before `Deutlich tritt diese Stellung...`, where Bacon's physics definition starts.
- A follow-up scan check of `_0043` corrected the paragraphing: `Und dennoch...` continues the Macaulay paragraph, while the break before `So zeigt...` is a real indented paragraph break.
- The pass tightened English and Latin-facing choices around `Ausführung`, `Geltung`, `tätiges Wesen`, `lustvoll berührt`, `Besonderung`, and Latin `condimus`, and restored Macaulay's original English phrase in the main text.

## 2026-05-14 - Bacon Physics, Astronomy, And Motion

Created `parts/006-bacon-physics-astronomy-and-motion.md` from PDF pages `44-48` / printed pages `24-28`, beginning with Bacon's definition of physics and closing the Bacon chapter before `Zweites Kapitel. Gassendi`.

What this tranche clarified:

- Bacon's physics appears to take the needed step from static being to becoming, but his concept of motion remains an inward qualitative property of things.
- The decisive issue in Bacon's astronomy is not simply his rejection of the Copernican world-system. It is his judgment of modern astronomy's method: he wants living physical grounds but seeks them in the appetites and passions of moved subjects.
- The chapter-closing Atalanta comparison makes the Bacon self-reversal pattern explicit. Bacon himself warns that light-bringing experiments must precede fruit-bearing ones, yet Cassirer says Bacon reached for the fruits of experience before winning the principles that could shape experience scientifically.

Structural center:

- The load-bearing contrast is between motion as living process or appetite and motion as `Ortsveränderung`. Bacon names motion as the real object of physics but cannot make the mathematical move that would turn this claim into mechanics.

Routing decision:

- Add `Bewegung` as an open glossary entry. It links Part 003's falling-motion contrast with the chapter-closing analysis of Bacon's physics and astronomy.
- Create `reading/2026-05-14-bacon-self-reversal-pattern.md` as a bounded Bacon note. The pattern is now earned for this chapter, but not yet generalized to the whole volume.
- Keep `Form`, `Erfahrung`, and `Experiment` open. Part 006 deepens all three but does not settle them.

Re-entry hooks:

- Part 007 should begin on PDF page `49` / printed page `29`, the opening of `Zweites Kapitel. Gassendi`.
- At the Gassendi boundary, test whether `Bewegung` remains a Bacon-local problem or becomes a cross-chapter empiricism problem.
- Watch whether Cassirer reads Gassendi by Gassendi's own internal standards, as he did Bacon, or shifts to a different comparative mode.
- Watch whether the Bacon chapter's repeated structural-center shape hardens into a template. Bacon repeatedly produced split structures; Gassendi should be allowed to produce a different center if the material demands it.

What to expect next:

- The Gassendi opening explicitly denies that Bacon is the real ground of modern empiricism and shifts the origin to Gassendi and Hobbes, who are more inwardly familiar with exact research. This should test whether empirical and corpuscular method can separate itself more cleanly from Bacon's substantial and anthropomorphic physics, or whether early empiricism remains bound to older explanatory forms in a different register.

Decision for now:

- Part 006 can be treated as a checked controlled draft. Do not make subagent review mandatory in the future `/goal`; keep the self-review gate mandatory and use subagents only for targeted escalation.

Verification result:

- Part 006 passes the self-review gate for controlled draft status. The check-over found no word-level German correction after PDF and scan/Tesseract comparison.
- The paragraphing audit found one real source adjustment: `_0046` confirms the paragraph break before `Es ist vor allem die Astronomie...`, but `_0047` shows no new paragraph before `Wer in dieser Fragestellung...`; the part now follows the scan.
- The external-pressure review was useful as a check but too slow to make a subagent mandatory for the `/goal` workflow. The default should be the translating agent's own source-facing review pass; subagents are reserved for targeted escalation.
- The pass tightened the greater/lesser congregation sentence, the Latin `comminisci` rendering, and the Gassendi boundary expectation.
- A follow-up review added two boundary watchpoints rather than corrections: do not force Gassendi into Bacon's split-pattern structural center, and do not let the four-section reading-note form become a default template unless a future note earns that shape.

## 2026-05-14 - Gassendi Opening And Perceptual Mediation

Created `parts/007-gassendi-opening-and-perception.md` from PDF pages `49-53` / printed pages `29-33 partial`, beginning with `Zweites Kapitel. Gassendi` and stopping before `Wenn somit Gassendi die Epikureische Lehre...`.

What this tranche clarified:

- Cassirer explicitly displaces Bacon from the origin of modern empiricism. The new starting point is the `Erfahrungsbegriff der neueren Physik`, carried by thinkers inwardly familiar with exact research.
- Gassendi's unity is not systematic derivation from one principle. It is the goal of taking the new scientific material philosophically into possession by drawing on atomism, Aristotle, scholastic psychology, and Italian natural philosophy.
- The first perception passage translates Epicurean material images into mediated motion-signs: the object does not enter the mind as matter, but affects an external medium and the nerves; mind reconstructs the acting cause from this sign.

Structural center:

- The load-bearing movement is Gassendi's attempt to make inherited philosophical materials usable for mathematical physics. The center is not a Bacon-style split but a mediated appropriation: `philosophisch in Besitz nehmen` becomes perception as motion-sign rather than direct material intake.

Routing decision:

- Update `Erfahrung`, `Bewegung`, and `Idole / Ideen` only as cross-boundary qualifications in the glossary. `Erfahrung` now points beyond Bacon toward modern physics; `Bewegung` recurs as local motion and motion-state; Gassendi's `Idola seu Simulacra` must not be collapsed into Bacon's `Idole / Ideen`.
- Keep `Sinn`, `Wahrnehmung`, `Empfindung`, `Erfahrungserkenntnis`, and `eigene Tätigkeit` in the close-reading ledger for now. They are active in this tranche, but the next page tests whether they become epistemological terms rather than psychological setup.
- No new reading note. The material forced a chapter-boundary reorientation, not a bounded synthesis yet.

Re-entry hooks:

- Part 008 should begin on printed page `33` / PDF page `53` with `Wenn somit Gassendi die Epikureische Lehre...`.
- Watch whether `Sinn` remains merely the psychological source of assurance or becomes the criterion of truth in the doctrine of unerring perception.
- Watch whether Gassendi's `eigene Tätigkeit` of mind becomes a pressure point against his sensualism when the chapter moves toward judgment, Descartes, and self-consciousness.

Decision for now:

- Part 007 passes the self-review gate for controlled draft status. Continue to Part 008 under the same source-facing review discipline.

Verification result:

- The source-facing review checked PDF pages `49-53` against scan/Tesseract output. The active boundary was corrected to include the sentence and source note at the top of PDF page `53`, then stop before the next paragraph.
- The review restored one source-layer punctuation item in the German block: the closing quotation mark after the `Idola seu Simulacra` citation.
- The long Latin footnote on sensation, sensible species, motion, and the impressed mark is translated in the draft-footnote layer. The other footnotes are bibliographic or source references only.
- No subagent was used; this was the translating agent's own mandatory review pass.

## 2026-05-14 - Gassendi Sense-Truth, Judgment, And Atomism

Created `parts/008-gassendi-sense-truth-judgment-and-atomism.md` from PDF pages `53-56` / printed pages `33-36 partial`, beginning with `Wenn somit Gassendi die Epikureische Lehre...` and stopping before `Schärfer noch tritt dieser Widerstreit...`.

What this tranche clarified:

- Gassendi preserves the Epicurean consequence even after modifying the perceptual mechanism: sense-perception is unerring because it always reports a real effect.
- Error belongs to the `Urteil des Verstandes`, which transfers a situated feature of the perceptual image to the object as a lasting property `an sich`.
- This criterion immediately becomes a problem for Gassendi's own physics. Atomism and mathematical physics require concepts generated by scientific reason against naive sensory intuition.

Structural center:

- The load-bearing movement is from sensory infallibility to theoretical insufficiency. Perception is the object that thought must satisfy, but not the origin or principle from which genuine knowledge springs.

Routing decision:

- Add `Sinn / Sinneswahrnehmung` as an open glossary entry. It has now moved from Part 007's foundation of knowledge to Part 008's criterion of unerring sensory truth, while also showing its own limit.
- Keep `Urteil`, `Verstand`, `Vernunftgrund`, `wissenschaftliche Vernunft`, `Geltung`, `Atombegriff`, and `Anschauung` in the ledger. The next space/time movement should show which of these persist.
- Do not create a bounded reading note yet. The contradiction is chapter-structural, but its full form likely emerges through the Raum/Zeit section rather than within the perception passage alone.

Re-entry hooks:

- Part 009 should begin on printed page `36` / PDF page `56` with `Schärfer noch tritt dieser Widerstreit...`.
- Watch whether `Raum` and `Zeit` become the next examples of concepts scientific reason requires against Gassendi's sensory criterion.
- Watch whether `Atombegriff` remains a transition term or becomes the organizing pressure for the next section.

Decision for now:

- Part 008 passes the self-review gate for controlled draft status. Continue to Part 009 without easing the source-facing review discipline.

Verification result:

- PDF pages `53-56` were checked against scan/Tesseract output. The boundary was confirmed: the paragraph beginning `Schärfer noch...` is visibly indented on scan `_0056` and belongs to the next part.
- The review restored source punctuation after `beilegen`, corrected the OCR-damaged long Latin footnote, and translated that footnote in the draft-footnote layer.
- The raw and normalized extracts include extra page-56 material for Part 009 because the active boundary falls mid-page; the corrected Part 008 text deliberately stops before that paragraph.
- No subagent was used; this was the translating agent's own mandatory review pass.

## 2026-05-14 - Gassendi Space, Time, And Objective Validity

Created `parts/009-gassendi-space-time-and-objective-validity.md` from PDF pages `56-59` / printed pages `36-39 partial`, beginning with `Schärfer noch tritt dieser Widerstreit...` and stopping before `Die spezielle Durchführung von Gassendis Physik...`.

What this tranche clarified:

- Gassendi grasps pure space and pure time as true entities that are independent of bodies and of thinking subjects, yet are not substances or accidents.
- The objectivity of space and time lies in the unconditional necessity with which they must be thought, not in any analogy to the reality of physical things and their properties.
- This forces the epistemological problem Part 008 opened: if sense is the only witness of reality, then pure space and pure time should not count as knowable because they do not act on the organs of sense-perception.

Structural center:

- Objective validity has to be extended beyond perceptual content to concepts indispensable for thinking experience as a necessarily connected whole. Gassendi brings the need for another grounding into view but cannot supply it from his own sensualism.

Routing decision:

- Add `Raum / Zeit` as an open glossary entry and update `Sinn / Sinneswahrnehmung` with the Part 009 limit.
- Keep `objektive Gültigkeit`, `reine Relationen`, `Notwendigkeit`, `Wirklichkeit`, and `Wesenheiten` in the ledger. The next part should test whether these are local to space/time or general to Gassendi's physics.
- No bounded reading note yet. The problem is now clearly chapter-structural, but Part 010 should show whether the same pattern governs motion and special physics.

Re-entry hooks:

- Part 010 should begin on printed page `39` / PDF page `59` with `Die spezielle Durchführung von Gassendis Physik...`.
- Watch whether `Raum / Zeit` remains the local example of non-sensory objective validity or whether motion theory generalizes the same problem.
- Watch whether the emerging positive name for the alternative grounding is `reine Relationen`, `objektive Gültigkeit`, or mathematical `Naturerkenntnis`.

Decision for now:

- Part 009 passes the self-review gate for controlled draft status. Continue to Part 010 under the same review discipline.

Verification result:

- PDF pages `56-59` were checked against scan/Tesseract output. The source boundary was narrowed from the initial `56-61` extract after review showed that `Die spezielle Durchführung...` begins a new paragraph on scan `_0059`.
- The review corrected OCR residue in the Latin footnotes and restored the page-59 phrase `zuzusprechen, sondern ... zu`.
- Footnotes 1 and 2 are translated because they carry historical argument about Campanella, Riehl, Newton, Locke, and Gassendi; footnotes 3 and 4 translate the substantive Latin.
- No subagent was used; this was the translating agent's own mandatory review pass.

## 2026-05-14 - Gassendi Physics, Motion, And Atomistic Explanation

Created `parts/010-gassendi-physics-motion-and-atomistic-explanation.md` from PDF pages `59-61` / printed pages `39-41 partial`, beginning with `Die spezielle Durchführung von Gassendis Physik...` and stopping before `Wenn indessen die Ausführung der Physik...`.

What this tranche clarified:

- Gassendi's special physics confirms the same pattern as the space/time passage: it is permeated by rational assumptions his epistemology cannot strictly admit.
- The sensory appearance of continuous bodies cannot be the final standard. Reason and science replace it with discrete elementary parts.
- The same atomistic decomposition extends to motion itself. Continuous motion becomes a sensory appearance; different speeds are explained through different mixtures of motion and rest.

Structural center:

- The load-bearing point is not whether Gassendi's physics is physically correct. Cassirer's point is that it consciously transforms perceptual data by conceptual criteria in order to think them as a contradictionless whole.

Routing decision:

- Add `Atombegriff / Atomistik` as an open glossary entry.
- Update `Bewegung` and `Raum / Zeit` with the Part 010 pressure: Gassendi's motion is neither Baconian appetite nor modern continuous kinematics, but atomistic passage through simple space-points and time-moments.
- Keep `Stetigkeit`, `Ruhe`, `begriffliche Kriterien`, `rationale Grundannahmen`, and `widerspruchsloses Ganze` in the ledger. A bounded Gassendi reading note is now plausible but should wait for the Descartes/psychology close.

Re-entry hooks:

- Part 011 should begin on printed page `41` / PDF page `61` with `Wenn indessen die Ausführung der Physik...`.
- Watch whether the Descartes comparison converts the Gassendi problem from physics into psychology and self-consciousness.
- Watch whether `eingeborene Begriffe`, `Geist`, `Empfindung`, and `wissenschaftliches Sein` need glossary or ledger treatment at chapter close.

Decision for now:

- Part 010 passes the self-review gate for controlled draft status. Continue to the chapter-closing Part 011 under the same review discipline.

Verification result:

- PDF pages `59-61` were checked against scan/Tesseract output. The boundary was confirmed: scan `_0061` shows the motion paragraph closed by a dash before the psychology/Descartes paragraph begins.
- The review corrected OCR residue around `Erscheinung`, `Ruhepausen`, `Raum`, `Raumpunkt`, `verschiedene`, `in Wahrheit`, and punctuation around `deutlich, daß`.
- The only footnote is bibliographic/source-reference only, so no source-language quotation translation was needed.
- No subagent was used; this was the translating agent's own mandatory review pass.

## 2026-05-14 - Gassendi Psychology, Self-Consciousness, And Descartes

Created `parts/011-gassendi-psychology-self-consciousness-and-descartes.md` from PDF pages `61-65` / printed pages `41-45`, beginning with `Wenn indessen die Ausführung der Physik...` and closing the Gassendi chapter before `Drittes Kapitel. Hobbes`.

What this tranche clarified:

- The chapter's physics problem returns inside psychology. Gassendi can criticize the form of Cartesian proof, but he misses the methodological principle by which scientific being is worked out in thought.
- His theory cannot explain the active formation and expansion of sensory data. It knows consciousness only as reaction to an external stimulus, not as original and creative activity.
- Experience becomes the ground-riddle: it is supposed to explain knowledge, but it itself means the transition of an absolute external object into an equally independent `Ich`.

Structural center:

- The fact of self-consciousness is the chapter's closing test. It cannot be treated as a derivative result because it is the beginning and condition of all objective knowledge.

Routing decision:

- Add `Selbstbewußtsein / Ich / innere Erfahrung` as an open glossary entry.
- Update `Erfahrung` and `Sinn / Sinneswahrnehmung` with the chapter-close pressure.
- Keep `Geist`, `eingeborene Begriffe`, `Urteil`, `Bewußtsein`, `Antizipationen des Geistes`, and `Bildertheorie` in the ledger rather than opening more glossary entries at the close.
- Create `reading/2026-05-14-gassendi-experience-as-ground-riddle.md` as a bounded chapter note.

Re-entry hooks:

- The next chapter begins on printed page `46` / PDF page `66` with `Drittes Kapitel. Hobbes.`
- At the Hobbes opening, test whether the relation between object, sensation, and thought is reformulated as a logical, mechanical, or political problem.
- Do not carry the Gassendi bounded note forward as a template; use it as chapter-local calibration for what Hobbes changes.

Decision for now:

- Part 011 passes the self-review gate for controlled draft status and closes the Gassendi chapter.
- Run a completion audit for the active Gassendi `/goal` before marking it complete.

Verification result:

- PDF pages `61-65` were checked against scan/Tesseract output. PDF page `65` closes the Gassendi chapter; PDF page `66` opens Hobbes.
- The review corrected OCR residue around `wissenschaftlichen Sein`, `anfänglichen`, `Gegenstandes`, `quidquam`, `incurrit`, `eindringt`, `Selbstbewußtsein`, `inneren Erfahrung`, and `der scholastischen Seelenlehre`.
- Substantive Latin footnotes 1, 3, and 4 are translated in the draft-footnote layer; footnotes 2 and 5 remain source/bibliographic references.
- No subagent was used; this was the translating agent's own mandatory review pass.

## 2026-05-14 - Gassendi Gate Calibration After Burst Run

The post-run reviews disagreed less about the text than about status. The Gassendi work is strong as draft, but the run did shift from the paced Bacon pattern into a five-tranche `/goal` burst. That shift should not be hidden by the phrase `passes the self-review gate`.

What this clarified:

- The Gassendi parts should be treated as `self-reviewed controlled drafts`, not automatically as identical in authority to Bacon parts that received iterative external pressure during drafting.
- The content-level checks are reassuring: Opus spot-checks found the OCR corrections, Latin translations, and English drafts competent, and the structural-center pattern did not groove on Bacon.
- Status language matters. A translating agent's own review is mandatory and useful, but it is not the same topology as a later pressure read.

Probe review:

- Ran a focused Part 011 probe because it is the chapter close and carries the hardest conceptual and Latin load.
- JP2/Tesseract spot-checks confirmed the claimed paragraph boundaries: `_0056` has a real break before `Schärfer noch...`, and `_0061` has a break after the dash before `Wenn indessen...`.
- Part 011's German, long Latin notes, and chapter-close reading were checked again against the normalized source and scan/Tesseract output. No correction was needed.

Routing decision:

- Keep Gassendi Parts 007-011 at `controlled draft` status, with Part 011 additionally `probe-reviewed`.
- Do not commit the burst merely because the `/goal` completed; commit-readiness requires either this recorded calibration plus user acceptance, or fuller second-pass review of the remaining Gassendi tranches.
- For future open-ended goals, keep self-review mandatory but add a chapter-level ratification step before status elevation.

Decision for now:

- Hobbes can begin from a position of trust in the apparatus, but not with unlimited speed. The next chapter should use the same self-review gate plus a planned chapter-boundary probe before any commit/status promotion.

## 2026-05-14 - Hobbes Opening And Definition Of Knowledge

Created `parts/012-hobbes-opening-definition-of-knowledge.md` from PDF pages `66-68` / printed pages `46-48 partial`, beginning with `Drittes Kapitel. Hobbes.` and stopping before `Es ist Hobbes' eigentümliche und originale Leistung...`.

What this tranche clarified:

- Hobbes is introduced as the next measure of the philosophical reception of exact physics. The comparison is explicitly among Bacon's, Gassendi's, and Hobbes's `Erfahrungsbegriff`.
- Hobbes still begins from Bacon's thesis that true knowledge is knowledge from causes, but the thesis changes internally once cause is understood in the Galilean sense.
- The decisive shift is from cause as inner force, substantial form, or essence to cause as a complete aggregate of conditions whose positing makes the effect necessary.

Structural center:

- The load-bearing movement is the passage from Bacon to Galileo through Hobbes's redefinition of motion and cause. Motion becomes a constructible mathematical relation; cause becomes conditional necessity within appearances and accidents.

Routing decision:

- Update `Erfahrung` and `Bewegung` in the glossary. Both are already open and the Hobbes opening changes their cross-chapter shape.
- Keep `Ursache / Bedingung`, `Mechanismus`, `Wesenheiten`, and `Formalursachen` in the close-reading ledger for now. The next Hobbes tranche should show whether `Ursache / Bedingung` earns a glossary entry through causal definition, generation, and a priori knowledge.
- No reading note yet. This is a chapter-opening pivot, not a closed Hobbes synthesis.

Re-entry hooks:

- Part 013 should begin on printed page `48` / PDF page `68` with `Es ist Hobbes' eigentümliche und originale Leistung...`.
- Watch whether Hobbes's `Bewegung` becomes the cross-chapter answer to Bacon and Gassendi, or whether the next pressure shifts to deduction, construction, and method.
- Watch whether cause-as-condition becomes stable enough to promote as `Ursache / Bedingung`.

Decision for now:

- Part 012 passes the self-review gate for controlled draft status. Continue one tranche at a time through Hobbes until the new chapter rhythm is clearer.

Verification result:

- PDF pages `66-68` were checked against scan/Tesseract output. The scan OCR misread the Roman `I.` as `E`; the part restores `I.`.
- The review removed Sperrung in names and emphasis words, restored `§ 1-5`, corrected OCR residue around `einfachen Naturen`, `konstruieren`, and `omnibus`, and confirmed that PDF page `68` begins the next paragraph after the Part 012 stop.
- Hobbes's Latin definition of cause is translated in the main draft. The remaining footnotes are bibliographic/source references or cross-references.
- No subagent was used; this was the translating agent's mandatory source-facing review pass after the Gassendi calibration.

## 2026-05-14 - Hobbes Method, Deduction, And Construction

Created `parts/013-hobbes-method-deduction-and-construction.md` from PDF pages `68-75` / printed pages `48-55 partial`, beginning with `Es ist Hobbes' eigentümliche...` and stopping before section `II.` / `Eine zweite nicht minder wichtige Schranke...`.

What this tranche clarified:

- Hobbes's original move is to transfer Galileo's method from physics to the whole of knowledge.
- To understand a content is to generate it from conditions fixed by thought. Geometry is certain because we create its figures; physics must imitate this constructive method analogically by deriving appearances from possible causes.
- The same passage names Hobbes's limit: he sees motion as the bridge between nature and thought, but without the modern analysis of the infinite his logic reduces connection too much to separating, composing, adding, and subtracting.

Structural center:

- The load-bearing movement is constructive generation. Geometry, physics, calculation, concept formation, and body all become knowable only where thought can decompose a whole into parts and build it back up from generated conditions.

Routing decision:

- Add `Ursache / Bedingung / Erzeugung` as an open glossary entry and update `Bewegung`.
- Keep `Deduktion`, `Rechnen`, `Körper`, `Mehr / Weniger`, `Analysis des Unendlichen`, and `conatus` in the ledger. They are active, but Part 014 should show whether they persist beyond section I's method problem.
- No reading note yet. The section has a strong method finding, but the next section may alter it by introducing word, sign, convention, and political analogy.

Re-entry hooks:

- Part 014 should begin on printed page `55` / PDF page `75` with section `II.` and `Eine zweite nicht minder wichtige Schranke...`.
- Watch whether `Rechnen`, `Begriff / Wort`, and sign-construction earn glossary treatment or remain local pressures.
- Watch whether the political motif around will, convention, and sovereignty enters logic structurally rather than as a later application.

Decision for now:

- Part 013 passes the self-review gate for controlled draft status. Continue to Part 014 one tranche at a time.

Verification result:

- PDF pages `68-75` were checked against scan/Tesseract output. Scan `_0075` confirms the boundary: section `II.` begins after the conatus/Wallis paragraph.
- The review corrected OCR residue around `überträgt`, `gewährleistet. Es gibt`, `vor uns entstehen`, `Ideen`, `Verknüpfung`, `intelligitur`, `festumschriebene`, `Beschaffenheiten`, `Das Erkenntnisideal`, `Deduktion`, `Übereinstimmung in der Grundverfassung`, `verständlich`, `Zeitdauer`, and `Frischeisen-Köhler`.
- Substantive Latin footnotes 1, 2, and 4 are translated in the draft-footnote layer. The Hobbes geometry quotation and the `ubi generatio...` formula are translated in the main draft.
- No subagent was used; this was the translating agent's mandatory source-facing review pass.

## 2026-05-14 - Hobbes Concept, Word, And Nominalist Rationalism

Created `parts/014-hobbes-concept-word-and-nominalist-rationalism.md` from PDF pages `75-81` / printed pages `55-61 partial`, beginning with section `II.` / `Eine zweite nicht minder wichtige Schranke...` and stopping before section `III.` / `Es ist ein originaler und fruchtbarer Gedanke...`.

What this tranche clarified:

- Hobbes's sign theory first appears to break the method doctrine: logic seems to dissolve into grammar, truth into names, and necessity into convention.
- Cassirer keeps the contradiction visible, especially the intrusion of Hobbes's sovereign-model into logic.
- The deeper motive is still rationalist. Names and words stabilize judgment, preserve constructed sequences for memory, and let a particular geometrical insight become universally valid.

Structural center:

- The load-bearing movement is from arbitrary sign-convention to rational validity through judgment and mathematics. Word and sign do not simply replace reality; they become the vehicle by which active construction gains repeatability and generality.

Routing decision:

- Add `Begriff / Wort / Zeichen` as an open glossary entry.
- Update `Erfahrung` with Hobbes's sense/memory versus science contrast and update `Ursache / Bedingung / Erzeugung` with the `Willkür` pressure.
- Keep `Nominalismus / Rationalismus`, `Urteil`, `Namengebung`, `Zahlzeichen`, `Souveränität`, and `Tatsachen` in the ledger. They are live pressures, but Part 015 should show whether they persist beyond the logic/language section.

Re-entry hooks:

- Part 015 should begin on printed page `61` / PDF page `81` with section `III.` and `Es ist ein originaler und fruchtbarer Gedanke...`.
- Watch whether Hobbes's destruction-of-the-world thought experiment carries the sign/name problem into nature philosophy or shifts the center back toward space, body, imagination, and motion.
- Watch whether `Begriff / Wort / Zeichen` remains local to section II or becomes a bridge into political and natural-philosophical construction.

Decision for now:

- Part 014 passes the self-review gate for controlled draft status. Continue to section `III.` one tranche at a time.

Verification result:

- PDF pages `75-81` were checked against scan/Tesseract output. Scan `_0075` confirms the section `II.` start after the conatus/Wallis paragraph, and scan `_0081` confirms the stop before section `III.`.
- The review corrected OCR residue around `Arithmetik und Analysis`, `Summenbildung`, `Zeildauer`, `Frischeisen-Köhler`, `Erzeugungen der Natur`, `Konstanz, die wir`, `Entschiedenheit und Deutlichkeit`, `Sprachgebrauch`, `Wahrheit`, `offenen Widerspruch`, `Tönnies`, `demonstrationem`, `hominum`, `Grundsätze preisgeben`, `Gedächtnis wäre`, `Vorstellungen und Namen`, `konkreten`, `Zahlzeichen`, `zu unterwerfen`, `Weiterführung`, `proficiscuntur`, `Leviathan`, `Betrachtung der sinnlich einzelnen Gestalt`, `Seriei`, and `strictioris`.
- Substantive Latin quotations in footnotes 3, 5, and 7 are translated in the draft-footnote layer. The Tönnies German quotation in footnote 2 is also translated because it carries the argument.
- No subagent was used; this was the translating agent's mandatory source-facing review pass.
- A trailing review flagged `veritas in dicto, non in re consistit` as a forward-compatibility point. The draft now renders `dicto` as `what is said` rather than `speech`, and the close-reading ledger records `dicto` as assertion-content for later Leibniz/proposition work.

## 2026-05-14 - Hobbes World-Destruction, Space-Time, And Matter

Created `parts/015-hobbes-world-destruction-space-time-and-matter.md` from PDF pages `81-87` / printed pages `61-67 partial`, beginning with section `III.` / `Es ist ein originaler und fruchtbarer Gedanke...` and stopping before `Der Gegensatz, der hier bestehen bleibt...`.

What this tranche clarified:

- Hobbes's destruction-of-the-world thought experiment is the natural-philosophy form of the constructive method. The finished external world gives thought no starting point, so thought negates it in order to reconstruct it.
- Space and time are introduced as phantasms or products of intellectual activity: space as the representation of externality, time as the phantasm of motion/order, and division as a work of the intellect.
- Body is first a rational postulate, not a sensory datum. But once body has been introduced in this way, Hobbes lets it harden into absolute substance and real motion, reopening the gap between ideal truth and actual reality.

Structural center:

- The load-bearing movement is constructive negation turning into metaphysical hardening. Hobbes makes the world knowable by reconstructing it from thought, but then treats the constructed body as if it were first and absolute.

Routing decision:

- Update `Raum / Zeit` and `Bewegung`.
- Add `Körper / Materie / Substanz` as an open glossary entry.
- Keep `Phantasie / Phantasma`, `Ort / Größe`, `Merkzeichen`, `Naturbegriff`, and `Skepsis` in the ledger until the perception section shows whether they remain structural.

Re-entry hooks:

- Part 016 should begin on printed page `67` / PDF page `87` with `Der Gegensatz, der hier bestehen bleibt...`.
- Watch whether Hobbes's perception theory reproduces the Part 015 pattern: a logically required condition becomes an absolute material source behind phenomena.
- Watch whether `Sinnesempfindung`, `Phänomen`, `Gedächtnis`, and `innere Erfahrung` reopen the Gassendi problem or get transformed by Hobbes's constructive logic.

Decision for now:

- Part 015 passes the self-review gate for controlled draft status. The chapter close is now a focused final tranche.

Verification result:

- PDF pages `81-87` were checked against scan/Tesseract output. Scan `_0081` confirms the section `III.` start and scan `_0087` confirms the stop before the perception-theory paragraph.
- The review corrected OCR residue around `bestehen`, `steht`, `zu erkennen`, `Proposita`, `potest`, `beachten und`, `seu`, `alicujus`, `nec`, `sic`, `existentis`, `praeterquam`, `keine`, `begrenzte`, `Verhältnis zum erkennenden Subjekt`, `lediglich`, `Schlußfolgerung`, `coincidat`, `ut non sensibus`, `ratione tantum`, `genita, sed non res`, `Bewegungslehre`, `zusammen ausdehnt`, `également`, `matériaux`, `détaché`, `géométrique`, and `pensée`.
- Substantive Latin footnotes 1, 2, 3, 4, and 5 are translated in the draft-footnote layer. The French Lyon quotation in footnote 8 is also translated because it carries the critique.
- No subagent was used; this was the translating agent's mandatory source-facing review pass.

## 2026-05-14 - Hobbes Perception, Psychology, And Chapter Close

Created `parts/016-hobbes-perception-psychology-and-self-created-principles.md` from PDF pages `87-90` / printed pages `67-70`, beginning with `Der Gegensatz, der hier bestehen bleibt...` and closing the Hobbes chapter before `Fünftes Buch`.

What this tranche clarified:

- Hobbes's perception theory repeats the reversal from the nature-philosophy section. Sensation is first the `Prinzip der Prinzipien`, because phenomena must be investigated from within phenomena, memory, and inner experience.
- The same sensation is then explained from a thing-like origin behind it: matter pressing on sense organs and producing counter-striving.
- The final chapter diagnosis generalizes the pattern: reason creates principles from itself, then those products detach from their conditions and bind reason as absolute powers.

Structural center:

- The load-bearing movement is self-created principle becoming binding authority. Cassirer ties together Hobbes's political theory, logic, and natural philosophy through this form.

Routing decision:

- Update `Körper / Materie / Substanz`, `Bewegung`, `Sinn / Sinneswahrnehmung`, `Begriff / Wort / Zeichen`, and `Erfahrung`.
- Do not open separate entries for `Phänomen`, `Gedächtnis`, `innere Erfahrung`, `Assoziation`, or `Selbstgesetzgebung der Vernunft`; route them to a bounded Hobbes reading note.
- Create a bounded Hobbes chapter-close note on self-created principles hardening into absolute powers.

Re-entry hooks:

- Before moving into Book V / Spinoza, run chapter-level calibration for Parts 012-016.
- Watch whether Spinoza inherits Hobbes's autonomy problem or transforms it by refusing the split between generated rational order and absolute substance.
- Watch whether `Substanz` must remain tied to Hobbes's body/matter problem or get re-anchored under Spinoza immediately.

Decision for now:

- Part 016 passes the self-review gate for controlled draft status. The Hobbes chapter is drafted through the close, pending chapter-level calibration.

Verification result:

- PDF pages `87-90` were checked against scan/Tesseract output. Scan `_0090` confirms the Hobbes chapter closes before `Fünftes Buch`; scan `_0091` begins the next book divider.
- The review corrected OCR residue around `Beziehungen auf`, `während der Körper`, `bedeuten soll`, `Sinnesempfindung`, `miteinander`, `innerhalb ihrer selbst`, `Phaenomenon`, `principia`, `dicendum est`, `investigationem`, `alio Phaenomeno`, `eam ipsam`, `contemplabimur`, `Eodem ipso`, `sensibilium`, `tamen`, `De Corpore`, `P. IV`, `Elements of law`, `Einwirkung des Dinges`, `Bd. I, S.`, `vgl.`, `gelten`, and `Bedingungen los`.
- The substantive Latin quotation in footnote 1 is translated in the draft-footnote layer. The German note on the `Elements of Law` reversal is translated/summarized because it carries the chapter-close argument.
- No subagent was used; this was the translating agent's mandatory source-facing review pass.

## 2026-05-14 - Hobbes Chapter Calibration Before Spinoza

Calibration scope: Parts `012-016`, from `Drittes Kapitel. Hobbes.` through the close before `Fünftes Buch`.

What this calibration clarified:

- The Hobbes chapter was completed at section-bounded scale, not page-bounded scale. Part 012 remained short because it was a chapter-opening definition; Parts 013-014 follow sections I and II; section III was split into Parts 015-016 because the nature-philosophy and perception/psychology movements are distinct.
- The trailing review confirmed Parts 013-014 as controlled drafts and flagged `veritas in dicto` as a forward-compatibility issue. The draft now renders `dicto` as `what is said`, and the close-reading ledger records it as assertion-content rather than merely speech.
- Boundary checks requested by the trailing review were already covered in the self-review: `_0075` confirms the Part 013/014 section-II boundary, and `_0081` confirms the Part 014/015 section-III boundary.
- Part 015's wide source extract was intentionally narrowed. The source file covers PDF `81-92`, but the part stops at PDF `87` before the perception-theory turn; Part 016 closes the chapter through PDF `90`.
- A trailing Part 015 review flagged two earned additions: Lyon's French quotation is load-bearing because it names the latent idealist consequence of Hobbes's reconstruction, and the world-destruction thought experiment should remain a future Kant/transcendental comparison point. Both are recorded in the close-reading ledger and bounded Hobbes note without promoting them to a cross-volume thesis.
- A trailing Part 016 review confirmed the chapter close and highlighted the restored Greek `τὸ φαίνεσθαι` in Hobbes's De Corpore footnote as a genuine source-facing catch. It also flagged `Urphänomen` and `Selbstgesetzgebung der Vernunft` as later Goethe/Kant-adjacent watchpoints; both remain ledger pressures, not glossary entries.
- This is the first complete book-to-book transition in Vol. 2: Book IV / `Die Anfänge des Empirismus` is now drafted through Bacon, Gassendi, and Hobbes. The Book V divider is on PDF/scan `_0091`; the first Spinoza text page remains the page-map's calculated PDF `93` anchor until visually verified.

Structural finding:

- Hobbes's chapter is organized by self-created principles hardening into absolute powers. Cause becomes constructible condition; method becomes generation; words and signs fix judgment; the external world is negated to be reconstructed; body then hardens into absolute substance; sensation begins as the principle of principles but is explained by matter behind it.

Routing decision:

- Created `reading/2026-05-14-hobbes-self-created-principles.md` as the bounded Hobbes chapter note.
- Keep all Hobbes additions at `open` status: `Ursache / Bedingung / Erzeugung`, `Begriff / Wort / Zeichen`, and `Körper / Materie / Substanz`.
- Do not open separate entries for `Nominalismus / Rationalismus`, `Urteil`, `Phänomen`, `Gedächtnis`, `innere Erfahrung`, `Assoziation`, or `Selbstgesetzgebung der Vernunft`; the chapter note is the right surface for those until Spinoza gives contrast evidence.

What to expect next:

- Book V / Spinoza should test whether Hobbes's autonomy/substance problem is inherited or transformed. If Spinoza refuses the split between generated rational order and absolute substance, Hobbes's pattern stays chapter-local. If the same hardening recurs, it becomes a broader rationalism problem.
- `Substanz` must be watched carefully at the transition. The Hobbes entry ties substance to body/matter and metaphysical hardening; Spinoza may immediately re-anchor it in a different register.
- A later comparison with Cassirer's own `Substanzbegriff und Funktionsbegriff` may become earned if the substance/function contrast continues to organize the rationalism chapters. Do not use that systematic comparison as an interpretive shortcut before the Spinoza and Leibniz material supplies evidence.

Decision for now:

- Hobbes Parts `012-016` have passed translating-agent self-review for controlled draft status. The chapter also has a recorded chapter-level calibration and bounded reading note. Commit/status elevation would still require user acceptance or a later second-pass review, matching the Gassendi calibration rule.

## 2026-05-14 - Spinoza Opening, Intuition, And Pure Passion

Created `parts/017-spinoza-short-treatise-intuition-and-passion.md` from PDF pages `93-96` / printed pages `73-76`, beginning with `Erstes Kapitel. Spinoza.` and stopping before `Für das Verständnis dieser Grundansicht...` on printed page `77`.

What this tranche clarified:

- Book V opens by seeming to break the continuity of the problem of knowledge. Hobbes and Descartes both sought criteria of truth before determining absolute being; early Spinoza begins from infinite being as immediately given.
- The `Short Treatise` reverses the Hobbes chapter-close pattern. Knowledge is not first self-created construction; the object grasps the mind and brings about knowledge in it.
- Experience is placed low in the order of knowledge, as hearsay or acquaintance with individual facts. True belief and clear/distinct knowledge stand above it, with intuition of the universal in the individual as the highest stage.

Structural center:

- The load-bearing movement is the displacement of self-activity by pure passion. `Gottesbewußtsein`, not Cartesian self-consciousness, functions as the basic fact, and the order of being carries the order of knowing.

Routing decision:

- Update `Erfahrung`, `Bewegung`, `Körper / Materie / Substanz`, and `Selbstbewußtsein / Ich / innere Erfahrung`.
- Keep `Intuition / Anschauung`, `reines Leiden`, `Gottesbewußtsein`, `Allnatur`, `wahrer Glaube`, `Wahrheit / Irrtum`, and `Selbsttätigkeit` in the close-reading ledger.
- Do not split `Substanz` from the Hobbes `Körper / Materie / Substanz` entry yet; the explicit Spinoza substance section begins later and should decide the split.

Re-entry hooks:

- Part 018 should begin on printed page `77` / PDF page `97` with `Für das Verständnis dieser Grundansicht...`.
- Watch whether Cassirer's historical comparison with Descartes, mysticism, Bruno, Telesio, and Campanella makes `Intuition / Anschauung` glossary-worthy.
- Watch whether Spinoza's passivity is a local `Short Treatise` stage or the first step in rationalism's completion.
- Watch whether the Hobbes note's next-test resolves as refusal, transformation, or inheritance of the autonomy/substance problem.

Decision for now:

- Part 017 passes the self-review gate for controlled draft status. Continue to Part 018 before opening any new Spinoza glossary entry.

Verification result:

- PDF pages `91-96` were checked against PDF extraction and scan/Tesseract output. Scan `_0091` confirms the Book V divider, `_0092` returns no text, and `_0093` begins `Erstes Kapitel. Spinoza.` / `Die Erkenntnislehre des Kurzen Traktats`.
- The active translation starts on PDF `_0093` and stops at the end of `_0096`; PDF `_0097` begins the historical-perspective paragraph reserved for Part 018.
- The review corrected OCR residue around `Wirklichkeit des unendlichen Seins`, `von`, `gut ist`, `Gottesbewußtsein das Grundfaktum`, `die Sache`, `etwas`, `Wirkungen, die`, `außen`, `Verwerfens`, `hinterlassen, wird`, `sinnlichen`, `substantiellen`, `sofern`, `macht`, `wahren Glauben`, `erschließen`, and `verfolgen`.
- The quoted German from the `Short Treatise` is translated in the main draft. The remaining footnotes are source identifications and cross-references, with no substantive source-language footnote quotation deferred.
- Trailing review integrated two register fixes: the opener now avoids implying that Spinoza "lets" the object seize the mind, and the part note explains the deliberate `Glückseligkeit` split between title `Well-Being` and quoted doctrinal `blessedness`. The `anschaulich` / `Intuition` distinction stays open for Part 018 rather than being settled from the opener alone.

## 2026-05-14 - Spinoza, Intuition, Renaissance, And The Short Treatise

Created `parts/018-spinoza-intuition-renaissance-and-the-short-treatise.md` from PDF pages `97-104` / printed pages `77-84 partial`, beginning with `Für das Verständnis dieser Grundansicht...` and stopping before section `II. Der Tractatus de intellectus emendatione`.

What this tranche clarified:

- Cassirer places the `Short Treatise` at a distance from the actual logical tendency of Cartesianism. Spinoza knows Descartes, but his early concept of intuition is not Cartesian mathematical insight.
- The Part 017 `anschaulich` watchpoint resolved into a sharper distinction: Cartesian intuition has axioms as its content, while early Spinozan intuition has infinite divine being as its content.
- The historical comparison shifts Spinoza away from Bruno when the measure is epistemology. The nearer context is Telesio and Campanella: passive knowing, Renaissance natural philosophy, all-unity, and all-animation.
- The section closes by naming the next problem: Spinoza's ethics keeps the Renaissance inheritance, but his epistemology undergoes a decisive transformation that gives the system a new logical form.

Structural center:

- The load-bearing movement is the split between mathematical and mystical intuition. `Intuition / Anschauung` is no longer only a watchpoint; it is the term through which Cassirer distinguishes the `Short Treatise` from both Descartes and Spinoza's mature system.

Routing decision:

- Add `Intuition / Anschauung` as an open glossary entry.
- Keep `reines Leiden`, `Allnatur`, `Alleinheit / Allbeseelung`, `Naturbegriff`, `Selbsterhaltung`, and `Freiheit / Notwendigkeit` in the close-reading ledger.
- Do not split `Substanz` from the Hobbes `Körper / Materie / Substanz` entry yet; the explicit substance section still has not arrived.

Re-entry hooks:

- Part 019 should begin on printed page `84` / PDF page `104` with section `II. Der Tractatus de intellectus emendatione`.
- Watch whether the `Tractatus de intellectus emendatione` transforms intuition from mystical union into methodical possession of the true idea.
- Watch whether `reines Leiden` ends as a `Short Treatise` stage once the intellect receives its own force and criterion.
- Watch whether the Spinoza chapter is forming a two-stage pattern: Renaissance all-nature and passivity first, then Cartesian/logical self-correction.

Decision for now:

- Part 018 passes the self-review gate for controlled draft status after a fresh same-agent second pass. The successful test tranche supports setting a Spinoza chapter goal, provided the goal keeps the fresh second-pass-per-tranche requirement.

Verification result:

- PDF pages `97-104` were checked against scan/Tesseract output on `_0097` through `_0104`. Scan `_0097` confirms the start on printed page `77`; scan `_0104` confirms the stop before section `II. Der Tractatus de intellectus emendatione`.
- The review corrected OCR residue around `geometrischen`, `Einsicht, so`, `der Sache selbst`, `Sklaven Gottes`, `Dies`, `hier`, `Empfindung`, `erinnern`, `Alles`, `sowie`, `Campanella`, `juxta propria`, `secundum`, `Sapientia`, `Essentia`, `participata`, `Urteil der Seele`, `Weisheit`, `Einschränkungen und`, `Jede Determination`, `Oportet`, `immensum`, `ungereimt`, `flössen`, `mathematisch-mechanischen`, `Zusammenhang in`, `Spinozas`, `Dilthey`, and `Zusammenhang bis in`.
- The Campanella Latin quotation is translated in the draft-footnote layer. The long Campanella apparatus note is translated/summarized because it carries Cassirer's argument about Spinoza, Renaissance pantheism, determination/negation, space, and freedom.
- Fresh second pass checked corrected-German continuity, English register, footnote marker sequencing, and routing. The page-reset footnotes are represented as a single part sequence in both German and draft-footnote layers.
- Trailing review corrected the lower-register `Anschauung` rendering in the Bruno comparison from `intuition` to `view` and added that policy to the part note, glossary entry, and close-reading ledger.

## 2026-05-14 - Spinoza, Tractatus, True Idea, And Intellect

Created `parts/019-spinoza-tractatus-true-idea-and-intellect.md` from PDF pages `104-108` / printed pages `84 partial-88 partial`, beginning with section `II. Der Tractatus de intellectus emendatione` and stopping before `Aber freilich: nicht unser beschränktes...`.

What this tranche clarified:

- The `Tractatus de intellectus emendatione` preserves the ethical end of the `Short Treatise` but changes the way toward it. Blessedness no longer descends from an external good; the means lie in the mind itself.
- The decisive epistemic move is the self-illumination of the true idea. Certainty is not supplied by agreement with an external object, but by the power and nature of the intellect itself.
- Spinoza's correction now reaches the Cartesian starting point Cassirer cares about: not things outside, but the intellect is the first object of philosophical reflection.

Structural center:

- The load-bearing movement is from object-given certainty to immanent criterion. The true idea validates itself and makes deduction possible, while the former `reines Leiden` of the mind before the object is explicitly surpassed.

Routing decision:

- Update `Intuition / Anschauung` for the transition from immediate possession/vision to methodical acquisition and reflective procedure.
- Keep `Idee / wahre Idee`, `Intellekt / Verstand`, `conceptus / perceptio`, `Definition`, and `Wahrheit / Gültigkeit` in the close-reading ledger. Do not open a new glossary entry until Part 020 tests the definition doctrine.
- Do not split `Körper / Materie / Substanz` yet; this tranche is epistemological and has not reached Spinoza's explicit substance doctrine.

Re-entry hooks:

- Part 020 should begin on printed page `88` / PDF page `108` with `Aber freilich: nicht unser beschränktes...`.
- Watch whether `Idee / wahre Idee` and `Definition` earn glossary status when Cassirer turns from the criterion of truth to genetic definition.
- Watch whether `reines Leiden` is truly left behind or returns in transformed form when Spinoza's metaphysics enters.
- Watch whether the chapter continues the two-stage movement from Renaissance passivity to Cartesian/logical self-correction, or whether the two motives remain unresolved.

Decision for now:

- Part 019 passes the self-review gate for controlled draft status after a fresh same-agent second pass. Continue to Part 020 before promoting any new Spinoza terms.

Verification result:

- PDF pages `104-108` were checked against scan/Tesseract output on `_0104`, `_0105`, and `_0108`. Scan `_0104` confirms the transition from the close of section I into `II. Der Tractatus de intellectus emendatione`; scan `_0108` confirms the stop before `Aber freilich...`.
- The review corrected OCR residue around `Spinozas`, `Zusammenhang in`, `Dilthey`, `Tractatus`, `Daseinsgüter`, `mehr`, `wahre Idee`, `äußeres`, `Paragrapheneinteilung`, `Verbesserungen und Zusätzen`, `Gewahrwerden`, `wie`, `Gegebenes ist, sondern`, `Anfang`, and `Reflexion`.
- The quoted German from the `Tractatus de intellectus emendatione` is translated in the main draft. Footnote 3 is translated because it carries dating evidence for the `Short Treatise` additions; the other footnotes are bibliographic or source identifications.
- Fresh second pass tightened the English for `Scheingüter` and `Beschaffenheiten und Kräfte`, checked footnote marker sequencing, and confirmed that no new glossary entry was earned before the Part 020 definition test.

## 2026-05-14 - Spinoza, Genetic Definition, And Causa/Ratio

Created `parts/020-spinoza-genetic-definition-and-causa-ratio.md` from PDF pages `108-111` / printed pages `88 partial-91 partial`, beginning with `Aber freilich: nicht unser beschränktes...` and stopping after `Die Gleichsetzung von Realgrund und Erkenntnisgrund, von causa und ratio ist vollzogen.`

What this tranche clarified:

- Spinoza's method rejects both disconnected empirical comparison and scholastic abstraction. They seem opposed, but both compare individual things and arrive only at blurred generic total representations.
- Genuine definition is genetic. It does not list marks of an already-given object; it lets the object arise before the mind in lawful sequence.
- Geometry becomes the model for metaphysics because it knows the particular as particular through a universal law of construction. The tranche closes with the equation of real ground and ground of knowledge, `causa` and `ratio`.

Structural center:

- The load-bearing movement is from abstraction to construction. Productive knowledge is synthetic: thought comprehends fully only what arises from thought itself according to law.

Routing decision:

- Add `Definition / Konstruktion` as an open glossary entry.
- Update `Ursache / Bedingung / Erzeugung`, `Begriff / Wort / Zeichen`, and `Intuition / Anschauung`.
- Keep `causa / ratio`, `Realgrund / Erkenntnisgrund`, `geistiger Automat`, `anschaulich möglich`, and `Idee / wahre Idee` in the close-reading ledger until the next mediation tranche tests whether they widen.

Re-entry hooks:

- Part 021 should begin on printed page `91` / PDF page `111` with `Die Vermittlung zwischen den beiden Gegengliedern...`.
- Watch whether `causa / ratio` becomes the chapter's structural center or stays the local result of the definition doctrine.
- Watch whether Spinoza repeats Hobbes's construction pattern or transforms it by identifying rational derivation with the One order of being.
- Watch whether the next tranche forces a clearer split between Hobbesian generation and Spinozan causa/ratio.

Decision for now:

- Part 020 passes the self-review gate for controlled draft status after a fresh same-agent second pass. Continue to Part 021 before making any chapter-level Spinoza pattern claim.

Verification result:

- PDF pages `108-111` were checked against scan/Tesseract output on `_0108` through `_0111`. Scan `_0108` confirms the Part 019/020 boundary, and scan `_0111` confirms the stop after `causa und ratio ist vollzogen`.
- The review corrected OCR residue around `Begriffsbildung teilt`, `läßt`, `Produkt`, `innerer`, `beschreiben`, `Geistes`, `bezeichnet`, `Akt der Konstruktion löst`, `entstanden sind. Erst`, `ist das Ziel`, `Verknüpfung der`, `ab uno ente reali`, `ita`, `aliquo reali`, and `automatum spirituale`.
- Substantive Latin footnotes 1, 3, 4, and 5 are translated in the draft-footnote layer. Footnote 2 is source identification only.
- Fresh second pass tightened the English around `sich konstituiert und aufbaut`, `zu neuen Inhalten des Wissens zu bestimmen`, `entwirft`, and `von den Ursachen zur Wirkung`, and confirmed that `Definition / Konstruktion` has earned glossary status.

## 2026-05-14 - Spinoza, Mathematics, And The Fixed Eternal Things

Created `parts/021-spinoza-mathematics-and-fixed-eternal-things.md` from PDF pages `111-116` / printed pages `91 partial-96 partial`, beginning with `Die Vermittlung zwischen den beiden Gegengliedern...` and stopping before the centered break and `Je schärfer der Gegensatz...`.

What this tranche clarified:

- Spinoza does not mediate cause and thought by dissolving physical cause into mathematical function. Mathematics itself takes up the concept of cause.
- This gives mathematics a different status than it has for Descartes and Galileo. It no longer only clarifies the order of knowledge; it guarantees the absolute reality of objects.
- The `fixed and eternal things` supply the mediating doctrine: mutable particulars are not reached by empirical sequence one by one, but by laws and basic natures such as motion and understanding.

Structural center:

- The load-bearing movement is mathematics becoming metaphysical cause. Geometrical deduction mirrors the real process by which things enter existence, and intuition becomes the mind's highest self-activity rather than surrender to alien being.

Routing decision:

- Add `feste und ewige Dinge` as an open glossary entry.
- Update `Definition / Konstruktion`, `Ursache / Bedingung / Erzeugung`, `Intuition / Anschauung`, and `Bewegung`.
- Keep `Funktionsbegriff`, `causa / ratio`, `Realgrund / Erkenntnisgrund`, `Erkenntnisstufen`, `geistiger Automat`, and `sub specie aeternitatis` in the close-reading ledger.

Re-entry hooks:

- Part 022 should begin on printed page `96` / PDF page `116` after the centered break with `Je schärfer der Gegensatz...`.
- Watch whether Hobbes is explicitly named as the historical mediator of Spinoza's genetic definition doctrine.
- Watch whether `feste und ewige Dinge` remains a `Tractatus`-local solution or becomes the bridge into the substance/metaphysics section.
- Watch whether a bounded Hobbes-Spinoza note becomes earned, but do not write it before section III supplies contrast evidence.

Decision for now:

- Part 021 passes the self-review gate for controlled draft status after a fresh same-agent second pass. Continue to Part 022 before making any chapter-level synthesis.

Verification result:

- PDF pages `111-116` were checked against scan/Tesseract output on `_0111` through `_0116`. Scan `_0111` confirms the start after `causa und ratio ist vollzogen`; scan `_0116` confirms the centered break before `Je schärfer der Gegensatz...`.
- The review corrected OCR residue around `Verknüpfung der`, `Funktionsbegriff`, `metaphysische`, `Phänomenen`, `Autorität der Sinne`, `Eigentümlichkeit des Verstandes`, `res non tam`, `quadam specie aeternitatis`, `nec`, `durationem attendit`, `bedingen. Es ist`, `Bezeichnungen und`, `Traetat`, `Pollock`, `Bewegungserscheinungen`, `wahrhafte`, `unendlichen`, `Grundelemente der Bewegung`, `Bewegungsvorgänge`, `Bewegungsgesetze`, and `mitten im Zeitverlauf`.
- The substantive Latin quotation in footnote 2 is translated in the draft-footnote layer. The longer `De intellectus emendatione` § 100 and `Short Treatise` quotations are translated in the main draft because Cassirer quotes them in German in the body.
- Fresh second pass tightened the English around deductive thought-sequence, `Eigentümlichkeit des Verstandes`, and the `Bewegungserscheinungen` sentence, and confirmed that `feste und ewige Dinge` is earned by the explicit mediation doctrine.

## 2026-05-14 - Spinoza, Descartes, Hobbes, And Causa Sui

Created `parts/022-spinoza-descartes-hobbes-and-causa-sui.md` from PDF pages `116-122` / printed pages `96 partial-102 partial`, beginning after the centered break with `Je schärfer der Gegensatz...` and stopping before section `III. Der Begriff der Substanz. — Die Metaphysik`.

What this tranche clarified:

- Descartes gives Spinoza the centrality of mathematics, but Cartesian freedom blocks the complete unity of method by introducing a break in necessary connection.
- Hobbes is the positive historical mediator for the `Tractatus` method. Cassirer says the doctrine of genetic definition agrees with `De Corpore` down to the examples.
- The agreement has a sharp limit: Hobbes can know what is generated, but excludes the ungenerated and eternal. Spinoza closes the method's gap through `causa sui`, where concept and being, essence and existence, coincide.

Structural center:

- The load-bearing movement is Spinoza taking Hobbes beyond Hobbes. Hobbes supplies genetic definition and constructive rationality; Spinoza turns that method toward the ungenerated by joining causal definition to `causa sui`.

Routing decision:

- Update `Definition / Konstruktion`, `feste und ewige Dinge`, `Ursache / Bedingung / Erzeugung`, `Begriff / Wort / Zeichen`, and `Körper / Materie / Substanz`.
- Keep `Geisteswissenschaften`, `Willensfreiheit`, `Anthropomorphismus`, `Phoronomie`, `Universalia`, `causa sui`, and `Nominalismus` in the close-reading ledger.
- Do not write a bounded Hobbes-Spinoza note yet; section III must first show what the method contrast does to substance and modes.

Re-entry hooks:

- Part 023 should begin on printed page `102` / PDF page `122` with section `III. Der Begriff der Substanz. — Die Metaphysik`.
- Watch whether `Körper / Materie / Substanz` should split into a Spinoza-specific `Substanz / Modi / Attribute` entry.
- Watch whether `causa sui` earns glossary status or remains routed through `Definition / Konstruktion` and the substance doctrine.
- Watch whether the section-II finding becomes a bounded Hobbes-Spinoza note after the substance section supplies contrast evidence.

Decision for now:

- Part 022 passes the self-review gate for controlled draft status after a fresh same-agent second pass. Section II of the Spinoza chapter is drafted through its close; continue to section III before chapter-level synthesis.

Verification result:

- PDF pages `116-122` were checked against scan/Tesseract output on `_0116` through `_0122`. Scan `_0116` confirms the start after the centered break; scan `_0122` confirms the stop before section `III. Der Begriff der Substanz. — Die Metaphysik`.
- The review corrected OCR residue around `entscheidenden`, `Zurückhaltung, die`, `Anthropomorphismus`, `imperium in imperio concipere`, `eadem`, `qualiumcunque`, `intelligendi`, `Geisteswissenschaften`, `Hobbes`, `äußeren`, `apriorisches`, `übertragen`, `Hobbes' Lehre von den Affekten`, `an Hobbes fesselte`, `zwischen`, `libitum`, `sic`, `tamen`, `Bacons`, `hervorgehoben`, `Phoronomie`, `gleichmäßig`, `Illa`, `Lemma`, `Bedeutung, die`, `kann es`, `gesamte Theologie`, `unbegreiflichen Gottes`, `Notwendigkeit und`, `Gewähr`, `Abschluß`, `Aufbau`, and `kenntlich macht`.
- Substantive Latin in footnotes 2, 5, 7, and 9 is translated in the draft-footnote layer. Footnote 6 is translated/summarized because Cassirer's German note carries the Bacon/Hobbes routing argument.
- Fresh second pass tightened the English around method's victory, Hobbes' attraction for Spinoza, and the Hobbesian beginning from general/simple causes. The scan-confirmed `Ethik III` citation was preserved in the German layer and flagged in the draft-footnote layer as a likely citation issue.

## 2026-05-14 - Spinoza, Substance, Pantheism, And Geometrical Method

Created `parts/023-spinoza-substance-pantheism-and-geometrical-method.md` from PDF pages `122-124` / printed pages `102 partial-104 partial`, beginning with section `III. Der Begriff der Substanz. — Die Metaphysik` and stopping before `Es ist interessant, die weiteren Spuren dieser Grundanschauung...`.

What this tranche clarified:

- The substance section opens by showing why the finished `Ethics` cannot be read as a static doctrine without its development. The relation between One substance and finite modes appears antinomic when its methodical genesis is not kept in view.
- Finite things are pulled in two directions: they are negations grounded in inadequate imagination, yet also necessary moments grounded in God's essence.
- The `Tractatus` material returns as the historical standpoint: the mind seeks the knowledge of unity that links it with all-nature, and geometry is the only medium that can free it from anthropomorphic concepts.

Structural center:

- Geometry is constitutive, not merely demonstrative. The geometrical method does not externally prove an already fixed concept of being; it first sets and grounds that concept in Spinoza's sense.

Routing decision:

- Add `Substanz / Modi` as a Spinoza-specific glossary entry and mark the split from Hobbes's `Körper / Materie / Substanz`.
- Update `Definition / Konstruktion`, `feste und ewige Dinge`, `Ursache / Bedingung / Erzeugung`, and `Intuition / Anschauung`.
- Keep `Attribute`, `causa sui`, `All / Allnatur`, `Pantheismus`, `Imagination`, `Zweck / Zeit / Zahl / Maß`, and `geometrische Methode` in the close-reading ledger.
- Do not write the Hobbes-Spinoza bounded note yet; this first substance tranche supplies real evidence, but section III still needs the next comparison before the pattern is stable.

Re-entry hooks:

- Part 024 should begin on printed page `104` / PDF page `124` with `Es ist interessant, die weiteren Spuren dieser Grundanschauung...`.
- Watch whether the `Theologisch-Politische Traktat` material confirms geometry as a cross-register principle of objectivity or opens a new scripture/politics register.
- Watch whether `Substanz / Modi` must expand to `Substanz / Modi / Attribute` once the attribute doctrine becomes explicit.
- Watch whether `All / Allnatur` becomes a glossary entry or remains routed through the substance/mode problem.

Decision for now:

- Part 023 passes the self-review gate for controlled draft status after a fresh same-agent second pass. Continue to Part 024 before chapter-level synthesis or a bounded Hobbes-Spinoza note.

Verification result:

- PDF pages `122-124` were checked against scan/Tesseract output on `_0122` through `_0124`. Scan `_0122` confirms the section heading; scan `_0124` confirms the stop before `Es ist interessant, die weiteren Spuren...`.
- The review corrected OCR residue around `Aufgabe`, `Gegensatz`, `kenntlich`, `der Substanz`, `endlichen`, `wenn`, `bestimmter`, `causa sui`, `solam`, `S. hierzu`, `getrennt`, `völlig`, `Schwäche`, `Mittel`, `Instrumente des Erkennens`, `geometrischen`, `Grundanschauung`, `Cogitata`, and `Cap.`.
- Footnote 2 is translated in the draft-footnote layer because it carries Cassirer's textual decision about Wenzel's `humana` / `humanam` variant. Footnotes 1 and 3 are source identifications.
- Fresh second pass tightened the English around `Fülle`, `vorzustellen`, `einzig und allein`, and the Wenzel footnote, and confirmed that `Substanz / Modi` has earned a split from the Hobbes body/matter entry.

## 2026-05-14 - Spinoza, Deus Sive Natura, And Nature-Order

Created `parts/024-spinoza-deus-sive-natura-and-nature-order.md` from PDF pages `124-126` / printed pages `104 partial-106 partial`, beginning with `Es ist interessant, die weiteren Spuren dieser Grundanschauung...` and stopping before `Damit erst ist der spezifische Grundcharakter...`.

What this tranche clarified:

- The `Theologisch-Politische Traktat` comparison confirms the same basic view rather than opening a separate register. God's guidance, decree, will, and action all mean the fixed order of nature.
- The formula `Deus sive natura` receives its sharper meaning: nature is not the sum of individual things or a thing-like whole, but the lawful connection of things.
- A gap, external intervention, or alternative course of occurrence would break the concept of God rather than defend it; Cassirer even names the admission of such a gap as atheism.

Structural center:

- The load-bearing movement is from thing-nature to order-nature. Divine being is not an object over against natural order; it is the thorough lawfulness and inviolability of that order.

Routing decision:

- Update `Substanz / Modi`, `Definition / Konstruktion`, and `Ursache / Bedingung / Erzeugung`.
- Keep `Deus sive natura`, `Naturordnung`, `Wille Gottes`, `Theologisch-Politischer Traktat`, and `Atheismus` in the close-reading ledger.
- Do not open a new glossary entry from this confirmation tranche alone.

Re-entry hooks:

- Part 025 should begin on printed page `106` / PDF page `126` with `Damit erst ist der spezifische Grundcharakter...`.
- Watch whether Cassirer now explains why the `Ethics` obscures this order-concept through scholastic substance terminology.
- Watch whether `Substanz / Modi` expands to include `Attribute`, or whether the next movement first detours through Aristotelian/scholastic category history.
- Watch whether the order-concept is stable enough after Part 025 to support a bounded Hobbes-Spinoza note, or whether the substance critique still needs more evidence.

Decision for now:

- Part 024 passes the self-review gate for controlled draft status after a fresh same-agent second pass. Continue to Part 025 before promoting `Deus sive natura` or drafting the bounded comparison note.

Verification result:

- PDF pages `124-126` were checked against scan/Tesseract output on `_0124` through `_0126`. Scan `_0124` confirms the start after the Part 023 stop; scan `_0126` confirms the stop before `Damit erst...`.
- The review corrected OCR residue around `Grundanschauung`, `Theologisch-Politische Traktat`, `derjenigen`, `Zwecken und Absichten`, `Unter der Leitung Gottes`, `unabänderliche`, `Verkettung`, `Theologico-Politicus`, `Cap.`, `Deus`, `legibus`, `naturae`, `atheismum`, `Gesetzen`, `Deus sive natura`, and `gesetzliche Verknüpfung`.
- Substantive Latin footnotes 2 and 3 are translated in the draft-footnote layer. Footnote 1 is source identification because the TPT claim is translated in the main draft.
- Fresh second pass tightened the syntax around `entgegenzustellen`, checked quote/footnote alignment, and kept `Deus sive natura` in the ledger rather than promoting it on first confirmation.

## 2026-05-14 - Spinoza, Scholastic Substance, And Abstract Existence

Created `parts/025-spinoza-scholastic-substance-and-abstract-existence.md` from PDF pages `126-130` / printed pages `106 partial-110 partial`, beginning with `Damit erst ist der spezifische Grundcharakter...` and stopping before `Der Satz „omnis determinatio est negatio"...`.

What this tranche clarified:

- The difficulty in the `Ethics` presentation is not the imitation of mathematical proof procedure. It is the inherited scholastic substance concept that Spinoza places at the system's head without critique.
- The substance/mode opposition looks self-certain because it is extremely general, but the Trendelenburg quotation shows that the positive content of substance is presupposed rather than defined.
- Reading substance as abstract `Dasein` or existence seems to solve the positivity problem, but Cassirer rejects that solution. Spinoza's own method requires a determinate `essentia particularis affirmativa`, not a vague common predicate.

Structural center:

- The load-bearing movement is from substance as inherited category to the failure of abstract existence. Cassirer is narrowing the question toward how a particular idea can nevertheless reject all limitation.

Routing decision:

- Update `Substanz / Modi`, `Definition / Konstruktion`, and `Intuition / Anschauung`.
- Keep `Sein / Dasein / Existenz`, `notiones communes`, `Imagination`, `essentia particularis affirmativa`, `A- oder B-Sein`, `Nicht-Sein`, and the restored Aristotle Greek in the close-reading ledger.
- Do not open a new glossary entry for `Sein / Dasein / Existenz` until Part 026 shows how `omnis determinatio est negatio` is resolved.

Re-entry hooks:

- Part 026 should begin on printed page `110` / PDF page `130` with `Der Satz „omnis determinatio est negatio"...`.
- Watch whether the solution shifts from individual being to the order of individual beings.
- Watch whether `Substanz / Modi` expands to include `Attribute`; attributes still have not become the center.
- Watch whether `Sein / Dasein / Existenz` becomes a recurring glossary pressure or remains a negative foil for the order-concept.

Decision for now:

- Part 025 passes the self-review gate for controlled draft status after a fresh same-agent second pass. Continue to Part 026 before opening `Sein / Dasein / Existenz` or drafting a bounded note.

Verification result:

- PDF pages `126-130` were checked against scan/Tesseract output on `_0126` through `_0130`. Scan `_0126` confirms the start after the Part 024 stop; scan `_0130` confirms the stop before `Der Satz „omnis determinatio est negatio"...`.
- The review corrected OCR residue around `Metaphysischen Gedanken`, `Ethik`, `Wirklichkeitserkenntnis. Freilich`, `Prädikat`, `omnia`, `οὐσία`, `συμβεβηκότα`, `und der Accidenzen`, `Simmel`, `übereinstimmen und`, `Behauptung`, `Nicht-Sein`, `notwendig`, `Ontologie`, `verschieben`, `notiones communes`, `bloße`, `verschwommener`, `aliquid`, `conclusio`, and `De intellect. emendat.`.
- The substantive Trendelenburg quotation is translated in the main draft because Cassirer quotes it in German. Footnote 4's Latin from the `Tractatus` is translated in the draft-footnote layer.
- Fresh second pass checked the `Dasein` rendering against Goethe's formula, restored the Greek category terms, and tightened the English around `Beweisverfahren`, `real angewandt`, and `inhaltliche Bedeutung`.

## 2026-05-14 - Spinoza, Order Of Individual Beings, And Immanent Cause

Created `parts/026-spinoza-order-of-individuals-and-immanent-cause.md` from PDF pages `130-132` / printed pages `110 partial-112 partial`, beginning with `Der Satz „omnis determinatio est negatio"...` and stopping before `Zu den gleichen Grundbestimmungen...`.

What this tranche clarified:

- The apparent conflict between a particular affirmative idea and the rejection of limitation is resolved by shifting the object of adequate knowledge from the individual being to the order of individual beings.
- The particular things remain the material of knowledge; they do not become scholastic entities. They are now seen in a new form of connection.
- Substance is immanent cause because it is the necessary mathematical connection of individual things, not a separated thing behind them and not their mere sum.

Structural center:

- The load-bearing movement is from individual being to order as immanent cause. The All becomes the pervasive order and unitary law that conditions the stock of individual things.

Routing decision:

- Update `Substanz / Modi`, `Definition / Konstruktion`, `feste und ewige Dinge`, and `Intuition / Anschauung`.
- Keep `omnis determinatio est negatio`, `Ordnung der Einzelwesen`, `immanente Ursache`, `transiente Ursache`, `All`, `logischer Kampf`, and `geometrische Gesetzlichkeit` in the close-reading ledger.
- Do not open `immanente Ursache` until Part 027 tests whether the dynamic-force contrast makes it recur strongly enough.

Re-entry hooks:

- Part 027 should begin on printed page `112` / PDF page `132` with `Zu den gleichen Grundbestimmungen...`.
- Watch whether Spinoza's non-numerical unity and whole/part critique continue the order-concept or require a separate `Einheit / Vielheit` entry.
- Watch whether the coming dynamic-force discussion reintroduces the `Short Treatise` / Renaissance nature view that Part 018 isolated.
- Watch whether the bounded Hobbes-Spinoza note is now earned; the order/immanent-cause result may be the contrast evidence that was missing earlier.

Decision for now:

- Part 026 passes the self-review gate for controlled draft status after a fresh same-agent second pass. Continue to Part 027 before opening `immanente Ursache` or writing a bounded note.

Verification result:

- PDF pages `130-132` were checked against scan/Tesseract output on `_0130` through `_0132`. Scan `_0130` confirms the start at `Der Satz...`; scan `_0132` confirms the stop before `Zu den gleichen Grundbestimmungen...`.
- The review corrected OCR residue around `omnis determinatio`, `Ordnung der Einzelwesen`, `verwirklicht. Die Regel`, `das`, `besondere Dinge`, `neuen Form`, `erblicken`, `intelligimus`, `und Schlußfolgerungen`, `Substantialität`, `transiente`, `immanente`, `inkommensurabel, aber`, `gegen den`, `ethisch-religiösen`, `Sein`, `allumfassender`, `bloßes`, and `konkret und wirklich`.
- The short substantive Latin in footnote 1 is translated in the draft-footnote layer.
- Fresh second pass checked the `order of individual beings` rendering against Part 025's `particular affirmative essence` hook, tightened `gedanklicher Bestand`, `einmalige Folge des Geschehens`, and `Sinnesempfindung`, and kept `immanente Ursache` in the ledger.

## 2026-05-14 - Spinoza, Non-Numerical Unity, And Dynamic Force

Created `parts/027-spinoza-non-numerical-unity-and-dynamic-force.md` from PDF pages `132-135` / printed pages `112 partial-115 partial`, beginning with `Zu den gleichen Grundbestimmungen...` and stopping before `Auch der persönliche Entwicklungsgang Spinozas...`.

What this tranche clarified:

- Spinoza's unity of substance is not numerical unity. Number, one/many, whole/part are imagination-concepts for comparing empirical things, not valid determinations of the All.
- The dynamic image of substance as a unitary basic force belongs most fully to the `Short Treatise` and the Renaissance nature-view, but it does not simply vanish.
- As mathematical deduction develops, divine action becomes mathematical sequence: `operari` passes into `sequi`. Yet `causa` and `ratio` interpenetrate, and mathematical law itself retains efficacy.

Structural center:

- The load-bearing movement is dynamic force yielding to mathematical order without being eliminated. Spinoza's mature rationalism is marked by the residual affective/Renaissance motive that becomes `intellektuelle Liebe zu Gott`.

Routing decision:

- Update `Substanz / Modi`, `Ursache / Bedingung / Erzeugung`, `Definition / Konstruktion`, and `Intuition / Anschauung`.
- Keep `Einheit / Vielheit`, `Ganzes / Teil`, `Kraft`, `operari / sequi`, `causa / ratio`, `Naturbegriff`, `intellektuelle Liebe zu Gott`, and `Deus sive natura` in the close-reading ledger.
- Do not open standalone entries for `Kraft` or `causa / ratio` until the chapter close tests whether they remain structural.

Re-entry hooks:

- Part 028 should begin on printed page `115` / PDF page `135` with `Auch der persönliche Entwicklungsgang Spinozas...`.
- Watch whether the personal-development passage confirms the two-ideal structure or simply restates the historical sequence already found.
- Watch whether `Verfestigung und Verdinglichung` makes the Hobbes-Spinoza bounded comparison earned.
- Watch whether the attribute doctrine forces `Substanz / Modi` to expand to `Substanz / Modi / Attribute`.

Decision for now:

- Part 027 passes the self-review gate for controlled draft status after a fresh same-agent second pass. Continue to Part 028 before opening any new entries or writing the bounded comparison note.

Verification result:

- PDF pages `132-135` were checked against scan/Tesseract output on `_0132` through `_0135`. Scan `_0132` confirms the start after the Part 026 stop; scan `_0135` confirms the stop before `Auch der persönliche Entwicklungsgang Spinozas...`.
- The review corrected OCR residue around `Zahleinheit`, `Einer`, `Einziger`, `entgegensetzen`, `Ganzes und Teil`, `Größe`, `Beschaffenheit`, `Einzeldinge`, `dynamischem`, `Kurzen Traktat`, `Wirksamkeit`, `operari`, `sequi`, `causa`, `ratio`, `zusammenhalten`, `Deus sive natura`, `Entstehung der exakten Wissenschaft`, `Weg`, `Naturerklärung`, `intellektuellen Liebe zu Gott`, and `Begriffsmomente`.
- The footnotes are source and historiographical identifications rather than substantive quotations.
- Fresh second pass checked the dynamic/mathematical contrast against Parts 017-018's Renaissance nature register, tightened the `Wirksamkeit` / `Kraft` handling, and kept `causa / ratio` and `operari / sequi` in the ledger rather than opening new entries.

## 2026-05-14 - Spinoza, Attribute Doctrine, And Order Identity

Created `parts/028-spinoza-attribute-doctrine-and-order-identity.md` from PDF pages `135-139` / printed pages `115 partial-119 partial`, beginning with `Auch der persönliche Entwicklungsgang Spinozas...` and stopping before `Läßt sich bis hierher das Motiv...`.

What this tranche clarified:

- Spinoza's personal development confirms the two-ideal structure named in Part 027: religious-pantheistic speculation, a brief naturalistic phase, and then Cartesian geometry as the definitive ideal that transforms his view of actuality.
- The doctrine of attributes is where mathematical order hardens into metaphysics. Attributes cannot be merely subjective standpoints, but Spinoza still has to explain how real manifoldness belongs to an absolutely unitary primal being.
- The positive clue is analytic geometry: the same functional connection appears as an order of objects and as a necessary sequence in thought.

Structural center:

- The load-bearing movement is order-identity across attributes. What is connected differs and belongs to different attributes; the way of connection remains the same. The identity of order becomes the identity of substance.

Routing decision:

- Expand `Substanz / Modi` to `Substanz / Modi / Attribute`.
- Update `Definition / Konstruktion`, `Ursache / Bedingung / Erzeugung`, `Intuition / Anschauung`, and `Erfahrung`.
- Keep `Verfestigung / Verdinglichung`, `Funktionszusammenhang`, `Parallelismus`, `Ordnung und Verknüpfung`, `analytische Geometrie`, `subjektive / objektive Betrachtungsweise`, and `Teilansicht` in the close-reading ledger.
- Do not open standalone `Attribute` or `Parallelismus` entries from this tranche alone.

Re-entry hooks:

- Part 029 should begin on printed page `119` / PDF page `139` with `Läßt sich bis hierher das Motiv...`.
- Watch whether the infinite-attributes problem forces a separate `Attribute` entry or remains inside `Substanz / Modi / Attribute`.
- Watch the de Vries/experience footnote: Spinoza rejects experience for attributes because essence and existence are not separated there. If the next part turns this into skepticism about inaccessible attributes, update `Erfahrung` and possibly `Sein / Dasein / Existenz`.
- Do not write the Hobbes-Spinoza bounded note yet. The `Verfestigung und Verdinglichung` link is strong, but the chapter close should decide whether the pattern is chapter-level or section-local.

Decision for now:

- Part 028 passes the self-review gate for controlled draft status after a fresh same-agent second pass. Continue to Part 029 before opening `Attribute` as a standalone entry or writing the bounded comparison note.

Verification result:

- PDF pages `135-139` were checked against scan/Tesseract output on `_0135` through `_0139`. Scan `_0135` confirms the start and the paragraph break before `In der Verfestigung...`; scan `_0139` confirms the stop before `Läßt sich bis hierher...` and shows that the de Vries/experience note continues the attribute-order footnote.
- The review corrected OCR residue around `Religionsphilosophie geht er`, `Betrachtung der Körperwelt`, `Religionsphilosophie`, `Verdinglichung`, `Attributenlehre`, `referiert`, `zurückgreift`, `Lehrgebäude`, `ausprägt`, `unmittelbar`, `Ein beliebiger`, `Funktionszusammenhang`, `Identität der Ordnung`, `Spinoza`, `Raumgestalten`, `logische Reduktion des Kausalbegriffs`, `Begriffsverhältnis`, `zwiefachen Kausalität`, `zwiefachen Logik`, `stellen sie nur`, `Teilansicht`, `zerfallen`, `Berufung`, and `geometrischen Wissens`.
- The Wenzel quotation and the substantive Latin/de Vries source-language material were translated in the draft-footnote layer.
- Fresh second pass checked the attribute argument against Parts 023-027, tightened `referiert` as "reports," and kept the Hobbes-Spinoza bounded comparison deferred until the infinite-attributes and thought-attribute material has been tested.

## 2026-05-14 - Spinoza, Infinite Attributes, And Skepsis

Created `parts/029-spinoza-infinite-attributes-and-skepsis.md` from PDF pages `139-141` / printed pages `119 partial-121 partial`, beginning with `Läßt sich bis hierher das Motiv...` and stopping before `Die Stellung, die das Attribut des Denkens...`.

What this tranche clarified:

- The infinite-attributes doctrine breaks the mediation that Part 028 had secured through order-identity. If infinitely many attributes remain forever inaccessible to the human mind, absolute knowledge yields only a small excerpt of the All.
- Cassirer roots this difficulty developmentally: the infinity of attributes belongs to the early `Short Treatise` doctrine of all-sided qualitative perfection.
- That early doctrine resists the later purification of being into lawful world-order, leaving Spinozism split between universal rule and a thing-like `Ens realissimum`.

Structural center:

- The load-bearing movement is from order-identity to skepticism pressure. The attribute doctrine can be motivated through analysis of knowledge, but the infinity of attributes reintroduces an inaccessible beyond inside the system of absolute knowledge.

Routing decision:

- Update `Substanz / Modi / Attribute`, `Erfahrung`, and `Intuition / Anschauung`.
- Keep `Skepsis`, `Unendlichkeit der Attribute`, `Ens realissimum`, `Ding aller Dinge`, `Weltordnung`, `Seinsfülle`, `qualitative Vollkommenheit`, and `Tschirnhaus` in the close-reading ledger.
- Do not open standalone `Attribute`, `Skepsis`, or `Sein / Dasein / Existenz` entries before the thought-attribute close.

Re-entry hooks:

- Part 030 should begin on printed page `121` / PDF page `141` with `Die Stellung, die das Attribut des Denkens...`.
- Watch whether thought becomes a common exponent rather than one attribute among others; this may force a route through `Selbstbewußtsein / Ich / innere Erfahrung`.
- Watch whether the chapter close turns the anthropomorphism of geometry into the bounded Spinoza note. The Hobbes-Spinoza comparison remains plausible, but the final issue may be broader.

Decision for now:

- Part 029 passes the self-review gate for controlled draft status after a fresh same-agent second pass. Continue to Part 030 before writing a bounded chapter note.

Verification result:

- PDF pages `139-141` were checked against scan/Tesseract output on `_0139` through `_0141`. Scan `_0139` confirms the start immediately after Part 028's stop and confirms `Epist. 65 u. 67` in the Tschirnhaus footnote. Scan `_0141` confirms the stop before `Die Stellung, die das Attribut des Denkens...`.
- The review corrected OCR residue around `Attribute`, `Tschirnhaus`, `Beziehung`, `Skepsis`, `Zwiespalts`, `Kurzen Traktat`, `Zusammenhange`, `Seinsfülle`, `Wesensbestimmtheit in sich`, `Weltordnung`, `Antinomien, in die`, `allbefassende Regel`, and `Ens realissimum`.
- The Sigwart quotation is translated in the main draft because Cassirer quotes it in German in the body. The two footnotes are source identifications.
- Fresh second pass checked the infinite-attributes argument against Part 028's de Vries/experience footnote, tightened the translation around `beschränkten Ausschnitt des Alls`, and kept `Attribute` inside the expanded substance cluster rather than opening a standalone entry.

## 2026-05-14 - Spinoza, Thought Attribute, And Anthropomorphism

Created `parts/030-spinoza-thought-attribute-and-anthropomorphism.md` from PDF pages `141-145` / printed pages `121 partial-125`, beginning with `Die Stellung, die das Attribut des Denkens...` and closing the Spinoza chapter before `Zweites Kapitel. Leibniz.`

What this tranche clarified:

- Thought is not merely one attribute beside others. Any unified world, even one made of unknown attributes, must be conceived through thought.
- Spinoza must introduce `idea mentis` and infinite reflection to explain thinking as activity conscious of itself, but this raises thought out of the coordinate attribute series.
- Geometry escapes subjective relativity only by relying on space-intuition and logical inference, the two attributes given to human cognition. The chapter therefore closes with an unavoidable anthropomorphism.

Structural center:

- The load-bearing movement is thought becoming the common exponent of being. This solves the infinite-attributes problem only by making the absolute order depend on the conditions of knowledge.

Routing decision:

- Update `Substanz / Modi / Attribute`, `Selbstbewußtsein / Ich / innere Erfahrung`, `Definition / Konstruktion`, and `Intuition / Anschauung`.
- Keep `Denken / Idee / Intellekt`, `idea corporis / idea mentis`, `idea ideae`, `Parallelismus`, `Anthropomorphismus`, `modi cogitandi`, `subjectum et adjunctum`, and `Geometrie` in the close-reading ledger.
- Create a bounded chapter note: `reading/2026-05-14-spinoza-absolute-order-and-anthropomorphism.md`.

Re-entry hooks:

- Book V, chapter 1 is complete. The Leibniz opening should test Cassirer's final demand: whether a transformation of the concept of being and of the concept of knowledge is supplied by Leibniz's logical-principle focus.
- Do not promote the Spinoza chapter finding to a cross-book thesis until Leibniz supplies contrast evidence.

Decision for now:

- Part 030 passes the self-review gate for controlled draft status after a fresh same-agent second pass. Spinoza chapter can receive a concise calibration before moving to Leibniz.

Verification result:

- PDF pages `141-145` were checked against scan/Tesseract output on `_0141` through `_0145`. Scan `_0141` confirms the start after Part 029's stop; scan `_0145` confirms the Spinoza chapter closes before the Leibniz chapter begins on PDF `_0146`.
- The review corrected OCR residue around `allbefassende Regel`, `Ens realissimum`, `bestehen: immer`, `Grundvoraussetzungen der reifen`, `ein weiterer Schritt`, `formale`, `ein Recht`, `Gesichtspunkt`, `Spiegelung`, `Bewußtsein`, `Subjekt`, `eine neue Dimension`, `Zusammenhang des Seins`, `Raumes`, `Hier stehen wir`, and `absoluten Wirklichkeitserkenntnis`.
- The substantive Latin in footnote 2 is translated in the draft-footnote layer. Main-text Latin phrases are preserved with English framing.
- Fresh second pass checked the chapter close against Parts 028-029 and shifted the bounded-note center away from a simple Hobbes-Spinoza hardening comparison toward Spinoza's absolute order and the anthropomorphism of geometry.

## 2026-05-14 - Spinoza Chapter Calibration

Book V, chapter 1 is drafted through the close: Parts 017-030. The chapter moved in three visible stages:

- Early Spinoza begins from immediate infinite being, pure passion, and Renaissance all-nature.
- The `Tractatus` and the geometry/substance sections transform that beginning into self-active true idea, genetic definition, order, and substance as necessary connection.
- The attribute close exposes the unresolved limit: absolute order depends on thought and geometry, yet these are the very humanly given conditions through which Spinoza tries to overcome anthropomorphism.

Status:

- Parts 017-030 are controlled drafts with same-agent second passes and scan/Tesseract verification.
- `Substanz / Modi / Attribute` is the chapter's major glossary outcome; no standalone `Attribute`, `Skepsis`, `Parallelismus`, or `Denken / Idee / Intellekt` entry has been opened.
- The bounded reading note is chapter-local and explicitly points to Leibniz as the next test.

What to expect next:

- Leibniz should test whether Cassirer treats logical principles as the transformation of being and knowledge that Spinoza's chapter demanded.
- Watch whether Leibniz resolves Spinoza's geometry anthropomorphism by shifting from substance/order to function/principle, or whether Cassirer first routes through Descartes, Hobbes, and Spinoza as inherited materials.

## 2026-05-14 - Spinoza Trailing Review: Function Wording and Pace Check

Integrated the trailing review after the Spinoza chapter close.

Decisions:

- Changed Part 028's translation of `Funktionszusammenhang` from `functional nexus` to `functional connection`. This keeps Cassirer's function-language visible without pre-loading the later `Substanzbegriff und Funktionsbegriff` frame before primary contact has earned it.
- Cold-read Parts 025 and 027 without the apparatus frame as a pace check. No substantive translation correction emerged. Part 025 still reads as a clean negative test of abstract `Dasein`; Part 027 still reads as the hinge from dynamic force to mathematical order, with the dynamic motive retained rather than erased.
- Keep the `two-ideal structure` language as Cassirer's developmental reconstruction, not as a project template. The Leibniz opening should watch whether Cassirer repeats a similar early-phase / transition / mature-ideal arc; if he does, record it as a possible Cassirer historiographical habit rather than assuming it is purely thinker-local.

## 2026-05-14 - Leibniz, Logical Principles, And The Concept Of Truth

Created `parts/031-leibniz-opening-logical-principles-and-truth.md` from PDF pages `146-152` / printed pages `126-132 partial`, beginning with `Zweites Kapitel. Leibniz.` and stopping before section `I.` / `Wenn wir -- wie die Fragestellung Leibnizens...`.

What this tranche clarified:

- Leibniz is introduced through the question of logical principles becoming, for the first time, an end in itself. Cassirer distinguishes him from Descartes's self-consciousness and Spinoza's ethical-religious God-start without treating him as an eclectic borrower.
- The common rationalist ideal of pure deduction remains active across Descartes, Spinoza, Hobbes, Galileo, and Boyle, but Leibniz evaluates these doctrines by their `Forschungsweise`, the way they reach and ground their results.
- The chapter preface shifts the fixed point from God or immediate possession of truth to the concept and definition of truth itself.

Structural center:

- The load-bearing movement is from genetic construction to critical analysis of truth. Leibniz inherits the demand that concepts be shown through possibility, generation, and cause, but refuses to claim that human cognition can simply reduce all thought to God's absolute attributes or first irresoluble concepts.

Routing decision:

- Update `Definition / Konstruktion`, `Intuition / Anschauung`, `Substanz / Modi / Attribute`, and `Selbstbewußtsein / Ich / innere Erfahrung`.
- Keep `Wahrheit / Wahrheitsbegriff`, `Analysis`, `allgemeine Charakteristik`, `reine Deduktion`, `Nominaldefinition`, `conceptus aptus / conceptus realis`, `Prinzipienlehre`, and `Gottesbegriff / Wahrheitsbegriff` in the close-reading ledger.
- Do not open a new `Wahrheit / Wahrheitsbegriff` glossary entry from this preface alone. Part 032's judgment analysis should decide whether truth/judgment earns a glossary surface.

Re-entry hooks:

- Part 032 should begin on PDF page `152` / printed page `132` with section `I.` and `Wenn wir -- wie die Fragestellung Leibnizens es verlangt...`.
- Watch whether `Wahrheit / Urteil / Subjekt-Prädikat` becomes the chapter's major new cluster.
- Watch whether Leibniz answers Spinoza's geometry/being problem by shifting from substance/order to truth/principle, or whether the next section first deepens the shared rationalist definition doctrine.

Decision for now:

- Part 031 passes the self-review gate for controlled draft status after a fresh same-agent second pass. Continue one tranche into section `I.` before deciding whether the Leibniz chapter is ready for a broader goal run.

Verification result:

- PDF pages `146-152` were checked against scan/Tesseract output on `_0146` through `_0152`. Scan `_0146` confirms the chapter start at `Zweites Kapitel. Leibniz.`; scan `_0152` confirms the stop before section `I.` and its opening sentence.
- The review corrected OCR residue around `Verhältnis zu Gott`, `Spinoza`, `Hobbes`, `Experimentalphilosophie`, `Gotteslehre`, `wie wir sahen`, `Begriffsgestaltung`, `Specimen`, `in den Anfängen`, `allgemeine Charakteristik`, `sed est index sui`, `völlig distinkt`, `conceptus aptus`, `Aufweisung`, `Einzelwissenschaften`, `Meditationes de Cognitione, Veritate et Ideis`, `possit`, `ultimam`, `nunc quidem`, `Gerh.`, `Wahrheit`, and `in ipsa generali natura Veritatum`.
- The substantive French and Latin quotations in footnotes 1 and 4 are translated in the draft-footnote layer. The abbreviation list is summarized because it is a reference surface rather than argumentative evidence.
- Fresh second pass checked the preface against the Spinoza chapter close and kept the Spinoza bounded note chapter-local. Trailing review confirmed the close-reading ledger entry was already present, restored the anchor paragraph's `for the first time` emphasis, and tightened `angeblichen Axiome` from "alleged axioms" to "putative axioms." Leibniz is now a live test of the Spinoza demand for a transformed concept of being and knowledge, not its immediate resolution.

## 2026-05-14 - Leibniz, Judgment, Induction, And Innate Ideas

Created `parts/032-leibniz-judgment-induction-and-innate-ideas.md` from PDF pages `152-161` / printed pages `132 partial-141 partial`, beginning with section `I.` / `Wenn wir -- wie die Fragestellung Leibnizens es verlangt...` and stopping before section `II.` / `Die Forderung eines Gedankenalphabets...`.

What this tranche clarified:

- Leibniz's truth-concept becomes a theory of judgment: a valid judgment requires the predicate to be included in the subject, not merely encountered with it in observation.
- Induction cannot ground itself. Moral certainty, probability, and inference from observed to unobserved cases already presuppose rational principles and a lawful order of occurrence.
- The distinction between truths of reason and truths of fact is not a double truth. It is a difference in how far analysis can be completed: necessary truths reach an end; contingent truths can only be approached through progressive analysis.
- Leibniz's doctrine of innate ideas becomes a theory of the mind's own conditions. Experience may occasion knowledge, but it cannot create content in the I that is not intelligible from the mind's own ground.
- Logic receives a wider task: it must present the interweaving of rational concepts and principles through which objective cognition of particulars becomes possible.

Structural center:

- The load-bearing movement is from empirical induction to rational grounding. Experience remains the first route by which truths of fact become known to us, but the grounding of those truths belongs to the predicate-in-subject structure of judgment and to the a priori reasons analysis seeks.

Routing decision:

- Add `Wahrheit / Urteil` as an open glossary entry.
- Update `Erfahrung`, `Definition / Konstruktion`, `Begriff / Wort / Zeichen`, `Intuition / Anschauung`, and `Selbstbewußtsein / Ich / innere Erfahrung`.
- Keep `Scientia generalis`, `allgemeine Charakteristik`, `Logik / Kombinatorik`, `Bewußtsein`, `eingeborene Ideen`, `adminicula`, `totum discretum / totum distributivum`, `moralische Gewißheit`, `Vernunftwahrheiten / Tatsachenwahrheiten`, `apriorische Gründe`, and `symbolische / intuitive Erkenntnis` in the close-reading ledger rather than opening separate entries from section `I.` alone.

Re-entry hooks:

- Part 033 should begin on PDF page `161` / printed page `141` with section `II.` and `Die Forderung eines Gedankenalphabets...`.
- Watch whether `Scientia generalis` and `allgemeine Charakteristik` earn separate glossary treatment, or whether they remain under `Begriff / Wort / Zeichen` plus `Wahrheit / Urteil`.
- Watch whether section `II.` shifts the chapter from truth/judgment to alphabet/characteristic/function; this will decide how far the Spinoza geometry problem has become a Leibnizian logic of relations rather than a substance/order problem.

Decision for now:

- Part 032 passes the self-review gate for controlled draft status after a fresh same-agent second pass. The Leibniz chapter has now cleared the opening and section `I.`; a chapter-level goal can be considered after one more check on whether section `II.` introduces a new translation burden around characteristic/alphabet.

Verification result:

- PDF pages `152-161` were checked against scan/Tesseract output on `_0152` through `_0161`. Scan `_0152` confirms the start at section `I.` after Part 031's stop; scan `_0161` confirms the stop before section `II.` / `Die Forderung eines Gedankenalphabets...`.
- The review corrected OCR residue around `Leibniz`, `I.`, `allgemeine`, `eingeschlossen`, `b` / `a und b`, `Verknüpfungen von`, `zu fordern`, `abstrakten`, `Zusammenfassung für`, `Namen`, `Deduktion, die rein`, `darin enthalten`, `wollen`, `Beobachtung dargeboten`, `Gewißheit`, `sich`, `bei ihnen`, `Abschn. III`, `empirisch, auf`, `Gesetzlichkeit alles`, `Reflexion`, `Weltbild`, `und seiner`, `Échantillon`, `Entendement de l'homme`, `irgendeine`, `Wissenschaft`, `intelligimus`, `zu erwerben`, `die Erkenntnis`, `sie ist`, and `Zusammengesetzte so weit`.
- The substantive French Arnauld quotation in footnote 2 is translated in the draft-footnote layer. Main-text quotations from Leibniz's Nizolius preface, the `Échantillon`, and the `Scientia generalis` material are translated in the draft body rather than compressed into summaries.
- Fresh read removed a duplicated Nizolius footnote marker after the first distributive-sense quotation; the scan/raw source places the marker after the second induction quotation. It also tightened `sachlich` from "factual" to "substantive" where Cassirer contrasts formal connection with content, punctuated the nested `Scientia generalis` quotation with single inner quotes so the translated quote structure remains readable, renamed the tranche metadata from "inborn ideas" to "innate ideas" to match the body policy for `eingeborene Ideen`, and added `Bewußtsein` as an active ledger/watchpoint under the self-consciousness cluster.

## 2026-05-14 - Leibniz, Thought Alphabet, Number, And Combinatorics

Created `parts/033-leibniz-thought-alphabet-number-and-combinatorics.md` from PDF pages `161-164` / printed pages `141 partial-144 partial`, beginning with section `II.` / `Die Forderung eines Gedankenalphabets...` and stopping before `Aber es ist nur ein allgemeiner programmatischer Entwurf...`.

What this tranche clarified:

- Section `II.` begins by making `Scientia generalis` a changing task, not a fixed youthful program. The thought alphabet opens Leibniz's philosophy, but Cassirer immediately says the task will be transformed by the contents drawn into it.
- Number supplies the first secure analogue for adequate cognition. Every complex calculable concept is to be derived from unity, plurality, and sequence, while number appears as the formal model of knowledge.
- The characteristic-number model translates judgment theory into calculation: subject and predicate must share a basic determination, as numbers share a common factor.
- Combinatorics extends the model from concepts to being. If everything real or thinkable is composed of parts, then the art of combinations seems to offer the schema for all possible questions of actuality.
- Early atomism appears as the natural-philosophical correlate of this logic: it is the sensible embodiment of a thought that still imagines all being as buildable from simple elements.

Structural center:

- The load-bearing movement is from truth-as-judgment to the first concrete schema of universal logic. Part 032 made predicate-in-subject inclusion the condition of valid judgment; Part 033 models that condition arithmetically and combinatorially before the next tranche tests its insufficiency.

Routing decision:

- Add `Scientia generalis / Charakteristik / Kombinatorik` as an open glossary entry.
- Update `Wahrheit / Urteil`, `Definition / Konstruktion`, `Begriff / Wort / Zeichen`, and `Atombegriff / Atomistik`.
- Keep `Funktion / Funktionsbegriff`, `Analysis der Lage`, `geometrische Charakteristik`, `Kontinuum / Stetigkeit`, `Infinitesimalkalkül`, and `Bewegung` in the close-reading ledger for the next parts of section `II.`.

Re-entry hooks:

- Part 034 should begin on PDF page `164` / printed page `144` with `Aber es ist nur ein allgemeiner programmatischer Entwurf...`.
- Watch whether the function concept earns a separate glossary entry or remains a pressure inside `Definition / Konstruktion` and `Scientia generalis / Charakteristik / Kombinatorik`.
- Watch whether `De Arte combinatoria` is treated as a merely youthful schema or as a necessary first form whose failure drives the transition to function, analysis of position, and the continuum problem.

Decision for now:

- Part 033 passes the same-agent self-review gate for controlled draft status. It is enough evidence that section `II.` has a distinct alphabet/characteristic burden; Part 034 should still be done before setting a whole-chapter goal, because it introduces the function turn directly.

Verification result:

- PDF pages `161-164` were checked against scan/Tesseract output on `_0161` through `_0164`. Scan `_0161` confirms the section `II.` start; scan `_0164` confirms the stop before the programmatic-insufficiency paragraph.
- The review corrected OCR residue around `II.`, `Leibniz'`, `Gesamtentwicklung seiner`, `mit Couturat`, `Analysis`, `Leibniz`, `adaequaten`, `Grundverhältnis`, `Inhalt`, `Subjekt und Prädikat`, `Teilen`, `wird`, `man es nun`, `um in`, `wir`, `Gerh.`, `daliegen`, `Die Atomistik`, and `Begriffsbestimmung der Logik`.
- Cassirer's substantive methodological footnote on Couturat, logic, the real sciences, and the new analysis is translated in the draft-footnote layer. The three Leibniz quotations are translated in the draft body because they carry the argument.
- Fresh second pass checked the tranche against Parts 031-032 and the beginning of Part 034, and removed a false paragraph break after the common-factor sentence because the scan continues directly with `Und wie hier der Begriff...`. The wide `pdf-161-180` staging extract was removed so the source layer only keeps the exact `pdf-161-164` tranche files.

## 2026-05-14 - Leibniz, Function, Geometric Characteristic, And Symbolic Cognition

Created `parts/034-leibniz-function-geometric-characteristic-and-symbolic-cognition.md` from PDF pages `164-170` / printed pages `144 partial-150 partial`, beginning with `Aber es ist nur ein allgemeiner programmatischer Entwurf...` and stopping before `Der Übergang zu den Problemen der Natur...`.

What this tranche clarified:

- `De Arte combinatoria` is now explicitly treated as only a programmatic design. The early schema matters, but it cannot itself determine the path of solution.
- The modern geometrical and analytical methods Leibniz learns in Paris fill the universal science with deeper content and push him beyond merely arithmetical consideration.
- The function concept replaces the number concept as mathematics' proper ground and content. Number becomes the simplest case of relation in general.
- Logic must expand beyond the Aristotelian ABC toward higher logical forms: there are as many conceptual calculi as there are kinds of deductive advance from concept to concept and truth to truth.
- The geometrical characteristic and `Analysis der Lage` provide the test case. Analytic geometry still translates figures into an alien algebraic language; the analysis of position seeks a symbolic calculus that derives positional relations from their determining conditions.
- The tranche closes by defining the high point of this movement as adequate symbolic cognition: signs reproduce relations that clear images and empirical imagination cannot reach.

Structural center:

- The load-bearing movement is from element-combination to relation-form. The universal science survives the insufficiency of `De Arte combinatoria` by shifting from simple elements and characteristic numbers to function, connection-form, and symbolic reconstruction.

Routing decision:

- Add `Funktion / Funktionsbegriff` as an open glossary entry.
- Update `Scientia generalis / Charakteristik / Kombinatorik`, `Definition / Konstruktion`, `Begriff / Wort / Zeichen`, `Wahrheit / Urteil`, and `Intuition / Anschauung`.
- Keep `Analysis der Lage / geometrische Charakteristik`, `Kalkül der Lage / calculus situs`, `adäquate symbolische Erkenntnis`, `Idee / Bild / Einbildungskraft`, `Kontinuum / Stetigkeit`, `Infinitesimalkalkül`, and `Bewegung` in the close-reading ledger until the next tranche tests their independence.

Re-entry hooks:

- Part 035 should begin on PDF page `170` / printed page `150` with `Der Übergang zu den Problemen der Natur...`.
- Watch whether `Kontinuum / Stetigkeit` earns its own glossary entry or remains a pressure inside `Funktion / Funktionsbegriff` and `Definition / Konstruktion`.
- Watch whether infinitesimal analysis makes function the bridge from geometry to nature, or whether Cassirer first stages a failure of discrete analysis before Leibniz's answer appears.

Decision for now:

- Part 034 passes the same-agent self-review gate for controlled draft status. The Leibniz chapter now has enough evidence to define a broader goal-run shape, but Part 035 is the natural next calibration point because it tests continuity and infinitesimal analysis.

Verification result:

- PDF pages `164-170` were checked against scan/Tesseract output on `_0164` through `_0170`. Scan `_0164` confirms the start after Part 033's em dash; scan `_0170` confirms the stop before the continuity/nature transition.
- The review corrected OCR residue around `bezeichnet, der in`, `wenig`, `völlig`, `Abszissen- und Ordinatenwerte`, `Funktionsbegriff`, `Verknüpfung zu`, `Wahrheit`, `Relation überhaupt`, `rerum`, `Matheseos`, `Gerh.`, `glaube`, `die geometrische Charakteristik`, `analytische Geometrie`, `in ihren Voraussetzungen`, `Characteristica Geometrica`, `äußerlicher Unterschied`, `Universalwissenschaft sich stellt`, `Eigentümlichkeiten dieses Prozesses`, `abgeleitet`, `Prinzipienlehre`, `erkennen`, `z. B. Lastträger`, `regelmäßigen Zehneck`, `Funktionsgleichung`, and `Lageverhältnisse zu tun`.
- The long Wagner quotation, the determining-conditions quotation, the `calculus situs` quotation, the `Nouveaux Essais` image/idea passage, and the final `De Analysi Situs` passage are translated in the draft body because all carry the argument.
- Fresh second pass checked the function entry against the Part 028 `functional connection` warning. Here `Funktionsbegriff` is not a later-Cassirer import; Cassirer himself names it as the replacement for `Zahlbegriff`, so the glossary promotion is earned. The same pass corrected `Statiker` from "statistician" to "statics expert" in the `Nouveaux Essais` quotation.

## 2026-05-14 - Leibniz, Continuity, Infinitesimal, And Ideal Grounds

Created `parts/035-leibniz-continuity-infinitesimal-and-ideal-grounds.md` from PDF pages `170-176` / printed pages `150 partial-156 partial`, beginning with `Der Übergang zu den Problemen der Natur...` and stopping before `Die historische Frage nach der Ursprünglichkeit...`.

What this tranche clarified:

- The transition to nature cannot happen directly from geometrical characteristic. The discrete manifold still leaves space, time, and continuous change outside the earlier element-analysis.
- The continuum problem forces Leibniz to distinguish limits from parts: points of space and moments of time are set within the finished totality, not components from which it is composed.
- `Transcreatio` is Cassirer's staged false solution. It satisfies the formal demand for separable moments by turning motion into repeated annihilation and creation, but thereby makes natural explanation depend on a constant miracle.
- The infinitesimal solution is logical rather than metaphysical. The simple and the infinitely small are conceptual requisites or ideal grounds, not tiny actual parts.
- Differential and integral calculus give genetic definition its technical fulfillment: the rule of generation becomes the true element of the curve.

Structural center:

- The load-bearing movement is from metaphysical transcreation to logical infinitesimal. Cassirer shows Leibniz first taking the continuum crisis into a doctrine of divine re-creation, then finding the real solution in the function concept's power to preserve relation, validity, and law where intuitive magnitude disappears.

Routing decision:

- Add `Kontinuum / Stetigkeit / Infinitesimal` as an open glossary entry.
- Update `Funktion / Funktionsbegriff`, `Definition / Konstruktion`, `Scientia generalis / Charakteristik / Kombinatorik`, `Raum / Zeit`, and `Bewegung`.
- Keep `Analysis des Unendlichen`, `Transcreatio`, `ideale Gründe`, `Fiktion`, `Ganzes / Teil`, `Auflösung in Begriffe / Zerfällung in Teile`, and `Formenlehre` in the close-reading ledger rather than opening separate entries.

Re-entry hooks:

- Part 036 should begin on PDF page `176` / printed page `156` with `Die historische Frage nach der Ursprünglichkeit...`.
- Watch whether the next tranche keeps `Kontinuum / Stetigkeit / Infinitesimal` as a mathematical-method entry or expands it into physical motion, force, and natural law.
- Watch the Fardella quotation on the analysis of the infinite from the inner source of philosophy; it may justify a bounded Leibniz note on mathematical discovery as philosophy made technical.
- Keep `Maschine / Mechanismus` visible as a possible nature-transition pressure only if the next tranche picks up the `Maschinen der Natur` line from Part 034.

Decision for now:

- Part 035 passes the same-agent self-review gate for controlled draft status. The Leibniz chapter now has enough calibration to define a broader chapter goal: Parts 031-035 have tested truth, judgment, characteristic, function, and continuum/infinitesimal. Part 036 remains the first goal-run stress test because it shifts toward historical priority and physical/natural-philosophical force.

Verification result:

- PDF pages `170-176` were checked against scan/Tesseract output on `_0170` through `_0176`. Scan `_0170` confirms the start after Part 034's final `De Analysi Situs` quotation; scan `_0176` confirms the stop before `Die historische Frage...`.
- The review corrected OCR residue around `Universalwissenschaft vor`, `Punkt-Mannigfaltigkeit`, `Zusammensetzung des Kontinuums`, `Ganzen`, `Deus ex machina`, `Begreiflichkeit`, `Einzelwissenschaften`, `Die neue Analysis`, `rein qualitativer`, `zu tun`, `Formenlehre`, `Sinn und seiner Geltung`, `Maßverhältnisse`, `Richtungsänderung`, `Universalwissenschaft`, `Kalkül`, `Schärfe`, `Auflösung in Begriffe`, `Zerfällung in Teile`, `methodischen Fiktion`, and `idealen Gründen`.
- The substantive Latin `transcreatio` quotation is translated in the draft-footnote layer; the Bourguet and Johann Bernoulli quotations are translated in the draft body.
- Fresh second pass tightened the methodical-fiction sentence so the antecedent is explicit: everything behaves as if this fiction were unconditional truth. The raw/normalized source filenames were also aligned to the part slug (`ideal-grounds`) so the page-map, part handle, and working files match.

## 2026-05-14 - Leibniz, Movement, Continuity, And Ideal Form

Created `parts/036-leibniz-movement-continuity-and-ideal-form.md` from PDF pages `176-180` / printed pages `156 partial-160 partial`, beginning with `Die historische Frage nach der Ursprünglichkeit...` and stopping before `Jetzt erst ist uns der Weg zur Betrachtung des realen Geschehens...`.

What this tranche clarified:

- The priority question is reframed: Leibniz's originality does not lie in first encountering the infinitesimal, but in finding a unified conceptual foundation for scattered mathematical and mechanical beginnings.
- The Fardella quotation confirms the Part 035 hook. Leibniz himself describes the analysis of the infinite as derived from the innermost source of philosophy and as mathematics rising beyond the merely imaginable.
- Movement becomes an ideal rational form. It is not an empirical datum, but a pure basic concept through which thought constructs the composite from the simple.
- The principle of continuity is the rule that lets thought include limiting cases despite the disappearance of sensible analogy: rest must be framed as a special case of movement, equality as a special case under the rule of the unequal.
- Continuity is ideal but objective. Cassirer stresses that Leibniz does not prove it from the metaphysical essence of motion; he derives it from rational order, and because reality is rational through and through, the ideal law governs the real.

Structural center:

- The load-bearing movement is from historical priority to logical objectivity. The infinitesimal calculus matters because it reveals how a rational rule can include its own limit, and continuity matters because ideal order governs actuality without being read directly from sensible or metaphysical givens.

Routing decision:

- Update `Kontinuum / Stetigkeit / Infinitesimal`, `Bewegung`, `Definition / Konstruktion`, `Scientia generalis / Charakteristik / Kombinatorik`, and `Funktion / Funktionsbegriff`.
- Keep `Kraft`, `Harmonie`, `mechanische Analogie`, `ewige Wahrheit`, `Fardella`, and `mathematical discovery as philosophy made technical` in the close-reading ledger.
- Do not open a `Kraft` glossary entry yet; Part 037 begins the explicit force material and should decide whether force becomes a separate surface.

Re-entry hooks:

- Part 037 should begin on PDF page `180` / printed page `160` with `Jetzt erst ist uns der Weg zur Betrachtung des realen Geschehens...`.
- Watch whether `Kraft` becomes the bridge from ideal continuity to physical dynamics.
- Watch whether the analysis of real temporal occurrence makes `Wahrheit / Urteil` active again through predicate-in-subject inclusion over time.
- Hold the Fardella/discovery note until the next tranche shows whether this is a repeated chapter pattern or only the historical framing of Part 036.

Decision for now:

- Part 036 passes the same-agent self-review gate for controlled draft status. The broader Leibniz goal run is operating with the intended discipline: one small formatting sweep, exact source extraction, scan boundary verification, source-language quotation handling, lean glossary routing, and a fresh second pass.

Verification result:

- PDF pages `176-180` were checked against scan/Tesseract output on `_0176` through `_0180`. Scan `_0176` confirms the start at `Die historische Frage...`; scan `_0180` confirms the stop before `Jetzt erst ist uns der Weg...`, where the next problem begins.
- The review corrected OCR residue around `Durchführung der`, `Entdeckung in`, `intimo philosophiae fonte`, `imaginabilia`, `Historia et origo Calculi differentialis`, `Hannover 1846`, `Dissertatio`, `praesenti`, `novissimis deque usu`, `Grundbegriff, der`, `reine Formen`, `Anfänge`, `in der Anschauung`, `überbrücken`, `in einem letzten Terminus`, `increbuisset`, `Beweis`, `aus dem Wesen`, `Prinzipien`, `d. h.`, `etwas Ideales`, `Leibniz`, and the French accents in the Varignon quotation.
- The substantive Latin Fardella quotation and French Varignon quotation are translated in the draft-footnote layer. The other substantive quoted material is translated in the draft body.

## 2026-05-14 - Leibniz, Temporal Occurrence, Force, And Living Force

Created `parts/037-leibniz-temporal-occurrence-force-and-living-force.md` from PDF pages `180-186` / printed pages `160 partial-166 partial`, beginning with `Jetzt erst ist uns der Weg zur Betrachtung des realen Geschehens...` and stopping before section `III.`.

What this tranche clarified:

- The transition from ideal continuity to real occurrence immediately reopens the problem of time. If genuinely new contents arise in the sequence of moments, the predicate-in-subject doctrine is threatened by becoming.
- Leibniz's mechanical nature-view is rooted in reason, not in materialist experience. Its principles account for experiences and make experimental cases determinable, but are not themselves products of mere experiment.
- The force concept supplies the mediating form. Derivative force names the present state as tending toward the next and pre-involving it, so the future is not externally added to the present.
- Cause is recast as rational accountability, not real influx. Causes are taken from the demand to render a reason.
- Work and living force make heterogeneous phenomena comparable. Conservation of living force turns apparent new creation into transformation of one persistent magnitude, preserving continuity inside physical change.

Structural center:

- The load-bearing movement is from temporal occurrence to force as rational account. Cassirer shows Leibniz extending the same continuity discipline from mathematics into dynamics: the present must contain the rule of its transition, and force is the concept by which that rule becomes physically legible.

Routing decision:

- Add `Kraft / Arbeit / lebendige Kraft` as an open glossary entry.
- Update `Bewegung`, `Kontinuum / Stetigkeit / Infinitesimal`, `Ursache / Bedingung / Erzeugung`, `Erfahrung`, `Wahrheit / Urteil`, and `Scientia generalis / Charakteristik / Kombinatorik`.
- Keep `mechanische Naturauffassung`, `Satz vom zureichenden Grunde`, `geistiges Sein`, `höhere Charakteristik`, `Erhaltung der Richtung`, and `Erhaltung / conservation` in the close-reading ledger rather than opening separate glossary entries.

Re-entry hooks:

- Part 038 should begin on PDF page `186` / printed page `166` with section `III.` and `Der Aufbau und der Stufengang der rationalen Erkenntnis...`.
- Watch whether the next section shifts from force and physical law to `Bild`, `Symbol`, `Ausdruck`, and cognition levels strongly enough to earn a new glossary surface.
- Watch whether the force/living-force entry remains physical or begins to require a broader metaphysical or biological force note.
- Do not create the Fardella/discovery note yet. Part 037 made force/dynamics the stronger chapter pattern; the discovery hook remains useful but not chapter-dominant so far.

Decision for now:

- Part 037 passes the same-agent self-review gate for controlled draft status. The broader Leibniz goal run remains on track: Part 036 tested continuity as ideal law, and Part 037 tested its physical/dynamical extension without forcing a premature bounded chapter note.

Verification result:

- PDF pages `180-186` were checked against scan/Tesseract output on `_0180` through `_0186`. Scan `_0180` confirms the start at `Jetzt erst...`; scan `_0186` confirms the stop before section `III.`.
- The review corrected OCR residue around `μετάβασις εἰς ἄλλο γένος`, `Zeitverlaufs`, `Leibnizischen`, `Charakteristische des zeitlichen Wandels`, `Bewußtsein als etwas`, `Sinneserfahrung ein zweites`, `Robert Boyle`, `Corporum`, `percipi`, `intelligibel`, `Erkenntniszusammenhang`, `status praesens`, `praeinvolvit`, `praesens gravidum est futuro`, `Specimen dynamicum`, `Clarke`, `reali influxu`, `a reddenda ratione`, `seine relative Berechtigung`, `Erhaltung der lebendigen Kraft`, `Erscheinungen auch`, `so fiele`, `feste Größe`, `Zeitverlauf`, `Leibniz`, `seine Geltung`, and `Einzelwissenschaften`.
- The substantive Latin quotations on mechanical principles, derivative force, and cause as reason rather than influx are translated in the draft-footnote layer. The Leibniz body quotations on truths of fact, higher characteristic, force, work, and conservation of living force are translated in the draft body because each carries the argument.

## 2026-05-14 - Leibniz, Image, Symbol, And Eternal Truths

Created `parts/038-leibniz-image-symbol-and-eternal-truths.md` from PDF pages `186-196` / printed pages `166 partial-176 partial`, beginning with section `III.` / `Der Aufbau und der Stufengang der rationalen Erkenntnis...` and stopping before `Alle skeptischen Einwände gegen die Realität der Erscheinungswelt...`.

What this tranche clarified:

- Section `III.` shifts from force/dynamics to the form of rational cognition itself. Leibniz's truth-concept now appears as an ideal of symbolic expression.
- Leibniz rejects the copy theory from the start: ideas do not need likeness to things, but must preserve relations in a regulated expression.
- Perception is reinterpreted through sign-function. Sensation is mute by itself; it becomes cognition only by receiving an ideal meaning for which it serves as indication.
- The general characteristic is defended against conventionalism. Its signs can be arbitrary in material, but their relation-content is independent and law-governed.
- Infinitesimal measure and physical work both become symbolic translations. Heterogeneous magnitudes and qualitative processes are made knowable by a rule of correspondence, not by direct homogeneity.
- The tranche closes by placing appearance under eternal truths. Eternal truths do not depend on facts for evidence, but the order of facts must point toward them.

Structural center:

- The load-bearing movement is from image to symbol to appearance under law. Cassirer shows the same relation-preserving form at work in ideas, characters, differentials, work-magnitudes, and eternal truths.

Routing decision:

- Add `Bild / Symbol / Ausdruck` as an open glossary entry.
- Update `Begriff / Wort / Zeichen`, `Scientia generalis / Charakteristik / Kombinatorik`, `Intuition / Anschauung`, `Kontinuum / Stetigkeit / Infinitesimal`, `Kraft / Arbeit / lebendige Kraft`, `Erfahrung`, and `Wahrheit / Urteil`.
- Keep `Phänomen / Erscheinung`, `ewige Wahrheiten`, `Harmonie / Vollkommenheit`, `primäre / sekundäre Qualitäten`, `Abbildtheorie`, `Molyneux`, `Hertz`, and `Ähnlichkeit / Analogie` in the close-reading ledger rather than opening separate entries.

Re-entry hooks:

- Part 039 should begin on PDF page `196` / printed page `176` with `Alle skeptischen Einwände gegen die Realität der Erscheinungswelt...`.
- Watch whether `Phänomen / Erscheinung` earns a glossary entry now that the next paragraph directly takes up the reality of the appearance-world.
- Watch whether `Harmonie / Vollkommenheit` becomes the bridge from symbolic cognition to substance/metaphysics.
- Do not create the bounded Leibniz chapter note yet. The symbol pattern is now visible, but the next appearance/substance tranche should decide its chapter-level form.

Decision for now:

- Part 038 passes the same-agent self-review gate for controlled draft status. It earns one new glossary surface and keeps the more tempting appearance/metaphysics terms deferred to Part 039.

Verification result:

- PDF pages `186-196` were checked against scan/Tesseract output on `_0186`, `_0187`, `_0190`, `_0191`, `_0195`, and `_0196`. Scan `_0186` confirms the section `III.` start; scan `_0196` confirms the stop before `Alle skeptischen Einwände...`.
- The review corrected OCR residue around `Ideals der Erkenntnis`, `Maschine`, `Konvention`, `Gegend`, `daß`, `Quid Sit Idea`, `formuliert`, `Molyneuxsche`, `Wahrnehmungskomplexen`, `vorliegt`, `hierzu`, `Mannigfaltigkeit zu`, `Wahrheitsgehalt zu`, `irgendeine`, `Ergebnis, zu`, `S. ob.`, `Kontingenzwinkels`, `Leibniz' Zeiten`, `πρῶτα`, `Mathematicarum metaphysica`, French accents in the `Nouveaux Essais` quotation, `vollkommen zu`, `Bewegungen, von`, `durchdringen, als indem`, `Unterschiede, die zwischen`, `enthüllt: so`, `Bedingungssätze, die`, `Mollat`, `von der Bewegung`, `darzustellen, als`, `verschaffen`, and `Réponse aux réflexions de Bayle`.
- The substantive French quotation on expressive resemblance is translated in the draft-footnote layer. The Hertz footnote quotation is summarized/translated because Cassirer uses it as evidence for the modern afterlife of Leibniz's truth concept. The long Bayle-response quotation is translated in the body because it closes the tranche's argument.

## 2026-05-14 - Leibniz, Appearance, Truths Of Fact, And Individuality

Created `parts/039-leibniz-appearance-truths-of-fact-and-individuality.md` from PDF pages `196-201` / printed pages `176 partial-181 partial`, beginning with `Alle skeptischen Einwände gegen die Realität der Erscheinungswelt...` and stopping before section `IV.`.

What this tranche clarified:

- Skepticism is right against thing-like originals behind phenomena, but wrong against the reality of the appearance-world. Appearance is real as logical truth and systematic connection.
- The astronomical example states the criterion sharply: Copernican truth is intelligibility, not exclusive correspondence to an absolute corporeal order.
- The senses cannot decide what truth or being means. Demonstrative truths stand above skeptical doubt and decide the truth of sense-things.
- The ideal and actual require functional correspondence, not material likeness. The actual is ordered as if ideal norms were full realities.
- The Leibnizian truth of fact is completed only by preserving tension: facts harmonize with eternal truths but never wholly dissolve into them.
- The individual becomes an unfinishable task for reason. Its analysis can proceed by a rule of progress without ever exhausting the individual.

Structural center:

- The load-bearing movement is from the reality criterion of appearances to the modified truth criterion for contingent fact. Leibniz answers skepticism by systematic connection, then prevents rationalism from erasing individuality by using the infinitesimal model of endless approximation.

Routing decision:

- Add `Phänomen / Erscheinung` as an open glossary entry.
- Update `Bild / Symbol / Ausdruck`, `Wahrheit / Urteil`, `Erfahrung`, `Bewegung`, `Kontinuum / Stetigkeit / Infinitesimal`, and `Scientia generalis / Charakteristik / Kombinatorik`.
- Keep `Harmonie / Vollkommenheit`, `Tatsachenwahrheit`, `Einzelnes / Individualität`, `platonisches Streben`, `Copernikanisches System`, `Foucher`, and `Skepsis` in the close-reading ledger rather than opening separate glossary entries.

Re-entry hooks:

- Part 040 should begin on PDF page `201` / printed page `181` with section `IV.` and `In der Einsicht, daß das Einzelne...`.
- Watch whether `Einzelnes / Individualität` earns a glossary entry in section `IV.` or is immediately absorbed into `Substanz / Monade`.
- Watch whether `Harmonie / Vollkommenheit` becomes a glossary entry through monadology and the system of viewpoints.
- Keep the bounded Leibniz note deferred until section `IV.` decides whether the symbol/appearance pattern becomes a harmony/monadology pattern.

Decision for now:

- Part 039 passes the same-agent self-review gate for controlled draft status. It earns `Phänomen / Erscheinung` and leaves the monadology/harmony material for the next section.

Verification result:

- PDF pages `196-201` were checked against scan/Tesseract output on `_0196` and `_0201`. Scan `_0196` confirms the start at `Alle skeptischen Einwände...`; scan `_0201` confirms the stop before section `IV.`.
- The review corrected OCR residue around `Das Kriterium der Wirklichkeit`, `erkenntnistheoretische`, `Ordnungen`, `logische Wahrheit`, French accents in the `Nouveaux Essais` quotation, `Verständlichkeit`, `Hält`, `Copernikanischen`, `eine`, `Phoranomus`, `Tentamen de motuum coelestium causis`, `Foucher`, `matière`, `démonstratives`, `exempte`, `Il n'est pas nécessaire`, `parfaitement semblable`, `exprime`, `l'Ellipse`, `certaine loi`, `harmonieren`, `andererseits in ihnen`, `Übereinstimmung der Grundstruktur`, `völlig`, `ins Unendliche auflösbar sind`, `Rational- und Irrationalzahlen`, `Unerschöpflichen`, `Mittelstellung`, and `Generales Inquisitiones de Analysi Notionum et Veritatum`.
- The substantive French quotations from the `Nouveaux Essais` and the Foucher letter are translated in the draft-footnote layer. The long Latin quotation from `Generales Inquisitiones` is translated in the draft-footnote layer because it supplies the formal criterion for contingent truth.

## 2026-05-14 - Leibniz, Monadology, Harmony, And Chapter Close

Created `parts/040-leibniz-monadology-harmony-and-chapter-close.md` from PDF pages `201-210` / printed pages `181 partial-190`, beginning with section `IV.` / `In der Einsicht, daß das Einzelne...` and stopping before `Drittes Kapitel. Tschirnhaus.`

What this tranche clarified:

- The finite `Scientia generalis` reaches its natural limit in the individual. The individual contains an infinity of conceptual partial conditions that finite cognition can clarify only successively.
- The metaphysical-rationalist pressure remains: divine intellect sees in one glance the completed resolution that finite analysis can only approach.
- Leibniz's contrast with Spinoza is now explicit. Spinoza pushed individual empirical sequences aside as unnecessary for grasping fixed-eternal things; Leibniz treats this as evading the task empirical research sets.
- The monadological turn comes through primitive force. The individual subject is not a resting aggregate of conditions but a self-active source whose changes are logically preformed by its own law.
- The appearance-world is grounded through harmony among representing subjects, not through a shared copied object.
- The chapter closes by expanding the mathematical function concept into the harmony concept of ethics and metaphysics.

Structural center:

- The load-bearing movement is from inexhaustible individuality to symbolic harmony. The chapter's earlier function, symbol, appearance, and force threads are gathered into a final account of harmony as the agreement among ideal ways of considering being.

Routing decision:

- Add `Substanz / Monade / primitive Kraft` as an open glossary entry.
- Add `Harmonie / Vollkommenheit` as an open glossary entry.
- Update `Wahrheit / Urteil`, `Scientia generalis / Charakteristik / Kombinatorik`, `Funktion / Funktionsbegriff`, `Kraft / Arbeit / lebendige Kraft`, `Bild / Symbol / Ausdruck`, `Phänomen / Erscheinung`, `Raum / Zeit`, `Intuition / Anschauung`, `Bewegung`, and `Begriff / Wort / Zeichen`.
- Keep `Einzelnes / Individualität` absorbed into `Substanz / Monade / primitive Kraft` for now. The chapter makes individuality monadological rather than a separate glossary surface.

Re-entry hooks:

- The next translation part should begin on PDF page `211` / printed page `191` with `Drittes Kapitel. Tschirnhaus.`
- Tschirnhaus should test whether constructive method and symbolic cognition can be sustained without Leibniz's harmony-metaphysics.
- Do not use the Leibniz bounded note as a template for Tschirnhaus. Use it as a contrast test: what happens to method once harmony is no longer the obvious chapter close?

Decision for now:

- Part 040 passes the same-agent self-review gate for controlled draft status. The Leibniz chapter is complete as controlled draft, pending the chapter-level calibration audit below.

Verification result:

- PDF pages `201-210` were checked against scan/Tesseract output on `_0201`, `_0202`, `_0204`, `_0205`, `_0206`, `_0207`, `_0208`, `_0209`, and `_0210`. Scan `_0201` confirms the section `IV.` start; scan `_0210` confirms the chapter close before `Drittes Kapitel. Tschirnhaus.`
- The review corrected OCR residue around `Mittelstellung`, `Analysi`, `Leibniz`, `begnügen, die`, `tamen`, `ut`, `veritatum`, `nicht genug`, `Zeitpunkt`, `zunächst`, `Entwicklungsreihen`, `Begriff der primitiven Kraft`, `Veränderungsreihen, die`, `Bilder`, `vernichte. Ist`, `Wissenschaften`, `darin,`, `Grundbegriff der Harmonie`, `keinen`, `fortgesetzten`, `dieser`, `Stufengang`, `Gesamtinhalt der Wirklichkeit`, `Vorbereitung für`, `ineinandergreifen`, `Verhältnisse`, `vérité`, `réalité`, `fundamentum habentes`, `unbedingtes Dasein`, `Kräfte`, `ausgerüstet, tritt`, `oberflächliche`, `Reich der Natur`, and `id est Deus`.
- The substantive Latin `De libertate` quotation, the French Clarke quotation, and the Latin `modi considerandi` quotation are translated in the draft-footnote layer. The de Volder and `Harmonia universalis` quotations are translated in the draft body.

## 2026-05-14 - Leibniz Chapter Calibration After Goal Run

The Leibniz chapter goal ran from Part 036 through Part 040 after Parts 031-035 had already calibrated the opening, judgment, characteristic, function, and continuum material. The goal did not require loosening the controlled-draft tier: each tranche still used exact source extraction, scan/Tesseract boundary checks, corrected German, source-language quotation handling, glossary routing, and a same-agent second pass.

Chapter-level finding:

- Leibniz answers the Spinoza close not by removing mediation, but by making mediating forms the route to objectivity. Function replaces element-search, symbol replaces copy, force carries continuity into temporal occurrence, the individual remains an inexhaustible task, and harmony names the accord among the ideal standpoints through which being is interpreted.

What changed during the goal:

- The Fardella/discovery hook did not become a bounded note. It stayed important as evidence that the calculus arises from the inner source of Leibniz's philosophy, but the chapter's dominant pattern became function-symbol-harmony rather than mathematical discovery alone.
- `Kraft / Arbeit / lebendige Kraft` became a glossary entry in Part 037, then split in Part 040 against `primitive Kraft`.
- `Bild / Symbol / Ausdruck` and `Phänomen / Erscheinung` became distinct glossary entries in Parts 038-039 because the chapter made symbol and appearance into separate structural surfaces.
- `Substanz / Monade / primitive Kraft` and `Harmonie / Vollkommenheit` were opened only at the chapter close, after section `IV.` made them more than anticipated metaphysical vocabulary.

Decision for now:

- The bounded Leibniz note at `reading/2026-05-14-leibniz-function-symbol-and-harmony.md` is earned and should remain chapter-local.
- Do not promote a cross-book Cassirer thesis from Leibniz alone. The Tschirnhaus chapter is the next test: whether constructive method and symbolic cognition can stand without Leibnizian harmony.
- The whole Leibniz chapter is controlled draft, not final translation. A later cold read can still target one mid-goal tranche and Part 040, but no known blocker remains before moving to Tschirnhaus.

Trailing review note, 2026-05-15:

- External review confirmed the chapter coverage: Parts `031-040` cover Leibniz from printed pages `126-190`, matching the chapter preface and sections `I-IV`.
- Follow-up scan check confirms `daserkenntnispro02cassuoft_0211.jp2` opens `Drittes Kapitel. Tschirnhaus.` The prose claim that the Leibniz chapter runs through printed page `191` should be read as an off-by-one slip; Part 040 closes on printed page `190`.
- Earlier concern about work-title backtick inconsistency in Parts `031-035` is retracted. The bare titles were in the faithful German Footnotes block; the English Draft Footnotes convention is consistent.
- `ewige Wahrheiten` remains a watchpoint rather than a glossary entry. Parts `038-039` made it load-bearing, but the term should be tested against Locke and Hume before it gets its own surface.
- Leibniz produced unusually dense glossary growth. Treat this as Leibniz-specific unless Tschirnhaus and the shorter following chapters earn comparable density through primary contact.

## 2026-05-15 - Tschirnhaus, Method Doctrine, Definition, And Experience

Created `parts/041-tschirnhaus-method-doctrine-definition-and-experience.md` from PDF pages `211-215` / printed pages `191-195 partial`, beginning with `Drittes Kapitel. Tschirnhaus.` and stopping before `Die Aufstellung der allgemeinen Forderung einer kritischen Erfahrungslehre...`.

What this tranche clarified:

- Tschirnhaus is introduced as mediator rather than originator. His importance lies in joining Spinoza's unfinished theory of experiential knowledge, Leibniz's Paris-era development of genetic definition, and Descartes' algebraic method into a narrower doctrine of experience for the particular sciences.
- The Leibniz contrast is explicit from the start. Leibniz presses beyond algebra toward a universal science and a general "science of forms"; Tschirnhaus holds to a narrower physical-method target.
- Definition remains genetic: to comprehend a thing is to let it arise before the mind, and every legitimate definition must include generation.
- Experience becomes the aim and regulator of rational method. It determines the concept without replacing it, while experiment helps select among abstract concept-plans when sensible particularity becomes too complex for pure deduction.

Structural center:

- The load-bearing movement is from Leibnizian universal science to Tschirnhausian methodical limitation. The opening tests whether constructive rational method can survive without Leibniz's harmony-metaphysics by turning toward physics, experiment, and Erfahrungslehre.

Routing decision:

- No new glossary entry yet.
- Update `Erfahrung`, `Experiment`, `Induktion`, `Ursache / Bedingung / Erzeugung`, `Definition / Konstruktion`, and `Scientia generalis / Charakteristik / Kombinatorik`.
- Keep `Methodenlehre`, `Erfahrungswissen / Erfahrungslehre`, `apriorischer / aposteriorischer Weg`, `methodische Beobachtung`, `Lambert`, and `deutsche vorkantische Philosophie` in the close-reading ledger until the critique of fulfillment decides whether they become more than opening pressures.

Re-entry hooks:

- Part 042 should begin on PDF page `215` / printed page `195 partial` with `Die Aufstellung der allgemeinen Forderung einer kritischen Erfahrungslehre...`.
- Watch whether `Realität`, `Entia Realia seu Physica`, `Gedankendinge`, or the three classes of the thinkable earn a glossary surface in the critique.
- Test whether Tschirnhaus's narrowed method produces critical Erfahrungslehre or exposes a new metaphysical/psychological gap.

Decision for now:

- Part 041 passes the same-agent self-review gate for controlled draft status. It is enough to open the Tschirnhaus chapter, but not enough to set a whole-chapter goal until Part 042 tests the failure/fulfillment critique.

Verification result:

- PDF pages `211-215` were checked against scan/Tesseract output on `_0211`, `_0212`, `_0213`, `_0214`, `_0215`, and `_0216`. Scan `_0211` confirms the chapter opening; scan `_0215` confirms the stop boundary just before the critique paragraph; scan `_0216` confirms the critique begins after the stop.
- The review corrected OCR residue around `Tschirnhaus`, `Methodenlehre`, `Theorie des Erfahrungswissens`, `prinzipiell`, `wollen. Auch`, `Verknüpfungen`, `Zahlenlehre`, `Standpunkt`, `Wörterbuch`, `Geometrie`, `Tschirnhaus'`, `geht`, `heißt`, `Einzeldinges`, `entstehen lassen`, `unfehlbare`, `abschätzen`, `fruchtbarste`, `aposteriorischen`, `Erfahrung determiniert`, `ausschließlich`, `Experiment`, `förderlich`, `Vernunft`, `Physices`, `considerandae`, `impossibile`, `praestare omnibus Empiricis`, and `impossibile`.
- The PDF text-layer page header `Die Lehre von der Definition. 105` was checked against the scan and corrected as printed page `195`.
- The Tschirnhaus quotations on Descartes' Mersenne letter and definition-as-generation are translated in the body. The substantive Latin `Medicina mentis` quotation in footnote 4 is translated in the draft-footnote layer.

## 2026-05-15 - Tschirnhaus, Reality, Inner Experience, And Physics

Created `parts/042-tschirnhaus-reality-inner-experience-and-physics.md` from PDF pages `215-221` / printed pages `195 partial-201`, beginning with `Die Aufstellung der allgemeinen Forderung einer kritischen Erfahrungslehre...` and stopping before `Viertes Kapitel. Der Rationalismus in der englischen Philosophie.`.

What this tranche clarified:

- Tschirnhaus's demand for a critical doctrine of experience is not identical with its fulfillment. The chapter close shows that scientific experience has become the central modern problem inside rationalism, but the method cannot fully mediate reason and experience.
- The concept of reality remains ambiguous. The thinkable divides into sensory-intuitive contents, rational/mathematical constructions, and physical or real things; the third class is supposed to arise in one way and from one cause, but this makes empirico-physical being fall outside the circle of logic.
- When factual content cannot be logically resolved, Tschirnhaus grounds deduction back in inner experience and the four facts of self-observation.
- The truth criterion slides toward psychological compulsion. Tschirnhaus then restores objectivity by a metaphysical assertion of the common identity of reason rather than by a demonstrated logical bridge.
- Physics receives an exceptional position: it is the sum of genuine cognition and the place where God's laws in things are disclosed, but this privilege is won by postulate rather than by completed method.

Structural center:

- The load-bearing movement is from methodical limitation to unresolved dualism. Tschirnhaus narrows the rationalist method toward experience and physics, but the narrowed method leaves reality outside logic, makes inner experience foundational again, and leaves harmony between reason and experience as postulate.

Routing decision:

- Add `Realität / Entia Realia / Gedankendinge` as an open glossary entry.
- Update `Erfahrung`, `Definition / Konstruktion`, `Ursache / Bedingung / Erzeugung`, `Scientia generalis / Charakteristik / Kombinatorik`, `Wahrheit / Urteil`, `Selbstbewußtsein / Ich / innere Erfahrung`, and `Harmonie / Vollkommenheit`.
- Keep `allgemeine Mitteilbarkeit`, `Intellekt / Einbildungskraft`, `Denkvermögen`, and `Physik` in the close-reading ledger rather than opening separate entries from the chapter close.
- Do not write a bounded Tschirnhaus reading note. The chapter finding is compact and is carried sufficiently by this journal entry, the ledger entry, and the new glossary cluster.

Re-entry hooks:

- The next part should begin on PDF page `222` / printed page `202` with `Viertes Kapitel. Der Rationalismus in der englischen Philosophie.`
- The next chapter should test Cassirer's transition claim: the Hobbes-Spinoza-Leibniz-Tschirnhaus line forms a closed development around definition and concept, while English rationalist currents remain relatively isolated but consequential.
- Watch whether physics remains the privileged solution or whether the rationalist issue shifts toward religion, Platonism, and innate principles.
- Do not promote Tschirnhaus's physics-exception into a cross-book thesis before the English rationalism chapter supplies contrast evidence.

Decision for now:

- Part 042 passes the same-agent self-review gate for controlled draft status. The Tschirnhaus chapter is complete as controlled draft. Its glossary growth stayed restrained after Leibniz, which supports the earlier judgment that Leibniz's dense entry-rate was chapter-specific rather than the new default.

Verification result:

- PDF pages `215-221` were checked against scan/Tesseract output on `_0215`, `_0216`, `_0217`, `_0218`, `_0219`, `_0220`, `_0221`, and `_0222`. Scan `_0215` confirms the start after Part 041's stop; scan `_0221` confirms the Tschirnhaus chapter close; scan `_0222` confirms the next chapter begins with `Viertes Kapitel. Der Rationalismus in der englischen Philosophie.`
- The review corrected OCR residue around `Tschirnhaus`, `Realität`, `Vorstellungen`, `äußeren`, `äquivalent`, `Körper`, `seu Physica`, `Gedankendingen`, `Mitwirkung`, `Entia`, `tamen`, `praecedentium`, `nullatenus`, `objecta`, `existentia`, `Ausdehnung`, `Intellekts`, `Einbildungskraft`, `perzipiert`, `besitzen wir`, `Begreifens`, `allgemeingültige`, `bleibt`, `eigentliche Bereich des wirklichen`, `empirisch-physikalischen`, `fühlbarer`, `vollständige`, `selbst`, `inneren Erfahrung`, `Bewußtseins`, `lustvoll`, `möglich`, `Vorstellungsverbindung`, `nicht etwas Stummes`, `Nicht-Sein`, `unvollziehbar`, `Denkvermögens`, `gehorcht`, `erschlichen`, `wahren Vorstellung`, `allgemeingültig`, `allgemeine Mitteilbarkeit`, `Notwendigkeit nicht besteht`, `einzelnen Individuen`, `alle Fälle`, `begründen`, `durchgängigen Gleichartigkeit`, `Harmonie`, `Postulat`, `apriorischen`, `Inbegriff`, `Gegenstände`, `enthüllen`, `Wirksamkeiten Gottes`, and `modernen Aufgaben`.
- The substantive Latin `Medicina mentis` quotation on `Entia Realia seu Physica` is translated in the draft-footnote layer. The Tschirnhaus body quotations on concept/idea and physics as divine works are translated in the draft body.

## 2026-05-15 - English Rationalism, Herbert Of Cherbury, And Common Notions

Created `parts/043-english-rationalism-herbert-common-notions.md` from PDF pages `222-227` / printed pages `202-207 partial`, beginning with `Viertes Kapitel. Der Rationalismus in der englischen Philosophie.` and stopping before `Ein zweites Moment des gedanklichen Fortschritts...`.

What this tranche clarified:

- Cassirer treats the Hobbes-Spinoza-Leibniz-Tschirnhaus line as a closed development around definition and concept, then opens a relatively isolated English side current.
- English rationalism begins next to experiential science, but not from physics in Tschirnhaus's sense. Its first a priori pressure is ethical and religious: the demand for a universal ground of moral norms and a universal church of reason.
- Herbert's `de Veritate` makes the concept of truth central. Revelation may add historical concreteness, but it cannot ground or contradict rational universal truth.
- Common notions are grounded in a natural faculty or natural instinct. They are awakened by objects but not carried into the mind by objects.
- Herbert's `notitiae communes` are "anticipations" of experience: not experiences themselves, but conditions without which nothing can be experienced.

Structural center:

- The load-bearing movement is from universal religion to a natural-faculty theory of common notions. The a priori no longer appears chiefly as genetic definition, symbolic construction, or physics; it appears as an inborn common possession of mind, held in natural instinct and opened by contact with objects.

Routing decision:

- No new glossary entry yet.
- Update `Wahrheit / Urteil`, `Erfahrung`, `Begriff / Wort / Zeichen`, and `Selbstbewußtsein / Ich / innere Erfahrung`.
- Keep `notitiae communes`, `natürlicher Instinkt`, `Einheitsreligion`, `Vermögen`, `Allnatur`, `katholische Kirche`, `Herbert`, `Platonismus`, and `κοιναὶ ἔννοιαι` in the close-reading ledger. Digby and the Cambridge school should decide whether this chapter earns a new common-notions, intelligible-being, Platonism, or faculty-psychology surface.

Re-entry hooks:

- Part 044 should begin on PDF page `227` / printed page `207 partial` with `Ein zweites Moment des gedanklichen Fortschritts...`, then move into Kenelm Digby.
- Test whether Digby's thing/existence analysis earns a distinct `Ding / Existenz / Sein` surface or instead updates existing reality, substance, and truth entries.
- Watch whether the chapter's center remains common notions and faculty psychology, or shifts toward intelligible being and Platonism in Cudworth and Norris.

Decision for now:

- Part 043 passes the same-agent self-review gate for controlled draft status. The chapter-opening absorption discipline held: Herbert's terms are strong, but the part updates existing truth, experience, sign, and faculty surfaces rather than opening a new glossary entry on first contact.

Verification result:

- PDF pages `222-227` were checked against scan/Tesseract output on `_0222`, `_0223`, `_0224`, `_0225`, `_0226`, `_0227`, and `_0228`. Scan `_0222` confirms the chapter opening; scan `_0227` confirms the stop before `Ein zweites Moment...`; scan `_0228` confirms the Digby material continues after the stop.
- The review corrected OCR residue around `einer . völlig`, `Cartesischen`, `Materialisten`, `Platon`, `mannigfach`, `Hertling`, `katholische Kirche`, `Keine Religion`, `die gleichen`, `Naturmacht`, `wahrhafte Siegel`, `waltet`, `Erfahrung`, `notitiae communes`, `nichts zu erfahren vermögen`, `eindringen`, `Sache`, `confirmatio`, `Vermögen`, `Wahrscheinlichkeit`, `Mittelpunkt`, and the Greek `κοιναὶ ἔννοιαι`.
- The substantive Latin footnotes on natural instinct and `notitiae communes` are translated in the draft-footnote layer. The body quote from Herbert on universal providence and the true catholic church is translated in the draft body.

## 2026-05-15 - Gassendi To Hobbes Bridge Note

Created `reading/2026-05-15-gassendi-to-hobbes-method-bridge.md` after the completed *Disquisitio metaphysica* source campaign.

Bridge finding:

- Gassendi exposes the problem that early empiricism must solve: experience cannot remain passive sensory reception because scientific objects require comparison, correction, abstraction, enlargement, naming, and relation.
- Hobbes gives the next methodological answer by making knowledge constructive: cause becomes a condition-aggregate, geometry supplies the model of demonstrability, names stabilize judgment, and nature is reconstructed after the destruction-of-the-world fiction.
- The answer is only partial. Hobbes's constructed principles then harden into absolute powers: body, matter, motion, sovereign convention, and external pressure.

Routing decision:

- Keep the bridge as a bounded reading note, not a glossary promotion or a new thread handle.
- Use it as a re-entry surface for Gassendi's *Syntagma* / *Physica*, Hobbes source work, and the Spinoza/Leibniz genetic-definition and symbolic-cognition line.
- Do not generalize it into a thesis about all empiricism or rationalism until the later Vol. 2 material is tested against it.

## 2026-05-15 - English Rationalism, Digby, Existence, And The Unity-Function

Created `parts/044-english-rationalism-digby-existence-and-unity-function.md` from PDF pages `227-235` / printed pages `207 partial-215 partial`, beginning with `Ein zweites Moment des gedanklichen Fortschritts...` and stopping before section `II.` / `Die Lehre Kenelm Digbys ist ein Beweis...`.

What this tranche clarified:

- Digby complements Herbert's truth/common-notion opening with an analysis of the thing and existence.
- Cassirer reads Digby as a paradoxical mediator: still scholastic-Aristotelian in physics and metaphysics, but already forcing a critical turn by making the dogmatic premise of thing/intellect agreement into a theory of active apprehension.
- The traditional species/image theory is rejected. Cognition is not a partial image of the thing, but the passage of the thing itself into the knowing I, even if the mode of that passage remains a mystery for Digby.
- Existence becomes the final irresolvable concept and the deepest means of thought. Every possible content must be grafted into the basic trunk of being before it can become knowledge.
- Relation, number, substantiality, and empirical judgment are all read back to a unity-function of the soul/consciousness. Judgment binds separated determinations through the copula `is` and makes them one for knowledge.

Structural center:

- The load-bearing movement is from scholastic agreement-theory to the mind's unity-function. Digby starts with truth as agreement between intellect and thing, sharpens it into a doctrine of the thing's presence in the knowing I, then turns existence and judgment into the formal means by which manifold content becomes knowable.

Routing decision:

- Add `Existenz / Sein / Ding` as an open glossary entry.
- Update `Wahrheit / Urteil`, `Realität / Entia Realia / Gedankendinge`, `Selbstbewußtsein / Ich / innere Erfahrung`, `Bild / Symbol / Ausdruck`, and `Begriff / Wort / Zeichen`.
- Keep `potentia comparativa`, `Einheitsfunktion der Seele / des Bewußtseins`, `Substantialität`, `Accidentien`, `Spezies`, `Apprehension`, `Grundstamm`, and `Ineinssetzen` in the close-reading ledger rather than opening separate entries from Digby alone.

Re-entry hooks:

- Part 045 should begin on PDF page `235` / printed page `215 partial` with section `II.` / `Die Lehre Kenelm Digbys ist ein Beweis...`.
- Cudworth and Norris should decide whether the chapter's center shifts from Digby's being/judgment analysis toward Platonism, intelligible being, faculty psychology, or common notions.
- Watch whether `Existenz / Sein / Ding` needs to merge with or split from `Realität / Entia Realia / Gedankendinge` once Locke tests thing, idea, and inner experience from the empiricist side.

Decision for now:

- Part 044 passes the same-agent self-review gate for controlled draft status. It opens one glossary entry, which is proportionate: Digby's section supplies a real new structural surface, while the other active terms serve that surface rather than demanding their own entries yet.

Verification result:

- PDF pages `227-235` were checked against scan/Tesseract output on `_0227`, `_0228`, `_0229`, `_0230`, `_0231`, `_0232`, `_0233`, `_0234`, and `_0235`. Scan `_0227` confirms the start at `Ein zweites Moment...`; scan `_0235` confirms the stop before section `II.`.
- The review corrected OCR residue around `notitiae communes`, `Mittelpunkt`, `Digby`, `Spezies`, `repräsentieren`, `Wirklichen`, `natürlichstes`, `Notio enim existentiae`, `universalissima`, `Ex iis`, `diligenter`, `postulant`, `insitionem`, `negotiatio omnis intellectus`, `Intellekt und Sinnlichkeit`, `sinnlicher`, `Bewußtseins`, `wachsen`, `Accidentien`, `Weise der Betrachtung`, `propriisque`, `Caeterae`, `Geulincx`, `Cartesischer`, `Erfahrungswirklichkeit`, `cuilibet`, `cujuslibet`, `simplicem`, `compositione`, `applicatione`, and `illos`.
- Substantive Latin footnotes 3-8 are translated in the draft-footnote layer. Bibliographic footnotes 1-2 remain source identifications.

## 2026-05-15 - English Rationalism, Cambridge Platonism, And Eternal Truths

Created `parts/045-english-rationalism-cambridge-platonism-and-eternal-truths.md` from PDF pages `235-244` / printed pages `215 partial-224`, beginning with section `II.` / `Die Lehre Kenelm Digbys ist ein Beweis...` and stopping before `Sechstes Buch. Das Erkenntnisproblem im System des Empirismus`.

What this tranche clarified:

- The English-rationalism chapter closes by turning from Digby's being/judgment analysis to Cambridge Platonism and Malebranche's English afterlife.
- Cudworth uses Platonism to fight sensationalism and materialism: atheism's theoretical assumption is that things make knowledge rather than knowledge making things.
- Mathematical knowledge supplies the methodical edge of the Platonist argument. It does not ascend from singulars to universals; it descends from universal definitions to singular application.
- Norris sharpens the issue into the being of eternal truths. If truth is relation, then eternal truths require enduring correlates or intelligible essences; otherwise science hangs on nothing.
- The objection that Norris confuses the being of the copula with concrete existence is named and answered: for Norris, the whole conditional judgment has absolute standing, and ideal truths require ideal objects.
- The chapter closes with sense subordinated to judgment. Sense cannot judge the existence of objects; even apparent sensory evidence of the external world depends on rational principles.
- Locke is introduced as the conscious reaction against this recurring rationalist view.

Structural center:

- The load-bearing movement is from intelligible world to Locke's starting problem. Cudworth gives Platonism a methodical formulation through mathematics and natural science; Norris converts eternal logical validity into categorical intelligible being; Locke will begin by separating the epistemological problem from speculative soul/God doctrine.

Routing decision:

- Add `intelligible Welt / ewige Wahrheiten` as an open glossary entry.
- Update `Wahrheit / Urteil`, `Existenz / Sein / Ding`, `Sinn / Sinneswahrnehmung`, `Realität / Entia Realia / Gedankendinge`, `Bild / Symbol / Ausdruck`, and `Selbstbewußtsein / Ich / innere Erfahrung`.
- Keep `Platonismus`, `Cudworth`, `Norris`, `Malebranche`, `plastische Naturen`, `nunc stans`, `Copula`, `hypothetisches / kategorisches Sein`, and `Locke reaction` in the close-reading ledger. The new intelligible-world entry is the right scale for the chapter close.

Re-entry hooks:

- Book V is closed. The next part should begin Book VI / Locke on PDF page `247` / printed page `227` with `Erstes Kapitel. Locke.`
- Read Locke as reaction against the rationalist thesis made explicit here: sense does not judge, and what is truly in the understanding was never in the senses in the proper sense.
- Test whether `intelligible Welt / ewige Wahrheiten` remains a chapter-local English-rationalist surface or becomes the direct foil for Locke's critique of innate principles, ideas, and the limits of understanding.
- Watch whether Locke's separation of the problem of objective value from speculative theories of soul and God changes the journal/routing shape for Book VI; do not carry Cambridge's theological-metaphysical frame forward as the default.

Decision for now:

- Part 045 passes the same-agent self-review gate for controlled draft status. The English-rationalism chapter is complete as controlled draft. Its glossary growth stayed proportionate: Herbert opened none, Digby opened `Existenz / Sein / Ding`, and the Cambridge close opened `intelligible Welt / ewige Wahrheiten`.

Verification result:

- PDF pages `235-244` were checked against scan/Tesseract output on `_0235`, `_0236`, `_0237`, `_0238`, `_0239`, `_0240`, `_0241`, `_0242`, `_0243`, and `_0244`. Scan `_0235` confirms the section `II.` start; scan `_0244` confirms the chapter close; scan `_0245` confirms the Book VI title page; scan `_0247` confirms Locke begins after the stop.
- The review corrected OCR residue around `Platonismus`, `Schule von Cambridge`, `Cudworth`, `philosophischem`, `Tummelplatz`, `intelligible Naturen`, `contrary`, `Descending apply them`, `is not`, `relations`, `Immutable Verities`, `Noemata and Ideas`, `Wahrheit der intellektuellen Welt`, `Hobbes`, `plastischen Naturen`, `John Norris`, `vollen Deutlichkeit`, `S. hierzu`, `Theory`, `Part II: London 1704`, `Aussagen`, `Correlates`, `Reverie`, `Copula`, `Suarez`, `Argument`, `vorhandenen`, `nunc stans`, `Form`, `Sinnlichkeit`, `That`, `ein kategorisches`, `having`, `conviction`, `existiert`, `die in uns und zu uns spricht`, `Wie Digby`, and `Lockes`.
- Cudworth and Norris quotations are already English in Cassirer's apparatus. The draft footnotes preserve references and summarize the load-bearing quoted claims rather than retranslating English into English.

## 2026-05-15 - Locke, Critical Method, And Innate Ideas

Created `parts/046-locke-critical-method-and-innate-ideas.md` from PDF pages `247-252` / printed pages `227-232 partial`, beginning with `Erstes Kapitel. Locke.` and stopping before section `I. Sensation und Reflexion.`

What this tranche clarified:

- Locke's originality is not that he first discovers the problem of knowledge. Cassirer frames Descartes and the English rationalists as already having posed it.
- Locke's decisive move is separation: the question of the objective value and limits of knowledge is detached from metaphysical and natural-scientific theories of the soul and its faculties.
- The Cartesian method problem carries into Locke through the atmosphere created by the `Regeln`, Port-Royal, and Malebranche, whether or not Locke knew the `Regeln` directly.
- Locke's psychological method is not physiology or metaphysics. It observes and analyzes psychic phenomena without deciding their physical or metaphysical primal ground.
- The critique of innate ideas is not the essential result of Locke's philosophy. It is a clearing operation that removes a fictive explanatory ground and defines the field in which the question must move.
- Cassirer blocks a flat empiricist reading: Locke does not deny universal and necessary principles; he denies that they are available as a finished innate possession.
- Genetic derivation is the indispensable aid of logical analysis. Temporal genesis matters only as a passage toward analysis of the content of representations.

Structural center:

- The load-bearing movement is from rationalist foil to critical boundary-determination. Part 045 closed by making sense depend on judgment and eternal truths depend on intelligible being; Part 046 opens Locke by separating the knowledge problem from that theological-metaphysical frame while preserving the rational demand for principles and critical grounding.

Routing decision:

- No new glossary entry yet. The chapter opening names `angeborene Ideen`, `genetische Ableitung`, `psychologische Methode`, and `Grenzbestimmung des Verstandes`, but section `I. Sensation und Reflexion` should decide which of these becomes the first Locke-specific glossary surface.
- Update `Erfahrung`, `Sinn / Sinneswahrnehmung`, `Wahrheit / Urteil`, `intelligible Welt / ewige Wahrheiten`, `Begriff / Wort / Zeichen`, and `Selbstbewußtsein / Ich / innere Erfahrung`.
- Keep `angeborene Ideen / angeborene Wahrheiten`, `genetische Ableitung`, `psychologische Methode`, `Grenzbestimmung des Verstandes`, `historical plain method`, `Vernunftforschung`, and `Aufklärungsphilosophie` in the close-reading ledger.

Re-entry hooks:

- Part 047 should begin with section `I. Sensation und Reflexion` on PDF page `252` / printed page `232 partial`.
- Test whether `Sensation / Reflexion` earns a new glossary entry immediately or first updates `Sinn / Sinneswahrnehmung`, `Selbstbewußtsein / Ich / innere Erfahrung`, and `Erfahrung`.
- Track whether Locke's `reine Erfahrung` remains a methodological field for genetic-logical analysis or begins to narrow toward sense-data doctrine.
- Preserve the Part 046 anti-simplification: Locke's empiricism is carried by a rational Enlightenment intention, not by rejection of universal validity.

Decision for now:

- Part 046 passes the same-agent self-review gate for controlled draft status. This is only the chapter opening, so no larger Locke chapter goal should be assumed until Part 047 tests the sensation/reflection burden.

Verification result:

- PDF pages `247-252` were checked against scan/Tesseract output on `_0247`, `_0248`, `_0249`, `_0250`, `_0251`, and `_0252`. Scan `_0247` confirms `Erstes Kapitel. Locke.`; scan `_0252` confirms the stop before section `I. Sensation und Reflexion.`
- The review corrected OCR residue around `Burthogge`, `Seele`, `Gegenständen sie`, `Erkenntnis`, `Baillet`, `Recherche de la vérité`, `gekannt`, `Grenzbestimmung`, `daß alle`, `Hobbes`, `Malebranche`, `konnte. Sie`, `Vorstellungen zu haben`, `historical plain method`, `Essay`, `Angeborene`, `Evidenz`, `Fraser`, `self-evidence`, `something else`, `nobody`, `hierzu`, `wie weit`, and `ruhen`.
- Footnotes were renumbered sequentially for the continuous part file. Locke's English phrase `in this historical plain method` is preserved in the draft; the English self-evidence quotation is summarized in the draft-footnote layer because the source quote is already in English.

## 2026-05-15 - Locke, Sensation, Reflection, And Simple Ideas

Created `parts/047-locke-sensation-reflection-and-simple-ideas.md` from PDF pages `252-257` / printed pages `232 partial-237 partial`, beginning with section `I. Sensation und Reflexion` and stopping before `Ueber diese Begriffsbestimmung der Reflexion ist Locke...`.

What this tranche clarified:

- Locke's source-pair is not self-explanatory. "All knowledge consists in sensation and reflection" is so indeterminate that empiricist, materialist, intellectualist, critical, and dogmatic readings can all claim it.
- Cassirer therefore makes `Reflexion` the first problem of the section. In its original sense, reflection is an optical mirroring of inner processes, just as sensation is a copy of external things.
- In this first schema, sensation and reflection stand on the same passive level: the mind receives and reproduces contents that confront it.
- This blocks a simple sensualist reading because sense- and self-perception are equally independent and indispensable factors of knowledge.
- The cost is an element-model of consciousness: psychic functions and logical relations count only insofar as they harden into fixed individual representations.
- Locke's merit is that he follows the fact of knowledge closely enough that this original schema will be progressively criticized from within.
- The first widening of `Reflexion` appears when it names connection, comparison, joining, and separating; but these activities still remain arbitrary operations without objective stock or support.

Structural center:

- The load-bearing movement is from dual source to passive element-schema. Sensation and reflection split experience into two moments, but both are initially treated as fixed contents. Cassirer neither flattens Locke into sensualism nor yet grants reflection genuine logical activity; he shows the starting schema that later scientific concepts will strain.

Routing decision:

- Add `Sensation / Reflexion` as an open glossary entry.
- Update `Erfahrung`, `Sinn / Sinneswahrnehmung`, `Selbstbewußtsein / Ich / innere Erfahrung`, `Begriff / Wort / Zeichen`, and `Bild / Symbol / Ausdruck`.
- Keep `Idee / Vorstellung`, `einfache Ideen`, `mixed modes`, `Verbindung`, `seelische Tätigkeit`, `psychologischer Dogmatismus`, and `Verfestigung` in the close-reading ledger for now rather than opening separate entries from the first section unit.

Re-entry hooks:

- Part 048 should begin on PDF page `257` / printed page `237 partial` with `Ueber diese Begriffsbestimmung der Reflexion ist Locke...`.
- Test whether the infinity analysis turns `Reflexion` from passive mirror into necessary mental function.
- Watch whether `Unendlichkeit / Zahl / Raum` earns a new surface or whether it should update `Sensation / Reflexion`, `Raum / Zeit`, `Begriff / Wort / Zeichen`, and `Wahrheit / Urteil`.
- Track whether `Idee / Vorstellung` remains absorbed by `Sensation / Reflexion` or becomes its own Locke-specific problem.

Decision for now:

- Part 047 passes the same-agent self-review gate for controlled draft status. It justifies the first Locke-specific glossary entry, but the next tranche must decide whether the section's center shifts from the source-pair itself to infinity, space, and scientific concept-formation.

Verification result:

- PDF pages `252-257` were checked against scan/Tesseract output on `_0252`, `_0253`, `_0254`, `_0255`, `_0256`, and `_0257`. Scan `_0252` confirms the section start after the Part 046 close; scan `_0257` confirms the stop before the next paragraph beginning `Ueber diese Begriffsbestimmung der Reflexion...`.
- The review corrected OCR residue around `unbefangen`, `lediglich seinen`, `besteht`, `schwierigen Terminus`, `daß`, `Locke`, `Hertling`, `ursprünglich für Locke`, `merkwürdige`, `wider`, `so wenig`, `bewirken`, `Begriff des Einfachen`, `Philosophie`, `ihrem`, `Tätigkeit`, `Verbindung`, `Vorstellungsgebilde`, `ungewisse`, and `Of discerning and other operations of the mind`.

## 2026-05-15 - Part 018 Campanella Absorption Back-Ported

Applied the Campanella source campaign's Vol. 2 Part 018 crosswalk back into `parts/018-spinoza-intuition-renaissance-and-the-short-treatise.md` without opening new Latin in this pass.

What changed:

- Footnote 6 now records that Cassirer's `intrinsecatio, per quam unum fit aliud` anchor is verified at Campanella leaf 906 / Pars III, Liber XVII, Caput II, Articulus I, while its local register is beatitude and gustation rather than a free-standing law of all cognition.
- Footnote 7 now records that Cassirer's Part II p. 78 `saporem` quotation is verified at leaf 444 and adds the hidden-love / hidden-self-sense pairing (`Amor abditus`, `sensus abditus`) as source-context.
- Footnote 8 now preserves Cassirer's power/love/wisdom exposition while noting that the opened Part II primalities locus gives the doctrinal order as `Potentia, Sapientia, & Amor`.
- The part notes, close-reading ledger, and `Intuition / Anschauung` glossary entry now carry the source-contact qualification: Cassirer's Campanella bridge is right, but too smooth if reused as a claim that all Campanellan cognition is self-dissolution into the object.

Routing decision:

- Keep the translation of Cassirer's German paragraph faithful. The correction belongs in the footnote and notes layer, because the primary task here is not to rewrite Cassirer's claim but to mark what the opened Campanella Latin now lets us say about its reach.
- Use `sources/latin/campanella-metaphysica/reading/cassirer-vol2-part018-intrinsecation-crosswalk.md` before opening additional Campanella Latin for this Spinoza passage.

## 2026-05-15 - Part 018 Campanella Back-Port Review And Reading Note

Reviewed the Part 018 back-port after the Campanella absorption edits. Checked:

- `parts/018-spinoza-intuition-renaissance-and-the-short-treatise.md`
- `reading/close-reading-ledger.md`
- `source/glossary.yaml` entry `Intuition / Anschauung`
- this journal's back-port entry

Decision: a short Cassirer-side reading note is warranted after all, but only because the sidebar review surfaced a synthesis need that the local back-port did not carry: the argument-walk from bodily taste to beatific `intrinsecatio`, and especially the bridge between leaf 402's hidden self-intellection and leaf 444's hidden self-love / hidden self-sense.

Created `reading/2026-05-15-campanella-part018-absorption-note.md`. Its job is not to replace the source-side crosswalk and not to open new Latin. It gives a compact Cassirer-side use-rule: keep Cassirer's historical bridge, qualify it as "right, but too smooth," and treat the `abditus` family as a re-entry point only if later Spinoza work requires the relation between self-activity, love of God, and intuitive cognition to be traced back through Campanella.

## 2026-05-15 - Locke, Infinity, Reflection, And Necessary Function

Created `parts/048-locke-infinity-reflection-and-necessary-function.md` from PDF pages `257-262` / printed pages `237 partial-242 partial`, beginning with `Ueber diese Begriffsbestimmung der Reflexion ist Locke...` and stopping before `Der gleiche Fortgang, der hier hervortritt...`.

What this tranche clarified:

- Part 048 answers the hook from Part 047. Locke's application of the sensation/reflection principle to scientific concepts forces a substantive transformation of the principle itself.
- `Reflexion` cannot remain passive imprint if it must explain the infinite. The infinite is not an observed content and not a merely arbitrary continuation of representations.
- Sensation and reflection now confront one another as factors with different logical character and validity-value.
- Cassirer distinguishes psychological possibility from logical necessity. The number series does not mean merely that we can proceed from a number to a higher one; it means that this continuability is set and required by the concept of number.
- Locke's own examples undermine his initial explanation. The sailor's lead that never reaches the seabed gives only negative evidence, not a justified concept of infinity.
- The result is a forced widening of reflection: the infinite becomes a necessary activity of mind and fuses with the image of objective actuality even if Locke's original schema cannot justify that fusion.

Structural center:

- The load-bearing movement is from arbitrary connection to necessary function. Part 047 showed reflection widening from mirror to connection, but still as arbitrary operation; Part 048 shows scientific cognition requiring a rule and method by which an unfinishable series can be surveyed conceptually.

Routing decision:

- No new glossary entry yet. The infinity problem is central, but it is functioning as the first internal transformation of `Sensation / Reflexion`, not yet as a separate durable surface.
- Update `Sensation / Reflexion`, `Wahrheit / Urteil`, `Kontinuum / Stetigkeit / Infinitesimal`, `Raum / Zeit`, `Begriff / Wort / Zeichen`, and `Erfahrung`.
- Keep `Unendlichkeit`, `Zahl`, `potentielle / aktuelle Unendlichkeit`, `Vermögen`, `Dasein / Existenz`, and `wissenschaftliche Begriffe` in the close-reading ledger until the space/time/force analyses decide whether one of them needs promotion.

Re-entry hooks:

- Part 049 should begin on PDF page `262` / printed page `242 partial` with `Der gleiche Fortgang, der hier hervortritt...`.
- The next tranche should test whether `Raum / Zeit` becomes the next Locke-specific pressure or remains an application of the same reflection/function problem.
- Watch whether `Kraft`, `Dasein / Existenz`, and empirical physics begin to shift the chapter center away from infinity and toward the foundations of empirical physics.

Decision for now:

- Part 048 passes the same-agent self-review gate for controlled draft status. This is the calibration tranche needed before a larger Locke goal: it confirms that the chapter can proceed section-bounded, but the goal should still require self-review and chapter-level ratification before completion.

Verification result:

- PDF pages `257-262` were checked against scan/Tesseract output on `_0257`, `_0258`, `_0259`, `_0260`, `_0261`, and `_0262`; `_0263` was checked to confirm the next boundary. Scan `_0257` confirms the start after the Part 047 closing sentence and footnote; scan `_0262` confirms the stop before `Der gleiche Fortgang...`.
- The review corrected OCR residue around `Erklärung der wissenschaftlichen Begriffe`, `Sinnen- und Selbstwahrnehmung`, `Die Naivität`, `Vorstellungsinhalt`, `noch größer`, `anzuspornen`, `Und`, `verbannen`, `zusprechen`, `ein allgemeines Urteil`, `Unabschließbarkeit begrifflich zu beherrschen`, `gedrängt`, `darbietet`, `verschwommen`, `notwendige Betätigung`, `Einzeldaten`, and `objektive Wirklichkeit`.

## 2026-05-15 - Parts 019-030 Campanella Qualification Audit

Audited the already translated Spinoza stretch after the Part 018 Campanella note, without opening new Campanella Latin and without translating new Cassirer text.

Scope checked at apparatus level first:

- Part notes / re-entry hooks for `parts/019` through `parts/030`
- close-reading ledger entries from `Spinoza: True Idea And Immanent Criterion` through `Spinoza: Thought Attribute and Anthropomorphism`
- glossary entries `Intuition / Anschauung`, `Substanz / Modi / Attribute`, and `Ursache / Bedingung / Erzeugung`
- the ledger pressure around `intellektuelle Liebe zu Gott` in Part 027

Decision: the Campanella qualification should remain localized to the Part 018 / Part 027 interface for now. No later translated part needs wording changes. The later apparatus already preserves the necessary development:

- Part 019 reverses the `Short Treatise` posture from passive/mystical possession into methodical acquisition of the true idea.
- Part 021 makes intuition the mind's highest self-activity rather than surrender to alien being.
- Parts 023-030 move the problem into substance, order, attributes, thought, and the anthropomorphism of geometry, not into another Campanella source question.
- Part 027 is the only later pressure point where the Campanella note matters directly: `intellektuelle Liebe zu Gott` names the residual Renaissance affective motive as it passes into mathematical order. The new `abditus` bridge is useful as a re-entry route if later work needs to trace self-activity, love of God, and intuitive cognition back through Campanella, but it does not currently require changing the Part 027 apparatus.

So the current Cassirer-side rule holds: use the new `reading/2026-05-15-campanella-part018-absorption-note.md` as a compact synthesis layer, keep `Intuition / Anschauung` as the retrieval hook, and do not widen the Campanella qualification across Parts 019-030 unless a later Spinoza revision creates a concrete question that the existing note cannot answer.

## 2026-05-16 - Locke, Space, Time, Number, And Objective Existence

Created `parts/049-locke-space-time-number-and-objective-existence.md` from PDF pages `262-273` / printed pages `242 partial-253 partial`, beginning with `Der gleiche Fortgang, der hier hervortritt...` and closing section `I. Sensation und Reflexion` before section `II. Der Begriff der Wahrheit.`

What this tranche clarified:

- Part 049 carries Part 048's transformation of reflection across the remaining scientific concepts of section `I`.
- Locke's early space doctrine tends toward a consistent empiricist and relational account: space is relation among bodies and becomes a reified illusion if detached from the things whose distances it names.
- The `Essay` abandons that consistency under pressure from empirical physics. Motion requires pure space distinct from body if it is to be comprehended and "saved."
- The time analysis makes reflection more than passive inner mirroring: reflection now supplies the criterion and control by which sensory changes are measured.
- Number exposes the deepest pressure on the simple-idea schema: two and three are not representational images but logical functions that presuppose and distinguish one another conceptually.
- Section `I` closes by naming Locke's limit. Simple ideas are treated as immediate warrants for external things, so sensation/reflection become mediators while substances and real effects remain the uncomprehended real ground of knowledge.

Structural center:

- The load-bearing movement is from scientific concept-pressure to metaphysical remainder. Space, time, and number all push Locke beyond passive sensation/reflection, but instead of producing a critical account of validity, section `I` leaves the reality of external things as a dogmatic guarantee attached to simple sensation.

Routing decision:

- No new glossary entry. The section close intensifies existing surfaces rather than creating a new one.
- Update `Raum / Zeit`, `Sensation / Reflexion`, `Erfahrung`, `Bewegung`, `Körper / Materie / Substanz`, `Existenz / Sein / Ding`, `Bild / Symbol / Ausdruck`, `Begriff / Wort / Zeichen`, and `Wahrheit / Urteil`.
- Keep `leerer Raum`, `Ort / Ausdehnung`, `Dauer`, `Zahl`, `Gedankenalphabet`, `einfache Ideen`, `sekundäre Qualitäten`, `Original`, `Realgrund`, `Subjekt / Objekt`, and `Kraft / Verursachung` in the close-reading ledger until sections `II` and `III` test whether any become durable Locke surfaces.

Section-I ratification:

- Parts 047-049 remain controlled draft. The section's provisional finding is stable enough to guide section `II`: Locke's genetic psychology repeatedly discovers logical function inside experience but lacks a critical validity account, so it falls back on the external thing as real ground.
- Do not write a bounded Locke reading note yet. The truth section must decide whether Locke's concept of truth repairs, repeats, or deepens the section-I remainder.

Re-entry hooks:

- Part 050 should begin on PDF page `273` / printed page `253 partial` with section `II. Der Begriff der Wahrheit.`
- Test whether `Wahrheit / Urteil` becomes the next Locke-specific surface, or whether section `II` remains an update to `Sensation / Reflexion`, `Begriff / Wort / Zeichen`, and `Existenz / Sein / Ding`.
- Preserve the anti-simplification from section `I`: Locke is not flat sense-data empiricism; Cassirer is showing a method that discovers logical functions but cannot yet justify their objective validity.

Decision for now:

- Part 049 passes the same-agent self-review gate for controlled draft status. Because it closes section `I`, the next tranche should start section `II` with the section-I ratification explicitly in view.

Verification result:

- PDF pages `262-273` were checked against scan/Tesseract output on `_0262`, `_0263`, `_0264`, `_0265`, `_0266`, `_0267`, `_0268`, `_0269`, `_0270`, `_0271`, `_0272`, and `_0273`. Scan `_0262` confirms the start after Part 048's closing dash; scan `_0273` confirms the section-I close and the next boundary at `II. Der Begriff der Wahrheit.`
- The review corrected OCR residue around `Locke`, `versch\Yommen`, `Verknüpfungen`, `Einzeldaten`, `objektiven Wirklichkeit`, `einfache`, `Er beginnt`, `Hobbes'`, `Space`, `Vernichtung`, `reinen Raumes`, `Gassendi`, `Newton`, `leeren Raumes`, `Unterscheidung`, `Wort`, `retten`, `Henry More`, `psychologischen Bestimmungen`, `succession`, `successive`, `und eine Forderung`, `Vorstellungsfunktionen in feste`, `Modi`, `Bewußtseinsinhalte`, `unbezweifelbaren`, `äußeren, dinglichen`, `product`, `in a natural way`, `sekundären Qualitäten`, and `Subjekt` / `Objekt`.

## 2026-05-16 - Locke, Concept Of Truth, Intuition, And Experience

Created `parts/050-locke-concept-of-truth-intuition-and-experience.md` from PDF pages `273-283` / printed pages `253 partial-263 partial`, beginning with section `II. Der Begriff der Wahrheit.` and stopping before section `III. Der Begriff des Seins.`

What this tranche clarified:

- Section `II` tests the section-I finding by shifting from the first two books of the `Essay` to the fourth book.
- The starting point changes from psychological source-analysis to logical validity. Universal and universally valid relations now stand at the beginning.
- Locke separates from Hobbes's nominalism at the decisive point: mathematical signs help memory, but they do not ground the generality of mathematical judgment.
- The `Idee` now gains a logical nature. It is no longer a movable representational element, but a content that has a determinate place in a system of presuppositions and derivations.
- `Intuition` becomes the foundation of certainty. Mathematics and morals have genuine knowledge because they concern necessary connections among ideas.
- Natural science is excluded from strict science. It remains probable experience because the lawful bond among bodily properties cannot be deduced from the sensory facts.
- Locke is therefore an empiricist from resignation in natural philosophy, not from Baconian confidence in experience as the mother of science.
- The section closes by turning the critique back on Locke's own psychology: if outer and inner experience are merely momentary perceptions, neither can ground constant things, objective validity, or the whole of cognition.

Structural center:

- The load-bearing movement is from psychological source-analysis to logical critique of experience. Section `II` does not repair the section-I remainder; it sharpens it. Locke discovers a truth-standard higher than induction and experience, but that standard splits being and knowing apart again.

Routing decision:

- No new glossary entry. `Wahrheit / Urteil` becomes dominant, but the existing entry can absorb this Locke pressure for now.
- Update `Wahrheit / Urteil`, `Intuition / Anschauung`, `Sensation / Reflexion`, `Erfahrung`, `Experiment`, `Begriff / Wort / Zeichen`, `Bild / Symbol / Ausdruck`, `Existenz / Sein / Ding`, `Sinn / Sinneswahrnehmung`, and `Körper / Materie / Substanz`.
- Keep `Intuition`, `Idee`, `Moral`, `Naturwissenschaft / natural philosophy`, `scientifical knowledge`, `philosophische Erfahrungstheorie`, `primäre Qualitäten`, `innere Erfahrung`, and `Grenzen der Erkenntnis` in the close-reading ledger until section `III` tests them through being and substance.

Section-II ratification:

- Parts 047-050 remain controlled draft. Section `II` strengthens the candidate chapter finding: Locke's empiricism becomes a logical critique of experience precisely where it despairs of making experience strict science.
- Do not promote this to a bounded Locke reading note yet. Section `III` must decide whether the being/substance critique repeats this rupture or transforms it.

Re-entry hooks:

- Part 051 should begin on PDF page `283` / printed page `263 partial` with section `III. Der Begriff des Seins.`
- Test whether the concept of being supplies a distinct Locke surface around `Substanz / Ding / Träger`, or whether it remains absorbed by `Existenz / Sein / Ding`, `Körper / Materie / Substanz`, and `Sensation / Reflexion`.
- Watch `primäre Qualitäten`, `Ich`, and `innere Erfahrung`: section `II` has already argued that both outer and inner experience fall into probability if stripped of thought functions.

Decision for now:

- Part 050 passes the same-agent self-review gate for controlled draft status. The next tranche begins the final Locke section and should carry the section-II ratification explicitly.

Verification result:

- PDF pages `273-283` were checked against scan/Tesseract output on `_0273`, `_0274`, `_0275`, `_0276`, `_0277`, `_0278`, `_0279`, `_0280`, `_0281`, `_0282`, and `_0283`. Scan `_0273` confirms the section-II start after Part 049's close; scan `_0283` confirms the stop before `III. Der Begriff des Seins.`
- The review corrected OCR residue around `Subjekt`, `Objekt`, `Der Begriff der Wahrheit`, `ursprünglichen`, `Einzelfiguren`, `phänomenologische`, `mathematischen`, `nominalistischen`, `The cyphers`, `numerical`, `hervorwagen`, `richtet`, `Schwarz`, `völlig neuer`, `künftigen`, `Wissensobjekten`, `Strukturverhältnisse`, `Empirismus`, `zu verstehen`, `industry`, `scientifical`, `examination`, `capable`, `matters`, `getting and improving`, `getrennte Welten`, `Lockes`, `hierzu`, `Untersuchungen`, `zu einem`, and `Sprengung`.

## 2026-05-16 - Locke, Substance, Being, And Metaphysical Transcendence

Created `parts/051-locke-substance-being-and-metaphysical-transcendence.md` from PDF pages `283-294` / printed pages `263 partial-274`, beginning with section `III. Der Begriff des Seins.` and closing the Locke chapter before `Zweites Kapitel. Berkeley.`

What this tranche clarified:

- Section `III` confirms the candidate Locke finding from sections `I-II`.
- Locke's critique of substance first looks like the successful self-dissolution of metaphysics: substance is an unknown bearer, a mere word, and an `idolon fori`.
- The critique cannot silence the problem because Locke still needs the unknown bearer for objecthood, for the world of appearance, and for the scientific ideal of knowledge from causes.
- The standpoint reverses: sensation and reflection initially judge substance as dark and unclear, but substance then becomes true being, inaccessible only because of defects in our faculties.
- Cassirer locates the defect in Locke's question-form, not in the substance concept alone. Locke seeks substance as a separate sensory or psychical image rather than as a necessary function in the system of knowledge.
- The closing reality analysis repeats the truth-section problem. Mathematical objects have their archetype in thought; sensory ideas require comparison with actual things, but Locke's own logic of ideas cannot perform that comparison.
- The chapter closes by distinguishing two problems Locke fuses: the objective certainty of empirical cognition and the metaphysical transcendence of a corporeal world existing in itself.

Structural center:

- The load-bearing movement is from critique of substance to critique of the question-form. Locke's psychological analysis discovers that substance is not an isolated content, but because he lacks a functional account of its role in cognition, substance returns as thing-like transcendence.

Routing decision:

- No new glossary entry. Update `Existenz / Sein / Ding`, `Körper / Materie / Substanz`, `Sensation / Reflexion`, `Wahrheit / Urteil`, `Erfahrung`, `Bild / Symbol / Ausdruck`, `Begriff / Wort / Zeichen`, `Selbstbewußtsein / Ich / innere Erfahrung`, and `Intuition / Anschauung`.
- Keep `Substanz / Träger`, `idolon fori`, `Form / Materie`, `Urbild / Archetyp`, `einfache Empfindung`, `objektive Gewißheit der empirischen Erkenntnis`, and `metaphysische Transzendenz der Körperwelt` in the close-reading ledger and bounded note rather than opening separate entries.
- Add `reading/2026-05-16-locke-experience-validity-and-transcendence.md` as the bounded Locke chapter note.

Chapter-close ratification:

- Parts 046-051 remain controlled draft.
- The chapter finding is now earned: Locke's empiricism becomes philosophically sharp where its psychological source-analysis uncovers logical functions, objective norms, and necessary relations it cannot ground; lacking a critical account of empirical objectivity, Locke displaces that objectivity into unknowable things and substances beyond cognition.
- Keep this chapter-local until Berkeley tests it. Do not make it a Book VI thesis yet.

Re-entry hooks:

- Part 052 should begin on PDF page `295` / printed page `275` with `Zweites Kapitel. Berkeley.`
- Berkeley should test the Locke close directly: does removing the unknowable corporeal thing clarify empirical objectivity, or does it also unsettle the logical foundations of experience?
- Watch `Dingbegriff`, `Außenwelt`, `Wahrnehmung`, `Skepsis`, and `psychologischer Prozeß` as possible Berkeley surfaces.

Decision for now:

- Part 051 passes the same-agent self-review gate for controlled draft status. The Locke chapter is complete at controlled-draft tier, with a bounded chapter note and a Berkeley re-entry test.

Verification result:

- PDF pages `283-294` were checked against scan/Tesseract output on `_0283`, `_0284`, `_0285`, `_0286`, `_0287`, `_0288`, `_0289`, `_0290`, `_0291`, `_0292`, `_0293`, and `_0294`; `_0295` was checked to confirm the next chapter boundary at `Zweites Kapitel. Berkeley.`
- The review corrected OCR residue around `Substanzbegriffs`, `Der Begriff des Seins`, `Selbstauflösung`, `Bewußtsein`, `endgültige`, `Realität`, `äußeren`, `Zuständlichkeiten`, `Aufeinanderfolge`, `sine re substante`, `idolon fori`, `bewahrt`, `unanalysierbaren`, `Träger`, `solidity`, `chief`, `empirisches`, `adäquates`, `geistigen Naturen`, `Substanzbegriff`, `oberflächlichen Vorstellungen`, `unserer subjektiven Fähigkeiten`, `Mangel der Lockeschen Fragestellung`, `zutage`, `Vorstellungsreste`, `einfache`, `Relation`, `Archetyp`, `their archetypes`, `ursprünglichen Definitionen`, `zusammenstimmen`, `Erkenntnismitteln`, `physikalische`, and `metaphysischen Transzendenz`.

## 2026-05-16 - Berkeley, Perception, Vision, And Suggestion

Created `parts/052-berkeley-perception-vision-and-suggestion.md` from PDF pages `295-304` / printed pages `275-284 partial`, beginning with `Zweites Kapitel. Berkeley.` and section `I. Die Theorie der Wahrnehmung`, and stopping before section `II. Die Begründung des Idealismus.`

What this tranche clarified:

- Berkeley opens as the direct test of the Locke chapter close.
- Locke left the external world as a condition and origin of experience rather than a product of experience. Berkeley turns that leftover into the first problem of empirical psychology: the external object must be derived as a result of a necessary psychological process.
- Sight supplies only light and color, not distance, external things, or spatial articulation. Space and distance belong to the finished representation-world, but they are not immediately perceived.
- Berkeley first follows Descartes and Malebranche in treating sensations as signs rather than copies, but he rejects their unconscious geometry because it does not belong to consciousness itself.
- The Molyneux case supplies the decisive test: visible and tangible contents have no inner similarity, so their relation is learned through experience, association, habit, and custom.
- Berkeley's term `suggested` names the section's hinge. It supplements bare perception by explaining how one sensory field calls up another, but it does not yet supply a self-conscious logical function.

Structural center:

- The load-bearing movement is from given object to suggested object. Objectivity is not present in isolated sensation; it is produced when heterogeneous sensory fields are interpreted, judged, and habitually correlated.

Routing decision:

- No new glossary entry yet. `Wahrnehmung / Perzeption / Suggestion` is strongly active, but section `II` should decide whether it becomes Berkeley's durable surface or remains the vision-theory route into the critique of corporeal transcendence.
- Update `Erfahrung`, `Sensation / Reflexion`, `Sinn / Sinneswahrnehmung`, `Raum / Zeit`, `Wahrheit / Urteil`, `Existenz / Sein / Ding`, `Bild / Symbol / Ausdruck`, and `Begriff / Wort / Zeichen`.
- Keep `Wahrnehmung / Perzeption / Suggestion`, `Dingbegriff`, `Außenwelt`, `Urwahrnehmung`, `Assoziation`, `habit and custom`, `psychologische Methode`, `unbewußte Geometrie`, and `Naturtrieb des Bewußtseins` in the close-reading ledger.

Re-entry hooks:

- Part 053 should begin on PDF page `304` / printed page `284 partial` with section `II. Die Begründung des Idealismus.`
- The next tranche should test whether Berkeley removes the residual privilege of touch and extends the theory of visual signs into full idealism.
- Watch whether the chapter center stays with perception/suggestion or shifts toward the critique of corporeal transcendence and the grounding of empirical objectivity.
- Do not turn the Locke chapter finding into a Book VI thesis yet. Berkeley has begun to dissolve Locke's transcendent thing, but the first solution routes objectivity through habit and suggestion rather than through a critical account of logical validity.

Decision for now:

- Part 052 passes the same-agent self-review gate for controlled draft status. It opens the Berkeley chapter cleanly and sets up section `II` as the test of whether suggestion remains local to vision or becomes the chapter's governing surface.

Verification result:

- PDF pages `295-304` were checked against scan/Tesseract output on `_0295`, `_0296`, `_0297`, `_0298`, `_0299`, `_0300`, `_0301`, `_0302`, `_0303`, and `_0304`; `_0305` was checked to confirm that section `II. Die Begründung des Idealismus` has already begun.
- The review corrected OCR residue around `Bewußtsein`, `Einsicht`, `Außenwelt`, `schon`, `Wissens`, `Ideen`, `Natur`, `Außen`, `Innen`, `aneinanderreihen`, `Wahrnehmung`, `Prägnanz`, `nature`, `sight`, `wechselseitigen`, `Symbole`, `schematische`, `Befestigung`, `nicht`, `Einheit`, `unbewußten`, `psychologischen`, `angenommen`, `daher`, `Menschen`, `einzige`, `Eindrücken`, `Logik`, `Identität`, `Molyneux`, `Würfels`, `Gemeinschaft`, `Übung`, `suggested`, `imagination`, and `faculty`.

## 2026-05-16 - Berkeley, Idealism, Existence, And Nature Law

Created `parts/053-berkeley-idealism-existence-and-nature-law.md` from PDF pages `304-317` / printed pages `284 partial-297 partial`, beginning with section `II. Die Begründung des Idealismus.` and stopping before section `III. Kritik der Berkeleyschen Begriffstheorie.`

What this tranche clarified:

- Berkeley removes the residual privilege of touch that remained in the `New Theory of Vision`. Tangible extension can no longer stand as real extension outside consciousness.
- The critique of abstract concepts becomes a bridge to the critique of one fatal abstraction: `Dasein` understood as thing-like existence outside consciousness.
- `Esse = percipi` is not rendered as momentary sense-content. Its critical sense depends on `Perzeption` as present content plus associative relations, possible perceptions, and the empirical context represented through it.
- Berkeley and Leibniz nearly coincide in defining appearance-reality by constancy and lawful order, but Cassirer marks the decisive method difference: Leibniz grounds order in rational rules, Berkeley in empirical association.
- Nature law becomes the correlate of Berkeley's reality concept. Science describes coexistence and regular sequence of phenomena; forces, absolute causes, and absolute space/time are rejected as experience-unconfirmed additions.

Structural center:

- The load-bearing movement is from suggested object to law-governed appearance-reality. The same sign/suggestion structure that explained vision now explains empirical reality: present perceptions symbolize a regulated whole of possible experience, not absolute things outside mind.

Routing decision:

- Add `Wahrnehmung / Perzeption / Suggestion` as an open Berkeley glossary entry.
- Update `Erfahrung`, `Sensation / Reflexion`, `Sinn / Sinneswahrnehmung`, `Raum / Zeit`, `Wahrheit / Urteil`, `Existenz / Sein / Ding`, `Bild / Symbol / Ausdruck`, `Phänomen / Erscheinung`, `Begriff / Wort / Zeichen`, `Körper / Materie / Substanz`, and `Bewegung`.
- Keep `Naturgesetz`, `absolute Materie`, `primäre / sekundäre Qualitäten`, `Terminismus`, `Urwahrnehmungen`, `Natur der Dinge`, `esse = percipi`, `De motu`, and `immanente Kritik` in the close-reading ledger rather than opening separate entries.

Re-entry hooks:

- Part 054 should begin on PDF page `317` / printed page `297 partial` with section `III. Kritik der Berkeleyschen Begriffstheorie.`
- Test whether Berkeley's next critique accepts the idealism section as internally coherent or finds the failure in Berkeley's concept theory, especially around perception, judgment, and the objective validity of law.
- Watch whether `Naturgesetz` or `immanente Kritik` deserves a separate surface after the Newton/`De motu` material returns in Book VII, or whether it should remain under `Erfahrung`, `Phänomen / Erscheinung`, `Bewegung`, and `Raum / Zeit`.
- Keep the Locke-Berkeley contrast provisional: Berkeley dissolves Locke's unknowable thing and preserves empirical objectivity as ordered phenomena, but he grounds the order in empirical association rather than rational necessity.

Decision for now:

- Part 053 passes the same-agent self-review gate for controlled draft status. Section `II` earns the Berkeley perception/suggestion glossary surface and sets up section `III` as the test of whether Berkeley's concept theory can sustain the idealism it grounds.

Verification result:

- PDF pages `304-317` were checked against scan/Tesseract output on `_0304`, `_0305`, `_0306`, `_0307`, `_0308`, `_0309`, `_0310`, `_0311`, `_0312`, `_0313`, `_0314`, `_0315`, `_0316`, and `_0317`; `_0318` was checked to confirm that section `III. Kritik der Berkeleyschen Begriffstheorie` continues after the stop.
- The review corrected OCR residue around `New theory of vision`, `knowledge`, `Erscheinungen zu`, `Urwahrnehmungen`, `Kopie`, `Kraft`, `New theory`, `repräsentative Funktion`, `Perzeption`, `Baumbild` -> `Raumbild`, `kritisch berichtigten`, `wahren`, `gewöhnlichen`, `Fraser`, `Chimäre`, `deprived`, `full force`, `dienen`, `begrifflich`, `Hilfsgrößen`, `De motu`, `gelten`, and `Kritik der Berkeleyschen Begriffstheorie`.
- Trailing content-fidelity audit flagged the body quotation anchored by Draft Footnote 8 as Cassirer's structural paraphrase of Berkeley `Principles` § 5 rather than a direct rendering. The part now records that caveat in Draft Footnote 8 and the Source-language note; the fuller audit remains in `review/audit-log.md`.

## 2026-05-16 - Berkeley, Concept Theory, Relations, And Objectivity

Created `parts/054-berkeley-concept-theory-relations-and-objectivity.md` from PDF pages `317-330` / printed pages `297 partial-310 partial`, beginning with section `III. Kritik der Berkeleyschen Begriffstheorie.` and stopping before section `IV. Der Begriff der Substanz.`

What this tranche clarified:

- Cassirer's critique remains immanent: Berkeley must be measured by his own method, not by assumptions about absolute matter that Berkeley rejects.
- The Berkeley section-II result is now tested and limited. `Perzeption` plus association can explain how contents call one another up, but not how a concept gains formal sense.
- Berkeley's attack on Lockean abstract images leaves the rationalist concept problem untouched. Conceptual generality requires a fixed standpoint, comparison, judgment, and ideal relations.
- The mathematics test is decisive: Berkeley rejects infinitesimals, irrational magnitudes, and mathematical exactness because they lack immediate sensory images, thereby falling back into the psychological abstraction of the simple.
- The empirical-object test repeats the same problem. Association yields revisable expectations, but not the timelessly valid order needed for a common world of phenomena.
- The section closes by showing Berkeley's theological solution: nature's order is guaranteed by divine will and understanding, not by necessary rational principles immanent in experience.

Structural center:

- The load-bearing movement is from representation as associative standing-in to the missing objective-conceptual ground. Berkeley's sign/suggestion doctrine blocks copy-theory and transcendent matter, but association cannot supply concept-function, continuity, identity-setting, motion-law, or empirical necessity.

Routing decision:

- No new glossary entry. Section `III` bends existing surfaces rather than earning a separate term.
- Update `Wahrnehmung / Perzeption / Suggestion`, `Begriff / Wort / Zeichen`, `Wahrheit / Urteil`, `Bild / Symbol / Ausdruck`, `Kontinuum / Stetigkeit / Infinitesimal`, `Raum / Zeit`, `Bewegung`, `Erfahrung`, `Phänomen / Erscheinung`, `Existenz / Sein / Ding`, and `Selbstbewußtsein / Ich / innere Erfahrung`.
- Keep `Repräsentation`, `Assoziation`, `Relationsbegriffe`, `Identitätssetzung`, `objektiv-begrifflicher Grund`, `Gottesbegriff`, `Zeichensprache Gottes`, and `Vernunft als Korrelat des Seins` in the close-reading ledger.

Re-entry hooks:

- Part 055 should begin on PDF page `330` / printed page `310 partial` with section `IV. Der Begriff der Substanz.`
- Test whether Berkeley answers the missing objective-conceptual ground by shifting from passive ideas to spirit, self, notion, relation, will, and causality.
- Watch whether `Idee / Begriff / notion`, `Geist / Seele / Ich`, `Substanz`, `Wille / Kraft`, or `Kausalprinzip` earns a new surface, or whether they update existing `Begriff / Wort / Zeichen` and `Selbstbewußtsein / Ich / innere Erfahrung`.
- Keep the Berkeley chapter finding provisional until section `V` shows whether the later sign/reason doctrine transforms the early sensualistic starting point.

Decision for now:

- Part 054 passes the same-agent self-review gate for controlled draft status. It answers the Part 053 test: Berkeley's idealism is internally coherent only up to the point where empirical association must do the work of logical concept-grounding.

Verification result:

- PDF pages `317-330` were checked against the PDF text layer and scan/Tesseract output on `_0317`, `_0318`, `_0319`, `_0320`, `_0321`, `_0322`, `_0323`, `_0324`, `_0325`, `_0326`, `_0327`, `_0328`, `_0329`, and `_0330`; `_0330` confirms that section `IV. Der Begriff der Substanz` begins after the stop.
- The review corrected OCR residue around `Kritik der Berkeleyschen Begriffstheorie`, `begriffliche`, `repräsentieren`, `vertreten`, `Grundauffassung Berkeleys`, `Auftreten`, `Einzelinhalte`, `Umfang`, `Vergleichung`, `Wahrnehmung`, `Aufreihung`, `Erkenntnis`, `Principles`, `Repräsentationstheorie`, `Unendlich-Kleinen`, `Zuwüchsen`, `zerfließend`, `schließlich`, `Relationen`, `ganze Zahl`, `Pythagoreische`, `Erfahrungswissenschaft`, `meinen`, `Erscheinungswirklichkeit`, `fragwürdig`, `Identitätssetzung`, `Bewegungsphänomene`, `Wechsel`, `heightening`, and `Alciphron`.

## 2026-05-16 - Berkeley, Substance, Spirit, And Causality

Created `parts/055-berkeley-substance-spirit-and-causality.md` from PDF pages `330-335` / printed pages `310 partial-315 partial`, beginning with section `IV. Der Begriff der Substanz.` and stopping before section `V. Die Umgestaltung der Berkeleyschen Erkenntnislehre.`

What this tranche clarified:

- Berkeley's concept of God, needed for the close of his experience theory, creates a problem for the sensualistic beginning of that theory.
- The passive `idea` schema cannot contain relations, self, or active spirit. The later Berkeley therefore distinguishes `idea` from `notion` and admits spirits and relations as objects of knowledge without making them sensory images.
- The I is not secured by pure experience as a congeries of perceptions. Berkeley moves the proof from theoretical consciousness to practical consciousness: will and free spiritual activity become the primal phenomenon of the individual mind.
- Berkeley's critique of cause applies to the application of causality inside empirical natural science, not to the causal principle as such. In metaphysics and speculative theology, judgment and inference of understanding grasp necessary connection.
- Section `IV` closes by naming the system split: the concept theory with which the `Principles` begin and the spiritualist metaphysics with which they close now stand in irreconcilable tension unless Berkeley transforms his first principles.

Structural center:

- The load-bearing movement is from passive idea to active spirit. The gain is not a smooth correction: Berkeley recovers self, notion, will, causality, and divine substance by moving beyond the sensualistic idea-schema that carried the first sections.

Routing decision:

- No new glossary entry yet. Section `IV` creates strong pressure for `Idee / Begriff / notion` and `Geist / Seele / Ich`, but the closing paragraph explicitly hands the issue to section `V`.
- Update `Wahrnehmung / Perzeption / Suggestion`, `Begriff / Wort / Zeichen`, `Selbstbewußtsein / Ich / innere Erfahrung`, `Sensation / Reflexion`, `Ursache / Bedingung / Erzeugung`, `Kraft / Arbeit / lebendige Kraft`, `Körper / Materie / Substanz`, `Existenz / Sein / Ding`, `Intuition / Anschauung`, `Wahrheit / Urteil`, and `Erfahrung`.
- Keep `Idee / Begriff / notion`, `Geist / Seele / Ich`, `Wille`, `geistige Substanz`, `göttliche Substanz`, `Kausalprinzip`, `Verstandesschluß`, and `notwendige Verknüpfung` in the close-reading ledger.

Re-entry hooks:

- Part 056 should begin on PDF page `335` / printed page `315 partial` with section `V. Die Umgestaltung der Berkeleyschen Erkenntnislehre.`
- Test whether Berkeley's final revision heals the split named in section `IV`, or whether it deepens the turn from empirical association into divine sign-language and speculative reason.
- Watch whether `Idee / notion / Begriff` earns a Berkeley-specific glossary surface, or whether section `V` routes the chapter close through `Zeichensprache`, `Vernunft`, `Gottesbewußtsein`, and the transformed concept of experience.
- Keep the Berkeley chapter finding provisional until section `V` supplies the attempted radical transformation of first principles.

Decision for now:

- Part 055 passes the same-agent self-review gate for controlled draft status. It decides not to open a new Berkeley spirit/notion glossary entry before the explicit transformation section tests whether that pressure stabilizes.

Verification result:

- PDF pages `330-335` were checked against the PDF text layer and scan/Tesseract output on `_0330`, `_0331`, `_0332`, `_0333`, `_0334`, and `_0335`; `_0335` confirms that section `V. Die Umgestaltung der Berkeleyschen Erkenntnislehre` begins after the stop.
- The review corrected OCR residue around `weiteren`, `hervorruft`, `Principles`, `klaren`, `jeglicher`, `perfectly`, `immediately`, `intuitively`, `sinnlicher`, `Wahrheit`, `Commonplace`, `the mind`, `zu wahrhafter`, `Kausalprinzips`, `leitet`, `powerful`, `connection`, `Kausalprinzip`, and `hinwegtäuschen`.

## 2026-05-16 - Berkeley, Transformation Of The Theory Of Knowledge

Created `parts/056-berkeley-transformation-of-theory-of-knowledge.md` from PDF pages `335-347` / printed pages `315 partial-327 partial`, beginning with section `V. Die Umgestaltung der Berkeleyschen Erkenntnislehre.` and stopping before the Collier continuation.

What this tranche clarified:

- Berkeley's final revision is not a compromise between the early idea-schema and the spiritualist close. It rebuilds the meaning of experience: the sensible world is readable as a text because an infinite intelligence orders it through signs.
- The `Alciphron` and `Siris` material turns signs from arbitrary names into the condition of objective experience. Scientific signs do not create ideal relations; they fix those relations for consciousness.
- Berkeley's self-criticism is real and unusually explicit. Cassirer reads the movement from the `Commonplace Book` to `Siris` as a path from certainty in sense and distrust of pure intellect toward a Platonic doctrine of ideas as causes and principles.
- The gain has a decisive limit. Berkeley raises logic and metaphysics above sense, but leaves mathematics and mathematical physics in a lower sphere. His "transcendental" science determines limits by appeal to a realm of immaterial beings, not by grounding the logical conditions of experience.
- Cassirer's Kant comparison is therefore not incidental. Kant's charge against Berkeley is intelligible if Berkeley is read through `Siris`: Berkeley's idealism builds a higher being above experience, whereas Kant asks after the a priori lawfulness of experience itself.

Structural center:

- The load-bearing movement is from empirical association to intelligible symbolism, then to Platonic mind. Berkeley escapes Locke's passive idea-schema only by binding consciousness to divine reason; he does not recover the mathematical-logical route that would make the idealism critical.

Routing decision:

- No new glossary entry. Section `V` pressures `Zeichensprache Gottes`, `Vernunft`, `Platonismus`, `transszendentale Wissenschaft`, and `reine Logik`, but these should remain in the close-reading ledger until Collier and Hume decide whether they become stable surfaces.
- Update `Wahrnehmung / Perzeption / Suggestion`, `Bild / Symbol / Ausdruck`, `Begriff / Wort / Zeichen`, `Erfahrung`, `Wahrheit / Urteil`, `Selbstbewußtsein / Ich / innere Erfahrung`, `Intuition / Anschauung`, `Sinn / Sinneswahrnehmung`, `Raum / Zeit`, `Körper / Materie / Substanz`, `Kraft / Arbeit / lebendige Kraft`, and `intelligible Welt / ewige Wahrheiten`.
- Keep the Berkeley finding provisional. Part 056 closes Berkeley proper, but Cassirer immediately uses Collier as a related development of metaphysical idealism before turning to Hume.

Re-entry hooks:

- Part 057 should begin on PDF page `347` / printed page `327 partial` with `Die metaphysische Entwicklung des Idealismus...`, the Collier continuation.
- Test whether Collier shifts the Berkeley finding from divine sign-language to the logical antinomies of transcendence and absolute external matter.
- Watch `Außenwelt`, `absolute Materie`, `primäre / sekundäre Qualitäten`, `Raum`, `Antinomien des Unendlichen`, and the Leibniz-Clarke bridge.
- Do not write the Berkeley/Collier chapter-close note until Collier has been translated and checked.

Decision for now:

- Part 056 passes the same-agent self-review gate for controlled draft status. It closes Berkeley proper but not the full chapter's idealism sequence, because Collier remains Cassirer's immediate contrast and extension.

Verification result:

- PDF pages `335-347` were checked against the PDF text layer and scan/Tesseract output on `_0335`, `_0336`, `_0337`, `_0338`, `_0339`, `_0340`, `_0341`, `_0342`, `_0343`, `_0344`, `_0345`, `_0346`, and `_0347`; `_0348` confirms the next tranche begins with Collier.
- The review corrected OCR residue around `Religionsphilosophie`, `intelligibles`, `völliger`, `erwarten`, `metaphysische`, `Aperçu`, `Alciphron`, `Handelns`, `Hülfe`, `irgendwelcher`, `unentbehrlich`, `Siris`, `Platon`, `αἴτιον`, `ἀρχή`, `Theaetet`, `ἐν τῷ περὶ ἐκείνων συλλογισμῷ`, `Verstande`, `Reason was given us`, `spirituales`, `transszendental`, `Vernunfterwägung`, `verständlich`, `ursprünglichen`, `où l'on`, `Réflexions`, and `l'Anglois`.

## 2026-05-19 - Berkeley, Collier, Absolute Matter, And Antinomies

Created `parts/057-berkeley-collier-absolute-matter-and-antinomies.md` from PDF pages `347-354` / printed pages `327 partial-334`, beginning with the Collier continuation `Die metaphysische Entwicklung des Idealismus...` and stopping before `Drittes Kapitel. Hume.`

What this tranche clarified:

- Collier is not treated as a mere historical appendage to Berkeley. Cassirer uses him as a parallel development of metaphysical idealism: related to Berkeley in motive, but independent in proof-form.
- The first move preserves the Berkeley perception problem while changing its proof. Collier accepts the apparent quasi-externality of visible objects, but explains it from the conditions and function of seeing rather than from an independent external object.
- The central method is proof-burden plus antinomy. A thing detached from every relation to cognition must justify its warrant; if absolute external matter is nevertheless hypothesized, it generates contradictory consequences about extension and motion.
- The antinomy does not destroy logic. It shows that the subject of the inference -- absolute external matter -- is logically nothing, like a triangular quadrilateral.
- The theological form of the space problem completes the bridge: independent matter entails independent space, and absolute space either stands outside God as another necessary infinite being or collapses God and world into pantheistic all-unity.
- Cassirer marks the limit sharply. Collier exposes contradictions in the common world-concept, but he does not show how those contradictions are positively resolved from the new idealist standpoint.

Structural center:

- The load-bearing movement is from quasi-external perception to antinomy of absolute matter. Berkeley had transformed experience into divine sign-language; Collier transforms the same anti-matter motive into a logical proof that absolute external being is self-abolishing.

Routing decision:

- No new glossary entry. The Collier continuation is compact and chapter-closing; its terms belong inside existing surfaces and the bounded Berkeley/Collier note rather than in new Collier-specific entries.
- Update `Wahrnehmung / Perzeption / Suggestion`, `Existenz / Sein / Ding`, `Körper / Materie / Substanz`, `Raum / Zeit`, `Wahrheit / Urteil`, `Sinn / Sinneswahrnehmung`, `Phänomen / Erscheinung`, `Erfahrung`, and `Bewegung`.
- Keep `quasi externity`, `Beweislast`, `eadem est ratio non entis et non apparentis`, `opprobrium philosophorum`, `dreieckiges Viereck`, `absolute äußere Materie`, `Idol unserer Einbildungskraft`, `Raumproblem / Gottesproblem`, and `positive Erfüllung` in the close-reading ledger.
- Add `reading/2026-05-19-berkeley-collier-idealism-sign-and-antinomy.md` as the bounded chapter note.

Chapter-close ratification:

- Parts 052-057 remain controlled draft.
- The Berkeley/Collier chapter finding is now earned but chapter-local: Berkeley and Collier dissolve Locke's transcendent matter, but the dissolution does not yet give a critical account of experience's lawful objectivity. Berkeley secures order through divine sign-language; Collier secures the negative proof through antinomy; neither supplies Kant's immanent grounding of possible experience.
- Keep this chapter-local until Hume tests what regularity, causal expectation, and object-formation can claim when neither absolute matter nor divine sign-order is available as support.

Re-entry hooks:

- Part 058 should begin on PDF page `355` / printed page `335` with `Drittes Kapitel. Hume.`
- Hume should test the Berkeley/Collier close directly: can experience itself ground the uniformity of nature and the connections by which impressions become objects?
- Watch `Gleichförmigkeit des Naturlaufs`, `Zeichen`, `Assoziation`, `Natur`, `Wahrscheinlichkeit`, `Kausalität`, and `hypothetischer Grund` as Hume-opening pressures.
- Do not convert the Berkeley/Collier note into a Book VI thesis before Hume supplies contrast evidence.

Decision for now:

- Part 057 passes the same-agent self-review gate for controlled draft status. The Berkeley/Collier chapter sequence is complete at controlled-draft tier with a bounded chapter note and a clear Hume re-entry test.

Verification result:

- PDF pages `347-354` were checked against the PDF text layer, layout extraction, and scan/Tesseract output on `_0347` through `_0354`; `_0355` confirms the next chapter boundary at `Drittes Kapitel. Hume.`
- The review corrected OCR residue around `wiedergewonnen. So`, `ursprünglichen`, `sich`, `Grundanschauung von`, `Auffassung der`, `où l'on`, `joint`, `Réflexions`, `l'Anglois`, `Clavis universalis`, `after Truth. Being`, `Non Existence`, `Bayle`, `angefangen bis`, `wirklichen`, `Vorstellungen und`, `his will`, `dependance`, `Beweislast`, `Rechtsgrund`, `Rechtfertigung des`, `Antinomien des Unendlichen`, `endlich`, `Welt`, `dreieckigen`, `Schlußfolgerung im geringsten`, `gemeiner`, `Auffassung`, `Gottesproblem`, `verstehen, in welcher`, and `hierzu`.

## 2026-05-19 - Hume, Experience, Uniformity, And Abstraction

Created `parts/058-hume-experience-uniformity-and-abstraction.md` from PDF pages `355-359` / printed pages `335-339`, beginning with `Drittes Kapitel. Hume.` and stopping before section `I. Die Kritik der mathematischen Erkenntnis.`

What this tranche clarified:

- Hume opens by taking the Berkeley/Collier chapter close as a problem of connection. If impressions are to become objects, they must recur uniformly enough for experience to connect and read them.
- Berkeley's sign-language supplies the immediate contrast. The world can be a readable text for Berkeley because divine intelligence guarantees the order of signs; Hume removes this guarantee and asks what experience can justify from within itself.
- The same Berkeleyan facts now reverse direction. What drove Berkeley beyond sensation into intelligible sign-language binds Hume more strictly to sensation.
- Hume is not presented as a passive registrar of facts. Cassirer stresses that Hume too applies a criterion: `reine Empfindung` becomes a methodical standard for ranking the relative truth of concepts.
- The abstraction critique sharpens Berkeley. Berkeley rejects abstract generic images while retaining a `general idea`; Hume makes generality belong only to the word, not to a psychological property of the representation.

Structural center:

- The load-bearing movement is from sign-readability to impression-authentication. Hume accepts that empirical being is a work of connecting representations, but demands that each connection authenticate itself in an accompanying immediate impression.

Routing decision:

- No new glossary entry. This is a chapter opening and names multiple pressures without yet deciding the chapter's center.
- Update `Erfahrung`, `Wahrnehmung / Perzeption / Suggestion`, `Begriff / Wort / Zeichen`, `Bild / Symbol / Ausdruck`, `Wahrheit / Urteil`, `Sinn / Sinneswahrnehmung`, `Sensation / Reflexion`, and `Phänomen / Erscheinung`.
- Keep `Gleichförmigkeit des Naturlaufs`, `hypothetischer Grund`, `Kryptogramm der Natur`, `reine Empfindung`, `psychologischer Zwang`, `Abstraktion`, `allgemeine Vorstellungen`, `Name / Wort`, `general idea`, and `Tatsachen der Erkenntnis` in the close-reading ledger.

Source-language decision:

- The Hume opener begins the chapter's English-source problem. Cassirer quotes Berkeley and Hume through German, noting his use of Lipps for Hume. The Draft restores identifiable Berkeley `Principles` § 107 and Hume `Treatise` I.I.VII English-source wording in normalized spelling rather than re-translating Cassirer's German back into English.
- This is recorded explicitly in the part Notes because it changes the Berkeley-chapter mitigation pattern from footnote-only source preservation into body-level restoration where the English source wording is certain.

Re-entry hooks:

- Part 059 should begin on PDF page `360` / printed page `340` with section `I. Die Kritik der mathematischen Erkenntnis.`
- Test whether Hume's criterion of pure sensation can survive mathematics. The next section should decide whether mathematical cognition becomes the first case where Hume's empiricist criterion breaks against science.
- Watch `Mathematik`, `Ideen`, `Eindrücke`, `Adäquatheit`, `Psychologie als Richterin`, and `Fundament aller menschlichen Erkenntnis`.
- Do not open a Hume-specific uniformity or abstraction entry until section `I` shows whether the chapter center is mathematical critique, causal uniformity, nominalism, or the broader problem of objectivity under pure sensation.

Decision for now:

- Part 058 passes the same-agent self-review gate for controlled draft status. It opens Hume with a clear test of the Berkeley/Collier chapter note while holding new glossary promotion until the mathematics section supplies contrast evidence.

Verification result:

- PDF pages `355-359` were checked against the PDF text layer, layout extraction, and scan/Tesseract output on `_0355` through `_0359`; `_0360` confirms the next tranche begins with section `I. Die Kritik der mathematischen Erkenntnis.`
- The review corrected OCR residue around `Einzelempfindungen ist`, `Vorstellungszusammenhang zu stiften`, `Zeichen`, `Gleichförmigkeit des Naturlaufs`, `notwendig`, `eben dies`, `Natur`, `Gesetzlichkeit, die`, `Humes`, `unaufheblich`, `abstehen, an denen`, `jeden`, `repräsentieren`, `wird`, `die ein`, `nachzuzeichnen, so`, `vorgezeichnet: es bleibt`, and `bestimmen, wie`.
