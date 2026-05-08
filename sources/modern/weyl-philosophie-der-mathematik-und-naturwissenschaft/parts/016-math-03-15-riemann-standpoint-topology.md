# Part 016: The Riemannian Standpoint. Topology

Fourth chapter-III batch. Section 15 completes `Geometrie` by moving from
dimension and orientation to differentiable manifolds, Riemannian metric
fields, general relativity, local frames, and topology. It is the explicit
handoff from mathematical geometry into physics.

## Scope

- `15. Der Riemannsche Standpunkt. Topologie`
- section-local `LITERATUR`
- printed pages `113-122`
- PDF/page-image pages `114-123`

Section 15 starts on printed page `113` / PDF page `114` after the section-14
Kant paragraph and ends with the literature list on printed page `122` / PDF
page `123`. PDF page `124` begins `ZWEITER TEIL: NATURWISSENSCHAFT`.

## Source Anchors

- `source/cleaned/010-math-03-geometrie.txt`
- `source/page-images/jpg-200/page-0114.jpg`
- `source/page-images/jpg-200/page-0115.jpg`
- `source/page-images/jpg-200/page-0116.jpg`
- `source/page-images/jpg-200/page-0117.jpg`
- `source/page-images/jpg-200/page-0118.jpg`
- `source/page-images/jpg-200/page-0119.jpg`
- `source/page-images/jpg-200/page-0120.jpg`
- `source/page-images/jpg-200/page-0121.jpg`
- `source/page-images/jpg-200/page-0122.jpg`
- `source/page-images/jpg-200/page-0123.jpg`

## Source Status

The active page range was visually checked against page images. The cleaned
German source was corrected for this batch, especially:

- coordinate notation in the local chart formulas: `x₁`, `xₙ`, `yᵢ`, `φᵢ`,
  `xₖ`, and `ψₖ`
- differential and Jacobian notation: `dxᵢ`, `dyᵢ`, `aᵢₖ`, `bₖᵢ`, `uₖ`,
  `vᵢ`, and the Jacobian determinant
- Riemannian metric notation: `ds²`, `gᵢₖ`, `dxᵢ dxₖ`, `P₀`, and the normal
  metric form `ds² = dx₁² + dx₂² + ... + dxₙ²`
- local-frame notation: `e₁, ..., eₙ`, `u₁e₁ + ... + uₙeₙ`, `Δ₀`,
  `zᵦ′`, `aᵦᵧ`, `eᵢᵦ`, and `gᵢₖ = eᵢ₁eₖ₁ + ... + eᵢₙeₖₙ`
- corrupted quotation marks around `Maßfeld`, `Nahgeometrie`,
  `Ferngeometrie`, `geometrischer`, `mitnehmen`, `Tensor`,
  `Elementarstücke`, `topologische Gerüst`, `Zusammenhangsverhältnisse`, and
  `Vergrößerungen`
- the topology skeleton notation `(ν — 1)ter Stufe` and the reference `§9`

## German Source

The visually corrected German for this long section is kept in
`source/cleaned/010-math-03-geometrie.txt`, from `15. Der Riemannsche
Standpunkt. Topologie` through the section-local `LITERATUR`, ending before
`[[pdf-page:0124 printed-page:123]]`.

Key formulas preserved in the cleaned source:

```text
yᵢ = φᵢ(x₁, ..., xₙ)        (i = 1, ..., m);
xₖ = ψₖ(y₁, ..., yₘ)        (k = 1, ..., n)

dyᵢ = Σₖ aᵢₖ · dxₖ,     dxₖ = Σᵢ bₖᵢ · dyᵢ,     (*)

ds² = Σᵢₖ gᵢₖ dxᵢ dxₖ     (**)

ds² = dx₁² + dx₂² + ... + dxₙ²

S: zᵦ′ = Σᵧ aᵦᵧzᵧ (β, γ = 1, ..., n),

z₁′² + ... + zₙ′² = z₁² + ... + zₙ²

gᵢₖ = eᵢ₁eₖ₁ + ... + eᵢₙeₖₙ.
```

