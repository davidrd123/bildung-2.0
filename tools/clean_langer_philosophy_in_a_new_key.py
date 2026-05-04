#!/usr/bin/env python3

from __future__ import annotations

import re
import subprocess
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "sources/modern/langer-philosophy-in-a-new-key/source"
RAW_DIR = SOURCE_DIR / "raw"
CLEANED_DIR = SOURCE_DIR / "cleaned"
PDF_AUTHORITY = ROOT / (
    "sources/modern/incoming/books/Philosophy in a New Key, Suzanne K. Langer.pdf"
)
PDF_TEXT = Path("/tmp/pnk_langer_pdf_text.txt")
PDF_INDEX_LAYOUT_TEXT = Path("/tmp/pnk_langer_pdf_index_layout.txt")


@dataclass(frozen=True)
class Section:
    seq: int
    slug: str
    title: str
    file: str
    start: str | None
    end: str | None
    source: str = "pdf"


SECTIONS = [
    Section(
        0,
        "title-pages-and-publisher-matter",
        "Title pages and publisher matter",
        "000-title-pages-and-publisher-matter.txt",
        "About This Book",
        "CONTENTS",
    ),
    Section(
        1,
        "preface-to-the-second-edition",
        "Preface to the Second Edition",
        "001-preface-to-the-second-edition.txt",
        None,
        None,
        source="raw-witness-only",
    ),
    Section(
        2,
        "preface-to-the-first-edition",
        "Preface",
        "002-preface-to-the-first-edition.txt",
        "PREFACE",
        "1.\n\nThe New Key",
    ),
    Section(
        3,
        "contents",
        "Contents",
        "003-contents.txt",
        "CONTENTS",
        "PREFACE",
    ),
    Section(10, "the-new-key", "1. The New Key", "010-the-new-key.txt", "1.\n\nThe New Key", "2.\n\nSymbolic Transformation"),
    Section(11, "symbolic-transformation", "2. Symbolic Transformation", "011-symbolic-transformation.txt", "2.\n\nSymbolic Transformation", "3.\n\nThe Logic of Signs and Symbols"),
    Section(12, "the-logic-of-signs-and-symbols", "3. The Logic of Signs and Symbols", "012-the-logic-of-signs-and-symbols.txt", "3.\n\nThe Logic of Signs and Symbols", "4.\n\nDiscursive and Presentational Forms"),
    Section(13, "discursive-forms-and-presentational-forms", "4. Discursive and Presentational Forms", "013-discursive-forms-and-presentational-forms.txt", "4.\n\nDiscursive and Presentational Forms", "5.\n\nLanguage"),
    Section(14, "language", "5. Language", "014-language.txt", "5.\n\nLanguage", "6.\n\nLife-Symbols: The Roots of Sacrament"),
    Section(15, "life-symbols-the-roots-of-sacrament", "6. Life-Symbols: The Roots of Sacrament", "015-life-symbols-the-roots-of-sacrament.txt", "6.\n\nLife-Symbols: The Roots of Sacrament", "7.\n\nLife-Symbols: The Roots of Myth"),
    Section(16, "life-symbols-the-roots-of-myth", "7. Life-Symbols: The Roots of Myth", "016-life-symbols-the-roots-of-myth.txt", "7.\n\nLife-Symbols: The Roots of Myth", "8.\n\nOn Significance in Music"),
    Section(17, "on-significance-in-music", "8. On Significance in Music", "017-on-significance-in-music.txt", "8.\n\nOn Significance in Music", "9.\n\nThe Genesis of Artistic Import"),
    Section(18, "the-genesis-of-artistic-import", "9. The Genesis of Artistic Import", "018-the-genesis-of-artistic-import.txt", "9.\n\nThe Genesis of Artistic Import", "10.\n\nThe Fabric of Meaning"),
    Section(19, "the-fabric-of-meaning", "10. The Fabric of Meaning", "019-the-fabric-of-meaning.txt", "10.\n\nThe Fabric of Meaning", "ACKNOWLEDGMENTS"),
    Section(30, "acknowledgments", "Acknowledgments and Suggested Reading", "030-acknowledgments.txt", "ACKNOWLEDGMENTS", "INDEX\nabstraction"),
    Section(31, "index", "Index", "031-index.txt", "INDEX\nabstraction", None),
]


KEEP_HYPHEN_PREFIXES = {
    "cross",
    "code",
    "fact",
    "form",
    "grammar",
    "language",
    "life",
    "mind",
    "neo",
    "non",
    "one",
    "pseudo",
    "self",
    "sense",
    "sign",
    "space",
    "symbol",
    "time",
    "word",
    "world",
}


