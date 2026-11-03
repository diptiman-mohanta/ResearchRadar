"""The skill's helper script. Parsing is tested on small inputs, and storage on the dataset's real record shape."""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import pytest

SCRIPT = Path(__file__).parents[1] / ".claude/skills/problem-statement-finder/scripts/radar.py"
sys.dont_write_bytecode = True
_spec = importlib.util.spec_from_file_location("radar", SCRIPT)
radar = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(radar)


def lines(*rows):
    return [json.dumps(row).encode() for row in rows]


class TestMatching:
    @pytest.mark.parametrize(
        ("title", "queries", "expected"),
        [
            ("Rethinking pooling in graph neural networks", ["graph neural"], True),
            ("Neural Topographic Factor Analysis", ["graph neural"], False),
            ("Learning of Discrete Graphical Models with Neural Networks", ["graph neural"], False),
            ("Graph Networks for Physics", ["graph network"], True),
            ("Something else", ["graph neural", "something"], True),
            ("A (GNN) study", ["gnn"], True),
        ],
    )
    def test_whole_words_only(self, title, queries, expected):
        assert radar.matches(title, queries) is expected

    def test_results_spread_across_years(self):
        spread = radar.spread_across_years({2020: [("a", "A"), ("b", "B")], 2019: [("c", "C")]})
        assert [year for year, _, _ in spread] == [2020, 2019, 2020]


class TestParsing:
    def test_neurips_listing(self):
        page = '<li><a title="paper title" href="/paper_files/paper/2020/hash/0004d0b59e19461ff126e3a08a814c33-Abstract.html">A graph &amp; B</a></li>'
        assert radar.parse_listing(page) == [("0004d0b59e19461ff126e3a08a814c33", "A graph & B")]

    def test_review_page_drops_the_header(self):
        page = "<html><style>x{}</style><h1>NeurIPS 2019</h1><pre>Reviewer 1\nGood point.</pre></html>"
        text = radar.parse_review_page(page, "T")
        assert text.startswith("Reviewer 1") and "NeurIPS 2019" not in text and "x{}" not in text

    def test_openalex_abstract_is_rebuilt_in_order(self):
        assert radar.openalex_abstract({"world": [1], "hello": [0], "again": [2]}) == "hello world again"
        assert radar.openalex_abstract(None) is None

    def test_openalex_record(self):
        body = {
            "results": [
                {
                    "id": "https://openalex.org/W1",
                    "title": " A  title ",
                    "publication_year": 2021,
                    "doi": "https://doi.org/10.1/x",
                },
                {"id": "W2"},
            ]
        }
        assert [(p["title"], p["openalex_id"], p["url"]) for p in radar.parse_openalex(body)] == [
            ("A title", "W1", "https://doi.org/10.1/x")
        ]

    def test_arxiv_entry_and_error_entry(self):
        xml = (
            "<feed><entry><id>http://arxiv.org/abs/1706.03762v7</id><title>Attention\n Is All</title><summary>Abs</summary><published>2017-06-12T00</published></entry>"
            "<entry><id>https://arxiv.org/api/errors#x</id><title>Error</title></entry></feed>"
        )
        papers = radar.parse_arxiv(xml)
        assert (
            len(papers) == 1
            and papers[0]["title"] == "Attention Is All"
            and papers[0]["arxiv_id"] == "1706.03762"
        )
        assert papers[0]["peer_reviewed"] is False

    def test_limits_finds_sections_and_admissions(self):
        page = "<h2>1 Intro</h2><p>Hello.</p><h2>5 Limitations</h2><p>Our method fails to scale on graphs with a million nodes.</p><h2>6 Refs</h2><p>x</p>"
        out = radar.extract_limits(page)
        assert [s["heading"] for s in out["sections"]] == ["5 Limitations"]
        assert "fails to scale" in out["admissions"][0]

    def test_elife_text_is_flattened(self):
        assert radar._flatten({"content": [{"text": "<b>One</b>"}, {"content": [{"text": "Two"}]}]}) == [
            "One",
            "Two",
        ]


