# Lotman - *Культура и взрыв* Journal

## 2026-05-06 - Journal Discipline

This journal should follow the same basic discipline as
`texts/erkenntnisproblem-vol1/journal.md`: source-bound, chronological, and
workflow-bound.

For this book, the journal is not a free interpretive notebook. It should record:

- setup decisions and witness status
- page-batch or section-batch cleanup progress
- what the batch clarified about OCR failure modes, page mapping, footnotes,
  headings, and formatting
- decisions for now, especially when a page image is ambiguous
- remaining blockers or witness gaps

Interpretive comparisons, reading-order notes, or broader Lotman-system claims
belong elsewhere unless the cleaned page itself forces them. The cross-Lotman
reading-order note now lives at `../lotman-reading-order.md`.

Expected batch-entry shape:

- completed scan / printed page range
- cleaned file touched
- image authority used
- notable corrections or formatting decisions
- current decision / next continuation point

## 2026-05-06 - Initial DjVu Setup

Created a new source scaffold for Ю. М. Лотман, *Культура и взрыв*.

The canonical local witness is the user-supplied DjVu copied from Windows
Downloads to:

`source/local/lotman-kultura-i-vzryv.djvu`

This path is gitignored through the repo rule
`sources/russian/*/source/local/`.

Extraction state:

- `tools/extract_lotman_kultura_pages.py` extracts the DjVu hidden text layer.
- The DjVu reports 273 scan pages.
- Page-level OCR is under `source/raw/pages/NNN.txt`.
- Combined OCR is under `source/raw/full-ocr.txt`.
- Section-scale raw splits are under `source/raw/`.
- PNG proof images are under `source/page-images/pages/NNN.png`.
- `source/page-images/` is gitignored.

Initial witness observations:

- The DjVu and the convenient PDF derivative have the same OCR layer defects in
  sampled pages, so the PDF text layer is not a cleaner authority.
- The rendered DjVu page images are legible enough for page-by-page proofing.
- The OCR visibly damages names and common words. For example, scan page 007
  mangles the acknowledgments line, while the image reads: `В. И. Гехтман,
  Т. Д. Якушевой, Е. А. Погосян и С. Салупере`.
- The chapter heading on scan page 220 reads `Сон - семиотическое окно`; OCR
  may confuse `н` with `и` in this heading.

Current state:

- Raw OCR scaffold exists.
- Page-image proof workflow is ready.
- Cleaned text has not started.
- The detailed whole-book objective is recorded in
  `source/cleaned/cleanup-goal.md`.

## 2026-05-06 - Calibration Cleanup Batch

Completed the first page-image-proofed cleanup batch:

- `source/cleaned/000-front-matter.txt`
  - scans 001-007
- `source/cleaned/001-postanovka-problemy.txt`
  - scans 008-012
  - printed pages 7-11

Image authority:

- `source/page-images/pages/001.png` through
  `source/page-images/pages/012.png`

What this batch clarified:

- The DjVu OCR is only a scaffold. It missed the opening drop cap on scan 008
  and damaged names and common words in the front matter.
- Main-text page mapping holds for this range: printed page N maps to scan page
  N+1.
- Front matter should use `[scan NNN]` markers; numbered main text should use
  `[page N | scan NNN]`.
- Page breaks inside words should be preserved inline only when necessary. The
  page 7/8 break is recorded as `со[page 8 | scan 009]держания-выражения`.
- Scan 003 is a photo page, represented in the cleaned text with
  `[photo: Ю. М. Лотман]`.

Notable corrections:

- `Н. Гринцера`
- `Т. Д. Якушевой`
- `Е. А. Погосян`
- `подготовке этой книги`
- `Коренными вопросами`
- `трансцендентальным`
- `убивает Платона Каратаева`

Decision for now:

- Use star footnote markers as `[*]` and `[**]` in cleaned text where the
  printed page uses asterisks.
- Continue with `002-sistema-s-odnim-yazykom.txt`, beginning at scan 013 /
  printed page 12.

## 2026-05-06 - `Система с одним языком`

Completed:

- `source/cleaned/002-sistema-s-odnim-yazykom.txt`
  - scans 013-017
  - printed pages 12-16

Image authority:

- `source/page-images/pages/013.png` through
  `source/page-images/pages/017.png`

What this batch clarified:

