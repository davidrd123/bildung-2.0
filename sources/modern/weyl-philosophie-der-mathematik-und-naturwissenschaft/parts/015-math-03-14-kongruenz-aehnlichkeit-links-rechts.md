# Part 015: Congruence And Similarity. Left And Right

Section 14 develops congruence from the physical handling of rigid bodies, then
shows how the relation between congruence and similarity can be formulated by
normalizers and invariant subgroups. The final left/right discussion turns
Kant's puzzle into a combinatorial fact about even and odd permutations.

## Scope

- `14. Kongruenz und Ähnlichkeit. Links und rechts`
- printed pages `104-113`
- PDF/page-image pages `105-114`

Section 14 begins on the same page where section 13 ends, printed page `104` /
PDF page `105`, and ends on printed page `113` / PDF page `114`, immediately
before section 15.

## Source Anchors

- `source/cleaned/010-math-03-geometrie.txt`
- `source/page-images/jpg-200/page-0105.jpg`
- `source/page-images/jpg-200/page-0106.jpg`
- `source/page-images/jpg-200/page-0107.jpg`
- `source/page-images/jpg-200/page-0108.jpg`
- `source/page-images/jpg-200/page-0109.jpg`
- `source/page-images/jpg-200/page-0110.jpg`
- `source/page-images/jpg-200/page-0111.jpg`
- `source/page-images/jpg-200/page-0112.jpg`
- `source/page-images/jpg-200/page-0113.jpg`
- `source/page-images/jpg-200/page-0114.jpg`

## Source Status

The active page range was visually checked against page images. The cleaned
German source was corrected for this batch, especially:

- prime notation in `V′`, `v₁/v₂`, `x₁′/x₂′/x₃′`, and related expressions
- `Δ⁺`, `C⁻¹`, `S₁⁻¹S₂`, and the normalizer diagram
- vector and coordinate notation: `e₁`, `e₂`, `e₃`, `x₁e₁ + x₂e₂ + x₃e₃`,
  `xᵢ′ = aᵢ + aᵢ₁x₁ + ... + aᵢₙxₙ`
- physical-component notation: `fᵢ`, `Fᵢₖ = −Fₖᵢ`, `fᵢ′`, and `Fᵢₖ′`
- `F₁/F₂`, `n (≥ 2)`, the left/right footnote marker, and `sieht`
- moved the `Vgl. S. 108` footnote so it belongs to the left/right paragraph
  rather than to the beginning of section 15

## German

