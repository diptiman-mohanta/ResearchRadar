# Output format

Keep to this order. The statements come first because they are what the user came for. The rest is what lets them trust it.

````markdown
# Problem statements: <topic>

**Assumed:** <scope you chose, in one line. They can correct it.>

**Funnel:** Read <N> papers and <N> reviews (<N> accepted, <N> rejected) -> <N> candidates -> <N> killed -> <N> statements

## 1. <Short title>

**Problem statement:** Two or three sentences: what is unsolved, in what setting, and why current approaches fall short.

**Why it matters:** What becomes possible if it is solved.

**Evidence**
- "<exact quote>" — review of <paper>, <venue year>, <accepted or rejected>, <link>
- "<exact quote>" — <paper>, conclusions, <link>
- Seen in <N> different papers. Gap type: <type>.

**Closest existing work:** <paper, year, link>, and what it leaves open.

**Strongest case against:** The best argument that this is not worth doing, in one or two sentences.

**Research question:** One question an experiment could answer.

**First experiment:** The smallest test worth running: data, baseline, metric.

**This idea is dead if:** The specific result that would show it is wrong or not worth pursuing.

**Fit:** How it matches what they told you about skills, data, compute or time. Leave this out if they told you nothing.

**Confidence:** Low, medium or high, and why. No numeric scores.

## What was killed

| Candidate | Why | Killed by |
|---|---|---|
| ... | ... | <named paper, or the reason> |

## What I could not check

- Sources that failed or were not used.
- Lenses that did not run.
- How much was read closely and how much was only skimmed.

## Next steps

Offer the one or two most useful: build the ICLR index, deepen with `novelty-auditor`, or develop a statement with `research-idea-lab`.
````

Write for the researcher. Label anything you inferred. A statement with an honest "low" confidence is more useful than a confident one you cannot support.

## Worked example

From a real run on 2026-11-03, for the topic "graph neural networks". Every quote was checked by script against its source. This shows the format and the standard of evidence. It was produced while developing the skill, not as an independent test, and it reports a quick pass: reviews were filtered by keyword rather than read in full.

---

# Problem statements: graph neural networks

**Assumed:** Graph-level and node-level prediction in machine learning. Say if you mean something narrower.

**Funnel:** Reviews of 42 accepted NeurIPS 2017-2020 papers, plus abstracts from 6 searches -> 4 candidates tested -> 2 killed, 1 early signal -> 1 statement

## 1. Are the gains of more expressive GNNs caused by expressiveness?

**Problem statement:** Many GNNs are designed to exceed the 1-WL expressiveness limit, yet one study finds that 1-WL already identifies almost all graphs in most standard datasets, and concludes that more expressive models are unnecessary. Another reports that expressive GNNs frequently generalise well. It is unresolved how much of the performance reported for these models comes from expressive power, and how much from other things that change with them, such as tuning, features or inductive bias.

**Why it matters:** A large line of work is justified by expressiveness. If the gains come from elsewhere, simpler models would do, and expressiveness theory needs a different link to prediction.

**Evidence**
- "it seems to me that the additional "power" of the DEGNN method is not due to the particular encoding proposed here, but instead comes from focusing on an easier problem." — [review of Distance Encoding](https://proceedings.neurips.cc/paper_files/paper/2020/file/2f73168bf3656f697507752ec592c437-Review.html), NeurIPS 2020, accepted
- "it is unclear why accurate counting matters in prediction tasks." — [review of Can Graph Neural Networks Count Substructures?](https://proceedings.neurips.cc/paper_files/paper/2020/file/75877cb75154206c4e65e76b88a12712-Review.html), NeurIPS 2020, accepted
- "experiments seem somewhat "constructed" in a way to fit the theory" — [review of How hard is to distinguish graphs with graph neural networks?](https://proceedings.neurips.cc/paper_files/paper/2020/file/23685a2431acad7789c1e3d43ea1522c-Review.html), NeurIPS 2020, accepted
- "more expressive GNNs are not necessary to achieve a good performances" — [1-WL Expressiveness Is (Almost) All You Need](https://arxiv.org/abs/2202.10156), 2022, conclusions
- "empirical evidence often contradicts this assumption, with expressive GNNs frequently demonstrating strong generalization." — [Towards Bridging Generalization and Expressivity of GNNs](https://arxiv.org/abs/2410.10051), 2024, abstract
- Seen in 3 different reviewed papers, plus a disagreement in the literature. Gap type: evidence.

**Closest existing work:** [1-WL Expressiveness Is (Almost) All You Need](https://arxiv.org/abs/2202.10156) tests whether expressiveness limits standard datasets. From its abstract and conclusions, it does not separate the sources of gain in models that do go beyond 1-WL.

**Strongest case against:** The 2022 result may already settle this for standard datasets, leaving only a question about harder real tasks. A direct test may also exist under vocabulary these searches missed.

**Research question:** On datasets where 1-WL already separates nearly all graphs, does a more expressive model still outperform a message-passing model given the same tuning budget and features?

**First experiment:** Pick 3 or 4 standard graph classification datasets that 1-WL separates. Compare a tuned message-passing GNN with a subgraph or higher-order GNN, under one hyperparameter budget. Metric: test accuracy over several seeds and splits.

**This idea is dead if:** The gains vanish under equal tuning on every dataset, which would answer the question with no new theory, or a published paper already ran this design.

**Confidence:** Low to medium. Three reviews and two papers point here, but only a few short searches were run, and the rejected-paper comparison did not run.

## What was killed

| Candidate | Why | Killed by |
|---|---|---|
| GNN comparisons are unfair because hyperparameters are not tuned | Addressed for node classification, after a reviewer raised it for pooling in 2020 | [Classic GNNs are Strong Baselines](https://arxiv.org/abs/2406.08993), 2024: earlier superiority "may have been overstated due to suboptimal hyperparameter configurations" |
| Training cost is not reported | 4 reviews mention it, but it looks like a reporting habit. Nothing shows that it changes conclusions | Reason, not a paper. One search only |

**Early signal, not a statement:** Whether GNN attacks and defences use realistic threat models. One review says "it's not clear what is a reasonable threat model in practice" ([GNNGuard](https://proceedings.neurips.cc/paper_files/paper/2020/file/690d83983a63aa1818423fd6edd3bfdb-Review.html)). That is one quote, and the search was too noisy to judge.

## What I could not check

- Reviews of rejected papers: the ICLR index was not built, so accepted versus rejected did not run.
- Semantic Scholar: rate limited, so not searched.
- Reviews after 2020: not used, because NeurIPS stopped publishing them.
- Future Directions in the Theory of Graph Machine Learning (2024) looks relevant, and was not read.