- Diagram pages should be represented with concise bracketed placeholders rather
  than omitted; scan 013 has the communication model and scan 015 has the
  intersecting A/B circles.
- Latin diagram labels should remain `A` and `B`; OCR tends to make them look
  like Cyrillic `А` and `В`.
- Some printed irregularities should be retained rather than silently corrected:
  `Язык — это код плюс его история.)` on scan 014 and Goethe's `in meinen
  Brust` on scan 015.

Notable corrections:

- Restored the opening drop-cap word `Ставшая`.
- Removed `Культура u взрыв` running-header OCR damage.
- Reflowed page-break hyphenation and separated the Goethe and film-adaptation
  footnotes.
- Represented the first diagram as `передающий` / `текст` / `ЯЗЫК` /
  `принимающий`.

Decision for now:

- Preserve clear printed irregularities in the cleaned text and mention them in
  `page-proof-manifest.md`.
- Continue with `003-postepennyy-progress.txt`, beginning at scan 018 /
  printed page 17.

## 2026-05-06 - `Постепенный прогресс`

Completed:

- `source/cleaned/003-postepennyy-progress.txt`
  - scans 018-025
  - printed pages 17-24

Image authority:

- `source/page-images/pages/018.png` through
  `source/page-images/pages/025.png`

What this batch clarified:

- The section mixes conceptual exposition with long literary quotations, so
  quotation boundaries and footnote placement need to be checked against the
  page image rather than inferred from OCR.
- Page breaks inside words should stay inline only when the word spans the
  printed break; scan 022/023 is recorded as
  `пред[page 22 | scan 023]ставление`.
- Some apparent errors are printed features rather than OCR damage:
  `джентельмена`, `Иххх`, `Schneiders`, and the missing period after
  `процессов` on scan 024.

Notable corrections:

- Restored the opening drop-cap word `Движение`.
- Removed running-header OCR intrusions and reflowed line breaks into
  paragraphs.
- Separated the Delumeau, Bulwer-Lytton, and Mordovchenko footnotes from the
  body text.
- Preserved verse lineation for `Быть знаменитым некрасиво.`

Decision for now:

- Retain legible printed peculiarities in the cleaned text and document them in
  the proof manifest rather than silently normalizing them.
- Continue with `004-preryvnoe-i-nepreryvnoe.txt`, beginning at scan 026 /
  printed page 25.

## 2026-05-06 - `Прерывное и непрерывное`

Completed:

- `source/cleaned/004-preryvnoe-i-nepreryvnoe.txt`
  - scans 026-035
  - printed pages 25-34

Image authority:

- `source/page-images/pages/026.png` through
  `source/page-images/pages/035.png`

What this batch clarified:

- This section has several page breaks inside words; those were kept inline at
  `взаи[page 26 | scan 027]модействия`,
  `шест[page 27 | scan 028]вие`,
  `обя[page 28 | scan 029]зательно`, and
  `воз[page 29 | scan 030]можностей`.
- The Chekhov quotation on scans 032-033 needed image checking because OCR
  damaged both the author note and the second footnote marker.
- Printed omission markers in the Chekhov passage appear as `<... >`; retained
  that form for now rather than normalizing silently.

Notable corrections:

- Restored the opening drop-cap word `До`.
- Corrected `стадий`, `сферах`, `имманентной`, and the printed page 33 number.
- Corrected the Chekhov citation to `Чехов А. П. Полн. собр. соч. и писем в
  30-ти т. Т. V, М., 1976. С. 271.`
- Separated the Pushkin verse block and the two Chekhov star footnotes from the
  body flow.

Decision for now:

- Keep true literary quotation layout as readable text blocks, but leave source
  punctuation and omission typography faithful when legible.
- Continue with
  `005-semanticheskoe-peresechenie-kak-smyslovoy-vzryv.txt`, beginning at scan
  036 / printed page 35.

## 2026-05-06 - `Семантическое пересечение как смысловой взрыв. Вдохновение`

Completed:

- `source/cleaned/005-semanticheskoe-peresechenie-kak-smyslovoy-vzryv.txt`
  - scans 036-044
  - printed pages 35-43

Image authority:

- `source/page-images/pages/036.png` through
  `source/page-images/pages/044.png`

What this batch clarified:

- Literary material in this section needs lineation-first proofing: the
  Zhukovsky quotation, Pushkin passages, and Blok's `Художник` all required
  checking against the page image instead of trusting OCR line breaks.
- Page breaks inside words were retained inline at
  `геогра[page 36 | scan 037]фическая` and
  `слав[page 42 | scan 043]ный вопрос`.
- Lotman's bracketed insertions are printed with spaces before the closing
  bracket, e.g. `<душе — Ю. Л. >` and `<Чарский — Ю. Л. >`; retained for now.

Notable corrections:

- Restored the heading `Семантическое пересечение как смысловой взрыв.
  Вдохновение` from damaged OCR.
- Corrected `Длятся`, `Пушкин А. С. Полн. собр. соч.`, `Т. II`,
  `непереводимости`, and `полилингвиальной`.
- Removed running-header intrusions and separated three star footnotes from the
  body text.
- Preserved the Blok poem as verse rather than prose-wrapping it.

Decision for now:

- Preserve source lineation for cited verse and use separate footnote blocks
  immediately after the quotation or poem they support.
- Continue with `006-myslyashchiy-trostnik.txt`, beginning at scan 045 /
  printed page 44.

## 2026-05-06 - `Мыслящий тростник`

Completed:

- `source/cleaned/006-myslyashchiy-trostnik.txt`
  - scans 045-052
  - printed pages 44-51

Image authority:

- `source/page-images/pages/045.png` through
  `source/page-images/pages/052.png`

What this batch clarified:

- The Tyutchev poem and the long first note need to remain verse-like; OCR
  flattened the citation block and damaged several initials.
- The Radlov quotation contains the scanned term `гектохорд`; retained it and
  recorded it in the manifest instead of silently replacing it.
- Notes on scan 047 interrupt a body word that continues as
  `Тютчев[page 47 | scan 048]ский`; the cleaned text keeps the body paragraph
  continuous and places the notes after the annotated paragraph.

Notable corrections:

- Restored `В равной мере` on scan 045.
- Corrected `Полн. собр. стихотворений`, `Л.`, `Радлов Э. Л.`,
  `Философский словарь`, `Клиний`, and `сталкиваемся`.
- Separated Tyutchev, Radlov, and Plato footnotes from the main text.
- Preserved true split-word page markers at `служа[page 48 | scan 049]щих`,
  `обуча[page 50 | scan 051]ется`, and
  `ма[page 51 | scan 052]гических`.

Decision for now:

- For pages with heavy footnote apparatus, keep the main body readable first and
  log any note-placement decision in the journal.
- Continue with `007-mir-sobstvennykh-imen.txt`, beginning at scan 053 /
  printed page 52.

## 2026-05-06 - `Мир собственных имен`

Completed:

- `source/cleaned/007-mir-sobstvennykh-imen.txt`
  - scans 053-064
  - printed pages 52-63

Image authority:

- `source/page-images/pages/053.png` through
  `source/page-images/pages/064.png`

What this batch clarified:

- This section required page-image checking for several quotation-heavy pages:
  Chekhov on scan 054, Rousseau on scan 058, Bulgakov/Krylov on scan 060,
  Radishchev on scan 063, and Gogol on scan 064.
- Page markers often fall inside running sentences rather than at paragraph
  boundaries, so the cleaned text keeps several markers inline to avoid
  creating false paragraph breaks.
- The Bulgakov passage and its three footnotes were badly damaged by OCR; the
  page image restores `по-всамделишному`, `Настасье Ивановне`, the internal
  quote `„убью тебя, негодя!“`, and the Томашевский citation.

Notable corrections:

- Restored the opening drop-cap word `Отождествление`.
- Corrected `целовали`, `не как животное`, `свой и чужой`,
  `человеческому`, and `может быть`.
- Restored Rousseau's printed omission marker `<... >` and citation
  `Жан-Жак Руссо. Трактаты. М., 1969. С. 60—61.`
- Separated the individuality, Rousseau, Bulgakov, Томашевский, Radishchev,
  and Gogol notes from the body flow.

Decision for now:

- Keep inline page markers when a page break falls inside a sentence, but keep
  footnotes as separate readable blocks near their reference point.
- Continue with `008-durak-i-sumasshedshiy.txt`, beginning at scan 065 /
  printed page 64.

## 2026-05-06 - `Дурак и сумасшедший`

Completed:

- `source/cleaned/008-durak-i-sumasshedshiy.txt`
  - scans 065-104
  - printed pages 64-103

Image authority:

- `source/page-images/pages/065.png` through
  `source/page-images/pages/104.png`

What this batch clarified:

- This is the first long proofing section and needs verse/source-apparatus
  handling as much as ordinary prose cleanup: Don Quixote, Devgenii, medieval
  honor/glory notes, Homer, Pushkin, Nekrasov, Mayakovsky, and Pasternak all
  required line- or citation-level checking against the page images.
- Page markers remain sequential from `[page 64 | scan 065]` through
  `[page 103 | scan 104]`; many are inline because the scan break falls inside
  a word or sentence.
- A few scanned peculiarities were retained rather than silently normalized:
  Monomakh's `лиси день` in the old-Russian quote and printed
  `условности..`.

Notable corrections:

- Restored the opening drop-cap word `Бинарное`.
- Corrected OCR damage in `не к месту`, `щадили`, `Ю. Л.`, `был`,
  `мотоциклистов`, `Транквилл`, `трансфигурация`, `Тьмутараканью`,
  `Гегельянское`, `Кифа Мокиевич`, and `Полн. собр. соч.`
- Rebuilt the long note sequences around the chivalric-love note, Malkiel /
  Greimas, Apolonio, Toporov/Homer, Pushkin/Gogol, and Mayakovsky/Pasternak so
  they are readable and not fused into the body text.

Decision for now:

- For long sections, complete the whole section when practical, but keep the
  proof ledger detailed enough that retained scanned oddities are visible.
- Continue with `009-tekst-v-tekste-vstavnaya-glava.txt`, beginning at
  scan 105 / printed page 104.

## 2026-05-06 - `Текст в тексте. Вставная глава`

Completed:

- `source/cleaned/009-tekst-v-tekste-vstavnaya-glava.txt`
  - scans 105-123
  - printed pages 104-122

Image authority:

- `source/page-images/pages/105.png` through
  `source/page-images/pages/123.png`

What this batch clarified:

- This section is citation- and metatext-heavy rather than lexically difficult.
  The cleanup work was mainly preserving the nested text structure: Onegin
  stanza, Pushkin prose, Shakespeare/Hamlet lines and notes, Bulgakov embedded
  chapter transitions, mirror examples, and frame/composition apparatus.
- Page markers are sequential from `[page 104 | scan 105]` through
  `[page 122 | scan 123]`; broken-word markers were kept inline at points such
  as `Прогнози[page 105 | scan 106]рование`,
  `вклю[page 112 | scan 113]ченными`, and
  `фраг[page 121 | scan 122]ментарном`.

Notable corrections:

- Restored the opening drop-cap word `В`.
- Corrected `Полн. собр. соч.`, `Б. А. Успенскому`, `кодированности`,
  `Первый актер`, `Шекспиром`, `Ю. Л.`, `негромко`, `все время`, and page
  header intrusions such as `Текст s тексте` / `Культура u взрыв`.
- Rebuilt notes for Pushkin, Uspensky, Shakespeare, Derzhavin, Bulgakov,
  Shubnikov/Koptsik, Mints, Lotman, and Francastel as separate readable note
  blocks.

Decision for now:

- Continue to use the cleaned corpus as source text, not commentary: nested
  text examples should be preserved structurally, but the journal should only
  record cleanup/proofing decisions.
- Continue with `010-perevernutyy-obraz.txt`, beginning at scan 124 /
  printed page 123.

## 2026-05-06 - `Перевернутый образ`, First Batch

Completed the first proof batch for the long section:

- `source/cleaned/010-perevernutyy-obraz.txt`
  - scans 124-133
  - printed pages 123-132
  - partial section file; remaining section text starts at scan 134 / printed
    page 133

Image authority:

- `source/page-images/pages/124.png` through
  `source/page-images/pages/133.png`

What this batch clarified:

- The section begins with another damaged drop cap; the image reads `В
  пространстве`, not the raw OCR's `П пространстве`.
- The hidden OCR and fresh page OCR both misread several ordinary words and page
  numbers in this range, so page-image checking remains necessary even when the
  raw scaffold looks fluent.
- The long section can be safely handled in proof batches as long as manifests
  mark `010` as partial and do not claim full section coverage.

Notable corrections:

- Restored `предопределена`, `произведения искусства`, `абсурдистское`,
  `разрешают`, `самолюбие`, `Панченко А. М.`, and the printed page 131 marker.
- Preserved the parody verse, French bibliography, `couleur locale`, German
  `Der Narr in Christo Emanuel Quint`, Davydov notes, and Panchenko notes.
- Separated all star notes from the body flow and kept inline page markers at
  page-broken words such as `являет[page marker]ся`, `предопределена`,
  `противоречие`, `Веселовского`, and `неизбежно`.

Decision for now:

- Continue section `010` at scan 134 / printed page 133, beginning with
  `власти не мог решить, Бого- или дьяволоподобна...`.

## 2026-05-06 - `Перевернутый образ`, Completion

Completed the remaining proof batches for the long section:

- `source/cleaned/010-perevernutyy-obraz.txt`
  - scans 134-176 completed in this continuation
  - full section coverage is now scans 124-176 / printed pages 123-175

Image authority:

- `source/page-images/pages/134.png` through
  `source/page-images/pages/176.png`

What this batch clarified:

- The section required strict page-image checking even where the raw OCR looked
  fluent: names, citation abbreviations, Roman numerals, French/German/Polish
  phrases, and page-local star notes were frequent failure points.
- Page markers are sequential across the completed section from
  `[page 123 | scan 124]` through `[page 175 | scan 176]`.
- No unresolved readings were left in this batch; no `[unclear: ...]` markers
  were added.

Notable corrections:

- Completed the Orlova/Fotiy passage and corrected the Shishkov/Krylov/Pushkin
  apparatus around scans 154-155.
- Rebuilt the Ponomareva, Zinaida Volkonskaya, Zakrevskaya, Karamzina/Tolstoy,
  Kovalevskaya, Tsvetaeva/Pasternak, and Gogol/Dantes passages with verse and
  footnotes separated from body flow.
- Corrected OCR damage in names and phrases including `Пономаревой`,
  `Геништою`, `Pokój grecki`, `au dessus du vulgaire`, `Ковалевская`,
  `Персиду`, `comme il faut`, and `fin du siècle`.

Decision for now:

- Continue with `011-logika-vzryva.txt`, beginning at scan 177 / printed page
  176.

## 2026-05-06 - `Логика взрыва`

Completed:

- `source/cleaned/011-logika-vzryva.txt`
  - scans 177-190
  - printed pages 176-189

Image authority:

- `source/page-images/pages/177.png` through
  `source/page-images/pages/190.png`

What this batch clarified:

- This section is shorter but dense in cross-language and citation details. The
  raw OCR damaged the opening drop cap, Roman numerals, French epigraph,
  Chaplin dates, and several page-bottom notes.
- Page markers are sequential from `[page 176 | scan 177]` through
  `[page 189 | scan 190]`.
- No unresolved readings were left in this batch; no `[unclear: ...]` markers
  were added.

Notable corrections:

- Restored the opening `Мы`, the Lermontov French epigraph, and the French
  explanatory note.
- Corrected textology apparatus around Tomashevsky/Eikhenbaum and Uspensky,
  including the `München` bibliography line.
- Corrected Chaplin film titles/dates, `Демоне`, `автоцитату`, the Chesterton
  quotation, the Poe/Barker passage, and retained the printed `решения, Эта`
  punctuation on scan 190.

Decision for now:

- Continue with `012-moment-nepredskazuemosti.txt`, beginning at scan 191 /
  printed page 190.

## 2026-05-06 - `Момент непредсказуемости`

Completed:

- `source/cleaned/012-moment-nepredskazuemosti.txt`
  - scans 191-205
  - printed pages 190-204

Image authority:

- `source/page-images/pages/191.png` through
  `source/page-images/pages/205.png`

What this batch clarified:

- The raw OCR was mostly fluent, but the page images were needed for the
  opening drop cap, printed page numbers, footnote anchors, line-broken words,
  foreign phrase `le roi de Rome`, and source apparatus.
- Page markers are sequential from `[page 190 | scan 191]` through
  `[page 204 | scan 205]`.
- No unresolved readings were left in this batch; no `[unclear: ...]` markers
  were added.

Notable corrections:

- Rebuilt the duel analysis and its page-local notes, including the Boris
  Ivanov/Nabokov note and the Pierre/Dolokhov note.
- Restored the Pasternak verse block and notes on A. Schlegel/Pustygina and the
  early 1924 version.
- Corrected the Zavalishin memoir passage, Karamzin verse, Citsianov anecdotes,
  Pushkin table-talk note, and long Dostoevsky/Ivolgin quotation with the
  French explanatory note.
- Corrected OCR damage including `круг декабристов`, `Полн. собр. соч.`,
  `Достоевский Ф. М.`, and page-number misreads such as printed pages 196 and
  198.

Decision for now:

- Continue with `013-vnutrennie-struktury-i-vneshnie-vliyaniya.txt`, beginning
  at scan 206 / printed page 205. During setup for the next batch, page images
  showed that `013` ends at scan 213 / printed page 212 and `014` begins at
  scan 214 / printed page 213; `sections.yaml` and the manifests were corrected
  accordingly.

## 2026-05-06 - `Внутренние структуры и внешние влияния`

Completed:

- `source/cleaned/013-vnutrennie-struktury-i-vneshnie-vliyaniya.txt`
  - scans 206-213
  - printed pages 205-212

Image authority:

- `source/page-images/pages/206.png` through
  `source/page-images/pages/213.png`

What this batch clarified:

- The previous section map had an off-by-two boundary: images show `013` ends
  on scan 213 / printed page 212, and `014` begins on scan 214 / printed page
  213. `sections.yaml`, `cleanup-manifest.md`, and `page-proof-manifest.md`
  were corrected before creating the cleaned file.
- Page markers are sequential from `[page 205 | scan 206]` through
  `[page 212 | scan 213]`.
- No unresolved readings were left in this batch; no `[unclear: ...]` markers
  were added.

Notable corrections:

- Restored the opening `Динамика` and corrected OCR scars such as
  `имманентный`, `Наполеоновские`, and damaged printed page numbers.
- Preserved the Pushkin verse block with the scanned punctuation
  `землей?,`.
- Reflowed the Lermontov/synonymy and common/proper-name passages, separating
  the `Мир собственных имен` note from the body flow.
- Corrected the Marr/Sorokin passage, including `Н. Я. Марра`, `50-е годы`,
  and `Юрия Сергеевича Сорокина`.

Decision for now:

- Continue with `014-dve-formy-dinamiki.txt`, beginning at scan 214 / printed
  page 213.

## 2026-05-06 - `Две формы динамики`

Completed:

- `source/cleaned/014-dve-formy-dinamiki.txt`
  - scans 214-219
  - printed pages 213-218

Image authority:

- `source/page-images/pages/214.png` through
  `source/page-images/pages/219.png`

What this batch clarified:

- Because the corrected section boundary moved `014` earlier, the section OCR
  file began two scans late. Scans 214-215 were therefore proofed from
  per-page OCR and images.
- Page markers are sequential from `[page 213 | scan 214]` through
  `[page 218 | scan 219]`.
- No unresolved readings were left in this batch; no `[unclear: ...]` markers
  were added.

Notable corrections:

- Restored the opening `Соотношение` and reflowed the Zhirmunsky/Gukovsky
  comparison.
- Corrected citation details including `Academia`, `де Мюссе`, `Новая Элоиза`,
  `Герман и Доротея`, and the Gukovsky bibliography.
- Rebuilt the Freidenberg `Терсит` passage and three page-local notes, including
  `Яфетический сборник VI`.
- Corrected final-page name OCR around `О. М. Фрейденберг` and `М. М. Бахтина`.

Decision for now:

- Continue with `015-son-semioticheskoe-okno.txt`, beginning at scan 220 /
  printed page 219.

## 2026-05-06 - `Сон - семиотическое окно`

Completed:

- `source/cleaned/015-son-semioticheskoe-okno.txt`
  - scans 220-227
  - printed pages 219-226

Image authority:

- `source/page-images/pages/220.png` through
  `source/page-images/pages/227.png`

What this batch clarified:

- The title and opening were especially OCR-fragile: the page image confirms
  `Сон - семиотическое окно` and the initial drop-cap `В`.
- Page markers are sequential from `[page 219 | scan 220]` through
  `[page 226 | scan 227]`.
- No unresolved readings were left in this batch; no `[unclear: ...]` markers
  were added.

Notable corrections:

- Corrected the Florensky/Uspensky note and the surrounding account of dream
  retelling and temporal organization.
- Reflowed the sleep-as-message argument, including the transition through
  semiotic experiment, the alien prophetic voice, and the first-/third-person
  ambiguity.
- Corrected the Zola/Doctor Pascal example, including `больному
  дистиллированную воду`.
- Corrected the final pages around `полилингвиальностью`, `акад. А. Н.
  Веселовского`, `предельно близком`, and `ich-Erzählung'ом`; retained scanned
  `сно-видения`.

