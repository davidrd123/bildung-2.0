# Weyl Translation Journal

## 2026-05-08 - Encounter Layer Opened

Opened a bounded translation/encounter layer for Weyl under `sources/modern/`
without promoting the source into `texts/`.

Reason:

- the cleaned German source layer is now usable and page-anchored
- the book is philosophically central enough to test a real translation pass
- the OCR/page-image authority situation still argues for source-local work
  before any full project promotion

Structure:

- `parts/` contains English translation batches with German source excerpts and
  source-status notes
- `glossary.yaml` records only active term pressure
- `journal.md` stays source-bound: workflow, batch decisions, source quality,
  and translation pressure

Current constraint:

- page images remain the authority for active passages
- cleaned text is a working layer, not a critical edition
- formula-heavy and symbol-heavy pages need direct visual checking before
  translation

## 2026-05-08 - Calibration: `Einführung`

Completed a first calibration part for printed page 15 / PDF page 16.

What the page shows:

- Weyl presents the book as philosophy emerging from the internal work of
  mathematics and natural science, not as philosophy externally applied to them
- examples will be kept simple, but the philosophy of the sciences still
  presupposes knowledge of the sciences themselves
- the mathematics sequence is explicitly methodological: from surface to depth,
  from the formal toward the substantive problematic of the infinite
- Leibniz is named as the philosophical hero who saw the essence of the
  mathematical and integrated mathematics organically into his system

Translation decisions:

- `Philosophie der Wissenschaften` is rendered as `philosophy of the sciences`
  to preserve the plural and avoid reducing the phrase to generic philosophy of
  science
- `Naturwissenschaft` is rendered as `natural science` in the singular where
  Weyl pairs it with mathematics as a field
- `das Mathematische` is provisionally `the mathematical`, not simply
  `mathematics`, because Weyl is naming an essence or mode
- `inhaltliche Problematik` is provisionally `substantive problematic`; `problem
  of content` is too literal and too weak

Measure:

- the introduction is too short to set normal batch size
- the next honest unit is likely the first subsection of chapter I, printed
  pages 16-21, ending before section 2
- future batches should be argument-units rather than whole chapters; chapter I
  is 31 printed pages and contains enough formula/notation risk to require
  smaller visual checks

## 2026-05-08 - Part 002: Relations And Judgment Structure

Completed the chapter opening plus subsection 1, printed pages 16-21 / PDF
pages 17-22.

Source corrections:

- corrected the Leibniz/Clarke passage (`§ 47`, `L und M`, ellipsis, quote
  punctuation)
- corrected relation notation and logical symbols: `N̄`, `∨`, `Π`, `Σ`, `Σ̄`,
  products, and the three displayed example formulas
- corrected several OCR joins and misread words around `zum Ausdruck`, `so z.
  B.`, `partikulär`, and `A, B hindurchgehende`

What the batch clarified:

- Weyl's first move is anti-subject-predicate: relational judgment is not
  reducible to subject, copula, and predicate
- `Leerstelle` is structurally important because it lets the logical form be
  separated from accidental grammar
- the passage already names a later reversal: first operations are subordinated
  to static relations, but later relations will be replaced by constructive
  processes
- numbers are introduced as freely producible, individually characterized
  `Sonderwesen`, while points in space are homogeneous under geometry's basic
  relations

Translation decisions:

- `Urteil` remains `judgment`
- `Leerstelle` is `empty place`
- `anschaulich aufgewiesen` is `intuitively exhibited`
- `Sonderwesen` is provisionally `special entity`

Next batch:

- section 2, `Die aufbauende mathematische Definition`, printed pages 22-28 /
  PDF pages 23-29

## 2026-05-08 - Part 003: Constructive Definition And Abstraction

Completed subsection 2, printed pages 22-28 / PDF pages 23-29.

Source corrections:

- corrected the circle example (`Kreis um O durch A`, `O′ durch A′`,
  `OA′ = OA`) and the function example (`b sei der Wert`)
- corrected projective-geometry notation (`[a b c]`, `π`) and equivalence
  notation (`~`)
- corrected source references and symbols: `§ 13`, `§§ 63—68`, `μέθεξις`,
  `Φ`, and the final abstractum formula
- corrected OCR joins in the set passage, including `Menge aller`, `auf einer`,
  `zu sein`, and `Kreis um`

What the batch clarified:

- Weyl's `schöpferische Definition` is not decorative terminology: mathematical
  definition creates ideal objects by specifying how they are given and how
  their identity is tested
