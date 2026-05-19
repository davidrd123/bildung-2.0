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

The current local Humboldt scaffold at
`sources/german/humboldt-verschiedenheit-sprachbau/` is a different working
witness: the 1876 Pott edition of *Ueber die Verschiedenheit des menschlichen
Sprachbaues*, with Volume 2 now serving as the primary Humboldt running-text
witness for that edition.

Do not collapse these witnesses. The 1876 Pott Band 2 material may overlap
with, excerpt, reframe, or transmit material adjacent to the 1838 Kawi volume,
but that relation still needs verification. Until checked, use:

- `ia-1876-pott-band2` as the current local Humboldt *Verschiedenheit* witness
- the 1838 Buschmann-edited Kawi Bd. II as Cassirer's named Kawi citation
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
high-priority source target.

## Next Honest Moves

1. Add a witness entry if the 1838 Buschmann-edited Kawi Bd. II is located.
2. Verify whether the current 1876 Pott Band 2 witness transmits any of the
   exact passages behind Cassirer's Kawi Bd. II page references.
3. If Kant/Humboldt pressure strengthens, locate Cassirer's *Kantischen
   Elemente* essay before widening to a general Cassirer-Humboldt synthesis.
