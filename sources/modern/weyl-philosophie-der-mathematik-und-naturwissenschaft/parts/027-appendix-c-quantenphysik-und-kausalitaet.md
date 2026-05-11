# Part 027: Appendix C, Quantum Physics and Causality

Appendix C is Weyl's explicit quantum correction to section 23. It does not
merely add later physics. It sharpens the earlier causal argument by separating
three levels: strict causal evolution of the wave-state, probabilistic
projection in measurement, and thermodynamic-statistical directionality for the
arrow of time.

## Scope

- `Anhang C: Quantenphysik und Kausalität`
- printed pages `324-340`, PDF/page-image pages `325-341`
- cleaned source:
  `source/cleaned/016-appendix-c-quantenphysik-und-kausalitaet.txt`

The appendix begins with the claim that modern quantum theory has abandoned
strict causal determination for elementary atomic processes. It then develops
the photoelectric effect, polarization, quantum grids/sieves, noncommuting
observables, the wave-state/measurement split, composite systems, Pauli
antisymmetry, quantum logic, and the future-directed emission problem.

## Source Anchors

- `source/cleaned/016-appendix-c-quantenphysik-und-kausalitaet.txt`
- `source/page-images/jpg-200/page-0325.jpg`
- `source/page-images/jpg-200/page-0326.jpg`
- `source/page-images/jpg-200/page-0327.jpg`
- `source/page-images/jpg-200/page-0328.jpg`
- `source/page-images/jpg-200/page-0329.jpg`
- `source/page-images/jpg-200/page-0330.jpg`
- `source/page-images/jpg-200/page-0331.jpg`
- `source/page-images/jpg-200/page-0332.jpg`
- `source/page-images/jpg-200/page-0333.jpg`
- `source/page-images/jpg-200/page-0334.jpg`
- `source/page-images/jpg-200/page-0335.jpg`
- `source/page-images/jpg-200/page-0336.jpg`
- `source/page-images/jpg-200/page-0337.jpg`
- `source/page-images/jpg-200/page-0338.jpg`
- `source/page-images/jpg-200/page-0339.jpg`
- `source/page-images/jpg-200/page-0340.jpg`
- `source/page-images/jpg-200/page-0341.jpg`

## Source Status

The appendix range was visually checked against the page images. The cleaned
German was corrected for this batch, especially:

- photoelectric-effect notation: `ν`, `hν`, `ν = eV/h`, and Planck's constant
  `h`
- polarization notation: vectors `z⃗`, `s⃗`, components `s₁`, `s₂`, and the
  probability expression `s₁² + s₂² = 1`
- Stern-Gerlach / magnetic-moment notation: `mₓ`, `+μ`, `—μ`
- classical sieve/grid notation: `MM = M`, `FF = F`, `MF = FM = 0`,
  `E₁ ... Eᵣ`, `EᵢEₖ′`, and `αᵢ`
- finite-dimensional quantum model notation: `x⃗`, `Eᵢx⃗`,
  `pᵢ = |Eᵢx⃗|² / |x⃗|²`, `I = E₁ + ... + Eᵣ`, and noncommuting `G`, `G′`
- dynamical-law notation: `dx⃗/dt = Lx⃗`, `dxᵢ/dt = Σⱼ lᵢⱼxⱼ(t)`, and
  antisymmetric coefficients `lⱼᵢ = −lᵢⱼ`
- complex-vector and Schrödinger notation: `dx⃗/dt = iνx⃗`,
  `x⃗₀{cos(νt) + i sin(νt)}`, `Uⱼ = hνⱼ`, `H = (h/i)L`, and
  `(h/i) · dx⃗/dt = Hx⃗`
- measurement-system notation: `Σ`, `Σ*`, and the enlargement of the original
  system by including the grid
- product-space / tensor notation: `Σ`, `Σ′`, `S`, `S′`, `zᵢₖ = xᵢyₖ`,
  `|zᵢₖ|² = |xᵢ|²|yₖ|²`, and symmetric/antisymmetric tensor conditions
- summary and literature residue: `Eulersche Prinzip`, `Quantenlogik`,
  `P. A. M. Dirac`, and Rosenfeld's French title

The printed source has an awkward sentence applying the symmetry condition to
an `Elektronenschauer` while immediately noting that the Pauli prohibition does
not apply to photons. The cleaned text preserves the printed wording rather
than silently emending it to `Photonenschauer`.

## Translation / Analytic Digest

Weyl's opening claim is stronger than a claim about ignorance. Quantum theory
does not merely say that we lack hidden details behind atomic events. It says
that the sort of strict causal determination one may still imagine behind
gas-thermodynamic regularities is not available at the elementary quantum
level. The uncertainty of an atomic experiment is not a temporary defect that
could be driven to zero by better knowledge of hidden factors.

The photoelectric effect gives the first decisive pressure. Field theory would
describe weak light as a fraction of a continuous energy-field. Quantum theory
requires that the same situation be read as a small probability for the
presence of a photon with energy `hν`. Intensity governs the number of emitted
electrons, not the energy of each electron. Probability has become attached to
physical reality, not just to incomplete bookkeeping.

Polarization supplies Weyl's cleanest pedagogical model. A polarized wave-state
is already maximally homogeneous, yet when it passes through a differently
oriented Nicol prism it splits again according to probabilities determined by
the new orientation. The Stern-Gerlach example makes the same point for silver
atoms. A vector whose components in every possible direction are only `+μ` or
`—μ` is a geometrical absurdity. The impossibility is in the nature of the
thing, not in human clumsiness.

