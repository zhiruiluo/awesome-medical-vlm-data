<div align="center">

# Awesome Medical VLM Dataset & Benchmark

### A data intelligence layer for medical multimodal datasets and benchmarks.

</div>

<p align="center">
 <a href="https://awesome.re" alt="Awesome">
    <img src="https://awesome.re/badge.svg" />
 </a>
 <a href="https://www.linkedin.com/in/luobill2017/" alt="LinkedIn">
    <img src="https://img.shields.io/badge/LinkedIn-Connect-blue">
 </a>
</p>

---

<!-- BEGIN GENERATED:LAST_UPDATED -->
**Last updated:** 2026-09-01
<!-- END GENERATED:LAST_UPDATED -->

A maintained, machine-readable catalog of medical AI datasets and benchmarks for training and evaluation. Datasets describe released data; benchmarks separately describe evaluation protocols, metrics, and their constituent datasets.

Resources are organized by the data they release:

- **Text Only:** clinical and biomedical language resources.
- **Image Only:** medical images with labels, bounding boxes, masks, or other visual annotations.
- **Text-Image Pairs:** reports, captions, question-answer pairs, grounded text, and other image-language supervision.

Each dataset is a version-controlled record in `datasets/records/`, not just a link. Records capture clinical domains and modalities, release year and scale, tasks and capabilities, annotation provenance and expert review, spatial grounding, quality signals, and access or license restrictions. `included`, `candidate`, and `excluded` statuses make the catalog's publication decisions auditable.


## Quick Start
> Generated from the records in `datasets/` and `benchmarks/`. Do not edit generated content by hand; run `python3 scripts/generate_tables.py`.

```bash
python3 scripts/validate_records.py
python3 scripts/format_records.py --check
python3 scripts/generate_tables.py
python3 scripts/check_links.py --timeout 15
```

## Catalog Status

<!-- BEGIN GENERATED:CATALOG_SUMMARY -->
28 included datasets: 0 text-only, 13 image-only, and 15 text-image pairs. 48 candidate and 1 excluded dataset records are retained for auditability. 1 included benchmark; 0 candidate and 0 excluded benchmark records are omitted from public tables.
<!-- END GENERATED:CATALOG_SUMMARY -->

## Catalog Navigation

