# Langer PNK Page Proof Manifest

Authority: `sources/modern/incoming/books/Philosophy in a New Key, Suzanne K. Langer.pdf`

Rendered images: `/tmp/pnk_langer_pages/pnk-NNN.png`, produced from all 255 PDF pages at 180 dpi with `pdftoppm`.

Deliverable target: clean source text only. Preserve headings, paragraphs, page markers, footnotes, acknowledgments, suggested reading, index entries, and any retained publisher matter. Do not transform this corpus into audiobook script formatting.

## Scope Notes

- PDF page 001 is the scanned cover/wrap. It is not currently included in the cleaned text corpus.
- PDF pages 002-009 are unnumbered front matter and preface pages included in the cleaned text.
- Printed pages 1-75 map to PDF pages 010-084.
- Printed pages 76-77 are missing from this PDF. The current corpus fills them from the raw text witness; they cannot be page-image-proofed from this PDF unless another scan is supplied.
- Printed pages 78-239 map to PDF pages 085-246.
- PDF pages 247-249 are unnumbered back matter between printed page 239 and the index: acknowledgments, suggested reading, and a publisher catalog page. Logical pagination implies pp. 240-242, but no page numbers are printed on the images.
- Printed index pages 243-248 map to PDF pages 250-255.
- `001-preface-to-the-second-edition.txt` is retained from the raw witness only; it is not present in this PDF and cannot be verified from these page images.

## Proof Status

| cleaned file | PDF / printed range | status | notes |
| --- | --- | --- | --- |
| `000-title-pages-and-publisher-matter.txt` | PDF 002-005, unnumbered | visually checked | Page images opened; wording matches the included front matter; printing lines and title matter are now formatted cleanly. |
| `003-contents.txt` | PDF 006, unnumbered | visually checked | `ON SIGNIFICANCE IN Music` is printed exactly this way and should remain. |
| `002-preface-to-the-first-edition.txt` | PDF 007-009, unnumbered | visually checked | Page images opened; no corrections made yet. |
| `010-the-new-key.txt` | printed 1-20, PDF 010-029 | visually proofed | PDF p. 010 has a damaged-looking `AGE` glyph read by OCR as `ACE`; text correctly keeps `AGE`. |
| `011-symbolic-transformation.txt` | printed 20-42, PDF 029-051 | visually proofed | Printed pp. 20-42 checked against images; direct manual corrections made in the cleaned file and not yet folded into the cleaner. Shared boundary with chapter 3 remains in `012-the-logic-of-signs-and-symbols.txt`. |
| `012-the-logic-of-signs-and-symbols.txt` | printed 42-63, PDF 051-072 | visually proofed | Printed pp. 42-63 checked against images; direct manual corrections made in the cleaned file and not yet folded into the cleaner. Shared boundary with chapter 4 remains in `013-discursive-forms-and-presentational-forms.txt`. |
| `013-discursive-forms-and-presentational-forms.txt` | printed 63-83, PDF 072-090 plus raw-only pp. 76-77 | available images visually proofed; raw gap normalized | Printed pp. 63-75 and 78-83 checked against images; printed pp. 76-77 normalized from the raw witness only. Direct manual corrections made in the cleaned file and not yet folded into the cleaner. PDF jumps from printed p. 75 to p. 78; printed pp. 76-77 remain unavailable for image proof. |
| `014-language.txt` | printed 83-116, PDF 090-123 | partial visual proof in progress | Printed pp. 83-94 checked against images; direct manual corrections made in the cleaned file and not yet folded into the cleaner. Shared boundary pages require chapter-overlap checking. |
| `015-life-symbols-the-roots-of-sacrament.txt` | printed 116-138, PDF 123-145 | pending full page proof | Shared boundary pages require chapter-overlap checking. |
| `016-life-symbols-the-roots-of-myth.txt` | printed 138-165, PDF 145-172 | pending full page proof | Shared boundary pages require chapter-overlap checking. |
| `017-on-significance-in-music.txt` | printed 165-199, PDF 172-206 | pending full page proof | Shared boundary pages require chapter-overlap checking. |
| `018-the-genesis-of-artistic-import.txt` | printed 199-216, PDF 206-223 | pending full page proof | Shared boundary pages require chapter-overlap checking. |
| `019-the-fabric-of-meaning.txt` | printed 216-239, PDF 223-246 | pending full page proof | Shared boundary pages require chapter-overlap checking. |
| `030-acknowledgments.txt` | PDF 247-249, logical pp. 240-242 | visually checked | Rebuilt from page images with inferred logical markers `[page 240]`-`[page 242]`; publisher catalog page retained and cleaned. |
| `031-index.txt` | printed 243-248, PDF 250-255 | partially image-repaired | Printed pp. 247-248 were image-repaired earlier; the full index still needs page-by-page proof. |
| `001-preface-to-the-second-edition.txt` | not in PDF | raw witness only | Needs separate witness decision; cannot satisfy PDF page-image proof. |

