# Notion documents

Prof. Peng keeps most of his notes on Notion rather than in the GitHub repository. This directory holds the English translations of his **research-advice** pages.

His Notion also contains study notes, where he takes notes on other people's talks, interviews, books and papers. Those are linked in [not-translated.md](./not-translated.md) rather than translated.

His pages change every few weeks, so a translation here can be behind. Every page records the date it was fetched. When in doubt, read his original.

## Translated

| Document | Original | Translation |
|---|---|---|
| A paper writing template | [Notion](https://pengsida.notion.site/c1a22465a0fa4b15a12985223916048e) | [translated](./paper-writing-template/README.md) (8 sub-pages) |
| The awareness and abilities a PhD student should have, and how to run a research project | [Notion](https://pengsida.notion.site/b43507ef26d044bd888ac29f4736e116) | [translated](./phd-awareness-abilities-and-research-project/README.md) |
| How to build the ability to come up with ideas | [Notion](https://pengsida.notion.site/da6ce171c13846b7a7ffaa7473ffa6ea) | [translated](./how-to-build-idea-ability/README.md) |
| How to write a rebuttal | [Notion](https://pengsida.notion.site/af99ce47103e4917b6a5bd1fd4b3c022) | [translated](./how-to-rebuttal/README.md) |
| How to read papers effectively | [Notion](https://pengsida.notion.site/d192db870bc64436ae4a4a590b36772a) | [translated](./how-to-read-papers-effectively/README.md) |
| How to find why an experiment does not work | [Notion](https://pengsida.notion.site/1aee6e718de6472f834d13da8f4ff097) | [translated](./how-to-find-why-an-experiment-fails/README.md) |
| How to build a literature tree | [Notion](https://pengsida.notion.site/f8b36e484b344a2893a94e4608b72ec2) | [translated](./how-to-build-a-literature-tree/README.md) |
| How to hold an efficient discussion | [Notion](https://pengsida.notion.site/d697ef578d784c869d4f8314f0d617da) | [translated](./how-to-discuss-efficiently/README.md) |
| How research study differs from course study | [Notion](https://pengsida.notion.site/a3fe9f17b8af46558cd1112627009c83) | [translated](./research-study-vs-course-study/README.md) |
| How to make slides for an academic talk | [Notion](https://pengsida.notion.site/810f02670691444f8c94cc3d5b76dcbc) | [translated](./how-to-make-talk-slides/README.md) |
| How to keep experiment records | [Notion](https://pengsida.notion.site/caf34717f4c046c69ee7e14ea953c46f) | [translated](./how-to-keep-experiment-records/README.md) (with a template and a worked example) |
| Template for analyzing a project's core technical problems | [Notion](https://pengsida.notion.site/1753fe292ff180948215cf82cd2b30ae) | [translated](./core-technical-problem-template/README.md) |
| A model PhD student: Sebastian Starke | [Notion](https://pengsida.notion.site/1713fe292ff1808eb33be93ea2d79ad9) | [translated](./a-model-phd-student-sebastian-starke/README.md) |
| Research qualities, via interview questions | [Notion](https://pengsida.notion.site/1d13fe292ff180de91afcb7f2eb57b69) | [translated](./research-qualities-via-interview-questions/README.md) |
| Exploratory experiments should follow minimum viability | [Notion](https://pengsida.notion.site/2863fe292ff180759413f51ed1d1fdc3) | [translated](./minimum-viability-in-exploratory-experiments/README.md) |
| Machine setup | [Notion](https://pengsida.notion.site/59569d7b66954578b21bf1dc6ea35776) | [translated](./machine-setup/README.md) |
| Idea-driven vs. goal-driven research | [Notion](https://pengsida.notion.site/d9c6556326e84962a2d7ae190e2705af) | [translated](./idea-driven-vs-goal-driven-research/README.md) |
| How to practice writing papers | [Notion](https://pengsida.notion.site/c13c7e52aab64c1a8e3576b97fcb9851) | [translated](./how-to-practice-writing-papers/README.md) |
| An example study plan | [Notion](https://pengsida.notion.site/8911dcc5922b4442a80d4407926e65bf) | [translated](./example-study-plan/README.md) |
| How to find papers | [Notion](https://pengsida.notion.site/c278dab7e4764d61a92c1fd1ef3135b1) | [translated](./how-to-find-papers/README.md) |
| The definition of natural science | [Notion](https://pengsida.notion.site/1053fe292ff18015b2f3cde4498a5f0f) | [translated](./definition-of-natural-science/README.md) (link only: his page reprints someone else's article) |
| What things are taboo in research | [Notion](https://pengsida.notion.site/1fa3fe292ff1807e98c5e3513045cbab) | [translated](./taboos-in-research/README.md) (link only: his page is a bookmark) |

Every translated file opens with a link to its original, and records in an HTML comment the page id, the fetch date, and whether a second model has verified it against the Chinese.

## Not translated

See [not-translated.md](./not-translated.md): his study notes, his homepage, and two page ids that no longer resolve.

## Re-fetching a page

```
python3 tools/notion_fetch.py <page-id> --out .notion-cache --depth 3
```

Then check the fetch before trusting it, and follow the rules in [.claude/CLAUDE.md](../.claude/CLAUDE.md).
