# Six lenses for finding gaps

Use each lens separately, so that one strong signal does not hide the rest. A candidate found through two or more lenses is usually the strongest.

## 1. What reviewers keep raising

Look for the same specific criticism across different papers.

- Strong: "reviewed on one dataset" appears for 6 different papers across 3 years, for the same underlying reason.
- Weak: "needs more baselines" appears everywhere. Ask whether meeting the demand would change any conclusion.

Split each review into separate items first, and tag each one:

| Tag | Counts towards a gap? |
|---|---|
| Factual criticism: says something checkable | Yes |
| Methodological concern: doubts soundness | Yes |
| Requested experiment: asks for specific work | Yes, as weak evidence. A request does not prove the need |
| Question | No, but may be a lead |
| Speculation: "this probably overfits" | No |
| Preference: "I would prefer a shorter introduction" | No |
| Praise | No, though it shows what the field values |

## 2. Accepted versus rejected

Only possible with the ICLR index. If it is not built, say this lens was not run.

Compare accepted with rejected, as `--outcome both` does. Authors withdraw papers for many reasons, so analyse withdrawn papers separately, if at all.

- **Tolerated flaws.** A weakness raised against accepted papers too. The field lives with it, so it may be hard rather than careless. Often the most interesting signal.
- **Fatal flaws.** Raised mainly against rejected papers. May show a standard the field enforces, which is less often a research gap.
- **Good ideas, rejected.** Reviewers liked the idea and rejected the execution. Someone may do it properly.

Treat every pattern here as a lead. Samples are small, and many other things decide acceptance. Never present this as predicting acceptance.

## 3. What authors admit

From `radar.py limits`: limitations sections, future work, conclusions, and "we did not" sentences.

- Strong: several groups stop at the same wall, and say why.
- Weak: boilerplate future work ("we plan to test more datasets").

## 4. Where results disagree

Papers reporting opposite results on similar questions. The disagreement is often the problem statement: what condition explains it?

Example form: one paper finds an effect, and another finds none. What differs: data, metric, assumptions?

## 5. Assumptions nobody tests

Something everyone assumes, imports from another area, or takes from one old paper.

- Ask: what is assumed in every paper's setup, and what evidence is there for it?
- Look for reviewers asking "why assume this?" and for papers that cite one source for a central assumption.

## 6. Benchmark versus reality

Methods that do well on standard benchmarks and were never tested in the conditions they claim to serve: scale, noise, distribution shift, cost, real users.

- Look for reviewers or authors saying results may not transfer.
- Check whether anyone has actually measured the difference.

## Types of gap

Name the type in each statement. It tells the reader what kind of work would close it.

| Type | The problem is |
|---|---|
| Evidence | Results conflict |
| Knowledge | Something has simply not been studied |
| Method | Existing methods cannot answer the question |
| Empirical | A claim has not been tested in practice |
| Theory | No explanation for an observed result |
| Population or setting | It works somewhere, and is untested elsewhere |
| Practice | Known in research, not usable in reality |

## Reviewer concern or real gap?

Before keeping a candidate, ask:

| Explanation | Check |
|---|---|
| Reviewing fashion | Would meeting the demand change any conclusion? |
| Venue checklist | Does it appear only at one venue, or only after a rule change? |
| Local weakness | Do stronger papers avoid it easily? |
| Already solved | Search later work |
| Selection bias | Whose reviews are readable, and whose are not? |
| One research group | Do the supporting papers share authors? |
