#!/usr/bin/env python3
"""Compute the maximum autonomy level for a use case from a worksheet answers file.

Usage: python tools/score.py templates/answers.example.yaml
"""
import sys

import yaml

from levels import max_level, required_controls


def main(path: str) -> int:
    with open(path) as f:
        data = yaml.safe_load(f)
    score, level = max_level(data["answers"])
    print(f"use case:        {data.get('use_case', path)}")
    print(f"score:           {score} / 16")
    print(f"maximum level:   {level}")
    print(f"controls at max: {', '.join(required_controls(level))}")
    print("start at L1 or L2 and promote with evidence (FRAMEWORK.md section 6)")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1]))
