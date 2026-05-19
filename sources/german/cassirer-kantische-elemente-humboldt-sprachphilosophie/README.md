# Cassirer - *Die Kantischen Elemente in Wilhelm von Humboldts Sprachphilosophie*

Ernst Cassirer, "Die Kantischen Elemente in Wilhelm von Humboldts
Sprachphilosophie," in Julius Binder, ed., *Festschrift fuer Paul
Hensel-Erlangen*. Greiz i. Vogtl.: Ohag, 1923, pp. 105-127.

## Status

Source text landed from the ECW 16 Hamburger Ausgabe PDF. It now has two
working normalized tranches for bounded source-near orientation before a
Kant/Humboldt synthesis, but it is not the original 1923 Festschrift scan.

This shelf exists because PSF I cites the essay at p. 97 and the Humboldt
source-use map identifies it as the direct Cassirer-Humboldt-Kant bridge.

## Local Source

Local authority copy, gitignored:

- `source/local/ecw16-aufsaetze-und-kleine-schriften-1922-1926-compress.pdf`
  - copied from `/Users/daviddickinson/Downloads/gesammelte-werke-hamburger-ausgabe-aufstze-und-kleine-schriften-1922-1926_compress.pdf`
  - Felix Meiner / Hamburger Ausgabe, ECW 16, *Aufsaetze und kleine Schriften
    1922-1926*

Tracked raw extract:

- `source/raw/010-kantische-elemente-ecw16-pdf-112-140.txt`
  - extracted with `pdftotext -layout`
  - PDF pages 112-140
  - ECW pages 105-133
  - original publication pagination in headers: pp. 105-127

Tracked normalized tranches:

- `source/normalized/010a-kant-synthesis-language-objectivity-pdf-128-131.txt`
  - PDF pages 128-131 / ECW pages 121-124
  - Cassirer's central Kantian objectivity/synthesis framing for Humboldt's
    language philosophy.
- `source/normalized/010b-ergon-energeia-critical-objectivity-pdf-139-140.txt`
  - PDF pages 139-140 / ECW pages 132-133
  - closing Ergon/Energeia formulation of the Kant-Humboldt relation.

Structure helpers:

- `source/witnesses.yaml`
- `source/sections.yaml`

## Verified Bibliographic Anchors

- PSF I Schriftenregister:
  `sources/german/cassirer-philosophie-der-symbolischen-formen/source/vol1-die-sprache/920-schriftenregister.txt`
- Berliner Klassik / BBAW bibliography record:
  `https://berlinerklassik.bbaw.de/bibliographie/2338`
- Original publication:
  *Festschrift fuer Paul Hensel-Erlangen*, ed. Julius Binder, Greiz i. Vogtl.:
  Ohag, 1923, pp. 105-127.
- Later English translation:
  "The Kantian Elements in Wilhelm von Humboldt's Philosophy of Language
  (1923)," trans. S. G. Lofts, in *The Warburg Years (1919-1933)*, Yale
  University Press, 2013, pp. 101-129.
- Later French translation:
  "Les elements kantiens dans la philosophie du langage de Wilhelm von
  Humboldt," trans. Aurelien Djian, *Les Etudes philosophiques* 113/2
  (2015), pp. 259-282.
- Later German reprint references found in secondary literature:
  ECW 16, *Aufsaetze und kleine Schriften 1922-1926*, and *Geist und Leben*.

## Search Pass

Checked locally:

- `/Users/daviddickinson/Downloads` for Hensel, Ohag, Binder, Festschrift,
  Kantische/Kantian, Humboldt, Warburg Years, ECW, Geist und Leben.

Checked publicly:

- Internet Archive-style searches for *Festschrift fuer Paul Hensel* and the
  exact essay title.
- BBAW Berliner Klassik bibliography.
- Library/catalog records from CiNii, HEIDI, LIBRIS, and DNB.
- Gated republication surfaces on De Gruyter/Yale and Cairn.

Result: bibliographic identity is verified, and an ECW 16 PDF witness is now
landed locally. A scan of the 1923 Festschrift original remains preferable for
citation-critical work.

## Acquisition Rule

If a better PDF, scan, or OCR witness is obtained, land it here, not in the PSF
shelf and not in a general Cassirer shelf.

Expected first source paths:

- `source/local/` for the PDF/scan/OCR sidecars; gitignored.
- `source/raw/` for uncorrected extracted text.
- `source/normalized/` only after checking against page images or a reliable
  scan; current tranches are working normalizations, not diplomatic text.

Do not treat later translations as substitutes for the 1923 German essay unless
the task explicitly needs a translation witness.