OCR_REPLACEMENTS = {
    "Tract at us Logico-Philosophicus": "Tractatus Logico-Philosophicus",
    "Tfactatus Logico-Philosophicus": "Tractatus Logico-Philosophicus",
    "The Harizon of Experience": "The Horizon of Experience",
    "EVERY ACE": "EVERY AGE",
    "rtself": "itself",
    "out day": "our day",
    "requires tvery philosophical problem": "requires every philosophical problem",
    "access'ble": "accessible",
    "projectabiliry": "projectability",
    "discursive projectabiliry": "discursive projectability",
    "sphere-of subjective": "sphere of subjective",
    "PliH»Kphy": "Philosophy",
    "the tide of Professor": "the title of Professor",
    "The tide of Professor": "The title of Professor",
    "fust how": "Just how",
    "minrl": "mind",
    "index m the mind": "index of the mind",
    "they arc involved": "they are involved",
    "place fij words": "place of words",
    "sentient lifer": "sentient life?",
    "symbollci": "symbolic",
    "P'eeling": "Feeling",
    "Itid.": "Ibid.",
    "Tract at us": "Tractatus",
    "Gesta.lt": "Gestalt",
    "Life-Symbols.- The Roots of Myth": "Life-Symbols: The Roots of Myth",
    "/.\n\nLanguage": "5.\n\nLanguage",
    "I.\n\nThe New Key": "1.\n\nThe New Key",
    "9\n\nThe Genesis of Artistic Import": "9.\n\nThe Genesis of Artistic Import",
    "10\n\nThe Fabric of Meaning": "10.\n\nThe Fabric of Meaning",
    "somone": "someone",
    "nomrtistic": "nonartistic",
    "subiective": "subjective",
    "freauently": "frequently",
    "Affektenlebre": "Affektenlehre",
    "Musikal'uch-Sckdnen": "Musikalisch-Schönen",
    "Passages Mom": "Passages from",
    "Harizon": "Horizon",
    "Out of of these": "Out of these",
    "different langi*agesr    >": "different languages.",
    "areas of fight and shade": "areas of light and shade",
    "e.g..": "e.g.,",
    "oneto-one": "one-to-one",
    "Uie power": "the power",
    "this m?tter": "this matter",
    "names lor relations": "names for relations",
    "ear'ier": "earlier",
    "\"prrjection\"": "\"projection\"",
    "G<?.rta//-psychologists": "Gestalt-psychologists",
    "open to Verstand. and": "open to Verstand, and",
    "medium and meanlog bcg:tn": "medium and meaning began",
    "Verttandfsformen": "Verstandesformen",
    "were lumper!": "were lumped",
    "\"sietalogjcal\"": "\"metalogical\"",
    "sentient life? 1 May not": "sentient life? May not",
    "deforming) symbolic is itself": "deforming) symbol15 is itself",
    "deafand-dumb": "deaf-and-dumb",
    "deafmutes": "deaf-mutes",
    "appreciationcorrespond": "appreciation—correspond",
    "meaningsituations": "meaning-situations",
    "Association lor": "Association for",
    "Untenuchungen iiber die Gnndfragen lies Sprachlebem": "Untersuchungen iiber die Grundfragen des Sprachlebens",
    "Halle a/s.": "Halle a/S.",
    "languagemaking": "language-making",
    "socalled": "so-called",
    "wilder; \"ss": "wilderness",
    "precocious eftc v<; or": "precocious efforts, or",
    "1920.n": "1920.11",
    "Language, though nor• Ibid.": "Language, though normally learned in infancy without any compulsion or formal training, is none the less a product of sheer learning, an art handed down from generation to generation, and where there is no teacher there is no accomplishment. Ibid.",
    "open repeated": "often repeated",
    "symbolseeking": "symbol-seeking",
    "maybe so": "may be so",
    "Pubi:*hing Co., 1925J": "Publishing Co., 1925)",
    "rrpn hv": "rain by",
    "nre ntes": "are rites",
    "dov/npour": "downpour",
    "\"Die entwick'nngspsychologische The' rie der Zai'berei.\"": "\"Die entwicklungspsychologische Theorie der Zauberei.\"",
    "Arch'-v liir gesammte Psychologic, XCVIII H937)": "Archiv fiir gesammte Psychologie, XCVIII (1937)",
    "p\"ssib'e": "possible",
    "activi'y": "activity",
    "extinctrn": "extinction",
    "ritual lv": "ritually",
    "acqmisition": "acquisition",
    "Hke a drama": "like a drama",
    "The Principles oj Religious Ceremonial": "The Principles of Religious Ceremonial",
    "Prolegomena to the Study oj Creek Religion": "Prolegomena to the Study of Greek Religion",
    "major>defecty": "major defects",
    "fig'-ire": "figure",
    "Language p. 4 2 8": "Language, p. 428",
    "syr\"bol-rnon-Tering": "symbol-mongering",
    "whi-h": "which",
    "no linger": "no longer",
    "imssin-tivc": "imaginative",
    "thit 'Vegetative\"": "that \"vegetative\"",
    "in^ rporated": "incorporated",
    "brm^ing": "bringing",
    "hum^n": "human",
    "formerl": "formed",
    "concT0tion": "conception",
    "h u m a n": "human",
    "arvmal": "animal",
    "ftmile Durkhe'm": "Emile Durkheim",
    "Durkhe'm": "Durkheim",
    "(ttudy": "study",
    "elimentaires": "elementaires",
    "worsh'O": "worship",
    "itseli": "itself",
    "emb'em": "emblem",
    "vis'ble": "visible",
    "w'thont": "without",
    "w'th": "with",
    "oowers": "powers",
    "D'asia": "Diasia",
    "anneasing": "appeasing",
    "aporoach": "approach",
    "Demetet": "Demeter",
    "nemeter": "Demeter",
    "imaginarv": "imaginary",
    "Me'Kchios": "Meilichios",
    "DifS'a": "Diasia",
    "hvbn'dsr": "hybrids;",
    "ident'fied": "identified",
    "conceot;on": "conception",
    "ob'ects": "objects",
    "objects of aboriginal worship which he found in his path.\" says": "objects of aboriginal worship which he found in his path,\" says",
    "usurped}": "usurped]",
    "H'rrisin P\">lrtimr>ta. n. *<V.": "Harrison, Prolegomena, p. 304.",
    "reoresents": "represents",
    "app'es": "apples",
    "express've": "expressive",
    "loved ob'ects": "loved objects",
    "forb ; dden": "forbidden",
    "obiects": "objects",
    "Die Philciophie der Mtisik": "Die Philosophie der Musik",
    "Stuttcart": "Stuttgart",
    "Ztitsckrilt jiir Uusikvissensckalt": "Zeitschrift fur Musikwissenschaft",
    "Lwsuase and Reality": "Language and Reality",
    "The Basis of Mutitul Pleasure": "The Basis of Musical Pleasure",
    "Welt^ejiihl": "Weltgefiihl",
    "7G Music": "76 Music",
    "TS ™ \"Versuch": "78 \"Versuch",
    "ZettscAnfl jxr Uusikicisscnichajt": "Zeitschrift fur Musikwissenschaft",
    "N'ew York": "New York",
    "Wie Borer, Wir Miisik?": "Wie Horen Wir Musik?",
    "fwherefore": "(wherefore",
    "»ny": "any",
    "subtle thru nobody": "subtle that nobody",
    "duplir-tes": "duplicates",
    "The Practice ol Philosophy": "The Practice of Philosophy",
    "Karl BCcher": "Karl Bucher",
    "Rhytkmus": "Rhythmus",
    "1S96": "1896",
    "WiHiam Wallace": "William Wallace",
    "Threshold o/ Mu:ic": "Threshold of Music",
    "BUcher": "Bucher",
    "p. 380.L Cf.": "p. 380. Cf.",
    "Xow,": "Now,",
    "Wfsen dfr ^tt^sik": "Wesen der Musik",
    "A Philosophical Studv of Language": "A Philosophical Study of Language",
    "re?.ctnn": "reaction",
    "steam enzine": "steam engine",
    "adv-nced": "advanced",
    "There wa> nothing": "There was nothing",
    "Vision and Drsign": "Vision and Design",
    "h^ve": "have",
    "embro'dery": "embroidery",
    "pract'cal": "practical",
    "N'ow": "Now",
    "a»d": "and",
    "»nd": "and",
    "th^n": "than",
    "th«": "the",
    "w^uld": "would",
    "by'significance": "by significance",
    "H'na": "Hina",
    "Ha'e": "Hale",
    "MAUl'S": "MAUI'S",
    "character^": "character",
    "fairy'ale": "fairy-tale",
    "h^me": "home",
    "mi'es": "miles",
    "quite'as": "quite as",
    "st'll": "still",
    "th'nk": "think",
    "unempin'cal": "unempirical",
    "wri'es": "writes",
    "Casoari": "Caspari",
    "Franl'Lbzt": "Franz Liszt",
    "G~ethe": "Goethe",
    "Personll'hkeit": "Personlichkeit",
    "Wha't": "What",
    "comol'cated": "complicated",
    "crit'cs": "critics",
    "dis'inction": "distinction",
    "dramat'c": "dramatic",
    "emot'ons": "emotions",
    "hes'tation": "hesitation",
    "impat'ent": "impatient",
    "imposs'b": "impossible",
    "perfect'v": "perfectly",
    "ph'losophy": "philosophy",
    "represent'": "represent",
    "sub'ective": "subjective",
    "t^ble": "table",
    "Whitehe^d": "Whitehead",
    "a'l": "all",
    "att'tude": "attitude",
    "ohyst'cal": "physical",
    "poss'b": "possible",
    "real'ty": "reality",
    "somet'mes": "sometimes",
    "trad'tion": "tradition",
    "or'entat": "orientat",
    "thi^": "this",
    "ANAXIMENKS": "ANAXIMENES",
    "CARXAP": "CARNAP",
    "AUGUSTS": "AUGUSTE",
    "DTSSERENS, CII. M.": "DISSERENS, CH. M.",
    "fee also": "see also",
    "FRECiE": "FREGE",
    "enyisagement": "envisagement",
    "CESELL": "GESELL",
    "PO1NCARE": "POINCARE",
    "HEI\\RICH": "HEINRICH",
    "V1SCHER": "VISCHER",
    "symbo'ic": "symbolic",
    "Xature": "Nature",
    "Speech ot Uonkeys": "Speech of Monkeys",
    "in totot": "in toto",
    "OrangUtoas": "Orang-Utans",
    "2J1-290": "281-290",
    "Xew York": "New York",
    "The. Mentality oj Ape;": "The Mentality of Apes",
    "trnt": "that",
    "conne-tion": "connection",
    "de-ire": "desire",
    "whi':h": "which",
    "unn'-turalness": "unnaturalness",
    "D':e. sprachphilnsopkischen Wcrke Wtikelm": "Die sprachphilosophischen Werke Wilhelm",
    "Untersuchungtn": "Untersuchungen",
    "Principles o! the Bhtory": "Principles of the History",
    "taf>a": "tapa",
    "f«'Hale": "fairytale",
    "univers-I'y d i d": "universally did",
    "1S49": "1849",
    "18S6": "1856",
    "E*ifl':;hHmvaiian": "English-Hawaiian",
    "Maon-Polynestan": "Maori-Polynesian",
    "Dictionary oj the Hawaiian": "Dictionary of the Hawaiian",
    "The divs were verv short": "The days were very short",
    "so th''n": "so thin",
    "stur-bHng I'non": "stumbling upon",
    "Wemaer": "Wernaer",
    "\"Dss aesthetische Symbol.\"": "\"Das aesthetische Symbol.\"",
    "Zeitsckrift": "Zeitschrift",
    "Symbo'.": "Symbol.\"",
    "Psyche-Analysis": "Psycho-Analysis",
    "kimn'erische": "kunstlerische",
    "Proceed'-ngs": "Proceedings",
    "Gnmdhgen": "Grundlagen",
    "Mu=rk": "Musik",
    "u'akre": "wahre",
    "dis«rtation": "dissertation",
    "Wfrkung": "Wirkung",
    "Ansickt^": "Ansicht",
    "impossible'v": "impossibly",
    "Beytr'dge": "Beytrage",
    "Aujnahme": "Aufnahme",
    "Afusik": "Musik",
    "Gr stall t'syflia'ogy": "Gestalt Psychology",
    "analoay": "analogy",
    "Gedcmkenmelodien": "Gedankenmelodien",
    "gr.ste": "geste",
    "lb:d.": "Ibid.",
    "gestalteader Attsdruck scelischen Lebcns": "gestaltender Ausdruck seelischen Lebens",
    "extern\"!": "external",
    "Beaucjuier": "Beauquier",
    "Philosophic de ht musiquc": "Philosophie de la musique",
    "already denned": "already defined",
    "irrmression": "impression",
    "psycbiscbe": "psychische",
    "wh<'ch": "which",
    "emotivevalue": "emotive-value",
    "faipossible;l;ty": "impossibility",
    "Oprr und Drama": "Oper und Drama",
    "Abhrndlung": "Abhandlung",
    "Nachahrnung": "Nachahmung",
    "\\atur": "Natur",
    "\\Ve were": "We were",
    "possible'Iities": "possibilities",
    "possible'e": "possible",
    "La Science et I'byfrotbese": "La Science et l'hypothese",
    "muste1-": "muster",
    "O932t": "(1932)",
    "be't": "belt",
    "negot'a.bly": "negotiably",
    "oJd": "old",
    " s« ": " so ",
    "Osden": "Ogden",
    "The Sense ofIbid., the Horizon": "\"The Sense of the Horizon\"; Ibid.",
    "spatio-temooral": "spatio-temporal",
    "explanatidl>": "explanation.",
    "philosophical isues": "philosophical issues",
    "readymade": "ready-made",
    "deep\" emotional": "deep emotional",
    "deeprooted": "deep-rooted",
    "amusment": "amusement",
    "be came": "became",
    "l i m i t": "limit",
    "mind ?": "mind?",
    "say —shows": "say—shows",
    "meanings— in this case": "meanings—in this case",
    "century— \"the": "century—\"the",
    "philosphy": "philosophy",
    "have a lite of its own": "have a life of its own",
    "factfinding": "fact-finding",
    "GrecoRoman": "Greco-Roman",
    "hardheaded": "hard-headed",
    "\"facts\" ?": "\"facts\"?",
    "compounds ?": "compounds?",
    "experimentation— typified": "experimentation—typified",
    "senseexperiences": "sense-experiences",
    "ail at ' once": "all at once",
    "definite.\nWeltanschauung, They": "definite Weltanschauung. They",
    "v ivifying": "vivifying",
    "reasonable - but": "reasonable—but",
    "evalution": "evaluation",
    "Ivfoof": "Moof",
    "Jaurnal ff PhUosefhy": "Journal of Philosophy",
    "ray article": "my article",
    "Untersttcbungen": "Untersuchungen",
    "Biihler": "Buhler",
    "Buhler, Sprachtheorif.": "Buhler, Sprachtheorie",
    "intellitdble": "intelligible",
    "Dk Urspriinge dtr Mctapher": "Die Ursprunge der Metapher",
    "Die Phdosophie ArMclaphorischtn": "Die Philosophie des Metaphorischen",
    "Op. f i t .": "Op. cit.",
    "Geselhchajt /«> verglcicttcnde Ifytttenjorscfiung": "Gesellschaft fur vergleichende Mythenforschung",
    "Au/gaben and 'Ziele dtr vergleichenden Uythenjorschunf": "Aufgaben und Ziele der vergleichenden Mythenforschung",
    "Lac. cit.": "Loc. cit.",
    "La genese des mythes": "La genese des mythes",
    "An ^ften": "An often",
    "psycholngie": "psychologie",
    "unmi:sical": "unmusical",
    "flrrmaia": "Hermaia",
    "Vew28 York. 1915). Pee": "New York, 1915). See",
    "AMrich": "Aldrich",
    "J. A. Huller": "J. A. Hiller",
    "Xatur": "Natur",
    "Beytr'dge zur Aujnahme der Afusik": "Beytrage zur Aufnahme der Musik",
    "experiments18": "experiments 18",
    "classifications53": "classifications 53",
    "piece.\" e9 Therefore": "piece.\" 69 Therefore",
    "M'tnt": "Metrik",
    "18;>3": "1853",
    "''\"Die Natur der Harmonik und Metrik (Leipzig, 1853).": "70 Die Natur der Harmonik und Metrik (Leipzig, 1853).",
    "Tirpandcr": "Terpander",
    "th? Future": "the Future",
    "Dtrtt-n Sr Co.": "Dutton & Co.",
    "The Meaning of Musk": "The Meaning of Music",
    "M-Or w-Hill": "McGraw-Hill",
    "Die Tonkunst m ihrem Verh\"hnis": "Die Tonkunst in ihrem Verhaltnis",
    "''\"Die \\atur der Harmonik und M'tnt (Leipzig, 18;>3).": "70 Die Natur der Harmonik und Metrik (Leipzig, 1853).",
    "soace": "space",
    "vet its ideal": "yet its ideal",
    "adult stafe": "adult stage",
    "1139": "1939",
    "Adventures oi Ideas": "Adventures of Ideas",
    "O\"ew York": "(New York",
    "permission \"f": "permission of",
    "Micmillan": "Macmillan",
    "British Journal »/ Psychology": "British Journal of Psychology",
    "real'ty": "reality",
    "orientat'on": "orientation",
    "J85ff": "185ff",
    "1S9": "159",
    "ghosts, 141, 145, 147, ISO": "ghosts, 141, 145, 147, 150",
    "<;.\\TE\\VOOD, ESTHER": "GATEWOOD, ESTHER",
    "RAXK, OTTO": "RANK, OTTO",
}


