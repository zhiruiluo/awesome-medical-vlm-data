#!/usr/bin/env python3
"""Generate catalog views from JSON-compatible YAML records."""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECORDS = ROOT / "datasets" / "records"
BENCHMARK_RECORDS = ROOT / "benchmarks" / "records"
DOMAINS = json.loads((ROOT / "taxonomies" / "domains.json").read_text())["enum"]
RESOURCE_TYPES = ("text-only", "image-only", "text-image-pairs")
LONGITUDINAL_IMAGE_STRUCTURE = "longitudinal-sequence"
LONGITUDINAL_CAPABILITY = "longitudinal-comparison"


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


def load_benchmarks() -> list[dict]:
    records = []
    for path in sorted(BENCHMARK_RECORDS.glob("*.yaml")):
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


def longitudinal_records(items: list[dict]) -> list[dict]:
    """Return datasets with explicit sequence data or longitudinal task support."""
    return [
        item for item in items
        if LONGITUDINAL_IMAGE_STRUCTURE in item["image_structure"]
        or LONGITUDINAL_CAPABILITY in item["capabilities"]
    ]


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
    if record.get("leaderboard"):
        badges.append(f"[![Leaderboard](https://img.shields.io/badge/Leaderboard-2E7D32?style=flat-square&logo=bar-chart&logoColor=white)]({record['leaderboard']})")
    return " ".join(badges) or "-"


def table(items: list[dict]) -> str:
    lines = ["| Dataset | Year | Structure | Capability | Scale | Grounding | Links | License / access |", "| --- | ---: | --- | --- | ---: | --- | --- | --- |"]
    for item in items:
        source = item["homepage"] or item["paper"] or item["repository"] or item["download"]
        access = "credentialed" if item["access"]["credentialing_required"] else "registration" if item["access"]["registration_required"] else "open"
        lines.append(f"| [{item['name']}]({source}) | {item['year']} | {cells(item['image_structure'])} | {cells(item['capabilities'][:2])} | {scale(item)} | {cells(item['annotation']['grounding'])} | {links(item)} | {item['license']} ({access}) |")
    return "\n".join(lines)


def benchmark_sources(record: dict, datasets: dict[str, dict]) -> str:
    names = [datasets[source["dataset_id"]]["name"] for source in record["source_datasets"]]
    names.extend(source["name"] for source in record["external_sources"])
    return ", ".join(names) or "-"


