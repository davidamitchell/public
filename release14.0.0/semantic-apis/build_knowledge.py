#!/usr/bin/env python3
"""Generate standalone, traceable NotebookLM knowledge files from the OAS3/AsyncAPI specs.

Outputs (in ./bundled/):
  01_service_domain_catalogue*.md
  02_data_model_relationships*.md
  03_business_scenarios*.md

Everything is DERIVED from the spec files. Every statement cites `File.yaml:<line>` and
those citations are machine-verified against the source before the script finishes.
Requires PyYAML (pip install pyyaml).
"""
import collections
import glob
import hashlib
import os
import re
import subprocess
import sys

import yaml

BASE = os.path.dirname(os.path.abspath(__file__))
OAS = os.path.join(BASE, "oas3 ", "yamls")
ASYNC = os.path.join(BASE, "asyncapi-3.x", "yamls")
OUT = os.path.join(BASE, "bundled")
WORD_LIMIT = 400_000
SHARED_MIN = 10  # a schema name used by >= this many specs is "shared"
OAS_REL = "release14.0.0/semantic-apis/oas3 /yamls"  # note trailing space in "oas3 "
ASYNC_REL = "release14.0.0/semantic-apis/asyncapi-3.x/yamls"
SCHEMA_PREFIX = "#/components/schemas/"

CITES = []  # (relpath-key, abs file, line, expected substring)


# ---------------------------------------------------------------- yaml helpers
def load(path):
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    return yaml.compose(text, Loader=yaml.CSafeLoader), text.split("\n")


def mp(node):
    if isinstance(node, yaml.MappingNode):
        return {k.value: (k, v) for k, v in node.value}
    return {}


def sv(node):
    return node.value if isinstance(node, yaml.ScalarNode) else None


def ln(node):
    return node.start_mark.line + 1


def clean(text, n=300):
    t = re.sub(r"(\\r)?\\n|\r?\n", " ", text or "")
    t = re.sub(r"\s+", " ", t).strip()
    return t if len(t) <= n else t[: n - 1].rstrip() + "…"


def walk_refs(node, prop, out):
    if isinstance(node, yaml.MappingNode):
        for k, v in node.value:
            if k.value == "$ref" and isinstance(v, yaml.ScalarNode):
                if v.value.startswith(SCHEMA_PREFIX):
                    out.append((prop, v.value[len(SCHEMA_PREFIX):], ln(v)))
            else:
                walk_refs(v, prop, out)
    elif isinstance(node, yaml.SequenceNode):
        for x in node.value:
            walk_refs(x, prop, out)


class Domain:
    pass


