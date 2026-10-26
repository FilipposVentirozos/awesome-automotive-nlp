# 📊 Tabular + text

Part of [awesome-automotive-nlp](../README.md). Same taxonomy as the main list: see [Taxonomy](../README.md#️-taxonomy).

**15 corpora** in 3 languages.

**Languages:** English 13 · Chinese 2 · French 1

## 📑 Contents

- [Corpora by application area](#corpora-by-application-area)
  - [🏷️ B. Listings, adverts & claims](#️-b-listings-adverts--claims) (1)
  - [⭐ D. Reviews, opinion & sentiment](#-d-reviews-opinion--sentiment) (2)
  - [⚠️ E. Complaints, safety, recalls & incidents](#️-e-complaints-safety-recalls--incidents) (10)
  - [🔧 G. Faults, diagnostics & repair](#-g-faults-diagnostics--repair) (1)
  - [🛣️ J. Driving-scene language & multimodal](#️-j-driving-scene-language--multimodal) (1)

## Corpora by application area

### 🏷️ B. Listings, adverts & claims

#### Listings and adverts

| Corpus | Task | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|
| Craigslist Used Cars | listings | English | \~426k rows | CC0: Public Domain | open | 2021 | [data](https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data) | — |

### ⭐ D. Reviews, opinion & sentiment

#### Consumer and expert reviews

| Corpus | Task | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|
| Expert Car Reviews Dataset (Kaggle) | summarisation | English | not stated | Other | open | 2024 | [data](https://www.kaggle.com/datasets/ademboukhris/expert-car-reviews-dataset) | — |
| SRNI-CAR (Chinese automotive market dataset) - owner reviews component | sentiment | Chinese | 217,292 comments | CC BY-NC 4.0 | open | 2023 | [data](https://srni-car.github.io) · [paper](https://arxiv.org/abs/2401.05395) | — |

### ⚠️ E. Complaints, safety, recalls & incidents

#### NHTSA defects, recalls and investigations (US)

| Corpus | Task | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|
| NHTSA Customer Complaints (Kaggle) | complaint text | English | not stated | CC0: Public Domain | open | 2026 | [data](https://www.kaggle.com/datasets/alshival/nhtsa-complaints) | — |
| NHTSA Defect Investigations (flat file) | investigation text | English | not stated | unknown | open | 1972 | [data](https://static.nhtsa.gov/odi/ffdd/inv/INV.txt) | — |
| NHTSA Manufacturer Communications / Technical Service Bulletins (flat file) | service bulletins | English | not stated | unknown | open | 1995 | [data](https://static.nhtsa.gov/odi/ffdd/tsbs/TSBS.txt) | — |
| NHTSA ODI Complaints (flat file) | complaint text | English | 2.2M complaints | unknown | open | 1995 | [data](https://static.nhtsa.gov/odi/ffdd/cmpl/CMPL.txt) | — |
| NHTSA ODI complaints - high-signal subset (Hugging Face) | complaint text | English | 213,093 records | federal-works-and-cc0-card-metadata | open | — | [data](https://huggingface.co/datasets/emperor-mew/nhtsa-complaints) | — |
| NHTSA Recalls (flat file) | recall text | English | not stated | unknown | open | 1967 | [data](https://static.nhtsa.gov/odi/ffdd/rcl/RCL.txt) | — |

#### Recalls in other jurisdictions

| Corpus | Task | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|
| DVSA Vehicle Recalls File (UK) | recall text | English | \~5 MB CSV | Open Government Licence v3.0 | open | 1992 | [data](https://www.check-vehicle-recalls.service.gov.uk/) | — |
| Transport Canada Vehicle Recalls Database | recall text | English, French | not stated | Open Government Licence - Canada | open | — | [data](https://open.canada.ca/data/en/dataset/1ec92326-47ef-4110-b7ca-959fab03f96d) | — |

#### Crash and automated-driving incident narratives

| Corpus | Task | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|
| California DMV Autonomous Vehicle Disengagement Reports | incident reports | English | \~634k characters (2024) | unknown | open | 2015 | [data](https://www.dmv.ca.gov/portal/file/2024-autonomous-vehicle-disengagement-reports-csv/) | — |
| NHTSA Standing General Order 2021-01 Crash Reports (ADS and Level 2 ADAS) | crash narratives | English | not stated | unknown | open | 2021 | [data](https://static.nhtsa.gov/odi/ffdd/sgo-2021-01/SGO-2021-01_Data_Element_Definitions.pdf) | — |

### 🔧 G. Faults, diagnostics & repair

| Corpus | Task | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|
| Vehicle Fleet Fault Association Dataset | NER + KG / ontology | Chinese | not stated | CC BY 4.0 | open | 2026 | [data](https://data.mendeley.com/datasets/r98g7g6k5t/1) | — |

### 🛣️ J. Driving-scene language & multimodal

*For papers and models on language in autonomous driving, see [Awesome-LLM4AD](https://github.com/Thinklab-SJTU/Awesome-LLM4AD), which this section complements; it lists corpora only.*

#### Reasoning and planning with language

| Corpus | Task | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|
| Driving-with-LLMs | VQA | English | \~10k/1k VQA items | repo Apache-2.0 | open | 2023 | [data](https://github.com/wayveai/Driving-with-LLMs) · [paper](https://arxiv.org/abs/2310.01957) | — |

---

_Generated by `python scripts/build_readme.py` from `data/corpora.yaml`. Do not edit this page by hand._
