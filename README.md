# learning_research, in English

An English translation of [Prof. Sida Peng's open research notes](https://github.com/pengsida/learning_research), which are written in Chinese. Practical advice on how to do research: how to start, how to get better, how to write.

All ideas and examples are his. If the advice helps you, the credit is his, and [his repository](https://github.com/pengsida/learning_research) is the one to star first.

## No license, on purpose

His repository has no license, so he keeps all rights to the content. This translation carries no license over that text either, and there is no `LICENSE` file here deliberately.

Read it freely. Do not relicense it, repackage it, or sell it. To reuse it beyond reading, ask him. [NOTICE.md](./NOTICE.md) is the full statement, including that any request from him about this repository will be followed.

## Contents

| Source | Translation | Checked by a second model | Read by a Chinese reader |
|---|---|---|---|
| `README.md` | [en/readme.md](./en/readme.md) | 7 passes, last one clean | not yet |
| `getting_started_in_research.md` | [en/getting-started-in-research.md](./en/getting-started-in-research.md) | 13 passes, last one clean | not yet |
| `getting_advanced_in_research.md` | [en/getting-advanced-in-research.md](./en/getting-advanced-in-research.md) | 1 pass, clean | not yet |
| `changelog` | [en/changelog.md](./en/changelog.md) | 2 passes, last one clean | not yet |

Most of his writing lives on Notion, not in that repository. **All of his research-advice pages are now translated**: 22 top-level pages plus their sub-pages, indexed in [`notion/`](./notion).

His study notes, where he takes notes on other people's talks, interviews, books and papers, are linked in [`notion/not-translated.md`](./notion/not-translated.md) rather than translated. They are most of his Notion by length and little of it by use to someone learning research.

A "pass" is a fresh model reading the English against the Chinese and reporting every difference it can quote both sides of. Passes repeat because each round of fixes is new prose that needs its own check. On the longest file above, the passes found 9, 6, 9, 9, 6, 8, 2, 4, 4, 4, 3, 2, then 0 defects. The late ones were small: a dropped "can", one Chinese word rendered two ways, a quantifier lost in one sentence and kept in the next.

Each page in `notion/` records its own state in an HTML comment at the top. Those pages had **one pass each**, not thirteen. On the evidence above, one pass catches maybe half of this kind of defect, so expect more small errors in `notion/` than in `en/`.

## Found a mistake? Please tell me

Every page here was translated by a model and checked by a second one. No human who reads Chinese has read any of it yet, so reader reports are the main way this gets accurate.

**[Open an issue](https://github.com/dipta007/learning-research-en/issues/new)** for anything at all:

- a sentence whose meaning looks wrong against the original
- English that is technically right but hard to read
- a missing or wrong figure, a broken link, a term used two different ways
- anything that just reads oddly, even if you cannot say why

One line is enough. "This sentence sounds off" is a useful report, and you do not need to read Chinese to file it.

**Or open a pull request** and fix it directly. Small corrections are very welcome and I would rather merge your fix than debate it. See [CONTRIBUTING.md](./CONTRIBUTING.md) for the few translation rules, mainly that a page holds the translation and nothing else.

## Reading it

Read the original if you read Chinese. A translation always loses something, and his Notion pages are updated more often than this repository.

For a tool rather than a guide, [Master-cai/Research-Paper-Writing-Skills](https://github.com/Master-cai/Research-Paper-Writing-Skills/) packages his paper-writing notes as a skill for coding agents. He links to it himself.

## Contributing

Corrections from people who read Chinese are the most useful. See the section above for how to report something.

The rules live in [.claude/CLAUDE.md](./.claude/CLAUDE.md), which coding agents load on their own, so an agent working in this repository already knows them. [CONTRIBUTING.md](./CONTRIBUTING.md) is the short human version and [GLOSSARY.md](./GLOSSARY.md) fixes the terms.

Two things to know before editing a file in `en/` or `notion/`: those files hold the translation and nothing else, and every change is checked by a second model against the Chinese before it lands.