SUSPICIOUS_RE = re.compile(
    r"[A-Za-z][A-Za-z]*[~^<>\\\\][A-Za-z]*|"
    r"[A-Za-z]+['’][A-Za-z]*|"
    r"[A-Za-z]+[0-9]+[A-Za-z]*|"
    r"[A-Za-z]*(?:[Il]i|l[Il])?[»«][A-Za-z]*|"
    r"\b(?:tvery|rtself|somone|nomrtistic|projectabiliry|access'ble|subiective|freauently)\b"
)


NOTE_COLLISION_REPAIRS = [
    (
        r"equally untutored de3 Philosophy, VIII \(1933\), 31: 301-317\."
        r".*?pp\. 306-307\.\n\n\[page 4\]\n\nscendants",
        "equally untutored descendants\n\n"
        "[footnote 3] Philosophy, VIII (1933), 31: 301-317. This preliminary essay was followed by his book, The Horizon of Experience (New York: W. W. Norton & Co., 1934). See p. 301.\n"
        "[footnote 4] \"The Sense of the Horizon,\" pp. 303-304.\n"
        "[footnote 5] Ibid., pp. 306-307.\n\n"
        "[page 4]\n\n",
    ),
    (
        r"Die Philosophie der symbolischen Formen: 9 Language, Truth and Logic; l0 Symbol und Existenz der Wissen78 C\. K\. Ogden"
        r".*?10 A\. J\. Ayer \(London\. 1936\)\.\n\n\[page 17\]\n\n12\ns c h a f t ;",
        "Die Philosophie der symbolischen Formen; 9 Language, Truth and Logic; 10 Symbol und Existenz der Wissenschaft; 11\n\n"
        "[footnote 7] C. K. Ogden and I. A. Richards (London, 1923).\n"
        "[footnote 8] Ralph Munroe Eaton (Cambridge, Mass.: Harvard Univ. Press, 1925).\n"
        "[footnote 9] Ernst Cassirer, 3 vols. (Berlin, 1923, 1924, 1929).\n"
        "[footnote 10] A. J. Ayer (London, 1936).\n\n"
        "[page 17]\n\n",
    ),
    (
        r"Short Introduc5 Frank Lorimer\. The Growth of Reason .*?\[page 27\]\n\ntion",
        "Short Introduction\n\n"
        "[footnote 5] Frank Lorimer, The Growth of Reason (New York: Harcourt, Brace & Co., 1929), pp. 76-77.\n\n"
        "[page 27]\n\n",
    ),
    (
        r"than by swas19 See also, Group Psychology and the Analysis of the Ego .*?\[page 42\]\n\ntikas",
        "than by swastikas\n\n"
        "[footnote 19] See also, Group Psychology and the Analysis of the Ego (New York: Boni & Liveright, 1922).\n\n"
        "[page 42]\n\n",
    ),
    (
        r"It is the func11\np\. 14\.\nCf\. Th\. Ribot, Essai sur I'imagination creatrice .*?\[page 59\]\n\ntion",
        "It is the function\n\n"
        "[footnote 11] Cf. Th. Ribot, Essai sur l'imagination creatrice (Paris, 1921; 1st ed. 1900), p. 14.\n\n"
        "[page 59]\n\n",
    ),
    (
        r"foreign lan18\nBertrand Russell, Philosophy .*?\[page 62\]\n\ng\.?uage",
        "foreign language\n\n"
        "[footnote 18] Bertrand Russell, Philosophy (New York: W. W. Norton & Co., 1927), p. 44.\n\n"
        "[page 62]\n\n",
    ),
    (
        r"Its conven14\nA more detailed discussion of this double function.*?\[page 63\]\n\ntional",
        "Its conventional\n\n"
        "[footnote 14] A more detailed discussion of this double function may be found in my article, \"A Logical Study of Verbs,\" The Journal of Philosophy, XXIV (1927), 5: 120-129.\n\n"
        "[page 63]\n\n",
    ),
    (
        r"The dis8\nTractatus\.\n\n\[page 67\]\n\ntinctions",
        "The distinctions\n\n"
        "[footnote 3] Tractatus.\n\n"
        "[page 67]\n\n",
    ),
    (
        r"Yerkes, Kel12 From Sapir, Article \"Language,\" p\. 159\..*?\[page 90\]\n\nlogg, and Kohler\. Gua",
        "Yerkes, Kellogg, and Kohler.\n\n"
        "[footnote 12] From Sapir, Article \"Language,\" p. 159. By permission of The Macmillan Company, publishers.\n\n"
        "[page 90]\n\n"
        "Gua",
    ),
    (
        r"It is not altogether sur18 Kohler, The Mentality of Apes .*?\[page 93\]\n\nprising",
        "It is not altogether surprising\n\n"
        "[footnote 18] Kohler, The Mentality of Apes (New York: Harcourt, Brace & Co., 1925), p. 334.\n"
        "[footnote 19] Kellogg, op. cit., p. 160.\n"
        "[footnote 20] Kohler, The Mentality of Apes, p. 99.\n\n"
        "[page 93]\n\n",
    ),
    (
        r"linguists and psychol29\nSee\n10\nSingh and Zingg.*?\[page 100\]\n\nogists",
        "linguists and psychologists\n\n"
        "[footnote 29] Singh and Zingg, op. cit., p. 103 ff.\n"
        "[footnote 30] Thus Israel Latif, speaking of the \"lalling stage\" of babyhood, says: \"Many more sounds are produced by the infant during this period than are later used, at least in its own language. . . .\" He cites Stern, Lorimer, K. C. More, Stanley Hall, Preyer, and Conradi. See \"The Physiological Basis of Linguistic Development and the Ontogeny of Meaning,\" Psychological Review, XLI (1934), 55-85, 153-176, 246-264, esp. p. 60.\n"
        "[footnote 31] See his article \"On the Intuitive Capacity of Children to Understand Spoken Language,\" British Journal of Psychology, XVI (1925-26), 53-55.\n\n"
        "[page 100]\n\n",
    ),
    (
        r"in a state47\nSee\n48\nBuhler, Sprachtheorie.*?\[page 111\]\n\nment",
        "in a statement\n\n"
        "[footnote 47] See Buhler, Sprachtheorie, chap. iii, passim.\n"
        "[footnote 48] \"Where a diacritical verbal sign is built into the action, it frequently needs no surrounding framework or other verbal indicators...\" Ibid., p. 158.\n\n"
        "[page 111]\n\n",
    ),
    (
        r"occurred with phe52 For detailed studies of motives governing.*?\[page 116\]\n\nnomenal speed",
        "occurred with phenomenal speed\n\n"
        "[footnote 52] For detailed studies of motives governing the use of metaphor, see Heinz Werner, Die Ursprunge der Metapher (1919); Hermann Paul, Principles of the History of Language (1888; German, 1880); Alfred Biese, Die Philosophie des Metaphorischen (1893).\n"
        "[footnote 53] Op. cit., p. 429.\n\n"
        "[page 116]\n\n",
    ),
    (
        r"Krappe de27 .*?\[page 159\]\n\nclares",
        "Krappe declares\n\n"
        "[footnote 26] Ibid., p. 12.\n"
        "[footnote 27] Cf. Dixon, Oceanic Mythology, pp. 26-27.\n"
        "[footnote 28] Cf. Westervelt, op. cit., p. 156.\n"
        "[footnote 29] Gesellschaft fur vergleichende Mythenforschung.\n"
        "[footnote 30] H. Lessmann, Aufgaben und Ziele der vergleichenden Mythenforschung (Leipzig, 1907-1908), p. 7.\n"
        "[footnote 31] Loc. cit.\n\n"
        "[page 159]\n\n",
    ),
    (
        r"momentary adjust1 Roger Fry has said.*?\[page 217\]\n\nment",
        "momentary adjustment\n\n"
        "[footnote 1] Roger Fry has said in this connection: \"Biologically speaking, art is a blasphemy. We were given our eyes to see things, not to look at them.\" (Vision and Design, p. 47.)\n\n"
        "[page 217]\n\n",
    ),
    (
        r"without distortion, hy11 Karl Schmidt.*?Held at Harvard University in the autumn of 1940\.\n\n",
        "without distortion, hypothesis, or interpretation\n\n"
        "[footnote 11] Karl Schmidt has discussed the scientific versus the naive conception of fact, in his article, \"The Existential Status of Facts and Laws in Physics,\" The Monist, XLIII (1933), 2: 161-172.\n"
        "[footnote 12] Held at Harvard University in the autumn of 1940.\n\n",
    ),
    (
        r"science, his15 Hugh Miller, History and Science .*?\[page 226\]\n\ntory",
        "science, history\n\n"
        "[footnote 15] Hugh Miller, History and Science (Berkeley: University of California Press, 1939), p. 30.\n\n"
        "[page 226]\n\n",
    ),
    (
        r"works to the cor11 From A\. N\. Whitehead.*?\[page 237\]\n\nruption",
        "works to the corruption\n\n"
        "[footnote 18] From A. N. Whitehead, Adventures of Ideas (New York, 1933), p. 84. (Italics mine.) By permission of The Macmillan Company, publishers.\n"
        "[footnote 19] See \"Disorders of Symbolic Thinking and Expression,\" British Journal of Psychology, XI (1920-21), part II, 179-193.\n\n"
        "[page 237]\n\n",
    ),
]


