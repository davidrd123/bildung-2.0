# Part 028: Appendix D, Chemical Valence and the Hierarchy of Structures

Appendix D is Weyl's clearest statement of why provisional diagrams can be
legitimate without being final. Chemical valence is not a primitive structure
for him. It is a useful symbolic layer whose apparent lines and bonds are
grounded by deeper quantum-mechanical and invariant-theoretic structures.

## Scope

- `Anhang D: Die chemische Valenz und die Hierarchie der Strukturen`
- printed pages `341-353`, PDF/page-image pages `342-354`
- cleaned source:
  `source/cleaned/017-appendix-d-chemische-valenz.txt`

The appendix begins with Kekulé's molecular diagrams as mediated structures,
derives valence from electron spin and antisymmetry, translates valence diagrams
into invariant theory, tests the apparatus on benzene resonance, and closes
with a methodological lesson about provisional symbolic schemata and the
possible quantum grounding of heredity.

## Source Anchors

- `source/cleaned/017-appendix-d-chemische-valenz.txt`
- `source/page-images/jpg-200/page-0342.jpg`
- `source/page-images/jpg-200/page-0343.jpg`
- `source/page-images/jpg-200/page-0344.jpg`
- `source/page-images/jpg-200/page-0345.jpg`
- `source/page-images/jpg-200/page-0346.jpg`
- `source/page-images/jpg-200/page-0347.jpg`
- `source/page-images/jpg-200/page-0348.jpg`
- `source/page-images/jpg-200/page-0349.jpg`
- `source/page-images/jpg-200/page-0350.jpg`
- `source/page-images/jpg-200/page-0351.jpg`
- `source/page-images/jpg-200/page-0352.jpg`
- `source/page-images/jpg-200/page-0353.jpg`
- `source/page-images/jpg-200/page-0354.jpg`

## Source Status

The appendix range was visually checked against the page images. The cleaned
German was corrected for this batch, especially:

- spin/wave-function notation: `ψ(P)`, `ψ(P₁, ..., P_f)`, `ψ(Pρ)`,
  `ψ_+(P)`, `ψ_−(P)`, `ψ(P₁ρ₁, ..., P_fρ_f)`, and `φ(ρ₁, ..., ρ_f)`
- spin-variable algebra: `φ_g`, `φ_f`, `φ_{f−1}`, `φ_0`, `2^f`,
  `x_+`, `x_-`, and the summation formula for symmetric spin functions
- linear-transformation notation: `x′_+`, `x′_-`, `αδ − βγ = 1`, `f_a`,
  `f_b`, and invariants `F(x, y, ...)`
- atomic-system notation: `O_a`, `O_b`, `hν_a`, `hν_b`, `ν_0`,
  `Π_v`, `n_v`, `Σ_v n_v(v + 1)`, and `Δν = V(O_a, O_b, ...)`
- invariant-theory notation: `[xy] = x_+y_- − x_-y_+`,
  `[xy]^d [xl]^{a−d} [yl]^{b−d}`, and form factor `λ`
- benzene-resonance notation: `A`, `A′`, `B₁`, `B₂`, `B₃`, `β₁`,
  `β₂`, `β₃`, and `√13`
- hierarchy markers: `α`, `β`, `γ`, and the historical descent
  `γ → β → α`
- OCR residues in the Sylvester footnote, Cusanus passage, and final
  combinatorics/biology bridge

The benzene diagrams are retained as compact diagram descriptions in the
cleaned text; the page images remain the authority for the visual layout.

## Translation / Analytic Digest

Weyl opens by distinguishing two kinds of structure. Quantum theory may be
primitive and irreducible for atomic phenomena, but Kekulé's aggregate of
atomic points joined by valence lines is mediated. Valence lines are convenient
symbols for deeper quantum-mechanical forces among atoms, which are themselves
complex dynamic systems. The Kekulé diagram is therefore grounded in a primary
structure beneath it. Weyl names this, after Hilbert, a `Tieferlegung der
Fundamente`: a lowering or deepening of the foundations.

The chemistry discussion continues Appendix C's antisymmetry line. If position
alone supplied a finest grid, an electron wave-state would be a complex-valued
function over spatial positions. For an aggregate of electrons the wave
function must be antisymmetric under odd permutations. The Pauli exclusion
principle follows from this antisymmetry, because a suitable antisymmetric
function vanishes when two relevant arguments coincide.

Spin adds the decisive complication. The electron wave function depends on a
continuous position variable `P` and a two-valued spin variable `ρ`. Pauli's
spinor representation from section 15 returns here: the two components
`ψ_+(P)` and `ψ_−(P)` transform under rotations. Even if the dynamic influence
of spin is neglected, spin cannot be ignored, because antisymmetry applies to
the pairs `(Pρ)`. Spin therefore changes the multiplicity and valence
structure of the possible terms.

Weyl then defines valence through permutation symmetry. If the spatial factor
`η(P₁, ..., P_f)` is antisymmetric, the spin factor `φ(ρ₁, ..., ρ_f)` must be
symmetric. A symmetric spin function is characterized by the number `g` of
spin arguments equal to `+1`, giving `f + 1` values. If `η` were symmetric,
`φ` would need to be antisymmetric; because the spin space has only two
values, such a function vanishes for `f > 2`. Valence is thus not a primitive
chemical line count. It is a number describing the available permutation
symmetry types of spin functions.

