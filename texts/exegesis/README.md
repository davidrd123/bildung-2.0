# The Exegesis of Philip K. Dick — Reading Atlas

Philip K. Dick, *The Exegesis* (written 1974–1982, published 2011)

## What This Is

A disciplined transformation of Dick's recursive archive into a readable map — without flattening the recursion. Not a translation (the text is already in English), not a summary (the spiral is the point), but an atlas: entry-level granularity, thread-level interpretation.

## Source

- `../../books/The Exegesis of Philip K. Dick - Dick, Philip K_.txt` — ebook text of the 2011 Jackson/Lethem abridgement
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
  09-folder-30.md       # Hologram composite universe and anomaly as sign of the real
  10-folder-14.md       # Out-of-order 1978 block: dead twin, Sophia whisper, and anti-power discernment
  11-folder-15.md       # Living information, rebellion, and books as hosts
  12-folder-16.md       # Alibi-world, anti-punishment kerygma, and inner illumination
  13-folder-38.md       # The macro-brain, Paraclete, and living-information swarm
  14-folder-18.md       # A-prime logic, Thomas as cohabitant, and Tears as diagnostic signal
  15-folder-02.md       # Model B, Siddhartha waking, and enlightenment as anamnesis
  16-folder-03.md       # Bruno, Paracelsus, covert advent, and the anti-fugue turn
  17-folder-19.md       # Scanner as occlusion key and the corpus as one kerygma
  18-folder-20.md       # Creator in amnesia, Christological correction, and writing as outgoing signal
  19-folder-21.md       # Four deformations, homoplasmate doctrine, and the road into VALIS
  20-folder-22.md       # Crossbonding, maze theory, tractate, and the final exegesis handoff
  21-folder-09.md       # Fat frame, irrational cosmos, and VALIS as new organism
  22-folder-11.md       # Laminated time, perturbation in the reality field, and binary paratruths
  23-folder-08.md       # Books as contact protocol, Empire as stasis, and Ubik overlaid with VALIS
  24-folder-06.md       # Previous-frame anamnesis, Bardo world, and the potentiated past
  25-folder-10.md       # Negentropic cut-in, Sophia as whisper, and the hidden female deity
  26-folder-13.md       # Idea computer, tragedy, and Valis as ultra-thought
  27-folder-39.md       # Track switch, Thomas as revolutionary, and Sophia-Tao oscillation
  28-folder-41.md       # Valis as doomsday device and authoritarian override
  29-folder-42.md       # Survival recoil, self-deflation, and residual enemy-image
  30-folder-43.md       # Irreality, perturbation, and the methodological defense of the enigma
  31-folder-44.md       # Psychosis cross-examination, living scripture, and Christic surrogation
  32-folder-45.md       # Death-strip surgery, divine trash, and the fish's secret victory
  33-folder-46.md       # Ritual identification, lifelong programming, and the richer Christian universe
  34-folder-47.md       # Beethoven, the Christian urwelt, and Spinozan world-brain monism
  35-folder-48.md       # YHWH, Torah, the false church, and the blank-document Christ
  36-folder-49.md       # Macro-mind monotheism, tragic kosmos, and the Godhead split
  37-folder-82.md       # Participatory Valis, groove override, and the survival faculty
  38-folder-83.md       # Third Age, sacred narratives, and the exegesis as memory-work
  39-folder-01.md       # Plotinian mechanism, Tao-perturbation, and the 11-17-80 correction
  40-folder-87.md       # Messianic underground, agape above reason, and the two-tier settlement
  41-folder-88.md       # Exegesis before theophany, Valis as construct, and compassion's bridge
  42-folder-85.md       # Non-being, Logos-world generation, and Holy Spirit as master circuit
  43-folder-89.md       # Part Four opens with 4-D perception, manifesto, and Dionysus
  44-folder-59.md       # VALIS as protest artifact, maze, and hidden Christology
  45-folder-90.md       # Binary process cosmology, Christ consciousness, and the cosmocrator trap
  46-folder-77.md       # VALIS demoted to artistic vision and corpus-within-corpus
  47-folder-78.md       # Bishop Archer as Californian Commedia and Christ-search design note
  48-folder-79.md       # Anokhi, meta-abstraction, and Archer as trilogy capstone
  49-folder-80.md       # Hidden vertical space, Angel as soul, and God evolving from machine to play
  50-folder-91.md       # Ditheon, recombinant scripture, and beauty as benchmark
  51-folder-81.md       # Justification, Angel Archer, and VALIS as code book
  52-folder-62.md       # Tagore, eco-theology, Gnosis, and the heroic reversal
  53-folder-63.md       # God as wounded world-body and Tears as holy book
  54-folder-64.md       # Luke-Acts object mode, hyper-information, and the 23rd letter
  55-folder-56.md       # Gnostic repair, continuum cosmos, and Androids as third kerygma
  56-folder-55.md       # Justification, interface theology, and the moral YHWH turn
  57-folder-67.md       # Tagore heals the schism and sanctions political commitment
  58-folder-68.md       # Armageddon becomes palpable in the anti-nuclear field
  59-folder-69.md       # Hair-shirt Christianity rejected in favor of earned dignity
  60-folder-73.md       # Owl as holy-fool parody and corrective to salvation-through-gnosis
  61-folder-53.md       # 5-D rescue, ETI, Holy Wisdom, and the biosphere-Christ doctrine
  62-folder-54.md       # Sophia's authorship, compassion-maze logic, psychosis limit, and Gnostic success
  63-folder-60.md       # Sacred Christianity redesign and VALIS as art completing 2-3-74
  64-folder-75.md       # Heartbreak, emergent Valis, agape against will, and Tao as center
  65-folder-76.md       # Stop running: fate, thrownness, and world-transformation
  66-folder-84.md       # Christ as ex nihilo newness and VALIS as paradox-machine
  67-folder-57.md       # Final folder: soteriology, interface, Maitreya, and Yang-Yin rescue
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
- **Late (1980–82, the out-of-order Folder 1 block plus the scattered 1980s folders across 53–91)**: literary self-awareness, corrective theology, public apocalypse, writing VALIS and Timothy Archer, and reading them back into the Exegesis

### Journal

Tracks the reader's changing model of Dick and of the Exegesis itself. With this text, the changing model is part of the read.

## Deferred (Phase 2+)

- **Source & Swerve**: parallel texts of Dick's citations vs. actual sources (Heraclitus, Parmenides, Gnostic texts, Kant, etc.)
- **Tractate Archaeology**: reverse-engineering the Tractates Cryptica Scriptura back into the Exegesis
- **Cross-project resonances**: connections to Jünger (Zeitmauer/time-crisis) and Gómez Dávila (scholia to an implicit text)

## Regeneration

```bash
python3 texts/exegesis/scripts/extract_entries.py
```

The extraction script validates the current corpus counts and fails if obvious preview junk or count drift appears.
