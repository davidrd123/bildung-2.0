#!/usr/bin/env python3
"""
Split Récoltes et Semailles Tome I into parts following Grothendieck's sectioning.

Outputs:
  sources/french/grothendieck-recoltes-et-semailles/source/raw/NNN-slug.txt
  sources/french/grothendieck-recoltes-et-semailles/source/sections.yaml
"""

import re
import unicodedata
from pathlib import Path

SOURCE = Path("/Users/daviddickinson/Projects/Lora/bildung-2.0/sources/modern/incoming/books/Recoltes et Semailles I, II - Alexandre Grothendieck.txt")
BASE = Path("/Users/daviddickinson/Projects/Lora/bildung-2.0/sources/french/grothendieck-recoltes-et-semailles")
RAW_DIR = BASE / "source" / "raw"
SECTIONS_YAML = BASE / "source" / "sections.yaml"


# (line_number, kind, slug, title, parent_slug)
# line_number is 1-indexed, where the section STARTS
# kind: 'front'|'prelude'|'promenade'|'lettre'|'intro'|'part'|'chapter'|'section'|'notes'|'enterrement'|'back'
# Order matches body order; line numbers must be strictly increasing
SECTIONS = [
    (1,     "front",       "front-matter",                        "Front matter (title, editor's note, dedication)",          None),

    # Prelude — Mouvement I
    (64,    "prelude",     "prelude-01-mouvement-i",              "Prélude I — En guise d'avant-propos",                      None),

    # Prelude — Mouvement II : Promenade à travers une œuvre
    (135,   "prelude",     "prelude-02-mouvement-ii-promenade",   "Prélude II — Promenade à travers une œuvre",               None),
    (200,   "promenade",   "prelude-02-01-magie-des-choses",      "La magie des choses",                                      "prelude-02-mouvement-ii-promenade"),
    (230,   "promenade",   "prelude-02-02-importance-etre-seul",  "L'importance d'être seul",                                 "prelude-02-mouvement-ii-promenade"),
    (252,   "promenade",   "prelude-02-03-aventure-interieure",   "L'aventure intérieure — ou mythe et témoignage",           "prelude-02-mouvement-ii-promenade"),
    (274,   "promenade",   "prelude-02-04-tableau-de-moeurs",     "Le tableau de mœurs",                                      "prelude-02-mouvement-ii-promenade"),
    (286,   "promenade",   "prelude-02-05-heritiers-batisseur",   "Les héritiers et le bâtisseur",                            "prelude-02-mouvement-ii-promenade"),
    (310,   "promenade",   "prelude-02-06-point-de-vue-vision",   "Point de vue et vision",                                   "prelude-02-mouvement-ii-promenade"),
    (332,   "promenade",   "prelude-02-07-grande-idee",           "La « grande idée » — ou les arbres et la forêt",           "prelude-02-mouvement-ii-promenade"),
    (352,   "promenade",   "prelude-02-08-vision-douze-themes",   "La vision — ou douze thèmes pour une harmonie",            "prelude-02-mouvement-ii-promenade"),
    (376,   "promenade",   "prelude-02-09-forme-et-structure",    "Forme et structure — ou la voie des choses",               "prelude-02-mouvement-ii-promenade"),
    (396,   "promenade",   "prelude-02-10-geometrie-nouvelle",    "La géométrie nouvelle — ou les épousailles du nombre et de la grandeur", "prelude-02-mouvement-ii-promenade"),
    (418,   "promenade",   "prelude-02-11-eventail-magique",      "L'éventail magique — ou l'innocence",                      "prelude-02-mouvement-ii-promenade"),
    (438,   "promenade",   "prelude-02-12-topologie",             "La topologie — ou l'arpentage des brumes",                 "prelude-02-mouvement-ii-promenade"),
    (454,   "promenade",   "prelude-02-13-topos",                 "Les topos — ou le lit à deux places",                      "prelude-02-mouvement-ii-promenade"),
    (488,   "promenade",   "prelude-02-14-mutation-espace",       "Mutation de la notion d'espace — ou le souffle et la foi", "prelude-02-mouvement-ii-promenade"),
    (507,   "promenade",   "prelude-02-15-chevaux-du-roi",        "Tous les chevaux du roi",                                  "prelude-02-mouvement-ii-promenade"),
    (515,   "promenade",   "prelude-02-16-motifs-coeur",          "Les motifs — ou le cœur dans le cœur",                     "prelude-02-mouvement-ii-promenade"),
    (539,   "promenade",   "prelude-02-17-decouverte-mere",       "À la découverte de la Mère — ou les deux versants",        "prelude-02-mouvement-ii-promenade"),
    (569,   "promenade",   "prelude-02-18-enfant-et-mere",        "L'enfant et la Mère",                                      "prelude-02-mouvement-ii-promenade"),
    (596,   "promenade",   "prelude-02-19-epilogue-cercles",      "Épilogue : les cercles invisibles",                        "prelude-02-mouvement-ii-promenade"),
    (605,   "promenade",   "prelude-02-20-mort-est-mon-berceau",  "La mort est mon berceau",                                  "prelude-02-mouvement-ii-promenade"),
    (624,   "promenade",   "prelude-02-21-voisins-en-face",       "Coup d'œil chez les voisins d'en face",                    "prelude-02-mouvement-ii-promenade"),
    (646,   "promenade",   "prelude-02-22-unique-don-solitude",   "L'« unique » — ou le don de solitude",                     "prelude-02-mouvement-ii-promenade"),

    # Prelude — Mouvement III : Une Lettre
    (1076,  "prelude",     "prelude-03-mouvement-iii-lettre",     "Prélude III — Une lettre",                                 None),
    (1128,  "lettre",      "prelude-03-01-lettre-mille-pages",    "La lettre de mille pages",                                 "prelude-03-mouvement-iii-lettre"),
    (1164,  "lettre",      "prelude-03-03-deces-du-patron",       "Le décès du patron — chantiers à l'abandon",               "prelude-03-mouvement-iii-lettre"),
    (1189,  "lettre",      "prelude-03-04-vent-enterrement",      "Un vent d'enterrement…",                                   "prelude-03-mouvement-iii-lettre"),
    (1217,  "lettre",      "prelude-03-05-le-voyage",             "Le voyage",                                                "prelude-03-mouvement-iii-lettre"),
    (1233,  "lettre",      "prelude-03-06-versant-ombre",         "Le versant d'ombre — ou création et mépris",               "prelude-03-mouvement-iii-lettre"),
    (1255,  "lettre",      "prelude-03-07-respect-et-fortitude",  "Le respect et la fortitude",                               "prelude-03-mouvement-iii-lettre"),
    (1271,  "lettre",      "prelude-03-08-mes-proches",           "Mes « proches » — ou la connivence",                       "prelude-03-mouvement-iii-lettre"),
    (1301,  "lettre",      "prelude-03-09-depouillement",         "Le dépouillement",                                         "prelude-03-mouvement-iii-lettre"),
    (1320,  "lettre",      "prelude-03-10-quatre-vagues",         "Quatre vagues dans un mouvement",                          "prelude-03-mouvement-iii-lettre"),
    (1346,  "lettre",      "prelude-03-11-mouvement-et-structure","Mouvement et structure",                                   "prelude-03-mouvement-iii-lettre"),
    (1371,  "lettre",      "prelude-03-12-spontaneite-rigueur",   "Spontanéité et rigueur",                                   "prelude-03-mouvement-iii-lettre"),
    (1396,  "lettre",      "prelude-03-13-epilogue-postscriptum", "Épilogue en Post-scriptum — ou contexte et préalables d'un débat", "prelude-03-mouvement-iii-lettre"),
    (1405,  "lettre",      "prelude-03-14-spectrographe",         "Le spectrographe à bouteilles",                            "prelude-03-mouvement-iii-lettre"),
    (1421,  "lettre",      "prelude-03-15-trois-pieds-plat",      "Trois pieds dans un plat",                                 "prelude-03-mouvement-iii-lettre"),
    (1469,  "lettre",      "prelude-03-16-gangrene",              "La gangrène — ou l'esprit du temps (1)",                   "prelude-03-mouvement-iii-lettre"),
    (1487,  "lettre",      "prelude-03-17-amende-honorable",      "Amende honorable — ou l'esprit du temps (2)",              "prelude-03-mouvement-iii-lettre"),

    # Prelude — Mouvement IV : Introduction
    (1785,  "prelude",     "prelude-04-mouvement-iv-introduction","Prélude IV — Introduction",                                None),
    (1826,  "intro",       "prelude-04-01-reve-accomplissement",  "Rêve et accomplissement",                                  "prelude-04-mouvement-iv-introduction"),
    (1858,  "intro",       "prelude-04-02-esprit-voyage",         "L'esprit d'un voyage",                                     "prelude-04-mouvement-iv-introduction"),
    (1877,  "intro",       "prelude-04-03-boussole-bagages",      "Boussole et bagages",                                      "prelude-04-mouvement-iv-introduction"),
    (1894,  "intro",       "prelude-04-04-choses-evidentes",      "Un voyage à la poursuite des choses évidentes",            "prelude-04-mouvement-iv-introduction"),
    (1910,  "intro",       "prelude-04-05-dette-bienvenue",       "Une dette bienvenue",                                      "prelude-04-mouvement-iv-introduction"),
    (1936,  "intro",       "prelude-04-06-enterrement",           "L'Enterrement",                                            "prelude-04-mouvement-iv-introduction"),
    (1962,  "intro",       "prelude-04-07-ordonnancement",        "L'ordonnancement des obsèques",                            "prelude-04-mouvement-iv-introduction"),
    (1978,  "intro",       "prelude-04-08-fin-secret",            "La fin d'un secret",                                       "prelude-04-mouvement-iv-introduction"),
    (1999,  "intro",       "prelude-04-09-scene-acteurs",         "La scène et les acteurs",                                  "prelude-04-mouvement-iv-introduction"),
    (2009,  "intro",       "prelude-04-10-acte-de-respect",       "Un acte de respect",                                       "prelude-04-mouvement-iv-introduction"),

    # Part I : Fatuité et Renouvellement
    (2094,  "part",        "part-i-fatuite",                      "Première Partie — Fatuité et Renouvellement",              None),

    (2129,  "chapter",     "part-i-ch1-travail-et-decouverte",    "Chapitre I — Travail et découverte",                       "part-i-fatuite"),
    (2158,  "section",     "part-i-s01-enfant-bon-dieu",          "(1) L'enfant et le bon Dieu",                              "part-i-ch1-travail-et-decouverte"),
    (2182,  "section",     "part-i-s02-erreur-decouverte",        "(2) Erreur et découverte",                                 "part-i-ch1-travail-et-decouverte"),
    (2196,  "section",     "part-i-s03-inavouables-labeurs",      "(3) Les inavouables labeurs",                              "part-i-ch1-travail-et-decouverte"),
    (2218,  "section",     "part-i-s04-infaillibilite-mepris",    "(4) Infaillibilité (des autres) et mépris (de soi)",       "part-i-ch1-travail-et-decouverte"),

    (2236,  "chapter",     "part-i-ch2-reve-et-reveur",           "Chapitre II — Le rêve et le Rêveur",                       "part-i-fatuite"),
    (2262,  "section",     "part-i-s05-reve-interdit",            "(5) Le rêve interdit",                                     "part-i-ch2-reve-et-reveur"),
    (2284,  "section",     "part-i-s06-le-reveur",                "(6) Le Rêveur",                                            "part-i-ch2-reve-et-reveur"),
    (2299,  "section",     "part-i-s07-heritage-galois",          "(7) L'héritage de Galois",                                 "part-i-ch2-reve-et-reveur"),
    (2319,  "section",     "part-i-s08-reve-et-demonstration",    "(8) Rêve et démonstration",                                "part-i-ch2-reve-et-reveur"),

    (2335,  "chapter",     "part-i-ch3-naissance-crainte",        "Chapitre III — Naissance de la crainte",                   "part-i-fatuite"),
    (2361,  "section",     "part-i-s09-etranger-bienvenu",        "(9) L'étranger bienvenu",                                  "part-i-ch3-naissance-crainte"),
    (2383,  "section",     "part-i-s10-communaute-mathematique",  "(10) La « communauté mathématique » : fiction et réalité", "part-i-ch3-naissance-crainte"),
    (2405,  "section",     "part-i-s11-chevalley",                "(11) Rencontre avec Claude Chevalley — ou liberté et bons sentiments", "part-i-ch3-naissance-crainte"),
    (2425,  "section",     "part-i-s12-merite-et-mepris",         "(12) Le mérite et le mépris",                              "part-i-ch3-naissance-crainte"),
    (2447,  "section",     "part-i-s13-force-et-epaisseur",       "(13) Force et épaisseur",                                  "part-i-ch3-naissance-crainte"),
    (2473,  "section",     "part-i-s14-naissance-de-la-crainte",  "(14) Naissance de la crainte",                             "part-i-ch3-naissance-crainte"),
    (2487,  "section",     "part-i-s15-recoltes-et-semailles",    "(15) Récoltes et semailles",                               "part-i-ch3-naissance-crainte"),

    (2505,  "chapter",     "part-i-ch4-double-visage",            "Chapitre IV — Le double visage",                           "part-i-fatuite"),
    (2535,  "section",     "part-i-s16-marais-et-premiers-rangs", "(16) Marais et premiers rangs",                            "part-i-ch4-double-visage"),
    (2549,  "section",     "part-i-s17-terry-mirkil",             "(17) Terry Mirkil",                                        "part-i-ch4-double-visage"),
    (2565,  "section",     "part-i-s18-vingt-ans-fatuite",        "(18) Vingt ans de fatuité — ou l'ami infatigable",         "part-i-ch4-double-visage"),
    (2575,  "section",     "part-i-s19-monde-sans-amour",         "(19) Le monde sans amour",                                 "part-i-ch4-double-visage"),
    (2597,  "section",     "part-i-s20-monde-sans-conflit",       "(20) Un monde sans conflit ?",                             "part-i-ch4-double-visage"),
    (2625,  "section",     "part-i-s21-polichinelle",             "(21) Un secret de Polichinelle bien gardé",                "part-i-ch4-double-visage"),
    (2636,  "section",     "part-i-s22-bourbaki",                 "(22) Bourbaki, ou ma grande chance — et son revers",       "part-i-ch4-double-visage"),
    (2656,  "section",     "part-i-s23-de-profundis",             "(23) De Profundis",                                        "part-i-ch4-double-visage"),
    (2672,  "section",     "part-i-s24-mes-adieux",               "(24) Mes adieux — ou les étrangers",                       "part-i-ch4-double-visage"),

    (2720,  "chapter",     "part-i-ch5-maitre-et-eleves",         "Chapitre V — Maître et élèves",                            "part-i-fatuite"),
    (2748,  "section",     "part-i-s25-eleve-et-programme",       "(25) L'élève et le programme",                             "part-i-ch5-maitre-et-eleves"),
    (2768,  "section",     "part-i-s26-rigueur-et-rigueur",       "(26) Rigueur et rigueur",                                  "part-i-ch5-maitre-et-eleves"),
    (2782,  "section",     "part-i-s27-bavure",                   "(27) La bavure — ou vingt ans après",                      "part-i-ch5-maitre-et-eleves"),
    (2796,  "section",     "part-i-s28-recolte-inachevee",        "(28) La récolte inachevée",                                "part-i-ch5-maitre-et-eleves"),
    (2810,  "section",     "part-i-s29-pere-ennemi-1",            "(29) Le Père ennemi (1)",                                  "part-i-ch5-maitre-et-eleves"),
    (2834,  "section",     "part-i-s30-pere-ennemi-2",            "(30) Le Père ennemi (2)",                                  "part-i-ch5-maitre-et-eleves"),
    (2846,  "section",     "part-i-s31-pouvoir-decourager",       "(31) Le pouvoir de décourager",                            "part-i-ch5-maitre-et-eleves"),
    (2875,  "section",     "part-i-s32-ethique-mathematicien",    "(32) L'éthique du mathématicien",                          "part-i-ch5-maitre-et-eleves"),

    (2897,  "chapter",     "part-i-ch6-recoltes",                 "Chapitre VI — Récoltes",                                   "part-i-fatuite"),
    (2927,  "section",     "part-i-s33-note-nouvelle-ethique",    "(33) La note — ou la nouvelle éthique",                    "part-i-ch6-recoltes"),
    (2945,  "section",     "part-i-s34-limon-et-source",          "(34) Le limon et la source",                               "part-i-ch6-recoltes"),
    (2965,  "section",     "part-i-s35-mes-passions",             "(35) Mes passions",                                        "part-i-ch6-recoltes"),
    (2993,  "section",     "part-i-s36-desir-et-meditation",      "(36) Désir et méditation",                                 "part-i-ch6-recoltes"),
    (3015,  "section",     "part-i-s37-emerveillement",           "(37) L'émerveillement",                                    "part-i-ch6-recoltes"),
    (3039,  "section",     "part-i-s38-pulsion-retour",           "(38) Pulsion de retour et renouvellement",                 "part-i-ch6-recoltes"),
    (3055,  "section",     "part-i-s39-belle-de-nuit",            "(39) Belle de nuit, belle de jour — ou les écuries d'Augias", "part-i-ch6-recoltes"),
    (3075,  "section",     "part-i-s40-mathematique-sportive",    "(40) La mathématique sportive",                            "part-i-ch6-recoltes"),
    (3107,  "section",     "part-i-s41-fini-le-manege",           "(41) Fini le manège !",                                    "part-i-ch6-recoltes"),

    (3151,  "chapter",     "part-i-ch7-enfant-samuse",            "Chapitre VII — L'enfant s'amuse",                          "part-i-fatuite"),
    (3171,  "section",     "part-i-s42-enfant",                   "(42) L'enfant",                                            "part-i-ch7-enfant-samuse"),
    (3199,  "section",     "part-i-s43-patron-trouble-fete",      "(43) Le patron trouble-fête — ou la marmite à pression",   "part-i-ch7-enfant-samuse"),
    (3217,  "section",     "part-i-s44-re-renverse-vapeur",       "(44) On re-renverse la vapeur",                            "part-i-ch7-enfant-samuse"),
    (3239,  "section",     "part-i-s45-guru-pas-guru",            "(45) Le Guru-pas-Guru — ou le cheval à trois pattes",      "part-i-ch7-enfant-samuse"),

    (3267,  "chapter",     "part-i-ch8-aventure-solitaire",       "Chapitre VIII — L'aventure solitaire",                     "part-i-fatuite"),
    (3289,  "section",     "part-i-s46-fruit-defendu",            "(46) Le fruit défendu",                                    "part-i-ch8-aventure-solitaire"),
    (3313,  "section",     "part-i-s47-aventure-solitaire",       "(47) L'aventure solitaire",                                "part-i-ch8-aventure-solitaire"),
    (3337,  "section",     "part-i-s48-don-et-accueil",           "(48) Don et accueil",                                      "part-i-ch8-aventure-solitaire"),
    (3354,  "section",     "part-i-s49-constat-division",         "(49) Constat d'une division",                              "part-i-ch8-aventure-solitaire"),
    (3372,  "section",     "part-i-s50-poids-passe",              "(50) Le poids d'un passé",                                 "part-i-ch8-aventure-solitaire"),

    # Notes pour la première partie
    (3407,  "notes",       "part-i-notes",                        "Notes pour la première partie de Récoltes et Semailles",   "part-i-fatuite"),

    # Part II : L'Enterrement (1)
    # Body structure uses lettered parts (A, B, C, D) with Roman numeral chapters (I..X).
    # Chapter headers in the body are: standalone Roman numeral, then ALL-CAPS title.
    # The "I. L'élève posthume" lines I was originally picking up were Sommaire entries,
    # not body headers; corrected via Python scan of standalone Roman numerals.
    (3970,  "part",        "part-ii-enterrement",                 "Deuxième Partie — L'Enterrement (1) — ou la robe de l'empereur de Chine", None),
    (4004,  "letter-part", "part-ii-A-heritage",                  "A — Héritage et héritier",                                 "part-ii-enterrement"),
    (4087,  "enterrement", "part-ii-ch1-eleve-posthume",          "I — L'élève posthume",                                     "part-ii-A-heritage"),
    (4133,  "enterrement", "part-ii-ch2-orphelins",               "II — Les orphelins",                                       "part-ii-A-heritage"),
    (4310,  "enterrement", "part-ii-ch3-mode",                    "III — La mode — ou la vie des hommes illustres",           "part-ii-A-heritage"),
    (4564,  "letter-part", "part-ii-B-pierre-et-motifs",          "B — Pierre et les motifs",                                 "part-ii-enterrement"),
    (4701,  "enterrement", "part-ii-ch4-motifs",                  "IV — Les motifs (enterrement d'une naissance)",            "part-ii-B-pierre-et-motifs"),
    (4837,  "enterrement", "part-ii-ch5-mon-ami-pierre",          "V — Mon ami Pierre",                                       "part-ii-B-pierre-et-motifs"),
    (5177,  "enterrement", "part-ii-ch6-retour-des-choses",       "VI — Le retour des choses — ou l'Accord Unanime",          "part-ii-B-pierre-et-motifs"),
    (5633,  "letter-part", "part-ii-C-beau-monde",                "C — Le beau monde",                                        "part-ii-enterrement"),
    (5784,  "enterrement", "part-ii-ch7-colloque",                "VII — Le colloque — ou faisceaux de Mebkhout et perversité", "part-ii-C-beau-monde"),
    (6040,  "enterrement", "part-ii-ch8-eleve-alias-patron",      "VIII — L'Élève — alias le Patron",                         "part-ii-C-beau-monde"),
    (6173,  "enterrement", "part-ii-ch9-mes-eleves",              "IX — Mes élèves",                                          "part-ii-C-beau-monde"),
    (7229,  "letter-part", "part-ii-D-enterres",                  "D — Les enterrés",                                         "part-ii-enterrement"),
    (7268,  "enterrement", "part-ii-ch10-fourgon-funebre",        "X — Le Fourgon Funèbre",                                   "part-ii-D-enterres"),

    # End matter
    (7988,  "back",        "back-matter-toc",                     "Table du tome 1 (table of contents)",                      None),
    (8720,  "back",        "back-matter-colophon",                "Colophon and publisher notes",                             None),
]