Decision for now:

- Continue with `016-ya-i-ya.txt`, beginning at scan 228 / printed page 227.

## 2026-05-06 - `«Я» и «Я»`

Completed:

- `source/cleaned/016-ya-i-ya.txt`
  - scans 228-232
  - printed pages 227-231

Image authority:

- `source/page-images/pages/228.png` through
  `source/page-images/pages/232.png`

What this batch clarified:

- The title image confirms `«Я» и «Я»`; OCR had damaged the conjunction and
  capitalization.
- Page markers are sequential from `[page 227 | scan 228]` through
  `[page 231 | scan 232]`.
- No unresolved readings were left in this batch; no `[unclear: ...]` markers
  were added.

Notable corrections:

- Restored the opening drop-cap `Руссо` and corrected the Rousseau citation
  apparatus, including `Moi seul`, `Oeuvres complètes`, and the Russian
  edition note.
- Corrected page-number OCR damage and removed running headers from the body
  flow.
- Rebuilt the Fonvizin dialogue from the image, especially `Правдин` and the
  final `И ведомо`.
- Preserved the Pushkin/Tatyana verse block and the argument about
  simultaneous proper and common names.

Decision for now:

- Continue with `017-fenomen-iskusstva.txt`, beginning at scan 233 / printed
  page 232.