```text
14. Kongruenz und Ähnlichkeit. Links und rechts

Ohne Zweifel rührt die Überzeugungskraft, die die euklidische
Geometrie für uns besitzt, von unserer Vertrautheit im Umgang
mit solchen Körpern her, die wir starr nennen, und von denen
man sagen kann, sie blieben unter sich ändernden Bedingungen
gleich. Die Raumstücke, die ein solcher Körper in zwei möglichen

[[pdf-page:0106 printed-page:105]]

Lagen ausfüllt, heißen kongruent. Das Messen ist von starren Körpern im gleichen Grade abhängig wie das Zählen vom Gebrauch
konkreter Zahlensymbole. (Über die physikalische Begründung
der Geometrie s. auch §§ 16 und 18.) Ist eine Geometrie einmal
vom Verhalten wirklicher, angenähert starrer Körper abstrahiert
worden, so liefert sie eine Norm für die physikalische Untersuchung aller Körper, und wir können beurteilen, wie weit ein gegebener Körper das Ideal der Starrheit verwirklicht. Dieser Vorgang unterscheidet sich nicht wesentlich von dem, bei welchem
sich eine Temperaturskala zunächst auf das Verhalten wirklicher
Gase stützt und dann auf die „ideale Gasskala“ reduziert wird,
wobei die exakte Gültigkeit solcher Gesetze postuliert wird, die
von den existierenden Gasen nur näherungsweise befolgt werden.
Da die Orte bei einem starren Körper angemerkt werden können,
ist die Kongruenz eine punktweise Abbildung zweier kongruenter
Volumina V und V′. Zunächst bezieht sich der Kongruenzbegriff
auf einen gegebenen starren Körper b. Seine faktische Unabhängigkeit von b ist eine unserer fundamentalsten Erfahrungen.
Es seien nämlich V und V′ zwei Raumstücke, die vom Körper b
in zwei seiner Lagen ausgefüllt werden. b* sei ein anderer Körper,
der in V hineinpaßt; er kann dann so bewegt werden, daß er V′
ausfüllt. Da man einen starren Körper so groß machen kann,
daß er einen beliebig gegebenen Punkt überdeckt, kann die Abbildung V → V′ auf den ganzen Raum erweitert werden. Die kongruenten Abbildungen des Raumes bilden eine Gruppe Δ⁺ von
Transformationen, die wir die Gruppe der euklidischen Bewegungen
nennen. Ist diese Gruppe einmal bekannt, so können kongruente
Volumina als Raumstücke definiert werden, die ineinander durch
eine Transformation S von Δ⁺ überführt werden können. Die Tatsachen legen eine Deutung nahe, nach welcher die Gruppe Δ⁺
der kongruenten Abbildungen eine innere Struktur des Raumes
selbst zum Ausdruck bringt, und zwar eine Struktur, die vom
Raum allen Raumobjekten aufgeprägt wird.

Falls diese Ansicht zutrifft, sollte die Kongruenz eigentlich
zum einzigen Grundbegriff der Geometrie gemacht werden. Untersuchen wir zuerst einmal, welche Konsequenzen diese Auffassung
von der Geometrie für die Automorphismen des Raumes (Ähn-

[[pdf-page:0107 printed-page:106]]

lichkeiten) hat. Wir wissen ganz allgemein, daß die Gruppe Γ der
Automorphismen dann festliegt, wenn die Begriffe für die Grundrelationen einer Geometrie festliegen. In unserem Falle lautet das
Kriterium für einen Automorphismus so: sowohl C als auch C⁻¹
müssen jedes Paar kongruenter Raumstücke v₁, v₂ in ein kongruentes Paar transformieren. Wir betrachten das Paar v₁*, v₂*, das
durch die Transformation C aus v₁, v₂ entsteht. S sei die Bewegung, die v₁ in v₂ überführt. Wie das Diagramm

      (S)
v₁ ------> v₂
(C⁻¹) ↑   ↓ (C)
v₁*       v₂*

anzeigt, geht v₁* durch die Abbildung C⁻¹SC in v₂* über. Folglich
erfordert das Kriterium, daß immer dann, wenn S zu Δ⁺ gehört,
auch die Transformationen C⁻¹SC und CSC⁻¹ dazu gehören.
Eine Transformation heißt mit einer gegebenen Transformationsgruppe Δ vertauschbar, wenn mit S auch C⁻¹SC und CSC⁻¹ zu Δ
gehören. Die mit Δ vertauschbaren Transformationen bilden eine
Gruppe, den Normalisator von Δ. Diese Gruppe enthält notwendig
Δ als Untergruppe, sei es, daß Δ identisch mit seinem Normalisator
oder ein echter Teil davon ist. Unsere Analyse kann nun so zusammengefaßt werden: Die Gruppe Γ der Ähnlichkeiten ist der
Normalisator der Gruppe Δ⁺ der Bewegungen. Kongruente Figuren
sind also notwendig ähnlich. Die Umkehrung muß nicht gelten.
Ist nämlich Δ⁺ tatsächlich eine echte Untergruppe des Normalisators, so existieren ähnliche Figuren im euklidischen Raum, die
nicht kongruent sind. Beispiele dafür sind ein Körper und sein
Spiegelbild, oder ein Gebäude und ein kleinmaßstäbiges Modell
davon.

Nun wollen wir das Verfahren umkehren und Klein folgen,
indem wir von einer gegebenen Automorphismengruppe ausgehen.
Wir nehmen eine Untergruppe Δ von Γ und erklären zwei Figuren
für Δ-äquivalent, wenn durch eine Transformation von Δ die eine
in die andere überführt wird. Unter welchen Umständen besitzt
nun diese Relation der Δ-Äquivalenz objektive Bedeutung? Dann
und nur dann, wenn Δ-äquivalente Figuren durch jede Transfor-

[[pdf-page:0108 printed-page:107]]

mation C von Γ in Δ-äquivalente Figuren überführt werden, oder
mit andern Worten, wenn jedes Element C von Γ mit Δ vertauschbar ist. In diesem Falle sagt der Mathematiker, Δ sei eine invariante
Untergruppe von Γ. Infolgedessen ist die Δ-Äquivalenz dann eine
objektive Relation, wenn Δ eine invariante Untergruppe von Γ ist.
Zum Beispiel bilden die Parallelverschiebungen eine invariante
Untergruppe der Gruppe der euklidischen Ähnlichkeiten; denn
tatsächlich besitzt die Relation // zwischen zwei Figuren, die durch
Parallelverschiebung auseinander hervorgehen, objektive geometrische Bedeutung — obgleich ein passendes Wort dafür in
unserer Sprache fehlt. Der Normalisator der Gruppe der Parallelverschiebungen besteht aus allen affinen Transformationen; es
muß also möglich sein, die affine Geometrie auf der einen Relation // zwischen Figuren aufzubauen. Oder noch einfacher, die
allein aus der Identität bestehende Untergruppe ist eine invariante
Untergruppe, und tatsächlich ist die Relation der Identität zwischen zwei Figuren von objektiver Bedeutung. (Es gibt gar keine
mit einem besseren Anspruch auf Objektivität, weil ja die Identität
in jeder möglichen Transformationsgruppe Γ enthalten ist.) Je
kleiner die Gruppe Δ ist, desto größer ist ihr Normalisator, und
um so größer ist die Kluft zwischen Kongruenz und Ähnlichkeit;
oder genauer, ist Δ′ eine Untergruppe von Δ, dann enthält der
Normalisator Γ″ von Δ′ den Normalisator Γ′ von Δ. Der Normalisator einer invarianten Untergruppe Δ von Γ′ umfaßt stets Γ′.
Eine Geometrie, deren Automorphismengruppe Γ′ ist, kann allein
auf die objektive Relation der Δ-Äquivalenz aufgebaut werden,
vorausgesetzt, der Normalisator von Δ ist nicht größer als Γ′,
sondern fällt mit Γ′ zusammen.

Eine letzte Bemerkung möge diese Analyse beschließen. Der Raum
ist ein Kontinuum, und wenn wir von einer Transformation im Raum
sprechen, so ist es vernünftig dies im Sinne jeder beliebigen kontinuierlichen Transformation zu deuten. Wir bezeichnen mit Ω die Gruppe der
Transformationen, die überhaupt in Betracht kommen; im Falle eines
Kontinuums wäre dies die Gruppe aller kontinuierlichen Transformationen. Legt man dies ausdrücklich zugrunde, so kann unsere Definition
des Normalisators folgendermaßen wiederholt werden: Gegeben sei eine
Untergruppe Δ der Gruppe Ω; diejenigen Elemente von Ω, die mit Δ

[[pdf-page:0109 printed-page:108]]

vertauschbar sind, bilden den Normalisator Γ′ von Δ. In dieser Form
gewinnt der Begriff des Normalisators einen Sinn selbst für abstrakte
Gruppen Ω und Δ.

Kant spricht in Prolegomena §13 über den Unterschied zwischen
kongruent und ähnlich und behauptet: „Wir können daher auch den
Unterschied ähnlicher und gleicher, aber doch inkongruenter Dinge
(z. B. widersinnig gewundener Schnecken) durch keinen einzigen Begriff
verständlich machen, sondern nur durch das Verhältnis zur rechten und
linken Hand, welches unmittelbar auf Anschauung geht.“ Nach seiner
Ansicht bietet nur der transzendentale Idealismus eine Lösung für dieses
Rätsel an. Ohne Zweifel gründet sich die Bedeutung der Kongruenz auf
die Raumanschauung, aber ebenso ist es mit der Ähnlichkeit. Kant
scheint auf einen wunden Punkt zu zielen, aber gerade dieser Punkt
kann durch eine Analyse an Hand einer Gruppe Γ′ und ihrer invarianten
Untergruppen Δ, oder einer Gruppe Δ und ihres Normalisators Γ′ vollständig geklärt werden. Stets wenn Δ eine echte invariante Untergruppe
von Γ′ ist, fallen die Begriffe der Kongruenz = Δ-Äquivalenz und der
Ähnlichkeit = Γ′-Äquivalenz nicht zusammen, obgleich die erstere von
objektiver Bedeutung (= Γ′-invariant) ist. Das Phänomen, über das sich
Kant wundert, kann somit höchst befriedigend unter allgemeine und
abstrakte „Begriffe“ gestellt werden.

Wer die Kongruenz in den Rang der einzigen Grundrelation
der Geometrie erhebt, muß sodann die Geometrie aus diesem einen
Begriff heraus entwickeln. Hierfür stehen mehrere Wege offen.
Eine tiefere Einsicht, als die elementare Auffassung zuläßt, in den
Stil der euklidischen Axiome würde gewonnen, wenn es gelänge,
die fundamentalen Tatsachen der Geometrie als einfache Axiome
über die Gruppe Δ⁺ der euklidischen Bewegungen zu formulieren.
Nach Überweg hat als erster Helmholtz mit überraschendem
Erfolg dieses Programm in seiner Schrift „Über die Tatsachen,
die der Geometrie zugrunde liegen“ durchgeführt. Später hat S. Lie,
der eine allgemeine Theorie der Transformationsgruppen aufstellte,
das Problem mit seinen schärferen mathematischen Mitteln wieder
aufgegriffen und es von drei auf n Dimensionen verallgemeinert.
Die euklidische Bewegungsgruppe Δ⁺ ist beinahe vollständig dadurch gekennzeichnet, daß sie dem starren Körper dasjenige Maß
an freier Beweglichkeit verleiht, das uns aus der Erfahrung vertraut ist. In genauerer Fassung: Man ist durch eine kongruente

[[pdf-page:0110 printed-page:109]]

Abbildung imstande, einen beliebigen Punkt in einen beliebigen
Punkt überzuführen, außerdem bei festgehaltenem Punkt eine beliebige Linienrichtung in diesem Punkte in eine beliebige Linienrichtung daselbst, bei festgehaltenem Punkt und Linienrichtung
eine beliebige durch sie hindurchgehende Flächenrichtung in eine
beliebige andere ebensolche Flächenrichtung, und so fort bishinauf
zu den (n — 1)-dimensionalen Richtungselementen. Ist aber andererseits ein Punkt, eine hindurchgehende Linienrichtung, eine
durch sie hindurchgehende Flächenrichtung usw. bis hinauf zu
einem (n — 1)-dimensionalen Richtungselement gegeben, so existiert außer der Identität keine kongruente Abbildung, welche
dieses System inzidenter Elemente festläßt. Wir sagten soeben,
dieses Axiom kennzeichne beinahe vollständig die euklidische Bewegungsgruppe. Tatsächlich erhält man so die Gruppe der kongruenten Transformationen eines geringfügig allgemeineren Raumes, nämlich eines projektiven Raumes mit aufgeprägter Cayleyscher Maßbestimmung. Diese Gruppe enthält einen dem Werte
nach unbestimmt bleibenden Zahlparameter λ, die konstante
Raumkrümmung, von welcher nur das Vorzeichen wesentlich ist.
Je nachdem λ positiv, 0 oder negativ ist, kommt man auf den
elliptischen, parabolischen (euklidischen) oder hyperbolischen
Typus. Dies sind also die einzigen homogenen Räume, in denen
alle Punkte gleichwertig sind, ferner alle Richtungen in einem
Punkte usw.

Es ist schwer, über diese Probleme ohne exakte Beschreibung der
euklidischen Gruppen Γ′ und Δ⁺ vor Augen gescheit zu reden. Ein
kartesisches Bezugssystem im dreidimensionalen euklidischen Raum
besteht aus einem Punkt O, dem Ursprung, und drei aufeinander senkrecht stehenden Vektoren e₁, e₂, e₃ gleicher Länge. Die Koordinaten x₁,

x₂, x₃ eines Punktes werden durch

→OP = x₁e₁ + x₂e₂ + x₃e₃

definiert. Relativ zu einem solchen System wird eine Ähnlichkeit, die den
Punkt (x₁, x₂, x₃) in den Punkt (x₁′, x₂′, x₃′) abbildet, durch eine lineare
Transformation

S: xᵢ′ = aᵢ + aᵢ₁x₁ + ... + aᵢₙxₙ (i = 1, 2, ..., n) (*)

mit konstanten Koeffizienten aᵢ, aᵢₖ dargestellt, die der folgenden Be-

[[pdf-page:0111 printed-page:110]]

dingung genügen: (x₁′ − a₁)² + ... + (xₙ′ − aₙ)² ist ein konstantes
positives Vielfaches a von x₁² + ... + xₙ². (Die Dimensionszahl n ist
hier unbestimmt gelassen.) Die Ähnlichkeit ist „nicht-vergrößernd“
und heißt orthogonale Transformation für a = 1. Die orthogonalen
Transformationen bilden eine invariante Untergruppe Δ von Γ′. Aus der
oben erwähnten Bedingung, die durch jede Ähnlichkeit erfüllt wird,
folgt die Gleichung d² = aⁿ für die Determinante d aus den aᵢₖ. Folglich
hat eine orthogonale Transformation entweder das Vorzeichen +
(d = +1) oder das Vorzeichen — (d = −1). Die orthogonalen Transformationen mit dem Vorzeichen + bilden die Gruppe Δ⁺ der euklidischen Bewegungen. Δ⁺ ist eine Untergruppe von Δ mit dem Index 2,
d. h., wenn S₁, S₂ zwei beliebige Transformationen von Δ mit negativem
Vorzeichen sind, dann hat S₁⁻¹S₂ positives Vorzeichen. (Die fundamentale Tatsache der Unterscheidung von links und rechts: zwei gegenüber
einer gegebenen Schraube gegensinnig gewundene Schrauben winden
sich im gleichen Sinne.) Es macht nicht viel aus, ob wir Δ⁺ oder Δ als
Gruppe der kongruenten Abbildungen zugrundelegen. Angenommen
wir entscheiden uns für die größere Gruppe Δ. Dann würde die stetige
Bewegung eines starren Körpers durch eine Orthogonaltransformation
S(t) dargestellt, die vom Zeitparameter t abhängt und die Identität I
im Anfangsmoment t = 0 aufweist. Da die Determinante von S(t)
lediglich die beiden Werte + 1 und — 1 annehmen kann, da sie ferner
am Anfang t = 0 gleich + 1 ist und stetig mit t variiert, muß sie stets
+1 bleiben. So fallen selbst dann, wenn wir beliebige orthogonale
Transformationen zulassen, durch die Forderung der Stetigkeit für
S(t) die Transformationen mit negativem Vorzeichen automatisch
heraus. Ein starrer Körper könnte nur durch einen unstetigen Sprung
in sein Spiegelbild übergehen.

Ein viel tiefer greifender Aspekt für die Gruppe Δ als der, die
Beweglichkeit starrer Körper zu beschreiben, wird durch ihre Rolle
als Gruppe der Automorphismen der physikalischen Welt offenbar.
In der Physik können wir nicht nur die Punkte betrachten, sondern
ebenso die verschiedenen Arten physikalischer Größen wie Geschwindigkeit, Kraft, elektromagnetische Feldstärke usw. Aber
Tatsache ist, daß in einem kartesischen System nicht nur Punkte,
sondern alle physikalischen Größen durch Zahlen dargestellt werden können, zum Beispiel eine Kraft durch ihre Komponenten
fᵢ (i = 1, 2, ..., n), eine elektromagnetische Feldstärke durch eine
Menge schiefsymmetrischer Komponenten Fᵢₖ = −Fₖᵢ usw. Und

[[pdf-page:0112 printed-page:111]]

unter dem Einfluß einer beliebigen orthogonalen Abbildung S (*)
der Raumpunkte durchlaufen sie eine verwandte Transformation,
die eindeutig durch S bestimmt ist. So transformieren sich zum
Beispiel die Kraftkomponenten nach der Gleichung

fᵢ′ = Σλ aᵢλ fλ (i, λ = 1, 2, ..., n),

die Komponenten der elektromagnetischen Feldstärke nach der
Regel

Fᵢₖ′ = Σλ,μ aᵢλ aₖμ Fλμ (i, k, λ, μ = 1, 2, ..., n)

usw. Alle Naturgesetze sind gegenüber der so durch die Gruppe Δ
induzierten Transformation invariant. Indessen gilt nicht, daß sie
gegenüber allen Ähnlichkeiten invariant sind, obgleich es auf
einem gewissen Stand der Naturerscheinungen so aussieht. Aber
die Tatsachen des Atomismus lehren uns, daß die Länge nicht relativ, sondern absolut ist. Die Atomkonstanten der Ladung und
Masse des Elektrons und das Plancksche Wirkungsquantum h
legen ein absolutes Längennormal fest, das sich durch die Wellenlängen der Spektrallinien auch für praktische Messungen als zugänglich erweist. So sind wir nicht mehr von der Erhaltung des
Platin-Iridium-Urmeterstabes abhängig, der beim Comité International des Poids et Mesures in Paris aufbewahrt wird. Für die
Basisvektoren eines kartesischen Bezugssystems schreiben wir nun
die absolute Länge 1 vor. In Δ müssen auch die Transformationen
mit negativem Vorzeichen enthalten sein; denn in den Naturgesetzen gibt es keinen Hinweis für einen natürlichen Unterschied
zwischen links und rechts. Nun ist klar, warum ein Körper, dessen
Stellen alle eine Transformation S(t) der Gruppe Δ durchlaufen,
die stetig vom Zeitparameter t abhängt, und deren physikalische
Merkmale sich entsprechend ändern, mit vollem Recht von sich
behaupten kann: Physikalisch bin ich während meiner Bewegung
gleich geblieben.

Das extensive Medium der Außenwelt besteht sowohl aus der Zeit
als auch aus dem Raum. Wie die Zeit als vierte Koordinate in das obige
Schema paßt, wird in §16 auseinandergesetzt. Dieser Schritt wurde

[[pdf-page:0113 printed-page:112]]

dadurch vorbereitet, daß wir die Dimensionszahl n unbestimmt gelassen
haben. Für die Physik ist der Fall n = 4 sogar wichtiger als n = 3. Hier
werden wir uns freilich auf den Raum beschränken.

Wir fassen zusammen: Die Gruppe der physikalischen Automorphismen im Raum ist die Gruppe Δ der orthogonalen Transformationen. Die Gruppe der geometrischen Automorphismen ist
gemäß der eigentlichen Wortbedeutung der Normalisator Γ′ von Δ.
Er ist größer als Δ, insofern er die Dilatationen xᵢ′ = axᵢ mit beliebiger Konstanter a > 0 mit enthält. Diese Divergenz zwischen
Δ und Γ′ beweist letztlich, daß die Physik sich nie auf die Geometrie zurückführen läßt, wie Descartes gehofft hatte.

Links und rechts. Müßte ich die fundamentalsten mathematischen Tatsachen benennen, so würde ich wahrscheinlich mit der Tatsache (F₁)
beginnen, daß das Abzählen einer Menge von Elementen zur gleichen
Zahl führt, in welcher Reihenfolge man auch die Elemente vornimmt,
dann als zweites die Tatsache (F₂) erwähnen, daß man unter den Permutationen von n (≥ 2) Dingen die geraden und die ungeraden voneinander unterscheiden kann. Die geraden Permutationen bilden eine
Untergruppe mit Index 2 innerhalb der Gruppe aller Permutationen. Die erste Tatsache bildet den Grund des geometrischen Dimensionsbegriffes, die zweite den des „Sinnes“. Wir betrachten die affine
Vektorgeometrie. Eine Basis für ihre Vektoren besteht aus n Vektoren e₁, ..., eₙ, so daß jeder beliebige Vektor sich als Linearkombination x₁e₁ + ... + xₙeₙ eindeutig ausdrücken läßt, und der Satz von der
Invarianz der Dimensionszahl besagt, daß jede Basis notwendig aus
der gleichen Anzahl n Vektoren besteht. Aus dieser Aussage folgt klar
die Tatsache (F₁); denn durch jede Umgruppierung der Basisvektoren
geht man zu einer neuen Basis über. Umgekehrt bildet das Invarianztheorem einen leicht aus der Tatsache (F₁) zusammen mit der Regel
für die Addition und Multiplikation von Zahlen abgeleiteten algebraischen Satz. Jede Anordnung von n gegebenen, linear unabhängigen
Vektoren legt einen „Sinn“ fest, und zwei Anordnungen legen dann den
gleichen Sinn fest, wenn sie durch eine gerade Permutation auseinander
hervorgehen (Definition durch Abstraktion). Eine ungerade Permutation ändert den Sinn ins Gegenteil. Das ist ganz klar die kombinatorische
Wurzel der Unterscheidung zwischen links und rechts. Außerdem wird
man in Verbindung mit den Grundoperationen der affinen Vektorgeometrie (Vektoraddition, Multiplikation eines Vektors mit einer Zahl)
zu einem Vergleich des „Sinnes“ zweier Basen e₁, ..., eₙ und e₁*, ..., eₙ*

[[pdf-page:0114 printed-page:113]]

geführt. Wenn man die Vektoren e* durch die Vektoren e ausdrückt,
also

eᵢ* = a₁ᵢe₁ + ... + aₙᵢeₙ,

dann besitzen die Koeffizienten aᵢₖ eine nicht-verschwindende Determinante. Die Sinne der beiden Basen sind entweder gleich oder entgegengesetzt, je nachdem die Determinante positiv oder negativ ist.
Die Definition einer Determinante gründet sich aber auf die Unterscheidung gerader und ungerader Permutationen!

Kant findet den Schlüssel zum Rätsel des links und rechts¹) im transzendentalen Idealismus. Der Mathematiker sieht dahinter die kombinatorische Tatsache der Unterscheidung von geraden und ungeraden Permutationen. Die Diskrepanz zwischen der Fragestellung des Philosophen
und des Mathematikers nach den Wurzeln des Phänomens, das uns die
Natur stellt, kann kaum auffallender beleuchtet werden.

1) Vgl. S. 108.
```

