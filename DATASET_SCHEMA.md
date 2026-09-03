# Dataset Record Schema

Each file under `datasets/records/` is a JSON-compatible YAML object validated by [schemas/dataset.schema.json](schemas/dataset.schema.json). JSON is a YAML 1.2 subset, which keeps this minimal repository dependency-free. Filesystem placement does not define specialty: use one or more controlled `domains` values from `taxonomies/domains.json`.

Evaluation suites that define protocols, metrics, or leaderboards belong in `benchmarks/records/` and follow [BENCHMARK_SCHEMA.md](BENCHMARK_SCHEMA.md). A resource that releases data and defines an evaluation suite may have linked records in both catalogs.

## Required Fields

| Field | Meaning |
| --- | --- |
| `id`, `name`, `year` | Stable identifier, display name, and release year. |
| `homepage`, `paper`, `repository`, `download` | Source URLs. At least one must be present. Use `null` when unavailable. |
| `license`, `commercial_use` | License name/status and `yes`, `no`, or `unknown`. |
| `resource_type` | Released resource composition: `text-only`, `image-only`, or `text-image-pairs`. It controls the primary README section and is distinct from annotation supervision. |
| `domains`, `modalities`, `anatomical_targets`, `image_structure` | Controlled taxonomy lists for the data. `anatomical_targets` identifies the principal imaged or annotated body region or organ. Use `multi-anatomy` only when the resource is genuinely heterogeneous. Text-only records use empty `modalities` and `image_structure`; image-bearing records must provide both. |
| `tasks`, `capabilities`, `usage` | VLM tasks, supported capabilities, and `training`, `evaluation`, or `training-evaluation`. |
| `catalog_status`, `language_supervision`, `derived_from` | Publication eligibility, language signal types, and parent dataset IDs for derived releases. Use `structured-ehr` for coded or tabular EHR events; use `report` for free-text clinical notes. Only `included` records appear in generated public tables. |
| `annotation` | Annotation source, grounding types, and review status. |
| `scale` | `primary_count` and `primary_unit` drive generated tables; retain counts such as `images`, `qa_pairs`, `studies`, or `patients` as supporting detail. |
| `quality` | Auditing, split, validation, and known-issue signals. |
| `access` | Registration, credentialing, gating, data-use agreement, and citation requirements. |
| `last_verified` | ISO date for the latest source review. |

## Generated Link Badges

The README table renders a clickable Shields.io `GitHub` badge when `repository` is set and a `Download` badge when `download` is set. Keep both fields pointed at the official source whenever they are available; generated badges are omitted only when the relevant field is `null`.

## Example

```yaml
{
  "id": "example-vqa", "name": "Example VQA", "year": 2025,
  "homepage": "https://example.org", "paper": null, "repository": null, "download": null,
  "license": "unknown", "commercial_use": "unknown", "resource_type": "text-image-pairs",
  "domains": ["radiology"], "modalities": ["xray"], "anatomical_targets": ["chest"], "image_structure": ["2d-single"],
  "tasks": ["visual-question-answering"], "capabilities": ["recognition"], "usage": "evaluation",
  "catalog_status": "included", "language_supervision": ["question-answer"], "derived_from": [],
  "annotation": {"source": "human-authored", "expert_review": "yes", "grounding": ["image"]},
  "scale": {"primary_count": 1000, "primary_unit": "qa-pairs", "images": 100, "qa_pairs": 1000, "patients": null},
  "quality": {"contamination_audited": "unknown", "patient_level_split": "unknown", "external_validation": "unknown", "known_issues": []},
  "access": {"registration_required": false, "credentialing_required": false, "gated": "no", "data_use_agreement_required": "unknown", "citation_required": "yes"}, "last_verified": "2026-08-31"
}
```
