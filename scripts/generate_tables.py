#!/usr/bin/env python3
"""Generate catalog views from JSON-compatible YAML dataset records."""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECORDS = ROOT / "datasets" / "records"
DOMAINS = json.loads((ROOT / "taxonomies" / "domains.json").read_text())["enum"]
RESOURCE_TYPES = ("text-only", "image-only", "text-image-pairs")


def load_records() -> list[dict]:
    paths = sorted(RECORDS.glob("*.yaml"))
    if not paths:
        raise ValueError(f"No records found in {RECORDS.relative_to(ROOT)}")
    records = []
    for path in paths:
        try:
            records.append(json.loads(path.read_text()))
        except json.JSONDecodeError as error:
            raise ValueError(f"{path.relative_to(ROOT)}: invalid JSON-compatible YAML: {error.msg}") from error
    return sorted(records, key=lambda item: (item["year"], item["name"].lower()))


def published_records(items: list[dict]) -> list[dict]:
    return [item for item in items if item["catalog_status"] == "included"]


def cells(values: list[str]) -> str:
    return ", ".join(values) or "-"


def domain_title(domain: str) -> str:
    return domain.replace("-", " ").title()


def resource_type_title(resource_type: str) -> str:
    return {"text-only": "Text Only", "image-only": "Image Only", "text-image-pairs": "Text-Image Pairs"}[resource_type]


def group_by_domain(items: list[dict]) -> dict[str, list[dict]]:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for item in items:
        for domain in item["domains"]:
            grouped[domain].append(item)
    return {domain: grouped[domain] for domain in DOMAINS if grouped[domain]}


def group_by_resource_type(items: list[dict]) -> dict[str, list[dict]]:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for item in items:
        grouped[item["resource_type"]].append(item)
    return {resource_type: grouped[resource_type] for resource_type in RESOURCE_TYPES}


def scale(record: dict) -> str:
    value, unit = record["scale"]["primary_count"], record["scale"]["primary_unit"]
    return f"{value / 1_000_000:.1f}M {unit}" if value >= 1_000_000 else f"{value / 1_000:.1f}K {unit}" if value >= 1_000 else f"{value} {unit}"


def links(record: dict) -> str:
    badges = []
    if record.get("repository"):
        if record["repository"].startswith("https://github.com"):
            badges.append(f"[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)]({record['repository']})")
        elif record["repository"].startswith("https://huggingface.co"):
            badges.append(f"[![Hugging Face](https://img.shields.io/badge/Hugging%20Face-FF6C37?style=flat-square&logo=huggingface&logoColor=white)]({record['repository']})")
        else:
            badges.append(f"[![Repository](https://img.shields.io/badge/Repository-000000?style=flat-square&logo=repository&logoColor=white)]({record['repository']})")
    if record.get("download"):
        badges.append(f"[![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)]({record['download']})")
    if record.get("paper"):
        badges.append(f"[![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)]({record['paper']})")
    return " ".join(badges) or "-"


def table(items: list[dict]) -> str:
    lines = ["| Dataset | Year | Structure | Capability | Scale | Grounding | Links | License / access |", "| --- | ---: | --- | --- | ---: | --- | --- | --- |"]
    for item in items:
        source = item["homepage"] or item["paper"] or item["repository"] or item["download"]
        access = "credentialed" if item["access"]["credentialing_required"] else "registration" if item["access"]["registration_required"] else "open"
        lines.append(f"| [{item['name']}]({source}) | {item['year']} | {cells(item['image_structure'])} | {cells(item['capabilities'][:2])} | {scale(item)} | {cells(item['annotation']['grounding'])} | {links(item)} | {item['license']} ({access}) |")
    return "\n".join(lines)


def replace_marked(text: str, name: str, content: str) -> str:
    begin, end = f"<!-- BEGIN GENERATED:{name} -->", f"<!-- END GENERATED:{name} -->"
    if begin not in text or end not in text:
        raise ValueError(f"Missing generated markers for {name}")
    before, remainder = text.split(begin, 1)
    _, after = remainder.split(end, 1)
    return f"{before}{begin}\n{content}\n{end}{after}"


