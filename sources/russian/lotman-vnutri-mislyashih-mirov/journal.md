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

Nineteenth reader draft:

- `Альтернативный вариант: бесписьменная культура или культура до культуры?`
- source basis is raw OCR only
- raw `024` starts cleanly with the chapter title and ends before `О роли
  типологических символов в истории культуры` in raw `025`
- the draft keeps non-written-memory pressure in pass notes: non-written
  culture, culture before culture, writing as collective memory, memory of
  exceptional events versus memory of order, ritual as memory,
  mnemonic-sacred symbol, oral culture oriented toward the future, sacrifice
  as futurological experiment, choice transferred outside the person, omen and
  prediction, gesture of choice, oral memory saturated with symbols, loosened
  syntax of oral symbols, ornament versus phrase, written sign versus idol or
  sacred place, landscape as text, laws versus omens, isolation, and semiotic
  translation
- this is a strong later candidate for a checked encounter on writing,
  collective memory, and non-written symbolic order, but no glossary or thread
  promotion was made from the reader draft

Twentieth reader draft:

- `О роли типологических символов в истории культуры`
- source basis is raw OCR only
- raw `025` starts cleanly with the chapter title and ends before `Возможна ли
  историческая наука и в чем ее функция в системе культуры?` in raw `026`
- the draft keeps typological-symbol pressure in pass notes: magical system,
  religious act, reciprocity, compulsion, equivalence, contractuality,
  unconditional self-entrustment, unconditional gift, sign versus symbol,
  contract with holiness or unclean force, cross-kissing, wordplay as
  deception, sovereign's service, service as serving, signness, knightly
  honor, effect versus effectiveness, zero semiotics, living icon,
  desymbolization, tsar-worker, secular religion of statehood, silent
  contract, exchange of dignity for signs, noble privilege as advance, dandy
  culture, autonomy of the sign, motivated and unmotivated signs, social
  contract, Masonic emblem, Rousseau in Russia, deified People, contract with
  the alien, trust within one's own milieu, and typological tendency versus
  historical variation
- this is a strong later candidate for a checked encounter on contract,
  symbol, and Russian cultural semiotics, but no glossary or thread promotion
  was made from the reader draft

Twenty-first reader draft:

- `Возможна ли историческая наука и в чем ее функция в системе культуры?`
- source basis is raw OCR only
- raw `026` starts cleanly with the chapter title and ends before `Заключение`
  in raw `027`
- the draft keeps methodological pressure in pass notes: historical science,
  "how it actually was," problem of language, metalanguage and object, observer
  inside the described world, translation as universal scientific task,
  absolute point of view, historical semiotics, source language and researcher
  language, common-sense identification, understanding as translation, typology
  as historical-cultural instrument, historian's own culture type, history and
  historian as asymmetric languages, history as cultural memory, memory as
  active present mechanism, memory as generator, and forecasts of the past
- this is a strong later candidate for a checked encounter on history as
  translation and cultural memory, but no glossary or thread promotion was made
  from the reader draft

Twenty-second reader draft:

- `Заключение`
- source basis is raw OCR only
- raw `027` starts cleanly with the conclusion title and ends before
  `Литература` in raw `028`
- the draft keeps closing-method pressure in pass notes: individual
  intellectual apparatus, semiotic systems as thinking systems, integrating
  unity of the semiosphere, thought inside us and us inside thought, language
  generated by consciousness and surrounding consciousness, spatial image
  inside and outside us, enormous intellectual mechanism, synthetic study,
  single intellectual life of humanity, matryoshka, intellectual galaxy, and
  general and historical semiotics of culture
- no glossary or thread promotion was made from the reader draft

Twenty-third reader draft:

- `Вводные замечания`
- source basis is raw OCR, with the intellectual-functions and three-part
  outline passages supported by checked packet `001`
- raw `003` starts cleanly with the introductory remarks and ends before
  `После Соссюра` in raw `004`
- the draft keeps introductory pressure in pass notes: intellect, thinking
  objects, invariant of intellectuality, transmission of texts, creation of new
  information, memory, semiotic object, mutually untranslatable languages,
  block of translation, two-in-one culture, indivisibly unified culture,
  semiosphere, thinking structures, intellect as interlocutor, bipolar
  asymmetry, neurophysiology and semiotics, symmetry and asymmetry,
  autocatalytic reaction, beginning of culture, conventional/discrete/verbal
  and iconic/continuous/spatial languages, memory, depth-diachrony, and
  semiotics of history
- no glossary or thread promotion was made from the reader draft

Twenty-fourth reader draft:

- `После Соссюра`
- source basis is raw OCR only
- raw `004` starts cleanly with the second introductory chapter and ends with
  the Part One heading `Текст как смыслопорождающее устройство`; the reader
  draft excludes that heading because the first Part One chapter is already
  drafted in `005`
- the draft keeps Saussure-introduction pressure in pass notes: semiotics and
  structuralism, persecution and fashion, depth of scientific ideas,
  continuation and overcoming, semiotics as discipline, semiotics as method,
  semiotics as scientific psychology, semioticization by the researcher,
  describer and described object, language and speech, code and text, synchrony
  and diachrony, homeostatic synchrony, accidental diachrony, and Saussure as
  foundation and problem
