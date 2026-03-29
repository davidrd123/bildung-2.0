# An der Zeitmauer - Translation Project

Ernst Jünger, *An der Zeitmauer* (1959)

## Scope

This project tracks a working English translation of Jünger's main text in numbered units.

- Source corpus: sections `1-186` from `../books/An der Zeitmauer_ Mit Adnoten v - Ernst Jnger;.txt`
- Excluded from the translation corpus: Detlev Schöttker's adnotes and the appended author bio
- Default translation unit: the numbered section, not the sentence and not the full chapter

## Why This Is Not `escolios`

The `escolios` workflow is built for short aphorisms. Jünger is working in numbered prose blocks that develop an argument across pages. For that reason this project uses:

- one primary draft translation per section
- alternate phrasings only for crux terms or unstable passages
- notes where the German is genuinely difficult
- commentary mostly at the batch level, not for every paragraph

## Structure

```text
source/
  sections.yaml        # extracted German source, sections 1-186 only
  glossary.yaml        # key term decisions and unresolved concepts
parts/
  01-fremde-voegel.md  # translation batches in reading order
journal.md             # process notes, open problems, drift in decisions
scripts/
  extract_sections.py  # rebuilds source/sections.yaml from the ebook text
```

## Section Map

- `1-3`: `Fremde Vögel`
- `4-31`: `Meßbare und Schicksalszeit`
- `32-84`: `Humane Einteilungen`
- `85-166`: `Siderische Einteilungen`
- `167-186`: `Urgrund und Person`

For sections `32-166`, the larger frame title remains `An der Zeitmauer`.

## Working Method

1. Regenerate `source/sections.yaml` from the source text when needed.
2. Translate in small sequential batches.
3. Record unstable terms in `source/glossary.yaml`.
4. Keep stylistic and conceptual notes in `journal.md`.
5. Revisit earlier batches after the major terms settle.

The starting batch should stay small, usually `3-5` sections, until the title language and core philosophical vocabulary stop drifting.

## Regeneration

```bash
python3 zeitmauer/scripts/extract_sections.py
```

The extractor is intentionally simple and reproducible. It preserves the numbered prose units and drops the later adnotes.
