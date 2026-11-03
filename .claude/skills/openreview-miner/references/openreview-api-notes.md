# OpenReview API notes

Checked 2026-11-03 against `api2.openreview.net/docs/api.yml`, the official guides and live responses.

## What was observed

| Thing | v1 (`api.openreview.net`) | v2 (`api2.openreview.net`) |
|---|---|---|
| `/groups?id=` | Public | Public |
| `/venues/search` | 404, does not exist | Public |
| `/invitations?id=` | Public, but empty for many | Public, but empty even for invitations known to exist |
| `/notes` as guest | 403 `ChallengeRequiredError` | 403 `ChallengeRequiredError` |
| Note `content` | Plain values | Wrapped as `{"value": ...}` |
| Note invitation | `invitation` string | `invitations` list |

**Reading notes with a token has not been tested,** because no account was available.

## Names vary by edition

Read from venue group content, never assumed:

- `review_name`, `meta_review_name`, `decision_name`, `rebuttal_name`
- ICLR 2024 declares no rebuttal name. ICLR 2025 and 2026 use `Rebuttal`. ICLR 2027 uses `Author_Rebuttal`.
- ICLR 2020 to 2023 groups have empty content, and no conventional invitation could be confirmed as a guest. Treat these as unresolved unless the user knows the names.

## Getting a token (user's own account)

```python
import openreview
client = openreview.api.OpenReviewClient(baseurl="https://api2.openreview.net")  # reads OPENREVIEW_USERNAME and OPENREVIEW_PASSWORD
print(client.token)
```

Do not handle passwords. Ask the user to run this themselves and set `OPENREVIEW_TOKEN`. Never ask for the token in chat.

## The file route

The documented retrieval with the official client, under the user's own account:

```python
import json, openreview
client = openreview.api.OpenReviewClient(baseurl="https://api2.openreview.net")
venue = "ICLR.cc/2025/Conference"
group = client.get_group(venue)
name = group.content["submission_name"]["value"]
notes = client.get_all_notes(invitation=f"{venue}/-/{name}", details="replies")
json.dump([n.to_json() for n in notes], open("notes.json", "w"))
```

Then read `notes.json` directly. Ignore `signatures`, `tauthor`, `writers` and anything else that identifies a person, and do not copy those fields into your results. A file has no source total, so it cannot support a completeness claim on its own.

## Terms

From openreview.net/legal/terms: metadata is CC0 and reviews are CC BY 4.0, but the licence "does not imply" that records are readable through the API, and access rules must not be circumvented. Keep whole reviews local; quote briefly, with links.
