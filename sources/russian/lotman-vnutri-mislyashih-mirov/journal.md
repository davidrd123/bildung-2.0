# Lotman Journal

## 2026-05-04 - Bounded Pilot Opened

Opened a bounded encounter pilot for *Внутри мыслящих миров* without promoting
the scaffold into a full translation project.

Reason:

- the existing OCR scaffold is useful for orientation but not reliable enough
  for fine lexical or quotation discipline
- the first-contact notes identified three live axes, but also warned against
  turning Lotman into a project authority
- Cassirer and Zeitmauer suggest a hybrid method: paragraph-cluster translation
  and close-reading residue from Cassirer, lean glossary and evidence discipline
  from Zeitmauer

First axis:

- `minimal-paired-heterogeneity`

Current constraint:

- this was opened before the DjVu tool check, so the first packet began as
  explicitly OCR-unchecked

Decision for now:

- create one encounter packet from the introduction and `Три функции текста`
- seed a glossary only for terms active in that packet
- do not create handles, viewer exports, or thread dossiers yet

## 2026-05-04 - DjVu Check For Packet 001

The DjVu is present at
`sources/modern/incoming/books/vnutri-mislyashih-mirov.djvu`. It has no embedded
text layer, but `djvulibre-bin` and `tesseract-ocr-rus` are enough for a bounded
rendered-page check.

Mapping found during the check:

- printed page `n` = DjVu page `n + 16`
- introduction printed pages 2-5 = DjVu pages 18-21
- `Три функции текста` printed pages 13-17 = DjVu pages 29-33

Created:

- `source/checked/001-minimal-paired-heterogeneity.ru.txt`

Confirmed pressure:

- `связанных блоком перевода языков` is present in the scan-backed OCR; the
  term-pressure problem is lexical/contextual, not just an OCR artifact
- `двуединой` and `неразложимо-единой` are likewise confirmed in the minimal
  culture passage
- `Комбинация переводимости - непереводимости` is confirmed in the creative
  translation passage

Decision:

- packet 001 may now be treated as DjVu-backed for its active range
- the wider raw scaffold remains browsing OCR only
- no new thread or handles file is earned by this check

## 2026-05-04 - Reader-En Pass Opened

Opened a broad English access layer without promoting Lotman into a full
translation campaign.

Created:

- `source/reader-en/README.md`
- `source/reader-en/manifest.yaml`
- `source/reader-en/005-part-i-01-tri-funktsii-teksta.md`
- `source/tts/README.md`

Decision:

- `raw`, optional `cleaned`, `reader-en`, and `tts` are access layers
- `checked`, `encounters`, glossary, journal, threads, and handles remain the
  apparatus path
- reader drafts can travel chapter by chapter for discussion and audio
  preparation, but term or thread promotion requires a separate checked
  encounter

First reader draft:

- `Три функции текста`
- source basis is the raw OCR scaffold, with the central creative-translation
  passage supported by checked packet 001
- pass notes mark Saussure/Benveniste quotations, diagrams, formula subscripts,
  and literary examples as source-check candidates before quotation-grade use

Second reader draft:

- `Автокоммуникация: "Я" и "Другой" как адресаты`
- source basis is raw OCR only
- the raw split boundary is not clean: the chapter opens at the end of
  `source/raw/005-part-i-01-tri-funktsii-teksta.txt` and continues in
  `source/raw/006-part-i-02-avtokommunikatsiya.txt`
- the draft records that boundary and keeps all term pressure as pass notes, not
  apparatus promotion

Third reader draft:

- `Риторика - механизм смыслопорождения`
- source basis is raw OCR only
- the draft keeps rhetoric/trope pressure in pass notes: trope as translation
  across untranslatable systems, semantic indeterminacy, rhetoric in science,
  minus-rhetoric, text as a large word, and rhetoric versus stylistics
- no glossary or thread promotion was made from the reader draft

Fourth reader draft:

- `Иконическая риторика`
- source basis is raw OCR only
- the draft keeps iconic rhetoric pressure in pass notes: doubling as the
  precondition of signness, mirror as double doubling, theater as translator-code
  between life and painting, real behavior/theater/pictorial art as a semiotic
  triangle, and rhetoric as transfer of structural principles across arts
- no glossary or thread promotion was made from the reader draft

First TTS export:

- `source/tts/005-part-i-01-tri-funktsii-teksta.md`
- generated from the corresponding `reader-en` draft
- reader metadata and pass notes were stripped; the file is a speakable access
  derivative, not the editable translation draft
- tracked in `source/tts/manifest.yaml`

Fifth reader draft:

- `Текст в процессе движения: "Замысел - текст"`
- source basis is raw OCR only
- the draft keeps author/audience and design/text pressure in pass notes:
  image of audience, common memory, language for others/language for oneself,
  actualization, contemporaneity versus tradition, symbol as first link,
  asymmetry, untranslatability, reverse reading, tolerance, and productive
  misunderstanding
- the raw file is not cleanly bounded: after this chapter it contains the
  opening of `СИМВОЛ - "ГЕН СЮЖЕТА"`; the reader draft stops before that next
  chapter and records the boundary issue
- no glossary or thread promotion was made from the reader draft
