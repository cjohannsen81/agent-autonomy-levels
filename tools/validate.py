#!/usr/bin/env python3
"""Validate autonomy certificates against the schema and the framework rules.

Checks, beyond the JSON Schema:
  - level does not exceed max_level
  - every control required at the certified level is listed in controls.in_place
  - expires is after issued
  - writes are empty at L1

Usage: python tools/validate.py CERT.yaml [CERT.yaml ...]
"""
import datetime as dt
import json
import pathlib
import sys

import jsonschema
import yaml

from levels import LEVELS, required_controls

SCHEMA = pathlib.Path(__file__).resolve().parent.parent / "templates" / "certificate.schema.json"


def _to_json(obj):
    """YAML parses dates into date objects; the schema expects strings."""
    if isinstance(obj, dict):
        return {k: _to_json(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_to_json(v) for v in obj]
    if isinstance(obj, (dt.date, dt.datetime)):
        return obj.isoformat()
    return obj


def check(cert: dict) -> list[str]:
    errors = []
    schema = json.loads(SCHEMA.read_text())
    validator = jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker())
    for e in sorted(validator.iter_errors(cert), key=lambda e: list(e.path)):
        loc = "/".join(str(p) for p in e.path) or "(root)"
        errors.append(f"schema: {loc}: {e.message}")
    if errors:
        return errors

    if LEVELS.index(cert["level"]) > LEVELS.index(cert["max_level"]):
        errors.append(f"level {cert['level']} exceeds max_level {cert['max_level']}")
    missing = sorted(set(required_controls(cert["level"])) - set(cert["controls"]["in_place"]))
    if missing:
        errors.append(f"controls required at {cert['level']} but not in place: {', '.join(missing)}")
    if dt.date.fromisoformat(cert["expires"]) <= dt.date.fromisoformat(cert["issued"]):
        errors.append("expires must be after issued")
    if cert["level"] == "L1" and cert["scope"].get("writes"):
        errors.append("L1 certificates may not list write tools (AL-05)")
    return errors


def main(paths: list[str]) -> int:
    failed = 0
    for path in paths:
        with open(path) as f:
            cert = _to_json(yaml.safe_load(f))
        errors = check(cert)
        if errors:
            failed += 1
            print(f"FAIL {path}")
            for e in errors:
                print(f"  - {e}")
        else:
            print(f"ok   {path} ({cert['certificate']}, {cert['level']})")
    return 1 if failed else 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1:]))
