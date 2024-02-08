# Rag Eval Lab

Evaluate RAG retrieval quality and answer fidelity.

![CI](https://github.com/TryKosm/rag-eval-lab/actions/workflows/ci.yml/badge.svg)

Production-style toolkit for evaluating Retrieval Augmented Generation (RAG) quality across retrieval and answer-generation stages.

## Features
- Dataset-driven evaluation runner.
- Retriever quality metrics (precision@k, recall@k).
- Answer quality metrics (exact match, token overlap F1).
- JSON report output for CI/CD and benchmark tracking.
- CLI entrypoint for local and automated runs.

## Quickstart
```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
rag-evals --dataset examples/sample_dataset.json --output reports/report.json
pytest -q
```

## Project Layout
- `src/rag_evals`: Core library and CLI.
- `tests`: Unit tests for retrieval and answer metrics.
- `examples`: Small example dataset.

## License
MIT
