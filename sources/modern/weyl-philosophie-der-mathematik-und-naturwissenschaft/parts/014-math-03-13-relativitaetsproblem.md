# Part 014: The Relativity Problem

Second chapter-III batch. Section 13 gives Weyl's first explicit formulation
of the relativity problem: objectivity is not immediate givenness, but
invariance under a permitted group of transformations. The section then turns
from objective relations to symbolic coordinate construction, where the
reference frame remains the necessary residue of intuitive exhibition.

## Scope

- `13. Das Relativitätsproblem`
- section-local `LITERATUR`
- printed pages `95-104`
- PDF/page-image pages `96-105`

The initial next-batch note listed printed pages `95-103` / PDF pages
`96-104`. Direct inspection showed that section 13 continues onto printed page
`104` / PDF page `105`, including the final function-frame paragraph and the
literature item before section 14 begins.

## Source Anchors

- `source/cleaned/010-math-03-geometrie.txt`
- `source/page-images/jpg-200/page-0096.jpg`
- `source/page-images/jpg-200/page-0097.jpg`
- `source/page-images/jpg-200/page-0098.jpg`
- `source/page-images/jpg-200/page-0099.jpg`
- `source/page-images/jpg-200/page-0100.jpg`
- `source/page-images/jpg-200/page-0101.jpg`
- `source/page-images/jpg-200/page-0102.jpg`
- `source/page-images/jpg-200/page-0103.jpg`
- `source/page-images/jpg-200/page-0104.jpg`
- `source/page-images/jpg-200/page-0105.jpg`

## Source Status

The active page range was visually checked against page images. The cleaned
German source was corrected for this batch, especially:

- automorphism and group notation: `σ`, `τ`, `ι`, `σ⁻¹`, `στ`, `τ⁻¹σ⁻¹`,
  `Γ`, `Γ₀`, `Γ′`, `Γ″`, and `Σ`
- relation and congruence notation: `AB ≡ CD`, `R(ab ···)`,
  `R(a′b′c′)`, `R₁`, and `R₂`
- coordinate and reference-frame formulas: `P ↔ x`, `x = ax′ + b`,
  `A(p; f) = A(pσ; fσ)`, `x --(S)--> x′`, `x = x′S`, and `S* = CSC⁻¹`
- the page-103 diagram relating `x`, `x′`, `y`, and `y′`
- the footnote marker after `Ich-Vernichtung¹)` and prime notation in
  `O′E′`, `f′`, `p′`, `x′`, and `y′`

## German

