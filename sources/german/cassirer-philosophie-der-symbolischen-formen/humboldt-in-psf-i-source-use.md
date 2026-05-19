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
| *Ueber den Dualis* | none yet | Pull as GS VI/1 support if chapter III dual/plural/person pressure becomes active. |
| *Ueber die Verwandtschaft der Ortsadverbien mit dem Pronomen...* | none yet | Pull as GS VI/1 support if deixis/pronoun/adverb pressure becomes active. |
| *Lettre à Monsieur Abel-Rémusat... langue Chinoise* | none yet | Pull with the Chinese grammar pair when non-Indo-European form pressure becomes active. |
| *Ueber den grammatischen Bau der Chinesischen Sprache* | none yet | Pull with the Abel-Rémusat letter. |
| *Grundzüge des allgemeinen Sprachtypus* | none yet | Pull after Kawi and singular/plural distinction are stabilized. |
| *Ueber das vergleichende Sprachstudium...* | none yet | Pull after Kawi and singular/plural distinction are stabilized. |
| Brief an F. A. Wolf, 16 June 1804 | none yet | Low-volume support source for the chapter I Humboldt opening. |
| *Ankündigung einer Schrift über die Vaskische Sprache und Nation* | none yet | Minor support source; not a current pull priority. |

Cassirer's own *Die Kantischen Elemente in Wilhelm von Humboldts
Sprachphilosophie* is now represented as an acquisition target at
`sources/german/cassirer-kantische-elemente-humboldt-sprachphilosophie/`.
No full-text witness has landed there yet.

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
  - `source/raw/023-feststellung-des-begriffs-des-kawi-pdf-231-246.txt`
  - `source/raw/020-drittes-buch-erster-abschnitt-stammverwandtschaft-pdf-248-336.txt`
  - `source/raw/030-drittes-buch-zweiter-abschnitt-westlicher-zweig-pdf-337-485.txt`

The two smaller Kawi extracts are raw navigational tranches, not corrected
normalizations. They are the first local work surfaces for the Kawi opening
and the section 23 close where Humboldt explicitly fixes the concept of Kawi.

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

## Cassirer's 1923 Humboldt Essay

The PSF I Schriftenregister also lists Cassirer's own essay:

- Ernst Cassirer, *Die Kantischen Elemente in Wilhelm von Humboldts
  Sprachphilosophie*, in *Festschrift für Paul Hensel*, ed. Julius Binder,
  Greiz i. Vogtl. 1923, pp. 105-127; cited at PSF I p. 97.

This essay is the direct Cassirer-Humboldt-Kant node. If a later task wants to
move from current Humboldt work toward Kant, Erkenntnisproblem Vol. II, or
PSF I chapter I, this essay is likely the efficient next source surface.

Do not treat the essay's existence as already-earned synthesis. Treat it as a
high-priority source target. Current status: bibliographically verified, but
not yet pulled as a source text.

## Next Honest Moves

1. Check the two targeted Kawi raw tranches against the TIF page images before
   any quotation, translation, or interpretive claim: the Kawi opening and the
   `Feststellung des Begriffs des Kawi` close.
2. Verify whether the current 1876 Pott Band 2 witness transmits any of the
   exact passages behind Cassirer's singular *Verschiedenheit* references.
3. If Kant/Humboldt pressure strengthens, locate Cassirer's *Kantischen
   Elemente* essay before widening to a general Cassirer-Humboldt synthesis.