class TestPapersHint:
    def _run(self, monkeypatch, capsys, query):
        monkeypatch.setattr(radar, "fetch", lambda *_a, **_k: (200, ""))
        monkeypatch.setattr(radar, "_openalex", lambda _p: ("ok", []))
        radar.main(["papers", *query.split()])
        return json.loads(capsys.readouterr().out)

    def test_long_query_with_few_results_warns_about_false_gaps(self, monkeypatch, capsys):
        out = self._run(monkeypatch, capsys, "beyond one WL expressivity practical performance graph")
        assert "says nothing about whether the work exists" in out["hint"] and "2 to 4 words" in out["hint"]

    def test_short_empty_query_still_warns(self, monkeypatch, capsys):
        assert "says nothing" in self._run(monkeypatch, capsys, "graph noise")["hint"]


class TestWorkedExample:
    def test_example_is_marked_as_a_real_run_with_review_links(self):
        text = (SCRIPT.parent.parent / "references/output-format.md").read_text(encoding="utf-8")
        assert text.count("proceedings.neurips.cc") >= 4 and "real run" in text


class TestVerify:
    def test_exact_quote_passes_and_altered_quote_fails(self, tmp_path, capsys):
        source = tmp_path / "reviews.json"
        source.write_text(json.dumps({"papers": [{"reviews": "The baseline is\nweak here."}]}), encoding="utf-8")
        radar.main(["verify", str(source), "The baseline is weak here."])
        assert json.loads(capsys.readouterr().out)["all_found"] is True
        with pytest.raises(SystemExit) as exc:
            radar.main(["verify", str(source), "The baseline is poor here."])
        assert exc.value.code == 1

    def test_case_and_punctuation_must_match(self):
        assert not radar.quote_in_source("the baseline", "The baseline")
        assert not radar.quote_in_source("baseline, weak", "baseline weak")


class TestReviewText:
    def test_content_forms(self):
        assert "useful" in radar.review_text(
            {"review": "This is useful and long enough to keep.", "rating": "8"}
        )
        assert "useful" in radar.review_text("{'review': 'This is useful and long enough to keep.'}")
        assert "useful" in radar.review_text({"review": {"value": "This is useful and long enough to keep."}})
        assert (
            radar.review_text({"rating": "8", "title": "A long title that should not count as text."}) == ""
        )