```text
13. Das Relativitätsproblem

Unser Wissen steht unter der Norm der Objektivität. Wer an
die euklidische Geometrie glaubt, wird sagen, alle Punkte im Raum
seien objektiv gleich, ebenso alle möglichen Richtungen. Newton
indessen scheint gedacht zu haben, der Raum besitze ein absolutes

[[pdf-page:0097 printed-page:96]]

Zentrum. Epikur denkt sicher, die Vertikale lasse sich objektiv
von allen andern Richtungen unterscheiden. Als Grund führt er an,
daß sich alle sich selbst überlassenen Körper in ein und derselben
Richtung bewegen. Somit ist die Feststellung, eine Linie verlaufe
vertikal, elliptisch oder unvollständig, wobei die dahinter stehende
vollständige Feststellung etwa so lautet: die Linie hat die Richtung
der Schwerkraft im Punkte P. Somit geht das Schwerefeld, von
dem wir wissen, daß es von der Zusammensetzung der Materie der
Welt abhängt, in die vollständige Aussage als Zufallsfaktor ein,
ebenso auch ein einzeln angedeuteter Punkt P, auf den wir mit
dem Finger bei einem demonstrativen Akt weisen, der in Wörtern
wie „ich“, „hier“, „jetzt“, „dies“ zum Ausdruck kommt. Nur wenn
wir sicher sind, daß die Wahrheit der vollständigen Feststellung
nicht durch freie Variation der Zufallsfaktoren und solcher Faktoren, die einzeln aufgedeckt werden (wie etwa das Schwerefeld
und der Punkt P) beeinflußt wird, haben wir das Recht, diese
Faktoren aus der Feststellung wegzulassen und noch objektive Bedeutung dafür zu beanspruchen. Epikurs Glaube geht dahin, sobald festgestellt wird, daß die Richtung der Schwerkraft in Princeton anders verläuft als in Kalkutta, und daß sie sich außerdem
durch eine Umverteilung der Materie ändern kann. Ohne Anspruch
auf ein mechanisch anwendbares Kriterium bestätigt unsere Schilderung die wesentliche Tatsache, daß Objektivität etwas ist, das
nur auf dem Boden der Erfahrung entscheidbar ist. So erklären
sich auch zwei Hauptquellen für die so oft in der Geschichte der
Wissenschaften begangenen Irrtümer, nämlich eine Feststellung
für objektiv zu nehmen, ohne daß sie es ist: 1. man hat bestimmte
sachliche Umstände übersehen, von denen der Sinn der Feststellung abhängt, obgleich sie nicht explizit in ihrer elliptischen Form
erwähnt sind; 2. man hat, auch wenn diese Umstände oder Faktoren erkannt wurden, nicht sorgfältig genug untersucht, ob durch
deren Variation die Wahrheit der Aussage beeinflußt wird. Kein
Wunder, daß in mehreren Phasen im Verlaufe der Geschichte der
Naturwissenschaften das Gebiet dessen, was als objektiv angesehen wurde, zusammengeschrumpft ist.

Während die philosophische Frage der Objektivität nicht leicht
klar und definit beantwortet werden kann, kennen wir exakt die

[[pdf-page:0098 printed-page:97]]

adäquaten mathematischen Begriffe für die Formulierung dieser
Idee. Wir gehen von einer vollständig axiomatisierten Wissenschaft
wie der euklidischen Geometrie aus. Der Einfachheit halber nehmen wir nur eine fundamentale Kategorie an, nämlich die Raumpunkte. Nach Hilbert wären dann die Grundrelationen, die in die
Axiome eingehen, 1. die ternäre Relation: drei Punkte liegen auf
einer geraden Linie; 2. die Relation: (drei verschiedene Punkte
A, B und C liegen auf einer geraden Linie und) B liegt zwischen
A und C; 3. die Relation: vier Punkte liegen in einer Ebene; 4. die
Kongruenzrelation AB ≡ CD zwischen zwei Punktepaaren AB
und CD. Was wir damit sagen wollen, läßt sich auf jeden Bereich
von Dingen anwenden, dessen Axiome ein paar Grundrelationen
behandeln. Ohne vorzugreifen, was nun diese Dinge sind, können
wir sie Punkte nennen und vom Sachbereich somit als dem Punktfeld sprechen.

In § 4 ist der Begriff der isomorphen Abbildung eingeführt
worden. Wir betrachten nun den Sonderfall, daß unser Sachgebiet
nicht auf ein anderes Gebiet, sondern auf sich selbst abgebildet
wird, und gelangen so zum Begriff des Automorphismus: Automorphie ist eine eineindeutige oder umkehrbar eindeutige Abbildung p → p′ des Punktfeldes auf sich selbst, die die Grundrelationen ungestört läßt; das heißt, stets wenn Punkte a, b, ...
der Grundrelation R(ab ···) genügen, dann genügen auch die
Punkte a′, b′, ..., in die a, b durch die Abbildung übertragen werden, der gleichen Relation, und umgekehrt. Mit andern Worten,
aus R(ab ···) folgt R(a′b′ ···), und aus R(a′b′ ···) folgt R(ab ···).
Eine Abbildung σ überträgt jeden Punkt des Punktfeldes in einen
Punkt p′ = pσ. Die einfachste Abbildung ist die Identität ι, die
jeden Punkt p in p selbst überträgt. Zwei Abbildungen σ : p → p′
und τ : p′ → p″ können nacheinander ausgeführt und dann als
neue Abbildung στ : p → p″ aufgefaßt werden. Eine Abbildung
σ : p → p′ ist eineindeutig, wenn sie eine Inverse σ⁻¹ besitzt, die p′
zurück nach p abbildet: σσ⁻¹ = σ⁻¹σ = ι. Dann ist auch σ⁻¹ eineindeutig. Die Identität ist eine eineindeutige Abbildung; und wenn
σ und τ eineindeutige Abbildungen sind, so ist es auch στ mit der
Inversen τ⁻¹σ⁻¹. Das Wort Transformation wird als Synonym für
eineindeutige Abbildung verwendet. Die fundamentale Eigenschaft

[[pdf-page:0099 printed-page:98]]

für Automorphismen ist, daß sie eine Gruppe bilden. Dies bedeutet
die drei folgenden Dinge: 1. Die Identität ist ein Automorphismus;
2. ist σ ein Automorphismus, dann auch σ⁻¹; 3. sind σ und τ
Automorphismen, dann ist auch στ einer. Diese drei Tatsachen
folgen unmittelbar aus der Definition.

Eine Figur F im weitesten Sinne oder eine Konfiguration von
Punkten ist nichts anderes als eine Punktmenge; F ist gegeben,
wenn für jeden Punkt p bestimmt ist, ob er zu F gehört oder nicht.
Eine ternäre Relation R(xyz) zwischen Punkten heißt invariant
gegenüber einer gegebenen Transformation σ : p → p′ und ihrer
Inversen p′ → p, wenn aus R(abc) stets R(a′b′c′) folgt, und umgekehrt. Nun können wir exakt sagen, was mit objektiver Gleichheit oder „Unterschiedslosigkeit“ aller Punkte im euklidischen
Raum gemeint ist. Sie bedeutet, daß für zwei beliebige Punkte p₁
und p₀ stets ein Automorphismus existiert, der p₀ in p₁ überführt.
Zwei Figuren F und F′ heißen ähnlich, wenn die eine durch einen
Automorphismus in die andere überführt werden kann. Dies ist
nun unsere Deutung der Leibnizschen Definition ähnlicher Figuren als solche, die nicht auseinandergehalten werden können,
wenn sie jede für sich betrachtet werden. Die drei Gruppenpostulate stellen schlicht fest, daß jede Figur sich selbst ähnlich ist, und
daß die Ähnlichkeit symmetrisch und transitiv ist (s. die Äquivalenzaxiome auf S. 23). Eine Punktrelation heißt objektiv, wenn
sie gegenüber allen Automorphismen invariant ist. In diesem Sinne
sind die Grundrelationen objektiv, ebenso alle logisch aus ihnen
nach den in § 1 angegebenen Prinzipien definierten Relationen,
vorausgesetzt es wird kein Gebrauch von Prinzip Nr. 5 gemacht,
das eine Leerstelle zuläßt, die von einem individuell aufgewiesenen
Punkt ausgefüllt wird. (Ob jede objektive Relation so definiert
werden kann, wirft eine Frage der logischen Vollständigkeit auf,
die wohl kaum als entsprechende Frage der Vollständigkeit für
Axiome in der Form beantwortet werden kann, ob jede wahre
allgemeine Aussage über Punkte aus den Axiomen geschlossen
werden kann.)

Lautet unsere Aufgabe den wirklichen Raum zu untersuchen,
so sind uns weder die Axiome noch die Grundrelationen gegeben.
Im Gegenteil: Bei unserem Versuch, die Geometrie zu axiomati-

[[pdf-page:0100 printed-page:99]]

sieren, wählen wir als unsere Grundrelationen einige von den
Punktrelationen aus, von denen wir überzeugt sind, daß sie objektive Bedeutung besitzen (Epikur hätte zum Beispiel die Grundrelation mit aufgenommen: A, B liegen auf einer Vertikalen; Euklid
hat das nicht getan). Um also dem wahren Sachverhalt gerecht zu
werden, müssen wir wohl die Reihenfolge in der Entwicklung
unserer Gedanken umkehren. Wir gehen von einer Transformationsgruppe Γ aus. Sie beschreibt sozusagen, bis zu welchem Grade
unser Punktfeld homogen ist. Ist die Gruppe einmal gegeben, so
wissen wir, was Gleichheit oder Ähnlichkeit bedeutet, nämlich:
zwei Figuren sind ähnlich (oder gleich, oder äquivalent), die durch
eine Transformation von Γ auseinander hervorgehen; ferner, unter
welchen Bedingungen eine Relation objektiv ist, nämlich dann,
wenn sie gegenüber allen Transformationen von Γ invariant ist.
In diesem Sinne hat Felix Klein in seinem berühmten Erlanger
Programm (1872) die Formulierung gemeint, eine Geometrie sei
durch eine Transformationsgruppe bestimmt. Die Frage der Axiomatisierung dieser Geometrie ist damit auf den Hintergrund zurückgeführt. (Als erster Schritt müßten ein paar objektive Relationen R₁, R₂, ... aufgesucht werden, so daß dabei die Gruppe
aller Transformationen, die R₁, R₂, ... invariant lassen, nicht größer
als Γ wird, sondern mit Γ zusammenfällt.) Während wir unsere
Augen nicht vor der Tatsache verschließen müssen, daß objektive
Relationen logisch aus anderen derartigen Relationen konstruiert
werden können, verzichten wir darauf, einen Unterschied zwischen
Grundrelationen und abgeleiteten zu machen. Wir sind an allen
invarianten Relationen gleich interessiert.

Hätte Newton recht mit seinem absoluten Zentrum O des Raumes,
so bestünde die wahre Gruppe Γ₀ der Automorphismen aus den Transformationen der euklidischen Gruppe Γ von Automorphismen, die O
fest lassen; Newtons Γ₀ ist eine Untergruppe der euklidischen Gruppe Γ.
Andererseits sind wir bei der Untersuchung der euklidischen Geometrie
in erster Linie an solchen Eigenschaften interessiert, die gegenüber allen
affinen oder allen projektiven Transformationen invariant sind. (Die
affinen bzw. die projektiven Transformationen der Ebene sind solche,
die sich ergeben, wenn man nacheinander eine Anzahl Parallelprojektionen bzw. Zentralprojektionen ausführt.) Die Gruppen Γ′ und Γ″

[[pdf-page:0101 printed-page:100]]

dieser Transformationen sind umfassender als Γ; genauer: Γ ist ein Teil
von Γ′, und Γ′ ein Teil von Γ″. Die Wichtigkeit der affinen und der
projektiven Geometrie für die Theorie der Perspektive ist offenkundig.
Man sieht, wie nützlich sich der Kleinsche Standpunkt für eine geordnete
Übersicht erweist, und bei der Aufdeckung der gegenseitigen Beziehungen werden verschiedene Arten von Geometrien entweder durch die
Natur der Dinge angeregt, oder sie entspringen aus einer willkürlichen,
aber logisch nützlichen Abstraktion. (Ein Vorgänger von Klein war
Möbius, der den gruppentheoretischen Standpunkt für eine Anzahl bestimmter Arten von Geometrie betonte.) Die umfangreichste Automorphismengruppe, die man möglicherweise für ein Kontinuum betrachten kann, besteht aus allen kontinuierlichen Transformationen; die
entsprechende Geometrie heißt Topologie. Für die Entwicklung der
Mathematik war es ein glücklicher Zufall, daß das Relativitätsproblem
nicht zuerst für den kontinuierlichen Punktraum, sondern für ein System
angepackt wurde, das aus einer endlichen Anzahl verschiedener Dinge
bestand, nämlich dem System der Wurzeln einer algebraischen Gleichung
mit rationalen Koeffizienten (Galoissche Theorie). Dieser Umstand war
ein Segen für die Exaktheit der entsprechenden Begriffsbildungen. Die
objektiven Relationen sind hier solche, die sich aus den vier Grundoperationen der Algebra aufbauen lassen (Addition, Subtraktion, Multiplikation, Division), mit andern Worten, die algebraischen Relationen
mit rationalen Koeffizienten. Aus Problemen dieser Art entstand eine
allgemeine Theorie, nicht lediglich der Transformationsgruppen, sondern
auch der abstrakten Gruppen.

Nach dieser Erklärung der Automorphismen kommen wir nun
zu einer zweiten Phase des Relativitätsproblems. Wie lassen sich
den Punkten eines Punktfeldes Kennzeichen oder Marken zuordnen, die zur Identifizierung oder Unterscheidung der Punkte
dienen können? Die Marken sollen selbsterzeugende, verschiedene
und stets reproduzierbare Symbole sein wie Namen, Zahlen (oder
Zahlentripel x, y, z) usw. Erst dann kann man daran denken, das
Schauspiel der wirklich gegebenen Welt durch Konstruktion in
einem Symbolfeld darzustellen. Alles Wissen, auch wenn es von
der intuitiven Beschreibung ausgeht, tendiert zu einer symbolischen Konstruktion. Auf ernste Schwierigkeiten stößt man so lange
nicht, wie man es mit einem Bereich von einer nur endlichen Anzahl Punkte zu tun hat, die man nacheinander „aufrufen“ kann,

[[pdf-page:0102 printed-page:101]]

Das Problem wird ernst, wenn das Punktfeld unendlich wird, insbesondere wenn es ein Kontinuum ist. Eine begriffliche Festlegung
von Punkten durch Marken der oben geschilderten Art, die die
Rekonstruktion jedes einmal verlorenen Punktes ermöglichte, ist
hier nur in Verbindung mit einem Koordinatensystem oder einem
Bezugsrahmen möglich, was durch einen individuellen demonstrativen Akt aufgewiesen werden muß. Die Objektivierung durch
Ausschaltung des Ich und seines unmittelbaren Lebens der Anschauung gelingt nicht restlos, und das Koordinatensystem bleibt
als das notwendige Residuum der Ich-Vernichtung¹). Es ist gut
hier daran zu erinnern, daß praktisch zwei- oder dreidimensionale
Punktmengen gewöhnlich so gegeben werden, daß man sich tatsächlich einen Körper oder eine Figur mit Bleistift auf Papier
gezeichnet vor Augen hält, und nicht durch eine logisch-arithmetische Konstruktion von mengendefinierenden Eigenschaften.
Die Mathematik hat lange gebraucht, bis sie sich die konstruktiven Hilfsmittel erworben hatte, um mit der Komplexität und
Vielfalt solcher anschaulich gegebener Figuren fertig zu werden.
Nachdem sie jedoch dieses Stadium erreicht hatte, wurde die Überlegenheit ihrer symbolischen Methoden offenkundig.

Als Beispiel nehmen wir die Punkte auf einer Geraden. Das Koordinatensystem besteht hier aus einem Anfangspunkt O und einer
Einheitsstrecke OE oder aus zwei verschiedenen Punkten O und E. Ist
dieser Bezugsrahmen gegeben, kann jeder beliebige Punkt P durch seine
Abszisse x gekennzeichnet werden, das ist die Maßzahl der mit der
Einheitsstrecke OE ausgemessenen Länge OP (x ist positiv für die Punkte
auf der gleichen Seite von O aus wie E und negativ für die Punkte auf
der anderen Seite). Zwei Bezugsrahmen, OE und O′E′, sind objektiv
gleichwertig; denn es gibt genau einen Automorphismus (Ähnlichkeit),
der O auf O′ und E auf E′ abbildet. Infolgedessen ist durch Aufweisung
eines individuellen Koordinatensystems nicht mehr als unbedingt not-

1) Man könnte gegen die Statuierung eines prinzipiellen Unterschiedes
zwischen begrifflicher Fixierung und anschaulicher Aufweisung den Einwand
erheben, daß doch auch die objektiven geometrischen Relationen, auf welche
sich die begriffliche Bestimmung gründet, in der Anschauung aufgewiesen
werden müssen. Aber das sind einige wenige Relationsbegriffe, während die
Punkte selber ein Kontinuum bilden; es muß zugegeben werden, daß nur
hierin der prinzipielle Unterschied besteht.

[[pdf-page:0103 printed-page:102]]

wendig aufgewiesen. Das Feld für das Symbol x besteht aus allen reellen
Zahlen. In bezug auf ein gegebenes Koordinatensystem ist die Zuordnung P ↔ x eine eineindeutige Abbildung des Punktfeldes auf den
Variabilitätsbereich des Symbols. Die Koordinaten x und x′ eines beliebigen Punktes in zwei Koordinatensystemen sind durch eine Relation
x = ax′ + b miteinander verbunden, wo a ≠ 0 und b zwei Konstante
sind, die die relative Lage der beiden Koordinatensysteme zueinander
kennzeichnen.

Mit diesem Beispiel vor Augen können wir nun die folgende
allgemeine Beschreibung verstehen. Es sei eine Klasse Σ von Bezugsrahmen f gegeben. Die Klasse als solche sollte objektiv unterschieden werden können, das heißt wenn f zu ihr gehört, dann
auch jeder ähnliche Rahmen fσ = f′, der aus f durch einen Automorphismus σ hervorgeht. Die Klasse soll jedoch nicht mehr Elemente enthalten, als diese Forderung unbedingt notwendig macht,
das heißt zwei beliebige Rahmen f, f′ der Klasse sind ähnlich.
Außerdem soll eine objektive Vorschrift A gegeben sein, nach der
jeder Punkt p in bezug auf jeden Rahmen f der Klasse Σ ein definites (reproduzierbares) Symbol x = A(p; f) als Koordinate bestimmt. Für ein gegebenes f ist die Zuordnung p ↔ x zwischen
den Punkten p und den Symbolen x umkehrbar eindeutig. Daß x
durch p und f objektiv bestimmt ist, bedeutet, daß

A(p; f) = A(pσ; fσ)     (*)
für jeden Automorphismus zutrifft.

Aus diesen Bedingungen ergeben sich die folgenden Folgerungen. Es sei σ ein Automorphismus p → p′ des Punktfeldes und f
ein fester Rahmen der Klasse Σ. Die Koordinaten x von p und
x′ von p′ in diesem Rahmen sind durch eine Transformation
S, x′ = xS, miteinander verbunden, die den Automorphismus σ
durch f darstellt. Der Identität σ = ι entspricht die Identität S = I;
σ⁻¹ und στ werden durch S⁻¹ und ST dargestellt, wenn σ und τ
durch S und T dargestellt werden. In diesem Sinne bilden die
Transformationen S, die den verschiedenen σ von Γ entsprechen,
eine Gruppe G, die isomorph zu Γ ist. G ist nichts anderes als die
Darstellung von Γ mittels f. Nehmen wir andererseits einen festen
Rahmen f unserer Klasse Σ und einen beliebigen Rahmen f′ = fσ,

[[pdf-page:0104 printed-page:103]]

der aus f durch den Automorphismus σ hervorgeht; ich behaupte
nun, daß die Koordinaten x und x′ des gleichen beliebigen Punktes
in bezug auf f und f′ durch die Gleichung x = x′S miteinander
verknüpft sind. Bezeichnen wir nämlich den beliebigen Punkt mit
pσ statt mit p, so haben wir x = A(pσ; f) und wegen (*)

x′ = A(pσ; fσ) = A(p; f),
und daraus folgt unsere Behauptung. Die Gruppe G, die Γ mittels f
darstellt, muß unabhängig von f sein. Tatsächlich würde eine
Darstellung von Γ durch zwei verschiedene Gruppen G, G* mittels
den beiden ähnlichen Rahmen f und f* einen objektiven Unterschied zwischen f und f* erscheinen lassen, was unmöglich ist. Es
ist leicht dies explizit zu bestätigen. Es sei f* = fγ, wo γ ein Automorphismus ist. Außerdem seien x und x′ die Koordinaten eines
beliebigen Punktes p und seines Bildes p′ = pσ in bezug auf f, und
y und y′ in bezug auf f*. Die Transformationen, die γ und σ
mittels f darstellen, heißen C und S. Wir schreiben nun die

Gleichung x′ = xS in der einprägsameren Form x --(S)--> x′. Nach
dem Gesagten erhalten wir nun das Diagramm

        (S)
x  -------->  x′
(C) ↑      ↓ (C⁻¹).
y             y′

Folglich ist die Transformation, die y in y′ überführt und somit
mittels des Rahmens f* darstellt, S* = CSC⁻¹. Mit S gehört auch
CSC⁻¹ = S* zur Gruppe G, und umgekehrt ist S = C⁻¹S*C.
Solange die Punkte nicht begrifflich gekennzeichnet werden
konnten, konnten es auch die Transformationen des Punktfeldes
nicht, und es war vielleicht auch nicht ganz klar, was mit der Aussage gemeint war, die Automorphismengruppe sei bekannt oder
gegeben. Nun ist ein Stadium erreicht, wo dieser letzte Anflug
von Unklarheit verschwindet. Jeder einzelne Punkt wird durch
seine Koordinate x (in bezug auf einen festen Rahmen) ersetzt,
und somit erscheint die Gruppe Γ der Automorphismen σ als
Gruppe G der Transformationen S. Die individuelle Transformation S, die x in x′ = xS überführt, ist ein reproduzierbares

[[pdf-page:0105 printed-page:104]]

Symbol wie jeder einzelne individuelle Wert von x. Aber während
die Koordinate x nicht nur von p, sondern auch von f abhängt,
ist die Gruppe G unabhängig von f und somit frei von jeder Notwendigkeit individueller Aufweisung. Um die Forderung der Objektivität zu erfüllen, konstruieren wir ein Bild von der Welt in
Symbolen. Der reine Mathematiker drückt das so aus: Ist eine
Gruppe G von Transformationen in einem Feld von Symbolen
gegeben, so wird eine Geometrie durch die Übereinkunft aufgestellt, nur solche Relationen in dem Feld als objektiv zu untersuchen und zu betrachten, die gegenüber den Transformationen
von G invariant sind.

Eine letzte Bemerkung rein logischer Natur bezieht sich auf die
Rahmen. Es ist ganz rechtmäßig, als Bezugsrahmen f die von f gebildete
Koordinatenzuordnung p → x = f(p) selbst zu betrachten. Dies scheint
sogar zweckmäßig zu sein, wenn man auf eine so umfangreiche Automorphismengruppe gefaßt sein muß, die alle kontinuierlichen Transformationen enthält. Das Symbol f ist dann einfach ein Zeichen für die
Funktion f, deren Argumentbereich sich über die Punkte p erstreckt,
und deren Wert ein Element x im Symbolfeld ist. Ist σ : p → p′ eine beliebige Transformation, dann wird die transformierte Funktion f′ = fσ
durch die Gleichung f′(p′) = f(p) für p′ = pσ oder f′(p) = f(pσ⁻¹)
definiert. Schreiben wir x = A(p; f) für x = f(p), dann ist mit A
der allgemeine logische Operator „Wert von“ gemeint. x = A(p; f)
bedeutet: x ist der Wert der Funktion f für das Argument p.

LITERATUR

F. Klein, Vergleichende Betrachtungen über neuere geometrische
Forschungen. Erlangen 1872. (Gesammelte mathematische Abhandlungen I, S. 460—497.)
```

