# Part 013: Projective Geometry And Color Space

First chapter-III batch. Section 12 moves from non-Euclidean geometry through
analytic and vector geometry into dimension, projective geometry, and the color
space. It makes geometry a bridge case: formalization opens dimensions beyond
the actual three-dimensional space, while color shows that geometrical
treatment is not restricted to space.

## Scope

- chapter-III opening paragraph
- `12. Nichteuklidische, analytische, mehrdimensionale, affine, projektive
  Geometrie. Der Farbraum`
- section-local `LITERATUR`
- printed pages `91-95`
- PDF/page-image pages `92-96`

The initial campaign note listed printed pages `91-94` / PDF pages `92-95`.
Direct inspection showed that section 12 continues onto printed page `95` /
PDF page `96`, including the end of the color-space discussion and the
literature list.

## Source Anchors

- `source/cleaned/010-math-03-geometrie.txt`
- `source/page-images/jpg-200/page-0092.jpg`
- `source/page-images/jpg-200/page-0093.jpg`
- `source/page-images/jpg-200/page-0094.jpg`
- `source/page-images/jpg-200/page-0095.jpg`
- `source/page-images/jpg-200/page-0096.jpg`

## Source Status

The active page range was visually checked against page images. The cleaned
German source was corrected for this batch, especially:

- `§ 4`, `§ 2`, `§ 20`, and `§§ 1-4` where OCR read section signs as dollar
  signs or digits
- German quotation marks around `euklidischen`, `kongruent`, `unendlich fernen
  Punkte`, `Identität`, and `vernünftiger`
- the footnote marker after `vollzogen¹)`, `Descartes' Géométrie`, and
  `Graßmanns „Ausdehnungslehre“`
- subscript notation in `x = x₁e₁ + x₂e₂` and its surrounding `e₁/e₂`,
  `x₁/x₂` references
- the literature references for Helmholtz and Weyl

## German

