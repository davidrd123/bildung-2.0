# Escolios a un texto implícito — Translation Project

Nicolás Gómez Dávila, *Escolios a un texto implícito I* (1977)

## What This Is

A slow translation of Gómez Dávila's scholia, treated as a practice of reading — not just a product. Each aphorism gets two English renderings (close and free), translation notes, and exegesis. The journal tracks the process itself: what the act of translating reveals.

## Reading Claim

> "All literature is contemporary for the reader who knows how to read."

The wager here is not historical recovery for its own sake. The text is being read in the present tense, and translation is one way of earning that contemporaneity.

## Source

- `../../books/escolios.txt` — OCR text from Internet Archive
- `../../books/Gómez Dávila, N. - Escolios a un texto implícito I [ocr] [1977].pdf` — original scan
- [Don Colacho's Aphorisms](https://don-colacho.blogspot.com/) — existing English translations for reference/comparison

## Current Status

The current source surface is `Escolios a un texto implícito I` only. The translated and annotated first pass now covers the full available volume:

- `499` aphorisms
- `17` section files
- pages `11-126` of the 1977 volume

So the immediate work is no longer extending section count inside volume I. It is deepening use of the translated material without overbuilding new infrastructure.

The current second-pass work is intentionally limited to one reread memo focused on the load-bearing aphorisms already anchoring the project. It is not a separate synthesis tree.

A sibling intake scaffold for volume II now exists at [texts/escolios-ii](../escolios-ii/README.md), built from the currently available Italian translation witness.

## Structure

```
source/
  aphorisms.yaml        # cleaned Spanish, numbered, thematically tagged
  handles.yaml          # lean handle/evidence index for current load-bearing aphorisms
sections/
  01-prolegomena.md     # sequential batches, bilingual + commentary
  02-...
selective-second-pass.md # reread memo for volume I load-bearing aphorisms
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

The handle layer stays intentionally lean: section-range handles plus stable evidence handles for the aphorisms already carrying method or cross-project weight. It is not yet a full thread apparatus.

## Translation Philosophy

> "Translating is the most intimate way of reading." — Gómez Dávila never said this, but he would have approved.

Two renderings per aphorism because the *distance* between them is where understanding lives. The close translation preserves the Spanish architecture; the free translation asks what the aphorism would sound like if it had been *thought* in English. Neither is definitive. The process is the point.
