# Targeted Cleanup Risks

Status: post-campaign risk note after the first full source-local translation
pass. This records what was checked and what remains unresolved.

Date: 2026-05-08

## Latin

The verse and Latin insertions are translated literally enough for source-local
draft use, but they have not had a dedicated Latinist pass.

Primary local pressure:

- `parts/003-ai-principi-de-l-universo.md`
- Latin tags in the dialogues, especially Polihimnio's pedantic register

Current policy: preserve literal sense and image order, and do not polish the
Latin-derived English beyond the source-local draft until a separate Latin
check is done.

## Plain-Text Joined-Word Artifacts

The current source witness includes joined forms that look like e-text
artifacts rather than Bruno spellings:

- `source/raw/002-argomenti.txt:13`: `efficiente,etè`
- `source/raw/002-argomenti.txt:13`: `partietescrementi`
- `source/raw/002-argomenti.txt:13`: `Orcoetavaro`

The translation in `parts/002-argomenti.md` silently separates the obvious
words and records the source issue in its Translation Pressure section.

Current policy: leave the raw source unchanged; correct the English where the
separation is obvious; revisit against another witness before canonical
promotion.

## Missing Figures

The fifth dialogue requires three geometrical figures, but the local plain-text
source only supplies markers:

- `source/raw/008-dialogo-quinto.txt:48`: `Figura 1.`
- `source/raw/008-dialogo-quinto.txt:56`: `Figura 2.`
- `source/raw/008-dialogo-quinto.txt:66`: `Figura 3.`

The working translation preserves these as figure markers in
`parts/008c-dialogo-quinto-contraries-and-final-one.md`.

Current policy: do not invent diagrams in the source-local scaffold. A promoted
edition should recover the figures from a facsimile or reconstruct them in a
separate editorial apparatus, with the reconstruction status clearly marked.

## Names

The source-local draft preserves or lightly Anglicizes names without settling a
normalization policy.

Names requiring later policy:

- `Mauvissiero` / `Mauvissiere`: source form in title and patronage context;
  the working English currently uses both source-like and normalized forms.
- `Michel di Castelnovo`: preserved as `Michel of Castelnovo` in English.
- `Alessandro Dicsono Arelio`: kept as source-visible in the dialogue
  apparatus and speaker labels.
- `Polihimnio` / `Poliinnio` / `Poliinnia`: keep distinct because Bruno uses
  the pedant/muse contrast and the orthographic satire as part of the argument.

Current policy: do not normalize names globally inside the source-local draft.
For a public edition, make a name table with source form, historical
identification if source-backed, and reader-facing form.

## Promotion Consequence

None of these risks blocks the source-local scaffold. All of them block a
polished canonical edition.

Before promotion to a `texts/` project, run:

- a Latin check,
- a second witness or facsimile check for joined artifacts and names,
- recovery or marked reconstruction of the three figures,
- a single editorial policy for names and figure captions.

