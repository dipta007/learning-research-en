---
name: update-with-main
description: Use when checking whether this translation has fallen behind the upstream Chinese sources, or when asked to sync, update, or refresh the repository against pengsida/learning_research and his Notion documents. Triggers on "update with main", "is the translation stale", "sync upstream", "check for upstream changes", "refresh the notion docs".
---

# update-with-main

Bring the translation back in line with the Chinese sources. Two sources move independently: the GitHub repository, and the Notion documents it links to.

Read `.claude/CLAUDE.md` first. Every rule there applies to whatever you rewrite here, especially "never add", "never drop a figure", and the fable verification step.

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

Compare the result against the tables in `notion/README.md` and `notion/not-translated.md`. New on-topic pages get translated; new personal study notes get a row in `not-translated.md` with a link. If a page id in `not-translated.md` has stopped resolving, say so rather than deleting the row quietly.

## 4. Check the fetch before trusting it

Every refetch, before translating anything from it:

```bash
grep -o '\./assets/[^)]*' .notion-cache/<slug>/source.md | sort -u | wc -l   # figure refs
ls .notion-cache/<slug>/assets | wc -l                                       # files present
grep -c '\[[^]]*\](http' .notion-cache/<slug>/source.md                      # inline links
```

Refs must equal files. A link count of 0 on a cross-referencing page means links were dropped again. Both failure modes have happened and both look like a clean fetch. Details in `.claude/CLAUDE.md`.

## 5. Finish properly

1. Verify every file you touched with a fresh fable subagent. Rules and exact instructions are in `.claude/CLAUDE.md`. A file you edited and did not verify must have its header set back to `status: unverified`.
2. Update the status table in the root `README.md`.
3. Update `GLOSSARY.md` if a new term appeared.
4. Flip any `(not done)` marker that is now done.
5. Commit per source file, not one commit for everything, so a reviewer can follow which upstream change caused which edit. Subject line: `sync: <source file> to <short sha or date>`.

## Notes

- `.notion-cache/` is gitignored. Never commit the Chinese source.
- Notion's `syncRecordValues` endpoint refuses anonymous callers, so the fetch tool makes one request per nested block. A deep page takes minutes. Run it in the background and do the GitHub side while you wait.
- If `tools/notion_fetch.py` starts returning empty pages, Notion changed its private API. Say so plainly rather than reporting "no changes found", because the two look identical from the outside.
