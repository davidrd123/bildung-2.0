# Uexküll, Theoretische Biologie — Source Campaign

Jakob von Uexküll, *Theoretische Biologie* (2nd revised edition, 1928)

## What This Is

A bounded source-layer campaign around a small set of decisive passages from Uexküll's *Theoretische Biologie*.

This is more than a single `sources/` encounter, because the work needs its own page map, glossary pressure, and journal. It is less than a full `texts/` project, because the repo has not yet earned a sequential whole-book translation lane here.

## Why Here

Uexküll is already structurally active in the repo's genealogy:

- organism/world coupling
- no neutral view from nowhere
- perspective as constitutive, not decorative
- biology as a challenge to purely causal world-description

The immediate task is to recover the passages that put real pressure on those claims, not to build a new translation apparatus ahead of the evidence.

## Source

- `../../../books/Theoretische Biologie (German Edition) -- J_ von Uexküll (auth_) -- 2_ Aufl_ 1928.pdf`

## Structure

```text
source/
  raw/                  # direct pdftotext extracts for the active tranches
  normalized/           # lightly cleaned working text
  page-map.yaml         # printed-page / PDF-page anchors and encounter map
encounters/
  01-prefaces.md
  02-funktionskreis.md
  03-merkzeichen-und-umwelten.md
  04-fuegung.md
  05-welt-und-umwelt.md
glossary.yaml           # unstable terms under pressure
journal.md              # source-bound drift, not wider synthesis
```

## Working Hypothesis

These passages matter because they are where Uexküll most clearly forces the repo's existing threads:

- `Umwelt` is not reducible to neutral `environment`
- `Funktionskreis` binds organism and world in one circuit
- `Merkwelt` and `Wirkwelt` pressure any one-sided theory of perception or action
- `Planmäßigkeit` and `Fügung` challenge purely causal explanation
- overlapping worlds become biologically concrete rather than merely philosophical

## Encounter Queue

1. `01-prefaces.md`
   Printed `V-VII`, PDF `4-7`.
   Science as question-structure, scaffold, and non-identity with nature; early pressure on `Planmäßigkeit`.

2. `02-funktionskreis.md`
   Printed `99-104`, PDF `109-114`.
   Core definitions of `Funktionskreis`, `Merkwelt`, `Wirkwelt`, `Umwelt`, and the anti-neutral treatment of objects.

3. `03-merkzeichen-und-umwelten.md`
   Printed `61-70`, PDF `71-80`.
   `Merkzeichen`, `Merkmal`, many-worlds biology, and the observer's mediated reconstruction of foreign worlds.

4. `04-fuegung.md`
   Printed `140-145`, PDF `150-155`.
   `Fügung`, `Merkding`, `Wirkding`, `Gegengefüge`, and the distinction between organismic wisdom and mere knowledge.

5. `05-welt-und-umwelt.md`
   Printed `219-222`, PDF `229-232`.
   `Einpassung`, `Umwelttunnel`, overlapping worlds, and the functional-circle culmination.

## Promotion Trigger

Promote this campaign out of `sources/` only if the work starts to demand:

- sustained sequential translation beyond these anchor passages
- a larger tranche workflow than encounter dossiers can hold
- recurring journal drift that exceeds source-bound note-taking
- a fuller glossary than a bounded campaign can manage
- stable cross-project reuse strong enough to justify a standing `texts/` subproject
