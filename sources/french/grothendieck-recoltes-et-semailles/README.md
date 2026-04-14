# Grothendieck — *Récoltes et Semailles* — Source Campaign

Alexandre Grothendieck, *Récoltes et Semailles — Réflexions et témoignage sur un passé de mathématicien*, Tome I (Éditions Gallimard, 2021).

## What This Is

The primary French text of *Récoltes et Semailles* Tome I, split into navigable parts following Grothendieck's own sectioning. This exists so that conversational instances (LLM web chats, future agent encounters) can read specific passages at source-passage resolution without loading the full 1.6 MB / 8 800-line file at once.

This is a **text-only scaffold**, not yet a live encounter. No glossary, no journal, no encounter dossiers have been earned. The first-contact note is still at:

- `sources/modern/incoming/grothendieck/recoltes-et-semailles-first-contact.md`
- `sources/modern/incoming/2026-04-10-grothendieck-recoltes-et-semailles-first-contact.md`

Both predate this scaffold and document the first flicker of pressure toward opening the source. Neither has yet graduated into a full encounter.

## Why Here Rather Than Elsewhere

- Not `texts/recoltes-et-semailles/` — would be premature promotion to full subproject status. The April 13 Cassirer/Umwelt/Schicksalzeit chat established that Récoltes is structurally closer to the *Exegesis* decryption apparatus (passes and thread dossiers) than to the *Erkenntnisproblem* translation apparatus (parts and close-reading ledger), because the architectural content is buried in autobiography rather than laid out explicitly. Subproject shape is not yet clear.
- Not `sources/modern/` — that directory is for modern *concept encounters* (Rosen, von Foerster, Eilenberg-MacLane, Freedman) with lighter apparatus. Récoltes is a *primary text in a source language* and wants the fuller source-campaign pattern when it opens.
- `sources/french/` parallels `sources/german/uexkuell-theoretische-biologie/` (the most developed source-campaign apparatus in the repo) and places the work where French source-language encounter work belongs.

## Source

Canonical text file (gitignored archive copy):

- `sources/modern/incoming/books/Recoltes et Semailles I, II - Alexandre Grothendieck.txt`
  — Gallimard 2021 electronic edition, ISBN 9782072889790.
  — Contains Tome I: Prélude en quatre mouvements + Première Partie (Fatuité et Renouvellement) + Deuxième Partie (L'Enterrement (1) — ou la robe de l'empereur de Chine).

The split copies under `source/raw/` are what web chats and agents should read.

## Structure

```text
source/
  raw/                   # 130 split files, one per Grothendieck section
    000-front-matter.txt
    001-prelude-01-mouvement-i.txt
    002-prelude-02-mouvement-ii-promenade.txt
    003-prelude-02-01-magie-des-choses.txt
    ...
    127-part-ii-ch10-fourgon-funebre.txt
    128-back-matter-toc.txt
    129-back-matter-colophon.txt
  sections.yaml          # full section map: slug, title, kind, parent, line range, length
```

Not yet created (will be earned when the first live encounter runs):

- `source/normalized/` — cleaned working text with footnote pins
- `source/page-map.yaml` — tapuscrit `[◊ XN]` page markers mapped to section ranges
- `glossary.yaml` — unstable terms under pressure (seeds: `souffle`, `foi`, `innocence`, `bébête`, `topos`, `faisceau`, `point de vue` vs `vision`)
- `journal.md` — source-bound drift
- `encounters/` — encounter dossiers

## How To Navigate

Every split file begins with the section's own heading line (as Grothendieck wrote it) followed by the section body. The filename encodes the hierarchical position:

- `NNN-prefix-slug.txt`
  - `NNN` is a three-digit sequence number (000–129) giving reading order
  - `prefix` marks the top-level division:
    - `front-matter` — editor's note, dedication, title page
    - `prelude-01`, `prelude-02`, `prelude-03`, `prelude-04` — the four Mouvements of the Prélude
    - `part-i-ch1` .. `part-i-ch8` — Fatuité chapters (Roman numerals I–VIII)
    - `part-i-s01` .. `part-i-s50` — Fatuité numbered sections (1–50)
    - `part-i-notes` — Notes pour la première partie (the entire 563-line notes apparatus)
    - `part-ii-A`, `part-ii-B`, `part-ii-C`, `part-ii-D` — L'Enterrement lettered parts
    - `part-ii-ch1` .. `part-ii-ch10` — L'Enterrement Roman chapters
    - `back-matter-toc`, `back-matter-colophon` — end matter
  - `slug` is a de-accented, hyphenated form of the section title

The `sections.yaml` file is the authoritative index. It records, for each split file, the original body line range, the parent section (if any), and the structural `kind`. Use it when you need to map a passage back to its Grothendieck-canonical position or when building cross-references.

### Granularity notes

- **Prelude** (Mouvements I–IV) is split at the finest level Grothendieck uses. The Promenade (Mvt II) has 22 named sub-sections, Une Lettre (Mvt III) has 17, Introduction (Mvt IV) has 10.
- **Fatuité et Renouvellement** is split at the numbered-section level (50 sections across 8 chapters). Chapter headers sit in their own short files to preserve the *Sommaire* listings and date stamps.
- **Notes pour la première partie** is kept as a single 563-line file. The internal "Note 1, Note 2, …" structure could be split further, but hasn't been — the notes apparatus tends to reference things that only make sense relative to its container.
- **L'Enterrement** is split at the Roman-chapter level (10 chapters) plus the lettered parts (A/B/C/D) as their own container files. Individual named notes within each chapter (e.g. "Mes orphelins", "Refus d'un héritage", "Le colloque", "Le massacre") are NOT split out — they live inside the chapter file. Chapter 9 (*Mes élèves*) is 1056 lines and chapter 10 (*Le Fourgon Funèbre*) is 720 lines; these are the largest files in the set and reflect Grothendieck's own density.

## Splitting Methodology

The split was produced by a hand-curated line-number map, not by automatic detection. The detection heuristics tried first (all-caps patterns, "prose immediately after heading", SKOS-style structural matching) each failed on at least 20 edge cases:

- Promenade sub-section titles are bare (e.g. `La magie des choses`)
- Fatuité sub-sections use `(N) Title` format
- L'Enterrement chapter headers in the body use standalone Roman numeral + ALL-CAPS title on the next line — the `I. L'élève posthume` forms only appear in *Sommaire* listings, not in the body
- Introduction (Mvt IV) sub-sections use `N. Title` dotted format
- Section (10) of Fatuité (*La « communauté mathématique »…*) wraps its title across two body lines with a colon break
- Some titles include trailing ellipsis or suffix clauses in the body but not in the TOC

Rather than harden the heuristics against every edge case, the final splitter uses a hand-verified `(line_number, kind, slug, title, parent)` tuple list. The splitter script is preserved at `tools/split_recoltes.py` for reproducibility and for any future re-split (e.g. if Tome II arrives).

## Status

- 2026-04-13: Scaffold created. Text split into 130 parts, `sections.yaml` written. No encounter work has begun.
- `right-now.md` still holds the three trigger conditions for promoting the first-contact note into a live encounter. None have fired yet. The existence of the split should not be read as a live encounter in progress — it is infrastructure for the encounter that may later be earned.
