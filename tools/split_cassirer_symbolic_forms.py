from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = ROOT / "sources/german/cassirer-philosophie-der-symbolischen-formen/source"


# 1-based inclusive line ranges from the current pdftotext extractions.
# These are search/navigation surfaces, not verified critical text.
VOLUMES = [
    {
        "id": "psf-1",
        "title_de": "Die Sprache",
        "source": SOURCE_ROOT / "full/vol1-die-sprache.txt",
        "target_dir": SOURCE_ROOT / "vol1-die-sprache",
        "ranges": [
            ("000-front-matter-and-inhaltsuebersicht.txt", 1, 128),
            ("001-vorwort.txt", 129, 308),
            ("010-einleitung-und-problemstellung.txt", 309, 2098),
            ("020-kapitel-i-sprachproblem-in-der-geschichte-der-philosophie.txt", 2099, 4735),
            ("030-kapitel-ii-sprache-in-der-phase-des-sinnlichen-ausdrucks.txt", 4736, 5655),
            ("040-kapitel-iii-sprache-in-der-phase-des-anschaulichen-ausdrucks.txt", 5656, 9599),
            ("050-kapitel-iv-sprache-als-ausdruck-des-begrifflichen-denkens.txt", 9600, 10710),
            ("060-kapitel-v-sprache-und-ausdruck-der-reinen-beziehungsformen.txt", 10711, 11507),
            ("900-editorischer-bericht.txt", 11508, 11671),
            ("910-abkuerzungen.txt", 11672, 11736),
            ("920-schriftenregister.txt", 11737, 12677),
            ("930-personenregister.txt", 12678, None),
        ],
    },
    {
        "id": "psf-2",
        "title_de": "Das mythische Denken",
        "source": SOURCE_ROOT / "full/vol2-das-mythische-denken.txt",
        "target_dir": SOURCE_ROOT / "vol2-das-mythische-denken",
        "ranges": [
            ("000-front-matter-and-inhaltsuebersicht.txt", 1, 158),
            ("001-vorwort.txt", 159, 439),
            ("010-einleitung-problem-einer-philosophie-der-mythologie.txt", 440, 1632),
            ("020-abschnitt-i-kapitel-i-mythisches-gegenstandsbewusstsein.txt", 1633, 3037),
            ("030-abschnitt-i-kapitel-ii-einzelkategorien-des-mythischen-denkens.txt", 3038, 3490),
            ("040-abschnitt-ii-kapitel-i-grundgegensatz.txt", 3491, 3887),
            ("050-abschnitt-ii-kapitel-ii-formenlehre-des-mythos.txt", 3888, 7051),
            ("060-abschnitt-iii-kapitel-i-ich-und-seele.txt", 7052, 7985),
            ("070-abschnitt-iii-kapitel-ii-herausbildung-des-selbstgefuehls.txt", 7986, 9967),
            ("080-abschnitt-iii-kapitel-iii-kultus-und-opfer.txt", 9968, 10579),
            ("090-abschnitt-iv-dialektik-des-mythischen-bewusstseins.txt", 10580, 11813),
            ("900-editorischer-bericht.txt", 11814, 11987),
            ("910-abkuerzungen.txt", 11988, 12064),
            ("920-schriftenregister.txt", 12065, 13000),
            ("930-personenregister.txt", 13001, None),
        ],
    },
    {
        "id": "psf-3",
        "title_de": "Phaenomenologie der Erkenntnis",
        "source": SOURCE_ROOT / "full/vol3-phaenomenologie-der-erkenntnis.txt",
        "target_dir": SOURCE_ROOT / "vol3-phaenomenologie-der-erkenntnis",
        "ranges": [
            ("000-front-matter-and-inhaltsuebersicht.txt", 1, 213),
            ("001-vorrede.txt", 214, 361),
            ("010-einleitung.txt", 362, 2039),
            ("020-teil-i-kapitel-i-subjektive-und-objektive-analyse.txt", 2040, 2568),
            ("030-teil-i-kapitel-ii-ausdrucksphaenomen-als-grundmoment-des-wahrnehmungsbewusstseins.txt", 2569, 4027),
            ("040-teil-i-kapitel-iii-ausdrucksfunktion-und-leib-seelen-problem.txt", 4028, 4511),
            ("050-teil-ii-kapitel-i-begriff-und-problem-der-repraesentation.txt", 4512, 4933),
            ("060-teil-ii-kapitel-ii-ding-und-eigenschaft.txt", 4934, 5916),
            ("070-teil-ii-kapitel-iii-raum.txt", 5917, 6775),
            ("080-teil-ii-kapitel-iv-zeitanschauung.txt", 6776, 8021),
            ("090-teil-ii-kapitel-v-symbolische-praegnanz.txt", 8022, 8571),
            ("100-teil-ii-kapitel-vi-pathologie-des-symbolbewusstseins.txt", 8572, 11826),
            ("110-teil-iii-kapitel-i-theorie-des-begriffs.txt", 11827, 13277),
            ("120-teil-iii-kapitel-ii-begriff-und-gegenstand.txt", 13278, 13809),
            ("130-teil-iii-kapitel-iii-sprache-und-wissenschaft.txt", 13810, 15036),
            ("140-teil-iii-kapitel-iv-gegenstand-der-mathematik.txt", 15037, 17144),
            ("150-teil-iii-kapitel-v-grundlagen-der-naturwissenschaftlichen-erkenntnis.txt", 17145, 20382),
            ("900-editorischer-bericht.txt", 20383, 20542),
            ("910-abkuerzungen.txt", 20543, 20600),
            ("920-schriftenregister.txt", 20601, 21626),
            ("930-personenregister.txt", 21627, None),
        ],
    },
]


def split_range(lines: list[str], start: int, end: int | None) -> str:
    start_idx = start - 1
    end_idx = len(lines) if end is None else end
    return "\n".join(lines[start_idx:end_idx]).strip() + "\n"


def main() -> None:
    for volume in VOLUMES:
        # Use newline-only splitting so the ranges match `rg -n` / `nl` output.
        # `str.splitlines()` treats form-feed page breaks as separators and
        # shifts the boundaries in these pdftotext extracts.
        lines = volume["source"].read_text(encoding="utf-8").split("\n")
        target_dir = volume["target_dir"]
        target_dir.mkdir(parents=True, exist_ok=True)

        for filename, start, end in volume["ranges"]:
            (target_dir / filename).write_text(split_range(lines, start, end), encoding="utf-8")

        print(f"{volume['id']}: wrote {len(volume['ranges'])} files to {target_dir.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