## 2026-05-06 - `Феномен искусства`

Completed:

- `source/cleaned/017-fenomen-iskusstva.txt`
  - scans 233-248
  - printed pages 232-247

Image authority:

- `source/page-images/pages/233.png` through
  `source/page-images/pages/248.png`

What this batch clarified:

- The contents OCR had earlier misread the start page; the image map confirms
  this section runs from printed page 232 through printed page 247.
- Page markers are sequential from `[page 232 | scan 233]` through
  `[page 247 | scan 248]`.
- No unresolved readings were left in this batch; no `[unclear: ...]` markers
  were added.

Notable corrections:

- Restored the opening drop-cap `Трансформация` and corrected early OCR damage
  around `не могут`, `неизбежность`, and the ethics/aesthetics argument.
- Rebuilt the freedom/experiment passage, including the Gofman/Tolstoy examples
  and Lindsay Anderson's `If` discussion.
- Corrected the Pushkin/Onegin verse blocks, Kuechelbecker passage, repeated
  newspaper footnote, `Н. Смирнов-Сокольский`, and Pushkin apparatus.
- Corrected the folklore/improvisation and audience-participation pages,
  including `полюса`, `двуединство`, `условное соприсутствие`, and
  `не-зритель`.
- Preserved the Blok verse block and corrected the final Heraclitus reference
  to `112-й фрагмент`.

