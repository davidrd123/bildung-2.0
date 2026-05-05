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

Sixth reader draft:

- `Символ - "ген сюжета"`
- source basis is raw OCR only
- the source boundary is split: the chapter opening appears at the end of
  `source/raw/009-part-i-05-tekst-v-protsesse-dvizheniya.txt`, while
  `source/raw/010-part-i-06-simvol-gen-syuzheta.txt` starts mid-sentence and
  later includes the opening of `СИМВОЛ В СИСТЕМЕ КУЛЬТУРЫ`
- the draft keeps symbol/plot pressure in pass notes: image-model, semantic
  paradigm, complementary readings, element/statue/human triad, fatal feast,
  textual gene, asymmetry, and nonequilibrium creative inspiration
- no glossary or thread promotion was made from the reader draft

Reader review incorporation:

- an external reader-layer review judged the first five reader drafts ready for
  discussion and audio-prep use, with several low-severity polish notes
- the review also exposed a cross-batch polish gradient: the earliest drafts
  read slightly more settled, while `008` and `009` retain a few phrases closer
  to Russian syntax; continuing reader drafts should favor spoken transitions
  and aural clarity in dense survey passages without turning the access layer
  into checked apparatus
- `005-part-i-01-tri-funktsii-teksta.md` now records `ипостась` as checked-work
  pressure while keeping `form` in the reader body for audibility
- `007-part-i-03-ritorika-smysloporozhdeniya.md` was lightly smoothed around
  `non-univocality`/`multivalence` and the Group Mu transition
- `008-part-i-04-ikonicheskaya-ritorika.md` was lightly smoothed in the van
  Eyck mirror passage to clarify flat painted figures against illusionistic
  room depth
- `009-part-i-05-tekst-v-protsesse-dvizheniya.md` already records the
  `замысел`/`design` pressure; no additional apparatus promotion was made

Seventh reader draft:

- `Символ в системе культуры`
- source basis is raw OCR only
- the source boundary is split: the chapter opening appears at the end of
  `source/raw/010-part-i-06-simvol-gen-syuzheta.txt`, while
  `source/raw/011-part-i-07-simvol-v-sisteme-kultury.txt` starts mid-paragraph
  and ends with the Part Two `СЕМИОСФЕРА` header
- the draft keeps symbol/culture pressure in pass notes: symbol as structural
  position, symbol versus reminiscence/quotation/symptom, symbolizing and
  desymbolizing reading, cultural memory, semantic reserve, semiotic condenser,
  and symbol as cultural genetic memory
- no glossary or thread promotion was made from the reader draft

Eighth reader draft:

- `Семиотическое пространство`
- source basis is raw OCR only
- this opens Part Two's semiosphere sequence; the Part Two header itself appears
  at the end of `source/raw/011-part-i-07-simvol-v-sisteme-kultury.txt`, while
  this draft begins with the chapter title in
  `source/raw/012-part-ii-01-semioticheskoe-prostranstvo.txt`
- the draft keeps semiosphere pressure in pass notes: semiotic space, language
  as condensation of semiotic space, binarity/asymmetry, presumption of
  semioticity, center/periphery, self-description, metalevel, real semiotics,
  internal translation, and boundary
- no glossary or thread promotion was made from the reader draft

Ninth reader draft:

- `Понятие границы`
- source basis is raw OCR only
- raw `013` is cleanly bounded: it starts with `ПОНЯТИЕ ГРАНИЦЫ` and ends
  before `МЕХАНИЗМЫ ДИАЛОГА`
- the draft keeps boundary pressure in pass notes: inner/outer space,
  our/their, semiotic individuality, center/periphery, boundary as filtering
  membrane, constituted bilinguality, cultural double, sub-semiospheres,
  semiotic subject/personality, antispace, decoloring, koine, and creolized
  semiotic systems
- because this is structurally central for the Lotman pass, it is a strong
  later candidate for a checked encounter, but no glossary or thread promotion
  was made from the reader draft

Tenth reader draft:

- `Механизмы диалога`
- source basis is raw OCR only
- raw `014` starts cleanly with the chapter title, but after the dialogue
  chapter closes it carries a short bridge on the semiotics of space; the
  reader draft excludes that bridge and records it as material to consider with
  `015-part-ii-04-semiosfera-i-problema-syuzheta`
- the draft keeps dialogue pressure in pass notes: dialogue as elementary
  mechanism of translation, asymmetry/invariance, love or mutual attraction as
  dialogic precondition, discreteness versus continuous intensity, cultural
  self-description, excitation/saturation/transmission cycles, center/periphery
  reversal, receiving/transmitting cultures, and semiosphere as energetic
  information space
- no glossary or thread promotion was made from the reader draft

Eleventh reader draft:

- `Семиосфера и проблема сюжета`
- source basis is raw OCR only
- the reader draft includes the short spatial-semiotics bridge that appears at
  the tail of `source/raw/014-part-ii-03-mekhanizmy-dialoga.txt`; raw `015`
  itself starts cleanly with the chapter title and ends before
  `СИМВОЛИЧЕСКИЕ ПРОСТРАНСТВА`
- the draft keeps plot/space pressure in pass notes: plot as boundary-crossing
  chain of acts, mobile and immobile characters, cyclical versus linear time,
  infinite Text, topological myth, homeomorphism, myth as non-discrete world,
  novella/news, double characters, plot space, marked beginning/end,
  eschatological legend, temporary death, initiation frame as narrative grammar,
  central/peripheral text-generating mechanisms, law/chance, miracle/scandal,
  and plot as a life-interpreting language
- no glossary or thread promotion was made from the reader draft

Symbolic Spaces container handling:

