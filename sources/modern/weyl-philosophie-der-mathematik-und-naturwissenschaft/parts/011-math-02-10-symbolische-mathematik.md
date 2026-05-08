# Part 011: Symbolic Mathematics

Sixth chapter-II batch. Section 10 turns from Brouwer's constructive refusal of
the completed infinite to Hilbert's formalist rescue attempt: keep classical
analysis, but reinterpret it as a rule-governed sign game whose legitimacy rests
on consistency rather than intuitive truth.

## Scope

- `10. Symbolische Mathematik`
- section-local `LITERATUR`
- printed pages `76-85`
- PDF/page-image pages `77-86`

## Source Anchors

- `source/cleaned/009-math-02-zahl-und-kontinuum.txt`
- `source/page-images/jpg-200/page-0077.jpg`
- `source/page-images/jpg-200/page-0078.jpg`
- `source/page-images/jpg-200/page-0079.jpg`
- `source/page-images/jpg-200/page-0080.jpg`
- `source/page-images/jpg-200/page-0081.jpg`
- `source/page-images/jpg-200/page-0082.jpg`
- `source/page-images/jpg-200/page-0083.jpg`
- `source/page-images/jpg-200/page-0084.jpg`
- `source/page-images/jpg-200/page-0085.jpg`
- `source/page-images/jpg-200/page-0086.jpg`

## Source Status

The active page range was visually checked against page images. The cleaned
German source was corrected for this batch, especially:

- Hilbertian signs, operations, integrations, footnote markers, and `§`
  references
- formal placeholders and operators: `𝔄`, `𝔄̄`, `εₓ`, `Σₓ`, `Πₓ`, `→`, `⇔`,
  `σ`, and `b̄`
- the transfinite logical axiom rules and the restricted set-theoretic axiom
  rule
- the consistency argument around `b̄ → (b → c)` and `¯(1 = 1)`
- recursive definition notation: `σ1 = 2`, `σ(σb) = σ₂b`, `b + c`, `b · c`
- `10¹²`, `§ 6`, `§ 71`, Kant, Husserl, Brouwer's Dutch quote, `Blatt`,
  `Sphäre`, and the literature entry `inédits`

## German