def parse_domain(path):
    d = Domain()
    d.file = os.path.basename(path)
    d.stem = d.file[:-5]
    d.path = path
    root, lines = load(path)
    d.lines = lines
    d.sha = hashlib.sha256(open(path, "rb").read()).hexdigest()[:12]
    top = mp(root)
    info = mp(top["info"][1])
    d.title = sv(info["title"][1]).strip()
    d.title_line = ln(info["title"][0])
    d.version = sv(info["version"][1]) if "version" in info else ""
    d.desc = clean(sv(info["description"][1])) if "description" in info else ""
    d.desc_line = ln(info["description"][0]) if "description" in info else d.title_line

    d.ops = []
    for pk, pv in (mp(top.get("paths", (None, None))[1]) or {}).items():
        pkey, pnode = pv[0], pv[1]
        for method, (mk, mv) in mp(pnode).items():
            if method not in ("get", "put", "post", "delete", "patch"):
                continue
            o = mp(mv)
            segs = [s for s in pk.strip("/").split("/") if s and not s.startswith("{")]
            tags = []
            tag_line = ln(mk)
            if "tags" in o and isinstance(o["tags"][1], yaml.SequenceNode):
                tags = [sv(t) for t in o["tags"][1].value]
                tag_line = ln(o["tags"][1].value[0]) if o["tags"][1].value else tag_line
            summary = sv(o["summary"][1]) if "summary" in o else ""
            m = re.match(r"^([A-Z][a-z]{1,2}(?:CR|BQ))\b\s*(.*)$", summary or "")
            body = None
            if "requestBody" in o:
                rb = mp(o["requestBody"][1])
                if "$ref" in rb:
                    body = sv(rb["$ref"][1]).split("/")[-1]
            resp = None
            if "responses" in o:
                r200 = mp(o["responses"][1]).get("200")
                if r200:
                    rr = mp(r200[1])
                    if "$ref" in rr:
                        resp = sv(rr["$ref"][1]).split("/")[-1]
            d.ops.append(dict(
                path=pk, path_line=ln(pkey), method=method.upper(), method_line=ln(mk),
                op_id=sv(o["operationId"][1]) if "operationId" in o else "",
                summary=clean(summary), code=m.group(1) if m else "",
                tags=tags, tag_line=tag_line, action=segs[-1] if segs else "",
                domain_seg=segs[0] if segs else "", segs=segs, body=body, resp=resp,
                desc=clean(sv(o["description"][1]) if "description" in o else ""),
            ))

    comps = mp(top.get("components", (None, None))[1])
    d.schemas = {}
    for sk, (skey, snode) in mp(comps.get("schemas", (None, None))[1]).items():
        edges = []
        sm = mp(snode)
        for k, (kn, v) in sm.items():
            if k == "properties":
                for pk2, pv2 in v.value:
                    walk_refs(pv2, pk2.value, edges)
            else:
                walk_refs(v, "(schema)", edges)
        props = []
        if "properties" in sm:
            props = [p[0].value for p in sm["properties"][1].value]
        d.schemas[sk] = dict(line=ln(skey), edges=edges, props=props,
                             type=sv(sm["type"][1]) if "type" in sm else "")

    d.events = []
    apath = os.path.join(ASYNC, d.file)
    d.async_file = os.path.exists(apath)
    if d.async_file:
        aroot, _ = load(apath)
        chans = mp(mp(aroot).get("channels", (None, None))[1])
        for ck, (ckey, cnode) in chans.items():
            d.events.append((ck, ln(ckey)))
    return d


# ---------------------------------------------------------------- derived rules
THEMES = [  # priority order; first title match is primary
    ("Payments & Settlement", r"payment|settle|clearing|\bach\b|remittance|direct debit|wire|transfer"),
    ("Cards & Merchant Services", r"\bcards?\b|merchant|acquir"),
    ("Lending & Credit", r"loan|credit|lend|mortgage|overdraft|guarantee|collateral|factoring|leasing|syndicat"),
    ("Securities, Trading & Markets", r"securit|trading|trader|market|portfolio|investment|\bfunds?\b|broker|bond|derivative|\bfx\b|exchange rate|custod|underwrit|\bposition|\bfinancial instrument"),
    ("Risk, Compliance & Fraud", r"risk|complian|fraud|audit|regulat|\baml\b|sanction|legal|\bcontrols?\b|\bpolic"),
    ("Deposits & Accounts", r"deposit|saving|current account|account|\bbalance|\btermed"),
    ("Customer, Sales & Marketing", r"customer|party|prospect|relationship|sales|campaign|marketing|advertis|product|\bleads?\b|\boffers?\b|\bbrand|loyalty|contact"),
    ("Channels & Servicing", r"channel|branch|\batm\b|voice|call cent|mobile|\bweb\b|servicing|\bcase\b|dispute|complaint|correspondence|kiosk|\bsession"),
    ("Finance, Accounting & Treasury", r"ledger|accounting|financial|\btax|reconcil|treasury|budget|\bcash|\bfees?\b|billing|invoice|receivable|payable|capital"),
    ("Reference & Data Management", r"reference|directory|catalog|\brates?\b|pricing|calendar|\bdata\b|information|\bmodel\b|analytic|\breport|\bindex|benchmark|currency"),
    ("Corporate Operations & Support", r"human|employee|procure|supplier|facilit|technolog|\bit\b|document|record|archive|strateg|enterprise|organi|property|vendor|\bproject|\bcontract|\bsecurity|\bworkforce|\bsystem|\bservice|\bbusiness|\bsoftware|\bnetwork|\bdevice|\bpeople|\bfunction"),
]
THEME_RX = [(t, re.compile(p, re.I)) for t, p in THEMES]
ACTION_TERMS = {  # code -> term (observed in summaries; verified by build)
}


def classify(d):
    ev = []  # (theme, keyword, where, line)
    for t, rx in THEME_RX:
        m = rx.search(d.title)
        if m:
            ev.append((t, m.group(0), "title", d.title_line))
    prim = ev[0] if ev else None
    for t, rx in THEME_RX:
        m = rx.search(d.desc)
        if m and not any(e[0] == t for e in ev):
            ev.append((t, m.group(0), "description", d.desc_line))
    if not prim and ev:
        prim = ev[0]
    return prim, ev