def render_readme(items: list[dict], audited: list[dict]) -> str:
    readme = (ROOT / "README.md").read_text()
    by_resource_type = group_by_resource_type(items)
    navigation = " | ".join(f"[{resource_type_title(resource_type)}](#{resource_type})" for resource_type in RESOURCE_TYPES)
    sections = []
    for resource_type, records in by_resource_type.items():
        domains = group_by_domain(records)
        body = "\n\n".join(f"#### {domain_title(domain)}\n\n{table(group)}" for domain, group in domains.items()) or "No included records yet."
        sections.append(f"### {resource_type_title(resource_type)}\n\n{body}")
    resources = "\n\n".join(sections)
    counts = Counter(capability for item in items for capability in item["capabilities"])
    capabilities = "| Capability | Datasets |\n| --- | ---: |\n" + "\n".join(f"| {capability} | {count} |" for capability, count in sorted(counts.items()))
    status_counts = Counter(item["catalog_status"] for item in audited)
    type_counts = Counter(item["resource_type"] for item in items)
    summary = f"{len(items)} included resources: {type_counts['text-only']} text-only, {type_counts['image-only']} image-only, and {type_counts['text-image-pairs']} text-image pairs. {status_counts['candidate']} candidate and {status_counts['excluded']} excluded records are retained for auditability but omitted from the tables below."
    return replace_marked(replace_marked(replace_marked(replace_marked(readme, "CATALOG_SUMMARY", summary), "RESOURCE_TYPE_NAV", navigation), "RESOURCE_TYPE_TABLES", resources), "CAPABILITY_TABLE", capabilities)


def render_reports(items: list[dict]) -> tuple[str, str]:
    domains = Counter(domain for item in items for domain in item["domains"])
    resource_types = Counter(item["resource_type"] for item in items)
    capabilities = Counter(capability for item in items for capability in item["capabilities"])
    landscape = "# Landscape\n\nGenerated from `datasets/` by `scripts/generate_tables.py`.\n\n## Resource Types\n\n" + "\n".join(f"- {name}: {resource_types[name]}" for name in RESOURCE_TYPES) + "\n\n## Domains\n\n" + "\n".join(f"- {name}: {count}" for name, count in sorted(domains.items())) + "\n\n## Capabilities\n\n" + "\n".join(f"- {name}: {count}" for name, count in sorted(capabilities.items())) + "\n"
    uncertain = [item["name"] for item in items if item["commercial_use"] == "unknown" or "check" in item["license"].lower()]
    gaps = "# Coverage Gaps\n\nGenerated from `datasets/` by `scripts/generate_tables.py`.\n\n- The catalog is currently concentrated in 2D imaging; 3D, video, whole-slide, and longitudinal resources need more coverage.\n- Localization, segmentation, measurement, hallucination detection, and tool-use capabilities have no entries in this MVP.\n- Ophthalmology has one provisional entry and needs independently verified report-linked datasets.\n- Licensing or commercial-use status needs follow-up for: " + ", ".join(uncertain) + ".\n"
    return landscape, gaps


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if generated files are stale")
    parser.add_argument("--readme-only", action="store_true", help="emit only README.md")
    args = parser.parse_args()
    try:
        audited = load_records()
    except ValueError as error:
        print(error, file=sys.stderr)
        return 1
    items = published_records(audited)
    expected = {ROOT / "README.md": render_readme(items, audited)}
    if not args.readme_only:
        expected[ROOT / "reports/landscape.md"], expected[ROOT / "reports/gaps.md"] = render_reports(items)
    stale = [path for path, content in expected.items() if not path.exists() or path.read_text() != content]
    if args.check:
        if stale:
            print("Generated files are stale: " + ", ".join(str(path.relative_to(ROOT)) for path in stale))
            return 1
        print("Generated files are current.")
        return 0
    for path, content in expected.items():
        path.write_text(content)
    status_counts = Counter(item["catalog_status"] for item in audited)
    print(f"Generated {'README' if args.readme_only else 'catalog views'} for {len(items)} included datasets.")
    print(f"Catalog records: {status_counts['included']} included, {status_counts['candidate']} candidate, {status_counts['excluded']} excluded.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
