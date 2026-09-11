#!/usr/bin/env python3
"""Fetch a public Notion page tree as Markdown plus assets.

Usage: python3 tools/notion_fetch.py <page-id> [--out DIR] [--depth N]

Writes DIR/<slug>/source.md, DIR/<slug>/assets/*, DIR/<slug>/manifest.json,
and recurses into child pages as nested directories. The Chinese source it
writes is translation input, not repository content: keep DIR gitignored.
"""
import argparse, json, os, re, sys, time, urllib.parse, urllib.request

HOST = "https://pengsida.notion.site"
UA = {"user-agent": "Mozilla/5.0", "content-type": "application/json"}
SLEEP = 0.35

# no bulk endpoint: syncRecordValues is 403 for anonymous callers, so every
# nested block costs one request. hence the sleep and the depth cap.


def dashed(i):
    i = i.replace("-", "")
    return f"{i[:8]}-{i[8:12]}-{i[12:16]}-{i[16:20]}-{i[20:]}" if len(i) == 32 else i


def chunk(block_id, n=0):
    body = json.dumps({"pageId": block_id, "limit": 200, "cursor": {"stack": []},
                       "chunkNumber": n, "verticalColumns": False}).encode()
    req = urllib.request.Request(f"{HOST}/api/v3/loadPageChunk", data=body, headers=UA)
    with urllib.request.urlopen(req, timeout=40) as r:
        return json.loads(r.read())


def flatten(payload, into):
    for k, v in payload.get("recordMap", {}).get("block", {}).items():
        val = v.get("value", {})
        into.setdefault(k, val.get("value", val))


def fetch_tree(root_id, max_depth):
    """Pull the block tree, resolving lazily-loaded children one id at a time."""
    blocks, queue, seen = {}, [(root_id, 0)], set()
    while queue:
        bid, depth = queue.pop(0)
        if bid in seen or depth > max_depth:
            continue
        seen.add(bid)
        try:
            flatten(chunk(bid), blocks)
        except Exception as e:
            print(f"  !! {bid}: {e}", file=sys.stderr)
            continue
        time.sleep(SLEEP)
        for k, v in list(blocks.items()):
            for c in v.get("content") or []:
                if c not in blocks and c not in seen:
                    queue.append((c, depth + 1))
    return blocks


def text_of(block):
    out = []
    for seg in (block.get("properties") or {}).get("title") or []:
        if seg and isinstance(seg[0], str):
            out.append(seg[0])
    return "".join(out)


def slug(s, fallback):
    s = re.sub(r"[^\w一-鿿-]+", "-", s or "").strip("-").lower()
    return s[:60] or fallback


def asset_url(block_id, src):
    return (f"{HOST}/image/{urllib.parse.quote(src, safe='')}"
            f"?table=block&id={block_id}&cache=v2")


def save_asset(block_id, src, assets_dir):
    """Returns the local filename, or None when Notion will not serve the bytes."""
    os.makedirs(assets_dir, exist_ok=True)
    name = src.split(":")[-1] if src.startswith("attachment:") else src.split("/")[-1].split("?")[0]
    name = re.sub(r"[^\w.-]+", "_", urllib.parse.unquote(name))[:80] or f"{block_id[:8]}.bin"
    path = os.path.join(assets_dir, name)
    if os.path.exists(path):
        return name
    try:
        req = urllib.request.Request(asset_url(block_id, src), headers={"user-agent": UA["user-agent"]})
        with urllib.request.urlopen(req, timeout=40) as r:
            data = r.read()
            if b"<!doctype html" in data[:64].lower():
                return None
        open(path, "wb").write(data)
        time.sleep(SLEEP)
        return name
    except Exception as e:
        print(f"  !! asset {name}: {str(e)[:60]}", file=sys.stderr)
        return None


MARK = {"header": "## ", "sub_header": "### ", "sub_sub_header": "#### ",
        "bulleted_list": "- ", "numbered_list": "1. ", "quote": "> ", "text": ""}