```text
[[pdf-page:0092 printed-page:91]]

III. Geometrie

Wohl an keiner Stelle durchdringen sich Mathematik, Naturwissenschaft und Philosophie so innig wie im Problem des Raumes. Die von
der Mathematik erarbeiteten Voraussetzungen zu seiner Diskussion
sollen noch in diesem Teil kurz besprochen werden.

12. Nichteuklidische, analytische, mehrdimensionale, affine,
projektive Geometrie. Der Farbraum

Über die nicht-euklidische Geometrie ist dem, was in § 4 aus Anlaß
der Axiomatik gesagt wurde, nicht viel hinzuzufügen. Bei Aufrechterhaltung aller übrigen Axiome der euklidischen Geometrie bestehen die
drei Möglichkeiten, daß in einer Ebene zu einer Geraden durch einen
nicht auf ihr gelegenen Punkt unendlich viele, eine oder keine nichtschneidende Gerade existiert („hyperbolischer, parabolischer und elliptischer Fall“ nach Klein); die Winkelsumme im Dreieck ist entsprechend
kleiner, gleich oder größer als 180°. Die letzte Möglichkeit, auf die erst
Riemann Mitte des 19. Jahrhunderts hinwies, besteht nur, wenn die
Axiome der Anordnung dahin modifiziert werden, daß die Gerade nicht
als offene, sondern als geschlossene Linie erscheint. Die ebene elliptische
Geometrie ist keine andere als die, welche auf einer Kugel im euklidischen Raum gilt; nur muß man je zwei diametral gegenüberliegende
Kugelpunkte identifizieren. Oder anders ausgedrückt: indem wir alle
übrigen auf die Geometrie der Ebene E bezüglichen Worte in ihrem
gewöhnlichen „euklidischen“ Sinne verstehen, soll allein die Bedeutung
des Kongruenzbegriffes dahin modifiziert werden, daß zwei Figuren in
E als „kongruent“ gelten, wenn ihre Projektionen von einem außerhalb
E gelegenen Zentralpunkt O aus auf eine um O beschriebene Kugel im
gewöhnlichen Sinne kongruent sind. Der Ebene müssen dabei die „unendlich fernen Punkte“ einverleibt werden, deren Projektionsstrahlen
die zu E parallelen Geraden durch O sind. Die Abbildungen von E,
welche „kongruente“ Figuren ineinander überführen, lassen sich auch
ohne Bezugnahme auf den Raum als Kollineationen charakterisieren
mit ähnlicher Invarianzeigenschaft wie im Kleinschen Modell der Bolyai-Lobatschewskyschen Geometrie; und damit ist die Bahn frei zur Begründung nicht nur der ebenen, sondern auch der räumlichen elliptischen Geometrie. Das wahre Verhältnis der drei Arten von Geometrie

[[pdf-page:0093 printed-page:92]]

kommt am besten zum Ausdruck, wenn man von dem maßfreien projektiven Raum seinen Ausgang nimmt und in ihn eine „Cayleysche Maßbestimmung“ einbaut. Je nach dem Charakter des dabei zugrunde gelegten absoluten Kegelschnitts ergibt sich die eine oder andere der drei
metrischen Geometrien. So hat Klein selber seine Konstruktion aufgefaßt: als Einbau der Lobatschewskyschen Geometrie in den projektiven,
nicht als Herstellung eines Modells durch den metrisch-euklidischen
Raum.

Die analytische Geometrie führt jedes geometrische Problem
auf ein algebraisches zurück. Vorbedingung dafür ist, daß der
Zahlbegriff durch Aufnahme der Brüche und des Irrationalen diejenige Weite bekommen hat, welche ihn über die Zählung hinaus
zur Größenmessung geeignet macht. Nicht die Griechen, sondern
die Inder und Araber haben diesen Schritt vollzogen¹). Ihren
Bahnen folgte die abendländische Mathematik, die zu selbständigen Leistungen in der Geometrie erst gelangte, nachdem die Raumwissenschaft durch Descartes’ Géométrie (1637) dem algebraischen
Kalkül unterworfen war.

Heute behandelt man die analytische Geometrie wohl am besten
nach dem Vorbild von Graßmanns „Ausdehnungslehre“ durch Heranziehung des Vektorbegriffs. Der Vektorkalkül ist ein Rechenverfahren,
dessen Objekte nicht Zahlen, sondern geometrische Gebilde sind. Eine
solche Behandlung der Geometrie war von Leibniz gefordert, ja zum
Teil schon durchgeführt worden in seiner Schrift de analisi situs und dem
Entwurf einer geometrischen Charakteristik (Math. Schriften V, S. 178,
und II, S. 20), die in den Rahmen seiner „universellen Charakteristik“
gehören. Die Translationen oder Parallelverschiebungen des Raumes
bezeichnet man als Vektoren. Ein Punkt A geht durch die Translation a
in einen Punkt Aa = B über, den „Endpunkt des von A aufgetragenen
Vektors a“. Umgekehrt aber existiert, wenn A, B irgend zwei Raumpunkte sind, eine und nur eine Translation a, welche A in B überführt.
Zu den Translationen rechnen wir insbesondere die „Identität“, welche
alle Punkte fest läßt, den Vektor 0. Translationen lassen sich zusammensetzen, sie bilden eine Gruppe; durch Hintereinanderausführung zweier
Translationen a, b kommt ein Effekt zustande, der auch durch eine

1) Descartes spricht von dem „Bedenken der Alten gegen den Gebrauch
von Bezeichnungen der Arithmetik in der Geometrie, welches nur daraus
entspringen konnte, daß ihnen der Zusammenhang dieser beiden Disziplinen
nicht hinreichend klar geworden war“.

[[pdf-page:0094 printed-page:93]]

einzige, die resultierende Translation a + b erreicht werden kann. Der
Zahlbegriff dringt dadurch in die Geometrie ein, daß eine Translation a
iteriert, beliebig oft zu sich selbst addiert wird (vgl. den Anfang von § 5).
Man erhält so, wenn man von einem Punkte A ausgeht und denselben
Schritt a immer wiederholt, das Gerüst einer Geraden: eine mit A anhebende äquidistante gerade Punktfolge. Die Gerade selber entsteht sozusagen durch immer erneute Ausführung derselben unendlich kleinen
Translation. Wie in § 5 kommt man durch Teilung dazu, nicht nur ganzzahlige, sondern auch gebrochene Multiplikatoren λ auf den Vektor a
anzuwenden, und schließlich hebt die Stetigkeitsforderung die Beschränkung auf das Rationale auf. So entsteht ein axiomatischer Aufbau
der Geometrie (genauer: der affinen Geometrie, in der sich nur parallele
Strecken aneinander messen lassen), welcher den voll ausgebildeten Begriff der reellen Zahl voraussetzt — in ihn ist die ganze Analyse der
Stetigkeit hineingeworfen — und dessen Grundbegriffe daneben allein
„Punkt“ und „Vektor“ sind. Drei Grundoperationen verknüpfen diese
Gegenstände: 1. zwei Vektoren a, b erzeugen einen Vektor a + b, 2. eine
Zahl λ und ein Vektor a erzeugen den Vektor λa, 3. ein Punkt A und ein
Vektor a erzeugen einen Punkt Aa. Die auf sie bezüglichen Axiome
bilden nun, im Gegensatz zu den rein geometrischen Axiomen Euklids
oder Hilberts, ein System, das auch in rein logischer Hinsicht von ganz
einheitlichem und durchsichtigem Bau ist; sie fixieren, wie wir bereits in
§ 4 bemerkten, nichts anderes als das Operationsfeld der linearen Algebra.
In ihnen enthüllt sich eine wunderbare Harmonie zwischen dem Gegebenen und der Vernunft. Und auch die einfachsten abgeleiteten geometrischen Begriffe, zu denen hier insbesondere Gerade und Ebene gehören, korrespondieren denjenigen, die vom logischen Standpunkt aus
die nächstliegenden und natürlichsten sind. Alle Vektoren x, welche aus
zwei gegebenen e₁, e₂ nach der Formel

x = x₁e₁ + x₂e₂     (*)

entspringen mit beliebigen Zahlkoeffizienten x₁, x₂, bilden eine „lineare
Schar 2. Stufe“; um der Eindeutigkeit der Darstellung (*) willen ist dabei
vorausgesetzt, daß e₁, e₂ linear unabhängig sind, d. h. der Ausdruck
rechts nur dann den Vektor 0 ergibt, wenn x₁ und x₂ beide = 0 sind.
Trägt man alle diese Vektoren x von einem festen Anfangspunkt O aus
ab, so bilden die Endpunkte Ox = P ein „lineares Gebilde 2. Stufe“
oder eine Ebene. Das Koordinatensystem besteht hier aus dem Punkt O
und den beiden linear unabhängigen Vektoren e₁, e₂. Relativ zu diesem
wird der Punkt P durch die „Koordinaten“ x₁, x₂ charakterisiert. Analog

[[pdf-page:0095 printed-page:94]]

können konstruiert werden lineare Vektorscharen und lineare Punktgebilde der 1., 2., 3., ... Stufe (Gerade, Ebene, ...).

Und erst hier tritt nun der Dimensionsbegriff auf: im wirklichen
Raum können wir über die Stufenzahl 3 nicht hinaus; es existieren
in ihm wohl 3, aber nicht mehr voneinander linear unabhängige
Vektoren. Der ganzen in unserem Axiomensystem zum Ausdruck
kommenden durchsichtigen Gesetzmäßigkeit gegenüber erscheint
diese Dimensionszahl 3 als ein Zufall. Ohne weiteres können wir
die Zahl 3 durch irgendeine Dimensionszahl r ersetzen, indem wir
postulieren: Es existieren n, aber nicht mehr voneinander linear
unabhängige Vektoren. Ein Koordinatensystem für den Raum
besteht dann aus einem Anfangspunkt O und n solchen Vektoren.
Für n = 1, 2, 3 ergeben sich bzw. die Geometrie der Gerade, der
Ebene, des Raumes. Erst auf Grund einer solchen durch Formalisierung zwingend gewonnenen n-dimensionalen Geometrie hat das
Problem der Dimensionszahl, die Frage einen Sinn: Durch welche
inneren Eigentümlichkeiten ist der Fall n = 3 ausgezeichnet?
Wenn Gott bei Erschaffung der Welt dem Raume gerade 3 Dimensionen verlieh, läßt sich dafür durch Aufdeckung solcher Eigentümlichkeiten irgendein „vernünftiger“ Grund angeben?

Trägt man alle Vektoren von einem festen Anfangspunkt O aus ab,
so sieht man, daß die Geometrie der Vektoren identisch ist mit der
(affinen) Geometrie des mit einem absoluten Zentrum O versehenen
Raumes. Identifiziert man alle Vektoren, welche auseinander durch
Multiplikation mit Zahlen hervorgehen, verwendet als Elemente also
die durch O gehenden Strahlen, so entsteht aus der n-dimensionalen
Vektorgeometrie die (n — 1)-dimensionale projektive Geometrie (des
Strahlenbüschels in O).

Die projektive Geometrie gilt im Kontinuum der uns anschaulich
gegebenen Farbqualitäten. (Die Mannigfaltigkeit der verschiedenen objektiven physikalischen Farben hat unendlich viele Dimensionen; das
normale, nicht farbblinde Auge entwirft davon, indem eine ungeheure
Mannigfaltigkeit physikalisch verschiedener Farben denselben Farbeindruck hervorruft, eine 2-dimensionale „Projektion“.) Zwei in bestimmter Intensität gegebene Farben erzeugen durch Zusammenfügen
(Mischen) eine bestimmte neue Farbe in bestimmter Intensität. Die Intensitäten einer Farbe lassen sich miteinander vergleichen, so daß nach vorgenommener Wahl einer Einheitsintensität jede durch eine Maßzahl ge-

[[pdf-page:0096 printed-page:95]]

kennzeichnet werden kann (indem nämlich durch wiederholte Zusammenfügung einer Farbe in der Einheitsintensität mit sich selbst eine Skala
der Intensitäten ohne Qualitätsänderung entsteht). Hingegen sind die
Intensitäten zweier verschiedener Farbqualitäten unvergleichbar. Die
mit Intensitäten behafteten Farben erfüllen also die Axiome der Vektorgeometrie, wobei der Mischung die Addition korrespondiert, für die
Farbqualitäten gilt mithin die projektive Geometrie. Alle durch Mischung aus drei Grundfarben A, B, C entstehenden Farben bilden das
„Dreieck“ ABC. Als zweidimensional erweist sich der Farbraum durch
den Umstand, daß drei Grundfarben durch Mischung alle andern erzeugen, oder daß wenigstens aus solchen Dreiecken sich das ganze Farbfeld zusammensetzen läßt. Die wirklichen Farben erfüllen nämlich nur
einen beschränkten Ausschnitt der ganzen projektiven Ebene. Aber man
kann ihn, wie wir das in § 2 geschildert haben, ideell zur vollen projektiven Ebene erweitern; und man muß für die Grundfarben A, B, C
ideelle Farben wählen, wenn das Feld der wirklichen Farben ganz in das
Dreieck ABC hineinfallen soll. Die reinen Spektralfarben liegen in der
projektiven Farbebene auf einer krummen Kurve, deren äußerste Enden
sich sehr nahe kommen und durch das Purpur überbrückt werden. —
Es ist für die philosophische Diskussion der Geometrie wichtig, daß
neben dem Raum noch ein ganz anderes Gebiet anschaulicher Gegebenheiten besteht: die Farben, welche ein geometrischer Behandlung fähiges
Kontinuum bilden.

LITERATUR

H. v. Helmholtz, Handbuch der physiologischen Optik. 3 Bände.
3. Aufl. Hamburg u. Leipzig 1909—1911, § 20.

F. Klein, Über die sog. nicht-euklidische Geometrie. Ges. math. Abhandlg. I, Berlin 1921, S. 254—305, 311—350.

O. Veblen u. J. W. Young, Projective Geometry. 2 Bände, New York
1910—1918.

H. Weyl, Raum Zeit Materie, 5. Aufl. 1923, §§ 1—4.
```

