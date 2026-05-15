# Gassendi - Disquisitio Metaphysica

This is a bounded Latin source campaign for Pierre Gassendi's *Disquisitio metaphysica seu dubitationes, et instantiae adversus Renati Cartesii metaphysicam, & responsa*.

It exists first to ground and transclude the Gassendi material in `texts/erkenntnisproblem-vol2`, especially the chapter close where Cassirer compares Descartes' sensory and astronomical ideas of the sun. It is not yet a full sequential `texts/` project.

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
- `encounters/` keeps source-grounding passages and translation notes.
- `parts/` is reserved for longer sequential translation chunks if the campaign grows.
- `reading/` keeps crosswalks back to `texts/erkenntnisproblem-vol2`.
- `scripts/` keeps local extraction helpers.

## OCR Baseline

For now, use Tesseract as the local baseline rather than adding Calamari:

```sh
python3 scripts/ocr_jp2_page.py --page-index 138 --output source/raw/001-sun-idea-version2-jp2-0138.txt
```

The helper defaults to `script/Latin`, `--psm 4`, and preserved interword spacing. Fraktur/`frk` passes can be run manually as secondary stress witnesses, but they should not be treated as the primary OCR for this Antiqua scan.

## Current Priority

The first target is Cassirer's Part 011 footnote:

`Disquisitio Metaphysica seu Dubitationes et Instantiae adversus Ren. Cartesii Metaphysicam. In Meditat. III Dubitatio III. (Opera III, 294.)`

The corresponding standalone scan location is version2 JP2 image `ned-kbn-all-00004327-001_0138.jp2`, printed page `110`; the older Google OCR witness locates it at PDF page `126`.

Two ignored JPEGs for Transkribus testing are stored under `source/local/transkribus-test-jpegs/`: the located page `0138` and continuation page `0139`.
