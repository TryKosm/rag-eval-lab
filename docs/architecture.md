# Architecture

`rag-evals-lab` separates metric logic from orchestration:

- `metrics.py`: Pure scoring functions for retrieval and answer quality.
- `runner.py`: Dataset loop and aggregation.
- `cli.py`: Input/output boundary for local and CI usage.

## Data Contract
Each dataset record includes:
- `retrieved_doc_ids`
- `relevant_doc_ids`
- `predicted_answer`
- `expected_answer`

This keeps datasets portable and easy to generate from multiple RAG pipelines.