## Translation

Probably nowhere do mathematics, natural science, and philosophy interpenetrate
so intimately as in the problem of space. The presuppositions worked out by
mathematics for its discussion will still be treated briefly in this part.

### 12. Non-Euclidean, Analytic, Multidimensional, Affine, Projective Geometry. Color Space

There is not much to add about non-Euclidean geometry to what was said in § 4
on the occasion of axiomatics. If all the remaining axioms of Euclidean
geometry are maintained, there are three possibilities: in a plane, to a line
through a point not lying on it, infinitely many, one, or no non-intersecting
line exists ("hyperbolic, parabolic, and elliptic case," according to Klein);
the sum of the angles in a triangle is accordingly less than, equal to, or
greater than 180 degrees. The last possibility, to which Riemann first pointed
in the middle of the nineteenth century, exists only if the axioms of order are
modified so that the straight line appears not as an open but as a closed line.
Plane elliptic geometry is nothing other than the geometry that holds on a
sphere in Euclidean space; only, every two diametrically opposite points of the
sphere must be identified. Or, put differently: while we understand all other
words referring to the geometry of the plane E in their ordinary "Euclidean"
sense, only the meaning of the concept of congruence is to be modified so that
two figures in E count as "congruent" when their projections, from a central
point O lying outside E, onto a sphere described around O are congruent in the
ordinary sense. The "points at infinity" must thereby be incorporated into the
plane, their projection rays being the lines through O parallel to E. The
mappings of E that transfer "congruent" figures into one another can also be
characterized, without reference to space, as collineations with an invariance
property similar to that in Klein's model of Bolyai-Lobachevskian geometry; and
with that the path is open to grounding not only plane but also spatial
elliptic geometry. The true relation of the three kinds of geometry is best
expressed if one takes measure-free projective space as one's starting point
and builds into it a "Cayleyan determination of measure." Depending on the
character of the absolute conic section taken as basis, one or another of the
three metric geometries results. Klein himself understood his construction in
this way: as an incorporation of Lobachevskian geometry into the projective, not
as the production of a model by means of metric-Euclidean space.