INDEX_PAGE_248 = """[page 248]

INDEX
SPAIER, A., 17n
speech, 20, 36, 55, 61, 75, 82, 84, 85, 87, 89, 93, 94, 96, 98, 102, 104, 105, 107, 115, 117, 198, 206
SPENCER, H., 13, 149n
SPINOZA, B. DE, 68, 210
SQUIRES, P. C., 99n
STEBBING, L. S., 217n
STEKEL, WILHELM, quoted, 168, 168n-169n
STERN, GUSTAV, 17n, 99n
Story, 118, 125, 137, 138, 139f, 143, 144, 146, 148, 154, 158
STOUT, G. F., 84n
STRAUSS, RICHARD, 179, 179n, 197n
structure, logical, 42, 52, 55, 63, 83, 177
  artistic, 169
  grammatical, 55, 111, 112
  musical, 169, 183, 184, 187, 192, 193, 197
  propositional, 55, 218
  sensory, 216
STUMPF, KARL, 170, 172n
sun, 146, 147, 148, 149, 150, 152, 153, 154, 155, 156, 157, 158, 159, 162, 227
supernatural, the, 147
  —being, 142, 143, 148, 151
superstition, 34, 89, 103, 132, 135, 145, 160, 219
symbol, 14, 15, 16, 17, 19, 20, 21, 22, 24, 55, 56ff, 79, 108, 120, 166, 183
  —and object, 51, 60, 61, 76
  "charged," 231f, 234
  cosmic, 147, 154, 227
  discursive, 54, 65f, 71, 77, 78, 79
  dream-, 29, 30, 120, 121
  kinds of, 34, 36, 42, 76, 116, 177, 183, 211, 212, 229
  logic of, 48, 56
  misuse of, 27
  natural, 117, 122, 131, 155, 230, 231
  non-discursive, 75, 76, 77, 163
  presentational, 79, 80, 113, 118, 155, 176, 188, 211, 229
  —situations, 43, 63
  transparency of, 61
symbolic mode, 165, 168
symbolic transformation, 34, 35, 36, 39, 80, 89, 93, 100, 103, 116, 184, 239
symbolism, mathematical, 14, 15, 190, 194
symbolization, 17, 19, 21, 33
  law of, 131
  need of, 32, 36, 37
symbols and signs, see signs
sympathy, 180, 181
symptom, 24, 46, 67, 69, 85, 93, 103, 177, 180
synaesthesia, 100
taste, 171
telephone exchange, simile of, 24, 26, 27, 28, 30, 33, 48
terms, in meaning-relation, 44-47, 52, 189
THALES, 3, 4, 5, 136
THIMME, A., 144n
THORBURN, J. M., quoted, 168n
TOLSTOI, LEO, quoted, 56n
TOMB, J. W., 99
totem, 149, 163
  —animal, 149
totemism, 133f, 135, 139
transformer, 34
TREGEAR, E., 151n
truth, 6, 8, 11, 79, 211, 215, 221, 222, 223
  and falsity, 48, 62, 213
  artistic, 74, 213, 214
  literal, 164
TYLOR, E. B., quoted, 39, 156
understanding, 20, 72, 79, 80, 81, 116, 194, 217, 228, 233, 239
  "implicit," 210
  musical, 82, 180, 183, 196, 197, 198
URBAN, WILBUR M., 17n, 70n, 131n, 212, 213; quoted, 189, 190, 190n
value, 5, 6, 61, 105, 108, 122, 123, 164
  artistic, 165, 166, 194, 201
  human, 224, 227
  practical, 221
verb, 54, 62, 63, 228
verse, 162, 200, 202
Victor, the Savage of Aveyron, 87, 97-98, 101, 126
VIERKANDT, ALFRED, quoted, 129n
VISCHER, THEODOR, 191
vocable, 61, 86, 89, 102, 111, 185
WAGNER, RICHARD, 181, 215; quoted, 179-180, 190-191
WALLACE, WILLIAM, 205; quoted, 206
WALLASCHEK, R., 206n
washing, 130, 131
WEGENER, PHILIP, 59n, 111-114
WERNAER, R. M., quoted, 166n-167n
WERTHEIMER, MAX, 73
WESTERVELT, W. D., 149n, 150n, 158n; quoted, 152-153
WHITEHEAD, A. N., 9, 10, 17n, 21, 47n, 70, 121n; quoted, 2, 220n, 235-236, 239
WHITEHEAD, GEORGE, 167n
WIERLING, GUSTAV, 192n
WILSON, HENRY, 87n
WINCKELMANN, J. J., 170
WISDOM, JOHN, 217n
WITTGENSTEIN, LUDWIG, 17, 70, 218; quoted, 63, 64, 66, 68, 221
woman, 150, 151, 155, 157, 159
word, 27, 36, 49, 50, 61, 62, 66, 73, 78, 83, 85, 95, 96, 97, 98, 99, 102, 108, 109, 110, 112, 113, 117, 185, 188, 198, 201, 229
  —order, 59, 60, 63, 65, 66
  —tones, 104
words and music, 206, 207
  disconnected—, 54, 76, 84n, 230
  portraiture of—, 77
WUNDT, WILHELM, 170
YERKES, A. W., quoted, 85
YERKES, R. M., 89; quoted, 85, 91, 96n
"""


FRONT_MATTER_000 = """About This Book

Few people today, says Susanne Langer, are born to an environment which gives them spiritual support. Even as we are conquering nature, there is "little we see in nature that is ours." We have lost our life-symbols, and our actions no longer have ritual value; this is the most disastrous hindrance to the free functioning of the human mind.

For, as Mrs. Langer observes, ". . . the human brain is constantly carrying on a process of symbolic transformation" of experience, not as a poor substitute for action, but as a basic human need. This concept of symbolic transformation strikes a "new key in philosophy." It is a new generative idea, variously reflected even in such diverse fields as psychoanalysis and symbolic logic. Within it lies the germ of a complete reorientation to life, to art, to action. By posing a whole new world of questions in this key, Mrs. Langer presents a new world-view in which the limits of language do not appear as the last limits of rational, meaningful experience, but things inaccessible to discursive language have their own forms of conception. Her examination of the logic of signs and symbols, and her account of what constitutes meaning, what characterizes symbols, forms the basis for her further elaboration of the significance of language, ritual, myth and music, and the integration of all these elements into human mentality.

Irwin Edman says: "I suspect Mrs. Langer has established a key in terms of which a good deal of philosophy these next years may be composed."

To
ALFRED NORTH WHITEHEAD
my great Teacher and Friend

Philosophy in a New Key
A Study in the Symbolism of
Reason, Rite, and Art

By SUSANNE K. LANGER

A MENTOR BOOK
Published by THE NEW AMERICAN LIBRARY

FIRST PRINTING, FEBRUARY, 1948
SECOND PRINTING, JULY, 1949
THIRD PRINTING, MARCH, 1951
FOURTH PRINTING, JULY, 1952
FIFTH PRINTING, MAY, 1953
SIXTH PRINTING, JUNE, 1954
"""


