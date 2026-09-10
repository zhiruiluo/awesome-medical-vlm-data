<div align="center">

# Awesome Medical VLM Dataset & Benchmark

### A data intelligence layer for medical multimodal datasets and benchmarks.

</div>

<p align="center">
 <a href="https://awesome.re" alt="Awesome"><img src="https://awesome.re/badge.svg"/>
 </a>
 <a href="https://www.linkedin.com/in/luobill2017/" alt="LinkedIn"><img src="https://img.shields.io/badge/LinkedIn-Connect-blue">
 </a>
</p>

---

<!-- BEGIN GENERATED:LAST_UPDATED -->
**Last updated:** 2026-09-10
<!-- END GENERATED:LAST_UPDATED -->

A maintained, machine-readable catalog of medical AI datasets and benchmarks for training and evaluation. Datasets describe released data; benchmarks separately describe evaluation protocols, metrics, and their constituent datasets.

Resources are organized by the data they release:

- **Text Only:** clinical and biomedical language resources.
- **Image Only:** medical images with labels, bounding boxes, masks, or other visual annotations.
- **Text-Image Pairs:** reports, captions, question-answer pairs, grounded text, and other image-language supervision.

Each dataset is a version-controlled record in `datasets/records/`, not just a link. Records capture clinical domains and modalities, release year and scale, tasks and capabilities, annotation provenance and expert review, spatial grounding, quality signals, and access or license restrictions. `included`, `candidate`, and `excluded` statuses make the catalog's publication decisions auditable.

Table guide: **Data profile** is ordered as modality · anatomy · image structure. **Annotations** describes the released annotation artifact linked to each image or study. License/access cells also state commercial-use status and whether a data-use agreement is required.


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
47 included datasets: 3 text-only, 26 image-only, and 18 text-image pairs. 48 candidate and 1 excluded dataset records are retained for auditability. 4 included benchmarks; 0 candidate and 0 excluded benchmark records are omitted from public tables.
<!-- END GENERATED:CATALOG_SUMMARY -->

## Catalog Navigation

