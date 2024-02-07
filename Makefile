.PHONY: test sample-report

test:
	pytest -q

sample-report:
	python -m rag_evals.cli --dataset examples/sample_dataset.json --output reports/sample_report.json
