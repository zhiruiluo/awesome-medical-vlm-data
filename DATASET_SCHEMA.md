# Dataset Record Schema

Each file under `datasets/` is a JSON-compatible YAML object validated by [schemas/dataset.schema.json](schemas/dataset.schema.json). JSON is a YAML 1.2 subset, which keeps this minimal repository dependency-free.

## Required Fields

| Field | Meaning |
| --- | --- |
| `id`, `name`, `year` | Stable identifier, display name, and release year. |
| `homepage`, `paper`, `repository`, `download` | Source URLs. At least one must be present. Use `null` when unavailable. |
| `license`, `commercial_use` | License name/status and `yes`, `no`, or `unknown`. |
| `domains`, `modalities`, `image_structure` | Taxonomy lists for the data. |
| `tasks`, `capabilities`, `usage` | VLM tasks, supported capabilities, and `training`, `evaluation`, or `training-evaluation`. |
| `annotation` | Annotation source, grounding types, and review status. |
| `scale` | Counts such as `images`, `qa_pairs`, `studies`, or `patients`; use `null` when not reported. |
| `quality` | Auditing, split, validation, and known-issue signals. |
| `access` | Registration and credentialing requirements. |
| `last_verified` | ISO date for the latest source review. |

## Generated Link Badges

The README table renders a clickable Shields.io `GitHub` badge when `repository` is set and a `Download` badge when `download` is set. Keep both fields pointed at the official source whenever they are available; generated badges are omitted only when the relevant field is `null`.

## Example

```yaml
{
  "id": "example-vqa", "name": "Example VQA", "year": 2025,
  "homepage": "https://example.org", "paper": null, "repository": null, "download": null,
  "license": "unknown", "commercial_use": "unknown",
  "domains": ["radiology"], "modalities": ["xray"], "image_structure": ["2d-single"],
  "tasks": ["visual-question-answering"], "capabilities": ["recognition"], "usage": "evaluation",
  "annotation": {"source": "human-authored", "expert_review": "yes", "grounding": ["image"]},
  "scale": {"images": 100, "qa_pairs": 1000, "patients": null},
  "quality": {"contamination_audited": "unknown", "patient_level_split": "unknown", "external_validation": "unknown", "known_issues": []},
  "access": {"registration_required": false, "credentialing_required": false}, "last_verified": "2026-08-31"
}
```
