# Plato Dialogue Pack — Cassirer Greek Substrate

**Status:** Bounded Greek substrate folder. This is not a Plato `texts/`
campaign and not an engagement layer. It exists so Cassirer-facing work can
search and inspect the specific Plato dialogues repeatedly pressured by PSF,
`Substanzbegriff`, and `Erkenntnisproblem`.

## Why This Exists

The Cassirer Greek source-pressure scan identified a bounded Plato pack rather
than a generic "Platonism" need. The pressure clusters around Plato's
epistemological-semantic and mathematical-ontological surfaces:

- `Sophist`
- `Theaetetus`
- `Philebus`
- `Phaedo`
- `Republic`
- `Timaeus`
- `Cratylus`
- `Phaedrus`
- `Symposium`
- Seventh Letter, included through the `Letters` corpus

This folder makes those Greek texts directly searchable without depending on
the Perseus or Scaife viewers.

## Source

The TEI XML files come from:

- `PerseusDL/canonical-greekLit`
- raw GitHub URLs recorded in `source/manifest.yaml`

All local TEI files use Plato textgroup `tlg0059` and the Greek edition suffix
`perseus-grc2`, which the CTS metadata identifies as John Burnet's Oxford
Plato.

The TEI XML is the local source surface. The plain-text files are generated
search surfaces.

## Structure

```text
source/
  checksums.sha256
  manifest.yaml
  tei/
    cratylus.tlg0059.tlg005.perseus-grc2.xml
    letters.tlg0059.tlg036.perseus-grc2.xml
    phaedo.tlg0059.tlg004.perseus-grc2.xml
    phaedrus.tlg0059.tlg012.perseus-grc2.xml
    philebus.tlg0059.tlg010.perseus-grc2.xml
    republic.tlg0059.tlg030.perseus-grc2.xml
    sophist.tlg0059.tlg007.perseus-grc2.xml
    symposium.tlg0059.tlg011.perseus-grc2.xml
    theaetetus.tlg0059.tlg006.perseus-grc2.xml
    timaeus.tlg0059.tlg031.perseus-grc2.xml
  plain/
    generated `.txt` search surfaces
tools/
  tei_to_plain.py
```

## Rebuild Plain Text

```bash
python3 sources/greek/plato-dialogue-pack-cassirer-substrate/tools/tei_to_plain.py \
  sources/greek/plato-dialogue-pack-cassirer-substrate/source/tei \
  sources/greek/plato-dialogue-pack-cassirer-substrate/source/plain
```

The plain-text export preserves broad CTS/Stephanus sectioning as headings and
inline markers. It is for search and quick orientation, not citation-critical
philological work.

## Guardrails

- Keep the TEI files as the source layer.
- Use the generated plain text for search, not final citation.
- Do not treat this folder as full Plato coverage.
- Do not promote any dialogue to an engagement campaign until local reading
  pressure requires it.
- For the Humboldt seam, `Cratylus` is the first Greek anchor to inspect.