Weyl then turns Eddington's image into formal apparatus: in relativity the
observer goes out with a measuring rod; in quantum theory he goes out with a
sieve. A classical grid classifies states in an aggregate, and different
classifications can be overlaid because the operations commute. A quantum grid
is a decomposition of vector space into orthogonal subspaces. Applying the
grid is not a harmless classification. It throws the system from the wave-state
`x⃗` into one of the projected wave-states `Eᵢx⃗`, with only the probabilities
fixed in advance.

This is the conceptual center of the appendix. The wave-state changes by a
strict causal dynamical law, but the relation between wave-state and
quantum-state is probabilistic. Causality is not globally abolished; it is
relocated. Weyl keeps causal law for the continuous evolution of `x⃗`, then
withdraws strict causal determination from measurement outcomes.

Noncommuting grids make the philosophical cost explicit. If two grids commute,
their features can be combined as in classical logic. If they do not commute,
then the features are incompatible. Position and momentum are Weyl's physical
case, and Heisenberg's uncertainty principle is the precise form of Bohr's
complementarity. The classical question "green and round" becomes meaningless
if green and round are features defined only by incompatible grids.

Measurement also reopens Weyl's subject/object problem from sections 17 and
20. Experimental physicists always knew that measurement involves reaction of
instrument on object. Quantum physics makes that reaction principled for
atomic-scale objects. The idea of facts standing independently above
observation becomes doubtful at exactly the scale where no instrument can be
made infinitely more delicate than its object.

The Hilbert analogy is important. The unobserved physical process is represented
by mathematical formalism without intuitive interpretation. Only the concrete
experiment, the grid-measurement, can be intuitively described. Weyl maps this
onto Hilbert's contrast between formalism and meaningful mathematical thinking.
If we include the measuring grid in the original system and treat the
measurement as a physical process, then the enlarged system must itself be
measured by another grid. The cut moves; it does not disappear.

The composite-system argument gives Weyl his strongest whole/part claim.
Classically, two systems combine by taking pairs of states. Quantum theory
agrees only at the level of complete grids. At the level of wave-states, the
product space contains many more possible states than those generated by
products `x⃗ × y⃗` of separate part-states. In this precise sense the whole has
more possible wave-states than the mere combination of its parts, and the
probabilities of the whole cannot generally be recovered by the product rule
for statistically independent parts, even without dynamic interaction.

The Pauli exclusion principle then becomes a case of wave-state structure.
For two equal systems, the product-space tensors split into symmetric and
antisymmetric forms. Electrons empirically occupy the antisymmetric case, so
the probability that two electrons are found in the same complete quantum state
is zero. Appendix B introduced Pauli as a fact about individuation and
statistics; Appendix C explains it through the permanent antisymmetry of the
wave-state and immediately ties it to chemical bonding.

Weyl's six concluding claims are the philosophical payload:

- observation necessarily disturbs the phenomenon, with only statistical
  prediction of the disturbance
- features belonging to different grids cannot always be combined by classical
  `and` or `or`; quantum physics requires a kind of quantum logic
- causality holds for the temporal change of the wave-state, but not for the
  relation between wave-state and quantum-states
- the whole has more possible wave-state changes than the combination of its
  parts
- the Leibniz-Pauli exclusion principle follows from antisymmetry
- primary probability is a fundamental property of nature itself, independent
  of observer knowledge or ignorance

The appendix closes by returning to section 23's problem of past and future.
Elementary field formulas can be time-symmetric. But quantum emission has a
split between induced processes, which are symmetric with respect to past and
future, and spontaneous emission, which has no corresponding spontaneous
absorption. Weyl roots that asymmetry not in elementary laws but in the same
statistical principles that ground increasing entropy.

## Translation Decisions

- `Kausalbestimmung` is `causal determination`
- `Wellenzustand` is `wave-state`
- `Quantenzustand` is `quantum state`
- `Sieb` is `sieve`
- `Gitter` is `grid`; use `sieve` when Weyl is preserving Eddington's image
- `Observable` is `observable`
- `vertauschbar` is `commuting` for operators/grids
- `unverträglich` is `incompatible`
- `Unbestimmtheitsprinzip` is `uncertainty principle`
- `Komplementarität` is `complementarity`
- `Quantenlogik` is `quantum logic`
- `primäre Wahrscheinlichkeit` is `primary probability`
- `Antisymmetrie` is `antisymmetry`
- `Zerstrahlung` is preserved in German when naming Dirac's term; explain in
  prose as annihilation with photon emission
- `spontane Emission / erzwungene Emission` is `spontaneous emission / induced
  emission`

## What Appendix C Adds

- It prevents section 23 from being read as a simple retreat from causality.
  Weyl preserves strict causal law for wave-state evolution while denying
  strict causal determination of measurement outcomes.
- It makes probability ontological in Weyl's own terms: `primary probability`
  is not merely ignorance but a fundamental feature of nature.
- It links the subject/object problem to physics rather than epistemological
  introspection alone: observation becomes a principled physical intervention.
- It gives the Hilbert/formalism analogy a natural-scientific counterpart:
  formal evolution without intuitive meaning versus concrete meaningful
  measurement.
- It strengthens the whole/part thread with a precise quantum argument from
  product spaces and non-factorable wave-states.
- It reconnects the arrow of time to thermodynamic probability rather than
  elementary laws, sharpening the end of section 23.
