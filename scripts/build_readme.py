#!/usr/bin/env python3
"""Render README.md for awesome-automotive-nlp from data/corpora.yaml and data/papers.yaml.

Usage:
    python scripts/build_readme.py           validate both YAML files and write README.md
    python scripts/build_readme.py --check   validate only; do not write

Exit status: 0 on success; 1 if any entry fails validation (every failure is printed
to stderr with the entry name) or if a Contents link would not resolve; 2 if a file
cannot be read or parsed.

Dependencies: Python 3.9+ and PyYAML (pip install pyyaml). Nothing else.
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
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

# Optional merging of thin buckets into a neighbour, e.g. {"J": "B"}. Empty: every bucket renders on its own.
MERGE_INTO: dict = {}
MIN_ROWS = 3

# One italic line rendered directly under a section heading (explains a gap or points elsewhere).
SECTION_NOTES = {
    "C": ("No public automotive-specific attribute-extraction or catalogue-linking corpus was found. "
          "Auto-Features (forthcoming, under Our corpora) is built for this task; the general product-attribute "
          "sets MAVE, OA-Mine and AE-110K contain no automotive category."),
    "H": ("For papers and models on language in autonomous driving, see "
          "[Awesome-LLM4AD](https://github.com/Thinklab-SJTU/Awesome-LLM4AD), which this section complements; "
          "it lists corpora only."),
    "I": ("Spider's car_1 database is the only public automotive slice found. No open corpus maps "
          "natural-language car-search queries to structured filters."),
    "J": ("Used-car price and specification tables without free text are not NLP corpora and are not listed. "
          "Listing corpora with free text are in section B."),
}

ACCESS_VALUES = ("public", "request", "paper only (contact authors)", "forthcoming", "unreleased", "unknown")
# Labels shown in the Access column; the YAML keeps the values above.
ACCESS_LABELS = {"public": "open", "request": "on request",
                 "paper only (contact authors)": "paper only", "forthcoming": "forthcoming"}
MODALITY_VALUES = ("text", "speech", "multimodal", "image", "tabular+text")
LICENCE_MAX = 40

NoneType = type(None)
# Every key below must be present in every entry (null only where NoneType is accepted).
REQUIRED_FIELDS = {
    "name": (str,),
    "aliases": (list,),
    "section": (str,),
    "subsection": (str,),   # "" allowed: rows without a sub-heading
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
    "authors": (str,),  # short form, e.g. "Hu and Ma"; shown after the name
}
NON_EMPTY_STRINGS = ("name", "task_type", "modality", "language", "domain_subtopic",
                     "size", "license", "access", "source_quote")
URL_RE = re.compile(r"^https?://\S+$")
DASH = "\u2014"
ELLIPSIS = "\u2026"


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
    """Make a value safe inside a Markdown table cell (pipes; single tildes would strike text through)."""
    s = "" if text is None else str(text)
    return s.replace("|", "\\|").replace("~", "\\~").replace("\n", " ").strip()


def slug(heading: str) -> str:
    """GitHub-style anchor for a Markdown heading (before duplicate suffixing)."""
    s = re.sub(r"[^\w\- ]", "", heading.strip().lower())
    return s.replace(" ", "-")


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


def name_cell(e: dict) -> str:
    # Aliases stay in the YAML (for search); they are not rendered.
    name = esc(e["name"])
    if e.get("authors"):
        name += f" ({esc(e['authors'])})"
    return name


CORPUS_HEADER = ("| Corpus | Task | Modality | Lang | Size | Licence | Access | Year | Links | Cited in |\n"
                 "|---|---|---|---|---|---|---|---|---|---|")
PAPER_HEADER = ("| Paper | Task | Lang | Year | Link | Cited in |\n"
                "|---|---|---|---|---|---|")


def corpus_row(e: dict) -> str:
    cells = [name_cell(e), esc(e["task_type"]), esc(e["modality"]), esc(e["language"]), esc(e["size"]),
             esc(licence_short(e["license"])), esc(ACCESS_LABELS.get(e["access"], e["access"])),
             year_cell(e), links_cell(e), cited_cell(e)]
    return "| " + " | ".join(cells) + " |"


def paper_row(e: dict) -> str:
    link = f"[paper]({e['paper_url']})" if e["paper_url"] else DASH
    cells = [name_cell(e), esc(e["task_type"]), esc(e["language"]), year_cell(e), link, cited_cell(e)]
    return "| " + " | ".join(cells) + " |"


def corpus_table(entries: list) -> str:
    return "\n".join([CORPUS_HEADER] + [corpus_row(e) for e in entries])


def paper_table(entries: list) -> str:
    return "\n".join([PAPER_HEADER] + [paper_row(e) for e in entries])


# --------------------------------------------------------------------------- sections

def group_sections(corpora: list) -> list:
    """Return [(code, heading, entries, notes, subsections)] for every bucket A-K, in order.

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
    for code, (name, _definition) in BUCKETS.items():
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
        sections.append((code, f"{code}. {name}", entries, notes, subsections))
    return sections