## Translation

### 14. Congruence And Similarity. Left And Right

No doubt the persuasive force that Euclidean geometry possesses for us stems
from our familiarity in dealing with such bodies as we call rigid, and of which
one can say that they remain the same under changing conditions. The pieces of
space that such a body fills in two possible positions are called congruent.
Measurement depends on rigid bodies to the same degree as counting depends on
the use of concrete number-symbols. On the physical grounding of geometry, see
also §§ 16 and 18. Once a geometry has been abstracted from the behavior of
actual, approximately rigid bodies, it supplies a norm for the physical
investigation of all bodies, and we can judge how far a given body realizes the
ideal of rigidity. This procedure is not essentially different from the one by
which a temperature scale is first based on the behavior of actual gases and
then reduced to the "ideal gas scale," while the exact validity of such laws is
postulated as existing gases obey only approximately.

Since the places on a rigid body can be marked, congruence is a pointwise
mapping of two congruent volumes V and V′. Initially, the concept of congruence
refers to a given rigid body b. Its factual independence from b is one of our
most fundamental experiences. Let V and V′ be two pieces of space filled by the
body b in two of its positions. Let b* be another body that fits into V; it can
then be moved so that it fills V′. Since one can make a rigid body so large that
it covers any arbitrarily given point, the mapping V → V′ can be extended to
the whole of space. The congruent mappings of space form a group Δ⁺ of
transformations, which we call the group of Euclidean motions. Once this group
is known, congruent volumes can be defined as pieces of space that can be
transferred into one another by a transformation S of Δ⁺. The facts suggest an
interpretation according to which the group Δ⁺ of congruent mappings expresses
an inner structure of space itself, namely a structure impressed by space upon
all spatial objects.