The next layer treats a neutral atom as `f` electrons around a nucleus of
charge `f · e`. For an S-state with highest valence, the probability of finding
an electron at distance greater than `r` decreases exponentially. When several
neutral atoms are placed far apart, the first approximation assigns electrons
to neighborhoods of nuclei and thereby temporarily violates the full equality
of all electrons. Reintroducing the small interaction among atoms splits the
term `ν_0` through `Permutationsresonanz` into molecular term systems for
different valences.

Invariant theory supplies the middle symbolic layer. Each atom gets a binary
vector such as `x = (x_+, x_-)`, and the valence state `Π_v` is described by
invariants of specified degrees. The simplest invariant is the bracket factor
`[xy] = x_+y_- − x_-y_+`. Products of such bracket factors are monomial
invariants, and their diagrams are exactly Kekulé's valence diagrams. This is
the structural bridge: valence diagrams are not false, but they are the visible
monomial pieces of a larger linear invariant space.

The two-atom case behaves as the valence diagram suggests. For atoms of
valences `a` and `b`, the invariant `[xy]^d [xl]^{a−d} [yl]^{b−d}` records
`d` binding valence lines and the remaining free lines. The energy correction
has a form factor `λ`, and negative `λ` is sufficient for a stable molecular
state. With more than two atoms, the classical diagram picture becomes
inadequate: linear relations among monomial invariants reduce the number of
independent possibilities, and stationary quantum states generally become
linear combinations of pure valence states.

Benzene is the test case. Kekulé's formula allows two diagrams, while
ortho-derivatives show only one natural case. Weyl reduces the benzene ring to
six equal atoms with one remaining electron each and considers the five
monomial invariants `A`, `A′`, `B₁`, `B₂`, and `B₃`. The stable state is not
one pure diagram. It is a linear combination: a correction to the difference of
Kekulé's two diagrams plus a multiple of the sum of the Dewar diagrams.
Modern structural chemistry succeeds by holding onto useful valence schemata
while minimizing the corrections forced by resonance.

The philosophical lesson is the hierarchy:

- `α`: the quantum-mechanical structures themselves
- `β`: the molecule as a linear manifold of binary invariants
- `γ`: the valence diagrams used for chemical interpretation

Historically, discovery moved downward: Kekulé's diagrams at `γ`, Sylvester's
invariant-theory analogy at `β`, and only later quantum mechanics at `α`.
Philosophically, explanation moves upward from the deeper structure to the
usable diagram. This is the strongest methodological point of the appendix:
do not take provisional combinatorial diagrams too literally, but draw them
clearly anyway. A sharp limited symbol is better than a vague all-purpose one.

The final pages connect chemistry back to genetics and forward to Appendix E.
Weyl explicitly compares gene aggregates and chromosomal linkages to valence
diagrams: both are provisional combinatorial abstractions of limited validity.
The inheritance laws likely rest on the same quantum-mechanical structure as
chemical laws, but a mediating structure would need to account for the chemical
complexity of living carriers. He then asks whether the mathematics of large
permutation groups might be connected to a future quantum theory of organic
processes.

Appendix D therefore does not merely extend Appendix C's quantum chemistry. It
also states a source-local rule for this project: images and diagrams are
valuable when clear, limited, and known to be provisional. The danger is not
diagramming. The danger is forgetting which layer of the hierarchy a diagram
belongs to.

## Translation Decisions

- `chemische Valenz` is `chemical valence`
- `Valenzstrich` is `valence line`
- `Valenzdiagramm` is `valence diagram`
- `Tieferlegung der Fundamente` is `deepening/lowering of the foundations`;
  keep the German visible
- `Hierarchie der Strukturen` is `hierarchy of structures`
- `Elektronenspin` is `electron spin`
- `Spinordarstellung` is `spinor representation`
- `Valenzausdruck` is `valence expression`
- `S-Zustand` is `S-state`
- `Invariante` is `invariant`
- `Klammerfaktor` is `bracket factor`
- `monomische Invariante` is `monomial invariant`
- `reiner Valenzzustand` is `pure valence state`
- `Permutationsresonanz` is `permutation resonance`
- `quantenmechanische Resonanz` is `quantum-mechanical resonance`
- `Strukturchemie` is `structural chemistry`
- `Genaggregate` is `gene aggregates`

## What Appendix D Adds

- It gives Weyl's most explicit rule for layered explanation: a symbolic
  schema can be valid at one level while grounded by a deeper level.
- It links Appendix C's antisymmetry and Pauli principle directly to chemical
  valence and molecular bonding.
- It shows why classical-looking diagrams can remain useful after quantum
  theory: they are monomial invariant diagrams, not final pictures of reality.
- It connects mathematics, chemistry, and genetics through provisional
  combinatorial schemata.
- It makes the appendix campaign point forward to biology: the next live
  problem is the missing mediating structure between genetic diagrams and
  quantum physics.