## Page Batch Ledger

| printed / logical pages | PDF pages | status | corrections |
| --- | --- | --- | --- |
| unnumbered front matter | 002-006 | visually checked | Reformatted title/publisher matter; confirmed `ON SIGNIFICANCE IN Music`. |
| unnumbered first-edition preface | 007-009 | visually checked | No text corrections made. |
| 1-5 | 010-014 | visually proofed | Removed stray page number `1`; separated footnotes 1, 2, and 6 from running text. |
| 6-10 | 015-019 | visually proofed | Corrected OCR/format defects: `issues`, `ready-made`, `deep emotional`, `deep-rooted`, `amusement`, `became`, `limit`, `mind?`, dash spacing, and `philosophy`. |
| 11-15 | 020-024 | visually proofed | Corrected `life`, `fact-finding`, `Greco-Roman`, `hard-headed`, question-mark spacing, em-dash spacing, and `sense-experiences`. |
| 16-20 | 025-029 | visually proofed | Corrected `all at once`, footnotes 11-22, `symbol-using`, `Weltanschauung`, `vivifying`, `reasonable—but`, `evaluation`, and removed page-header fragments. |
| 21-25 | 030-034 | visually proofed | Corrected `animal$`, separated footnotes 1-4, restored `self-assertion`, repaired the `Nihil` quote opening, and split the Lorimer block quotation to match the page image. |
| 26-30 | 035-039 | visually proofed | Removed page 26 running-header fragments; split Chase quotation paragraphs; corrected footnote 6, `error-quotient`, and `experiences?`. |
| 31-35 | 040-044 | visually proofed | Corrected `because he`, `mind-Stuff`, `physical object`, footnote 7, `blood vessels`, `ideas—streams`, `symbolific activity—as`, and footnotes 8-10. Page 34 uses an inline marker in `super-switch[page 34]board` because the printed page break falls inside the word. |
| 36-42 | 045-051 | visually proofed | Separated and corrected footnotes 11-19; corrected `post-Revolutionary`, `dog-dances`, `standing-ground`, `Totem and Taboo. 19`, and `anything—out`. Preserved printed `past recognition` on p. 36. |
| 42-47 | 051-056 | visually proofed | Began chapter 3 shared-boundary proof; separated footnotes 1-5, corrected `denotation-or-connotation`, `A-in-relation-to-B`, dash spacing, and `ended—school`; represented the missing musical notation examples with bracketed `[music example: ...]` placeholders. |
| 48-52 | 057-061 | visually proofed | Corrected `psychology`, `sign-using`, `sign-meaning`, separated footnotes 6-8, restored Helen Keller quotation paragraphs, corrected `conceptual sign,`, `object`, and `H2O`. Page 53 marker is inline in `mean[page 53]ing-relation` because the printed page break falls inside the word. |
| 53-57 | 062-066 | visually proofed | Restored Willy rhyme lineation; corrected `peculiarity`, `propositional`, `symbolific`, `object`, `long-tailed`, `each other`, and dash artifacts; separated footnotes 9-10; added bracketed figure placeholders for figs. 1-2. Page 56 and 57 markers are inline at word boundaries to avoid splitting prose with footnote blocks. |
| 58-63 | 067-072 | visually proofed | Corrected `the real`, `word-endings`, foreign-title accents, footnotes 11-14, Russell quote punctuation, `language?`, Greek phi formulas, and added a bracketed numeric-pattern placeholder. Page 59, 60, 62, and 63 markers are inline at word boundaries. |
| 63-67 | 072-076 | visually proofed | Began chapter 4 shared-boundary proof; reformatted Wittgenstein quotation blocks; separated footnotes 1-3; restored Carnap paragraphs; corrected `pseudo-proposition`, `com[page 65]plex`, and `dis[page 67]tinctions` page-boundary splits. |
| 68-72 | 077-081 | visually proofed | Cleaned Carnap, Russell, and Wittgenstein quote blocks; separated footnotes 4-11; corrected `time-honored`, `talking?`, `language 9`, `neo-positivistic`, `by no means`, `formulation`, and the Coleridge footnote; kept p. 68 marker inline in `mu[page 68]sic`. |
| 73-75 | 082-084 | visually proofed | Cleaned Gestalt passage and footnote 12; corrected spurious quote before `did not see`, `Drei Abhandlungen zur Gestalttheorie`, `propositional thought`, Reid parenthesis spacing, and the p. 75 to raw-only p. 76 duplicate `we`. |
| 76-77 | no PDF image | raw witness normalized | PDF has no images for printed pp. 76-77. Normalized paragraphing, removed raw line-break damage (`mean-ing`, `sym-bol`, `ob-viously`), corrected dash spacing in `symbols—qualities, lines, rhythms—may`, removed a stray quote before `substitution`, and joined `Rogues' Gallery`. |
| 78-83 | 085-090 | visually proofed | Finished chapter 4 image-backed pages; restored paragraph breaks around nonverbal symbolism, presentational symbolism, Bergson/Creighton passages, music, and the closing transition; separated footnotes 13-18; corrected Bergson and Creighton citation OCR, `phenomenon`, `goal." 17`, `mind." 18`, and page-boundary markers at p. 78, p. 82, and p. 83. |
| 83-89 | 090-096 | visually proofed | Began chapter 5 shared-boundary proof; cleaned title and opening paragraphs; separated footnotes 1-12; corrected the long Kingsley/Sapir note, Yerkes/Kellogg/Hale citations, `food-bark`, `denotative words`, `Savage of Aveyron`, and the duplicated p. 87/88 continuation. |
| 90-94 | 097-101 | visually proofed | Corrected the Köhler passages and citations; separated footnotes 13-24; restored p. 93 `prising` and p. 94 `resentation` continuations; cleaned the symbolic-gesture paragraphs, `ba-ba`, `signification—all are pragmatic or emotional—that`, Clarence Day passage, and `This Simian World`. |
| 240-242 inferred | 247-249 | visually proofed | Rebuilt acknowledgments, suggested reading, and retained publisher catalog from page images. |
| 243-248 index | 250-255 | partial | Printed pp. 247-248 image-repaired; full index still pending page-by-page proof. |

## Open Proof Blockers

- Find or supply page images for printed pp. 76-77 if strict image proof is required for those pages.
- If the publisher catalog page at PDF p. 249 should be excluded from the reading corpus, remove it intentionally after proof rather than as OCR fallout.
- Unnumbered logical pages 240-242 are labeled with inferred `[page N]` markers so index pagination stays continuous; this remains a documented editorial choice.
- Decide whether the raw-only second-edition preface remains in this PDF-authority corpus or moves to a separate witness file.