BACK_MATTER_030 = """[page 240]

ACKNOWLEDGMENTS

Passages from the following works have been quoted in this book: from The Story of My Life, by Helen Keller, by permission of Doubleday, Doran & Company; from Tractatus Logico-Philosophicus, by Ludwig Wittgenstein, The Growth of Reason, by Frank Lorimer, The Mentality of Apes, by Wolfgang Kohler, and The Tyranny of Words, by Stuart Chase, by permission of Harcourt, Brace and Company, publishers; from The Ape and The Child, by W. N. and L. A, Kellogg, by permission of McGraw-Hill Book Company, publishers; from "How Can Music Express Emotion?" by Donald N. Ferguson, reprinted by permission from the Music Teachers National Association Volume of Proceedings for 1925; from "Observations on the Mentality of Chimpanzees and Orang-Utans," by W. H. Furness, courtesy of the American Philosophical Society; from "Musical Symbolism," by Henri Prunières, by permission of The Musical Quarterly; from Philosophy and Mysticism and Logic by Bertrand Russell, courtesy of W. W. Norton and Company, publishers; from "Reason and Feeling," by J. E. Creighton, by permission of The Philosophical Review; from Gestalt Psychology, by Wolfgang Kohler, courtesy Liveright Publishing Corporation; from Oceanic Mythology, by Roland Dixon, by permission of the Marshall Jones Company; from Primitive Culture, by E. B. Tylor, courtesy of G. P. Putnam's Sons; from Speech: its Function and Development, by Grace De Laguna, by permission of the Yale University Press; from Experience and Nature, by John Dewey, Open Court Publishing Company; from Five Stages of Greek Religion, by Gilbert Murray, Columbia University Press, publisher.

My thanks are due to all these copyright holders.

I also wish to acknowledge my indebtedness to the following English publishers: to George Allen & Unwin, for passages from Language and Reality, by W. M. Urban, and Language: its Nature, Development and Origin, by Otto Jespersen; to Kegan Paul, Trench, Trubner & Company, for passages from Philosophy and Logical Syntax, by Rudolf Carnap, Communication: a Philosophical Study of Language, by Karl Britton, and Art and the Unconscious, by J. M. Thorburn; to Chatto and Windus, for some lines from Vision and Design, by Roger Fry; and to the editor of Philosophy, for quotations from "The Sense of the Horizon," by C. D. Burns.

[page 241]

SUGGESTED READING

More books are listed here than the reader is likely to find in his local bookstore or public library. Among those books listed some at least will be easily available.

CHAPTER 1

The Horizon of Experience by C. D. Burns, W. W. Norton & Co., Inc., 1934; Science and the Modern World by A. N. Whitehead, The Macmillan Co., 1925, 1946

CHAPTER 2

Skepticism and Poetry by D. G. James, (London) Allen & Unwin, Ltd., 1937; The Natural History of the Mind by A. D. Ritchie, Longmans, Green & Co., 1936; The Growth of Reason by Frank Lorimer, Harcourt, Brace & Co., Inc., 1929

CHAPTER 3

Philosophy and Logical Syntax by Rudolf Carnap, (London) Routledge & Sons, Ltd., 1935; Signs, Language, and Behavior by Charles Morris, Prentice-Hall, Inc., 1946; Our Knowledge of the External World by Bertrand Russell, W. W. Norton & Co., Inc., 1929 (esp. "Logic as the Essence of Philosophy"); Symbolism: Its Meaning and Effect by A. N. Whitehead, The Macmillan Co., 1927

CHAPTER 4

Gestalt Psychology by Wolfgang Kohler, Boni & Liveright, 1929; Art and the Unconscious by J. M. Thorburn, (London) K. Paul, Trench, Trubner & Co., 1925

CHAPTER 5

Language: Its Nature, Development and Origin by Otto Jespersen, Henry Holt & Co., 1922; The Ape and the Child by W. N. and L. A. Kellogg, McGraw-Hill Book Co., 1933; The Mentality of Apes by Wolfgang Kohler, Harcourt, Brace & Co., Inc., 1926; Language and Myth by Ernst Cassirer, Harper & Brothers, 1946; Language and Reality; the Philosophy of Language and the Principles of Symbolism by W. M. Urban, The Macmillan Co., 1939

CHAPTER 6

Prolegomena to the Study of Greek Religion by Jane Harrison, The Macmillan Co.; Five Stages of Greek Religion by Gilbert Murray, Columbia University Press, 1925; The Principles of Religious Ceremonial by W. H. Frere, Morehouse Publishing Co., 1928

CHAPTER 7

Legends of Maui, a Demigod of Polynesia, and of his Mother Hina by W. D. Westervelt; The Mind of Primitive Man by Franz Boas, The Macmillan Co., 1911; The Golden Bough by J. G. Frazer, The Macmillan Co., 1907

CHAPTER 8

A Study in Aesthetics by L. A. Reid, The Macmillan Co., 1931; Vision and Design by Roger Fry, Coward-McCann, Inc., 1924; The Meaning of Music by C. C. Pratt, McGraw-Hill Book Co., 1932; J. S. Bach by Albert Schweitzer, The Macmillan Co., 1935; Art and Artist by Otto Rank, Alfred A. Knopf, Inc., 1932; On the Beautiful in Music by Eduard Hanslick, H. W. Gray Co.; Arts and the Man by Irwin Edman, W. W. Norton & Co., Inc., 1939

CHAPTER 9

The Threshold of Music by William Wallace, The Macmillan Co., 1908; The Birth of Tragedy (in Complete Works) by Friedrich Nietzsche, The Macmillan Co., 1925; The Spirit of the Forms (V. 5, History of Art), by Elie Faure, Harper & Brothers, 1930

CHAPTER 10

Adventures of Ideas by A. N. Whitehead, The Macmillan Co., 1933

[page 242]

THE SHAPING OF THE MODERN MIND

Crane Brinton. The concluding half of Ideas and Men--a self-contained history of Western thought since the Renaissance--a brilliant summation of our past, a realistic examination of our present and a hopeful look into our future. (#M98--35c)

RECONSTRUCTION IN PHILOSOPHY

John Dewey. America's most highly regarded thinker outlines how his philosophy of experience can be integrated with contemporary life. (#M53--35c)

THE AIMS OF EDUCATION

Alfred North Whitehead. Education as an intellectual process for the students is Professor Whitehead's goal. His general theory of education is one of stimulating inquiry into parallel fields. (#M41--35c)

GREEK CIVILIZATION AND CHARACTER

Edited by Arnold J. Toynbee. A companion volume to the famous historian's Greek Historical Thought. Brilliant translations of Hellenic life-history that shed light on contemporary problems by revealing the experience of the past. (Mentor #M99--35c)

THE DEMOCRATIC WAY OF LIFE

T. V. Smith and Eduard C. Lindeman. (A new and completely revised edition.) A challenging book which examines the democratic ideal and how it works in practical application. (#M59--35c)

PATTERNS OF CULTURE

Ruth Benedict. A famous anthropologist analyzes our social structure in relation to primitive civilizations. (#M89--35c)

SCIENCE AND THE MORAL LIFE

Max C. Otto, introduction by Eduard C. Lindeman. A noted philosopher sounds a positive approach to morals in a scientific age. (#M43--35c)

THE SONG OF GOD--BHAGAVAD-GITA

Introduction by Aldous Huxley. The timeless epic of Hindu faith vividly translated for Western readers by Swami Prabhavananda and Christopher Isherwood. A unique literary experience as well as a contemporary message which touches today's urgent problems. (#M103--35c)

THE USES OF THE PAST

Herbert J. Muller. A stimulating inquiry into the civilizations of the past, how they flourished, why they fell, and the meaning they hold for the present crisis of civilization. (#M112--50c)

THE WORLD OF HISTORY

Advisory editors: Crane Brinton, Alfred Kazin and John D. Hicks. A stimulating journey through the living past, this brilliant selection of the best in contemporary historical writing extends history to its broadest limits, makes it meaningful and exciting for the reader of today. With an introduction by Allan Nevins. (#M109--35c)

TO OUR READERS: We welcome your comments about any Signet, Signet Key or Mentor Book, as well as your suggestions for new reprints. If your dealer does not have the books you want, you may order them by mail, enclosing the list price plus 5c per copy to cover mailing costs. Send for a copy of our complete catalog. The New American Library of World Literature, Inc., 501 Madison Ave., New York.
"""


def repair_index_layout(text: str) -> str:
    text = re.sub(
        r"RICHET, CH 27.*?—painting, 178, 179",
        "RICHET, CH., 27\n"
        "RIEMANN, HUGO, 174, 177, 198; quoted, 199n\n"
        "RIGNANO, EUGENIO, 22n\n"
        "RIMSKY-KORSAKOFF, N. A., 215\n"
        "RITCHIE, A. D., quoted, 21, 32\n"
        "ritual, 35, 116, 124, 127, 128, 129, 132\n"
        "  gods of, 137, 158\n"
        "  in modern society, 234f, 236, 237\n"
        "  mimetic, 125\n"
        "ROUSSEAU, J. J., 104, 174\n"
        "SOCRATES, 4, 5, 6\n"
        "song, 82, 104, 105, 106, 106n, 162, 200, 201, 206, 207\n"
        "SORANTIN, E., 188n\n"
        "sound, 95, 96, 98, 99, 100, 101, 102, 104, 105, 106, 108, 109, 164, 199, 200, 201, 205\n"
        "  —painting, 178, 179",
        text,
        flags=re.S,
    )
    return re.sub(r"\[page 248\]\n\nINDEX\n.*\Z", INDEX_PAGE_248, text, flags=re.S)


