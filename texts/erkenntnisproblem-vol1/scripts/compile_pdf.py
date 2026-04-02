#!/usr/bin/env python3
"""Compile English translation drafts into a printable PDF via XeLaTeX.

Reads the viewer-index.json (regenerate with export_viewer_index.py first)
and emits a LaTeX file, then compiles it. The output is a clean reading
copy of the English drafts with part headings, page references, and
glossary appendix.

Usage:
    python3 texts/erkenntnisproblem-vol1/scripts/compile_pdf.py
    python3 texts/erkenntnisproblem-vol1/scripts/compile_pdf.py --split  # bilingual side-by-side
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX_PATH = ROOT / "source" / "viewer-index.json"
OUTPUT_DIR = ROOT / "output"


def load_index() -> dict:
    with INDEX_PATH.open("r", encoding="utf-8") as f:
        return json.load(f)


def tex_escape(s: str) -> str:
    """Escape special LaTeX characters."""
    replacements = [
        ("\\", r"\textbackslash{}"),
        ("&", r"\&"),
        ("%", r"\%"),
        ("$", r"\$"),
        ("#", r"\#"),
        ("_", r"\_"),
        ("{", r"\{"),
        ("}", r"\}"),
        ("~", r"\textasciitilde{}"),
        ("^", r"\textasciicircum{}"),
    ]
    # Handle backslash first, then the rest
    s = s.replace("\\", "\x00BACKSLASH\x00")
    for old, new in replacements[1:]:
        s = s.replace(old, new)
    s = s.replace("\x00BACKSLASH\x00", r"\textbackslash{}")
    return s


def build_preamble(split: bool = False) -> str:
    geometry = "margin=1in" if not split else "margin=0.75in"
    return rf"""\documentclass[11pt,a4paper]{{article}}

\usepackage{{fontspec}}
\setmainfont{{TeX Gyre Pagella}}
\setsansfont{{TeX Gyre Heros}}
\setmonofont{{TeX Gyre Cursor}}

\usepackage[{geometry}]{{geometry}}
\usepackage{{fancyhdr}}
\usepackage{{titlesec}}
\usepackage{{enumitem}}
\usepackage{{xcolor}}
\usepackage{{microtype}}
{"\\usepackage{paracol}" if split else ""}

% Colors
\definecolor{{accent}}{{HTML}}{{7C3238}}
\definecolor{{faint}}{{HTML}}{{8A7E6E}}
\definecolor{{detext}}{{HTML}}{{5C5040}}

% Section formatting
\titleformat{{\section}}{{\Large\bfseries\color{{accent}}}}{{}}{{0pt}}{{}}
\titleformat{{\subsection}}{{\large\itshape\color{{accent}}}}{{}}{{0pt}}{{}}
\titlespacing*{{\section}}{{0pt}}{{2em}}{{0.8em}}
\titlespacing*{{\subsection}}{{0pt}}{{1.5em}}{{0.5em}}

% Header/footer
\pagestyle{{fancy}}
\fancyhf{{}}
\fancyhead[L]{{\small\textit{{Das Erkenntnisproblem}} — Translation Draft}}
\fancyhead[R]{{\small\thepage}}
\renewcommand{{\headrulewidth}}{{0.4pt}}

% Paragraph spacing
\setlength{{\parindent}}{{0pt}}
\setlength{{\parskip}}{{0.6em}}

