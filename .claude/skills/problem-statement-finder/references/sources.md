# Sources

Checked live on 2026-11-03. Run `python scripts/radar.py check` for the current state. Everything below can be used without the script, by web fetch or `curl`.

## Papers

| Source | Key needed | Request |
|---|---|---|
| arXiv | No. Leave 3 s between requests | `https://export.arxiv.org/api/query?search_query=all:"term one" AND all:"term two"&start=0&max_results=25&sortBy=relevance` |
| arXiv full text | No | `https://arxiv.org/html/<id>`. Some papers have no HTML version |
| OpenAlex | No, though the free budget is shared per network. A personal key is free | `https://api.openalex.org/works?filter=title_and_abstract.search:term&per-page=25` |
| OpenAlex later work | Same | `https://api.openalex.org/works?filter=cites:W123,from_publication_date:2022-01-01&sort=cited_by_count:desc` |
| Semantic Scholar | Optional. The anonymous pool returned 429 on every attempt | `https://api.semanticscholar.org/graph/v1/paper/search?query=term&fields=title,year,abstract` |

OpenAlex stores abstracts as a word-position index. `radar.py` rebuilds them; by hand, sort the words by position.

## Reviews

| Source | Outcomes | Coverage | How |
|---|---|---|---|
| NeurIPS proceedings | Accepted only | 2013-2020 | `https://proceedings.neurips.cc/paper_files/paper/<year>/file/<hash>-Reviews.html`, or `-Review.html` for 2020. The hash comes from the year's listing page |
| SNOR dataset | **Accepted and rejected** | ICLR 2017 and 2019-2025, NeurIPS 2021-2024. Snapshot from July 2025 | [Zenodo record](https://zenodo.org/records/15866613), CC BY 4.0. About 2.2 GB in total |
| eLife | Published only | Older papers, life sciences | `https://api.elifesciences.org/articles/<id>` with `Accept: application/vnd.elife.article-vor+json;version=7`. See `decisionLetter` and `authorResponse` |

Things to know:

- **NeurIPS 2021 onwards** returned 404 for review pages.
- **Rejected papers in SNOR** are mostly in `failed_matches.jsonl`, not `normalized_papers.jsonl`, with their reviews embedded in `raw.details.directReplies`. Using only the main files would remove most rejected papers from the comparison.
- **eLife letters** contain names of editors in their standard text. Ignore these.
- **Newer eLife papers** use a reviewed-preprint model and may have no decision letter.
- **SNOR's rejected papers are mostly ICLR:** about 21,700 ICLR against about 670 NeurIPS. Compare accepted and rejected on ICLR. ICLR 2018 and NeurIPS 2025 are not in it, although its description lists them.
- **These are not random samples.** NeurIPS shows only winners. Say so when it matters.

## OpenReview live

Tested on 2026-11-03 as an anonymous client:

| Endpoint | Result |
|---|---|
| `/venues/search`, `/groups` | Public |
| `/notes`, on both API versions | `403 ChallengeRequiredError` |

OpenReview's API spec describes this as a Turnstile challenge against guest scraping. Do not try to pass it. Licensed reviews on OpenReview do not change that: its terms say the licence does not imply API readability, and that access rules must not be circumvented.

**With the user's own account.** It has not been verified that a token clears the challenge. Tell the user that, and have them set `OPENREVIEW_TOKEN` themselves. Never ask for the token in chat.

```bash
curl -s "https://api2.openreview.net/groups?id=ICLR.cc/2025/Conference"
curl -s -G "https://api2.openreview.net/notes" -H "Authorization: Bearer $OPENREVIEW_TOKEN" \
  --data-urlencode "content.venueid=ICLR.cc/2025/Conference/Rejected_Submission" -d "details=replies" -d "limit=25"
```

Reply names vary by year, so read `review_name` and `rebuttal_name` from the group first. Ignore `signatures` and anything else that identifies a person.

## Adding a field

If you know a venue in another field that publishes reviews openly, use it, and tell the user so they can suggest adding it here.
