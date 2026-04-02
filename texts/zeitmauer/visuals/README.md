# Zeitmauer Visuals

This folder is the first lightweight bridge between the repo's earned
`[visual candidate]` notes and Gemini image generation.

The rule from the project charter still applies: visuals should begin from
review-noted candidates, not from arbitrary prompt-chasing. Generated images are
derived exploratory artifacts, not canonical source material.

## Default Output

`python3 tools/vision.py edit ...` writes PNGs by default to:

```text
texts/zeitmauer/visuals/out/YYYY-MM-DD/
```

Use `--output-dir` if a different root is needed.

## Install

```bash
python3 -m pip install -r tools/vision-requirements.txt
```

Required environment:

- `GEMINI_API_KEY`

## List candidates

List all tagged visual candidates across the repo:

```bash
python3 tools/vision.py --pretty list-candidates
```

Limit the scan to `zeitmauer` notes:

```bash
python3 tools/vision.py --pretty list-candidates texts/zeitmauer --query warp
```

## Generate images

Pure text-to-image:

```bash
python3 tools/vision.py --pretty edit \
  "loom diagram: measurable time as warp, fateful time as weft, clear educational composition" \
  --label warp-weft \
  --num-outputs 2
```

Image edit / reference flow:

```bash
python3 tools/vision.py --pretty edit \
  "refine this into a cleaner line-and-spiral diagram with restrained labels" \
  --image path/to/source.png \
  --label line-circle-spiral
```

Useful flags:

- `--system-prompt "..."` for tighter art direction
- `--aspect-ratio 16:9`
- `--image-size 1536x1024`
- `--json-out texts/zeitmauer/visuals/out/latest-run.json`
- `--candidate-ref texts/zeitmauer/journal.md:343` to log which `[visual candidate]` note a run came from

Example with provenance:

```bash
python3 tools/vision.py --pretty edit \
  "a woven textile seen from above, where dark irregular weft creates the visible pattern" \
  --label warp-weft \
  --candidate-ref texts/zeitmauer/journal.md:343 \
  --json-out texts/zeitmauer/visuals/out/warp-weft-run.json
```

The JSON output will then carry a `candidate` object with source path, line, slug,
and note text.

## Analyze Images

Blind-read an image first:

```bash
python3 tools/vision.py --pretty analyze \
  texts/zeitmauer/visuals/out/2026-04-01/line-circle-spiral-refined_001.png
```

Run blind read plus intent-aware evaluation from a `[visual candidate]` note:

```bash
python3 tools/vision.py --pretty analyze \
  texts/zeitmauer/visuals/out/2026-04-01/line-circle-spiral-refined_001.png \
  --candidate-ref texts/zeitmauer/journal.md:345 \
  --json-out texts/zeitmauer/visuals/out/line-circle-spiral-analysis.json
```

Defaults:

- first-line analysis model: `gemini-3-flash-preview`
- fallback model: `gemini-3.1-pro-preview`
- default eval temperature: `0.2`

Useful flags:

- `--prompt "..."` to supply a target brief directly
- `--model gemini-3-flash-preview`
- `--fallback-model gemini-3.1-pro-preview`
- `--temperature 0.2`

## Compare Images

Rank multiple candidates against a target brief:

```bash
python3 tools/vision.py --pretty compare \
  texts/zeitmauer/visuals/out/2026-04-01/line-circle-spiral_001.png \
  texts/zeitmauer/visuals/out/2026-04-01/line-circle-spiral-refined_001.png \
  --candidate-ref texts/zeitmauer/journal.md:345
```

Or use an explicit prompt:

```bash
python3 tools/vision.py --pretty compare \
  texts/zeitmauer/visuals/out/2026-04-01/warp-weft_001.png \
  texts/zeitmauer/visuals/out/2026-04-01/warp-weft-refined_001.png \
  --prompt "a woven textile where irregular weft creates the visible pattern"
```

## Keepers

Promote a successful image into a curated keepers folder:

```bash
python3 tools/vision.py --pretty promote \
  texts/zeitmauer/visuals/out/2026-04-01/line-circle-spiral-refined_001.png \
  --candidate-ref texts/zeitmauer/journal.md:345 \
  --note "cleanest version so far"
```

This copies the image into:

```text
texts/zeitmauer/visuals/keepers/
```

and appends a record to:

```text
texts/zeitmauer/visuals/keepers/keepers.json
```

Useful flags:

- `--keepers-dir /tmp/vision-keepers` for testing
- `--slug line-circle-spiral` to override the default keeper name
- `--json-out path/to/promote-result.json`

## Current note

Right now this is intentionally smaller than `latent-dreamer/daydream_vision`.
What was pulled in is the reusable Gemini image-generation slice, not the
manifest, anchor-review, or world-pack loop.
