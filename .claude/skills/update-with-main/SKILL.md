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
while pages is not empty:
    dispatch fresh verifier agents over pages, batched 3 or 4 short pages each,
      one agent alone for a long page
    for each page:
        triage: real defect, or false positive you checked against the source
        apply the real ones, then grep to confirm each intended result is present
        page stays in the loop if you changed it, leaves if the round was clean
    commit and push this round
```

What this actually costs, measured here: `en/getting-started-in-research.md` needed **13 rounds** to reach an empty one (9, 6, 9, 9, 6, 8, 2, 4, 4, 4, 3, 2, 0 defects). The 32 `notion/` pages had each had one pass, and five further rounds found **155 more real defects** (53, 41, 21, 28, 12). A single pass catches about half.

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