## Translation

### 15. The Riemannian Standpoint. Topology

The concepts of dimension-number and sense are not restricted to metric
Euclidean or affine space. They hold for continuous manifolds in general.
Riemann was the first to analyze mathematically the general concept of an
n-dimensional manifold. A sufficiently small neighborhood of any arbitrary
point in an n-dimensional manifold can be mapped one-to-one and continuously
onto a region of n-dimensional number-space, the points of the latter being
n-tuples of real numbers (x₁, x₂, ..., xₙ). Every reversible one-to-one
transformation of the coordinates

```text
yᵢ = φᵢ(x₁, ..., xₙ)        (i = 1, ..., m);
xₖ = ψₖ(y₁, ..., yₘ)        (k = 1, ..., n)
```

supplies a new coordinate assignment that serves to represent the same
neighborhood. Is m necessarily equal to n? This is the question of the
topological invariance of the dimension-number.

Let P = (x₁, ..., xₙ) be a given point, and let P* = (x₁ + dx₁, ..., xₙ + dxₙ)
be any point lying infinitely near P. If the transformation-functions are
differentiable, then the components (dx₁, ..., dxₙ) of all infinitesimal
vectors →PP* issuing from P transform according to linear formulas:

```text
dyᵢ = Σₖ aᵢₖ · dxₖ,     dxₖ = Σᵢ bₖᵢ · dyᵢ,     (*)
```

Their coefficients aᵢₖ, bₖᵢ depend on the point P, but not on P*.
Infinitesimal magnitudes can be avoided by introducing an imaginary time τ and
letting a point move in the manifold according to an arbitrary law xₖ = xₖ(τ).
Suppose the point passes through P at the time τ = 0; its velocity at this time
is a vector in P with x-components uₖ = (dxₖ/dτ)_{τ=0}. The y-components vᵢ of
the same velocity are linked with the x-components by the equations (*):

```text
vᵢ = Σₖ aᵢₖuₖ,     uₖ = Σᵢ bₖᵢvᵢ,
```

which hold for all possible velocities in P. But these linear transformations
can be inverse to one another only when m = n and the determinant of the aᵢₖ,
the so-called Jacobian determinant, is different from zero. For the totality Ω,
only such "differentiable" transformations of the coordinates are now
admitted. Under these circumstances one speaks of a differentiable manifold.
Since the Jacobian determinant changes continuously with P, it is either
positive throughout the whole region covered by the two coordinate assignments,
or negative throughout it. In the first case we give the transformation the
signature +, in the second case −. Accordingly a "sense" can be fixed over the
whole region. One sees that both the dimension-number and the sense follow
from the fact that affine geometry holds in the infinitely small. While topology
has succeeded quite well in mastering continuity, we still do not understand
the inner meaning of the restriction to differentiable manifolds. Perhaps
physics will one day be able to dispense with it. At present it seems
indispensable, because the transformation laws of most physical magnitudes are
closely linked with those of the differentials dxᵢ (*).

Riemann, relying on Gauss's theory of curved surfaces, assumed that Euclidean
geometry holds in the infinitely small. The square of the length ds of the
infinitesimal vector →PP* with components dxᵢ can then be expressed by a
positive quadratic form

```text
ds² = Σᵢₖ gᵢₖ dxᵢ dxₖ     (**)
```

of the dxᵢ. Its coefficients gᵢₖ are independent of the vector →PP* with
components dxᵢ, but in general they will depend on the point P with coordinates
xᵢ and will be continuous functions of these coordinates. From the invariant
meaning of ds² it is clear how the components gᵢₖ of the "metric field"
transform in passing to a new coordinate system yᵢ. The metric of a
three-dimensional Riemannian space of this kind impresses itself on every
surface lying in it, which thereby is stamped as a two-dimensional Riemannian
space. By contrast, in three-dimensional Euclidean space two-dimensional
Euclidean geometry does not hold on every surface; for here all possible
two-dimensional Riemannian spaces appear as subspaces of three-dimensional
Euclidean space. Thus space in Euclidean geometry is of a much more special
nature, namely non-curved, than the possible surfaces in it, whereas the
Riemannian concept of space has exactly the right degree of generality to make
this discrepancy disappear.

