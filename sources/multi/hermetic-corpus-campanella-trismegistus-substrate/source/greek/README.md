# Greek Witnesses

Greek-side tracking for this shelf is in `../manifest.yaml`.

Tracked search surfaces:

- `tei/` - First1KGreek `tlg1286` TEI witnesses from Walter Scott's 1924
  *Hermetica*.
- `plain/` - generated plain-text search surfaces from `tei/`.

Use ignored local acquisitions for search and confirmation:

- `../local/greek/bibliotheca-augustana-ch-*.html` for CH I-XII.
- `../local/greek/scott-hermetica-vol-1-ocr.txt` for the Internet Archive OCR
  of Scott's 1924 *Hermetica* vol. I.
- `../local/greek/stobaeus-*.txt` for Wachsmuth-Hense Stobaeus OCR.
- `../pdf/scott-hermetica-vol-1.pdf` for Scott's scan witness.
- `../pdf/poimandres-ch-i-nock-festugiere-matheson.pdf` for CH I.
- `../pdf/stobaeus-*.pdf` for Stobaeus scan witnesses.

Treat First1KGreek/Scott as a substrate search layer. Do not use it as the
citation authority where Nock-Festugiere numbering or text-critical decisions
matter.

Nock-Festugiere vol. II is present as an ignored private PDF/text extraction
for the Asclepius/CH XIII-XVIII tranche. Do not add Bude/Nock-Festugiere full
text to tracked Greek surfaces unless a clean open-license surface is
identified. Treat those volumes as the critical citation spine.