- no glossary or thread promotion was made from the reader draft

Twenty-fifth reader draft:

- Vyach. Vs. Ivanov, `Семиосфера и история`, plus `От редактора`
- source basis is raw OCR only
- raw `002` starts cleanly with Ivanov's preface, includes the editor's note,
  and ends with the raw `Введение` heading; the reader draft excludes that
  final heading because the introduction proper is now drafted in `003` and
  `004`
- the draft keeps contextual pressure in pass notes: explosion in culture and
  history, unpredictability after explosion, gradual evolution and explosion,
  natural history and cultural history, Big Bang, anthropic principle,
  cyclical universe, information processes, information theory, chaos, strange
  attractors, fractals, semiosphere and history, Russian history and
  retrospection, reconstruction of unrealized possibilities, equiprobability,
  probability of post-explosion events, and future historical science
- this is non-Lotman contextual front matter; no glossary or thread promotion
  was made from the reader draft

Twenty-sixth reader draft:

- Umberto Eco, `Предисловие к английскому изданию`
- source basis is raw OCR only; the Russian source is itself a translation
  from Eco's English preface
- raw `029` starts cleanly with Eco's appendix and ends before Gasparov's
  `Лотман и марксизм` in raw `030`
- the draft keeps reception/theory pressure in pass notes: semiotics and
  structuralism, Russian Formalism, device and estrangement, structural
  description, semantic systems, universal communicative phenomena, code and
  message, exact methods in literary studies, primary and secondary modeling
  systems, typology of cultures, culture as code, grammar-oriented and
  text-oriented culture, handbook and Book, nonhereditary collective memory,
  boundary, cultural code, creolization, and semiosphere as single mechanism
- this is non-Lotman contextual appendix material; no glossary or thread
  promotion was made from the reader draft

Twenty-seventh reader draft:

- M. L. Gasparov, `Лотман и марксизм`
- source basis is raw OCR only
- raw `030` starts cleanly with Gasparov's appendix and ends before the name
  index in raw `031`
- the draft keeps Gasparov-context pressure in pass notes: Marxist method
  versus Marxist ideology, materialism, historicism, dialectics, structure as
  model of relations, ideology as anti-historical, text as field of norm and
  violation, information measure, concrete truth, proper names versus common
  nouns, history as lawful but not fatal, unused possibilities, average level
  of spiritual life, personality as intersection of social codes, science and
  art, true Pushkin versus my Pushkin, humanistic enrichment, history
  evaluating modernity, binary and ternary culture, scientificity between
  dogmatism and anti-dogmatism, and Marxist method and structuralism
- this is non-Lotman contextual appendix material; no glossary or thread
  promotion was made from the reader draft

TTS layer expansion:

- added repeatable exporter `tools/export_lotman_tts.py`
- regenerated `source/tts/*.md` from all current `source/reader-en/*.md`
- TTS exports strip reader metadata and `## Pass Notes`, leaving speakable
  headings and reading text for the Alexandria/Gemini audiobook pipeline
- the existing `reader-en` drafts remain the editable access layer; `tts`
  remains a derived audio layer and does not seed glossary, handles, threads,
  or encounter claims

TTS speech-normalization pass:

- extended the repeatable exporter with a narrow speech cleanup stage
- normalized compact symbolic forms in the generated TTS layer, especially
  `T1`/`T2`/`Tn`, `K1`/`K2`, `L1`/`L2`, and `k1`/`kn`
- normalized Lotman's schematic communication labels from dash notation
  (`I - HE`, `I - I`, `I - he/she`, `I - you`) into speakable `I to ...`
  wording in `source/tts/`
- smoothed the few model headings and schematic lists that would otherwise read
  as raw punctuation; no source-facing reader drafts or apparatus files were
  changed

TTS English filename pass:

- changed generated `source/tts/*.md` filenames to English slugs while
  preserving sequence numbers
- kept `source/reader-en/*.md` filenames in their source-oriented
  transliterated form; `source/tts/manifest.yaml` now records both the source
  reader filename and the English TTS filename
- the purpose is operational legibility for audiobook players, file browsers,
  and listening queues, not a new source-facing apparatus layer

May 6 extraction follow-up, Part I raw source check:

- added `encounters/2026-05-07-002-part-i-raw-source-check.md`
- verified the May 6 Part I extraction claims against the local Russian raw
  files for §§1-4: text functions and memory; autocommunication; rhetoric as
  meaning-generation; iconic rhetoric and theater as intermediate coding
- status is deliberately raw-OCR checked, not quotation-grade; only the §1
  creative-translation core inherits DjVu-backed support from Encounter 001
- the pass supports a narrow mechanism family: non-identical codes generate
  meaning, self-address introduces a second code, rhetoric/trope turns
  incompatibility into a generator, and iconic/theatrical mediation extends the
  pattern beyond verbal text
- no glossary, handle, or thread promotion was made; this is source-facing
  support for later checked work, especially the Hoffmeyer code-duality
  crosswalk and the separate `Культура и взрыв` dynamic-memory dossier
