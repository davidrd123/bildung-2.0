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
