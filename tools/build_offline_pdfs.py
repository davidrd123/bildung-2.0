#!/usr/bin/env python3
"""Build offline PDFs for text projects in bildung-2.0.

This keeps the existing bespoke Erkenntnisproblem compiler and uses Pandoc for
the other text projects, which already store readable markdown in stable
sequence order.

Usage:
    python3 tools/build_offline_pdfs.py all
    python3 tools/build_offline_pdfs.py zeitmauer escolios
    python3 tools/build_offline_pdfs.py --list
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class PandocProject:
    key: str
    title: str
    author: str
    subtitle: str
    input_glob: str
    output_pdf: str


PANDOC_PROJECTS = {
    "zeitmauer": PandocProject(
        key="zeitmauer",
        title="An der Zeitmauer",
        author="Ernst Junger",
        subtitle="Working Translation Draft",
        input_glob="texts/zeitmauer/parts/*.md",
        output_pdf="texts/zeitmauer/output/zeitmauer-draft.pdf",
    ),
    "tektologiya-vol1": PandocProject(
        key="tektologiya-vol1",
        title="Tektologiya Vol. 1",
        author="Alexander Bogdanov",
        subtitle="Working Translation Draft",
        input_glob="texts/tektologiya-vol1/parts/*.md",
        output_pdf="texts/tektologiya-vol1/output/tektologiya-vol1-draft.pdf",
    ),
    "escolios": PandocProject(
        key="escolios",
        title="Escolios a un texto implicito I",
        author="Nicolas Gomez Davila",
        subtitle="Working Translation Draft",
        input_glob="texts/escolios/sections/*.md",
        output_pdf="texts/escolios/output/escolios-i-draft.pdf",
    ),
    "escolios-ii": PandocProject(
        key="escolios-ii",
        title="Escolios a un texto implicito II",
        author="Nicolas Gomez Davila",
        subtitle="Working Translation Draft",
        input_glob="texts/escolios-ii/sections/*.md",
        output_pdf="texts/escolios-ii/output/escolios-ii-draft.pdf",
    ),
    "exegesis": PandocProject(
        key="exegesis",
        title="The Exegesis of Philip K. Dick",
        author="Philip K. Dick",
        subtitle="Reading Atlas Draft",
        input_glob="texts/exegesis/passes/*.md",
        output_pdf="texts/exegesis/output/exegesis-atlas-draft.pdf",
    ),
}

SPECIAL_PROJECTS = {"erkenntnisproblem-vol1"}
ALL_PROJECTS = [*SPECIAL_PROJECTS, *PANDOC_PROJECTS.keys()]


def run(cmd: list[str], quiet: bool = False) -> None:
    result = subprocess.run(
        cmd,
        cwd=ROOT,
        text=True,
        capture_output=quiet,
    )
    if result.returncode != 0:
        if quiet:
            if result.stdout:
                print(result.stdout.strip())
            if result.stderr:
                print(result.stderr.strip())
        raise SystemExit(result.returncode)


def ensure_dependencies() -> None:
    missing = [
        name for name in ("pandoc", "xelatex")
        if shutil.which(name) is None
    ]
    if missing:
        raise SystemExit(f"Missing required tools: {', '.join(missing)}")


def resolve_projects(requested: list[str]) -> list[str]:
    if not requested or requested == ["all"]:
        return ALL_PROJECTS

    unknown = [name for name in requested if name not in ALL_PROJECTS]
    if unknown:
        available = ", ".join(ALL_PROJECTS)
        raise SystemExit(f"Unknown project(s): {', '.join(unknown)}. Available: {available}")
    return requested


def build_erkenntnisproblem() -> None:
    run(["python3", "texts/erkenntnisproblem-vol1/scripts/export_viewer_index.py"])
    run(["python3", "texts/erkenntnisproblem-vol1/scripts/compile_pdf.py"])
    run(["python3", "texts/erkenntnisproblem-vol1/scripts/compile_pdf.py", "--split"])


def build_cover(project: PandocProject, file_count: int) -> str:
    today = date.today().isoformat()
    return (
        f"% {project.title}\n"
        f"% {project.author}\n"
        f"% {today}\n\n"
        f"*{project.subtitle}*\n\n"
        f"*Generated from `bildung-2.0` project sources for offline reading.*\n\n"
        f"*Source files included: {file_count}.*\n\n"
        f"*Working draft only. Not for distribution or citation.*\n\n"
        "\\newpage\n"
    )


def build_pandoc_project(project: PandocProject) -> None:
    input_paths = sorted((ROOT / Path()).glob(project.input_glob))
    if not input_paths:
        raise SystemExit(f"No input files matched {project.input_glob}")

    output_path = ROOT / project.output_pdf
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory() as tmpdir:
        cover_path = Path(tmpdir) / "cover.md"
        cover_path.write_text(build_cover(project, len(input_paths)), encoding="utf-8")

        cmd = [
            "pandoc",
            str(cover_path),
            *[str(path) for path in input_paths],
            "--from=gfm+smart",
            "--standalone",
            "--toc",
            "--pdf-engine=xelatex",
            "--output",
            str(output_path),
            "-V",
            "geometry:margin=1in",
            "-V",
            "mainfont=TeX Gyre Pagella",
            "-V",
            "sansfont=TeX Gyre Heros",
            "-V",
            "monofont=DejaVu Sans Mono",
            "-V",
            "colorlinks=true",
            "-V",
            "linkcolor=blue",
            "-V",
            "urlcolor=blue",
        ]
        run(cmd, quiet=True)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("projects", nargs="*", help="Project keys or 'all'")
    parser.add_argument("--list", action="store_true", help="List supported project keys and exit")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.list:
        for name in ALL_PROJECTS:
            print(name)
        return

    ensure_dependencies()
    projects = resolve_projects(args.projects)
    for name in projects:
        print(f"Building {name}...")
        if name == "erkenntnisproblem-vol1":
            build_erkenntnisproblem()
        else:
            build_pandoc_project(PANDOC_PROJECTS[name])
    print("Done.")


if __name__ == "__main__":
    main()
