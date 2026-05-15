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
