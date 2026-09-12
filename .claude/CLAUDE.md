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
8. **Other authors' text is cited, not reprinted.** See the section below. This governed roughly two thirds of the first page translated, so it is not an edge case.

## Other authors' work inside his pages

Large parts of his pages are not his writing. The `%% 例子:` lines in his LaTeX templates are verbatim sentences and whole paragraphs lifted from published papers (Neural Body, deep snake, ManhattanSDF, DreamBooth and others). One entire sub-page is the sentence-by-sentence draft of a published paper. Some figures are pages scanned out of books.

His permission covers his notes. It cannot cover those authors' work. So:

- **Translate all of his own prose and all of his scaffolding in full.** The LaTeX comment structure is his, and his comments inside it get translated.
- **For each borrowed passage, say what the slot does and name the source.** For example: `%% Example: Neural Body (Peng et al., CVPR 2021) states its key idea in one line, integrating observations over video frames.` The instructional point of those lines is *where to look and what shape the sentence takes*, which survives citation intact.
- **Never reprint the paragraph.** Do not paraphrase it closely either; that is the same reproduction with extra steps.
- **If you cannot identify the paper confidently, describe the slot without naming one.** Do not guess an author. A wrong citation is worse than none, and this has already happened once: two different Bill Freeman documents were conflated.
- Say what you did in the page's `Translator's note`, so a reader knows why the examples are citations and where to read them.

An already-English document needs no translation at all. Mark it `(in English)` and link it.

## Layout

| Source | Translation |
|---|---|
| `README.md` | `en/readme.md` |
| `getting_started_in_research.md` | `en/getting-started-in-research.md` |
| `getting_advanced_in_research.md` | `en/getting-advanced-in-research.md` |
| `changelog` | `en/changelog.md` |
| a Notion page | `notion/<slug>/README.md` |

Notion sub-pages become sub-directories of their parent, mirroring his nesting. Figures live in `notion/<slug>/assets/`.

### One page, one translation, keyed by page id

His Notion is a graph, not a tree. Pages cross-link each other, so a naive walk writes the same page once per parent that reaches it. A single crawl produced 60 source files for 40 real pages, with one page duplicated five times.

- **Deduplicate by Notion page id, never by title or path.** He has same-titled pages with different ids, and identical pages reachable by different paths.
- Each page gets **exactly one** translated file, at one canonical path. The shallowest path wins; on a tie, use the parent that links it most prominently.
- Everywhere else that reaches it, **link to that one file** rather than translating it again. A duplicate translation is worse than a link: the copies drift, and a reader cannot tell which is current.
- Before translating a source file, check whether its page id already has a translation. If it does, add the link and stop.

### Scope: keep anything touching research learning

Anything connected to learning or doing research stays in, even loosely. His talk notes, paper notes, book notes, pipeline summaries and technical study notes all count, because they show how he reads and thinks, which is the point of the collection.

The bar for leaving something out is high: it must have nothing to do with research learning at all, like a personal homepage or bio page. When unsure, translate it. Anything genuinely out goes in `notion/not-translated.md` with a link to the original, never dropped silently.

Every translated file starts with an HTML comment header holding `source`, `source commit` or `source fetched`, and `status`. A stale translation is only detectable if that header is accurate.

Directly under the H1, every translated file carries one line pointing at its original:

```
> [Original Article](https://pengsida.notion.site/<page-id>)
```

Use the page id of the page you actually translated, which is the one in `.notion-cache/manifest.json`. He sometimes has two pages with the same title and different ids, so the id he links to elsewhere is not always the one you fetched.

His pages repeat a `文档汇总（GitHub Repo）` line on nearly every page. Drop it. The original-article line above replaces it, and repeating one URL on every page is noise. This is a deliberate exception to "never cut", and the only one.

## How to link a Notion document

Keep the author's original link, then add ours in brackets. The original is the source of truth; ours is the convenience.

```
[A paper writing template](https://pengsida.notion.site/c1a2...) ([translated](../notion/paper-writing-template/README.md))
[How to make slides for an academic talk](https://pengsida.notion.site/slid...) (not done)
```

Three markers, and every link to one of his documents carries exactly one:

| Marker | When |
|---|---|
| `([translated](./path/README.md))` | a translation exists here |
| `(not done)` | his document, not translated yet |
| `(in English)` | already in English, so there is nothing to translate |

Never leave a bare link that implies a translation exists. Check the language before writing `(in English)`: download the file and look. The languages in this repo were established with `pdftotext`, not guessed.

## Figures

Figures carry real content in his notes, so losing them loses the point of the document.

1. Download them with the fetch tool. Notion serves images through its image proxy, so they arrive as PNGs.
2. Redraw diagrams in English. Read the PNG, rebuild it, keep the same structure and reading order. The `drawio` skill is the usual tool. This applies to real diagrams, like the writing plan diagram. Screenshots of a tool's output, such as his Copilot and GPT session captures, are used directly with no redraw: there is nothing in them worth reconstructing.
3. **Prefer Mermaid or a markdown table over a redrawn image.** His flowcharts and trees became Mermaid blocks, and his review checklist became a markdown table. Both render on GitHub, stay diffable in git, and cost nothing to correct later. Reach for an image only when the figure is genuinely pictorial.
4. Keep the original beside the redraw and link it, crediting him on the redraw, so a reviewer can check your work.
5. If a figure cannot be redrawn, embed the original and write an English caption under it. Never delete it and never leave it unmentioned.
6. **A figure that is a scan or screenshot of someone else's publication is cited, not embedded.** Several of his figures are pages photographed out of books and other people's talk slides. His permission does not cover those authors' work, so name the source precisely enough to find it (book, chapter, page; or talk title) and say what the figure shows. This is the one case where a figure legitimately does not appear in the translation.

Some attachments (`.drawio`, `.pdf`) are not downloadable anonymously: Notion returns an HTML page instead of the bytes. The fetch tool writes an HTML comment where that happens. Leave the comment in the source and note it in the pull request.

## Fetching the Chinese source

```
python3 tools/notion_fetch.py <notion-page-id> --out .notion-cache --depth 3
```

Writes `.notion-cache/<slug>/source.md`, its assets, and a manifest. `.notion-cache/` is gitignored on purpose: **never commit the Chinese source.** This repository holds translations and its own notes, nothing else.

### Always sanity-check a fetch before translating from it

The fetcher has silently lost content three separate times. Each bug looked like a clean fetch. Run these every time:

```bash
# figures: unique references must equal files actually downloaded
grep -o '\./assets/[^)]*' .notion-cache/<slug>/source.md | sort -u | wc -l
ls .notion-cache/<slug>/assets | wc -l

# inline links: if this is 0 on a page full of cross-references, links were dropped
grep -c '\[[^]]*\](http' .notion-cache/<slug>/source.md
```

The three bugs, so you recognise a recurrence:

1. Assets were named by filename, and he reuses `image.png` across many blocks, so figures overwrote each other. Fixed by prefixing the block id.
2. A short block-id prefix still collided, because Notion gives blocks created in one batch the same leading hex. Fixed by using the full id. Before this, 15 figures on one page collapsed into 2 files.
3. Inline links live in the rich-text annotation array, not the text, so every link he wrote inside prose was dropped. 33 on one page. Fixed in `seg_text`.

**Never estimate a page's size from a shallow fetch.** Content sits inside collapsed toggles that need deep per-block fetching. One page measured 1,376 characters shallow and 36,092 deep, a 26x undercount.

### Finding pages he has added

`tools/notion_fetch.py` follows child-page blocks. It does not follow pages he links only inline, and several pages are reachable only that way. To find them:

```bash
python3 tools/notion_map.py --depth 3
```

Anything new and on-topic gets translated. Anything that is his personal study notes goes in `notion/not-translated.md` with a link, not translated.

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

Fix everything it marks `contradicted` or `missing` before committing. Then set the file header to `status: verified by fable, <date>`. If the check did not run, the header must say `status: unverified`. Never claim a verification that did not happen. If you fix things *after* a pass, the pass no longer covers the file: either re-run it or set the status back.

**Batch it.** One agent given seven source-and-output pairs died on a 429 rate limit partway through. Three or four short pages per agent works; a long page gets its own.

**This step is not a formality.** On every page it has run, it found real defects: a meaning inversion, a dropped negation that reversed a rejection criterion, an invented rating scale, five invented sentences, two false claims about the source, eight dropped citations, and a fabricated citation that conflated two different papers by the same author. Assume your first pass has errors of this kind, because every previous one did.

## Mistakes that keep recurring

These are the error types verification has caught more than once in this repository's own translations. Check for them before you commit, not after.

1. **A "cited" claim with no citation.** Twice, a figure was replaced with the words "cited rather than copied in" while no link appeared anywhere. The content was simply lost, and the file asserted otherwise. If you replace a figure with a citation, the link must sit next to the claim. If there is no public link, say so plainly and summarise what the figure shows.
2. **Translator additions dressed as his content.** A remark of mine used his `> **note**` convention and read as his. Another added "Prof." to a page that never says it. Every insertion goes in a clearly-labelled translator's note or an italic `*Translator's note: ...*`, never his note format, and never an unlabelled fact such as a name or title. The `(in English)` / `(not done)` / `([translated])` link markers are the exception: those are this repository's own convention, documented above.
3. **Hedge strength drifts both ways.** `容易` became "easier", adding a comparative the source lacks. `大概率` became "at all likely", weakening it. `比较好地` became "well", dropping the hedge. Translate each hedge at its exact strength; if the source has no comparative, the English gets none.
4. **An ambiguous English idiom for a blunt Chinese one.** `基本完蛋` rendered as "basically finished", which can be read as "basically done", the opposite of doomed. For a negative idiom pick a word with only one reading.
5. **A substituted URL with no author-side source.** Internal `./page/source.md` links have to become public URLs. One substituted page id appeared in no author-written file, only in another of our translations, which is not evidence. Find the id in a source the author wrote, or record it as unconfirmed in the metadata comment.
6. **The same term rendered two ways on one page.** `精神内耗` was "wearing yourself out mentally" in one cell and "mental exhaustion" in the tutorial title beside it, breaking the link a reader needs. Pick one rendering per term and use `GLOSSARY.md`.
7. **Dropped parenthetical glosses.** `（解题能力）` was dropped in three places while a sibling page kept it, leaving the set inconsistent. His parentheses are content.

## Update on every change

1. The status table in the root `README.md`.
2. `GLOSSARY.md`, if the change introduced a term.
3. Any `(not done)` marker that is now done.

## Rights

No license file covers the translated content, because the ideas are not ours. Do not add one. Anything genuinely original here (the scripts in `tools/`) can be licensed separately and explicitly.
