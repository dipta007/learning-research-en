# How to help

Two kinds of help are most useful: fixing a translation that says the wrong thing, and fixing a translation that is technically right but hard to read.

## Ground rules

1. **Meaning first.** If a choice is between smooth English and the author's actual point, keep the point.
2. **Do not add.** No new advice, no extra examples, no opinions of our own. If a line needs context for a reader outside China, put it in a footnote marked `Translator's note`, never in the body.
3. **Do not cut.** If a passage is hard to translate, translate it and open an issue. Silence loses information.
4. **Plain language.** Most readers will not be native English speakers. Short sentences. One idea per sentence. Common words.
5. **Keep terms stable.** Use [GLOSSARY.md](./GLOSSARY.md). If a term is missing, add a row in the same pull request.
6. **Names stay as names.** People, documents, books, courses, and venues keep their original form, so a reader can search for them. A short English gloss in brackets after an opaque title is fine.

## File layout

One translated file per source file. Same order, so a reader can compare side by side.

```
en/getting-started-in-research.md   <- getting_started_in_research.md
```

Each translated file starts with a short header giving the source file and the commit of the original it was translated from. That way a reader can tell when a translation has gone stale.

## Review

Every translation needs a second pair of eyes before merge: someone who reads Chinese, checking it against the original. Say in the pull request what you want checked.