def render_summary(corpora: list) -> str:
    total = len({e["name"].strip().casefold() for e in corpora})
    modalities = Counter(e["modality"] for e in corpora)
    mod_text = ", ".join(f"{n} {m}" for m, n in sorted(modalities.items(), key=lambda kv: (-kv[1], kv[0])))
    tags = Counter()
    for e in corpora:
        # Count base languages: "Chinese (Taiwan Mandarin)" counts as Chinese. Cantonese stays separate.
        tags.update({t.strip() if t.strip().startswith("n/a") else t.split(" (")[0].strip()
                     for t in e["language"].split(", ") if t.strip()})

    def not_a_language(tag):
        t = tag.casefold()
        return t.startswith("n/a") or t in ("unknown", "multilingual")

    def rank(items):
        return sorted(items, key=lambda kv: (-kv[1], kv[0].casefold()))

    languages = rank([(t, n) for t, n in tags.items() if not not_a_language(t)])
    others = rank([(t, n) for t, n in tags.items() if not_a_language(t)])
    summary = f"**{total} corpora** ({mod_text}) in {len(languages)} languages."
    langs = "**Languages:** " + " \u00b7 ".join(f"{esc(t)} {n}" for t, n in languages + others)
    return summary + "\n\n" + langs


def render_contents(ours: list, sections: list, papers: list) -> str:
    lines = []
    if ours:
        lines.append(f"- [Our corpora](#{slug('Our corpora')}) ({len(ours)})")
    lines.append(f"- [Corpora by application area](#{slug('Corpora by application area')})")
    for _code, heading, entries, _notes, _subs in sections:
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
    for _code, heading, entries, notes, subsections in sections:
        out += [f"### {heading}", ""]
        for note in notes:
            out += [f"*{note}*", ""]
        if not entries and not notes:
            out += ["_No entries yet._", ""]
        for subsection, rows in subsections:
            if subsection:
                out += [f"#### {subsection}", ""]
            out += [corpus_table(rows), ""]
    return "\n".join(out).rstrip()


def render_papers(papers: list) -> str:
    out = ["## Related papers (no public data)", "",
           "Automotive NLP papers with no public corpus: each describes a system, benchmark or evaluation whose "
           "data has not been released. They are listed with the academic reference so that readers can contact "
           "the authors.", ""]
    if papers:
        out.append(paper_table(sorted(papers, key=lambda e: (e["section"], e["name"].casefold()))))
    else:
        out.append("_No entries yet._")
    return "\n".join(out)


def render_taxonomy() -> str:
    lines = [f"- **{code}. {name}**: {definition}" for code, (name, definition) in BUCKETS.items()]
    if MERGE_INTO:
        merges = "; ".join(f"{src} into {dst}" for src, dst in MERGE_INTO.items())
        lines += ["", f"A bucket with fewer than {MIN_ROWS} entries is merged into its named neighbour by the "
                      f"renderer ({merges}) and the section says so."]
    return "\n".join(lines)


def check_anchors(markdown: str) -> list:
    """Every in-page link must resolve; every Contents link must land on the heading it names."""
    headings, link_lines, in_code = [], [], False
    for line in markdown.splitlines():
        if line.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        m = re.match(r"^#{1,6}\s+(.+?)\s*$", line)
        if m:
            headings.append(m.group(1))
        link_lines.append(line)
    raw_count = Counter(slug(h) for h in headings)
    seen, target_of = {}, {}
    for h in headings:  # GitHub suffixes repeated slugs with -1, -2, ... in document order
        s = slug(h)
        if s in seen:
            seen[s] += 1
            s = f"{s}-{seen[s]}"
        else:
            seen[s] = 0
        target_of[s] = h
    errors, in_contents = [], False
    for line in link_lines:
        if line.startswith("## "):
            in_contents = line == "## Contents"
        for text, target in re.findall(r"\[([^\]]+)\]\(#([^)\s]+)\)", line):
            if target not in target_of:
                errors.append(f"README: link '[{text}](#{target})' has no matching heading")
            elif in_contents and target_of[target] != text:
                errors.append(f"README: Contents link '[{text}](#{target})' lands on heading '{target_of[target]}'")
            elif in_contents and raw_count[target] > 1:
                errors.append(f"README: Contents target '#{target}' is shared by {raw_count[target]} headings; "
                              f"rename the sub-heading that repeats '{text}'")
    return errors


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

    ours = sorted([e for e in corpora if e.get("ours")], key=lambda e: (e["section"], e["name"].casefold()))
    sections = group_sections(corpora)
    try:
        template = TEMPLATE_FILE.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"build_readme.py: cannot read template: {exc}", file=sys.stderr)
        return 2
    replacements = {
        "{{SUMMARY}}": render_summary(corpora),
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
    anchor_errors = check_anchors(output)
    if anchor_errors:
        for message in anchor_errors:
            print("ERROR " + message, file=sys.stderr)
        print("build_readme.py: README.md not written", file=sys.stderr)
        return 1
    if args.check:
        print("Anchors resolve. --check: README.md not written.")
        return 0
    README_FILE.write_text(output, encoding="utf-8")

    def sub_counts(subs):
        named = [(s, len(rows)) for s, rows in subs if s]
        flat = sum(len(rows) for s, rows in subs if not s)
        parts = ([f"(no sub-heading) {flat}"] if flat else []) + [f"{s} {n}" for s, n in named]
        return "; ".join(parts)

    print("Sections rendered (rows; sub-headings):")
    for code, _heading, entries, notes, subs in sections:
        flag = " [note]" if notes else ""
        print(f"  {code} {len(entries):3d}{flag}  {sub_counts(subs)}")
    print(f"Our corpora: {len(ours)}; related papers: {len(papers)}. All in-page anchors resolve.")
    print(f"Wrote {README_FILE.relative_to(ROOT)} ({output.count(chr(10))} lines).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
