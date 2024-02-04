from __future__ import annotations


def precision_at_k(retrieved: list[str], relevant: set[str], k: int) -> float:
    if k <= 0:
        return 0.0
    top_k = retrieved[:k]
    if not top_k:
        return 0.0
    hits = sum(1 for doc_id in top_k if doc_id in relevant)
    return hits / len(top_k)


def recall_at_k(retrieved: list[str], relevant: set[str], k: int) -> float:
    if not relevant:
        return 0.0
    top_k = retrieved[:k]
    hits = sum(1 for doc_id in top_k if doc_id in relevant)
    return hits / len(relevant)


def exact_match(predicted: str, expected: str) -> float:
    return 1.0 if predicted.strip().lower() == expected.strip().lower() else 0.0


def overlap_f1(predicted: str, expected: str) -> float:
    pred_tokens = predicted.lower().split()
    exp_tokens = expected.lower().split()
    if not pred_tokens or not exp_tokens:
        return 0.0
    pred_set = set(pred_tokens)
    exp_set = set(exp_tokens)
    overlap = len(pred_set & exp_set)
    if overlap == 0:
        return 0.0
    precision = overlap / len(pred_set)
    recall = overlap / len(exp_set)
    return 2 * precision * recall / (precision + recall)