```text
[[pdf-page:0077 printed-page:76]]

10. Symbolische Mathematik

Ist kein Weg geblieben, so radikalen Konsequenzen zu entgehen? Der Entschluß zu dem Opfer ist doppelt schwer angesichts
des historischen Faktums, daß in der mengentheoretischen Analysis trotz der kühnsten und mannigfaltigsten Kombinationen eine
vollkommene Sicherheit des Schließens und eine offenkundige
Einhelligkeit aller Ergebnisse angetroffen wird. Hilbert macht
sich anheischig, durch die axiomatische Methode die Mathematik
in ihrem vollen Besitzstande zu sichern. Freilich ist auch er davon
durchdrungen, daß die Kraft des inhaltlichen Denkens nicht
weiter reicht als Brouwer behauptet, daß sie die transfiniten
Schlußweisen der Mathematik nicht zu tragen imstande ist, daß
es keine Rechtfertigung für alle die transfiniten Aussagen der
Mathematik als inhaltlicher, einsichtiger Wahrheiten gibt. Was
Hilbert sicherstellen will, ist nicht die Wahrheit, sondern die
Widerspruchslosigkeit der alten Analysis.

Zu diesem Zweck muß er die Mathematik samt der Logik
formalisieren zu einem nach festen Regeln vor sich gehenden Spiel
mit Zeichen. (Sie sind nicht gemeint als Zeichen für etwas; Zeichen
der letzteren Art nennt Hilbert „Mitteilungszeichen“ und verwendet für sie die deutschen Buchstaben.) Die mathematischen
Formeln, die aus jenen Zeichen bestehen, lassen nicht durchweg
eine inhaltliche Deutung zu; neben die sinnvollen sind „ideale
Aussagen“ getreten, die eingeführt wurden, um die Gültigkeit der

[[pdf-page:0078 printed-page:77]]

einfachen logischen Gesetze künstlich wiederherzustellen, die
nach Brouwer beim Übergang zum Unendlichen verlorengegangen
waren — so wie in der algebraischen Zahlentheorie ideale Zahlen
eingeführt werden, um die Gültigkeit der einfachen Teilbarkeitssätze zu erzwingen. Es kommen vier verschiedene Sorten von
Zeichen vor¹), die sich durch die für sie gültigen Spielregeln analog
unterscheiden wie etwa die Bauern und die Springer im Schachspiel: Konstante (wie 1), Variable (Symbole für Leerstellen, x, y, ...),
ein- und mehrstellige Operationen und Integrationen. Die wichtigsten einstelligen Operationen sind ¯ (Negation), σ (Übergang von
einer natürlichen Zahl zur nächstfolgenden), Z (Za, lies: a ist
natürliche Zahl), die wichtigsten zweistelligen →, = und ε. Wir
fassen sie alle als Operationen auf; Z ist die Operation, welche
aus a die Aussage erzeugt: a ist eine Zahl, = die Operation, welche
aus a und b die Aussage erzeugt: a gleich b. Konsequenterweise
mögen diese Operationszeichen denn auch (um die Spielregeln
bequem allgemein formulieren zu können) alle vor die Glieder
geschrieben werden, auf welche sie sich erstrecken, z. B. ε(a, b)
statt a ε b. Integrationen sind Σₓ, Πₓ; sie tragen eine (oder mehrere)
beliebige Variable als Index. Durch ein vorgesetztes Integrationszeichen mit dem Index x wird die Variable x an allen Stellen der
darauf folgenden Formel „gebunden“, ihrer Substitutionsfähigkeit beraubt. Im Laufe der Entwicklung der Mathematik können
beständig neue Zeichen eingeführt werden. Was eine Formel ist,
wird rekursiv erklärt: „α) jede Konstante oder Variable für sich
ist eine Formel; β) aus einer oder zwei (oder mehreren) schon gebildeten Formeln entsteht eine neue, wenn man ein ein- bzw.
zwei- (bzw. mehr-)stelliges Operations- oder Integrationszeichen
hinschreibt und die betreffenden Formeln dahinter setzt.“ Die
fertige Formel sieht dann wie ein (parthenogenetischer) Stammbaum von Symbolen aus, von dem die „grammatikalische Struktur“ der Formel, das heißt die Art ihrer rekursiven Konstruktion
unzweideutig abgelesen werden kann. Außerdem kann man so

1) Ich schließe mich hier einem gegenüber Hilbert vereinfachten Formalismus an, den v. Neumann (Zur Hilbertschen Beweistheorie, Math. Zeitschr. 1926) aufstellt.

[[pdf-page:0079 printed-page:78]]

entscheiden, ob eine gegebene stammbaumähnliche Anordnung
von Symbolen eine Formel ist oder nicht.

Man braucht sich kein Gewissen daraus zu machen, daß im Formalismus die Operationen unterschiedslos auf alles mögliche ausgeübt
werden. Wer ob solcher Großzügigkeit bange ist, wird vielleicht zwischen
„numerischen“ und „faktischen“ Formeln unterscheiden wollen, etwa
nach den folgenden rekursiven Festsetzungen: „α) Eine Konstante oder
Variable für sich, ferner jede mit σ oder εₓ beginnende Formel ist eine
numerische Formel; andererseits sind Formeln, die mit ¯, →, ∨, &,
Z, =, ε, Σₓ, Πₓ beginnen, faktische. β) Auf die Symbole σ und Z muß
eine, auf =, ε müssen zwei numerische, dagegen auf ¯, εₓ, Σₓ, Πₓ eine
und auf →, &, ∨ zwei faktische Formeln folgen.“ Ähnliche Einschränkungen müssen sodann die axiomatischen Regeln und die syllogistische
Regel des Schließens begleiten. Ist (wie im folgenden stets) 𝔄(x) eine
beliebige Formel, in welcher nur eine Variable x frei (nicht gebunden)
vorkommt, b (oder c) eine Formel ohne freie Variable oder eine „geschlossene Formel“, so kann man in 𝔄 überall dort, wo x frei auftritt,
die ganze Formel b an Stelle von x einsetzen. Durch dieses anschaulich
beschriebene Verfahren der Substitution entsteht wiederum eine Formel;
sie ist gemeint mit dem Abkürzungszeichen 𝔄(b). Der Übersichtlichkeit
halber verwenden wir jetzt die Operationszeichen wieder in der üblichen
Weise vor, über oder zwischen den Gliedern und schreiben a + 1 an
Stelle von σa (so daß also + 1 ein nachgestelltes Operationszeichen ist,
das mit der Konstanten 1 nichts zu tun hat).

Ausgangspunkt eines Beweises sind die Axiome. Dazu gehören erstens
die Axiome der finiten Logik; z. B.

c → (b → c).

Doch werden sie jetzt als allgemeine Regeln zur Bildung von Axiomen
betrachtet: nimm irgend zwei Formeln b und c her ohne freie Variable
und stelle sie zu der Formel c → (b → c) zusammen; was du so erhältst,
darfst du als Axiom benutzen. Zweitens treten auf die beiden Axiomenregeln der Gleichheit; sie vermitteln zwischen Logik und Arithmetik:

b = b;
(b = c) → (𝔄(b) = 𝔄(c)).

Drittens spezifisch arithmetische Regeln von finitem Charakter; in ihnen
erscheint die Konstante 1, der gegenständliche Ausgangspunkt aller
Konstruktion:

[[pdf-page:0080 printed-page:79]]

Z1.

Zb → Z(b + 1).

(b + 1 = c + 1) → (b = c).
¯(b + 1 = 1).

Nunmehr folgt der transfinite Teil. Stützt man sich auf die von
Brouwer bestrittene Alternative, daß es entweder einen Redlichen
gibt oder daß alle Menschen unredlich sind, so kann man einen
Aristides finden, von welchem feststeht: ist irgendein Mensch
redlich, so ist Aristides redlich. Man wähle nämlich im ersten Fall
für Aristides einen der Redlichen, im zweiten einen beliebig
herausgegriffenen Menschen. Um aber für jede Eigenschaft,
nicht nur die „Redlichkeit“, für jede eine einzige Variable x frei
enthaltende Formel 𝔄 diesen Aristides konstruieren zu können,
fingieren wir einen göttlichen Automaten, der das leistet: er
liefert uns, wenn wir eine beliebige Eigenschaft 𝔄 in ihn hineinwerfen, jenes Individuum εₓ𝔄, das sicherlich die Eigenschaft 𝔄
besitzt, wenn es überhaupt ein derartiges Individuum gibt. εₓ ist
ein Integrationszeichen (aus Koketterie mit dem verhängnisvollen
Sprachgebrauch des Wörtleins „ist“ sowohl für die Kopula wie
für die Existenz verwenden auch wir für beide denselben Buchstaben ε; aber durch den an das existentiale ε angehängten Variablenindex wird die Verwechslung verhütet). Verfügten wir über
einen solchen Automaten, so wären wir aller Mühen überhoben,
die uns „es gibt“ und „alle“ bereiten; aber der Glaube an seine
Existenz ist natürlich der reinste Unsinn. Die Mathematik tut
jedoch so, als wäre er vorhanden. Das können wir in einer Axiomenregel zum Ausdruck bringen, und wenn die Anwendung
dieser Regel nicht zu Widersprüchen führt, so ist ihre Aufstellung
in der formalisierten Mathematik legitim. Die transfiniten logischen Axiomenregeln lauten nunmehr:

𝔄(b) → Σₓ𝔄(x).        Πₓ𝔄(x) → 𝔄(b).
Σₓ𝔄(x) → 𝔄(εₓ𝔄).     𝔄(εₓ𝔄̄) → Πₓ𝔄(x).

Die der zweiten Zeile, die wir in § 3 noch vermißten, erlauben uns,
aus Σₓ etwas zu folgern und von andern Formeln her auf Πₓ zu

[[pdf-page:0081 printed-page:80]]

schließen. Natürlich leisten sie nicht dieselben Dienste wie der
fingierte Automat; denn sie verschweigen für eine vorgelegte
Formel 𝔄, was εₓ𝔄 ist. Nur unter Umständen kann sich eine
Formel wie εₓ𝔄 = 1 als Endformel eines von den Axiomen ausgehenden Beweises ergeben.

Unter den arithmetischen Axiomen fehlt noch das Prinzip der vollständigen Induktion; es kann als transfinite arithmetische Axiomenregel gefaßt werden, welche zum Ausdruck bringt, daß eine Eigenschaft
𝔄, welche der Zahl 1 zukommt und für alle x von x auf x + 1 „sich
vererbt“, einer beliebigen Zahl zukommt. Sie wird jedoch überflüssig,
wie wir wissen, wenn es zulässig ist, zu jeder Eigenschaft 𝔄 ein neues
Ding y, die korrespondierende Menge einzuführen, derart, daß die Aussage „x ist Element von y“ mit dem Bestehen von 𝔄(x) gleichbedeutend
ist. Formuliert man dies als eine Axiomenregel, so stellt sich jedoch
alsbald heraus, daß ihre Anwendung unweigerlich zu einem formalen
Widerspruch führt, womit über das schrankenlose Recht zur Vergegenständlichung der Stab gebrochen ist. Für die Analysis genügt aber die
Beschränkung des Arguments x auf den Bereich der natürlichen Zahlen,
so daß wir die engere transfinite mengentheoretische Regel aufstellen:

ΣᵧΠₓ{Zx → ((x ε y) ⇔ 𝔄(x))},        (*)

wo B ⇔ C als Abkürzung für (B → C) & (C → B) dient. — Es scheint
für den Aufbau der Analysis nicht unerläßlich, aber wünschenswert zu
sein, das Axiom der Bestimmtheit hinzuzufügen, nach welchem zwei
Zahlmengen gleich sind, welche genau dieselben Elemente enthalten:

Πₓ{Zx → ((x ε b) ⇔ (x ε c))} → (b = c).

Ein mathematischer Beweis besteht darin, daß man sich
Axiome nach den angegebenen Regeln herstellt — diese Axiome
enthalten niemals freie Variable — und von ihnen aus durch Anwendung der schon in § 3 besprochenen Schlußregel des Syllogismus zunächst auf solche Axiome, weiterhin auf die bereits
gewonnenen Formeln zu immer neuen vordringt. Daß man nicht
a priori überblicken kann, zu was für „beweisbaren Formeln“
man durch dieses Spiel gelangt, liegt vor allem daran, daß durch
den Syllogismus aus zwei Formeln b und b → c eine neue c entsteht, welche kürzer ist als die zweite der Prämissen, daß im
Beweisspiel beständig Aufbau und Abbau miteinander wechseln.

[[pdf-page:0082 printed-page:81]]

Bis hierhin ist alles Spiel, nicht Erkenntnis. Das Spiel wird nun
aber in der „Metamathematik“, wie Hilbert sich ausdrückt, zum
Gegenstand der Erkenntnis gemacht: es soll erkannt werden, daß
man niemals zu einem Widerspruch gelangt. Ein solcher läge vor,
wenn von zwei in concreto durchgespielten Beweispartien die eine
mit einer Formel b endete, die andere mit der entgegengesetzten b̄.
Nur zur Gewinnung dieser einen Erkenntnis wird von Hilbert das
finite inhaltliche bedeutungserfüllte Denken benötigt, das auf keine
„Axiome“ gebracht werden kann. Insbesondere betätigt sich in
diesem inhaltlichen Denken ein anschaulich-finiter Schluß durch
vollständige Induktion, wie wir ihn analog vollzogen, als wir uns
zur Einsicht brachten (§ 4), daß in einer richtig gespielten Schachpartie niemals 10 Damen der gleichen Farbe auftreten können.

Eine der Regeln des elementaren Aussagekalküls, die entweder unter
den axiomatischen Regeln selbst auftritt oder leicht aus ihnen geschlossen
werden kann, lautet

b̄ → (b → c),        (*)

wo b und c beliebige geschlossene Formeln sind. Sei c eine willkürliche
derartige Formel, und nehmen wir an, eine gewisse Formel b und ihre
Negation b̄ seien bewiesen worden. Unter diesen Umständen führen
zwei syllogistische Schritte von (*) zunächst zu b → c und dann zu c.
Ist nun bekannt, daß der Formalismus nicht widerspruchsfrei ist, so
kann jede beliebige geschlossene Formel c bewiesen werden, und damit
verliert das Beweisspiel jedes Interesse. Die Widerspruchslosigkeit kann
also dadurch definiert werden, daß man sagt, die Formel ¯(1 = 1) sei
nicht beweisbar.

Das Axiomensystem kann beständig erweitert werden; aber
immer ist zu zeigen, daß dabei die Widerspruchslosigkeit aufrechterhalten bleibt. Insbesondere sind auch Definitionen in Gestalt
neuer Axiome oder Axiomenregeln einzuführen; z. B.

σ1 = 2,     σ(σb) = σ₂b.

Dies läßt sich besonders auf die rekursiven Definitionen von b + c,
b · c und anderen arithmetischen Operationen anwenden. Ein für
allemal läßt sich zeigen, daß eine zuvor bestehende Widerspruchslosigkeit erhalten bleibt, wenn Axiome dieser Art hinzugefügt

[[pdf-page:0083 printed-page:82]]

werden, die einfache oder rekursive Definitionen bedeuten¹).
Was die natürlichen Zahlen betrifft, kann der Hilbertsche Aufbau
im Gegensatz zum Brouwerschen verzichten auf jene „Möglichkeit
in infinitum“, die in § 6 als 3ter Schritt des konstruktiven Erkennens geschildert wurde; für Hilbert ist z. B. 10¹² ein „transfinites“
Symbol, das keine Zahl (Zeichen von der Gestalt σσ ... σ1) bedeutet. Geometrie und Physik können, sobald und soweit sie streng
axiomatisiert sind, angegliedert werden. Ja, Hilbert meint (Axiomatisches Denken, 1917): „Alles, was Gegenstand des wissenschaftlichen Denkens überhaupt sein kann, verfällt, sobald es zur
Bildung einer Theorie reif ist, der axiomatischen Methode und
damit mittelbar der Mathematik“).

Solange man die transfiniten Bestandteile außenvor läßt, ist der Beweis der Widerspruchslosigkeit (WB) leicht zu erbringen mittels „Wertung der Formeln“. Durch ein genau beschriebenes rekursives Verfahren
wird jeder Formel gemäß ihrer Entstehung einer der Werte W oder F
(wahr oder falsch) so verliehen, daß offenbarerweise die finiten Axiome
den Wert W bekommen und für die logischen Verknüpfungen die in § 3
angegebenen Regeln zur Wertbestimmung gelten. Solange das Transfinite
ausgeschaltet bleibt, ist also der Syllogismus, das deduktive Verfahren
ganz kraftlos; über die Wahrheit oder Falschheit des Vordersatzes b → c
wird hier nämlich immer erst entschieden, nachdem der Schlußsatz c
gewertet ist. — Auf diesem Wege ist der WB nicht mehr zu führen,
wenn die transfiniten Axiomregeln hinzugenommen werden. Hierin

1) Außerdem kann gezeigt werden, daß alle rekursiv definierbaren arithmetischen Operationen, sind die definierenden Axiome für b + c, b · c und
die entsprechenden Rechensymbole +, · erst einmal eingeführt, im Formalismus ausdrückbar sind. Vgl. z. B. Hilbert und Bernays, Grundlagen der
Mathematik, Bd. I, S. 412—422.

2) Aus einer wesentlich anderen Auffassung der Mathematik heraus
kommt Kant zu dem Ausspruch (Metaphysische Anfangsgründe der Naturwissenschaft, Vorrede): „daß in jeder besonderen Naturlehre nur so viel
eigentliche Wissenschaft angetroffen werden könne, als darin Mathematik
anzutreffen ist“. Im selben Sinne aber wie Hilbert erklärt Husserl (Logische
Untersuchungen I, § 71), mit besonderer Bezugnahme auf die mathematische
Logik, daß „die mathematische Form der Behandlung ... bei allen streng
entwickelten Theorien (man muß dies Wort allerdings auch im echten Sinne
nehmen) die einzig wissenschaftliche ist, die einzige, welche systematische
Geschlossenheit und Vollendung, welche Einsicht über alle möglichen Fragen
und die möglichen Formen ihrer Lösung bietet“.

[[pdf-page:0084 printed-page:83]]

macht sich bemerkbar, daß mit ihnen die Einsicht in wahr und falsch
aufhört. Gelungen ist aber auf einem mehr indirekten Wege der WB
für den Fall, daß die transfiniten logischen Axiome mitzugelassen werden
(v. Neumann, a. a. O.). Schon hier ist er recht verwickelt. Damit ist
sichergestellt, daß man keinen Widerspruch zu befürchten braucht, wenn
man — wie ich es in meiner Schrift „Das Kontinuum“ vom Jahre 1918
tat — die Reihe der natürlichen Zahlen als geschlossenen Inbegriff
seiender Gegenstände behandelt. Dagegen steht der WB noch aus für die
Einbeziehung der transfiniten mengentheoretischen Axiomregel (*),
welche den gleichen Standpunkt gegenüber dem „Inbegriff aller möglichen Zahlmengen“ zur Geltung bringen soll. Erst die Durchführung
des WB oder die Bemühungen darum decken uns die höchst verzwickte
logische Struktur der Mathematik auf, ein Gewirr von zirkelhaften
Rückverknüpfungen, von denen sich zunächst gar nicht übersehen läßt,
ob sie nicht zu eklatanten Widersprüchen führen.

Der geschilderte Symbolismus nimmt offenbar in verfeinerter Form
die Aufgabe von neuem in Angriff, welche sich Leibniz mit seiner „allgemeinen Charakteristik“ und ars combinatoria gestellt hatte. Aber geht
hier die alte Analysis nicht bloß noch als ein blutleeres Gespenst um?
Die Hilbertsche Mathematik mag ein hübsches Formelspiel sein, amüsanter selbst als das Schachspiel; aber was hat sie mit Erkenntnis zu tun,
da doch eingestandenermaßen ihre Formeln keine inhaltliche Bedeutung
haben sollen, derzufolge sie einsichtige Wahrheiten ausdrückten? Gegenstand der Mathematik sind nach Hilbert die konkreten Zeichen selber.
Es ist darum keine Ironie, wenn Brouwer sagt (Intuitionisme en formalisme, S. 7): Op de vraag, waar de wiskundige exactheid dan wel bestaat,
antwoorden beide partijen verschillend; de intuitionist zegt: in het menschelijk intellect, de formalist: op het papier. Auf die Frage, warum er
gerade diese Regeln aufstellt und warum ihm daran liegt, daß niemals
zwei beweisbare Formeln von der Gestalt b und b̄ vorkommen, muß der
konsequente Formalist die Antwort schuldig bleiben. An Philosophie,
Psychologie oder Anthropologie wird er uns, wie Brouwer meint, verweisen zur Rechtfertigung seines „lustgevoel van echtheidsovertuiging“
und seines Glaubens, daß das gewählte Axiomensystem sich besser auf
die Erfahrungswelt projizieren lasse als andere.

Die letzte Bemerkung erinnert uns daran, daß die Mathematik
sich in den Dienst der Naturwissenschaft zu stellen habe. Den Aussagen der theoretischen Physik eignet aber sicherlich nicht jener
Charakter, den Brouwer von den mathematischen verlangt, daß
nämlich jede ihren eigenen, restlos in der Anschauung vollzieh-

[[pdf-page:0085 printed-page:84]]

baren Sinn in sich trage; sondern dort steht, wenn es mit der Erfahrung konfrontiert wird, nur das System als Ganzes in Frage.
Wir müssen offenbar scharf scheiden zwischen phänomenalem
Wissen, anschauender Einsicht — wie sie z. B. in dem Urteil vorliegt: „Dies (mir in einem gegenwärtigen Akt der Wahrnehmung
gegebene) Blatt hat diese (mir in eben dieser Wahrnehmung gegebene) grüne Farbe“ — und theoretischer Gestaltung. Das Wissen
gibt Wahrheit, sein Organ ist das „Sehen“ im weitesten Sinne.
Die theoretische Gestaltung scheint nur an ein einziges streng
formulierbares Vernunftprinzip gebunden zu sein: Einstimmigkeit,
die hier in der Mathematik, wo die Sphäre des sinnlich Gegebenen
noch nicht berührt wird, lediglich in der Widerspruchslosigkeit
besteht; ihr Organ ist „das Schöpferische“. Im Zusammenhang
mit der Physik werden wir die Frage genauer erörtern müssen,
was außer der Einhelligkeit auf sie bestimmend wirkt. Die einsichtige Wahrheit ist dafür, wenn auch niemals letzte Norm, so
doch gewiß nicht gleichgültig. Hilbert selber äußert sich so darüber
(Über das Unendliche, Math. Annalen 95, S. 190): „Die Rolle,
die dem Unendlichen bleibt, ist ... lediglich die einer Idee — wenn
man, nach den Worten Kants, unter einer Idee einen Vernunftbegriff versteht, der alle Erfahrung übersteigt und durch den das
Konkrete im Sinne der Totalität ergänzt wird.“ Vielleicht findet
aber jene Frage eine vollständige Antwort nur durch den Hinweis
auf das in der Geschichte an uns sich vollziehende Leben des
Geistes, von dem meine eigene Existenz zwar ein wesentlicher,
aber kein autonomer Teil ist. Sie ist Licht und Finsternis, Zufälligkeit und Notwendigkeit, Sklaverei und Freiheit, und es kann
nicht erwartet werden, daß sich eine symbolische Konstruktion
der Welt je in einer endgültigen Form davon abheben würde.

LITERATUR
G. W. Leibniz, Philos. Schriften, ed. Gerhardt, VII, S. 184—189.
L. Couturat, Opuscules et fragments inédits de Leibniz. Paris 1902.
D. Hilbert, Neubegründung der Mathematik. Abhandlungen aus
dem Mathematischen Seminar der Universität Hamburg 1 (1922).
D. Hilbert, Die logischen Grundlagen der Mathematik. Math. Annalen 88 (1922).

[[pdf-page:0086 printed-page:85]]

D. Hilbert, Über das Unendliche. Math. Annalen 95 (1925).
D. Hilbert u. P. Bernays, Grundlagen der Mathematik. 2 Bände.
Berlin 1934—1939.
```