Just as, according to Leibniz's principle of continuity, the true lawfulness of
nature finds its expression in laws of near-action, in which only the values of
physical magnitudes in space-time points in immediate neighborhood to one
another are linked, so the basic relations of geometry should refer only to
infinitely near neighboring points, to "near-geometry" as opposed to
"far-geometry." Only in the infinitely small may we expect to encounter the
elementary laws that are the same everywhere; therefore the world must be
understood from its behavior in the infinitely small.

If, however, one demands the metric homogeneity of space, and space as the form
of appearances is necessarily homogeneous, then one immediately falls back from
the Riemannian to the classical concept of space, to which the Helmholtzian
postulates concerning the motion group lead. But Riemann assumed that the
metric field is not rigidly given once and for all, but stands in causal
dependence on matter and changes along with it. For him it does not belong to
the resting homogeneous form of appearances, but to changeful material
happening. Riemann asks after the inner ground of the metric relations of
space, and after distinguishing, in the words cited on p. 62, the case of the
discrete and the continuous manifold, he continues: "Either, then, the actual
that underlies space must form a discrete manifold, or the ground of metric
relations must be sought outside it, in binding forces acting upon it." The
metric field manifests itself by means of its physical effects, which it exerts
on rigid bodies, light rays, and all natural processes; from these alone can we
read off its state. But what acts must also undergo action, must itself be
something real, and cannot sit enthroned in "geometrical" rigidity,
unassailable above the forces of matter.

In this way, despite the inhomogeneity of the metric field, the free mobility
of bodies without changes of measure is recovered, since a body will "carry
along" the metric field generated or deformed by it during its motion. After
extending space through time into the full extensive medium of the external
world, Einstein developed the Riemannian thought into a physical theory of
gravitation elaborated in every detail, and in particular also discovered the
laws according to which matter acts upon the metric field.

Riemann and Einstein assert that the group of geometrical and physical
automorphisms coincides with the totality Ω of all differentiable
transformations. In this respect their theories differ radically from the
standpoint set out in the previous section. Their principle of general
relativity is acceptable only after the metric field has been incorporated
among the physical magnitudes that act upon matter and experience reaction from
it. Nevertheless, Euclidean geometry is retained for the infinitesimal
neighborhood of any given point P₀. For it is a mathematical fact that, for all
line-elements in a given point P₀, the metric equation (**) assumes the special
form

```text
ds² = dx₁² + dx₂² + ... + dxₙ²
```

if suitable coordinates xᵢ have been chosen for the neighborhood of P₀. In
this form there is no room for any indeterminacy, and therefore we can say that
the nature of the metric is the same at every point. But the coordinate system
in which the metric law assumes this fixed normal form, and which, as I want to
express it, is characteristic for the "orientation" of the metric, is in
general different from place to place. We use an analogous manner of speaking
in Euclidean geometry when we say: all cubes of a given size are of the same
nature, but they differ by their "orientation." The nature of the metric is
one, absolutely given; only the mutual orientation at different points is
capable of continuous changes and dependent on matter. Euclidean space is to be
compared to a crystal built out of nothing but identical, unchangeable atoms in
the regular, rigid, unchangeable arrangement of a lattice; Riemannian space, to
a fluid that consists of the same mutually identical, unchangeable atoms, but
in a movable arrangement and orientation that yield to acting forces.

