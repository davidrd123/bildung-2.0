# Greek Source Pressure in Cassirer — Substrate Note

**Status:** Source-scaffold note. This records which Greek source surfaces are
being pressured by the Cassirer material now on disk. It does not promote any
Greek author, PSF, or Cassirer generally to a full `texts/` campaign.

## Why This Exists

The PSF I-III chapter splits, the PSF apparatus, `Substanzbegriff und
Funktionsbegriff`, and the existing `Erkenntnisproblem` parts make it possible
to distinguish general name-frequency from real substrate pressure.

The result is not "Greek antiquity" as an undifferentiated source field. The
pressure clusters around a few recurring substrate objects:

1. a bounded Plato dialogue pack
2. Aristotle as logic/substance/perception/demonstration infrastructure
3. a Diels-style Presocratic and atomist dossier
4. Greek mathematics, with Euclid first
5. targeted Neoplatonic, Epicurean, and skeptical surfaces

These are substrate needs: searchable source surfaces that future readers and
agents can inspect when Cassirer's arguments lean on them.

## Highest Priority

### Plato Dialogue Pack

Plato is the strongest single Greek pressure, but not as a generic "Platonism"
bucket. Cassirer repeatedly names specific dialogues:

- `Sophist`
- `Theaetetus`
- `Philebus`
- `Phaedo`
- `Republic`
- `Timaeus`
- `Cratylus`
- `Phaedrus`
- `Symposium`
- Seventh Letter

Immediate evidence:

- PSF I Schriftenregister:
  `source/vol1-die-sprache/920-schriftenregister.txt`
  - `Kratylos` 58 f.
  - `Phaedon` 61
  - `Sophistes` 2, 26, 296
  - `Theatet` 126
  - Seventh Letter 47, 60, 62
- PSF II Schriftenregister:
  `source/vol2-das-mythische-denken/920-schriftenregister.txt`
  - `Phaedon` 201, 288
  - `Philebos` 305
  - `Republik` 157, 202, 294
  - `Sophistes` 158
  - `Symposion` 171, 294
  - `Timaios` 162 f., 248
- PSF III Schriftenregister:
  `source/vol3-phaenomenologie-der-erkenntnis/920-schriftenregister.txt`
  - `Kratylos` 214
  - `Phaidon` 380, 523
  - `Philebos` 449
  - `Politeia` 101
  - `Sophistes` 344, 351, 401
  - `Theaitet` 197, 279
- `Substanzbegriff und Funktionsbegriff` Schriftenregister:
  `../cassirer-substanzbegriff-und-funktionsbegriff/source/raw/032-schriftenregister.txt`
  - `Phaidon` 144
  - `Philebos` 145
  - `Politeia` 144
  - `Theaitetos` 355
- `Erkenntnisproblem` Vol. II, Berkeley:
  `../../../texts/erkenntnisproblem-vol2/parts/056-berkeley-transformation-of-theory-of-knowledge.md`
  where Berkeley's turn from impressions to ideal principles is explicitly
  framed through Plato and the `Theaetetus`.

Working implication: if a Plato substrate is built, do not start with a
whole-Plato ambition. Start with this dialogue pack and keep each dialogue
directly searchable.

Local substrate now exists at:

- `../../../greek/plato-dialogue-pack-cassirer-substrate/README.md`

It contains PerseusDL TEI XML and generated plain-text search surfaces for the
dialogue pack listed above.

### Aristotle Core Shelf

Aristotle is broad and persistent rather than concentrated in one citation
cluster. The pressure is real, but the substrate should begin as a core shelf,
not an attempt to unpack all Aristotle.

Initial Aristotle surfaces:

- `Categories`
- `Metaphysics`, especially substance/category material
- `De anima`, for soul, perception, and the Renaissance psychology line
- `Posterior Analytics` and Organon material, for demonstration and logic
- `Physics` and possibly `De caelo`, for motion, nature, and cosmology

Immediate evidence:

- PSF I Personenregister:
  `source/vol1-die-sprache/930-personenregister.txt`
  gives Aristotle at `62 f., 84, 86, 127-129, 135, 137, 218, 281`.
- PSF III Personenregister:
  `source/vol3-phaenomenologie-der-erkenntnis/930-personenregister.txt`
  gives Aristotle at `11, 19, 57, 107, 116, 352, 411, 525 ff., 529`.
- `Substanzbegriff und Funktionsbegriff` Personenregister:
  `../cassirer-substanzbegriff-und-funktionsbegriff/source/raw/032-schriftenregister.txt`
  gives Aristotle at `1 f., 5-7, 10, 121, 145, 146, 149, 166, 169, 181,
  218, 240 f., 252, 304, 356, 364`.
- `Erkenntnisproblem` Vol. II, Gassendi:
  `../../../texts/erkenntnisproblem-vol2/parts/007-gassendi-opening-and-perception.md`
  shows Epicurean perception theory being modified through Aristotle's account
  of form without matter.

