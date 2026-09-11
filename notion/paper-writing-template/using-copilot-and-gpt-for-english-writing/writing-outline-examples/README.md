<!--
source: notion page 写作思路典例 (nested under 如何使用copilot和gpt辅助英语写作, under 论文写作模板)
source page id: c1a22465a0fa4b15a12985223916048e (root) -> 写作思路典例
source fetched: 2026-09-11
status: unverified (fable pass 1 done 2026-09-11, corrections applied after, re-check pending)
-->

# Worked Examples of Writing Outlines

> **Translator's note.** Two things about this page.
>
> First, the worked example is built from the draft text of a published paper, ManhattanSDF, *Neural 3D Scene Reconstruction with the Manhattan-world Assumption* (Guo et al., CVPR 2022). The original page lists that paper's own sentences one by one. This translation keeps Prof. Peng's planning notes and the shape of the outline, and describes what each sentence slot does instead of reprinting another author's prose. Open the paper alongside this page to see the sentence that fills each slot. Where a slot is one of his Chinese placeholders rather than a finished sentence, it is translated directly.
>
> Second, the source uses `->` between steps. It is kept wherever the source has it, and not added anywhere else.

## Introduction

### Outline at paragraph granularity

1. The problem to solve: scene reconstruction -> COLMAP works very well, describe how -> COLMAP works poorly on low-textured regions like floors and walls, give the specific reason.
2. Traditional methods: use planes to help scene reconstruction -> the pipeline is complicated, many parameters to tune -> the plane works poorly, so the reconstruction quality is poor.
3. Recent methods: NeRF, VolSDF and NeuS work very well on object reconstruction -> experiments show that they work poorly on indoor low-textured regions -> across a large low-textured region there are many geometries that can explain the images.
4. Our method: use semantics to help reconstruction, and optimise the semantic information while reconstructing -> `Specifically,` detect the floor and the walls and make them obey their semantic properties -> assume a Manhattan-world structure, so the normals of surface points on the floor and the walls obey the matching property; the wall normal is itself optimised -> given that the segmentation may be inaccurate, define a semantic MLP -> use multi-view consistency to improve the accuracy of the semantic segmentation, and at the same time optimise the segmentation probability with a geometric loss.
5. Experiments.

### Outline at sentence granularity

**The problem to solve**, three sentences:

1. The task and why it matters, naming applications.
2. What traditional methods do: estimate a depth map per image with multi-view stereo, then fuse the depth maps into 3D geometry.
3. The limitation and its cause: they struggle on low-textured regions such as indoor floors and walls, because matching is unreliable there.

**Traditional methods use a planar prior to improve results**, four sentences:

1. To overcome that problem, some methods use the planar prior to help reconstruction.
2. How they use the planar prior.
3. How the plane is modelled: triangulation `\cite{planar prior}`, superpixel `\cite{tapa}`, or learning-based plane segmentation methods `\cite{}`.
4. The limitation: they improve performance, but when depth estimation or plane segmentation is inaccurate they tend to perform poorly.

**Recent methods**, five sentences:

1. Recent work `\cite{SRN, NeRF, IDR}` represents 3D scenes as implicit neural representations, learned from images with differentiable renderers.
2. What IDR does -> although it produces high-quality reconstruction, it tends to fail on complex scenes -> the reason: surface rendering back-propagates gradients only at the surface point, so it is prone to local optima.
3. What the volume rendering methods `\cite{unsurf, volsdf, neus}` do instead, producing gradient signal at many points along a ray -> so they handle complex scenes without extra mask supervision.
4. The limitation this paper attacks: they still perform poorly in low-textured planar regions, with a forward reference to the paper's own experiments.
5. The technical reason: many possible 3D representations produce the same observed images, especially in low-textured planar regions.

**Our method**, four sentences:

1. What is proposed, in one sentence: an implicit neural representation encoding both geometry and semantics, for 3D reconstruction of indoor scenes.
2. The innovation in one sentence: use the semantic properties of planar regions to resolve reconstruction ambiguity, while optimising the estimated plane segmentation from geometric properties.
3. `Specifically,` how it works: an MLP predicts signed distance and colour for any 3D point, and given floor and wall segmentation, the signed distance field is forced to respect the matching geometric structure under the Manhattan-world assumption.
4. The follow-up problem and its answer: because inaccurate segmentation could mislead the optimisation, a further network predicts a semantic label per 3D point, jointly optimised through the geometric loss.

## Related work

**Depth map reconstruction.**

1. Frame the long-standing problem `\cite{point clouds, volumetric, MVS}`: recovering the underlying 3D shape of a captured scene from images with calibrated camera poses.
2. The two-stage pipeline, per-image depth estimation by multi-view stereo then depth fusion -> traditional multi-view stereo reconstructs very accurate shapes and is used in downstream applications `\cite{view synthesis, human reconstruction}` -> however it performs poorly on texture-less regions -> the reason: texture-less regions make dense feature matching intractable.
3. Works that improve the pipeline with deep learning -> `\cite{gift, loftr}` improved feature matching -> MVSNet builds a cost volume to predict the depth map.
4. Another line of works uses scene priors to help reconstruction -> using planes to help COLMAP-style scene reconstruction -> some works cited in Haoyu's earlier paper.

**Volumetric reconstruction.**

