#!/usr/bin/env python3
"""Find hedges and intensifiers rendered inconsistently, or dropped.

Seven verification rounds found the same defect over and over: one Chinese word
rendered several ways in one file, or dropped entirely. A model finds those by
luck. This finds them exhaustively.

    python3 tools/check_renderings.py            # every translated page
    python3 tools/check_renderings.py notion/how-to-rebuttal/README.md

Two checks per file. NEITHER is a verdict. Both are leads to go and read.

1. suspect renderings. A form that past rounds got wrong is present, and so is
   the Chinese word it belongs to. They may be unrelated occurrences: the first
   run flagged "the usual Conclusion content" for 一般情况下 when the Chinese
   was 一般的, and "work out whether the reader can understand" for 总结 when
   the Chinese was 判断. Always read the context before editing.
2. count shortfall. The Chinese uses a word N times and the English has its
   settled rendering fewer than N times, so some were probably dropped. Same
   caveat: one English word often covers two Chinese ones, and a `<details>`
   summary repeats its own heading.

Exit code 1 if any suspect rendering is found, so CI can gate on a human
having looked.
"""

import json
import pathlib
import re
import sys

# (chinese, settled english, [renderings past rounds got wrong])
# Every banned entry here was a real defect, not a hypothetical.
RULES = [
    ("很多", "many", ["a lot of"]),
    ("各种", "all sorts of", ["various"]),
    ("真正", "genuinely", ["really"]),
    ("反复", "over and over", ["again and again", "repeatedly"]),
    ("一般情况下", "normally", ["the usual"]),
    ("非常重要", "very important", ["matters a great deal", "very very important"]),
    ("很重要", "matters a lot", []),
    ("简直", "simply", ["frankly"]),
    ("无法", "cannot", ["will not"]),
    ("只能", "can only", []),
    ("大概率", "very likely", ["a good chance"]),
    ("很可能", "very likely", ["may well", "quite possibly", "probably"]),
    ("比较", "fairly", []),
    ("挺", "quite", []),
    ("尽量", "as far as possible", ["try not to", "where possible"]),
    ("有所", "of some", []),
    ("总结", "summarize", ["collect", "lay out", "work out"]),
    ("经验", "experience", []),
    ("敢于", "dare to", ["willing to"]),
    ("喷", "slam", ["complain"]),
    ("适用于", "applies to", ["reflects"]),
    ("不一定", "not necessarily", ["not always"]),
    ("难以", "hard to", []),
    ("以求", "so as to", []),
    ("定制", "tailor", []),
    ("作业", "assignments", ["assignment code"]),
    ("增加", "increase", ["strengthen"]),
    ("极大地", "hugely", ["substantially"]),
    ("极强", "extremely strong", []),
    ("始终", "always", []),
    ("直接", "directly", []),
    ("完全", "completely", ["fully", "purely"]),
    ("一阵", "for a while", []),
    ("没什么", "hardly any", []),
    ("可行性", "feasibility", []),
]

# Words whose English form is too common to count meaningfully.
COUNT_EXEMPT = {"很", "一些", "有些", "需要", "能", "可以", "会", "才", "应该", "要", "多"}

# Hits checked by hand and found benign: a different Chinese word happens to
# share the English form. Keyed by (page stem, chinese, wrong form) -> why.
# Without this the report cries wolf every run and stops being read.
ALLOW = {
    ("how-to-build-a-literature-tree", "无法", "will not"): "不会更新, which is 'will not be updated'",
    ("how-to-build-idea-ability", "各种", "various"): "各个不同领域, which is 各个 not 各种",
    ("how-to-build-idea-ability", "无法", "will not"): "a different clause; no 无法 behind it",
    ("how-to-find-why-an-experiment-fails", "总结", "collect"): "搜集, which really is 'collect'",
    ("machine-setup", "无法", "will not"): "装不上, which is 'will not install'",
    ("paper-writing-template", "一般情况下", "the usual"): "一般的Conclusion内容, not 一般情况下",
    ("paper-writing-template", "无法", "will not"): "改不完, which is 'will not be able to finish'",
    ("paper-writing-template", "总结", "work out"): "判断, which is 'work out whether'",
    ("paper-writing-template", "完全", "fully"): "充分展示, which is 'fully show'",
    ("attractive-demo-and-application", "很可能", "probably"): "应该没法, which is 应该 not 很可能",
}