This perhaps comes out through another formulation of the Riemannian
conception, which has become indispensable for quantum physics if the
magnitudes characterizing a moving electron are to be fitted into the general
theory of relativity. From the explanation by velocities above, it is clear
what is meant by the collection of tangent vectors, or velocities, in P. They
form an n-dimensional vector space. The coordinate assignment P → xᵢ determines
a vector basis e₁, ..., eₙ in this tangent-vector space V(P) in P, so that
u₁e₁ + ... + uₙeₙ is the vector with x-components uᵢ. Suppose the vector space
in P possesses a Euclidean metric with an absolute standard of length. Then we
can introduce in it a local Cartesian reference frame 𝔣 = 𝔣(P), consisting of
n mutually perpendicular vectors of length 1. The arbitrariness in the choice
of this system is expressed by the group Δ₀ of Euclidean rotations. This group
consists of all linear transformations

```text
S: zᵦ′ = Σᵧ aᵦᵧzᵧ (β, γ = 1, ..., n),
```

for which

```text
z₁′² + ... + zₙ′² = z₁² + ... + zₙ²
```

holds. Here the variables zᵦ are the components of an arbitrary vector of V(P)
with respect to the Cartesian system 𝔣. The numerical values eᵢᵦ (β = 1, ...,
n) of the components of each individual vector eᵢ (i = 1, ..., n) with respect
to 𝔣 describe the embedding of the system 𝔣 in space. Thus the n² magnitudes
eᵢᵦ, which depend on the choice of the coordinates xᵢ as well as on the
Cartesian system 𝔣(P) in P and are functions of P, can now serve to
characterize the metric field. For the Riemannian gᵢₖ one easily computes the
values

```text
gᵢₖ = eᵢ₁eₖ₁ + ... + eᵢₙeₖₙ.
```

Only when the coordinates xᵢ and a Cartesian system 𝔣(P) have been chosen at
each point P can all physical magnitudes be represented by numbers. The laws of
nature are invariant, first, with respect to arbitrary transformations of the
coordinates xᵢ, and, second, with respect to a rotation S of the system 𝔣(P)
that can depend arbitrarily and continuously on the point P. Thus there is this
double invariance: one described by the group Ω of all transformations of the
coordinates xᵢ, and the other by an element of the group Δ₀ that can change
arbitrarily with the position of P.

What happened in the transition from the special to the general theory of
relativity is obviously the following. The physical automorphisms, which, as
described in the previous section, form the group Δ, have been decomposed into
their components, the translations and rotations. The translation group has
been replaced by the group of all possible transformations of the coordinates,
whereas the rotations have indeed remained Euclidean rotations, but are now
linked with a center P and are able to vary freely while the center P moves
over the manifold. Space, the extensive medium of the material world, is quite
clearly the seat of the group Ω of coordinate transformations; but the group Δ₀
seems to have its origin in the final elementary particles of matter. The
magnitudes eᵢᵦ are therefore the mediators between matter and space.

The question arises from what inner grounds nature has selected precisely Δ₀
among all possible groups of homogeneous linear transformations. One answer is
supplied by the Helmholtzian theory, according to which Δ₀ is completely
characterized by the axiom of free mobility: every incident set σ of 1-, 2-,
..., (n − 1)-dimensional directions can be carried into every other such set by
a transformation of Δ₀, while those transformations of Δ₀ that leave a given
set σ of incident directions fixed form a subgroup containing only two
elements, namely the identity and the reflection in σ. This characterization,
however, is less convincing now that the group no longer serves to describe
the mobility of a rigid body. Besides, it fails for the Lorentz group, which in
the four-dimensional world takes the place of the orthogonal group in
three-dimensional space.

The group Δ₀ could be considered as an abstract group for which different
representations by linear transformations are characteristic for different
physical magnitudes: for example, the representation of Δ₀ by orthogonal
transformations themselves for vectors, a certain "tensor" representation for
the electromagnetic field strength, and then a very remarkable one, namely the
so-called spinor representation for the electromagnetic wave-field.

Topology. In general, a coordinate assignment covers only a part of a given
continuous manifold. The "coordinate" (x₁, ..., xₙ) is a symbol consisting of
real numbers. One can think of the continuum of real numbers as created by
iterated bisection. In order to master the nature of a manifold as a whole,
topology had to develop combinatorial schemata of a more general nature. By
this combinatorial description it then got free of the restriction to
differentiable manifolds.

