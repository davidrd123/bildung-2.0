# 2026-04-15 — Short external-facing summary of repo design

**Status:** Working summary, not canonical wording. This note is for explaining the repo's current design choices briefly without importing the larger conversation vocabulary.

## Short version

`bildung-2.0` is a text-authoritative reading, translation, and source-probing instrument.

It is built to help a human reader and LLMs work with difficult source material without flattening it into premature clarity.

It supports both long-form translation runs and smaller bounded source-near tests, while keeping those modes distinct.

The repo does this through six main choices:

1. **Texts remain the authority.**  
   Handles, YAML, and views are derived structure that point back into canonical text files, not a replacement for them.  
   [patterns/handle-schema.md](/Users/daviddickinson/Projects/Lora/bildung-2.0/patterns/handle-schema.md:3)

2. **Unresolved terms are preserved as positive data.**  
   A term can remain `open`, with `preferred: null` and multiple failed alternatives, when the source genuinely resists resolution.  
   [patterns/handle-schema.md](/Users/daviddickinson/Projects/Lora/bildung-2.0/patterns/handle-schema.md:160), [sources/german/uexkuell-theoretische-biologie/glossary.yaml](/Users/daviddickinson/Projects/Lora/bildung-2.0/sources/german/uexkuell-theoretische-biologie/glossary.yaml:5)

3. **Trust comes from evidence chains, not fluent prose.**  
   Terms and claims are linked to explicit evidence handles and promotion follows evidence density and reuse, not rhetorical confidence.  
   [patterns/handle-schema.md](/Users/daviddickinson/Projects/Lora/bildung-2.0/patterns/handle-schema.md:86), [patterns/handle-schema.md](/Users/daviddickinson/Projects/Lora/bildung-2.0/patterns/handle-schema.md:166), [patterns/handle-schema.md](/Users/daviddickinson/Projects/Lora/bildung-2.0/patterns/handle-schema.md:203)

4. **Different texts are allowed different apparatus shapes.**  
   `Zeitmauer` is currently the strongest handle-first proving ground; `Erkenntnisproblem` is currently the strongest journal/ledger-first proving ground. The repo does not force one trace medium across all texts.  
   [texts/zeitmauer/README.md](/Users/daviddickinson/Projects/Lora/bildung-2.0/texts/zeitmauer/README.md:22), [texts/erkenntnisproblem-vol1/README.md](/Users/daviddickinson/Projects/Lora/bildung-2.0/texts/erkenntnisproblem-vol1/README.md:22), [00-Notes/process.md](/Users/daviddickinson/Projects/Lora/bildung-2.0/00-Notes/process.md:170)

5. **Bounded probes are allowed without quietly becoming campaigns.**  
   The repo can touch a prepared source once, under explicit pressure and with a narrow output contract, without treating that touch as a full source opening.  
   [2026-04-15-bounded-survey-encounters-as-middle-band.md](/Users/daviddickinson/Projects/Lora/bildung-2.0/00-Notes/working-syntheses/2026-04-15-bounded-survey-encounters-as-middle-band.md:1), [00-Notes/right-now.md](/Users/daviddickinson/Projects/Lora/bildung-2.0/00-Notes/right-now.md:1)

6. **Exploration and canon are filtered apart.**  
   Chats, extractions, experiments, working syntheses, distillations, and patterns do different jobs. Material only becomes canonical if it survives contact, contestation, and reuse.  
   [00-Notes/process.md](/Users/daviddickinson/Projects/Lora/bildung-2.0/00-Notes/process.md:9)

## Current operating shape

The repo is no longer only a forward-translation workspace.

It now operates across several linked modes:

- completed translation nodes with ongoing integration pressure
- active continuation lines where batching still makes sense
- bounded experiments and replay packets
- prepared but dormant source scaffolds held under trigger discipline

That is a change in operating shape, not in mission.

## What it is not

It is not primarily:

- a knowledge graph
- a digital humanities metadata project
- a simple translation archive
- a notes vault where everything is treated as the same kind of note

Those comparisons can be useful, but they are not the design center.

## What the design protects

This design tries to protect three things at once:

- source resistance
- replayable reasoning
- the ability to keep terms and threads live without forcing closure too early

## Use rule

Use this note when someone needs a quick explanation of how the repo is designed now.

Do not use it as a final pitch, publication blurb, or charter replacement. It is just a short, source-grounded summary of choices already on disk.
