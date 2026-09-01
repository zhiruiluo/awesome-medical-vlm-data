#!/usr/bin/env python3
"""Format JSON-compatible YAML dataset records consistently."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECORDS = ROOT / "datasets" / "records"


def formatted(path: Path) -> str:
    try:
        record = json.loads(path.read_text())
    except json.JSONDecodeError as error:
        raise ValueError(f"{path.relative_to(ROOT)}: invalid JSON-compatible YAML: {error.msg}") from error
    return json.dumps(record, indent=2, ensure_ascii=True) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail when records are not canonically formatted")
    args = parser.parse_args()
    stale = []
    for path in sorted(RECORDS.glob("*.yaml")):
        try:
            content = formatted(path)
        except ValueError as error:
            print(error, file=sys.stderr)
            return 1
        if path.read_text() != content:
            stale.append(path)
            if not args.check:
                path.write_text(content)
    if args.check and stale:
        print("Records need formatting: " + ", ".join(str(path.relative_to(ROOT)) for path in stale))
        return 1
    print(f"{'Checked' if args.check else 'Formatted'} {len(list(RECORDS.glob('*.yaml')))} dataset records.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
