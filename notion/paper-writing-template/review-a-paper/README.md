<!--
source: notion page 怎么审论文 (nested under 论文写作模板)
source page id: c1a22465a0fa4b15a12985223916048e (root) -> 怎么审论文
source fetched: 2026-09-11
status: verified by fable, 2026-09-11 (findings applied)
figures: 1, the author's original, English redraw pending
-->

# How to Review a Paper

> Collected documents (GitHub repo): https://github.com/pengsida/learning_research

Check carefully whether the paper has any factor that would get it rejected. Go through them one by one and you will know whether this paper should be rejected.

Table by Prof. Peng Sida, redrawn in English. [Original](./assets/0c1ce1013cd44592a926a357fc6997ff-Untitled.png).

| Rejection factor | Specifically |
|---|---|
| 1. Contribution is not enough<br>(the paper brings the reader no new knowledge) | 1.1 The failure cases you want to solve are very common<br>1.2 The proposed technique is already well-explored, and the performance improvement it brings is predictable / well-known |
| 2. The writing is unclear | 2.1 Technical details are missing, not reproducible<br>2.2 Some method module lacks motivation |
| 3. The experimental results are not good enough | 3.1 Only a little better than previous methods<br>3.2 Better than previous methods, but the results are still not good enough |
| 4. The experimental testing is not thorough | 4.1 Missing ablation studies<br>4.2 Missing important baselines, missing an important evaluation metric<br>4.3 The data is too simple, so it cannot prove whether the method really works |
| 5. There are problems with the method design | 5.1 The experimental setting is not realistic<br>5.2 The method has technical defects and looks unreasonable<br>5.3 The method is not robust, it needs hyperparameter tuning on every scene<br>5.4 The new method design brings a benefit but introduces a stronger limitation at the same time, so the new method's net gain is negative |

The reasons a paper is accepted. A paper needs to achieve these three things:

1. The contribution is enough (it needs to include several of these: novel task, novel pipeline, novel pipeline module, novel design choices, new experimental findings, new insights)
2. The experimental results are better than previous methods.
3. The ablation studies and comparison experiments are thorough.

The reasons a paper is rejected. The common reasons for rejection:

1. The contribution is not enough (the paper brings the reader no new knowledge, which usually includes several of these: the failure cases you want to solve are very common; the proposed technique is already well-explored, and the performance improvement it brings is predictable or well-known)
2. The writing is unclear (technical details are missing, so it is not reproducible; some method module lacks motivation)
3. The experimental results are not good enough (only a little better than previous methods; better than previous methods, but still not good enough)
4. The experimental testing is not thorough (missing ablation studies; missing important baselines; missing an important evaluation metric; the data is too simple, so it cannot prove whether the method really works)
5. There are problems with the method design (the experimental setting is not realistic; the method has technical defects and looks unreasonable; the method is not robust and needs hyperparameter tuning per scene; the new method design brings a benefit but introduces a stronger limitation at the same time, so its net gain is negative)
