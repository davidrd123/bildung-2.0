# Greek Source Tools

`tei_to_plain.py` generates plain-text search surfaces from PerseusDL and
OpenGreekAndLatin TEI XML. It preserves CTS edition metadata when present and
emits headings for nested TEI textpart divisions.

Use it from the repository root:

```sh
python3 sources/greek/tools/tei_to_plain.py <input-tei-dir> <output-plain-dir>
```

The output is for search and reading support. Citation-sensitive work should
return to the TEI and, where necessary, the scanned edition.
