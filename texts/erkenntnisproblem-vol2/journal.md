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

What to expect next:

- The Gassendi opening explicitly denies that Bacon is the real ground of modern empiricism and shifts the origin to Gassendi and Hobbes, who are more inwardly familiar with exact research. This should test whether empirical and corpuscular method can separate itself more cleanly from Bacon's substantial and anthropomorphic physics, or whether early empiricism remains bound to older explanatory forms in a different register.

Decision for now:

- Part 006 has a local draft and apparatus updates. It still needs the fresh-eyes verification result and read-only subagent pressure review before being marked as a checked controlled draft.

Verification result:

- Part 006 passes the self-review gate for controlled draft status. The check-over found no word-level German correction after PDF and scan/Tesseract comparison.
- The paragraphing audit found one real source adjustment: `_0046` confirms the paragraph break before `Es ist vor allem die Astronomie...`, but `_0047` shows no new paragraph before `Wer in dieser Fragestellung...`; the part now follows the scan.
- The external-pressure review was useful as a check but too slow to make a subagent mandatory for the `/goal` workflow. The default should be the translating agent's own source-facing review pass; subagents are reserved for targeted escalation.
- The pass tightened the greater/lesser congregation sentence, the Latin `comminisci` rendering, and the Gassendi boundary expectation.