## Translation

### 13. The Relativity Problem

Our knowledge stands under the norm of objectivity. Whoever believes in
Euclidean geometry will say that all points in space are objectively equal, and
so are all possible directions. Newton, however, seems to have thought that
space possesses an absolute center. Epicurus certainly thinks that the vertical
can be distinguished objectively from all other directions. As his reason he
adduces the fact that all bodies left to themselves move in one and the same
direction. Thus the statement that a line runs vertically is elliptical or
incomplete; the complete statement standing behind it might read: the line has
the direction of gravity at the point P. Thus the gravitational field, which we
know depends on the composition of matter in the world, enters into the
complete assertion as a contingent factor, and so does an individually indicated
point P, toward which we point with the finger in a demonstrative act expressed
in words such as "I," "here," "now," and "this." Only when we are certain that
the truth of the complete statement is not affected by free variation of the
contingent factors and of such factors as are individually disclosed, such as
the gravitational field and the point P, do we have the right to omit these
factors from the statement and still claim objective meaning for it. Epicurus'
belief vanishes as soon as it is established that the direction of gravity runs
differently in Princeton than in Calcutta, and that it can also change through a
redistribution of matter. Without claiming to have a mechanically applicable
criterion, our description confirms the essential fact that objectivity is
something decidable only on the ground of experience. This also explains two
main sources of errors so often committed in the history of the sciences,
namely taking a statement to be objective when it is not: 1. one has overlooked
definite factual circumstances on which the meaning of the statement depends,
although they are not explicitly mentioned in its elliptical form; 2. even when
these circumstances or factors were recognized, one did not investigate
carefully enough whether variation of them affects the truth of the statement.
No wonder that, in several phases in the course of the history of the natural
sciences, the domain of what was regarded as objective has shrunk.