- definition by abstraction is a quotienting procedure under an equivalence
  relation, and number is used as the central example
- set-formation is not presented as a reduction of ideal objects to concrete
  collections; Weyl reverses the explanation and uses creative definition to
  clarify what `Menge` means
- the earlier contrast between conceptual definition and intuitive exhibition
  returns explicitly in the discussion of originary abstraction and the
  relativity problem

Translation decisions:

- `aufbauende mathematische Definition` is rendered as `constructive
  mathematical definition`, with an open warning that the pressure is
  object-forming or building-up rather than merely later constructivist
- `schöpferische Definition` is `creative definition`
- `wirklich` is usually `actual` where Weyl contrasts actual and ideal points
- `Menge` is `set`, while `Inbegriff` is `aggregate`
- `Abstraktum` is kept as `abstractum` in the final formal principle

Next batch:

- section 3, `Das logische Schließen`, printed pages 28-33 / PDF pages 29-34

## 2026-05-08 - Part 004: Logical Inference

Completed subsection 3 plus the local `LITERATUR` list, printed pages 28-34 /
PDF pages 29-35.

Source corrections:

- corrected the Leibniz French citation and `§ 4`
- corrected quotation marks around `„es gibt“`, `„alle“`, `„analytisches“`, and
  the finite-prescription phrase
- corrected implication arrows, negation bars, `∨`, `Σx`, `Πx`, and the
  Sheffer-stroke notation
- rebuilt the damaged truth tables and the example formula `b → (a → b)`
- corrected the quantifier axioms, Cajus syllogism formulas, and blackletter
  placeholders `𝔄`, `𝔅`

What the batch clarified:

- Weyl gives finite propositional logic a direct decision procedure: truth-table
  inspection by the `finite Vorschrift`
- the entry of `es gibt` and `alle` breaks that direct survey and forces
  constructive proof step by step
- proof is therefore not merely formula manipulation; because construction is
  action, logic requires a practically exercisable rule of inference
- the implication sign is neutral between logical consequence, substantive law,
  causal connection, and empirical regularity, which makes Weyl's cause/ground
  distinction explicit
- Husserl, not Kant, supplies the closer match for Weyl's sharp notion of formal
  validity

Translation decisions:

- `Das logische Schließen` is `Logical Inference`
- `formale Gültigkeit` is `formal validity`
- `finite Vorschrift` is `finite prescription`
- `ursprüngliche Dunkelheit der Vernunft` is `originary darkness of reason`
- `Grund und Folge` is `ground and consequence`, kept distinct from
  `Ursache und Wirkung`

Next batch:

- section 4, `Die axiomatische Methode`, printed pages 34-46 / PDF pages 35-47

## 2026-05-08 - Part 005: The Axiomatic Method

Completed subsection 4 plus the final chapter-I `LITERATUR` list, printed
pages 34-46 / PDF pages 35-47.

Source corrections:

- corrected the Husserl/Pascal/Euclid opening, including `esprit géométrique`,
  `ὅροι`, `αἰτήματα`, and `κοιναὶ ἔννοιαι`
- corrected blackletter placeholders `𝔄`, `𝔅`, `𝔎`, the projective-plane
  incidence table, and local references such as `§ 12`, `§ 3`, `§§ 67—72`,
  and `VII`
- corrected the isomorphy notation `Σ₁`, `Σ₂`, `R′`, the electric-current
  notation `Jₛ`, the group-theory inequalities, and the area-function notation
  `J(γ)` / `c · J(γ)`
- corrected final quotation marks and French accents in the Schlick/Gonseth
  end matter

What the batch clarified:

- axiomatics is not merely a formal tidying operation; it is the method by which
  a science tries to collect the basic concepts and basic facts from which its
  relevant general truths follow
- because scientific theory is bold construction rather than direct copying of
  the given, `Widerspruchslosigkeit` becomes the decisive mathematical control
- the model method shows that consistency can be reduced by interpretation
  without requiring truth in the model domain
- `Vollständigkeit` cannot mean a universal decision procedure without
  trivializing mathematics; the viable axiomatic sense is categoricity, or
  uniqueness of contentful interpretations up to isomorphism
- the isomorphism passage is the epistemological peak of the chapter: science
  determines structure, not the inner essence of objects
- pure mathematics is finally characterized as the theory of `logische
  Leerformen`, with axioms acting as implicit definitions

