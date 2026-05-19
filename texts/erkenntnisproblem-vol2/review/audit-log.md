# Content Fidelity Audit Log

Per-part audit findings under `content-fidelity-review.md`. Each entry records what was sampled, what was checked, and the split verdict.

## 2026-05-16 — Parts 044-048 retrospective + Parts 044, 045 deep audit

### Reviewer self-correction

The Parts 044-048 review tranche (done 2026-05-15) passed structural review but had limited source-language quotation work. Verdicts of "passes review at controlled-draft tier" were issued on cross-file consistency + page-bridge stitching + key-term spot-checks, without:

- quoting specific Latin from Cassirer's footnotes and walking through the English clause by clause
- opening Locke/Cudworth/Norris originals to verify Cassirer's German rendering
- opening a JP2 scan to verify the normalized source itself
- systematic compression / gloss-creep test at clause granularity

The 048 paragraph-break catch (PDF 259→260 mis-segmentation) was the one content-level investigation; sample-size-of-one is near-miss, not pattern.

The `content-fidelity-review.md` standard now codifies the missing gates.

### Part 044 audit (deep)

Sampled: Latin footnotes 5 and 7; body paragraph 3 (constitutive elements through Etwas/Seiendes). JP2 scan checked for marginal captions.

Findings:

- **Latin fn 5**: two mild gloss-creeps. `juxtaque experimur` → "and accordingly we experience" (literal: "and at the same time / and likewise we experience" — "accordingly" introduces a logical-consequence flavor `juxta` doesn't carry). `negotiatio omnis intellectus` → "every activity of the intellect" (literal: "every dealing / business / transaction of the intellect" — Digby's commercial metaphor smoothed). Neither shifts the load-bearing claim.
- **Latin fn 7**: clean. Grafting metaphor preserved consistently with body's `Grundstamm` / `Schößling` / "trunk" / "shoot."
- **Body paragraph 3**: clean clause-by-clause. One mild gloss-creep at `schlechthin unauflöslich` → "absolutely irresolvable" (literal: "indissoluble"). Sein/Seienden/Ding distinction preserved through body as "being / existent / thing."
- **Density**: Cassirer's marginal captions `Das Sein als Grundbegriff der Seele.` (printed 209) and `Die Einheitsfunktion des Bewußtseins.` (printed 213) present in scan, excluded from normalized source per project convention. Part title aligns with these captions ("Existence" / "Unity-Function") — Cassirer's own structural reading preserved.
- **Paraphrase grep**: clean.

Verdict: **structural clean / content clean** with two named gloss-creeps in Latin fn 5. Not redo material.

### Part 045 audit (deep)

Sampled: Norris fn 6 (long English passage); Cudworth fn 2; body paragraph 4 (copula/existence distinction).

Findings:

- **Norris fn 6 chain**: Cassirer's German body smooths Norris's scholastic vocabulary. `Eternal Habitudes...Relations of things` → `Die Beziehung` (singular, "Habitudes" dropped). `respective Correlates` → `Elementen` ("correlates" reduced to "elements"). Norris's "from Everlasting to Everlasting" cadence preserved in nearby clause but loosened at this one. **Cassirer-step compression**, faithfully carried into Draft. Full Norris English preserved verbatim in German Footnotes block.
- **Cudworth fn 2 chain**: Cassirer adds `gegenüber etwas` → "stand over against them as something" — a German interpretive thickening not in Cudworth's stark English. Cassirer also selects only the second half of Cudworth's quote for the body; the first half (ascent/descent contrast) lives only in the German Footnotes block. Mild Cassirer-step expansion + selection.
- **Body paragraph 4**: clean. Copula/existence distinction preserved. `Sachverhalt` → "state of affairs" consistent with Notes.
- **Paraphrase grep**: clean.

Verdict: **structural clean / content provisional** — Cassirer-step smoothing of Norris's scholastic vocabulary survives into the Draft. Mitigated by the German Footnotes block preserving Norris's full English verbatim. The project convention (Notes line 104) is defensible but should be visible: **the Draft block alone undertranslates Norris/Cudworth scholastic texture; readers should consult the German Footnotes block for the original English.**

### Standing watchpoint

Cassirer-on-English-sources (Locke chapters, Cambridge Platonist chapters) has inherent multi-link risk: source English → Cassirer German → Draft English. A clean Draft can reflect either tight or smoothed Cassirer renderings. The reviewer's job is to test specific clauses against the original where the citation is accessible. The Draft Footnotes summary convention preserves the English in the German Footnotes block, so the file as a whole retains the original — but the Draft layer alone is a re-translation.

### Carry-forward

- Parts 046, 047, 048: not yet audited at content-fidelity standard. Earlier structural-only reviews still stand. Locke chapters likely have similar Cassirer-step risk (Locke quotations are English-sourced).
- Parts 049, 050, 051: committed at `aae44a9` but not reviewed at all. Lay them under the content-fidelity standard from the start.
- Part 047 carries an open footnote-8 callout issue (the `Essay II, 11, § 17` citation should anchor at "ein dunkler Raum" / Kaleidoskop sentence). Diagnosis confirmed via raw OCR pass for Part 048; fix is in Part 047's body.
- Part 048 carries an open paragraph-break issue (PDF 259→260, question/answer should be one paragraph not two).

## 2026-05-18 — Part 052 audit (content probe)

Sampled: Berkeley quotations at fn 1 (in body), fn 4, fn 7, fn 9 (all verbatim English in footnote block); the long German block-quote of `Theory of Vision Vindicated` §43 in body (PDF 301); raw OCR page-image check for marginal captions across PDF 295-304; clause-level read of body paragraphs on "Symbole für die räumlichen Verhältnisse des Tastsinnes" and "Naturtrieb des Bewußtseins."

Findings:

- **Verbatim English preservation, footnotes**: clean. Berkeley §11 (`Distance is in its own nature imperceptible...`) preserved verbatim in body and fn 1; §70 short quote in fn 4 verbatim; §37 long quote in fn 7 verbatim; TVV §9 long quote in fn 9 verbatim. The project convention of preserving English source quotations in the German Footnotes block holds at five of six Berkeley-quotation sites.
- **Sixth Berkeley site — TVV §43 long German block-quote in body**: three Cassirer-step compressions, faithfully preserved into Draft.
  - `simply sees` → `dazu gelangt, zu sehen` → "comes to see". Berkeley's adverbial "simply" (sheer immediate apprehension) is dropped; processual "arriving at seeing" substituted.
  - `refracted, or reflected, or crossing, or including angles` → `die Brechung und Zurückwerfung der Lichtstrahlen` → "the refraction and reflection of light-rays". Two of Berkeley's four optical phenomena silently dropped. This matters because Berkeley is naming the trigonometric-construction phenomena that the Cartesian/Malebranchean "unconscious geometry" relies on — exactly the geometry he is criticizing. Truncating the list flattens the polemical target.
  - `anatomy and experiments` → `experimentelle Anatomie` → "experimental anatomy". Berkeley's pairing of discipline (anatomy) with method (experiments) collapsed into a single compound noun phrase.
  - Mitigation: addressed after review in `parts/052-berkeley-perception-vision-and-suggestion.md`: Draft Footnote 7 and the part's Source-language note now flag the TVV §43 Cassirer-step compression explicitly. Berkeley's §43 English is still not re-quoted in full, but the reader is warned that the Draft follows Cassirer's compressed German rendering rather than restoring Berkeley's original phrasing.
- **Marginal captions** (excluded from normalized source per project convention, present on scan): `Das Wahrnehmungsproblem.` (p. 277), `Die Theorie des Sehens.` (p. 279), `Psychologische und physikalische Methode.` (p. 281), `Die symbolische Funktion der Empfindung.` (p. 283). The four captions form the section's argument arc. Part title sequence ("perception, vision, suggestion") tracks them, but the part Notes do not record the captions as part of Cassirer's own structural reading. Worth adding for parity with Part 044's audit treatment.
- **Body paragraphs (non-quotation)**: clean clause-by-clause. `bezeichnenden Ausdruck` → "characteristic expression" mild ("indicative/telling" is closer but "characteristic" is defensible); `eigentümliche logische Funktion` → "distinctive logical function" mild; `verstehen und zu verwerten` → "understand and use" acceptable. No silent drops in the spot-checked paragraphs.
- **Cassirer's `Grille...sehend zu machen` (§53)**: Berkeley's original is `conceit of making men see by geometry`. Cassirer's `Grille` and Draft's "whim" sit slightly off Berkeley's "conceit" (self-flattering pretension), but the chain is consistent and not load-bearing.
- **Paraphrase grep**: clean.
- **Page-bridge stitching**: clean across all nine page breaks.

