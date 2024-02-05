from __future__ import annotations

import argparse
import json
from pathlib import Path

from .runner import evaluate_dataset


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate a RAG dataset.")
    parser.add_argument("--dataset", type=Path, required=True, help="Path to dataset JSON file.")
    parser.add_argument("--output", type=Path, required=True, help="Output report JSON path.")
    args = parser.parse_args()

    result = evaluate_dataset(args.dataset)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result.__dict__, indent=2))
    print(f"Wrote report to {args.output}")


if __name__ == "__main__":
    main()