Analytic geometry reduces every geometrical problem to an algebraic one. The
precondition for this is that the concept of number, by taking up fractions and
the irrational, has acquired the breadth that makes it suitable for measuring
magnitudes beyond counting. Not the Greeks but the Indians and Arabs completed
this step. Western mathematics followed their paths and achieved independent
accomplishments in geometry only after the science of space had been subjected
to algebraic calculation by Descartes' Géométrie (1637).

Today analytic geometry is probably best treated, after the model of
Grassmann's Theory of Extension, by bringing in the concept of vector. The
vector calculus is a calculation procedure whose objects are not numbers but
geometrical formations. Such a treatment of geometry was demanded by Leibniz
and had even been partly carried out in his text de analisi situs and in the
draft of a geometrical characteristic (Mathematical Writings V, p. 178, and II,
p. 20), which belong within the frame of his "universal characteristic." The
translations or parallel displacements of space are called vectors. Through the
translation a, a point A passes into a point Aa = B, the "endpoint of the vector
a laid off from A." Conversely, if A and B are any two spatial points, there
exists one and only one translation a that transfers A into B. Among the
translations we count especially the "identity," which leaves all points fixed,
the vector 0. Translations can be composed; they form a group. By executing two
translations a, b one after the other, an effect is produced that can also be
achieved by a single translation, the resultant translation a + b.

