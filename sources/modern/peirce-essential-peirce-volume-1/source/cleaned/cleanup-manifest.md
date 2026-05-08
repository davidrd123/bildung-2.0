# Essential Peirce Volume 1 Cleanup Manifest

- PDF authority: `sources/modern/incoming/books/peirce/The Essential Peirce, Volume 1 Selected Philosophical.pdf`
- Extraction: `pdftotext -raw` per page, then section splitting by observed PDF ranges.
- Page markers: printed roman and arabic pages are preserved as `[page N]`; unnumbered front matter uses `[pdf page NNN]`.
- PDF page offset: printed page 1 begins at PDF page 45, so printed arabic page = PDF page - 44.
- Image proofing: page images are generated outside git under `/tmp/peirce_ep1_pages/`.
- Status: this is a clean source scaffold, not a critical edition and not a live Peirce encounter campaign.

| seq | cleaned file | PDF pages | printed pages | page markers | suspicious OCR items |
| ---: | --- | ---: | --- | ---: | ---: |
| 0 | `cleaned/000-title-pages-and-publisher-matter.txt` | 1-8 | - | 6 | 3 |
| 1 | `cleaned/001-chronology.txt` | 9-10 | ix-x | 2 | 0 |
| 2 | `cleaned/002-foreword.txt` | 11-17 | xi-xvii | 7 | 3 |
| 3 | `cleaned/003-introduction.txt` | 19-41 | xix-xli | 23 | 10 |
| 10 | `cleaned/010-on-a-new-list-of-categories-1867.txt` | 45-54 | 1-10 | 10 | 29 |
| 11 | `cleaned/011-questions-concerning-certain-faculties-claimed-for-man-1868.txt` | 55-71 | 11-27 | 17 | 33 |
| 12 | `cleaned/012-some-consequences-of-four-incapacities-1868.txt` | 72-99 | 28-55 | 28 | 86 |
| 13 | `cleaned/013-grounds-of-validity-of-the-laws-of-logic-1869.txt` | 100-126 | 56-82 | 27 | 136 |
| 14 | `cleaned/014-frasers-the-works-of-george-berkeley-1871.txt` | 127-149 | 83-105 | 23 | 25 |
| 15 | `cleaned/015-on-a-new-class-of-observations-suggested-by-the-principles-of-logic-1877.txt` | 150-152 | 106-108 | 3 | 11 |
| 16 | `cleaned/016-the-fixation-of-belief-1877.txt` | 153-167 | 109-123 | 15 | 36 |
| 17 | `cleaned/017-how-to-make-our-ideas-clear-1878.txt` | 168-185 | 124-141 | 18 | 72 |
| 18 | `cleaned/018-the-doctrine-of-chances-1878.txt` | 186-198 | 142-154 | 13 | 53 |
| 19 | `cleaned/019-the-probability-of-induction-1878.txt` | 199-213 | 155-169 | 15 | 21 |
| 20 | `cleaned/020-the-order-of-nature-1878.txt` | 214-229 | 170-185 | 16 | 31 |
| 21 | `cleaned/021-deduction-induction-and-hypothesis-1878.txt` | 230-243 | 186-199 | 14 | 25 |
| 22 | `cleaned/022-from-on-the-algebra-of-logic-1880.txt` | 244-253 | 200-209 | 10 | 91 |
| 23 | `cleaned/023-introductory-lecture-on-the-study-of-logic-1882.txt` | 254-258 | 210-214 | 5 | 25 |
| 24 | `cleaned/024-design-and-chance-1883-84.txt` | 259-268 | 215-224 | 10 | 54 |
| 25 | `cleaned/025-from-on-the-algebra-of-logic-a-contribution-to-the-philosophy-of-notation-1885.txt` | 269-272 | 225-228 | 4 | 21 |
| 26 | `cleaned/026-an-american-plato-review-of-royces-religious-aspect-of-philosophy-1885.txt` | 273-285 | 229-241 | 13 | 68 |
| 27 | `cleaned/027-one-two-three-kantian-categories-1886.txt` | 286-288 | 242-244 | 3 | 3 |
| 28 | `cleaned/028-a-guess-at-the-riddle-1887-88.txt` | 289-323 | 245-279 | 35 | 120 |
| 29 | `cleaned/029-trichotomie-1888.txt` | 324-328 | 280-284 | 5 | 14 |
| 30 | `cleaned/030-the-architecture-of-theories-1891.txt` | 329-341 | 285-297 | 13 | 45 |
| 31 | `cleaned/031-the-doctrine-of-necessity-examined-1892.txt` | 342-355 | 298-311 | 14 | 56 |
| 32 | `cleaned/032-the-law-of-mind-1892.txt` | 356-377 | 312-333 | 22 | 89 |
| 33 | `cleaned/033-mans-glassy-essence-1892.txt` | 378-395 | 334-351 | 18 | 39 |
| 34 | `cleaned/034-evolutionary-love-1893.txt` | 396-416 | 352-372 | 20 | 76 |
| 50 | `cleaned/050-notes.txt` | 417-432 | 373-388 | 16 | 19 |
| 51 | `cleaned/051-index.txt` | 433-443 | 389-399 | 11 | 3 |