Translation decisions:

- `Die axiomatische Methode` is rendered as `the axiomatic method`
- `Widerspruchslosigkeit` is rendered as `consistency`, with the literal
  freedom-from-contradiction pressure kept in notes
- `Vollständigkeit` is `completeness`; `kategorisch` is `categorical`
- `Isomorphie` is rendered as `isomorphism`, while `isomorphe Abbildung` is
  `isomorphic mapping`
- `logische Leerform` is rendered as `logical empty form`
- `inhaltliche Interpretation` is rendered as `contentful interpretation`
- `implizite Definition` is rendered as `implicit definition`

Chapter-I campaign status:

- all chapter-I subsections have now been visually checked, corrected in the
  cleaned German where needed, translated, and journaled
- synthesis added at `synthesis/2026-05-08-chapter-i-campaign-synthesis.md`
- decision: continue source-local into chapter II, do not promote to `texts/`
  yet, do not pause

## 2026-05-08 - Part 006: Rational Numbers And The Complex

Started chapter II with subsection 5, printed pages 47-51 / PDF pages 48-52.
Although the planned first batch named pages 47-50, the section spills onto the
top of printed page 51 before section 6 begins, so the full subsection and its
local `LITERATUR` were included.

Source corrections:

- corrected the multiplication and fraction formulas, including repeated
  addition, `(n + 1)a = (na) + a`, `mx/n + m*x/n*`, and `(K) m · n* = n · m*`
- corrected Greek list markers `α)` and `β)`, section references `§ 2` and
  `§ 7`, and the page reference `(S. 23)`
- corrected complex-number notation `(α, β)`, `i · i = — e`, and arithmetic
  identities involving `0` and `1`
- corrected the Huygens French quotation and several OCR failures in
  `arithmetischen`, `Zahlen`, `possit`, and `a > b`

What the batch clarified:

- Weyl treats fractions as ideal elements introduced to force invertibility of
  multiplication while preserving the main arithmetical laws
- the equality criterion for fractions first has a transfinite wording but can
  be replaced by the finite cross-multiplication test `(K)`
- rational and complex numbers are philosophically low-risk for Weyl; once the
  natural numbers and real continuum are handled, these extensions pass by "no
  abysses"
- complex numbers mark a natural boundary for preserving all formal laws of
  calculation, while hypercomplex systems remain useful despite losing some laws
- an axiomatic presentation of arithmetic is possible, but genesis still serves
  to reduce consistency to the natural-number axioms

Translation decisions:

- `genetischer Aufbau` is rendered as `genetic construction`
- `Brüche` is `fractions`, while `rationale Zahlen` is `rational numbers`
- `Vervielfältigung` is rendered as `multiplication` in this mathematical
  context
- `transfinites Kriterium` is `transfinite criterion`
- `Größen-Axiome` is `axioms of magnitude`

Next batch:

- section 6, `Die natürlichen Zahlen`, printed pages 51-56 / PDF pages 52-57

## 2026-05-08 - Part 007: Natural Numbers

Completed subsection 6 plus its local `LITERATUR`, printed pages 51-57 / PDF
pages 52-58. The section begins on the same printed page as the tail of section
5 and ends just before section 7.

Source corrections:

- corrected complete-induction notation, including `α)`, `β)`, `n′`,
  `a + 1 = a′`, `a + n′ = (a + n)′`, and the inference from `n` to `n + 1`
- corrected Schopenhauer, Helmholtz, Cantor, `§ 38`, `§ 10`, `S. 23`, and the
  commutativity formula `m + n = n + m`
- corrected quotation marks in the Hilbert and Helmholtz passages, plus
  `Inbegriff`, `kolligieren`, `fingieren`, and the parity definition
- corrected the stroke and dot examples used in the number-sign discussion:
  `/ / / /`, `∵`, and `∴`
- corrected `Billion = 10¹² Papiermark` and the later `10¹²` occurrences

What the batch clarified:

- the natural numbers, not the fractions or complex numbers, are Weyl's first
  hard philosophical case; they already involve construction, possibility,
  signs, and infinity
- complete induction is the soul of mathematical proof because it gives
  concepts and proofs their generality through the transfer from `n` to `n + 1`
- Weyl rejects the priority of cardinal number: counting an aggregate already
  orders it temporally, so ordinal structure is primary
- the sign discussion is exact: signs are not essential for direct comparison
  if the earlier sequence can be reproduced, but number-determination becomes
  essentially signitive once comparison is split into separate determinations
