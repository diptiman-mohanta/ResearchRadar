# Search playbook

One query proves little. A field may use different words for your idea, and the first paper on it may be old.

## Query kinds

Tag each query with one of these. The verdict rules check them.

| `kind` | Purpose | Example, for an idea about pruning attention heads during training |
|---|---|---|
| `problem` | The problem, without your method | "reducing inference cost of transformer models" |
| `mechanism` | The method, without your vocabulary | "removing attention heads during training" |
| `synonym` | Other names | "head pruning", "attention sparsification", "multi-head reduction" |
| `adjacent_field` | The same idea elsewhere | "channel pruning convolutional networks", "feature selection during training" |
| `foundational` | Old roots | "optimal brain damage", "network pruning" |
| `disconfirming` | Evidence against your claim | "pruning does not improve", "lottery ticket fails transformers" |

**A `potentially_underexplored` verdict needs answered `foundational` and `disconfirming` queries.**

## Provider notes

| Source | Needs | Notes |
|---|---|---|
| `arxiv` | Nothing | Preprints only, and not a peer-review source. 3 s between requests, so large plans are slow |
| `openalex` | Nothing | Broad, with citations. The free budget is shared per network |
| `semantic_scholar` | Optional `S2_API_KEY` | The anonymous pool is shared, and often returns 429. That means not searched |
| Web search | Your agent's own tool, if it has one | Useful for adjacent fields. Check what it returns against the source |

Do not imply a search happened when its status says otherwise. If a key source is missing, say what that leaves unchecked.

## Going further

- Citations cut across vocabulary. `radar.py citing W123` finds later work.
- Read the related-work sections of the closest papers you find.
- If several phrasings return the same few papers, you may be near the boundary of that vocabulary. Try another field's words before concluding anything.
- Check recent work too. The newest papers may be preprints, and may have appeared since the idea was first written.
