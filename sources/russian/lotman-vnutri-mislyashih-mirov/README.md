# Lotman — *Внутри мыслящих миров* — Text-Only Scaffold

Ю. М. Лотман, *Внутри мыслящих миров: Человек — текст — семиосфера — история* (Москва: Языки русской культуры, 1996).

## What This Is

A split, navigable scaffold of *Внутри мыслящих миров* for passage-level browsing in web chats and lightweight agent work.

This exists for the same reason as [Grothendieck's scaffold](/Users/daviddickinson/Projects/Lora/bildung-2.0/sources/french/grothendieck-recoltes-et-semailles/README.md): so a conversation can read a chapter-sized passage without loading the whole book at once.

This is **not** a live encounter and **not** a source-critical working text. It is an OCR-derived browsing scaffold.

## Status

- The source here was generated from a local DjVu with no embedded text layer.
- The split files under `source/raw/` come from a cleaned OCR reading copy.
- The text is good enough for orientation, browsing, and exploratory web chat.
- It is **not** good enough for fine term-pressure work, quotation discipline, or glossary building without checking the scan.

The bounded method notes remain:

- [00-Notes/method/lotman-incoming.md](/Users/daviddickinson/Projects/Lora/bildung-2.0/00-Notes/method/lotman-incoming.md)
- [00-Notes/method/lotman-vnutri-first-contact.md](/Users/daviddickinson/Projects/Lora/bildung-2.0/00-Notes/method/lotman-vnutri-first-contact.md)

Nothing in this scaffold should be read as promotion beyond that status.

## Why Here

- Not `00-Notes/method/`: that shelf is for method notes, not source text.
- Not `sources/modern/`: this is a Russian primary text, not a modern concept encounter.
- `sources/russian/` is the least misleading place for a source-language scaffold that may be useful for later passage work without yet earning glossary, journal, or encounter apparatus.

## Structure

```text
source/
  raw/                   # split OCR-derived text files
  sections.yaml          # sequence, title, kind, line range
```

Current granularity:

- front matter
- contents
- Ivanov preface
- the two introduction sections
- the major chapters of Parts I–III
- the four internal essays under `Символические пространства`
- conclusion, bibliography, appendices, indices

Not yet created:

- `source/normalized/`
- `journal.md`
- `glossary.yaml`
- `encounters/`

## How To Use

- Read `source/raw/*.txt` when you want chapter-scale access.
- Use `source/sections.yaml` when you need the order, title, and original line span.
- Treat this as a browsing aid, not as a stable lexical source.

If the book ever earns live pressure, the next honest move would be a checked working text for whichever bounded axis wakes first. Until then, this scaffold is just navigational infrastructure.