In order to subject a continuum to mathematical treatment, one must assume that
it has been divided into "elementary pieces" and that this division is steadily
refined by continually repeated subdivision according to a fixed schema. In the
one-dimensional case this schema consists in the bisection of every elementary
segment. The continuum is thereby overspun with an ever denser division-net.
Thus each continuum really has its own arithmetical schema, already completely
fixed by the combinatorial description of the way in which the individual
elementary pieces in the initial division border on one another, by the
"topological skeleton" of the manifold. The introduction of numerical
coordinates by relation to the special division-schema of the open
one-dimensional continuum is a forcible imposition, practically justified only
by the especially convenient calculational treatment of the ordinary number
continuum with its four operations.

The topological skeleton determines the "connectedness relations" of the
manifold on the large scale. It is an important but difficult mathematical
question when two such skeletons are equivalent, that is, capable of
representing the same continuum decomposed into elementary pieces in two
different ways. In the case of an n-dimensional closed manifold, the skeleton
consists of finitely many elements of 0th, 1st, 2nd, ..., nth level, vertices,
edges, and so on, which must be marked by some symbols. An element of ν-th level
is bounded by certain elements of (ν − 1)th level; through these data the
skeleton is completely described. Analysis situs, or combinatorial topology, is
concerned with the demands to be made on such a skeleton, with the properties
it possesses, and with the question of equivalence.

Topology has this distinctive feature: the questions belonging to it may under
certain circumstances be decidable with certainty even when the continua to
which they are posed are not given exactly but only vaguely, as is always the
case in actuality. Thus the topological skeleton of an uninjured brick can be
read off with certainty; a thread running back into itself, which determines a
curve in the sense of exact geometry only approximately, is nevertheless with
certainty either knotted or not. Where the possible cases form a discrete
manifold, no inexactness occurs.

Thus in the rational treatment of a continuum one can distinguish three
levels: morphology, which operates with vaguely circumscribed gestalt types;
topology, which, guided by conspicuous singularities or in free construction,
sees a skeleton into the manifold, vaguely localized but combinatorially
exactly determined; and geometry proper, operating with ideal formations, which
could be exactly carried into an actual continuum only if this continuum were
overspun with a division-net refining and sharpening itself into infinity. The
geometrical properties independent of the division-net of the formations
constructible in the continuum may rest on a structural field spread out in it,
after the manner of the metric field. What significance idealizing geometry
has in actuality despite the evident unfulfillability of the requirement just
set up for its application, we will discuss in the natural-scientific part.

In the ascent just described, the sensuous-categorial double face of geometry
reveals itself, on account of which Plato already assigned geometrical figures
a middle position between the Ideas and sensible things. For a more careful
phenomenological analysis of the opposition between the vague and the exact,
and of the concept of limit, I refer to O. Becker's work cited at the end of
§9. When we undertake the subdivision of the topological skeleton according to a
fixed schema, this means for a concretely present continuum that we assume we
were not mistaken, at the first division into pieces, about the analysis-situs
constitution of these elementary pieces. We therefore exclude the possibility
that, upon closer investigation of a surface, it could turn out that what we
took for an elementary piece in truth bears small attached handles, giving the
piece different connectedness relations, and so in infinitum, with ever
stronger "magnifications," ever new topological complications would be
uncovered.

The Riemannian standpoint permits, also for actual space, quite different
topological connectedness relations than those possessed by Euclidean space.
Only on the basis of the more general and freer conception of geometry
developed by the mathematics of the last century, only with an open eye for the
thinkable possibilities it has uncovered, can the problem of space today, I
believe, be attacked in a philosophically fruitful way.

Literature

P. Alexandroff, Einfachste Grundbegriffe der Topologie. Berlin 1932.

P. Alexandroff and H. Hopf, Topologie. Berlin 1935.

H. v. Helmholtz, Über die Tatsachen, die der Geometrie zugrunde liegen (1868).
Wiss. Abhandl. II, p. 618.

