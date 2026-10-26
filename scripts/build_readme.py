#!/usr/bin/env python3
"""Render README.md, the modalities/ pages and the CSV/JSON exports for awesome-automotive-nlp.

Sources: data/corpora.yaml and data/papers.yaml (the single source of truth).

Usage:
    python scripts/build_readme.py           validate the YAML, then write README.md, modalities/*.md and
                                             data/{corpora,papers}.{json,csv}
    python scripts/build_readme.py --check   validate and render in memory; write nothing; fail if any
                                             committed output is out of date (README.md is compared
                                             without its "Generated on" date line)

Exit status: 0 on success; 1 on a validation error (printed with the entry name), a broken link or
anchor, or (with --check) an out-of-date output; 2 if a file cannot be read or parsed.

Dependencies: Python 3.9+ and PyYAML (pip install pyyaml). Nothing else.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import io
import json
import posixpath
import re
import sys
import unicodedata
from collections import Counter, OrderedDict
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.stderr.write("build_readme.py: PyYAML is required (pip install pyyaml)\n")
    sys.exit(2)

ROOT = Path(__file__).resolve().parent.parent
CORPORA_FILE = ROOT / "data" / "corpora.yaml"
PAPERS_FILE = ROOT / "data" / "papers.yaml"
TEMPLATE_FILE = ROOT / "scripts" / "README.template.md"

# Taxonomy: bucket code -> (name as decided in TAXONOMY.md, one-line definition from SCHEMA.md).
BUCKETS: "OrderedDict[str, tuple[str, str]]" = OrderedDict([
    ("A", ("Vehicle identification & specifications",
           "make/model/trim/engine NER, car-type recognition from text or image, VIN, spec sheets")),
    ("B", ("Listings, adverts & claims",
           "classified-ad IE (condition, history, offers), ad generation & verification, listing corpora")),
    ("C", ("Features, attributes & catalogue linking",
           "feature-conditioned NER, attribute-value extraction, product/catalogue linking")),
    ("D", ("Reviews, opinion & sentiment",
           "car reviews, automotive ABSA, forums, social media opinion")),
    ("E", ("Complaints, safety, recalls & incidents",
           "NHTSA/ODI complaints, defect reports, crash narratives, recall text")),
    ("F", ("Owner's manuals & technical QA",
           "owner's-manual and FAQ question answering, manual retrieval, FAQ-oriented NER")),
    ("G", ("Faults, diagnostics & repair",
           "fault and repair-case text, customer failure reports, diagnostic NER and relation extraction, parts NER")),
    ("H", ("Engineering documents",
           "requirements, safety standards and patents")),
    ("I", ("In-car voice assistants & dialogue",
           "in-car task-oriented dialogue, SLU intent/slot, in-vehicle ASR/speech, driver-vehicle interaction")),
    ("J", ("Driving-scene language & multimodal",
           "Talk2Car, nuScenes-QA, DriveLM, BDD-X, LingoQA, HAD, DRAMA, referring expressions, driving captions")),
    ("K", ("Search, queries & semantic parsing",
           "NL-to-structured automotive search, query logs, synthetic query corpora, text-to-SQL on car data")),
    ("L", ("Market, pricing & listing tables with text",
           "used-car price datasets that carry free text, Craigslist/Kaggle car listings")),
    ("M", ("Knowledge graphs, ontologies & lexicons",
           "automotive ontologies (e.g. VSS), KGs, taxonomies, lexicons")),
])

# One emoji at the start of each section and top-level heading (sub-headings get none). In the anchor GitHub
# drops the emoji, keeps the following space as a leading "-", and KEEPS a variation selector (U+FE0F, a
# combining mark): "🗂️ Taxonomy" -> "#\uFE0F-taxonomy" (checked against the GitHub Markdown API).
HEADING_EMOJI = {
    "A": "\U0001F697", "B": "\U0001F3F7\uFE0F", "C": "\U0001F9E9", "D": "\u2B50", "E": "\u26A0\uFE0F",
    "F": "\U0001F4D8", "G": "\U0001F527", "H": "\U0001F4D0", "I": "\U0001F5E3\uFE0F", "J": "\U0001F6E3\uFE0F",
    "K": "\U0001F50E", "L": "\U0001F4B7", "M": "\U0001F578\uFE0F",
    "Taxonomy": "\U0001F5C2\uFE0F", "Related papers (no public data)": "\U0001F4C4",
    "How to cite": "\U0001F4DD", "Contributing": "\U0001F91D", "Contents": "\U0001F4D1",
}

# Modality pages: YAML value -> (file stem, emoji, page title). Order is the order of the "Browse by modality" line.
MODALITY_PAGES = OrderedDict([
    ("text", ("text", "\U0001F4DD", "Text")),
    ("speech", ("speech", "\U0001F399\uFE0F", "Speech")),
    ("multimodal", ("multimodal", "\U0001F3AC", "Multimodal")),
    ("image", ("image", "\U0001F5BC\uFE0F", "Images")),
    ("tabular+text", ("tabular-text", "\U0001F4CA", "Tabular + text")),
])
MODALITY_DIR = "modalities"

# Optional merging of thin buckets into a neighbour, e.g. {"L": "B"}. Empty: every bucket renders on its own.
MERGE_INTO: dict = {}
MIN_ROWS = 3

# One italic line rendered directly under a section heading (explains a gap or points elsewhere).
SECTION_NOTES = {
    "C": ("No public automotive-specific attribute-extraction or catalogue-linking corpus was found. "
          "Auto-Features (to be released, listed below) is built for this task; the general product-attribute "
          "sets MAVE, OA-Mine and AE-110K contain no automotive category."),
    "J": ("For papers and models on language in autonomous driving, see "
          "[Awesome-LLM4AD](https://github.com/Thinklab-SJTU/Awesome-LLM4AD), which this section complements; "
          "it lists corpora only."),
    "K": ("Spider's car_1 database is the only public automotive slice found. No open corpus maps "
          "natural-language car-search queries to structured filters."),
    "L": ("Used-car price and specification tables without free text are not NLP corpora and are not listed. "
          "Listing corpora with free text are in section B."),
}

# Controlled vocabulary for task_short (documented in CONTRIBUTING.md). One label, or two joined by " + ".
TASK_LABELS = (
    "NER", "fine-grained NER", "span labelling", "entity linking", "relation extraction",
    "ABSA", "sentiment", "summarisation", "classification",
    "QA", "VQA", "video QA", "captioning", "explanation", "grounding", "retrieval", "hallucination",
    "dialogue", "tool calling", "SLU", "ASR", "audio-visual ASR", "noise / acoustics",
    "image classification", "re-identification", "damage detection",
    "semantic parsing", "text-to-SQL",
    "complaint text", "recall text", "investigation text", "service bulletins", "crash narratives",
    "incident reports",
    "KG / ontology", "gazetteer", "lexicon", "schema / standard", "VIN decoding",
    "patents", "requirements", "listings",
)
TASK_SHORT_MAX = 22
SIZE_SHORT_MAX = 26

ACCESS_VALUES = ("public", "request", "paper only (contact authors)", "forthcoming", "unreleased", "unknown")
# Labels shown in the Access column; the YAML keeps the values above.
ACCESS_LABELS = {"public": "open", "request": "on request",
                 "paper only (contact authors)": "paper only", "forthcoming": "to be released"}
MODALITY_VALUES = tuple(MODALITY_PAGES)
LICENCE_MAX = 40

NoneType = type(None)
# Every key below must be present in every entry (null only where NoneType is accepted).
REQUIRED_FIELDS = {
    "name": (str,),
    "aliases": (list,),
    "section": (str,),
    "subsection": (str,),   # "" allowed: rows without a sub-heading
    "task_type": (str,),    # full description (exports)
    "task_short": (str,),   # Task column
    "modality": (str,),
    "language": (str,),
    "domain_subtopic": (str,),
    "size": (str,),         # as stated by the source (exports)
    "size_short": (str,),   # Size column
    "license": (str,),
    "access": (str,),
    "dataset_url": (str, NoneType),
    "paper_url": (str, NoneType),
    "year": (int, NoneType),
    "cited_in": (list,),
    "bibkey": (str, NoneType),
    "source_quote": (str,),
    "verified": (bool,),
    "notes": (str,),
}
OPTIONAL_FIELDS = {
    "ours": (bool,),    # the list author's own corpora (exported; false when absent)
    "authors": (str,),  # short form, e.g. "Hu and Ma"; shown after the name (exported; null when absent)
}
OPTIONAL_DEFAULTS = {"ours": False, "authors": None}
# Column order of the CSV and JSON exports (the YAML field order).
EXPORT_FIELDS = ["name", "aliases", "section", "subsection", "ours", "authors", "task_type", "task_short",
                 "modality", "language", "domain_subtopic", "size", "size_short", "license", "access",
                 "dataset_url", "paper_url", "year", "cited_in", "bibkey", "source_quote", "verified", "notes"]
NON_EMPTY_STRINGS = ("name", "task_type", "task_short", "modality", "language", "domain_subtopic",
                     "size", "size_short", "license", "access", "source_quote")
URL_RE = re.compile(r"^https?://\S+$")
DASH = "\u2014"
DOT = " \u00b7 "
ELLIPSIS = "\u2026"
DATE_LINE = "_Generated on "


# --------------------------------------------------------------------------- loading / validation

def load_entries(path: Path) -> list:
    rel = path.relative_to(ROOT)
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        sys.stderr.write(f"build_readme.py: cannot read {rel}: {exc}\n")
        sys.exit(2)
    if not isinstance(data, dict) or not isinstance(data.get("entries"), list):
        sys.stderr.write(f"build_readme.py: {rel} must be a mapping with a top-level 'entries' list\n")
        sys.exit(2)
    return data["entries"]


def type_ok(value, types) -> bool:
    # bool is a subclass of int: do not let `year: true` pass as an int.
    if isinstance(value, bool):
        return bool in types
    return isinstance(value, types)


def validate(entries: list, label: str, *, papers: bool = False) -> list:
    errors = []

    def err(entry, index, message):
        name = entry.get("name") if isinstance(entry, dict) else None
        ident = f"'{name}'" if isinstance(name, str) and name.strip() else f"entry #{index + 1} (unnamed)"
        errors.append(f"{label}: {ident}: {message}")

    for i, e in enumerate(entries):
        if not isinstance(e, dict):
            err({}, i, "entry is not a mapping")
            continue
        for field, types in REQUIRED_FIELDS.items():
            if field not in e:
                err(e, i, f"missing required field '{field}'")
            elif not type_ok(e[field], types):
                wanted = " or ".join("null" if t is NoneType else t.__name__ for t in types)
                err(e, i, f"field '{field}' must be {wanted}, got {type(e[field]).__name__}")
        for field, types in OPTIONAL_FIELDS.items():
            if field in e and not type_ok(e[field], types):
                err(e, i, f"field '{field}' must be {types[0].__name__}")
        for field in e:
            if field not in REQUIRED_FIELDS and field not in OPTIONAL_FIELDS:
                err(e, i, f"unknown field '{field}'")
        for field in NON_EMPTY_STRINGS:
            if isinstance(e.get(field), str) and not e[field].strip():
                err(e, i, f"field '{field}' is empty")

        section = e.get("section")
        if isinstance(section, str) and section not in BUCKETS:
            err(e, i, f"section '{section}' is not a bucket code {next(iter(BUCKETS))}-{next(reversed(BUCKETS))}")
        access = e.get("access")
        if isinstance(access, str) and access not in ACCESS_VALUES:
            if access == "commercial":
                err(e, i, "access 'commercial': fee-based commercial catalogues are excluded by the "
                          "inclusion rule (CONTRIBUTING.md); remove the entry")
            else:
                err(e, i, f"access '{access}' is not one of {list(ACCESS_VALUES)}")
        modality = e.get("modality")
        if isinstance(modality, str) and modality not in MODALITY_VALUES:
            err(e, i, f"modality '{modality}' is not one of {list(MODALITY_VALUES)}")
        task_short = e.get("task_short")
        if isinstance(task_short, str) and task_short.strip():
            if len(task_short) > TASK_SHORT_MAX:
                err(e, i, f"task_short '{task_short}' is {len(task_short)} characters (max {TASK_SHORT_MAX})")
            parts = task_short.split(" + ")
            if len(parts) > 2:
                err(e, i, f"task_short '{task_short}' joins more than two labels")
            for part in parts:
                if part not in TASK_LABELS:
                    err(e, i, f"task_short label '{part}' is not in the vocabulary (CONTRIBUTING.md)")
        size_short = e.get("size_short")
        if isinstance(size_short, str) and len(size_short) > SIZE_SHORT_MAX:
            err(e, i, f"size_short '{size_short}' is {len(size_short)} characters (max {SIZE_SHORT_MAX})")
        for field in ("dataset_url", "paper_url"):
            value = e.get(field)
            if isinstance(value, str) and not URL_RE.match(value):
                err(e, i, f"{field} must be null or an http(s) URL, got '{value}'")
        year = e.get("year")
        if type_ok(year, (int,)) and not 1950 <= year <= 2100:
            err(e, i, f"year {year} is out of range")
        for field in ("aliases", "cited_in"):
            value = e.get(field)
            if isinstance(value, list) and not all(isinstance(x, str) and x.strip() for x in value):
                err(e, i, f"{field} must be a list of non-empty strings")

        # Cross-field consistency.
        dataset_url = e.get("dataset_url")
        if access == "public" and dataset_url is None:
            err(e, i, "access 'public' requires a dataset_url")
        if access == "paper only (contact authors)" and dataset_url is not None:
            err(e, i, "access 'paper only (contact authors)' requires dataset_url null")
        if access == "forthcoming" and dataset_url is not None:
            err(e, i, "access 'forthcoming' requires dataset_url null (on release set the link and access 'public')")
        if papers and dataset_url is not None:
            err(e, i, "papers.yaml is for papers with no public data; an entry with a dataset_url belongs in corpora.yaml")
        if e.get("verified") is True and dataset_url is None and e.get("paper_url") is None:
            err(e, i, "verified is true but neither dataset_url nor paper_url is set")
    return errors


def check_duplicates(files: list) -> list:
    errors, seen = [], {}
    for label, entries in files:
        for e in entries:
            name = e.get("name") if isinstance(e, dict) else None
            if not isinstance(name, str):
                continue
            key = name.strip().casefold()
            if key in seen:
                errors.append(f"{label}: '{name}': duplicate name (already in {seen[key]})")
            else:
                seen[key] = label
    return errors


# --------------------------------------------------------------------------- rendering helpers

def esc(text) -> str:
    """Make a value safe inside a Markdown table cell (pipes; single tildes would strike text through)."""
    s = "" if text is None else str(text)
    return s.replace("|", "\\|").replace("~", "\\~").replace("\n", " ").strip()


def slug(heading: str) -> str:
    """GitHub-style anchor for a Markdown heading (before duplicate suffixing), as github-slugger does it:
    lower-case; keep letters, combining marks, numbers, "_", "-" and spaces; drop everything else (punctuation,
    emoji); spaces become "-". So "🚗 A. Cars & vans" -> "-a-cars--vans" and "🗂️ Taxonomy" -> "\uFE0F-taxonomy"."""
    kept = [ch for ch in heading.strip().lower()
            if ch in " -" or unicodedata.category(ch)[0] in "LMN" or unicodedata.category(ch) == "Pc"]
    return "".join(kept).replace(" ", "-")


def title(key: str, text: str = None) -> str:
    """Heading text with its emoji, e.g. title("Taxonomy") -> "🗂️ Taxonomy"."""
    text = key if text is None else text
    emoji = HEADING_EMOJI.get(key)
    return f"{emoji} {text}" if emoji else text


def section_title(code: str) -> str:
    return title(code, f"{code}. {BUCKETS[code][0]}")


def anchor(key: str, text: str = None) -> str:
    return "#" + slug(title(key, text))


def by_name(entries: list) -> list:
    return sorted(entries, key=lambda e: e["name"].casefold())


def licence_short(value) -> str:
    """Text before the first ' (' or ';', trimmed, at most LICENCE_MAX characters; 'unknown' if empty."""
    s = (value or "").strip()
    cut = len(s)
    for sep in (" (", ";"):
        i = s.find(sep)
        if i != -1:
            cut = min(cut, i)
    s = s[:cut].strip()
    if not s:
        return "unknown"
    if len(s) > LICENCE_MAX:
        window = s[:LICENCE_MAX - 1]
        space = window.rfind(" ")
        # Cut at a word boundary unless that would drop too much (e.g. the NonCommercial part of a CC name).
        window = window[:space].rstrip(" ,;:-/") if space >= 24 else window.rstrip()
        s = window + ELLIPSIS
    return s


def links_cell(e: dict) -> str:
    parts = []
    if e["access"] == "forthcoming" and e["dataset_url"] is None:
        parts.append("to be released")
    elif e["dataset_url"]:
        parts.append(f"[data]({e['dataset_url']})")
    elif e["access"] == "paper only (contact authors)":
        parts.append("paper only")
    if e["paper_url"]:
        parts.append(f"[paper]({e['paper_url']})")
    return DOT.join(parts) if parts else DASH


def year_cell(e: dict) -> str:
    return DASH if e["year"] is None else str(e["year"])


def cited_cell(e: dict) -> str:
    return esc(", ".join(e["cited_in"])) if e["cited_in"] else DASH


def name_cell(e: dict) -> str:
    # Aliases stay in the YAML and the exports (for search); they are not rendered.
    name = esc(e["name"])
    if e.get("authors"):
        name += f" ({esc(e['authors'])})"
    return name


def corpus_table(entries: list, *, with_modality: bool = True) -> str:
    cols = ["Corpus", "Task"] + (["Modality"] if with_modality else []) + \
           ["Lang", "Size", "Licence", "Access", "Year", "Links", "Cited in"]
    lines = ["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
    for e in entries:
        cells = [name_cell(e), esc(e["task_short"])] + ([esc(e["modality"])] if with_modality else []) + \
                [esc(e["language"]), esc(e["size_short"]), esc(licence_short(e["license"])),
                 esc(ACCESS_LABELS.get(e["access"], e["access"])), year_cell(e), links_cell(e), cited_cell(e)]
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines)


def paper_table(entries: list) -> str:
    lines = ["| Paper | Task | Lang | Year | Link | Cited in |", "|---|---|---|---|---|---|"]
    for e in entries:
        link = f"[paper]({e['paper_url']})" if e["paper_url"] else DASH
        lines.append("| " + " | ".join([name_cell(e), esc(e["task_short"]), esc(e["language"]),
                                         year_cell(e), link, cited_cell(e)]) + " |")
    return "\n".join(lines)


# --------------------------------------------------------------------------- sections

def group_sections(corpora: list) -> list:
    """Return [(code, entries, notes, subsections)] for every bucket A-M, in order.

    subsections is [(subsection, entries)]: the "" group first, then named sub-headings in
    first-appearance order from the YAML; rows within each group are sorted by name.
    """
    groups = {code: [] for code in BUCKETS}
    for e in corpora:
        groups[e["section"]].append(e)
    merged_from = {code: [] for code in BUCKETS}
    for src, dst in MERGE_INTO.items():
        if 0 < len(groups[src]) < MIN_ROWS:
            groups[dst].extend(groups[src])
            merged_from[dst].append(src)
            groups[src] = []
    sections = []
    for code in BUCKETS:
        entries = groups[code]
        notes = [SECTION_NOTES[code]] if code in SECTION_NOTES else []
        notes += [f"Bucket {src} ({BUCKETS[src][0]}) has fewer than {MIN_ROWS} entries and is merged into this section."
                  for src in merged_from[code]]
        order = []
        for e in entries:
            if e["subsection"] not in order:
                order.append(e["subsection"])
        order.sort(key=lambda s: s != "")  # stable: the "" group first, named ones keep their order
        subsections = [(s, by_name([e for e in entries if e["subsection"] == s])) for s in order]
        sections.append((code, entries, notes, subsections))
    return sections


def language_counts(corpora: list):
    """(languages, others): ranked (tag, count) pairs. Base languages are counted, so
    "Chinese (Taiwan Mandarin)" counts as Chinese; Cantonese stays separate. 'n/a ...', 'unknown' and
    'Multilingual' are listed last and not counted as languages."""
    tags = Counter()
    for e in corpora:
        tags.update({t.strip() if t.strip().startswith("n/a") else t.split(" (")[0].strip()
                     for t in e["language"].split(", ") if t.strip()})

    def not_a_language(tag):
        t = tag.casefold()
        return t.startswith("n/a") or t in ("unknown", "multilingual")

    def rank(items):
        return sorted(items, key=lambda kv: (-kv[1], kv[0].casefold()))

    languages = rank([(t, n) for t, n in tags.items() if not not_a_language(t)])
    others = rank([(t, n) for t, n in tags.items() if not_a_language(t)])
    return languages, others


def unique_count(corpora: list) -> int:
    return len({e["name"].strip().casefold() for e in corpora})


def languages_line(corpora: list) -> str:
    languages, others = language_counts(corpora)
    return "**Languages:** " + DOT.join(f"{esc(t)} {n}" for t, n in languages + others)


def in_languages(n: int) -> str:
    """" in 11 languages", " in 1 language", or "" when no row has a language (image-only pages)."""
    return "" if n == 0 else f" in {n} language{'' if n == 1 else 's'}"


def render_summary(corpora: list) -> str:
    modalities = Counter(e["modality"] for e in corpora)
    mod_text = ", ".join(f"{n} {m}" for m, n in sorted(modalities.items(), key=lambda kv: (-kv[1], kv[0])))
    languages, _others = language_counts(corpora)
    summary = f"**{unique_count(corpora)} corpora** ({mod_text}){in_languages(len(languages))}."
    return summary + "\n\n" + languages_line(corpora)


def render_badges(corpora: list) -> str:
    n_languages = len(language_counts(corpora)[0])
    return " ".join([
        "[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)",
        "[![Licence: CC BY 4.0](https://img.shields.io/badge/licence-CC%20BY%204.0-lightgrey.svg)](LICENSE)",
        f"![Corpora: {unique_count(corpora)}](https://img.shields.io/badge/corpora-{unique_count(corpora)}-blue.svg)",
        f"![Languages: {n_languages}](https://img.shields.io/badge/languages-{n_languages}-blue.svg)",
    ])


def by_modality(corpora: list) -> "OrderedDict[str, list]":
    return OrderedDict((m, [e for e in corpora if e["modality"] == m]) for m in MODALITY_PAGES)


def render_browse(corpora: list) -> str:
    groups = by_modality(corpora)
    assert sum(len(v) for v in groups.values()) == len(corpora)
    parts = [f"[{label}]({MODALITY_DIR}/{stem}.md) ({len(groups[m])})"
             for m, (stem, _emoji, label) in MODALITY_PAGES.items()]
    return "**Browse by modality:** " + DOT.join(parts)


def contents_section_lines(sections: list, *, indent: str = "  ") -> list:
    return [f"{indent}- [{section_title(code)}]({anchor(code, f'{code}. {BUCKETS[code][0]}')}) ({len(entries)})"
            for code, entries, _notes, _subs in sections]


def render_contents(sections: list, papers: list) -> str:
    lines = [f"- [{title('Taxonomy')}]({anchor('Taxonomy')})",
             "- [Corpora by application area](#corpora-by-application-area)"]
    lines += contents_section_lines(sections)
    lines.append(f"- [Browse by modality]({MODALITY_DIR}/README.md)")
    lines.append(f"- [{title('Related papers (no public data)')}]({anchor('Related papers (no public data)')}) ({len(papers)})")
    lines.append(f"- [{title('How to cite')}]({anchor('How to cite')})")
    lines.append(f"- [{title('Contributing')}]({anchor('Contributing')})")
    return "\n".join(lines)


def render_sections(sections: list, *, with_modality: bool = True, keep_empty: bool = True) -> str:
    out = ["## Corpora by application area", ""]
    for code, entries, notes, subsections in sections:
        if not entries and not keep_empty:
            continue
        out += [f"### {section_title(code)}", ""]
        for note in notes:
            out += [f"*{note}*", ""]
        if not entries and not notes:
            out += ["_No entries yet._", ""]
        for subsection, rows in subsections:
            if subsection:
                out += [f"#### {subsection}", ""]
            out += [corpus_table(rows, with_modality=with_modality), ""]
    return "\n".join(out).rstrip()


def render_papers(papers: list) -> str:
    out = [f"## {title('Related papers (no public data)')}", "",
           "Automotive NLP papers with no public corpus: each describes a system, benchmark or evaluation whose "
           "data has not been released. They are listed with the academic reference so that readers can contact "
           "the authors.", ""]
    if papers:
        out.append(paper_table(sorted(papers, key=lambda e: (e["section"], e["name"].casefold()))))
    else:
        out.append("_No entries yet._")
    return "\n".join(out)


def render_taxonomy() -> str:
    lines = [f"- **{section_title(code)}**: {definition}" for code, (_name, definition) in BUCKETS.items()]
    if MERGE_INTO:
        merges = "; ".join(f"{src} into {dst}" for src, dst in MERGE_INTO.items())
        lines += ["", f"A bucket with fewer than {MIN_ROWS} entries is merged into its named neighbour by the "
                      f"renderer ({merges}) and the section says so."]
    return "\n".join(lines)


def render_readme(template: str, corpora: list, papers: list, sections: list) -> str:
    replacements = {
        "{{BADGES}}": render_badges(corpora),
        "{{SUMMARY}}": render_summary(corpora),
        "{{BROWSE}}": render_browse(corpora),
        "{{CONTENTS}}": render_contents(sections, papers),
        "{{TAXONOMY}}": render_taxonomy(),
        "{{SECTIONS}}": render_sections(sections),
        "{{PAPERS}}": render_papers(papers),
        "{{DATE}}": dt.date.today().isoformat(),
    }
    output = template
    for token, text in replacements.items():
        output = output.replace(token, text)  # plain replace: the BibTeX braces must survive untouched
    # {{H2:Name}} -> "## <emoji> Name"; {{A:Name}} -> its anchor (e.g. "-contributing").
    output = re.sub(r"\{\{H2:([^}]+)\}\}", lambda m: f"## {title(m.group(1))}", output)
    output = re.sub(r"\{\{A:([^}]+)\}\}", lambda m: slug(title(m.group(1))), output)
    leftover = re.findall(r"\{\{[A-Z0-9_]+(?::[^}]*)?\}\}", output)
    if leftover:
        raise ValueError(f"unreplaced template token(s): {leftover}")
    return re.sub(r"\n{3,}", "\n\n", output).rstrip() + "\n"


def render_modality_page(modality: str, rows: list) -> str:
    stem, emoji, label = MODALITY_PAGES[modality]
    sections = group_sections(rows)
    present = [s for s in sections if s[1]]
    languages, _ = language_counts(rows)
    out = [f"# {emoji} {label}", "",
           f"Part of [awesome-automotive-nlp](../README.md). Same taxonomy as the main list: see "
           f"[Taxonomy](../README.md{anchor('Taxonomy')}).", "",
           f"**{unique_count(rows)} corpora**{in_languages(len(languages))}.", "",
           languages_line(rows), "",
           f"## {title('Contents')}", "",
           "- [Corpora by application area](#corpora-by-application-area)"]
    out += contents_section_lines(present)
    out += ["", render_sections(present, with_modality=False, keep_empty=False), "", "---", "",
            f"_Generated by `python scripts/build_readme.py` from `data/corpora.yaml`. "
            f"Do not edit this page by hand._"]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out)).rstrip() + "\n"


def render_modality_index(corpora: list) -> str:
    groups = by_modality(corpora)
    out = ["# Browse by modality", "",
           "Part of [awesome-automotive-nlp](../README.md). Each page lists the corpora of one modality under the "
           "same taxonomy, sections and sub-headings as the main list.", "",
           "| Modality | Corpora | Languages | Page |", "|---|---|---|---|"]
    for m, (stem, emoji, label) in MODALITY_PAGES.items():
        rows = groups[m]
        out.append(f"| {emoji} {label} | {len(rows)} | {len(language_counts(rows)[0]) or 'n/a'} | [{stem}.md]({stem}.md) |")
    out += ["", "---", "",
            "_Generated by `python scripts/build_readme.py` from `data/corpora.yaml`. Do not edit this page by hand._"]
    return "\n".join(out) + "\n"


# --------------------------------------------------------------------------- exports

def export_records(entries: list) -> list:
    return [{f: (e[f] if f in e else OPTIONAL_DEFAULTS[f]) for f in EXPORT_FIELDS} for e in entries]


def to_json(entries: list) -> str:
    return json.dumps(export_records(entries), ensure_ascii=False, indent=2) + "\n"


def to_csv(entries: list) -> str:
    def cell(value):
        if value is None:
            return ""
        if isinstance(value, bool):
            return "true" if value else "false"
        if isinstance(value, list):
            return "; ".join(value)
        return str(value)

    buf = io.StringIO()
    writer = csv.writer(buf, quoting=csv.QUOTE_MINIMAL, lineterminator="\n")
    writer.writerow(EXPORT_FIELDS)
    for record in export_records(entries):
        writer.writerow([cell(record[f]) for f in EXPORT_FIELDS])
    return buf.getvalue()


# --------------------------------------------------------------------------- link and anchor checks

def heading_targets(markdown: str):
    """Return ({anchor: heading text} after GitHub's -1, -2 suffixing, Counter of raw slugs)."""
    headings, in_code = [], False
    for line in markdown.splitlines():
        if line.startswith("```"):
            in_code = not in_code
            continue
        if not in_code:
            m = re.match(r"^#{1,6}\s+(.+?)\s*$", line)
            if m:
                headings.append(m.group(1))
    raw = Counter(slug(h) for h in headings)
    seen, target_of = {}, {}
    for h in headings:
        s = slug(h)
        if s in seen:
            seen[s] += 1
            s = f"{s}-{seen[s]}"
        else:
            seen[s] = 0
        target_of[s] = h
    return target_of, raw


def check_links(pages: dict, extra_files: set) -> list:
    """pages: {repo-relative path: markdown}. Every relative link must reach a file that exists (on disk,
    generated now, or in extra_files); every #anchor must match a heading of the target page; every
    Contents link must land on the heading it names, and on no other."""
    targets = {path: heading_targets(md) for path, md in pages.items()}
    errors = []
    for path, md in pages.items():
        base = posixpath.dirname(path)
        in_code, in_contents = False, False
        for line in md.splitlines():
            if line.startswith("```"):
                in_code = not in_code
                continue
            if in_code:
                continue
            if line.startswith("## "):
                in_contents = line == f"## {title('Contents')}"
            for target in re.findall(r"\]\(([^)\s]+)\)", line):
                if re.match(r"^(https?:|mailto:)", target):
                    continue
                file_part, _, frag = target.partition("#")
                dest = posixpath.normpath(posixpath.join(base, file_part)) if file_part else path
                if dest.startswith(".."):
                    errors.append(f"{path}: link '{target}' points outside the repository")
                    continue
                if dest not in pages and dest not in extra_files and not (ROOT / dest).exists():
                    errors.append(f"{path}: link '{target}' points to a missing file '{dest}'")
                    continue
                if frag:
                    if dest not in targets:
                        errors.append(f"{path}: link '{target}' has an anchor into a non-generated file")
                    elif frag not in targets[dest][0]:
                        errors.append(f"{path}: link '{target}' has no matching heading in {dest}")
            if in_contents:
                for text, target in re.findall(r"\[([^\]]+)\]\(#([^)\s]+)\)", line):
                    target_of, raw = targets[path]
                    if target in target_of and target_of[target] != text:
                        errors.append(f"{path}: Contents link '[{text}](#{target})' lands on '{target_of[target]}'")
                    elif raw[target] > 1:
                        errors.append(f"{path}: Contents target '#{target}' is shared by {raw[target]} headings")
    return errors


# --------------------------------------------------------------------------- main

def strip_date(text: str) -> str:
    return "\n".join(l for l in text.splitlines() if not l.startswith(DATE_LINE))


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Validate data/*.yaml; render README.md, modalities/ and exports.")
    parser.add_argument("--check", action="store_true",
                        help="write nothing; fail if README.md, modalities/ or the exports are out of date")
    args = parser.parse_args(argv)

    corpora = load_entries(CORPORA_FILE)
    papers = load_entries(PAPERS_FILE)
    errors = (validate(corpora, "data/corpora.yaml")
              + validate(papers, "data/papers.yaml", papers=True)
              + check_duplicates([("data/corpora.yaml", corpora), ("data/papers.yaml", papers)]))
    if errors:
        for message in errors:
            print("ERROR " + message, file=sys.stderr)
        print(f"build_readme.py: {len(errors)} validation error(s); nothing written", file=sys.stderr)
        return 1
    print(f"Validated {len(corpora)} corpora and {len(papers)} related paper(s): no errors.")

    try:
        template = TEMPLATE_FILE.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"build_readme.py: cannot read template: {exc}", file=sys.stderr)
        return 2
    sections = group_sections(corpora)
    try:
        readme = render_readme(template, corpora, papers, sections)
    except ValueError as exc:
        print(f"build_readme.py: {exc}", file=sys.stderr)
        return 2

    pages = {"README.md": readme, f"{MODALITY_DIR}/README.md": render_modality_index(corpora)}
    for modality, rows in by_modality(corpora).items():
        pages[f"{MODALITY_DIR}/{MODALITY_PAGES[modality][0]}.md"] = render_modality_page(modality, rows)
    exports = {"data/corpora.json": to_json(corpora), "data/corpora.csv": to_csv(corpora),
               "data/papers.json": to_json(papers), "data/papers.csv": to_csv(papers)}

    link_errors = check_links(pages, set(exports))
    if link_errors:
        for message in link_errors:
            print("ERROR " + message, file=sys.stderr)
        print("build_readme.py: broken link(s); nothing written", file=sys.stderr)
        return 1

    outputs = {**pages, **exports}
    if args.check:
        stale = []
        for path, text in outputs.items():
            target = ROOT / path
            current = target.read_text(encoding="utf-8") if target.exists() else None
            same = (current is not None and
                    (strip_date(current) == strip_date(text) if path == "README.md" else current == text))
            if not same:
                stale.append(path)
        expected = {p for p in pages if p.startswith(MODALITY_DIR + "/")}
        extra = sorted(f"{MODALITY_DIR}/{p.name}" for p in (ROOT / MODALITY_DIR).glob("*.md")
                       if f"{MODALITY_DIR}/{p.name}" not in expected) if (ROOT / MODALITY_DIR).is_dir() else []
        if stale or extra:
            for path in stale:
                print(f"ERROR out of date: {path} (run python scripts/build_readme.py and commit the result)",
                      file=sys.stderr)
            for path in extra:
                print(f"ERROR not generated by the renderer: {path} (delete it)", file=sys.stderr)
            return 1
        print(f"Links and anchors resolve on {len(pages)} pages. --check: all {len(outputs)} outputs are up to date.")
        return 0

    for path, text in outputs.items():
        target = ROOT / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")

    print("Sections rendered (rows; sub-headings):")
    for code, entries, notes, subs in sections:
        named = "; ".join(f"{s} {len(r)}" for s, r in subs if s)
        flat = sum(len(r) for s, r in subs if not s)
        detail = "; ".join(([f"(no sub-heading) {flat}"] if flat else []) + ([named] if named else []))
        print(f"  {code} {len(entries):3d}{' [note]' if notes else ''}  {detail}")
    print("Modality pages: " + ", ".join(f"{MODALITY_PAGES[m][2]} {len(r)}" for m, r in by_modality(corpora).items()))
    print(f"Links and anchors resolve on {len(pages)} pages.")
    print(f"Wrote {len(outputs)} files: " + ", ".join(outputs))
    return 0


if __name__ == "__main__":
    sys.exit(main())