If this view is correct, congruence should really be made the sole basic concept
of geometry. Let us first examine what consequences this conception of geometry
has for the automorphisms of space, that is, for similarities. We know quite
generally that the group Γ of automorphisms is fixed when the concepts for the
basic relations of a geometry are fixed. In our case the criterion for an
automorphism runs as follows: both C and C⁻¹ must transform every pair of
congruent pieces of space v₁, v₂ into a congruent pair. We consider the pair
v₁*, v₂* that arises from v₁, v₂ by the transformation C. Let S be the motion
that transfers v₁ into v₂. As the diagram indicates,

```text
      (S)
v₁ ------> v₂
(C⁻¹) ↑   ↓ (C)
v₁*       v₂*
```

v₁* passes by the mapping C⁻¹SC into v₂*. Consequently the criterion requires
that whenever S belongs to Δ⁺, the transformations C⁻¹SC and CSC⁻¹ also belong
to it. A transformation is called interchangeable with a given transformation
group Δ when, with S, C⁻¹SC and CSC⁻¹ also belong to Δ. The transformations
interchangeable with Δ form a group, the normalizer of Δ. This group necessarily
contains Δ as a subgroup, whether Δ is identical with its normalizer or is a
proper part of it. Our analysis can now be summarized as follows: the group Γ of
similarities is the normalizer of the group Δ⁺ of motions. Congruent figures
are therefore necessarily similar. The converse need not hold. If Δ⁺ is in fact
a proper subgroup of the normalizer, then similar figures exist in Euclidean
space that are not congruent. Examples are a body and its mirror image, or a
building and a small-scale model of it.

