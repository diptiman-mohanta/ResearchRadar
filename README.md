# ResearchRadar – AI Research Assistant for Research Gap Discovery

**ResearchRadar is an open-source AI research assistant that helps researchers discover research gaps, analyse academic peer reviews, generate evidence-backed research problem statements, and evaluate the novelty of research ideas.**

Built using portable AI agent skills for Claude Code and other Agent Skills-compatible assistants, ResearchRadar combines academic literature search, peer-review intelligence, research limitation analysis, and adversarial novelty auditing into one research workflow.

Instead of generating research ideas from generic AI knowledge, ResearchRadar investigates what researchers have published, what reviewers have criticised, which limitations recur across independent papers, and whether proposed research directions have already been explored.

### What can ResearchRadar do?

- **AI Literature Review:** Discover and organise relevant academic papers.
- **Peer Review Analysis:** Extract reviewer criticisms, questions, strengths, and rebuttal evidence.
- **Research Gap Discovery:** Identify recurring limitations across independent research papers.
- **Research Problem Generation:** Develop testable research questions and hypotheses.
- **Research Novelty Checking:** Find the closest prior work and challenge novelty claims.
- **Research Intelligence:** Produce evidence-backed research reports with traceable sources and explicit uncertainty.

ResearchRadar is designed for PhD students, academic researchers, research engineers, and scientists looking for more rigorous ways to identify and validate research opportunities.

