# Contributing

Thank you for helping to grow the list. Everything in `README.md` is generated from two YAML files, so a contribution is an edit to `data/corpora.yaml` or `data/papers.yaml` followed by one command.

## Inclusion rule

A corpus belongs in the list if **either**

1. it is freely downloadable, in which case the row carries the download link, **or**
2. it is described in a public paper but the download link is not recoverable, in which case the row is kept with the academic reference, `access: paper only (contact authors)` and `dataset_url: null`, so that readers can email the authors.

Excluded: fee-based commercial catalogues (for example paid LDC or ELRA licences) and anything whose only evidence is a search snippet. The renderer rejects `access: commercial`.

Automotive NLP papers with no public corpus (a system, benchmark or evaluation whose data has not been released) go in `data/papers.yaml` and render under *Related papers (no public data)*. A paper whose data later becomes available moves to `data/corpora.yaml`.

All modalities (text, speech, multimodal, image, tabular+text) and all languages are welcome; every row carries a modality and a language tag.

## Verification rule

- `verified: true` **only** if you fetched `dataset_url` or `paper_url` yourself and the page matched the entry. Otherwise set `verified: false` and say in `notes` what you could not check.
- `source_quote` must be a **verbatim** sentence from the paper or the dataset page proving that the resource exists and what it is. No paraphrase.
- Do not invent URLs. If you cannot find one, use `null`.
- `size` and `license` are recorded as the source states them; write `unknown` if the source does not say.

## Sections, sub-headings and section notes

The primary axis is the application area, bucket codes `A` to `K` (listed in the *Taxonomy* section of `README.md`). Pick the bucket that matches the corpus's main use with `section`; the task, modality and language columns carry the rest.

- **Sub-headings.** `subsection` places the entry under a sub-heading inside its section. Reuse an existing sub-heading string exactly (copy it from `data/corpora.yaml`); a new string creates a new sub-heading. Entries with `subsection: ""` render first, in a table directly under the section heading; the named sub-headings follow in the order in which they first appear in the YAML. Within each table, rows are sorted by name. Do not name a sub-heading after a section or a top-level heading (for example "Taxonomy"): the renderer rejects anchors that would collide.
- **Section notes.** Every bucket is rendered, even when it has no entries. A section may carry one short italic note under its heading, kept in `SECTION_NOTES` in `scripts/build_readme.py`, which explains a gap (for example, why section J is empty) or points to where related corpora are listed. Propose a change to a note in the pull request that makes it necessary.
- **Merging.** No buckets are merged (`MERGE_INTO` in `scripts/build_readme.py` is empty). Adding a pair such as `"J": "B"` would fold a bucket with fewer than three entries into its neighbour, with a line saying so.

## Adding an entry

Add one mapping to the `entries:` list. Every key must be present; use `null` where allowed. Keep free text in British English.

| Field | Type | Meaning |
|---|---|---|
| `name` | string | canonical corpus name (unique across both files) |
| `aliases` | list of strings | other names (including the original form of a shortened display name), or `[]`; kept for search, not shown in the README |
| `section` | `A`..`K` | bucket code |
| `subsection` | string | sub-heading within the section (see above); `""` for none |
| `task_type` | string | e.g. NER, span labelling, entity linking, attribute-value extraction, ABSA, sentiment, text classification, dialogue (task-oriented), SLU/intent+slot, ASR, TTS, QA, VQA, captioning, grounding/referring expression, semantic parsing / NL-to-query, summarisation, NLG (ad generation), fact verification, KG/ontology, image classification |
| `modality` | `text` / `speech` / `multimodal` / `image` / `tabular+text` | |
| `language` | string | e.g. English, Chinese, German; several languages separated by ", " (e.g. `English, Korean`); `Multilingual` for many; `n/a (images)` for non-linguistic data. The README's Languages line counts each tag |
| `domain_subtopic` | string | short phrase, e.g. "used-car listings", "in-car navigation dialogue" |
| `size` | string | as stated by the source, with unit (documents, utterances, hours, images) |
| `license` | string | as stated, or `unknown`. The Licence column shows a short form (the text before the first " (" or ";", at most 40 characters); keep the full terms here |
| `access` | `public` / `request` / `paper only (contact authors)` / `forthcoming` / `unreleased` / `unknown` | `public` requires a `dataset_url`; `paper only (contact authors)` and `forthcoming` require `dataset_url: null`. The Access column shows `open`, `on request`, `paper only` and `forthcoming` for the first four |
| `dataset_url` | http(s) URL or `null` | |
| `paper_url` | http(s) URL or `null` | |
| `year` | integer or `null` | |
| `cited_in` | list of strings | which of our public papers cite it: `AutoSpecNER`, `Auto-AdvER`, `Auto-Features`, `Useful Diversity (text2solr)`; `[]` if none |
| `bibkey` | string or `null` | BibTeX key in our .bib files, if any |
| `source_quote` | string | verbatim sentence from the paper or page (see above) |
| `verified` | boolean | see the verification rule |
| `notes` | string | splits, annotation scheme, known issues, relation to our work; may be empty |
| `ours` | boolean, optional | `true` only for the list author's own corpora |
| `authors` | string, optional | short form shown after the name, e.g. `Hu and Ma`; useful when `name` is a paper title |

Example:

```yaml
  - name: Example Car Reviews
    aliases: []
    section: D
    subsection: Consumer and expert reviews
    task_type: ABSA
    modality: text
    language: English
    domain_subtopic: car reviews
    size: "2,000 reviews; 12,400 aspect annotations"
    license: CC BY-NC 4.0
    access: public
    dataset_url: https://example.org/example-car-reviews
    paper_url: https://aclanthology.org/2025.example-1.1/
    year: 2025
    cited_in: []
    bibkey: null
    source_quote: "We release a corpus of 2,000 car reviews annotated with aspect terms and polarity."
    verified: true
    notes: "Train/dev/test split shipped with the release."
```

## Rendering the README

`README.md` is generated; never edit it by hand. Install PyYAML once, then run the renderer from the repository root:

```sh
pip install pyyaml
python scripts/build_readme.py
```

The script validates every entry (required fields, bucket code, access value, URL shape, cross-field consistency, duplicate names) and checks that every in-page link in the generated README resolves; it exits non-zero naming the offending entry or link if anything is wrong. `python scripts/build_readme.py --check` validates without writing. Commit the regenerated `README.md` together with the YAML change.

## Pull-request checklist

- [ ] The entry satisfies the inclusion rule (freely downloadable, or described in a public paper with `access: paper only (contact authors)`); it is not a commercial catalogue.
- [ ] Corpus rows are in `data/corpora.yaml`; papers with no public data are in `data/papers.yaml`.
- [ ] `source_quote` is verbatim from the paper or page; `verified` is set honestly; no invented URLs.
- [ ] `section` is a bucket code `A`..`K`, `subsection` reuses an existing sub-heading string where one fits, and `access` is one of the allowed values.
- [ ] `python scripts/build_readme.py` exits 0 and the regenerated `README.md` is committed.
- [ ] Free text is in British English (licence, catalogue, labelled).
- [ ] One corpus or paper per pull request where practical.
