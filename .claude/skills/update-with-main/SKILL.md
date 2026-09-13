---
name: update-with-main
description: Use when checking whether this translation has fallen behind the upstream Chinese sources, or when asked to sync, update, or refresh the repository against pengsida/learning_research and his Notion documents. Triggers on "update with main", "is the translation stale", "sync upstream", "check for upstream changes", "refresh the notion docs".
---

# update-with-main

Bring the translation back in line with the Chinese sources. Two sources move independently: the GitHub repository, and the Notion documents it links to.

Read `.claude/CLAUDE.md` first. Every rule there applies to whatever you rewrite here, especially "never add", "never drop a figure", the hedge table in `GLOSSARY.md`, and the verification loop in step 5. Syncing one changed paragraph still means looping verification over the page you changed it in.

Report at the end even when nothing changed. "Already current, checked N files" is a useful answer.

## 1. GitHub side

Each file in `en/` records the upstream commit it came from:

```bash
grep -H "source commit" en/*.md
```

For each one, compare against upstream and see whether that specific file moved:

```bash
gh api "repos/pengsida/learning_research/commits?path=<source-file>&per_page=1" -q '.[0].sha'
```

If the hashes differ, get the actual diff before touching the translation:

```bash
gh api "repos/pengsida/learning_research/compare/<recorded>...<current>" \
  -q '.files[] | select(.filename=="<source-file>") | .patch'
```

Translate only what the diff changed. Do not retranslate the file from scratch, because that throws away review work already done on the untouched parts. Update the `source commit` in the header.

## 2. Notion side

Notion has no commit hashes, so use two signals.

**Signal one, his changelog.** It is the cheapest check and he keeps it current:

```bash
gh api repos/pengsida/learning_research/contents/changelog -q .content | base64 -d | head -20
```

Compare the newest dates against `en/changelog.md`. A new entry naming a document you have translated means that document changed.

**Signal two, refetch and diff.** Authoritative, slower:

```bash
python3 tools/notion_fetch.py <page-id> --out .notion-cache --depth 3
```

Each translated Notion page records its page id and fetch date in its header. Refetch, then diff the new `.notion-cache/<slug>/source.md` against what the translation covers. Watch for three things:

- new or reworded sections, which need translating
- new figures in `assets/`, which need redrawing per the figures rules
- sections that disappeared upstream, which should be removed here too, not silently kept

## 3. Pages he has added since last time

Changed pages are not the only drift. He adds new pages, and some are reachable only through inline links, which the fetcher does not follow.

```bash
python3 tools/notion_map.py --depth 3
```

Compare the result against the tables in `notion/README.md` and `notion/not-translated.md`. If a page id in `not-translated.md` has stopped resolving, say so rather than deleting the row quietly.

**Scope is wide.** Anything touching research learning stays in, even loosely: talk notes, paper notes, book notes, pipeline summaries, technical study notes. Only something with no connection at all, like a personal homepage, goes in `not-translated.md`. When unsure, translate it.

**Deduplicate by page id.** A refetch will produce the same page under several parent paths, because his pages cross-link. Before translating any source file, check whether its page id already has a translation:

```bash
grep -rl "source page id: <id>" notion/
```

If one exists, link to it from the new location instead of translating it again. One page, one translated file, keyed by id and never by title or path.

## 4. Check the fetch before trusting it

Every refetch, before translating anything from it:

```bash
grep -o '\./assets/[^)]*' .notion-cache/<slug>/source.md | sort -u | wc -l   # figure refs
ls .notion-cache/<slug>/assets | wc -l                                       # files present
grep -c '\[[^]]*\](http' .notion-cache/<slug>/source.md                      # inline links
```

Refs must equal files. A link count of 0 on a cross-referencing page means links were dropped again. Both failure modes have happened and both look like a clean fetch. Details in `.claude/CLAUDE.md`.

## 5. Verify in a loop until every page you touched comes back clean

**This is the longest part of the job. Budget for it.** One verification pass is not enough, because the fixes you make in response to a pass are new prose that has never been checked. Verification is a loop.

`.claude/CLAUDE.md` holds the full procedure under "Verify in a loop until the page comes back clean". The short form:

```
pages = every page you translated or edited in steps 1 to 3
round = 1
while pages is not empty and round <= 7:        # seven is a hard cap
    dispatch fresh verifier agents over pages, batched 3 or 4 short pages each,
      one agent alone for a long page
    for each page:
        triage: real defect, or false positive you checked against the source
        apply the real ones, then grep to confirm each intended result is present
        page stays in the loop if you changed it, leaves if the round was clean
    commit and push this round
    round += 1

# any page still in the loop at round 7 stops there anyway
```