1) Descartes speaks of the "misgiving of the ancients about the use of signs
of arithmetic in geometry, which could only have arisen from the fact that the
connection between these two disciplines had not become sufficiently clear to
them."

The concept of number penetrates into geometry because a translation a is
iterated, added to itself arbitrarily often (cf. the beginning of § 5). In this
way, if one starts from a point A and repeats the same step a again and again,
one obtains the framework of a straight line: an equidistant straight sequence
of points beginning with A. The straight line itself arises, so to speak,
through ever renewed execution of the same infinitesimal translation. As in § 5,
division leads one to apply not only whole-number but also fractional
multipliers λ to the vector a, and finally the demand for continuity removes the
restriction to the rational. Thus there arises an axiomatic construction of
geometry, more precisely of affine geometry, in which only parallel segments can
be measured against one another. It presupposes the fully developed concept of
the real number, into which the whole analysis of continuity has been thrown,
and its basic concepts besides are only "point" and "vector." Three basic
operations connect these objects: 1. two vectors a, b generate a vector a + b;
2. a number λ and a vector a generate the vector λa; 3. a point A and a vector
a generate a point Aa. The axioms referring to them form, in contrast to the
purely geometrical axioms of Euclid or Hilbert, a system that is also, from a
purely logical point of view, of entirely unified and transparent construction.
As we already noted in § 4, they fix nothing other than the field of operations
of linear algebra. In them a wonderful harmony between the given and reason is
revealed. And even the simplest derived geometrical concepts, especially the
straight line and plane, correspond to those that from the logical standpoint
are the nearest and most natural. All vectors x that arise from two given
vectors e₁, e₂ according to the formula

