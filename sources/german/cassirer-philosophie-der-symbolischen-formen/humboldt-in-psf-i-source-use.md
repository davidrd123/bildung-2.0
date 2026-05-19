# Humboldt in PSF I — Source-Use Note

**Status:** Source-scaffold note. This records Cassirer's Humboldt source base
inside *Philosophie der symbolischen Formen* I. It does not promote PSF,
Humboldt, or the Cassirer-Humboldt-Kant line to a `texts/` campaign.

## Why This Exists

The PSF I split exposed a useful bibliographic fact: Cassirer's Humboldt is not
just the famous singular *Ueber die Verschiedenheit des menschlichen
Sprachbaues*. The PSF I apparatus shows Cassirer using a wider Humboldt source
base, including the 1838 Buschmann-edited Kawi volume, the plural
*Verschiedenheiten* essay, the Chinese grammar pieces, the *Dualis* essay, and
the Wolf letter.

This matters for later Humboldt, Chomsky, and Kant-facing work because it makes
the source-base asymmetry concrete. Cassirer is reading Humboldt through a
broader nineteenth-century philological and comparative-linguistic surface than
a later "Humboldt as universal grammar precursor" story usually preserves.

## Apparatus Evidence

Primary local evidence:

- PSF I Schriftenregister:
  `source/vol1-die-sprache/920-schriftenregister.txt`
- PSF I Personenregister:
  `source/vol1-die-sprache/930-personenregister.txt`

Verification pass:

- The Humboldt Schriftenregister cluster was checked locally against
  `source/vol1-die-sprache/920-schriftenregister.txt`, especially the Humboldt
  entries around lines 324-363.
- The Humboldt Personenregister entry was checked locally against
  `source/vol1-die-sprache/930-personenregister.txt`, lines 3-9.
- Chapter-split search confirms that the named Kawi references occur in the
  chapter II/III surfaces, especially
  `source/vol1-die-sprache/030-kapitel-ii-sprache-in-der-phase-des-sinnlichen-ausdrucks.txt`
  and
  `source/vol1-die-sprache/040-kapitel-iii-sprache-in-der-phase-des-anschaulichen-ausdrucks.txt`.

The Personenregister gives Humboldt as a continuous interlocutor across PSF I:
`VIII f., 23, 79, 86, 97-106, 117-119, 140-142, 146, 152 f., 163 f., 166-168,
173 f., 193, 196 f., 202, 206, 209, 213, 216, 219 f., 222, 225 f., 228, 234,
239 f., 244-248, 255-257, 261 f., 275 f., 280 f., 283, 289, 291, 299`.

That distribution means Humboldt is not chapter-bounded. He is present in the
preface, introduction, chapter I, and the main constructive language chapters.

## Humboldt Works Cassirer Uses

From the PSF I Schriftenregister:

| Work | Cassirer PSF I pages | Immediate note |
| --- | --- | --- |
| *Ankündigung einer Schrift über die Vaskische Sprache und Nation* | 99 | Minor but real Humboldt source in the chapter I cluster. |
| Brief an F. A. Wolf, 16 June 1804 | 98 | Used at the opening of Cassirer's Humboldt section. |
| *Grundzüge des allgemeinen Sprachtypus* | 102 | Part of the chapter I Humboldt/Kant/form cluster. |
| *Lettre à Monsieur Abel-Rémusat... langue Chinoise* | 106 | French Chinese-grammar essay; important non-standalone Humboldt surface. |
| *Ueber das vergleichende Sprachstudium...* | 100, 102 | Academy-address comparative-language frame. |
| *Ueber den Dualis* | 168, 196 f., 206, 213 | Reappears in the intuitive-expression chapter. |
| *Ueber den grammatischen Bau der Chinesischen Sprache* | 106 | Paired with the Abel-Rémusat letter in chapter I. |
| *Über die Kawi-Sprache auf der Insel Java*, Bd. II, Buschmann ed., 1838 | 140 f., 146, 152, 163, 174, 193, 202, 209, 216, 220, 222, 239 f., 246, 248 | The strongest evidence that Cassirer works with the Kawi descriptive material, not only the standalone *Verschiedenheit*. |
| *Ueber die Verschiedenheit des menschlichen Sprachbaues...* (singular) | 23, 98, 102-105, 140, 142, 174, 213, 226, 239, 245, 256, 262, 276, 280, 283, 289, 291, 299 | The famous standalone / GS VII surface. |
| *Ueber die Verschiedenheiten des menschlichen Sprachbaues* (plural) | 100 f., 206, 257 | Distinct earlier essay in GS VI/1; do not collapse into the singular title. |
| *Ueber die Verwandtschaft der Ortsadverbien mit dem Pronomen in einigen Sprachen* | 153, 164, 166, 213, 216, 225 | Important for pronoun/deixis/adverbial relation surfaces in chapter III. |