- the three `Grundzüge des konstruktiven Erkennens` summarize Weyl's
  constructive epistemology: operations become features of the given, signs
  split and stabilize operations, and actual signs are projected onto an
  infinity-open manifold of possibilities
- ideal numbers become dangerous only when the infinity-open sequence is turned
  into a closed aggregate of objects existing in themselves

Translation decisions:

- `vollständige Induktion` is `complete induction`, with `mathematical
  induction` treated as the modern gloss rather than the main rendering
- `Ordinalzahl` is `ordinal number`; `Kardinalzahl` is `cardinal number`
- `Zahlzeichen` is `number-sign`; `standhaltende Zeichen` is `enduring signs`
- `signativen Charakter` is `signitive character`
- `konstruktives Erkennen` is `constructive knowing`
- `Sprung ins Jenseits` is `leap into the beyond`

Next batch:

- section 7, `Das Irrationale und das Unendlichkleine`, printed pages 57-65 /
  PDF pages 58-66

## 2026-05-08 - Part 008: The Irrational And The Infinitesimal

Completed subsection 7 plus its local `LITERATUR`, printed pages 57-65 / PDF
pages 58-66.

Source corrections:

- corrected root and constant notation: `√2`, `∛2`, `π`
- reconstructed the Eudoxus ratio schema and the Dedekind-cut class labels
  `(I)`, `(II)`, `(III)`
- corrected Dedekind interval notation `aₙbₙ`, `bₙ — aₙ`, and the reference to
  the example `π`
- corrected Zeno's series `1/2 + 1/2² + 1/2³ + ...` and `1 — 1/2ⁿ`
- corrected names, footnotes, quotation marks, and the French d'Alembert
  quotation with accents

What the batch clarified:

- the continuum is Weyl's second open place after the natural-number series; it
  raises the infinite as infinite divisibility rather than serial generation
- Eudoxus supplies the anti-infinitesimal control: every pair of magnitudes is
  comparable by repeated addition, so the continuum contains neither actual
  infinitesimal nor actual infinitely large
- Dedekind reverses the old dependence of analysis on geometry: arbitrary cuts
  in the rationals define real numbers, then geometry receives completeness as
  an axiom
- logical completeness mirrors intuitive gaplessness, but only after analysis is
  made arithmetically independent of geometry
- the continuum problem drives toward epistemological idealism because a real
  thing is never adequately given; it unfolds an inner horizon through an
  indefinitely continuing process of experience
- Zeno is not fully answered by summing a convergent series; the deeper issue is
  whether infinitely many chopped-off parts may be treated as a completed
  traversed whole
- the limit process wins over actual infinitesimals, but only Cauchy and
  Dedekind clarify that the limit's existence must be guaranteed, not merely its
  value calculated

Translation decisions:

- `das Unendlichkleine` is `the infinitesimal`
- `aktual Unendlichkleines` is `actual infinitesimal`
- `Schnitt` is `cut`
- `Stetigkeit` is `continuity`; `Lückenlosigkeit` is `gaplessness`
- `Grenzprozeß` is `limiting process`; `Limes` is `limit`;
  `Grenzübergang` is `passage to the limit`
- `Grenzidee` is `limit-idea`
- `nicht-archimedische Größenlehre` is `non-Archimedean theory of magnitudes`

Next batch:

- section 8, `Die Mengenlehre`, printed pages 66-71 / PDF pages 67-72

## 2026-05-08 - Part 009: Set Theory

Completed subsection 8 plus its local `LITERATUR`, printed pages 66-71 / PDF
pages 67-72. The section and literature spill onto the same printed page where
section 9 begins.

Source corrections:

- corrected Greek and mathematical notation: `δυνάμει`, `ἐνεργείᾳ`, `π/4`,
  `ε`, `δ`, `n → n′`, `n → 2n`, `n → n²`, and Euclid's Greek axiom
- restored the missing Leibniz-series display and corrected the epsilon-delta
  continuity formula
- corrected Dedekind-chain notation and quotes around `es gibt`, `alle`,
  Bolzano's paradox, and the arithmetical comparison criterion
- corrected the property/type-theory notation: `𝔄`, `E𝔄`, first-level and
  second-level properties, Russell's self-totality principle, and `§ 1`
- corrected set-membership/copula notation `x ε X` and the section bibliography

What the batch clarified:

- set theory is Weyl's third attempted rescue of the continuum after atomism and
  infinitesimals; it is the static treatment of laws, possible sequences, and
  possible sets as already fixed objects
- Weyl grants that analysis becomes rigorous and shared once the actual
  infinite is accepted; the criticism is ontological, not a denial of the
  mathematical achievement
- the essence of set theory is the unrestricted use of `there is` and `all` on
  possible sequences, subsets, and properties
- Dedekind's infinite set is defined by self-embedding, and complete induction
  is recast as a theorem about all chains
- the key philosophical move is the objectification of properties, which
  transforms `x is red` into `x has property X` and treats the copula as a
  relation
- Russell's type-theory objection exposes the antinomy: a property defined from
  the totality of first-level properties cannot itself belong to that totality
- Weyl's `Das Kontinuum` is presented as the honest predicative route, while
  Russell's axiom of reducibility is treated as a forced postulate without
  insight
- Cantor's free use of power sets makes explicit the contradiction latent in
  treating a field of constructive possibilities as a closed aggregate of
  objects existing in themselves

Translation decisions:

- `Die Mengenlehre` is `set theory`
- `aktual Unendlichen` is `actual infinite`
- `geschlossen(en) Inbegriff` is `closed aggregate`
- `Kette` is `chain`
- `logisieren` is `logicize`
- `Vergegenständlichung` is `objectification`
- `Existentialabsolutismus` is `existential absolutism`
- `umfangsdefinit` is `extensionally definite`; `umfangsgleich` is `identical
  in extension`
- `Typenlehre` is `theory of types`; `circulus vitiosus` remains Latin

Next batch:

- section 9, `Intuitive Mathematik`, printed pages 71-76 / PDF pages 72-77

## 2026-05-08 - Part 010: Intuitive Mathematics

Completed subsection 9 plus its local `LITERATUR`, printed pages 71-76 / PDF
pages 72-77. Section 9 begins on the same printed page as the tail of section 8
and ends before section 10 begins on printed page 76.

Source corrections:

- corrected section/page references `§ 6`, `§ 3`, `S. 51`, and `H. Poincaré`
- corrected complete-induction notation: `φ(n)`, `α)`, `β)`, and
  `φ(n′) = (φ(n))′`
- corrected Brouwer's excluded-middle schema with `𝔄` and `𝔄̄`
- corrected `φ(n)` in the real-number sequence definition and
  `Entscheidung`
- rebuilt the binary-subdivision diagram that OCR had flattened into stray
  letters and fragments
- corrected `α`, `β`, Aristotle's Greek title `περὶ ἀτόμων γραμμῶν`,
  `Kap. VIII`, the Gassendi quote, and the literature page ranges

What the batch clarified:

- Brouwer is presented as the mathematician who refuses the `Sprung ins
  Jenseits`: no completed infinite domain is allowed to substitute for
  construction
- existential propositions over the infinite are `Urteilsabstrakte`; they are
  valuable only if they point back to a construction or proof
- complete induction remains the source of mathematical generality, but now as
  applied originary intuition rather than as a theorem over a completed set
- a universal assertion over natural numbers is hypothetical, not the infinite
  logical product of all individual assertions; this is why excluded middle has
  no unrestricted place
- Brouwerian real numbers are law-governed sequences, while the real variable or
  continuum is represented by a becoming choice sequence
- the continuum shifts from element-set to part-whole; it is an `extensive
  whole`, not an aggregate of fixed elements
- the dyadic subdivision tree is only an arithmetical empty form; its realization
  in an actual continuum is approximate, sharpening, and never fully exact at a
  finite stage
- Weyl ends with a real ambivalence: Brouwer gives maximum intuitive clarity,
  but at the cost of making higher mathematics painfully cumbersome

Translation decisions:

- `Intuitive Mathematik` is `intuitive mathematics`
- `Existentialsatz` is `existential proposition`
- `Urteilsabstrakt` is `judgment-abstract`
- `inhaltvolles Urteil` is `contentful judgment`
- `mathematische Urintuition` is `mathematical originary intuition`
- `Allheit` is `allness`
- `Wahlfolge` is `choice sequence`; `werdende Wahlfolge` is `becoming choice
  sequence`
- `Medium freien Werdens` is `medium of free becoming`
- `extensives Ganzes` is `extensive whole`
- `Dualbrüche` is `dyadic fractions`

Next batch:

- section 10, `Symbolische Mathematik`, printed pages 76-90 / PDF pages 77-91