```text
x = x₁e₁ + x₂e₂     (*)
```

with arbitrary numerical coefficients x₁, x₂ form a "linear family of the
second level." For the sake of the uniqueness of the representation (*), it is
thereby presupposed that e₁, e₂ are linearly independent; that is, the
expression on the right yields the vector 0 only if x₁ and x₂ are both equal to
0. If one lays off all these vectors x from a fixed initial point O, then the
endpoints Ox = P form a "linear formation of the second level," or a plane. The
coordinate system here consists of the point O and the two linearly independent
vectors e₁, e₂. Relative to it, the point P is characterized by the
"coordinates" x₁, x₂. Analogously, linear vector families and linear point
formations of the 1st, 2nd, 3rd, ... level can be constructed: line, plane, and
so on.

Only here does the concept of dimension enter: in actual space we cannot go
beyond the level-number 3; in it there do exist 3, but no more, linearly
independent vectors. In contrast to the transparent lawfulness expressed in our
axiom system as a whole, this dimension-number 3 appears as an accident. Without
further ado we can replace the number 3 by any dimension-number n, by
postulating: there exist n, but no more, mutually linearly independent vectors.
A coordinate system for space then consists of an initial point O and n such
vectors. For n = 1, 2, 3 one obtains respectively the geometry of the line, the
plane, and space. Only on the basis of such an n-dimensional geometry, won
compellingly through formalization, does the problem of the dimension-number,
the question, have a meaning: by what inner peculiarities is the case n = 3
distinguished? If God, in creating the world, gave space precisely 3
dimensions, can any "rational" ground for this be given by uncovering such
peculiarities?

If one lays off all vectors from a fixed initial point O, one sees that the
geometry of vectors is identical with the affine geometry of space provided
with an absolute center O. If one identifies all vectors that arise from one
another by multiplication with numbers, and therefore uses as elements the rays
passing through O, then from n-dimensional vector geometry there arises
(n - 1)-dimensional projective geometry, the projective geometry of the pencil of
rays in O.

