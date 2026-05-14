#!/usr/bin/env python3
"""Run a small source-grounded prompt probe through OpenAI chat completions."""

from __future__ import annotations

import argparse
import json
import os
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any


CHAT_COMPLETIONS_URL = "https://api.openai.com/v1/chat/completions"
SYSTEM_PROMPT = (
    "You are answering a short source-based interpretation probe. "
    "Use only the given passage. Keep the answer to 3-5 sentences. "
    "If a paraphrase is too smooth or misleading, say so directly."
)


def compose_prompt(case: dict[str, Any], variant: dict[str, Any]) -> str:
    source_locus = variant.get("source_locus", case["source_locus"])
    source_excerpt = variant.get("source_excerpt", case["source_excerpt"])
    return "\n\n".join(
        [
            f"Probe ID: {variant['id']}",
            f"Passage label: {case['label']}",
            f"Source locus: {source_locus}",
            "Source excerpt:",
            source_excerpt,
            "Question:",
            variant["question"],
        ]
    )


def request_completion(
    *,
    model: str,
    prompt: str,
    api_key: str,
    max_tokens: int,
    retries: int,
) -> str:
    payload = {
        "model": model,
        "temperature": 0,
        "max_tokens": max_tokens,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
    }
    body = json.dumps(payload).encode("utf-8")

    for attempt in range(retries):
        request = urllib.request.Request(
            CHAT_COMPLETIONS_URL,
            data=body,
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=90) as response:
                data = json.loads(response.read().decode("utf-8"))
            return data["choices"][0]["message"]["content"].strip()
        except urllib.error.HTTPError as error:
            message = error.read().decode("utf-8", errors="replace")
            if error.code not in {429, 500, 502, 503, 504} or attempt == retries - 1:
                raise RuntimeError(f"OpenAI chat completion failed: {error.code} {message}") from error
        except urllib.error.URLError as error:
            if attempt == retries - 1:
                raise RuntimeError(f"OpenAI chat completion failed: {error}") from error
        time.sleep(2**attempt)

    raise RuntimeError("OpenAI chat completion failed")


def load_existing(path: Path) -> set[str]:
    if not path.exists():
        return set()
    completed: set[str] = set()
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            row = json.loads(line)
            completed.add(row["prompt_id"])
    return completed


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--pack",
        default="00-Notes/working-syntheses/2026-05-08-uexkuell-cognitive-grammar-probe-pack.json",
    )
    parser.add_argument("--output", default="var/retrieval/uexkuell-cg-probe-gpt-4.1-mini.jsonl")
    parser.add_argument("--model", default="gpt-4.1-mini")
    parser.add_argument("--max-tokens", type=int, default=420)
    parser.add_argument("--retries", type=int, default=4)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise SystemExit("OPENAI_API_KEY is not set")

    pack_path = Path(args.pack)
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    pack = json.loads(pack_path.read_text(encoding="utf-8"))
    completed = set() if args.force else load_existing(output_path)
    mode = "w" if args.force else "a"

    with output_path.open(mode, encoding="utf-8") as handle:
        for case in pack["cases"]:
            for variant in case["variants"]:
                prompt_id = variant["id"]
                if prompt_id in completed:
                    continue
                prompt = compose_prompt(case, variant)
                output = request_completion(
                    model=args.model,
                    prompt=prompt,
                    api_key=api_key,
                    max_tokens=args.max_tokens,
                    retries=args.retries,
                )
                row = {
                    "pack": pack_path.as_posix(),
                    "pack_title": pack["title"],
                    "model": args.model,
                    "case_id": case["id"],
                    "case_label": case["label"],
                    "prompt_id": prompt_id,
                    "kind": variant["kind"],
                    "source_condition": variant.get("source_condition", case.get("source_condition", "")),
                    "question": variant["question"],
                    "expected_construal_difference": case["expected_construal_difference"],
                    "expected_failure_labels": case["failure_labels"],
                    "prompt": prompt,
                    "output": output,
                }
                handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True))
                handle.write("\n")
                handle.flush()
                print(f"wrote {prompt_id}")


if __name__ == "__main__":
    main()