Decision for now:

- Continue with `018-konets-kak-zvuchno-eto-slovo.txt`, beginning at scan 249 /
  printed page 248.

## 2026-05-06 - `«Конец! как звучно это слово...»`

Completed:

- `source/cleaned/018-konets-kak-zvuchno-eto-slovo.txt`
  - scans 249-257
  - printed pages 248-256

Image authority:

- `source/page-images/pages/249.png` through
  `source/page-images/pages/257.png`

What this batch clarified:

- The title and opening were OCR-damaged; the image confirms `«Конец! как
  звучно это слово...»` and the opening `В 1832 году`.
- Page markers are sequential from `[page 248 | scan 249]` through
  `[page 256 | scan 257]`.
- No unresolved readings were left in this batch; no `[unclear: ...]` markers
  were added.

Notable corrections:

- Restored Lermontov, Pushkin, Blok, Tvardovsky, and Baratynsky verse blocks
  and notes, including `Лопухиной`, `Полн. собр.`, and corrected page/date
  apparatus.
- Reflowed the argument on endings, death, cyclic models, and
  death-resurrection, preserving the page-local star notes.
- Corrected the Falstaff quotation and Shakespeare note, including
  `сенсуалистические идеи`, `Франц Моор`, and the Shamil-order sentence.
- Corrected the Vovelle citation, `fin du siècle`, `можно`, and the final
  sex-as-language argument.

