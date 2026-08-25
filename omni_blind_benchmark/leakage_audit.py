#!/usr/bin/env python3
"""Controlled leakage audit. It documents local same-account limitations honestly."""
import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from omni_blind_benchmark import build_fixture, run_public_inputs, scan_for_hidden_leakage


def run_audit(output_dir: str | Path) -> dict:
    output = Path(output_dir); output.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as temporary:
        base = Path(temporary); public, hidden, run = base / "public.jsonl", base / "reference.jsonl", base / "run.jsonl"
        build_fixture(100, public, hidden)
        run_public_inputs(public, run, "omni_blind_benchmark.runner.deterministic_validation_adapter:answer")
        baseline = scan_for_hidden_leakage([public, run], [json.loads(line) for line in hidden.read_text(encoding="utf-8").splitlines()])
        # This adapter receives a known path under the same user account, modeling
        # a compromised runtime with filesystem access. It must be detected, not hidden.
        module = base / "malicious_adapter.py"
        module.write_text("from pathlib import Path\nTARGET = r'''" + str(hidden).replace("\\", "\\\\") + "'''\ndef answer(item):\n return {'answer': Path(TARGET).read_text(encoding='utf-8')}\n", encoding="utf-8")
        sys.path.insert(0, str(base))
        try:
            run_public_inputs(public, base / "malicious_run.jsonl", "malicious_adapter:answer")
        finally:
            sys.path.remove(str(base)); sys.modules.pop("malicious_adapter", None)
        adversarial = scan_for_hidden_leakage([base / "malicious_run.jsonl"], [json.loads(line) for line in hidden.read_text(encoding="utf-8").splitlines()])
    result = {"baseline_api_isolation": baseline["status"], "malicious_same_account_adapter": adversarial["status"],
              "overall": "BLIND_ISOLATION_FAIL" if adversarial["status"] == "BLIND_ISOLATION_FAIL" else "BLIND_ISOLATION_PASS",
              "reason": "A same-account adapter that already knows the scorer path can read it; process/API guards cannot replace OS or container ACL separation."}
    report = "# Blind leakage audit\n\n| Check | Result |\n|---|---|\n" + "\n".join(f"| {key} | {value} |" for key, value in result.items()) + "\n\nThe scanner checks public input, outputs and generated artifacts for exact scorer-only values. It does not detect paraphrases, binary data or remote telemetry.\n"
    (output / "leakage_audit.md").write_text(report, encoding="utf-8")
    return result


if __name__ == "__main__":
    print(run_audit(Path(__file__).parent / "reports"))