Although the philosophical question of objectivity cannot easily be answered
clearly and definitively, we know exactly the adequate mathematical concepts
for formulating this idea. We start from a completely axiomatized science such
as Euclidean geometry. For simplicity, we assume only one fundamental category,
namely spatial points. According to Hilbert, the basic relations entering into
the axioms would then be: 1. the ternary relation that three points lie on a
straight line; 2. the relation that three distinct points A, B, and C lie on a
straight line and B lies between A and C; 3. the relation that four points lie
in a plane; 4. the congruence relation AB ≡ CD between two pairs of points AB
and CD. What we mean to say by this can be applied to any domain of things
whose axioms treat a few basic relations. Without prejudging what these things
are, we can call them points and thus speak of the subject-domain as the
point-field.

In § 4 the concept of isomorphic mapping was introduced. We now consider the
special case in which our subject-domain is not mapped onto another domain but
onto itself, and thus arrive at the concept of automorphism: an automorphism is
a one-to-one, or reversibly unique, mapping p → p′ of the point-field onto
itself that leaves the basic relations undisturbed. That is, whenever points a,
b, ... satisfy the basic relation R(ab ···), then the points a′, b′, ... into
which a, b are transferred by the mapping satisfy the same relation, and
conversely. In other words, R(ab ···) implies R(a′b′ ···), and R(a′b′ ···)
implies R(ab ···). A mapping σ transfers every point of the point-field into a
point p′ = pσ. The simplest mapping is the identity ι, which transfers every
point p into p itself. Two mappings σ : p → p′ and τ : p′ → p″ can be carried
out one after the other and then understood as a new mapping στ : p → p″. A
mapping σ : p → p′ is one-to-one if it possesses an inverse σ⁻¹ that maps p′
back to p: σσ⁻¹ = σ⁻¹σ = ι. Then σ⁻¹ is also one-to-one. The identity is a
one-to-one mapping; and if σ and τ are one-to-one mappings, then so is στ, with
inverse τ⁻¹σ⁻¹. The word transformation is used as a synonym for one-to-one
mapping. The fundamental property of automorphisms is that they form a group.
This means the following three things: 1. the identity is an automorphism; 2. if
σ is an automorphism, then so is σ⁻¹; 3. if σ and τ are automorphisms, then στ
is also one. These three facts follow immediately from the definition.

