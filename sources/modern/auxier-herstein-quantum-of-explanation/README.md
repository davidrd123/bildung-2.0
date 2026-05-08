# The Quantum of Explanation

Source-local scaffold for chapter-scale browsing of Randall E. Auxier and Gary
L. Herstein's *The Quantum of Explanation: Whitehead's Radical Empiricism*.

Status: incoming TXT witness, split only. This is not a cleaned, corrected, or
interpretive edition. The source text does not expose stable printed-page
markers, so `printed_page_start` is left null in the section manifest.

Source-local files:

- `source/full/quantum-of-explanation.txt` - copied text witness with only control-character cleanup.
- `source/raw/*.txt` - front matter, introduction, chapters, notes, and index split by source line.
- `source/sections.yaml` - section manifest with source-line coverage.

Generation:

- `python3 tools/split_auxier_herstein_quantum_of_explanation.py`