class TestIndex:
    @pytest.fixture
    def index(self, tmp_path, monkeypatch):
        monkeypatch.setattr(radar, "CACHE", tmp_path)
        conn = radar.open_snor(radar.snor_db())
        radar.ingest(
            conn,
            lines({"id": "A1", "title": "Graph neural study", "abstract": "Abs", "keywords": [], "accepted": True, "raw_decision": "ICLR 2024 Poster", "conference_name": "iclr", "conference_year": 2024, "review_score_avg": 7.0, "authors": ["Secret Author"], "embedding": [0.1]}),
            lines(
                {"paper_id": "A1", "signature": "ICLR/Reviewer_secret", "is_review": True, "numeric_rating": 8.0, "content": {"review": "The baseline comparison here is weak and incomplete."}},
                {"paper_id": "ZZ", "signature": "x", "is_review": True, "content": {"review": "A review of a paper we do not know about at all."}},
            ),
        )  # fmt: skip
        radar.ingest_failed(
            conn,
            lines(
                {
                    "id": "R1", "title": "Graph neural rejected", "abstract": "Abs", "keywords": [], "accepted": False, "venueid": "ICLR 2024 Rejected", "conference": "iclr2024",
                    "raw": {"signatures": ["~Secret_Person1"], "details": {"directReplies": [
                        {"invitations": ["V/Submission1/-/Official_Review"], "signatures": ["V/Reviewer_secret2"], "content": {"review": {"value": "The theory does not explain the observed result."}, "rating": {"value": 3}}},
                        {"invitations": ["V/Submission1/-/Rebuttal"], "signatures": ["~Secret_Person1"], "content": {"rebuttal": {"value": "We disagree with this reading of the results."}}},
                        {"invitations": ["V/Submission1/-/Meta_Review"], "content": {"metareview": {"value": "A meta review that is not stored as a review."}}},
                        {"invitations": ["V/Submission1/-/Decision"], "content": {"decision": {"value": "Reject"}}},
                    ]}},
                },
                {"id": "R2", "title": "Topographic neural rejected", "abstract": "Abs", "keywords": [], "accepted": False, "venueid": "ICLR 2024 Rejected", "conference": "iclr2024", "raw": {"details": {"directReplies": [{"invitations": ["V/Official_Review"], "content": {"review": "This also has a long enough review text."}}]}}},
            ),
        )  # fmt: skip
        conn.execute("INSERT INTO meta VALUES ('mode', 'full')")
        conn.commit()
        conn.close()

    def _search(self, capsys, *argv):
        radar.main(["iclr", *argv])
        return json.loads(capsys.readouterr().out)

    def test_accepted_and_rejected_are_both_returned(self, index, capsys):
        out = self._search(capsys, "graph neural", "--outcome", "both")
        assert {p["title"]: p["outcome"] for p in out["papers"]} == {
            "Graph neural study": "accepted",
            "Graph neural rejected": "rejected",
        }
        rejected = next(p for p in out["papers"] if p["outcome"] == "rejected")
        assert "does not explain" in rejected["reviews"] and rejected["venue"] == "ICLR 2024"
        assert rejected["url"] == "https://openreview.net/forum?id=R1"

    def test_outcome_filter(self, index, capsys):
        out = self._search(capsys, "graph neural", "--outcome", "rejected")
        assert [p["outcome"] for p in out["papers"]] == ["rejected"]

    def test_word_boundaries_apply_to_the_index(self, index, capsys):
        out = self._search(capsys, "graph neural", "--outcome", "rejected")
        assert all("Topographic" not in p["title"] for p in out["papers"])

    def test_no_identity_reaches_the_index(self, index):
        data = radar.snor_db().read_bytes()
        for secret in (b"Secret_Person", b"Reviewer_secret", b"Secret Author"):
            assert secret not in data

    def test_comments_of_unknown_papers_are_skipped(self, index):
        import sqlite3

        conn = sqlite3.connect(radar.snor_db())
        assert conn.execute("SELECT COUNT(*) FROM reviews WHERE paper_id = 'ZZ'").fetchone()[0] == 0

    def test_meta_reviews_and_decisions_are_not_reviews(self, index):
        import sqlite3

        conn = sqlite3.connect(radar.snor_db())
        texts = [row[0] for row in conn.execute("SELECT text FROM reviews WHERE paper_id = 'R1'")]
        assert len(texts) == 2 and not any("meta review" in t for t in texts)

    def test_unfinished_build_says_not_ready(self, index, capsys):
        import sqlite3

        conn = sqlite3.connect(radar.snor_db())
        with conn:
            conn.execute("DELETE FROM meta")
        conn.close()
        out = self._search(capsys, "graph neural")
        assert out["status"] == "not ready" and out["papers"] == []

    def test_locked_index_says_not_ready(self, index, capsys):
        import sqlite3

        conn = sqlite3.connect(radar.snor_db(), isolation_level=None)
        conn.execute("BEGIN EXCLUSIVE")
        try:
            assert self._search(capsys, "graph neural")["status"] == "not ready"
        finally:
            conn.execute("ROLLBACK")
            conn.close()

    def test_not_built_says_so_instead_of_returning_empty(self, tmp_path, monkeypatch, capsys):
        monkeypatch.setattr(radar, "CACHE", tmp_path / "none")
        out = self._search(capsys, "graph")
        assert out["status"] == "not built" and "iclr-build" in out["hint"]

    def test_download_needs_explicit_flag(self, tmp_path, monkeypatch, capsys):
        monkeypatch.setattr(radar, "CACHE", tmp_path)
        with pytest.raises(SystemExit) as exc:
            radar.main(["iclr-build"])
        assert exc.value.code == 2 and "Ask the user" in capsys.readouterr().err
        assert not radar.snor_db().exists()

    def test_sample_index_warns(self, index, capsys):
        import sqlite3

        conn = sqlite3.connect(radar.snor_db())
        with conn:
            conn.execute("UPDATE meta SET value = 'sample'")
        conn.close()
        assert "SAMPLE" in self._search(capsys, "graph neural")["warning"]
