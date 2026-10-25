# 🎬 Multimodal

Part of [awesome-automotive-nlp](../README.md). Same taxonomy as the main list: see [Taxonomy](../README.md#️-taxonomy).

**40 corpora** in 5 languages.

**Languages:** English 33 · Chinese 2 · Cantonese 1 · Japanese 1 · Romanian 1 · Multilingual 2

## 📑 Contents

- [Corpora by application area](#corpora-by-application-area)
  - [🏷️ B. Listings, adverts & claims](#️-b-listings-adverts--claims) (1)
  - [⭐ D. Reviews, opinion & sentiment](#-d-reviews-opinion--sentiment) (1)
  - [⚠️ E. Complaints, safety, recalls & incidents](#️-e-complaints-safety-recalls--incidents) (1)
  - [🔧 F. Maintenance, repair, parts & technical documents](#-f-maintenance-repair-parts--technical-documents) (1)
  - [🗣️ G. In-car voice assistants & dialogue](#️-g-in-car-voice-assistants--dialogue) (5)
  - [🛣️ H. Driving-scene language & multimodal](#️-h-driving-scene-language--multimodal) (30)
  - [🕸️ K. Knowledge graphs, ontologies & lexicons](#️-k-knowledge-graphs-ontologies--lexicons) (1)

## Corpora by application area

### 🏷️ B. Listings, adverts & claims

#### Listings and adverts

| Corpus | Task | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|
| DVM-CAR | listings | English | 0.25M+ adverts | CC BY-NC 4.0 | open | 2021 | [data](https://deepvisualmarketing.github.io/) · [paper](https://arxiv.org/abs/2109.00881) | — |

### ⭐ D. Reviews, opinion & sentiment

#### Social and video media

| Corpus | Task | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|
| MuSe-CaR (Multimodal Sentiment Analysis in Car Reviews) | sentiment | English | 40+ h video | EULA, academic use only | on request | 2021 | [data](https://www.muse-challenge.org) · [paper](https://arxiv.org/abs/2101.06053) | — |

### ⚠️ E. Complaints, safety, recalls & incidents

#### Crash and automated-driving incident narratives

| Corpus | Task | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|
| NMVCCS - National Motor Vehicle Crash Causation Survey | crash narratives | English | 6,949 crashes | unknown | open | 2008 | [data](https://catalog.data.gov/dataset/national-motor-vehicle-crash-causation-survey-nmvccs-nmvccs-xml-case-viewer) | — |

### 🔧 F. Maintenance, repair, parts & technical documents

#### Manuals, FAQs & question answering

| Corpus | Task | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|
| FETA car manuals benchmark | retrieval | English | not stated | apache-2.0 | open | 2022 | [data](https://huggingface.co/datasets/alfassy/FETA_IKEA_CAR_MANUALS) · [paper](https://arxiv.org/abs/2209.03648) | — |

### 🗣️ G. In-car voice assistants & dialogue

#### Task-oriented dialogue and tool use

| Corpus | Task | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|
| AMIE in-cabin passenger-agent dialogue dataset | SLU | English | 1,331 utterances | unknown | paper only | 2019 | paper only · [paper](https://arxiv.org/abs/1904.10500) | — |

#### Assistant evaluation

| Corpus | Task | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|
| InCarEmo | classification | Chinese | not stated | unknown | paper only | 2026 | paper only · [paper](https://arxiv.org/abs/2607.14683) | — |

#### In-car speech recognition

| Corpus | Task | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|
| CI-AVSR | audio-visual ASR | Cantonese | 4,984 samples (8.3 h) | CC0-1.0 | open | 2022 | [data](https://github.com/HLTCHKUST/CI-AVSR) · [paper](https://arxiv.org/abs/2201.03804) | — |
| CIAIR In-Car Speech Database | dialogue | Japanese | \~800 subjects | unknown | paper only | 2004 | paper only · [paper](https://www.isca-archive.org/interspeech_2004/kawaguchi04_interspeech.html) | — |
| UTDrive | ASR | English | 37 F + 40 M drivers | unknown | open | 2007 | [data](https://utdrive.utdallas.edu/corpus) | — |

### 🛣️ H. Driving-scene language & multimodal

*For papers and models on language in autonomous driving, see [Awesome-LLM4AD](https://github.com/Thinklab-SJTU/Awesome-LLM4AD), which this section complements; it lists corpora only.*

#### Grounding, referring expressions and retrieval

| Corpus | Task | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|
| CityFlow-NL | retrieval + grounding | English | 2,155 train tracks | repo Apache-2.0 | open | 2021 | [data](https://github.com/fredfung007/cityflow-nl) · [paper](https://arxiv.org/abs/2101.04741) | — |
| HAD | grounding + captioning | English | \~30 h video | non-commercial use only | on request | 2019 | [data](https://usa.honda-ri.com/HAD) · [paper](https://openaccess.thecvf.com/content_CVPR_2019/papers/Kim_Grounding_Human-To-Vehicle_Advice_for_Self-Driving_Vehicles_CVPR_2019_paper.pdf) | — |
| NuPrompt | grounding | English | 40,147 prompts | repo Apache-2.0 | open | 2023 | [data](https://github.com/wudongming97/Prompt4Driving) · [paper](https://arxiv.org/abs/2309.04379) | — |
| Refer-KITTI | grounding | English | 818 expressions | unknown | open | 2023 | [data](https://referringmot.github.io/) · [paper](https://arxiv.org/abs/2303.03366) | — |
| Talk2Car | grounding | English | 11,959 commands | unknown | open | 2019 | [data](https://talk2car.github.io/) · [paper](https://arxiv.org/abs/1909.10838) | — |

#### Scene question answering and instruction tuning

| Corpus | Task | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|
| MAPLM | VQA | English | not stated | repo MIT | open | 2023 | [data](https://github.com/LLVM-AD/MAPLM) · [paper](https://openaccess.thecvf.com/content/CVPR2024/papers/Cao_MAPLM_A_Real-World_Large-Scale_Vision-Language_Benchmark_for_Map_and_Traffic_CVPR_2024_paper.pdf) | — |
| NuInstruct | VQA | English | 91k video-QA pairs | unknown | open | 2024 | [data](https://github.com/xmed-lab/NuInstruct) · [paper](https://arxiv.org/abs/2401.00988) | — |
| NuScenes-MQA | VQA + captioning | English | not stated | repo Apache-2.0 | open | 2023 | [data](https://github.com/turingmotors/NuScenes-MQA) · [paper](https://arxiv.org/abs/2312.06352) | — |
| NuScenes-QA | VQA | English | 460k QA pairs | repo MIT | open | 2023 | [data](https://github.com/qiantianwen/NuScenes-QA) · [paper](https://arxiv.org/abs/2305.14836) | — |
| OmniDrive-nuScenes | VQA | English | not stated | unknown | open | 2024 | [data](https://github.com/NVlabs/OmniDrive) · [paper](https://arxiv.org/abs/2405.01533) | — |
| SURDS | VQA | English | not stated | academic use only | open | 2024 | [data](https://github.com/XiandaGuo/Drive-MLLM) | — |
| Talk2BEV | VQA | English | 20k+ questions | unknown | open | 2023 | [data](https://llmbev.github.io/talk2bev/) · [paper](https://arxiv.org/abs/2310.02251) | — |

#### Explanations, captions and risk narration

| Corpus | Task | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|
| BDD-OIA | classification | English | not stated | unknown | open | 2020 | [data](https://github.com/Twizwei/bddoia_project) | — |
| BDD-X | explanation | English | 6,970 videos (\~77 h) | unknown | open | 2018 | [data](https://github.com/JinkyuKimUCB/BDD-X-dataset) · [paper](https://openaccess.thecvf.com/content_ECCV_2018/papers/Jinkyu_Kim_Textual_Explanations_for_ECCV_2018_paper.pdf) | — |
| CoVLA | captioning | English | 80+ h video | released for academic use | open | 2024 | [data](https://turingmotors.github.io/covla-ad/) · [paper](https://arxiv.org/abs/2408.10845) | — |
| DRAMA | captioning + grounding | English | 17,785 clips | non-commercial use only | on request | 2023 | [data](https://usa.honda-ri.com/drama) · [paper](https://openaccess.thecvf.com/content/WACV2023/papers/Malla_DRAMA_Joint_Risk_Localization_and_Captioning_in_Driving_WACV_2023_paper.pdf) | — |
| DriveGPT4 instruction data | VQA | English | not stated | unknown | paper only | 2023 | paper only · [paper](https://arxiv.org/abs/2310.01412) | — |
| Rank2Tell | VQA + captioning | English | 116 clips | unknown | on request | 2023 | [data](https://usa.honda-ri.com/rank2tell) · [paper](https://arxiv.org/abs/2309.06597) | — |

#### Reasoning and planning with language

| Corpus | Task | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|
| DriveBench | VQA | English | 20,498 QA pairs | Apache-2.0 | open | 2025 | [data](https://github.com/drive-bench/toolkit) · [paper](https://arxiv.org/abs/2501.04003) | — |
| DriveLM | VQA | English | not stated | language data CC BY-NC-SA 4.0 | open | 2023 | [data](https://github.com/OpenDriveLab/DriveLM) · [paper](https://arxiv.org/abs/2312.14150) | — |
| LingoQA | video QA | English | 419.9k QA pairs | unknown | open | 2023 | [data](https://github.com/wayveai/LingoQA) · [paper](https://arxiv.org/abs/2312.14115) | — |
| Reason2Drive | VQA | English | 600k+ video-text pairs | unknown | open | 2023 | [data](https://github.com/fudan-zvg/Reason2Drive) · [paper](https://arxiv.org/abs/2312.03661) | — |
| V2V-QA | VQA | English | not stated | unknown | open | 2025 | [data](https://eddyhkchiu.github.io/v2vllm.github.io/) · [paper](https://arxiv.org/abs/2502.09980) | — |

#### Traffic rules and driving-test QA

| Corpus | Task | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|
| DriveCombo | QA + VQA | Multilingual | \~70k questions | unknown | paper only | 2026 | paper only · [paper](https://arxiv.org/abs/2603.01637) | — |
| DriveQA | QA + VQA | English | 474k QA pairs | unknown | open | 2025 | [data](https://driveqaiccv.github.io/) · [paper](https://arxiv.org/abs/2508.21824) | — |
| DrivingVQA | VQA | English | 3,931 problems | unknown | open | 2025 | [data](https://vita-epfl.github.io/DrivingVQA/) · [paper](https://arxiv.org/abs/2501.04671) | — |
| IDKB | QA + VQA | Multilingual | 1M+ data items | unknown | paper only | 2024 | paper only · [paper](https://arxiv.org/abs/2409.02914) | — |
| Romanian Driving Laws QA | QA + VQA | Romanian | 1,208 questions | unknown | paper only | 2025 | paper only · [paper](https://arxiv.org/abs/2509.23715) | — |

#### Roadside traffic-video QA

| Corpus | Task | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|
| SUTD-TrafficQA | video QA | English | 62,535 QA pairs | unknown | on request | 2021 | [data](https://github.com/sutdcv/SUTD-TrafficQA) · [paper](https://arxiv.org/abs/2103.15538) | — |
| TUMTraffic-VideoQA | video QA + captioning | English | 85k MCQ pairs | CC BY-NC-SA 4.0 | open | 2025 | [data](https://innovation-mobility.com/en/project-providentia/a9-dataset) · [paper](https://arxiv.org/abs/2502.02449) | — |

### 🕸️ K. Knowledge graphs, ontologies & lexicons

#### Glossaries and knowledge graphs

| Corpus | Task | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|
| Car-identification - Autohome car knowledge graph & QA | KG / ontology + QA | Chinese | 284 brands, 2,058 series | unknown | open | — | [data](https://github.com/LongxingHu/Car-identification) | — |

---

_Generated by `python scripts/build_readme.py` from `data/corpora.yaml`. Do not edit this page by hand._