def repair_note_collisions(text: str) -> str:
    for pattern, replacement in NOTE_COLLISION_REPAIRS:
        text = re.sub(pattern, replacement, text, flags=re.S)
    text = text.replace(
        "A question is really an ambiguous\n1\n\n[page 2]\n\nproposition;",
        "A question is really an ambiguous\n\n[page 2]\n\nproposition;",
    )
    text = text.replace(
        "who are living in his day or have 1Cf. Felix Cohen. \"What is a Question?\" The Monist, XXXIX (1929), 3: 350-364.\n"
        "2\n"
        "From Chapter III: The Century of Genius. By permission of The Macmillan\n"
        "Company, publishers.\n\n"
        "[page 3]",
        "who are living in his day or have\n\n"
        "[footnote 1] Cf. Felix Cohen. \"What is a Question?\" The Monist, XXXIX (1929), 3: 350-364.\n"
        "[footnote 2] From Chapter III: The Century of Genius. By permission of The Macmillan Company, publishers.\n\n"
        "[page 3]",
    )
    text = text.replace(
        "brought a new conceptual framework, an entirely different 6 Ibid., p. 307.\n\n[page 5]\n\nperspective",
        "brought a new conceptual framework, an entirely different\n\n"
        "[footnote 6] Ibid., p. 307.\n\n"
        "[page 5]\n\n"
        "perspective",
    )
    text = re.sub(
        r"\[page 17\]\n\nThe Logical Syntax of Language; Philosophy and Logical Syntax; 13 Meaning and Change of Meaning; 14 Symbolism: its Meaning and Effects; 15 Foundations of the Theory of Signs;10 Seele als Äusserung: 1 7 La pensée concrete: essai sur le symbolisme intellectuel; 18 Zeichen, die Fundamente des Wissens; 19 and recently, Language and Reality\.20 (?P<body>.*?)\n11\nH\. Noack, Symbol und Existenz der Wissenschaft: Untersuchungen zur\nGrundlegung einer philosophischen Wissenschaftslehre \(Halle a/S\., 1936\)\. 12 Rudolf Carnap \(London, 1935; German ed\., Vienna, 1934\)\. 13 Rudolf Carnap \(London, 1935; German ed\. 1934\)\. 14 Gustav Stern \(Göteborg, 1931\)\.\n15\nA\. N\. Whitehead \(New York: The Macmillan Co\., 1927\)\.\n16\nCharles W\. Morris \(Chicago: Univ\. of Chicago Press, 1938\)\. 17 Paul Helwig \(Leipzig-Berlin, 1936\)\.\n18\nA\. Spaier \(Paris, 1 9 2 7 \) \. 19 R\. Gätschenberger \(Stuttgart\. 1932\)\. 20 Wilbur M\. Urban\. Language and Reality; the Philosophy of Language and the 21 Principles of Symbolism \(London, 1939\)\. Ludwig Wittgenstein \(London, 1922; 2nd ed\. New York: Harcourt, Brace & Co\.,22 1933\)\. Louis Grudin \(New York: Covici Friedr, 1930\)\.\n\n\[page 18\]",
        "[page 17]\n\n"
        "The Logical Syntax of Language; 12 Philosophy and Logical Syntax; 13 Meaning and Change of Meaning; 14 Symbolism: its Meaning and Effects; 15 Foundations of the Theory of Signs; 16 Seele als Äusserung; 17 La pensée concrete: essai sur le symbolisme intellectuel; 18 Zeichen, die Fundamente des Wissens; 19 and recently, Language and Reality.20 "
        r"\g<body>"
        "\n\n"
        "[footnote 11] H. Noack, Symbol und Existenz der Wissenschaft: Untersuchungen zur Grundlegung einer philosophischen Wissenschaftslehre (Halle a/S., 1936).\n"
        "[footnote 12] Rudolf Carnap (London, 1935; German ed., Vienna, 1934).\n"
        "[footnote 13] Rudolf Carnap (London, 1935; German ed. 1934).\n"
        "[footnote 14] Gustav Stern (Göteborg, 1931).\n"
        "[footnote 15] A. N. Whitehead (New York: The Macmillan Co., 1927).\n"
        "[footnote 16] Charles W. Morris (Chicago: Univ. of Chicago Press, 1938).\n"
        "[footnote 17] Paul Helwig (Leipzig-Berlin, 1936).\n"
        "[footnote 18] A. Spaier (Paris, 1927).\n"
        "[footnote 19] R. Gätschenberger (Stuttgart. 1932).\n"
        "[footnote 20] Wilbur M. Urban, Language and Reality; the Philosophy of Language and the Principles of Symbolism (London, 1939).\n"
        "[footnote 21] Ludwig Wittgenstein (London, 1922; 2nd ed. New York: Harcourt, Brace & Co., 1933).\n"
        "[footnote 22] Louis Grudin (New York: Covici Friedr, 1930).\n\n"
        "[page 18]",
        text,
        flags=re.S,
    )
    text = re.sub(
        r"\[page 17\]\n\nThe Logical Syntax of Language; Philosophy and Logical Syntax; 13 .*?Louis Grudin \(New York: Covici Friedr, 1930\)\.\n\n\[page 18\]",
        "[page 17]\n\n"
        "The Logical Syntax of Language; 12 Philosophy and Logical Syntax; 13 Meaning and Change of Meaning; 14 Symbolism: its Meaning and Effects; 15 Foundations of the Theory of Signs; 16 Seele als Äusserung; 17 La pensée concrete: essai sur le symbolisme intellectuel; 18 Zeichen, die Fundamente des Wissens; 19 and recently, Language and Reality.20 The list is not nearly exhaustive. There are many books whose titles do not betray a preoccupation with semantic, for instance Wittgenstein's Tractatus Logico-Philosophicus,21 or Grudin's A Primer of Aesthetics.22 And were we to take an inventory of articles, even on the symbolism of science alone, we would soon have a formidable bibliography. But it is not only in philosophy proper that the new keynote has been struck. There are at least two limited and technical fields, which have suddenly been developed beyond all prediction, by the discovery of the all-importance of symbol-using or symbol-reading. They are widely separate fields, and their problems and procedures do not seem to belong together in any way at all: one is modern psychology, the other modern logic. In the former we are disturbed—thrilled or irritated, according to our temperaments—by the advent of psycho-analysis. In the latter we witness the rise of a new technique known as symbolic logic. The coincidence of these two pursuits seems entirely fortuitous; one stems from medicine and the other from mathematics, and there is nothing whatever on which they would care to compare notes or hold debate. Yet I believe they both embody the same generative idea, which is to preoccupy and inspire our philosophical age: for each in its own fashion has discovered the power of symbolization. They have different conceptions of symbolism and its functions. Symbolic logic is not \"symbolic\" in the sense of Freudian psychology, and The Analysis of Dreams makes no contribution to logical syntax. The emphasis on symbolism derives from entirely different interests, in their respective\n\n"
        "[footnote 11] H. Noack, Symbol und Existenz der Wissenschaft: Untersuchungen zur Grundlegung einer philosophischen Wissenschaftslehre (Halle a/S., 1936).\n"
        "[footnote 12] Rudolf Carnap (London, 1935; German ed., Vienna, 1934).\n"
        "[footnote 13] Rudolf Carnap (London, 1935; German ed. 1934).\n"
        "[footnote 14] Gustav Stern (Göteborg, 1931).\n"
        "[footnote 15] A. N. Whitehead (New York: The Macmillan Co., 1927).\n"
        "[footnote 16] Charles W. Morris (Chicago: Univ. of Chicago Press, 1938).\n"
        "[footnote 17] Paul Helwig (Leipzig-Berlin, 1936).\n"
        "[footnote 18] A. Spaier (Paris, 1927).\n"
        "[footnote 19] R. Gätschenberger (Stuttgart. 1932).\n"
        "[footnote 20] Wilbur M. Urban, Language and Reality; the Philosophy of Language and the Principles of Symbolism (London, 1939).\n"
        "[footnote 21] Ludwig Wittgenstein (London, 1922; 2nd ed. New York: Harcourt, Brace & Co., 1933).\n"
        "[footnote 22] Louis Grudin (New York: Covici Friedr, 1930).\n\n"
        "[page 18]",
        text,
        flags=re.S,
    )
    text = text.replace(
        "The Logical Syntax of Language; Philosophy and Logical Syntax; 13 Meaning and Change of Meaning; 14 Symbolism: its Meaning and Effects; 15 Foundations of the Theory of Signs;10 Seele als Äusserung: 1 7 La pensée concrete: essai sur le symbolisme intellectuel; 18 Zeichen, die Fundamente des Wissens; 19 and recently, Language and Reality.20",
        "The Logical Syntax of Language; 12 Philosophy and Logical Syntax; 13 Meaning and Change of Meaning; 14 Symbolism: its Meaning and Effects; 15 Foundations of the Theory of Signs; 16 Seele als Äusserung; 17 La pensée concrete: essai sur le symbolisme intellectuel; 18 Zeichen, die Fundamente des Wissens; 19 and recently, Language and Reality.20",
    )
    text = re.sub(
        r"in their respective\n11\nH\. Noack, Symbol und Existenz der Wissenschaft: Untersuchungen zur\nGrundlegung einer philosophischen Wissenschaftslehre \(Halle a/S\., 1936\)\. 12 Rudolf Carnap \(London, 1935; German ed\., Vienna, 1934\)\. 13 Rudolf Carnap \(London, 1935; German ed\. 1934\)\. 14 Gustav Stern \(Göteborg, 1931\)\.\n15\nA\. N\. Whitehead \(New York: The Macmillan Co\., 1927\)\.\n16\nCharles W\. Morris \(Chicago: Univ\. of Chicago Press, 1938\)\. 17 Paul Helwig \(Leipzig-Berlin, 1936\)\.\n18\nA\. Spaier \(Paris, 1 9 2 7 \) \. 19 R\. Gätschenberger \(Stuttgart\. 1932\)\. 20 Wilbur M\. Urban\. Language and Reality; the Philosophy of Language and the 21 Principles of Symbolism \(London, 1939\)\. Ludwig Wittgenstein \(London, 1922; 2nd ed\. New York: Harcourt, Brace & Co\.,22 1933\)\. Louis Grudin \(New York: Covici Friedr, 1930\)\.",
        "in their respective\n\n"
        "[footnote 11] H. Noack, Symbol und Existenz der Wissenschaft: Untersuchungen zur Grundlegung einer philosophischen Wissenschaftslehre (Halle a/S., 1936).\n"
        "[footnote 12] Rudolf Carnap (London, 1935; German ed., Vienna, 1934).\n"
        "[footnote 13] Rudolf Carnap (London, 1935; German ed. 1934).\n"
        "[footnote 14] Gustav Stern (Göteborg, 1931).\n"
        "[footnote 15] A. N. Whitehead (New York: The Macmillan Co., 1927).\n"
        "[footnote 16] Charles W. Morris (Chicago: Univ. of Chicago Press, 1938).\n"
        "[footnote 17] Paul Helwig (Leipzig-Berlin, 1936).\n"
        "[footnote 18] A. Spaier (Paris, 1927).\n"
        "[footnote 19] R. Gätschenberger (Stuttgart. 1932).\n"
        "[footnote 20] Wilbur M. Urban, Language and Reality; the Philosophy of Language and the Principles of Symbolism (London, 1939).\n"
        "[footnote 21] Ludwig Wittgenstein (London, 1922; 2nd ed. New York: Harcourt, Brace & Co., 1933).\n"
        "[footnote 22] Louis Grudin (New York: Covici Friedr, 1930).",
        text,
        flags=re.S,
    )
    text = text.replace(
        "[page 20]\n\nA\nNEW KEY\nnot even from mathematics;",
        "[page 20]\n\nnot even from mathematics;",
    )
    text = text.replace("symbolusing", "symbol-using")
    text = text.replace("determined in part2 by", "determined in part by")
    text = re.sub(
        r"determined in part by the understanding of statements\n(?:\[footnote 2\] )?As it certainly is.*?\[page 218\]",
        "determined in part by the understanding of statements\n\n"
        "[footnote 2] As it certainly is, in the writings of Moore, Stebbing, Ramsey, Wisdom, and other British philosophers. Cf. L. S. Stebbing, \"Substances, Events, and Facts,\" The Journal of Philosophy, XXIX (1932), 12: 309-322; F. P. Ramsey and G. E. Moore, \"Symposium: Facts and Propositions,\" Proceedings of the Aristotelian Society, suppl. vol. VII (1927), 153-206; John Wisdom, \"Time, Fact, and Substance,\" ibid., N.S. XXIX (1928-29), 67-94.\n"
        "[footnote 3] Cf. Hugh Miller, \"The Dimensions of Particular Fact,\" The Journal of Philosophy, XXXVI (1939), 7: 181-188.\n"
        "[footnote 4] C. I. Lewis, \"Facts, Systems, and the Unity of the World,\" The Journal of Philosophy, XX (1923), 6: 141-151. See p. 142.\n\n"
        "[page 218]",
        text,
        flags=re.S,
    )
    text = re.sub(
        r"which is to B Karl Britton\. Communication: A Philosophical Study of Language .*?\[page 219\]\n\nrecognize",
        "which is to recognize\n\n"
        "[footnote 5] Karl Britton, Communication: A Philosophical Study of Language (New York: Harcourt, Brace & Co., 1939), pp. 204-206.\n\n"
        "[page 219]\n\n",
        text,
        flags=re.S,
    )
    text = text.replace("It is not altogether surprising\n\n[footnote 18]", "It is not altogether surprising, therefore,\n\n[footnote 18]")
    text = text.replace("[page 93]\n\n, therefore, ", "[page 93]\n\n")
    text = text.replace("occurred with phenomenal speed\n\n[footnote 52]", "occurred with phenomenal speed.\n\n[footnote 52]")
    text = text.replace("[page 116]\n\n. For", "[page 116]\n\nFor")
    text = re.sub(r"(\[page \d+\]\n\n)[ \t]+(?=[A-Za-z\"'(])", r"\1", text)
    return text


