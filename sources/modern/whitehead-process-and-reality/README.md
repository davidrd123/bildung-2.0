# Process and Reality

Source-local scaffold for chapter-scale browsing of Alfred North Whitehead's
*Process and Reality: An Essay in Cosmology*.

Status: incoming TXT witness, split only. This is not a cleaned, corrected, or
interpretive edition. The bracketed pagination and editorial markers already
present in the source text are retained in the full text and raw section files.

Source-local files:

- `source/full/process-and-reality.txt` - copied text witness with only control-character cleanup.
- `source/raw/*.txt` - front matter, part markers, chapters, index, and editors' notes split by source line.
- `source/sections.yaml` - section manifest with source-line coverage and first detected bracketed page marker where available.

Generation:

- `python3 tools/split_whitehead_process_and_reality.py`

