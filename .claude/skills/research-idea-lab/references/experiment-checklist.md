# Experiment checklist

## Question and design

- [ ] Could a result of this experiment actually disprove the hypothesis?
- [ ] Do the hypotheses predict different observations? If not, the experiment cannot separate them.
- [ ] Are the metric and the decision threshold fixed before running?

## Baselines and controls

- [ ] A trivial baseline, to show the task is not easy.
- [ ] The current best method, with its published settings, re-run under your protocol.
- [ ] A negative control, where the effect should not appear.
- [ ] An ablation for each new component. If removing it changes nothing, it does nothing.

## Data

- [ ] Are the data available and licensed for this use?
- [ ] Is the split fixed, and leakage checked?
- [ ] More than one dataset, if you plan to claim generalisation.
- [ ] Do you know how the data differ from real conditions?

## Statistics

- [ ] Several seeds, with variation reported and not just the best run.
- [ ] Confidence intervals or a suitable test.
- [ ] Multiple comparisons considered.
- [ ] Hyperparameter search is the same for baselines and the proposed method.

## Staging

Order the work so that the cheapest informative test comes first.

| Stage | Purpose | Continue only if |
|---|---|---|
| 0 | Reproduce a baseline | Results match the published ones within a stated tolerance |
| 1 | Minimum viable experiment | The direct prediction holds at small scale |
| 2 | Ablations and controls | The effect comes from the proposed mechanism |
| 3 | Scale and other datasets | The effect survives |

## Falsification and stopping

Weak: "if the results are not good."

Strong: "if the mean improvement over the baseline across 5 seeds is below 1 point on two of three datasets, H1 is rejected for this setting."

Write stop conditions now, while you have no results to protect.