B. Riemann, Über die Hypothesen, welche der Geometrie zugrunde liegen (1854).
Ges. math. Werke 1876; separate edition with notes by H. Weyl, Berlin 1923.

O. Veblen, Analysis situs. A. Math. Soc. Colloquium Publications, 2nd ed. New
York 1931.

H. Weyl, Mathematische Analyse des Raumproblems. Berlin 1923.

## Notes

Section 15 completes the bridge from geometry to physics. Section 14 already
separated physical automorphisms from geometrical automorphisms; section 15
shows how Riemann and Einstein alter the whole setting by making the metric
field itself physical. General relativity is acceptable only after the metric
field is included among the magnitudes that act and are acted upon.

The crucial Riemannian move is local. Euclidean geometry survives in the
infinitely small, but the coordinate system in which the metric assumes its
normal form changes from point to point. Weyl's crystal/fluid analogy makes the
contrast vivid: Euclidean space is a rigid lattice; Riemannian space has the
same local metric nature but variable mutual orientation.

The local-frame discussion is the strongest physics handoff. The double
invariance under coordinate transformations Ω and point-dependent rotations Δ₀
prefigures the frame/gauge language needed for quantum physics and spinors.
Weyl explicitly says the quantities eᵢᵦ mediate between matter and space.

Topology closes the chapter by relaxing differentiability and replacing
coordinate domination with combinatorial skeletons. This is not an escape from
actual vagueness: topology matters precisely because some questions are exactly
decidable even when the given continuum is vague. Weyl's three levels are
morphology, topology, and idealizing geometry.

This modifies the chapter-II dossier. The chapter-II problem of the infinite
as a symbolic construction returns as an infinite refinement of a division-net:
ideal geometry can be applied exactly only under an unrealizable limiting
demand. Topology marks a middle discipline where combinatorial exactness can
operate on vague givens without pretending that the given continuum is already
an exact ideal object.

## Translation Decisions

- `Der Riemannsche Standpunkt` is `the Riemannian standpoint`
- `Dimensionszahl` remains `dimension-number`
- `Mannigfaltigkeit` is `manifold`
- `eineindeutig und stetig` is `one-to-one and continuous`
- `umkehrbar eindeutige Transformation` is rendered as `reversible one-to-one
  transformation`
- `Jacobische Determinante` is `Jacobian determinant`
- `Signatur` is `signature`
- `Unendlichkleine` is `infinitely small`
- `Nahgeometrie` is `near-geometry`; `Ferngeometrie` is `far-geometry`
- `Maßfeld` is `metric field`
- `wirkt, muß auch leiden` is `what acts must also undergo action`
- `allgemeine Relativität` is `general relativity`
- `örtliches kartesisches Bezugssystem` is `local Cartesian reference frame`
- `euklidische Drehungen` is `Euclidean rotations`
- `Darstellung` is `representation` in the group-theoretic physics passage
- `topologisches Gerüst` is `topological skeleton`
- `Zusammenhangsverhältnisse` is `connectedness relations`
- `Vergewaltigung` is `forcible imposition`
- `sinnlich-kategoriale Doppelantlitz` is `sensuous-categorial double face`
- `Denkbarkeiten` is `thinkable possibilities`

## Adversarial Check

The first risk is to read the Riemannian move as simply abandoning Euclidean
geometry. Weyl says the opposite: Euclidean metric form remains in the
infinitesimal neighborhood of each point, but the orientation of that local
form varies from point to point.

The second risk is to treat the metric field as merely geometrical. Weyl's
Riemann/Einstein reading makes it physical: it acts on matter, suffers reaction
from matter, and therefore cannot sit above material forces in geometrical
rigidity.

The third risk is to miss the local-frame physics. The introduction of 𝔣(P),
Δ₀, and eᵢᵦ is not decorative notation; it is the bridge to quantum physics,
representations, tensors, and spinors.

The fourth risk is to make topology into another exact ideal geometry. Weyl's
point is subtler: topology can be exact at the combinatorial level while its
skeleton is only vaguely localized in the actual continuum.