A figure F in the broadest sense, or a configuration of points, is nothing
other than a set of points; F is given when, for every point p, it is determined
whether or not it belongs to F. A ternary relation R(xyz) between points is
called invariant with respect to a given transformation σ : p → p′ and its
inverse p′ → p when R(abc) always implies R(a′b′c′), and conversely. Now we can
say exactly what is meant by the objective equality, or "indistinguishability,"
of all points in Euclidean space. It means that for any two points p₁ and p₀
there always exists an automorphism that transfers p₀ into p₁. Two figures F
and F′ are called similar if one can be transferred into the other by an
automorphism. This is now our interpretation of Leibniz's definition of similar
figures as those that cannot be told apart when each is considered by itself.
The three group postulates simply state that every figure is similar to itself,
and that similarity is symmetric and transitive; see the equivalence axioms on
p. 23. A point-relation is called objective if it is invariant with respect to
all automorphisms. In this sense the basic relations are objective, as are all
relations logically defined from them according to the principles stated in § 1,
provided no use is made of principle no. 5, which permits an empty place to be
filled by an individually exhibited point. Whether every objective relation can
be defined in this way raises a question of logical completeness, which can
hardly be answered as the corresponding question of completeness for axioms is
answered, in the form: can every true general statement about points be inferred
from the axioms?

