#!/usr/bin/env python3
"""Create the reproducible 100-question harness-validation report (not a model claim)."""
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from omni_blind_benchmark import build_fixture, evaluate_run, run_public_inputs


def run_dry_run(report_dir: str | Path, seed: int = 42) -> dict:
    with tempfile.TemporaryDirectory() as temporary:
        base = Path(temporary); public, hidden, run = base / "public.jsonl", base / "reference.jsonl", base / "run.jsonl"
        build_fixture(100, public, hidden, seed)
        run_public_inputs(public, run, "omni_blind_benchmark.runner.deterministic_validation_adapter:answer")
        return evaluate_run(public, hidden, run, report_dir, config_path=str(Path(__file__).parent / "config" / "v1.0.json"), random_seed=seed)


if __name__ == "__main__":
    print(run_dry_run(Path(__file__).parent / "reports" / "dry_run_100"))