## Translation

Has no path remained by which to avoid such radical consequences? The resolve
to make this sacrifice is doubly hard in view of the historical fact that, in
set-theoretic analysis, despite the boldest and most varied combinations, a
complete security of inference and an evident unanimity of all results is found.
Hilbert undertakes, by the axiomatic method, to secure mathematics in its full
possession. To be sure, he too is convinced that the power of contentful thought
does not reach further than Brouwer claims; that it cannot support the
transfinite modes of inference in mathematics; that there is no justification
for all the transfinite statements of mathematics as contentful, evident truths.
What Hilbert wants to secure is not the truth, but the consistency of the old
analysis.

For this purpose he must formalize mathematics together with logic into a game
with signs proceeding according to fixed rules. These signs are not meant as
signs for something; signs of the latter sort Hilbert calls "communication
signs," and he uses German letters for them. The mathematical formulas made of
the former signs do not always admit a contentful interpretation. Alongside the
meaningful formulas there have appeared "ideal statements," introduced in order
to restore artificially the validity of the simple logical laws that, according
to Brouwer, had been lost in the transition to the infinite, just as ideal
numbers are introduced in algebraic number theory in order to force the validity
of simple divisibility theorems.

Four different kinds of signs occur. They are distinguished by the game rules
valid for them, analogously to pawns and knights in chess: constants, such as
`1`; variables, symbols for empty places such as `x, y, ...`; one-place and
many-place operations; and integrations. The most important one-place operations
are negation, the transition from a natural number to its successor, and `Z`,
read as "a is a natural number." The most important two-place operations are
implication, equality, and membership. Weyl treats all of these as operations:
`Z` generates from `a` the statement that `a` is a number, and equality generates
from `a` and `b` the statement that `a` equals `b`. For convenience in
formulating the rules, the operation signs may all be written before the
elements over which they extend, for example `ε(a, b)` instead of `a ε b`.

