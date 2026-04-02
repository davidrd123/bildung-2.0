#!/usr/bin/env python3
from __future__ import annotations

import argparse
import base64
import datetime as dt
import importlib.metadata
import io
import json
import mimetypes
import os
import re
import shutil
import sys
from pathlib import Path
from typing import Any, Optional

try:
    from google import genai  # type: ignore
    from google.genai import types as gtypes  # type: ignore
except Exception:  # pragma: no cover
    genai = None  # type: ignore[assignment]
    gtypes = None  # type: ignore[assignment]

try:
    from PIL import Image
except Exception:  # pragma: no cover
    Image = None  # type: ignore[assignment]


REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUTPUT_ROOT = REPO_ROOT / "texts" / "zeitmauer" / "visuals" / "out"
DEFAULT_KEEPERS_ROOT = REPO_ROOT / "texts" / "zeitmauer" / "visuals" / "keepers"
DEFAULT_IMAGE_MODEL = "gemini-3.1-flash-image-preview"
DEFAULT_ANALYZE_MODEL = "gemini-3-flash-preview"
DEFAULT_ANALYZE_FALLBACK_MODEL = "gemini-3.1-pro-preview"
DEFAULT_ANALYZE_TEMPERATURE = 0.2
DEFAULT_SCAN_ROOTS = ("00-Notes", "texts")
VISUAL_CANDIDATE_PATTERN = re.compile(
    r"^\s*(?:[-*]\s+|#+\s+).*\[visual candidate\].*$",
    flags=re.IGNORECASE,
)


def resolve_path(path_str: str) -> Path:
    return Path(path_str).expanduser().resolve()


def resolve_repo_path(path_str: str) -> Path:
    candidate = Path(path_str).expanduser()
    if candidate.is_absolute():
        return candidate.resolve()
    return (REPO_ROOT / candidate).resolve()


def slugify(text: str, *, max_len: int = 60) -> str:
    value = text.strip().lower()
    value = re.sub(r"\s+", "-", value)
    value = re.sub(r"[^a-z0-9_-]+", "", value)
    value = re.sub(r"-{2,}", "-", value)
    value = value.strip("-_")
    if not value:
        return "untitled"
    return value[:max_len]


def prompt_stem(prompt: str) -> str:
    words = [word for word in re.split(r"\s+", prompt.strip()) if word]
    if not words:
        return "untitled"
    return slugify(" ".join(words[:4]))


def path_record(path: Path, *, root: Optional[Path] = None) -> dict[str, Any]:
    absolute = path.resolve()
    record: dict[str, Any] = {"path": str(absolute)}
    if root is not None:
        try:
            record["relativePath"] = str(absolute.relative_to(root.resolve()))
        except Exception:
            pass
    return record


def now_iso() -> str:
    return dt.datetime.now().astimezone().isoformat(timespec="seconds")


def dated_output_dir(output_dir: Optional[str]) -> tuple[Path, Path]:
    root = resolve_path(output_dir) if output_dir else DEFAULT_OUTPUT_ROOT.resolve()
    dated = (root / dt.date.today().isoformat()).resolve()
    dated.mkdir(parents=True, exist_ok=True)
    return root, dated


def next_seq(out_dir: Path, stem: str, *, suffix: str = ".png") -> int:
    max_value = 0
    for entry in out_dir.glob(f"{stem}_*{suffix}"):
        name = entry.stem
        if not name.startswith(f"{stem}_"):
            continue
        seq_part = name[len(stem) + 1 :]
        try:
            max_value = max(max_value, int(seq_part))
        except Exception:
            continue
    return max_value + 1


