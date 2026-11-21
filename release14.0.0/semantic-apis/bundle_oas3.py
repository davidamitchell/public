#!/usr/bin/env python3
"""Bundle OAS3 YAML files into NotebookLM-friendly Markdown chunks."""
import os
import re

BASE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(BASE, "oas3 ", "yamls")
OUT = os.path.join(BASE, "bundled")
LIMIT = 400_000

os.makedirs(OUT, exist_ok=True)
files = sorted(f for f in os.listdir(SRC) if f.endswith(".yaml"))

chunks, cur, cur_words, total = [], [], 0, 0
meta, part_of = {}, {}


def info(body):
    t = re.search(r"^  title:\s*(.+)$", body, re.M)
    v = re.search(r"^  version:\s*(.+)$", body, re.M)
    d = re.search(r"^  description:\s*(.*)$", body, re.M)
    clean = lambda m: m.group(1).strip().strip("'\"") if m else ""
    paths = re.findall(r"^  '?(/[^\n:]*?)'?:\s*$", body, re.M)
    desc = clean(d).replace("|", "\\|")
    return clean(t), clean(v), desc[:200], len(paths)


for name in files:
    with open(os.path.join(SRC, name), encoding="utf-8") as fh:
        body = fh.read()
    block = f"# FILE: {name}\n\n```yaml\n{body.rstrip()}\n```\n\n"
    meta[name] = (info(body), len(block.split()))
    w = len(block.split())
    total += w
    if cur and cur_words + w > LIMIT:
        chunks.append(cur)
        cur, cur_words = [], 0
    cur.append(block)
    part_of[name] = len(chunks) + 1
    cur_words += w
if cur:
    chunks.append(cur)

names = ["oas3_yamls.md"] if len(chunks) == 1 else [
    f"oas3_yamls_part{i}.md" for i in range(1, len(chunks) + 1)]
for n, c in zip(names, chunks):
    with open(os.path.join(OUT, n), "w", encoding="utf-8") as fh:
        fh.write("".join(c))
print(f"files={len(files)} words={total} outputs={names}")

single = len(chunks) == 1
lines = [
    "# OAS3 Specs Index",
    "",
    f"{len(files)} specs, {total:,} words, {len(chunks)} bundle file(s). "
    "Search for `# FILE: <filename>` in the bundle to jump to a spec.",
    "",
    "| File | Title | Version | Paths | Words | Bundle | Description |",
    "|---|---|---|---|---|---|---|",
]
for name in files:
    (t, v, d, p), w = meta[name]
    lines.append(f"| {name} | {t} | {v} | {p} | {w:,} | {names[part_of[name] - 1]} | {d} |")
with open(os.path.join(OUT, "INDEX.md"), "w", encoding="utf-8") as fh:
    fh.write("\n".join(lines) + "\n")