Integrations are `Σₓ` and `Πₓ`. They carry one or more variables as indices.
When an integration sign with index `x` is prefixed to a formula, the variable
`x` is bound at all places in the following formula and deprived of its
substitutability. New signs can be introduced continually in the development of
mathematics. What counts as a formula is explained recursively: a constant or
variable by itself is a formula; from one, two, or more already formed formulas,
a new one arises when an operation or integration sign of the corresponding
arity is written down and the relevant formulas are placed after it. The
finished formula then looks like a parthenogenetic family tree of symbols, from
which the grammatical structure of the formula, that is, the manner of its
recursive construction, can be read off unambiguously. One can also decide in
this way whether a given tree-like arrangement of symbols is a formula at all.

There is no need to have scruples about the fact that, in the formalism,
operations are applied without distinction to every possible thing. Anyone
anxious about such liberality may want to distinguish between "numerical" and
"factual" formulas by further recursive stipulations. But the proof game itself
starts from axioms. The axioms of finite logic are now treated as general rules
for producing axioms. Given two closed formulas `b` and `c`, for instance, the
formula `c → (b → c)` may be taken as an axiom. Then come the two axiom rules
of equality, mediating between logic and arithmetic: `b = b` and
`(b = c) → (𝔄(b) = 𝔄(c))`. Finally come specifically arithmetical finite rules,
where the constant `1` appears as the objective starting point of all
construction.

