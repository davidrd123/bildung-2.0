# Translation Methodology

Status: bounded pilot method. This is not a full translation campaign and not
repo-wide methodology.

## Governing Judgment

Use *Внутри мыслящих миров* as a source-facing encounter only where it puts
pressure on live repo practice. The current source is an OCR browsing scaffold,
so no fine lexical claim, quotation discipline, or glossary promotion is valid
without checking the scan.

The first legitimate mode is therefore not linear translation. It is a bounded
encounter packet:

- one live axis
- one checked or explicitly unchecked passage range
- close English draft
- readable English draft where useful
- term-pressure table
- residue / strain report
- one adversarial note on what might be wrong
- a decision about what the packet does and does not license

## Checked Source Rule

The DjVu at `sources/modern/incoming/books/vnutri-mislyashih-mirov.djvu` has no
embedded text layer. For active passages, render only the needed pages and make
a small checked working text under `source/checked/`.

Use the checked file as authority only for its stated range. Do not let one
checked packet silently upgrade the status of `source/raw/`.

## Reader-En Pass

The `source/reader-en/` pass is allowed to be broad because its purpose is
access: English reading, web discussion, and audiobook/TTS preparation. It is
not a critical translation and does not, by itself, admit Lotman into the
project apparatus.

Each reader file should correspond to one source section from
`source/sections.yaml`, using the same sequence and slug:

```text
source/reader-en/005-part-i-01-tri-funktsii-teksta.md
```

Each file should contain:

- title and source section
- status line: `reader draft`, `scan-backed where noted`, or `needs source
  check`
- source basis: the `source/raw/` file and any `source/checked/` file consulted
- a short note that the file is for reading/audio, not quotation-grade citation
- the English reader translation
- end-of-file pass notes for source uncertainties, possible encounter
  candidates, and TTS cleanup needs

Translation style:

- translate paragraph-by-paragraph in source order
- preserve argument structure and technical recurrence
- split overloaded Russian periods when needed for audible English
- keep headings and major section breaks
- avoid footnote-like interruptions in the reading flow
- use plain bracketed flags only where the source is unclear, for example
  `[source check]`
- do not force glossary stabilization while translating

When a reader pass notices a structurally important term or claim, record it as
a pass note or journal candidate. Promote it into `source/glossary.yaml`,
`encounters/`, `threads/`, or handles only after a checked source-facing
encounter earns that move.

## Why This Is A Hybrid

The Cassirer workflow contributes the right treatment for Lotman's prose:

- paragraph-cluster units rather than aphorisms or arbitrary pages
- just-in-time source correction for the active passage only
- a close-reading ledger function for local findings that are too important to
  lose but too small for synthesis
- glossary entries only for recurring conceptual pressure

The Zeitmauer workflow contributes the right treatment for Lotman's recurrence
network:

- keep the glossary lean
- treat open terms as positive evidence, not failure
- use evidence only after recurrence, not on first fluency
- create thread dossiers only when a pattern survives across multiple passages

Lotman especially needs both disciplines because his vocabulary is tempting as a
metalanguage. The method must preserve what he sharpens without replacing the
repo's earned vocabulary with Lotman's.

## Initial Axes

Only three axes are currently earned enough for bounded reread:

1. `minimal-paired-heterogeneity` - non-identical languages linked by translation
   as the minimal generator of new messages.
2. `autocommunication` - self-address as reformulation under a second code and
   shifted context, able to restructure the self.
3. `history-as-decryption` - historical fact as the result of deciphering texts
   produced under other codes.

Start with one axis. Do not widen to semiosphere, boundary, dialogue, memory, and
history all at once.

## Packet Template

Each encounter packet should include:

```text
Status
Axis
Source Anchors
Source Status
Why This Passage
Close English
Readable English
Term Pressure
Residue / Strain Report
Adversarial Note
What This Sharpens
What This Does Not License
Next Check
```

`Readable English` is optional. When the close version is already usable, do not
multiply versions for display.

## Glossary Rule

Create or revise `source/glossary.yaml` only when the term is structurally active
in the packet. Every seed entry must state whether it rests on raw OCR or a
DjVu-backed active passage.

Good seed entries name a pressure, not a decision:

- Russian term
- handle
- status
- provisional rendering options
- source anchors
- why it matters
- what would settle or revise it

## Thread Rule

No thread dossier is earned by a single Lotman packet. A thread becomes live only
after one problem survives at least three source-facing encounters or is needed
by a specific active subproject.

## Parallax Rule

Stereoscopic / parallax translation may be used only as a strain report. It is
heuristic, not evidence. It must say:

- what the second rendering exposed
- what it may have fabricated
- what would audit the result

The first Lotman axis may use parallax because Lotman's own claim concerns
non-identical languages and translation. That thematic fit does not make the
method generally licensed.

## Promotion Gate

After three packets, decide whether Lotman remains a bounded method-sidecar or
has earned a fuller local apparatus.

To promote, the packets must show at least one of:

- a term whose pressure cannot be handled by existing notes
- a repeated structure that changes how an active translation project works
- a negative result strong enough to block a tempting but false repo synthesis

Confirmation alone is not promotion.
