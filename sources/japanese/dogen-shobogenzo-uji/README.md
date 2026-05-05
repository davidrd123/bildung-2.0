# Dōgen — *Shōbōgenzō* 有時 (Uji) — Text Scaffold

道元禅師『正法眼蔵』「有時」

## What This Is

A text scaffold of *Uji* (Being-Time), with separate original/classical and
modern Japanese witness layers.

The `source/original/` file is the original/classical text supplied for this
scaffold. The `source/modern-japanese-raw/` file is **not** Dōgen's original
text; it is a raw extraction of a modern Japanese reading version with editorial
glosses in angle brackets (〈〉) clarifying implicit logical connectives.

## Status

- Source PDF in `sources/japanese/incoming/` (gitignored).
- Original/classical text stored under `source/original/`.
- Modern Japanese extracted text stored under `source/modern-japanese-raw/` via
  `pdftotext -raw`.
- The modern Japanese text is good enough for orientation, browsing, and
  discussion, but is not the translation base.
- Section markers (▼) from the modern Japanese source are preserved.

## Source

Original/classical layer: `source/original/020-uji.txt`

Modern Japanese witness PDF: `sources/japanese/incoming/shobo-gendaigoyaku/Vol02/11_Uji-ModJpn.pdf` (5 pages)

Parallel bilingual witness: `sources/japanese/incoming/eng-jap-shobo/Vol. 1/11. Uji.pdf`
This places Japanese text beside the Nishijima/Cross English translation and is
useful for phrase-level comparison during translation work. It is not the
authority source for this scaffold.

Numbering note: the modern Japanese and bilingual witness shelves label Uji as
`11`, while the original/classical text stored here labels it `第二十`.

Written at Kōshō-hōrin-ji (興聖宝林寺), 1240/10/1 (old calendar).
Copied by Ejō (懐弉) during summer retreat, 1243.

## Structure

```text
source/
  original/
    020-uji.txt          # original/classical Uji text, numbered 第二十 in this witness
  modern-japanese-raw/
    011-uji.txt          # pdftotext extraction of modern Japanese witness
```

## How To Use

- Use `source/original/020-uji.txt` as the base text for translation pressure.
- Use `source/modern-japanese-raw/011-uji.txt` as a modern Japanese
  interpretive witness.
- In `source/modern-japanese-raw/011-uji.txt`, ▼ markers indicate major section
  breaks.
- In `source/modern-japanese-raw/011-uji.txt`, 〈〉 brackets are editorial
  glosses, not Dōgen's original text.
- If the text earns encounter pressure, extend with cleaned, reader-en, or
  checked layers as needed.
