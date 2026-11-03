# Access states

Each state means something different. Use the exact word when reporting.

| State | Meaning | What you can conclude |
|---|---|---|
| `retrieved` | Records were returned | They exist and are readable by this identity |
| `not_returned` | The source returned nothing | Nothing about existence. Readers may filter results |
| `inaccessible` | The source reports more replies than are visible | Records exist but are hidden from this identity |
| `no_record_exists` | The source explicitly says there is none | Absent at that source only |
| `not_declared_by_venue` | Venue config has no name for this reply type | Weak evidence that the stage did not exist |
| `permission_denied` | 403 | Reader rules apply. Not retried |
| `auth_required` | 401 | Needs an account. Not retried |
| `challenge_required` | Guest verification gate | Terminal for this identity. Not retried, not worked around |
| `api_unsupported` | The endpoint or parameter does not exist | A capability gap, not a data gap |
| `rate_limited` | 429 after bounded retries | Transient. Retry later |
| `retrieval_failed` | 5xx or timeout after retries | Transient. Use `--resume` |
| `malformed_response` | Response could not be parsed | Not "no data" |
| `not_requested` | Not attempted | Nothing |
| `not_configured` | Provider has no credentials or configuration | No search happened |
| `unknown` | Anything else | Nothing |

## When you hit `challenge_required`

Tell the user plainly, then offer these options. Let them choose.

1. **Own account token.** Set `OPENREVIEW_TOKEN`. The API then applies that account's reader permissions. Whether a token clears the guest gate has not been verified, so say so.
2. **User-supplied file.** See [the API notes](openreview-api-notes.md).
3. **Open sources.** Published reviews from NeurIPS and eLife, and the open SNOR dataset for ICLR, need no account. See the "Open sources" section of the skill.
4. **Stop here.** Use the public metadata that venue discovery provides, and do the literature work with arXiv and OpenAlex instead.

## Summary format

```
Venue: <edition> (API <version>; identity: <anonymous|own_account_token>)
Submissions: <collected> of <source total or "unknown">; state: <state>
Reviews: <n> records. Papers: <state>=<count>, ... (denominator <papers>)
Rebuttals, meta-reviews, decisions: same form
Completeness: supported / NOT supported, with reasons
Job: <id> <status>; resume with --resume <id> if relevant
```

Do not round states together into "available" or "missing".