def benchmark_table(items: list[dict], datasets: dict[str, dict]) -> str:
    lines = [
        "| Benchmark | Year | Domain | Capability | Scale | Source datasets | Protocol | Links | License / access |",
        "| --- | ---: | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for item in items:
        source = item["homepage"] or item["paper"] or item["repository"] or item["download"] or item["leaderboard"]
        access = "credentialed" if item["access"]["credentialing_required"] else "registration" if item["access"]["registration_required"] else "restricted" if item["access"]["gated"] == "yes" else "open" if item["access"]["gated"] == "no" else "access unknown"
        lines.append(
            f"| [{item['name']}]({source}) | {item['year']} | {cells(item['domains'])} | "
            f"{cells(item['capabilities'][:3])} | {scale(item)} | {benchmark_sources(item, datasets)} | "
            f"{cells(item['evaluation']['protocols'])} | {links(item)} | {item['license']} ({access}; {item['source_license_policy']} sources) |"
        )
    return "\n".join(lines)


def replace_marked(text: str, name: str, content: str) -> str:
    begin, end = f"<!-- BEGIN GENERATED:{name} -->", f"<!-- END GENERATED:{name} -->"
    if begin not in text or end not in text:
        raise ValueError(f"Missing generated markers for {name}")
    before, remainder = text.split(begin, 1)
    _, after = remainder.split(end, 1)
    return f"{before}{begin}\n{content}\n{end}{after}"


def render_readme(items: list[dict], audited: list[dict], benchmarks: list[dict], audited_benchmarks: list[dict]) -> str:
    readme = (ROOT / "README.md").read_text()
    last_updated = max(item["last_verified"] for item in [*audited, *audited_benchmarks])
    by_resource_type = group_by_resource_type(items)
    longitudinal = longitudinal_records(items)
    navigation = " | ".join([
        *(f"[{resource_type_title(resource_type)}](#{resource_type})" for resource_type in RESOURCE_TYPES),
        "[Longitudinal Resources](#longitudinal-resources)",
        "[Benchmarks](#benchmarks)",
    ])
    sections = []
    for resource_type, records in by_resource_type.items():
        domains = group_by_domain(records)
        body = "\n\n".join(f"#### {domain_title(domain)}\n\n{table(group)}" for domain, group in domains.items()) or "No included records yet."
        sections.append(f"### {resource_type_title(resource_type)}\n\n{body}")
    resources = "\n\n".join(sections)
    longitudinal_domains = group_by_domain(longitudinal)
    longitudinal_content = "\n\n".join(
        f"#### {domain_title(domain)}\n\n{table(group)}"
        for domain, group in longitudinal_domains.items()
    ) or "No included longitudinal resources yet."
    longitudinal_summary = (
        f"{len(longitudinal)} included datasets with explicit longitudinal sequences "
        f"or longitudinal-comparison support. These records also remain listed under their primary resource type."
    )
    counts = Counter(capability for item in items for capability in item["capabilities"])
    capabilities = "| Capability | Datasets |\n| --- | ---: |\n" + "\n".join(f"| {capability} | {count} |" for capability, count in sorted(counts.items()))
    status_counts = Counter(item["catalog_status"] for item in audited)
    benchmark_status_counts = Counter(item["catalog_status"] for item in audited_benchmarks)
    type_counts = Counter(item["resource_type"] for item in items)
    benchmark_label = "benchmark" if len(benchmarks) == 1 else "benchmarks"
    summary = f"{len(items)} included datasets: {type_counts['text-only']} text-only, {type_counts['image-only']} image-only, and {type_counts['text-image-pairs']} text-image pairs. {status_counts['candidate']} candidate and {status_counts['excluded']} excluded dataset records are retained for auditability. {len(benchmarks)} included {benchmark_label}; {benchmark_status_counts['candidate']} candidate and {benchmark_status_counts['excluded']} excluded benchmark records are omitted from public tables."
    benchmark_pronoun = "its" if len(benchmarks) == 1 else "their"
    benchmark_summary = f"{len(benchmarks)} included benchmark{'s' if len(benchmarks) != 1 else ''}, maintained separately from {benchmark_pronoun} companion and source datasets."
    benchmark_content = benchmark_table(benchmarks, {item["id"]: item for item in audited}) if benchmarks else "No included benchmarks yet."
    rendered = replace_marked(readme, "LAST_UPDATED", f"**Last updated:** {last_updated}")
    rendered = replace_marked(rendered, "CATALOG_SUMMARY", summary)
    rendered = replace_marked(rendered, "RESOURCE_TYPE_NAV", navigation)
    rendered = replace_marked(rendered, "RESOURCE_TYPE_TABLES", resources)
    rendered = replace_marked(rendered, "LONGITUDINAL_SUMMARY", longitudinal_summary)
    rendered = replace_marked(rendered, "LONGITUDINAL_TABLE", longitudinal_content)
    rendered = replace_marked(rendered, "BENCHMARK_SUMMARY", benchmark_summary)
    rendered = replace_marked(rendered, "BENCHMARK_TABLE", benchmark_content)
    return replace_marked(rendered, "CAPABILITY_TABLE", capabilities)


def render_reports(items: list[dict], benchmarks: list[dict]) -> tuple[str, str]:
    domains = Counter(domain for item in items for domain in item["domains"])
    resource_types = Counter(item["resource_type"] for item in items)
    capabilities = Counter(capability for item in items for capability in item["capabilities"])
    benchmark_domains = Counter(domain for item in benchmarks for domain in item["domains"])
    longitudinal = longitudinal_records(items)
    longitudinal_benchmarks = [item for item in benchmarks if LONGITUDINAL_CAPABILITY in item["capabilities"]]
    landscape = "# Landscape\n\nGenerated from `datasets/` and `benchmarks/` by `scripts/generate_tables.py`.\n\n## Resource Types\n\n" + "\n".join(f"- {name}: {resource_types[name]}" for name in RESOURCE_TYPES) + "\n\n## Longitudinal Resources\n\n" + f"- datasets: {len(longitudinal)}\n- benchmarks: {len(longitudinal_benchmarks)}\n" + "\n## Domains\n\n" + "\n".join(f"- {name}: {count}" for name, count in sorted(domains.items())) + "\n\n## Capabilities\n\n" + "\n".join(f"- {name}: {count}" for name, count in sorted(capabilities.items())) + "\n\n## Benchmarks\n\n" + ("\n".join(f"- {name}: {count}" for name, count in sorted(benchmark_domains.items())) or "- None") + "\n"
    uncertain = [item["name"] for item in items if item["commercial_use"] == "unknown" or "check" in item["license"].lower()]
    uncertain_benchmarks = [item["name"] for item in benchmarks if item["commercial_use"] == "unknown" or item["license"].lower() == "unknown"]
    gaps = "# Coverage Gaps\n\nGenerated from `datasets/` and `benchmarks/` by `scripts/generate_tables.py`.\n\n- The catalog remains concentrated in 2D imaging; 3D, video, whole-slide, and longitudinal resources need broader coverage.\n- Hallucination detection and tool-use capabilities have no entries in this MVP.\n- Ophthalmology has one provisional entry and needs independently verified report-linked datasets.\n- Dataset licensing or commercial-use status needs follow-up for: " + ", ".join(uncertain) + ".\n- Benchmark licensing or commercial-use status needs follow-up for: " + (", ".join(uncertain_benchmarks) or "none") + ".\n"
    return landscape, gaps


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if generated files are stale")
    parser.add_argument("--readme-only", action="store_true", help="emit only README.md")
    args = parser.parse_args()
    try:
        audited = load_records()
        audited_benchmarks = load_benchmarks()
    except ValueError as error:
        print(error, file=sys.stderr)
        return 1
    items = published_records(audited)
    benchmarks = published_records(audited_benchmarks)
    expected = {ROOT / "README.md": render_readme(items, audited, benchmarks, audited_benchmarks)}
    if not args.readme_only:
        expected[ROOT / "reports/landscape.md"], expected[ROOT / "reports/gaps.md"] = render_reports(items, benchmarks)
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
    benchmark_status_counts = Counter(item["catalog_status"] for item in audited_benchmarks)
    benchmark_label = "benchmark" if len(benchmarks) == 1 else "benchmarks"
    print(f"Generated {'README' if args.readme_only else 'catalog views'} for {len(items)} included datasets and {len(benchmarks)} included {benchmark_label}.")
    print(f"Catalog records: {status_counts['included']} included, {status_counts['candidate']} candidate, {status_counts['excluded']} excluded.")
    print(f"Benchmark records: {benchmark_status_counts['included']} included, {benchmark_status_counts['candidate']} candidate, {benchmark_status_counts['excluded']} excluded.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
