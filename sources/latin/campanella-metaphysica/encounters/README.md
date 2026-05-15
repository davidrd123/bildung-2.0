# Encounters

Encounters are source-grounding passages tied to specific references in other projects. They include corrected Latin (verified against the JP2 page image, not only against the ABBYY OCR), a working translation, and notes on how the source passage bears on the target project.

Longer sequential translations should move into `parts/` if this campaign grows beyond citation-level grounding.

## Verification Discipline

Because the IA-shipped ABBYY OCR contains systematic long-s damage and occasional segmentation errors (notably right-column line-wrap mis-tagged as marginalia), every Latin quotation in an encounter note must be checked against a JP2 crop of the relevant column before being treated as settled. Record any caveats in `source/page-map.yaml` so the next encounter benefits.