Now we want to reverse the procedure and follow Klein by starting from a given
automorphism group. We take a subgroup Δ of Γ and declare two figures
Δ-equivalent when one is transferred into the other by a transformation of Δ.
Under what circumstances does this relation of Δ-equivalence possess objective
significance? If and only if Δ-equivalent figures are carried by every
transformation C of Γ into Δ-equivalent figures, or, in other words, if every
element C of Γ is interchangeable with Δ. In this case the mathematician says
that Δ is an invariant subgroup of Γ. Consequently, Δ-equivalence is an
objective relation when Δ is an invariant subgroup of Γ. For example, the
parallel displacements form an invariant subgroup of the group of Euclidean
similarities; for the relation // between two figures that arise from one
another by parallel displacement does in fact possess objective geometrical
significance, although our language lacks a suitable word for it. The normalizer
of the group of parallel displacements consists of all affine transformations;
therefore it must be possible to build affine geometry on the one relation //
between figures. Or still more simply, the subgroup consisting solely of the
identity is an invariant subgroup, and in fact the relation of identity between
two figures is of objective significance. There is none with a better claim to
objectivity, since identity is contained in every possible transformation group
Γ. The smaller the group Δ is, the larger its normalizer is, and the larger the
gap between congruence and similarity. More precisely, if Δ′ is a subgroup of Δ,
then the normalizer Γ″ of Δ′ contains the normalizer Γ′ of Δ. The normalizer of
an invariant subgroup Δ of Γ′ always includes Γ′. A geometry whose automorphism
group is Γ′ can be built solely on the objective relation of Δ-equivalence,
provided the normalizer of Δ is not larger than Γ′ but coincides with Γ′.