def render(blocks, node_id, out_dir, depth=0, seen=None):
    """Block tree to Markdown. Toggles become <details>, which keeps his structure."""
    seen = seen if seen is not None else set()
    if node_id in seen:
        return []
    seen.add(node_id)
    b = blocks.get(node_id) or {}
    t, txt, lines = b.get("type"), text_of(b), []
    kids = [c for c in (b.get("content") or []) if c in blocks]

    if t in MARK:
        lines.append(MARK[t] + txt if txt else "")
    elif t == "toggle":
        lines += ["<details>", f"<summary>{txt}</summary>", ""]
    elif t == "callout":
        lines += [f"> **note** {txt}" if txt else "> **note**"]
    elif t == "code":
        lines += ["```", txt, "```"]
    elif t == "to_do":
        lines.append(f"- [ ] {txt}")
    elif t in ("image", "file", "pdf", "video", "drawing", "embed"):
        src = ((b.get("properties") or {}).get("source") or [[""]])[0][0]
        name = save_asset(node_id, src, os.path.join(out_dir, "assets")) if src else None
        if name and t == "image":
            lines.append(f"![{txt or name}](./assets/{name})")
        elif name:
            lines.append(f"[{txt or name}](./assets/{name})")
        else:
            lines.append(f"<!-- {t} not downloadable: {txt or src} -->")
    elif t == "table_row":
        cells = [("".join(s[0] for s in p if s and isinstance(s[0], str)))
                 for p in (b.get("properties") or {}).values()]
        lines.append("| " + " | ".join(cells) + " |")
    elif t == "page" and depth > 0:
        lines.append(f"[{txt}](./{slug(txt, node_id[:8])}/source.md)")
        return lines
    elif txt:
        lines.append(txt)

    for c in kids:
        lines += render(blocks, c, out_dir, depth + 1, seen)
    if t == "toggle":
        lines += ["", "</details>"]
    return lines


def write_page(blocks, page_id, out_dir, manifest, max_depth):
    root = blocks.get(page_id) or {}
    title = text_of(root)
    os.makedirs(out_dir, exist_ok=True)
    body = render(blocks, page_id, out_dir)
    src = "\n".join([f"# {title}", ""] + body[1:]) + "\n"
    open(os.path.join(out_dir, "source.md"), "w", encoding="utf-8").write(src)
    manifest.append({"id": page_id, "title": title, "dir": out_dir,
                     "chars": len(re.sub(r"\s", "", src)),
                     "assets": sorted(os.listdir(os.path.join(out_dir, "assets")))
                     if os.path.isdir(os.path.join(out_dir, "assets")) else []})
    print(f"  {out_dir}: {manifest[-1]['chars']} chars, {len(manifest[-1]['assets'])} assets")

    for k, v in blocks.items():
        if k != page_id and v.get("type") == "page":
            child_title = text_of(v)
            child_dir = os.path.join(out_dir, slug(child_title, k[:8]))
            if any(m["id"] == k for m in manifest):
                continue
            sub = fetch_tree(k, max_depth)
            write_page(sub, k, child_dir, manifest, max_depth)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("page_id")
    ap.add_argument("--out", default=".notion-cache")
    ap.add_argument("--depth", type=int, default=3)
    a = ap.parse_args()
    pid = dashed(a.page_id)
    print(f"fetching {pid} (depth {a.depth})")
    blocks = fetch_tree(pid, a.depth)
    print(f"  {len(blocks)} blocks")
    manifest = []
    out = os.path.join(a.out, slug(text_of(blocks.get(pid) or {}), pid[:8]))
    write_page(blocks, pid, out, manifest, a.depth)
    open(os.path.join(a.out, "manifest.json"), "w", encoding="utf-8").write(
        json.dumps({"root": pid, "fetched_at": time.strftime("%Y-%m-%d"), "pages": manifest},
                   ensure_ascii=False, indent=1))
    print(f"\n{len(manifest)} pages, {sum(m['chars'] for m in manifest)} chars total")


if __name__ == "__main__":
    main()
