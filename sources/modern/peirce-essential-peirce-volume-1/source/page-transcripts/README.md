# Page-Grounded Transcripts

This directory is the image-grounded authority layer for the Peirce Volume 1
text scaffold.

The workflow is intentionally simple:

1. Render the authority PDF to page images outside git.
2. Open each page image directly.
3. Use the existing OCR/text-layer output only as a draft.
4. Correct or transcribe the page from what is visible in the image.
5. Save one transcript per PDF page, preserving `[pdf page NNN]` and printed
   `[page N]` markers.
6. Assemble cleaned section files from these page transcripts as batches are
   completed.

Python is only for mechanical work such as rendering pages, naming files, and
assembling completed page transcripts. It is not the authority for the text.

Current image cache:

- `/tmp/peirce_ep1_pages_300/peirce-ep1-NNN.png`

The image cache is intentionally untracked.