One final remark may conclude this analysis. Space is a continuum, and when we
speak of a transformation in space it is reasonable to interpret this as any
arbitrary continuous transformation. We denote by Ω the group of transformations
that come into consideration at all; in the case of a continuum, this would be
the group of all continuous transformations. If this is explicitly laid down,
our definition of the normalizer can be repeated as follows: given a subgroup Δ
of the group Ω, those elements of Ω that are interchangeable with Δ form the
normalizer Γ′ of Δ. In this form the concept of normalizer gains a sense even
for abstract groups Ω and Δ.

In Prolegomena §13 Kant speaks about the difference between congruent and
similar and claims: "We can therefore make intelligible the difference between
similar and equal, yet incongruent, things, such as oppositely coiled snails, by
no single concept, but only by the relation to the right and left hand, which
goes immediately to intuition." In his view, only transcendental idealism offers
a solution to this riddle. No doubt the meaning of congruence is grounded in the
intuition of space, but the same is true of similarity. Kant seems to aim at a
sore point, but precisely this point can be completely clarified by an analysis
in terms of a group Γ′ and its invariant subgroups Δ, or a group Δ and its
normalizer Γ′. Whenever Δ is a proper invariant subgroup of Γ′, the concepts of
congruence = Δ-equivalence and similarity = Γ′-equivalence do not coincide, even
though the former is of objective significance, that is, Γ′-invariant. The
phenomenon at which Kant marvels can thus be brought, in a highly satisfying
way, under general and abstract "concepts."