Decision for now:

- Continue with `019-perspektivy.txt`, beginning at scan 258 / printed page
  257.

## 2026-05-06 - `Перспективы`

Completed:

- `source/cleaned/019-perspektivy.txt`
  - scans 258-266
  - printed pages 257-265

Image authority:

- `source/page-images/pages/258.png` through
  `source/page-images/pages/266.png`

What this batch clarified:

- The section continues the main-text page map cleanly: printed page 257 maps to
  scan 258, and the final marker is `[page 265 | scan 266]`.
- Page markers are sequential from `[page 257 | scan 258]` through
  `[page 265 | scan 266]`.
- No unresolved readings were left in this batch; no `[unclear: ...]` markers
  were added.

Notable corrections:

- Restored the opening `Итак` and reflowed the binary/ternary contrast without
  running-header intrusions.
- Corrected the Masha Mironova/Grinev passage, Pushkin `Анджело` quotations and
  notes, and the Latin legal maxim apparatus.
- Rebuilt the Tolstoy `Власть тьмы` quotation, including Aким's dialectal
  `тае`, and separated the Tolstoy/Mandelshtam notes.
- Corrected the Savonarola/Bulgakov apparatus, Krylov `Парнас` verse block,
  `любой ценой`, `Горбачева`, `500 дней`, and the final transition passage.