## Local Shelf Routing

Use this routing when moving from Cassirer citations to Humboldt source work:

| Cassirer source object | Local route | Status |
| --- | --- | --- |
| *Über die Kawi-Sprache auf der Insel Java*, Bd. II, Buschmann ed., 1838 | `sources/german/humboldt-kawi-sprache/` | Landed. This is the direct shelf for Cassirer's named Kawi Bd. II citations. |
| *Ueber die Verschiedenheit des menschlichen Sprachbaues...* (singular) | `sources/german/humboldt-verschiedenheit-sprachbau/` | Landed as a Pott 1876 witness, with a targeted raw Ergon/Energeia tranche at `source/raw/008a-ergon-energeia-pdf-061-062.txt`. Useful local witness, but Cassirer's register cites the GS VII / 1907 form, so edition identity should stay visible. |
| *Ueber die Verschiedenheiten des menschlichen Sprachbaues* (plural) | `sources/german/humboldt-verschiedenheiten-sprachbau-gs-vi1/` | Landed as a clearly marked GS VI/1 witness. Do not fold into the singular shelf. |
| *Ueber den Dualis* | `sources/german/humboldt-verschiedenheiten-sprachbau-gs-vi1/` | Landed as a GS VI/1 support text with raw extract `source/raw/005-ueber-den-dualis-pdf-014-040.txt`. |
| *Ueber die Verwandtschaft der Ortsadverbien mit dem Pronomen...* | none yet | Pull as GS VI/1 support if deixis/pronoun/adverb pressure becomes active. |
| *Lettre à Monsieur Abel-Rémusat... langue Chinoise* | `sources/german/humboldt-chinesische-sprache-gs-v/` | Landed as a GS V witness with raw extract `source/raw/010-lettre-a-abel-remusat-pdf-264-318.txt`. |
| *Ueber den grammatischen Bau der Chinesischen Sprache* | `sources/german/humboldt-chinesische-sprache-gs-v/` | Landed with the Abel-Rémusat letter as a GS V Chinese-grammar pair. Raw extract: `source/raw/020-grammatischer-bau-der-chinesischen-sprache-pdf-319-334.txt`. |
| *Grundzüge des allgemeinen Sprachtypus* | `sources/german/humboldt-chinesische-sprache-gs-v/` | Landed from the same GS V witness. Raw extract: `source/raw/030-grundzuege-des-allgemeinen-sprachtypus-pdf-374-485.txt`. |
| *Ueber das vergleichende Sprachstudium...* | `sources/german/humboldt-vergleichendes-sprachstudium-gs-iv/` | Landed as a GS IV support text with raw extract `source/raw/010-ueber-das-vergleichende-sprachstudium-pdf-011-044.txt`. |
| Brief an F. A. Wolf, 16 June 1804 | none yet | Low-volume support source for the chapter I Humboldt opening. |
| *Ankündigung einer Schrift über die Vaskische Sprache und Nation* | none yet | Minor support source; not a current pull priority. |

Cassirer's own *Die Kantischen Elemente in Wilhelm von Humboldts
Sprachphilosophie* is now represented as an acquisition target at
`sources/german/cassirer-kantische-elemente-humboldt-sprachphilosophie/`.
No full-text witness has landed there yet.

## Current Working Verdict

For the Cratylus / Ergon-Energeia / Humboldt comparison, the current shelves
are enough to begin source-near work. The load-bearing Humboldt passage is the
targeted section 8 working tranche in
`sources/german/humboldt-verschiedenheit-sprachbau/source/normalized/008a-ergon-energeia-pdf-061-062.txt`.
That passage can be pressed directly against Cratylus 388b-c
(`onoma` as teaching instrument) and 389-390 (the natural lawgiver frame),
without waiting for broader Humboldt intake.

For fuller PSF I coverage, the main unlanded Humboldt support still named by
the Schriftenregister is *Ueber die Verwandtschaft der Ortsadverbien mit dem
Pronomen in einigen Sprachen*, which carries repeated chapter III citation
pressure. The Wolf letter and *Ankuendigung einer Schrift ueber die Vaskische
Sprache und Nation* remain smaller chapter I support targets. Cassirer's own
*Die Kantischen Elemente in Wilhelm von Humboldts Sprachphilosophie* remains a
separate Cassirer-Humboldt-Kant acquisition target, not a Humboldt-source gap.

## Singular vs. Plural Guardrail

Keep these distinct:

- **Singular:** *Ueber die Verschiedenheit des menschlichen Sprachbaues und
  ihren Einfluss auf die geistige Entwicklung des Menschengeschlechts*.
  Cassirer cites the GS VII / 1907 form at PSF I pp. 23, 98, 102-105, 140,
  142, 174, 213, 226, 239, 245, 256, 262, 276, 280, 283, 289, 291, 299.
