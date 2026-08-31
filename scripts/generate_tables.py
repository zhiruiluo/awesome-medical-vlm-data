#!/usr/bin/env python3
"""Generate catalog views from JSON-compatible YAML dataset records."""
from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def records() -> list[dict]:
    return sorted((json.loads(path.read_text()) for path in (ROOT / "datasets").rglob("*.yaml")), key=lambda item: item["name"].lower())


def cells(values: list[str]) -> str:
    return ", ".join(values)


def scale(record: dict) -> str:
    for key, label in (("qa_pairs", "QA"), ("studies", "studies"), ("images", "images")):
        value = record["scale"].get(key)
        if value is not None:
            return f"{value / 1_000_000:.1f}M {label}" if value >= 1_000_000 else f"{value / 1_000:.1f}K {label}" if value >= 1_000 else f"{value} {label}"
    return "Not reported"


def links(record: dict) -> str:
    badges = []
    if record.get("repository"):
        badges.append(f"[GitHub]({record['repository']})")
    if record.get("download"):
        badges.append(f"[Download]({record['download']})")
    return " ".join(badges) or "-"


def table(items: list[dict]) -> str:
    lines = ["| Dataset | Domain | Structure | Capability | Scale | Grounding | Links | License / access |", "| --- | --- | --- | --- | ---: | --- | --- | --- |"]
    for item in items:
        source = item["homepage"] or item["paper"] or item["repository"] or item["download"]
        access = "credentialed" if item["access"]["credentialing_required"] else "registration" if item["access"]["registration_required"] else "open"
        lines.append(f"| [{item['name']}]({source}) | {cells(item['domains'])} | {cells(item['image_structure'])} | {cells(item['capabilities'][:2])} | {scale(item)} | {cells(item['annotation']['grounding'])} | {links(item)} | {item['license']} ({access}) |")
    return "\n".join(lines)


def replace_marked(text: str, name: str, content: str) -> str:
    begin, end = f"<!-- BEGIN GENERATED:{name} -->", f"<!-- END GENERATED:{name} -->"
    if begin not in text or end not in text:
        raise ValueError(f"Missing generated markers for {name}")
    before, remainder = text.split(begin, 1)
    _, after = remainder.split(end, 1)
    return f"{before}{begin}\n{content}\n{end}{after}"


def render_readme(items: list[dict]) -> str:
    readme = (ROOT / "README.md").read_text()
    by_domain: dict[str, list[dict]] = defaultdict(list)
    for item in items:
        for domain in item["domains"]:
            by_domain[domain].append(item)
    domains = "\n\n".join(f"### {domain.replace('-', ' ').title()}\n\n{table(group)}" for domain, group in sorted(by_domain.items()))
    counts = Counter(capability for item in items for capability in item["capabilities"])
    capabilities = "| Capability | Datasets |\n| --- | ---: |\n" + "\n".join(f"| {capability} | {count} |" for capability, count in sorted(counts.items()))
    return replace_marked(replace_marked(replace_marked(readme, "MASTER_TABLE", table(items)), "DOMAIN_TABLES", domains), "CAPABILITY_TABLE", capabilities)


def render_reports(items: list[dict]) -> tuple[str, str]:
    domains = Counter(domain for item in items for domain in item["domains"])
    capabilities = Counter(capability for item in items for capability in item["capabilities"])
    landscape = "# Landscape\n\nGenerated from `datasets/` by `scripts/generate_tables.py`.\n\n## Domains\n\n" + "\n".join(f"- {name}: {count}" for name, count in sorted(domains.items())) + "\n\n## Capabilities\n\n" + "\n".join(f"- {name}: {count}" for name, count in sorted(capabilities.items())) + "\n"
    uncertain = [item["name"] for item in items if item["commercial_use"] == "unknown" or "check" in item["license"].lower()]
    gaps = "# Coverage Gaps\n\nGenerated from `datasets/` by `scripts/generate_tables.py`.\n\n- The catalog is currently concentrated in 2D imaging; 3D, video, whole-slide, and longitudinal resources need more coverage.\n- Localization, segmentation, measurement, hallucination detection, and tool-use capabilities have no entries in this MVP.\n- Ophthalmology has one provisional entry and needs independently verified report-linked datasets.\n- Licensing or commercial-use status needs follow-up for: " + ", ".join(uncertain) + ".\n"
    return landscape, gaps


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if generated files are stale")
    args = parser.parse_args()
    items = records()
    expected = {ROOT / "README.md": render_readme(items)}
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
    print(f"Generated catalog views for {len(items)} datasets.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
