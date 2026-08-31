#!/usr/bin/env python3
"""Validate catalog records without third-party dependencies."""
from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {"id", "name", "year", "license", "commercial_use", "domains", "modalities", "image_structure", "tasks", "capabilities", "usage", "annotation", "scale", "quality", "access", "last_verified"}
LIST_FIELDS = {"domains", "modalities", "image_structure", "tasks", "capabilities"}
URL_FIELDS = ("homepage", "paper", "repository", "download")


def load_records() -> list[tuple[Path, dict]]:
    records = []
    for path in sorted((ROOT / "datasets").rglob("*.yaml")):
        try:
            value = json.loads(path.read_text())
        except json.JSONDecodeError as error:
            raise ValueError(f"{path.relative_to(ROOT)}: invalid JSON-compatible YAML: {error.msg}") from error
        if not isinstance(value, dict):
            raise ValueError(f"{path.relative_to(ROOT)}: record must be an object")
        records.append((path, value))
    return records


def validate(path: Path, record: dict) -> list[str]:
    errors, label = [], path.relative_to(ROOT)
    missing = REQUIRED - record.keys()
    if missing:
        errors.append(f"{label}: missing required fields: {', '.join(sorted(missing))}")
    if not isinstance(record.get("id"), str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", record.get("id", "")):
        errors.append(f"{label}: id must be lowercase kebab-case")
    if not isinstance(record.get("name"), str) or not record.get("name", "").strip():
        errors.append(f"{label}: name must be a non-empty string")
    if not isinstance(record.get("year"), int) or record.get("year", 0) < 2000:
        errors.append(f"{label}: year must be an integer >= 2000")
    for field in LIST_FIELDS:
        if not isinstance(record.get(field), list) or not record[field] or not all(isinstance(item, str) and item for item in record[field]):
            errors.append(f"{label}: {field} must be a non-empty list of strings")
    if record.get("usage") not in {"training", "evaluation", "training-evaluation"}:
        errors.append(f"{label}: usage must be training, evaluation, or training-evaluation")
    if record.get("commercial_use") not in {"yes", "no", "unknown"}:
        errors.append(f"{label}: commercial_use must be yes, no, or unknown")
    if not any(record.get(field) for field in URL_FIELDS):
        errors.append(f"{label}: at least one official source URL is required")
    for field in URL_FIELDS:
        value = record.get(field)
        if value is not None and (not isinstance(value, str) or urlparse(value).scheme not in {"http", "https"}):
            errors.append(f"{label}: {field} must be an http(s) URL or null")
    for field in ("annotation", "scale", "quality", "access"):
        if not isinstance(record.get(field), dict):
            errors.append(f"{label}: {field} must be an object")
    if isinstance(record.get("annotation"), dict):
        for field in ("source", "expert_review", "grounding"):
            if field not in record["annotation"]:
                errors.append(f"{label}: annotation.{field} is required")
    if isinstance(record.get("quality"), dict):
        for field in ("contamination_audited", "patient_level_split", "external_validation", "known_issues"):
            if field not in record["quality"]:
                errors.append(f"{label}: quality.{field} is required")
    if isinstance(record.get("access"), dict):
        for field in ("registration_required", "credentialing_required"):
            if not isinstance(record["access"].get(field), bool):
                errors.append(f"{label}: access.{field} must be boolean")
    try:
        date.fromisoformat(record.get("last_verified", ""))
    except (TypeError, ValueError):
        errors.append(f"{label}: last_verified must be an ISO date")
    return errors


def main() -> int:
    try:
        records = load_records()
    except ValueError as error:
        print(error, file=sys.stderr)
        return 1
    if not records:
        print("No dataset records found.", file=sys.stderr)
        return 1
    errors = [error for path, record in records for error in validate(path, record)]
    ids = [record["id"] for _, record in records if isinstance(record.get("id"), str)]
    errors.extend(f"Duplicate dataset id: {item}" for item in sorted({item for item in ids if ids.count(item) > 1}))
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Validated {len(records)} dataset records.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
