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
7. **Names stay as names.** People, documents, books, courses, and venues keep their original form, so a reader can search for them. A short English gloss in brackets after an opaque title is fine. For a person, use the form in `GLOSSARY.md`: given name, family name, then the Chinese characters, the same way in every file. Use the name someone publishes under. The author is `Sida Peng`, not `Peng Sida`; his own page titles him that way, and reversing it breaks the search a reader would run.
8. **Other authors' text is cited, not reprinted.** See the section below. This governed roughly two thirds of the first page translated, so it is not an edge case.

## Other authors' work inside his pages

Large parts of his pages are not his writing. The `%% 例子:` lines in his LaTeX templates are verbatim sentences and whole paragraphs lifted from published papers (Neural Body, deep snake, ManhattanSDF, DreamBooth and others). One entire sub-page is the sentence-by-sentence draft of a published paper. Some figures are pages scanned out of books.

**The marker is not the test; the content is.** Some published-paper sentences sit on single `%` lines rather than `%%`, for example the deep snake abstract worked through as "版本3". Those are borrowed text too, and they are described and cited like any other. A verifier told only about `%%` will report every one of them as an already-English passage that should have been kept verbatim: that happened once and produced six false findings. When a line inside a LaTeX fence is a fluent English sentence from a real paper, it is borrowed, whatever marker precedes it.

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

### Scope: research-advice pages only

Translate the pages that teach how to do research: choosing a problem, running a project, reading papers, experiments, writing, figures, reviewing, rebuttals, working with an advisor, state of mind.

**Do not translate his study notes.** Those are his notes on other people's talks, interviews, books and papers. They are linked in `notion/not-translated.md` instead. They are the majority of his Notion by character count and almost none of it by use to someone learning research, and much of their substance is material he does not own.

Deciding between the two is usually easy: an advice page tells you what to do, a study note records what someone else said. When a page is genuinely both, translate the advice and cite the rest, the same as for borrowed passages inside an advice page.

Anything left out gets a row in `notion/not-translated.md` with a link to the original. Never drop a page silently.

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

- **A different model from the one that wrote the translation.** `model: "fable"` is the default choice. If fable is rate-limited, use `sonnet` instead; the guarantee that matters is independence, not any particular model. Record which model checked the file in its `status:` line.
- A **fresh** agent, so omit `subagent_type` or use `general-purpose`. **Never use `subagent_type: "fork"`.** A fork inherits the context that wrote the translation and will agree with itself, which is no check at all.
- Give it two paths, the Chinese source and the English output, and nothing else. Do not summarise what you intended, because that leads the verifier.

Ask it to report, section by section:

- each claim as `supported`, `contradicted`, or `missing`
- any English sentence with no counterpart in the source, which breaks rule 2
- any figure present in the source but absent from the translation
- **added intensifiers, contrasts, and actors.** The words that keep slipping in are "genuinely", "real", "clearly", "rather than", "instead of", and a place or person the Chinese sentence does not name, such as "in your lab". Each is small, each is plausible, and each is still an addition.
- **hedge drift in either direction**, checked against the hedge table in `GLOSSARY.md`
- **a cut alternative.** `掌握/熟悉` gives two verbs and only "master" survived. A slash in the Chinese means both halves are content.
- **a parenthetical attached to the wrong item, or widened.** `（闫令琪老师开的课）` sits on GAMES202 alone; "Both are taught by Prof. Lingqi Yan" widened it to cover GAMES101 too, which the source does not say.
- **the same Chinese word rendered two ways in one file.** `一定` was "some" in one line and "a certain amount of" four lines later.

**Tell the verifier this repository's settled conventions, or it will report them as defects.** List the `> [Original Article]` line, the three link markers, the top-of-file HTML comment block, a translated HTML comment in the body, the hedge table renderings, the name format, and an English colon standing where the Chinese has a colon. A first pass that omitted the `> [Original Article]` line reported it as added content in all four files, which is four wasted findings. Also require it to quote the Chinese for every finding; that alone kills most false positives.

Fix everything it marks `contradicted` or `missing` before committing. Then set the file header to `status: verified by fable, <date>`. If the check did not run, the header must say `status: unverified`. Never claim a verification that did not happen. If you fix things *after* a pass, the pass no longer covers the file: either re-run it or set the status back.

**Batch it.** One agent given seven source-and-output pairs died on a 429 rate limit partway through. Three or four short pages per agent works; a long page gets its own.

**This step is not a formality.** On every page it has run, it found real defects: a meaning inversion, a dropped negation that reversed a rejection criterion, an invented rating scale, five invented sentences, two false claims about the source, eight dropped citations, and a fabricated citation that conflated two different papers by the same author. Assume your first pass has errors of this kind, because every previous one did.

## Verify in a loop until the page comes back clean

**One pass is never enough.** A pass finds defects, you fix them, and the fixes are new prose that has never been checked. So verification is a loop, not a step. Run it until a round returns nothing you can act on.

The evidence, from this repository's own history:

| File set | Defects per round | Rounds to reach empty |
|---|---|---|
| `en/getting-started-in-research.md` | 9, 6, 9, 9, 6, 8, 2, 4, 4, 4, 3, 2, 0 | 13 |
| `en/readme.md` | 9, 6, 9, 9, 6, 8, 0 | 7 |
| all 32 `notion/` pages | 53, 41, 21, 28, 12, … | 5 and counting |

One pass catches roughly half. Round 4 of the `notion/` sweep found *more* than round 3 (28 against 21), because that was the first round with a particle-by-particle checklist. A low count means the check was blunt as often as it means the page is nearly clean. Never describe a page as verified on one round.

### The loop

```
round = 1
pages = every page you translated or edited
while pages is not empty and round <= 7:        # seven is a hard cap
    dispatch fresh verifier agents over pages, batched
    for each page:
        triage each finding: real, or false positive checked against the source
        apply the real ones
        if you changed the page: it stays in pages for the next round
        else: it leaves the loop, settled at this round
    commit and push this round's fixes
    round += 1

# any page still in the loop at round 7 stops there. Record its real state and
# hand it to a Chinese reader. Do not run round 8.
```

### Hard cap: seven rounds per page

**Never run more than seven rounds on a page.** If round seven is not clean, stop anyway. Record the true state and hand the page to a human who reads Chinese. Do not run round eight.

This cap comes from what the rounds actually produced here:

| Rounds | What they found |
|---|---|
| 1 to 2 | 94 defects, including a 15-line invented block, three dropped hyperlinks, and a reversed claim |
| 3 to 7 | steadily smaller, mostly one dropped particle at a time |
| 8 to 11 | about 45 defects over 15 agent runs, almost all single particles that do not change what a reader takes away |

Past seven, two things go wrong. The yield is nearly all cosmetic, and **the loop starts producing its own defects**. Round 9 read a 会 as a hedge, I applied "may have doubts", and round 11 flagged it as a weakened claim: 有些 already carried the hedge, so the fix double-hedged his sentence. Round 6 caught a "Very very important" that round 5's own fix had created. When a loop removes single particles while inserting errors of the same size, it has stopped paying.

What to do instead of round eight:

1. **Run `tools/check_renderings.py`.** It found 8 defects in pages that seven model rounds had called clean. For any enumerable defect class, write the check instead of running the round.
2. **Measure, then aim.** Round 10 was told "roughly 11 occurrences of 会 have lost their modal" rather than "look for problems", and found 16 defects after round 9 found 11. Counting beats noticing.
3. **Say the page is unfinished.** Set its `status:` to the real round count and state that the last round was not clean. An honest "6 rounds, last one found a defect" is worth more than a page that claims clean because the loop was stopped at a convenient moment.
4. **Ask for a Chinese reader.** This is the check no round replaces. One reader on the longest page for an hour will find more that matters than round eight will.

Rules that make the loop terminate instead of spinning:

- **A page leaves the loop only on a clean round.** Clean means the verifier returned nothing, or returned only findings you rejected with a reason after checking the source yourself.
- **A page you edit re-enters.** No exceptions. This is the whole point.
- **Feed each round what the last one learned.** Put every settled rendering in the verifier's prompt as a fixed-renderings list, and name the known failure modes. Otherwise round N rediscovers round N-1's category instead of finding what is left.
- **Give the verifier the settled conventions**, or it burns findings re-reporting the `> [Original Article]` line and the `<details>` toggles. See the list above.
- **Require a Chinese quote for every finding.** That one requirement kills most false positives.
- **Commit each round separately.** The history then shows what each round cost, and the work is never sitting uncommitted.
- **Stop when a round is clean, not when the count looks small.** 2 is not 0.

Record the result honestly in the `status:` line: how many rounds ran, and whether the last one was clean. `verified by sonnet, 2026-09-12. 13 passes; the last found nothing.` A page still mid-loop says so.

### Run the mechanical check before spending a round on it

Round 7 of the `notion/` sweep found nothing but one Chinese word rendered several ways in one file. A model finds those by luck, one at a time, over many rounds. A script finds them all at once:

```bash
python3 tools/check_renderings.py                        # every page
python3 tools/check_renderings.py notion/<page>/README.md
```

It reports two things, and **neither is a verdict**. Both are leads to go and read the context:

- `suspect`: a rendering that a past round got wrong is present, and so is the Chinese word it belongs to. On its first run, 8 of 15 were false positives, because a different Chinese word shares the English form: 搜集 really is "collect", 各个 is not 各种, 充分 is "fully" where 完全 is "completely", 不会 is "will not" where 无法 is "cannot", 应该没法 is not 很可能. Verify every hit against the Chinese before editing. Once verified benign, add it to `ALLOW` in the script with the reason, so the report keeps meaning something.
- `thin`: the Chinese uses a word N times and the English has its settled rendering fewer times. Weaker still. Legitimate variation is common: 可行性 reads "viability" on the minimum-viability page, 作业 reads "homework" on the coursework page, 学习了很多 reads "learned a great deal".