def split_camel(s):
    return re.findall(r"[A-Z]+(?![a-z])|[A-Z][a-z0-9]+|[a-z0-9]+", s)


def is_enum_like(name):
    return name.lower().endswith("typevalues") or name.lower().endswith("values")


def fmt_cite(d_or_file, line):
    f = d_or_file.file if hasattr(d_or_file, "file") else d_or_file
    return f"{f}:{line}"


def cite(d, line, expect):
    CITES.append((d.path, line, expect))
    return f"{d.file}:{line}"


def cite_async(d, line, expect):
    CITES.append((os.path.join(ASYNC, d.file), line, expect))
    return f"asyncapi:{d.file}:{line}"


def words(s):
    return len(s.split())


# ---------------------------------------------------------------- writers
def write_parts(prefix, title, preamble, sections, trailer_sections=()):
    for old in glob.glob(os.path.join(OUT, prefix + "*.md")):
        os.remove(old)
    all_sections = list(sections) + list(trailer_sections)
    pw = words(preamble) + 200
    parts, cur, cw = [], [], pw
    for s in all_sections:
        w = words(s)
        if cur and cw + w > WORD_LIMIT:
            parts.append(cur)
            cur, cw = [], pw
        cur.append(s)
        cw += w
    if cur:
        parts.append(cur)
    names = [f"{prefix}.md"] if len(parts) == 1 else [f"{prefix}_part{i}.md" for i in range(1, len(parts) + 1)]
    for i, (n, p) in enumerate(zip(names, parts), 1):
        head = f"# {title}" + (f" (part {i} of {len(parts)})" if len(parts) > 1 else "") + "\n\n"
        if len(parts) > 1:
            head += ("This document is split into parts; sibling parts: " + ", ".join(f"`{x}`" for x in names) +
                     ".\nEach part repeats the reading guide so it can be used on its own.\n\n")
        with open(os.path.join(OUT, n), "w", encoding="utf-8") as fh:
            fh.write(head + preamble + "\n" + "\n".join(p))
    return names, sum(words(s) for s in all_sections) + pw * len(parts)


def common_preamble(commit, nspecs, doc_specific):
    return f"""## Reading guide (applies to every statement below)

- **Source:** BIAN Service Landscape release 14.0.0 specifications held in the GitHub repo `davidamitchell/public`, commit `{commit}`.
  - OpenAPI 3 specs: `{OAS_REL}/<Domain>.yaml` ({nspecs} files; note the trailing space in the `oas3 ` directory name).
  - AsyncAPI 3 specs (events): `{ASYNC_REL}/<Domain>.yaml`.
  - The ISO 20022 / DDD variants under `release14.0.0/apis-iso20022_ext-ddd/` were not analysed.
- **Everything here is DERIVED** from those files by the script `release14.0.0/semantic-apis/build_knowledge.py`. Nothing comes from bian.org or from model memory.
  Where a grouping or ordering is an inference (not stated in a spec) it is labelled **[derived-rule]**.
- **Traceability:** each fact ends with a citation `File.yaml:<line>` = line number in the original source file
  (OpenAPI unless prefixed `asyncapi:`). The same spec text is in the companion bundles `oas3_yamls_partN.md` under the heading `# FILE: <File>.yaml`
  (bundle line numbers differ; search for the schema / path name quoted next to the citation). All citations were machine-checked: the cited line contains the quoted key.
  A 12-character `sha256` prefix of each source file is given in the catalogue for version pinning.
- **Vocabulary (BIAN):** a *Service Domain* = one spec file. A *Control Record* (CR) is the main managed record of the domain (tag `CR - <Name>`);
  a *Behavior Qualifier* (BQ) is a sub-record/aspect (tag `BQ - <Name>`). Operations have an action code in their summary, e.g. `CoCR` = Control (CR), `ReBQ` = Retrieve (BQ).
{doc_specific}
"""


