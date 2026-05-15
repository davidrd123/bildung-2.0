# Cassirer Campanella Latin Citation Map

Status: working citation ledger. Use this to find primary Campanella pages behind Cassirer's Vol. 1 and Vol. 2 claims; do not treat it as a completed page-map until the Campanella leaves are opened.

## Why This Matters

Cassirer was not working from a loose paraphrase tradition. The Vol. 1 and Vol. 2 apparatus cite Campanella's 1638 Latin *Metaphysica* by part, book, chapter, article, and per-part page. That means this campaign can check Cassirer's Campanella directly against the same Latin witness rather than reconstructing him only through later scholarship.

This is a stronger epistemic position than the campaign first assumed. The task is not merely to find where Cassirer got `intrinsecatio`; it is to recover the Latin chain Cassirer used when he made Campanella a hinge between Renaissance natural philosophy, Augustine, Descartes, and Spinoza.

## Confirmed Cassirer Loci In Local Files

From `texts/erkenntnisproblem-vol1/source/normalized/64-naturphilosophie-campanella-alienation-pdf-272-275.txt`:

- `Metaphysik, P. I, Lib. I, Cap. I, Art. IX. (Teil I, S. 20.)`  
  Cassirer's alienation passage: `insanire et perdere proprium esse...`
- `Metaphysik, P. I, Lib. I, Cap. IX. (Teil I, S. 80.)`  
  Pure or a priori knowing as seeing things in God.
- `Metaphysik, P. II, Lib. VI, Cap. III, Art. 5. (Teil II, S. 15.)`  
  The cogito-precursor: we can think this or that thing does not exist, but not that we ourselves do not exist, because thinking presupposes being.
- `Metaphysik P. II, Lib. VI, Cap. VIII, Art. V. (Teil II, S. 64.)`  
  `esse animae et cujuslibet cognoscentis est cognitio sui`.
- `Metaphys. P. II, Lib. VI, Cap. VI, Art. 9 (Teil II, S. 36)`  
  `Unaquaeque res intelligit se ipsam intellectione abdita per suam essentiam...`
- `Metaphysik: Pars III, Lib. XVII, Cap. II, Art. I. (Teil III, S. 244 f.)`  
  Cited by Cassirer in Vol. 1 for cognition/love/deification context; this points to the same printed-page neighborhood as the Vol. 2 intrinsecation passage.

From `texts/erkenntnisproblem-vol1/source/normalized/65-naturphilosophie-campanella-divine-ideas-pdf-276-279.txt`:

- `Metaphysik P. I, Lib. I, Cap. VII. (Teil I, S. 63.)` and `Metaphys. Pars. I, Lib. I, Cap. IV, Art. I. (T. I, S. 33.)`  
  Objects give the occasion of knowing, not knowledge itself.
- `P. I, Lib. II, Cap. V, Art. VII. (T. I, S. 160.)`  
  The stone does not teach me what stone is, but offers the occasion for specification of the act.
- `P. I, Lib. I, Cap. IX, Art. IX. (T. I, S. 73.)`  
  This is now opened as leaf 85: `notitia superaddita`, `innata & abdita`, `scientia non acquiritur, sed scibilia acquiruntur`, and `Sapientia est primalitas sicut potestas & voluntas`.
- `P. II, Lib. VI, Cap. XI, Art. VIII.`  
  Related judgment/occasion passage, not yet located.

From `texts/erkenntnisproblem-vol2/parts/018-spinoza-intuition-renaissance-and-the-short-treatise.md`:

- `Campanella, Universalis Philosophiae seu Metaphysicarum Rerum juxta propria dogmata Partes tres. Parisiis 1638, fol., Teil III, S. 244 f.`  
  Vol. 2 Spinoza bridge: `intrinsecatio, per quam unum fit aliud`; opened in encounter 001 at JP2 leaf 906.
- `Campanella, Metaphysik, Teil II, S. 78`  
  Essential love of God and participated divinity having `saporem`; unlocated in the Campanella witness.
- Long Vol. 2 note on Campanella/Spinoza parallels cites `Metaphysik II, S. 11 f.`, `II, S. 13`, `Metaphysik S. 2`, `Metaphys. II, S. 156 f.`, `Metaphys. II, 194 f.`, and `Metaphys. II, S. 164 f.`  
  These are strong candidates for a later Spinoza crosswalk, but should remain unlocated until opened.

## Bibliographic And Pipeline Notes

### Teil And Pars Numbering

Cassirer's `Teil I/II/III` page references are per-part page references inside the 1638 folio. They do not automatically map to IA JP2 leaves by a fixed offset, and the printed page number can restart or be reused across parts.

Do not merge Ernst's page references and Cassirer's part references just because the numbers resemble each other. Ernst's `Metaphysica part I, p. 73a/b` is now confirmed as JP2 leaf 85, `P. I, Lib. I, Cap. IX, Art. IX`. Cassirer's `P. II, Lib. VI, Cap. VI, Art. 9 (Teil II, S. 36)` is a related `abdita` self-knowledge locus, but it is not the same opened leaf unless the Latin proves it.

### Leaf 906 Section Label Resolved

The campaign currently labels encounter 001 as `Pars III, Liber XVII, Caput II, Articulus I`, printed page 244 / JP2 leaf 906. The local ABBYY extract itself visibly confirms `CAP. II. ARTIC. I.`

Cassirer Vol. 1's local normalized extract previously gave `Pars II, Lib. XVII, Cap. I, Art. I. (Teil III, S. 244 f.)`, but that was a normalization over-correction from damaged OCR, not a reliable print reading. The raw line has `Pars LIE Lib. XVII, Gap. Il Art2`, which should be decoded with the page/part pattern as `Pars III, Lib. XVII, Cap. II, Art. I.` The `Teil III` reference agrees with the 1638 witness and with encounter 001.

The same normalization failure affected the following Vol. 1 footnote: the raw OCR has no secure `P. II` and a damaged `Cap. 'EX`; the corrected local citation is `Metaphysik, P. I, Lib. I, Cap. IX. (Teil I, S. 80.)`. Until the normalization pipeline is reviewed, treat severely damaged Cassirer footnote citations as raw-OCR problems to be re-decoded, not as already-clean bibliographic evidence.

The Vol. 1 divine-ideas extract had the same pattern in file 65: raw OCR `P. I]` had been normalized to `P. II` while the same citation gave `T. I, S. 160`. The local normalized citation is corrected to `P. I, Lib. II, Cap. V, Art. VII. (T. I, S. 160.)`.

## Transmission Note

The Vol. 1 page 274 apparatus explicitly routes one self-knowledge note through Francesco Fiorentino (`Bernardino Telesio`, I, 324 f.; II, 143 f.). That supports the user's handoff hypothesis: Cassirer's path runs through nineteenth-century Italian Renaissance-revival scholarship, but the operative citations are still primary Latin Campanella.

## Queue Implication

- Leaf 85 is now opened because it is both Ernst-guided and Cassirer-cited (`P. I, Lib. I, Cap. IX, Art. IX`, `Teil I, S. 73`).
- The next Cassirer self-consciousness targets are the `Teil II` loci: p. 15, p. 36, p. 64, and the unlocated `P. II, Lib. VI, Cap. XI, Art. VIII`.
- The next Spinoza/Campanella targets are the `Teil II` and `Teil III` pages in Vol. 2 footnotes: especially `Teil II, S. 78`, `Metaphysik II, S. 11 f.`, and `Metaphys. II, S. 156 f.`
- The leaf-906 label is resolved: encounter 001's `Pars III, Lib. XVII, Cap. II, Art. I` agrees with the corrected Cassirer citation.