Two bugs in that script are worth knowing about, because both produced confident nonsense before being fixed. Substring matching made "carefully" match "fully". And stripping code fences from the English while counting the Chinese in full made every term inside his LaTeX template look dropped. If you extend the script, check its output against a page you have read.

Run it after every fix round. It is cheap, it is exhaustive over the words it knows, and it turns a defect class that took four rounds to chase into one command.

### Applying findings without introducing new defects

Both of these happened here and both would have shipped silently.

1. **Never trust an "applied" count.** A fix script reported `5/5 applied` while one substitution had matched an earlier, different occurrence and the flagged line was untouched. Re-grep the file for the intended result. The script's own tally is not proof.
2. **Never leave a placeholder in a fix script.** Two substitutions marked "checked below" were left in and executed, rewriting a sentence about lab discussions into a claim the source does not make. Both had to be reverted. Write the real target string or leave the entry out.
3. **Do not apply a fix mechanically from the glossary.** `才` is "only then" standing alone, but inside `因为...才...` it is a cleft: "it is because X that Y". The mechanical version read "It may be only because they hit some problems...", which overstates. A rule applied without judgment produces stiff, wrong English.
4. **Fixing one occurrence is not fixing the word.** When a finding names a word rendered two ways, grep every occurrence in the file and settle them all. 很大 needed four fixes, not the one that was flagged.

## Mistakes that keep recurring

These are the error types verification has caught more than once in this repository's own translations. Check for them before you commit, not after.

1. **A "cited" claim with no citation.** Twice, a figure was replaced with the words "cited rather than copied in" while no link appeared anywhere. The content was simply lost, and the file asserted otherwise. If you replace a figure with a citation, the link must sit next to the claim. If there is no public link, say so plainly and summarise what the figure shows.
2. **Translator additions dressed as his content.** A remark of mine used his `> **note**` convention and read as his. Another added "Prof." to a page that gave the name no honorific at all. That is different from rendering his 老师 or 教授 as "Prof.", which is translating an honorific he wrote and is settled in `GLOSSARY.md`. Inventing one is the mistake. Every insertion goes in a clearly-labelled translator's note or an italic `*Translator's note: ...*`, never his note format, and never an unlabelled fact such as a name or title. The `(in English)` / `(not done)` / `([translated])` link markers are the exception: those are this repository's own convention, documented above.
3. **Hedge strength drifts both ways.** `容易` became "easier", adding a comparative the source lacks. `大概率` became "at all likely", weakening it. `比较好地` became "well", dropping the hedge. `推荐` and `建议` both became bare imperatives, turning his suggestions into orders, six times in one short file. `比较好的情况` became "the better case", which reads as a comparison of two named cases rather than a relative degree. Translate each hedge at its exact strength; if the source has no comparative, the English gets none. `GLOSSARY.md` has a hedge table with the settled rendering for each one. This is the single most frequent defect found so far, so read that table before translating and check against it afterwards.
4. **An ambiguous English idiom for a blunt Chinese one.** `基本完蛋` rendered as "basically finished", which can be read as "basically done", the opposite of doomed. For a negative idiom pick a word with only one reading.
5. **A substituted URL with no author-side source.** Internal `./page/source.md` links have to become public URLs. One substituted page id appeared in no author-written file, only in another of our translations, which is not evidence. Find the id in a source the author wrote, or record it as unconfirmed in the metadata comment.
6. **The same term rendered two ways on one page.** `精神内耗` was "wearing yourself out mentally" in one cell and "mental exhaustion" in the tutorial title beside it, breaking the link a reader needs. Pick one rendering per term and use `GLOSSARY.md`.
7. **Dropped parenthetical glosses.** `（解题能力）` was dropped in three places while a sibling page kept it, leaving the set inconsistent. His parentheses are content.
8. **Counts written by eye instead of measured.** Three separate `figures:` claims in metadata headers were wrong, every time by exactly one. Never type a count you have not measured:

   ```bash
   grep -c '!\[' .notion-cache/<slug>/source.md      # figures in the source
   grep -c '!\[' notion/<page>/README.md             # figures embedded here
   ```

   When auditing counts across the repo, resolve each page to its source **by page id, not by title**. Duplicate caches of the same page exist at different fetch depths, and a shallower copy reports fewer figures, which makes a correct page look wrong. That false positive has already happened once.
9. **Claims of exactness that are not exact.** A note promised command blocks "reproduced exactly as written" while non-breaking spaces had been flattened to ordinary ones, and promised "three worth knowing about" while a fourth and worse hazard went undisclosed: a line whose quote opens straight and closes curly, so a shell hangs waiting for input. If you promise completeness, count first; if you promise byte-identity, diff first.

## Update on every change

1. The status table in the root `README.md`.
2. `GLOSSARY.md`, if the change introduced a term.
3. Any `(not done)` marker that is now done.

## Rights

No license file covers the translated content, because the ideas are not ours. Do not add one. Anything genuinely original here (the scripts in `tools/`) can be licensed separately and explicitly.
