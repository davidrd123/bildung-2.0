# Source Verification Queue from `erk-vol02-5-13a`

Status: queue only. These items do not need verification unless future work
wants to reuse them as claims.

Target transcript:

- `../2026-05-14_ClaudeCode_erk-vol02-5-13a.md`

## Local / Repo Checks

### 1. Claude Code export behavior

Claim to verify if tooling changes: Claude Code JSONL stores custom title /
agent name inline, and `tools/convert_claude_code_jsonl_to_markdown.py` is the
right repeatable export path.

Anchors: [chat line 870](../2026-05-14_ClaudeCode_erk-vol02-5-13a.md:870), [chat line 2461](../2026-05-14_ClaudeCode_erk-vol02-5-13a.md:2461), [chat line 2514](../2026-05-14_ClaudeCode_erk-vol02-5-13a.md:2514)

Verification path: inspect current JSONL schema and converter script before
relying on field names.

### 2. Vol. II apparatus state after the session

Claim to verify if continuing Vol. II: Parts 001-011, glossary, journal,
session-ledger, and reading notes reflect the Bacon/Gassendi status summarized
in the chat.

Anchors: [chat line 2355](../2026-05-14_ClaudeCode_erk-vol02-5-13a.md:2355), [chat line 2395](../2026-05-14_ClaudeCode_erk-vol02-5-13a.md:2395), [chat line 2494](../2026-05-14_ClaudeCode_erk-vol02-5-13a.md:2494)

Verification path: read local `texts/erkenntnisproblem-vol2/` files, not the
chat summary.

## Source / Theory Checks

### 3. Lotman's minimal semiotic structure

Claim to verify before reuse: the minimal working semiotic structure is a pair
of mutually non-translatable languages plus a translation block; symmetric vs.
asymmetric transformation distinguishes transfer from meaning generation.

Anchors: [chat line 2271](../2026-05-14_ClaudeCode_erk-vol02-5-13a.md:2271), [chat line 2275](../2026-05-14_ClaudeCode_erk-vol02-5-13a.md:2275), [chat line 2291](../2026-05-14_ClaudeCode_erk-vol02-5-13a.md:2291)

Verification path: check the relevant Lotman source/encounter note in
`sources/russian/lotman-vnutri-mislyashih-mirov/` before making this a method
claim.

### 4. Peirce / Lotman lineage and architectural comparison

Claim to verify before reuse: Lotman was reading Peirce indirectly through
Jakobson, and the Peirce/Lotman relation is family resemblance rather than
identity.

Anchors: [chat line 2320](../2026-05-14_ClaudeCode_erk-vol02-5-13a.md:2320), [chat line 2322](../2026-05-14_ClaudeCode_erk-vol02-5-13a.md:2322), [chat line 2337](../2026-05-14_ClaudeCode_erk-vol02-5-13a.md:2337)

Verification path: use existing May 6 Lotman extraction queue and primary /
secondary Tartu-Peirce sources before writing a stable crosswalk.

### 5. Heidegger on `Wirklichkeit`, `energeia`, and `actualitas`

Claim to verify before reuse: Heidegger treats Latin `actualitas` as a
metaphysical narrowing of Greek `energeia`, while German `Wirklichkeit` preserves
the operative sense more strongly.

Anchors: [chat line 1939](../2026-05-14_ClaudeCode_erk-vol02-5-13a.md:1939), [chat line 1945](../2026-05-14_ClaudeCode_erk-vol02-5-13a.md:1945), [chat line 1957](../2026-05-14_ClaudeCode_erk-vol02-5-13a.md:1957)

Verification path: check Heidegger source passages and at least one critical
classicist/philological treatment before using it beyond conversation.

### 6. German morphological transparency and cognitive processing

Claim to verify before reuse: transparent compound morphology changes processing
speed, combinability, or conceptual availability even when speakers are not
consciously etymologizing.

Anchors: [chat line 1213](../2026-05-14_ClaudeCode_erk-vol02-5-13a.md:1213), [chat line 1919](../2026-05-14_ClaudeCode_erk-vol02-5-13a.md:1919), [chat line 1966](../2026-05-14_ClaudeCode_erk-vol02-5-13a.md:1966)

Verification path: psycholinguistic literature on compound morphology and
semantic transparency; do not rely on LLM introspection.

## Historical / Cultural Claims

### 7. Classical education decline and English formal-register thinning

Claims to verify before reuse: classical training in US/UK education collapsed
post-1960; formal connective vocabulary (`thereby`, `wherein`, etc.) moved from
educated-common to specialist/formal register; Plain English and Hemingway/Orwell
style norms actively discouraged older connective prose.

Anchors: [chat line 1457](../2026-05-14_ClaudeCode_erk-vol02-5-13a.md:1457), [chat line 1485](../2026-05-14_ClaudeCode_erk-vol02-5-13a.md:1485), [chat line 1489](../2026-05-14_ClaudeCode_erk-vol02-5-13a.md:1489), [chat line 1503](../2026-05-14_ClaudeCode_erk-vol02-5-13a.md:1503)

Verification path: education-history sources, corpus frequency checks, style
manual history.

### 8. Jewish educational tradition as counterexample to mass-depth tradeoff

Claim to verify before reuse: Jewish educational tradition preserved depth at
scale through Hebrew/Aramaic textual practice, chevruta, communal anchors, and
multilingual interpretation.

Anchors: [chat line 1515](../2026-05-14_ClaudeCode_erk-vol02-5-13a.md:1515), [chat line 1521](../2026-05-14_ClaudeCode_erk-vol02-5-13a.md:1521), [chat line 1525](../2026-05-14_ClaudeCode_erk-vol02-5-13a.md:1525)

Verification path: Jewish education history and sociology of European /
American Jewish intellectual life.

### 9. High-cultural survival after hollowing-out

Claims to verify before reuse: Rome/monastic preservation, rabbinic Judaism,
Chinese literati through conquest dynasties, Catholic institutional continuity,
Islamic Golden Age, and Imperial Russia serve as comparative cases for
high-culture survival or loss.

Anchors: [chat line 1623](../2026-05-14_ClaudeCode_erk-vol02-5-13a.md:1623), [chat line 1637](../2026-05-14_ClaudeCode_erk-vol02-5-13a.md:1637), [chat line 1649](../2026-05-14_ClaudeCode_erk-vol02-5-13a.md:1649)

Verification path: treat as a comparative-history project, not a chat claim.

### 10. China / India / Israel / Singapore as future refuges

Claim to verify before reuse: specific countries may function as receptors for
parts of Western high-cultural or technical apparatus under future emigration.

Anchors: [chat line 1664](../2026-05-14_ClaudeCode_erk-vol02-5-13a.md:1664), [chat line 1672](../2026-05-14_ClaudeCode_erk-vol02-5-13a.md:1672), [chat line 1689](../2026-05-14_ClaudeCode_erk-vol02-5-13a.md:1689)

Verification path: this is current-events and political analysis. Search current
sources before making any claim.

## Already Locally Verified Enough for Draft Status

### 11. `mente captus`

This was verified in-session and patched locally according to the transcript.
No further action unless editing the Part 001 footnote again.

Anchors: [chat line 531](../2026-05-14_ClaudeCode_erk-vol02-5-13a.md:531), [chat line 571](../2026-05-14_ClaudeCode_erk-vol02-5-13a.md:571)

Verification path if needed: check the current Part 001 file and Latin source
quotation.
