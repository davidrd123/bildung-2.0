# Part 004: Logical Inference

Third chapter-I batch. This subsection moves from definition to proof and
isolates the break between finite propositional procedure and transfinite logic
with quantifiers.

## Scope

- `3. Das logische Schließen`
- `LITERATUR` list before section 4
- printed pages `28-34`
- PDF/page-image pages `29-35`

## Source Anchors

- `source/cleaned/008-math-01-mathematische-logik-axiomatik.txt`
- `source/page-images/jpg-200/page-0029.jpg`
- `source/page-images/jpg-200/page-0030.jpg`
- `source/page-images/jpg-200/page-0031.jpg`
- `source/page-images/jpg-200/page-0032.jpg`
- `source/page-images/jpg-200/page-0033.jpg`
- `source/page-images/jpg-200/page-0034.jpg`
- `source/page-images/jpg-200/page-0035.jpg`

## Source Status

The active page range was visually checked against page images. The cleaned
German source was corrected for this batch before translation, especially:

- French accents and the `§ 4` Leibniz citation
- quotation marks around `„es gibt“`, `„alle“`, and `„analytisches“`
- implication arrows, negation bars, `∨`, `Σx`, `Πx`, and the Sheffer stroke
- both truth tables and the example formula `b → (a → b)`
- the quantifier axioms, the Cajus syllogism formulas, and blackletter
  placeholders `𝔄`, `𝔅`
- the section-local literature list before `4. Die axiomatische Methode`

## German