- `СИМВОЛИЧЕСКИЕ ПРОСТРАНСТВА` is a two-line heading-only container in
  `source/raw/016-part-ii-05-simvolicheskie-prostranstva.txt`
- it is marked `skip` in the reader manifest rather than being made into a
  fake reader chapter
- the heading is carried as context in the numbered essays `017` through `020`

Twelfth reader draft:

- `1. О понятии географического пространства в русских средневековых текстах`
- source basis is raw OCR only
- raw `017` starts cleanly with the first numbered Symbolic Spaces essay and
  ends before Dante's Ulysses essay in raw `018`
- the draft keeps geographical-space pressure in pass notes: spatial
  construction of the world, earth/heaven, geography as ethical knowledge,
  paradise/hell as local space, utopian geography, pilgrimage, chosenness,
  one's-own/alien, Babylon at home, moral status as spatial movement, local
  ethics, remoteness, West/East, and maps as historical semiotics
- no glossary or thread promotion was made from the reader draft

Thirteenth reader draft:

- `2. Путешествие Улисса в "Божественной комедии" Данте`
- source basis is raw OCR only
- raw `018` starts cleanly with the second numbered Symbolic Spaces essay and
  ends before the Bulgakov house essay in raw `019`
- the draft keeps Dante/spatial-symbolic pressure in pass notes: Dante as
  architect, universe as encoded message, spatial semiotics, relative versus
  absolute up/down, symbolic content/expression, Truth/Lie, straight line
  versus circular movement, moralized space, Dante/Ulysses doublehood, vertical
  pilgrimage versus horizontal travel, extra-moral knowledge, and science
  versus morality
- no glossary or thread promotion was made from the reader draft

Fourteenth reader draft:

- `3. Дом в "Мастере и Маргарите"`
- source basis is raw OCR only
- raw `019` starts cleanly with the third numbered Symbolic Spaces essay and
  ends before `Символика Петербурга` in raw `020`
- the draft keeps Bulgakov/house pressure in pass notes: House/Anti-house,
  forest house, homelessness, false house, communal apartment, housing
  question, apartment and death, Griboedov's House, city as anti-world,
  light/sound signs, House as spirituality, demonic spirituality, art,
  Master's search for the House, apartment versus House, and real space as
  iconic image of the semiosphere
- no glossary or thread promotion was made from the reader draft

Fifteenth reader draft:

- `4. Символика Петербурга`
- source basis is raw OCR only
- raw `020` starts cleanly with the fourth numbered Symbolic Spaces essay and
  ends before the Part II conclusion `Некоторые итоги` in raw `021`
- the draft keeps Petersburg/city pressure in pass notes: city as space/name,
  concentric and eccentric city, city on a hill, city on the edge,
  natural/artificial, eschatological city myth, water/stone, moving immovable,
  inverted world, Petersburg as eternal and doomed Rome, paradise and
  Antichrist, artificial city and mythogenesis, city as semiotic polyglot,
  city as mechanism resisting time, Petersburg mythology, external observer,
  spectrality, theatricality, stage/backstage, and Petersburg as artistic text
  versus metalanguage
- no glossary or thread promotion was made from the reader draft

Sixteenth reader draft:

- `Некоторые итоги`
- source basis is raw OCR only
- raw `021` starts cleanly with the Part II conclusion, then carries the Part
  III heading `ПАМЯТЬ КУЛЬТУРЫ. ИСТОРИЯ И СЕМИОТИКА`; the reader draft excludes
  that heading and records it as context for `022`
- the draft keeps spatial-modeling pressure in pass notes: organized spatial
  sphere, spatial image of the universe, iconic-continuous basis,
  verbal-discrete modeling, self-description, continuous/discrete sign
  pictures, multilayered spatial picture, historical experience,
  content/expression, spatial model and personality, and the collective/poetic
  language analogy
- no glossary or thread promotion was made from the reader draft

Seventeenth reader draft:

- `Проблема исторического факта`
- source basis is raw OCR only
- the Part III heading appears at the tail of raw `021` and is carried as
  reader context; raw `022` starts cleanly with the chapter title and ends
  before `Исторические закономерности и структура текста` in raw `023`
- the draft keeps history/decryption pressure in pass notes: historical fact,
  document criticism, historian as decipherer, fact as result rather than
  starting point, reconstruction of codes, excluded non-facts, genre code, fact
  as text, sender/receiver, extrasystemic elements, the Nag Hammadi/Gospel of
  Thomas scenario, fact relative to a cultural universe, and fact emerging from
  and dissolving in semiotic space
- this is a strong later candidate for a checked encounter on history as
  decryption, but no glossary or thread promotion was made from the reader
  draft

Eighteenth reader draft:

- `Исторические закономерности и структура текста`
- source basis is raw OCR only
- raw `023` starts cleanly with the chapter title and ends before
  `Альтернативный вариант: бесписьменная культура или культура до культуры?`
  in raw `024`
- the draft keeps historical-regularity pressure in pass notes: event as text,
  narrative deformation, plot-linearity, ideological coding, longue duree,
  anonymous process, literary language versus living speech, chance and
  necessity, bifurcation point, retrospective determinism, unrealized
  possibilities, intervention of a thinking being, historical semiotics,
  actant self-consciousness, creative text, prophet turned toward the past,
  beginning-oriented and end-oriented cultures, first deed, renewer, ancestral
  glory, eschatological ending, finite model of an infinite world,
  periodization, absolute beginning, and autocatalytic culture-production
- this is a strong later candidate for a checked encounter on history,
  semiotic choice, and narrative deformation, but no glossary or thread
  promotion was made from the reader draft
