#!/usr/bin/env python3
import argparse
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from omni_blind_benchmark import run_public_inputs

parser = argparse.ArgumentParser(description="Run public blind inputs. This command has no reference option.")
parser.add_argument("--public", required=True)
parser.add_argument("--output", required=True)
parser.add_argument("--adapter", required=True, help="module:function; receives only {'id','prompt'}")
args = parser.parse_args()
print(run_public_inputs(args.public, args.output, args.adapter))