Whoever raises congruence to the rank of the sole basic relation of geometry
must then develop geometry out of this one concept. Several paths are open for
this. A deeper insight than the elementary conception permits into the style of
the Euclidean axioms would be gained if one succeeded in formulating the
fundamental facts of geometry as simple axioms about the group Δ⁺ of Euclidean
motions. According to Ueberweg, Helmholtz was the first to carry out this
program, with surprising success, in his essay "On the Facts That Underlie
Geometry." Later S. Lie, who established a general theory of transformation
groups, took up the problem again with his sharper mathematical means and
generalized it from three to n dimensions.

The Euclidean motion group Δ⁺ is characterized almost completely by the fact
that it gives the rigid body the measure of free mobility familiar to us from
experience. More exactly: by a congruent mapping one is able to transfer any
arbitrary point into any arbitrary point; in addition, while holding a point
fixed, to transfer any arbitrary line direction at that point into any other
line direction there; while holding a point and line direction fixed, to
transfer any arbitrary plane direction passing through them into any other such
plane direction; and so on up to the (n - 1)-dimensional direction elements. If,
on the other hand, a point, a line direction passing through it, a plane
direction passing through that, and so on up to an (n - 1)-dimensional direction
element is given, then apart from the identity no congruent mapping exists that
leaves this system of incident elements fixed. We just said that this axiom
characterizes the Euclidean motion group almost completely. In fact, one obtains
in this way the group of congruent transformations of a slightly more general
space, namely a projective space with an impressed Cayleyan determination of
measure. This group contains a numerical parameter λ whose value remains
undetermined: the constant curvature of space, of which only the sign is
essential. Depending on whether λ is positive, zero, or negative, one arrives at
the elliptic, parabolic (Euclidean), or hyperbolic type. These, then, are the
only homogeneous spaces in which all points are equivalent, and likewise all
directions at a point, and so on.

It is hard to speak sensibly about these problems without having before one's
eyes an exact description of the Euclidean groups Γ′ and Δ⁺. A Cartesian
reference system in three-dimensional Euclidean space consists of a point O, the
origin, and three mutually perpendicular vectors e₁, e₂, e₃ of equal length. The
coordinates x₁, x₂, x₃ of a point are defined by

```text
→OP = x₁e₁ + x₂e₂ + x₃e₃.
```

Relative to such a system, a similarity that maps the point (x₁, x₂, x₃) into
the point (x₁′, x₂′, x₃′) is represented by a linear transformation

```text
S: xᵢ′ = aᵢ + aᵢ₁x₁ + ... + aᵢₙxₙ (i = 1, 2, ..., n) (*)
```

with constant coefficients aᵢ, aᵢₖ, which satisfy the following condition:
`(x₁′ - a₁)² + ... + (xₙ′ - aₙ)²` is a constant positive multiple a of
`x₁² + ... + xₙ²`. The dimension-number n is left undetermined here. The
similarity is "non-enlarging" and is called an orthogonal transformation when
`a = 1`. The orthogonal transformations form an invariant subgroup Δ of Γ′.
From the above-mentioned condition, which is fulfilled by every similarity,
there follows the equation `d² = aⁿ` for the determinant d formed from the
aᵢₖ. Consequently, an orthogonal transformation has either sign +, `d = +1`, or
sign -, `d = -1`. The orthogonal transformations with sign + form the group Δ⁺
of Euclidean motions. Δ⁺ is a subgroup of Δ with index 2; that is, if S₁ and S₂
are any two transformations of Δ with negative sign, then S₁⁻¹S₂ has positive
sign. This is the fundamental fact of the distinction between left and right:
two screws wound oppositely with respect to a given screw wind in the same
sense. It makes little difference whether we take Δ⁺ or Δ as the group of
congruent mappings. Suppose we decide in favor of the larger group Δ. Then the
continuous motion of a rigid body would be represented by an orthogonal
transformation S(t), dependent on the time-parameter t and exhibiting the
identity I at the initial moment `t = 0`. Since the determinant of S(t) can take
only the two values +1 and -1, and since further it is equal to +1 at the
beginning `t = 0` and varies continuously with t, it must always remain +1.
Thus even if we admit arbitrary orthogonal transformations, the requirement of
continuity for S(t) automatically excludes the transformations with negative
sign. A rigid body could pass into its mirror image only by a discontinuous
jump.

A much deeper-reaching aspect of the group Δ than that of describing the
mobility of rigid bodies is disclosed by its role as the group of automorphisms
of the physical world. In physics we can consider not only points but also the
various kinds of physical quantities, such as velocity, force, electromagnetic
field strength, and so forth. But the fact is that, in a Cartesian system, not
only points but all physical quantities can be represented by numbers, for
example a force by its components fᵢ, or an electromagnetic field strength by a
set of skew-symmetric components Fᵢₖ = −Fₖᵢ. Under the influence of an arbitrary
orthogonal mapping S (*) of the space-points, they undergo a related
transformation uniquely determined by S. Thus, for example, the force components
transform according to the equation

```text
fᵢ′ = Σλ aᵢλ fλ (i, λ = 1, 2, ..., n),
```

and the components of electromagnetic field strength according to the rule

```text
Fᵢₖ′ = Σλ,μ aᵢλ aₖμ Fλμ (i, k, λ, μ = 1, 2, ..., n).
```

