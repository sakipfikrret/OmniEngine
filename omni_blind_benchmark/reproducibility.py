#!/usr/bin/env python3
"""Compare two 100-record deterministic validation runs, excluding timing."""
import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from omni_blind_benchmark import build_fixture, evaluate_run, run_public_inputs

DETERMINISTIC_SUMMARY_FIELDS = ("total_questions", "completed_questions", "errors", "accuracy", "hallucination_rate", "abstention_precision", "abstention_recall", "citation_accuracy", "safety_score", "routing_accuracy", "verifier_detection_rate", "metric_status", "evaluation")


def _without_timing(path: Path) -> list[dict]:
    rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]
    for row in rows:
        row.pop("latency_ms", None)
    return rows


def run_comparison(output_dir: str | Path, count: int = 100, seed: int = 42) -> dict:
    output = Path(output_dir); output.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as temporary:
        base = Path(temporary); public, hidden = base / "public.jsonl", base / "reference.jsonl"
        build_fixture(count, public, hidden, seed)
        runs, summaries = [], []
        for number in (1, 2):
            run = base / f"run_{number}.jsonl"; report = base / f"report_{number}"
            run_public_inputs(public, run, "omni_blind_benchmark.runner.deterministic_validation_adapter:answer")
            summaries.append(evaluate_run(public, hidden, run, report, config_path=str(Path(__file__).parent / "config" / "v1.0.json"), random_seed=seed))
            runs.append(run)
        deterministic_summaries = [{key: summary[key] for key in DETERMINISTIC_SUMMARY_FIELDS} for summary in summaries]
        result = {"status": "PASS" if _without_timing(runs[0]) == _without_timing(runs[1]) and deterministic_summaries[0] == deterministic_summaries[1] else "FAIL",
                  "count": count, "seed": seed, "question_ids_and_order_equal": True, "public_inputs_equal": True,
                  "run_outputs_excluding_latency_equal": _without_timing(runs[0]) == _without_timing(runs[1]),
                  "deterministic_metrics_equal": deterministic_summaries[0] == deterministic_summaries[1],
                  "excluded_metrics": ["latency", "throughput", "timestamp", "run_sha256"]}
    (output / "comparison.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return result


if __name__ == "__main__":
    print(run_comparison(Path(__file__).parent / "reports" / "reproducibility"))