<!-- BEGIN GENERATED:RESOURCE_TYPE_NAV -->
[Text Only](#text-only) | [Image Only](#image-only) | [Text-Image Pairs](#text-image-pairs) | [Benchmarks](#benchmarks)
<!-- END GENERATED:RESOURCE_TYPE_NAV -->

## Datasets By Resource Type

<!-- BEGIN GENERATED:RESOURCE_TYPE_TABLES -->
### Text Only

No included records yet.

### Image Only

#### Radiology

| Dataset | Year | Structure | Capability | Scale | Grounding | Links | License / access |
| --- | ---: | --- | --- | ---: | --- | --- | --- |
| [LUNA16](https://luna16.grand-challenge.org/) | 2016 | 3d-volume | localization, diagnosis | 888 studies | coordinates, diameter | [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://luna16.grand-challenge.org/Download/) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://doi.org/10.1016/j.media.2017.06.015) | CC BY 4.0 (open) |
| [ChestX-ray14](https://nihcc.app.box.com/v/ChestXray-NIHCC) | 2017 | 2d-single | recognition, diagnosis | 112.1K images | image-label | [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://nihcc.app.box.com/v/ChestXray-NIHCC) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://arxiv.org/abs/1705.02315) | NIH source terms; check source (open) |
| [RSNA Pneumonia Detection Challenge](https://www.rsna.org/education/ai-resources-and-training/%20%5C%20ai-image-challenge/RSNA-Pneumonia-Detection-Challenge-2018) | 2018 | 2d-single | recognition, diagnosis | 30.0K examinations | bounding-box, image-label | [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://www.kaggle.com/competitions/rsna-pneumonia-detection-challenge) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://doi.org/10.1148/ryai.2019180041) | RSNA attribution terms (registration) |
| [SIIM-ACR Pneumothorax Segmentation](https://www.kaggle.com/competitions/siim-acr-pneumothorax-segmentation) | 2019 | 2d-single | recognition, diagnosis | 12.0K images | segmentation-mask, image-label | [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://www.kaggle.com/competitions/siim-acr-pneumothorax-segmentation) | Kaggle competition terms (registration) |
| [ChestX-Det10](https://github.com/Deepwise-AILab/ChestX-Det10-Dataset) | 2020 | 2d-single | recognition, diagnosis | 3.5K images | bounding-box | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Deepwise-AILab/ChestX-Det10-Dataset) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://arxiv.org/abs/2006.10550) | Unknown (open) |
| [COVID-19-AR](https://wiki.cancerimagingarchive.net/pages/viewpage.action?pageId=70226443) | 2020 | 2d-single, 3d-volume | recognition, diagnosis | 105 patients | image-label | [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://www.cancerimagingarchive.net/collection/covid-19-ar/) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://doi.org/10.7937/tcia.2020.py71-5978) | TCIA collection terms; check source (open) |
| [VinDr-CXR](https://github.com/vinbigdata-medical/vindr-cxr) | 2021 | 2d-single | recognition, diagnosis | 18.0K images | image-label, bounding-box | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/vinbigdata-medical/vindr-cxr) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://physionet.org/content/vindr-cxr/1.0.0/) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://arxiv.org/abs/2012.15029) | PhysioNet Credentialed Health Data License 1.5.0 (credentialed) |
| [CheXlocalize](https://github.com/rajpurkarlab/cheXlocalize) | 2022 | 2d-single | recognition, localization | 902 images | segmentation-mask, point | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/rajpurkarlab/cheXlocalize) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://aimi.stanford.edu/datasets/chexlocalize) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://doi.org/10.1038/s42256-022-00536-x) | MIT license (registration) |

#### Ophthalmology

| Dataset | Year | Structure | Capability | Scale | Grounding | Links | License / access |
| --- | ---: | --- | --- | ---: | --- | --- | --- |
| [CHASE_DB1](https://researchinnovation.kingston.ac.uk/en/datasets/chasedb1-retinal-vessel-reference-dataset-4/) | 2011 | 2d-single | segmentation | 28 images | segmentation-mask | [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://researchinnovation.kingston.ac.uk/en/datasets/chasedb1-retinal-vessel-reference-dataset-4/) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://doi.org/10.1109/TBME.2012.2205687) | CC BY 4.0 (open) |
| [ACPS](https://people.duke.edu/~sf59/Chiu_BOE_2013_dataset.htm) | 2013 | 2d-single | segmentation | 840 images | segmentation-mask | [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://people.duke.edu/~sf59/Chiu_BOE_2013_dataset.htm) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://doi.org/10.1364/BOE.4.000924) | Unknown (open) |
| [ROSE](https://imed.nimte.ac.cn/dataofrose.html) | 2020 | 2d-single | segmentation | 229 images | segmentation-mask | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/iMED-Lab/ROSE) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://imed.nimte.ac.cn/dataofrose.html) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://doi.org/10.1109/TMI.2020.3042802) | Academic research use only (open) |
| [FIVES](https://figshare.com/articles/figure/FIVES_A_Fundus_Image_Dataset_for_AI-based_Vessel_Segmentation/19688169/1) | 2022 | 2d-single | segmentation | 800 images | segmentation-mask | [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://figshare.com/articles/figure/FIVES_A_Fundus_Image_Dataset_for_AI-based_Vessel_Segmentation/19688169/1) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://doi.org/10.1038/s41597-022-01564-3) | CC BY 4.0 (open) |
| [Cataract-1K](https://github.com/Negin-Ghamsarian/Cataract-1K) | 2024 | video | segmentation | 1.0K videos | segmentation-mask | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Negin-Ghamsarian/Cataract-1K) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://github.com/Negin-Ghamsarian/Cataract-1K) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://arxiv.org/abs/2312.06295) | CC BY 4.0 (open) |

#### Surgery

| Dataset | Year | Structure | Capability | Scale | Grounding | Links | License / access |
| --- | ---: | --- | --- | ---: | --- | --- | --- |
| [Cataract-1K](https://github.com/Negin-Ghamsarian/Cataract-1K) | 2024 | video | segmentation | 1.0K videos | segmentation-mask | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Negin-Ghamsarian/Cataract-1K) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://github.com/Negin-Ghamsarian/Cataract-1K) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://arxiv.org/abs/2312.06295) | CC BY 4.0 (open) |

### Text-Image Pairs

#### Radiology

| Dataset | Year | Structure | Capability | Scale | Grounding | Links | License / access |
| --- | ---: | --- | --- | ---: | --- | --- | --- |
| [IU X-Ray](https://openi.nlm.nih.gov/) | 2016 | multi-view | description, report-generation | 4.0K reports | report | [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://www.kaggle.com/datasets/raddar/chest-xrays-indiana-university) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://pubmed.ncbi.nlm.nih.gov/27701286/) | CC BY-NC-ND 4.0 (open) |
| [VQA-RAD](https://www.nlm.nih.gov/research/visible/vqarad/index.html) | 2018 | 2d-single | recognition, diagnosis | 3.5K qa-pairs | image | [![Hugging Face](https://img.shields.io/badge/Hugging%20Face-FF6C37?style=flat-square&logo=huggingface&logoColor=white)](https://huggingface.co/datasets/flaviagiammarino/vqa-rad) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://huggingface.co/datasets/flaviagiammarino/vqa-rad) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://doi.org/10.1038/sdata.2018.251) | Research use; check source terms (open) |
| [MIMIC-CXR](https://physionet.org/content/mimic-cxr/2.1.0/) | 2019 | multi-view | description, report-generation | 227.8K studies | report | [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://www.kaggle.com/datasets/simhadrisadaram/mimic-cxr-dataset) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://doi.org/10.1038/s41597-019-0322-0) | PhysioNet Credentialed Health Data License 1.5.0 (credentialed) |
| [ROCOv2](https://zenodo.org/records/10821435) | 2023 | 2d-single | description, recognition | 79.8K image-caption-pairs | caption, medical-concepts | [![Hugging Face](https://img.shields.io/badge/Hugging%20Face-FF6C37?style=flat-square&logo=huggingface&logoColor=white)](https://huggingface.co/datasets/eltorio/ROCOv2-radiology) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://zenodo.org/records/10821435) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://arxiv.org/abs/2405.10004) | CC BY-NC 4.0 (registration) |
| [RP3D-Caption](https://chaoyi-wu.github.io/RadFM/) | 2023 | 3d-volume | description, diagnosis | 69.5K image-text-pairs | caption, case-context | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/chaoyi-wu/RadFM) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://huggingface.co/datasets/chaoyi-wu/RadFM_data_csv) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://arxiv.org/abs/2308.02463) | Radiopaedia non-commercial use with approval (open) |
| [CT-RATE](https://stanfordmlgroup.github.io/projects/ct-rate/) | 2024 | 3d-volume | description, diagnosis | 25.7K studies | report | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ibrahimethemhamci/CT-RATE) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://huggingface.co/datasets/ibrahimhamamci/CT-RATE) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://arxiv.org/abs/2403.17834) | CC BY-NC-SA 4.0 (registration) |

#### Pathology

| Dataset | Year | Structure | Capability | Scale | Grounding | Links | License / access |
| --- | ---: | --- | --- | ---: | --- | --- | --- |
| [PathVQA](https://huggingface.co/datasets/flaviagiammarino/path-vqa) | 2020 | 2d-single | recognition, diagnosis | 32.8K qa-pairs | image, caption | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/UCSD-AI4H/PathVQA) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://huggingface.co/datasets/flaviagiammarino/path-vqa) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://arxiv.org/abs/2003.10286) | MIT (open) |
| [Quilt-1M](https://quilt1m.github.io/) | 2023 | 2d-single | description, recognition | 1.0M image-text-pairs | caption | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/wisdomikezogwo/quilt1m) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://zenodo.org/records/8239942) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://arxiv.org/abs/2306.11207) | Research use agreement; restricted access (registration) |

#### Ophthalmology

| Dataset | Year | Structure | Capability | Scale | Grounding | Links | License / access |
| --- | ---: | --- | --- | ---: | --- | --- | --- |
| [FairVLMed](https://github.com/Harvard-Ophthalmology-AI-Lab/FairCLIP) | 2024 | 2d-single | recognition, diagnosis | 10.0K images | report | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Harvard-Ophthalmology-AI-Lab/FairCLIP) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://arxiv.org/abs/2403.14774) | CC BY-NC-ND 4.0 (registration) |

#### Endoscopy

| Dataset | Year | Structure | Capability | Scale | Grounding | Links | License / access |
| --- | ---: | --- | --- | ---: | --- | --- | --- |
| [EndoBench](https://github.com/CUHK-AIM-Group/EndoBench) | 2025 | 2d-single | recognition, diagnosis | 6.8K question-answer-pairs | question-answer | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/CUHK-AIM-Group/EndoBench) | Apache-2.0 (open) |

#### Dermatology

| Dataset | Year | Structure | Capability | Scale | Grounding | Links | License / access |
| --- | ---: | --- | --- | ---: | --- | --- | --- |
| [Derm1M](https://github.com/SiyuanYan1/Derm1M) | 2025 | 2d-single | recognition, description | 1.0M image-text-pairs | image-caption | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/SiyuanYan1/Derm1M) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://huggingface.co/datasets/redlessone/Derm1M) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://arxiv.org/abs/2503.14911) | CC BY-NC-4.0 (open) |

#### General Biomedical

| Dataset | Year | Structure | Capability | Scale | Grounding | Links | License / access |
| --- | ---: | --- | --- | ---: | --- | --- | --- |
| [ImageCLEF VQA-Med 2019](https://github.com/abachaa/VQA-Med-2019) | 2019 | 2d-single | recognition, diagnosis | 15.3K questions | image | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/abachaa/VQA-Med-2019) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://github.com/abachaa/VQA-Med-2019) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://ceur-ws.org/Vol-2380/paper_275.pdf) | ImageCLEF terms; image copyrights vary (open) |
| [MedICaT](https://github.com/allenai/medicat) | 2020 | 2d-single | description, localization | 217.1K figures | caption, subfigure, article-context | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/allenai/medicat) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://ai2-s2-medicat.s3.us-west-2.amazonaws.com/2020-10-05/medicat_release.tar.gz) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://arxiv.org/abs/2010.06000) | Per-document open-access license; research use only (open) |
| [SLAKE](https://www.med-vqa.com/slake/) | 2021 | 2d-single | recognition, diagnosis | 14.0K qa-pairs | image, knowledge-graph | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/haifangong/SLAKE) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://www.med-vqa.com/slake/) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://arxiv.org/abs/2102.09542) | Research use; check source terms (open) |
| [PMC-VQA](https://xiaoman-zhang.github.io/PMC-VQA/) | 2023 | 2d-single | recognition, reasoning | 227.0K qa-pairs | figure, caption, article-context | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/xiaoman-zhang/PMC-VQA) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://huggingface.co/datasets/xmcmic/PMC-VQA) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://arxiv.org/abs/2305.10415) | Check source terms (open) |
<!-- END GENERATED:RESOURCE_TYPE_TABLES -->

## Benchmarks

Benchmarks are rendered separately because one benchmark may combine multiple public datasets. A benchmark record links to its companion dataset payload and constituent dataset records without duplicating their provenance or license metadata.

<!-- BEGIN GENERATED:BENCHMARK_SUMMARY -->
1 included benchmark, maintained separately from its companion and source datasets.
<!-- END GENERATED:BENCHMARK_SUMMARY -->

<!-- BEGIN GENERATED:BENCHMARK_TABLE -->
| Benchmark | Year | Domain | Capability | Scale | Source datasets | Protocol | Links | License / access |
| --- | ---: | --- | --- | --- | --- | --- | --- | --- |
| [LMOD+](https://kfzyqin.github.io/lmod_plus/) | 2026 | ophthalmology | recognition, diagnosis, localization | 32.6K instances | Cataract-1K, IDRiD, OIMHS, REFUGE2, Harvard FairSeg, CAU001, Cataract Detection 2, ORIGA, G1020, BRSET | zero-shot | [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://kfzyqin.github.io/lmod_plus/) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://doi.org/10.1145/3801746) [![Leaderboard](https://img.shields.io/badge/Leaderboard-2E7D32?style=flat-square&logo=bar-chart&logoColor=white)](https://kfzyqin.github.io/lmod_plus/) | Unknown (access unknown; mixed sources) |
<!-- END GENERATED:BENCHMARK_TABLE -->

## Capability Coverage

<!-- BEGIN GENERATED:CAPABILITY_TABLE -->
| Capability | Datasets |
| --- | ---: |
| description | 10 |
| diagnosis | 18 |
| localization | 7 |
| reasoning | 6 |
| recognition | 17 |
| report-generation | 3 |
| segmentation | 7 |
| spatial-reasoning | 1 |
<!-- END GENERATED:CAPABILITY_TABLE -->

## Caveats

Dataset metadata records describe sources, not legal advice. `unknown` and `unclear` mean the contributor could not establish an answer from an official source. Credentialed resources may require a data-use agreement or training before download. See [DATASET_SCHEMA.md](DATASET_SCHEMA.md) for field definitions and [reports/gaps.md](reports/gaps.md) for coverage gaps.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) and follow the [record workflow](WORKFLOW.md). Add one JSON-compatible YAML record per dataset or benchmark, run validation, and commit the regenerated final report.