If our task is to investigate actual space, then neither the axioms nor the
basic relations are given to us. On the contrary: in our attempt to axiomatize
geometry, we select as our basic relations some among the point-relations that
we are convinced possess objective meaning; Epicurus, for example, would have
included the basic relation: A and B lie on a vertical; Euclid did not do this.
Thus, in order to do justice to the true state of affairs, we probably have to
reverse the order in the development of our thoughts. We start from a
transformation group Γ. It describes, so to speak, the degree to which our
point-field is homogeneous. Once the group is given, we know what equality or
similarity means: two figures are similar, or equal, or equivalent, when they
arise from one another by a transformation of Γ. We also know under what
conditions a relation is objective: namely, when it is invariant with respect
to all transformations of Γ. In this sense Felix Klein meant the formulation in
his famous Erlangen Program of 1872 that a geometry is determined by a
transformation group. The question of the axiomatization of this geometry is
thereby pushed into the background. As a first step, a few objective relations
R₁, R₂, ... would have to be found, in such a way that the group of all
transformations that leave R₁, R₂, ... invariant does not become larger than Γ
but coincides with Γ. While we need not close our eyes to the fact that
objective relations can be logically constructed from other such relations, we
renounce making a distinction between basic and derived relations. We are
equally interested in all invariant relations.