All laws of nature are invariant with respect to the transformation induced in
this way by the group Δ. It does not hold, however, that they are invariant with
respect to all similarities, although at a certain level of natural phenomena it
appears so. But the facts of atomism teach us that length is not relative but
absolute. The atomic constants of the charge and mass of the electron and
Planck's quantum of action h fix an absolute length standard, which proves
accessible for practical measurements through the wavelengths of spectral
lines. Thus we no longer depend on the preservation of the platinum-iridium
standard meter kept at the Comité International des Poids et Mesures in Paris.
For the basis vectors of a Cartesian reference system we now prescribe the
absolute length 1. The transformations with negative sign must also be contained
in Δ, for in the laws of nature there is no indication of a natural difference
between left and right. It is now clear why a body, all of whose places undergo
a transformation S(t) of the group Δ, depending continuously on the time
parameter t, and whose physical features change correspondingly, can with full
right assert of itself: physically, I have remained the same during my motion.

The extensive medium of the outer world consists of time as well as space. How
time fits into the above schema as a fourth coordinate will be explained in
§ 16. This step was prepared by our having left the dimension-number n
undetermined. For physics the case n = 4 is even more important than n = 3.
Here, however, we shall confine ourselves to space.

We summarize: the group of physical automorphisms in space is the group Δ of
orthogonal transformations. The group of geometrical automorphisms is, according
to the proper meaning of the word, the normalizer Γ′ of Δ. It is larger than Δ
insofar as it also contains the dilations `xᵢ′ = axᵢ` with arbitrary constant
`a > 0`. This divergence between Δ and Γ′ ultimately proves that physics can
never be reduced to geometry, as Descartes had hoped.

Left and right. If I had to name the most fundamental mathematical facts, I
would probably begin with the fact F₁ that counting a set of elements leads to
the same number no matter in what order one takes the elements, and then mention
as second the fact F₂ that among the permutations of n (≥ 2) things one can
distinguish the even from the odd. The even permutations form a subgroup of
index 2 inside the group of all permutations. The first fact forms the basis of
the geometrical concept of dimension; the second, the basis of "sense." We
consider affine vector geometry. A basis for its vectors consists of n vectors
e₁, ..., eₙ, so that any arbitrary vector can be uniquely expressed as a linear
combination `x₁e₁ + ... + xₙeₙ`; and the theorem of the invariance of the
dimension-number says that every basis necessarily consists of the same number n
of vectors. From this assertion the fact F₁ clearly follows, for by any
regrouping of the basis vectors one passes to a new basis. Conversely, the
invariance theorem forms an algebraic theorem easily derived from the fact F₁
together with the rule for addition and multiplication of numbers. Every
ordering of n given, linearly independent vectors fixes a "sense," and two
orderings fix the same sense when they arise from one another by an even
permutation, a definition by abstraction. An odd permutation changes the sense
into its opposite. That is quite clearly the combinatorial root of the
distinction between left and right. In addition, in connection with the basic
operations of affine vector geometry, vector addition and multiplication of a
vector by a number, one is led to a comparison of the "sense" of two bases
e₁, ..., eₙ and e₁*, ..., eₙ*. If one expresses the vectors e* by the vectors e,
so that

```text
eᵢ* = a₁ᵢe₁ + ... + aₙᵢeₙ,
```

then the coefficients aᵢₖ possess a non-vanishing determinant. The senses of
the two bases are either the same or opposed, according as the determinant is
positive or negative. But the definition of a determinant is grounded on the
distinction between even and odd permutations.

Kant finds the key to the riddle of left and right in transcendental idealism.
The mathematician sees behind it the combinatorial fact of the distinction
between even and odd permutations. The discrepancy between the way the
philosopher and the mathematician pose the question of the roots of the
phenomenon set before us by nature could hardly be illuminated more strikingly.

Footnote 1: Cf. p. 108.

## Notes

- The section makes congruence doubly grounded: historically in our practical
  use of rigid bodies, but mathematically as the group Δ⁺ of Euclidean motions.
- Similarity is not the same relation as congruence. It is recovered as the
  normalizer Γ of the motion group Δ⁺; mirror images and scale models are the
  accessible examples.
- Kant's left/right problem is respected but deflated. The phenomenon points to
  spatial intuition, yet its abstract structure can be handled by invariant
  subgroups, normalizers, determinants, and even/odd permutations.
- Physics now pushes beyond pure geometry. Natural laws are invariant under the
  physical automorphism group Δ, but not under all geometrical similarities;
  atomism gives an absolute length standard.
- The sentence that physics can never be reduced to geometry is the section's
  hinge into the natural-science part of the book.

## Translation Decisions

- `Kongruenz` is `congruence`; `Ähnlichkeit` is `similarity`.
- `starre Körper` is `rigid bodies`.
- `euklidische Bewegungen` is `Euclidean motions`.
- `Normalisator` is `normalizer`.
- `vertauschbar` is rendered as `interchangeable with`; the local definition is
  conjugation-closure, not ordinary commutativity.
- `invariante Untergruppe` is `invariant subgroup`, preserving Weyl's wording
  rather than replacing it everywhere with the later standard `normal subgroup`.
- `Raumanschauung` is `intuition of space`.
- `Sinn` is `sense`, with quotation marks where Weyl has them; it carries the
  orientation/handedness issue but should not be flattened immediately to
  `orientation`.
- `Längennormal` is `length standard`.

## Adversarial Check

The main risk is making Weyl sound like he is simply replacing Kant with group
theory. The section is subtler: he grants that congruence and similarity are
grounded in spatial intuition, but argues that the precise puzzle Kant treats
as resistant to concepts can be brought under abstract concepts once the
normalizer/invariant-subgroup structure is made explicit.