```text
3. Das logische Schließen

Nachdem das Definieren besprochen ist, kommen wir zum
Beweisen. Macht man einen geometrischen Satz zu einem hypothetischen Urteil, dessen Vordersatz aus den sämtlichen geometrischen Axiomen besteht, und ersetzt im Geiste die abkürzenden
Ausdrücke durch das, was sie laut Definition bedeuten, so entsteht
ein „formal gültiges“, „analytisches“ Urteil, dessen Wahrheit an
den Sinn der darin eingehenden Begriffe: Punkt, Gerade, Ebene,
liegt auf, zwischen, kongruent, in keiner Weise gebunden ist. In
der Logik des Schließens handelt es sich darum, diejenigen Urteilsstrukturen zu kennzeichnen, welche die formale Gültigkeit des
Urteils bedingen. Barbara, Baralipton usw. helfen dazu nicht viel.
Leibniz sah in der Lehre von den „argumens en forme“ une espèce
de Mathématique universelle, dont l’importance n’est pas assez
connue (Nouveaux Essais, L. IV, ch. XVII, § 4):

Denjenigen Teil der Logik, welcher ausschließlich mit den
logischen Verknüpfungen „nicht“, „und“, „oder“ operiert, wollen

[[pdf-page:0030 printed-page:29]]

wir als finite Logik der transfiniten gegenüberstellen, die sich darüber hinaus der Aussageoperationen „es gibt“ und „alle“ bedient.
Der Grund für diese Einteilung ist der folgende. Liegen vor mir
mehrere Stücke Kreide, so ist die Aussage „Alle diese Stücke sind
weiß“ nur eine Abkürzung für die Aussage: Dies Stück ist weiß &
dies Stück ist weiß & ... (indem ich eines nach dem andern vorzeige); ebenso ist „es gibt unter ihnen ein rotes“ ein abkürzender
Ausdruck für: Dieses ist rot ∨ dieses ist rot ∨ .... Aber nur bei
endlichen Mengen, deren Elemente aufgewiesen sind, ist eine derartige Interpretation möglich. Für unendliche Mengen liegt im
Sinne des „alle“ und „es gibt“ ein tiefes Problem verborgen,
welches das Zentrum der Mathematik, das eigentliche Geheimnis
des Unendlichen berührt; es wird sich uns im nachfolgenden
Kapitel entfalten. Die Dinge stehen hier analog wie bei dem Übergange von den endlichen zu den unendlichen Summen; der letzteren
Sinn ist an besondere Konvergenzbedingungen gebunden, und
man kann mit ihnen nicht in jeder Hinsicht so operieren wie mit
den endlichen.

Im Aussagekalkül ist es zweckmäßig, neben den Zeichen für
„nicht“, „und“, „oder“ noch das Symbol a → b, lies: aus a folgt b,
einzuführen. Es meint nichts anderes als ā ∨ b (a gilt nicht oder
b gilt) und bezeichnet keinen darüber hinausgehenden tieferen
Zusammenhang zwischen den Aussagen a und b.

Es würden übrigens zwei der vier Zeichen —, &, ∨, → genügen;
für den Aussagekalkül wählt man zweckmäßig → und —. Ja, man findet
sogar mit einem Zeichen a|b sein Auslangen, das die Unverträglichkeit
der Aussagen a und b bedeutet (ā ∨ b̄). An Stelle von

ā,     a → b,     a & b,     a ∨ b
kann man nämlich schreiben
a|a,   a|(b|b),   (a|b)|(a|b),   (a|a)|(b|b).

Doch wollen wir hier um der Übersichtlichkeit willen alle vier Zeichen
nebeneinander benutzen.

In einer finit-logischen Formel sind die Buchstaben („Aussagevariablen“), für welche beliebige Aussagen (Urteile ohne Leer-

[[pdf-page:0031 printed-page:30]]

stellen) eingesetzt werden dürfen, verknüpft durch jene vier Zeichen
—, &, ∨, →. Beispiel:

b → (a → b).

Es gibt eine allgemeine Vorschrift, nach der man einer solchen
Formel ihre formale Gültigkeit ansehen kann. Man erteile nämlich
den vorkommenden Buchstaben einen der Werte „wahr“ W oder
„falsch“ F in allen möglichen Kombinationen und bestimme jedesmal den Wert der gesamten Formel nach der folgenden Anweisung
für die Wertbestimmung der Verknüpfungen:

 a | ā
---+---
 W | F
 F | W

 a | b | a → b | a & b | a ∨ b
---+---+-------+-------+------
 W | W |   W   |   W   |   W
 W | F |   F   |   F   |   W
 F | W |   W   |   F   |   W
 F | F |   W   |   F   |   F

(Die Anzahl der durchzuprobierenden Kombinationen beträgt
z. B., wenn in die Formel 5 verschiedene Aussagevariable eingehen, 2⁵.) Ergibt sich als Wert der Formel in jedem Falle W, so
ist sie formal gültig. Diese Vorschrift, von der man sagen kann,
daß sie auf dem Satze des Widerspruchs und dem tertium non datur
basiert sei, will ich kurz „die finite Vorschrift“ nennen.

Beispiel: b → (a → b).

 a | b | a → b | b → (a → b)
---+---+-------+-------------
 W | W |   W   |      W
 W | F |   F   |      W
 F | W |   W   |      W
 F | F |   W   |      W

Auf dieser Stufe kann man es einer Behauptung also direkt ansehen, man kann es durch ein kombinatorisches Verfahren nach
festem Schema entscheiden, ob sie eine logische Folge gewisser
anderer Sätze ist, wenn Voraussetzung und Behauptung aus Ur-

[[pdf-page:0032 printed-page:31]]

teilen a, b, ... (gleichgültigen Sinnes) durch die vier Operationen
—, →, &, ∨ zusammengebaut sind.

Dies wird völlig anders, sobald „es gibt“ und „alle“ hinzutreten (mit ihnen halten auch die Leerstellen ihren Einzug in die
Formeln). Σx und Πx zwingen zur Konstruktion: wir stellen einige
formal gültige Grundformeln als logische Axiome auf und geben
eine Regel an, durch welche aus formal gültigen Urteilen neue
formal gültige Urteile hervorgehen. Die Regel ist keine andere als
die, nach welcher Logik auf alle theoretischen Wissenschaften
angewendet wird, der Syllogismus: Hast du ein Urteil 𝔄 und ein
Urteil 𝔄 → 𝔅, in welchem links von → das erste Urteil 𝔄 auftritt,
so stelle das Urteil 𝔅 hin. Alle Urteilsstrukturen, welche durch
wiederholte Anwendung dieser Regel, ausgehend von den logischen
Axiomen, gewonnen werden, haben analytischen Charakter, ohne
daß es möglich wäre, unabhängig von der konstruktiven Erzeugung
der einzelnen Strukturen ihre unendliche Mannigfaltigkeit deskriptiv zu kennzeichnen. Daher die Notwendigkeit des Beweises
Schritt für Schritt. So kann man mit einem von J. Fries in etwas
anderem Sinne geprägten Wort sprechen von einer „ursprünglichen Dunkelheit der Vernunft“. Wir haben die Wahrheit nicht,
sondern sie will durch Handeln gewonnen sein.

Galilei (Dialogo, Opere complete, Firenze 1842/56, Bd. I, S. 116)
spricht einen verbreiteten Gedanken aus, wenn er hierin den Unterschied
der menschlichen von der göttlichen Erkenntnis sieht: „Wir gehen mittels
schrittweiser Erörterung weiter von Schluß zu Schluß, während Er durch
bloße Anschauung begreift. So beginnen wir z. B., um die Kenntnis
einiger Eigenschaften des Kreises zu gewinnen, deren er unendlich viele
besitzt, bei einer der einfachsten, stellen sie als seine Definition hin und
gehen von ihr aus durch Schlüsse zu einer zweiten über, von dieser zu
einer dritten, sodann zu einer vierten usw. Der göttliche Intellekt hingegen begreift durch bloße Erfassung seines Wesens ohne zeitliches Erwägen die unendliche Fülle seiner Eigenschaften“ (intensive, der objektiven Gewißheit nach, aber stehe in jeder gewonnenen mathematischen
Einsicht der menschliche Intellekt dem göttlichen nicht nach).

Über „es gibt“ und „alle“, Σx und Πx, können wir zunächst
die beiden folgenden Axiome aufstellen, in denen für a(x) ein
beliebiges Urteilsschema mit der einen Leerstelle x gesetzt werden

[[pdf-page:0033 printed-page:32]]

darf und für c ein aufgewiesener Gegenstand der zugehörigen
Kategorie:

I. Πx a(x) → a(c);     II. a(c) → Σx a(x).

Sie gestatten uns nur, aus der Allheitsaussage etwas zu folgern,
aber sie schildern noch nicht, wie man von andern Urteilen her
jemals auf eine Allheitsaussage schließen kann. Für das „es gibt“
verhält es sich umgekehrt.

Das klassische Schulbeispiel eines Schlusses — (α) alle Menschen
sind sterblich, (β) Cajus ist ein Mensch; also (γ) Cajus ist sterblich —
vollzieht sich bei uns in mehreren Stufen. M und S mögen die Eigenschaften bedeuten, Mensch und sterblich zu sein, der Buchstabe c den
Cajus. Er liefert

(α) Πx(M(x) → S(x))
in Verbindung mit I:

Πx(M(x) → S(x)) → (M(c) → S(c))

durch die Schlußregel die Aussage:

M(c) → S(c).

Aus (β): M(c) und dem vorigen Urteil abermals durch die Schlußregel:

(γ) S(c).

So wie in (α), kann sich das → mit dem „alle“ zu einem allgemeinen
hypothetischen Satz verbinden, an sich enthält es die Idee der Allheit
nicht. Die Geltung eines allgemeinen Folgesatzes von der Form

Πx(a(x) → b(x))

kann natürlich verschiedene Fundamente haben. Wenn sie allein in den
logischen Axiomen liegen, drückt das Zeichen → eine rein logische
Folge aus; doch mag das Fundament auch in einem sachhaltigen Wesensgesetz, einem naturgesetzlich bestehenden Wirkungszusammenhang oder
einer empirischen Regelmäßigkeit liegen. Diese Bemerkung halte ich zur
Klärung der Frage für ausreichend, was das Verhältnis von Ursache und
Wirkung mit dem von Grund und Folge zu tun hat. Doch bleibt das
Zeichen → alledem gegenüber neutral.

[[pdf-page:0034 printed-page:33]]

Die finiten logischen Axiome findet man aufgezählt bei Ackermann,
Mathem. Annalen 93 (1924), S. 4; ferner in Grundlagen der Mathematik,
I, von D. Hilbert und P. Bernays, Berlin 1934, S. 66. Sie sind natürlich
so gebaut, daß sich ihre formale Gültigkeit aus der „finiten Vorschrift“
ablesen läßt. Man kann aber auch umgekehrt zeigen — doch erfordert
dies schon einen eigentlichen mathematischen, nicht ganz auf der Oberfläche liegenden Beweis —, daß alle nur die Zeichen —, →, &, ∨ enthaltenden logischen Formeln, welche nach der „finiten Vorschrift“ formal gültig sind, aus diesen wenigen Axiomen durch Substitution und
wiederholte Anwendung der Syllogismenregel gewonnen werden können;
daher ist die Aufzählung vollständig. Die transfinite Axiomgruppe aber,
von der wir bis jetzt nur die beiden Axiome I. und II. kennen, bleibt
ergänzungsbedürftig.

Mit Hilfe der Schlußregel kann man aus den logischen Axiomen neue
abgeleitete Beweisregeln gewinnen. Jedes formal gültige Urteil von der
Bauart 𝔄 → 𝔅 (wo 𝔄 und 𝔅 aus den Aussagevariablen, den unbestimmten Urteilen a, b, ... durch die logischen Zeichen zusammengebaut sind)
führt nämlich mit Hilfe des Syllogismus zu der Regel: Hast du ein Urteil
von der Gestalt 𝔄, so kannst du daraufhin das entsprechende Urteil von
der Gestalt 𝔅 hinstellen. Umgekehrt hat auch die Syllogismusregel ihren
Repräsentanten unter den logischen Formeln:

a → ((a → b) → b).

Dennoch kommt man, da Konstruieren Handeln heißt, mit Formeln
allein nicht aus, man braucht durchaus eine praktisch auszuübende
Schlußregel. Das ist wohl der richtige Kern der Ansicht vom normativen
Charakter der Logik.

Kants Unterscheidung von analytischen und synthetischen Urteilen
(Kritik der reinen Vernunft, Einleitung) ist so unklar gefaßt, daß ein
Vergleich mit dem scharfen Begriff der formalen Gültigkeit in der mathematischen Logik — der letzten Endes durch die logischen Axiome
statuiert wird — nicht gut möglich ist. Hingegen deckt sich mit ihm die
Husserlsche Definition (Logische Untersuchungen, Bd. II, 2. Aufl.,
S. 254): „Analytische Gesetze sind unbedingt allgemeine Sätze, welche
keine anderen Begriffe als formale enthalten. Den analytischen Gesetzen
stehen gegenüber ihre Besonderungen, welche durch Einführung sachhaltiger Begriffe und ev. individuelle Existenz setzender Gedanken erwachsen. Wie überhaupt Besonderungen von Gesetzen Notwendigkeiten
ergeben, so Besonderungen analytischer Gesetze analytische Notwendigkeiten.“

[[pdf-page:0035 printed-page:34]]

LITERATUR

G. W. Leibniz, Philosophische Schriften, VII, S. 43—247, 292—301.
Mathematische Schriften, VII, S. 49—76, 203—216.

L. Couturat, La logique de Leibniz. Paris 1901. Opuscules et fragments inédits de Leibniz. Paris 1903.

G. Boole, The Mathematical Analysis of Logic. London und Cambridge 1847. An Investigation of the Laws of Thought. London 1854.
Neudruck in: Collected Logical Works, Chicago und London 1916.

E. Schröder, Vorlesungen über die Algebra der Logik. 3 Bände,
Leipzig 1890—1895.

A. N. Whitehead und B. Russell, Principia Mathematica. 3 Bände,
Cambridge 1910—1913; 2. Aufl. 1925—1927.

B. Russell, The Principles of Mathematics. Cambridge 1903; 2. Aufl.
New York 1938. Introduction to Mathematical Philosophy. 2. Aufl.
London 1920.

L. Wittgenstein, Tractatus Logico-Philosophicus, New York und
London 1922 und Frankfurt/M. 1960.

C. I. Lewis und C. H. Langford, Symbolic Logic. New York 1932.

A. Tarski, Introduction to Logic. New York 1941.

H. Freudenthal, Einführung in die Sprache der Logik. München 1965.
```

