<!--
source: notion page 如何培养想idea的能力（选题能力和解题能力）
source page id: da6ce171-c138-46b7-a7ff-aa7473ffa6ea
source fetched: 2026-09-11
status: unverified
figures: 6 in the source, all screenshots of other people's writing, cited here instead of embedded
-->

# How to Build the Ability to Come Up with Ideas (Choosing a Problem and Solving It)

> [Original Article](https://pengsida.notion.site/da6ce171c13846b7a7ffaa7473ffa6ea)

> **Translator's note.** Every figure on this page is a screenshot of someone else's writing: a Zhihu answer, and two English pages by other researchers. Those are cited with their links rather than copied in, and the English ones need no translation. His own text is translated in full.
>
> One passage below is marked by him as an outdated view that he has since replaced. That marking is kept, because the change of mind is part of what the page says.

<details>
<summary>Reference documents</summary>

<!-- John_Schulman的科研经验.pdf is not downloadable from Notion -->
<!-- Michael_Nielsen的科研经验.pdf is not downloadable from Notion -->

[A Chinese version of Michael Nielsen's research experience](https://zhuanlan.zhihu.com/p/560852116)

<details>
<summary>A Zhihu answer</summary>

"When did your research ability start to improve rapidly?", answered by 叶小飞 on Zhihu: [https://www.zhihu.com/question/524855881/answer/2819447733](https://www.zhihu.com/question/524855881/answer/2819447733)

The source embeds four screenshots of that answer. Read it at the link.

</details>

</details>

Coming up with an idea splits into two steps: choose a good problem, then solve it.

Use a literature tree (a novelty tree and a challenge-insight tree) to train and accumulate the ability to come up with ideas.

<details>
<summary>The concrete process for coming up with ideas (goal-driven research)</summary>

1. Plan a general goal for the research direction, and set a roadmap for reaching that general goal.

   <details>
   <summary>How to do it</summary>

   Generally the general goal is easy to define, but setting the roadmap needs a deep understanding of the field.

   You can build up your understanding of the field by building a literature tree, that is, doing a literature review and building a novelty tree and a challenge-insight tree.

   [How to build a literature tree (how to do a literature review, and build a novelty tree and a challenge-insight tree)](https://pengsida.notion.site/f8b36e484b344a2893a94e4608b72ec2?pvs=25)

   </details>

2. **Choosing the problem.** From the roadmap laid out by the novelty tree, choose a task that has research room, and investigate whether that task has an important technical challenge. Choosing the problem is the step with the largest effect on a research project, not the later step of thinking of a method.

   > **note** How to find an important research problem:
   > Think about the long-term goal of this task, and what a final form of it would look like.
   > Ask why current work only runs on this data and not on other data. You should try data covering more general cases.
   > Aim to discover new failure cases, and improve the existing technique starting from those new failure cases. (1. New failure cases are easier to find on a new task setting or new data. 2. Exploring what a method can do on new data, so that people see new experimental conclusions, is a large contribution.)

   <details>
   <summary>What strong researchers think about "finding an important research problem"</summary>

   The source shows a screenshot of another researcher's writing on this. It is cited rather than copied in, because it is not his text.

   </details>

3. **Choosing the problem.** Think about whether the current failure case already has a well-established solution. If it does, do not solve that failure case, switch to another problem. If it does not, then the technique that solves this failure case is certain to be novel.

   > **note**
   > How to judge whether the current failure case already has a well-established solution:
   > 1. The first situation: a task with the same input and output already has a decent solution, and only some parts are still not done well enough.
   > 2. The second situation: a task whose input or output has changed somewhat already has a decent solution. Or several tasks in completely different data domains, whose technical core is the same, all already have decent similar solutions.
   > 3. The third situation: only one or two tasks in completely different data domains, whose technical core is the same, have a decent solution.
   > 4. The fourth situation: across tasks in various different fields, there are similar technical problems but none has a good solution.
   >
   > If you meet the first two situations, you must switch to another failure case, otherwise the project will be very boring and a struggle, wasting people's time and draining their enthusiasm for research.
   >
   > The third situation suits a beginner. The fourth suits an expert.

4. **Solving the problem.** How to improve your ability to design a solution: [https://www.notion.so/pengsida/pipeline-997f611cd2e24ef1a62210ff099948e2](https://www.notion.so/pengsida/pipeline-997f611cd2e24ef1a62210ff099948e2)

   <details>
   <summary>How to improve your ability to design a solution</summary>

   How to propose a novel and effective technique: first you have to know which techniques exist and what problems they solve. Then combine some of them.

   My own approach is: (1) build a challenge-insight tree. (2) Pick some techniques from the challenge-insight tree and solve the current task's technical challenge through a creative combination of them. (3) List all the possible pipelines, then compare their strengths and weaknesses and choose one.

   > **note** One strong researcher's view: the essence of technique is combining methods, combining small techniques into large ones, and combining old techniques into new ones.

   Combining existing techniques and digging out their properties on a new task and new data is a large contribution.

   The combination cannot be a fully A-plus-B combination of the form input → A → intermediate output → B → output, that is, a purely concatenated combination. The combination needs to be a creative one.

   Under normal circumstances, directly concatenating two methods will not solve the problem anyway; otherwise the problem would have no technical challenge.

   <details>
   <summary>The overwhelming majority of new techniques are examples of this (can you name a counterexample?)</summary>

   1. NeRF combined two techniques, occupancy network and differentiable rendering, on the task of reconstruction from images.
   2. EG3D combined three techniques, StyleGAN, GRAF and convolutional occupancy network, on the task of 3D GAN.
   3. DreamFusion combined two techniques, SDS loss and NeRF, on the task of text-to-3D.
   4. MVP combined two techniques, neural volumes and local radiance fields, on the task of image-based human reconstruction.

   </details>

   </details>

5. Validate the technical contribution on some data, and tune the results.

   > **note** Do not expect that a nice-sounding paper story and an interesting application will make reviewers let our technical contribution off.
   > See this document for details: [https://www.notion.so/pengsida/434a6b3e34d0403ca178fb0db2338232](https://www.notion.so/pengsida/434a6b3e34d0403ca178fb0db2338232)

<details>
<summary>A strong researcher's discussion of goal-driven research (this person does not recommend idea-driven research)</summary>

The source shows a screenshot of another researcher's page on problem-driven research. It is already in English and is not his text, so it is cited rather than copied in. Its argument is that PhD research means finding an important open problem and making significant progress on it, that starting from method design instead leaves the underlying problem vaguely defined, and that problem-driven research instead settles the problem, its motivation, why current methods cannot solve it, and how the proposed method addresses it, before looking for a method.

<details>
<summary>My own understanding of idea-driven research</summary>

Trying to propose a better technique on top of some existing technique makes it hard to have a clear goal, since what counts as a better technique is unclear, and it easily traps you inside the current task's setting, chasing numbers.

You should look at which milestone tasks the current technique still cannot solve, from the angle of reaching a general goal, rather than fixating on the technique's shortcomings in its current task setting. Being limited to chasing numbers narrows your view.

Do not improve a technique on its own existing setting, data or failure cases. In that situation the room for improvement is usually very small. Find new failure cases and start from those.

</details>

</details>

[Idea-driven research vs. goal-driven research](https://pengsida.notion.site/d9c6556326e84962a2d7ae190e2705af?pvs=25)

<details>
<summary>The benefits of goal-driven research for research output</summary>

The style of goal-driven research is to pursue an important task and try all sorts of methods to make that task work. By relaxing some conditions, you can always get some working results on an important task. That gives the project a guaranteed output.

Some people like to chase new techniques, single-mindedly tuning a new technique until it works. But our direction is an experimental science, and it is hard to establish whether a technique really works without a large number of experiments, which makes that way of doing research too risky.

</details>

<details>
<summary>A special case for coming up with ideas (important!! this case easily produces influential papers)</summary>

When a new hammer appears, it is very much worth taking that new hammer to one of the milestone tasks on your own roadmap, because that easily produces influential work.

> **note** Note, this is not about improving things within the new hammer's own task setting (for example tuning view synthesis results on NeRF's datasets within NeRF's task setting). It is about taking the new hammer to solve the problems in the milestone tasks you are working on. That is still goal-driven research.

<details>
<summary>There are many examples of this</summary>

1. When Transformer came out, it was taken and used for LoFTR.
2. When NeRF came out, it was taken and used for Neural Body.
3. When Stable Diffusion came out, it was taken and used for DreamFusion and DreamBooth.

What will the next new hammer be? What will the next example be?

</details>

</details>

<details>
<summary>Points to watch when coming up with ideas (which projects are not worth doing)</summary>

> **note** Proposing an idea and writing a paper is meant to make a real contribution to the field, not for the sake of the paper itself.
> If a paper contributes nothing to the field, then writing it is wasting your own time, because we will not gain the field's respect through it, and may even collect negative opinions.
> The benefits of writing that kind of paper: (1) you get familiar with the submission process. (2) There is a chance of getting a paper out of it, though the probability is fairly small.
> The costs: (1) wasted time. The time spent on that project could go to something more meaningful. (2) You may be judged negatively.

</details>

</details>

A point that needs particular attention: do not develop a mindset of depending on your advisor. Train the habit and the ability to do research independently. From one angle you could say this matters even more than publishing papers itself. And in fact you need this ability for a paper to be at all likely, otherwise the project is basically finished.

> **note** In fact an advisor can hardly find time to design a project's technical details, and the student needs to realise that the only way out is to think of the solution themselves.

~~If a student depends on their advisor to think of the detailed solution, that project is basically finished. Because an advisor cannot spend more than half of every day thinking about solutions, and can only give some intuitive, very rough ideas. In that situation, only the student can propose or refine a complete solution.~~

The struck-through text above is an outdated view. In my own opinion, the best advisor does research hands-on, is the student's partner, and does research together with the student. Advisor and student should compete with each other, to see who understands the research direction better.

The lab's experience in developing students' independent research ability, while doing a project: when a problem comes up, ask the student's own thinking first, encourage the student to have their own ideas (the solution to the problem, what to do next), and listen patiently to the whole of the student's thinking.

> **note** In a research project, the lab generally makes a large contribution in two areas: (1) thinking of important novel tasks, helping to find important research problems. (2) Reviewing the paper, suggesting some interesting experiments, applications and demos, and aiming to pick out every problem in the paper and give suggestions for improvement.

On building a solution to the problem, the lab generally makes three contributions:

1. Preventing the student's thinking from falling into a local minimum, encouraging and prompting the student to think more divergently and list more candidate solutions.
2. When the student's proposed solution has a technical flaw, or needs so many handcrafted tricks that its applicability is too narrow, the lab generally points out the matching problem and gives other possible rough solutions for the student to refine.
3. Helping the student improve their proposed solution, making it more beautiful.

The usual division of labour between advisor and student in a research project:

> **note** Notion's export scrambles this table's columns and drops the advisor cell on some rows. It is rendered here as item, advisor, student, with an empty advisor cell where the source has none.

| What a research project contains | Advisor | Student |
|---|---|---|
| 1. Think of an important task | The advisor's contribution here is large. The lab aims to build a long-term, important research goal for the student. | Student |
| 2. Think of the technical challenge or failure case that needs solving | Advisor | Student |
| 3. Judge whether the failure case already has a well-established solution | Advisor | Student |
| 4. Think of a solution to the problem | | Student |
| 5. Sort out the logic of the solution | Advisor (supporting) | Student (leading) |
| 6. Judge whether the solution is correct and novel | Advisor (supporting) | Student (leading) |
| 7. Design a simple experiment to quickly validate that the solution is correct | Advisor (supporting) | Student (leading) |
| 8. Improve the solution | Advisor (supporting) | Student (leading) |
| 9. Imagine more candidate solutions | Advisor (supporting) | Student (leading) |
| 10. Run experiments to tune the solution until it works | | Student |
| 11. Think about what to do next | | Student |
| 12. Get clear on what to do next | Advisor (supporting) | Student (leading) |
| 13. Set your paper's important internal deadlines from the paper's own deadline (comparison experiments, ablation study, introduction writing, method writing, abstract writing, experiment writing, related work writing). Normally, start writing at least one month before the deadline. | Advisor (supporting) | Student (leading) |
| 14. Write the paper | | Student |
| 15. Review the paper (list the missing experiments and the writing problems it has) | The advisor's contribution here is large. The lab will suggest some interesting experiments, applications and demos, aiming to pick out every problem and give suggestions for improvement. | Student |
| 16. Revise the paper | Advisor (supporting) | Student (leading) |
