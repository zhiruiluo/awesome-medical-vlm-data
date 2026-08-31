# Awesome Medical VLM Data

A structured catalog of datasets and benchmarks for training and evaluating vision-language models on medical images.

This repository covers image–text pairs, visual question answering, grounded annotations, report generation, multimodal reasoning, longitudinal comparison, hallucination evaluation, and medical-image agent tasks.

It goes beyond collecting links by documenting each resource’s:

Imaging modalities and clinical domains
Dataset scale and input structure
Training and evaluation capabilities
Annotation sources and generation methods
Spatial grounding and reasoning supervision
Clinical or expert validation
Patient-level splits and contamination analysis
Licensing, access, and commercial-use restrictions


## Quick Start
> Generated from the records in `datasets/`. Do not edit generated tables by hand; run `python3 scripts/generate_tables.py`.

```bash
python3 scripts/validate_records.py
python3 scripts/generate_tables.py
python3 scripts/check_links.py --timeout 15
```

## By Specialty

<!-- BEGIN GENERATED:DOMAIN_TABLES -->
### General Biomedical

| Dataset | Structure | Capability | Scale | Grounding | Links | License / access |
| --- | --- | --- | ---: | --- | --- | --- |
| [PMC-VQA](https://xiaoman-zhang.github.io/PMC-VQA/) | 2d-single | recognition, reasoning | 227.0K qa-pairs | figure, caption, article-context | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/xiaoman-zhang/PMC-VQA) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://huggingface.co/datasets/xmcmic/PMC-VQA) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://arxiv.org/abs/2305.10415) | Check source terms (open) |
| [SLAKE](https://www.med-vqa.com/slake/) | 2d-single | recognition, diagnosis | 14.0K qa-pairs | image, knowledge-graph | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/haifangong/SLAKE) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://www.med-vqa.com/slake/) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://arxiv.org/abs/2102.09542) | Research use; check source terms (open) |

### Ophthalmology

| Dataset | Structure | Capability | Scale | Grounding | Links | License / access |
| --- | --- | --- | ---: | --- | --- | --- |
| [FairVLMed](https://github.com/Harvard-Ophthalmology-AI-Lab/FairCLIP) | 2d-single | recognition, diagnosis | 10.0K images | report | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Harvard-Ophthalmology-AI-Lab/FairCLIP) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://arxiv.org/abs/2403.14774) | CC BY-NC-ND 4.0 (registration) |

### Pathology

| Dataset | Structure | Capability | Scale | Grounding | Links | License / access |
| --- | --- | --- | ---: | --- | --- | --- |
| [PathVQA](https://pathvqa.com/) | 2d-single | recognition, diagnosis | 32.8K qa-pairs | image, caption | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/UCSD-AI4H/PathVQA) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://pathvqa.com/) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://arxiv.org/abs/2003.10286) | Check source terms (open) |
| [Quilt-1M](https://quilt1m.github.io/) | 2d-single | description, recognition | 1.0M image-text-pairs | caption | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/wisdomikezogwo/quilt1m) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://huggingface.co/datasets/wisdomik/Quilt-1M) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://arxiv.org/abs/2306.11207) | Research use agreement; restricted access (registration) |

### Radiology

| Dataset | Structure | Capability | Scale | Grounding | Links | License / access |
| --- | --- | --- | ---: | --- | --- | --- |
| [CT-RATE](https://stanfordmlgroup.github.io/projects/ct-rate/) | 3d-volume | description, diagnosis | 25.7K studies | report | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ibrahimethemhamci/CT-RATE) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://huggingface.co/datasets/ibrahimhamamci/CT-RATE) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://arxiv.org/abs/2403.17834) | CC BY-NC-SA 4.0 (registration) |
| [MIMIC-CXR](https://physionet.org/content/mimic-cxr/2.1.0/) | multi-view | description, report-generation | 227.8K studies | report | [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://physionet.org/content/mimic-cxr/2.1.0/) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://doi.org/10.1038/s41597-019-0322-0) | PhysioNet Credentialed Health Data License 1.5.0 (credentialed) |
| [VQA-RAD](https://www.nlm.nih.gov/research/visible/vqarad/index.html) | 2d-single | recognition, diagnosis | 3.5K qa-pairs | image | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/cuhksz-nlp/VQA-RAD) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://www.nlm.nih.gov/research/visible/vqarad/index.html) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://doi.org/10.1038/sdata.2018.251) | Research use; check source terms (open) |
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