1. These methods predict the properties of points in 3D space directly.
2. What Atlas does.
3. What NeuralRecon does -> it reaches real-time reconstruction.
4. They represent scenes with discretised voxels, so memory consumption is high.
5. Recent methods `\cite{occupancy network, deepsdf, SRN, nerf, IDR, volsdf, neus}` represent scenes with neural implicit representations.
6. What IDR does.
7. What NeuS does.
8. They mostly present results on scenes with rich textures.

**Semantic segmentation.**

1. Deep learning based methods achieve impressive progress on semantic segmentation.
2. 2D semantic segmentation: what the CNN-based methods `\cite{deeplab, pspnet, ade20k, other work}` do -> how some methods use transformers to improve performance.
3. 3D semantic segmentation: `\cite{pointnet, pointnet++, other work}` develop networks for different representations of 3D data -> what `\cite{semantic nerf}` does.
4. Some methods exploit the relationship between 2D and 3D to improve the performance of both.

## Method

### Outline at sub-section granularity

1. Problem statement.
2. Overview of our method.
3. Volume rendering of signed distance fields.
4. Semantics-guided scene reconstruction.
5. Joint optimisation of semantics and geometry.

### Outline at sentence granularity

**Problem statement and overview**, five sentences:

1. The goal, given multi-view images with camera poses of an indoor scene.
2. A pointer to the overview figure.
3. What Section 3.1 covers: representing geometry and appearance with signed distance and colour fields, learned from images by volume rendering.
4. What Section 3.2 covers and why: semantic segmentation to find floors and walls, then geometric constraints from the Manhattan-world assumption.
5. What Section 3.3 covers and which weakness of 3.2 it answers: encoding semantics into the representation and jointly optimising them with geometry and appearance.

**Volume rendering of signed distance fields**, six sentences:

1. Contrast with multi-view stereo methods: the scene is modelled as an implicit neural representation learned with a differentiable renderer.
2. Credit the prior work the representation follows `\cite{idr, volsdf, neus}`.
3. Describe the geometry network: a 3D point maps to a signed distance, with the defining equation, then what implements it and what the geometry feature is.
4. Describe the colour network: which inputs it takes, with the equation, then how the normal is obtained as the gradient of the signed distance at the point.
5. Describe training the representation with volume rendering: credit the prior work being followed `\cite{volsdf, neus}` -> for one image pixel, sample N points along its camera ray -> predict signed distance and colour per point -> convert signed distance to density with Equation 1 -> get the colour with the volume rendering equation -> state the image loss.
6. Describe adding a depth map loss from COLMAP: report that the image loss alone reconstructs poorly, with a figure reference, and give the reason, that a view-dependent colour network can explain the images well even when the geometry is wrong -> in contrast, multi-view stereo mostly returns incomplete reconstructions but its recovered geometry is accurate -> the guidance loss using multi-view stereo depth maps, with its equation -> define each term -> state what improved and what did not, since the depth maps are themselves incomplete in texture-less planar regions, with a figure reference.

**Semantics-guided scene reconstruction**, seventeen sentences:

1. The observation that most texture-less planar regions lie on floors and walls.
2. What the Manhattan-world assumption says: floors and walls of indoor scenes align with three dominant directions.
3. What that means concretely: the floor is horizontal, walls are vertical to the floor and to each other.
4. Therefore, apply the geometric constraints to floor and wall regions.
5. `Specifically,` obtain the floor and wall regions with a 2D semantic segmentation network.
6. Then apply loss functions forcing surface points on a planar region to share one normal direction.
7. Introduce a predefined learnable normal for supervising the walls.
8. The wall loss, aligning or making vertical the normals of wall surface points against that learnable normal, with its equation.
9. Define its terms, the surface normal being the gradient of the signed distance at the point.
10. Note that the learnable normal is randomly initialised, jointly optimised with the network parameters, and converges stably to the ground-truth normal in experiments.
11. The floor assumption, alignment with the z-axis, correct in most scenes, and the floor normal loss.
12. Define its terms.
13. An extra geometric constraint, that floor surface points share one height, with its equation.
14. Define its terms, including the learnable scalar for floor height.
15. How that height is initialised, by clustering multi-view stereo point clouds in the floor region.
16. Note the height is also jointly optimised, then give the combined floor loss.
17. Define its remaining term, the coefficient weight.

**Joint optimisation of semantics and geometry**, eight sentences:

1. State what the geometric constraints achieved.
2. State the remaining problem: predicted 2D segmentation can be wrong in places, making the reconstruction inaccurate, with a figure reference.
3. The fix in one sentence: optimise the input semantic information together with scene geometry and appearance.
4. Credit the prior work `\cite{semantic nerf}` and state the mechanism: also predict semantic logits for any 3D point.
5. Describe what the logits represent: softmax over them gives the probability of the point being floor, wall or background, with the defining equation and what implements it.
6. Describe how the logits are rendered: volume rendering into 2D image space as with the image, the per-pixel equation, then softmax normalisation into multi-class probabilities.
7. Describe the joint optimisation with the normal, and its motivation: fold the class probabilities into the geometric losses from the previous section, give the combined loss, define its terms, then explain why it works, that a wrong segmentation makes its loss term unstable, so the optimiser drives that probability down and the wrong supervision signal is suppressed.
8. Describe learning the logits with a rendering loss: the supervision from the input segmentation with its equation, its terms, the observation that a 3D region is classified correctly in most camera views, and the conclusion that learning semantics in 3D naturally exploits multi-view consistency.
