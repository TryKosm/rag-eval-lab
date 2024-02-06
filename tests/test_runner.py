from pathlib import Path

from rag_evals.runner import evaluate_dataset


def test_evaluate_dataset_returns_expected_fields() -> None:
    result = evaluate_dataset(Path("examples/sample_dataset.json"))
    assert 0 <= result.retrieval_precision_at_3 <= 1
    assert 0 <= result.retrieval_recall_at_3 <= 1
    assert 0 <= result.answer_exact_match <= 1
    assert 0 <= result.answer_f1 <= 1
