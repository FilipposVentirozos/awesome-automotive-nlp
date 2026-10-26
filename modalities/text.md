# 📝 Text

Part of [awesome-automotive-nlp](../README.md). Same taxonomy as the main list: see [Taxonomy](../README.md#️-taxonomy).

**55 corpora** in 7 languages.

**Languages:** English 42 · Chinese 8 · Korean 4 · German 2 · Italian 2 · Indonesian 1 · Japanese 1 · Multilingual 1 · unknown 1

## 📑 Contents

- [Corpora by application area](#corpora-by-application-area)
  - [🚗 A. Vehicle identification & specifications](#-a-vehicle-identification--specifications) (3)
  - [🏷️ B. Listings, adverts & claims](#️-b-listings-adverts--claims) (2)
  - [🧩 C. Features, attributes & catalogue linking](#-c-features-attributes--catalogue-linking) (1)
  - [⭐ D. Reviews, opinion & sentiment](#-d-reviews-opinion--sentiment) (17)
  - [⚠️ E. Complaints, safety, recalls & incidents](#️-e-complaints-safety-recalls--incidents) (1)
  - [📘 F. Owner's manuals & technical QA](#-f-owners-manuals--technical-qa) (3)
  - [🔧 G. Faults, diagnostics & repair](#-g-faults-diagnostics--repair) (5)
  - [📐 H. Engineering documents](#-h-engineering-documents) (2)
  - [🗣️ I. In-car voice assistants & dialogue](#️-i-in-car-voice-assistants--dialogue) (9)
  - [🛣️ J. Driving-scene language & multimodal](#️-j-driving-scene-language--multimodal) (1)
  - [🔎 K. Search, queries & semantic parsing](#-k-search-queries--semantic-parsing) (1)
  - [🕸️ M. Knowledge graphs, ontologies & lexicons](#️-m-knowledge-graphs-ontologies--lexicons) (10)

## Corpora by application area

### 🚗 A. Vehicle identification & specifications

#### Text: vehicle-domain NER

| Corpus | Task | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|
| AutoSpecNER | NER | English | 659 adverts | CC BY 4.0 | open | 2026 | [data](https://github.com/FilipposVentirozos/AutoSpecNER) · [paper](https://aclanthology.org/2026.icnlsp-1.8/) | — |
| EWNERTC (automotive subset) | fine-grained NER | English | 10,349 sentences | CC BY 4.0 | open | 2020 | [data](https://data.mendeley.com/datasets/cdcztymf4k/1) · [paper](https://aclanthology.org/2020.coling-main.334) | Auto-AdvER |
| FindVehicle | NER | English | 42.3k descriptions | unknown | open | 2024 | [data](https://github.com/GuanRunwei/FindVehicle) · [paper](https://doi.org/10.1007/s11042-023-16373-y) | AutoSpecNER, Auto-AdvER, Auto-Features |

### 🏷️ B. Listings, adverts & claims

#### Listings and adverts

| Corpus | Task | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|
| Auto-AdvER | span labelling | English | 605 adverts | CC BY 4.0 | open | 2026 | [data](https://github.com/FilipposVentirozos/Auto-AdvER) · [paper](https://arxiv.org/abs/2412.05655) | AutoSpecNER, Auto-Features |

#### Buyer-seller dialogue

| Corpus | Task | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|
| CraigslistBargain | dialogue | English | 6k+ dialogues | unknown | open | 2018 | [data](https://huggingface.co/datasets/stanfordnlp/craigslist_bargains) · [paper](https://aclanthology.org/D18-1256/) | — |

### 🧩 C. Features, attributes & catalogue linking

*No public automotive-specific attribute-extraction or catalogue-linking corpus was found. Auto-Features (to be released, listed below) is built for this task; the general product-attribute sets MAVE, OA-Mine and AE-110K contain no automotive category.*

| Corpus | Task | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|
| Auto-Features | NER + entity linking | English | 1,256 adverts | to be announced at release | to be released | 2026 | to be released | — |

### ⭐ D. Reviews, opinion & sentiment

#### Consumer and expert reviews

| Corpus | Task | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|
| Amazon Review Data (2018) - Automotive category | sentiment | English | 7,990,166 reviews | unknown | open | 2018 | [data](https://nijianmo.github.io/amazon/index.html) | — |
| Amazon Reviews 2023 - Automotive category | sentiment | English | 20.0M reviews | unknown | open | 2023 | [data](https://amazon-reviews-2023.github.io/) | — |
| Car Reviews (Hugging Face) | sentiment | English | 36,984 rows | unknown | open | — | [data](https://huggingface.co/datasets/florentgbelidji/car-reviews) | — |
| Edmunds Car Reviews (Kaggle) | sentiment | English | not stated | CC BY-SA 4.0 | open | 2021 | [data](https://www.kaggle.com/datasets/shreemunpranav/edmunds-car-review) | — |
| Electric Vehicles User Reviews India (Kaggle) | sentiment | English | not stated | CC0: Public Domain | open | 2022 | [data](https://www.kaggle.com/datasets/deadprstkrish/ev-cars-user-reviews-india) | — |
| OpinRank Review Dataset (Edmunds car reviews) | sentiment | English | \~42,230 car reviews | CC BY 4.0 | open | 2011 | [data](https://archive.ics.uci.edu/dataset/205/opinrank+review+dataset) | — |
| Yelp Open Dataset (Automotive category businesses) | sentiment | English | not stated | intended for educational use | open | 2013 | [data](https://business.yelp.com/data/resources/open-dataset/) | — |

#### Sentiment and aspect-based gold standards

| Corpus | Task | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|
| ALSA (Aspect-Level Sentiment Analysis in Automotive Domain) | ABSA | English, Korean | 58k+ comment-aspect pairs | research use only | on request | 2020 | [data](https://github.com/dmhyun/ALSAdata) · [paper](https://aclanthology.org/2020.coling-main.83/) | — |
| CCF BDCI 2018 Automotive User Opinion Topic and Sentiment Recognition | ABSA | Chinese | not stated | unknown | on request | 2018 | [data](https://www.datafountain.cn/competitions/310) | — |
| Chinese car review sentiment dataset (Liu et al. 2022, ATWWM-BERT) | sentiment | Chinese | 9,947 reviews | unknown | paper only | 2022 | paper only · [paper](https://arxiv.org/abs/2206.02389) | — |
| IndoNLU CASA (Indonesian car review ABSA) | ABSA | Indonesian | 1,080 reviews | MIT | open | 2018 | [data](https://huggingface.co/datasets/indonlp/indonlu) | — |
| InfoBarometer (German automotive industry explainable sentiment) | sentiment | German | 1,039 news articles | unknown | paper only | 2023 | paper only · [paper](https://aclanthology.org/2023.wassa-1.13/) | — |
| JDPA Sentiment Corpus for the Automotive Domain | ABSA | English | 515 documents | (c) Copyright 2009-2010, J.D. Power… | on request | 2010 | [data](https://verbs.colorado.edu/jdpacorpus/README.txt) | — |
| PACE Corpus (Polarity-annotated Automotive and CEllphone) | ABSA | English, German | 2,000 forum posts | unknown | paper only | 2014 | paper only · [paper](https://aclanthology.org/L14-1240/) | — |

#### Social and video media

| Corpus | Task | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|
| Automotive brand's products - Twitter dataset (Mendeley Data) | sentiment | unknown | not stated | CC BY 4.0 | open | — | [data](https://data.mendeley.com/datasets/hcc2h426h3/1) | — |
| SenTube (SenTube-A automobiles subset) | sentiment | English, Italian | 3,381/225/903 comments | unknown | paper only | 2014 | paper only · [paper](https://aclanthology.org/L14-1188/) | — |
| YouTube AV 50K | sentiment | English | 50k+ comments | unknown | paper only | 2018 | paper only · [paper](https://arxiv.org/abs/1807.11227) | — |

### ⚠️ E. Complaints, safety, recalls & incidents

#### Crash and automated-driving incident narratives

| Corpus | Task | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|
| Iowa DOT crash report narratives (as used in Bhagat et al. 2025) | crash narratives | English | 94,367 narratives | unknown | paper only | 2025 | paper only · [paper](https://arxiv.org/abs/2504.13068) | — |

### 📘 F. Owner's manuals & technical QA

| Corpus | Task | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|
| ADMit | NER | Korean, English | not stated | unknown | paper only | 2023 | paper only · [paper](https://doi.org/10.1016/j.eswa.2023.120007) | AutoSpecNER, Auto-AdvER |
| DelucionQA | QA + hallucination | English | 913 questions | CC BY 4.0 | open | 2023 | [data](https://github.com/boschresearch/DelucionQA) · [paper](https://aclanthology.org/2023.findings-emnlp.59.pdf) | — |
| MaQA | QA + classification | Korean, English | 45,641 questions | unknown | paper only | 2024 | paper only · [paper](https://doi.org/10.3390/electronics13244972) | — |

### 🔧 G. Faults, diagnostics & repair

| Corpus | Task | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|
| Automobile fault text NER (Entropy 2025) | NER | Chinese | \~4.5k/5.5k/4.0k sentences | unknown | on request | 2025 | [paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC11854445/) | — |
| Automotive Industry Fault Data Set | relation extraction | Chinese | 1,441 records | apache-2.0 | open | 2023 | [data](https://huggingface.co/datasets/zhengr/Automotive_Industry_Fault_Data_Set) | — |
| Automotive parts NER (Hu and Ma) | NER | Chinese | not stated | unknown | paper only | 2024 | paper only · [paper](https://doi.org/10.1109/NNICE61279.2024.10499162) | AutoSpecNER, Auto-AdvER, Auto-Features |
| Customer failure reports (Khodadadi et al. 2021) | classification | English | not stated | unknown | paper only | 2021 | paper only · [paper](https://arxiv.org/abs/2111.14977) | — |
| Vehicle fault repair case NER (Electronics 2025) | NER | Chinese | not stated | unknown | paper only | 2025 | paper only · [paper](https://doi.org/10.3390/electronics14071361) | — |

### 📐 H. Engineering documents

| Corpus | Task | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|
| HUPD patents (CPC B60, vehicles) | patents | English | not stated | cc-by-sa-4.0 | open | 2022 | [data](https://huggingface.co/datasets/HUPD/hupd) · [paper](https://arxiv.org/abs/2207.04043) | — |
| ISO 26262 Safety Requirements | requirements | English | \~1,000 samples | MIT | open | — | [data](https://huggingface.co/datasets/Muhammmadd/iso26262-automotive-safety-requirements) | — |

### 🗣️ I. In-car voice assistants & dialogue

#### Task-oriented dialogue and tool use

| Corpus | Task | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|
| CAR-bench | dialogue | English | 254 tasks | MIT | open | 2026 | [data](https://github.com/CAR-bench/car-bench) · [paper](https://arxiv.org/abs/2601.22027) | — |
| CarMem | dialogue | English | 1,000 conversations | unknown | open | 2025 | [data](https://github.com/johanneskirmayr/CarMem) · [paper](https://aclanthology.org/2025.coling-industry.29/) | — |
| In-Vehicle-Tool-Calls | tool calling | English | 43,087 rows | other | open | 2026 | [data](https://huggingface.co/datasets/Senthi1Kumar/In-Vehicle-Tool-Calls-v0.2) | — |
| KVRET (Stanford In-Car Assistant dataset) | dialogue | English | 3,031 dialogues | unknown | open | 2017 | [data](https://huggingface.co/datasets/ConvLab/kvret) · [paper](https://arxiv.org/abs/1705.05414) | — |
| LoCar | dialogue | Korean | not stated | unknown | paper only | 2026 | paper only · [paper](https://arxiv.org/abs/2605.21086) | — |

#### Spoken commands and language understanding

| Corpus | Task | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|
| MAC-SLU | SLU | Chinese | 20.5k rows | apache-2.0 | open | 2025 | [data](https://huggingface.co/datasets/Gatsby1984/MAC_SLU) · [paper](https://arxiv.org/abs/2512.01603) | — |

#### Assistant evaluation

| Corpus | Task | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|
| CarExpert factual-correctness evaluation dataset (Giebisch et al. 2025) | QA | English | not stated | unknown | paper only | 2025 | paper only · [paper](https://arxiv.org/abs/2504.01248) | — |
| In-car contextual-understanding benchmark (Habicht et al. 2025) | classification | English | not stated | unknown | paper only | 2025 | paper only · [paper](https://arxiv.org/abs/2512.12042) | — |
| Vehicle Voice Command Authorization safety benchmark (Afroze et al. 2026) | classification | English | 202 scenarios | unknown | paper only | 2026 | paper only · [paper](https://arxiv.org/abs/2609.19630) | — |

### 🛣️ J. Driving-scene language & multimodal

*For papers and models on language in autonomous driving, see [Awesome-LLM4AD](https://github.com/Thinklab-SJTU/Awesome-LLM4AD), which this section complements; it lists corpora only.*

#### Reasoning and planning with language

| Corpus | Task | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|
| LaMPilot | semantic parsing | English | 4,900 test cases | MIT | open | 2024 | [data](https://github.com/PurdueDigitalTwin/LaMPilot) | — |

### 🔎 K. Search, queries & semantic parsing

*Spider's car_1 database is the only public automotive slice found. No open corpus maps natural-language car-search queries to structured filters.*

| Corpus | Task | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|
| Spider (car_1 database) | text-to-SQL | English | not stated | unknown | open | 2018 | [data](https://yale-lily.github.io/spider) · [paper](https://arxiv.org/abs/1809.08887) | — |

### 🕸️ M. Knowledge graphs, ontologies & lexicons

#### Standards and schemas

| Corpus | Task | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|
| COVESA Vehicle Signal Specification (VSS) | schema / standard | English | not stated | MPL-2.0 | open | — | [data](https://github.com/COVESA/vehicle_signal_specification) | — |
| schema.org Automotive extension (auto.schema.org) / Car & Vehicle types | schema / standard | English | \~15 properties | unknown | open | 2016 | [data](https://schema.org/docs/automotive.html) | — |

#### Make, model and VIN catalogues

| Corpus | Task | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|
| NHTSA vPIC (Vehicle Product Information Catalog) VIN decoder API & standalone database | VIN decoding | English | not stated | unknown | open | — | [data](https://vpic.nhtsa.dot.gov/api/) | — |
| us-car-models-data | gazetteer | English | 15k+ models | unknown | open | — | [data](https://github.com/AbhiOnlyOne/us-car-models-data) | — |
| vehicle-makes-models | gazetteer | English | 164 makes, 2,621 models | ODbL 1.0 | open | — | [data](https://github.com/gor3a/vehicle-makes-models) | — |
| VehicleName - multilingual automotive name database | gazetteer | English, Chinese (Simplified and Traditional), Japanese | 3,030 models, 164 brands | CC BY-SA 4.0 | open | — | [data](https://github.com/ixiehao/VehicleName) | — |
| vehiclesdb | gazetteer | English | 19,282 models | CC BY 4.0 | open | 2026 | [data](https://github.com/vehiclesdb/vehiclesdb) | — |
| Wikidata 'car model' class (Q3231690) and vehicle subgraph | KG / ontology | Multilingual | not stated | unknown | open | — | [data](https://www.wikidata.org/wiki/Q3231690) | — |

#### Glossaries and knowledge graphs

| Corpus | Task | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|
| EVKG - Electric Vehicle Knowledge Graph | KG / ontology | English | not stated | MIT | open | 2023 | [data](https://github.com/EVKG/evkg) · [paper](https://arxiv.org/abs/2304.04893) | — |
| Italian Automotive Glossary | lexicon | Italian | 212 terms | CC BY 4.0 | open | — | [data](https://huggingface.co/datasets/DealerMax/italian-automotive-glossary) | — |

---

_Generated by `python scripts/build_readme.py` from `data/corpora.yaml`. Do not edit this page by hand._
