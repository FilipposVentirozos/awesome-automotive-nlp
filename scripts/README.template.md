# awesome-automotive-nlp

{{BADGES}}

A curated list of corpora for natural language processing on automotive text, speech and driving scenes: vehicle adverts and listings, reviews and complaints, repair manuals and parts catalogues, in-car dialogue, driving-scene language and the knowledge resources that tie them together. The list grew out of three Auto Trader UK advertisement corpora (AutoSpecNER, Auto-AdvER and Auto-Features), whose related-work sections showed how scattered the field's datasets are. Every row carries task, modality, language, size, licence, access and year tags, and says which of our papers cites it. A corpus is listed if it is freely downloadable or described in a public paper (in which case the row says *paper only* and readers can contact the authors); fee-based commercial catalogues are excluded. See [Contributing](#{{A:Contributing}}) to add one.

{{SUMMARY}}

_Listing a dataset here does not grant any licence to it: each dataset keeps its own terms, so check them before use. If you own a listed dataset and want its entry corrected or removed, please [open an issue](https://github.com/FilipposVentirozos/awesome-automotive-nlp/issues)._

**Download:** [CSV](data/corpora.csv) · [JSON](data/corpora.json) (related papers: [CSV](data/papers.csv) · [JSON](data/papers.json))

{{BROWSE}}

{{H2:Contents}}

{{CONTENTS}}

{{H2:Taxonomy}}

The primary axis is the application area, one section per bucket; larger sections are split into sub-headings. Every bucket is shown, even when empty, and a short note under a section heading explains a gap or points to where related corpora are listed. The secondary axes are the table columns: task, modality (text, speech, multimodal, image, tabular+text), language, size, licence, access, year, links and the paper of ours that cites the row. Task, size and licence are shown in short form; the full values are in `data/corpora.yaml` and in the CSV and JSON downloads.

{{TAXONOMY}}

{{SECTIONS}}

{{PAPERS}}

{{H2:How to cite}}

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

Auto-Features: the citation will be added when the corpus is released.

{{H2:Contributing}}

Contributions are welcome. Open an issue with the *New corpus* form, or send a pull request that edits `data/corpora.yaml` or `data/papers.yaml`, runs `python scripts/build_readme.py` and commits the regenerated `README.md`, `modalities/` pages and `data/` exports. [CONTRIBUTING.md](CONTRIBUTING.md) has the inclusion rule, the verification rule, the field reference and the pull-request checklist.

---

_Generated on {{DATE}} by `python scripts/build_readme.py` from `data/corpora.yaml` and `data/papers.yaml`. Do not edit README.md, the `modalities/` pages or the `data/*.json` and `data/*.csv` exports by hand: edit the YAML files and re-run the command._
