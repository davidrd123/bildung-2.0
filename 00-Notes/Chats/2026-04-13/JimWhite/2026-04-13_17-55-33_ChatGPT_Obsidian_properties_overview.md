# Obsidian properties overview

Source: [ChatGPT](https://chatgpt.com/share/69dd904e-e694-83e8-b0c6-6823ad3fadf8)
Extracted: 2026-04-14T00:55:33.347Z
🚀 Exported with [Save my Chatbot](https://save.hugocolin.com)!

---

#### You said:

How do Obsidian properties work? Does it have other built-in logic?

 

#### ChatGPT said:

I’m checking the current Obsidian docs so I can explain the built-in behavior accurately, especially around newer Properties behavior and what counts as actual logic.

Thought for 12s

In Obsidian, **properties are just structured metadata attached to a note**. Under the hood, they are stored as **YAML frontmatter** at the top of the Markdown file, and Obsidian gives you a nicer UI for editing them. They can hold text, lists, numbers, checkboxes, dates, date-times, and tags. Obsidian also has a few built-in special property names like `tags`, `aliases`, and `cssclasses`. Once you assign a type to a property name, that type is used for that property name across the whole vault. [Obsidian+1](https://obsidian.md/help/properties)

Example:

YAML

--- 
status: active 
due: 2026-04-20 
tags: 
 - project 
 - writing 
rating: 4 
---

What properties *do* by themselves is fairly modest:

They help you **organize notes**.

They support **property-aware search syntax**.

They work with **templates**, where template properties get added or merged into a note.

They can be managed globally through the **Properties view** core plugin, which lets you inspect property names/types and rename them across the vault. [Obsidian+1](https://obsidian.md/help/properties)

So on their own, properties are **data, not a full rules engine**.

As for “other built-in logic”: **yes, but only in certain features**.

The main built-in logic layer is **Bases**, a core plugin that gives you database-like views over notes and their properties. In Bases you can **sort, filter, group, and calculate formulas** from properties. Its filter system supports boolean structure like `and`, `or`, and `not`, and formulas support arithmetic plus built-in functions. Bases also includes built-in summary formulas like Average, Min, Max, Sum, Earliest, and Latest. [Obsidian+1](https://obsidian.md/help/bases)

So the practical picture is:

**Properties** = stored metadata fields on notes.

**Search / Templates / Properties view** = built-in ways to use that metadata.

**Bases** = built-in logic for querying, filtering, and computing with that metadata. [Obsidian+3Obsidian+3Obsidian+3](https://obsidian.md/help/properties)

A couple of limits are worth knowing:

Obsidian’s Properties UI does **not currently support nested properties** well.

Bulk editing is limited outside the dedicated views and external tools/plugins. [Obsidian](https://obsidian.md/help/properties)

So if you are asking, “Can Obsidian properties behave like variables with automation, conditions, and computed fields?” the answer is:

**Partly built in** through **Bases** formulas and filters.

**Not as a full app-logic system** by default.

For heavier automation, people usually add community plugins such as Dataview, Templater, Tasks, or custom plugins. [Obsidian+2Obsidian+2](https://obsidian.md/help/properties)

If you want, I can show the difference between **plain properties**, **Bases formulas**, and **Dataview logic** with a small concrete example.

![](https://www.google.com/s2/favicons?domain=https://obsidian.md&sz=32)

Sources

 

#### You said:

Are there any properties with defined behavior?

 

#### ChatGPT said:

I’m checking which property names Obsidian treats specially versus ordinary user-defined fields, so I can separate built-in behavior from just “metadata with a type.”

Thought for 6s

Yes. A **small number** of property names have built-in behavior; most others are just user-defined metadata.

The main built-in ones are:

**`tags`** — treated as note tags by Obsidian, not just plain text. [Obsidian](https://obsidian.md/help/properties?utm_source=chatgpt.com)

**`aliases`** — used as alternate names for a note, which affects linking behavior. [Obsidian](https://obsidian.md/help/properties?utm_source=chatgpt.com)

**`cssclasses`** — adds CSS classes to the note’s view so snippets/themes can style that note differently. [Obsidian+1](https://obsidian.md/help/properties?utm_source=chatgpt.com)

Everything else is generally just a typed field unless a built-in feature or plugin uses it. Obsidian’s official Properties docs explicitly call out those defaults and otherwise describe properties as structured metadata with types like text, list, number, date, and tags. [Obsidian+1](https://obsidian.md/help/properties?utm_source=chatgpt.com)

One version-related gotcha: older singular names like **`tag`**, **`alias`**, and **`cssclass`** were deprecated and support was later removed in newer Obsidian versions; the plural forms are the current supported ones. [Obsidian Forum+1](https://forum.obsidian.md/t/reconsider-ending-support-for-tag-alias-cssclass/100992?utm_source=chatgpt.com)

So the practical rule is:

**Special behavior:** `tags`, `aliases`, `cssclasses`

**Everything else:** ordinary metadata unless something else reads it

Example:

YAML

--- 
tags: 
 - project 
aliases: 
 - My Alternate Note Name 
cssclasses: 
 - wide-page 
status: active 
priority: 2 
---

Here, `status` and `priority` do not mean anything to core Obsidian by themselves, but `tags`, `aliases`, and `cssclasses` do.

I can also give you a longer list of what Obsidian core treats specially beyond properties, like file name, links, headings, embeds, tasks, and Bases fields.

![](https://www.google.com/s2/favicons?domain=https://forum.obsidian.md&sz=32)

![](https://www.google.com/s2/favicons?domain=https://obsidian.md&sz=32)

Sources

 

#### You said:

We need to map Obsidian vaults into wiki3.ai's JupyterLite notebook approach. .ipynb to/from .md supports working in either format. Can we use the parameters metadata for Jupyter notebooks for the templates feature of Obsidian?

 

#### ChatGPT said:

I’m checking the current notebook metadata conventions and how Obsidian templates/properties behave, then I’ll map the two cleanly and call out the edge cases.

Thought for 18s

Yes, **you can use notebook metadata as the backing store for an Obsidian-like template system**, but I would **not** use Papermill’s `parameters` convention itself as the primary equivalent of Obsidian templates. A better mapping is:

**Obsidian template fields / frontmatter** ⇄ **notebook metadata or a dedicated template cell**

**Papermill `parameters`** ⇄ **runtime inputs for executable notebooks**

That split stays closer to what each system is designed to do. In Jupyter, metadata is intentionally extensible: notebook, cell, and output metadata can contain arbitrary JSON-able data, and custom metadata should use a unique namespace. [nbformat+1](https://nbformat.readthedocs.io/en/latest/format_description.html?utm_source=chatgpt.com)

Why I would not make Papermill `parameters` the direct equivalent of Obsidian templates:

Papermill’s model is specifically about **parameterizing notebook execution**. You mark a cell with the `parameters` tag, Papermill treats the assignments in that cell as defaults, and when executing it can insert an `injected-parameters` cell with overrides. That is execution-time behavior, not note-creation behavior. It also has semantics that can be surprising for derived values, because overrides are injected after the original parameter cell rather than recomputing dependent assignments inside it. [Papermill+1](https://papermill.readthedocs.io/_/downloads/en/latest/pdf/)

Obsidian’s core Templates plugin is much simpler: it inserts predefined text snippets and replaces a small built-in set of variables such as `{{title}}`, `{{date}}`, and `{{time}}`. In practice, templates often include YAML frontmatter at note creation time. That means Obsidian templates are fundamentally **content scaffolds**, not execution parameters. [Obsidian](https://obsidian.md/help/plugins/templates)

So for wiki3.ai’s JupyterLite-notebook approach, I’d recommend this mapping:

Obsidian note frontmatter 
 ↓ 
Notebook metadata["wiki3"] or metadata["obsidian"]

and optionally:

Obsidian template body 
 ↓ 
A markdown cell tagged/named as a template scaffold

Because Jupyter metadata is arbitrary JSON, you can safely define a namespace like `metadata.wiki3.template`, `metadata.wiki3.properties`, or `metadata.obsidian.frontmatter`. That gives you a stable place to round-trip Obsidian properties without overloading Papermill semantics. [nbformat+1](https://nbformat.readthedocs.io/en/latest/format_description.html?utm_source=chatgpt.com)

A practical design would be:

JSON

{ 
 "metadata": { 
 "wiki3": { 
 "template": "project-note", 
 "properties": { 
 "status": "draft", 
 "tags": ["project", "research"], 
 "due": "2026-04-20" 
 } 
 } 
 } 
}

Then your `.ipynb ↔ .md` converter can render that as Obsidian frontmatter in Markdown:

YAML

--- 
template: project-note 
status: draft 
tags: 
 - project 
 - research 
due: 2026-04-20 
---

That is a clean conceptual match because Obsidian properties are basically structured metadata on a note, while notebook metadata is also structured metadata on the document. [nbformat+1](https://nbformat.readthedocs.io/en/latest/format_description.html?utm_source=chatgpt.com)

Where Papermill *does* fit nicely is as an **optional second layer**:

use `metadata.wiki3.properties` for the canonical note/template fields

generate a Papermill `parameters` cell from a selected subset when the notebook is meant to execute

on export back to Markdown, write the canonical metadata back to frontmatter, not the transient `injected-parameters` cell

That way, a notebook can be both a note and an executable artifact without confusing “template defaults” with “run-time overrides.” Papermill itself treats `parameters` and `injected-parameters` as execution machinery, which is why I would keep them derived rather than canonical. [Papermill+1](https://papermill.readthedocs.io/_/downloads/en/latest/pdf/)

I would also avoid storing all template information only in **cell tags**, because Jupyter cell tags are just a list of strings like `tags: string[]`. They are useful for marking roles such as `parameters`, `template`, `frontmatter`, or `hide-input`, but they are too thin to carry the full structure of Obsidian properties on their own. [JupyterLab Documentation+1](https://jupyterlab.readthedocs.io/en/latest/api/interfaces/nbformat.IBaseCellMetadata.html)

So the answer is:

**Yes, you can absolutely use Jupyter notebook metadata to support an Obsidian-like template feature.** 

But **use general notebook metadata as the canonical store**, and treat Papermill `parameters` as a derived execution interface, not as the template system itself. [nbformat+2Papermill+2](https://nbformat.readthedocs.io/en/latest/format_description.html?utm_source=chatgpt.com)

A good rule of thumb is:

**Template / vault semantics** → notebook metadata

**Executable defaults / reruns** → Papermill `parameters`

**Round-trip `.md` compatibility** → YAML frontmatter generated from canonical metadata

That will make `.md` and `.ipynb` feel like two views of the same document instead of two competing models. [nbformat+2Obsidian+2](https://nbformat.readthedocs.io/en/latest/format_description.html?utm_source=chatgpt.com)

I can sketch a concrete round-trip schema next, including which Obsidian fields should map to notebook metadata, cell tags, markdown cells, and Papermill parameters.

![](https://www.google.com/s2/favicons?domain=https://obsidian.md&sz=32)

![](https://www.google.com/s2/favicons?domain=https://papermill.readthedocs.io&sz=32)

![](https://www.google.com/s2/favicons?domain=https://nbformat.readthedocs.io&sz=32)

Sources

 

#### You said:

What Jupyter extension(s) implement this frontmatter concept in notebooks? And we should make our approach compatible with Obsidian so that we could roundtrip edits of the .md files including templates and other special stuff like that.

 

#### ChatGPT said:

I’m looking for the most relevant notebook-side implementations of “frontmatter” and for formats that already round-trip Markdown plus notebook structure cleanly, so I can recommend a compatibility path instead of inventing one.

I’ve got the likely candidates now. The main distinction is between tools that *store notebook metadata in YAML frontmatter* and tools that *render special frontmatter semantics*; for Obsidian compatibility, that distinction matters a lot.

Thought for 57s

There is **not one canonical Jupyter extension that adds “Obsidian-style frontmatter to notebooks.”** The main things in this space are:

**Jupytext**: text notebooks in `.md` with an optional YAML header, synchronized with `.ipynb`. [Jupytext+1](https://jupytext.readthedocs.io/en/latest/formats-markdown.html)

**MyST notebooks**: Markdown notebooks that use frontmatter mainly so Jupytext/MyST can convert them to `.ipynb`. [Jupyter Book](https://jupyterbook.org/v1/file-types/myst-notebooks.html)

**Quarto**: supports YAML front matter for notebook documents, and in `.ipynb` it uses the **first Raw cell** for document YAML. [Quarto+1](https://quarto.org/docs/tools/jupyter-lab.html)

So the answer to “what Jupyter extension implements this frontmatter concept?” is mostly:

**Jupytext is the closest match for Markdown-frontmatter roundtripping.**
MyST and Quarto also use frontmatter, but they are more publishing/document systems than “Obsidian metadata compatibility layers.” [Jupytext+2Jupyter Book+2](https://jupytext.readthedocs.io/en/latest/formats-markdown.html)

## What I’d use for wiki3.ai

For **Obsidian compatibility**, I would make the canonical editable `.md` format be:

**plain Markdown**

**standard YAML frontmatter at the top**

**Obsidian keys preserved exactly**

**Jupyter-specific data kept separate**

That is because Obsidian properties are YAML at the top of the file, and its core Templates plugin is just text insertion with variables like `{{title}}`, `{{date}}`, and `{{time}}`. [Obsidian+1](https://obsidian.md/help/properties)

## Best compatibility choice

Use **Jupytext Markdown** as the notebook-text representation, because:

it already supports a YAML header, [Jupytext](https://jupytext.readthedocs.io/en/latest/formats-markdown.html)

it preserves Markdown cells **verbatim**, [Jupytext](https://jupytext.readthedocs.io/en/latest/formats-markdown.html)

it supports paired `.ipynb` + `.md` workflows, where opening/saving updates both sides. [Jupytext](https://jupytext.readthedocs.io/en/latest/paired-notebooks.html)

That makes it the least disruptive base for Obsidian roundtripping.

## Important design point

I would **not** make raw Jupytext YAML the canonical frontmatter for user notes, because Jupytext expects notebook metadata under the `jupyter:` section. It says custom notebook metadata like `author` or `title` can go under `jupyter:` and be synchronized to notebook metadata. [Jupytext](https://jupytext.readthedocs.io/en/latest/formats-markdown.html)

That is fine for Jupyter, but not ideal for Obsidian, because:

Obsidian wants properties as normal top-level frontmatter fields. [Obsidian](https://obsidian.md/help/properties)

Obsidian does not fully support nested properties well in its UI. [Obsidian](https://obsidian.md/help/properties)

So for wiki3.ai, I’d treat this as a **bridge problem**, not something to hand entirely to Jupytext.

## Recommended schema

Use `.md` as the **authoritative note format** and keep:

YAML

--- 
title: Project Alpha 
status: draft 
tags: 
 - project 
 - research 
aliases: 
 - Alpha 
cssclasses: 
 - wide-page 
 
wiki3_template: project-note 
 
jupyter: 
 jupytext: 
 formats: ipynb,md 
 text_representation: 
 extension: .md 
 format_name: markdown 
 kernelspec: 
 name: python3 
 display_name: Python 3 
 language: python 
---

Why this works:

`title`, `status`, `tags`, `aliases`, `cssclasses`, and your template marker are plain Obsidian-visible properties. Obsidian’s default built-in properties include `tags`, `aliases`, and `cssclasses`. [Obsidian](https://obsidian.md/help/properties)

`jupyter:` is reserved for notebook sync metadata, which Jupytext understands. [Jupytext](https://jupytext.readthedocs.io/en/latest/formats-markdown.html)

## What should happen in `.ipynb`

On conversion to `.ipynb`, your bridge should:

write the Jupyter metadata to normal notebook metadata

copy the Obsidian-facing frontmatter fields into a dedicated notebook metadata namespace, such as:

`metadata.wiki3.frontmatter`

or `metadata.obsidian.frontmatter`

That gives you lossless roundtripping even when `.ipynb` is edited directly.

I would **not** rely on Quarto’s Raw first-cell YAML as the canonical notebook storage for this use case, because that is Quarto document metadata, not a neutral Obsidian-compatible metadata model. Quarto also notes that `.ipynb ↔ .qmd` roundtrips can concatenate consecutive markdown cells and turn raw cells into markdown cells, which is not ideal when you care about strict structural fidelity. [Quarto+1](https://quarto.org/docs/tools/jupyter-lab.html)

## Templates and “special stuff”

For Obsidian templates specifically:

Obsidian Templates is a **text insertion system**, not a notebook metadata system. [Obsidian](https://obsidian.md/help/plugins/templates)

So template source files should remain ordinary `.md` notes with frontmatter and template variables like `{{title}}` and `{{date}}`. [Obsidian](https://obsidian.md/help/plugins/templates)

Your converter should preserve those variables **literally** when handling template files, not try to evaluate them.

That means:

**regular notes**: roundtrip as note content + metadata

**template notes**: roundtrip as literal template source files

A simple rule is to mark templates with a property like:

YAML

template: true

or

YAML

wiki3_kind: template

and then preserve the body exactly.

## Obsidian compatibility details worth preserving

A few things matter if you want real Obsidian compatibility:

`tags`, `aliases`, and `cssclasses` should use the current plural forms. [Obsidian](https://obsidian.md/help/properties)

Internal links in frontmatter should be quoted, like `link: "[[Note]]"`. [Obsidian](https://obsidian.md/help/properties)

List properties should remain YAML lists. [Obsidian](https://obsidian.md/help/properties)

Date properties should stay in Obsidian’s expected date formats. [Obsidian](https://obsidian.md/help/properties)

## What about code cells in Obsidian?

Jupytext Markdown already has a workable answer:

markdown cells are stored as markdown

code cells are fenced code blocks

cell metadata can be appended after the language

raw cells can be represented with HTML comment markers. [Jupytext](https://jupytext.readthedocs.io/en/latest/formats-markdown.html)

So Obsidian can still open the `.md` file as readable Markdown, even if it will not treat those notebook-specific fences/comments specially.

## My recommendation

I would standardize on this:

**Canonical user-editable source:** plain `.md`

**Markdown dialect:** **Jupytext Markdown**, not MyST or Quarto

**Obsidian properties:** top-level YAML keys

**Notebook sync metadata:** under `jupyter:`

**Lossless notebook-only metadata:** mirrored in `.ipynb` under `metadata.wiki3.*`

**Templates:** preserved as literal Obsidian template files, not converted into Papermill/Quarto semantics

That gives you the best chance of roundtripping:

Obsidian edits

Obsidian templates

Obsidian special properties

notebook edits

executable notebook structure

without making Obsidian users write MyST or Quarto-specific syntax.

The one thing I’d avoid is making **MyST** or **Quarto** the canonical markdown format for vault files, because both introduce extra semantics that are useful for publishing, but not ideal when your primary requirement is “must behave like normal Obsidian Markdown.” [Jupyter Book+2Quarto+2](https://jupyterbook.org/v1/file-types/myst-notebooks.html)

I can draft a concrete roundtrip spec next: exact YAML fields, exact `.ipynb metadata` layout, and the conversion rules for templates, tags, aliases, links, and code cells.

![](https://www.google.com/s2/favicons?domain=https://quarto.org&sz=32)

![](https://www.google.com/s2/favicons?domain=https://jupyterbook.org&sz=32)

![](https://www.google.com/s2/favicons?domain=https://jupytext.readthedocs.io&sz=32)

Sources

 

#### You said:

Another convention we want to integrate into wiki3.ai are skill.md specs like in Hermes agent. A key improvement is we can incorporate both the skill .md content but also in some or maybe even most cases the code too by using the correct kernel. This is a case for parameterized notebooks, for both skills and subtasks.

 

#### ChatGPT said:

I’m checking the current public references for “skill.md” and notebook parameterization patterns so I can ground the design in real conventions rather than guessing from memory.

The public pieces line up pretty well: SKILL.md is a Markdown-plus-frontmatter convention, while parameterized notebooks are a good fit for the executable side. I’m pulling the authoritative docs that matter for a round-trip design.

Thought for 15s

Yes — that is a strong fit, and it suggests a **three-layer model** for wiki3.ai rather than trying to force everything into either plain Markdown or plain notebooks.

## Recommended model

Treat a skill as three separable things:

**Skill identity and routing metadata**
Stored in **Obsidian-compatible YAML frontmatter** at the top of the `.md` file.

**Human-readable instructions**
Stored in the **Markdown body** of `SKILL.md`, matching the Agent Skills / Hermes-style convention that the body is free-form instructions after frontmatter. [GitHub+1](https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx?utm_source=chatgpt.com)

**Executable implementation and subtask logic**
Stored in a paired `.ipynb`, with **parameter cells** for runtime inputs and the correct kernel for the language or environment. Papermill’s model is explicitly built around a cell tagged `parameters`, plus injected overrides at execution time. [Papermill+2Papermill+2](https://papermill.readthedocs.io/en/latest/usage-parameterize.html?utm_source=chatgpt.com)

That gives you a clean distinction:

**frontmatter** = what the skill *is*

**Markdown body** = how the skill *should be used*

**parameterized notebook** = what the skill *can execute*

## Why this matches the SKILL.md ecosystem

The public skill conventions are already very close to what you want:

The Agent Skills format expects a `SKILL.md` with YAML frontmatter and a Markdown body. The body has no strict format restrictions and is meant to hold task instructions, examples, edge cases, and workflow guidance. [GitHub+1](https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx?utm_source=chatgpt.com)

Hermes-style loading also centers around recursively discovering `SKILL.md` files rather than treating skills as code-first packages. [GitHub+1](https://github.com/mudrii/hermes-agent-docs/blob/main/skills.md?utm_source=chatgpt.com)

So wiki3.ai can stay compatible by keeping `SKILL.md` as the primary skill manifest and human-editable document.

## Why notebooks help

Parameterized notebooks are a good fit for the **executable half** of skills and subtasks because Papermill already provides a standard convention:

mark a cell with the `parameters` tag,

put default values there,

override them at execution time,

and keep the rest of the notebook as normal executable logic. [Papermill+2Papermill+2](https://papermill.readthedocs.io/en/latest/usage-parameterize.html?utm_source=chatgpt.com)

That is especially useful when:

a skill needs actual code execution,

the implementation language varies by kernel,

the same skill scaffold is reused with different inputs,

or a skill decomposes into executable subtasks.

## Best way to combine them

I would make `SKILL.md` the canonical skill file and pair it with an optional notebook.

Example structure:

skills/ 
 summarize-csv/ 
 SKILL.md 
 skill.ipynb 
 helpers.py 
 examples/

### `SKILL.md`

Use Obsidian-compatible frontmatter first:

YAML

--- 
name: summarize-csv 
description: Summarize a CSV file and produce charts and key findings. 
tags: 
 - data 
 - notebook 
 - reporting 
aliases: 
 - csv-summary 
wiki3_kind: skill 
wiki3_notebook: skill.ipynb 
wiki3_kernel: python3 
wiki3_parameters_schema: 
 input_path: string 
 max_rows: integer 
 include_charts: boolean 
template: false 
---

Then the body remains ordinary skill instructions:

Markdown

When to use 
- Use for tabular CSV datasets where a quick profile and summary are needed. 
 
Steps 
1. Validate the CSV path. 
2. Load the dataset. 
3. Compute descriptive statistics. 
4. Generate charts if requested. 
5. Write a concise findings summary. 
 
Edge cases 
- Empty file 
- Missing headers 
- Very large row counts

This stays compatible with the existing skill format idea that the Markdown body is the instructions layer. [GitHub+1](https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx?utm_source=chatgpt.com)

### `skill.ipynb`

Use the notebook for actual execution:

first code cell tagged `parameters`

remaining cells implement the task

notebook metadata stores kernel and any notebook-only execution metadata

Papermill’s conventions already define the `parameters` tag and injected override behavior, so you do not need to invent execution semantics. [Papermill+1](https://papermill.readthedocs.io/en/latest/usage-parameterize.html?utm_source=chatgpt.com)

## How this should round-trip with Obsidian

For Obsidian compatibility, the key rule should be:

**all skill-defining metadata that a human may edit should live in top-level YAML frontmatter in the Markdown file.**

That is important because Obsidian properties are just YAML frontmatter fields, and its special built-in ones like `tags`, `aliases`, and `cssclasses` work only when preserved in normal Obsidian form. Obsidian templates are also fundamentally Markdown/text-based scaffolds, not notebook execution specs. [Jupytext](https://jupytext.readthedocs.io/en/latest/formats-markdown.html?utm_source=chatgpt.com)

So I would avoid making the notebook metadata the canonical source for user-facing fields.

Instead:

`.md` is canonical for:

skill name

description

tags

aliases

template markers

routing hints

skill instructions

`.ipynb` is canonical for:

executable cells

outputs

kernel/runtime-specific execution metadata

## Where Jupytext fits

Jupytext is the best existing bridge for this because its Markdown notebook formats support an optional YAML header storing selected notebook metadata, and it is designed for paired `.ipynb` + `.md` workflows. [Jupytext+1](https://jupytext.readthedocs.io/en/latest/formats-markdown.html?utm_source=chatgpt.com)

That means wiki3.ai can do one of two things:

### Option A: paired files

`SKILL.md` = skill manifest + instructions

`skill.ipynb` = execution artifact

This is the safest and cleanest.

### Option B: one Markdown notebook file

Use a Jupytext Markdown notebook as the canonical file and embed both notebook structure and frontmatter in a single `.md`. Jupytext supports Markdown notebooks with YAML headers. [Jupytext+1](https://jupytext.readthedocs.io/en/latest/formats-markdown.html?utm_source=chatgpt.com)

But for **Obsidian roundtripping**, I still prefer **paired files**, because a pure Jupytext notebook Markdown file has notebook cell markers and notebook conventions mixed into the note. That is workable, but less “native Obsidian.”

## Templates vs parameters

This is the key conceptual split:

**Obsidian templates** are for **note creation / scaffolding**

**Papermill parameters** are for **execution-time inputs**

Those are related, but not identical.

A good design is:

A template creates a new skill or subtask note with frontmatter defaults.

Some of those frontmatter fields are then mapped into the notebook’s parameter cell at execution time.

The notebook runs with the selected kernel and produces results.

So a template might define:

YAML

--- 
wiki3_template: subtask 
status: draft 
input_path: data.csv 
include_charts: true 
---

and the runtime bridge would map `input_path` and `include_charts` into Papermill parameters before execution. That keeps template defaults and runtime overrides distinct, which is safer than conflating them.

## Skills and subtasks should use the same pattern

You mentioned using this for both **skills** and **subtasks**. I think that is right.

Use the same document model for both:

`wiki3_kind: skill`

`wiki3_kind: subtask`

and optionally:

`wiki3_parent_skill`

`wiki3_subtask_of`

`wiki3_notebook`

`wiki3_kernel`

Then both can have:

human-readable instructions in Markdown

structured metadata in frontmatter

optional executable backing in notebooks

That gives you a uniform architecture instead of separate note and execution systems.

## A concrete compatibility rule set

I’d recommend these rules:

### Canonical Markdown rule

Keep all user-editable metadata in top-level YAML frontmatter in the `.md` file.

### Notebook mirroring rule

Mirror that metadata into notebook metadata under a dedicated namespace such as:

JSON

metadata: { 
 "wiki3": { 
 "frontmatter": { ... }, 
 "kind": "skill", 
 "linked_markdown": "SKILL.md" 
 } 
}

### Execution rule

Only a selected subset of frontmatter becomes notebook parameters, for example:

`input_path`

`question`

`dataset`

`model`

`max_rows`

Do not blindly convert all frontmatter into runtime parameters.

### Template rule

Preserve template source files literally as Markdown so Obsidian can keep editing them naturally.

### Kernel rule

Put language/runtime binding in frontmatter and notebook metadata, for example:

YAML

wiki3_kernel: python3 
wiki3_runtime: papermill

## One important caution

Papermill parameters are great for runtime inputs, but they are not a full declarative workflow system. Papermill’s own docs warn that parameter cells can behave unintuitively with interdependent assignments because overrides are injected after the defaults cell rather than recomputing earlier derived values in that cell. [Papermill](https://papermill.readthedocs.io/_/downloads/en/latest/pdf/?utm_source=chatgpt.com)

So for skills/subtasks, I would use Papermill parameters for:

simple inputs

file paths

toggles

model names

limits

but not for complex dependency graphs. For those, put the logic in regular notebook code.

## Bottom line

Yes — **skill.md + parameterized notebooks is a very good combined model**.

The cleanest wiki3.ai design is:

**`SKILL.md` stays the canonical skill spec**

**Obsidian-compatible frontmatter stays the canonical metadata**

**Markdown body stays the canonical instructions**

**paired `.ipynb` provides executable implementation**

**Papermill parameters provide runtime inputs for skills and subtasks**

**Jupytext provides the text/notebook bridge when needed** [GitHub+5Papermill+5Jupytext+5](https://papermill.readthedocs.io/en/latest/usage-parameterize.html?utm_source=chatgpt.com)

That will let wiki3.ai support:

Obsidian-native editing,

skill-spec compatibility,

executable kernels,

and round-tripping between `.md` and `.ipynb`.

I can turn this into a concrete mini-spec next: exact frontmatter fields, notebook metadata layout, and the conversion algorithm for `SKILL.md` ⇄ `.ipynb`.

![](https://www.google.com/s2/favicons?domain=https://jupytext.readthedocs.io&sz=32)

![](https://www.google.com/s2/favicons?domain=https://papermill.readthedocs.io&sz=32)

Sources

 

#### You said:

Well, I don't mean pairing so much as alternative representations with roundrrippable conversions.

 

#### ChatGPT said:

I’m tightening the model around a single canonical document with two lossless views, rather than “two files that travel together.” The key is deciding which semantics survive every conversion unchanged and which are only execution/runtime adornments.

Thought for 7s

Yes — that changes the architecture.

You do **not** want “a Markdown file plus a notebook file that stay paired.”
You want **one logical document type** with **two alternative serializations**:

an **Obsidian-native Markdown serialization**

a **Jupyter notebook serialization**

and conversions between them should be **lossless for the shared model**.

That is a much better framing.

## The right abstraction

Think in terms of a **canonical semantic model**, not a canonical file.

Something like:

document metadata

body blocks

executable cells

template markers

skill/subtask role

parameter schema

runtime bindings

notebook-only execution state

Then:

`.md` is one projection of that model

`.ipynb` is another projection of that model

So the question becomes:

**Which semantics are part of the shared document model, and which are view-specific?**

## What should be in the shared model

These should round-trip between `.md` and `.ipynb` unchanged:

Obsidian-style frontmatter properties, since Obsidian stores properties as YAML frontmatter at the top of the file. [Obsidian](https://obsidian.md/help/properties?utm_source=chatgpt.com)

Template source text, because Obsidian Templates is fundamentally text insertion with variables like `{{title}}`, `{{date}}`, and `{{time}}`, not notebook execution logic. [Obsidian](https://obsidian.md/help/properties?utm_source=chatgpt.com)

Skill/spec body text from `SKILL.md`

Parameter *definitions* for skills/subtasks

Code cells as executable blocks

Cell ordering

Links, tags, aliases, and other Obsidian-visible note semantics

In other words, the shared model is “note + metadata + executable regions + template/spec semantics.”

## What should be view-specific

These should **not** be treated as core shared semantics:

notebook outputs

transient execution counts

kernel session state

Papermill’s injected override cell, because Papermill explicitly inserts an `injected-parameters` cell after the `parameters` cell at execution time. That is runtime machinery, not author intent. [Papermill+1](https://papermill.readthedocs.io/en/latest/usage-parameterize.html?utm_source=chatgpt.com)

So your conversion should preserve the author’s parameter declaration, but probably strip or normalize transient injected execution artifacts unless you intentionally want execution history in the shared model.

## Consequence for templates and skills

This means:

**Obsidian templates** are part of the shared model as literal source text plus metadata.

**Papermill parameters** are also part of the shared model, but as a **parameter block abstraction**, not specifically as “this exact injected notebook cell.”

That is the key difference.

A template is “how to instantiate a document.” 

A parameter block is “what values can be supplied to execute this document.”

They overlap, but they are not the same thing.

## Best file strategy

For your goal, I would define:

### Markdown serialization

Use **plain Markdown with top-level YAML frontmatter** so it stays maximally compatible with Obsidian. Obsidian properties are stored that way already. [Obsidian](https://obsidian.md/help/properties?utm_source=chatgpt.com)

Then represent executable content using notebook-style fenced blocks.

Jupytext is the closest existing precedent here: its Markdown notebook format starts with an optional YAML header and represents notebooks in Markdown form. [Jupytext](https://jupytext.readthedocs.io/en/latest/formats-markdown.html?utm_source=chatgpt.com)

### Notebook serialization

Use standard `.ipynb` JSON with:

notebook metadata for document-level fields

markdown cells for prose/spec/template content

code cells for executable sections

cell tags or metadata for semantic roles like:

`parameters`

`template`

`skill`

`subtask`

Papermill already uses the `parameters` tag convention for the execution-facing side. [Papermill+1](https://papermill.readthedocs.io/en/latest/usage-parameterize.html?utm_source=chatgpt.com)

## The most important design rule

Do **not** make either Obsidian frontmatter syntax or Papermill cell injection syntax the canonical meaning.

Instead define a shared internal concept like:

`document.properties`

`document.template_source`

`document.parameter_schema`

`document.blocks[]`

Then map it both ways.

That avoids subtle corruption from tool-specific behavior.

For example, Obsidian’s own frontmatter handling has known formatting/normalization issues when programmatically rewritten, so preserving source intent matters if exact round-trip fidelity is a goal. [Obsidian Forum](https://forum.obsidian.md/t/yaml-properties-api-processfrontmatter-removes-alters-string-quotes-comments-types-formatting/65851?utm_source=chatgpt.com)

## Concrete recommendation

I would model one wiki3 document like this conceptually:

Document 
 metadata 
 kind: note | template | skill | subtask 
 properties 
 template_variables 
 parameters 
 blocks: 
 - markdown 
 - code 
 - raw

Then serialize it as:

### `.md`

YAML frontmatter for `properties` and top-level role fields

Markdown body for prose/spec/template content

fenced executable blocks for code cells

optional comments/directives for cell metadata

### `.ipynb`

notebook metadata for the same top-level properties

markdown/code/raw cells for the same blocks

tags/metadata on cells for roles

optional `parameters` tag on the parameter-definition cell

## How this helps with SKILL.md

This is exactly the right fit for `SKILL.md`.

In Markdown view:

it looks like a normal skill spec with frontmatter and readable instructions

In notebook view:

the same document becomes a notebook with:

a markdown introduction/spec

a parameter-definition cell

executable implementation cells

the correct kernel selected in metadata

So `SKILL.md` is not “paired with” a notebook. 

It **is** a document that can be rendered as either Markdown or notebook JSON.

## Compatibility with Obsidian

To stay Obsidian-compatible, your Markdown serialization should preserve:

top-level YAML frontmatter

`tags`, `aliases`, and `cssclasses` as ordinary Obsidian property names

literal template expressions

ordinary wiki links and Markdown content

Because Obsidian treats properties as YAML frontmatter and has built-in semantics for certain property names like `tags`, `aliases`, and `cssclasses`. [Obsidian](https://obsidian.md/help/properties?utm_source=chatgpt.com)

That means the Markdown representation should look like a real Obsidian note first, and a notebook encoding second.

## Compatibility with Jupyter

To stay Jupyter-compatible, your notebook serialization should preserve:

valid nbformat metadata

markdown/code/raw cell structure

kernel metadata

Papermill-compatible parameter tagging where applicable

Jupyter notebook metadata is designed to be extensible, and Jupytext already proves that Markdown can carry notebook metadata in a YAML header. [Jupytext](https://jupytext.readthedocs.io/en/latest/formats-markdown.html?utm_source=chatgpt.com)

## The main trap to avoid

Do not let the notebook view introduce semantics that cannot be represented back in Obsidian Markdown without distortion.

Examples:

injected runtime parameter cells

output-heavy execution artifacts

raw publishing-specific constructs that only Quarto/MyST understand

Those can exist as **derived or optional** notebook-specific artifacts, but they should not be required for the logical document.

## My recommendation in one sentence

Define **wiki3 documents as a tool-neutral semantic model with two round-trippable serializations**—Obsidian-flavored Markdown and Jupyter `.ipynb`—and treat templates, skills, and parameters as first-class document semantics rather than as file-pair conventions.

The next step is to write the conversion contract:

exact frontmatter fields

exact markdown encoding for code/parameter blocks

exact notebook metadata layout

which fields are guaranteed lossless

which notebook artifacts are intentionally dropped or normalized on export

![](https://www.google.com/s2/favicons?domain=https://jupytext.readthedocs.io&sz=32)

![](https://www.google.com/s2/favicons?domain=https://papermill.readthedocs.io&sz=32)

![](https://www.google.com/s2/favicons?domain=https://obsidian.md&sz=32)

Sources

 

#### You said:

There's a spec for these skill .md files. We should support all of its features.

 

#### ChatGPT said:

I’m pulling the actual skill-file spec so I can map its full feature set into a round-trippable `.md` ⇄ `.ipynb` model instead of hand-waving the details.

Thought for 17s

Agreed. If wiki3.ai says it supports `SKILL.md`, it should support the **full spec surface** and the **real-world extensions people actually use**, not just `name` + `description`.

The current Agent Skills spec defines a skill directory with a required `SKILL.md`, plus optional `scripts/`, `references/`, `assets/`, and any additional files or directories. `SKILL.md` itself is YAML frontmatter followed by unrestricted Markdown body. The spec-defined frontmatter fields are `name` and `description` as required, with optional `license`, `compatibility`, `metadata`, and experimental `allowed-tools`. It also constrains `name` and `description`, and says the body has no format restrictions. [GitHub+3GitHub+3GitHub+3](https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx)

That means the wiki3 document model should explicitly preserve at least these **shared semantics**:

skill directory structure

full YAML frontmatter

unrestricted Markdown body

optional supporting files under `scripts/`, `references/`, `assets/`

extra nonstandard files/directories without dropping them [GitHub+1](https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx)

The important design consequence is this:

**You cannot model `SKILL.md` as “just Obsidian properties.”**

Obsidian properties are useful for many top-level fields, but the skill spec includes:

unrestricted Markdown instructions,

optional executable code in `scripts/`,

optional reference docs,

optional assets/templates,

and implementation-specific metadata/extensions. [GitHub+1](https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx)

So the round-trippable unit needs to be a **skill package document**, not merely a note.

## What to support exactly

For spec compliance, wiki3.ai should preserve these fields exactly as data, not normalize them away:

YAML

name: 
description: 
license: 
compatibility: 
metadata: 
allowed-tools:

because those are the spec-defined frontmatter fields. `allowed-tools` is experimental, so support may vary across agents, but if you round-trip skills you should still preserve it exactly. [GitHub+1](https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx)

It should also preserve the `name` constraints in validation logic:

1–64 chars

lowercase alphanumeric + hyphens

no leading/trailing hyphen

no consecutive hyphens

matches parent directory name [GitHub](https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx)

And it should preserve the intended role of the Markdown body as open-ended instructions, examples, and edge cases rather than trying to parse it into a rigid schema. [GitHub](https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx)

## Why “full spec support” is not enough by itself

There is a second requirement: **real Hermes compatibility**.

The formal Agent Skills spec describes `metadata` as an optional map for additional properties, with string keys and string values. [GitHub](https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx)
But current Hermes materials and examples show richer nested use under `metadata.hermes`, including things like recommended model/provider configuration, and existing Hermes skills visibly carry extra frontmatter beyond the base spec, such as `version`, `author`, and nested Hermes-specific metadata. [GitHub+2GitHub+2](https://github.com/NousResearch/hermes-agent/issues/5997)

So if you want wiki3.ai to be compatible with both the **spec** and the **Hermes ecosystem**, the safest rule is:

**Preserve arbitrary YAML frontmatter losslessly, even for fields or nesting that are outside the strict base spec.**

That avoids breaking:

`metadata.hermes.*`

extra top-level fields like `version` or `author`

future extensions

implementation-specific conventions in other skill runtimes [GitHub+2GitHub+2](https://github.com/NousResearch/hermes-agent/issues/5997)

## What that means for `.md` ⇄ `.ipynb`

For the alternative-representation model, I’d define the shared object as:

`skill_manifest` = full frontmatter, lossless

`skill_body` = Markdown body, lossless

`supporting_files` = path-keyed resources, lossless

`execution_blocks` = optional code-bearing blocks

`notebook_runtime` = notebook-only execution artifacts, noncanonical

Then:

### Markdown representation

The `.md` view should be a real `SKILL.md`:

top-level YAML frontmatter

original Markdown body

no forced notebook syntax unless needed for executable regions

### Notebook representation

The `.ipynb` view should map:

frontmatter → notebook metadata namespace, losslessly

Markdown body → markdown cells

executable content / scripts / subtasks → code cells or attached file references

selected parameter definitions → Papermill-compatible parameter cell where appropriate

The critical point is that the **notebook view must not flatten or reinterpret the skill manifest**. It should carry the full original frontmatter as structured data.

## How to handle scripts, references, and assets

The spec explicitly allows:

`scripts/` for executable code,

`references/` for docs loaded on demand,

`assets/` for templates, images, data files. [GitHub](https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx)

That argues for representing a skill as a **compound document/package**, not just a single notebook file.

So even if `.md` and `.ipynb` are alternative representations of the main skill document, the overall skill still needs a package/container model around them:

skill/ 
 SKILL.md or skill.ipynb 
 scripts/ 
 references/ 
 assets/ 
 ...

In other words:

the **main skill file** can round-trip between Markdown and notebook forms,

but the **skill package** also includes supporting files that must survive untouched. [GitHub+1](https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx)

## Best compatibility rule

I’d make this a hard rule:

**Round-tripping must preserve the exact YAML frontmatter content and the exact Markdown body unless the user explicitly edits semantics.**

That is especially important because Obsidian users may care about literal frontmatter layout and template text, while Hermes-style skills may rely on implementation-specific metadata that is not part of the base spec. The safe path is lossless preservation first, interpretation second. [GitHub+2GitHub+2](https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx)

## Practical conclusion

Yes — wiki3.ai should support **all features of the `SKILL.md` spec**.

Concretely, that means:

full required and optional frontmatter support,

unrestricted Markdown body,

optional `scripts/`, `references/`, `assets/`,

preservation of extra files,

preservation of experimental `allowed-tools`,

and lossless handling of real-world extensions like Hermes-specific nested metadata. [GitHub+3GitHub+3GitHub+3](https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx)

The architectural implication is that wiki3.ai needs a **lossless skill package model with two main-file serializations** (`SKILL.md` and `.ipynb`), not just a note model and not just a paired-file trick.

The next sensible step is to write a **normative conversion spec** with:

exact mapping of frontmatter to notebook metadata,

exact preservation rules for unknown YAML fields,

exact encoding of parameter cells,

and exact treatment of `scripts/`, `references/`, and `assets/`.

Sources

 

#### You said:

Anything else to add from Skills Hub ? Do skills .md files use fenced code blocks? How?
https://agentskills.io/home

 

#### ChatGPT said:

I’m checking Skills Hub’s current docs/examples and the spec language around code blocks so I can separate what the formal spec requires from what the ecosystem commonly does.

Thought for 21s

Yes. A few things from Skills Hub are worth adding to wiki3.ai beyond the bare `SKILL.md` spec:

The biggest one is **progressive disclosure** as a first-class loading model: clients should load only `name` + `description` at startup, then the full `SKILL.md` body when a skill is activated, and only load `scripts/`, `references/`, and `assets/` when the instructions actually point to them. Skills Hub presents that as the core client integration pattern. [Agent Skills+1](https://agentskills.io/client-implementation/adding-skills-support)

A second one is **discovery conventions**. Skills Hub recommends scanning both client-specific locations and the cross-client `.agents/skills/` convention at project and user scope, with `.claude/skills/` sometimes scanned for pragmatic compatibility. That matters if you want wiki3.ai skills to interoperate with the broader ecosystem. [Agent Skills](https://agentskills.io/client-implementation/adding-skills-support)

A third one is **size/shape guidance**, not just syntax. Skills Hub recommends keeping the activated `SKILL.md` body under about **5,000 tokens / 500 lines** and pushing bulky material into references or other resource files. That is not just style guidance; it affects how a client should package, load, and convert content. [Agent Skills+2Agent Skills+2](https://agentskills.io/skill-creation/best-practices?utm_source=chatgpt.com)

A fourth one is **script ergonomics**. Skills Hub explicitly encourages one-off commands directly in `SKILL.md`, reusable code in `scripts/`, relative paths from the skill root, self-contained scripts when possible, non-interactive interfaces, `--help`, helpful errors, and structured output. That is useful for your notebook conversion design because it tells you which executable patterns are common and should map cleanly into parameterized notebook cells or notebook-backed tools. [Agent Skills](https://agentskills.io/skill-creation/using-scripts)

On your code-block question: **yes, `SKILL.md` files absolutely use fenced code blocks**. The spec says the Markdown body has **no format restrictions**, so fenced blocks are allowed as ordinary Markdown, and the official docs show them being used for shell commands and code examples. [Agent Skills+1](https://agentskills.io/specification?utm_source=chatgpt.com)

But the important nuance is **how** they are used: in the spec, fenced code blocks are primarily **instructional Markdown content**, not a separate formal syntax layer. For example, the official “Using scripts” guide shows bash fences inside the workflow instructions to tell the agent what to run, and it also uses indented/fenced examples for one-off commands. [Agent Skills](https://agentskills.io/skill-creation/using-scripts)

So I would model fenced blocks like this:

**Spec-level meaning:** just Markdown body content. The spec does not assign special schema semantics to fenced blocks beyond normal Markdown. [Agent Skills](https://agentskills.io/specification?utm_source=chatgpt.com)

**Ecosystem-level meaning:** often they contain runnable commands, examples, JSON schemas, or snippets the agent may copy, execute, or adapt. The official scripts guide demonstrates command blocks in workflow steps, and validator tooling even checks for unclosed fences because broken fences can make skills unusable for agents. [Agent Skills+1](https://agentskills.io/skill-creation/using-scripts)

For wiki3.ai, that suggests a good rule:

Preserve fenced blocks **verbatim** in the Markdown representation for full compatibility.

In the notebook representation, map fenced blocks either to:

**Markdown cells** when they are explanatory examples, or

**code cells with metadata/tags** when they are declared executable blocks you want the notebook runtime to understand.

I would **not** assume every fenced block becomes executable code. Skills Hub examples include code fences as instructions, not necessarily as “run this automatically.” [Agent Skills+1](https://agentskills.io/skill-creation/using-scripts)

One more thing worth adding from the ecosystem, even though it is not the normative spec itself: validator tooling flags **unclosed fences**, warns on **unknown frontmatter fields**, checks **orphan resources**, and treats mention of relative paths anywhere in reachable text—including inline code and code blocks—as a reference signal. That is useful for designing round-trip conversion and validation in wiki3.ai. [GitHub](https://github.com/agent-ecosystem/skill-validator)

So my net recommendation is:

Support the official spec fully, but also adopt these Skills Hub conventions:

progressive disclosure

`.agents/skills/` discovery

small activated `SKILL.md`, larger details in referenced files

relative-path resource references

fenced blocks preserved literally

optional interpretation of some fenced blocks as executable notebook cells when the block is explicitly marked/typed for execution

And for round-tripping, treat fenced code blocks as **lossless content first, executable structure second**.

I can draft a concrete conversion table next, like “Markdown fence language/tag → notebook cell type + metadata + execution policy.”

![](https://www.google.com/s2/favicons?domain=https://agentskills.io&sz=32)

Sources

 

#### You said:

We want to take agent skills to the next stage by ingesting them into a KG and using an "autoformalization" style of input processing so that skill execution is triggered by KG logical inference, not directly by LLM agent ReAct. This is a key step in most trustworthy/reliable AI because the context can now include conditions/properties that are always correctly applied.

 

#### ChatGPT said:

I’m grounding this in current references on agent skills, knowledge graphs, and “autoformalization” so I can give you a concrete architecture instead of just agreeing with the direction.

Thought for 15s

Yes — I think that is a major step up.

What you are proposing is to move from:

**LLM chooses tools directly from text at runtime**

to:

**LLM helps formalize inputs and maintain the knowledge graph, while skill triggering is decided by an explicit inference layer**

That is exactly the kind of separation that tends to improve reliability, because the “when does this skill apply?” decision is no longer buried inside a transient ReAct trace. The autoformalization literature increasingly frames the core task as translating informal language into a target language that supports logical inference and automated reasoning, not just into executable code. [arXiv+1](https://arxiv.org/pdf/2509.09810?utm_source=chatgpt.com)

For Skills Hub specifically, this also fits the ecosystem well because `SKILL.md` already has a structured manifest plus free-form instructions, and clients are expected to do structured discovery and progressive loading rather than blindly dump everything into the prompt. [Agent Skills](https://agentskills.io/home?utm_source=chatgpt.com)

## What changes architecturally

I would make skill execution a **compiled policy problem**, not an agent prompting problem.

A good pipeline is:

**Ingest skill packages**

Parse full `SKILL.md` frontmatter and body.

Preserve scripts, references, assets, and extra files.

Extract explicit applicability conditions, inputs, outputs, constraints, and side effects.

**Autoformalize into a logic-ready representation**

Convert informal text like “use when the user asks to summarize a CSV” into structured predicates, types, and rules.

Keep provenance back to the exact lines/spans of the original skill text.

**Store in a KG plus rule layer**

KG for entities, relationships, capabilities, data types, tools, dependencies, and resource links.

Rule layer for applicability, preconditions, exclusions, permission checks, and priority.

**At runtime, infer applicable skills**

User request and environment state are autoformalized into facts.

Logical inference proposes which skills are applicable, blocked, or preferred.

The LLM can still help with ambiguous parsing or downstream execution, but not as the sole arbiter of skill selection.

That separation is aligned with broader neuro-symbolic work: combine natural-language understanding with graph or formal reasoning so that retrieval and action selection are constrained by explicit structure rather than only free-form chain-of-thought. [arXiv+1](https://arxiv.org/abs/2310.11220?utm_source=chatgpt.com)

## Why this is better than direct ReAct

The main advantages are:

**Stable policy application.**
Conditions like “only use this skill if the file is a CSV,” “never call this skill without a path,” or “prefer the notebook-backed version when Python is available” can be represented as rules and applied consistently. That consistency is exactly what you were pointing at with “conditions/properties that are always correctly applied.” Autoformalization work outside theorem proving now explicitly includes translation into languages for knowledge representation, planning, and logical inference. [arXiv+1](https://arxiv.org/pdf/2509.09810?utm_source=chatgpt.com)
**Auditability.**
You can explain: “Skill X fired because predicates A, B, and C held, and exception E did not.” That is much easier to inspect than “the model thought this seemed right.”
**Compositional subtasks.**
Once skills and subtasks are graph nodes with typed inputs/outputs and rule guards, you can infer multi-step plans symbolically.
**Safer defaults.**
You can encode hard constraints outside the model, such as required approvals, prohibited tools, or environment restrictions.

## The right representation

I would not use a plain RDF-only KG by itself, because a KG without a rule layer usually cannot express enough operational policy.

Use three layers:

### 1. Skill graph

Facts like:

`Skill(summarize_csv)`

`AcceptsType(summarize_csv, csv_file)`

`Produces(summarize_csv, summary_report)`

`UsesKernel(summarize_csv, python3)`

`HasAsset(summarize_csv, "templates/report.md")`

### 2. Rule layer

Rules like:

applicable if request asks for summarization and resource type is CSV

blocked if no readable file path is available

prefer notebook execution when kernel is available

avoid if a stronger domain-specific skill matches

### 3. Provenance layer

Every fact/rule points back to:

source file

frontmatter key

markdown span

script path

confidence

whether it was human-authored or autoformalized

Without provenance, autoformalization becomes hard to trust.

## How to ingest `SKILL.md`

For each skill, extract at least:

identity: `name`, `description`

compatibility/tool constraints

declared metadata and custom fields

mentioned scripts, references, assets

explicit imperative instructions

examples

fenced code blocks

relative file references

exception language like “unless,” “only if,” “do not,” “prefer”

Then normalize these into:

**facts**

**candidate rules**

**open questions / ambiguities**

The last category matters. A lot of skills will not be formal enough to compile cleanly in one pass.

## Where the notebook model fits

Your notebook idea becomes stronger in this architecture.

A notebook-backed skill can be represented as:

a **declarative skill spec**

plus an **executable implementation**

plus a **parameter schema**

Then the inference layer decides that the skill is applicable, and the execution layer instantiates the notebook with the inferred parameters.

That is a much better use of parameterized notebooks than letting the LLM decide ad hoc whether to use them.

## What “autoformalization” should mean here

Not “convert Markdown into one giant formal object.”

Instead, do a staged compilation:

### Stage A: structural extraction

Pull out obvious machine-readable pieces:

YAML/frontmatter

headings

lists

code fences

file references

scripts

parameter definitions

### Stage B: controlled semantic extraction

Translate natural-language instructions into candidate predicates and rules, for example:

“Use this skill when the user wants a quick profile of a CSV file.”

becomes roughly:

`Intent(user_request, summarize_dataset)`

`HasInputType(context, csv_file)`

`Applicable(summarize_csv_skill)`

### Stage C: verification / repair

Check:

are referenced predicates in the ontology?

are required inputs satisfiable?

do two rules conflict?

is there an exception path?

### Stage D: human-reviewable formal artifact

Store both:

the formal rule

the exact source text that produced it

That is closer to trustworthy autoformalization than a one-shot LLM parse.

## Critical cautions

This approach is strong, but there are real traps.

### Open-world vs closed-world assumptions

A KG often behaves as if missing facts are just unknown. Operational policies often need closed-world behavior: “if permission is not present, deny.” You need to choose this explicitly.

### Defaults and exceptions

Skills often say things like “usually,” “prefer,” “if possible,” or “unless the user asked otherwise.” Those are not plain hard logic. You will want:

hard constraints

soft preferences

defeasible rules

A defeasible-rule framework is often more realistic than pure monotonic logic for agent policies. Recent work on defeasible reasoning emphasizes explicit handling of exceptions and conflicting rules, which maps well to skill selection. [arXiv](https://arxiv.org/html/2603.15317v1?utm_source=chatgpt.com)

### Ambiguous natural language

Many skills will under-specify applicability. Autoformalization should produce:

formal rule candidates

confidence

unresolved ambiguities 

not pretend certainty where there is none.

### Rule explosion

If every sentence becomes a rule, the system becomes brittle. You need a controlled ontology and compilation target.

## My recommended execution stack

I would split runtime into four components:

**1. Parser/Compiler**
Turns `SKILL.md` and related resources into a typed intermediate representation.
**2. Graph + rule engine**
Stores capabilities, dependencies, applicability, constraints, and preferences.
**3. World-state extractor**
Autoformalizes the current request/context into facts:

user intent

available files

environment capabilities

permissions

current subtask state

**4. Executor**
Runs the chosen implementation:

notebook

script

direct tool

subworkflow

The LLM still matters in two places:

helping produce candidate formalizations

helping inside execution for underspecified tasks

But it stops being the final policy engine for skill triggering.

## A concrete example

Suppose a skill says:

“Use when the user asks to summarize a CSV.”

“Requires a readable CSV path.”

“Prefer Python notebook execution.”

“Do not use for SQL databases.”

That can compile into something like:

`intent = summarize_table`

`input_type = csv_file`

`requires(readable_path)`

`prefers(runtime = python_notebook)`

`excludes(input_type = sql_database)`

Then if the runtime facts are:

request asks for summary

attached file is `.csv`

Python kernel available

the rule engine selects the skill before any ReAct-style tool choice happens.

## Bottom line

I think this is exactly the right direction for wiki3.ai.

The strongest version is:

**treat skills as compilable policy-bearing artifacts**

**autoformalize them into KG facts plus explicit rules**

**infer applicability symbolically**

**let the LLM assist with interpretation and execution, but not own the trigger decision**

That gives you better consistency, better auditability, and a much clearer path to trustworthy behavior than direct skill selection inside an unconstrained agent loop. [arXiv+2arXiv+2](https://arxiv.org/pdf/2509.09810?utm_source=chatgpt.com)

The next thing to write is a **formal intermediate representation** for skills: entities, predicates, rule types, confidence/provenance fields, and how notebook parameters map into inferred executable plans.

![](https://www.google.com/s2/favicons?domain=https://agentskills.io&sz=32)

![](https://www.google.com/s2/favicons?domain=https://arxiv.org&sz=32)

Sources

 

#### You said:

Our primary formal tool is ACL2 but it is too resource intensive to require in every (or even most) use cases. Z3 has multiple deployment options. There are also Semantic Web inference tools that have implementations using it. Do you have any other recommendations?

 

#### ChatGPT said:

I’m comparing a few practical options by role — lightweight SMT, Datalog/rule engines, Semantic Web reasoners, and proof-oriented systems — so I can recommend a stack that complements ACL2 instead of trying to replace it wholesale.

Thought for 24s

Yes. Given your architecture, I would not look for one replacement for ACL2. I would use a **tiered stack**:

**ACL2** for the small fraction of logic that really needs deep proof and high assurance.

**SMT** for fast satisfiability, typing, consistency, guards, arithmetic, and small symbolic checks.

**Datalog / rule engines** for skill triggering, KG inference, and policy application.

**Semantic Web tooling** where RDF/OWL/SHACL interoperability matters.

That split matches the strengths of the tools much better than trying to make ACL2 handle routine runtime inference. SMT solvers are designed as verification backends, while SHACL, OWL-profile reasoners, and Datalog systems are better suited to operational graph inference. [Soufflé+3SMT-COMP+3Apache Jena+3](https://smt-comp.github.io/2026/introduction/?utm_source=chatgpt.com)

My strongest recommendations are these.

**1) cvc5 as the second SMT backend, alongside Z3.**
cvc5 is a current open-source SMT solver with SMT-LIB support and broad theory support, and it gives you useful diversity from Z3 instead of betting everything on one solver. For your use case, that matters for cross-checking, portability, and avoiding solver-specific assumptions. [cvc5+2cvc5+2](https://cvc5.github.io/?utm_source=chatgpt.com)
**2) pySMT as the orchestration layer above Z3/cvc5.**
pySMT gives you a solver-agnostic API, can target multiple SMT solvers, and supports portfolio solving. That is a very practical way to keep wiki3.ai’s formal layer modular while letting different deployments use different backends. [pySMT+2GitHub+2](https://pysmt.readthedocs.io/?utm_source=chatgpt.com)
**3) Soufflé or clingo for rule-heavy skill triggering.**
If your core question is “which skill fires under which conditions?”, I would seriously consider a Datalog-family engine instead of pushing that logic into SMT. Soufflé is a typed Datalog system with a component model and was built for large logic-heavy analyses. Clingo gives you Answer Set Programming, which is especially attractive if you need defaults, exceptions, and alternative plans rather than only monotonic entailment. [Potassco+3Soufflé+3Soufflé+3](https://souffle-lang.github.io/docs.html?utm_source=chatgpt.com)

For your particular “trustworthy skill triggering” idea, the choice is usually:

**Soufflé** if you want scalable, explicit, mostly monotonic rule evaluation.

**clingo** if you want nonmonotonic reasoning, defaults, priorities, and exception handling.

**4) SHACL rules for lightweight KG inference and validation.**
This is one of the best fits for your “conditions/properties that are always correctly applied” goal. SHACL is not just validation anymore; SHACL 1.2 Rules explicitly defines declarative inference rules for deriving RDF triples, and there are implementations in TopBraid SHACL API and pySHACL. This gives you a nice middle ground between “full theorem proving” and “just prompt the model.” [W3C GitHub+3W3C+3GitHub+3](https://www.w3.org/TR/shacl12-rules/?utm_source=chatgpt.com)

If you already expect RDF-like skill metadata and KG facts, SHACL is a very natural deployment-friendly layer for:

applicability checks

preconditions

constraint validation

small local inferences

**5) Apache Jena as the open Semantic Web baseline.**
Jena gives you a solid open-source stack for RDF models, inference APIs, and RDFS/OWL rule-based reasoning. I would view it as the default interoperability layer if you want standards-based RDF plumbing without committing to a heavier commercial engine. [Apache Jena+2Apache Jena+2](https://jena.apache.org/documentation/inference/?utm_source=chatgpt.com)
**6) RDFox if you want high-performance materialized reasoning.**
RDFox is much stronger when you need Datalog-style rules over RDF at speed, incremental updates, and serious graph reasoning performance. It is a good fit when the graph is central and you want the inference engine itself to be a first-class runtime component. [RDFox Documentation+2Oxford Semantic Technologies+2](https://docs.oxfordsemantic.tech/reasoning.html?utm_source=chatgpt.com)
**7) ELK if your ontologies fit OWL 2 EL.**
If you want ontology classification and lightweight tractable reasoning, ELK is worth a look. OWL 2 EL exists exactly for scalable reasoning, and ELK is specialized for that profile. [Live Ontologies+2GitHub+2](https://liveontologies.github.io/elk-reasoner/?utm_source=chatgpt.com)

A few more targeted recommendations:

**Why3** is useful if you want an intermediate verification platform that can dispatch proof obligations to external provers. I would not use it as the runtime inference layer for skill triggering, but it is attractive for proving parts of your compiler or formalization pipeline and farming obligations out to multiple provers. [Why3+2Why3+2](https://why3.org/?utm_source=chatgpt.com)

**Ontop** is worth considering if a lot of your KG should stay virtual over relational data instead of being copied into RDF storage. It exposes relational data as a virtual knowledge graph and is built around SPARQL-to-SQL rewriting. That can simplify deployments that already have structured stores underneath. [Ontop+2W3C+2](https://ontop-vkg.org/guide/?utm_source=chatgpt.com)

**egglog** is interesting if equality reasoning and rewrite saturation become central, especially for canonicalizing autoformalized expressions before feeding them into downstream provers. I would treat it as an advanced adjunct, not a first recommendation. [GitHub+2PLDI 2022+2](https://github.com/egraphs-good/egglog?utm_source=chatgpt.com)

My practical stack recommendation for wiki3.ai would be:

**Primary runtime inference:** Soufflé or SHACL rules

**Constraint/discharge layer:** Z3 + cvc5 via pySMT

**High-assurance proofs:** ACL2

**RDF interoperability:** Jena

**Performance-upgrade path:** RDFox

**Ontology classification when needed:** ELK

In plain terms:

Use **Datalog/SHACL** to decide *when a skill is applicable*.

Use **SMT** to check *whether the conditions are internally consistent and satisfiable*.

Use **ACL2** only for the small kernel of logic you truly need to verify deeply.

That architecture keeps the expensive proof work small while still making the runtime behavior explicit and checkable. [Apache Jena+3Soufflé+3W3C+3](https://souffle-lang.github.io/docs.html?utm_source=chatgpt.com)

If you want one concrete “start here” combination, I’d start with:

**Soufflé + pySMT + Z3/cvc5 + pySHACL/Jena + ACL2 for the trusted kernel.**

That is the best balance I see between deployability, logical transparency, and performance.

![](https://www.google.com/s2/favicons?domain=https://pysmt.readthedocs.io&sz=32)

![](https://www.google.com/s2/favicons?domain=https://cvc5.github.io&sz=32)

![](https://www.google.com/s2/favicons?domain=https://smt-comp.github.io&sz=32)

Sources

 

#### You said:

What about for JS/TS/WASM environments?

 

#### ChatGPT said:

I’m checking which of these actually have maintained JS/TS or WASM deployment options today, so I can recommend what is realistic in-browser versus Node/server-side.

Thought for 13s

For **JS/TS/WASM**, I’d use a different emphasis than for Python/Java.

My top picks are:

**Z3 via `z3-solver`** for SMT in Node/browser/WASM

**N3.js** for lightweight RDF/N3 rule reasoning in JS

**`rdf-validate-shacl`** for SHACL validation in pure JS

**Comunica** for SPARQL/query-time KG access, with optional reasoning packages

**clingo-wasm** only if you specifically want ASP-style defaults/exceptions in-browser

## Best practical stack

### 1) SMT: Z3 is the easiest choice in JS/TS

Z3 has official JavaScript/TypeScript bindings and a WebAssembly build published as **`z3-solver`** on npm, so it is the most straightforward solver for browser, Node, and edge-style environments. [GitHub+2npm+2](https://github.com/z3prover/z3?utm_source=chatgpt.com)

That makes it my default recommendation for:

satisfiability checks

constraint solving

guard checking

small symbolic consistency checks

### 2) cvc5 is viable, but less turnkey in JS

cvc5 supports **WebAssembly compilation**, so it is a real option for JS/WASM deployments. But based on the current docs, it is more of a build/deployment path than a polished npm-first JS experience. [cvc5](https://cvc5.github.io/docs/cvc5-1.0.8/installation/installation.html?utm_source=chatgpt.com)

So I would treat cvc5 as:

a good secondary backend

useful when you want solver diversity

not the first choice for simple TS/browser deployment

## Semantic Web / KG side

### 3) N3.js is a strong fit for browser-native inference

N3.js supports reasoning directly in JS with a `Reasoner`, and recent work on the N3.js reasoner reports browser performance that is good enough for standard use cases. [GitHub+1](https://github.com/rdfjs/N3.js/?utm_source=chatgpt.com)

This is a very good fit for:

local graph inference

Horn-rule-style skill applicability

client-side reasoning over modest graphs

### 4) `rdf-validate-shacl` is the best JS-native validation layer

`rdf-validate-shacl` is a **pure JavaScript** SHACL implementation built on RDF/JS. That makes it a strong choice for enforcing skill/package constraints and KG shape checks in Node or the browser. [npm+1](https://www.npmjs.com/package/rdf-validate-shacl?utm_source=chatgpt.com)

I’d use it for:

validating autoformalized facts

checking that skill manifests satisfy required shapes

enforcing preconditions before execution

### 5) Comunica is the right JS query layer

Comunica is a JavaScript framework for querying knowledge graphs, and it also has packages for **reasoning during query execution**. It is especially attractive if you want SPARQL/GraphQL-style access in a JS stack. [GitHub+2GitHub+2](https://github.com/comunica/comunica?utm_source=chatgpt.com)

I’d use it for:

querying RDF stores or distributed sources

retrieval over your KG

integrating reasoning with query execution

## If you want defaults and exceptions

### 6) clingo-wasm is interesting for nonmonotonic policies

If your skill-triggering logic needs things like:

defaults

priorities

exceptions

choosing among alternatives

then **ASP** is often more natural than SMT or plain RDF rules. There is a WebAssembly build of clingo available for the web. [GitHub](https://github.com/domoritz/clingo-wasm?utm_source=chatgpt.com)

I would only pick this if you really need defeasible/nonmonotonic behavior, because it adds complexity.

## What I would not center on in JS/WASM

### Apache Jena

Jena is excellent, but it is a **Java** framework, not a JS-native one. So I would not make it the core of a browser/TS deployment. [Apache Jena](https://jena.apache.org/?utm_source=chatgpt.com)

## Recommended combinations by use case

For a **browser-first** stack:

`z3-solver`

N3.js

`rdf-validate-shacl`

Comunica

For a **Node/TS backend**:

`z3-solver`

optional cvc5 WASM backend

Comunica

`rdf-validate-shacl`

maybe clingo-wasm for policy-heavy triggering

For an **edge/WASM** deployment:

`z3-solver` first

N3.js for local rules

`rdf-validate-shacl` for validation

avoid heavier JVM-centric tooling

## My bottom-line recommendation

If wiki3.ai is targeting **JS/TS/WASM**, I’d start with:

**`z3-solver` + N3.js + `rdf-validate-shacl` + Comunica**

That gives you:

SMT constraints

local rule inference

standards-based RDF validation

queryable KG integration

Then add **clingo-wasm** only if your skill-triggering rules need real defaults/exceptions, and add **cvc5 WASM** only if you want a second SMT backend for cross-checking. [cvc5+5GitHub+5GitHub+5](https://github.com/z3prover/z3?utm_source=chatgpt.com)

A useful architecture here is:

**SHACL/N3** to decide applicability

**Z3** to check constraints

**Comunica** to query the KG

**ACL2** reserved for a much smaller trusted kernel outside the hot path

![](https://www.google.com/s2/favicons?domain=https://www.npmjs.com&sz=32)

![](https://www.google.com/s2/favicons?domain=https://cvc5.github.io&sz=32)

Sources

Thinking

ChatGPT can make mistakes. Check important info.