The transfinite part follows. If one relies on the alternative contested by
Brouwer, namely that either there is an honest person or all human beings are
dishonest, then one can find an Aristides of whom it is certain that, if any
human being is honest, Aristides is honest. To be able to construct such an
Aristides for every property, we feign a divine automaton. When any property
`𝔄` is thrown into it, it supplies the individual `εₓ𝔄`, which certainly has
the property `𝔄` if any such individual exists. This `εₓ` is an integration
sign. If we possessed such an automaton, we would be relieved of all the
difficulties caused by "there is" and "all," but belief in its existence is
obviously pure nonsense. Mathematics nevertheless proceeds as if it were there.
That can be expressed in an axiom rule, and if applying the rule does not lead
to contradictions, then its use in formalized mathematics is legitimate.

The second line of the transfinite logical axiom rules supplies what was still
missing in § 3: it allows one to infer something from an existential integration
and to infer a universal integration from other formulas. Of course these rules
do not do the same work as the feigned automaton, since for a given formula
`𝔄` they do not reveal what `εₓ𝔄` is. Only under certain circumstances can a
formula such as `εₓ𝔄 = 1` occur as the final formula of a proof proceeding from
the axioms.

Among the arithmetical axioms the principle of complete induction is still
missing. It can be understood as a transfinite arithmetical axiom rule saying
that a property `𝔄` which belongs to `1` and is inherited from `x` to `x + 1`
belongs to any arbitrary number. But it becomes superfluous if it is permissible
to introduce, for each property `𝔄`, a new thing `y`, the corresponding set,
such that the statement "x is an element of y" is equivalent to the holding of
`𝔄(x)`. If this is formulated as an axiom rule, it quickly turns out that its
application inevitably leads to a formal contradiction. The unrestricted right
to objectification is thereby condemned. For analysis, however, it is enough to
restrict the argument `x` to the natural numbers and introduce the narrower
transfinite set-theoretic rule. Weyl also notes that an axiom of determinacy,
according to which two number-sets are equal when they contain exactly the same
elements, is not indispensable but desirable.