def ensure_dir(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    return path.resolve()


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def load_json(path: Path, *, default: Any) -> Any:
    if not path.is_file():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def google_genai_version() -> str:
    try:
        return importlib.metadata.version("google-genai")
    except Exception:
        return "unknown"


def supports_image_config() -> bool:
    return bool(gtypes is not None and hasattr(gtypes, "ImageConfig"))


def require_image_stack() -> None:
    if genai is None or gtypes is None:
        raise RuntimeError(
            "google-genai is not installed. Install with "
            "`python3 -m pip install -r tools/vision-requirements.txt`."
        )
    if Image is None:
        raise RuntimeError(
            "Pillow is not installed. Install with "
            "`python3 -m pip install -r tools/vision-requirements.txt`."
        )


def init_client() -> Any:
    require_image_stack()
    try:
        from dotenv import load_dotenv  # type: ignore

        load_dotenv()
    except Exception:
        pass
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY not set.")
    return genai.Client(api_key=api_key)


def build_image_config(aspect_ratio: Optional[str], image_size: Optional[str]) -> Any:
    if not aspect_ratio and not image_size:
        return None
    if not supports_image_config():
        raise RuntimeError(
            "Installed google-genai does not expose types.ImageConfig. "
            "Upgrade to google-genai>=1.49.0."
        )
    return gtypes.ImageConfig(  # type: ignore[call-arg]
        aspect_ratio=aspect_ratio or None,
        image_size=image_size or None,
    )


def load_input_image(path: Path) -> Any:
    require_image_stack()
    if not path.is_file():
        raise FileNotFoundError(f"Image not found: {path}")
    mime_type, _ = mimetypes.guess_type(str(path))
    if not (mime_type and mime_type.startswith("image/")):
        raise RuntimeError(f"Expected image/* input, got {mime_type or 'unknown'}: {path}")
    img = Image.open(path)
    return img.convert("RGB")


def decode_inline_image(part: Any) -> Optional[Any]:
    inline = getattr(part, "inline_data", None)
    if inline is None:
        return None
    mime_type = getattr(inline, "mime_type", None)
    if not (isinstance(mime_type, str) and mime_type.startswith("image/")):
        return None
    data = getattr(inline, "data", None)
    raw: Optional[bytes]
    if isinstance(data, (bytes, bytearray)):
        raw = bytes(data)
    elif isinstance(data, str):
        try:
            raw = base64.b64decode(data)
        except Exception:
            raw = None
    else:
        raw = None
    if not raw:
        return None
    try:
        img = Image.open(io.BytesIO(raw))
        return img.convert("RGB")
    except Exception:
        return None


def img_size(img: Any) -> dict[str, int]:
    try:
        width, height = img.size  # type: ignore[attr-defined]
        return {"width": int(width), "height": int(height)}
    except Exception:
        return {"width": 0, "height": 0}


def collect_response_text(response: Any) -> str:
    try:
        if hasattr(response, "text") and response.text:
            return response.text
    except Exception:
        pass

    parts_out: list[str] = []
    candidates = getattr(response, "candidates", None) or []
    for candidate in candidates:
        content = getattr(candidate, "content", None) or candidate
        parts = getattr(content, "parts", None) or []
        for part in parts:
            if getattr(part, "thought", False):
                continue
            text_value = getattr(part, "text", None)
            if text_value:
                parts_out.append(text_value)
    return "\n".join(parts_out).strip()


def build_media_contents(prompt: str, media_paths: list[str]) -> tuple[list[Path], list[Any]]:
    require_image_stack()
    resolved_media = [resolve_path(path) for path in media_paths]
    contents: list[Any] = [prompt]
    for path in resolved_media:
        if not path.is_file():
            raise RuntimeError(f"media not found: {path}")
        mime_type, _ = mimetypes.guess_type(str(path))
        mime_type = mime_type or ""
        if not mime_type.startswith("image/"):
            raise RuntimeError(
                f"only image inputs are supported right now; got {mime_type or 'unknown'} for {path}"
            )
        contents.append(load_input_image(path))
    return resolved_media, contents


def generate_json_text(
    *,
    client: Any,
    model: str,
    contents: list[Any],
    system_prompt: str,
    temperature: float,
    max_tokens: int,
) -> str:
    cfg = gtypes.GenerateContentConfig(  # type: ignore[call-arg]
        system_instruction=system_prompt or None,
        response_mime_type="application/json",
        max_output_tokens=max_tokens,
        temperature=temperature,
    )
    response = client.models.generate_content(model=model, contents=contents, config=cfg)
    text = collect_response_text(response)
    if not text.strip():
        raise RuntimeError("model returned no text")
    return text


def render_images(
    *,
    prompt: str,
    image_paths: list[str],
    num_outputs: int,
    output_dir: Optional[str],
    label: Optional[str],
    model: str,
    temperature: float,
    system_prompt: str,
    aspect_ratio: Optional[str],
    image_size: Optional[str],
    json_out: Optional[str],
    candidate: Optional[dict[str, Any]],
) -> dict[str, Any]:
    if not prompt.strip():
        raise RuntimeError("prompt is required")
    if num_outputs < 1 or num_outputs > 4:
        raise RuntimeError("num_outputs must be between 1 and 4")

    client = init_client()
    root, out_dir = dated_output_dir(output_dir)
    resolved_inputs = [resolve_path(path) for path in image_paths]
    contents: list[Any] = [prompt]
    for path in resolved_inputs:
        contents.append(load_input_image(path))

    cfg_kwargs: dict[str, Any] = {
        "response_modalities": ["IMAGE", "TEXT"],
        "system_instruction": system_prompt or None,
        "temperature": temperature,
    }
    image_cfg = build_image_config(aspect_ratio=aspect_ratio, image_size=image_size)
    if image_cfg is not None:
        cfg_kwargs["image_config"] = image_cfg
    config = gtypes.GenerateContentConfig(  # type: ignore[call-arg]
        **{key: value for key, value in cfg_kwargs.items() if value is not None}
    )

    requested_outputs = num_outputs
    images: list[Any] = []
    texts: list[str] = []
    attempts = 0
    while len(images) < requested_outputs and attempts < requested_outputs:
        attempts += 1
        response = client.models.generate_content(model=model, contents=contents, config=config)
        candidates = getattr(response, "candidates", None) or []
        for candidate in candidates:
            content = getattr(candidate, "content", None) or candidate
            parts = getattr(content, "parts", None) or []
            for part in parts:
                if hasattr(part, "as_image") and callable(getattr(part, "as_image")):
                    try:
                        image_obj = part.as_image()  # type: ignore[call-arg]
                        if image_obj is not None:
                            images.append(image_obj.convert("RGB"))
                            continue
                    except Exception:
                        pass
                inline_img = decode_inline_image(part)
                if inline_img is not None:
                    images.append(inline_img)
                    continue
                text_value = getattr(part, "text", None)
                if text_value:
                    texts.append(text_value)

    images = images[:requested_outputs]
    if not images:
        raise RuntimeError("No image parts returned from Gemini.")

    stem = slugify(label) if label else prompt_stem(prompt)
    seq0 = next_seq(out_dir, stem)
    outputs: list[dict[str, Any]] = []
    for index, img in enumerate(images):
        filename = f"{stem}_{seq0 + index:03d}.png"
        output_path = (out_dir / filename).resolve()
        img.save(str(output_path), format="PNG")
        metadata = path_record(output_path, root=root)
        metadata.update(img_size(img))
        outputs.append(metadata)

    result = {
        "command": "edit",
        "createdAt": now_iso(),
        "prompt": prompt,
        "model": model,
        "temperature": temperature,
        "systemPrompt": system_prompt,
        "aspectRatio": aspect_ratio,
        "imageSize": image_size,
        "label": label,
        "input_count": len(resolved_inputs),
        "inputs": [path_record(path) for path in resolved_inputs],
        "requested_outputs": requested_outputs,
        "attempts": attempts,
        "output_count": len(outputs),
        "outputRoot": str(root),
        "outputDir": str(out_dir),
        "sdk": {
            "googleGenaiVersion": google_genai_version(),
            "imageConfigSupported": supports_image_config(),
        },
        "text": "\n".join(texts).strip() or None,
        "outputs": outputs,
    }
    if candidate is not None:
        result["candidate"] = candidate

    if json_out:
        json_path = resolve_path(json_out)
        write_json(json_path, result)
        result["jsonOut"] = str(json_path)

    return result


def extract_json_object(text: str) -> Optional[dict[str, Any]]:
    if not text.strip():
        return None

    fenced = re.search(r"```(?:json)?\s*(\{.*\})\s*```", text, flags=re.DOTALL)
    candidates = [fenced.group(1)] if fenced else []

    stripped = text.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        candidates.append(stripped)

    first = text.find("{")
    last = text.rfind("}")
    if first != -1 and last != -1 and last > first:
        candidates.append(text[first : last + 1])

    for candidate in candidates:
        try:
            payload = json.loads(candidate)
        except Exception:
            continue
        if isinstance(payload, dict):
            return payload
    return None


def clean_eval_text(value: Any) -> str:
    if not isinstance(value, str):
        return ""
    return " ".join(value.split()).strip()


def clean_eval_enum(value: Any, allowed: set[str], default: str) -> str:
    if isinstance(value, str):
        normalized = value.strip().lower().replace("-", "_").replace(" ", "_")
        if normalized in allowed:
            return normalized
    return default


def clean_eval_bool(value: Any, default: bool = False) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        normalized = value.strip().lower()
        if normalized in {"true", "yes", "1"}:
            return True
        if normalized in {"false", "no", "0"}:
            return False
    return default


def clean_eval_list(value: Any) -> list[str]:
    if isinstance(value, str):
        value = [value]
    if not isinstance(value, list):
        return []
    cleaned: list[str] = []
    seen: set[str] = set()
    for item in value:
        if not isinstance(item, str):
            continue
        normalized = " ".join(item.split()).strip()
        if not normalized:
            continue
        key = normalized.casefold()
        if key in seen:
            continue
        seen.add(key)
        cleaned.append(normalized)
    return cleaned


def clean_eval_score(value: Any, default: int) -> int:
    try:
        score = int(round(float(value)))
    except Exception:
        return default
    return max(0, min(100, score))


def default_score_for_match(match: str) -> int:
    return {"strong": 90, "partial": 60, "weak": 30}.get(match, 60)


def compose_blind_read_prompt() -> str:
    return "\n".join(
        [
            "Review the provided image or images without being told the intended concept.",
            "Return JSON only with exactly these keys:",
            "{",
            '  "description": "short visual summary",',
            '  "inferredConcept": "what concept or argument the image seems to communicate",',
            '  "diagramType": "diagram | symbolic_plate | scene | infographic | unclear",',
            '  "textPresent": false,',
            '  "clarity": "clear | partial | unclear",',
            '  "strengths": ["brief strings"],',
            '  "ambiguities": ["brief strings"],',
            '  "notes": "short justification"',
            "}",
        ]
    )


def compose_intent_eval_prompt(*, target_text: str) -> str:
    return "\n".join(
        [
            "Evaluate whether the provided image or images achieve the intended conceptual reading below.",
            f"Target brief: {target_text}",
            "Use this scoring rubric for overallScore (0-100):",
            "- conceptual match to the target: 50",
            "- composition and legibility: 25",
            "- symbolic precision: 15",
            "- absence of distracting text or clutter: 10",
            "Return JSON only with exactly these keys:",
            "{",
            '  "description": "short visual summary",',
            '  "match": "strong | partial | weak",',
            '  "conceptualFit": "strong | partial | weak",',
            '  "compositionFit": "strong | partial | weak",',
            '  "textInterference": "none | minor | major",',
            '  "strengths": ["brief strings"],',
            '  "issues": ["brief strings"],',
            '  "suggestedRefinement": "empty string if none",',
            '  "overallScore": 0,',
            '  "notes": "short justification"',
            "}",
        ]
    )


def compose_compare_prompt(*, target_text: str, candidate_count: int) -> str:
    return "\n".join(
        [
            f"Review {candidate_count} candidate images for the same target.",
            "The images are provided in order. Candidate 1 is the first image, Candidate 2 is the second image, and so on.",
            f"Target brief: {target_text}",
            "Use this scoring rubric for overallScore (0-100):",
            "- conceptual fit: 45",
            "- composition and legibility: 25",
            "- symbolic precision: 20",
            "- absence of distracting text or clutter: 10",
            "Return JSON only with exactly these keys:",
            "{",
            '  "bestCandidateIndex": 1,',
            '  "ranking": [1, 2, 3],',
            '  "overallNotes": "short comparison summary",',
            '  "candidates": [',
            "    {",
            '      "candidateIndex": 1,',
            '      "description": "short visual summary",',
            '      "match": "strong | partial | weak",',
            '      "conceptualFit": "strong | partial | weak",',
            '      "compositionFit": "strong | partial | weak",',
            '      "textInterference": "none | minor | major",',
            '      "strengths": ["brief strings"],',
            '      "issues": ["brief strings"],',
            '      "suggestedRefinement": "empty string if none",',
            '      "overallScore": 0,',
            '      "notes": "short justification"',
            "    }",
            "  ]",
            "}",
        ]
    )


def run_json_pass(
    *,
    prompt: str,
    media_paths: list[str],
    model: str,
    fallback_model: Optional[str],
    temperature: float,
    system_prompt: str,
    max_tokens: int,
) -> tuple[list[Path], str, dict[str, Any], str, bool]:
    client = init_client()
    resolved_media, contents = build_media_contents(prompt, media_paths)
    errors: list[str] = []
    model_names = [model]
    if fallback_model and fallback_model != model:
        model_names.append(fallback_model)

    for index, model_name in enumerate(model_names):
        try:
            text = generate_json_text(
                client=client,
                model=model_name,
                contents=contents,
                system_prompt=system_prompt,
                temperature=temperature,
                max_tokens=max_tokens,
            )
            payload = extract_json_object(text)
            if payload is None:
                raise RuntimeError("model returned non-JSON text")
            return resolved_media, text, payload, model_name, index > 0
        except Exception as exc:
            errors.append(f"{model_name}: {exc}")

    raise RuntimeError("all analysis models failed: " + " | ".join(errors))


def blind_read_result(payload: dict[str, Any], *, model_used: str, fallback_used: bool) -> dict[str, Any]:
    return {
        "modelUsed": model_used,
        "fallbackUsed": fallback_used,
        "description": clean_eval_text(payload.get("description")),
        "inferredConcept": clean_eval_text(payload.get("inferredConcept")),
        "diagramType": clean_eval_enum(
            payload.get("diagramType"),
            {"diagram", "symbolic_plate", "scene", "infographic", "unclear"},
            "unclear",
        ),
        "textPresent": clean_eval_bool(payload.get("textPresent"), default=False),
        "clarity": clean_eval_enum(payload.get("clarity"), {"clear", "partial", "unclear"}, "partial"),
        "strengths": clean_eval_list(payload.get("strengths")),
        "ambiguities": clean_eval_list(payload.get("ambiguities")),
        "notes": clean_eval_text(payload.get("notes")),
    }


def intent_eval_result(payload: dict[str, Any], *, model_used: str, fallback_used: bool) -> dict[str, Any]:
    match = clean_eval_enum(payload.get("match"), {"strong", "partial", "weak"}, "partial")
    return {
        "modelUsed": model_used,
        "fallbackUsed": fallback_used,
        "description": clean_eval_text(payload.get("description")),
        "match": match,
        "conceptualFit": clean_eval_enum(payload.get("conceptualFit"), {"strong", "partial", "weak"}, "partial"),
        "compositionFit": clean_eval_enum(payload.get("compositionFit"), {"strong", "partial", "weak"}, "partial"),
        "textInterference": clean_eval_enum(
            payload.get("textInterference"),
            {"none", "minor", "major"},
            "minor",
        ),
        "strengths": clean_eval_list(payload.get("strengths")),
        "issues": clean_eval_list(payload.get("issues")),
        "suggestedRefinement": clean_eval_text(payload.get("suggestedRefinement")),
        "overallScore": clean_eval_score(payload.get("overallScore"), default_score_for_match(match)),
        "notes": clean_eval_text(payload.get("notes")),
    }


def sanitize_compare_candidate(payload: dict[str, Any], *, candidate_index: int) -> dict[str, Any]:
    match = clean_eval_enum(payload.get("match"), {"strong", "partial", "weak"}, "partial")
    return {
        "candidateIndex": candidate_index,
        "description": clean_eval_text(payload.get("description")),
        "match": match,
        "conceptualFit": clean_eval_enum(payload.get("conceptualFit"), {"strong", "partial", "weak"}, "partial"),
        "compositionFit": clean_eval_enum(payload.get("compositionFit"), {"strong", "partial", "weak"}, "partial"),
        "textInterference": clean_eval_enum(
            payload.get("textInterference"),
            {"none", "minor", "major"},
            "minor",
        ),
        "strengths": clean_eval_list(payload.get("strengths")),
        "issues": clean_eval_list(payload.get("issues")),
        "suggestedRefinement": clean_eval_text(payload.get("suggestedRefinement")),
        "overallScore": clean_eval_score(payload.get("overallScore"), default_score_for_match(match)),
        "notes": clean_eval_text(payload.get("notes")),
    }


def compare_result(
    payload: dict[str, Any],
    *,
    candidate_count: int,
    model_used: str,
    fallback_used: bool,
) -> dict[str, Any]:
    raw_candidates = payload.get("candidates")
    candidate_map: dict[int, dict[str, Any]] = {}
    if isinstance(raw_candidates, list):
        for item in raw_candidates:
            if not isinstance(item, dict):
                continue
            try:
                candidate_index = int(item.get("candidateIndex"))
            except Exception:
                continue
            if candidate_index < 1 or candidate_index > candidate_count:
                continue
            candidate_map[candidate_index] = sanitize_compare_candidate(item, candidate_index=candidate_index)

    candidates: list[dict[str, Any]] = []
    for index in range(1, candidate_count + 1):
        candidates.append(candidate_map.get(index) or sanitize_compare_candidate({}, candidate_index=index))

    ranking_raw = payload.get("ranking")
    ranking: list[int] = []
    if isinstance(ranking_raw, list):
        seen: set[int] = set()
        for item in ranking_raw:
            try:
                candidate_index = int(item)
            except Exception:
                continue
            if candidate_index < 1 or candidate_index > candidate_count or candidate_index in seen:
                continue
            seen.add(candidate_index)
            ranking.append(candidate_index)
    if len(ranking) != candidate_count:
        ranking = [
            item["candidateIndex"]
            for item in sorted(candidates, key=lambda candidate: candidate.get("overallScore", 0), reverse=True)
        ]

    try:
        best_candidate = int(payload.get("bestCandidateIndex"))
    except Exception:
        best_candidate = ranking[0] if ranking else 1
    if best_candidate not in ranking:
        best_candidate = ranking[0] if ranking else 1

    return {
        "modelUsed": model_used,
        "fallbackUsed": fallback_used,
        "bestCandidateIndex": best_candidate,
        "ranking": ranking,
        "overallNotes": clean_eval_text(payload.get("overallNotes")),
        "candidates": candidates,
    }


def analyze_media(
    *,
    media_paths: list[str],
    prompt: str,
    candidate: Optional[dict[str, Any]],
    model: str,
    fallback_model: Optional[str],
    temperature: float,
    system_prompt: str,
    max_tokens: int,
    json_out: Optional[str],
) -> dict[str, Any]:
    blind_prompt = compose_blind_read_prompt()
    resolved_media, _, blind_payload, blind_model_used, blind_fallback_used = run_json_pass(
        prompt=blind_prompt,
        media_paths=media_paths,
        model=model,
        fallback_model=fallback_model,
        temperature=temperature,
        system_prompt=system_prompt,
        max_tokens=max_tokens,
    )

    target_text = prompt.strip() or (candidate.get("text", "").strip() if candidate else "")
    result = {
        "command": "analyze",
        "createdAt": now_iso(),
        "requestedModel": model,
        "fallbackModel": fallback_model,
        "temperature": temperature,
        "mediaCount": len(resolved_media),
        "media": [path_record(path) for path in resolved_media],
        "blindRead": blind_read_result(
            blind_payload,
            model_used=blind_model_used,
            fallback_used=blind_fallback_used,
        ),
    }
    if candidate is not None:
        result["candidate"] = candidate

    if target_text:
        _, _, intent_payload, intent_model_used, intent_fallback_used = run_json_pass(
            prompt=compose_intent_eval_prompt(target_text=target_text),
            media_paths=media_paths,
            model=model,
            fallback_model=fallback_model,
            temperature=temperature,
            system_prompt=system_prompt,
            max_tokens=max_tokens,
        )
        result["target"] = target_text
        result["intentEval"] = intent_eval_result(
            intent_payload,
            model_used=intent_model_used,
            fallback_used=intent_fallback_used,
        )

    if json_out:
        json_path = resolve_path(json_out)
        write_json(json_path, result)
        result["jsonOut"] = str(json_path)

    return result


def compare_media(
    *,
    media_paths: list[str],
    prompt: str,
    candidate: Optional[dict[str, Any]],
    model: str,
    fallback_model: Optional[str],
    temperature: float,
    system_prompt: str,
    max_tokens: int,
    json_out: Optional[str],
) -> dict[str, Any]:
    if len(media_paths) < 2:
        raise RuntimeError("compare requires at least two images")

    target_text = prompt.strip() or (candidate.get("text", "").strip() if candidate else "")
    if not target_text:
        raise RuntimeError("compare requires --prompt or --candidate-ref")

    resolved_media, _, payload, model_used, fallback_used = run_json_pass(
        prompt=compose_compare_prompt(target_text=target_text, candidate_count=len(media_paths)),
        media_paths=media_paths,
        model=model,
        fallback_model=fallback_model,
        temperature=temperature,
        system_prompt=system_prompt,
        max_tokens=max_tokens,
    )

    result = {
        "command": "compare",
        "createdAt": now_iso(),
        "requestedModel": model,
        "fallbackModel": fallback_model,
        "temperature": temperature,
        "target": target_text,
        "mediaCount": len(resolved_media),
        "media": [path_record(path) for path in resolved_media],
        "comparison": compare_result(
            payload,
            candidate_count=len(resolved_media),
            model_used=model_used,
            fallback_used=fallback_used,
        ),
    }
    if candidate is not None:
        result["candidate"] = candidate

    if json_out:
        json_path = resolve_path(json_out)
        write_json(json_path, result)
        result["jsonOut"] = str(json_path)

    return result


def clean_candidate_text(raw_line: str) -> str:
    text = raw_line.strip()
    text = re.sub(r"^\s*[-*]\s+", "", text)
    text = re.sub(r"^\s*#+\s+", "", text)
    text = re.sub(r"`?\[visual candidate\]`?", "", text, flags=re.IGNORECASE)
    text = text.replace("**", "")
    text = text.replace("`", "")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def candidate_slug(text: str) -> str:
    head = re.split(r"[.:]", text, maxsplit=1)[0]
    return slugify(head, max_len=40)


def candidate_from_ref(candidate_ref: str) -> dict[str, Any]:
    if ":" not in candidate_ref:
        raise RuntimeError("candidate ref must look like path/to/file.md:123")
    path_part, line_part = candidate_ref.rsplit(":", 1)
    try:
        line_no = int(line_part)
    except Exception as exc:
        raise RuntimeError(f"invalid candidate line number in {candidate_ref}") from exc
    if line_no < 1:
        raise RuntimeError("candidate line number must be >= 1")

    source_path = resolve_repo_path(path_part)
    if not source_path.is_file():
        raise RuntimeError(f"candidate source not found: {source_path}")

    lines = source_path.read_text(encoding="utf-8").splitlines()
    if line_no > len(lines):
        raise RuntimeError(f"candidate line {line_no} is out of range for {source_path}")
    line = lines[line_no - 1]
    if not VISUAL_CANDIDATE_PATTERN.match(line):
        raise RuntimeError(f"line {line_no} in {source_path} is not a [visual candidate] entry")

    cleaned = clean_candidate_text(line)
    rel_path = str(source_path.relative_to(REPO_ROOT))
    return {
        "ref": f"{rel_path}:{line_no}",
        "path": rel_path,
        "line": line_no,
        "slug": candidate_slug(cleaned),
        "text": cleaned,
    }


def iter_markdown_files(paths: list[str]) -> list[Path]:
    if paths:
        roots = [resolve_path(path) for path in paths]
    else:
        roots = [REPO_ROOT / root for root in DEFAULT_SCAN_ROOTS]

    files: list[Path] = []
    for root in roots:
        if root.is_file():
            if root.suffix.lower() == ".md":
                files.append(root)
            continue
        if not root.exists():
            continue
        files.extend(sorted(root.rglob("*.md")))
    return files


def list_visual_candidates(
    *,
    paths: list[str],
    query: str,
) -> dict[str, Any]:
    normalized_query = query.strip().lower()
    candidates: list[dict[str, Any]] = []
    for file_path in iter_markdown_files(paths):
        try:
            text = file_path.read_text(encoding="utf-8")
        except Exception:
            continue
        rel_path = str(file_path.resolve().relative_to(REPO_ROOT))
        for line_no, line in enumerate(text.splitlines(), start=1):
            match = VISUAL_CANDIDATE_PATTERN.match(line)
            if not match:
                continue
            cleaned = clean_candidate_text(line)
            haystack = f"{rel_path} {cleaned}".lower()
            if normalized_query and normalized_query not in haystack:
                continue
            candidates.append(
                {
                    "path": rel_path,
                    "line": line_no,
                    "slug": candidate_slug(cleaned),
                    "text": cleaned,
                }
            )
    return {
        "command": "list-candidates",
        "query": query,
        "count": len(candidates),
        "candidates": candidates,
    }


def keepers_root(path_str: Optional[str]) -> Path:
    root = resolve_path(path_str) if path_str else DEFAULT_KEEPERS_ROOT.resolve()
    return ensure_dir(root)


def next_keeper_path(root: Path, stem: str, suffix: str) -> Path:
    stem = slugify(stem)
    target = root / f"{stem}{suffix}"
    if not target.exists():
        return target.resolve()
    seq = next_seq(root, stem, suffix=suffix)
    return (root / f"{stem}_{seq:03d}{suffix}").resolve()


def promote_image(
    *,
    image_path: str,
    keepers_dir: Optional[str],
    slug: Optional[str],
    note: str,
    candidate: Optional[dict[str, Any]],
    json_out: Optional[str],
) -> dict[str, Any]:
    source = resolve_path(image_path)
    if not source.is_file():
        raise RuntimeError(f"source image not found: {source}")
    mime_type, _ = mimetypes.guess_type(str(source))
    if not (mime_type and mime_type.startswith("image/")):
        raise RuntimeError(f"promote expects an image file, got {mime_type or 'unknown'}: {source}")

    root = keepers_root(keepers_dir)
    stem = slug or (candidate.get("slug") if candidate else None) or source.stem
    target = next_keeper_path(root, stem, source.suffix.lower() or ".png")
    shutil.copy2(source, target)

    index_path = root / "keepers.json"
    index = load_json(index_path, default={"items": []})
    if not isinstance(index, dict):
        index = {"items": []}
    items = index.get("items")
    if not isinstance(items, list):
        items = []
        index["items"] = items

    entry = {
        "promotedAt": now_iso(),
        "slug": slugify(stem),
        "note": note,
        "keeper": path_record(target, root=root),
        "sourceImage": path_record(source),
    }
    if candidate is not None:
        entry["candidate"] = candidate

    items.append(entry)
    write_json(index_path, index)

    result = {
        "command": "promote",
        "promotedAt": entry["promotedAt"],
        "note": note,
        "keepersDir": str(root),
        "keeperIndex": str(index_path.resolve()),
        "keeper": entry["keeper"],
        "sourceImage": entry["sourceImage"],
    }
    if candidate is not None:
        result["candidate"] = candidate

    if json_out:
        json_path = resolve_path(json_out)
        write_json(json_path, result)
        result["jsonOut"] = str(json_path)

    return result


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Minimal Gemini vision CLI plus visual-candidate listing for bildung-2.0."
    )
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output.")

    subparsers = parser.add_subparsers(dest="command", required=True)

    edit = subparsers.add_parser("edit", help="Generate or edit images with Gemini.")
    edit.add_argument("prompt", help="Prompt or edit instruction.")
    edit.add_argument(
        "--image",
        dest="images",
        action="append",
        default=[],
        help="Optional input image path. Repeat for multiple images.",
    )
    edit.add_argument("--num-outputs", type=int, default=1, help="Number of output images (1-4).")
    edit.add_argument("--output-dir", help="Optional output root directory.")
    edit.add_argument("--label", help="Optional short label used for output filenames.")
    edit.add_argument("--json-out", help="Optional JSON output path.")
    edit.add_argument(
        "--candidate-ref",
        help="Optional visual-candidate source in path/to/file.md:line form. Logged into JSON metadata.",
    )
    edit.add_argument("--model", default=DEFAULT_IMAGE_MODEL)
    edit.add_argument("--temperature", type=float, default=0.7)
    edit.add_argument("--system-prompt", default="")
    edit.add_argument("--aspect-ratio")
    edit.add_argument("--image-size")

    analyze = subparsers.add_parser(
        "analyze",
        help="Analyze one or more images with a blind read first, then intent-aware evaluation when a target is available.",
    )
    analyze.add_argument("media", nargs="+", help="One or more image paths.")
    analyze.add_argument("--prompt", default="", help="Optional target brief for the intent-aware pass.")
    analyze.add_argument("--candidate-ref", help="Optional visual-candidate source in path/to/file.md:line form.")
    analyze.add_argument("--json-out", help="Optional JSON output path.")
    analyze.add_argument("--model", default=DEFAULT_ANALYZE_MODEL)
    analyze.add_argument("--fallback-model", default=DEFAULT_ANALYZE_FALLBACK_MODEL)
    analyze.add_argument("--temperature", type=float, default=DEFAULT_ANALYZE_TEMPERATURE)
    analyze.add_argument("--system-prompt", default="")
    analyze.add_argument("--max-tokens", type=int, default=8192)

    compare = subparsers.add_parser(
        "compare",
        help="Rank multiple images against a target brief or visual-candidate note.",
    )
    compare.add_argument("media", nargs="+", help="Two or more image paths.")
    compare.add_argument("--prompt", default="", help="Target brief for comparison. Optional when --candidate-ref is supplied.")
    compare.add_argument("--candidate-ref", help="Optional visual-candidate source in path/to/file.md:line form.")
    compare.add_argument("--json-out", help="Optional JSON output path.")
    compare.add_argument("--model", default=DEFAULT_ANALYZE_MODEL)
    compare.add_argument("--fallback-model", default=DEFAULT_ANALYZE_FALLBACK_MODEL)
    compare.add_argument("--temperature", type=float, default=DEFAULT_ANALYZE_TEMPERATURE)
    compare.add_argument("--system-prompt", default="")
    compare.add_argument("--max-tokens", type=int, default=8192)

    list_candidates = subparsers.add_parser(
        "list-candidates",
        help="List markdown entries tagged with [visual candidate].",
    )
    list_candidates.add_argument(
        "paths",
        nargs="*",
        help="Optional files or directories to scan. Defaults to 00-Notes/ and texts/.",
    )
    list_candidates.add_argument(
        "--query",
        default="",
        help="Optional case-insensitive substring filter against path and candidate text.",
    )

    promote = subparsers.add_parser(
        "promote",
        help="Copy a generated image into a keepers directory and append a keeper record.",
    )
    promote.add_argument("image_path", help="Image to promote into keepers.")
    promote.add_argument("--keepers-dir", help="Optional keepers directory. Defaults to texts/zeitmauer/visuals/keepers.")
    promote.add_argument("--slug", help="Optional keeper slug. Defaults to candidate slug or source stem.")
    promote.add_argument(
        "--candidate-ref",
        help="Optional visual-candidate source in path/to/file.md:line form.",
    )
    promote.add_argument("--note", default="", help="Optional curator note for why this image was kept.")
    promote.add_argument("--json-out", help="Optional JSON output path.")

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    try:
        if args.command == "edit":
            candidate = candidate_from_ref(args.candidate_ref) if args.candidate_ref else None
            result = render_images(
                prompt=args.prompt,
                image_paths=args.images,
                num_outputs=args.num_outputs,
                output_dir=args.output_dir,
                label=args.label,
                model=args.model,
                temperature=args.temperature,
                system_prompt=args.system_prompt,
                aspect_ratio=args.aspect_ratio,
                image_size=args.image_size,
                json_out=args.json_out,
                candidate=candidate,
            )
        elif args.command == "analyze":
            candidate = candidate_from_ref(args.candidate_ref) if args.candidate_ref else None
            result = analyze_media(
                media_paths=args.media,
                prompt=args.prompt,
                candidate=candidate,
                model=args.model,
                fallback_model=args.fallback_model,
                temperature=args.temperature,
                system_prompt=args.system_prompt,
                max_tokens=args.max_tokens,
                json_out=args.json_out,
            )
        elif args.command == "compare":
            candidate = candidate_from_ref(args.candidate_ref) if args.candidate_ref else None
            result = compare_media(
                media_paths=args.media,
                prompt=args.prompt,
                candidate=candidate,
                model=args.model,
                fallback_model=args.fallback_model,
                temperature=args.temperature,
                system_prompt=args.system_prompt,
                max_tokens=args.max_tokens,
                json_out=args.json_out,
            )
        elif args.command == "list-candidates":
            result = list_visual_candidates(paths=args.paths, query=args.query)
        elif args.command == "promote":
            candidate = candidate_from_ref(args.candidate_ref) if args.candidate_ref else None
            result = promote_image(
                image_path=args.image_path,
                keepers_dir=args.keepers_dir,
                slug=args.slug,
                note=args.note,
                candidate=candidate,
                json_out=args.json_out,
            )
        else:  # pragma: no cover
            raise RuntimeError(f"Unsupported command: {args.command}")
    except Exception as exc:
        payload = {"ok": False, "error": str(exc)}
        print(json.dumps(payload, indent=2 if args.pretty else None))
        return 1

    print(json.dumps(result, indent=2 if args.pretty else None))
    return 0


if __name__ == "__main__":
    sys.exit(main())