<!-- BEGIN GENERATED:RESOURCE_TYPE_NAV -->
[Text Only](#text-only) | [Image Only](#image-only) | [Text-Image Pairs](#text-image-pairs) | [Longitudinal Resources](#longitudinal-resources) | [Benchmarks](#benchmarks)
<!-- END GENERATED:RESOURCE_TYPE_NAV -->

## Datasets By Resource Type

<!-- BEGIN GENERATED:RESOURCE_TYPE_TABLES -->
### Text Only

#### Radiology

| Dataset | Data profile | Tasks | Scale | Annotations | Links | License / access |
| --- | --- | --- | ---: | --- | --- | --- |
| [MIMIC-IV-Note](https://physionet.org/content/mimic-iv-note/2.2/) | multi-anatomy | clinical-prediction, multi-label-classification | 2.7M notes | clinical-note, radiology-report | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/MIT-LCP/mimic-code) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://physionet.org/content/mimic-iv-note/2.2/) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://doi.org/10.13026/1n74-ne17) | PhysioNet Credentialed Health Data License 1.5.0 (credentialed; DUA; commercial: no) |

#### General Biomedical

| Dataset | Data profile | Tasks | Scale | Annotations | Links | License / access |
| --- | --- | --- | ---: | --- | --- | --- |
| [eICU Collaborative Research Database](https://physionet.org/content/eicu-crd/2.0/) | multi-anatomy | clinical-prediction, multi-label-classification | 200.0K icu-admissions | clinical-events, diagnosis-codes | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/MIT-LCP/eicu-code) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://physionet.org/content/eicu-crd/2.0/) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://doi.org/10.1038/sdata.2018.178) | PhysioNet Credentialed Health Data License 1.5.0 (credentialed; DUA; commercial: no) |
| [MIMIC-IV-Note](https://physionet.org/content/mimic-iv-note/2.2/) | multi-anatomy | clinical-prediction, multi-label-classification | 2.7M notes | clinical-note, radiology-report | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/MIT-LCP/mimic-code) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://physionet.org/content/mimic-iv-note/2.2/) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://doi.org/10.13026/1n74-ne17) | PhysioNet Credentialed Health Data License 1.5.0 (credentialed; DUA; commercial: no) |
| [MIMIC-IV](https://physionet.org/content/mimiciv/3.1/) | multi-anatomy | clinical-prediction, multi-label-classification | 364.6K patients | clinical-events, diagnosis-codes | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/MIT-LCP/mimic-code) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://physionet.org/content/mimiciv/3.1/) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://doi.org/10.1038/s41597-022-01899-x) | PhysioNet Credentialed Health Data License 1.5.0 (credentialed; DUA; commercial: no) |

### Image Only

#### Radiology

| Dataset | Data profile | Tasks | Scale | Annotations | Links | License / access |
| --- | --- | --- | ---: | --- | --- | --- |
| [LUNA16](https://luna16.grand-challenge.org/) | ct · lung · 3d-volume | nodule-detection, false-positive-reduction | 888 studies | coordinates, diameter | [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://luna16.grand-challenge.org/Download/) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://doi.org/10.1016/j.media.2017.06.015) | CC BY 4.0 (open; commercial: yes) |
| [Automated Cardiac Diagnosis Challenge](https://www.creatis.insa-lyon.fr/Challenge/acdc/) | mri · heart · 3d-volume | image-segmentation, multi-label-classification | 150 cardiac MRI patients | segmentation-mask, patient-label | [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://www.creatis.insa-lyon.fr/Challenge/acdc/) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://doi.org/10.1109/TMI.2018.2837502) | ACDC challenge terms (registration; commercial: unknown) |
| [ChestX-ray14](https://nihcc.app.box.com/v/ChestXray-NIHCC) | chest-xray · chest · 2d-single | multi-label-classification | 112.1K images | image-label | [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://nihcc.app.box.com/v/ChestXray-NIHCC) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://arxiv.org/abs/1705.02315) | NIH source terms; check source (open; commercial: unknown) |
| [MM-WHS](https://zmiclab.github.io/zxh/0/mmwhs/) | ct, mri · heart · 3d-volume | image-segmentation | 120 cardiac volumes | segmentation-mask | [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://zmiclab.github.io/zxh/0/mmwhs/) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://doi.org/10.1016/j.media.2019.101537) | MM-WHS data-use agreement (registration; DUA; commercial: unknown) |
| [RSNA Pneumonia Detection Challenge](https://www.rsna.org/education/ai-resources-and-training/%20%5C%20ai-image-challenge/RSNA-Pneumonia-Detection-Challenge-2018) | chest-xray · chest · 2d-single | object-detection, multi-label-classification | 30.0K examinations | bounding-box, image-label | [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://www.kaggle.com/competitions/rsna-pneumonia-detection-challenge) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://doi.org/10.1148/ryai.2019180041) | RSNA attribution terms (registration; DUA; commercial: yes) |
| [SIIM-ACR Pneumothorax Segmentation](https://www.kaggle.com/competitions/siim-acr-pneumothorax-segmentation) | chest-xray · chest · 2d-single | image-segmentation, multi-label-classification | 12.0K images | segmentation-mask, image-label | [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://www.kaggle.com/competitions/siim-acr-pneumothorax-segmentation) | Kaggle competition terms (registration; DUA; commercial: yes) |
| [ASOCA](https://asoca.grand-challenge.org/) | ct, angiography · heart · 3d-volume | image-segmentation | 60 CCTA studies | segmentation-mask, patient-label | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Ramtingh/ASOCADataDescription) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://asoca.grand-challenge.org/access/) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://doi.org/10.1016/j.compbiomed.2022.105718) | ASOCA data access terms (registration; DUA; commercial: yes) |
| [ChestX-Det10](https://github.com/Deepwise-AILab/ChestX-Det10-Dataset) | chest-xray · chest · 2d-single | object-detection | 3.5K images | bounding-box | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Deepwise-AILab/ChestX-Det10-Dataset) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://arxiv.org/abs/2006.10550) | Unknown (access unknown; commercial: unknown) |
| [COVID-19-AR](https://wiki.cancerimagingarchive.net/pages/viewpage.action?pageId=70226443) | chest-xray, ct · chest · 2d-single, 3d-volume | multi-label-classification | 105 patients | image-label | [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://www.cancerimagingarchive.net/collection/covid-19-ar/) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://doi.org/10.7937/tcia.2020.py71-5978) | TCIA collection terms; check source (open; commercial: unknown) |
| [M&Ms Cardiac Segmentation Challenge](https://www.ub.edu/mnms/) | mri · heart · 3d-volume | image-segmentation | 375 cardiac MRI examinations | segmentation-mask, patient-label | [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://www.ub.edu/mnms/) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://doi.org/10.1109/TMI.2021.3090082) | M&Ms Challenge Data Use Agreement (registration; DUA; commercial: no) |
| [VinDr-CXR](https://github.com/vinbigdata-medical/vindr-cxr) | chest-xray · chest · 2d-single | multi-label-classification, object-detection | 18.0K images | image-label, bounding-box | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/vinbigdata-medical/vindr-cxr) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://physionet.org/content/vindr-cxr/1.0.0/) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://arxiv.org/abs/2012.15029) | PhysioNet Credentialed Health Data License 1.5.0 (credentialed; DUA; commercial: no) |
| [CheXlocalize](https://github.com/rajpurkarlab/cheXlocalize) | chest-xray · chest · 2d-single | image-segmentation, object-detection | 902 images | segmentation-mask, point | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/rajpurkarlab/cheXlocalize) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://aimi.stanford.edu/datasets/chexlocalize) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://doi.org/10.1038/s42256-022-00536-x) | MIT license (registration; commercial: yes) |
| [PI-CAI](https://pi-cai.grand-challenge.org/DATA/) | mri · prostate · 3d-volume | multi-label-classification, object-detection, image-segmentation | 1.5K biparametric MRI examinations | segmentation-mask, patient-label, clinical-label | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/DIAGNijmegen/picai_labels) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://zenodo.org/record/6624726) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://doi.org/10.1016/S1470-2045(24)00220-1) | CC BY-NC 4.0 (open; commercial: no) |

#### Pathology

| Dataset | Data profile | Tasks | Scale | Annotations | Links | License / access |
| --- | --- | --- | ---: | --- | --- | --- |
| [CAMELYON17](https://camelyon17.grand-challenge.org/Data/) | whole-slide-image · lymph-node · whole-slide-image | multi-label-classification, image-segmentation | 1.0K whole-slide-images | clinical-label, segmentation-mask | [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://camelyon17.grand-challenge.org/Download/) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://doi.org/10.1109/TMI.2018.2867350) | CC BY-NC-ND 4.0 (open; commercial: no) |
| [PAIP 2019 Liver Cancer Segmentation](https://paip2019.grand-challenge.org/Dataset/) | whole-slide-image · liver · whole-slide-image | image-segmentation | 100 whole-slide-images | segmentation-mask, scalar | [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://paip2019.grand-challenge.org/) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://doi.org/10.1016/j.media.2020.101854) | Research-use data-use and confidentiality agreement (registration; DUA; commercial: unknown) |
| [BRACS](https://www.bracs.icar.cnr.it/) | whole-slide-image · breast · whole-slide-image | multi-label-classification | 547 whole-slide-images | clinical-label, region-of-interest | [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://www.bracs.icar.cnr.it/) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://doi.org/10.1093/database/baac093) | CC0 1.0 (registration; DUA; commercial: yes) |
| [PANDA](https://panda.grand-challenge.org/data/) | whole-slide-image · prostate · whole-slide-image | multi-label-classification, image-segmentation | 10.6K whole-slide-images | clinical-label, segmentation-mask | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/DIAGNijmegen/panda-challenge) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://www.kaggle.com/c/prostate-cancer-grade-assessment/data) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://doi.org/10.1038/s41591-021-01620-2) | CC BY-NC-SA 4.0 (registration; commercial: no) |

#### Ophthalmology

| Dataset | Data profile | Tasks | Scale | Annotations | Links | License / access |
| --- | --- | --- | ---: | --- | --- | --- |
| [CHASE_DB1](https://researchinnovation.kingston.ac.uk/en/datasets/chasedb1-retinal-vessel-reference-dataset-4/) | fundus · eye · 2d-single | image-segmentation | 28 images | segmentation-mask | [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://researchinnovation.kingston.ac.uk/en/datasets/chasedb1-retinal-vessel-reference-dataset-4/) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://doi.org/10.1109/TBME.2012.2205687) | CC BY 4.0 (access unknown; commercial: yes) |
| [ACPS](https://people.duke.edu/~sf59/Chiu_BOE_2013_dataset.htm) | oct · eye · 2d-single | image-segmentation | 840 images | segmentation-mask | [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://people.duke.edu/~sf59/Chiu_BOE_2013_dataset.htm) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://doi.org/10.1364/BOE.4.000924) | Unknown (access unknown; commercial: unknown) |
| [ROSE](https://imed.nimte.ac.cn/dataofrose.html) | oct · eye · 2d-single | image-segmentation | 229 images | segmentation-mask | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/iMED-Lab/ROSE) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://imed.nimte.ac.cn/dataofrose.html) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://doi.org/10.1109/TMI.2020.3042802) | Academic research use only (access unknown; commercial: no) |
| [FIVES](https://figshare.com/articles/figure/FIVES_A_Fundus_Image_Dataset_for_AI-based_Vessel_Segmentation/19688169/1) | fundus · eye · 2d-single | image-segmentation | 800 images | segmentation-mask | [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://figshare.com/articles/figure/FIVES_A_Fundus_Image_Dataset_for_AI-based_Vessel_Segmentation/19688169/1) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://doi.org/10.1038/s41597-022-01564-3) | CC BY 4.0 (access unknown; commercial: yes) |
| [OLIVES](https://github.com/olivesgatech/OLIVES_Dataset) | fundus, oct · eye · 2d-single, 3d-volume, longitudinal-sequence | multi-label-classification | 1.3K fundus-image visits | image-label, clinical-label | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/olivesgatech/OLIVES_Dataset) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://doi.org/10.5281/zenodo.7105232) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://arxiv.org/abs/2209.11195) | MIT (open; commercial: yes) |
| [Harvard Glaucoma Detection and Progression](https://github.com/Harvard-Ophthalmology-AI-Lab/Harvard-GDP) | oct · eye · 2d-single | multi-label-classification | 1.0K patients | image-label, clinical-label | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Harvard-Ophthalmology-AI-Lab/Harvard-GDP) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://huggingface.co/datasets/harvardairobotics/Harvard-GDP) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://arxiv.org/abs/2308.13411) | CC BY-NC-ND 4.0 (open; commercial: no) |
| [Cataract-1K](https://github.com/Negin-Ghamsarian/Cataract-1K) | surgical-video · eye · video | image-segmentation | 1.0K videos | segmentation-mask | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Negin-Ghamsarian/Cataract-1K) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://github.com/Negin-Ghamsarian/Cataract-1K) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://arxiv.org/abs/2312.06295) | CC BY 4.0 (access unknown; commercial: yes) |

#### Ultrasound

| Dataset | Data profile | Tasks | Scale | Annotations | Links | License / access |
| --- | --- | --- | ---: | --- | --- | --- |
| [CAMUS](https://www.creatis.insa-lyon.fr/Challenge/camus/onlinePlatform.html) | ultrasound · heart · multi-view, video | image-segmentation | 500 patients | segmentation-mask, scalar | [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://www.creatis.insa-lyon.fr/Challenge/camus/onlinePlatform.html) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://arxiv.org/abs/1908.06948) | CAMUS challenge terms (registration; commercial: unknown) |
| [EchoNet-Dynamic](https://echonet.github.io/dynamic/) | ultrasound · heart · video | image-segmentation, multi-label-classification | 10.0K echocardiography videos | segmentation-mask, scalar, image-label | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/echonet/dynamic) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://echonet.github.io/dynamic/) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://doi.org/10.1038/s41586-020-2145-8) | Stanford EchoNet-Dynamic Research Use Agreement (registration; DUA; commercial: no) |

#### Surgery

| Dataset | Data profile | Tasks | Scale | Annotations | Links | License / access |
| --- | --- | --- | ---: | --- | --- | --- |
| [Cataract-1K](https://github.com/Negin-Ghamsarian/Cataract-1K) | surgical-video · eye · video | image-segmentation | 1.0K videos | segmentation-mask | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Negin-Ghamsarian/Cataract-1K) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://github.com/Negin-Ghamsarian/Cataract-1K) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://arxiv.org/abs/2312.06295) | CC BY 4.0 (access unknown; commercial: yes) |

### Text-Image Pairs

#### Radiology

| Dataset | Data profile | Tasks | Scale | Annotations | Links | License / access |
| --- | --- | --- | ---: | --- | --- | --- |
| [IU X-Ray](https://openi.nlm.nih.gov/) | chest-xray · chest · multi-view | report-generation, image-report-retrieval | 4.0K reports | report | [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://www.kaggle.com/datasets/raddar/chest-xrays-indiana-university) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://pubmed.ncbi.nlm.nih.gov/27701286/) | CC BY-NC-ND 4.0 (open; commercial: no) |
| [VQA-RAD](https://www.nlm.nih.gov/research/visible/vqarad/index.html) | xray, ct, mri · multi-anatomy · 2d-single | visual-question-answering | 3.5K qa-pairs | image | [![Hugging Face](https://img.shields.io/badge/Hugging%20Face-FF6C37?style=flat-square&logo=huggingface&logoColor=white)](https://huggingface.co/datasets/flaviagiammarino/vqa-rad) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://huggingface.co/datasets/flaviagiammarino/vqa-rad) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://doi.org/10.1038/sdata.2018.251) | Research use; check source terms (open; commercial: unknown) |
| [MIMIC-CXR](https://physionet.org/content/mimic-cxr/2.1.0/) | chest-xray · chest · multi-view | report-generation, image-report-retrieval | 227.8K studies | report | [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://www.kaggle.com/datasets/simhadrisadaram/mimic-cxr-dataset) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://doi.org/10.1038/s41597-019-0322-0) | PhysioNet Credentialed Health Data License 1.5.0 (credentialed; DUA; commercial: no) |
| [Medical-Diff-VQA](https://physionet.org/content/medical-diff-vqa/1.0.1/) | chest-xray · chest · longitudinal-sequence | visual-question-answering | 700.7K question-answer-pairs | question-answer, report | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Holipori/MIMIC-Diff-VQA) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://physionet.org/content/medical-diff-vqa/1.0.1/) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://arxiv.org/abs/2406.06347) | PhysioNet Credentialed Health Data License 1.5.0 (credentialed; DUA; commercial: no) |
| [ROCOv2](https://zenodo.org/records/10821435) | angiography, ct, mri, pet, ultrasound, xray · multi-anatomy · 2d-single | image-captioning, image-text-retrieval, multi-label-classification | 79.8K image-caption-pairs | caption, medical-concepts | [![Hugging Face](https://img.shields.io/badge/Hugging%20Face-FF6C37?style=flat-square&logo=huggingface&logoColor=white)](https://huggingface.co/datasets/eltorio/ROCOv2-radiology) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://zenodo.org/records/10821435) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://arxiv.org/abs/2405.10004) | CC BY-NC 4.0 (registration; DUA; commercial: no) |
| [RP3D-Caption](https://chaoyi-wu.github.io/RadFM/) | ct, mri, ultrasound, xray · multi-anatomy · 3d-volume | image-captioning, image-text-retrieval | 69.5K image-text-pairs | caption, case-context | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/chaoyi-wu/RadFM) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://huggingface.co/datasets/chaoyi-wu/RadFM_data_csv) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://arxiv.org/abs/2308.02463) | Radiopaedia non-commercial use with approval (gated; DUA; commercial: no) |
| [CheXpert Plus](https://aimi.stanford.edu/datasets/chexpert-plus) | chest-xray · chest · multi-view, longitudinal-sequence | report-generation, image-report-retrieval, multi-label-classification | 187.7K studies | report, image-label | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Stanford-AIMI/chexpert-plus) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://stanford.redivis.com/datasets/5yyj-1a9f6ap0x?v=next) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://arxiv.org/abs/2405.19538) | Stanford CheXpert Plus Data Use Agreement (registration; DUA; commercial: no) |
| [CT-RATE](https://stanfordmlgroup.github.io/projects/ct-rate/) | ct · chest · 3d-volume | report-generation, multi-label-classification | 25.7K studies | report | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ibrahimethemhamci/CT-RATE) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://huggingface.co/datasets/ibrahimhamamci/CT-RATE) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://arxiv.org/abs/2403.17834) | CC BY-NC-SA 4.0 (registration; commercial: no) |

#### Pathology

| Dataset | Data profile | Tasks | Scale | Annotations | Links | License / access |
| --- | --- | --- | ---: | --- | --- | --- |
| [PathVQA](https://huggingface.co/datasets/flaviagiammarino/path-vqa) | pathology-image · multi-anatomy · 2d-single | visual-question-answering | 32.8K qa-pairs | image, caption | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/UCSD-AI4H/PathVQA) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://huggingface.co/datasets/flaviagiammarino/path-vqa) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://arxiv.org/abs/2003.10286) | MIT (open; commercial: yes) |
| [Quilt-1M](https://quilt1m.github.io/) | pathology-image · multi-anatomy · 2d-single | image-captioning, image-text-retrieval | 1.0M image-text-pairs | caption | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/wisdomikezogwo/quilt1m) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://zenodo.org/records/8239942) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://arxiv.org/abs/2306.11207) | Research use agreement; restricted access (registration; DUA; commercial: no) |

#### Ophthalmology

| Dataset | Data profile | Tasks | Scale | Annotations | Links | License / access |
| --- | --- | --- | ---: | --- | --- | --- |
| [FairVLMed](https://github.com/Harvard-Ophthalmology-AI-Lab/FairCLIP) | fundus · eye · 2d-single | visual-question-answering, image-captioning | 10.0K images | report | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Harvard-Ophthalmology-AI-Lab/FairCLIP) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://arxiv.org/abs/2403.14774) | CC BY-NC-ND 4.0 (registration; commercial: no) |

#### Endoscopy

| Dataset | Data profile | Tasks | Scale | Annotations | Links | License / access |
| --- | --- | --- | ---: | --- | --- | --- |
| [EndoBench](https://github.com/CUHK-AIM-Group/EndoBench) | endoscopy-image · gastrointestinal · 2d-single | visual-question-answering | 6.8K question-answer-pairs | question-answer | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/CUHK-AIM-Group/EndoBench) | Apache-2.0 (access unknown; commercial: yes) |

#### Dermatology

| Dataset | Data profile | Tasks | Scale | Annotations | Links | License / access |
| --- | --- | --- | ---: | --- | --- | --- |
| [Derm1M](https://github.com/SiyuanYan1/Derm1M) | dermoscopy, pathology-image · skin · 2d-single | image-captioning, image-text-retrieval | 1.0M image-text-pairs | image-caption | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/SiyuanYan1/Derm1M) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://huggingface.co/datasets/redlessone/Derm1M) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://arxiv.org/abs/2503.14911) | CC BY-NC-4.0 (access unknown; commercial: no) |

#### Ultrasound

| Dataset | Data profile | Tasks | Scale | Annotations | Links | License / access |
| --- | --- | --- | ---: | --- | --- | --- |
| [MIMIC-IV-ECHO](https://physionet.org/content/mimic-iv-echo/1.0/) | ultrasound · heart · multi-view, video | clinical-prediction, multi-label-classification | 7.2K transthoracic echocardiogram studies with DICOMs | clinical-events, scalar, image | [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://physionet.org/content/mimic-iv-echo/1.0/) | PhysioNet Credentialed Health Data License 1.5.0 (credentialed; DUA; commercial: no) |

#### General Biomedical

| Dataset | Data profile | Tasks | Scale | Annotations | Links | License / access |
| --- | --- | --- | ---: | --- | --- | --- |
| [ImageCLEF VQA-Med 2019](https://github.com/abachaa/VQA-Med-2019) | mixed-medical-figures · multi-anatomy · 2d-single | visual-question-answering | 15.3K questions | image | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/abachaa/VQA-Med-2019) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://github.com/abachaa/VQA-Med-2019) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://ceur-ws.org/Vol-2380/paper_275.pdf) | ImageCLEF terms; image copyrights vary (open; commercial: unknown) |
| [MedICaT](https://github.com/allenai/medicat) | mixed-medical-figures · multi-anatomy · 2d-single | image-captioning, image-text-retrieval, grounded-captioning | 217.1K figures | caption, subfigure, article-context | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/allenai/medicat) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://ai2-s2-medicat.s3.us-west-2.amazonaws.com/2020-10-05/medicat_release.tar.gz) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://arxiv.org/abs/2010.06000) | Per-document open-access license; research use only (open; commercial: no) |
| [SLAKE](https://www.med-vqa.com/slake/) | xray, ct, mri · multi-anatomy · 2d-single | visual-question-answering, knowledge-based-visual-question-answering | 14.0K qa-pairs | image, knowledge-graph | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/haifangong/SLAKE) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://www.med-vqa.com/slake/) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://arxiv.org/abs/2102.09542) | Research use; check source terms (open; commercial: unknown) |
| [PMC-VQA](https://xiaoman-zhang.github.io/PMC-VQA/) | mixed-medical-figures · multi-anatomy · 2d-single | visual-question-answering | 227.0K qa-pairs | figure, caption, article-context | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/xiaoman-zhang/PMC-VQA) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://huggingface.co/datasets/xmcmic/PMC-VQA) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://arxiv.org/abs/2305.10415) | Check source terms (open; commercial: unknown) |
| [MIMIC-IV-ECHO](https://physionet.org/content/mimic-iv-echo/1.0/) | ultrasound · heart · multi-view, video | clinical-prediction, multi-label-classification | 7.2K transthoracic echocardiogram studies with DICOMs | clinical-events, scalar, image | [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://physionet.org/content/mimic-iv-echo/1.0/) | PhysioNet Credentialed Health Data License 1.5.0 (credentialed; DUA; commercial: no) |
<!-- END GENERATED:RESOURCE_TYPE_TABLES -->

## Longitudinal Resources

This cross-cutting view includes datasets with an explicit longitudinal sequence or longitudinal-comparison support. Resources remain listed under their primary type above.

<!-- BEGIN GENERATED:LONGITUDINAL_SUMMARY -->
6 included datasets with explicit longitudinal sequences or longitudinal-comparison support. These records also remain listed under their primary resource type.
<!-- END GENERATED:LONGITUDINAL_SUMMARY -->

<!-- BEGIN GENERATED:LONGITUDINAL_TABLE -->
#### Radiology

| Dataset | Data profile | Tasks | Scale | Annotations | Links | License / access |
| --- | --- | --- | ---: | --- | --- | --- |
| [Medical-Diff-VQA](https://physionet.org/content/medical-diff-vqa/1.0.1/) | chest-xray · chest · longitudinal-sequence | visual-question-answering | 700.7K question-answer-pairs | question-answer, report | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Holipori/MIMIC-Diff-VQA) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://physionet.org/content/medical-diff-vqa/1.0.1/) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://arxiv.org/abs/2406.06347) | PhysioNet Credentialed Health Data License 1.5.0 (credentialed; DUA; commercial: no) |
| [CheXpert Plus](https://aimi.stanford.edu/datasets/chexpert-plus) | chest-xray · chest · multi-view, longitudinal-sequence | report-generation, image-report-retrieval, multi-label-classification | 187.7K studies | report, image-label | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Stanford-AIMI/chexpert-plus) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://stanford.redivis.com/datasets/5yyj-1a9f6ap0x?v=next) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://arxiv.org/abs/2405.19538) | Stanford CheXpert Plus Data Use Agreement (registration; DUA; commercial: no) |

#### Ophthalmology

| Dataset | Data profile | Tasks | Scale | Annotations | Links | License / access |
| --- | --- | --- | ---: | --- | --- | --- |
| [OLIVES](https://github.com/olivesgatech/OLIVES_Dataset) | fundus, oct · eye · 2d-single, 3d-volume, longitudinal-sequence | multi-label-classification | 1.3K fundus-image visits | image-label, clinical-label | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/olivesgatech/OLIVES_Dataset) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://doi.org/10.5281/zenodo.7105232) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://arxiv.org/abs/2209.11195) | MIT (open; commercial: yes) |
| [Harvard Glaucoma Detection and Progression](https://github.com/Harvard-Ophthalmology-AI-Lab/Harvard-GDP) | oct · eye · 2d-single | multi-label-classification | 1.0K patients | image-label, clinical-label | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Harvard-Ophthalmology-AI-Lab/Harvard-GDP) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://huggingface.co/datasets/harvardairobotics/Harvard-GDP) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://arxiv.org/abs/2308.13411) | CC BY-NC-ND 4.0 (open; commercial: no) |

#### General Biomedical

| Dataset | Data profile | Tasks | Scale | Annotations | Links | License / access |
| --- | --- | --- | ---: | --- | --- | --- |
| [eICU Collaborative Research Database](https://physionet.org/content/eicu-crd/2.0/) | multi-anatomy | clinical-prediction, multi-label-classification | 200.0K icu-admissions | clinical-events, diagnosis-codes | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/MIT-LCP/eicu-code) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://physionet.org/content/eicu-crd/2.0/) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://doi.org/10.1038/sdata.2018.178) | PhysioNet Credentialed Health Data License 1.5.0 (credentialed; DUA; commercial: no) |
| [MIMIC-IV](https://physionet.org/content/mimiciv/3.1/) | multi-anatomy | clinical-prediction, multi-label-classification | 364.6K patients | clinical-events, diagnosis-codes | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/MIT-LCP/mimic-code) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://physionet.org/content/mimiciv/3.1/) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://doi.org/10.1038/s41597-022-01899-x) | PhysioNet Credentialed Health Data License 1.5.0 (credentialed; DUA; commercial: no) |
<!-- END GENERATED:LONGITUDINAL_TABLE -->

## Benchmarks

Benchmarks are rendered separately because one benchmark may combine multiple public datasets. A benchmark record links to its companion dataset payload and constituent dataset records without duplicating their provenance or license metadata.

<!-- BEGIN GENERATED:BENCHMARK_SUMMARY -->
4 included benchmarks, maintained separately from their companion and source datasets.
<!-- END GENERATED:BENCHMARK_SUMMARY -->

<!-- BEGIN GENERATED:BENCHMARK_TABLE -->
| Benchmark | Year | Scope | Tasks | Scale | Source datasets | Protocol | Links | License / access |
| --- | ---: | --- | --- | --- | --- | --- | --- | --- |
| [MS-CXR-T](https://physionet.org/content/ms-cxr-t/1.0.0/) | 2023 | radiology · chest-xray | multi-label-classification | 1.7K annotations | MIMIC-CXR | zero-shot, linear-probe | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/hi-ml-multimodal) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://physionet.org/content/ms-cxr-t/1.0.0/) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://arxiv.org/abs/2301.04558) | PhysioNet Credentialed Health Data License 1.5.0 (credentialed; DUA; commercial: no); inherited sources |
| [TemMed-Bench](https://temmedbench.github.io/) | 2025 | radiology · chest-xray | visual-question-answering, report-generation | 21.0K instances | CheXpert Plus | closed-book, retrieval-augmented generation | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Levi-ZJY/TemMed-Bench) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://huggingface.co/datasets/uclanlp/TemMed-Bench) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://arxiv.org/abs/2509.25143) | CC BY 4.0 (open; commercial: yes); mixed sources |
| [LMOD+](https://kfzyqin.github.io/lmod_plus/) | 2026 | ophthalmology · fundus, oct, slo, lens-photography, surgical-video | visual-question-answering, multi-label-classification, object-detection, image-segmentation | 32.6K instances | Cataract-1K, IDRiD, OIMHS, REFUGE2, Harvard FairSeg, CAU001, Cataract Detection 2, ORIGA, G1020, BRSET | zero-shot | [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://kfzyqin.github.io/lmod_plus/) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://doi.org/10.1145/3801746) [![Leaderboard](https://img.shields.io/badge/Leaderboard-2E7D32?style=flat-square&logo=bar-chart&logoColor=white)](https://kfzyqin.github.io/lmod_plus/) | Unknown (access unknown; commercial: unknown); mixed sources |
| [LUNGUAGE](https://physionet.org/content/lunguage/1.0.0/) | 2026 | radiology · chest-xray | report-generation | 1.5K expert-annotated reports | MIMIC-CXR | structured-report evaluation, patient-level temporal evaluation | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/SuperSupermoon/Lunguage) [![Download](https://img.shields.io/badge/Download-0969DA?style=flat-square&logo=download&logoColor=white)](https://physionet.org/content/lunguage/1.0.0/) [![Paper](https://img.shields.io/badge/Paper-000000?style=flat-square&logo=paper&logoColor=white)](https://arxiv.org/abs/2505.21190) | PhysioNet Credentialed Health Data License 1.5.0 (credentialed; DUA; commercial: no); inherited sources |
<!-- END GENERATED:BENCHMARK_TABLE -->

## Capability Coverage

<!-- BEGIN GENERATED:CAPABILITY_TABLE -->
| Capability | Datasets |
| --- | ---: |
| clinical-prediction | 4 |
| description | 12 |
| diagnosis | 35 |
| localization | 12 |
| longitudinal-comparison | 6 |
| measurement | 5 |
| reasoning | 8 |
| recognition | 21 |
| report-generation | 4 |
| segmentation | 17 |
| spatial-reasoning | 1 |
<!-- END GENERATED:CAPABILITY_TABLE -->

## Caveats

Dataset metadata records describe sources, not legal advice. `unknown` and `unclear` mean the contributor could not establish an answer from an official source. Credentialed resources may require a data-use agreement or training before download. See [DATASET_SCHEMA.md](DATASET_SCHEMA.md) for field definitions and [reports/gaps.md](reports/gaps.md) for coverage gaps.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) and follow the [record workflow](WORKFLOW.md). Add one JSON-compatible YAML record per dataset or benchmark, run validation, and commit the regenerated final report.
