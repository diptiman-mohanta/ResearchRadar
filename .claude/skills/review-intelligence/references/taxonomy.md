# Taxonomy

## Category: what the item is about

| Value | Use for |
|---|---|
| `experimental` | Experiment design, datasets, baselines, metrics, sample size |
| `methodological` | Soundness of the approach or analysis |
| `robustness` | Sensitivity to seeds, noise, hyperparameters, perturbations |
| `generalisation` | Whether results extend beyond the tested setting |
| `theoretical` | Proofs, assumptions, formal claims |
| `reproducibility` | Code, data availability, enough detail to repeat |
| `novelty_positioning` | Relation to prior work, claims of contribution |
| `presentation_clarity` | Writing, structure, figures |
| `ethics_safety` | Ethical or safety concerns |
| `other` | None of these. Say why in `evidence_notes` |

## Claim type: what kind of statement it is

| Value | Test | Example form |
|---|---|---|
| `factual_criticism` | Asserts something checkable about the paper | "The baseline uses a different split." |
| `methodological_concern` | Doubts a method's soundness, without a checkable fact | "This metric may hide the failure cases." |
| `requested_experiment` | Asks for specific additional work | "Please add a seed sensitivity study." |
| `question` | Genuinely asks, without asserting a flaw | "Why was this baseline excluded?" |
| `unsupported_speculation` | Guesses, without evidence | "This probably overfits." |
| `positive_observation` | Praises or notes a strength | "The derivation is elegant." |
| `preference` | Taste or style | "I would prefer a shorter introduction." |
| `other` | None of these | |

Only `factual_criticism`, `methodological_concern` and `requested_experiment` can later support a research gap.

## Severity (optional, 1 to 4)

| Value | Meaning |
|---|---|
| 1 | Minor: does not affect the conclusions |
| 2 | Moderate: weakens part of the argument |
| 3 | Major: a main claim is significantly weakened |
| 4 | Critical: undermines the main claim |

A severity needs a written rationale. Do not give one for questions, preferences or strengths. It reflects how serious the reviewer's point would be if true, not whether it is true.

## Response status

| Status | Requires |
|---|---|
| `addressed` | A link with status `addressed` and `evidence_in_text: true`, and no indeterminate link |
| `partially_addressed` | At least one link |
| `unaddressed` | A retrieved rebuttal that does not respond to this item, and no links |
| `indeterminate` | Default. Use for ambiguity, missing evidence, conflicting links, or no retrieved rebuttal |
| `not_applicable` | Required for `positive_observation`; also for other items needing no response |

Link statuses can only be `addressed`, `partially_addressed` or `indeterminate`.

On each link, record separately:

- `claims_resolution`: the authors say it is resolved.
- `evidence_in_text`: the text gives evidence such as new results or a concrete change.

"We fixed this" sets the first and not the second.