# ---------------------------------------------------------------- main
def main():
    commit = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=BASE, capture_output=True, text=True).stdout.strip()
    files = sorted(f for f in glob.glob(os.path.join(OAS, "*.yaml")))
    doms = [parse_domain(f) for f in files]
    bymap = {d.file: d for d in doms}
    n = len(doms)
    os.makedirs(OUT, exist_ok=True)

    # bundle part per file (from INDEX.md)
    part_of = {}
    idx = os.path.join(OUT, "INDEX.md")
    if os.path.exists(idx):
        for row in open(idx, encoding="utf-8"):
            c = [x.strip() for x in row.split("|")]
            if len(c) > 7 and c[1].endswith(".yaml"):
                part_of[c[1]] = c[6]

    # roles per domain
    for d in doms:
        d.cr = []
        d.bq = []
        for o in d.ops:
            for t in o["tags"]:
                if t.startswith("CR - ") and t[5:] not in [x[0] for x in d.cr]:
                    d.cr.append((t[5:], o["tag_line"], t))
                if t.startswith("BQ - ") and t[5:] not in [x[0] for x in d.bq]:
                    d.bq.append((t[5:], o["tag_line"], t))
        d.role = {}
        for name, _, _ in d.cr:
            d.role[name] = "Control Record"
        for name, _, _ in d.bq:
            d.role.setdefault(name, "Behavior Qualifier")

    # schema usage across specs
    usage = collections.defaultdict(list)
    for d in doms:
        for s in d.schemas:
            usage[s].append(d)
    shared = {s for s, ds in usage.items() if len(ds) >= SHARED_MIN}

    # action code glossary (derived from summaries)
    code_terms = collections.defaultdict(collections.Counter)
    code_ex = {}
    for d in doms:
        for o in d.ops:
            if o["code"]:
                code_terms[o["code"]][o["action"]] += 1
                code_ex.setdefault(o["code"], (d, o))

    # themes
    for d in doms:
        d.prim, d.theme_ev = classify(d)

    # related-domain mentions (info.description only)
    title_rx = {}
    for d in doms:
        t = d.title
        if len(t) >= 8:
            title_rx[d.file] = re.compile(r"(?<![A-Za-z])" + re.escape(t.lower()) + r"(?![A-Za-z])")
    for d in doms:
        d.mentions = []
        low = d.desc.lower()
        for f, rx in title_rx.items():
            if f != d.file and rx.search(low):
                d.mentions.append(bymap[f])

    # families by shared leading/trailing camel token
    fam = collections.defaultdict(list)
    for d in doms:
        toks = split_camel(d.stem)
        if len(toks) >= 2:
            fam["starts: " + toks[0]].append(d)
            fam["ends: " + toks[-1]].append(d)
    generic_end = {"ends: " + x for x in ()}

    s01 = build_catalogue(doms, code_terms, code_ex, shared, part_of)
    s02 = build_relationships(doms, usage, shared, part_of)
    s03 = build_scenarios(doms, bymap, part_of)

    results = {}
    results["01_service_domain_catalogue"] = write_parts(
        "01_service_domain_catalogue", "BIAN 14.0.0 Service Domain Catalogue (derived)",
        common_preamble(commit, n, s01["doc"]), s01["sections"], s01["trailer"])
    results["02_data_model_relationships"] = write_parts(
        "02_data_model_relationships", "BIAN 14.0.0 Data Model Relationships (derived)",
        common_preamble(commit, n, s02["doc"]), s02["sections"], s02["trailer"])
    results["03_business_scenarios"] = write_parts(
        "03_business_scenarios", "BIAN 14.0.0 Business Scenarios (derived from API operations)",
        common_preamble(commit, n, s03["doc"]), s03["sections"], s03["trailer"])

    bad = verify()
    for k, (names, w) in results.items():
        print(k, names, w)
    print("citations checked:", len(CITES), "failures:", len(bad))
    for b in bad[:20]:
        print("BAD", b)
    return 1 if bad else 0


def verify():
    cache, bad = {}, []
    for path, line, expect in set(CITES):
        if path not in cache:
            with open(path, encoding="utf-8") as fh:
                cache[path] = fh.read().split("\n")
        ls = cache[path]
        if not (1 <= line <= len(ls)) or expect not in ls[line - 1]:
            bad.append((os.path.basename(path), line, expect))
    return bad