If this is useful to you, please [give it a star](https://github.com/diptiman-mohanta/ResearchRadar) ⭐ so that other researchers can find it.

## What you get

Abridged from a real run on 2026-11-03. Most of it is the skill's own wording, and every quote was checked by script against its saved source.

```
> /problem-statement-finder continual learning of asr

Assumed: ASR means automatic speech recognition, with ordinary GPU access and
public speech datasets only. Tell me if not.

Funnel: Read 52 papers and the review pages of 52 papers (52 accepted, 0 rejected)
        -> 12 candidates -> 8 killed or folded in, 2 kept as early signals -> 2 statements

1. Do ASR continual-learning rankings survive tuning you could actually deploy?

   Evidence: papers set the same crucial setting in incompatible ways
   - "we sweep through the hyper-parameters to optimize average word error rate"
       CL Optimizations for Auto-regressive Decoder, 2024
   - "Hyper-parameters are tuned using the validation sets on the first adaptation."
       Inverse-Hessian Regularization, 2026
   - "how baselines are tuned" is among the causes of "huge variations in performance"
       review of Improved Schemes for Episodic Memory, NeurIPS 2020

   Strongest case against: a vision study found that fitting hyperparameters on
   the first task "performs comparably to any other", which may also hold for ASR.

   Also includes: closest work, research question, first experiment, what would
   kill the idea, and a confidence rating with reasons.

What was killed
   "Unknown task boundaries": already studied in ASR (named papers, with links)

What I could not check
   Semantic Scholar was rate limited. NeurIPS reviews stop at 2020. Most full
   texts were keyword-searched, not read in full.
```

Then you can go deeper in the same chat. Asking for the accepted-versus-rejected comparison gave this, from 187 accepted and 329 rejected continual-learning papers at ICLR 2019-2025:

| Reviewers raised | Accepted | Rejected | Reading |
|---|---|---|---|
| How methods were tuned | 14% | 12% | Tolerated: the field lives with it |
| Task order | 7% | 7% | Tolerated |
| Memory or buffer size | 10% | 18% | Leans rejected |

It also found real reviews of a rejected ICLR 2025 speech paper, which asked for "an analysis of language relationships and similarities". These counts are keyword-based leads, and the run said so.

Asking for a novelty audit on the second statement gave the verdict `partially_explored`, with the recommendation to narrow it. It named the closest paper, compared it in detail, and warned that "several groups are close".

## Install

### What you need

| Needed | Why |
|---|---|
| [Claude Code](https://claude.com/claude-code), or another agent that reads [Agent Skills](https://agentskills.io) | Runs the skills |
| [Python 3.10 or newer](https://www.python.org/downloads/) | Runs the helper script. No packages to install |
| [Git](https://git-scm.com/downloads) | To download this repository |
| An internet connection | To search for papers and fetch reviews |

No API keys and no paid services are needed.

### What gets downloaded

| What | Size | When | Where |
|---|---|---|---|
| This repository | Under 1 MB | When you clone it | Wherever you run `git clone` |
| NeurIPS paper listings | A few MB | Automatically, the first time they are needed | `~/.cache/problem-statement-finder` |
| Rejected-paper reviews: [open review dataset](https://zenodo.org/records/15866613) (optional) | 2.2 GB download, 1.5 GB on disk. Took about 40 minutes when tested | Only if you run the command in step 3 | `~/.cache/problem-statement-finder` |

Without the optional dataset everything else still works, but the accepted-versus-rejected comparison does not run. The skill tells you when this is the case.

### Step 1: Copy the skills

**macOS, Linux or Git Bash:**

```bash
git clone https://github.com/diptiman-mohanta/ResearchRadar.git
mkdir -p ~/.claude/skills
cp -r ResearchRadar/.claude/skills/* ~/.claude/skills/
```

**Windows PowerShell:**

```powershell
git clone https://github.com/diptiman-mohanta/ResearchRadar.git
New-Item -ItemType Directory -Force "$HOME\.claude\skills"
Copy-Item -Recurse -Force ResearchRadar\.claude\skills\* "$HOME\.claude\skills\"
```

### Step 2: Check it works

```bash
python "$HOME/.claude/skills/problem-statement-finder/scripts/radar.py" check
```

This shows which sources are responding. If `python` is not found, use `python3`. It is normal for `semantic_scholar` to say `rate limited`, and for `iclr_index` to say `not built` until you do step 3.

### Step 3: Add rejected-paper reviews (optional, recommended)

```bash
python "$HOME/.claude/skills/problem-statement-finder/scripts/radar.py" iclr-build --yes-download-2.2gb
```

Leave it running until it finishes. If the connection drops, run it again, and it starts over.

### Step 4: Run it

Start a new Claude Code chat and type your topic after the command:

```
/problem-statement-finder continual learning of asr
```

### Other install options

**Claude Code plugin.** This has not been tested yet. Installed this way, the command is `/researchradar:problem-statement-finder`.

```
/plugin marketplace add diptiman-mohanta/ResearchRadar
/plugin install researchradar
```

**Update:** run `git pull` in your `ResearchRadar` folder, then repeat step 1's copy command.

**Uninstall:** delete the six skill folders listed under [The skills](#the-skills) from `~/.claude/skills`, and delete `~/.cache/problem-statement-finder`.

## Use

Put the topic after the command, or just ask in your own words:

```
/problem-statement-finder graph neural network oversmoothing
find me a research gap in federated learning
what should I work on for my PhD in protein structure prediction?
```

It does not interview you. It states what it assumed, and you can correct it. Mention your skills, data, compute or deadline if you want the statements to fit them.

Then continue in the same chat:

```
Rerun the accepted-versus-rejected lens
Run novelty-auditor on statement 2
Take statement 1 to research-idea-lab
```

**Expect a thorough run to take a while.** It reads many papers and waits between requests. Long runs can also hit the free rate limits of arXiv and OpenAlex. When that happens it reports the search as not done, rather than as finding nothing, and you can ask it to retry later.

## How it works

| Step | What happens |
|---|---|
| 1. Gather | Finds papers on arXiv and OpenAlex, and reads what authors admit in their limitations sections |
| 2. Read reviews | Reads real reviews from the open sources below, plus anything you paste |
| 3. Extract | Pulls specific criticisms with exact quotes. Questions, preferences and praise are kept apart |
| 4. Mine | Looks through six lenses, such as what reviewers keep raising, or weaknesses tolerated even in accepted papers. Counts different papers, not comments |
| 5. Kill | Tries to prove each idea already solved or not worth doing. "Already solved" needs a named paper |
| 6. Craft | Writes survivors with a research question, a first experiment, and the result that would kill the idea |

## Where the reviews come from

| Source | Papers | Coverage | Setup |
|---|---|---|---|
| NeurIPS proceedings | Accepted | 2013-2020 | None |
| eLife | Published | Life sciences, older papers | None |
| [SNOR dataset](https://zenodo.org/records/15866613) (CC BY 4.0) | 23,439 accepted, 16,972 rejected, 5,933 withdrawn, 167 desk rejected, 291 others | ICLR 2017 and 2019-2025, NeurIPS 2021-2024 | Step 3 above |
| Anything you paste | Whatever you have | Any field | None |

Many fields have no open review source yet. Speech venues such as Interspeech and ICASSP publish no reviews that the skill can reach. In those cases it uses reviews from nearby fields, or works from papers alone, and says so.

**OpenReview's live site is not used.** It puts a human-verification check in front of anonymous reads, and this tool does not try to get around it.

## What it will not do

- Invent a paper, quote or link.
- Call something novel because a search found nothing.
- Give a made-up score.
- Try to work out who a reviewer is.

## The skills

`problem-statement-finder` does the whole job. The others go deeper on one step, and are useful on their own:

| Skill | Use it to |
|---|---|
| **`problem-statement-finder`** | **Go from a topic to problem statements** |
| `openreview-miner` | Find out which reviews can be collected, and how complete they are |
| `review-intelligence` | Turn reviews and rebuttals into checkable evidence |
| `research-gap-miner` | Analyse limitations recurring across papers |
| `research-idea-lab` | Turn a gap into hypotheses and an experiment plan |
| `novelty-auditor` | Check rigorously whether an idea has been done |

## Honest limits

- **Quality has not been measured.** It has had a few real runs by its maintainers, on Windows with Python 3.10. There is no benchmark and no independent evaluation yet.
- **Coverage is uneven.** It is strongest in machine learning, and the review data is not a random sample. NeurIPS published reviews of accepted papers only, and rejected papers are nearly all from ICLR.
- **Reviews stop at 2020 without the dataset,** and at mid-2025 with it. Newer work comes from paper searches, and much of that is preprints.
- **Withdrawn papers are labelled `rejected`** in the script's `outcome` field. Check the `decision` field to tell them apart.
- **The search covers titles, abstracts and keywords,** not the text of the reviews, so it can miss reviews of related papers.
- **"Open" means "not found".** Someone may already be working on it under different wording.
- **An AI is doing the reading.** Check the quotes that matter, and have someone who knows the field look at a statement before you commit to it.

## Contributing

This project is open to new features, collaborators and bug reports.

- **Found a bug?** [Open an issue](https://github.com/diptiman-mohanta/ResearchRadar/issues/new). Tell us the topic you used, what you expected, and what happened.
- **Have a feature idea?** [Open an issue](https://github.com/diptiman-mohanta/ResearchRadar/issues/new) to discuss it, or send a pull request.
- **Want to collaborate?** Open an issue to introduce yourself, or pick up any idea below.

Ideas we would love help with:

- More open review sources, especially outside machine learning, such as speech venues.
- Searching the text of reviews, not just titles and abstracts.
- A built-in accepted-versus-rejected comparison, with results balanced by year.
- Handling rate limits with automatic retries, and API keys for those who have them.
- A public benchmark for judging the quality of the statements.

To contribute, edit the skills in `.claude/skills/`. If you change `radar.py`, run `python -m pytest tests`.

**If it helped you, please [star the repository](https://github.com/diptiman-mohanta/ResearchRadar)** ⭐ It helps other researchers find it.

## Licence

[MIT](LICENSE). Review text belongs to its sources: reviews from OpenReview are CC BY 4.0, so quote briefly and link back.
