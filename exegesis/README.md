# The Exegesis of Philip K. Dick — Reading Atlas

Philip K. Dick, *The Exegesis* (written 1974–1982, published 2011)

## What This Is

A disciplined transformation of Dick's recursive archive into a readable map — without flattening the recursion. Not a translation (the text is already in English), not a summary (the spiral is the point), but an atlas: entry-level granularity, thread-level interpretation.

## Source

- `../books/The Exegesis of Philip K. Dick - Dick, Philip K_.txt` — ebook text of the 2011 Jackson/Lethem abridgement
- The published Exegesis is itself an abridgement of ~8,000 handwritten pages into ~800
- The current ebook source yields **1009 indexed pieces** across **75 folders**: **988 journal entries** and **21 indexed letters**

## Structure

```
source/
  entries.yaml          # one record per bracketed entry; source_id preserves printed [folder:page], id disambiguates repeats
threads/
  README.md             # master thread list and definitions
  zebra-valis.md        # living dossier — grows entry by entry
  black-iron-prison.md
  thomas-anamnesis.md
  orthogonal-time.md
  logos-holy-spirit.md
  fiction-as-prophecy.md
  the-dialectic.md
  2-3-74.md
passes/
  01-folder-04.md       # calibration pass: raw aftermath and first frameworks
  02-folder-23.md       # system-building pass: James-James, prison-world, anamnesis
  03-folder-24.md       # Brahman, the Black Iron Prison, and the mimicking entity
  04-folder-25.md       # Zebra named: signals, providence, and fiction as prior contact
  05-folder-26.md       # Process God, Spirit in history, and anamnesis as memory architecture
  06-folder-27.md       # Psychosis, bicamerality, Zebra as king, and layered-time retrieval
  07-folder-28.md       # Thomas explicit, sacred time, and Ubik as scripture
  08-folder-29.md       # Timaeus, St. Sophia, anti-information, and religion as intervention
scripts/
  extract_entries.py    # rebuilds source/entries.yaml from the ebook text
journal.md              # the reader's changing model of Dick
```

## Why This Is Not `escolios`

The escolios workflow treats each aphorism as an independent unit that gets two translations plus exegesis. The Exegesis defeats that approach because:

- The text is already in English — the problem isn't linguistic transfer
- Individual entries are not self-contained — meaning lives in recurrence, mutation, and self-contradiction across entries
- Even the published abridgement is large: the current extraction yields 1009 indexed pieces across 75 folders, and the text remains obsessively recursive

The **entry** is the archival unit; the **thread** is the interpretive unit.

## Method

### Per-entry annotation (in reading passes)

Each bracketed entry receives:
- **Claim** — the core insight or assertion in 1–2 sentences
- **Threads** — recurring strands that are already active in the entry as written
- **Foreshadows** — optional; later-named strands that are only latent here
- **Drift** — how this relates to earlier/later versions of the same idea; does Dick know he's revising?
- **Echoes** — specific entries this repeats, contradicts, or transforms
- **Sources** — crux references noted (not full parallel text — that's a later phase)

### Thread dossiers (living documents)

Each thread file collects:
- Key entries where the thread appears
- How the concept mutates across the chronological arc
- Internal contradictions and self-revisions
- Connections to other threads

Thread dossiers grow as reading progresses. They are not written upfront.

### Chronological arc

The reading passes respect the source's chronology because the *kind* of thinking changes:
- **Early (1974–76, Folder 4)**: experiential, epistolary, raw shock of 2-3-74
- **Middle (1977–79, Folders 23–50)**: theoretical system-building, attempts at coherence
- **Late (1980–82, Folders 75–91)**: literary self-awareness, writing VALIS and Timothy Archer, reading them back into the Exegesis

### Journal

Tracks the reader's changing model of Dick and of the Exegesis itself. With this text, the changing model is part of the read.

## Deferred (Phase 2+)

- **Source & Swerve**: parallel texts of Dick's citations vs. actual sources (Heraclitus, Parmenides, Gnostic texts, Kant, etc.)
- **Tractate Archaeology**: reverse-engineering the Tractates Cryptica Scriptura back into the Exegesis
- **Cross-project resonances**: connections to Jünger (Zeitmauer/time-crisis) and Gómez Dávila (scholia to an implicit text)

## Regeneration

```bash
python3 exegesis/scripts/extract_entries.py
```

The extraction script validates the current corpus counts and fails if obvious preview junk or count drift appears.
