# Intake Notes

## Source Files

- `../../books/Escolios a un texto implícito II -- Nicolás Gómez Dávila -- Colección de autores nacionales, II.pdf`
- `../../books/Escolios a un texto implicito II - Nicolas Gomez Davila.txt`

## Witness Hierarchy

Primary witness:

- the Spanish PDF is the original volume II source
- `pdftotext` on the opening pages confirms `ESCOLIOS A UN TEXTO IMPLICITO II` and the 1977 Bogotá edition

Secondary witness:

- the Italian `.txt` file had been misnamed as volume I
- its own front matter identifies it as `Escolios a un texto implicito II`
- it remains useful as a line-addressable comparison surface

## What The Italian File Actually Is

The Italian file is:

- volume II, not volume I
- Italian translation, not original Spanish
- a mixed export containing front matter, main body, endnotes, postface, and notes

## Working Line Map

For the Italian witness:

- `1-391`: front matter and prefatory material
- `392-14325`: main aphorism body
- `14326-14441`: endnotes
- `14442-14658`: postface and notes

These boundaries are good enough for reproducible extraction of the Italian witness.

## Extraction Questions

1. Which OCR or conversion artifacts in the Spanish extraction need systematic cleanup before batching?
2. The Italian body contains `3833` extracted blocks. The Spanish primary currently yields `2442` recovered aphorism starts. Why do the witnesses segment so differently?
3. Is any page structure recoverable from the print edition?
4. What batch size makes sense for the first real section given the current state of the Spanish surface?

## Current Working Extraction

- `source/aphorisms.yaml`: Spanish primary extraction from the PDF
- `source/aphorisms.it.yaml`: Italian witness extraction from the translated text file

The Spanish extraction is now the project's working source. The Italian extraction is comparison material.

## Known Witness Problems

In the Spanish extraction:

- OCR spacing and line-break artifacts survive in places
- some entries contain letter-spaced or otherwise damaged typography that will need cleanup

In the Italian witness:

- inline note markers remain embedded in some aphorisms
- at least two aphorisms have visibly truncated openings:
  - `id: 3750` / line `14014`
  - `id: 3830` / line `14310`

## First Principles

- Extract before interpreting.
- Keep witness status explicit in every downstream file.
- Do not build handle or thread infrastructure until real batching pressure appears.
