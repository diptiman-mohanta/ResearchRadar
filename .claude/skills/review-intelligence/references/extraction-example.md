# Extraction example

The review and rebuttal below are invented to show the format.

**Review:** "The evaluation uses only one dataset, so the generalisation claim is not supported. Why was no baseline with dense attention reported? The derivation in section 3 is elegant. I would prefer a shorter introduction."

**Rebuttal:** "We added two further datasets in Table 4, which show the same trend. The issue of the dense baseline is resolved."

## Items

| # | Quote | Claim (your words) | Category | Claim type | Severity | Confidence | Response |
|---|---|---|---|---|---|---|---|
| a | "The evaluation uses only one dataset, so the generalisation claim is not supported." | The generalisation claim rests on a single dataset | generalisation | factual_criticism | 3: generalisation is a main claim | 0.9 | partially_addressed |
| b | "Why was no baseline with dense attention reported?" | Asks why no dense-attention baseline was reported | experimental | question | | 0.9 | indeterminate |
| c | "The derivation in section 3 is elegant." | Praises the derivation in section 3 | theoretical | positive_observation | | 0.9 | not_applicable |
| d | "I would prefer a shorter introduction." | Prefers a shorter introduction | presentation_clarity | preference | | 0.9 | not_applicable |

## Rebuttal links

| Item | Rebuttal quote | Status | Authors claim resolved? | Evidence in text? | Why |
|---|---|---|---|---|---|
| a | "We added two further datasets in Table 4, which show the same trend." | partially_addressed | No | Yes | New datasets respond directly, but the text reports a trend rather than a tested claim |
| b | "The issue of the dense baseline is resolved." | indeterminate | Yes | No | Authors assert a resolution, with no result shown |

Notice:

- Item b stays `indeterminate` despite the author's claim of resolution.
- Item d is kept as evidence, but as a preference it can never support a gap.
- The claim is new wording; the quote is exact.
