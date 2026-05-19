# Sequential Run Standard

This is the quick reference for Campanella page-order work. Use it before starting any `part-iii-NNN-*` or other numeric sequential run.

The lesson from the first Part III long tranche is simple: speed is useful only if the output remains translation. A sequential run may be rough, bracketed, and incomplete in collation, but it must not turn the `English` section into argument summary.

## What Sequential Means

Sequential work is page-order substrate:

- move through the witness in order
- keep source paths and leaf numbers visible
- transcribe the body text in the order it appears
- translate the transcribed Latin directly enough that a later chat can cite the English as a working translation
- put synthesis, compression, and cross-leaf interpretation in `## Note`, not in `## English`

If the work is mostly argument summary, it is not a sequential part. Label it as a reading note or scratch summary instead.

## Required Part Shape

Use this compact shape:

```md
# Part III NNN: Short Content Title

Source: JP2 leaf `NNNN`, Part III, Liber X, Caput Y, Articulus Z if visible. Printed page not collated.

Raw: `source/raw/...`  
Normalized: `source/normalized/...`

## Latin

[Corrected working transcription of the body argument, in order.]

## English

[Direct working translation, paragraph-aligned with the Latin.]

## Note

[2-4 sentences on what the leaf/part is doing and what it connects to.]
```

Do not add encounter-only sections such as `Opening Finding`, `Translation Risk`, `Re-Entry`, or Latin-German bridges unless the file is deliberately being promoted out of the sequential lane.

## Latin Standard

The `## Latin` section is a corrected working transcription, not a selected quotation bank.

- Include the body argument in sequence.
- Exclude running headers and non-substantive marginalia.
- Include marginalia only when it bears on the argument or supplies a heading.
- Preserve uncertainty inline with `[?]`.
- Do not silently omit a paragraph because it is hard.
- If OCR is too damaged to transcribe, write a visible marker such as `[leaf block too damaged for working transcription; raw extract requires page-image collation]` and keep moving only if the loss is local.

If only selected Latin is being copied, the file must say `Latin excerpts`, not `Latin`, and it should not count as completed sequential transcription.

## English Standard

The `## English` section is a translation, not a paraphrase.

Minimum rule: each Latin paragraph should have a corresponding English paragraph in the same order.

Good:

> Sense too knows quiddity, because it knows the universal and the particular, species and differences; not the eye, to be sure, but the sensing power in the eye.

Bad:

> Sense also knows quiddity, not the eye as eye but the sensing power in the eye. Reason arises from universals and collected experiments; memory, reminiscence, common sense, fantasy, reason, and intellect are differentiated operations of the same spirit.

The bad version is a useful note, but it is not a direct translation of the Latin paragraph. It compresses multiple clauses into interpretation and changes the function of the English section.

Avoid these paraphrase signals in `## English` unless the Latin itself warrants them:

- "Campanella argues..."
- "His reply is..."
- "The passage shows..."
- "The key move is..."
- "This means..."

Those belong in `## Note`.

## Fidelity Check Before Moving On

Before calling a part done, check:

- Does every substantive Latin paragraph have an English counterpart?
- Could a reader reconstruct the Latin order from the English order?
- Is every interpretive sentence outside the translation section?
- Are hard readings marked rather than smoothed?
- Did the file translate what it transcribed, rather than translate a mental summary of the leaf?

If any answer fails, reduce the number of leaves in the run. Do fewer parts rather than produce summaries labeled as translations.

## Long-Run Discipline

Long sequential runs are still allowed. The correction is not to return to short pilots; it is to keep the unit honest.

- Quantity target is secondary to translation fidelity.
- Apparatus can stay scratch-only during the run.
- Canonical uptake can happen at tranche boundaries.
- If the Latin is too hard for 25 leaves, run 5-10 leaves well.
- If a fast pass is desired, call it a `survey summary`, not a translated sequential run.

## Redo Flag

The tranche `part-iii-003` through `part-iii-027` was produced under a flawed standard: many `## English` sections are argument summaries rather than direct paragraph-level translations, and many `## Latin` sections are condensed selected transcription rather than full body transcription.

Treat those files as provisional reading summaries until redone against this standard.