- **Plural:** *Ueber die Verschiedenheiten des menschlichen Sprachbaues*.
  Cassirer cites the GS VI/1 essay at PSF I pp. 100 f., 206, 257.

The title difference is small enough to disappear in chat summaries and search
results, but Cassirer uses both as distinct textual objects.

## Kawi Bd. II Guardrail

Cassirer's PSF I Schriftenregister names:

- *Über die Kawi-Sprache auf der Insel Java*, Bd. II: *Fortsetzung der
  Kawi-Sprache; Malayischer Sprachstamm im Allgemeinen und dessen westlicher
  Zweig*, edited by Johann Carl Eduard Buschmann, Berlin 1838.

The current local Kawi shelf is:

- `sources/german/humboldt-kawi-sprache/`
- witness id: `ia-1838-kawi-band2-google-ia`
- tracked source surfaces:
  - `source/full/kawi-sprache-band2.txt`
  - `source/raw/010-zweites-buch-ueber-die-kawi-sprache-pdf-042-246.txt`
  - `source/raw/011-kawi-book-opening-pdf-042-047.txt`
  - `source/normalized/011a-kawi-language-opening-pdf-044.txt`
  - `source/raw/023-feststellung-des-begriffs-des-kawi-pdf-231-246.txt`
  - `source/normalized/023a-feststellung-des-begriffs-des-kawi-opening-pdf-231-237.txt`
  - `source/normalized/020a-raumverba-praepositionen-pdf-207-209.txt`
  - `source/raw/020-drittes-buch-erster-abschnitt-stammverwandtschaft-pdf-248-336.txt`
  - `source/raw/030-drittes-buch-zweiter-abschnitt-westlicher-zweig-pdf-337-485.txt`
  - `source/normalized/030a-tagalisch-sa-ortsbegriff-pdf-402-403.txt`

The two smaller Kawi raw tranches now have bounded working normalizations:
one for the opening page and one for the opening movement of §23 where Humboldt
explicitly fixes the concept of Kawi. These are not whole-section
normalizations.

The local Pott shelf at `sources/german/humboldt-verschiedenheit-sprachbau/`
is a different working witness: the 1876 Pott edition of *Ueber die
Verschiedenheit des menschlichen Sprachbaues*, with Volume 2 now serving as
the primary Humboldt running-text witness for that edition.

Do not collapse these witnesses. The 1876 Pott Band 2 material may overlap
with, excerpt, reframe, or transmit material adjacent to the 1838 Kawi volume,
but that relation still needs verification. Until checked, use:

- `ia-1876-pott-band2` as the current local Humboldt *Verschiedenheit* witness
- `ia-1838-kawi-band2-google-ia` as Cassirer's named Kawi Bd. II citation
  witness

## PSF I Chapter Pressure

The direct Kawi Bd. II page references sit mainly in PSF I chapter III, with a
small lead-in at the end of chapter II:

- PSF I chapter II begins at p. 122 and runs through p. 146.
- PSF I chapter III begins at p. 147 and runs through p. 248.
- PSF I chapter IV begins at p. 249.

So the Kawi Bd. II citation sequence `140 f., 146, 152, 163, 174, 193, 202,
209, 216, 220, 222, 239 f., 246, 248` maps to late chapter II and especially
chapter III, not chapter IV.

Working implication:

- Open `source/vol1-die-sprache/030-kapitel-ii-sprache-in-der-phase-des-sinnlichen-ausdrucks.txt`
  for the lead-in citations.
- Open `source/vol1-die-sprache/040-kapitel-iii-sprache-in-der-phase-des-anschaulichen-ausdrucks.txt`
  for the main Kawi/Humboldt pressure.
- Use chapter IV and chapter V for broader Humboldt form, class, relation, and
  predicative-synthesis pressure, but do not represent them as the center of
  the Kawi Bd. II citation chain.

## PSF I Chapter III Kawi Pressure Map

Local check on 2026-05-19 against
`source/vol1-die-sprache/040-kapitel-iii-sprache-in-der-phase-des-anschaulichen-ausdrucks.txt`:
Kawi paths below are relative to `sources/german/humboldt-kawi-sprache/`.
For compactness, `raw/010`, `raw/020`, `raw/030`, `norm/020a`, and
`norm/030a` name:
`source/raw/010-zweites-buch-ueber-die-kawi-sprache-pdf-042-246.txt`,
`source/raw/020-drittes-buch-erster-abschnitt-stammverwandtschaft-pdf-248-336.txt`,
`source/raw/030-drittes-buch-zweiter-abschnitt-westlicher-zweig-pdf-337-485.txt`,
`source/normalized/020a-raumverba-praepositionen-pdf-207-209.txt`, and
`source/normalized/030a-tagalisch-sa-ortsbegriff-pdf-402-403.txt`.

