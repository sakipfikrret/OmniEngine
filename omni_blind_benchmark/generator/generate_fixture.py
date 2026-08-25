#!/usr/bin/env python3
import argparse
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from omni_blind_benchmark import build_fixture

parser = argparse.ArgumentParser(description="Generate deterministic blind-benchmark public/reference fixtures.")
parser.add_argument("--count", type=int, default=100, choices=(100, 1000, 10000))
parser.add_argument("--public", required=True)
parser.add_argument("--reference", required=True, help="Scorer-controlled path; never pass this to runner.")
args = parser.parse_args()
print(build_fixture(args.count, args.public, args.reference))