def load_pairs():
    """Map each translated page to the Chinese source it was fetched from.

    The cache manifest goes stale, so resolve by the title each translation
    records in its own header, and prefer the largest cached copy: his pages
    cross-link, so the same page is cached at several crawl depths and a
    shallow copy silently holds less.
    """
    root = pathlib.Path(__file__).resolve().parent.parent
    by_title = {}
    for p in (root / ".notion-cache").rglob("source.md"):
        text = p.read_text(encoding="utf-8")
        title = text.split("\n", 1)[0].lstrip("# ").strip()
        if title not in by_title or len(text) > len(by_title[title][1]):
            by_title[title] = (p, text)

    pairs = {}
    for f in sorted((root / "notion").rglob("README.md")):
        t = f.read_text(encoding="utf-8")
        m = re.search(r"source:\s*notion page\s*(.+)", t)
        if not m:
            continue
        title = re.sub(r"\s*\(nested under.*$", "", m.group(1).strip())
        if title in by_title:
            pairs[f] = by_title[title][0]
    return pairs


def strip_noise(text):
    """Drop fenced code and HTML comments. Commands are verbatim on purpose."""
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    return re.sub(r"<!--.*?-->", "", text, flags=re.S)


def count_words(haystack, needle):
    """Whole-word count. Without the boundaries, "carefully" matches "fully"
    and the report fills with noise; that happened on the first run."""
    return len(re.findall(r"\b" + re.escape(needle.lower()) + r"\b", haystack))


def check(en_path, zh_path):
    # Strip fences from BOTH sides. Stripping only the English while counting
    # the Chinese in full made every term inside his LaTeX template look
    # dropped: 很重要 counted 6 in the source against 2 in the English.
    en = strip_noise(en_path.read_text(encoding="utf-8")).lower()
    zh = strip_noise(zh_path.read_text(encoding="utf-8"))
    banned, thin = [], []
    for cn, right, wrong in RULES:
        n_cn = zh.count(cn)
        if not n_cn:
            continue
        stem = en_path.parent.name
        for bad in wrong:
            n = count_words(en, bad)
            if n and (stem, cn, bad) not in ALLOW:
                banned.append((cn, right, bad, n))
        if cn not in COUNT_EXEMPT:
            n_en = count_words(en, right)
            if n_en < n_cn:
                thin.append((cn, right, n_cn, n_en))
    return banned, thin


def english_runs(zh_text, min_words=10):
    """His sources contain whole sentences already in English: example sentences
    from papers, quoted advice, limitation templates. Those must be carried over
    verbatim, never retranslated. Round 8 found one reworded, with a framing
    clause added, and the exact wording was the point of the page.

    Yield each long English-only run, so the caller can check it survived.
    """
    for line in zh_text.split("\n"):
        line = line.strip()
        if not line or line.startswith(("#", ">", "|", "!", "<")):
            continue
        # A line starting with % is his LaTeX scaffolding, and %% marks an
        # example sentence lifted verbatim from a published paper. Those are
        # cited rather than reprinted, on purpose, so they must not be flagged.
        if line.startswith("%"):
            continue
        if re.search(r"[一-鿿]", line):
            continue
        bare = re.sub(r"^(\d+\.|[-*])\s*", "", line).strip()
        if len(bare.split()) >= min_words:
            yield bare


# Pages built entirely on another paper's draft sentences. Every list item there
# describes a sentence slot instead of reprinting it, by design, so the verbatim
# check has nothing to say about them.
VERBATIM_EXEMPT = {"writing-outline-examples"}


def check_verbatim(en_path, zh_path):
    """English-only source runs that do not appear verbatim in the translation."""
    if en_path.parent.name in VERBATIM_EXEMPT:
        return []
    en = en_path.read_text(encoding="utf-8")
    zh = strip_noise(zh_path.read_text(encoding="utf-8"))
    missing = []
    for run in english_runs(zh):
        if run not in en:
            missing.append(run)
    return missing


def main():
    pairs = load_pairs()
    if len(sys.argv) > 1:
        want = {pathlib.Path(a).resolve() for a in sys.argv[1:]}
        pairs = {k: v for k, v in pairs.items() if k.resolve() in want}

    total_banned = 0
    for en_path, zh_path in sorted(pairs.items()):
        banned, thin = check(en_path, zh_path)
        missing = check_verbatim(en_path, zh_path)
        if not banned and not thin and not missing:
            continue
        print(f"\n{en_path}")
        for run in missing:
            total_banned += 1
            print(f"  VERBATIM already English in the source, not found here:")
            print(f"           {run[:150]}")
        for cn, right, bad, n in banned:
            total_banned += 1
            print(f"  suspect  {cn} -> {right!r}, but found {bad!r} x{n}")
        for cn, right, n_cn, n_en in thin:
            print(f"  thin     {cn} x{n_cn} in source, {right!r} x{n_en} here")

    print(f"\n{len(pairs)} pages checked, {total_banned} suspect renderings to read")
    return 1 if total_banned else 0


if __name__ == "__main__":
    sys.exit(main())