# ---------------------------------------------------------------- 01 catalogue
def build_catalogue(doms, code_terms, code_ex, shared, part_of):
    sections = []
    doc = """- **This document:** a catalogue of every Service Domain (title, purpose, Control Record, Behavior Qualifiers, operation and event counts) plus a **[derived-rule]** grouping into themes.
  The themes are NOT BIAN's official Business Areas / Business Domains; they come from keyword rules applied to each spec's `info.title` (primary) and `info.description` (secondary).
  Each domain shows the matched keyword and where it matched so the grouping can be audited or overridden."""

    # themes
    by_theme = collections.defaultdict(list)
    for d in doms:
        by_theme[d.prim[0] if d.prim else "Unclassified"].append(d)
    order = [t for t, _ in THEMES] + ["Unclassified"]
    lines = ["## Theme grouping **[derived-rule]**", "",
             "Rule: first matching theme (in the order below) for a keyword found in the title; if the title matches nothing, the first match in the description; otherwise `Unclassified`. "
             "Keyword patterns are in `build_knowledge.py` (`THEMES`).", ""]
    for t in order:
        ds = by_theme.get(t, [])
        lines.append(f"### {t} ({len(ds)} domains)")
        for d in ds:
            if d.prim:
                lines.append(f"- {d.title} (`{d.file}`) — matched `{d.prim[1]}` in {d.prim[2]} [{cite(d, d.prim[3], 'title:' if d.prim[2]=='title' else 'description:')}]")
            else:
                lines.append(f"- {d.title} (`{d.file}`) — no keyword matched [{cite(d, d.title_line, 'title:')}]")
        lines.append("")
    sections.append("\n".join(lines))

    # families
    fam = collections.defaultdict(list)
    for d in doms:
        toks = split_camel(d.stem)
        if len(toks) >= 2:
            fam["starts with " + toks[0]].append(d)
            fam["ends with " + toks[-1]].append(d)
    lines = ["## Sibling name families **[derived-rule]**", "",
             "Domains whose CamelCase file name shares a first or last word with at least 2 (first word) or 3 (last word) others. "
             "This surfaces pairs such as `*Management` / `*Operations`. Name similarity only; it does not prove a BIAN relationship.", ""]
    for k in sorted(fam):
        ds = fam[k]
        need = 2 if k.startswith("starts") else 3
        if len(ds) >= need and len(ds) <= 25:
            lines.append(f"- **{k}** ({len(ds)}): " + ", ".join(f"{d.title}" for d in ds) + ". Titles cited: " +
                         ", ".join(f"[{cite(d, d.title_line, 'title:')}]" for d in ds[:30]))
    sections.append("\n".join(lines) + "\n")

    # glossary of action codes
    lines = ["## Action codes seen in operation summaries **(observed)**", "",
             "Code = first word of an operation `summary`; term = last path segment of that operation. Example citation is the first occurrence.", "",
             "| Code | Term(s) in URL path | Operations | Example |", "|---|---|---|---|"]
    for code in sorted(code_terms):
        terms = ", ".join(f"{t} ({c})" for t, c in code_terms[code].most_common(3))
        d, o = code_ex[code]
        lines.append(f"| {code} | {terms} | {sum(code_terms[code].values())} | {cite(d, o['path_line'], o['path'][:20].split('{')[0])}: {o['summary'][:70]} |")
    sections.append("\n".join(lines) + "\n")

    # per domain cards
    for d in doms:
        L = [f"## {d.title}", "",
             f"- **Spec file:** `{OAS_REL}/{d.file}` (sha256 `{d.sha}…`, version {d.version}); bundle: `{part_of.get(d.file, 'n/a')}` under `# FILE: {d.file}`",
             f"- **Purpose (verbatim from spec):** {d.desc or 'none given'} [{cite(d, d.desc_line, 'description') if d.desc else cite(d, d.title_line, 'title')}]"]
        if d.prim:
            ths = [f"{e[0]} (`{e[1]}` in {e[2]})" for e in d.theme_ev]
            L.append(f"- **Theme [derived-rule]:** primary {d.prim[0]}; all matches: " + "; ".join(ths) +
                     f" [{cite(d, d.prim[3], 'title:' if d.prim[2]=='title' else 'description:')}]")
        else:
            L.append(f"- **Theme [derived-rule]:** Unclassified [{cite(d, d.title_line, 'title:')}]")
        if d.cr:
            L.append("- **Control Record:** " + ", ".join(f"{n} [{cite(d, l, t)}]" for n, l, t in d.cr))
        if d.bq:
            L.append(f"- **Behavior Qualifiers ({len(d.bq)}):** " + ", ".join(f"{n} [{cite(d, l, t)}]" for n, l, t in d.bq))
        else:
            L.append("- **Behavior Qualifiers:** none")
        cnt = collections.Counter(o["action"] for o in d.ops)
        first = d.ops[0] if d.ops else None
        if first:
            L.append(f"- **Operations ({len(d.ops)}):** " + ", ".join(f"{a} {c}" for a, c in sorted(cnt.items())) +
                     f" [{cite(d, first['path_line'], first['path'][:12].split('{')[0])}]")
        else:
            L.append("- **Operations:** none defined (the OpenAPI `paths` section is empty or absent)")
        sch_spec = [s for s in d.schemas if s not in shared and s != "HTTPError"]
        L.append(f"- **Schemas:** {len(d.schemas)} total, {len(sch_spec)} domain-specific, {len([s for s in d.schemas if s in shared])} shared-across-≥{SHARED_MIN}-specs")
        if d.events:
            e0 = d.events[0]
            L.append(f"- **Event channels:** {len(d.events)} (e.g. `{e0[0]}`) [{cite_async(d, e0[1], e0[0].split('/')[0])}]")
        else:
            L.append("- **Event channels:** none (no AsyncAPI file or no channels)")
        if d.mentions:
            L.append("- **Other domains named in this purpose text:** " + ", ".join(m.title for m in d.mentions) +
                     f" [{cite(d, d.desc_line, 'description')}]")
        sections.append("\n".join(L) + "\n")
    return dict(doc=doc, sections=sections, trailer=[])