Decision for now:

- Continue with `020-vmesto-vyvodov.txt`, beginning at scan 267 / printed page
  266.

## 2026-05-06 - `Вместо выводов`

Completed:

- `source/cleaned/020-vmesto-vyvodov.txt`
  - scans 267-271
  - printed pages 266-270

Image authority:

- `source/page-images/pages/267.png` through
  `source/page-images/pages/271.png`

What this batch clarified:

- This is the final main-text section; the next proof target is the
  contents/colophon block on scans 272-273.
- Page markers are sequential from `[page 266 | scan 267]` through
  `[page 270 | scan 271]`.
- No unresolved readings were left in this batch; no `[unclear: ...]` markers
  were added.

Notable corrections:

- Restored the opening drop-cap `Представление` and the chapter heading.
- Corrected OCR damage around `значительно более`, `далекой от политики`,
  `социал-демократии`, and the split `социализм`.
- Reflowed the binary/ternary comparison and preserved the page-broken
  `Наполеоновской` and `социализму` markers.
- Corrected the final French slogan `laissez faire, laissez passer`, the
  `Нарвской битвой` / `Ништадским миром` passage, `старый мир до основанья`,
  and the footnote ending `предоставьте собственному движению`.

Decision for now:

- Continue with `021-contents-and-colophon.txt`, beginning at scan 272.

## 2026-05-06 - Contents and colophon

Completed:

- `source/cleaned/021-contents-and-colophon.txt`
  - scans 272-273

Image authority:

- `source/page-images/pages/272.png`
- `source/page-images/pages/273.png`

What this batch clarified:

- The contents page confirms the corrected section boundary already used in the
  cleanup: `Две формы динамики` begins on printed page 213, not the OCR-damaged
  page 215.
- The contents page also confirms `Феномен искусства` begins on printed page
  232.
- No unresolved readings were left in this batch; no `[unclear: ...]` markers
  were added.

Notable corrections:

- Corrected contents OCR damage in item numbering, `Постановка проблем`,
  `Логика взрыва`, `Перевернутый образ`, and `Перспективы`.
- Rebuilt multiline contents entries for `Семантическое пересечение как
  смысловой взрыв`, `Текст в тексте. (Вставная глава)`, `Внутренние структуры
  и внешние влияния`, and `«Конец! как звучно это слово...»`.
- Corrected the colophon names and publication data, including `ИБ № 19459`,
  `29.09.92`, `70 × 100 1/32`, `№ 48610`, `119847, Москва`, and the typography
  address.

Decision for now:

- Run the full-book completion audit and residue checks before calling the
  cleanup complete.
