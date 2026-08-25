#!/usr/bin/env python3
import argparse
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from omni_blind_benchmark import evaluate_run

parser = argparse.ArgumentParser(description="Scorer-only evaluator for External Blind Benchmark v1.0.")
parser.add_argument("--public", required=True); parser.add_argument("--reference", required=True); parser.add_argument("--run", required=True); parser.add_argument("--reports", required=True)
parser.add_argument("--model"); parser.add_argument("--holodb"); parser.add_argument("--config"); parser.add_argument("--seed", type=int)
args = parser.parse_args()
print(evaluate_run(args.public, args.reference, args.run, args.reports, args.model, args.holodb, args.config, args.seed))