% Latin inline
\newcommand{{\lat}}[1]{{\textit{{#1}}}}

\begin{{document}}

\begin{{titlepage}}
\vspace*{{4cm}}
\begin{{center}}
{{\Huge\bfseries Ernst Cassirer}}\\[1.5em]
{{\huge\itshape Das Erkenntnisproblem}}\\[0.3em]
{{\huge\itshape in der Philosophie und Wissenschaft}}\\[0.3em]
{{\huge\itshape der neueren Zeit}}\\[1.5em]
{{\Large Volume I}}\\[3em]
{{\large Working Translation Draft}}\\[0.5em]
{{\normalsize\color{{faint}} Generated from \texttt{{bildung-2.0}} project sources}}
\end{{center}}
\vfill
{{\small\color{{faint}}\noindent This is a working draft for review purposes only.\\
Not for distribution or citation.}}
\end{{titlepage}}

\tableofcontents
\newpage
"""


def build_english_body(data: dict) -> str:
    """Build English-only body text."""
    lines = []
    for part in data["parts"]:
        lines.append(rf"\section{{{tex_escape(part['title'])}}}")
        if part.get("scope"):
            lines.append(rf"{{\small\color{{faint}} {tex_escape(part['scope'])}}}")
            lines.append("")

        for section in part["sections"]:
            lines.append(rf"\subsection{{{tex_escape(section['heading'])}}}")
            for para in section.get("en_paragraphs", []):
                lines.append("")
                lines.append(tex_escape(para))
            lines.append("")

    return "\n".join(lines)


def build_split_body(data: dict) -> str:
    """Build bilingual side-by-side body using paracol."""
    lines = []
    for part in data["parts"]:
        lines.append(rf"\section{{{tex_escape(part['title'])}}}")
        if part.get("scope"):
            lines.append(rf"{{\small\color{{faint}} {tex_escape(part['scope'])}}}")
            lines.append("")

        for section in part["sections"]:
            lines.append(rf"\subsection{{{tex_escape(section['heading'])}}}")
            lines.append(r"\begin{paracol}{2}")
            lines.append(r"\setcolumnwidth{0.48\textwidth, 0.48\textwidth}")

            de_paras = section.get("de_paragraphs", [])
            en_paras = section.get("en_paragraphs", [])
            max_len = max(len(de_paras), len(en_paras))

            for i in range(max_len):
                en = en_paras[i] if i < len(en_paras) else ""
                de = de_paras[i] if i < len(de_paras) else ""

                # English on the left
                lines.append("")
                lines.append(tex_escape(en) if en else r"\textcolor{faint}{---}")
                lines.append(r"\switchcolumn")
                # German on the right
                lines.append(rf"{{\color{{detext}} {tex_escape(de) if de else r'\textcolor{faint}{---}'}}}")
                lines.append(r"\switchcolumn*")

            lines.append(r"\end{paracol}")
            lines.append("")

    return "\n".join(lines)


def build_glossary(data: dict) -> str:
    """Build glossary appendix."""
    glossary = data.get("glossary", [])
    if not glossary:
        return ""

    lines = [
        r"\newpage",
        r"\section*{Glossary}",
        r"\addcontentsline{toc}{section}{Glossary}",
        "",
        r"\begin{description}[style=nextline, leftmargin=2em]",
    ]

    for entry in glossary:
        term = tex_escape(entry["term"])
        preferred = tex_escape(entry.get("preferred") or "unsettled")
        status = entry.get("status", "unknown")
        alts = ", ".join(tex_escape(a) for a in entry.get("alternatives", []))
        notes = tex_escape(entry.get("notes", ""))

        status_color = {
            "open": "accent",
            "tentative": "faint",
        }.get(status, "faint")

        lines.append(rf"\item[\textit{{{term}}}] \textbf{{{preferred}}} "
                     rf"{{\small\color{{{status_color}}} [{status}]}}")
        if alts:
            lines.append(rf"  \\ {{\small also: {alts}}}")
        if notes:
            lines.append(rf"  \\ {{\small\color{{faint}} {notes}}}")

    lines.append(r"\end{description}")
    return "\n".join(lines)


def build_document(data: dict, split: bool = False) -> str:
    preamble = build_preamble(split)
    body = build_split_body(data) if split else build_english_body(data)
    glossary = build_glossary(data)
    return preamble + body + "\n" + glossary + "\n" + r"\end{document}" + "\n"


def main():
    split = "--split" in sys.argv

    if not INDEX_PATH.exists():
        print(f"Error: {INDEX_PATH} not found. Run export_viewer_index.py first.")
        sys.exit(1)

    data = load_index()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    suffix = "-split" if split else ""
    tex_path = OUTPUT_DIR / f"erkenntnisproblem-draft{suffix}.tex"
    pdf_path = OUTPUT_DIR / f"erkenntnisproblem-draft{suffix}.pdf"

    doc = build_document(data, split)
    tex_path.write_text(doc, encoding="utf-8")
    print(f"Wrote LaTeX: {tex_path}")

    # Compile twice for TOC
    for pass_num in (1, 2):
        result = subprocess.run(
            ["xelatex", "-interaction=nonstopmode", f"-output-directory={OUTPUT_DIR}", str(tex_path)],
            capture_output=True,
            text=True,
            cwd=ROOT,
        )
        if result.returncode != 0 and pass_num == 2:
            # Check if PDF was actually produced despite warnings
            if not pdf_path.exists():
                print(f"XeLaTeX error (pass {pass_num}):")
                log_path = OUTPUT_DIR / f"erkenntnisproblem-draft{suffix}.log"
                if log_path.exists():
                    log_lines = log_path.read_text().splitlines()
                    for line in log_lines[-30:]:
                        print(f"  {line}")
                sys.exit(1)
            else:
                print(f"  (XeLaTeX returned warnings on pass {pass_num}, but PDF was produced)")

    print(f"Wrote PDF:   {pdf_path}")
    print(f"  ({len(data['parts'])} parts, {len(data.get('glossary', []))} glossary terms)")


if __name__ == "__main__":
    main()
