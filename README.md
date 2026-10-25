# awesome-automotive-nlp

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![Licence: CC BY 4.0](https://img.shields.io/badge/licence-CC%20BY%204.0-lightgrey.svg)](LICENSE) ![Corpora: 131](https://img.shields.io/badge/corpora-131-blue.svg) ![Languages: 11](https://img.shields.io/badge/languages-11-blue.svg)

A curated list of corpora for natural language processing on automotive text, speech and driving scenes: vehicle adverts and listings, reviews and complaints, repair manuals and parts catalogues, in-car dialogue, driving-scene language and the knowledge resources that tie them together. The list grew out of three Auto Trader UK advertisement corpora (AutoSpecNER, Auto-AdvER and Auto-Features), whose related-work sections showed how scattered the field's datasets are. Every row carries task, modality, language, size, licence, access and year tags, and says which of our papers cites it. A corpus is listed if it is freely downloadable or described in a public paper (in which case the row says *paper only* and readers can contact the authors); fee-based commercial catalogues are excluded. See [Contributing](#-contributing) to add one.

**131 corpora** (55 text, 40 multimodal, 15 tabular+text, 11 speech, 10 image) in 11 languages.

**Languages:** English 90 · Chinese 14 · Korean 5 · Japanese 4 · Cantonese 2 · German 2 · Italian 2 · Czech 1 · French 1 · Indonesian 1 · Romanian 1 · n/a (images) 10 · Multilingual 3 · n/a (noise recordings) 2 · unknown 1

**Download:** [CSV](data/corpora.csv) · [JSON](data/corpora.json) (related papers: [CSV](data/papers.csv) · [JSON](data/papers.json))

**Browse by modality:** [Text](modalities/text.md) (55) · [Speech](modalities/speech.md) (11) · [Multimodal](modalities/multimodal.md) (40) · [Images](modalities/image.md) (10) · [Tabular + text](modalities/tabular-text.md) (15)

## 📑 Contents

- [🗂️ Taxonomy](#️-taxonomy)
- [Corpora by application area](#corpora-by-application-area)
  - [🚗 A. Vehicle identification & specifications](#-a-vehicle-identification--specifications) (13)
  - [🏷️ B. Listings, adverts & claims](#️-b-listings-adverts--claims) (4)
  - [🧩 C. Features, attributes & catalogue linking](#-c-features-attributes--catalogue-linking) (1)
  - [⭐ D. Reviews, opinion & sentiment](#-d-reviews-opinion--sentiment) (20)
  - [⚠️ E. Complaints, safety, recalls & incidents](#️-e-complaints-safety-recalls--incidents) (12)
  - [🔧 F. Maintenance, repair, parts & technical documents](#-f-maintenance-repair-parts--technical-documents) (12)
  - [🗣️ G. In-car voice assistants & dialogue](#️-g-in-car-voice-assistants--dialogue) (25)
  - [🛣️ H. Driving-scene language & multimodal](#️-h-driving-scene-language--multimodal) (32)
  - [🔎 I. Search, queries & semantic parsing](#-i-search-queries--semantic-parsing) (1)
  - [💷 J. Market, pricing & listing tables with text](#-j-market-pricing--listing-tables-with-text) (0)
  - [🕸️ K. Knowledge graphs, ontologies & lexicons](#️-k-knowledge-graphs-ontologies--lexicons) (11)
- [Browse by modality](modalities/README.md)
- [📄 Related papers (no public data)](#-related-papers-no-public-data) (2)
- [📝 How to cite](#-how-to-cite)
- [🤝 Contributing](#-contributing)

## 🗂️ Taxonomy

The primary axis is the application area, one section per bucket; larger sections are split into sub-headings. Every bucket is shown, even when empty, and a short note under a section heading explains a gap or points to where related corpora are listed. The secondary axes are the table columns: task, modality (text, speech, multimodal, image, tabular+text), language, size, licence, access, year, links and the paper of ours that cites the row. Task, size and licence are shown in short form; the full values are in `data/corpora.yaml` and in the CSV and JSON downloads.

- **🚗 A. Vehicle identification & specifications**: make/model/trim/engine NER, car-type recognition from text or image, VIN, spec sheets
- **🏷️ B. Listings, adverts & claims**: classified-ad IE (condition, history, offers), ad generation & verification, listing corpora
- **🧩 C. Features, attributes & catalogue linking**: feature-conditioned NER, attribute-value extraction, product/catalogue linking
- **⭐ D. Reviews, opinion & sentiment**: car reviews, automotive ABSA, forums, social media opinion
- **⚠️ E. Complaints, safety, recalls & incidents**: NHTSA/ODI complaints, defect reports, crash narratives, recall text
- **🔧 F. Maintenance, repair, parts & technical documents**: auto-parts NER, repair/diagnostic QA, service records, manuals, patents
- **🗣️ G. In-car voice assistants & dialogue**: in-car task-oriented dialogue, SLU intent/slot, in-vehicle ASR/speech, driver-vehicle interaction
- **🛣️ H. Driving-scene language & multimodal**: Talk2Car, nuScenes-QA, DriveLM, BDD-X, LingoQA, HAD, DRAMA, referring expressions, driving captions
- **🔎 I. Search, queries & semantic parsing**: NL-to-structured automotive search, query logs, synthetic query corpora, text-to-SQL on car data
- **💷 J. Market, pricing & listing tables with text**: used-car price datasets that carry free text, Craigslist/Kaggle car listings
- **🕸️ K. Knowledge graphs, ontologies & lexicons**: automotive ontologies (e.g. VSS), KGs, taxonomies, lexicons

## Corpora by application area

### 🚗 A. Vehicle identification & specifications

#### Text: vehicle-domain NER

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| AutoSpecNER | NER | text | English | 659 adverts | CC BY 4.0 | open | 2026 | [data](https://github.com/FilipposVentirozos/AutoSpecNER) · [paper](https://aclanthology.org/2026.icnlsp-1.8/) | — |
| EWNERTC (automotive subset) | fine-grained NER | text | English | 10,349 sentences | CC BY 4.0 | open | 2020 | [data](https://data.mendeley.com/datasets/cdcztymf4k/1) · [paper](https://aclanthology.org/2020.coling-main.334) | Auto-AdvER |
| FindVehicle | NER | text | English | 42.3k descriptions | unknown | open | 2024 | [data](https://github.com/GuanRunwei/FindVehicle) · [paper](https://doi.org/10.1007/s11042-023-16373-y) | AutoSpecNER, Auto-AdvER, Auto-Features |

#### Images: make, model and type recognition

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| BoxCars116k | image classification | image | n/a (images) | \~116k images | research only | open | 2018 | [data](https://github.com/JakubSochor/BoxCars) | — |
| Car Connection Picture Dataset | image classification | image | n/a (images) | \~60k images | unknown | open | — | [data](https://github.com/nicolas-gervais/predicting-car-price-from-scraped-data/tree/master/picture-scraper) | — |
| Car Models 3778 | image classification | image | n/a (images) | \~193k images | other | open | — | [data](https://huggingface.co/datasets/Unit293/car_models_3887) | — |
| CompCars | image classification | image | n/a (images) | 136,726 + 50,000 images | non-commercial research only | on request | 2015 | [data](https://mmlab.ie.cuhk.edu.hk/datasets/comp_cars/index.html) | — |
| Stanford Cars | image classification | image | n/a (images) | 16,185 images | unknown | open | 2013 | [data](https://www.tensorflow.org/datasets/catalog/cars196) | — |
| VMMRdb | image classification | image | n/a (images) | 291,752 images | MIT | open | 2017 | [data](https://github.com/faezetta/VMMRdb) | — |

#### Images: re-identification and damage

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| CarDD | damage detection | image | n/a (images) | 4,000 images | unknown | on request | 2023 | [data](https://cardd-ustc.github.io/) | — |
| PKU VehicleID | re-identification | image | n/a (images) | 221,763 images | academic use only | on request | 2016 | [data](https://www.pkuml.org/resources/pku-vehicleid.html) | — |
| VeRi-776 | re-identification | image | n/a (images) | 50k+ images | non-commercial use only | on request | 2016 | [data](https://vehiclereid.github.io/VeRi/) | — |
| VERI-Wild | re-identification | image | n/a (images) | 416,314 images | non-commercial | on request | 2019 | [data](https://github.com/PKU-IMRE/VERI-Wild) | — |

### 🏷️ B. Listings, adverts & claims

#### Listings and adverts

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| Auto-AdvER | span labelling | text | English | 605 adverts | CC BY 4.0 | open | 2026 | [data](https://github.com/FilipposVentirozos/Auto-AdvER) · [paper](https://arxiv.org/abs/2412.05655) | AutoSpecNER, Auto-Features |
| Craigslist Used Cars | listings | tabular+text | English | \~426k rows | CC0: Public Domain | open | 2021 | [data](https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data) | — |
| DVM-CAR | listings | multimodal | English | 0.25M+ adverts | CC BY-NC 4.0 | open | 2021 | [data](https://deepvisualmarketing.github.io/) · [paper](https://arxiv.org/abs/2109.00881) | — |

#### Buyer-seller dialogue

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| CraigslistBargain | dialogue | text | English | 6k+ dialogues | unknown | open | 2018 | [data](https://huggingface.co/datasets/stanfordnlp/craigslist_bargains) · [paper](https://aclanthology.org/D18-1256/) | — |

### 🧩 C. Features, attributes & catalogue linking

*No public automotive-specific attribute-extraction or catalogue-linking corpus was found. Auto-Features (forthcoming, listed below) is built for this task; the general product-attribute sets MAVE, OA-Mine and AE-110K contain no automotive category.*

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| Auto-Features | NER + entity linking | text | English | 1,256 adverts | to be announced at release | forthcoming | 2026 | forthcoming (release pending) | — |

### ⭐ D. Reviews, opinion & sentiment

#### Consumer and expert reviews

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| Amazon Review Data (2018) - Automotive category | sentiment | text | English | 7,990,166 reviews | unknown | open | 2018 | [data](https://nijianmo.github.io/amazon/index.html) | — |
| Amazon Reviews 2023 - Automotive category | sentiment | text | English | 20.0M reviews | unknown | open | 2023 | [data](https://amazon-reviews-2023.github.io/) | — |
| Car Reviews (Hugging Face) | sentiment | text | English | 36,984 rows | unknown | open | — | [data](https://huggingface.co/datasets/florentgbelidji/car-reviews) | — |
| Edmunds Car Reviews (Kaggle) | sentiment | text | English | not stated | CC BY-SA 4.0 | open | 2021 | [data](https://www.kaggle.com/datasets/shreemunpranav/edmunds-car-review) | — |
| Electric Vehicles User Reviews India (Kaggle) | sentiment | text | English | not stated | CC0: Public Domain | open | 2022 | [data](https://www.kaggle.com/datasets/deadprstkrish/ev-cars-user-reviews-india) | — |
| Expert Car Reviews Dataset (Kaggle) | summarisation | tabular+text | English | not stated | Other | open | 2024 | [data](https://www.kaggle.com/datasets/ademboukhris/expert-car-reviews-dataset) | — |
| OpinRank Review Dataset (Edmunds car reviews) | sentiment | text | English | \~42,230 car reviews | CC BY 4.0 | open | 2011 | [data](https://archive.ics.uci.edu/dataset/205/opinrank+review+dataset) | — |
| SRNI-CAR (Chinese automotive market dataset) - owner reviews component | sentiment | tabular+text | Chinese | 217,292 comments | CC BY-NC 4.0 | open | 2023 | [data](https://srni-car.github.io) · [paper](https://arxiv.org/abs/2401.05395) | — |
| Yelp Open Dataset (Automotive category businesses) | sentiment | text | English | not stated | intended for educational use | open | 2013 | [data](https://business.yelp.com/data/resources/open-dataset/) | — |

#### Sentiment and aspect-based gold standards

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| ALSA (Aspect-Level Sentiment Analysis in Automotive Domain) | ABSA | text | English, Korean | 58k+ comment-aspect pairs | research use only | on request | 2020 | [data](https://github.com/dmhyun/ALSAdata) · [paper](https://aclanthology.org/2020.coling-main.83/) | — |
| CCF BDCI 2018 Automotive User Opinion Topic and Sentiment Recognition | ABSA | text | Chinese | not stated | unknown | on request | 2018 | [data](https://www.datafountain.cn/competitions/310) | — |
| Chinese car review sentiment dataset (Liu et al. 2022, ATWWM-BERT) | sentiment | text | Chinese | 9,947 reviews | unknown | paper only | 2022 | paper only · [paper](https://arxiv.org/abs/2206.02389) | — |
| IndoNLU CASA (Indonesian car review ABSA) | ABSA | text | Indonesian | 1,080 reviews | MIT | open | 2018 | [data](https://huggingface.co/datasets/indonlp/indonlu) | — |
| InfoBarometer (German automotive industry explainable sentiment) | sentiment | text | German | 1,039 news articles | unknown | paper only | 2023 | paper only · [paper](https://aclanthology.org/2023.wassa-1.13/) | — |
| JDPA Sentiment Corpus for the Automotive Domain | ABSA | text | English | 515 documents | (c) Copyright 2009-2010, J.D. Power… | on request | 2010 | [data](https://verbs.colorado.edu/jdpacorpus/README.txt) | — |
| PACE Corpus (Polarity-annotated Automotive and CEllphone) | ABSA | text | English, German | 2,000 forum posts | unknown | paper only | 2014 | paper only · [paper](https://aclanthology.org/L14-1240/) | — |

#### Social and video media

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| Automotive brand's products - Twitter dataset (Mendeley Data) | sentiment | text | unknown | not stated | CC BY 4.0 | open | — | [data](https://data.mendeley.com/datasets/hcc2h426h3/1) | — |
| MuSe-CaR (Multimodal Sentiment Analysis in Car Reviews) | sentiment | multimodal | English | 40+ h video | EULA, academic use only | on request | 2021 | [data](https://www.muse-challenge.org) · [paper](https://arxiv.org/abs/2101.06053) | — |
| SenTube (SenTube-A automobiles subset) | sentiment | text | English, Italian | 3,381/225/903 comments | unknown | paper only | 2014 | paper only · [paper](https://aclanthology.org/L14-1188/) | — |
| YouTube AV 50K | sentiment | text | English | 50k+ comments | unknown | paper only | 2018 | paper only · [paper](https://arxiv.org/abs/1807.11227) | — |

### ⚠️ E. Complaints, safety, recalls & incidents

#### NHTSA defects, recalls and investigations (US)

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| NHTSA Customer Complaints (Kaggle) | complaint text | tabular+text | English | not stated | CC0: Public Domain | open | 2026 | [data](https://www.kaggle.com/datasets/alshival/nhtsa-complaints) | — |
| NHTSA Defect Investigations (flat file) | investigation text | tabular+text | English | not stated | unknown | open | 1972 | [data](https://static.nhtsa.gov/odi/ffdd/inv/INV.txt) | — |
| NHTSA Manufacturer Communications / Technical Service Bulletins (flat file) | service bulletins | tabular+text | English | not stated | unknown | open | 1995 | [data](https://static.nhtsa.gov/odi/ffdd/tsbs/TSBS.txt) | — |
| NHTSA ODI Complaints (flat file) | complaint text | tabular+text | English | 2.2M complaints | unknown | open | 1995 | [data](https://static.nhtsa.gov/odi/ffdd/cmpl/CMPL.txt) | — |
| NHTSA ODI complaints - high-signal subset (Hugging Face) | complaint text | tabular+text | English | 213,093 records | federal-works-and-cc0-card-metadata | open | — | [data](https://huggingface.co/datasets/emperor-mew/nhtsa-complaints) | — |
| NHTSA Recalls (flat file) | recall text | tabular+text | English | not stated | unknown | open | 1967 | [data](https://static.nhtsa.gov/odi/ffdd/rcl/RCL.txt) | — |

#### Recalls in other jurisdictions

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| DVSA Vehicle Recalls File (UK) | recall text | tabular+text | English | \~5 MB CSV | Open Government Licence v3.0 | open | 1992 | [data](https://www.check-vehicle-recalls.service.gov.uk/) | — |
| Transport Canada Vehicle Recalls Database | recall text | tabular+text | English, French | not stated | Open Government Licence - Canada | open | — | [data](https://open.canada.ca/data/en/dataset/1ec92326-47ef-4110-b7ca-959fab03f96d) | — |

#### Crash and automated-driving incident narratives

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| California DMV Autonomous Vehicle Disengagement Reports | incident reports | tabular+text | English | \~634k characters (2024) | unknown | open | 2015 | [data](https://www.dmv.ca.gov/portal/file/2024-autonomous-vehicle-disengagement-reports-csv/) | — |
| Iowa DOT crash report narratives (as used in Bhagat et al. 2025) | crash narratives | text | English | 94,367 narratives | unknown | paper only | 2025 | paper only · [paper](https://arxiv.org/abs/2504.13068) | — |
| NHTSA Standing General Order 2021-01 Crash Reports (ADS and Level 2 ADAS) | crash narratives | tabular+text | English | not stated | unknown | open | 2021 | [data](https://static.nhtsa.gov/odi/ffdd/sgo-2021-01/SGO-2021-01_Data_Element_Definitions.pdf) | — |
| NMVCCS - National Motor Vehicle Crash Causation Survey | crash narratives | multimodal | English | 6,949 crashes | unknown | open | 2008 | [data](https://catalog.data.gov/dataset/national-motor-vehicle-crash-causation-survey-nmvccs-nmvccs-xml-case-viewer) | — |

### 🔧 F. Maintenance, repair, parts & technical documents

#### Manuals, FAQs & question answering

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| ADMit automotive NER data | NER | text | Korean, English | not stated | unknown | paper only | 2023 | paper only · [paper](https://doi.org/10.1016/j.eswa.2023.120007) | AutoSpecNER, Auto-AdvER |
| DelucionQA | QA + hallucination | text | English | 913 questions | CC BY 4.0 | open | 2023 | [data](https://github.com/boschresearch/DelucionQA) · [paper](https://aclanthology.org/2023.findings-emnlp.59.pdf) | — |
| FETA car manuals benchmark | retrieval | multimodal | English | not stated | apache-2.0 | open | 2022 | [data](https://huggingface.co/datasets/alfassy/FETA_IKEA_CAR_MANUALS) · [paper](https://arxiv.org/abs/2209.03648) | — |
| MaQA (Manual Question Answering) | QA + classification | text | Korean, English | 45,641 questions | unknown | paper only | 2024 | paper only · [paper](https://doi.org/10.3390/electronics13244972) | — |

#### Faults, repair and parts

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| Automotive_Industry_Fault_Data_Set | relation extraction | text | Chinese | 1,441 records | apache-2.0 | open | 2023 | [data](https://huggingface.co/datasets/zhengr/Automotive_Industry_Fault_Data_Set) | — |
| Chinese automobile fault text NER datasets (Entropy 2025) | NER | text | Chinese | \~4.5k/5.5k/4.0k sentences | unknown | on request | 2025 | [paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC11854445/) | — |
| Chinese vehicle fault repair case NER (Electronics 2025) | NER | text | Chinese | not stated | unknown | paper only | 2025 | paper only · [paper](https://doi.org/10.3390/electronics14071361) | — |
| Chinese Vehicle Fleet Fault Association Dataset (Hangzhou Normal University) | NER + KG / ontology | tabular+text | Chinese | not stated | CC BY 4.0 | open | 2026 | [data](https://data.mendeley.com/datasets/r98g7g6k5t/1) | — |
| Free-text customer failure reports for automated vehicle diagnostics (Khodadadi et al. 2021) | classification | text | English | not stated | unknown | paper only | 2021 | paper only · [paper](https://arxiv.org/abs/2111.14977) | — |
| Named Entity Recognition of Automotive Parts Based on RoBERTa-CRF Model (Hu and Ma) | NER | text | Chinese | not stated | unknown | paper only | 2024 | paper only · [paper](https://doi.org/10.1109/NNICE61279.2024.10499162) | AutoSpecNER, Auto-AdvER, Auto-Features |

#### Requirements, standards and patents

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| Automotive ISO 26262 Safety Requirements Dataset | requirements | text | English | \~1,000 samples | MIT | open | — | [data](https://huggingface.co/datasets/Muhammmadd/iso26262-automotive-safety-requirements) | — |
| Harvard USPTO Patent Dataset (HUPD) - CPC B60 (vehicles) filterable | patents | text | English | not stated | cc-by-sa-4.0 | open | 2022 | [data](https://huggingface.co/datasets/HUPD/hupd) · [paper](https://arxiv.org/abs/2207.04043) | — |

### 🗣️ G. In-car voice assistants & dialogue

#### Task-oriented dialogue and tool use

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| AMIE in-cabin passenger-agent dialogue dataset | SLU | multimodal | English | 1,331 utterances | unknown | paper only | 2019 | paper only · [paper](https://arxiv.org/abs/1904.10500) | — |
| CAR-bench | dialogue | text | English | 254 tasks | MIT | open | 2026 | [data](https://github.com/CAR-bench/car-bench) · [paper](https://arxiv.org/abs/2601.22027) | — |
| CarMem | dialogue | text | English | 1,000 conversations | unknown | open | 2025 | [data](https://github.com/johanneskirmayr/CarMem) · [paper](https://aclanthology.org/2025.coling-industry.29/) | — |
| In-Vehicle-Tool-Calls | tool calling | text | English | 43,087 rows | other | open | 2026 | [data](https://huggingface.co/datasets/Senthi1Kumar/In-Vehicle-Tool-Calls-v0.2) | — |
| KVRET (Stanford In-Car Assistant dataset) | dialogue | text | English | 3,031 dialogues | unknown | open | 2017 | [data](https://huggingface.co/datasets/ConvLab/kvret) · [paper](https://arxiv.org/abs/1705.05414) | — |
| LoCar | dialogue | text | Korean | not stated | unknown | paper only | 2026 | paper only · [paper](https://arxiv.org/abs/2605.21086) | — |

#### Spoken commands and language understanding

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| in_car_commands (Korean in-car voice commands) | ASR | speech | Korean | 72,000 rows | apache-2.0 | open | — | [data](https://huggingface.co/datasets/Angeriod/in_car_commands_60) | — |
| MAC-SLU | SLU | text | Chinese | 20.5k rows | apache-2.0 | open | 2025 | [data](https://huggingface.co/datasets/Gatsby1984/MAC_SLU) · [paper](https://arxiv.org/abs/2512.01603) | — |

#### Assistant evaluation

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| CarExpert factual-correctness evaluation dataset (Giebisch et al. 2025) | QA | text | English | not stated | unknown | paper only | 2025 | paper only · [paper](https://arxiv.org/abs/2504.01248) | — |
| In-car contextual-understanding benchmark (Habicht et al. 2025) | classification | text | English | not stated | unknown | paper only | 2025 | paper only · [paper](https://arxiv.org/abs/2512.12042) | — |
| InCarEmo | classification | multimodal | Chinese | not stated | unknown | paper only | 2026 | paper only · [paper](https://arxiv.org/abs/2607.14683) | — |
| Vehicle Voice Command Authorization safety benchmark (Afroze et al. 2026) | classification | text | English | 202 scenarios | unknown | paper only | 2026 | paper only · [paper](https://arxiv.org/abs/2609.19630) | — |

#### In-car speech recognition

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| AISHELL-5 | ASR | speech | Chinese | 100+ h speech | CC BY-SA 4.0 | open | 2025 | [data](https://openslr.org/159/) · [paper](https://arxiv.org/abs/2505.23036) | — |
| AVICAR | ASR | speech | English | \~59k utterances | unknown | paper only | 2004 | paper only · [paper](https://www.isca-archive.org/interspeech_2004/lee04m_interspeech.html) | — |
| CENSREC-2 | ASR | speech | Japanese | 14,687 utterances | For research and development purposes… | on request | 2005 | [data](https://research.nii.ac.jp/src/en/CENSREC-2.html) | — |
| CENSREC-3 | ASR | speech | Japanese | 14,050 utterances | For research and development purposes… | on request | 2006 | [data](https://research.nii.ac.jp/src/en/CENSREC-3.html) | — |
| CI-AVSR | audio-visual ASR | multimodal | Cantonese | 4,984 samples (8.3 h) | CC0-1.0 | open | 2022 | [data](https://github.com/HLTCHKUST/CI-AVSR) · [paper](https://arxiv.org/abs/2201.03804) | — |
| CIAIR In-Car Speech Database | dialogue | multimodal | Japanese | \~800 subjects | unknown | paper only | 2004 | paper only · [paper](https://www.isca-archive.org/interspeech_2004/kawaguchi04_interspeech.html) | — |
| CU-Move | ASR | speech | English | \~500 speakers | unknown | on request | 2001 | [data](https://utdrive.utdallas.edu/corpus) · [paper](https://www.isca-archive.org/eurospeech_2001/hansen01b_eurospeech.html) | — |
| Guangzhou Cantonese Scripted Speech Corpus in the Vehicle | ASR | speech | Cantonese | 6,219 utterances (5 h) | CC BY-NC-ND 4.0 | open | — | [data](https://huggingface.co/datasets/AlienKevin/guangzhou-cabin-speech) | — |
| STAZKA - Speech recordings from vehicles | ASR | speech | Czech | 26 speakers | Creative Commons - Attribution-NonComme… | open | 2015 | [data](https://b2find.eudat.eu/dataset/9d65f782-5271-5cb9-afd0-5c0f28667403) | — |
| TAICAR | ASR | speech | Chinese (Taiwan Mandarin) | 163k+ files (16.8 GB) | unknown | paper only | 2005 | paper only · [paper](https://aclanthology.org/O05-3005/) | — |
| UTDrive | ASR | multimodal | English | 37 F + 40 M drivers | unknown | open | 2007 | [data](https://utdrive.utdallas.edu/corpus) | — |

#### Cabin acoustics and noise

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| ASR-CabNois (MagicHub in-vehicle noise dataset) | noise / acoustics | speech | n/a (noise recordings) | 5.08 h noise | Magic Data open-source license / CC… | open | — | [data](https://magichub.com/datasets/in-vehicle-noise-dataset/) | — |
| CAVEMOVE | noise / acoustics | speech | n/a (noise recordings) | 7.6 GB recordings | Creative Commons Attribution 4.0… | open | 2025 | [data](https://zenodo.org/doi/10.5281/zenodo.13594242) · [paper](https://arxiv.org/abs/2508.19691) | — |

### 🛣️ H. Driving-scene language & multimodal

*For papers and models on language in autonomous driving, see [Awesome-LLM4AD](https://github.com/Thinklab-SJTU/Awesome-LLM4AD), which this section complements; it lists corpora only.*

#### Grounding, referring expressions and retrieval

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| CityFlow-NL | retrieval + grounding | multimodal | English | 2,155 train tracks | repo Apache-2.0 | open | 2021 | [data](https://github.com/fredfung007/cityflow-nl) · [paper](https://arxiv.org/abs/2101.04741) | — |
| HAD | grounding + captioning | multimodal | English | \~30 h video | non-commercial use only | on request | 2019 | [data](https://usa.honda-ri.com/HAD) · [paper](https://openaccess.thecvf.com/content_CVPR_2019/papers/Kim_Grounding_Human-To-Vehicle_Advice_for_Self-Driving_Vehicles_CVPR_2019_paper.pdf) | — |
| NuPrompt | grounding | multimodal | English | 40,147 prompts | repo Apache-2.0 | open | 2023 | [data](https://github.com/wudongming97/Prompt4Driving) · [paper](https://arxiv.org/abs/2309.04379) | — |
| Refer-KITTI | grounding | multimodal | English | 818 expressions | unknown | open | 2023 | [data](https://referringmot.github.io/) · [paper](https://arxiv.org/abs/2303.03366) | — |
| Talk2Car | grounding | multimodal | English | 11,959 commands | unknown | open | 2019 | [data](https://talk2car.github.io/) · [paper](https://arxiv.org/abs/1909.10838) | — |

#### Scene question answering and instruction tuning

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| MAPLM | VQA | multimodal | English | not stated | repo MIT | open | 2023 | [data](https://github.com/LLVM-AD/MAPLM) · [paper](https://openaccess.thecvf.com/content/CVPR2024/papers/Cao_MAPLM_A_Real-World_Large-Scale_Vision-Language_Benchmark_for_Map_and_Traffic_CVPR_2024_paper.pdf) | — |
| NuInstruct | VQA | multimodal | English | 91k video-QA pairs | unknown | open | 2024 | [data](https://github.com/xmed-lab/NuInstruct) · [paper](https://arxiv.org/abs/2401.00988) | — |
| NuScenes-MQA | VQA + captioning | multimodal | English | not stated | repo Apache-2.0 | open | 2023 | [data](https://github.com/turingmotors/NuScenes-MQA) · [paper](https://arxiv.org/abs/2312.06352) | — |
| NuScenes-QA | VQA | multimodal | English | 460k QA pairs | repo MIT | open | 2023 | [data](https://github.com/qiantianwen/NuScenes-QA) · [paper](https://arxiv.org/abs/2305.14836) | — |
| OmniDrive-nuScenes | VQA | multimodal | English | not stated | unknown | open | 2024 | [data](https://github.com/NVlabs/OmniDrive) · [paper](https://arxiv.org/abs/2405.01533) | — |
| SURDS | VQA | multimodal | English | not stated | academic use only | open | 2024 | [data](https://github.com/XiandaGuo/Drive-MLLM) | — |
| Talk2BEV | VQA | multimodal | English | 20k+ questions | unknown | open | 2023 | [data](https://llmbev.github.io/talk2bev/) · [paper](https://arxiv.org/abs/2310.02251) | — |

#### Explanations, captions and risk narration

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| BDD-OIA | classification | multimodal | English | not stated | unknown | open | 2020 | [data](https://github.com/Twizwei/bddoia_project) | — |
| BDD-X | explanation | multimodal | English | 6,970 videos (\~77 h) | unknown | open | 2018 | [data](https://github.com/JinkyuKimUCB/BDD-X-dataset) · [paper](https://openaccess.thecvf.com/content_ECCV_2018/papers/Jinkyu_Kim_Textual_Explanations_for_ECCV_2018_paper.pdf) | — |
| CoVLA | captioning | multimodal | English | 80+ h video | released for academic use | open | 2024 | [data](https://turingmotors.github.io/covla-ad/) · [paper](https://arxiv.org/abs/2408.10845) | — |
| DRAMA | captioning + grounding | multimodal | English | 17,785 clips | non-commercial use only | on request | 2023 | [data](https://usa.honda-ri.com/drama) · [paper](https://openaccess.thecvf.com/content/WACV2023/papers/Malla_DRAMA_Joint_Risk_Localization_and_Captioning_in_Driving_WACV_2023_paper.pdf) | — |
| DriveGPT4 instruction data | VQA | multimodal | English | not stated | unknown | paper only | 2023 | paper only · [paper](https://arxiv.org/abs/2310.01412) | — |
| Rank2Tell | VQA + captioning | multimodal | English | 116 clips | unknown | on request | 2023 | [data](https://usa.honda-ri.com/rank2tell) · [paper](https://arxiv.org/abs/2309.06597) | — |

#### Reasoning and planning with language

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| DriveBench | VQA | multimodal | English | 20,498 QA pairs | Apache-2.0 | open | 2025 | [data](https://github.com/drive-bench/toolkit) · [paper](https://arxiv.org/abs/2501.04003) | — |
| DriveLM | VQA | multimodal | English | not stated | language data CC BY-NC-SA 4.0 | open | 2023 | [data](https://github.com/OpenDriveLab/DriveLM) · [paper](https://arxiv.org/abs/2312.14150) | — |
| Driving-with-LLMs | VQA | tabular+text | English | \~10k/1k VQA items | repo Apache-2.0 | open | 2023 | [data](https://github.com/wayveai/Driving-with-LLMs) · [paper](https://arxiv.org/abs/2310.01957) | — |
| LaMPilot | semantic parsing | text | English | 4,900 test cases | MIT | open | 2024 | [data](https://github.com/PurdueDigitalTwin/LaMPilot) | — |
| LingoQA | video QA | multimodal | English | 419.9k QA pairs | unknown | open | 2023 | [data](https://github.com/wayveai/LingoQA) · [paper](https://arxiv.org/abs/2312.14115) | — |
| Reason2Drive | VQA | multimodal | English | 600k+ video-text pairs | unknown | open | 2023 | [data](https://github.com/fudan-zvg/Reason2Drive) · [paper](https://arxiv.org/abs/2312.03661) | — |
| V2V-QA | VQA | multimodal | English | not stated | unknown | open | 2025 | [data](https://eddyhkchiu.github.io/v2vllm.github.io/) · [paper](https://arxiv.org/abs/2502.09980) | — |

#### Traffic rules and driving-test QA

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| DriveCombo | QA + VQA | multimodal | Multilingual | \~70k questions | unknown | paper only | 2026 | paper only · [paper](https://arxiv.org/abs/2603.01637) | — |
| DriveQA | QA + VQA | multimodal | English | 474k QA pairs | unknown | open | 2025 | [data](https://driveqaiccv.github.io/) · [paper](https://arxiv.org/abs/2508.21824) | — |
| DrivingVQA | VQA | multimodal | English | 3,931 problems | unknown | open | 2025 | [data](https://vita-epfl.github.io/DrivingVQA/) · [paper](https://arxiv.org/abs/2501.04671) | — |
| IDKB | QA + VQA | multimodal | Multilingual | 1M+ data items | unknown | paper only | 2024 | paper only · [paper](https://arxiv.org/abs/2409.02914) | — |
| Romanian Driving Laws QA | QA + VQA | multimodal | Romanian | 1,208 questions | unknown | paper only | 2025 | paper only · [paper](https://arxiv.org/abs/2509.23715) | — |

#### Roadside traffic-video QA

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| SUTD-TrafficQA | video QA | multimodal | English | 62,535 QA pairs | unknown | on request | 2021 | [data](https://github.com/sutdcv/SUTD-TrafficQA) · [paper](https://arxiv.org/abs/2103.15538) | — |
| TUMTraffic-VideoQA | video QA + captioning | multimodal | English | 85k MCQ pairs | CC BY-NC-SA 4.0 | open | 2025 | [data](https://innovation-mobility.com/en/project-providentia/a9-dataset) · [paper](https://arxiv.org/abs/2502.02449) | — |

### 🔎 I. Search, queries & semantic parsing

*Spider's car_1 database is the only public automotive slice found. No open corpus maps natural-language car-search queries to structured filters.*

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| Spider (car_1 database) | text-to-SQL | text | English | not stated | unknown | open | 2018 | [data](https://yale-lily.github.io/spider) · [paper](https://arxiv.org/abs/1809.08887) | — |

### 💷 J. Market, pricing & listing tables with text

*Used-car price and specification tables without free text are not NLP corpora and are not listed. Listing corpora with free text are in section B.*

### 🕸️ K. Knowledge graphs, ontologies & lexicons

#### Standards and schemas

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| COVESA Vehicle Signal Specification (VSS) | schema / standard | text | English | not stated | MPL-2.0 | open | — | [data](https://github.com/COVESA/vehicle_signal_specification) | — |
| schema.org Automotive extension (auto.schema.org) / Car & Vehicle types | schema / standard | text | English | \~15 properties | unknown | open | 2016 | [data](https://schema.org/docs/automotive.html) | — |

#### Make, model and VIN catalogues

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| NHTSA vPIC (Vehicle Product Information Catalog) VIN decoder API & standalone database | VIN decoding | text | English | not stated | unknown | open | — | [data](https://vpic.nhtsa.dot.gov/api/) | — |
| us-car-models-data | gazetteer | text | English | 15k+ models | unknown | open | — | [data](https://github.com/AbhiOnlyOne/us-car-models-data) | — |
| vehicle-makes-models | gazetteer | text | English | 164 makes, 2,621 models | ODbL 1.0 | open | — | [data](https://github.com/gor3a/vehicle-makes-models) | — |
| VehicleName - multilingual automotive name database | gazetteer | text | English, Chinese (Simplified and Traditional), Japanese | 3,030 models, 164 brands | CC BY-SA 4.0 | open | — | [data](https://github.com/ixiehao/VehicleName) | — |
| vehiclesdb | gazetteer | text | English | 19,282 models | CC BY 4.0 | open | 2026 | [data](https://github.com/vehiclesdb/vehiclesdb) | — |
| Wikidata 'car model' class (Q3231690) and vehicle subgraph | KG / ontology | text | Multilingual | not stated | unknown | open | — | [data](https://www.wikidata.org/wiki/Q3231690) | — |

#### Glossaries and knowledge graphs

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| Car-identification - Autohome car knowledge graph & QA | KG / ontology + QA | multimodal | Chinese | 284 brands, 2,058 series | unknown | open | — | [data](https://github.com/LongxingHu/Car-identification) | — |
| EVKG - Electric Vehicle Knowledge Graph | KG / ontology | text | English | not stated | MIT | open | 2023 | [data](https://github.com/EVKG/evkg) · [paper](https://arxiv.org/abs/2304.04893) | — |
| Italian Automotive Glossary | lexicon | text | Italian | 212 terms | CC BY 4.0 | open | — | [data](https://huggingface.co/datasets/DealerMax/italian-automotive-glossary) | — |

## 📄 Related papers (no public data)

Automotive NLP papers with no public corpus: each describes a system, benchmark or evaluation whose data has not been released. They are listed with the academic reference so that readers can contact the authors.

| Paper | Task | Lang | Year | Link | Cited in |
|---|---|---|---|---|---|
| CarExpert | QA | English | 2023 | [paper](https://aclanthology.org/2023.emnlp-industry.56/) | — |
| DeepTest 2026 LLM Testing Competition: automotive manual assistant benchmark | QA | English | 2026 | [paper](https://arxiv.org/abs/2604.12615) | — |

## 📝 How to cite

To cite the list itself, use the repository's [CITATION.cff](CITATION.cff). The three Auto Trader UK corpora that seeded it:

```bibtex
@inproceedings{lee-etal-2026-autospecner,
    title = "{A}uto{S}pec{NER}: A Fine-Grained Named Entity Recognition Dataset for Vehicle Specification Extraction",
    author = "Lee, Jordan  and
      Ventirozos, Filippos  and
      Abdullahm, Abdirahman  and
      Nteka, Ioanna  and
      Appleby, Peter  and
      Shardlow, Matthew",
    editor = "Abbas, Mourad  and
      Freihat, Abed Alhakim",
    booktitle = "Proceedings of the 9th International Conference on Natural Language and Speech Processing ({ICNLSP}-2026)",
    month = sep,
    year = "2026",
    address = "University of Trento, Trento, Italy",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2026.icnlsp-1.8/",
    pages = "67--81",
    ISBN = "979-8-89176-458-3"
}
```

```bibtex
@inproceedings{ventirozos2026autoadver,
  title     = {Auto-AdvER: Disentangling Condition, History, and Commercial Offers in
               Automotive Advertisements},
  author    = {Filippos Ventirozos and Ioanna Nteka and Tania Nandy and Jozef Baca and Charlie Roadhouse and Peter Appleby and Matthew Shardlow},
  booktitle = {Proceedings of the 5th Conference of the Asia-Pacific Chapter of the Association for
               Computational Linguistics and the 15th International Joint Conference on Natural
               Language Processing (AACL-IJCNLP 2026)},
  year      = {2026},
  note      = {To appear}
}
```

```bibtex
% TODO author to complete: Auto-Features is under review; add authors, venue and year at camera-ready.
@misc{auto-features-TODO,
  title = {Auto-Features: An LLM-Assisted Corpus for Contextual Recognition of Standard and Optional Car Features},
  note  = {Under review}
}
```

## 🤝 Contributing

Contributions are welcome. Open an issue with the *New corpus* form, or send a pull request that edits `data/corpora.yaml` or `data/papers.yaml`, runs `python scripts/build_readme.py` and commits the regenerated `README.md`, `modalities/` pages and `data/` exports. [CONTRIBUTING.md](CONTRIBUTING.md) has the inclusion rule, the verification rule, the field reference and the pull-request checklist.

---

_Generated on 2026-10-25 by `python scripts/build_readme.py` from `data/corpora.yaml` and `data/papers.yaml`. Do not edit README.md, the `modalities/` pages or the `data/*.json` and `data/*.csv` exports by hand: edit the YAML files and re-run the command._
