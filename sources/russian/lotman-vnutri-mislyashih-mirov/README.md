# Lotman — *Внутри мыслящих миров* — Text-Only Scaffold

Ю. М. Лотман, *Внутри мыслящих миров: Человек — текст — семиосфера — история* (Москва: Языки русской культуры, 1996).

## What This Is

A split, navigable scaffold of *Внутри мыслящих миров* for passage-level browsing in web chats and lightweight agent work.

This exists for the same reason as [Grothendieck's scaffold](/Users/daviddickinson/Projects/Lora/bildung-2.0/sources/french/grothendieck-recoltes-et-semailles/README.md): so a conversation can read a chapter-sized passage without loading the whole book at once.

This is **not** a full translation campaign and **not** a source-critical working
text. It is an OCR-derived browsing scaffold with one bounded encounter pilot
now attached.

## Status

- The source here was generated from a local DjVu with no embedded text layer.
- The split files under `source/raw/` come from a cleaned OCR reading copy.
- The text is good enough for orientation, browsing, and exploratory web chat.
- It is **not** good enough for fine term-pressure work, quotation discipline, or glossary building without checking the scan.
- The first encounter packet now has one DjVu-backed checked working text under
  `source/checked/`.
- Access layers may include `raw`, `cleaned`, `reader-en`, and `tts`. These can
  support reading, discussion, and audiobook/TTS use without becoming critical
  apparatus.

The bounded method notes remain:

- [00-Notes/method/lotman-incoming.md](/Users/daviddickinson/Projects/Lora/bildung-2.0/00-Notes/method/lotman-incoming.md)
- [00-Notes/method/lotman-vnutri-first-contact.md](/Users/daviddickinson/Projects/Lora/bildung-2.0/00-Notes/method/lotman-vnutri-first-contact.md)

Local pilot additions:

- `methodology.md` — bounded Lotman encounter method
- `journal.md` — local pilot state
- `source/checked/001-minimal-paired-heterogeneity.ru.txt` — DjVu-backed
  working text for the first active passage range
- `source/reader-en/` — English reader drafts for discussion/audio use
- `source/reader-en/manifest.yaml` — pass state for reader drafts
- `source/tts/` — future audio-ready exports derived from `reader-en`
- `source/tts/manifest.yaml` — pass state for audio-ready exports
- `source/glossary.yaml` — seed glossary from encounter packets only
- `encounters/` — bounded source-facing packets

Nothing in this scaffold should be read as promotion beyond that status.

## Why Here

- Not `00-Notes/method/`: that shelf is for method notes, not source text.
- Not `sources/modern/`: this is a Russian primary text, not a modern concept encounter.
- `sources/russian/` is the least misleading place for a source-language scaffold that may be useful for later passage work without yet earning glossary, journal, or encounter apparatus.

## Structure

```text
source/
  raw/                   # split OCR-derived text files
  cleaned/               # optional cleaned Russian reading text
  checked/               # active-passage scan-backed working texts
  reader-en/             # English reader drafts; not quotation-grade
  tts/                   # optional audio-ready exports
  sections.yaml          # sequence, title, kind, line range
  glossary.yaml          # seed terms from bounded encounter packets
encounters/              # bounded source-facing packets
journal.md               # local pilot state and method drift
methodology.md           # local method for Lotman packets
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
- `source/cleaned/`
- full translation `parts/`
- `threads/`
- `source/handles.yaml`

## How To Use

- Read `source/raw/*.txt` when you want chapter-scale access.
- Read `source/checked/*.txt` when a packet needs scan-backed passage authority.
- Read `source/reader-en/*.md` when you want English chapter-scale discussion or
  audiobook preparation.
- Use `source/sections.yaml` when you need the order, title, and original line span.
- Use `encounters/*.md` only as bounded method packets.
- Treat the raw scaffold and `reader-en` drafts as access aids, not as stable
  lexical sources.

If the book earns stronger live pressure, extend checked working text only for
the active passage range. Until then, the pilot remains bounded and OCR-aware.