def ensure_pdf_text() -> str:
    if not PDF_AUTHORITY.exists():
        raise SystemExit(f"Missing PDF authority: {PDF_AUTHORITY}")
    subprocess.run(["pdftotext", str(PDF_AUTHORITY), str(PDF_TEXT)], check=True)
    return PDF_TEXT.read_text(encoding="utf-8", errors="replace")


def is_page_number(line: str) -> bool:
    return bool(re.fullmatch(r"\d{1,3}|[ivxlcdmIVXLCDM]+", line.strip()))


def is_running_header(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return False
    if stripped in {"ACKNOWLEDGMENTS", "INDEX", "SUGGESTED READING"}:
        return False
    letters = [c for c in stripped if c.isalpha()]
    if not letters or len(stripped) <= 5:
        return False
    upper_ratio = sum(1 for c in letters if c.isupper()) / len(letters)
    return stripped.upper() == stripped or upper_ratio >= 0.8


def is_corrupt_page_token(line: str) -> bool:
    stripped = line.strip()
    if bool(re.fullmatch(r"[A-Za-z0-9 ][A-Za-z0-9 ]{0,4}", stripped)) and any(
        c.isdigit() for c in stripped
    ):
        return True
    return bool(re.fullmatch(r"[0-9OolIbB ]{1,4}", stripped)) and any(
        c in "OolIbB" for c in stripped
    )


def is_running_header_fragment(line: str) -> bool:
    return line.strip() in {
        "THE",
        "NEW",
        "KEY",
        "PHILOSOPHY",
        "LANGUAGE",
        "LIFE-SYMBOLS:",
        "ROOTS",
        "MYTH",
        "SACRAMENT",
    }


def clean_page(page: str, expected_numeric_page: int | None = None) -> tuple[str | None, list[str]]:
    lines = [line.rstrip() for line in page.replace("\xad", "").splitlines()]
    while lines and not lines[0].strip():
        lines.pop(0)

    printed_page: str | None = None

    if expected_numeric_page is not None:
        for idx, line in enumerate(lines[:10]):
            if line.strip() == str(expected_numeric_page):
                preceding = [candidate.strip() for candidate in lines[:idx] if candidate.strip()]
                if preceding and all(
                    is_running_header(candidate) or is_running_header_fragment(candidate) or len(candidate) <= 4
                    for candidate in preceding
                ):
                    printed_page = line.strip()
                    del lines[: idx + 1]
                    break

    # Common forms: "64" + running head, or running head + "65".
    if printed_page is None and len(lines) >= 2 and is_page_number(lines[0]) and is_running_header(lines[1]):
        printed_page = lines[0].strip()
        del lines[:2]
    elif printed_page is None and len(lines) >= 2 and is_running_header(lines[0]) and is_page_number(lines[1]):
        printed_page = lines[1].strip()
        del lines[:2]
    elif printed_page is None and len(lines) >= 3 and is_page_number(lines[0]) and is_running_header(lines[2]):
        printed_page = lines[0].strip()
        del lines[:3]
    elif printed_page is None and len(lines) >= 3 and is_running_header(lines[0]) and is_page_number(lines[2]):
        printed_page = lines[2].strip()
        del lines[:3]
    elif printed_page is None and lines and is_page_number(lines[0]):
        printed_page = lines[0].strip()
        del lines[0]

    if printed_page is None and expected_numeric_page is not None and lines:
        headerish = False
        for candidate in [line.strip() for line in lines[:4] if line.strip()]:
            if is_running_header(candidate) or is_running_header_fragment(candidate) or is_corrupt_page_token(candidate):
                headerish = True
                break
        if headerish:
            printed_page = str(expected_numeric_page)
            while lines and (
                not lines[0].strip()
                or is_running_header(lines[0])
                or is_running_header_fragment(lines[0])
                or is_page_number(lines[0])
                or is_corrupt_page_token(lines[0])
            ):
                lines.pop(0)

    while lines and not lines[0].strip():
        lines.pop(0)

    return printed_page, lines


def extract_pdf_stream(pdf_text: str) -> str:
    chunks: list[str] = []
    last_numeric_page: int | None = None
    for page in pdf_text.split("\f"):
        expected = last_numeric_page + 1 if last_numeric_page is not None else None
        printed_page, lines = clean_page(page, expected)
        if (
            printed_page
            and printed_page.isdigit()
            and last_numeric_page is not None
            and int(printed_page) <= last_numeric_page
        ):
            printed_page = str(last_numeric_page + 1)
        if not lines:
            continue
        if printed_page:
            chunks.append(f"[page {printed_page}]")
            chunks.append("")
            if printed_page.isdigit():
                last_numeric_page = int(printed_page)
        chunks.extend(lines)
        chunks.append("")
    stream = "\n".join(chunks)
    for old, new in OCR_REPLACEMENTS.items():
        stream = stream.replace(old, new)
    return stream


def extract_index_layout() -> str:
    subprocess.run(
        [
            "pdftotext",
            "-layout",
            "-f",
            "250",
            "-l",
            "255",
            str(PDF_AUTHORITY),
            str(PDF_INDEX_LAYOUT_TEXT),
        ],
        check=True,
    )
    pages = [page for page in PDF_INDEX_LAYOUT_TEXT.read_text(encoding="utf-8", errors="replace").split("\f") if page.strip()]
    blocks: list[str] = []
    for offset, page in enumerate(pages[:6]):
        printed_page = 243 + offset
        lines: list[str] = []
        for raw_line in page.splitlines():
            line = raw_line.rstrip()
            stripped = line.strip()
            if not stripped and not lines:
                continue
            if stripped == "INDEX" or stripped == str(printed_page):
                continue
            if re.fullmatch(rf"{printed_page}\s+INDEX", stripped) or re.fullmatch(
                rf"INDEX\s+{printed_page}", stripped
            ):
                continue
            lines.append(line)
        while lines and not lines[-1].strip():
            lines.pop()
        block = f"[page {printed_page}]\n\nINDEX\n" + "\n".join(lines).rstrip()
        blocks.append(block)
    normalized = "\n\n".join(blocks).strip() + "\n"
    for old, new in OCR_REPLACEMENTS.items():
        normalized = normalized.replace(old, new)
    normalized = repair_index_layout(normalized).strip() + "\n"
    return normalized


def find_required(text: str, marker: str, start: int = 0) -> int:
    idx = text.find(marker, start)
    if idx == -1:
        raise SystemExit(f"Could not find marker: {marker!r}")
    return idx


def slice_section(stream: str, section: Section) -> str:
    if section.source == "raw-witness-only":
        raw = (RAW_DIR / section.file).read_text(encoding="utf-8", errors="replace")
        return normalize_section(raw, fallback_title=section.title)

    start = 0 if section.start is None else find_required(stream, section.start)
    end = len(stream) if section.end is None else find_required(stream, section.end, start + 1)
    if end <= start:
        raise SystemExit(f"Invalid section span for {section.file}")

    segment = stream[start:end]
    page_idx = stream.rfind("[page ", 0, start)
    if page_idx != -1 and not segment.startswith("[page "):
        page_end = stream.find("\n", page_idx)
        page_marker = stream[page_idx:page_end].strip()
        segment = f"{page_marker}\n\n{segment}"
    normalized = normalize_section(segment, fallback_title=section.title)
    if section.file == "013-discursive-forms-and-presentational-forms.txt":
        normalized = fill_chapter_4_pdf_gap(normalized)
    return normalized


def fill_chapter_4_pdf_gap(cleaned: str) -> str:
    if "[page 76]" in cleaned:
        return cleaned
    raw = (RAW_DIR / "013-discursive-forms-and-presentational-forms.txt").read_text(
        encoding="utf-8", errors="replace"
    )
    start = raw.find("we owe to sight and touch")
    end = raw.find("standard key for translating sculpture")
    if start == -1 or end == -1 or end <= start:
        return cleaned
    snippet = raw[start:end]
    snippet = re.sub(
        r"\n\s*DISCURSIVE AND PRESENTATIONAL FORMS\s+87\s*\n",
        "\n",
        snippet,
    )
    snippet = re.sub(
        r"\n\s*88\s+PHILOSOPHY IN A NEW KEY\s*\n",
        "\n[page 77]\n\n",
        snippet,
    )
    snippet = "[page 76]\n\n" + snippet
    snippet = normalize_section(snippet, fallback_title="PDF gap fill")
    return cleaned.replace("\n[page 78]\n\nstandard key", "\n" + snippet + "\n[page 78]\n\nstandard key")


def normalize_section(text: str, fallback_title: str) -> str:
    for old, new in OCR_REPLACEMENTS.items():
        text = text.replace(old, new)
    lines = [line.strip() for line in text.splitlines()]
    out: list[str] = []
    para = ""

    def flush() -> None:
        nonlocal para
        if para:
            out.append(para.strip())
            para = ""

    for line in lines:
        if not line:
            flush()
            continue
        if line.startswith("[page "):
            flush()
            if out and out[-1] != "":
                out.append("")
            out.append(line)
            out.append("")
            continue
        if re.fullmatch(r"\d+\.?|I\.|/\.|[A-Z][A-Za-z:;,. -]{1,70}", line) and len(line) < 80:
            flush()
            out.append(line)
            continue
        if not para:
            para = line
        elif para.endswith("-"):
            prefix = para.rsplit(None, 1)[-1][:-1].lower()
            if prefix in KEEP_HYPHEN_PREFIXES:
                para += line
            else:
                para = para[:-1] + line
        else:
            para += " " + line
    flush()

    normalized = "\n".join(out).strip() + "\n"
    normalized = re.sub(r"\n{3,}", "\n\n", normalized)
    normalized = normalized.replace("1.\n\nThe New Key", "1. The New Key")
    normalized = normalized.replace("1.\nThe New Key", "1. The New Key")
    normalized = normalized.replace("2.\n\nSymbolic Transformation", "2. Symbolic Transformation")
    normalized = normalized.replace("2.\nSymbolic Transformation", "2. Symbolic Transformation")
    normalized = normalized.replace("3.\n\nThe Logic of Signs and Symbols", "3. The Logic of Signs and Symbols")
    normalized = normalized.replace("3.\nThe Logic of Signs and Symbols", "3. The Logic of Signs and Symbols")
    normalized = normalized.replace("4.\n\nDiscursive and Presentational Forms", "4. Discursive and Presentational Forms")
    normalized = normalized.replace("4.\nDiscursive and Presentational Forms", "4. Discursive and Presentational Forms")
    normalized = normalized.replace("5.\n\nLanguage", "5. Language")
    normalized = normalized.replace("5.\nLanguage", "5. Language")
    normalized = normalized.replace("6.\n\nLife-Symbols: The Roots of Sacrament", "6. Life-Symbols: The Roots of Sacrament")
    normalized = normalized.replace("6.\nLife-Symbols: The Roots of Sacrament", "6. Life-Symbols: The Roots of Sacrament")
    normalized = normalized.replace("7.\n\nLife-Symbols: The Roots of Myth", "7. Life-Symbols: The Roots of Myth")
    normalized = normalized.replace("7.\nLife-Symbols: The Roots of Myth", "7. Life-Symbols: The Roots of Myth")
    normalized = normalized.replace("8.\n\nOn Significance in Music", "8. On Significance in Music")
    normalized = normalized.replace("8.\nOn Significance in Music", "8. On Significance in Music")
    normalized = normalized.replace("9.\n\nThe Genesis of Artistic Import", "9. The Genesis of Artistic Import")
    normalized = normalized.replace("9.\nThe Genesis of Artistic Import", "9. The Genesis of Artistic Import")
    normalized = normalized.replace("10.\n\nThe Fabric of Meaning", "10. The Fabric of Meaning")
    normalized = normalized.replace("10.\nThe Fabric of Meaning", "10. The Fabric of Meaning")
    for old, new in OCR_REPLACEMENTS.items():
        normalized = normalized.replace(old, new)
    normalized = repair_note_collisions(normalized)
    return normalized


def suspicious_items(text: str) -> list[str]:
    items = sorted(set(m.group(0) for m in SUSPICIOUS_RE.finditer(text)))
    return [item for item in items if item not in {"men's", "one's", "it's", "man's"}]


def page_gaps(text: str) -> list[tuple[int, int]]:
    nums = [int(m.group(1)) for m in re.finditer(r"^\[page (\d+)\]", text, flags=re.M)]
    return [(a, b) for a, b in zip(nums, nums[1:]) if b != a + 1]


def main() -> None:
    pdf_text = ensure_pdf_text()
    stream = extract_pdf_stream(pdf_text)
    CLEANED_DIR.mkdir(parents=True, exist_ok=True)

    manifest_lines = [
        "# Langer PNK Cleanup Manifest",
        "",
        f"- PDF authority: `{PDF_AUTHORITY.relative_to(ROOT)}`",
        "- Extraction: `pdftotext` default text layer for prose; `pdftotext -layout` for the two-column index; then local cleanup script.",
        "- Page markers: printed page numbers recovered from PDF running headers as `[page N]`.",
        "- Index note: PDF pages 250-255 are the printed index pages 243-248; badly garbled index spans on printed pages 247-248 were checked against rendered page images.",
        "- Witness mismatch: the raw scaffold has a separate second-edition preface; the current PDF does not. That one file is retained from the raw text witness and marked below.",
        "",
        "| seq | cleaned file | source | page markers | page gaps | suspicious OCR items |",
        "| ---: | --- | --- | ---: | --- | ---: |",
    ]
    uncertainty_lines = [
        "# Langer PNK OCR Uncertainties",
        "",
        "These are mechanically detected candidates after first-pass cleanup. They are not all errors; proper names, possessives, foreign titles, and index entries are expected to appear here. Items that matter for quotation should be checked against the PDF page image.",
        "",
    ]

    for section in SECTIONS:
        if section.file == "000-title-pages-and-publisher-matter.txt":
            cleaned = FRONT_MATTER_000
        elif section.file == "030-acknowledgments.txt":
            cleaned = BACK_MATTER_030
        elif section.file == "031-index.txt":
            cleaned = extract_index_layout()
        else:
            cleaned = slice_section(stream, section)
        out_path = CLEANED_DIR / section.file
        out_path.write_text(cleaned, encoding="utf-8")
        page_markers = len(re.findall(r"^\[page ", cleaned, flags=re.M))
        gaps = page_gaps(cleaned)
        susp = suspicious_items(cleaned)
        source_label = section.source
        if section.file == "013-discursive-forms-and-presentational-forms.txt":
            source_label = "pdf + raw gap fill for missing PDF pages 76-77"
        elif section.file == "000-title-pages-and-publisher-matter.txt":
            source_label = "pdf page-image proof"
        elif section.file == "030-acknowledgments.txt":
            source_label = "pdf page-image proof with inferred logical pages 240-242"
        elif section.file == "031-index.txt":
            source_label = "pdf-layout + page-image repair for index pp. 247-248"
        manifest_lines.append(
            f"| {section.seq} | `{out_path.relative_to(SOURCE_DIR)}` | {source_label} | {page_markers} | {', '.join(f'{a}->{b}' for a, b in gaps) or '-'} | {len(susp)} |"
        )
        uncertainty_lines.append(f"## {section.file}")
        uncertainty_lines.append("")
        if susp:
            shown = ", ".join(f"`{item}`" for item in susp[:120])
            if len(susp) > 120:
                shown += f", ... ({len(susp) - 120} more)"
            uncertainty_lines.append(shown)
        else:
            uncertainty_lines.append("No mechanical OCR candidates found.")
        uncertainty_lines.append("")

    (CLEANED_DIR / "cleanup-manifest.md").write_text("\n".join(manifest_lines) + "\n", encoding="utf-8")
    (CLEANED_DIR / "ocr-uncertainties.md").write_text("\n".join(uncertainty_lines) + "\n", encoding="utf-8")
    print(f"Wrote {len(SECTIONS)} cleaned files to {CLEANED_DIR}")


if __name__ == "__main__":
    main()
