# awesome-automotive-nlp

A curated list of corpora for natural language processing on automotive text, speech and driving scenes: vehicle adverts and listings, reviews and complaints, repair manuals and parts catalogues, in-car dialogue, driving-scene language and the knowledge resources that tie them together. The list grew out of three Auto Trader UK advertisement corpora (AutoSpecNER, Auto-AdvER and Auto-Features), whose related-work sections showed how scattered the field's datasets are. Every row carries task, modality, language, size, licence, access and year tags, and says which of our papers cites it. A corpus is listed if it is freely downloadable or described in a public paper (in which case the row says *paper only* and readers can contact the authors); fee-based commercial catalogues are excluded. See [Contributing](#contributing) to add one.

## Contents

- [Our corpora](#our-corpora) (3)
- [Corpora by application area](#corpora-by-application-area)
  - [A. Vehicle identification & specifications](#a-vehicle-identification--specifications) (1)
  - [B. Listings, adverts & claims](#b-listings-adverts--claims) (1)
  - [C. Features, attributes & catalogue linking](#c-features-attributes--catalogue-linking) (1)
- [Related papers (no public data)](#related-papers-no-public-data) (1)
- [Taxonomy](#taxonomy)
- [How to cite](#how-to-cite)
- [Contributing](#contributing)

## Our corpora

The Auto Trader UK advertisement corpora this list grew out of. They are also listed under their application areas below.

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| AutoSpecNER | NER | text | English | 659 vehicle adverts; 15 entity types; 4,609 entity spans (public release); 100-document 3-annotator IAA study | CC BY 4.0 | public | 2026 | [data](https://github.com/FilipposVentirozos/AutoSpecNER) · [paper](https://aclanthology.org/2026.icnlsp-1.8/) | — |
| Auto-AdvER | span labelling | text | English | 605 UK car adverts; 104,382 tokens; 3 span labels (Condition / Historic / Sales Options); 113-advert 3-annotator IAA subset; 3 cross-validation folds | CC BY 4.0 (data and guidelines); MIT (code) | public | 2026 | [data](https://github.com/FilipposVentirozos/Auto-AdvER) · [paper](https://arxiv.org/abs/2412.05655) | AutoSpecNER, Auto-Features |
| Auto-Features | feature-conditioned NER; entity linking | text | English | 1,256 UK car adverts (430 human-gold + 925 LLM-silver, 99 overlap); 188,980 (advert, feature) instances per fold | to be announced at release | forthcoming | 2026 | forthcoming (release pending) | — |

## Corpora by application area

### A. Vehicle identification & specifications

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| AutoSpecNER | NER | text | English | 659 vehicle adverts; 15 entity types; 4,609 entity spans (public release); 100-document 3-annotator IAA study | CC BY 4.0 | public | 2026 | [data](https://github.com/FilipposVentirozos/AutoSpecNER) · [paper](https://aclanthology.org/2026.icnlsp-1.8/) | — |

### B. Listings, adverts & claims

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| Auto-AdvER | span labelling | text | English | 605 UK car adverts; 104,382 tokens; 3 span labels (Condition / Historic / Sales Options); 113-advert 3-annotator IAA subset; 3 cross-validation folds | CC BY 4.0 (data and guidelines); MIT (code) | public | 2026 | [data](https://github.com/FilipposVentirozos/Auto-AdvER) · [paper](https://arxiv.org/abs/2412.05655) | AutoSpecNER, Auto-Features |

### C. Features, attributes & catalogue linking

| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |
|---|---|---|---|---|---|---|---|---|---|
| Auto-Features | feature-conditioned NER; entity linking | text | English | 1,256 UK car adverts (430 human-gold + 925 LLM-silver, 99 overlap); 188,980 (advert, feature) instances per fold | to be announced at release | forthcoming | 2026 | forthcoming (release pending) | — |

## Related papers (no public data)

Automotive papers cited in our work that describe a resource without a recoverable download. The rows are kept, with the academic reference, so that readers can contact the authors.

| Paper | Task | Lang | Year | Link | Cited in |
|---|---|---|---|---|---|
| Named Entity Recognition of Automotive Parts Based on RoBERTa-CRF Model (Hu and Ma) | NER | Chinese | 2024 | [paper](https://doi.org/10.1109/NNICE61279.2024.10499162) | AutoSpecNER, Auto-Features |

## Taxonomy

The primary axis is the application area, one section per bucket. The secondary axes are the table columns: task, modality (text, speech, multimodal, image, tabular+text), language, size, licence, access, year, links and the paper of ours that cites the row.

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

A bucket with fewer than 3 entries is merged into its named neighbour by the renderer (J into B; K into F) and the section says so.

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
