# Source Layout

Primary witness: IA item `gesammelteschrif03humbuoft`, GS III / *Werke III*.

Tracked:

- `full/gesammelte-schriften-iii.txt` - whole-volume PDF text extraction.
- `raw/010-ankuendigung-vaskische-sprache-pdf-300-319.txt` - uncorrected
  article extract.
- `normalized/010a-sprache-vermittlerin-pdf-308-309.txt` - checked working
  normalization of the Cassirer-facing mediation passage.
- `witnesses.yaml`, `page-map.yaml`, `sections.yaml`.

Ignored local files:

- `local/gesammelteschrif03humbuoft.pdf`
- `local/gesammelteschrif03humbuoft_djvu.txt`
- `local/gesammelteschrif03humbuoft_page_numbers.json`
- `local/gesammelteschrif03humbuoft_scandata.xml`

The IA page-number JSON is not fully reliable in this range. Use the checked
article-local alignment in `page-map.yaml` before citing.
