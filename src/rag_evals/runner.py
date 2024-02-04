from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

from .metrics import exact_match, overlap_f1, precision_at_k, recall_at_k


@dataclass
class EvalResult:
    retrieval_precision_at_3: float
    retrieval_recall_at_3: float
    answer_exact_match: float
    answer_f1: float


def evaluate_dataset(dataset_path: Path) -> EvalResult:
    raw = json.loads(dataset_path.read_text())
    records = raw["records"]

    p_at_3 = []
    r_at_3 = []
    em = []
    f1 = []
    for row in records:
        retrieved = row["retrieved_doc_ids"]
        relevant = set(row["relevant_doc_ids"])
        predicted = row["predicted_answer"]
        expected = row["expected_answer"]

        p_at_3.append(precision_at_k(retrieved, relevant, 3))
        r_at_3.append(recall_at_k(retrieved, relevant, 3))
        em.append(exact_match(predicted, expected))
        f1.append(overlap_f1(predicted, expected))

    count = len(records) or 1
    return EvalResult(
        retrieval_precision_at_3=sum(p_at_3) / count,
        retrieval_recall_at_3=sum(r_at_3) / count,
        answer_exact_match=sum(em) / count,
        answer_f1=sum(f1) / count,
    )
