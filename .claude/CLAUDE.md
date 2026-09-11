# CLAUDE.md

This repository is an English translation of https://github.com/pengsida/learning_research (Chinese) and of the Notion documents that repository links to.

The job here is translation, not authoring. That single fact decides most questions.

Rights are settled. Do not re-open the licensing question, do not add a license file, and do not write anything about how the rights were arranged. NOTICE.md is the whole public position.

## Rules for translated files

1. **Meaning over style.** If smooth English and the author's actual point conflict, keep the point.
2. **Never add.** No new advice, no extra examples, no opinions. A reader who needs context gets a footnote marked `Translator's note`, never a line in the body. Our own commentary belongs in the root `README.md`.
3. **Never cut.** Translate the hard passage and flag it in the pull request. Skipping loses information silently.
4. **Never drop a figure.** See the figures section below.
5. **Plain language.** Most readers are not native English speakers. Short sentences, one idea each, common words.
6. **Terms come from GLOSSARY.md.** Missing term? Add the row in the same change. Do not change an existing row without an issue.
7. **Names stay as names.** People, documents, books, courses, and venues keep their original form, so a reader can search for them. A short English gloss in brackets after an opaque title is fine.

## Layout

| Source | Translation |
|---|---|
| `README.md` | `en/readme.md` |
| `getting_started_in_research.md` | `en/getting-started-in-research.md` |
| `getting_advanced_in_research.md` | `en/getting-advanced-in-research.md` |
| `changelog` | `en/changelog.md` |
| a Notion page | `notion/<slug>/README.md` |

Notion sub-pages become sub-directories of their parent, mirroring his nesting. Figures live in `notion/<slug>/assets/`.

Every translated file starts with an HTML comment header holding `source`, `source commit` or `source fetched`, and `status`. A stale translation is only detectable if that header is accurate.

## How to link a Notion document

Keep the author's original link, then add ours in brackets. The original is the source of truth; ours is the convenience.

```
[A paper writing template](https://pengsida.notion.site/c1a2...) ([translated](../notion/paper-writing-template/README.md))
[How to make slides for an academic talk](https://pengsida.notion.site/slid...) (not done)
```

Write `(not done)` for anything not yet translated. Never leave a bare link that implies a translation exists.

## Figures

Figures carry real content in his notes, so losing them loses the point of the document.

1. Download them with the fetch tool. Notion serves images through its image proxy, so they arrive as PNGs.
2. Redraw diagrams in English. Read the PNG, rebuild it, keep the same structure and reading order. The `drawio` skill is the usual tool. This applies to real diagrams, like the writing plan diagram. Screenshots of a tool's output, such as his Copilot and GPT session captures, are used directly with no redraw: there is nothing in them worth reconstructing.
3. Keep the original beside the redrawn version, named `*-original.png`, so a reviewer can check the redraw.
4. If a figure cannot be redrawn, embed the original and write an English caption under it. Never delete it and never leave it unmentioned.
5. **A figure that is a scan or screenshot of someone else's publication is cited, not embedded.** Several of his figures are pages photographed out of books and other people's talk slides. His permission does not cover those authors' work, so name the source precisely enough to find it (book, chapter, page; or talk title) and say what the figure shows. This is the one case where a figure legitimately does not appear in the translation.

Some attachments (`.drawio`, `.pdf`) are not downloadable anonymously: Notion returns an HTML page instead of the bytes. The fetch tool writes an HTML comment where that happens. Leave the comment in the source and note it in the pull request.

## Fetching the Chinese source

```
python3 tools/notion_fetch.py <notion-page-id> --out .notion-cache --depth 3
```

Writes `.notion-cache/<slug>/source.md`, its assets, and a manifest. `.notion-cache/` is gitignored on purpose: **never commit the Chinese source.** This repository holds translations and its own notes, nothing else.

## Verify every translation with a fresh subagent

A translation is not done until a second model has checked it against the source.

After finishing any translated file, dispatch a subagent with the Agent tool:

- `model: "fable"`.
- A **fresh** agent, so omit `subagent_type` or use `general-purpose`. **Never use `subagent_type: "fork"`.** A fork inherits the context that wrote the translation and will agree with itself, which is no check at all.
- Give it two paths, the Chinese source and the English output, and nothing else. Do not summarise what you intended, because that leads the verifier.

Ask it to report, section by section:

- each claim as `supported`, `contradicted`, or `missing`
- any English sentence with no counterpart in the source, which breaks rule 2
- any figure present in the source but absent from the translation

Fix everything it marks `contradicted` or `missing` before committing. Then set the file header to `status: verified by fable, <date>`. If the check did not run, the header must say `status: unverified`. Never claim a verification that did not happen.

## Update on every change

1. The status table in the root `README.md`.
2. `GLOSSARY.md`, if the change introduced a term.
3. Any `(not done)` marker that is now done.

## Rights

No license file covers the translated content, because the ideas are not ours. Do not add one. Anything genuinely original here (the scripts in `tools/`) can be licensed separately and explicitly.