A mathematical proof consists in producing axioms according to these rules and
then, from those axioms and later from the formulas already obtained, advancing
to new formulas by the syllogistic rule discussed in § 3. One cannot survey in
advance which "provable formulas" will be reached in this game, especially
because syllogism can move from `b` and `b → c` to a shorter formula `c`; in the
proof game, construction and dismantling constantly alternate.

Up to this point everything is game, not knowledge. The game now becomes an
object of knowledge in what Hilbert calls "metamathematics": it is to be known
that one never arrives at a contradiction. Such a contradiction would exist if
one concrete proof play ended with a formula `b` and another with the opposite
formula `b̄`. Only for gaining this one piece of knowledge does Hilbert require
finite, contentful, meaning-filled thought, which cannot itself be reduced to
"axioms." In particular, this contentful thought uses an intuitive finite
inference by complete induction, analogous to the insight that a correctly
played chess game can never contain ten queens of the same color.

If a formula and its negation have both been proved, then by the elementary rule
`b̄ → (b → c)` any arbitrary closed formula `c` can be proved. If the formalism
is known not to be consistent, the proof game loses all interest. Consistency
can therefore be defined by saying that the formula `¯(1 = 1)` is not provable.
The axiom system can be continually extended, but it must always be shown that
consistency is preserved. Definitions too are introduced in the form of new
axioms or axiom rules, and simple or recursive definitions can be added without
destroying a previously existing consistency.