# ---------------------------------------------------------------- 02 relationships
def build_relationships(doms, usage, shared, part_of):
    doc = """- **This document:** how data models (OpenAPI `components/schemas`) relate: (1) per domain, the resource hierarchy Control Record → Behavior Qualifiers and the `$ref` graph between schemas;
  (2) a shared-schema catalogue; (3) cross-domain links.
- **Notation:** `Schema@L<n>` = schema defined at that line. `prop→Target@L<n>` = property `prop` holds a `$ref` to `Target` at that line. `used-by` lists schemas in the same spec that reference it.
  Roles: `CR` = Control Record, `BQ` = Behavior Qualifier, `enum` = names ending in `values` (type-value enumerations), `shared` = schema name present in ≥""" + str(SHARED_MIN) + """ specs.
- **Important limit:** specs are self-contained; there are no `$ref`s between files. Cross-domain links below are **[derived-rule]** name matches and prove similarity of name only, not identical meaning."""
    sections = []
    for d in doms:
        L = [f"## {d.title} (`{d.file}`)", ""]
        # hierarchy
        L.append("### Resource hierarchy (from tags and paths)")
        for n_, l, t in d.cr:
            L.append(f"- Control Record **{n_}** [{cite(d, l, t)}]" + (f"; schema@L{d.schemas[n_]['line']} [{cite(d, d.schemas[n_]['line'], n_ + ':')}]" if n_ in d.schemas else "; no schema of that name"))
        for n_, l, t in d.bq:
            L.append(f"  - Behavior Qualifier **{n_}** [{cite(d, l, t)}]" + (f"; schema@L{d.schemas[n_]['line']} [{cite(d, d.schemas[n_]['line'], n_ + ':')}]" if n_ in d.schemas else "; no schema of that name"))
        # CR payload refs
        for n_, _, _ in d.cr:
            if n_ in d.schemas:
                tg = [(p, t_, l) for p, t_, l in d.schemas[n_]["edges"] if t_ in {x[0] for x in d.bq}]
                if tg:
                    L.append(f"  - CR {n_} embeds BQs: " + ", ".join(f"{p}→{t_}@L{l} [{cite(d, l, t_)}]" for p, t_, l in tg))
        # reverse refs
        rev = collections.defaultdict(set)
        for s, info in d.schemas.items():
            for p, t_, l in info["edges"]:
                rev[t_].add(s)
        L.append("")
        L.append("### Schema relationships (domain-specific schemas)")
        spec = [s for s in d.schemas if s not in shared and s != "HTTPError"]
        for s in spec:
            info = d.schemas[s]
            role = d.role.get(s) and ("CR" if d.role[s] == "Control Record" else "BQ") or ("enum" if is_enum_like(s) else "")
            edges = info["edges"]
            e_txt = ", ".join(f"{p}→{t_}@L{l}" for p, t_, l in edges) if edges else "no outgoing refs"
            used = sorted(rev.get(s, set()) - {s})
            L.append(f"- **{s}**@L{info['line']}" + (f" [{role}]" if role else "") + f" [{cite(d, info['line'], s + ':')}] → {e_txt}" +
                     (f"; used-by: {', '.join(used)}" if used else ""))
            for p, t_, l in edges:
                cite(d, l, t_)
        used_shared = sorted({t_ for s in spec for _, t_, _ in d.schemas[s]["edges"] if t_ in shared})
        L.append("")
        L.append("Shared schemas used (see shared catalogue below): " + (", ".join(used_shared) if used_shared else "none"))
        sections.append("\n".join(L) + "\n")

    # trailer: shared catalogue
    T = ["## Shared schema catalogue", "",
         f"Schema names defined in ≥{SHARED_MIN} specs. 'Definitions' = number of distinct property/ref shapes among specs (1 = identical everywhere). "
         "Outgoing refs shown for the most common shape with one example citation.", ""]
    for s in sorted(shared, key=lambda x: (-len(usage[x]), x)):
        ds = usage[s]
        shapes = collections.defaultdict(list)
        for d in ds:
            i = d.schemas[s]
            shapes[(tuple(i["props"]), tuple((p, t_) for p, t_, _ in i["edges"]))].append(d)
        top = max(shapes.values(), key=len)
        ex = top[0]
        i = ex.schemas[s]
        e_txt = ", ".join(f"{p}→{t_}@L{l}" for p, t_, l in i["edges"]) or "no outgoing refs"
        for p, t_, l in i["edges"]:
            cite(ex, l, t_)
        T.append(f"- **{s}** — in {len(ds)} specs, {len(shapes)} definition(s); most common shape ({len(top)} specs), example {cite(ex, i['line'], s + ':')}: props {', '.join(i['props']) or '(none)'}; refs {e_txt}")
    sections_tr = ["\n".join(T) + "\n"]

    # adoption matrix
    T = ["## Shared schema adoption (which domains use which shared schema)", ""]
    for s in sorted(shared, key=lambda x: (-len(usage[x]), x)):
        T.append(f"- **{s}** ({len(usage[s])}): " + ", ".join(d.stem for d in usage[s]))
    sections_tr.append("\n".join(T) + "\n")

    # cross-domain name matches
    cr_names = collections.defaultdict(list)
    bq_names = collections.defaultdict(list)
    for d in doms:
        for n_, l, t in d.cr:
            cr_names[n_].append((d, l, t))
        for n_, l, t in d.bq:
            bq_names[n_].append((d, l, t))
    T = ["## Cross-domain links by shared name **[derived-rule]**", "",
         "### Control Record / Behavior Qualifier names that appear in more than one domain", ""]
    for kind, nm in (("Control Record", cr_names), ("Behavior Qualifier", bq_names)):
        for n_ in sorted(nm):
            ds = nm[n_]
            if len({x[0].file for x in ds}) >= 2:
                T.append(f"- {kind} **{n_}** in {len(ds)} domains: " + ", ".join(f"{x[0].stem} [{cite(x[0], x[1], x[2])}]" for x in ds[:40]) + (" …" if len(ds) > 40 else ""))
    T += ["", "### A domain's Behavior Qualifier named like another domain's Control Record or file name", ""]
    stems = {re.sub(r"[^a-z0-9]", "", d.stem.lower()): d for d in doms}
    crn = {re.sub(r"[^a-z0-9]", "", n_.lower()): n_ for n_ in cr_names}
    hits = 0
    for d in doms:
        for n_, l, t in d.bq:
            key = re.sub(r"[^a-z0-9]", "", n_.lower())
            tgt = stems.get(key)
            if tgt and tgt.file != d.file:
                T.append(f"- {d.stem} BQ **{n_}** [{cite(d, l, t)}] ↔ domain **{tgt.title}** (`{tgt.file}`) [{cite(tgt, tgt.title_line, 'title:')}]")
                hits += 1
    if not hits:
        T.append("- none found")
    T += ["", f"### Domain-specific schema names shared by 2–{SHARED_MIN - 1} domains", ""]
    for s in sorted(usage):
        ds = usage[s]
        if 2 <= len(ds) < SHARED_MIN:
            T.append(f"- **{s}** ({len(ds)}): " + ", ".join(f"{d.stem} [{cite(d, d.schemas[s]['line'], s + ':')}]" for d in ds))
    sections_tr.append("\n".join(T) + "\n")
    return dict(doc=doc, sections=sections, trailer=sections_tr)


