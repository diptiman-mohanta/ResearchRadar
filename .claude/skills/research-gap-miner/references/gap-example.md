# Gap format

The content is invented to show the format.

```markdown
## Node classification methods are rarely evaluated under structured label noise

**Scope:** Semi-supervised node classification on citation and product graphs.
**Excludes:** Graph-level tasks, and synthetic uniform noise.
**Category:** robustness

**Supporting evidence** (3 independent works, 2 venues, 2023-2025; none share authors)
- "<exact quote>" — review of <paper>, <venue year>, <link>
- "<exact quote>" — review of <paper>, <venue year>, <link>
- "<exact quote>" — review of <paper>, <venue year>, <link>

**Contradicting evidence**
- <Paper, year, link>: this benchmark does include structured noise.

**Later work:** Partly resolved. <Paper, year, link> addresses it for one dataset family.

**What I searched for counterevidence:** arXiv and OpenAlex for structured noise benchmarks, on <date>. Citing papers checked for two of the three works. Semantic Scholar was rate limited, so not searched.

**Reviewer concern or real gap?** Could be a reviewer habit, but authors concede it with reasons, and the later benchmark shows that results change under this noise.

| Dimension | Rating | Why |
|---|---|---|
| Evidence strength | medium | Three independent works and one benchmark, but only public reviews were visible |
| Scientific importance | medium | Real graph labels often have structured noise, so reported rankings may not transfer |
| Persistence | medium | Partly addressed; no general treatment found in the searches run |
| Tractability | high | Benchmarks and noise models exist |

**Status:** candidate, not established.

**Coverage limits:** Only ICLR 2023 to 2025 were covered. Reviews are visible for a minority of submissions.
```

To abstain:

```markdown
**No solid gap found.** Only 2 independent works raise this, and both share an author. Coverage is 8% of papers. More reviews from <venues> would help.
```
