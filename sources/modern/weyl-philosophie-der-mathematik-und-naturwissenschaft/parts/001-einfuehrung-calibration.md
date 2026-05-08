# Part 001: Einführung Calibration

Calibration batch for Weyl's sentence strategy, source-status discipline, and
opening vocabulary.

## Scope

- `Einführung`
- printed page `15`
- PDF/page-image page `16`

## Source Anchors

- `source/cleaned/007-intro.txt`
- `source/page-images/jpg-200/page-0016.jpg`

## Source Status

The cleaned German text for this page was checked directly against the page
image. No source correction was needed in the active passage.

## German

```text
[[pdf-page:0016 printed-page:15]]

Einführung

Über einige wichtige philosophische Resultate und Gesichtspunkte,
welche sich hauptsächlich aus der Arbeit der Mathematik und Naturwissenschaft selbst ergeben haben, soll in den beiden Teilen dieses Artikels berichtet werden. Auf die Verknüpfung mit den großen Philosophemen der Vergangenheit werde ich hinweisen, wo sie mir fühlbar
geworden ist. Die belegenden Beispiele werde ich so einfach wie möglich
wählen; prinzipiell muß aber daran festgehalten werden, daß die Beschäftigung mit der Philosophie der Wissenschaften die Kenntnis der
Wissenschaften selber voraussetzt.

Der hier befolgte Gang in der Darstellung der Grundlagen der
Mathematik wird von der Oberfläche in die Tiefe führen, das mehr
Formale der inhaltlichen Problematik des Unendlichen vorausgehen
lassen. Die sorgfältige formale Vorbereitung und die strenge Erfassung
dieser natürlich von je her lebendigen und zum Ausdruck gelangten
Problematik ist erst ein Werk der jüngsten Zeit. Von den Heroen der
Philosophie besaß vor allen Leibniz den Blick für das Wesen des Mathematischen; Mathematik ist als organischer und bedeutsamer Bestandteil
seinem philosophischen Systeme eingefügt.
```

## Draft

```text
Introduction

The two parts of this article will report on several important philosophical
results and points of view that have emerged chiefly from the work of
mathematics and natural science themselves. I will point to the connection with
the great philosophemes of the past wherever it has become palpable to me. I
will choose the supporting examples as simply as possible; but as a matter of
principle it must be held fast that engagement with the philosophy of the
sciences presupposes knowledge of the sciences themselves.

The course followed here in presenting the foundations of mathematics will lead
from the surface into the depth, letting the more formal precede the substantive
problematic of the infinite. The careful formal preparation and the strict grasp
of this problematic, which has of course always been alive and has found
expression, is only a work of the most recent period. Among the heroes of
philosophy, Leibniz above all possessed the eye for the essence of the
mathematical; mathematics is inserted into his philosophical system as an
organic and significant component.
```

## Notes

- `Philosophie der Wissenschaften` is kept as `philosophy of the sciences`.
  This is less idiomatic than `philosophy of science`, but it preserves Weyl's
  plural and the passage's demand that one know the sciences themselves.
- `Philosophemen` is rendered as `philosophemes` for now. It is ugly but
  precise; `doctrines` or `themes` may be smoother in a reader-facing layer.
- `fühlbar geworden` becomes `has become palpable to me`, preserving Weyl's
  modest evidential stance: he will mark connections where he has felt them,
  not force a historical system.
- `das Mathematische` is rendered as `the mathematical`, with `essence` already
  present from `Wesen`. Flattening it to `mathematics` would lose the nominalized
  pressure.
- The page establishes a useful warning for future work: Weyl wants simple
  examples, but not simplified prerequisites.

## Next Batch Candidate

The next natural unit is chapter I, subsection 1:

- `I. Mathematische Logik. Axiomatik`
- `1. Relationen und ihre Verknüpfung. Struktur der Urteile`
- printed pages `16-21`
- PDF/page-image pages `17-22`

This should be treated as a real first batch, not merely calibration, because it
introduces Weyl's relation-based correction of traditional subject-predicate
logic and the first active notation risks.
