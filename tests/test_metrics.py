from rag_evals.metrics import exact_match, overlap_f1, precision_at_k, recall_at_k


def test_precision_and_recall_at_k() -> None:
    retrieved = ["a", "b", "c"]
    relevant = {"b", "d"}
    assert precision_at_k(retrieved, relevant, 3) == 1 / 3
    assert recall_at_k(retrieved, relevant, 3) == 1 / 2


def test_exact_match_and_overlap_f1() -> None:
    assert exact_match("Hello", "hello") == 1.0
    score = overlap_f1("hello world", "hello there")
    assert score > 0