Projective geometry holds in the continuum of color qualities given to us in
intuition. The manifold of different objective physical colors has infinitely
many dimensions; the normal, non-color-blind eye projects this into two
dimensions, in that an immense manifold of physically different colors calls
forth the same color-impression. Two colors given with determinate intensity
produce, by combination or mixing, a determinate new color with determinate
intensity. The intensities of one color can be compared with one another, so
that after the choice of a unit intensity each can be characterized by a
measure-number, since a scale of intensities without change of quality arises
by repeated combination of a color in the unit intensity with itself. By
contrast, the intensities of two different color qualities are incomparable.
Colors furnished with intensities therefore fulfill the axioms of vector
geometry, with addition corresponding to mixing; for color qualities,
accordingly, projective geometry holds. All colors arising by mixture from three
primary colors A, B, C form the "triangle" ABC. The color space proves itself
two-dimensional by the fact that three primary colors generate all others by
mixing, or at least that the whole color-field can be assembled out of such
triangles. Actual colors fill only a restricted sector of the whole projective
plane. But one can, as we described in § 2, extend it ideally to the full
projective plane; and one must choose ideal colors for the primary colors A, B,
C if the field of actual colors is to fall wholly within the triangle ABC. The
pure spectral colors lie in the projective color-plane on a curved line whose
outermost ends come very close to one another and are bridged by purple. For the
philosophical discussion of geometry it is important that, beside space, there
exists a wholly different region of intuitive givens: colors, which form a
continuum capable of geometrical treatment.

Literature

H. v. Helmholtz, Handbuch der physiologischen Optik. 3 vols. 3rd ed. Hamburg
and Leipzig, 1909-1911, § 20.

F. Klein, Über die sog. nicht-euklidische Geometrie. Ges. math. Abhandlg. I,
Berlin 1921, pp. 254-305, 311-350.

O. Veblen and J. W. Young, Projective Geometry. 2 vols. New York, 1910-1918.

H. Weyl, Raum Zeit Materie, 5th ed. 1923, §§ 1-4.

## Notes

Section 12 does not present geometry as a settled doctrine of physical space.
It first shows non-Euclidean geometry becoming intelligible through projective
relations and Cayley's metric construction, then shows analytic geometry
requiring the completed real-number apparatus from chapter II.

The vector treatment is the section's main bridge from number to geometry:
translations form a group, iteration brings number into geometry, and affine
geometry becomes the operational field of linear algebra. This makes geometry
look formally transparent, but the actual dimension-number `3` then appears as
a contingent fact requiring a further question.

The color-space example matters because it blocks a too-spatial reading of
geometry. Projective geometry applies to a continuum of intuitively given color
qualities. Geometry is therefore not simply the science of actual physical
space; it is a formal treatment that can organize other intuitive continua.

This section sharpens the chapter-II dossier. Symbolic/formal construction is
not merely a way to speak about the infinite; it also creates meaningful
questions, such as the problem of why actual space has three dimensions. The
bridge to physics is now more concrete: formal geometry opens a possibility
space, and natural science must decide which formally possible structure
belongs to the world.

## Translation Decisions

- `Raum` is `space`
- `nicht-euklidische Geometrie` is `non-Euclidean geometry`
- `Kongruenzbegriff` is `concept of congruence`
- `unendlich ferne Punkte` is `points at infinity`
- `maßfreier projektiver Raum` is `measure-free projective space`
- `Cayleysche Maßbestimmung` is `Cayleyan determination of measure`
- `analytische Geometrie` is `analytic geometry`
- `Raumwissenschaft` is `science of space`
- `Vektorkalkül` is `vector calculus`
- `Operationsfeld der linearen Algebra` is `field of operations of linear
  algebra`
- `lineare Schar / lineares Gebilde ... Stufe` is `linear family / linear
  formation ... level`, kept provisional
- `Dimensionsbegriff` is `concept of dimension`
- `Dimensionszahl` is `dimension-number`
- `Zufall` is `accident`
- `Strahlenbüschel` is `pencil of rays`
- `Farbraum` is `color space`
- `Farbqualitäten` is `color qualities`
- `anschauliche Gegebenheiten` is `intuitive givens`

## Adversarial Check

The risky simplification is to read this section as a technical detour before
the real philosophical work of relativity. That misses Weyl's progression. The
formalization of geometry is already doing philosophical work: it separates
space from any single naive intuition of space, makes dimension into a problem,
and demonstrates a non-spatial continuum that still admits geometrical
treatment.

The opposite risk is to overstate the formalist result and treat geometry as
free construction detached from experience. Weyl does not do that either. The
whole section prepares the next problem: once formal geometry opens many
possibilities, the question becomes how objectivity and experience select among
them.
