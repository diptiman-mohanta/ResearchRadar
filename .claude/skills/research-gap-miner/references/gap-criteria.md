# Telling a reviewer concern from a scientific gap

Repetition has many causes. Work through these before calling something a gap.

## Reasons a recurring complaint may not be a gap

| Explanation | How to check |
|---|---|
| Reviewing norm or fashion ("add more baselines") | Would meeting the demand change any conclusion? |
| Venue template or checklist effect | Does it appear only at one venue, or only after a rule change? |
| Local weakness of those papers | Do stronger papers in the area avoid it easily? |
| Already solved, and reviewers are behind | Search later work and citing papers |
| Selection bias | Only some reviews are public. Which reviewers, papers and outcomes are visible? |
| Same group of authors | Check whether the papers share authors |

## Signs it may be a real gap

- Independent works hit the same limitation for the same underlying reason.
- It appears across venues, years, datasets and method families, not just one.
- Serious attempts exist and fall short. Authors concede it in rebuttals with reasons, not just as politeness.
- A credible mechanism explains why it is hard.
- Closing it would change what can be concluded or built.

## Rating each dimension separately

Give each a rating (`low`, `medium`, `high` or `unknown`) and written reasons. Do not combine them.

| Dimension | Question |
|---|---|
| Evidence strength | How well do the spans and later work support the claim? |
| Scientific importance | If true and closed, what would change? |
| Persistence | Is it still open? Needs a later-work check. Otherwise `unknown` |
| Tractability | Could it plausibly be attacked with available data and methods? |

A gap can be important and weakly evidenced at the same time. Say so rather than averaging.

## `later_work_status`

| Value | Needs |
|---|---|
| `not_checked` | Forces `verification_status: hypothesis` and `persistence: unknown` or `low` |
| `no_resolution_found` | At least one search that answered. Means "not found", not "does not exist" |
| `partially_resolved` | An answered search and `later_work` evidence |
| `appears_resolved` | An answered search and `later_work` evidence. Usually means this is not a gap |

## Writing the coverage limitations

Always state:

- Papers in scope, and how many have review text.
- Access states that reduced coverage.
- That readable reviews are a selected sample.
- Which venues and years were not covered.
