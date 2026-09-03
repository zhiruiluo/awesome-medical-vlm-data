#!/usr/bin/env python3
"""Validate dataset and benchmark records without dependencies."""
from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
RECORDS = ROOT / "datasets" / "records"
BENCHMARKS = ROOT / "benchmarks" / "records"
TAXONOMIES = ROOT / "taxonomies"
REQUIRED = {"id", "name", "year", "license", "commercial_use", "resource_type", "domains", "modalities", "anatomical_targets", "image_structure", "tasks", "capabilities", "usage", "catalog_status", "language_supervision", "derived_from", "annotation", "scale", "quality", "access", "last_verified"}
LIST_FIELDS = {"domains", "modalities", "anatomical_targets", "image_structure", "tasks", "capabilities", "language_supervision", "derived_from"}
URL_FIELDS = ("homepage", "paper", "repository", "download")
STATUS = {"included", "candidate", "excluded"}
RESOURCE_TYPES = {"text-only", "image-only", "text-image-pairs"}
ACCESS_VALUES = {"yes", "no", "unknown"}
IMAGE_STRUCTURES = {"2d-single", "multi-view", "3d-volume", "whole-slide-image", "video", "longitudinal-sequence"}
LANGUAGE_SUPERVISION = {"caption", "report", "question-answer", "grounded-text", "instruction-dialogue", "reasoning-trace", "preference-pair", "structured-ehr", "none"}
BENCHMARK_REQUIRED = {
    "id", "name", "year", "homepage", "paper", "repository", "download", "leaderboard",
    "catalog_status", "domains", "modalities", "tasks", "capabilities", "companion_dataset_id",
    "source_datasets", "external_sources", "evaluation", "scale", "reproducibility", "license",
    "commercial_use", "source_license_policy", "access", "known_issues", "last_verified",
}
BENCHMARK_URL_FIELDS = (*URL_FIELDS, "leaderboard")
SOURCE_ROLES = {"training", "validation", "evaluation", "development", "unknown"}
OUTPUTS = {"free-text", "class-label", "bounding-box", "segmentation-mask", "scalar"}


def taxonomy(name: str) -> set[str]:
    return set(json.loads((TAXONOMIES / f"{name}.json").read_text())["enum"])


ALLOWED = {name: taxonomy(name) for name in ("domains", "modalities", "anatomical_targets", "tasks", "capabilities")}


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


def load_benchmarks() -> list[tuple[Path, dict]]:
    records = []
    for path in sorted(BENCHMARKS.glob("*.yaml")):
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
    anatomical_targets = record.get("anatomical_targets")
    if isinstance(anatomical_targets, list) and len(anatomical_targets) != len(set(anatomical_targets)):
        errors.append(f"{label}: anatomical_targets must not contain duplicates")
    for field, allowed in ALLOWED.items():
        if isinstance(record.get(field), list):
            unknown = sorted(set(record[field]) - allowed)
            if unknown:
                errors.append(f"{label}: unknown {field}: {', '.join(unknown)}")
    for field in ("domains", "anatomical_targets", "tasks", "capabilities"):
        if not record.get(field):
            errors.append(f"{label}: {field} must not be empty")
    if record.get("resource_type") not in RESOURCE_TYPES:
        errors.append(f"{label}: resource_type must be text-only, image-only, or text-image-pairs")
    elif record["resource_type"] == "text-only":
        for field in ("modalities", "image_structure"):
            if record.get(field):
                errors.append(f"{label}: text-only records must have an empty {field} list")
    else:
        for field in ("modalities", "image_structure"):
            if not record.get(field):
                errors.append(f"{label}: image-bearing records require {field}")
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
    if record.get("catalog_status") == "included" and "none" in record.get("language_supervision", []) and record.get("resource_type") != "image-only":
        errors.append(f"{label}: only included image-only records can use language_supervision none")
    if record.get("resource_type") == "image-only" and record.get("language_supervision") != ["none"]:
        errors.append(f"{label}: image-only records must use language_supervision [\"none\"]")
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