## Draft

```text
3. Logical Inference

Having discussed defining, we come to proving. If one turns a geometrical
theorem into a hypothetical judgment whose antecedent consists of all the
geometrical axioms, and if in thought one replaces the abbreviating expressions
by what they mean according to definition, then there arises a "formally valid,"
"analytic" judgment whose truth is in no way bound to the sense of the concepts
entering into it: point, line, plane, lies on, between, congruent. In the logic
of inference the issue is to characterize those judgment-structures that
condition the formal validity of the judgment. Barbara, Baralipton, and the
like do not help much with this. In the doctrine of "arguments in form,"
Leibniz saw a kind of universal mathematics whose importance is not sufficiently
known.

That part of logic which operates exclusively with the logical connectives
"not," "and," and "or" we will set over against transfinite logic as finite
logic; transfinite logic also makes use of the statement-operations "there
exists" and "all." The reason for this division is the following. If several
pieces of chalk lie before me, then the statement "All these pieces are white"
is only an abbreviation for the statement: this piece is white & this piece is
white & ... as I point to one after another. Likewise, "there exists among them
a red one" is an abbreviating expression for: this one is red ∨ this one is red
∨ .... But only with finite sets whose elements are exhibited is such an
interpretation possible. For infinite sets, a deep problem lies hidden in the
sense of "all" and "there exists," a problem that touches the center of
mathematics, the proper secret of the infinite; it will unfold for us in the
following chapter. Things stand here analogously to the transition from finite
to infinite sums; the sense of the latter is bound to special convergence
conditions, and one cannot operate with them in every respect as with finite
sums.

In the propositional calculus it is useful, alongside the signs for "not,"
"and," and "or," also to introduce the symbol a → b, read: from a follows b. It
means nothing other than ā ∨ b (a does not hold or b holds), and it designates
no deeper connection beyond that between the statements a and b.

Incidentally, two of the four signs —, &, ∨, → would suffice; for the
propositional calculus one conveniently chooses → and —. Indeed, one can even
make do with a single sign a|b, which means the incompatibility of the
statements a and b (ā ∨ b̄). Namely, in place of

ā,     a → b,     a & b,     a ∨ b
one can write
a|a,   a|(b|b),   (a|b)|(a|b),   (a|a)|(b|b).

For the sake of clarity, however, we will use all four signs alongside one
another here.

In a finite-logical formula, the letters ("statement-variables"), for which any
statements whatever may be inserted (judgments without empty places), are linked
by those four signs —, &, ∨, →. Example:

b → (a → b).

There is a general prescription by which one can see the formal validity of such
a formula. Namely, one assigns to the letters that occur one of the values
"true" W or "false" F in all possible combinations, and each time determines the
value of the whole formula according to the following instruction for the value
determination of the connectives:

 a | ā
---+---
 W | F
 F | W

 a | b | a → b | a & b | a ∨ b
---+---+-------+-------+------
 W | W |   W   |   W   |   W
 W | F |   F   |   F   |   W
 F | W |   W   |   F   |   W
 F | F |   W   |   F   |   F

The number of combinations to be tried through is, for example, 2⁵ when 5
different statement-variables enter into the formula. If the value of the
formula comes out W in every case, then it is formally valid. This prescription,
which one can say is based on the principle of contradiction and the tertium non
datur, I will call "the finite prescription" for short.

Example: b → (a → b).

 a | b | a → b | b → (a → b)
---+---+-------+-------------
 W | W |   W   |      W
 W | F |   F   |      W
 F | W |   W   |      W
 F | F |   W   |      W

At this level, then, one can see it directly in an assertion; one can decide by
a combinatorial procedure according to a fixed schema whether it is a logical
consequence of certain other propositions, provided that premise and assertion
are built up out of judgments a, b, ... of indifferent sense by the four
operations —, →, &, ∨.

This becomes entirely different as soon as "there exists" and "all" enter; with
them the empty places also make their entry into the formulas. Σx and Πx compel
construction: we set up some formally valid basic formulas as logical axioms,
and give a rule by which new formally valid judgments proceed from formally
valid judgments. The rule is none other than the one according to which logic is
applied to all theoretical sciences, the syllogism: if you have a judgment 𝔄
and a judgment 𝔄 → 𝔅, in which the first judgment 𝔄 occurs to the left of →,
then set down the judgment 𝔅. All judgment-structures that are obtained by
repeated application of this rule, starting from the logical axioms, have an
analytic character, without its being possible to characterize their infinite
manifold descriptively independently of the constructive generation of the
individual structures. Hence the necessity of proof step by step. Thus one can,
with a word coined by J. Fries in a somewhat different sense, speak of an
"originary darkness of reason." We do not possess the truth; rather, it wants to
be won through action.

Galileo gives voice to a widespread thought when he sees in this the difference
between human and divine knowledge: "We proceed by stepwise discussion from
inference to inference, while He comprehends by mere intuition. Thus, for
example, in order to gain knowledge of some properties of the circle, of which
it possesses infinitely many, we begin with one of the simplest, set it down as
its definition, and from it pass by inferences to a second, from this to a
third, then to a fourth, and so on. The divine intellect, by contrast, by mere
grasp of its essence and without temporal deliberation comprehends the infinite
fullness of its properties" (intensively, that is, in objective certainty; but
in each mathematical insight gained, the human intellect does not fall behind
the divine).

Concerning "there exists" and "all," Σx and Πx, we can first set up the
following two axioms, in which for a(x) any judgment-schema with the one empty
place x may be put, and for c an exhibited object of the corresponding category:

I. Πx a(x) → a(c);     II. a(c) → Σx a(x).

They allow us only to infer something from the statement of allness; they do not
yet describe how one can ever infer a statement of allness from other judgments.
For "there exists" the situation is reversed.

The classical school example of an inference, (α) all human beings are mortal,
(β) Cajus is a human being, therefore (γ) Cajus is mortal, takes place for us in
several stages. Let M and S mean the properties of being human and being mortal,
and let the letter c stand for Cajus. It yields

(α) Πx(M(x) → S(x))
in conjunction with I:

Πx(M(x) → S(x)) → (M(c) → S(c))

through the rule of inference, the statement:

M(c) → S(c).

From (β): M(c), and from the preceding judgment once again through the rule of
inference:

(γ) S(c).

As in (α), the → can combine with "all" into a general hypothetical proposition;
in itself it does not contain the idea of allness. The validity of a general
consequence-proposition of the form

Πx(a(x) → b(x))

can of course have various foundations. If they lie solely in the logical
axioms, then the sign → expresses a purely logical consequence; but the
foundation may also lie in a substantive essential law, a law-governed causal
connection, or an empirical regularity. I take this remark to be sufficient for
clarifying the question of what the relation of cause and effect has to do with
that of ground and consequence. The sign →, however, remains neutral with
respect to all this.

The finite logical axioms are listed in Ackermann, Mathematische Annalen 93
(1924), p. 4; also in Foundations of Mathematics I, by D. Hilbert and P.
Bernays, Berlin 1934, p. 66. They are of course so constructed that their formal
validity can be read off from the "finite prescription." Conversely, however,
one can also show, though this already requires a proper mathematical proof, one
not lying entirely on the surface, that all logical formulas containing only the
signs —, →, &, ∨ that are formally valid according to the "finite prescription"
can be obtained from these few axioms by substitution and repeated application
of the syllogism rule; hence the enumeration is complete. The transfinite axiom
group, however, of which we so far know only the two axioms I and II, remains in
need of supplementation.

With the help of the rule of inference, one can obtain new derived proof rules
from the logical axioms. Every formally valid judgment of the construction 𝔄 →
𝔅, where 𝔄 and 𝔅 are built out of the statement-variables, the indeterminate
judgments a, b, ..., by the logical signs, leads with the help of the syllogism
to the rule: if you have a judgment of the form 𝔄, then on that basis you can
set down the corresponding judgment of the form 𝔅. Conversely, the syllogism
rule also has its representative among the logical formulas:

a → ((a → b) → b).

Nevertheless, because constructing means acting, formulas alone do not suffice;
one absolutely needs a practically exercisable rule of inference. This is
probably the correct kernel of the view that logic has a normative character.

Kant's distinction between analytic and synthetic judgments (Critique of Pure
Reason, Introduction) is formulated so unclearly that comparison with the sharp
concept of formal validity in mathematical logic, which is ultimately instituted
by the logical axioms, is hardly possible. By contrast, Husserl's definition
agrees with it: "Analytic laws are unconditionally general propositions that
contain no concepts other than formal ones. Opposed to analytic laws are their
particularizations, which arise through the introduction of substantive concepts
and possibly thoughts positing individual existence. Just as particularizations
of laws in general yield necessities, so particularizations of analytic laws
yield analytic necessities."

Literature

G. W. Leibniz, Philosophische Schriften, VII, pp. 43-247, 292-301.
Mathematische Schriften, VII, pp. 49-76, 203-216.

L. Couturat, La logique de Leibniz. Paris 1901. Opuscules et fragments inédits
de Leibniz. Paris 1903.

G. Boole, The Mathematical Analysis of Logic. London and Cambridge 1847. An
Investigation of the Laws of Thought. London 1854. Reprint in: Collected
Logical Works, Chicago and London 1916.

E. Schröder, Vorlesungen über die Algebra der Logik. 3 volumes, Leipzig
1890-1895.

A. N. Whitehead and B. Russell, Principia Mathematica. 3 volumes, Cambridge
1910-1913; 2nd ed. 1925-1927.

B. Russell, The Principles of Mathematics. Cambridge 1903; 2nd ed. New York
1938. Introduction to Mathematical Philosophy. 2nd ed. London 1920.

L. Wittgenstein, Tractatus Logico-Philosophicus, New York and London 1922 and
Frankfurt/M. 1960.

C. I. Lewis and C. H. Langford, Symbolic Logic. New York 1932.

A. Tarski, Introduction to Logic. New York 1941.

H. Freudenthal, Einführung in die Sprache der Logik. Munich 1965.
```

## Notes

- `das logische Schließen` is rendered as `logical inference`. `Concluding`
  would be more literal, but the whole passage concerns proof and inference
  rules.
- `formale Gültigkeit` is `formal validity`; this is the section's sharp
  contrast with Kant's unclear analytic/synthetic distinction.
- `finite Vorschrift` is `finite prescription`, not simply `finite rule`,
  because Weyl means a mechanical truth-table procedure for recognizing formal
  validity in the finite propositional case.
- `Σx und Πx zwingen zur Konstruktion` is the hinge: quantifiers destroy the
  direct finite inspection procedure and force proof by constructive generation.
- `ursprüngliche Dunkelheit der Vernunft` is left as `originary darkness of
  reason`; it names the fact that truth is not possessed by immediate survey but
  must be won through action.
- `Grund und Folge` is translated as `ground and consequence` to keep it
  distinct from cause/effect, which Weyl explicitly says the implication sign
  does not itself encode.
