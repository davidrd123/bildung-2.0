# Gassendi - Disquisitio Metaphysica

A sequential Latin translation of Pierre Gassendi's *Disquisitio metaphysica seu dubitationes, et instantiae adversus Renati Cartesii metaphysicam, & responsa*, working through the Cartesian *Meditationes* via Gassendi's *Dubitationes* / *Instantiae* / *Responsiones* exchange with Descartes.

## Status and Scope

The campaign was opened in May 2026 as a bounded source-grounding campaign tied to **one Cassirer footnote** in `texts/erkenntnisproblem-vol2` (Part 011, the sun-idea passage from Meditatio III, Dubitatio III). It has since grown well past its originating anchor:

- **Sequential translation through Meditations III, IV, and V** with their associated *Dubitationes*, *Instantiae*, and *Responsiones* -- roughly 140 printed pages of Latin walked through tranche by tranche.
- **62 parts files** with corrected German-format Latin, draft English, and structural notes. See `parts/` for the current depth.
- **30+ glossary entries** earned through the translation (`idea / notio`, `realitas objectiva / formalis`, `essentia / existentia`, `petitio principii`, etc.). See `glossary.yaml`.

This now lives at two levels at once:

1. **A Cassirer-anchored ground for `texts/erkenntnisproblem-vol2`** -- the original purpose. The `reading/erk-vol2-gassendi-crosswalk.md` records which parts overlap with Cassirer's Vol. 2 Gassendi chapter.
2. **A test case for sustained primary-source Latin translation** in this project's apparatus. It is the first campaign in `sources/latin/` to grow this far, and the methodological lessons (encounter format vs. sequential parts, glossary-as-routing surface, witness-set discipline) feed back into other Latin campaigns -- currently the *Universalis Philosophia* and *Spinoza Opera* campaigns under `sources/latin/`.

### Deferred decision: promotion to `texts/`

The current scale matches what `texts/` projects do -- 62 sequential parts, structured journal, substantive glossary, chapter-bounded scope. The right architectural move is eventually to promote this to `texts/gassendi-disquisitio-metaphysica/` and rename the parts so this is honestly described as the translation project it has become.

For now, the directory stays at `sources/latin/gassendi-disquisitio-metaphysica/` because **active translation work is ongoing** and moving a live directory would create cross-reference and working-tree race conditions. Promote when the work reaches a natural pause (Meditation V close was reached at Part 062; Meditation VI would be the next logical extension or stopping point).

When the promotion happens, the following will need to update in lockstep:
- The directory itself (`git mv` to `texts/gassendi-disquisitio-metaphysica/`).
- `.gitignore` entries for `source/{pdf,page-images,local,abbyy}/` paths.
- Cross-references in `sources/latin/spinoza-opera/`, `sources/latin/campanella-metaphysica/`, `sources/modern/ernst-campanella-book-and-body-of-nature/`, and `texts/erkenntnisproblem-vol2/`.
- The README framing here (this section) and `encounters/README.md`, `parts/README.md`.

## Source Decision

- Preferred page-image witness: the higher-quality KB / ProQuest / Early European Books scan from `Disquisitio metaphysica version2.pdf` and its JP2 directory, archive id `ned-kbn-all-00004327-001`.
- OCR witness: the smaller Google / Internet Archive PDF from `Disquisitio metaphysica.pdf`, archive id `bub_gb_M5UziO9dSMQC`.
- Fallback page-image witness: the Google / Internet Archive JP2 directory from `Disquisitio metaphysica`.

The version2 PDF text layer is mostly ProQuest boilerplate, so page-image OCR should be done from the JP2 files. The older PDF has a noisy but useful embedded OCR layer and is useful for locating passages quickly.

## Local Binary Policy

The local PDFs and JP2 directories are deliberately untracked:

- `source/pdf/`
- `source/page-images/`
- `source/local/`

The tracked files in this folder should be maps, corrected extracts, translation encounters, glossary entries, journals, and scripts.

## Structure

- `source/witnesses.yaml` records the local witness set and import policy.
- `source/page-map.yaml` records known page correspondences and Vol. 2 anchors.
- `source/raw/` keeps raw OCR or PDF text extraction outputs.
- `source/normalized/` keeps corrected working extracts, never silent emendations.
- `encounters/` keeps source-grounding passages tied to specific Cassirer citations (single-passage, citation-grade work). Currently one encounter: the sun-idea anchor that opened the campaign.
- `parts/` holds sequential translation tranches following Gassendi's *Dubitatio* / *Instantia* / *Responsio* structure through the Cartesian *Meditationes*. Currently 62 parts walking through Meditations III, IV, and V.
- `reading/` keeps crosswalks back to `texts/erkenntnisproblem-vol2`.
- `scripts/` keeps local extraction helpers.

## OCR Baseline

For now, use Tesseract as the local baseline rather than adding Calamari:

```sh
python3 scripts/ocr_jp2_page.py --page-index 138 --output source/raw/001-sun-idea-version2-jp2-0138.txt
```

The helper defaults to `script/Latin`, `--psm 4`, and preserved interword spacing. Fraktur/`frk` passes can be run manually as secondary stress witnesses, but they should not be treated as the primary OCR for this Antiqua scan.

## Original Anchor

The campaign was first opened against this Cassirer Vol. 2 footnote:

`Disquisitio Metaphysica seu Dubitationes et Instantiae adversus Ren. Cartesii Metaphysicam. In Meditat. III Dubitatio III. (Opera III, 294.)`

The sun-idea passage is at version2 JP2 image `ned-kbn-all-00004327-001_0138.jp2`, printed page `110`; the older Google OCR witness locates it at PDF page `126`. The first encounter file `encounters/001-sun-idea-meditatio-iii-dubitatio-iii.md` documents this anchor with the full Trigger / Witnesses / Local Context / Cassirer Passage / Working Translation / Surrounding Argument / Reply / Notes / Re-entry format. That file is the template for any future single-passage encounter work in this campaign or its sister Latin campaigns.

The sequential translation in `parts/` began from this anchor and has continued forward through the Disquisitio's argument structure.

Two ignored JPEGs for Transkribus testing are stored under `source/local/transkribus-test-jpegs/`: the located page `0138` and continuation page `0139`.
