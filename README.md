# awesome-automotive-nlp

A curated list of corpora for natural language processing on automotive text, speech and driving scenes: vehicle adverts and listings, reviews and complaints, repair manuals and parts catalogues, in-car dialogue, driving-scene language and the knowledge resources that tie them together. The list grew out of three Auto Trader UK advertisement corpora (AutoSpecNER, Auto-AdvER and Auto-Features), whose related-work sections showed how scattered the field's datasets are. Every row carries task, modality, language, size, licence, access and year tags, and says which of our papers cites it. A corpus is listed if it is freely downloadable or described in a public paper (in which case the row says *paper only* and readers can contact the authors); fee-based commercial catalogues are excluded. See [Contributing](#contributing) to add one.

**131 corpora** (55 text, 40 multimodal, 15 tabular+text, 11 speech, 10 image) in 14 languages.

**Languages:** English 90 · Chinese 12 · Korean 5 · Japanese 4 · Multilingual 3 · Cantonese 2 · German 2 · Italian 2 · Chinese (Simplified and Traditional) 1 · Chinese (Taiwan Mandarin) 1 · Czech 1 · French 1 · Indonesian 1 · Romanian 1 · n/a (images) 10 · n/a (noise recordings) 2 · unknown 1

## Contents

- [Our corpora](#our-corpora) (3)
- [Corpora by application area](#corpora-by-application-area)
  - [A. Vehicle identification & specifications](#a-vehicle-identification--specifications) (13)
  - [B. Listings, adverts & claims](#b-listings-adverts--claims) (4)
  - [C. Features, attributes & catalogue linking](#c-features-attributes--catalogue-linking) (1)
  - [D. Reviews, opinion & sentiment](#d-reviews-opinion--sentiment) (20)
  - [E. Complaints, safety, recalls & incidents](#e-complaints-safety-recalls--incidents) (12)
  - [F. Maintenance, repair, parts & technical documents](#f-maintenance-repair-parts--technical-documents) (12)
  - [G. In-car voice assistants & dialogue](#g-in-car-voice-assistants--dialogue) (25)
  - [H. Driving-scene language & multimodal](#h-driving-scene-language--multimodal) (32)
  - [I. Search, queries & semantic parsing](#i-search-queries--semantic-parsing) (1)
  - [J. Market, pricing & listing tables with text](#j-market-pricing--listing-tables-with-text) (0)
  - [K. Knowledge graphs, ontologies & lexicons](#k-knowledge-graphs-ontologies--lexicons) (11)
- [Related papers (no public data)](#related-papers-no-public-data) (2)
- [Taxonomy](#taxonomy)
- [How to cite](#how-to-cite)
- [Contributing](#contributing)

## Our corpora

The Auto Trader UK advertisement corpora this list grew out of. They are also listed under their application areas below.

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| AutoSpecNER | NER | text | English | 659 vehicle adverts; 15 entity types; 4,609 entity spans (public release); 100-document 3-annotator IAA study | CC BY 4.0 | open | 2026 | [data](https://github.com/FilipposVentirozos/AutoSpecNER) · [paper](https://aclanthology.org/2026.icnlsp-1.8/) | — |
| Auto-AdvER | span labelling | text | English | 605 UK car adverts; 104,382 tokens; 3 span labels (Condition / Historic / Sales Options); 113-advert 3-annotator IAA subset; 3 cross-validation folds | CC BY 4.0 | open | 2026 | [data](https://github.com/FilipposVentirozos/Auto-AdvER) · [paper](https://arxiv.org/abs/2412.05655) | AutoSpecNER, Auto-Features |
| Auto-Features | feature-conditioned NER; entity linking | text | English | 1,256 UK car adverts (430 human-gold + 925 LLM-silver, 99 overlap); 188,980 (advert, feature) instances per fold | to be announced at release | forthcoming | 2026 | forthcoming (release pending) | — |

## Corpora by application area

### A. Vehicle identification & specifications

#### Text: vehicle-domain NER

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| AutoSpecNER | NER | text | English | 659 vehicle adverts; 15 entity types; 4,609 entity spans (public release); 100-document 3-annotator IAA study | CC BY 4.0 | open | 2026 | [data](https://github.com/FilipposVentirozos/AutoSpecNER) · [paper](https://aclanthology.org/2026.icnlsp-1.8/) | — |
| EWNERTC (automotive subset) | fine-grained NER | text | English | EWNERTC: \~7 million automatically annotated Wikipedia sentences in 49 domains; the 'automotive' domain subset has 10,349 sentences (paper Table, row 12); entity types capped at the top 50 per domain for the experiments | CC BY 4.0 | open | 2020 | [data](https://data.mendeley.com/datasets/cdcztymf4k/1) · [paper](https://aclanthology.org/2020.coling-main.334) | Auto-AdvER |
| FindVehicle | NER (text side of natural-language vehicle retrieval; VehicleFinder is a keyword-based cross-modal retrieval system) | text | English | 42.3k labelled natural-language descriptions of vehicle tracks (arXiv abstract); released as FindVehicle_train/test in CoNLL-style .txt and .jsonl (NER + relation labels), hosted on Google Drive / Baidu Cloud Disk | unknown | open | 2024 | [data](https://github.com/GuanRunwei/FindVehicle) · [paper](https://doi.org/10.1007/s11042-023-16373-y) | AutoSpecNER, Auto-AdvER, Auto-Features |

#### Images: make, model and type recognition

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| BoxCars116k | image classification (fine-grained, traffic surveillance) + verification | image | n/a (images) | \~116k images grouped into tracks (one vehicle ID per track) | research only | open | 2018 | [data](https://github.com/JakubSochor/BoxCars) | — |
| Car Connection Picture Dataset | image classification / attribute prediction (filename-encoded specs) | image | n/a (images) | \~60,000 exterior images (scraper collects \~297,000 pictures / \~198,000 unique URLs) | unknown | open | — | [data](https://github.com/nicolas-gervais/predicting-car-price-from-scraped-data/tree/master/picture-scraper) | — |
| Car Models 3778 | image classification (model variants) + attribute metadata | image | n/a (images) | \~193k images (512x512); 3,778 model variants; 44-column metadata CSV; 7.58 GB | other | open | — | [data](https://huggingface.co/datasets/Unit293/car_models_3887) | — |
| CompCars | image classification + attribute prediction + car-model verification | image | n/a (images) | 163 makes, 1,716 models, 136,726 whole-car images + 27,618 part images (web); 50,000 surveillance images | non-commercial research only | on request | 2015 | [data](https://mmlab.ie.cuhk.edu.hk/datasets/comp_cars/index.html) | — |
| Stanford Cars | image classification (fine-grained make/model/year) | image | n/a (images) | 16,185 images, 196 classes (8,144 train / 8,041 test) | unknown | open | 2013 | [data](https://www.tensorflow.org/datasets/catalog/cars196) | — |
| VMMRdb | image classification (make-model-year) | image | n/a (images) | 291,752 images, 9,170 classes (model years 1950-2016) | MIT | open | 2017 | [data](https://github.com/faezetta/VMMRdb) | — |

#### Images: re-identification and damage

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| CarDD | damage detection / segmentation (image) | image | n/a (images) | 4,000 high-resolution images; >9,000 instances; 6 damage categories | unknown | on request | 2023 | [data](https://cardd-ustc.github.io/) | — |
| PKU VehicleID | re-identification (+ vehicle-model labels on subset) | image | n/a (images) | 26,267 vehicles / 221,763 images; model labels for 10,319 vehicles (90,196 images) | academic use only | on request | 2016 | [data](https://www.pkuml.org/resources/pku-vehicleid.html) | — |
| VeRi-776 | re-identification | image | n/a (images) | >50,000 images of 776 vehicles; 20 cameras; 1.0 km^2; 24 h | non-commercial use only | on request | 2016 | [data](https://vehiclereid.github.io/VeRi/) | — |
| VERI-Wild | re-identification | image | n/a (images) | 416,314 images of 40,671 vehicles; 174 cameras; 1 month | non-commercial | on request | 2019 | [data](https://github.com/PKU-IMRE/VERI-Wild) | — |

### B. Listings, adverts & claims

#### Listings and adverts

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| Auto-AdvER | span labelling | text | English | 605 UK car adverts; 104,382 tokens; 3 span labels (Condition / Historic / Sales Options); 113-advert 3-annotator IAA subset; 3 cross-validation folds | CC BY 4.0 | open | 2026 | [data](https://github.com/FilipposVentirozos/Auto-AdvER) · [paper](https://arxiv.org/abs/2412.05655) | AutoSpecNER, Auto-Features |
| Craigslist Used Cars | price table with free-text listing description | tabular+text | English | \~426,000 rows x 26 columns incl. free-text 'description' (row count per derivative HF card Yoad22/craigslist-used-cars-eda; Kaggle page: 275 MB zip) | CC0: Public Domain | open | 2021 | [data](https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data) | — |
| DVM-CAR | listing corpus (tables + images); image classification / price prediction | multimodal | English | 1,451,784 images; 899 UK-market car models; >0.25 million used-car adverts; Basic/Sales/Price/Trim/Ad/Image tables | CC BY-NC 4.0 | open | 2021 | [data](https://deepvisualmarketing.github.io/) · [paper](https://arxiv.org/abs/2109.00881) | — |

#### Buyer-seller dialogue

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| CraigslistBargain | dialogue (buyer-seller price negotiation over marketplace listings) | text | English | more than 6K negotiation dialogues (5,247 train / 597 validation / 838 test) over six categories, one of which is cars | unknown | open | 2018 | [data](https://huggingface.co/datasets/stanfordnlp/craigslist_bargains) · [paper](https://aclanthology.org/D18-1256/) | — |

### C. Features, attributes & catalogue linking

*No public automotive-specific attribute-extraction or catalogue-linking corpus was found. Auto-Features (forthcoming, under Our corpora) is built for this task; the general product-attribute sets MAVE, OA-Mine and AE-110K contain no automotive category.*

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| Auto-Features | feature-conditioned NER; entity linking | text | English | 1,256 UK car adverts (430 human-gold + 925 LLM-silver, 99 overlap); 188,980 (advert, feature) instances per fold | to be announced at release | forthcoming | 2026 | forthcoming (release pending) | — |

### D. Reviews, opinion & sentiment

#### Consumer and expert reviews

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| Amazon Review Data (2018) - Automotive category | sentiment | text | English | Automotive: 7,990,166 reviews (ratings-only 7,990,166), 932,019 product metadata records, 5-core subset 1,711,519 reviews (whole dataset 233.1 million reviews) | unknown | open | 2018 | [data](https://nijianmo.github.io/amazon/index.html) | — |
| Amazon Reviews 2023 - Automotive category | sentiment | text | English | Automotive: 8.0M users, 2.0M items, 20.0M ratings/reviews, 824.9M review tokens, 1.7B metadata tokens (whole dataset 571.54M reviews) | unknown | open | 2023 | [data](https://amazon-reviews-2023.github.io/) | — |
| Car Reviews (Hugging Face) | sentiment | text | English | 36,984 rows, 8 columns, 24.3 MB CSV; review dates 2003-2018 visible | unknown | open | — | [data](https://huggingface.co/datasets/florentgbelidji/car-reviews) | — |
| Edmunds Car Reviews (Kaggle) | sentiment | text | English | not stated on page (Review.csv; one row per review with Company, Model, Year, Reviewer, Date, Title, Review, Rating) | CC BY-SA 4.0 | open | 2021 | [data](https://www.kaggle.com/datasets/shreemunpranav/edmunds-car-review) | — |
| Electric Vehicles User Reviews India (Kaggle) | sentiment | text | English | not stated on page (multiple CSVs, one per site/vehicle type) | CC0: Public Domain | open | 2022 | [data](https://www.kaggle.com/datasets/deadprstkrish/ev-cars-user-reviews-india) | — |
| Expert Car Reviews Dataset (Kaggle) | summarisation | tabular+text | English | not stated on page | Other | open | 2024 | [data](https://www.kaggle.com/datasets/ademboukhris/expert-car-reviews-dataset) | — |
| OpinRank Review Dataset (Edmunds car reviews) | sentiment | text | English | \~42,230 car reviews (model years 2007, 2008, 2009) + \~259,000 hotel reviews | CC BY 4.0 | open | 2011 | [data](https://archive.ics.uci.edu/dataset/205/opinrank+review+dataset) | — |
| SRNI-CAR (Chinese automotive market dataset) - owner reviews component | sentiment | tabular+text | Chinese | 217,292 owner comments from 358 cities covering 13,039 models / 672 series / 127 brands; Reviews CSV 480 MB | CC BY-NC 4.0 | open | 2023 | [data](https://srni-car.github.io) · [paper](https://arxiv.org/abs/2401.05395) | — |
| Yelp Open Dataset (Automotive category businesses) | sentiment | text | English | whole dataset: 6,990,280 reviews, 150,346 businesses, 11 metropolitan areas; JSON tar 4.35 GB compressed / 8.65 GB uncompressed (Automotive subset not broken out) | intended for educational use | open | 2013 | [data](https://business.yelp.com/data/resources/open-dataset/) | — |

#### Sentiment and aspect-based gold standards

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| ALSA (Aspect-Level Sentiment Analysis in Automotive Domain) | ABSA | text | English, Korean | 58,000+ comment-aspect pairs | research use only | on request | 2020 | [data](https://github.com/dmhyun/ALSAdata) · [paper](https://aclanthology.org/2020.coling-main.83/) | — |
| CCF BDCI 2018 Automotive User Opinion Topic and Sentiment Recognition | ABSA | text | Chinese | training set + test set (counts not stated on fetched pages; community write-ups report \~9.9k training sentences) | unknown | on request | 2018 | [data](https://www.datafountain.cn/competitions/310) | — |
| Chinese car review sentiment dataset (Liu et al. 2022, ATWWM-BERT) | sentiment | text | Chinese | 9,947 reviews (3,670 positive / 3,661 neutral / 2,616 negative) per paper body; abstract page does not state size | unknown | paper only | 2022 | paper only · [paper](https://arxiv.org/abs/2206.02389) | — |
| IndoNLU CASA (Indonesian car review ABSA) | ABSA | text | Indonesian | 1,080 reviews (train 810 / valid 90 / test 180) | MIT | open | 2018 | [data](https://huggingface.co/datasets/indonlp/indonlu) | — |
| InfoBarometer (German automotive industry explainable sentiment) | sentiment | text | German | 1,039 news articles (per paper; not stated on the Anthology abstract page) | unknown | paper only | 2023 | paper only · [paper](https://aclanthology.org/2023.wassa-1.13/) | — |
| JDPA Sentiment Corpus for the Automotive Domain | ABSA | text | English | 515 documents (blog posts), 19,322 sentences, 330,762 tokens (automobiles + cameras) | (c) Copyright 2009-2010, J.D. Power… | on request | 2010 | [data](https://verbs.colorado.edu/jdpacorpus/README.txt) | — |
| PACE Corpus (Polarity-annotated Automotive and CEllphone) | ABSA | text | English, German | 1,000 forum posts per language (2,000 total), each annotated by at least four annotators | unknown | paper only | 2014 | paper only · [paper](https://aclanthology.org/L14-1240/) | — |

#### Social and video media

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| Automotive brand's products - Twitter dataset (Mendeley Data) | sentiment | text | unknown | not stated on page | CC BY 4.0 | open | — | [data](https://data.mendeley.com/datasets/hcc2h426h3/1) | — |
| MuSe-CaR (Multimodal Sentiment Analysis in Car Reviews) | sentiment | multimodal | English | over 40 hours of user-generated video material; more than 350 reviews; 70 host speakers and 20 overdubbed narrators | EULA, academic use only | on request | 2021 | [data](https://www.muse-challenge.org) · [paper](https://arxiv.org/abs/2101.06053) | — |
| SenTube (SenTube-A automobiles subset) | sentiment | text | English, Italian | SenTube-A automobile subset: 3,381 train / 225 dev / 903 test comments (per Barnes et al. 2017); full corpus counts not stated on the Anthology page | unknown | paper only | 2014 | paper only · [paper](https://aclanthology.org/L14-1188/) | — |
| YouTube AV 50K | sentiment | text | English | more than 50,000 YouTube comments plus metadata | unknown | paper only | 2018 | paper only · [paper](https://arxiv.org/abs/1807.11227) | — |

### E. Complaints, safety, recalls & incidents

#### NHTSA defects, recalls and investigations (US)

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| NHTSA Customer Complaints (Kaggle) | text classification | tabular+text | English | not stated on page (version 2509 at fetch time, i.e. daily versions); complaints from 2016 onwards | CC0: Public Domain | open | 2026 | [data](https://www.kaggle.com/datasets/alshival/nhtsa-complaints) | — |
| NHTSA Defect Investigations (flat file) | text classification | tabular+text | English | all NHTSA safety-related defect investigations opened since 1972 (11 fields; count not stated) | unknown | open | 1972 | [data](https://static.nhtsa.gov/odi/ffdd/inv/INV.txt) | — |
| NHTSA Manufacturer Communications / Technical Service Bulletins (flat file) | text classification | tabular+text | English | all manufacturer communications received by NHTSA since January 1, 1995, in 5-year chunks (14 fields; count not stated) | unknown | open | 1995 | [data](https://static.nhtsa.gov/odi/ffdd/tsbs/TSBS.txt) | — |
| NHTSA ODI Complaints (flat file) | text classification | tabular+text | English | all safety-related defect complaints received by NHTSA since January 1, 1995 (count not stated in dictionary; 2.2M total complaints per MORVS HF card; 51 fields) | unknown | open | 1995 | [data](https://static.nhtsa.gov/odi/ffdd/cmpl/CMPL.txt) | — |
| NHTSA ODI complaints - high-signal subset (Hugging Face) | text classification | tabular+text | English | 213,093 records out of 2.2M total complaints | federal-works-and-cc0-card-metadata | open | — | [data](https://huggingface.co/datasets/emperor-mew/nhtsa-complaints) | — |
| NHTSA Recalls (flat file) | text classification | tabular+text | English | all NHTSA safety-related defect and compliance campaigns since 1967 (29 fields; count not stated in dictionary) | unknown | open | 1967 | [data](https://static.nhtsa.gov/odi/ffdd/rcl/RCL.txt) | — |

#### Recalls in other jurisdictions

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| DVSA Vehicle Recalls File (UK) | text classification | tabular+text | English | all UK recalls since 1992, CSV \~5MB | Open Government Licence v3.0 | open | 1992 | [data](https://www.check-vehicle-recalls.service.gov.uk/) | — |
| Transport Canada Vehicle Recalls Database | text classification | tabular+text | English, French | full database refreshed monthly (CSV/XML); count not stated on page | Open Government Licence - Canada | open | — | [data](https://open.canada.ca/data/en/dataset/1ec92326-47ef-4110-b7ca-959fab03f96d) | — |

#### Crash and automated-driving incident narratives

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| California DMV Autonomous Vehicle Disengagement Reports | text classification | tabular+text | English | annual CSVs 2020-2024 (standard, first-time filers, driverless); 2024 file \~634k characters of text, hundreds of rows per large filer; older years by request (AVarchive@dmv.ca.gov) | unknown | open | 2015 | [data](https://www.dmv.ca.gov/portal/file/2024-autonomous-vehicle-disengagement-reports-csv/) | — |
| Iowa DOT crash report narratives (as used in Bhagat et al. 2025) | text classification | text | English | 173,512 crash records and 94,367 crash narrative records (2019-2020) | unknown | paper only | 2025 | paper only · [paper](https://arxiv.org/abs/2504.13068) | — |
| NHTSA Standing General Order 2021-01 Crash Reports (ADS and Level 2 ADAS) | text classification | tabular+text | English | monthly CSV releases since June 2021, separate ADS and ADAS files; data dictionary 33 pages; latest change-log entry 10/15/2026 (reports received through September 15, 2026); row counts not stated in dictionary | unknown | open | 2021 | [data](https://static.nhtsa.gov/odi/ffdd/sgo-2021-01/SGO-2021-01_Data_Element_Definitions.pdf) | — |
| NMVCCS - National Motor Vehicle Crash Causation Survey | text classification | multimodal | English | 6,949 investigated crashes Jan 2005 - Dec 2007 (5,470 nationally representative + 1,479 clinical cases) per NHTSA report DOT HS 811 059; data.gov page gives no count | unknown | open | 2008 | [data](https://catalog.data.gov/dataset/national-motor-vehicle-crash-causation-survey-nmvccs-nmvccs-xml-case-viewer) | — |

### F. Maintenance, repair, parts & technical documents

#### Manuals, FAQs & question answering

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| ADMit automotive NER data | NER (domain-adversarial multi-task training) | text | Korean, English | unknown (not stated in the citing papers) | unknown | paper only | 2023 | paper only · [paper](https://doi.org/10.1016/j.eswa.2023.120007) | AutoSpecNER, Auto-AdvER |
| DelucionQA | QA / hallucination detection (RAG over car manual) | text | English | 913 unique questions; 2,038 question-context-answer triples (513/100/300 train/dev/test questions + 240 excluded) | CC BY 4.0 | open | 2023 | [data](https://github.com/boschresearch/DelucionQA) · [paper](https://aclanthology.org/2023.findings-emnlp.59.pdf) | — |
| FETA car manuals benchmark | text-to-image / image-to-text retrieval over manuals | multimodal | English | not stated (archive \~7 GB incl. IKEA part) | apache-2.0 | open | 2022 | [data](https://huggingface.co/datasets/alfassy/FETA_IKEA_CAR_MANUALS) · [paper](https://arxiv.org/abs/2209.03648) | — |
| MaQA (Manual Question Answering) | QA / FAQ classification from car manual | text | Korean, English | 45,641 questions in each of Korean and English; 1,526 FAQ categories | unknown | paper only | 2024 | paper only · [paper](https://doi.org/10.3390/electronics13244972) | — |

#### Faults, repair and parts

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| Automotive_Industry_Fault_Data_Set | relation / triple extraction (instruction format) | text | Chinese | 1,441 instruction records (spo_0.json, 1.33 MB) | apache-2.0 | open | 2023 | [data](https://huggingface.co/datasets/zhengr/Automotive_Industry_Fault_Data_Set) | — |
| Chinese automobile fault text NER datasets (Entropy 2025) | NER | text | Chinese | three datasets: D1 \~4.5k, D2 \~5.5k, D3 \~4.0k sentences (train/test/dev splits) | unknown | on request | 2025 | [paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC11854445/) | — |
| Chinese vehicle fault repair case NER (Electronics 2025) | NER (incl. discontinuous/nested entities) | text | Chinese | not stated in abstract | unknown | paper only | 2025 | paper only · [paper](https://doi.org/10.3390/electronics14071361) | — |
| Chinese Vehicle Fleet Fault Association Dataset (Hangzhou Normal University) | NER + KG triples over repair/maintenance records | tabular+text | Chinese | not stated (files: fault_events.csv 33 fields, vehicle_fleet.csv 20 fields, ner_annotations.csv with 6 entity types, knowledge_graph_triples.csv) | CC BY 4.0 | open | 2026 | [data](https://data.mendeley.com/datasets/r98g7g6k5t/1) | — |
| Free-text customer failure reports for automated vehicle diagnostics (Khodadadi et al. 2021) | text classification / IE on service-call failure reports | text | English | not stated | unknown | paper only | 2021 | paper only · [paper](https://arxiv.org/abs/2111.14977) | — |
| Named Entity Recognition of Automotive Parts Based on RoBERTa-CRF Model (Hu and Ma) | NER | text | Chinese | unknown | unknown | paper only | 2024 | paper only · [paper](https://doi.org/10.1109/NNICE61279.2024.10499162) | AutoSpecNER, Auto-AdvER, Auto-Features |

#### Requirements, standards and patents

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| Automotive ISO 26262 Safety Requirements Dataset | text classification (ASIL rating) / generation | text | English | \~1,000 samples | MIT | open | — | [data](https://huggingface.co/datasets/Muhammmadd/iso26262-automotive-safety-requirements) | — |
| Harvard USPTO Patent Dataset (HUPD) - CPC B60 (vehicles) filterable | patent corpus (classification, LM, summarisation); automotive via CPC filter | text | English | full corpus 2004-2018 (abstract reports >4.5M documents); B60 subset size not stated | cc-by-sa-4.0 | open | 2022 | [data](https://huggingface.co/datasets/HUPD/hupd) · [paper](https://arxiv.org/abs/2207.04043) | — |

### G. In-car voice assistants & dialogue

#### Task-oriented dialogue and tool use

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| AMIE in-cabin passenger-agent dialogue dataset | SLU/intent+slot | multimodal | English | 1331 utterances with commands to the AMIE agent (per paper; not on abstract page) | unknown | paper only | 2019 | paper only · [paper](https://arxiv.org/abs/1904.10500) | — |
| CAR-bench | dialogue (task-oriented) | text | English | 254 tasks (Base 100 / Hallucination 98 / Disambiguation 56; README elsewhere says 248); 58 tools (27 set, 29 get, 2 no-op) | MIT | open | 2026 | [data](https://github.com/CAR-bench/car-bench) · [paper](https://arxiv.org/abs/2601.22027) | — |
| CarMem | dialogue (task-oriented) | text | English | per paper: 1,000 extraction conversations, 1,000 retrieval utterances, 3,000 maintenance utterances (not on fetched pages) | unknown | open | 2025 | [data](https://github.com/johanneskirmayr/CarMem) · [paper](https://aclanthology.org/2025.coling-industry.29/) | — |
| In-Vehicle-Tool-Calls | semantic parsing / NL-to-query | text | English | 43,087 rows + 65 held-out novel-tool rows; 25 intents, 6 domains, 30 tool schemas | other | open | 2026 | [data](https://huggingface.co/datasets/Senthi1Kumar/In-Vehicle-Tool-Calls-v0.2) | — |
| KVRET (Stanford In-Car Assistant dataset) | dialogue (task-oriented) | text | English | 3,031 multi-turn dialogues (train 2,424 / validation 302 / test 304) | unknown | open | 2017 | [data](https://huggingface.co/datasets/ConvLab/kvret) · [paper](https://arxiv.org/abs/1705.05414) | — |
| LoCar | dialogue (task-oriented) | text | Korean | not stated on abstract page | unknown | paper only | 2026 | paper only · [paper](https://arxiv.org/abs/2605.21086) | — |

#### Spoken commands and language understanding

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| in_car_commands (Korean in-car voice commands) | ASR | speech | Korean | 72,000 rows (train 57.6k / valid 7.2k / test 7.2k), 12.8 GB, clips 0.15-12.7 s | apache-2.0 | open | — | [data](https://huggingface.co/datasets/Angeriod/in_car_commands_60) | — |
| MAC-SLU | SLU/intent+slot | text | Chinese | 20.5k rows (train 18k / validation 1.39k / test 1.15k); 8 domains, 81 intents, 192 slots (paper); up to 5 intents per query | apache-2.0 | open | 2025 | [data](https://huggingface.co/datasets/Gatsby1984/MAC_SLU) · [paper](https://arxiv.org/abs/2512.01603) | — |

#### Assistant evaluation

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| CarExpert factual-correctness evaluation dataset (Giebisch et al. 2025) | QA | text | English | not stated on abstract page | unknown | paper only | 2025 | paper only · [paper](https://arxiv.org/abs/2504.01248) | — |
| In-car contextual-understanding benchmark (Habicht et al. 2025) | text classification | text | English | not stated on abstract page | unknown | paper only | 2025 | paper only · [paper](https://arxiv.org/abs/2512.12042) | — |
| InCarEmo | text classification | multimodal | Chinese | not stated on abstract page (search snippet: \~2,000 generated multi-turn driver-assistant dialogue scripts) | unknown | paper only | 2026 | paper only · [paper](https://arxiv.org/abs/2607.14683) | — |
| Vehicle Voice Command Authorization safety benchmark (Afroze et al. 2026) | text classification | text | English | 202 scenarios with reference decisions under a seven-class taxonomy (161 non-execution) | unknown | paper only | 2026 | paper only · [paper](https://arxiv.org/abs/2609.19630) | — |

#### In-car speech recognition

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| AISHELL-5 | ASR | speech | Chinese | >100 hours multi-channel speech (train 54 GB, Dev 1.9 GB, Eval1 1.7 GB, Eval2 1.8 GB) + 40 hours in-car noise (13 GB); 60+ driving scenarios | CC BY-SA 4.0 | open | 2025 | [data](https://openslr.org/159/) · [paper](https://arxiv.org/abs/2505.23036) | — |
| AVICAR | ASR | speech | English | 100 speakers (50 male, 50 female); \~59,000 utterances; 8 mics + 4 cameras; 5 noise conditions | unknown | paper only | 2004 | paper only · [paper](https://www.isca-archive.org/interspeech_2004/lee04m_interspeech.html) | — |
| CENSREC-2 | ASR | speech | Japanese | 14,687 utterances (7,492 close-talk, 7,195 remote); 4 in-car environments x vehicle speeds; 1 DVD | For research and development purposes… | on request | 2005 | [data](https://research.nii.ac.jp/src/en/CENSREC-2.html) | — |
| CENSREC-3 | ASR | speech | Japanese | 293 speakers (202 m / 91 f); 14,050 utterances per microphone; 50 words; 16 conditions (3 speeds x 6 in-car environments); 1 DVD | For research and development purposes… | on request | 2006 | [data](https://research.nii.ac.jp/src/en/CENSREC-3.html) | — |
| CI-AVSR | ASR | multimodal | Cantonese | 4,984 samples (8.3 hours) of 200 in-car commands from 30 native Cantonese speakers; augmented set 10x larger | CC0-1.0 | open | 2022 | [data](https://github.com/HLTCHKUST/CI-AVSR) · [paper](https://arxiv.org/abs/2201.03804) | — |
| CIAIR In-Car Speech Database | dialogue (task-oriented) | multimodal | Japanese | \~800 subjects, \~60-minute drive each (per IEICE 2005 abstract via search); 16 microphones, 3 cameras | unknown | paper only | 2004 | paper only · [paper](https://www.isca-archive.org/interspeech_2004/kawaguchi04_interspeech.html) | — |
| CU-Move | ASR | speech | English | target +1000 speakers across the US (Eurospeech 2001); \~500 speakers recorded in 2001 per later chapter; 14 noise conditions across 6 vehicles; 5-mic array | unknown | on request | 2001 | [data](https://utdrive.utdallas.edu/corpus) · [paper](https://www.isca-archive.org/eurospeech_2001/hansen01b_eurospeech.html) | — |
| Guangzhou Cantonese Scripted Speech Corpus in the Vehicle | ASR | speech | Cantonese | 5 hours; 6,219 utterances; 10 speakers | CC BY-NC-ND 4.0 | open | — | [data](https://huggingface.co/datasets/AlienKevin/guangzhou-cabin-speech) | — |
| STAZKA - Speech recordings from vehicles | ASR | speech | Czech | 26 speakers for the scripted prompts; hours not stated; files full_noises.zip + prompts (Transcriber .trs transcripts) | Creative Commons - Attribution-NonComme… | open | 2015 | [data](https://b2find.eudat.eu/dataset/9d65f782-5271-5cb9-afd0-5c0f28667403) | — |
| TAICAR | ASR | speech | Chinese (Taiwan Mandarin) | preliminary corpus from 192 speakers; more than 163,000 files, 16.8 GB | unknown | paper only | 2005 | paper only · [paper](https://aclanthology.org/O05-3005/) | — |
| UTDrive | ASR | multimodal | English | 37 female + 40 male drivers (at time of page); Toyota RAV4; Release 3.0 (Aug 2020) | unknown | open | 2007 | [data](https://utdrive.utdallas.edu/corpus) | — |

#### Cabin acoustics and noise

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| ASR-CabNois (MagicHub in-vehicle noise dataset) | ASR | speech | n/a (noise recordings) | 5.08 hours of in-vehicle noise (seven noise pieces); WAV PCM 44.1 kHz 16-bit stereo | Magic Data open-source license / CC… | open | — | [data](https://magichub.com/datasets/in-vehicle-noise-dataset/) | — |
| CAVEMOVE | ASR | speech | n/a (noise recordings) | multichannel recordings in four cars across static and in-motion conditions; cavemove_dataset.zip 7.6 GB (v4, 2025-10-21) + Python API | Creative Commons Attribution 4.0… | open | 2025 | [data](https://zenodo.org/doi/10.5281/zenodo.13594242) · [paper](https://arxiv.org/abs/2508.19691) | — |

### H. Driving-scene language & multimodal

*For papers and models on language in autonomous driving, see [Awesome-LLM4AD](https://github.com/Thinklab-SJTU/Awesome-LLM4AD), which this section complements; it lists corpora only.*

#### Grounding, referring expressions and retrieval

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| CityFlow-NL | retrieval (NL-based vehicle track retrieval) / grounding | multimodal | English | 2,155 training tracks x 3 NL descriptions; 184 test tracks / 184 test queries (2023 release) | repo Apache-2.0 | open | 2021 | [data](https://github.com/fredfung007/cityflow-nl) · [paper](https://arxiv.org/abs/2101.04741) | — |
| HAD | grounding/referring expression (advice grounding) + captioning | multimodal | English | \~30 hours of driving video with natural-language advice | non-commercial use only | on request | 2019 | [data](https://usa.honda-ri.com/HAD) · [paper](https://openaccess.thecvf.com/content_CVPR_2019/papers/Kim_Grounding_Human-To-Vehicle_Advice_for_Self-Driving_Vehicles_CVPR_2019_paper.pdf) | — |
| NuPrompt | grounding/referring expression (prompt-based 3D multi-object tracking) | multimodal | English | 40,147 language prompts for 3D objects | repo Apache-2.0 | open | 2023 | [data](https://github.com/wudongming97/Prompt4Driving) · [paper](https://arxiv.org/abs/2309.04379) | — |
| Refer-KITTI | grounding/referring expression (referring multi-object tracking) | multimodal | English | 18 videos, 818 expressions, avg 10.7 objects per expression | unknown | open | 2023 | [data](https://referringmot.github.io/) · [paper](https://arxiv.org/abs/2303.03366) | — |
| Talk2Car | grounding/referring expression | multimodal | English | 11,959 commands (8,349 train / 1,163 val / 2,447 test) | unknown | open | 2019 | [data](https://talk2car.github.io/) · [paper](https://arxiv.org/abs/1909.10838) | — |

#### Scene question answering and instruction tuning

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| MAPLM | VQA (map and traffic-scene understanding) | multimodal | English | not stated on fetched page | repo MIT | open | 2023 | [data](https://github.com/LLVM-AD/MAPLM) · [paper](https://openaccess.thecvf.com/content/CVPR2024/papers/Cao_MAPLM_A_Real-World_Large-Scale_Vision-Language_Benchmark_for_Map_and_Traffic_CVPR_2024_paper.pdf) | — |
| NuInstruct | VQA (instruction; 17 subtasks: perception, prediction, risk, planning with reasoning) | multimodal | English | 91K multi-view video-QA pairs across 17 subtasks | unknown | open | 2024 | [data](https://github.com/xmed-lab/NuInstruct) · [paper](https://arxiv.org/abs/2401.00988) | — |
| NuScenes-MQA | VQA + captioning (Markup-QA) | multimodal | English | not stated on fetched page | repo Apache-2.0 | open | 2023 | [data](https://github.com/turingmotors/NuScenes-MQA) · [paper](https://arxiv.org/abs/2312.06352) | — |
| NuScenes-QA | VQA | multimodal | English | 460K QA pairs over 34K visual scenes (arXiv abstract) | repo MIT | open | 2023 | [data](https://github.com/qiantianwen/NuScenes-QA) · [paper](https://arxiv.org/abs/2305.14836) | — |
| OmniDrive-nuScenes | VQA (reasoning, planning, counterfactual) | multimodal | English | not stated on fetched pages | unknown | open | 2024 | [data](https://github.com/NVlabs/OmniDrive) · [paper](https://arxiv.org/abs/2405.01533) | — |
| SURDS | VQA (spatial understanding and reasoning) | multimodal | English | not stated on fetched page | academic use only | open | 2024 | [data](https://github.com/XiandaGuo/Drive-MLLM) | — |
| Talk2BEV | VQA (spatial reasoning over BEV maps) | multimodal | English | 1,000 human-annotated BEV scenarios; >20,000 questions | unknown | open | 2023 | [data](https://llmbev.github.io/talk2bev/) · [paper](https://arxiv.org/abs/2310.02251) | — |

#### Explanations, captions and risk narration

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| BDD-OIA | text classification (action + explanation labels) | multimodal | English | not stated on fetched page | unknown | open | 2020 | [data](https://github.com/Twizwei/bddoia_project) | — |
| BDD-X | captioning (action description + justification) | multimodal | English | 6,970 videos, \~77 hours, >26K activities, >8.4M frames (5,597/717/656 split) | unknown | open | 2018 | [data](https://github.com/JinkyuKimUCB/BDD-X-dataset) · [paper](https://openaccess.thecvf.com/content_ECCV_2018/papers/Jinkyu_Kim_Textual_Explanations_for_ECCV_2018_paper.pdf) | — |
| CoVLA | captioning (vision-language-action: captions + trajectories) | multimodal | English | >80 hours of real-world driving video | released for academic use | open | 2024 | [data](https://turingmotors.github.io/covla-ad/) · [paper](https://arxiv.org/abs/2408.10845) | — |
| DRAMA | captioning + grounding (risk localisation) + VQA | multimodal | English | 17,785 two-second clips (17,066 risk scenarios); 306,708 caption tokens, 992 unique words | non-commercial use only | on request | 2023 | [data](https://usa.honda-ri.com/drama) · [paper](https://openaccess.thecvf.com/content/WACV2023/papers/Malla_DRAMA_Joint_Risk_Localization_and_Captioning_in_Driving_WACV_2023_paper.pdf) | — |
| DriveGPT4 instruction data | VQA / visual instruction tuning | multimodal | English | not stated on fetched page | unknown | paper only | 2023 | paper only · [paper](https://arxiv.org/abs/2310.01412) | — |
| Rank2Tell | VQA + captioning (importance ranking + reasoning) | multimodal | English | 116 clips of \~20 s at 10 FPS | unknown | on request | 2023 | [data](https://usa.honda-ri.com/rank2tell) · [paper](https://arxiv.org/abs/2309.06597) | — |

#### Reasoning and planning with language

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| DriveBench | VQA (VLM reliability benchmark: MCQ / VQA / captioning over perception, prediction, planning, behavior) | multimodal | English | 19,200 frames; 20,498 QA pairs; 17 input settings | Apache-2.0 | open | 2025 | [data](https://github.com/drive-bench/toolkit) · [paper](https://arxiv.org/abs/2501.04003) | — |
| DriveLM | VQA (graph VQA: perception -> prediction -> planning) | multimodal | English | not stated on fetched pages | language data CC BY-NC-SA 4.0 | open | 2023 | [data](https://github.com/OpenDriveLab/DriveLM) · [paper](https://arxiv.org/abs/2312.14150) | — |
| Driving-with-LLMs | VQA (object-level vector input; action prediction, justification, DrivingQA) | tabular+text | English | \~10k train / 1k test VQA items (from bundled archive names; not stated in prose) | repo Apache-2.0 | open | 2023 | [data](https://github.com/wayveai/Driving-with-LLMs) · [paper](https://arxiv.org/abs/2310.01957) | — |
| LaMPilot | semantic parsing / NL-to-program (instruction following via language-model programs) | text | English | 32 driving scenarios; 4,900 test cases (DbLv1) | MIT | open | 2024 | [data](https://github.com/PurdueDigitalTwin/LaMPilot) | — |
| LingoQA | VQA (video QA) | multimodal | English | 419.9K QA pairs over \~28K clips: Scenery 3.5k videos/267.8k QA; Action 24.5k videos/152.5k QA; eval 100 videos/1,000 QA | unknown | open | 2023 | [data](https://github.com/wayveai/LingoQA) · [paper](https://arxiv.org/abs/2312.14115) | — |
| Reason2Drive | VQA (chain-based reasoning: perception, prediction, reasoning) | multimodal | English | >600K video-text pairs | unknown | open | 2023 | [data](https://github.com/fudan-zvg/Reason2Drive) · [paper](https://arxiv.org/abs/2312.03661) | — |
| V2V-QA | VQA (grounding, notable-object identification, planning; cooperative) | multimodal | English | not stated on fetched page | unknown | open | 2025 | [data](https://eddyhkchiu.github.io/v2vllm.github.io/) · [paper](https://arxiv.org/abs/2502.09980) | — |

#### Traffic rules and driving-test QA

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| DriveCombo | QA + VQA (compositional traffic-rule reasoning, multiple choice) | multimodal | Multilingual | \~70K multiple-choice questions; 5 countries | unknown | paper only | 2026 | paper only · [paper](https://arxiv.org/abs/2603.01637) | — |
| DriveQA | QA + VQA (traffic rules, signs, right-of-way; multiple choice) | multimodal | English | 474K QA pairs: \~26K text-based, \~448K vision-based | unknown | open | 2025 | [data](https://driveqaiccv.github.io/) · [paper](https://arxiv.org/abs/2508.21824) | — |
| DrivingVQA | VQA (driving theory-exam MCQ with explanations and grounded entities) | multimodal | English | 3,931 multiple-choice problems (80/20 split; 789 test) | unknown | open | 2025 | [data](https://vita-epfl.github.io/DrivingVQA/) · [paper](https://arxiv.org/abs/2501.04671) | — |
| IDKB | QA + VQA (driving handbooks, theory tests, simulated road tests) | multimodal | Multilingual | >1 million data items | unknown | paper only | 2024 | paper only · [paper](https://arxiv.org/abs/2409.02914) | — |
| Romanian Driving Laws QA | QA + VQA with explanation generation | multimodal | Romanian | 1,208 questions (387 multimodal) | unknown | paper only | 2025 | paper only · [paper](https://arxiv.org/abs/2509.23715) | — |

#### Roadside traffic-video QA

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| SUTD-TrafficQA | VQA (video QA over traffic events; 6 reasoning tasks) | multimodal | English | 10,080 in-the-wild videos; 62,535 QA pairs | unknown | on request | 2021 | [data](https://github.com/sutdcv/SUTD-TrafficQA) · [paper](https://arxiv.org/abs/2103.15538) | — |
| TUMTraffic-VideoQA | VQA + captioning + grounding (video MCQ, referred-object captioning, spatio-temporal grounding) | multimodal | English | 1,000 videos; 85,000 MCQ pairs; 2,300 object captions; 5,700 grounding annotations | CC BY-NC-SA 4.0 | open | 2025 | [data](https://innovation-mobility.com/en/project-providentia/a9-dataset) · [paper](https://arxiv.org/abs/2502.02449) | — |

### I. Search, queries & semantic parsing

*Spider's car_1 database is the only public automotive slice found. No open corpus maps natural-language car-search queries to structured filters.*

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| Spider (car_1 database) | semantic parsing / NL-to-query (text-to-SQL) | text | English | 10,181 questions, 5,693 unique SQL queries, 200 databases, 138 domains (whole benchmark); car_1 subset size not stated | unknown | open | 2018 | [data](https://yale-lily.github.io/spider) · [paper](https://arxiv.org/abs/1809.08887) | — |

### J. Market, pricing & listing tables with text

*Used-car price and specification tables without free text are not NLP corpora and are not listed. Listing corpora with free text are in section B.*

### K. Knowledge graphs, ontologies & lexicons

#### Standards and schemas

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| COVESA Vehicle Signal Specification (VSS) | KG/ontology (signal taxonomy / data model) | text | English | not stated on README | MPL-2.0 | open | — | [data](https://github.com/COVESA/vehicle_signal_specification) | — |
| schema.org Automotive extension (auto.schema.org) / Car & Vehicle types | KG/ontology (web vocabulary) | text | English | Vehicle/Car types plus \~15 extension properties and 3 enumerations | unknown | open | 2016 | [data](https://schema.org/docs/automotive.html) | — |

#### Make, model and VIN catalogues

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| NHTSA vPIC (Vehicle Product Information Catalog) VIN decoder API & standalone database | VIN decoding / vehicle identification lookup (structured) | text | English | not stated | unknown | open | — | [data](https://vpic.nhtsa.dot.gov/api/) | — |
| us-car-models-data | reference table (US car models by year) | text | English | over 15,000 car models (one CSV per year) | unknown | open | — | [data](https://github.com/AbhiOnlyOne/us-car-models-data) | — |
| vehicle-makes-models | reference table (make -> model -> generation -> engine specs) | text | English | 164 makes, 2,621 models, 7,169 generations, 30,390 engines | ODbL 1.0 | open | — | [data](https://github.com/gor3a/vehicle-makes-models) | — |
| VehicleName - multilingual automotive name database | lexicon / gazetteer (models, brands, terms with cross-market aliases) | text | English, Chinese (Simplified and Traditional), Japanese | 3,030 vehicle models, 164 brands, 72 terms (data v1.2.0) | CC BY-SA 4.0 | open | — | [data](https://github.com/ixiehao/VehicleName) | — |
| vehiclesdb | reference table / gazetteer (make-model catalogue) | text | English | 19,282 models, 933 makes, 6 kinds (page header); v2026.10.3 table: 15,068 models, 934 makes, 18 countries | CC BY 4.0 | open | 2026 | [data](https://github.com/vehiclesdb/vehiclesdb) | — |
| Wikidata 'car model' class (Q3231690) and vehicle subgraph | KG (SPARQL-queryable) | text | Multilingual | not stated (instance count not shown on item page) | unknown | open | — | [data](https://www.wikidata.org/wiki/Q3231690) | — |

#### Glossaries and knowledge graphs

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| Car-identification - Autohome car knowledge graph & QA | KG construction + simple QA (plus image classification) | multimodal | Chinese | text: 284 brands, 2,058 car series; images: 55,945 (155 brands, 900 series) | unknown | open | — | [data](https://github.com/LongxingHu/Car-identification) | — |
| EVKG - Electric Vehicle Knowledge Graph | KG/ontology | text | English | not stated on fetched pages (83 classes / 69 properties reported in search snippet, unverified) | MIT | open | 2023 | [data](https://github.com/EVKG/evkg) · [paper](https://arxiv.org/abs/2304.04893) | — |
| Italian Automotive Glossary | lexicon / glossary (schema.org DefinedTerm) | text | Italian | 212 terms (JSON Lines, \~324 KB) | CC BY 4.0 | open | — | [data](https://huggingface.co/datasets/DealerMax/italian-automotive-glossary) | — |

## Related papers (no public data)

Automotive NLP papers with no public corpus: each describes a system, benchmark or evaluation whose data has not been released. They are listed with the academic reference so that readers can contact the authors.

| Paper | Task | Lang | Year | Link | Cited in |
|---|---|---|---|---|---|
| CarExpert | QA | English | 2023 | [paper](https://aclanthology.org/2023.emnlp-industry.56/) | — |
| DeepTest 2026 LLM Testing Competition: automotive manual assistant benchmark | QA | English | 2026 | [paper](https://arxiv.org/abs/2604.12615) | — |

## Taxonomy

The primary axis is the application area, one section per bucket; larger sections are split into sub-headings. Every bucket is shown, even when empty, and a short note under a section heading explains a gap or points to where related corpora are listed. The secondary axes are the table columns: task, modality (text, speech, multimodal, image, tabular+text), language, size, licence (short form; the full terms are in `data/corpora.yaml`), access, year, links and the paper of ours that cites the row.

- **A. Vehicle identification & specifications**: make/model/trim/engine NER, car-type recognition from text or image, VIN, spec sheets
- **B. Listings, adverts & claims**: classified-ad IE (condition, history, offers), ad generation & verification, listing corpora
- **C. Features, attributes & catalogue linking**: feature-conditioned NER, attribute-value extraction, product/catalogue linking
- **D. Reviews, opinion & sentiment**: car reviews, automotive ABSA, forums, social media opinion
- **E. Complaints, safety, recalls & incidents**: NHTSA/ODI complaints, defect reports, crash narratives, recall text
- **F. Maintenance, repair, parts & technical documents**: auto-parts NER, repair/diagnostic QA, service records, manuals, patents
- **G. In-car voice assistants & dialogue**: in-car task-oriented dialogue, SLU intent/slot, in-vehicle ASR/speech, driver-vehicle interaction
- **H. Driving-scene language & multimodal**: Talk2Car, nuScenes-QA, DriveLM, BDD-X, LingoQA, HAD, DRAMA, referring expressions, driving captions
- **I. Search, queries & semantic parsing**: NL-to-structured automotive search, query logs, synthetic query corpora, text-to-SQL on car data
- **J. Market, pricing & listing tables with text**: used-car price datasets that carry free text, Craigslist/Kaggle car listings
- **K. Knowledge graphs, ontologies & lexicons**: automotive ontologies (e.g. VSS), KGs, taxonomies, lexicons

## How to cite

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

## Contributing

Contributions are welcome. Open an issue with the *New corpus* form, or send a pull request that edits `data/corpora.yaml` or `data/papers.yaml`, runs `python scripts/build_readme.py` and commits the regenerated `README.md`. [CONTRIBUTING.md](CONTRIBUTING.md) has the inclusion rule, the verification rule, the field reference and the pull-request checklist.

---

_Generated on 2026-10-25 by `python scripts/build_readme.py` from `data/corpora.yaml` and `data/papers.yaml`. Do not edit README.md by hand: edit the YAML files and re-run the command._
