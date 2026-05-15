# Spinoza Opera (Latin source campaign)

This is a Latin primary-source campaign for Spinoza's *Opera*, anchored on the *Ethica* but flexible to grow into other works (*Tractatus de intellectus emendatione*, *Cogitata Metaphysica*, *Epistolae*).

It exists to ground and triangulate Cassirer's Spinoza chapter in `texts/erkenntnisproblem-vol2`, where most Latin footnote quotations come from the *Ethica*. It is not yet an active campaign -- no encounter has been earned.

## Witness Set

Three layered Latin witnesses are imported:

1. **Gentile 1915 (Ethica only)** -- preferred page-image authority. Both PDF and JP2 page-images are available locally, so this is the witness for citation-grade extraction.
2. **Van Vloten / Land 1882 (Opera, vol. 1)** -- the Cassirer-anchored witness. This is the edition Cassirer cites in Erk. Vol. 2 (see Part 018 footnote 6). Volume II of this edition is not yet imported.
3. **Gebhardt 1925 (Opera)** -- the standard modern critical reference. The Ethica sits in volume II.

See `source/witnesses.yaml` for details on each, and `source/page-map.yaml` for the candidate Erk. Vol. 2 anchors.

## Status

- Scaffold opened; witness set imported.
- No encounter file yet. The obvious first target is the *Ethica* Part I prop. 10 scholium, which Cassirer quotes in Erk. Vol. 2 Part 030 footnote 2 to anchor the chapter-close claim that the attribute concept depends on the intellect's mode of attribution. That passage is short, self-contained, and structurally load-bearing -- the right scale for a first encounter, analogous to the Gassendi sun-idea encounter.
- No `parts/` yet. The campaign should stay at encounter scale unless a sequential translation chunk is actually called for by Vol. 2 pressure.

## Local Binary Policy

The PDFs and page-images are deliberately gitignored:

- `source/pdf/` -- the three edition PDFs
- `source/page-images/` -- the Gentile JP2 directory (404 files)
- `source/local/` -- scratch space for OCR/lexicon artifacts

The tracked files in this folder are the witness map, page map, corrected extracts, encounter notes, glossary entries, journal, and scripts.

## Structure

```text
source/
  pdf/                                            (gitignored)
    spinoza-ethica-gentile-1915.pdf
    spinoza-opera-vanvloten-land-1882-vol1.pdf
    spinoza-opera-gebhardt-1925.pdf
  page-images/                                    (gitignored)
    gentile-jp2/
      EthicaSpinozaGentile_0000.jp2
      ...
      EthicaSpinozaGentile_0403.jp2
  raw/                                            (text extractions, tracked when earned)
  normalized/                                     (corrected working texts, tracked when earned)
  local/                                          (gitignored scratch)
  witnesses.yaml
  page-map.yaml
encounters/                                       (bounded encounter notes)
parts/                                            (only if sequential translation is earned)
reading/
  erk-vol2-spinoza-crosswalk.md
scripts/                                          (extraction helpers, can reuse Gassendi templates)
journal.md
glossary.yaml
```

## How To Open The First Encounter

The Gassendi *Disquisitio* campaign has a working template: see `sources/latin/gassendi-disquisitio-metaphysica/encounters/001-sun-idea-meditatio-iii-dubitatio-iii.md` for the shape (Trigger / Witnesses / Local Context / Cassirer Passage / Working Translation / Surrounding Argument / Reply / Notes / Re-entry).

For the *Ethica* Part I prop. 10 scholium target:

1. Locate the passage in the Gentile JP2 page-images (likely around printed pages 12-15; verify against the actual JP2 index).
2. Run OCR via `tesseract` against the JP2, or use `pdftotext -layout` on the Gentile PDF as a cross-check.
3. Open `encounters/001-ethica-i-prop-10-scholium.md` with the seven standard sections.
4. Triangulate against Van Vloten/Land (printed pages in vol. 1) and Gebhardt (vol. II page number).

If the Cassirer-anchored verification is the question, the Van Vloten/Land witness is the right one to check; if the question is the canonical modern Latin, Gebhardt is the witness. The Gentile gives the best page-image quality for verification.
