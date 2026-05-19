# Pott 1876 / GS VII/1 Crosswalk

Status: bounded source-hygiene check, 2026-05-19.

## Witnesses

- Pott comparison witness: `ia-1876-pott-band2`, Berlin: S. Calvary & Co.,
  1876, edited by A. F. Pott.
- Cassirer citation witness: `googlebooks-gs-vii1-1907`, GS VII/1, Berlin:
  B. Behr's Verlag, 1907, edited by Albert Leitzmann.

## Finding

The checked loci show that Pott Band 2 and GS VII/1 transmit the same singular
*Ueber die Verschiedenheit des menschlichen Sprachbaues* text at the places
now needed for Cassirer PSF I work, but their page numbers diverge. There is
no single stable Pott-to-GS offset.

Use GS VII/1 for Cassirer's Schriftenregister page references. Use Pott Band 2
as a comparison witness and for the already-normalized Ergon/Energeia tranche.

## Checked Loci

| Locus | GS VII/1 | Pott 1876 Band 2 | Result |
| --- | --- | --- | --- |
| Text opening | p. 1 / PDF p. 15 | p. 1 / PDF p. 7 | Same opening text. |
| Ergon/Energeia | pp. 46-47 / PDF pp. 60-61 | pp. 55-56 / PDF pp. 61-62 | Same passage; Pott normalized tranche exists at `source/normalized/008a-ergon-energeia-pdf-061-062.txt`. |
| Subject/object/objectivity | p. 55 / PDF p. 69 | p. 66 / PDF p. 72 | Same passage around subjective activity forming an object in thinking. |
| Language as ever-generating | p. 57f. / PDF pp. 71-72 | around p. 70 / PDF p. 76 | Phrase-level check confirms overlap around language not being handed over as a fixed mass. |
| Weltansicht / image in the soul | p. 60 / PDF p. 74 | not exact-mapped in this pass | GS VII/1 raw extract contains the Cassirer-relevant locus; exact Pott page remains unnecessary unless Pott collation becomes the task. |

## GS VII/1 Page Offset

For the main GS VII/1 text and appendix, checked anchors support:

```text
pdf_page = printed_page + 14
```

Checked anchors include printed pp. 1, 46, 60, 105, 223, 300, and appendix
opening p. 345.

## Consequence

The earlier open question was whether the local 1876 Pott witness could stand
behind Cassirer's singular *Verschiedenheit* references. The answer is now:
only as a comparison witness. Since the GS VII/1 citation witness has landed,
do not route Cassirer page references through Pott pagination.
