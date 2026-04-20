#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path


PROTOCOL_TEXT_PREFIXES = (
    "[Request interrupted by user",
)


def derive_title(path: Path) -> str:
    stem = path.stem
    stem = re.sub(r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}_", "", stem)
    stem = re.sub(r"^ClaudeCode_", "", stem)
    return stem.replace("_", " ").title()


def keep_text(text: str) -> bool:
    stripped = text.strip()
    if not stripped:
        return False
    return not any(stripped.startswith(prefix) for prefix in PROTOCOL_TEXT_PREFIXES)


def normalize_text(text: str) -> str:
    return text.strip().replace("\r\n", "\n")


def collect_turns(path: Path) -> tuple[list[tuple[str, str]], set[str], str | None, str | None]:
    raw_turns: list[tuple[str, str]] = []
    session_ids: set[str] = set()
    first_timestamp: str | None = None
    last_timestamp: str | None = None

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        if not raw_line.strip():
            continue
        obj = json.loads(raw_line)

        session_id = obj.get("sessionId")
        if session_id:
            session_ids.add(session_id)

        timestamp = obj.get("timestamp")
        if timestamp:
            if first_timestamp is None or timestamp < first_timestamp:
                first_timestamp = timestamp
            if last_timestamp is None or timestamp > last_timestamp:
                last_timestamp = timestamp

        if obj.get("type") not in {"user", "assistant"}:
            continue

        message = obj.get("message", {})
        role = message.get("role")
        if role not in {"user", "assistant"}:
            continue

        content = message.get("content")
        blocks: list[str] = []
        image_count = 0

        if isinstance(content, str):
            text = normalize_text(content)
            if keep_text(text):
                blocks.append(text)
        elif isinstance(content, list):
            for item in content:
                item_type = item.get("type")
                if item_type == "text":
                    text = normalize_text(item.get("text", ""))
                    if keep_text(text):
                        blocks.append(text)
                elif item_type == "image":
                    image_count += 1

        if image_count:
            suffix = "s" if image_count != 1 else ""
            blocks.append(f"[{image_count} image{suffix} attached omitted]")

        if not blocks:
            continue

        speaker = "User" if role == "user" else "Claude"
        raw_turns.append((speaker, "\n\n".join(blocks)))

    turns: list[tuple[str, str]] = []
    for speaker, body in raw_turns:
        if turns and turns[-1][0] == speaker:
            turns[-1] = (speaker, f"{turns[-1][1]}\n\n{body}")
        else:
            turns.append((speaker, body))

    return turns, session_ids, first_timestamp, last_timestamp


def render_markdown(
    title: str,
    source_path: Path,
    turns: list[tuple[str, str]],
    session_ids: set[str],
    first_timestamp: str | None,
    last_timestamp: str | None,
) -> str:
    lines = [f"# {title}", ""]
    lines.append("Source: Claude Code session")
    if session_ids:
        if len(session_ids) == 1:
            lines.append(f"Session ID: `{next(iter(session_ids))}`")
        else:
            joined = ", ".join(f"`{sid}`" for sid in sorted(session_ids))
            lines.append(f"Session IDs: {joined}")
    if first_timestamp:
        lines.append(f"First timestamp: {first_timestamp}")
    if last_timestamp:
        lines.append(f"Last timestamp: {last_timestamp}")
    lines.append(
        f"Converted: {datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')}"
    )
    lines.append(f"Original: `{source_path.as_posix()}`")
    lines.append(
        "Note: encrypted thinking, internal protocol rows, and tool use/results were removed; image payloads were replaced with placeholders."
    )
    lines.append("")
    lines.append("---")
    lines.append("")

    for speaker, body in turns:
        lines.append(f"## {speaker}")
        lines.append("")
        lines.append(body)
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("-o", "--output", type=Path)
    args = parser.parse_args()

    input_path = args.input
    output_path = args.output or input_path.with_suffix(".md")

    turns, session_ids, first_timestamp, last_timestamp = collect_turns(input_path)
    markdown = render_markdown(
        derive_title(input_path),
        input_path,
        turns,
        session_ids,
        first_timestamp,
        last_timestamp,
    )
    output_path.write_text(markdown, encoding="utf-8")


if __name__ == "__main__":
    main()
