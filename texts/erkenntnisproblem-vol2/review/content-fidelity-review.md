# Content Fidelity Review Standard

This is the reviewer-side companion to `texts/erkenntnisproblem-vol2/review-checklist.md`. Use it when a review needs to claim more than structural cleanliness for a part file in `texts/erkenntnisproblem-vol2/parts/*.md`.

The lesson from the Parts 044-048 review tranche is simple: **structural review is not content review**. The tranche passed every cross-file consistency check (glossary entries threading correctly, journal/ledger/page-map aligned, page-bridge stitching clean) and the verdicts were nevertheless not earned at content-fidelity level. A reviewer who reads the part file, normalized source, glossary, journal, ledger, page-map, and session-ledger cross-references — and stops there — has completed a structural review. The source-language quotations have not been verified.

## What Failed Last Time

The Parts 044-048 reviews were approved on:

- boundary cleanness (PDF/printed page coverage, scan files listed in page-map at trust:high)
- cross-file consistency (glossary updates threading through, ledger entries matching journal)
- page-bridge stitching (paragraphs reassembled from cross-page text in normalized source matched part body)
- key-term spot-checks (a handful of vocabulary choices in Notes/Translation note)
- glossary routing discipline (entries opened, updated, or deferred against the project's "absorption before promotion" pattern)

None of those checks:

- quoted specific Latin from Cassirer's footnotes and walked through the English rendering clause by clause
- opened Locke's `Essay` (or Cudworth/Norris) to verify Cassirer's German rendering preserved the cited English
- opened a JP2 scan to verify the normalized source itself captured the full printed page (the scan → OCR → normalized → part chain has multiple risk steps; cross-file consistency only audits the last step)
- systematically tested for compression (silently dropped clauses) or gloss-creep (smoothed paraphrase replacing literal rendering), the two failure modes named in `review-checklist.md`

The reviewer mistake was issuing "passes review at controlled-draft tier" verdicts where the actual content-fidelity work was limited to:

- spotting one or two vocabulary choices in passing
- restating the Notes' Translation note as if it had been independently verified
- assuming that German body density equaled scan density because the part body matched the normalized source

The single content-level investigation across the tranche (paragraph-break check at Part 048's PDF 259→260, done by opening the raw OCR) found a real issue. Sample size of one is not a pattern; it is a near-miss.

## The Translation Chain Has Multiple Links

Each link can fail independently. The reviewer must keep them distinct:

- **Scan → OCR → normalized source.** Scan dust, marginalia, footnotes spanning pages, hyphenation across line breaks, indent loss in OCR. The normalized source is an extracted approximation, not the printed page.
- **Cassirer's German prose.** Cassirer is often translating Latin/French/English into German. His renderings can be tight or loose; either way, the German body is the part file's primary text.
- **Cassirer's source-language footnote quotations.** Latin and French quotations carry source evidence at primary level. Errors at this layer escape into the part directly.
- **German body → Draft English.** The translator's main work, judged most often.
- **English re-translation of English originals.** When Cassirer quotes Locke/Cudworth/Norris in English, the part's Draft re-translates Cassirer's German rendering back into English. A clean re-translation of a tight rendering is fine; a clean re-translation of a loose rendering preserves Cassirer's smoothing as if it were the original.

Asserting that the chain is sound without testing any link earns no verdict beyond "structural clean."

## Verdict Tiers

Use split verdicts. Do not let `controlled draft`, `reviewed`, or `passes the gate` blur what was actually checked.

- **Structural clean**: boundaries, page-map, journal, ledger, glossary, footnote callouts, YAML, diff hygiene, and obvious OCR residue have been checked. This tier can support controlled-draft status, but it does not claim source-language fidelity.
- **Content probe**: structural clean plus a bounded source-facing sample. At minimum: one JP2 page checked against the normalized source, one substantive source-language quotation or English-source quotation checked against its rendering, and one dense German/Draft paragraph checked clause by clause for compression and gloss-creep. This tier can raise confidence in a tranche or chapter, but it is still a spot-check.
- **Content clean**: the full content-fidelity review described below. Each sampled part gets source-language quotation checks, JP2 density checks, and at least two clause-level paragraph checks. This is the tier required before saying a part has passed content-fidelity review without qualification.

Most ordinary forward translation work should aim for `structural clean` with occasional `content probe` checks at chapter boundaries, high-risk footnotes, or external-review disputes. Reserve `content clean` for commit-readiness probes, suspected drift, or parts that will carry chapter-level claims.

## First Gate: Source-Language Quotation Fidelity

Before judging the Draft English at content-probe or content-clean level, check the source-language quotations.

For at least one substantive Latin or French footnote per part:

1. Quote the source-language text verbatim in the review report.
2. Quote the part file's English rendering verbatim alongside it.
3. Walk through the load-bearing clauses, naming what each phrase maps to.
4. Flag any clause where the English over- or under-translates the source.

If the part includes English-source quotations (Locke, Cudworth, Norris), additionally:

5. Open the cited section of the original work where reasonably possible.
6. Verify that Cassirer's German rendering reflects the original English claim.
7. Flag any clause where Cassirer himself appears to have smoothed or shifted the claim.

For a content probe, one demonstrably verified source-language quotation is enough. For content clean, perform this check for every sampled part that contains substantive source-language quotation. If the review report contains no quoted source-language content, it has not earned a content-probe or content-clean verdict.

## Second Gate: German Body Density

The `review-checklist.md` Quality Question: "Has the German block preserved Cassirer's main prose at full density, even when documentary footnotes or page spillover are handled selectively?"

For content-probe or content-clean review, verify directly:

- For at least one page per part, open the JP2 scan and confirm the normalized source captured the full page — paragraph indents, marginal captions, running headers, page-bottom material.
- If a marginal caption (Cassirer often runs topical captions at page tops, e.g. `Potentielle und aktuelle Unendlichkeit.`) is visible on the scan but absent from the normalized source, that is a silent OCR drop. It does not become part of the German body, but the reviewer should note it.
- Verify paragraph indentation against the printed scan. The normalized source's paragraph segmentation can deviate from Cassirer's original printed paragraphs. (This is the Part 048 case: question and answer split into two part-file paragraphs when the printed text had them as one continuous paragraph.)

## Third Gate: Compression and Gloss-Creep

For content clean, check at least two paragraphs per part — one chosen for argumentative density, one chosen for source-language quotation density when available. For a content probe, one dense paragraph is enough if the report names the limited scope.

- Quote the German clause by clause.
- Quote the English clause by clause.
- Verify each German clause has an English correspondent.
- Verify each English clause comes from a German clause and not from synthesis.

This catches **gloss-creep** (smoothed paraphrase) and **compression** (silently dropped clauses) at clause granularity.

## Content-Clean Checklist

For each sampled part file under a content-clean verdict:

- [ ] German body has been read against the normalized source (any silent drops noted)
- [ ] At least one JP2 scan page has been opened to verify the normalized source itself
- [ ] At least one substantive Latin/French footnote translation has been verified clause by clause against the source-language text quoted in the review
- [ ] For English-source quotations, Cassirer's German rendering has been checked against the original English where the citation is accessible
- [ ] At least two paragraphs have been clause-by-clause checked for compression and gloss-creep
- [ ] No paraphrase signals appear inside the Draft block: "Cassirer argues...", "Locke's point is...", "What the passage means is...", "The thrust of the argument is..." Synthesis belongs in Notes
- [ ] Notes' Translation note is consistent with the actual translation choices observed in the Draft
- [ ] Cited Essay/Demonstratio sections actually contain the load-bearing claims (citation accuracy)

## Paraphrase Signal Quick-Grep

Run as a smoke test, not a verdict:

```sh
rg -n -A1 '^\*\*Draft\*\*' texts/erkenntnisproblem-vol2/parts/*.md | rg -i \
  "(Cassirer (argues|reads|holds|says)|Locke('?s)? (point|view|argument)|The argument is|What this means|The thrust|The key move|Digby argues|Cudworth makes|Norris argues)"
```

Hits inside Draft blocks are warning signs (synthesis disguised as translation). Hits inside Notes blocks are fine. A clean grep does not prove fidelity; it only removes one obvious warning sign.

## Failure Modes to Watch For

- **Cross-file consistency hiding source-language failure** — glossary, journal, ledger, page-map all match each other, but none was verified against the printed scan.
- **Translation note hiding what wasn't translated** — the Notes section lists careful translation choices that the Draft made; what's *not* in the Notes may have been silently smoothed.
- **Verbatim quotation hiding silent omission** — a long block-quote in English may match the German block-quote's structure while dropping a subordinate clause inside it.
- **"Controlled draft" verdict satisfying tier rather than content** — the reviewer marks the part "controlled draft" because the producer ran a same-agent second pass, not because the reviewer independently verified anything.
- **Boundary success hiding mid-page error** — clean start/stop boundaries do not guarantee that the body between them is faithful.
- **Glossary discipline hiding translation gaps** — holding entries open is good methodology, but it does not vouch for the body.
- **Page-bridge stitching success hiding internal compression** — re-stitching paragraphs across `[[pdf-page-N]]` markers verifies only that what is in the normalized source ended up in the part body. It does not verify the normalized source itself.
- **English re-translation of an English original reading well** — if Cassirer quoted Locke in English and the part renders it cleanly in English, the cleanliness may be Locke's, Cassirer's, or the translator's. Test which.

## What to Do When a Review Fails Content Check

- Name the specific failure (gloss-creep at clause X; compression at clause Y; Latin word Z over-translated).
- Record the failure scope in the part's Notes block or in the close-reading ledger.
- Do not absorb apparatus from a content-failed part into chapter-level claims until the failure is addressed.
- Keep the structural verdict separate. "Structural review clean; content fidelity has open issues at clauses X, Y, Z" is an honest split verdict.
- A redo brief should name the specific clauses, not the whole part. The German block usually does not need rework; the Draft and possibly the Notes may.

## Review Report Shape

A content-clean review must include:

- Specific filenames sampled with page ranges.
- Source-language excerpts (Latin/French/English-source) quoted verbatim from the part file.
- English translations quoted verbatim from the part file alongside the source.
- A walk-through of at least one substantive translation, naming what each clause/phrase maps to.
- A density check noting at least one JP2 scan opened.
- A grep result for paraphrase signals (or a note that the grep was clean).
- Verdict, split into structural and content. Examples:
  - `structural clean / content clean`
  - `structural clean / content probe clean at sampled clauses`
  - `structural clean / content provisional with notes at X, Y`
  - `structural clean / content needs redo at clauses X, Y`

If the review report does not quote specific source-language content from the part and walk through specific translation choices, the verdict is not earned at content-probe or content-clean level. The verdict at most reaches `structural clean`.

## Scope

This document applies to translation parts in `texts/erkenntnisproblem-vol2/parts/*.md`. It does **not** apply to:

- Reading notes in `texts/erkenntnisproblem-vol2/reading/` (synthesis, not translation)
- Journal or session-ledger entries (project state, not source-language content)
- Glossary entries (consult `review-checklist.md` for promotion discipline)

For producer-side discipline (what to do when creating a part), see `review-checklist.md` Per Tranche section. This document is exclusively reviewer-side.
