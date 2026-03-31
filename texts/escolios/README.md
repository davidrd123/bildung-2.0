# Escolios a un texto implícito — Translation Project

Nicolás Gómez Dávila, *Escolios a un texto implícito I* (1977)

## What This Is

A slow translation of Gómez Dávila's scholia, treated as a practice of reading — not just a product. Each aphorism gets two English renderings (close and free), translation notes, and exegesis. The journal tracks the process itself: what the act of translating reveals.

## Source

- `../../books/escolios.txt` — OCR text from Internet Archive
- `../../books/Gómez Dávila, N. - Escolios a un texto implícito I [ocr] [1977].pdf` — original scan
- [Don Colacho's Aphorisms](https://don-colacho.blogspot.com/) — existing English translations for reference/comparison

## Structure

```
source/
  aphorisms.yaml        # cleaned Spanish, numbered, thematically tagged
sections/
  01-prolegomena.md     # sequential batches, bilingual + commentary
  02-...
journal.md              # translation diary / process reflections
```

## Method

Each aphorism receives:
- **Original** Spanish (cleaned from OCR)
- **Close** translation — structural fidelity, follow the syntax
- **Free** translation — capture the snap in English, even at the cost of structure
- **Notes** — word choices, what's lost/gained between the two renderings
- **Exegesis** — meaning, resonances, connections

Sections follow Gómez Dávila's original sequence. Thematic tags accumulate in `aphorisms.yaml` for future cross-reference passes.

## Translation Philosophy

> "Translating is the most intimate way of reading." — Gómez Dávila never said this, but he would have approved.

Two renderings per aphorism because the *distance* between them is where understanding lives. The close translation preserves the Spanish architecture; the free translation asks what the aphorism would sound like if it had been *thought* in English. Neither is definitive. The process is the point.