def yaml_quote(s: str) -> str:
    """Minimal YAML string quoting."""
    if "'" in s:
        # Use double quotes, escape
        return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'
    return "'" + s + "'"


def main() -> None:
    text = SOURCE.read_text(encoding="utf-8")
    lines = text.split("\n")
    n_lines = len(lines)

    # Validate monotonically increasing line numbers
    prev = 0
    for ln, *_ in SECTIONS:
        if ln <= prev:
            raise RuntimeError(f"Section line numbers must be strictly increasing: {ln} after {prev}")
        prev = ln

    RAW_DIR.mkdir(parents=True, exist_ok=True)

    # Compute section boundaries: each section runs from its start line to the
    # line before the next section (or end of file for the last one)
    boundaries = []
    for i, (line_num, kind, slug, title, parent) in enumerate(SECTIONS):
        if i + 1 < len(SECTIONS):
            end_line = SECTIONS[i + 1][0] - 1
        else:
            end_line = n_lines
        boundaries.append((line_num, end_line, kind, slug, title, parent))

    # Write section files with sequence-numbered filenames
    written = []
    for idx, (start, end, kind, slug, title, parent) in enumerate(boundaries):
        seq = f"{idx:03d}"
        filename = f"{seq}-{slug}.txt"
        out_path = RAW_DIR / filename
        # Slice by 0-indexed range
        content = "\n".join(lines[start - 1:end])
        out_path.write_text(content, encoding="utf-8")
        written.append((seq, filename, kind, slug, title, parent, start, end, end - start + 1))

    # Write sections.yaml
    with SECTIONS_YAML.open("w", encoding="utf-8") as f:
        f.write("# Récoltes et Semailles — Tome I — sections map\n")
        f.write("# Generated by tools/split_recoltes.py from the Gallimard 2021 electronic edition.\n")
        f.write("# Each entry records the split file, original line range, and hierarchical parent.\n")
        f.write("# 'kind' distinguishes structural roles:\n")
        f.write("#   front/back  = editorial matter, TOC, colophon\n")
        f.write("#   prelude     = top-level Prélude division or its Mouvement header\n")
        f.write("#   promenade   = named sub-section of Mouvement II (Promenade)\n")
        f.write("#   lettre      = named sub-section of Mouvement III (Une lettre)\n")
        f.write("#   intro       = numbered sub-section of Mouvement IV (Introduction)\n")
        f.write("#   part        = Partie header\n")
        f.write("#   chapter     = Fatuité chapter header (Roman numeral)\n")
        f.write("#   section     = Fatuité numbered section (1..50)\n")
        f.write("#   notes       = Notes pour la première partie\n")
        f.write("#   enterrement = L'Enterrement Roman-numeral chapter\n")
        f.write("\n")
        f.write("sections:\n")
        for seq, filename, kind, slug, title, parent, start, end, length in written:
            f.write(f"  - seq: {seq}\n")
            f.write(f"    file: raw/{filename}\n")
            f.write(f"    kind: {kind}\n")
            f.write(f"    slug: {slug}\n")
            f.write(f"    title: {yaml_quote(title)}\n")
            if parent:
                f.write(f"    parent: {parent}\n")
            f.write(f"    start_line: {start}\n")
            f.write(f"    end_line: {end}\n")
            f.write(f"    length: {length}\n")

    # Summary
    print(f"Wrote {len(written)} files to {RAW_DIR}")
    print(f"Wrote sections map to {SECTIONS_YAML}")
    print()
    print(f"{'seq':>4}  {'length':>6}  kind          slug")
    for seq, filename, kind, slug, title, parent, start, end, length in written:
        print(f"  {seq}  {length:6d}  {kind:12s}  {slug}")


if __name__ == "__main__":
    main()
