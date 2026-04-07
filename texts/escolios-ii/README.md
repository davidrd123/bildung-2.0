# Escolios a un texto implicito II — Intake Scaffold

Nicolás Gómez Dávila, *Escolios a un texto implícito II*.

## What This Is

A sibling project to [volume I](/home/davidrd/Projects/Learning/SelfStructure/bildung-2.0/texts/escolios/README.md), but at an earlier stage.

The available source surfaces are now:

- `../../books/Escolios a un texto implícito II -- Nicolás Gómez Dávila -- Colección de autores nacionales, II.pdf` — primary Spanish source
- `../../books/Escolios a un texto implicito II - Nicolas Gomez Davila.txt` — secondary Italian witness, previously misnamed as volume I

So this scaffold is no longer an Italian-only intake problem. It is now a primary-source project with a usable secondary witness and a first working Spanish extraction.

## Current Status

- the original Spanish volume II PDF is present in the workspace
- the Spanish PDF now yields `2442` recovered aphorism starts into `source/aphorisms.yaml`
- one conservative cleanup pass on the Spanish extractor is complete
- the Spanish extraction currently carries one flagged OCR-heavy entry: `id 1189`
- the Italian witness file is now correctly labeled as volume II
- the Italian witness body has been isolated as lines `392-14325`
- that witness yields `3833` aphorism blocks
- endnotes begin at line `14326`; postface begins at line `14442`
- two aphorisms in the Italian witness appear to have truncated openings
- the first fourteen real batches now exist in `sections/01-history-and-ruin.md`, `sections/02-judgment-and-civilization.md`, `sections/03-history-and-the-dying-century.md`, `sections/04-christianity-and-servility.md`, `sections/05-culture-and-concrete-value.md`, `sections/06-historiography-and-tragic-man.md`, `sections/07-order-and-its-ruins.md`, `sections/08-mythology-and-technique.md`, `sections/09-scale-luck-and-authority.md`, `sections/10-sacred-remnant.md`, `sections/11-poterna-and-pretension.md`, `sections/12-soul-forgiveness-authority.md`, `sections/13-love-method-and-homage.md`, and `sections/14-grace-and-the-legitimate.md`

The immediate task here is no longer intake triage. It is to keep batching from the cleaned Spanish source and use the Italian extraction as a check, not as the primary basis of the project.

## Structure

```
source/
  intake.md            # source boundaries, extraction notes, open questions
  aphorisms.yaml       # primary Spanish extraction from the PDF
  aphorisms.it.yaml    # secondary Italian witness extraction
scripts/
  extract_spanish_aphorisms.py # Spanish PDF -> working aphorism source
  extract_italian_aphorisms.py # Italian witness extraction
sections/
  00-intake.md         # launch point before first real batch
journal.md             # project diary for volume II intake
```

## Method

This scaffold stays deliberately lean.

First tasks:

1. preserve the Spanish extraction as the working source
2. preserve the Italian witness as a secondary control surface
3. determine where the Spanish and Italian block counts diverge and why
4. inspect OCR-heavy Spanish entries and damaged Italian entries as they begin to affect batching

Do not assume this project is interchangeable with volume I. Volume II now has the original Spanish print PDF, but not yet the clean OCR surface that made volume I easy to batch.
