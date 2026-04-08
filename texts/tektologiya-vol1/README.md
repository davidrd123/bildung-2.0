# Tektologiya Vol. 1 - Translation Project

Alexander Bogdanov, *Всеобщая организационная наука (тектология)*, volume 1 in the 1989 reprint.

## Scope

This project tracks a working English translation of Bogdanov's volume-1 main text, with front matter retained as a secondary but real part of scope.

- Source FB2: `../../books/Bogdanov/Тектология (всеобщая организационная наука) -- 1989.fb2`
- Source facsimile: `../../books/Bogdanov/Тектология_ Всеобщая организационная наука кн_1.djvu`
- Immediate scope: volume-1 front matter plus the main text headed `Том 1`

## Current Status

The translated first pass through the volume-1 main text is now complete:

- `18` part files
- chapters `1-5`
- leaf units `1.1` through `5.4`

So the immediate work is no longer extending the main-text sequence. It is bounded consolidation:

- tightening glossary statuses only where the full volume earned it
- keeping one reread memo for the load-bearing arc of volume `1`, now extended by the earned outer framing from `front.04-10`
- approaching front matter selectively rather than turning it into an automatic second linear march
- beginning a first architectural visual packet from the journal's earned diagram candidates

That selective front-matter pass has now been carried through the main authorial and late framing units:

- `front.04` through `front.10`
- with `front.01-03` still remaining secondary editorial material rather than the active entry path

## Why This Is Not `zeitmauer` or `erkenntnisproblem`

The source is already structured enough to extract directly from the FB2, but the work is neither a flat sequence of numbered prose blocks nor an OCR-heavy page workflow. It is a nested hierarchy:

- front matter
- volume
- chapters
- lettered subgroups in some chapters
- numbered `§` sections in some but not all of those groups

For that reason the workflow here is:

- one reproducible FB2 extractor
- leaf-level translation units rather than page tranches
- a lean glossary for terms that immediately start governing the argument
- small calibration batches before any attempt to widen into a full-volume march

## Structure

```text
source/
  outline.yaml          # front matter and main-text hierarchy derived from the FB2
  front-matter.yaml     # extracted front matter units
  sections.yaml         # extracted leaf units from `Том 1`
  glossary.yaml         # recurring term decisions and active pressure points
parts/
  01-calibration.md     # initial translation batch
selective-second-pass.md # bounded consolidation memo for the main-text arc plus the earned front-matter outer arc
what-tektologiya-is-for-in-bildung.md # bounded local positioning note for repo-level use
journal.md              # source-bound process notes and decision drift
visuals/
  packet-01-volume-1-architecture.md # first curated set of architectural diagram drafts
scripts/
  extract_sections.py   # rebuilds the extracted source files from the FB2
```

## Working Method

1. Regenerate the extracted source files from the FB2 when needed.
2. Translate in small batches anchored to leaf sections.
3. Record unstable terms in `source/glossary.yaml`.
4. Keep source-bound decisions in `journal.md`.
5. Use the DJVU only as a facsimile check when the FB2 wording looks suspicious.

After a bounded sequential run is complete, prefer one selective reread memo before widening into a new track.

The source is structurally cleaner than a raw OCR text, but it should still be treated as a working source rather than unquestioned authority. Obvious scan-era oddities can be corrected during active tranches instead of pre-cleaning the whole book.

## Calibration Bias

The first batch should stay deliberately small:

- `1.1` (`§ 1. Организационная точка зрения`)
- `2.a.1` (`§ 1. Организованные комплексы`)

That pair is enough to test:

- the title language around `тектология`
- whether `комплекс` can stay `complex`
- how to handle `организованность / дезорганизованность`
- how much of Bogdanov's recursive terminology can be carried without deadening the English

## Regeneration

```bash
python3 texts/tektologiya-vol1/scripts/extract_sections.py
```

The extractor is intentionally conservative. It preserves the FB2 hierarchy, splits out front matter from the main volume, and keeps note markers visible rather than silently deleting them.

## Visual Candidates

The journal now contains a dense set of earned `[visual candidate]` notes. The
first curated packet lives in
[`visuals/packet-01-volume-1-architecture.md`](visuals/packet-01-volume-1-architecture.md)
and stays focused on the architecture of volume `1` rather than section-level
illustrations.