For the natural numbers, Hilbert's construction can, unlike Brouwer's, dispense
with the "possibility in infinitum" described in § 6 as the third step of
constructive knowing. For Hilbert, `10¹²` is a "transfinite" symbol that denotes
no number, if a number is a sign of the form `σσ ... σ1`. Geometry and physics
can be attached once and insofar as they are strictly axiomatized. Hilbert even
holds that everything capable of becoming an object of scientific thought falls,
as soon as it is ripe for theory, under the axiomatic method and therefore
indirectly under mathematics.

So long as the transfinite components are left out, the proof of consistency is
easy by means of "valuation of formulas." A recursively described procedure
assigns to each formula, according to its genesis, one of the values true or
false. The finite axioms receive the value true, and the logical connectives obey
the rules of valuation from § 3. While the transfinite is excluded, the
syllogism, the deductive procedure, is therefore powerless: the truth or falsity
of the antecedent `b → c` is always decided only after the conclusion `c` has
been valued. This path no longer works when the transfinite axiom rules are
admitted. With them, insight into true and false stops.

The proof of consistency has succeeded indirectly for the case in which the
transfinite logical axioms are included. Even there it is quite intricate. This
secures that there is no contradiction to fear when one treats the series of
natural numbers as a closed aggregate of existing objects, as Weyl did in
`Das Kontinuum` in 1918. By contrast, the consistency proof is still lacking for
the inclusion of the transfinite set-theoretic axiom rule, which would apply the
same standpoint to the "aggregate of all possible number-sets." Only the
execution of the consistency proof, or the effort to execute it, reveals the
highly tangled logical structure of mathematics, a tangle of circular
back-connections whose possible contradictions cannot initially be surveyed.

