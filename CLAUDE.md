# CLAUDE.md

This repository is an English translation of https://github.com/pengsida/learning_research (Chinese).

The job here is translation, not authoring. That single fact decides most questions.

Rights are settled. Do not re-open the licensing question, do not add a license file, and do not write anything about how the rights were arranged. NOTICE.md is the whole public position on this.

## Rules for translated files

1. **Meaning over style.** If smooth English and the author's actual point conflict, keep the point.
2. **Never add.** No new advice, no extra examples, no opinions. A reader outside China who needs context gets a footnote marked `Translator's note`, never a line in the body.
3. **Never cut.** Translate the hard passage and flag it in the pull request. Skipping loses information silently.
4. **Plain language.** Most readers will not be native English speakers. Short sentences, one idea each, common words.
5. **Terms come from GLOSSARY.md.** Missing term? Add the row in the same change. Do not change an existing row without an issue.
6. **Names stay as names.** People, documents, books, courses, and venues keep their original form, so a reader can search for them. A short English gloss in brackets after an opaque title is fine.

## File layout

One translated file per source file, same order as the original.

| Source | English |
|---|---|
| `README.md` | `en/readme.md` |
| `getting_started_in_research.md` | `en/getting-started-in-research.md` |
| `getting_advanced_in_research.md` | `en/getting-advanced-in-research.md` |
| `changelog` | `en/changelog.md` |

Every translated file keeps the HTML comment header at the top with `source`, `source commit`, and `status`. Fill in the real commit hash of the original you translated from. A stale translation is only detectable if that hash is there.

## Do not commit the Chinese source

Translate from the upstream repository, do not copy its files into this one. This repository holds translations and its own notes, nothing else.

## Two things to update on every translation change

1. The status table in `README.md`.
2. `GLOSSARY.md`, if the change introduced a term.

## Rights

No license file covers the translated content, because the ideas are not ours. Do not add one. Anything genuinely original in this repository (scripts, tooling) can be licensed separately and explicitly.