**Seven rounds is a hard cap. If round seven is not clean, stop and hand the page to a Chinese reader.** Do not run round eight.

That cap is measured, not a guess. Rounds 1 and 2 on the `notion/` pages found 94 defects including a 15-line invented block, three dropped hyperlinks and a reversed claim. Rounds 8 to 11 found about 45 over 15 agent runs, almost all a single dropped particle. Worse, past round seven the loop began producing its own defects: round 6 caught a "Very very important" that round 5's fix had created, and round 11 caught a sentence that round 9's advice had double-hedged. When a loop removes single particles while inserting errors the same size, it has stopped paying.

When you hit the cap, do these instead of another round:

1. **Run `python3 tools/check_renderings.py`.** It found 8 defects in pages that seven model rounds had called clean. For any enumerable defect class, write the check rather than run the round.
2. **Measure, then aim.** Round 10 was told "roughly 11 occurrences of 会 have lost their modal" instead of "look for problems", and found 16 defects right after round 9 found 11. Counting beats noticing.
3. **Say the page is unfinished.** Set `status:` to the real round count and state that the last round was not clean. "6 rounds, last one found a defect" is worth more than a page claiming clean because the loop stopped at a convenient moment.
4. **Ask for a Chinese reader.** No round replaces this. One reader on the longest page for an hour finds more that matters than round eight.

What the loop costs, measured here: `en/getting-started-in-research.md` took 13 rounds before the cap existed (9, 6, 9, 9, 6, 8, 2, 4, 4, 4, 3, 2, 0). The 32 `notion/` pages had each had one pass, and further rounds found 231 more real defects. A single pass catches about half, and rounds 3 to 7 catch most of the rest.

**Run the mechanical check first, every round.** One whole round found nothing but the same word rendered two ways in one file, which a script finds exhaustively and a model finds by luck:

```bash
python3 tools/check_renderings.py
```

Its hits are leads, not verdicts: on the first run 8 of 15 were false positives where a different Chinese word shares the English form. Verify each against the Chinese, then record the benign ones in the script's `ALLOW` table so the report stays worth reading. Doing this before dispatching agents means the round spends its attention on meaning rather than on bookkeeping.

Three things make the loop converge rather than spin:

- **Carry forward what each round learns.** Add every settled rendering to `GLOSSARY.md` and paste that list into the next verifier's prompt as fixed renderings. Round 4 here found more than round 3 purely because it was the first round given a particle-by-particle checklist. A blunt check returns a low count that looks like progress and is not.
- **Tell the verifier the settled conventions** so it does not spend findings on the `> [Original Article]` line, `<details>` toggles, Mermaid diagrams, or cited-not-reprinted third-party passages.
- **Require a Chinese quote for every finding.** Most false positives die on that requirement alone.

The defect this loop exists to catch is not bad English. It is his voice being flattened: 很, 一些, 某个, 需要, 应该, 能, 会, 才 dropped one at a time until hedged advice reads as flat instruction. Read the hedge table in `GLOSSARY.md` before you translate and check the result against it after.

A file you edited and did not verify must have its header set back to `status: unverified`. Never claim a round that did not run.

## 6. Finish properly

1. Record each page's real state in its `status:` line: how many rounds ran and whether the last was clean.
2. Update the status table in the root `README.md`, including the per-file round counts.
3. Update `GLOSSARY.md` with every term and hedge the loop settled.
4. Flip any `(not done)` marker that is now done.
5. Re-run the mechanical checks: broken relative links, figure references against files on disk, Mermaid blocks still parsing, no em-dashes, no British spellings.
6. Commit per source file, not one commit for everything, so a reviewer can follow which upstream change caused which edit. Subject line: `sync: <source file> to <short sha or date>`. Commit each verification round separately from the translation itself.

## Notes

- `.notion-cache/` is gitignored. Never commit the Chinese source.
- Notion's `syncRecordValues` endpoint refuses anonymous callers, so the fetch tool makes one request per nested block. A deep page takes minutes. Run it in the background and do the GitHub side while you wait.
- If `tools/notion_fetch.py` starts returning empty pages, Notion changed its private API. Say so plainly rather than reporting "no changes found", because the two look identical from the outside.
