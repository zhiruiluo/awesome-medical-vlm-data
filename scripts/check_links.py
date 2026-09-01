#!/usr/bin/env python3
"""Check official record URLs; protected sources are warnings by default."""
from __future__ import annotations

import argparse
import json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
URL_FIELDS = ("homepage", "paper", "repository", "download", "leaderboard")
RECORD_DIRS = (ROOT / "datasets" / "records", ROOT / "benchmarks" / "records")


def check(url: str, timeout: int) -> tuple[str, int | None, str]:
    request = Request(url, method="HEAD", headers={"User-Agent": "awesome-medical-vlm-data-link-checker/1.0"})
    try:
        with urlopen(request, timeout=timeout) as response:
            return url, response.status, "ok"
    except HTTPError as error:
        return url, error.code, "protected or HEAD unsupported" if error.code in {401, 403, 405} else "http error"
    except URLError as error:
        return url, None, f"network error: {error.reason}"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--timeout", type=int, default=10)
    parser.add_argument("--strict", action="store_true", help="treat protected URLs as errors")
    args = parser.parse_args()
    urls = sorted({record[field] for directory in RECORD_DIRS for path in directory.glob("*.yaml") for record in [json.loads(path.read_text())] for field in URL_FIELDS if record.get(field)})
    failed = 0
    with ThreadPoolExecutor(max_workers=8) as pool:
        for url, status, result in pool.map(lambda item: check(item, args.timeout), urls):
            prefix = "OK" if result == "ok" else "WARN" if result == "protected or HEAD unsupported" and not args.strict else "FAIL"
            print(f"{prefix} {status or '-'} {url} ({result})")
            failed += prefix == "FAIL"
    print(f"Checked {len(urls)} unique URLs.")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
