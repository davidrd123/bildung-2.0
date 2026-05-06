# Whole-Book Cleanup Goal

Produce a clean, page-image-proofed Russian text corpus for Ю. М. Лотман,
*Культура и взрыв* under
`sources/russian/lotman-kultura-i-vzryv/source/cleaned/`.

The output must be good enough to serve as the textual source for later
audiobook/script generation. Do not translate it. Do not convert it into an
audiobook script. Preserve the book as clean Russian source text.

## Authority

- Use `source/local/lotman-kultura-i-vzryv.djvu` as the canonical local source.
- Use `source/page-images/pages/NNN.png` as the page-by-page visual authority.
- Use `source/raw/pages/NNN.txt` and `source/raw/NNN-*.txt` only as OCR
  scaffolds.
- Use `source/sections.yaml` for batching, but verify section boundaries against
  the page images while working.

## Deliverable

- Clean section files in `source/cleaned/`, matching the sequence and scope of
  `source/sections.yaml`.
- Page markers preserved throughout the cleaned text.
- Headings, epigraphs, block quotations, footnotes, contents, and colophon
  retained when present in the scan.
- Russian text corrected against the page images.
- Formatting clean enough for downstream TTS preparation: readable paragraphs,
  separated footnotes, no fused running headers, no OCR line-break garbage, and
  no unresolved hyphenation except where the printed text truly requires it.

Preferred cleaned page marker policy:

- For numbered main-text pages, use `[page N | scan NNN]`.
- For unnumbered front/back matter, use `[scan NNN]`.
- If a page break falls inside a word, keep the marker inline only when moving it
  would misrepresent the printed boundary.

## Workflow

1. Work section by section in `source/sections.yaml`, not from the whole book at
   once.
2. For each scan page in the section, open the corresponding rendered image and
   compare it to `source/raw/pages/NNN.txt`.
3. Correct OCR damage directly into the cleaned section file.
4. Reflow line-broken OCR into readable paragraphs while preserving real
   paragraph breaks, quotations, verse, lists, and footnotes.
5. Remove repeated running headers from the cleaned reading flow unless the
   header is the actual section title on its opening page.
6. Preserve footnotes in readable form, separated from body text. If a note
   continues across pages, join it cleanly and keep page markers at the real
   boundary.
7. Preserve names, foreign-language quotations, Greek/Latin text, bibliographic
   details, and punctuation as printed when the image is legible.
8. When the image is ambiguous, do not guess silently. Mark the passage with a
   concise `[unclear: ...]` note and record it in the proof manifest.
9. Update `page-proof-manifest.md` after each completed page range.
10. Update `cleanup-manifest.md` when a section file is created or its proof
    status changes.

## Completion Criteria

- Every included scan page has been checked against its rendered page image.
- Every cleaned section file is listed in `cleanup-manifest.md`.
- Every printed or scan page range is covered in `page-proof-manifest.md`.
- Page markers are present and sequential.
- Chapter titles match the images, not the damaged OCR contents page.
- No obvious OCR substitutions remain in proofed sections: wrong Cyrillic
  letters, Latin/Cyrillic confusions, broken names, fused words, header
  intrusions, or page-break hyphenation scars.
- Footnotes and citations are readable and not fused into body text.
- All uncertainties are logged with scan page number and reason.
- `git diff --check -- sources/russian/lotman-kultura-i-vzryv tools/extract_lotman_kultura_pages.py`
  passes.

## Do Not Do

- Do not treat the DjVu OCR layer as authoritative.
- Do not modernize Lotman's spelling or punctuation beyond correcting OCR.
- Do not remove page markers or source apparatus.
- Do not turn this into reader-English, commentary, glossary, or TTS output
  during the cleanup pass.
- Do not mark the whole book complete until the manifest proves page-by-page
  visual coverage.