If Newton were right about his absolute center O of space, then the true group
Γ₀ of automorphisms would consist of those transformations of the Euclidean
group Γ of automorphisms that leave O fixed; Newton's Γ₀ is a subgroup of the
Euclidean group Γ. On the other hand, in investigating Euclidean geometry we
are primarily interested in those properties that are invariant with respect to
all affine or all projective transformations. The affine and projective
transformations of the plane, respectively, are those that result when one
carries out a number of parallel projections or central projections one after
another. The groups Γ′ and Γ″ of these transformations are more comprehensive
than Γ; more precisely: Γ is a part of Γ′, and Γ′ a part of Γ″. The importance
of affine and projective geometry for the theory of perspective is obvious. One
sees how useful the Kleinian standpoint proves for an ordered survey, and in
uncovering the mutual relations, different kinds of geometry are either
suggested by the nature of things or arise from an arbitrary but logically
useful abstraction. A predecessor of Klein was Möbius, who emphasized the
group-theoretical standpoint for a number of determinate kinds of geometry. The
most comprehensive automorphism group that one can possibly consider for a
continuum consists of all continuous transformations; the corresponding
geometry is called topology. For the development of mathematics it was a happy
accident that the relativity problem was first tackled not for continuous
point-space but for a system consisting of a finite number of distinct things,
namely the system of roots of an algebraic equation with rational coefficients,
Galois theory. This circumstance was a blessing for the exactness of the
corresponding concept-formations. The objective relations here are those that
can be built up from the four basic operations of algebra, addition,
subtraction, multiplication, and division; in other words, algebraic relations
with rational coefficients. From problems of this kind arose a general theory,
not merely of transformation groups but also of abstract groups.

After this explanation of automorphisms we now come to a second phase of the
relativity problem. How can signs or marks be assigned to the points of a
point-field, serving to identify or distinguish the points? The marks are to be
self-generating, distinct, and always reproducible symbols, such as names,
numbers or number-triples x, y, z, and so on. Only then can one think of
representing the spectacle of the actually given world by construction in a
symbol-field. All knowledge, even when it starts from intuitive description,
tends toward a symbolic construction. One does not encounter serious
difficulties so long as one has to do with a domain of only a finite number of
points that can be "called up" one after another.

The problem becomes serious when the point-field becomes infinite, especially
when it is a continuum. A conceptual fixing of points by marks of the kind
described above, one that would permit the reconstruction of any once-lost
point, is possible here only in connection with a coordinate system or a
reference frame, which must be exhibited through an individual demonstrative
act. Objectification through elimination of the I and of its immediate life of
intuition does not succeed without remainder, and the coordinate system remains
as the necessary residue of the annihilation of the I. It is good to recall
here that in practice two- or three-dimensional point-sets are usually given by
actually holding before one's eyes a body or a figure drawn with pencil on
paper, and not by a logical-arithmetical construction of set-defining
properties. Mathematics took a long time to acquire the constructive aids
needed to deal with the complexity and variety of such intuitively given
figures. Yet once it had reached this stage, the superiority of its symbolic
methods became obvious.

As an example, let us take the points on a line. The coordinate system here
consists of an initial point O and a unit segment OE, or of two distinct points
O and E. If this reference frame is given, any arbitrary point P can be marked
by its abscissa x, that is, the measure-number of the length OP measured by the
unit segment OE. The number x is positive for points on the same side of O as E
and negative for points on the other side. Two reference frames, OE and O′E′,
are objectively equivalent; for there is exactly one automorphism, a similarity,
that maps O onto O′ and E onto E′. Consequently, by the exhibition of an
individual coordinate system no more than is absolutely necessary is exhibited.

1) Against the positing of a difference in principle between conceptual fixing
and intuitive exhibition, one could raise the objection that the objective
geometrical relations on which conceptual determination is based must also be
exhibited in intuition. But those are a few relational concepts, whereas the
points themselves form a continuum; it must be admitted that the difference in
principle consists only in this.

The field for the symbol x consists of all real numbers. With respect to a
given coordinate system, the assignment P ↔ x is a one-to-one mapping of the
point-field onto the range of variability of the symbol. The coordinates x and
x′ of an arbitrary point in two coordinate systems are connected by a relation
x = ax′ + b, where a ≠ 0 and b are two constants characterizing the relative
position of the two coordinate systems with respect to one another.

With this example before our eyes, we can now understand the following general
description. Let there be given a class Σ of reference frames f. The class as
such should be objectively distinguishable, that is, if f belongs to it, then so
does every similar frame fσ = f′ that arises from f by an automorphism σ. The
class should not, however, contain more elements than this requirement makes
absolutely necessary; that is, any two frames f, f′ of the class are similar.
In addition, let an objective prescription A be given, according to which every
point p, with respect to every frame f of the class Σ, determines a definite
reproducible symbol x = A(p; f) as its coordinate. For a given f, the
assignment p ↔ x between the points p and the symbols x is reversibly unique.
That x is objectively determined by p and f means that

```text
A(p; f) = A(pσ; fσ)     (*)
```

holds for every automorphism.

From these conditions the following consequences result. Let σ be an
automorphism p → p′ of the point-field, and let f be a fixed frame of the class
Σ. The coordinates x of p and x′ of p′ in this frame are connected by a
transformation S, x′ = xS, which represents the automorphism σ by means of f. To
the identity σ = ι corresponds the identity S = I; σ⁻¹ and στ are represented
by S⁻¹ and ST if σ and τ are represented by S and T. In this sense the
transformations S corresponding to the different σ of Γ form a group G
isomorphic to Γ. G is nothing other than the representation of Γ by means of f.
If, on the other hand, we take a fixed frame f of our class Σ and an arbitrary
frame f′ = fσ that arises from f by the automorphism σ, then I claim that the
coordinates x and x′ of the same arbitrary point with respect to f and f′ are
linked by the equation x = x′S. For if we designate the arbitrary point by pσ
instead of by p, then we have x = A(pσ; f), and because of (*)

```text
x′ = A(pσ; fσ) = A(p; f),
```

and from this our claim follows. The group G that represents Γ by means of f
must be independent of f. In fact, a representation of Γ by two different
groups G, G* by means of the two similar frames f and f* would allow an
objective difference between f and f* to appear, which is impossible. It is
easy to confirm this explicitly. Let f* = fγ, where γ is an automorphism.
Further, let x and x′ be the coordinates of an arbitrary point p and of its
image p′ = pσ with respect to f, and y and y′ with respect to f*. The
transformations that represent γ and σ by means of f are called C and S. We
now write the equation x′ = xS in the more memorable form x --(S)--> x′.
According to what has been said, we now obtain the diagram

