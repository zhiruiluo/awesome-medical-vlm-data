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

## Catalog Status

<!-- BEGIN GENERATED:CATALOG_SUMMARY -->
13 included medical VLM datasets across 4 specialties. 5 candidate and 1 excluded records are retained for auditability but omitted from the tables below.
<!-- END GENERATED:CATALOG_SUMMARY -->

## By Specialty

<!-- BEGIN GENERATED:DOMAIN_NAV -->
[Radiology](#radiology) | [Pathology](#pathology) | [Ophthalmology](#ophthalmology) | [General Biomedical](#general-biomedical)
<!-- END GENERATED:DOMAIN_NAV -->

<!-- BEGIN GENERATED:DOMAIN_TABLES -->
### Radiology

| Dataset | Year | Structure | Capability | Scale | Grounding | Links | License / access |
| --- | ---: | --- | --- | ---: | --- | --- | --- |
| [CT-RATE](https://stanfordmlgroup.github.io/projects/ct-rate/) | 2024 | 3d-volume | description, diagnosis | 25.7K studies | report | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ibrahimethemhamci/CT-RATE) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://huggingface.co/datasets/ibrahimhamamci/CT-RATE) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://arxiv.org/abs/2403.17834) | CC BY-NC-SA 4.0 (registration) |
| [IU X-Ray](https://openi.nlm.nih.gov/) | 2016 | multi-view | description, report-generation | 4.0K reports | report | [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://www.kaggle.com/datasets/raddar/chest-xrays-indiana-university) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://pubmed.ncbi.nlm.nih.gov/27701286/) | Per-image Open-i terms; check source (open) |
| [MIMIC-CXR](https://physionet.org/content/mimic-cxr/2.1.0/) | 2019 | multi-view | description, report-generation | 227.8K studies | report | [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://physionet.org/content/mimic-cxr/2.1.0/) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://doi.org/10.1038/s41597-019-0322-0) | PhysioNet Credentialed Health Data License 1.5.0 (credentialed) |
| [ROCOv2](https://zenodo.org/records/10821435) | 2023 | 2d-single | description, recognition | 79.8K image-caption-pairs | caption, medical-concepts | [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://zenodo.org/records/10821435) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://arxiv.org/abs/2405.10004) | Per-image license information included; check source (registration) |
| [RP3D-Caption](https://chaoyi-wu.github.io/RadFM/) | 2023 | 3d-volume | description, diagnosis | 69.5K image-text-pairs | caption, case-context | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/chaoyi-wu/RadFM) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://huggingface.co/datasets/chaoyi-wu/RadFM_data_csv) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://arxiv.org/abs/2308.02463) | Radiopaedia non-commercial use with approval (open) |
| [VQA-RAD](https://www.nlm.nih.gov/research/visible/vqarad/index.html) | 2018 | 2d-single | recognition, diagnosis | 3.5K qa-pairs | image | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/cuhksz-nlp/VQA-RAD) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://www.nlm.nih.gov/research/visible/vqarad/index.html) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://doi.org/10.1038/sdata.2018.251) | Research use; check source terms (open) |

### Pathology

| Dataset | Year | Structure | Capability | Scale | Grounding | Links | License / access |
| --- | ---: | --- | --- | ---: | --- | --- | --- |
| [PathVQA](https://pathvqa.com/) | 2020 | 2d-single | recognition, diagnosis | 32.8K qa-pairs | image, caption | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/UCSD-AI4H/PathVQA) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://pathvqa.com/) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://arxiv.org/abs/2003.10286) | Check source terms (open) |
| [Quilt-1M](https://quilt1m.github.io/) | 2023 | 2d-single | description, recognition | 1.0M image-text-pairs | caption | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/wisdomikezogwo/quilt1m) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://huggingface.co/datasets/wisdomik/Quilt-1M) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://arxiv.org/abs/2306.11207) | Research use agreement; restricted access (registration) |

### Ophthalmology

| Dataset | Year | Structure | Capability | Scale | Grounding | Links | License / access |
| --- | ---: | --- | --- | ---: | --- | --- | --- |
| [FairVLMed](https://github.com/Harvard-Ophthalmology-AI-Lab/FairCLIP) | 2024 | 2d-single | recognition, diagnosis | 10.0K images | report | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Harvard-Ophthalmology-AI-Lab/FairCLIP) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://arxiv.org/abs/2403.14774) | CC BY-NC-ND 4.0 (registration) |

### General Biomedical

| Dataset | Year | Structure | Capability | Scale | Grounding | Links | License / access |
| --- | ---: | --- | --- | ---: | --- | --- | --- |
| [ImageCLEF VQA-Med 2019](https://github.com/abachaa/VQA-Med-2019) | 2019 | 2d-single | recognition, diagnosis | 15.3K questions | image | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/abachaa/VQA-Med-2019) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://github.com/abachaa/VQA-Med-2019) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://ceur-ws.org/Vol-2380/paper_275.pdf) | ImageCLEF terms; image copyrights vary (open) |
| [MedICaT](https://github.com/allenai/medicat) | 2020 | 2d-single | description, localization | 217.1K figures | caption, subfigure, article-context | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/allenai/medicat) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://ai2-s2-medicat.s3.us-west-2.amazonaws.com/2020-10-05/medicat_release.tar.gz) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://arxiv.org/abs/2010.06000) | Per-document open-access license; research use only (open) |
| [PMC-VQA](https://xiaoman-zhang.github.io/PMC-VQA/) | 2023 | 2d-single | recognition, reasoning | 227.0K qa-pairs | figure, caption, article-context | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/xiaoman-zhang/PMC-VQA) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://huggingface.co/datasets/xmcmic/PMC-VQA) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://arxiv.org/abs/2305.10415) | Check source terms (open) |
| [SLAKE](https://www.med-vqa.com/slake/) | 2021 | 2d-single | recognition, diagnosis | 14.0K qa-pairs | image, knowledge-graph | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/haifangong/SLAKE) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://www.med-vqa.com/slake/) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://arxiv.org/abs/2102.09542) | Research use; check source terms (open) |
<!-- END GENERATED:DOMAIN_TABLES -->

## Capability Coverage

<!-- BEGIN GENERATED:CAPABILITY_TABLE -->
| Capability | Datasets |
| --- | ---: |
| description | 9 |
| diagnosis | 9 |
| localization | 1 |
| reasoning | 5 |
| recognition | 8 |
| report-generation | 3 |
| spatial-reasoning | 1 |
<!-- END GENERATED:CAPABILITY_TABLE -->

## Caveats

Dataset metadata records describe sources, not legal advice. `unknown` and `unclear` mean the contributor could not establish an answer from an official source. Credentialed resources may require a data-use agreement or training before download. See [DATASET_SCHEMA.md](DATASET_SCHEMA.md) for field definitions and [reports/gaps.md](reports/gaps.md) for coverage gaps.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) and follow the [record workflow](WORKFLOW.md). Add one JSON-compatible YAML record per dataset, run validation, and commit the regenerated final report.