Working implication: Aristotle is a reference substrate for categories,
substance, psychology, and proof. It should not be treated as a single
engagement target until a local task forces a narrower tranche.

Local substrate now exists at:

- `../../../greek/aristotle-core-cassirer-substrate/README.md`

It contains TEI XML and generated plain-text search surfaces for the bounded
core shelf: `Categories`, `De interpretatione`, `Analytica Priora` /
`Analytica Posteriora`, `Metaphysics`, `De anima`, `De sensu`, `Physics`,
`De caelo`, `Topica`, and `Sophistical Refutations`.

### Diels Presocratics / Atomist Dossier

The Presocratic pressure should be one dossier-style substrate organized by
author/fragments, not a set of disconnected mini-campaigns.

Highest-pressure names:

- Parmenides and Zeno
- Democritus and Leucippus
- Heraclitus
- Empedocles
- Anaxagoras
- Xenophanes
- Pythagoreans

Immediate evidence:

- PSF I Schriftenregister:
  `source/vol1-die-sprache/920-schriftenregister.txt`
  cites Heraclitus and Parmenides through Diels.
- PSF II Schriftenregister:
  `source/vol2-das-mythische-denken/920-schriftenregister.txt`
  cites Diels fragments for Democritus, Empedocles, Heraclitus, Leucippus, and
  Parmenides.
- PSF III Schriftenregister:
  `source/vol3-phaenomenologie-der-erkenntnis/920-schriftenregister.txt`
  cites Parmenides fragments at `20, 186, 197`.
- `Substanzbegriff und Funktionsbegriff` Personenregister:
  `../cassirer-substanzbegriff-und-funktionsbegriff/source/raw/032-schriftenregister.txt`
  gives Anaxagoras, Democritus, Empedocles, and Epicurus as live references.
- `Erkenntnisproblem` Vol. I:
  `../../../texts/erkenntnisproblem-vol1/parts/98-galilei-ancient-atomism-and-the-subjectivity-of-sensible-qualities.md`
  makes the Democritus/Galilei connection methodological rather than merely
  atomistic: Cassirer treats the real kinship as a problem of the logical
  foundations of physics, one/many, thought/sense, and mathematical
  objectivity.
- `Substanzbegriff und Funktionsbegriff`:
  `../cassirer-substanzbegriff-und-funktionsbegriff/source/normalized/0145-iv-v.txt`
  treats atomism as a historically decisive expression of physical being,
  motion, void, non-being, and the separation of scientific principle from
  concrete sensible givenness.

Working implication: build this as a Diels-style fragment/search surface with
author-level subdivisions. Democritus/Leucippus and Parmenides/Zeno should come
first inside the dossier.

Local substrate now exists at:

- `../../../greek/presocratic-atomist-doxography-cassirer-substrate/README.md`

This is deliberately an OCR/doxography shelf rather than a clean fragment TEI:
Diels' `Fragmente der Vorsokratiker` and `Doxographi Graeci` are present as
search surfaces, with a standing instruction to verify citation-sensitive
passages against scans or a critical edition. Diogenes Laertius is available in
the Neoplatonic/Epicurean/Skeptic pack as a practical doxographic witness.

## Second Priority

### Greek Mathematics

Greek mathematics is not ornamental in Cassirer. It supplies a recurring model
for construction, relation, deduction, and objectivity.

Initial surfaces:

- Euclid, `Elements`
- Proclus, commentary on Euclid
- Archimedes selections
- Apollonius of Perga
- Ptolemy later, if the astronomy/cosmology line grows

Immediate evidence:

- `Erkenntnisproblem` Vol. I:
  `../../../texts/erkenntnisproblem-vol1/parts/93-kepler-geometry-scientific-possibility-and-the-law-of-the-nonuniform.md`
  reads Euclid through Kepler: the element is not raw material but form of
  connection, and geometry remains the model of deduction.
- `Substanzbegriff und Funktionsbegriff` Personenregister:
  `../cassirer-substanzbegriff-und-funktionsbegriff/source/raw/032-schriftenregister.txt`
  gives Apollonius of Perga, Archimedes, and Euclid as live references.
- PSF I Personenregister:
  `source/vol1-die-sprache/930-personenregister.txt`
  cites Proclus at p. 183.
- PSF III Personenregister:
  `source/vol3-phaenomenologie-der-erkenntnis/930-personenregister.txt`
  gives Ptolemy and Pythagoras as live references.

Working implication: start with Euclid. Add Proclus as a secondary ancient
mathematical-philosophical witness. Archimedes is likely next when Galilei and
modern mathematical physics become active again.

Local substrate now exists at:

- `../../../greek/greek-mathematics-cassirer-substrate/README.md`

It contains TEI XML and generated plain-text search surfaces for Euclid's
`Elements`, selected Archimedes, Apollonius' `Conica`, and Ptolemy's
`Syntaxis mathematica`. Proclus on Euclid Book I is present as Internet Archive
OCR, not TEI; use it for discovery and verify citations against the scan.

