# Medical VLM Data Intelligence

> Generated from the records in `datasets/`. Do not edit the tables by hand; run `python3 scripts/generate_tables.py`.

Curated datasets and benchmarks for medical vision-language models. Every entry includes its clinical domain, image structure, supervision, access constraints, licensing status, and evidence-backed quality signals.

## Quick Start

```bash
python3 scripts/validate_records.py
python3 scripts/generate_tables.py
python3 scripts/check_links.py --timeout 15
```

## How To Use This Repository

- **Training data:** choose entries marked `training` or `training-evaluation`; check the license and access flags before use.
- **Evaluation:** select `evaluation` entries by domain and capability, then confirm the official split and terms.
- **Grounding and reasoning:** use the grounding and annotation columns to distinguish image-only QA from report, region, or article-context supervision.

## Dataset Directory

<!-- BEGIN GENERATED:MASTER_TABLE -->
| Dataset | Domain | Structure | Capability | Scale | Grounding | License / access |
| --- | --- | --- | --- | ---: | --- | --- |
| [CT-RATE](https://stanfordmlgroup.github.io/projects/ct-rate/) | radiology | 3d-volume | description, diagnosis | 25.7K studies | report | CC BY-NC-SA 4.0 (registration) |
| [FairVLMed](https://github.com/Harvard-Ophthalmology-AI-Lab/FairCLIP) | ophthalmology | 2d-single | recognition, diagnosis | 10.0K images | report | CC BY-NC-ND 4.0 (registration) |
| [MIMIC-CXR](https://physionet.org/content/mimic-cxr/2.1.0/) | radiology | multi-view | description, report-generation | 227.8K studies | report | PhysioNet Credentialed Health Data License 1.5.0 (credentialed) |
| [PathVQA](https://pathvqa.com/) | pathology | 2d-single | recognition, diagnosis | 32.8K QA | image, caption | Check source terms (open) |
| [PMC-VQA](https://xiaoman-zhang.github.io/PMC-VQA/) | general-biomedical | 2d-single | recognition, reasoning | 227.0K QA | figure, caption, article-context | Check source terms (open) |
| [Quilt-1M](https://quilt1m.github.io/) | pathology | 2d-single | description, recognition | 1.0M images | caption | Research use agreement; restricted access (registration) |
| [SLAKE](https://www.med-vqa.com/slake/) | general-biomedical | 2d-single | recognition, diagnosis | 14.0K QA | image, knowledge-graph | Research use; check source terms (open) |
| [VQA-RAD](https://www.nlm.nih.gov/research/visible/vqarad/index.html) | radiology | 2d-single | recognition, diagnosis | 3.5K QA | image | Research use; check source terms (open) |
<!-- END GENERATED:MASTER_TABLE -->

## By Specialty

<!-- BEGIN GENERATED:DOMAIN_TABLES -->
### General Biomedical

| Dataset | Domain | Structure | Capability | Scale | Grounding | License / access |
| --- | --- | --- | --- | ---: | --- | --- |
| [PMC-VQA](https://xiaoman-zhang.github.io/PMC-VQA/) | general-biomedical | 2d-single | recognition, reasoning | 227.0K QA | figure, caption, article-context | Check source terms (open) |
| [SLAKE](https://www.med-vqa.com/slake/) | general-biomedical | 2d-single | recognition, diagnosis | 14.0K QA | image, knowledge-graph | Research use; check source terms (open) |

### Ophthalmology

| Dataset | Domain | Structure | Capability | Scale | Grounding | License / access |
| --- | --- | --- | --- | ---: | --- | --- |
| [FairVLMed](https://github.com/Harvard-Ophthalmology-AI-Lab/FairCLIP) | ophthalmology | 2d-single | recognition, diagnosis | 10.0K images | report | CC BY-NC-ND 4.0 (registration) |

### Pathology

| Dataset | Domain | Structure | Capability | Scale | Grounding | License / access |
| --- | --- | --- | --- | ---: | --- | --- |
| [PathVQA](https://pathvqa.com/) | pathology | 2d-single | recognition, diagnosis | 32.8K QA | image, caption | Check source terms (open) |
| [Quilt-1M](https://quilt1m.github.io/) | pathology | 2d-single | description, recognition | 1.0M images | caption | Research use agreement; restricted access (registration) |

### Radiology

| Dataset | Domain | Structure | Capability | Scale | Grounding | License / access |
| --- | --- | --- | --- | ---: | --- | --- |
| [CT-RATE](https://stanfordmlgroup.github.io/projects/ct-rate/) | radiology | 3d-volume | description, diagnosis | 25.7K studies | report | CC BY-NC-SA 4.0 (registration) |
| [MIMIC-CXR](https://physionet.org/content/mimic-cxr/2.1.0/) | radiology | multi-view | description, report-generation | 227.8K studies | report | PhysioNet Credentialed Health Data License 1.5.0 (credentialed) |
| [VQA-RAD](https://www.nlm.nih.gov/research/visible/vqarad/index.html) | radiology | 2d-single | recognition, diagnosis | 3.5K QA | image | Research use; check source terms (open) |
<!-- END GENERATED:DOMAIN_TABLES -->

## Capability Coverage

<!-- BEGIN GENERATED:CAPABILITY_TABLE -->
| Capability | Datasets |
| --- | ---: |
| description | 5 |
| diagnosis | 6 |
| reasoning | 4 |
| recognition | 6 |
| report-generation | 2 |
<!-- END GENERATED:CAPABILITY_TABLE -->

## Caveats

Dataset metadata records describe sources, not legal advice. `unknown` and `unclear` mean the contributor could not establish an answer from an official source. Credentialed resources may require a data-use agreement or training before download. See [DATASET_SCHEMA.md](DATASET_SCHEMA.md) for field definitions and [reports/gaps.md](reports/gaps.md) for coverage gaps.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) and follow the [record workflow](WORKFLOW.md). Add one JSON-compatible YAML record per dataset, run validation, and commit the regenerated final report.