```text
        (S)
x  -------->  x′
(C) ↑      ↓ (C⁻¹).
y             y′
```

Consequently the transformation that transfers y into y′ and thus represents σ
by means of the frame f* is S* = CSC⁻¹. Along with S, CSC⁻¹ = S* also belongs
to the group G, and conversely S = C⁻¹S*C.

As long as the points could not be conceptually marked, neither could the
transformations of the point-field be so marked, and perhaps it was also not
entirely clear what was meant by the statement that the automorphism group was
known or given. Now a stage has been reached at which this last trace of
unclarity disappears. Each individual point is replaced by its coordinate x,
with respect to a fixed frame, and thus the group Γ of automorphisms σ appears
as the group G of transformations S. The individual transformation S that
transfers x into x′ = xS is a reproducible symbol, like every single individual
value of x. But while the coordinate x depends not only on p but also on f, the
group G is independent of f and thus free of any necessity of individual
exhibition. In order to satisfy the demand of objectivity, we construct an
image of the world in symbols. The pure mathematician expresses this as
follows: if a group G of transformations in a field of symbols is given, then a
geometry is set up by the convention that only those relations in the field are
to be investigated and regarded as objective that are invariant with respect to
the transformations of G.

One final remark of a purely logical nature concerns the frames. It is entirely
legitimate to regard as reference frame f the coordinate assignment p → x =
f(p) itself formed by f. This even seems expedient when one must be prepared
for so comprehensive an automorphism group, one that contains all continuous
transformations. The symbol f is then simply a sign for the function f, whose
domain of arguments extends over the points p and whose value is an element x
in the symbol-field. If σ : p → p′ is any transformation, then the transformed
function f′ = fσ is defined by the equation f′(p′) = f(p) for p′ = pσ, or
f′(p) = f(pσ⁻¹). If we write x = A(p; f) for x = f(p), then A means the
general logical operator "value of." x = A(p; f) means: x is the value of the
function f for the argument p.

Literature

F. Klein, Vergleichende Betrachtungen über neuere geometrische Forschungen.
Erlangen 1872. Gesammelte mathematische Abhandlungen I, pp. 460-497.

## Notes

Section 13 makes relativity a general problem of objectivity, not first a
physics doctrine. The philosophical question is difficult because omitted
contingent factors can quietly control the truth of a statement. Weyl's
mathematical clarification is to replace naive objectivity with invariance
under automorphisms.

The key reversal is methodological: when actual space is at stake, the axioms
and basic relations are not simply given. Weyl says one should begin with a
transformation group Γ and define equality, similarity, equivalence, and
objective relation through invariance under that group. Klein's Erlangen
program becomes the organizing model.

The second phase adds the coordinate problem. A continuum cannot have its
points conceptually fixed one by one without a coordinate system or reference
frame. That frame must be individually exhibited, so symbolic construction does
not abolish intuition without remainder. The reference frame is the necessary
residue of the annihilation of the I.

This section sharpens the chapter-II dossier. Chapter II showed that the
infinite cannot be possessed as an object and must be satisfied symbolically.
Section 13 shows the same discipline operating inside geometry: the continuum
of points is handled by symbolic construction, but the construction still
depends on a demonstrated frame. Symbolization is not escape from givenness; it
is a regulated way of preserving objectivity under transformations.

The bridge to physics is now sharper than in section 12. Physics will not just
choose a geometry from a menu of formal possibilities; it must decide, through
experience, which transformations leave the content of a statement objective
and which omitted factors were illegitimately suppressed.

## Translation Decisions

- `Relativitätsproblem` is `relativity problem`
- `Objektivität` is `objectivity`
- `Feststellung` is usually `statement`; `Aussage` is `assertion` or
  `statement` according to local pressure
- `Zufallsfaktor` is `contingent factor`
- `Automorphismus` is `automorphism`
- `Automorphie` is rendered idiomatically as `an automorphism is`
- `eineindeutige Abbildung` is `one-to-one mapping`, with `reversibly unique`
  kept for `umkehrbar eindeutig`
- `Sachbereich` is `subject-domain`; `Punktfeld` is `point-field`
- `Unterschiedslosigkeit` is `indistinguishability`
- `ähnlich` is `similar`, not merely `alike`
- `wirklicher Raum` is `actual space`
- `Transformationsgruppe` is `transformation group`
- `Erlanger Programm` is `Erlangen Program`
- `Begriffsbildungen` is `concept-formations`
- `symbolische Konstruktion` is `symbolic construction`
- `Koordinatensystem` is `coordinate system`
- `Bezugsrahmen` is `reference frame`
- `Aufweisung` is `exhibition`
- `Ich-Vernichtung` is `annihilation of the I`
- `Vorschrift` is `prescription`
- `Variabilitätsbereich` is `range of variability`
- `Wert von` is `value of`

## Adversarial Check

The first risk is to read the `Relativitätsproblem` too narrowly as a prelude
to Einstein. Weyl's argument is broader: any objective science has to know
which transformations preserve meaning, and this applies equally to Euclidean,
affine, projective, topological, and algebraic cases.

The second risk is to let the group-theoretic formulation look like pure
formalism. Weyl explicitly blocks that. Which factors can be omitted from a
statement, and which transformations count, is finally decidable only on the
ground of experience.

The third risk is to over-translate `Ich-Vernichtung` psychologically. The
point is methodological: objectivity tries to eliminate the individual
demonstrative standpoint, but the coordinate frame remains as its necessary
residue when a continuum must be symbolically reconstructed.
