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
