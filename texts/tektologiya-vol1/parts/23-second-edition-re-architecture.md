# Part 23: Second-Edition Re-Architecture (front.08 ¶1-4a)

The opening of `front.08` is one of the most valuable retrospective documents in the whole subproject. It tells us, in plain authorial prose, that the architecture of the current work is not simply the one with which the project began. Bogdanov says the first exposition had proceeded along the line of least resistance rather than of greatest logical sequence, that it required reworking, and that the present arrangement reflects that later rethinking.

## Why This Batch

- `front.08 ¶1` says the present edition is a reworked architecture based on the later `Essays in Organizational Science`, not a mere reprint of the first arrangement.
- `front.08 ¶2` states the central architectural revision directly: the formative mechanism is now placed before the regulating one, and a general sketch comes before detailed investigation.
- `front.08 ¶3` records a small but important terminological cleanup: `conjugational sum` is replaced by `analytic sum`, while `copulation` is dropped as unnecessary.
- `front.08 ¶4a` says the new third part on crises and organizational dialectic completes the exposition of the general theory, while special applied works are still to come.

## front.08 - Preface to the Second Edition

### Passage A (front.08 ¶1-2)

**Russian (lightly normalized from the FB2)**

```text
Те годы, которые прошли со времени первого издания, принесли немало нового материала; в работе оформились и некоторые новые выводы, а старым удалось придать больше точности, хотя по существу ни от чего сколько-нибудь важного отказываться пока не приходилось. Всего менее удовлетворительным казался мне сам порядок изложения, который первоначально шел по линии, так сказать, наименьших сопротивлений, начиная с того, что было наиболее подготовлено предыдущим развитием науки, и переходя к менее привычным концепциям, а не по линии наибольшей логической последовательности. Нужна была переработка. Она была намечена и частью выполнена в ряде журнальных статей «Очерки организационной науки» (журнал «Пролетарская культура». 1919–1921 № 7—20). Но по редакционным условиям пришлось значительно сократить материал. В нынешнем издании взята за основу архитектура «Очерков», но включен по возможности весь прежний материал и частью новый — к сожалению, далеко не весь, какой накопился: не позволила ограниченность времени и сил, а откладывать не приходилось, первое издание стало библиографической редкостью, даже журнал с «Очерками» мало кому из интересующихся удавалось достать.

Главное изменение в архитектуре работы сводится к тому, что формирующий механизм поставлен впереди регулирующего, как это логически и должно быть; кроме того, дан сначала общий очерк обоих механизмов, а потом уже более подробное исследование.
```

**Draft**

```text
The years that have passed since the first edition have brought a good deal of new material. Some new conclusions have taken shape in the work, and older ones have been given greater precision, though in substance there has so far been no need to abandon anything at all important. What seemed to me least satisfactory was the very order of exposition, which originally proceeded, so to speak, along the line of least resistance, beginning with what had been most prepared by the previous development of science and passing on to less familiar conceptions, rather than along the line of greatest logical sequence. A reworking was needed. It was planned, and partly carried out, in a series of journal articles, `Essays in Organizational Science` (the journal `Proletarian Culture`, 1919-1921, nos. 7-20). But editorial conditions forced a considerable reduction of the material. In the present edition the architecture of the `Essays` has been taken as the basis, while the whole earlier material and some new material have been included as far as possible, unfortunately far from all that had accumulated: the limitation of time and strength did not allow it, and there was no point in delaying, since the first edition had become a bibliographical rarity and even the journal with the `Essays` was difficult for many interested readers to obtain.

The main change in the architecture of the work comes down to this: the formative mechanism has been placed before the regulating mechanism, as logically it should be; moreover, a general sketch of both mechanisms is given first, and only afterward a more detailed investigation.
```

### Passage B (front.08 ¶3)

**Russian (lightly normalized from the FB2)**

```text
Есть небольшая перемена в терминологии. Выражение «конъюгационная сумма», недостаточно соответствовавшее идее сложения активностей, мысленно выделенных анализом из целого комплекса, заменено выражением «аналитическая сумма», более точным. Термин «копуляция» устранен как не вполне необходимый и т. п.
```

**Draft**

```text
There is a small change in terminology. The expression `conjugational sum`, which did not correspond sufficiently well to the idea of adding activities mentally distinguished by analysis from a whole complex, has been replaced by the expression `analytic sum`, which is more exact. The term `copulation` has been removed as not entirely necessary, and so forth.
```

### Passage C (front.08 ¶4a)

**Russian (lightly normalized from the FB2; source breaks after the last sentence)**

```text
Третья, новая часть работы охватывает учение о кризисах и организационную диалектику. Этим завершается изложение общей организационной теории, поскольку она успела для меня выясниться. Дальше должны последовать специальные работы по приложению этой теории к отдельным областям науки, которые ей предстоит глубоко преобразовать. Две такие работы, относящиеся одна к социальным наукам, другая к психологии, мною уже в значительной мере подготовлены. Первая из них даже отчасти опубликована.
```

**Draft**

```text
The third, new part of the work embraces the doctrine of crises and organizational dialectic. With this the exposition of general organizational theory is completed, insofar as it has thus far become clear to me. What should follow are special works on the application of this theory to particular fields of science, which it is destined profoundly to transform. Two such works, one belonging to the social sciences and the other to psychology, have already been prepared by me to a considerable extent. The first of them has even been published in part.
```

## Notes

- `front.08` gives explicit authorial evidence for how the present work should be read: not as an untouched sequence, but as a later reorganization toward logical order.
- The most important architectural statement is exact and simple: formative before regulating, overview before detail. That directly clarifies the current volume's opening shape.
- The terminological note matters because it retrospectively settles a live local issue. `Analytic sum` is not just our convenient English choice; it is the author's own later correction against the earlier `conjugational sum`.
- The removal of `copulation` also helps explain why some earlier vocabulary now reads historically rather than systematically.
- The opening of paragraph `4` matters even though the source breaks later in the paragraph. It shows that the addition of crises and organizational dialectic is what, for Bogdanov, completes the general theory before special applications begin.
- The available FB2/YAML witness is damaged immediately after the final sentence quoted in Passage `C`, so this batch stops at the last fully recoverable point rather than smoothing over the break.

## Next Move

Continue within `front.08` after the source break, because the later clean paragraphs still matter: Bogdanov turns to applied tektological work, changed historical timeliness, and the finally realized appearance of co-workers.
