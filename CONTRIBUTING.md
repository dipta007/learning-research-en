# How to help

Two kinds of help are most useful: fixing a translation that says the wrong thing, and fixing a translation that is technically right but hard to read.

## Ground rules

1. **Meaning first.** If a choice is between smooth English and the author's actual point, keep the point.
2. **Do not add.** No new advice, no extra examples, no opinions of our own. If a line needs context for a reader outside China, put it in a footnote marked `Translator's note`, never in the body.
3. **Do not cut.** If a passage is hard to translate, translate it and open an issue. Silence loses information.
4. **Plain language.** Most readers of the English version will not be native English speakers. Short sentences. One idea per sentence. Common words.
5. **Keep terms stable.** Use [GLOSSARY.md](./GLOSSARY.md). If a term is missing, add a row in the same pull request.

## File layout

One translated file per source file. Same name, same order, so a reader can compare side by side.

```
en/getting-started-in-research.md   <- getting_started_in_research.md
bn/getting-started-in-research.md   <- getting_started_in_research.md
```

Each translated file starts with a short header giving the source file and the commit of the original it was translated from. That way a reader can tell when a translation has gone stale.

## Bengali specifics

- Keep technical terms in English inside the Bengali text when that is what researchers actually say (for example `baseline`, `ablation`, `rebuttal`). Forcing a Bengali coinage nobody uses makes the text harder, not easier.
- **Names stay as names.** Do not put people, documents, books, courses, or venues into Bengali script. A reader who cannot search for the thing cannot find it. Write `Bill Freeman`, `GAMES101`, `CVPR`, and keep a document's title in its own language. A short Bengali gloss in brackets after the title is fine when the title alone is opaque.
- Give the English term in brackets the first time a Bengali term is used.
- Aim for the register of a senior student explaining something to a junior, not a textbook.

## Review

Every translation needs a second pair of eyes before merge: someone who reads Chinese for accuracy, or a native Bengali speaker for the Bengali files. Say in the pull request which check you want.