Verdict: **structural clean / content provisional with notes at TVV §43 rendering**. The Draft block alone undertranslates Berkeley's §43 in three clauses; the German Footnotes block does not mitigate (it carries §37, not §43). All other Berkeley source quotations are clean. Not redo material. Mitigation chosen after review: record the Cassirer-step compression in Draft Footnote 7 and the part Notes block rather than re-quote Berkeley §43 in full. The section's argument is not displaced by the compression.

### Standing watchpoint (extended)

Cassirer-on-English-sources risk now confirmed across two chapters (Cambridge in Part 045; Berkeley in Part 052). **The mitigation pattern is to preserve the source-language English in the German Footnotes block.** When Cassirer's German body carries an English-source quotation that is *not* echoed verbatim in any footnote, the Draft block alone becomes the only access path — and Cassirer-step compression survives undetected unless the reviewer opens the original. Future English-source chapters (Berkeley II–III, Hume) should be audited for this specific gap: any long German block-quote whose source-language English is not preserved in a footnote.

## 2026-05-18 — Part 053 audit (content probe)

Sampled: Berkeley quotations at fn 1, fn 6, fn 9, fn 11, fn 13, fn 15, fn 16, fn 17 (all verbatim English in footnote block, eight of twenty-one footnotes); five body block-quotes rendered into German only at fn 2 (Principles §44), fn 4 (Principles Intro §12 — geometer's black line), fn 8 (Principles §5), fn 10 (Commonplace Book — "trees in the garden"), fn 12 (Principles Intro §24 — "In vain do we extend"); raw OCR page-image check for marginal captions across PDF 304-317; paragraph-bridge check at PDF 311→312 boundary; clause-level read of the Leibniz-comparison paragraph and the Sein/Existenz/Dasein passages.

Findings:

- **Verbatim English preservation, footnotes**: strong. Eight of twenty-one footnotes carry Berkeley's English verbatim, including the long Three Dialogues passages (fn 6, fn 9, fn 11), three Commonplace Book entries (fn 13, fn 15, fn 16), Principles §111 (fn 1), and Principles §34 (fn 17). Better mitigation coverage than Part 052.
- **Five body block-quotes rendered into German only — Cassirer-step risk sites:**
  - **fn 4 (Principles Intro §12, geometer's black line)**: mild scholastic-vocabulary drop. Berkeley's "particular line" → Cassirer's `einzelne Linie` → Draft "individual line" loses some scholastic-technical load (Berkeley's particular/universal distinction). Berkeley's "demonstrated...demonstrated" parallel → Cassirer's `bewiesen...gilt` (proved...holds) — mild rhetorical-parallelism weakening. Berkeley's "suppose a geometrician is demonstrating" → Cassirer's `Betrachten wir das Verfahren` ("let us consider the procedure") modal-shift from hypothetical to invitation. None load-bearing.
  - **fn 8 (Principles §5)**: significant. This is a **Cassirer-step paraphrase rendered as a direct quotation**, not a translation. Berkeley's §5 reads "Light and colours, heat and cold, extension and figures — in a word the things we see and feel — what are they but so many sensations, notions, ideas, or impressions on the sense; and is it possible to separate, even in thought, any of these from perception?" Cassirer's `So unmöglich es ist, ohne eine tatsächliche Empfindung ein Etwas zu sehen und zu fühlen, so unmöglich ist es, in Gedanken irgendein sinnliches Objekt oder Ding gesondert von seiner Wahrnehmung oder Perzeption zu setzen` reframes Berkeley's rhetorical question + qualities catalogue into Cassirer's preferred "Just as X, so Y" parallel and substitutes `irgendein sinnliches Objekt oder Ding` (any sensible object or thing) for Berkeley's specific list (light, colours, heat, cold, extension, figures). The Draft faithfully renders Cassirer's paraphrase as if it were a translation. Stronger Cassirer-step move than Part 052's TVV §43 compression — that was selective omission within a structural rendering; this is structural reframing of the underlying claim.
  - **fn 12 (Principles Intro §24, "In vain do we extend")**: real polemical-imagery sanitization. Berkeley's `pry into the entrails of the earth` → Cassirer's `suchen in die Tiefen der Erde zu dringen` → Draft "seek to penetrate into the depths of the earth." Berkeley's deliberately visceral/anti-scholastic diction ("pry," "entrails") is replaced with Cassirer's abstract/clean diction ("penetrate," "depths"). Berkeley's polemical register against speculative metaphysics is muted at Cassirer-step. Faithfully preserved by Draft. The rhetorical force of the passage — Berkeley using earthy imagery to mock scholastic abstraction — survives only partially.
  - **fn 2 (Principles §44) and fn 10 (Commonplace Book I, 65, trees in the garden)**: not audited clause-by-clause in this pass; recorded as carry-forward risk sites.
- **Page-bridge stitching, PDF 311 → 312**: clean. Raw OCR confirms the "jeg-" / "licher" hyphenation is a mid-word page break, and the "Die Bäume sind im Garten" sentence at line 348 of raw OCR follows "realisieren können." with no paragraph indent, so they are continuous in Cassirer's printed text. Part body correctly stitches them as one paragraph.
- **Marginal captions**: all seven captions listed in the part Notes (`Das Problem der Transzendenz.` p. 285, `Die Theorie des Begriffs.` p. 287, `Der Begriff des Daseins.` p. 289, `Die Definition der Erscheinungswirklichkeit.` p. 291, `Sein und Perzeption.` p. 293, `Die Aufhebung der absoluten Materie.` p. 295, `Beschreibung und Erklärung.` p. 297) verified against raw OCR. Part 053 records the captions in Notes where Part 052 did not — improvement.
- **Body paragraphs (non-quotation)**: spot-checked the Leibniz comparison and the Sein/Existenz/Dasein clauses; clean clause-by-clause. The Notes' rendering convention (`Dasein` / `Existenz` / `Sein` / `Wirklichkeit` mapping) is observable in Draft.
- **Paraphrase grep**: clean.

Verdict: **structural clean / content provisional with notes at fn 4 (mild scholastic drop), fn 8 (paraphrase-as-quotation), fn 12 (polemical-imagery sanitization)**. Mitigation options for fn 8 specifically: either (a) preserve Berkeley's actual §5 English in the German Footnotes block alongside Cassirer's paraphrase, or (b) flag in the part Notes that fn 8's body block-quote is Cassirer's structural paraphrase of §5 rather than a translation of it. The fn 12 finding can be flagged in Notes only. The fn 4 finding is minor enough to leave unannotated. fn 2 and fn 10 remain carry-forward risk sites.

Mitigation: addressed after review in `parts/053-berkeley-idealism-existence-and-nature-law.md`: Draft Footnote 8 and the Source-language note now flag that the §5 body quotation follows Cassirer's German paraphrase rather than Berkeley's exact English. The full Berkeley §5 wording is not re-quoted in the Draft layer, but the reader is warned about the Cassirer-step restructuring.

### Pattern confirming across Berkeley chapter

Where Cassirer integrates Berkeley directly into his German argument as a body block-quote, the Cassirer-step risk increases roughly in proportion to how much rhetorical/polemical material Berkeley's original carries. Direct conceptual statements (fn 4 geometer-line) survive Cassirer's German with mild drops. Rhetorical reframings (fn 8 §5) get restructured. Polemical visceral imagery (fn 12 Intro §24) gets sanitized. The verbatim-English-in-footnote convention catches the worst case (long argumentative passages) but not the mid-range case (paraphrases-as-quotations).

## 2026-05-18 — Part 054 audit (content probe)

Sampled: Berkeley quotations at fn 1 (Principles Intro §15), fn 4 (Commonplace I, 9 — infinitesimals), fn 5 (Commonplace I, 9 — line/space infinitely great), fn 7 (Principles §142 — idea/notion distinction), fn 9 (Commonplace I, 19 — Pythagoric theorem), fn 15 (Dialogues II — God by reflection) — all verbatim English in footnotes, six of seventeen footnotes. Body block-quotes at fn 2 anchor (Principles Intro §16), fn 6 anchor (Analyst §4), fn 11 anchor (Commonplace I, 91 — short quote) rendered into German only. Marginal captions verified across raw OCR of PDF 317-330. Clause-level read of two non-quotation paragraphs (Aufreihung; Identitätssetzung).

Findings:

- **Verbatim English preservation, footnotes**: six of seventeen footnotes carry Berkeley's English verbatim, slightly better coverage than Part 053. Includes the critical `idea / notion` quotation in fn 7 — see below.
- **Body block-quote audits**:
  - **fn 2 anchor (Principles Intro §16, abstract triangle)**: two mild Cassirer-step shifts. Berkeley's three-fold coordination `abstract general inconsistent idea` → Cassirer's `abstrakte, allgemeine Idee... die in sich selbst widerspruchsvoll ist` reframes the `inconsistent` adjective from built-in property to consequence via relative clause. Berkeley's bare `relations of the sides` → Cassirer's `Größenverhältnisse der Seiten` (size-relations) specifies what Berkeley leaves implicit. Neither load-bearing.
  - **fn 6 anchor (Analyst §4, sense strained and puzzled)**: three mild Cassirer-step diction shifts: Berkeley's `puzzled` (cognitive bafflement) → Cassirer's `Verlegenheit` (embarrassment/perplexity); Berkeley's emphatic repetition `strained and puzzled... very much strained and puzzled` compressed to single `verwirrt sich auch` on second occurrence; Berkeley's quantitative `least particles` → Cassirer's ordinal `letzten Teilen` (last parts). **Important mitigation**: the ellipsis `...` in Cassirer's body block-quote marks selection between two parts of §4, signaling honest scholarly excerption rather than silent paraphrase. This is the form-honesty Part 053's fn 8 paraphrase lacked.
  - **fn 11 anchor (Commonplace I, 91, "I can square the circle")**: short German rendering, not audited clause-by-clause this pass; the load is rhetorical/personal rather than terminological, so risk is low.
- **fn 7 — idea/notion distinction (significant Cassirer-step move, well-mitigated)**: Berkeley's specific technical distinction `idea / notion` (introduced in the 1734 second-edition addition to §142, central to his later epistemology of spirits and relations) is silently flattened in Cassirer's German body to `sinnliche / rein begriffliche` (sensory / purely conceptual). Berkeley's word `notion` never appears in the body. **However**: fn 7 preserves Berkeley's verbatim English with `notion` visible, AND the part Notes explicitly flags the move: "The Berkeley § 142 `idea` / `notion` distinction is left visible because it sets up section `IV`." This is mitigation working as designed — the part is conscious of its own Cassirer-step risk and routes the reader to where Berkeley's actual terminology can be found. This is the cleanest example yet of the convention serving its function.
- **Husserl footnote (fn 3)**: Cassirer's analytic move, not a Berkeley quotation. Notes is right not to treat it as source-language risk.
- **Marginal captions**: all six listed in Notes verified in raw OCR (p. 299, 301, 303, 305, 307, 309). Page 303's caption OCR'd as `Die Relationshegriffe.` (b→h confusion) but recoverable as `Die Relationsbegriffe.`.
- **Page-bridge stitching**: clean across all 13 page breaks. PDF 317→318 boundary specifically: body stitches "auf sich selbst zu stellen" + "und besitzt sie die Mittel" as one continuous sentence.
- **Non-quotation paragraphs**: spot-checked the Aufreihung/stringing-together paragraph and the Identitätssetzung/identity-positing passage; both clean clause-by-clause, with translation choices matching Notes conventions.
- **Paraphrase grep**: false-positive hits on "Berkeley's view" — both occurrences are faithful Draft translations of Cassirer's German (`Berkeleys Anschauung`, `Grundauffassung Berkeleys`), not reviewer synthesis. Effectively clean.

Verdict: **structural clean / content probe clean at sampled clauses with notes at fn 2 (minor adjective-reshape), fn 6 (mild diction shifts, ellipsis-marked selection)**. The fn 7 idea/notion handling is best-practice for the chapter — silent flattening in body is matched by verbatim-English-in-footnote + explicit Notes flag. No redo material. fn 11 and the second part of fn 6's quotation remain as low-priority carry-forward audit sites.

### Pattern after three Berkeley parts

Part 054 closes the Berkeley-chapter audit with the cleanest content-fidelity verdict so far. The chapter has now demonstrated three discrete Cassirer-step risk grades:

- **Compression/omission inside an otherwise faithful rendering** (Part 052 fn 7 / TVV §43 — `crossing or including angles` dropped). Caught only by external Berkeley text.
- **Paraphrase rendered as direct quotation** (Part 053 fn 8 / Principles §5 — Cassirer's "Just as X, so Y" frame substituted for Berkeley's rhetorical question). Caught only by external Berkeley text. No internal mitigation.
- **Ellipsis-marked selection** (Part 054 fn 6 / Analyst §4 — Cassirer drops middle of §4, marks it with `...`). Form-honest at quotation level; diction-level smoothing still present but visible.
- **Body-flattened terminology with footnote-preserved English + Notes flag** (Part 054 fn 7 / Principles §142 idea/notion). Best-practice mitigation; the part is conscious of its own risk.

The convention "preserve verbatim English in German Footnotes block when Cassirer's body either translates or paraphrases" catches most of the risk. The remaining gap is **paraphrases that read as quotations**: when Cassirer's reformulation is structural enough to substitute his own "Just as X, so Y" frame for Berkeley's, the verbatim-English convention doesn't catch it because the body never claims to be a direct quotation. Part 053's fn 8 is the only instance of this in the chapter; it remains the highest-risk Cassirer-step site Berkeley I has produced.

## 2026-05-18 — Part 055 audit (self-probe)

Sampled: Berkeley body quotations at `Principles` § 2 and § 89; verbatim English footnote passages at `Dialogues` III, `Commonplace Book` I, 27 f., `Dialogues` II/III, and `Theory of Vision Vindicated` § 42; raw OCR page-image check for marginal captions across PDF 330-335.

Findings:

- **Verbatim English preservation, footnotes**: strong for the later section-IV evidence. The `Dialogues` III addition preserves `idea`, `spirit`, `thinking substance`, `immediately or intuitively`, and `The Mind, Spirit, or Soul`; the `Commonplace Book` note preserves `congeries of perceptions`; `Theory of Vision Vindicated` § 42 preserves the critical distinctions `to perceive / to judge` and `to be suggested / to be inferred`.
- **Body quote at `Principles` § 2**: Cassirer's German quote is not accompanied by verbatim English in the German footnote block. The Draft therefore follows Cassirer's German rendering rather than preserving Berkeley's original English texture. Opus trailing review sharpened the caveat: Berkeley's `mind, spirit, soul, or myself` becomes Cassirer's `Geist, Seele, Bewußtsein oder Ich`, displacing `spirit` into `consciousness`; `willing` becomes `begehrt` / desiring; `imagining` becomes connecting-and-separating in representation; and Berkeley's closing esse-est-percipi gloss inside § 2 is omitted. This is not a correction target. Mitigation selected after review: preserve Berkeley's § 2 English sentence verbatim in Draft Footnote 1, rather than adding editorial brace-markers inside Cassirer's German body.
- **Body quote at `Principles` § 89**: also a German body rendering, but partially mitigated by Cassirer's parenthetical `some knowledge or notion`. The load-bearing `idea` / `notion` distinction remains visible at the exact point where the argument needs it.
- **Marginal captions**: verified against raw OCR: `Idee und Begriff.` (p. 311), `Der Ichbegriff.` (p. 313), and `Das Kausalprinzip.` (p. 315). These are recorded in the part Notes and align with the title's idea/notion → I/spirit → causality arc.
- **Paraphrase grep**: clean.

Verdict: **structural clean / content controlled with one named caveat at `Principles` § 2**. The part's file-level mitigation is now accurate: English originals are preserved where Cassirer gives them in footnotes, and Berkeley's § 2 English is preserved in Draft Footnote 1 because Cassirer's German body rendering makes substantive shifts. The § 89 body quote remains a Cassirer German rendering, but its load-bearing English `some knowledge or notion` is preserved inline. Section argument not displaced.

### Reviewer-side complement to Part 055 self-probe

The producer-side self-probe above named the `Principles § 2` Cassirer-step issue at the general level (German rendering vs. verbatim English) and added a flag in Draft Footnote 1. A reviewer-side clause-level pass identifies four specific findings inside the § 2 body quote, all silent and all faithfully preserved into Draft:

1. **`mind, spirit, soul, or myself` → `Geist, Seele, Bewußtsein, Ich`**. Berkeley's four-term list silently substitutes `Bewußtsein` (consciousness) for `spirit`. This is the same `spirit` term that Berkeley elevates to technical status in § 89 (the next body quote, where the brace-marking convention is applied) and that fn 3's verbatim preserves (`I, who am a spirit or thinking substance`). The § 2 rendering makes it look as if Berkeley introduces `spirit` only at § 89 when he actually uses it from § 2 onward. The Notes Source-language line explicitly lists `spirit` as a load-bearing term to preserve — but the discipline was not applied to § 2's body quote itself.

2. **`willing` → `begehrt` (desiring)**. Berkeley's voluntarist `will` muted to `desiring`. This creates an internal inconsistency in the part: body paragraph 4 later restores `Wille` (will) as `das eigentliche Urphänomen` (the proper primal phenomenon). Berkeley's `willing → will` continuity is broken at Cassirer-step. Reader sees Cassirer paraphrasing "desiring" in § 2 and then suddenly invoking "will" as Berkeley's central category two paragraphs later.

3. **`imagining` → `sie in der Vorstellung verknüpft und trennt`**. Berkeley's bare verb expanded to Cassirer's elaborated clause about the imagination's combining-and-separating operation. Cassirer-step expansion that imports analytic-psychology vocabulary not in Berkeley.

4. **`for the existence of an idea consists in being perceived` — completely dropped**. The famous esse-est-percipi gloss within § 2 is silently removed. Cassirer's German body ends at `bezeichne` without the explanatory clause. The most significant drop in the part because it's Berkeley's signature thesis in compact form.

Mitigation gap: the brace-marking convention applied at fn 2 (`{some knowledge or notion}`) would have caught at least finding 1 if extended to § 2 (`{spirit}` after `Bewußtsein`). The current Draft Footnote 1 warning is generic; a follow-up could either (a) add `{spirit}` and `{willing}` in-body braces, or (b) preserve Berkeley's § 2 English verbatim in fn 1 alongside the section cross-references.

### Pattern after four Berkeley parts (mitigation grades)

The Berkeley chapter now demonstrates five discrete mitigation grades, worst to best:

| Grade | Pattern | Example | Internal mitigation |
|-------|---------|---------|---------------------|
| 1 | Compression/omission inside faithful rendering | Part 052 fn 7 (TVV §43) | None (post-hoc Notes flag added) |
| 2 | Paraphrase rendered as quotation | Part 053 fn 8 (Principles §5); Part 055 fn 1 (Principles §2) | None (post-hoc Notes flag added) |
| 3 | Ellipsis-marked selection | Part 054 fn 6 (Analyst §4) | Form-honest at quotation level |
| 4 | Verbatim English preserved in footnote + Notes flag | Part 054 fn 7 (Principles §142 idea/notion) | Strong |
| 5 | In-body curly-brace marking of source English | Part 055 fn 2 (Principles §89 `{some knowledge or notion}`) | Strongest |

Producer-side observation across the chapter: when a body block-quote is a German rendering of a known English-source quotation, the discipline of choosing one of grades 3–5 *before* the part is committed would close most of the gap. The post-hoc Notes flag (grade 1/2 → grade 1/2-with-flag) is a useful repair, but the in-body brace marking (grade 5) requires only the producer to know which term is load-bearing and parenthesize it inline.

## 2026-05-18 — Part 056 audit note (producer-side)

Part 056 carries a stronger source-language caveat than Parts 052-055 because many of the load-bearing Berkeley quotations from `Siris`, `Alciphron`, `Dialogues`, and `De motu` appear in Cassirer's German body with citation-only footnotes, not with verbatim English or Latin preservation. The Draft therefore follows Cassirer's German rendering and does not reconstruct Berkeley's original prose.

Mitigation in the part:

- The Source-language note names the pattern explicitly.
- Draft Footnotes identify the key English terms Cassirer does preserve: `universal intellectual notions`, `signs`, `abstract from sensible matters`, `Pure intellect`, `Reason was given us for nobler uses`, and `philosophia prima`.
- Greek OCR garbage in the Plato/Theaetetus passage was restored as `αἴτιον`, `ἀρχή`, and `ἐν τῷ περὶ ἐκείνων συλλογισμῷ`.

Verdict: **structural clean / content controlled with a global source-layer caveat**. No single Berkeley quotation in this part has yet received the clause-level external-source walk-through that Part 055's `Principles § 2` received. The part's internal mitigation is reader-awareness rather than full source reconstruction.

### Reviewer-side complement to Part 056 self-probe

The producer-side note above acknowledges the global caveat but has not done the clause-level walk-through. A reviewer-side pass:

**Structural verification:**

- Page-bridge stitching clean across all 12 page breaks (spot-checked PDF 335→336).
- All 24 footnote callouts mapped.
- Six marginal captions in Notes verified against raw OCR: `Vernunft und Erfahrung.` (p. 317, line 85), `Die Allgemeinheit der Zeichen.` (p. 319, line 167), `Verhältnis zu Platon.` (p. 321, line 249 — OCR `Piaton` i↔l confusion), `Mathematik und Metaphysik.` (p. 323, line 334), `Das "Transzendentale" bei Berkeley und Kant` (p. 325, line 418), `Der Doppelsinn des "Idealismus".` (p. 327, line 504).
- Paraphrase signal grep clean.

**Verbatim source-language preservation (8 of 24 footnotes):** fns 3, 5, 7, 12, 17, 18, 22 carry verbatim Berkeley English; fn 19 carries verbatim De motu Latin; fn 24 carries verbatim Kant Prolegomena German. Coverage is strong for the apparatus.

**In-body grade-5 mitigation (3 sites):**

- fn 11 anchor (Siris §297): body preserves `(abstract from sensible matters)` parenthetically inline.
- fn 13 anchor (Siris §335): body preserves Greek `αἴτιον` and `ἀρχή` verbatim. Restoration from OCR garbage noted in Notes.
- fn 16 anchor (Siris §305): body ends with verbatim Greek `ἐν τῷ περὶ ἐκείνων συλλογισμῷ`. Same restoration.

**Clause-level audit, fn 9 anchor (Siris §294, the ascent passage) — sample of unmitigated risk:**

Berkeley §294 (original English): "Sense at first besets and overbears the mind. The sensible appearances are all in all: our reasonings are employed about them: our desires terminate in them: we look no farther for realities or causes; till intellect begins to dawn, and casts a ray on this shadowy scene. We then perceive the true principle of unity, identity, and existence. Those things that before seemed to constitute the whole of being, upon taking an intellectual view of things, prove to be but fleeting phantoms."

Four mild Cassirer-step diction shifts, all preserved into Draft:

1. **`besets and overbears`** (Berkeley's military/siege register: surrounds and overwhelms) **→ `unterjochen und gefangen nehmen`** (Cassirer's political-imprisonment register: subjugates and takes captive). Different metaphor register; mild but real.
2. **`shadowy scene`** (Berkeley's natural-light imagery) **→ `Schattenspiel`** → Draft "shadow-play" (Cassirer's theatrical/illusion imagery). Shifts the scene from a contrast of light/shadow to a performed illusion.
3. **`fleeting phantoms`** (Berkeley's temporal motion: in flight) **→ `zerfließenden Phantomen`** → Draft "dissolving phantoms" (Cassirer's dissolutional register: melting away). Berkeley's temporal "fleeting" muted to spatial-textural "dissolving."
4. **`upon taking an intellectual view`** → **`mit dem Auge des Intellekts betrachten`** (with the eye of the intellect). Cassirer adds figurative concreteness (an eye) where Berkeley's "view" left the metaphor implicit.

None displace the ascent thesis, but the imagery register shifts at Cassirer-step. Comparable in magnitude to the Part 054 fn 6 (Analyst §4) findings — diction-level smoothing rather than structural reframing.

**fn 4 anchor (Alciphron VII §11-12, signs and arithmetic):** Cassirer's body uses ellipsis `. . .` between two halves of the §11-12 selection. Grade-3 honest excerption — same form-honest move as Part 054 fn 6. Within the selected halves the conceptual claim is faithful (signs allow general operations via methodical handling).

**fn 13 anchor (Siris §338 + §335, Plato passage):** Cassirer combines two non-contiguous Siris sections. The transition is form-honest: body marks the second Berkeley passage with quotation marks introduced by Cassirer's gloss `Denn in der Sprache Platons bedeutet die Idee...` Berkeley's Greek terms preserved verbatim. Grade 5 for the Greek; grade 3 for the §338+§335 combination via Cassirer's explicit gloss-transition.

**fn 23 anchor (De motu §71-72) — highest-risk unmitigated site in the part:** long German body block-quote of Berkeley's Latin original. De motu was published in Latin, so the German body is already a Cassirer-step translation of Berkeley's Latin, and the Draft re-translates Cassirer's German back into English — three-link chain with no Latin preservation anywhere. The conceptual claim (physics/mechanics/first philosophy as three distinct sciences with different objects) is preserved, but Berkeley's Latin technical terms (`scientia transscendentalis`, `causae corporeae secundariae`, etc.) are lost at Cassirer-step. Not audited clause-by-clause this pass — would benefit from a clause-level pass against De motu §71-72 Latin.

**fn 2 anchor (Siris §237) and fn 1 anchor (Dialogues II) and fn 13 anchor:** long body block-quotes with citation-only footnotes. The Notes Source-language section names these as risk sites. Not audited clause-by-clause this pass.

**Source oddity (already in Notes):** body prints `Alciphron` as "1723", fn 4 correctly gives 1732. Producer chose to preserve Cassirer's typo in body and let the footnote show the correction rather than silently emending. Honest preservation; reader has both data points.

**Updated mitigation grade tally across Part 056:**

- 8 fns at grade 4 (verbatim source-language in footnote)
- 3 anchors at grade 5 (in-body parenthetical/Greek preservation)
- fn 4 at grade 3 (ellipsis-marked selection)
- fn 13 at grade 3 (explicit gloss-transition between non-contiguous sections)
- fns 1, 2, 9, 23 at grade 1/2 (citation-only, Cassirer rendering)

Verdict refinement: **structural clean / content provisional with mild diction shifts at fn 9 (Siris §294) and unaudited risk at fn 23 (De motu §71-72)**. The producer-side global caveat is appropriate. Reviewer-side spot-check confirms diction-level smoothing pattern consistent with Parts 052-054; structural reframing of Part 053 fn 8 / Part 055 fn 1 magnitude does not appear in the sampled Part 056 passages. fn 23 remains the highest-value carry-forward audit site for clause-level work against Berkeley's De motu Latin.

### Updated pattern after five Berkeley parts

The chapter now shows:

- **Strong verbatim apparatus** at the footnote layer across all five parts (Part 052: 4/9; Part 053: 8/21; Part 054: 6/17; Part 055: 4/7; Part 056: 8/24 footnotes carry verbatim source).
- **Grade-5 in-body marking** now demonstrated four times: Part 055 fn 2 (`{some knowledge or notion}`); Part 056 fn 11 (`(abstract from sensible matters)`); Part 056 fn 13 (Greek `αἴτιον / ἀρχή`); Part 056 fn 16 (Greek phrase). The convention is reproducing, which is good.
- **Grade-2 paraphrase-as-quotation** remains the residual gap: Part 053 fn 8 (Principles §5), Part 055 fn 1 (Principles §2). Both received post-hoc Notes flags. No grade-2 instance was identified in Part 056's audited passages — the Cassirer-step issues in fn 9 are diction-level (grade 1) rather than structural (grade 2).
- **Multi-link Latin risk** at Part 056 fn 23 (De motu §71-72) is new in form: it's the first Berkeley body block-quote in the chapter where the original is Latin rather than English. Three-link chain (Latin → Cassirer German → Draft English) without any Latin preservation. Future De motu / Alciphron / Siris citations should be flagged for clause-level Latin checks.

## 2026-05-18 — Session wrap (pre-compact handoff)

### What was audited this session

Five sequential Berkeley-chapter parts under the content-fidelity-review standard: **Parts 052, 053, 054, 055, 056**. Each got a clause-level pass on at least one Berkeley source-language quotation, raw-OCR verification of marginal captions, page-bridge stitching check, and paraphrase-signal grep. Audit findings persisted as per-part entries above.

Codex ran producer-side self-probes on Parts 055 and 056 in parallel; reviewer-side complement sections were appended for each. Mitigation actions were taken inside several parts during the session (Part 052 Draft fn 7 + Source-language note flagging TVV §43 compression; Part 053 Draft fn 8 + Source-language note flagging Principles §5 paraphrase; Part 055 Draft fn 1 flagging §2 as Cassirer rendering).

### What emerged as a pattern

The chapter's source-language mitigation now has a stable five-grade taxonomy (table at the end of the Part 055 entry; refined at the end of Part 056). Strongest: **grade-5 in-body curly-brace/parenthetical preservation of source English or Greek** (demonstrated 4× across Parts 055-056). Weakest: **grade-2 paraphrase-as-quotation** (Part 053 fn 8, Part 055 fn 1) — present only twice and both received post-hoc Notes flags.

The verbatim-English-in-footnote convention is doing most of the load-bearing work. Per-part verbatim coverage: P052 ~5/9; P053 8/21; P054 6/17; P055 4/7; P056 8/24. The gap is body block-quotes with citation-only footnotes, especially where Berkeley's original is Latin (P056 fn 23, De motu).

### Open carry-forwards

- **Pre-existing carry-forwards** (Parts 044-048 retrospective): Part 047 footnote-8 callout anchor missing at "ein dunkler Raum" / Kaleidoskop sentence; Part 048 paragraph-break mis-segmentation at PDF 259→260. Both diagnosed, neither fixed yet.
- **Unaudited at content-fidelity standard**: Parts 046, 047, 048, 049, 050, 051. Earlier structural-only reviews still stand.
- **Part 053 carry-forward audit sites**: fn 2 anchor (Principles §44), fn 10 anchor (Commonplace I, 65 — "trees in the garden"). Not audited clause-by-clause.
- **Part 056 highest-value carry-forward**: fn 23 anchor (De motu §71-72) against Berkeley's Latin original. First Latin-source Berkeley quote in the chapter; three-link Latin → German → English chain with no Latin preservation. Worth a dedicated clause-level pass.
- **Part 055 mitigation suggestion** (not actioned): apply grade-5 brace marking at Principles §2 body quote — `{spirit}` after `Bewußtsein`, `{willing}` after `begehrt`. Currently Draft Footnote 1 has a generic flag only.

### Standing watchpoints

- **Cassirer-on-English-sources multi-link risk** continues across the chapter; convention is "preserve verbatim English in German Footnotes block" but it leaves gaps for paraphrases-as-quotations (grade 2) and Latin-source body quotes.
- **Producer-side discipline check** worth adding to the standard: for any body block-quote of a known source-language quotation, the producer should choose grade 3 (ellipsis selection), grade 4 (verbatim source in footnote + Notes flag), or grade 5 (in-body parenthetical marking) *before* commit. Post-hoc flags are repair, not first-pass discipline.

### Next step

**Part 057** picks up at PDF 347 / printed 327 partial with the Collier transition (`Die metaphysische Entwicklung des Idealismus...`). Per Part 056 re-entry hooks: treat Collier as contrast/prolongation tranche before writing the Berkeley chapter-close note. Watch whether Collier shifts the finding from divine sign-language to logical antinomies of transcendence (Außenwelt, absolute Materie, primäre/sekundäre Qualitäten, Raum, Antinomien des Unendlichen, Leibniz-Clarke bridge).

### Durable artifacts (safe to compact context after this)

- `texts/erkenntnisproblem-vol2/review/audit-log.md` — this file; all per-part findings, mitigation grade table, and session wrap
- `texts/erkenntnisproblem-vol2/review/content-fidelity-review.md` — the reviewer-side standard
- `texts/erkenntnisproblem-vol2/review-checklist.md` — producer-side checklist (pre-existing)
- Per-part Draft Footnote and Source-language note flags inside Parts 052, 053, 055 (mitigation actions taken this session)

## 2026-05-18 — Part 058 (Hume opener) content-fidelity review

**Scope audited:** `parts/058-hume-experience-uniformity-and-abstraction.md` against `source/normalized/058-...txt` and `source/raw/058-...txt`. PDF pages 355-359 / printed 335-339. Two long body block-quotes (Berkeley `Principles` §107; Hume `Treatise` I.I.VII via Lipps's German translation). Five footnotes total: fn 1 citation-only (TVV §26); fn 2 English-source (Principles §107); fn 3 English-source double-mediated (Hume via Lipps); fn 4 citation-only (Meinong); fn 5 citation-only (Principles Intro §12).

**User context:** Part 057 (Collier transition) has been drafted and committed, but it has not yet received the content-fidelity audit that had been projected in the prior session-wrap. Part 057 remains an open audit carry-forward before any Berkeley chapter-close synthesis.

### Source-language fidelity gate — fn 2 (Berkeley Principles §107)

**Berkeley English (original §107):**
> Fourthly, By a diligent observation of the phenomena within our view, we may discover the general laws of nature, and from them deduce the other phenomena; I do not say demonstrate, for all deductions of that kind depend on a supposition that the Author of nature always operates uniformly, and in a constant observance of those rules we take for principles: which we cannot evidently know.

**Cassirer German (body):**
> Wir können durch sorgfältige Beobachtung der Phänomene, die in unseren Gesichtskreis fallen, zwar die allgemeinen Gesetze der Natur erkennen und aus ihnen die besonderen Erscheinungen ableiten, nicht aber sie als notwendig erweisen. Denn alle Deduktionen dieser Art sind abhängig von der Voraussetzung, daß der Urheber der Natur stets gleichmäßig handelt und die Regeln, die wir als Prinzipien zugrunde gelegt haben, beständig befolgt: eben dies aber können wir niemals mit Evidenz erkennen.

**Draft English (Part 058 body):** verbatim Berkeley restoration with the leading "Fourthly," dropped (Cassirer also drops it).

Cassirer-step moves identified:
- "I do not say demonstrate" → "nicht aber sie als notwendig erweisen" (Cassirer expands Berkeley's terse `demonstrate` into the logical gloss `prove as necessary`). Without grade-4 restoration this would have been a grade-1 diction smoothing.
- "which we cannot evidently know" → "eben dies aber können wir niemals mit Evidenz erkennen" (Cassirer inserts intensifier `niemals` + connective `eben dies aber`). Same: would have been minor gloss-creep had it been forward-translated.
- "the other phenomena" → "die besonderen Erscheinungen" (slight semantic shift: `other` → `particular`).

Draft mitigation grade: **4 (verbatim source-language restoration in body + Footnote 2 flag).** Footnote 2 text: "The Draft uses the English-source wording in normalized spelling where Cassirer quotes Berkeley through German." This is the correct flag. Verbatim restoration neutralizes all three Cassirer-step diction moves.

### Source-language fidelity gate — fn 3 (Hume Treatise I.I.VII — double-mediated)

This is the highest-risk site in the part because Cassirer's own footnote names the double mediation: `Ich benutze im Text vielfach die vortreffliche von Lipps herausgegebene Übersetzung`. Chain: **Hume English → Lipps German translation (1904) → Cassirer's adapted German body.**

**Hume English (Treatise I.I.VII original):**
> A great philosopher has disputed the receiv'd opinion in this particular, and has asserted, that all general ideas are nothing but particular ones, annex'd to a certain term, which gives them a more extensive signification, and makes them recall upon occasion other individuals, which are similar to them. As I look upon this to be one of the greatest and most valuable discoveries that has been made of late years in the republic of letters, I shall here endeavour to confirm it by some arguments, which I hope will put it beyond all doubt and controversy.

**Cassirer/Lipps German (body):**
> Ein großer Philosoph hat die herkömmliche Meinung in diesem Punkte bekämpft und behauptet, alle allgemeinen Vorstellungen seien nichts als individuelle Vorstellungen, verknüpft mit einem bestimmten Namen, der ihnen eine umfassendere Bedeutung gebe und bewirke, daß im gegebenen Falle andere ähnliche Einzelvorstellungen in die Erinnerung gerufen werden. Ich sehe in dieser Einsicht eine der größten und schätzenswertesten Entdeckungen, die in den letzten Jahren im Reiche der Wissenschaften gemacht worden sind. Ich will aber versuchen, sie noch durch einige Argumente zu bestätigen, die sie, wie ich hoffe, über jeden Zweifel und jede Anfehdung erheben sollen.

**Draft English (Part 058 body):** verbatim Hume restoration in normalized spelling.

Lipps-step / Cassirer-step moves identified (all neutralized by grade-4 restoration):
- "term" → "Namen" (Lipps renders `term` as `name`)
- "republic of letters" → "Reiche der Wissenschaften" (Lipps modernizes Hume's 18th-c. literary register to `realm of sciences`)
- "controversy" → "Anfehdung" (Lipps uses archaic German `attack/feud`)
- "other individuals" → "Einzelvorstellungen" (Lipps adds `Vorstellungen`, making Hume's nominalism slightly more representationalist)
- Connective additions: "aber", "noch" (Lipps softening, not in Hume)

Draft mitigation grade: **4 (verbatim source-language restoration in body + Footnote 3 flag).** The double-mediation makes verbatim restoration not just defensible but mandatory. Footnote 3 explicitly names the Lipps mediation.

**Mitigation observation:** This is the strongest case in the chapter so far for **grade-5 in-body brace marking** (per Part 055 fn 2 precedent). Candidates: `{term}`, `{republic of letters}`, `{controversy}`, `{other individuals}`. Reader of body without footnote currently cannot tell that two German layers (Lipps + Cassirer) have been bypassed. Not actioned this pass.

### Body density gate — paragraph segmentation and OCR cleanup

**Marginal captions (confirmed in raw OCR, excluded from normalized body per project convention, named in Notes block):**
- Raw OCR line 70: `Die "Oleichförmigkeü der Natur**. 337` → caption `Die "Gleichförmigkeit der Natur".` at top of printed page 337.
- Raw OCR line 149: `Die Kritik der "abstrakten" Begriffe. 339` at top of printed page 339.

Both correctly identified in the Notes "Marginal-caption note." The two captions confirm the two-arc structure of the opener (uniformity problem → nominalism radicalization).

**Page-bridge stitching:** Five page boundaries (355→356, 356→357, 357→358, 358→359). Mid-sentence cross-page breaks at 355→356 ("Wäre / das Ganze..."), 356→357 ("Beweis ... in den / Erscheinungen..."), 357→358 ("über die Schätzung unseres Wissens / [n 22 fascicle mark] / entscheidet."), 358→359 ("Allgemeinen' in / einem abstrakten Vorstellungsbilde"). All stitched cleanly in body.

**OCR residue corrections (verified against raw OCR):** "Einzelempfindungenistes" → "Einzelempfindungen ist"; "Vorstellungszusammenhangzustiften" → "Vorstellungszusammenhang zu stiften"; "desNaturlaufs" → "des Naturlaufs"; "notwendig" rejoined; "abstehen,andenen" → "abstehen, an denen"; "jedeii" → "jeden"; "wdrd" → "wird"; "nachzuzeichnen,so" → "nachzuzeichnen, so"; "vorgezeichnet:esbleibt" → "vorgezeichnet: es bleibt"; "bestimmen,wie" → "bestimmen, wie"; "Gesetzlichkeit, di€" → "Gesetzlichkeit, die"; emphasis-spaced `H u m e s` collapsed to `Humes`. Notes "Verification result" lists all of these accurately.

**Paragraph segmentation:** Draft has 5 German paragraphs. Breaks fall at: end of Berkeley §107 quote → "So sehen wir..."; end of "gefügig macht" → "So führt..."; end of "Philosophie" → "Der Vergleich..."; end of "zuweisen können" → "Der Kampf gegen jegliche Form...". Raw OCR does not preserve printed indentation reliably, so I cannot independently verify each break against the print. Topic shifts at each break are coherent; no obvious mis-segmentation. **Not a clean confirmation** — would need JP2 visual inspection.

### Compression / gloss-creep gate — clause-level checks

**Paragraph 4 ("Der Vergleich zwischen Berkeley und Hume..."), eight sentences sampled:**

All eight sentences tracked clause-for-clause with English correspondents. Specific clauses:
- `festzubannen` → "bind us fast" — preserves spell-binding connotation ✓
- `unaufheblich` → "uneliminable" — loses Hegelian `Aufhebung` resonance but defensible ✓
- `zufällig und äußerlich mit ihm verbinden` → "happen to connect with it externally" — `zufällig` collapses into `happen to` (minor idiom reduction, no semantic loss)
- `wieder zurückzutun` → "undo" — tight

No silent omissions, no synthesis material.

**Paragraph 5 ("Der Kampf gegen jegliche Form..."), sampled around the Hume quote:**

One **minor gloss-creep flag** at the `hier... dort` construction:

German: "wenn es sich hier darum handelt, zum Zweck der allgemeinen Verständigung die psychischen Erlebnisse nur in ihren groben und äußeren Umrissen nachzuzeichnen, so soll dort die konkrete Fülle des Bewußtseins ausgeschöpft werden."

Draft: "where language is concerned with tracing psychic experiences only in their coarse and external outlines for the purpose of general communication, cognition is supposed to exhaust the concrete fullness of consciousness."

The Draft makes explicit the subjects `language` and `cognition` that Cassirer leaves implicit (just `hier... dort`). The interpretation is correct (recoverable from the prior `Das Ziel der Erkenntnis steht zu dem Verfahren, das die Sprache notgedrungen einschlagen muß`), but the form is smoothed from German indexical construction to English explicit naming. Borderline gloss-creep; defensible idiomatization. Worth recording, not requiring redo.

**Asymmetry observation:** The body renders `allgemeine Vorstellungen` as `general representations` (Cassirer's voice preserved) while the Hume quote restores `general ideas` (Hume's voice restored). This is the correct policy but the Notes Translation note does not flag the asymmetry. A reader without the Footnote may not realize the technical term Hume/Berkeley were debating is "general ideas," not "general representations." Minor apparatus tightening opportunity, not a content error.

### Paraphrase-signal grep

```
rg -n -i "Cassirer (argues|reads|holds|says)|Hume\b.{0,30}(point|view|argument)|Berkeley\b.{0,30}(point|view|argument)|The argument is|What this means|The thrust|The key move" parts/058-...md
```

Result: **CLEAN.** No paraphrase signals inside the Draft block.

### Verdict

**structural clean / content clean with one minor gloss-creep flag (P5 `hier... dort` smoothing) and one apparatus-tightening note (P5 `general representations` vs. `general ideas` asymmetry not flagged in Notes).**

Both block-quotes (fn 2 Berkeley, fn 3 Hume) handled at grade-4 mitigation correctly; the Hume case is the strongest argument in the chapter for promoting to grade-5 in-body brace marking given the double-mediation through Lipps. Per-part footnote verbatim coverage: 2 of 5 footnotes carry verbatim English source (the two block-quote anchors); the other three are citation-only references where verbatim apparatus is not required.

### Updated mitigation taxonomy (post-Part 058)

The Hume chapter introduces a new sub-pattern beneath grade 4: **double-mediation through a known translator** (Lipps in this case). When Cassirer himself names his German source, the verbatim restoration becomes mandatory rather than discretionary; the Cassirer-step risk multiplies through Lipps's smoothing as well as Cassirer's. Future Hume-chapter parts should treat any block-quote covered by the Lipps caveat as a grade-4-minimum site, with grade-5 brace marking strongly encouraged.

### Open carry-forwards (after Part 058)

- **Part 057 (Collier transition)** drafted and committed, but not yet audited at content-fidelity tier. PDF 347 / printed 327 partial; should be revisited before the Berkeley chapter-close synthesis.
- **Part 058 fn 3 grade-5 candidates** (optional mitigation): `{term}`, `{republic of letters}`, `{controversy}` could be brace-marked in body to make the Lipps→Cassirer double-mediation in-body-visible.
- **Part 058 Notes apparatus tightening** actioned post-review: the part Notes and journal now flag the deliberate `allgemeine Vorstellungen` (body) vs. `general ideas` (quote) asymmetry and record named translator mediation as a grade-4-minimum source-language site.
- Pre-existing carry-forwards from prior session (Parts 044-051 unaudited at content-fidelity; Part 053 fns 2/10; Part 056 fn 23 De motu Latin) remain unchanged.

### Next step

**Part 059** picks up at PDF 360 / printed 340 with section `I. Die Kritik der mathematischen Erkenntnis.` Per Part 058 re-entry hooks: this is where Hume's criterion of pure sensation meets mathematics — first test case for whether the impressionist criterion breaks against a non-empirical science. Watch `Mathematik`, `Ideen`, `Eindrücke`, `Adäquatheit`, `Psychologie als Richterin`, `Fundament aller menschlichen Erkenntnis`.

## 2026-05-18 — Part 059 (Hume on mathematics) content-fidelity review

**Scope audited:** `parts/059-hume-mathematics-space-time-and-number.md` against `source/normalized/059-...txt` and `source/raw/059-...txt`. PDF pages 360-372 / printed 340-352. Twelve footnotes; substantial Hume English-source apparatus. Three body block-quotes restored verbatim from Hume's Treatise: fn 3 (I.II.IV standard/perfection), fn 7 (I.II.III five-notes-on-flute), fn 10 (I.II.IV colored/tangible points). Six citation-anchor footnotes (fns 2, 6, 8, 9, 11) and four substantive English-source footnotes where Cassirer carries verbatim Hume in his own German apparatus (fns 1, 4, 5, 12).

### Source-language fidelity gate — body block-quotes

**fn 3 (Treatise I.II.IV — standard/perfection)** — verbatim restored:
> As the ultimate standard of these figures is deriv'd from nothing but the senses and imagination, 'tis absurd to talk of any perfection beyond what these faculties can judge of; since the true perfection of any thing consists in its conformity to its standard.

Cassirer/Lipps adds `unser` (our) and `geometrischen Gebilde` (geometrical formations) where Hume has "these figures" — minor expansion, neutralized by verbatim restoration. ✓ Grade-4.

**fn 7 (Treatise I.II.III — five notes on flute)** — verbatim restored with ellipsis matching Cassirer's selection. Notable: Cassirer/Lipps inverts Hume's "Since it appears not as any primary distinct impression, [time] can plainly be nothing but..." into "Tritt somit die Zeit nicht als ein primärer und gesonderter Eindruck in die Erscheinung, so kann sie offenbar nichts anderes sein..." — Draft restores Hume's original syntax with `[S]ince` and `[time]` bracket-restorations marking the syntactic reversal. ✓ Grade-4 with bracket-clarification (sub-grade-5).

**fn 10 (Treatise I.II.IV — colored/tangible points)** — verbatim restored. Notable: Cassirer/Lipps converts Hume's first-person rhetorical address ("I ask any one, if he sees a necessity...") into impersonal "Läßt sich irgendeine Notwendigkeit dafür einsehen" — Draft restores Hume's address form. ✓ Grade-4.

**Grade-5 in-body parenthetical preservation already present in Cassirer's own text:** `(roughly and with some liberty)` and `(the manner or order, in which objects exist)`. Cassirer himself anticipated grade-5 marking at these two anchors. The Draft preserves both. This is the chapter's first case where Cassirer's own apparatus performs grade-5; the Draft inherits without re-marking.

### Source-language fidelity gate — footnote-layer compression flag (largest issue)

Cassirer's German footnotes 1, 4, 5, and 12 each carry **substantive verbatim Hume English passages** (some ~50 words, fn 5 ~150 words, fn 12 ~140 words). The Draft Footnotes block has compressed all four:

- **fn 1:** Cassirer's footnote: full 40-word Hume passage ("Wherever ideas are adequate representations of objects, the relations, contradictions and agreements of the ideas are all applicable to the objects; and this we may in general observe to be the foundation of all human knowledge."). Draft Footnote 1: meta-comment only, no verbatim.
- **fn 4:** Cassirer: 40-word Hume passage on right-line standard. Draft: short phrase quotation `"nothing but a certain general appearance"` + meta-comment.
- **fn 5:** Cassirer: ~150-word Hume passage with internal ellipses on equality, imaginary standard, fiction of mind. Draft: two short phrase quotations + meta-summary.
- **fn 12:** Cassirer: ~140-word Hume passage on "pure and intellectual view" / "asylum ignorantiae." Draft Footnote: no verbatim; just citation + meta-comment that "the Draft preserves Hume's English-source wording for the 'pure and intellectual view' passage." But the body still uses Cassirer's German rendering `reine intellektuelle Perzeptionen` → Draft `pure intellectual perceptions`, **not** Hume's `pure and intellectual view`. So Footnote 12 claims a preservation that doesn't actually appear in either body or footnote.

This is a **partial regression from the chapter pattern**. In Parts 052-056 the producer brought Cassirer's verbatim source-language footnote quotations into the Draft Footnotes block (grade-4 apparatus). Here the producer's pattern has narrowed: body block-quotes get verbatim restoration in the body, but Cassirer's own footnote verbatim passages are summarized rather than reproduced. The Draft apparatus is leaner than Cassirer's.

**Specific issue at fn 12:** Cassirer's "reine intellektuelle Perzeptionen" semantically shifts Hume's "pure and intellectual view" (faculty/mode of seeing) to "perceptions" (plural perceptual content). The Draft preserves Cassirer's shift in the body (`pure intellectual perceptions`) and claims to preserve Hume's wording in the Footnote — but neither location actually carries Hume's `view`. This is a **substantive Cassirer-step terminological shift** that the Draft apparatus claims to handle but does not.

### Body density gate

**Marginal captions** (raw OCR top-of-page): six captions confirmed — `Die Kritik der mathematischen Erkenntnis.` (341, doubles as section header), `Sinnliche und mathematische "Ideen".` (343), `Die "Fiktionen" der Mathematik.` (345), `Raum und Zeit.` (347), `Die mathematischen und die sinnlichen "Punkte".` (349), `Der Begriff der Zahl.` (351). All listed accurately in Notes; excluded from normalized body per convention.

**Page-bridge stitching:** twelve page-breaks across PDF 360→372. All stitched cleanly. Several mid-word hyphen breaks (`seit-/samer`, `dem Hume sie ent-/lehnt`) handled correctly.

**Paragraph segmentation:** ten German paragraphs. All breaks topically motivated (post-fn 3 quote → certainty-renunciation; post-fn 4 → Grundbegriffe analysis; post-fn 5 → consistency-judgment; post-`Unterbau des Systems` → subjective-necessity question; post-`hinausgehen` → spatial-relations analysis; post-fn 9 → mathematical-points analysis; post-fn 10 → critique of `Berührung`; post-`dulden dürfte` → number). Cannot independently verify each break without JP2 visual inspection; no obvious mis-segmentation.

**OCR residue corrections:** Notes list ~20 corrections. Verified ~18 against raw OCR: `Vor-stellung,daß`, `über-schreitet,das`, `Psychologie ils → als Richterin`, `verHeren → verlieren`, `Zusammentreffeneine → Zusammentreffen eine`, `z.TB. → z. B.`, `wahrnehm-baren`, `un-bekümmertum`, `begriffUche → begriffliche`, `seit-/samer → seltsamer`, `sieht- → sicht-`, `Lage-/verhältnisund`, `Be-/merkungendieAnschauung`, `er-/hobenzu`, `einiem → einem`, `Einlleiten → Einheiten`, `nins → runs`, `nar → nor`. Two items not obviously locatable: `Teil` (probably routine de-hyphenation) and the `appearing → appealing` claim (raw OCR has `appealing` already, so either Cassirer's printed text had `appearing` typo and the correction was made against the print, or the correction wasn't needed; unverified without JP2).

**Apparatus discrepancy:** Notes Translation note states "`Allgemeine Gesamterscheinung` is total appearance in the Draft body but held in the Notes as general total appearance." But the Draft body actually renders it as `general total appearance` (not `total appearance`). Minor apparatus inconsistency — the Translation note describes a choice that wasn't taken.

### Compression / gloss-creep gate — clause-level checks

**Paragraph 4 ("Führen wir dieses Kriterium..."), full clause-by-clause sample including fn 5 anchor:**

All clauses tracked. Notable:
- `allseitig durch` → `through on every side` ✓
- `Anzahl... Menge` → `number... quantity` ✓
- `kleinsten noch eben wahrnehmbaren Ausdehnungsgrößen` → `smallest still just perceptible magnitudes of extension` ✓
- `Größenübereinstimmung` → `agreement in magnitude` ✓
- `unausführbare Zerlegung` → `unperformable decomposition` ✓
- `den vorstellenden Subjekten ... gleichartig zumute ist` → `we, as representing subjects, feel the same way` (affective `zumute` captured by `feel the same way`)
- `imaginäres Gebilde` → `imaginary formation` ✓
- `ebenso nutzlos wie unverständlich` → `as useless as they are incomprehensible` — note: Hume's actual phrase (in fn 5 quote, verbatim) is `useless as well as incomprehensible`; Cassirer renders as `ebenso ... wie`; Draft follows Cassirer's smoothing in body since this is not a block-quote. Acceptable grade-1 diction within non-quoted prose.

No compression, no gloss-creep, no synthesis material.

**Paragraph 7 ("Denn der Versuch, den Hume unternimmt..."), sampled around fns 8 and 9:**

All clauses tracked. Notable:
- `räumliches Beisammen` → `spatial being-together` (preserves the German nominalization)
- `Gesichts- oder Tasteindrücke` → `impressions of sight or touch` ✓
- `Lageverhältnis` → `relation of position` (preserves relational sense) ✓
- `Anschauung des Raumes` → `intuition of space` (preserves Kantian register, appropriate) ✓
- `ausnahmslose Entsprechung` → `exceptionless correspondence` ✓
- `noch hinter ... zurück` → `falls back behind` ✓
- `Kunde verschafft` → `informs us` ✓

Tight throughout.

### Paraphrase-signal grep

Three grep hits, all false positives: Cassirer's `Standpunkt` translated as `standpoint`; Hume's `point of departure` (Cassirer's `Ansatzpunkt`) translated; one Notes-block hit at line 149 (Notes-block content is allowed). **Effectively CLEAN** for paraphrase signals inside the Draft body.

### Verdict

**structural clean / content clean at body level; content provisional at apparatus level with one substantive flag (Footnote-layer compression at fns 1, 4, 5, 12) and one terminological-shift flag (fn 12 `pure and intellectual view` → `pure intellectual perceptions` shift claimed-but-not-restored).**

The body translation work is strong: three Hume block-quotes restored verbatim, two Cassirer-internal grade-5 parentheticals preserved, clause-level fidelity in sampled paragraphs, and clean OCR cleanup at high count. The weakness is at the apparatus layer: Cassirer carries substantive verbatim English Hume passages in his own German footnotes 1, 4, 5, 12 (the longest one ~150 words at fn 5), and the Draft Footnotes block has trimmed all four. A reader of the Draft sees less than a reader of Cassirer.

Per-part verbatim coverage: 3 of 12 footnotes carry full verbatim Hume English in the Draft Footnotes block — markedly down from the Berkeley-chapter chapter average (P053 8/21, P054 6/17, P055 4/7, P056 8/24). The numerical regression matches the apparatus-level finding.

### Updated taxonomy notes (post-Part 059)

The Hume chapter introduces a **footnote-layer compression risk** distinct from the body-layer mitigation grades. When Cassirer carries verbatim source-language passages in his own German footnotes (rather than in body block-quotes), the producer has three options:

1. **Reproduce verbatim** in Draft Footnotes block (apparatus parity with Cassirer — grade-4 equivalent at the footnote layer).
2. **Selective verbatim** with key phrases preserved + meta-summary (grade-3 equivalent).
3. **Meta-summary only** with citation (grade-2 equivalent).

Part 059 mixes options 2 and 3 across its footnotes; Parts 052-056 generally used option 1. Worth a producer-side discipline note: the choice should be deliberate, not drift.

### Carry-forwards raised by audit

- **Resolved below: Part 059 fn 12 apparatus repair** (recommended): either restore Hume's verbatim "pure and intellectual view" passage in the Draft Footnote, or change the body rendering to `pure and intellectual view` to match Hume directly. The audited state had the Footnote claiming a preservation that did not appear anywhere.
- **Resolved below: Part 059 fns 1, 4, 5 apparatus tightening** (optional): consider bringing Cassirer's verbatim English Hume passages from the German footnotes into the Draft Footnotes block for apparatus parity.
- **Resolved below: Part 059 Notes Translation note inconsistency** (minor): the `Gesamterscheinung` note described a choice (`total appearance`) different from the actual body rendering (`general total appearance`).

**Producer-side repair applied after audit:**

- Draft Footnotes 1, 4, 5, and 12 now reproduce Cassirer's substantive verbatim Hume English apparatus rather than replacing it with meta-summary only.
- Draft Footnote 12 now explicitly leaves Hume's `pure and intellectual view` visible beside Cassirer's body-level `reine intellektuelle Perzeptionen` / `pure intellectual perceptions`, resolving the claimed-but-not-present preservation.
- The Part Notes translation line now describes the actual body choice for `allgemeine Gesamterscheinung` as `general total appearance`.
- The Part Notes and journal verification lists no longer claim an OCR correction from `appearing` to `appealing`; the raw OCR already had `appealing`.
- **Part 057 (Collier transition)** content-fidelity audit still pending.
- Pre-existing carry-forwards (P053 fns 2/10, P056 fn 23 De motu Latin, Parts 046-051 unaudited) unchanged.

### Next step

**Part 060** picks up at PDF 373 / printed 353 with section `II. Die Kritik des Kausalbegriffs.` Per Part 059 re-entry hooks: this is where the chapter tests whether causality repeats the mathematics pattern — consciousness cannot stay inside immediate impressions because objectivity requires a relation/transition not given as a separate impression. Watch whether `Kausalität`, `Glaube / belief`, `Gewöhnung`, `Wahrscheinlichkeit`, `Assoziation`, `Einbildungskraft`, `reine Wahrnehmung` earn new surfaces or are absorbed by existing entries. The Hume causality section is the chapter's most-cited Hume material in subsequent philosophy; expect dense source-language apparatus and another stress test of the footnote-layer compression question raised here.
