#!/usr/bin/env python3
"""Validate catalog records and controlled vocabulary without dependencies."""
from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
RECORDS = ROOT / "datasets" / "records"
TAXONOMIES = ROOT / "taxonomies"
REQUIRED = {"id", "name", "year", "license", "commercial_use", "domains", "modalities", "image_structure", "tasks", "capabilities", "usage", "catalog_status", "language_supervision", "derived_from", "annotation", "scale", "quality", "access", "last_verified"}
LIST_FIELDS = {"domains", "modalities", "image_structure", "tasks", "capabilities", "language_supervision", "derived_from"}
URL_FIELDS = ("homepage", "paper", "repository", "download")
STATUS = {"included", "candidate", "excluded"}
ACCESS_VALUES = {"yes", "no", "unknown"}
IMAGE_STRUCTURES = {"2d-single", "multi-view", "3d-volume", "whole-slide-image", "video", "longitudinal-sequence"}
LANGUAGE_SUPERVISION = {"caption", "report", "question-answer", "grounded-text", "instruction-dialogue", "reasoning-trace", "preference-pair", "none"}


def taxonomy(name: str) -> set[str]:
    return set(json.loads((TAXONOMIES / f"{name}.json").read_text())["enum"])


ALLOWED = {name: taxonomy(name) for name in ("domains", "modalities", "tasks", "capabilities")}


def load_records() -> list[tuple[Path, dict]]:
    records = []
    for path in sorted(RECORDS.glob("*.yaml")):
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
        if not isinstance(record.get(field), list) or not all(isinstance(item, str) and item for item in record[field]):
            errors.append(f"{label}: {field} must be a list of strings")
    for field, allowed in ALLOWED.items():
        if isinstance(record.get(field), list):
            unknown = sorted(set(record[field]) - allowed)
            if unknown:
                errors.append(f"{label}: unknown {field}: {', '.join(unknown)}")
    for field in ("domains", "modalities", "image_structure", "tasks", "capabilities"):
        if not record.get(field):
            errors.append(f"{label}: {field} must not be empty")
    if isinstance(record.get("language_supervision"), list):
        unknown = sorted(set(record["language_supervision"]) - LANGUAGE_SUPERVISION)
        if unknown:
            errors.append(f"{label}: unknown language_supervision: {', '.join(unknown)}")
    if isinstance(record.get("image_structure"), list):
        unknown = sorted(set(record["image_structure"]) - IMAGE_STRUCTURES)
        if unknown:
            errors.append(f"{label}: unknown image_structure: {', '.join(unknown)}")
    if record.get("usage") not in {"training", "evaluation", "training-evaluation"}:
        errors.append(f"{label}: usage must be training, evaluation, or training-evaluation")
    if record.get("commercial_use") not in ACCESS_VALUES:
        errors.append(f"{label}: commercial_use must be yes, no, or unknown")
    if record.get("catalog_status") not in STATUS:
        errors.append(f"{label}: catalog_status must be included, candidate, or excluded")
    if record.get("catalog_status") == "included" and not record.get("language_supervision"):
        errors.append(f"{label}: included records require language_supervision")
    if record.get("catalog_status") == "included" and "none" in record.get("language_supervision", []):
        errors.append(f"{label}: included records cannot use language_supervision none")
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
    if isinstance(record.get("scale"), dict):
        if not isinstance(record["scale"].get("primary_count"), int) or record["scale"]["primary_count"] < 1:
            errors.append(f"{label}: scale.primary_count must be a positive integer")
        if not isinstance(record["scale"].get("primary_unit"), str) or not record["scale"].get("primary_unit"):
            errors.append(f"{label}: scale.primary_unit must be a non-empty string")
    if isinstance(record.get("quality"), dict):
        for field in ("contamination_audited", "patient_level_split", "external_validation", "known_issues"):
            if field not in record["quality"]:
                errors.append(f"{label}: quality.{field} is required")
    if isinstance(record.get("access"), dict):
        for field in ("registration_required", "credentialing_required"):
            if not isinstance(record["access"].get(field), bool):
                errors.append(f"{label}: access.{field} must be boolean")
        for field in ("gated", "data_use_agreement_required", "citation_required"):
            if record["access"].get(field) not in ACCESS_VALUES:
                errors.append(f"{label}: access.{field} must be yes, no, or unknown")
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