def validate_benchmark(path: Path, record: dict, dataset_ids: set[str]) -> list[str]:
    errors, label = [], path.relative_to(ROOT)
    missing = BENCHMARK_REQUIRED - record.keys()
    if missing:
        errors.append(f"{label}: missing required fields: {', '.join(sorted(missing))}")
    if not isinstance(record.get("id"), str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", record.get("id", "")):
        errors.append(f"{label}: id must be lowercase kebab-case")
    if not isinstance(record.get("name"), str) or not record.get("name", "").strip():
        errors.append(f"{label}: name must be a non-empty string")
    if not isinstance(record.get("year"), int) or record.get("year", 0) < 2000:
        errors.append(f"{label}: year must be an integer >= 2000")
    for field in ("domains", "modalities", "tasks", "capabilities"):
        values = record.get(field)
        if not isinstance(values, list) or not values or not all(isinstance(item, str) and item for item in values):
            errors.append(f"{label}: {field} must be a non-empty list of strings")
        elif len(values) != len(set(values)):
            errors.append(f"{label}: {field} must not contain duplicates")
        else:
            unknown = sorted(set(values) - ALLOWED[field])
            if unknown:
                errors.append(f"{label}: unknown {field}: {', '.join(unknown)}")
    if record.get("catalog_status") not in STATUS:
        errors.append(f"{label}: catalog_status must be included, candidate, or excluded")
    if record.get("commercial_use") not in ACCESS_VALUES:
        errors.append(f"{label}: commercial_use must be yes, no, or unknown")
    if record.get("source_license_policy") not in {"uniform", "mixed", "inherited", "unknown"}:
        errors.append(f"{label}: invalid source_license_policy")
    if not any(record.get(field) for field in BENCHMARK_URL_FIELDS):
        errors.append(f"{label}: at least one official source URL is required")
    for field in BENCHMARK_URL_FIELDS:
        value = record.get(field)
        if value is not None and (not isinstance(value, str) or urlparse(value).scheme not in {"http", "https"}):
            errors.append(f"{label}: {field} must be an http(s) URL or null")

    companion = record.get("companion_dataset_id")
    if companion is not None and companion not in dataset_ids:
        errors.append(f"{label}: unknown companion_dataset_id: {companion}")
    sources = record.get("source_datasets")
    if not isinstance(sources, list):
        errors.append(f"{label}: source_datasets must be a list")
    else:
        source_ids = []
        for index, source in enumerate(sources):
            prefix = f"{label}: source_datasets[{index}]"
            if not isinstance(source, dict):
                errors.append(f"{prefix} must be an object")
                continue
            missing_source_fields = {"dataset_id", "role", "subset"} - source.keys()
            if missing_source_fields:
                errors.append(f"{prefix} missing fields: {', '.join(sorted(missing_source_fields))}")
            dataset_id = source.get("dataset_id")
            source_ids.append(dataset_id)
            if dataset_id not in dataset_ids:
                errors.append(f"{prefix}.dataset_id is unknown: {dataset_id}")
            if source.get("role") not in SOURCE_ROLES:
                errors.append(f"{prefix}.role is invalid")
            if source.get("subset") is not None and not isinstance(source.get("subset"), str):
                errors.append(f"{prefix}.subset must be a string or null")
        duplicates = sorted({item for item in source_ids if item and source_ids.count(item) > 1})
        if duplicates:
            errors.append(f"{label}: duplicate source dataset ids: {', '.join(duplicates)}")

    external = record.get("external_sources")
    if not isinstance(external, list):
        errors.append(f"{label}: external_sources must be a list")
    else:
        names = []
        for index, source in enumerate(external):
            prefix = f"{label}: external_sources[{index}]"
            if not isinstance(source, dict):
                errors.append(f"{prefix} must be an object")
                continue
            missing_source_fields = {"name", "homepage", "role", "subset"} - source.keys()
            if missing_source_fields:
                errors.append(f"{prefix} missing fields: {', '.join(sorted(missing_source_fields))}")
            name = source.get("name")
            names.append(name)
            if not isinstance(name, str) or not name.strip():
                errors.append(f"{prefix}.name must be a non-empty string")
            homepage = source.get("homepage")
            if homepage is not None and (not isinstance(homepage, str) or urlparse(homepage).scheme not in {"http", "https"}):
                errors.append(f"{prefix}.homepage must be an http(s) URL or null")
            if source.get("role") not in SOURCE_ROLES:
                errors.append(f"{prefix}.role is invalid")
        duplicates = sorted({item for item in names if item and names.count(item) > 1})
        if duplicates:
            errors.append(f"{label}: duplicate external source names: {', '.join(duplicates)}")
    if not sources and not external and companion is None:
        errors.append(f"{label}: a companion dataset or source dataset is required")

    evaluation = record.get("evaluation")
    if not isinstance(evaluation, dict):
        errors.append(f"{label}: evaluation must be an object")
    else:
        missing_evaluation_fields = {"protocols", "metrics", "outputs", "models_evaluated"} - evaluation.keys()
        if missing_evaluation_fields:
            errors.append(f"{label}: evaluation missing fields: {', '.join(sorted(missing_evaluation_fields))}")
        for field in ("protocols", "metrics", "outputs"):
            values = evaluation.get(field)
            if not isinstance(values, list) or not values or not all(isinstance(item, str) and item for item in values):
                errors.append(f"{label}: evaluation.{field} must be a non-empty list of strings")
        if isinstance(evaluation.get("outputs"), list):
            unknown = sorted(set(evaluation["outputs"]) - OUTPUTS)
            if unknown:
                errors.append(f"{label}: unknown evaluation outputs: {', '.join(unknown)}")
        models = evaluation.get("models_evaluated")
        if models is not None and (not isinstance(models, int) or models < 0):
            errors.append(f"{label}: evaluation.models_evaluated must be a non-negative integer or null")
    if isinstance(record.get("scale"), dict):
        if not isinstance(record["scale"].get("primary_count"), int) or record["scale"]["primary_count"] < 1:
            errors.append(f"{label}: scale.primary_count must be a positive integer")
        if not isinstance(record["scale"].get("primary_unit"), str) or not record["scale"].get("primary_unit"):
            errors.append(f"{label}: scale.primary_unit must be a non-empty string")
    else:
        errors.append(f"{label}: scale must be an object")
    reproducibility = record.get("reproducibility")
    if not isinstance(reproducibility, dict):
        errors.append(f"{label}: reproducibility must be an object")
    else:
        missing_reproducibility_fields = {"prompts_available", "evaluation_code_available", "fixed_splits", "contamination_audited"} - reproducibility.keys()
        if missing_reproducibility_fields:
            errors.append(f"{label}: reproducibility missing fields: {', '.join(sorted(missing_reproducibility_fields))}")
        for field in ("prompts_available", "evaluation_code_available", "fixed_splits", "contamination_audited"):
            if reproducibility.get(field) not in ACCESS_VALUES:
                errors.append(f"{label}: reproducibility.{field} must be yes, no, or unknown")
    access = record.get("access")
    if not isinstance(access, dict):
        errors.append(f"{label}: access must be an object")
    else:
        missing_access_fields = {"registration_required", "credentialing_required", "gated", "data_use_agreement_required", "citation_required"} - access.keys()
        if missing_access_fields:
            errors.append(f"{label}: access missing fields: {', '.join(sorted(missing_access_fields))}")
        for field in ("registration_required", "credentialing_required"):
            if not isinstance(access.get(field), bool):
                errors.append(f"{label}: access.{field} must be boolean")
        for field in ("gated", "data_use_agreement_required", "citation_required"):
            if access.get(field) not in ACCESS_VALUES:
                errors.append(f"{label}: access.{field} must be yes, no, or unknown")
    if not isinstance(record.get("known_issues"), list) or not all(isinstance(item, str) and item for item in record.get("known_issues", [])):
        errors.append(f"{label}: known_issues must be a list of strings")
    try:
        date.fromisoformat(record.get("last_verified", ""))
    except (TypeError, ValueError):
        errors.append(f"{label}: last_verified must be an ISO date")
    return errors


def main() -> int:
    try:
        records = load_records()
        benchmarks = load_benchmarks()
    except ValueError as error:
        print(error, file=sys.stderr)
        return 1
    if not records:
        print("No dataset records found.", file=sys.stderr)
        return 1
    errors = [error for path, record in records for error in validate(path, record)]
    ids = [record["id"] for _, record in records if isinstance(record.get("id"), str)]
    errors.extend(f"Duplicate dataset id: {item}" for item in sorted({item for item in ids if ids.count(item) > 1}))
    dataset_ids = set(ids)
    errors.extend(error for path, record in benchmarks for error in validate_benchmark(path, record, dataset_ids))
    benchmark_ids = [record["id"] for _, record in benchmarks if isinstance(record.get("id"), str)]
    errors.extend(f"Duplicate benchmark id: {item}" for item in sorted({item for item in benchmark_ids if benchmark_ids.count(item) > 1}))
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Validated {len(records)} dataset and {len(benchmarks)} benchmark records.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