### Plotinus / Neoplatonism

Plotinus is real but usually mediated through Renaissance figures rather than
pressed as a direct independent source.

Immediate evidence:

- PSF II Schriftenregister:
  `source/vol2-das-mythische-denken/920-schriftenregister.txt`
  cites Plotinus' `Enneads`.
- `Erkenntnisproblem` Vol. I:
  `../../../texts/erkenntnisproblem-vol1/parts/72-bruno-plotinus-beauty-and-imagination.md`
  uses Plotinus with Plato to frame beauty as mediator between sensible and
  intelligible form, especially in Bruno.

Working implication: build excerpts first: the One, soul, matter, beauty, and
imagination. Do not begin with a full Plotinus campaign.

Local substrate now exists at:

- `../../../greek/neoplatonic-epicurean-skeptic-cassirer-substrate/README.md`

The pack contains the full `Enneads` as TEI plus a generated plain-text search
surface. It remains a substrate shelf, not a Plotinus campaign.

### Epicurus / Sextus / Skepticism

Epicurus is pressured through Gassendi and the empiricism line. Sextus and
Pyrrhonism remain lower-level watch items for the skepticism material.

Immediate evidence:

- `Erkenntnisproblem` Vol. II:
  `../../../texts/erkenntnisproblem-vol2/parts/007-gassendi-opening-and-perception.md`
  shows the conceptual equipment of sensationalism being taken over from
  Epicurus.
- `Erkenntnisproblem` Vol. II:
  `../../../texts/erkenntnisproblem-vol2/parts/011-gassendi-psychology-self-consciousness-and-descartes.md`
  keeps the Epicurus/Gassendi line active through anticipations, image theory,
  and the limits of experience.
- `Substanzbegriff und Funktionsbegriff` Personenregister:
  `../cassirer-substanzbegriff-und-funktionsbegriff/source/raw/032-schriftenregister.txt`
  points to Natorp's ancient-epistemology work on Protagoras, Democritus,
  Epicurus, and skepticism.

Working implication: Epicurus deserves targeted substrate before Sextus.
Sextus/Pyrrhonism should wait until the skepticism surfaces ask for direct
source support.

Local substrate now exists at:

- `../../../greek/neoplatonic-epicurean-skeptic-cassirer-substrate/README.md`

Diogenes Laertius' `Vitae philosophorum` is present as the practical Epicurus
witness, especially Book X. Sextus' `Pyrrhoniae Hypotyposes` and `Adversus
Mathematicos` are also present as TEI/plain search surfaces, but they remain
watch surfaces until the skepticism material becomes more active.

## Reserve And Negative Evidence

### PSF II Mythic Greek Axis

The current substrate order follows the philosophical-epistemological Cassirer:
Plato, Aristotle, Presocratics, mathematics, Plotinus, Epicurus, and skepticism.
PSF II creates a second possible Greek axis around Homer, Hesiod, tragedy,
mystery religion, and Heraclitus as religious thinker. That axis is real, but
it is not yet unpacked here because the present task was to fill the existing
Cassirer-pressure scaffold rather than open the mythical-symbolic shelf.

Working implication: when mythical-symbolic Cassirer becomes active, add a
separate Greek mythic/tragic reserve rather than folding Homer, Hesiod, and
tragedy into the philosophy-of-knowledge substrate.

### Roads Not Yet Taken

The apparatus pressure currently does not justify a Stoic pack, a medical
Hippocratic/Galenic pack, or a broad doxographic tradition pack beyond Diels and
Diogenes Laertius. That absence is evidence about Cassirer's Greek source-base:
it is Plato-Aristotle-Presocratic-mathematical-Neoplatonic before it is Stoic,
medical, rhetorical, or antiquarian.

## Current Substrate Order

1. Plato dialogue pack
2. Aristotle core shelf
3. Diels Presocratics / atomist dossier
4. Euclid and Greek mathematics, with Proclus/Archimedes/Apollonius/Ptolemy nearby
5. Plotinus / Neoplatonism
6. Epicurus, then Sextus/Pyrrhonism as watch surfaces

This order is practical, not canonical. It follows current Cassirer pressure in
the repo rather than an abstract history-of-philosophy sequence.

## Guardrails

- Do not turn name frequency into priority by itself. Priority comes from
  repeated argumentative pressure across PSF, `Substanzbegriff`, and
  `Erkenntnisproblem`.
- Do not collapse the Plato pressure into generic Platonism. Keep the dialogue
  surfaces explicit.
- Do not treat Aristotle as "all Aristotle." Start from the category,
  substance, perception, demonstration, and physics surfaces.
- Do not split the Presocratics too early. A Diels-style fragment substrate is
  more useful than isolated author folders until a specific author becomes
  engagement-active.
- Do not promote Greek sources to `texts/` campaigns just because Cassirer uses
  them. This note records substrate pressure only.