This symbolism plainly takes up again, in refined form, the task Leibniz had
set himself with his universal characteristic and `ars combinatoria`. But does
the old analysis survive here only as a bloodless ghost? Hilbertian mathematics
may be a pretty formula game, more amusing even than chess, but what does it
have to do with knowledge, given that its formulas are not supposed to have
contentful meaning by which they express evident truths? For Hilbert, the
objects of mathematics are the concrete signs themselves. Brouwer's irony is
therefore not misplaced: to the question where mathematical exactness exists,
the intuitionist answers, in the human intellect; the formalist, on paper. The
consistent formalist must leave unanswered why he sets up these rules and why
he cares that formulas of the form `b` and `b̄` never both occur as provable.

This last point reminds us that mathematics must place itself in the service of
natural science. The statements of theoretical physics certainly do not have the
character Brouwer demands of mathematical statements, namely that each carries
within itself its own sense, completely executable in intuition. There, when
confronted with experience, only the system as a whole is at issue. We must
therefore sharply distinguish phenomenal knowledge, intuitive insight, from
theoretical formation. Knowledge gives truth; its organ is "seeing" in the
broadest sense. Theoretical formation appears to be bound to only one strictly
formulable rational principle: concordance, which here in mathematics, where the
sphere of the sensibly given is not yet touched, consists solely in consistency.
Its organ is "the creative." In connection with physics Weyl will have to ask
more exactly what, besides unanimity, determines it. Evident truth is not the
last norm for it, but it is certainly not indifferent. Perhaps the full answer
lies only in the life of spirit that takes place in history through us, of which
one's own existence is an essential but not autonomous part. It is light and
darkness, contingency and necessity, slavery and freedom; and no symbolic
construction of the world can be expected ever to detach itself from it in a
definitive form.

## Notes

Hilbert is not presented as simply undoing Brouwer. Weyl grants Hilbert the
diagnosis that contentful thought cannot justify transfinite mathematics as
evident truth. The rescue is therefore not a truth rescue, but a consistency
rescue.

The formal signs are explicitly not signs for something. This matters for the
larger repo pattern around sign, sense, and objectification: Hilbertian
formalism brackets reference and asks only whether the sign game can be played
without contradiction.

The `εₓ𝔄` automaton is Weyl's clearest image for the formalist fiction. It is
absurd as an existing power, but can be admitted as a formal rule if consistency
is preserved. This is exactly the threshold where symbolic mathematics replaces
insight with licensed play.

Weyl's criticism of unrestricted objectification sharpens rather than weakens
after section 8. The unrestricted set rule leads to contradiction; the restricted
rule for number-sets is mathematically useful but still awaits the relevant
consistency proof.

The final turn toward physics prevents a simple Brouwer victory. Natural science
does not consist of self-contained intuitive judgments; it tests systems as
wholes. Weyl's emerging position therefore requires a distinction between
phenomenal seeing and theoretical formation, with consistency as the minimal
mathematical form of concordance.

## Translation Decisions

- `Symbolische Mathematik` is `symbolic mathematics`
- `inhaltliches Denken` is `contentful thought`
- `Widerspruchslosigkeit` is `consistency`
- `Mitteilungszeichen` is `communication signs`
- `ideale Aussagen` is `ideal statements`
- `Integrationen` remains `integrations`, because Weyl uses it technically for
  `Σₓ` and `Πₓ`
- `Axiomenregel` is `axiom rule`
- `Wertung der Formeln` is `valuation of formulas`
- `Metamathematik` is `metamathematics`
- `phänomenales Wissen` is `phenomenal knowledge`
- `theoretische Gestaltung` is `theoretical formation`
- `Einstimmigkeit` is `concordance`; `Einhelligkeit` remains `unanimity`
- `das Schöpferische` is `the creative`

## Adversarial Check

The tempting simplification is to read this section as Weyl moving from
Brouwerian philosophy back to standard formalism. That is wrong. Weyl accepts
formalism as a powerful rescue strategy, but he repeatedly marks what it cannot
provide: truth, meaning, reasons for the rules, or a philosophical account of
why the game matters.

The opposite simplification is also wrong. Weyl does not merely dismiss Hilbert
as empty symbol manipulation. Formal consistency has real mathematical force,
and theoretical physics makes any purely intuitionistic account insufficient.
The batch should therefore be read as a pressure point, not a verdict: Brouwer
guards insight; Hilbert guards analysis; Weyl is trying to understand what kind
of knowing can legitimately use both.