# ---------------------------------------------------------------- 03 scenarios
ORDER = ["Initiate", "Update", "Execute", "Request", "Evaluate", "Exchange", "Grant", "Register", "Control", "Notify", "Retrieve"]


def step_rank(a):
    return ORDER.index(a) if a in ORDER else len(ORDER)


def build_scenarios(doms, bymap, part_of):
    doc = """- **This document:** business scenarios derived purely from each spec: its stated purpose, the operations offered on its Control Record and Behavior Qualifiers, and its published events.
  BIAN's own business scenarios are not in the repository, so these are **operation-lifecycle scenarios**, not narrative use cases.
- **[derived-rule] step order:** steps are ordered by an assumed convention: Initiate → Update → Execute → Request → Evaluate → Exchange → Grant → Register → Control → Notify → Retrieve → other.
  The spec does not state any ordering; only the *existence* of each operation (with its path, method and citation) is factual.
- **Reading a step:** `METHOD /path` — summary text from the spec [citation]. `Retrieve` can occur at any point."""
    sections = []
    for d in doms:
        L = [f"## Scenarios for {d.title} (`{d.file}`)", "",
             f"Business purpose: {d.desc or 'not stated'} [{cite(d, d.desc_line, 'description') if d.desc else cite(d, d.title_line, 'title')}]", ""]
        if not d.ops:
            L.append("No operations are defined in the OpenAPI spec (empty or absent `paths`), so no operation scenario can be derived.")
            L.append("")
        groups = collections.OrderedDict()
        for o in d.ops:
            key = None
            for t in o["tags"]:
                if t.startswith("CR - ") or t.startswith("BQ - "):
                    key = t
                    break
            groups.setdefault(key or "(untagged)", []).append(o)
        i = 0
        for key, ops in groups.items():
            i += 1
            kind = "Control Record" if key.startswith("CR - ") else "Behavior Qualifier" if key.startswith("BQ - ") else "operations"
            name = key[5:] if key[:3] in ("CR ", "BQ ") else key
            L.append(f"### Scenario {i}: work with {kind} “{name}”")
            for j, o in enumerate(sorted(ops, key=lambda x: (step_rank(x["action"]), x["path"])), 1):
                L.append(f"{j}. {o['action']} — `{o['method']} {o['path']}` — {o['summary'] or '(no summary)'} [{cite(d, o['path_line'], o['path'].split('{')[0][:25])}]"
                         + (f" request {o['body']}" if o["body"] else "") + (f", returns {o['resp']}" if o["resp"] else ""))
            L.append("")
        if d.events:
            L.append("### Event notifications (AsyncAPI)")
            for ck, l in d.events:
                L.append(f"- `{ck}` [{cite_async(d, l, ck.split('/')[0])}]")
            L.append("")
        if d.mentions:
            L.append("### Cross-domain scenario candidates")
            L.append("Domains named in this purpose text (potential collaborators): " + ", ".join(f"{m.title} (`{m.file}`)" for m in d.mentions) +
                     f" [{cite(d, d.desc_line, 'description')}]")
            L.append("")
        sections.append("\n".join(L))

    # trailer: patterns
    T = ["## Scenario patterns across all domains", "",
         "Counts of domains by lifecycle shape (derived from the operation lists above).", ""]
    shape = collections.Counter()
    ex = {}
    for d in doms:
        acts = {o["action"] for o in d.ops if any(t.startswith("CR - ") for t in o["tags"])}
        key = "Initiate" in acts, "Retrieve" in acts, bool(d.events), bool(d.bq)
        shape[key] += 1
        ex.setdefault(key, d)
    for (ini, ret, ev, bq), c in shape.most_common():
        d = ex[(ini, ret, ev, bq)]
        T.append(f"- {c} domains: CR can be initiated={ini}, CR retrievable={ret}, publishes events={ev}, has Behavior Qualifiers={bq}. Example: {d.title} [{cite(d, d.title_line, 'title:')}]")
    return dict(doc=doc, sections=sections, trailer=["\n".join(T) + "\n"])


if __name__ == "__main__":
    sys.exit(main())
