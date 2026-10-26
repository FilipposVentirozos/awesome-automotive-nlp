# Contributing

Thank you for helping to grow the list. `README.md`, the `modalities/` pages and the CSV and JSON downloads in `data/` are all generated from two YAML files, so a contribution is an edit to `data/corpora.yaml` or `data/papers.yaml` followed by one command.

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

The primary axis is the application area, bucket codes `A` to `M` (listed in the *Taxonomy* section of `README.md`). Pick the bucket that matches the corpus's main use with `section`; the task, modality and language columns carry the rest.

| Code | Section | Covers |
|---|---|---|
| `A` | 🚗 Vehicle identification & specifications | make/model/trim/engine NER, car-type recognition from text or image, VIN, spec sheets |
| `B` | 🏷️ Listings, adverts & claims | classified-ad IE (condition, history, offers), ad generation & verification, listing corpora |
| `C` | 🧩 Features, attributes & catalogue linking | feature-conditioned NER, attribute-value extraction, product/catalogue linking |
| `D` | ⭐ Reviews, opinion & sentiment | car reviews, automotive ABSA, forums, social media opinion |
| `E` | ⚠️ Complaints, safety, recalls & incidents | NHTSA/ODI complaints, defect reports, crash narratives, recall text |
| `F` | 📘 Owner's manuals & technical QA | owner's-manual and FAQ question answering, manual retrieval, FAQ-oriented NER |
| `G` | 🔧 Faults, diagnostics & repair | fault and repair-case text, customer failure reports, diagnostic NER and relation extraction, parts NER |
| `H` | 📐 Engineering documents | requirements, safety standards and patents |
| `I` | 🗣️ In-car voice assistants & dialogue | in-car task-oriented dialogue, SLU intent/slot, in-vehicle ASR/speech, driver-vehicle interaction |
| `J` | 🛣️ Driving-scene language & multimodal | Talk2Car, nuScenes-QA, DriveLM, BDD-X, LingoQA, HAD, DRAMA, referring expressions, driving captions |
| `K` | 🔎 Search, queries & semantic parsing | NL-to-structured automotive search, query logs, synthetic query corpora, text-to-SQL on car data |
| `L` | 💷 Market, pricing & listing tables with text | used-car price datasets that carry free text, Craigslist/Kaggle car listings |
| `M` | 🕸️ Knowledge graphs, ontologies & lexicons | automotive ontologies (e.g. VSS), KGs, taxonomies, lexicons |

The emoji are set in `HEADING_EMOJI` in `scripts/build_readme.py`, which also gives the top-level headings theirs (Contents 📑, Taxonomy 🗂️, Related papers (no public data) 📄, How to cite 📝, Contributing 🤝). Codes were re-lettered on 2026-10-26, when the old section F was split into F, G and H: the former G-K are now I-M.

- **Sub-headings.** `subsection` places the entry under a sub-heading inside its section. Reuse an existing sub-heading string exactly (copy it from `data/corpora.yaml`); a new string creates a new sub-heading. Entries with `subsection: ""` render first, in a table directly under the section heading; the named sub-headings follow in the order in which they first appear in the YAML. Within each table, rows are sorted by name. Do not name a sub-heading after a section or a top-level heading (for example "Taxonomy"): the renderer rejects anchors that would collide.
- **Section notes.** Every bucket is rendered, even when it has no entries. A section may carry one short italic note under its heading, kept in `SECTION_NOTES` in `scripts/build_readme.py`, which explains a gap (for example, why section L is empty) or points to where related corpora are listed. Propose a change to a note in the pull request that makes it necessary.
- **Merging.** No buckets are merged (`MERGE_INTO` in `scripts/build_readme.py` is empty). Adding a pair such as `"L": "B"` would fold a bucket with fewer than three entries into its neighbour, with a line saying so.

## Short Task and Size columns

The tables show `task_short` and `size_short` so that they stay narrow; the full `task_type` and `size` stay in the YAML and in the downloads. If you leave them out of an issue, the maintainer fills them in.

**`task_short`** is one label, or two joined by `" + "` (for example `QA + VQA`), at most 22 characters, using exactly these labels (case matters). The renderer rejects any other label and names the entry. To add a label, add it to `TASK_LABELS` in `scripts/build_readme.py` and to this list in the same pull request.

- Text extraction: `NER`, `fine-grained NER`, `span labelling`, `entity linking`, `relation extraction`
- Opinion and classification: `ABSA`, `sentiment`, `summarisation`, `classification`
- Question answering and vision-language: `QA`, `VQA`, `video QA`, `captioning`, `explanation`, `grounding`, `retrieval`, `hallucination`
- Dialogue and speech: `dialogue`, `tool calling`, `SLU`, `ASR`, `audio-visual ASR`, `noise / acoustics`
- Images: `image classification`, `re-identification`, `damage detection`
- Queries: `semantic parsing`, `text-to-SQL`
- Safety records: `complaint text`, `recall text`, `investigation text`, `service bulletins`, `crash narratives`, `incident reports`
- Knowledge resources: `KG / ontology`, `gazetteer`, `lexicon`, `schema / standard`, `VIN decoding`
- Documents and listings: `patents`, `requirements`, `listings`

**`size_short`** is the headline figure and its unit, at most 26 characters, with no prose: for example `659 adverts`, `42.3k descriptions`, `16,185 images`, `460k QA pairs`, `20.0M reviews`, `100+ h speech`. Rules:

- Every number in `size_short` must appear in that entry's `size`. Exact figures may be shortened with `k` (thousand) or `M` (million), rounding only, as in 42,300 -> `42.3k`. Never add or derive figures: two stated figures may sit side by side (`3,381/225/903 comments`), but a sum that the source does not state may not.
- Keep the source's hedges: `~` for approximately, `N+` for "more than" or "over".
- Use `h` for hours, `GB` and `MB` for file sizes, lower-case `k` and upper-case `M`.
- Write `not stated` when the source does not give a size, or gives one only for a larger collection whose automotive part is not counted (for example the whole of Spider or Yelp).

## Adding an entry

Add one mapping to the `entries:` list. Every key must be present; use `null` where allowed. Keep free text in British English.

| Field | Type | Meaning |
|---|---|---|
| `name` | string | canonical corpus name (unique across both files) |
| `aliases` | list of strings | other names (including the original form of a shortened display name), or `[]`; kept for search, not shown in the README |
| `section` | `A`..`M` | bucket code (see the table above) |
| `subsection` | string | sub-heading within the section (see above); `""` for none |
| `task_type` | string | e.g. NER, span labelling, entity linking, attribute-value extraction, ABSA, sentiment, text classification, dialogue (task-oriented), SLU/intent+slot, ASR, TTS, QA, VQA, captioning, grounding/referring expression, semantic parsing / NL-to-query, summarisation, NLG (ad generation), fact verification, KG/ontology, image classification |
| `task_short` | string | the Task column: one or two labels from the vocabulary below, joined by " + " (at most 22 characters) |
| `modality` | `text` / `speech` / `multimodal` / `image` / `tabular+text` | also decides the `modalities/` page the row appears on |
| `language` | string | e.g. English, Chinese, German; several languages separated by ", " (e.g. `English, Korean`); `Multilingual` for many; `n/a (images)` for non-linguistic data. The Languages line counts base languages ("Chinese (Taiwan Mandarin)" counts as Chinese); `Multilingual`, `n/a (...)` and `unknown` are listed but not counted |
| `domain_subtopic` | string | short phrase, e.g. "used-car listings", "in-car navigation dialogue" |
| `size` | string | as stated by the source, with unit (documents, utterances, hours, images); kept in full in the downloads |
| `size_short` | string | the Size column: the headline figure and unit (at most 26 characters); see below |
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
| `ours` | boolean, optional | `true` only for the list author's own corpora (AutoSpecNER, Auto-AdvER, Auto-Features); exported, not rendered separately. Missing means `false` in the downloads |
| `authors` | string, optional | short form shown after the name, e.g. `Hu and Ma`; useful when `name` is a paper title. Missing means `null` (an empty cell in the CSV) |

Example:

```yaml
  - name: Example Car Reviews
    aliases: []
    section: D
    subsection: Consumer and expert reviews
    task_type: ABSA
    task_short: ABSA
    modality: text
    language: English
    domain_subtopic: car reviews
    size: "2,000 reviews; 12,400 aspect annotations"
    size_short: "2,000 reviews"
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

## Generated files

Never edit these by hand; they are rewritten on every run and must be committed together with the YAML change:

- `README.md`;
- `modalities/README.md` and one page per modality (`text.md`, `speech.md`, `multimodal.md`, `image.md`, `tabular-text.md`), which repeat the main list's sections and sub-headings with only that modality's rows;
- `data/corpora.json`, `data/corpora.csv`, `data/papers.json` and `data/papers.csv`: every field of every entry, in YAML field order. JSON is UTF-8 with two-space indentation; CSV is UTF-8 with a header row, lists (`aliases`, `cited_in`) joined with `"; "`, booleans as `true`/`false` and `null` as an empty cell.

Install PyYAML once, then run the renderer from the repository root:

```sh
pip install pyyaml
python scripts/build_readme.py
```

The script validates every entry (required fields, bucket code, access value, `task_short` vocabulary and length, `size_short` length, URL shape, cross-field consistency, duplicate names) and checks every link on every generated page: relative links must reach a file, and every `#anchor` must match a heading (GitHub's rules: the heading emoji drops out, a following space becomes a leading `-`, and a variation selector U+FE0F is kept). It exits non-zero naming the offending entry or link.

`python scripts/build_readme.py --check` writes nothing and fails if any generated file is out of date with the YAML (README.md is compared without its "Generated on" date line), or if `modalities/` holds a page the renderer did not generate. Run it before opening a pull request.

Section and top-level headings carry one emoji each, set in `HEADING_EMOJI` in `scripts/build_readme.py`; sub-headings carry none.

## Pull-request checklist

- [ ] The entry satisfies the inclusion rule (freely downloadable, or described in a public paper with `access: paper only (contact authors)`); it is not a commercial catalogue.
- [ ] Corpus rows are in `data/corpora.yaml`; papers with no public data are in `data/papers.yaml`.
- [ ] `source_quote` is verbatim from the paper or page; `verified` is set honestly; no invented URLs.
- [ ] `section` is a bucket code `A`..`M`, `subsection` reuses an existing sub-heading string where one fits, and `access` is one of the allowed values.
- [ ] `task_short` uses the vocabulary above; every number in `size_short` appears in `size`.
- [ ] `python scripts/build_readme.py` exits 0, and the regenerated `README.md`, `modalities/` pages and `data/` exports are committed (`python scripts/build_readme.py --check` passes).
- [ ] Free text is in British English (licence, catalogue, labelled).
- [ ] One corpus or paper per pull request where practical.
