#!/usr/bin/env python3
"""Map the reachable Notion page graph before translating anything.

Usage: python3 tools/notion_map.py [--depth N] [--out FILE]

DFS from the pages his GitHub repo links, following BOTH child-page blocks and
inline page links, which is how pages get missed. Counts pages and characters
so the size of the job is known up front. Fetches text only, no assets.
"""
import argparse, json, re, sys, time
from notion_fetch import chunk, dashed, text_of, HOST

# the 18 pages linked from pengsida/learning_research
SEEDS = """
c1a22465a0fa4b15a12985223916048e b43507ef26d044bd888ac29f4736e116
da6ce171c13846b7a7ffaa7473ffa6ea c13c7e52aab64c1a8e3576b97fcb9851
74aef88b9187439fa4e301704f6eb49a af99ce47103e4917b6a5bd1fd4b3c022
810f02670691444f8c94cc3d5b76dcbc d192db870bc64436ae4a4a590b36772a
d697ef578d784c869d4f8314f0d617da 1aee6e718de6472f834d13da8f4ff097
caf34717f4c046c69ee7e14ea953c46f 59569d7b66954578b21bf1dc6ea35776
a3fe9f17b8af46558cd1112627009c83 8911dcc5922b4442a80d4407926e65bf
1713fe292ff1808eb33be93ea2d79ad9 1753fe292ff180948215cf82cd2b30ae
c278dab7e4764d61a92c1fd1ef3135b1 1d13fe292ff180de91afcb7f2eb57b69
""".split()

ID = re.compile(r"([0-9a-f]{32})")


def page_blocks(pid, max_chunks=4):
    blocks = {}
    for n in range(max_chunks):
        try:
            payload = chunk(pid, n)
        except Exception as e:
            print(f"  !! {pid[:8]} chunk{n}: {str(e)[:60]}", file=sys.stderr)
            break
        got = payload.get("recordMap", {}).get("block", {})
        before = len(blocks)
        for k, v in got.items():
            val = v.get("value", {})
            blocks[k] = val.get("value", val)
        if len(blocks) == before:
            break
        time.sleep(0.35)
    return blocks


def links_in(blocks):
    """Page ids reachable from this page: child page blocks plus inline links."""
    out = set()
    for v in blocks.values():
        if v.get("type") == "page":
            out.add(v.get("id") or "")
        for prop in (v.get("properties") or {}).values():
            for seg in prop:
                for ann in (seg[1] if seg and len(seg) > 1 else None) or []:
                    if ann and ann[0] == "a" and len(ann) > 1:
                        m = ID.search(ann[1].replace("-", ""))
                        if m:
                            out.add(dashed(m.group(1)))
    return {o for o in out if o}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--depth", type=int, default=3)
    ap.add_argument("--out", default="/tmp/nx/page_map.json")
    a = ap.parse_args()

    seen, pages, queue = set(), [], [(dashed(s), 0, None) for s in SEEDS]
    while queue:
        pid, d, parent = queue.pop(0)          # BFS order, DFS-equivalent coverage
        if pid in seen or d > a.depth:
            continue
        seen.add(pid)
        blocks = page_blocks(pid)
        root = blocks.get(pid) or {}
        title = text_of(root) or "(unknown)"
        chars = len(re.sub(r"\s", "", "".join(text_of(v) for v in blocks.values())))
        kids = links_in(blocks) - {pid}
        pages.append({"id": pid, "title": title, "depth": d, "chars": chars,
                      "parent": parent, "links": sorted(kids)})
        print(f"{'  '*d}{title[:44]!r} d{d} chars={chars} links={len(kids)}", flush=True)
        for k in kids:
            queue.append((k, d + 1, pid))

    json.dump({"pages": pages}, open(a.out, "w"), ensure_ascii=False, indent=1)
    print(f"\nreachable pages: {len(pages)}")
    print(f"total characters: {sum(p['chars'] for p in pages)}")
    print(f"seeds: {len(SEEDS)}  discovered beyond seeds: {len(pages) - len([p for p in pages if p['depth'] == 0])}")


if __name__ == "__main__":
    main()