| PSF I chapter III locus | Cassirer theme | Kawi citation | Local Kawi route | Working result |
| --- | --- | --- | --- | --- |
| lines 190-218 / PSF pp. 152-153 | Demonstratives and spatial near/far deixis | Kawi, p. 153 | `raw/010` | Kawi enters the chapter at the point where pointing becomes a spiritual/structuring act, not mere natural sound. |
| lines 611-636 / PSF pp. 163-164 | Space-verbs and the shift from static spatial substance to action/relation | Kawi, pp. 164 ff., 341 | `norm/020a` and `norm/030a` | This is the strongest chapter III bridge to the Ergon/Energeia pressure: spatial relations become "fluid" when carried by verbs rather than substantives. |
| lines 1011-1047 / PSF p. 174 | Time-expression and the limits of verb-centered temporality | Kawi, p. 286 | `raw/020` | Cassirer uses the Kawi volume to show that temporal relation may attach to nominal forms; time is not already identical with the modern finite verb. |
| lines 1768-1777, 2108-2124, 2397-2405 / PSF pp. 193, 202, 209 | Numeratives, inclusive/exclusive plural, and verbal plurality | Kawi, pp. 269 ff., 317, 376 ff., 39 | `raw/020` and `raw/030` | Number remains qualitative, group-like, person-bound, or action-bound before it becomes homogeneous mathematical plurality. |
| lines 2768-2833 and 2908-2917 / PSF pp. 216, 220 | Passive, nominalized verbal forms, and causal verb formation | Kawi, pp. 80, 85, 143 | `raw/010` | The Malay/Tagalog material helps Cassirer avoid a simple active/passive binary; "voice" is mediated by nominal and relational forms. |
| lines 3557-3584, 3861-3863, 3897-3933 / PSF pp. 239, 246, 248 | Blurred noun/verb boundary and Humboldt's "actuale Sein" of the verb | Kawi, pp. 81, 129 ff., 287; pp. 80, 350 f., 397; p. 79 f. | `raw/010`, `raw/020`, `raw/030` | Cassirer presses Kawi into the Ich/person chapter: the verb is not a self-sufficient thing but becomes actual only with person, time, and determinate case. |

Guardrail: the incorporation / Satzwort passage at lines 3748-3818 is
Humboldt-heavy, but Cassirer cites the singular *Verschiedenheit*, pp. 144 f.,
not Kawi Bd. II. Do not attribute that Mexican-incorporation surface to the
Kawi volume unless a separate source check shows the same material there.

Result: the current Kawi shelf is sufficient for chapter III mapping at rough
page level, and it now has normalized support for the Kawi opening, the opening
movement of §23, and the strongest exact PSF III space-verb locus. The other
PSF III citation loci in the table above remain raw unless otherwise noted. The
next normalization should be chosen from one of those concrete loci, not from a
bulk Kawi pass. If chapter III deixis/person pressure becomes the next focus,
the unlanded Humboldt source to pull is still *Ueber die Verwandtschaft der
Ortsadverbien mit dem Pronomen*, not more Kawi intake.

## Cassirer's 1923 Humboldt Essay

The PSF I Schriftenregister also lists Cassirer's own essay:

- Ernst Cassirer, *Die Kantischen Elemente in Wilhelm von Humboldts
  Sprachphilosophie*, in *Festschrift für Paul Hensel*, ed. Julius Binder,
  Greiz i. Vogtl. 1923, pp. 105-127; cited at PSF I p. 97.

This essay is the direct Cassirer-Humboldt-Kant node. It now has a local raw
ECW 16 witness at
`sources/german/cassirer-kantische-elemente-humboldt-sprachphilosophie/source/raw/010-kantische-elemente-ecw16-pdf-112-140.txt`.
If a later task wants to move from current Humboldt work toward Kant,
Erkenntnisproblem Vol. II, or PSF I chapter I, this essay is likely the
efficient next source surface.

Do not treat the essay's existence as already-earned synthesis. Treat the raw
ECW 16 extract as an acquired orientation witness; normalize exact passages
only when the Kant/Humboldt pressure actually starts. A scan of the 1923
Festschrift original remains preferable for citation-critical collation.

## Next Honest Moves

1. Normalize only one chapter III Kawi locus when a concrete quotation or
   close-reading use requires it; otherwise keep the Kawi shelf at mapped raw
   page level.
2. Verify whether the current 1876 Pott Band 2 witness transmits any of the
   exact passages behind Cassirer's singular *Verschiedenheit* references.
3. If Kant/Humboldt pressure strengthens, begin from the landed ECW 16 raw
   extract of Cassirer's *Kantischen Elemente* essay and normalize only the
   exact passages being used.
