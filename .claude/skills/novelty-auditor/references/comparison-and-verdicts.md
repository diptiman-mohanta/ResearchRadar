# Comparison and verdicts

## Comparing a closest work

All fields are required for each work. Compare against the proposal, not just describe the paper.

| Field | Question |
|---|---|
| `research_problem` | Same problem? |
| `task_and_setting` | Same task, and same setting? |
| `assumptions` | Same assumptions? A difference here may be the real contribution |
| `mechanism` | Does it work in the same way? |
| `architecture_or_objective` | Same architecture or training objective? |
| `data_and_supervision` | Same data and supervision? |
| `evaluation_protocol` | Evaluated in the same way? |
| `claimed_contribution` | What do they claim? |
| `limitations_and_differences` | What did they not do, and what is different from the proposal? |

## Precedent kinds

| Kind | Meaning |
|---|---|
| `direct_precedent` | Same problem, equivalent mechanism and assumptions |
| `partial_precedent` | Overlaps substantially, but differs in a meaningful part |
| `adjacent_precedent` | Related problem or field, and the idea could transfer |
| `counterexample` | Evidence against the idea's premise or expected result |

## Verdicts

A verdict needs its requirements met. If they are not, use a weaker verdict.

| Verdict | Requires |
|---|---|
| `already_explored` | At least one `direct_precedent` |
| `partially_explored` | At least one `direct_precedent` or `partial_precedent` |
| `potentially_underexplored` | No direct precedent; at least 3 compared works; at least 2 sources that answered; answered `foundational` and `disconfirming` queries. These thresholds are rules of thumb |
| `insufficient_evidence` | Nothing further. Always available |

`potentially_underexplored` does not mean novel. It means a serious search did not find it. It needs expert review.

## Recommendations

| Value | Use when |
|---|---|
| `reject` | The closest work already does this |
| `narrow` | Part of it is taken. A smaller claim may survive |
| `reformulate` | The framing is the problem, or the evidence is too thin to judge |
| `proceed_to_expert_review` | The search found no direct precedent. A human who knows the field should now check |

## Writing the verdict

Avoid these.

| Do not write | Write |
|---|---|
| "This is novel." | "No direct precedent was found in these searches." |
| "An exhaustive search shows..." | "This was not exhaustive: these queries, these providers, on this date." |
| "This does not exist." | "I did not find this." |
| "Novelty score: 8/10." | Reasoning only. |
| "No results, so the idea is new." | "No results for this phrasing. Other vocabularies remain unchecked." |

## Example fragment

```markdown
**Closest work:** <Exact title>, 2021, ICLR 2021, arXiv:2101.00000. Partial precedent.

| Dimension | Compared with the proposal |
|---|---|
| Research problem | Same problem |
| Task and setting | Same task; different dataset scale |
| Assumptions | Assumes fixed head count; the proposal does not |
| Mechanism | Prunes after training rather than during it |
| Architecture or objective | Same architecture; no sparsity term |
| Data and supervision | Supervised, on ImageNet |
| Evaluation protocol | Top-1 accuracy against parameter count |
| Claimed contribution | Post-training pruning preserves accuracy |
| Limitations and differences | Does not study pruning during training, which is the proposal's only real difference |

**Genuinely different:** Pruning during training rather than after it. Possibly meaningful, because it could change what is learned. Not established.

**Verdict:** partially_explored. One close partial precedent differs only in when pruning happens, so the contribution is narrow at best.

**Recommendation:** narrow.

**Coverage:** Not exhaustive: six queries on arXiv and OpenAlex on <date>. Semantic Scholar was rate limited and not searched.

**Unresolved:** Vision-specific vocabulary may hide further work.
```
