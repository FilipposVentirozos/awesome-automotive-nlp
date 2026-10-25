#!/usr/bin/env python3
"""Render README.md for awesome-automotive-nlp from data/corpora.yaml and data/papers.yaml.

Usage:
    python scripts/build_readme.py           validate both YAML files and write README.md
    python scripts/build_readme.py --check   validate only; do not write

Exit status: 0 on success; 1 if any entry fails validation (every failure is printed
to stderr with the entry name); 2 if a file cannot be read or parsed.

Dependencies: Python 3.9+ and PyYAML (pip install pyyaml). Nothing else.
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from collections import OrderedDict
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
README_FILE = ROOT / "README.md"

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
    ("F", ("Maintenance, repair, parts & technical documents",
           "auto-parts NER, repair/diagnostic QA, service records, manuals, patents")),
    ("G", ("In-car voice assistants & dialogue",
           "in-car task-oriented dialogue, SLU intent/slot, in-vehicle ASR/speech, driver-vehicle interaction")),
    ("H", ("Driving-scene language & multimodal",
           "Talk2Car, nuScenes-QA, DriveLM, BDD-X, LingoQA, HAD, DRAMA, referring expressions, driving captions")),
    ("I", ("Search, queries & semantic parsing",
           "NL-to-structured automotive search, query logs, synthetic query corpora, text-to-SQL on car data")),
    ("J", ("Market, pricing & listing tables with text",
           "used-car price datasets that carry free text, Craigslist/Kaggle car listings")),
    ("K", ("Knowledge graphs, ontologies & lexicons",
           "automotive ontologies (e.g. VSS), KGs, taxonomies, lexicons")),
])

# A bucket that ends with fewer than MIN_ROWS corpora is folded into the neighbour named here
# (TAXONOMY.md: "J into B; K into F"). To merge another bucket, add a pair.
MERGE_INTO = {"J": "B", "K": "F"}
MIN_ROWS = 3

ACCESS_VALUES = ("public", "request", "paper only (contact authors)", "forthcoming", "unreleased", "unknown")
MODALITY_VALUES = ("text", "speech", "multimodal", "image", "tabular+text")

NoneType = type(None)
# Every key below must be present in every entry (null only where NoneType is accepted).
REQUIRED_FIELDS = {
    "name": (str,),
    "aliases": (list,),
    "section": (str,),
    "task_type": (str,),
    "modality": (str,),
    "language": (str,),
    "domain_subtopic": (str,),
    "size": (str,),
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
    "ours": (bool,),    # the list author's own corpora; rendered first under "Our corpora"
    "authors": (str,),  # short form for papers.yaml rows, e.g. "Hu and Ma"
}
NON_EMPTY_STRINGS = ("name", "task_type", "modality", "language", "domain_subtopic",
                     "size", "license", "access", "source_quote")
URL_RE = re.compile(r"^https?://\S+$")
DASH = "\u2014"


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
            err(e, i, f"section '{section}' is not a bucket code A-K")
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
    """Make a value safe inside a Markdown table cell."""
    s = "" if text is None else str(text)
    return s.replace("|", "\\|").replace("\n", " ").strip()


def slug(heading: str) -> str:
    """GitHub-style anchor for a Markdown heading."""
    s = re.sub(r"[^\w\- ]", "", heading.strip().lower())
    return s.replace(" ", "-")


def by_name(entries: list) -> list:
    return sorted(entries, key=lambda e: e["name"].casefold())


def links_cell(e: dict) -> str:
    parts = []
    if e["access"] == "forthcoming" and e["dataset_url"] is None:
        parts.append("forthcoming (release pending)")
    elif e["dataset_url"]:
        parts.append(f"[data]({e['dataset_url']})")
    elif e["access"] == "paper only (contact authors)":
        parts.append("paper only")
    if e["paper_url"]:
        parts.append(f"[paper]({e['paper_url']})")
    return " \u00b7 ".join(parts) if parts else DASH


def year_cell(e: dict) -> str:
    return DASH if e["year"] is None else str(e["year"])


def cited_cell(e: dict) -> str:
    return esc(", ".join(e["cited_in"])) if e["cited_in"] else DASH


CORPUS_HEADER = ("| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |\n"
                 "|---|---|---|---|---|---|---|---|---|---|")
PAPER_HEADER = ("| Paper | Task | Lang | Year | Link | Cited in |\n"
                "|---|---|---|---|---|---|")


def corpus_row(e: dict) -> str:
    name = esc(e["name"])
    if e["aliases"]:
        name += " (also: " + esc(", ".join(e["aliases"])) + ")"
    cells = [name, esc(e["task_type"]), esc(e["modality"]), esc(e["language"]), esc(e["size"]),
             esc(e["license"]), esc(e["access"]), year_cell(e), links_cell(e), cited_cell(e)]
    return "| " + " | ".join(cells) + " |"


def paper_row(e: dict) -> str:
    title = esc(e["name"])
    if e.get("authors"):
        title += f" ({esc(e['authors'])})"
    link = f"[paper]({e['paper_url']})" if e["paper_url"] else DASH
    cells = [title, esc(e["task_type"]), esc(e["language"]), year_cell(e), link, cited_cell(e)]
    return "| " + " | ".join(cells) + " |"


def corpus_table(entries: list) -> str:
    return "\n".join([CORPUS_HEADER] + [corpus_row(e) for e in entries])


def paper_table(entries: list) -> str:
    return "\n".join([PAPER_HEADER] + [paper_row(e) for e in entries])


# --------------------------------------------------------------------------- sections

def group_sections(corpora: list) -> list:
    """Return [(code, heading, entries, notes)] for every non-empty bucket, after merging."""
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
    for code, (name, _definition) in BUCKETS.items():
        if not groups[code]:
            continue
        notes = [f"_Bucket {src} ({BUCKETS[src][0]}) has fewer than {MIN_ROWS} entries and is merged "
                 f"into this section._" for src in merged_from[code]]
        sections.append((code, f"{code}. {name}", by_name(groups[code]), notes))
    return sections


def render_contents(ours: list, sections: list, papers: list) -> str:
    lines = []
    if ours:
        lines.append(f"- [Our corpora](#{slug('Our corpora')}) ({len(ours)})")
    lines.append(f"- [Corpora by application area](#{slug('Corpora by application area')})")
    for _code, heading, entries, _notes in sections:
        lines.append(f"  - [{heading}](#{slug(heading)}) ({len(entries)})")
    lines.append(f"- [Related papers (no public data)](#{slug('Related papers (no public data)')}) ({len(papers)})")
    lines += ["- [Taxonomy](#taxonomy)", "- [How to cite](#how-to-cite)", "- [Contributing](#contributing)"]
    return "\n".join(lines)


def render_our_corpora(ours: list) -> str:
    if not ours:
        return ""
    return "\n".join([
        "## Our corpora", "",
        "The Auto Trader UK advertisement corpora this list grew out of. "
        "They are also listed under their application areas below.", "",
        corpus_table(ours),
    ])


def render_sections(sections: list) -> str:
    out = ["## Corpora by application area", ""]
    if not sections:
        out.append("_No entries yet._")
    for _code, heading, entries, notes in sections:
        out += [f"### {heading}", ""]
        for note in notes:
            out += [note, ""]
        out += [corpus_table(entries), ""]
    return "\n".join(out).rstrip()


def render_papers(papers: list) -> str:
    out = ["## Related papers (no public data)", "",
           "Automotive papers cited in our work that describe a resource without a recoverable download. "
           "The rows are kept, with the academic reference, so that readers can contact the authors.", ""]
    if papers:
        out.append(paper_table(sorted(papers, key=lambda e: (e["section"], e["name"].casefold()))))
    else:
        out.append("_No entries yet._")
    return "\n".join(out)


def render_taxonomy() -> str:
    lines = [f"- **{code}. {name}**: {definition}" for code, (name, definition) in BUCKETS.items()]
    merges = "; ".join(f"{src} into {dst}" for src, dst in MERGE_INTO.items())
    lines += ["", f"A bucket with fewer than {MIN_ROWS} entries is merged into its named neighbour by the renderer "
                  f"({merges}) and the section says so."]
    return "\n".join(lines)


# --------------------------------------------------------------------------- main

def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Validate data/*.yaml and render README.md.")
    parser.add_argument("--check", action="store_true", help="validate only; do not write README.md")
    args = parser.parse_args(argv)

    corpora = load_entries(CORPORA_FILE)
    papers = load_entries(PAPERS_FILE)
    errors = (validate(corpora, "data/corpora.yaml")
              + validate(papers, "data/papers.yaml", papers=True)
              + check_duplicates([("data/corpora.yaml", corpora), ("data/papers.yaml", papers)]))
    if errors:
        for message in errors:
            print("ERROR " + message, file=sys.stderr)
        print(f"build_readme.py: {len(errors)} validation error(s); README.md not written", file=sys.stderr)
        return 1
    print(f"Validated {len(corpora)} corpora and {len(papers)} related paper(s): no errors.")
    if args.check:
        return 0

    ours = sorted([e for e in corpora if e.get("ours")], key=lambda e: (e["section"], e["name"].casefold()))
    sections = group_sections(corpora)
    try:
        template = TEMPLATE_FILE.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"build_readme.py: cannot read template: {exc}", file=sys.stderr)
        return 2
    replacements = {
        "{{CONTENTS}}": render_contents(ours, sections, papers),
        "{{OUR_CORPORA}}": render_our_corpora(ours),
        "{{SECTIONS}}": render_sections(sections),
        "{{PAPERS}}": render_papers(papers),
        "{{TAXONOMY}}": render_taxonomy(),
        "{{DATE}}": dt.date.today().isoformat(),
    }
    output = template
    for token, text in replacements.items():
        output = output.replace(token, text)  # plain replace: the BibTeX braces must survive untouched
    leftover = re.findall(r"\{\{[A-Z_]+\}\}", output)
    if leftover:
        print(f"build_readme.py: unreplaced template token(s): {leftover}", file=sys.stderr)
        return 2
    output = re.sub(r"\n{3,}", "\n\n", output).rstrip() + "\n"
    README_FILE.write_text(output, encoding="utf-8")

    counts = ", ".join(f"{code}={len(entries)}" for code, _h, entries, _n in sections) or "none"
    print(f"Sections rendered: {counts}; our corpora: {len(ours)}; related papers: {len(papers)}.")
    print(f"Wrote {README_FILE.relative_to(ROOT)} ({output.count(chr(10))} lines).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
