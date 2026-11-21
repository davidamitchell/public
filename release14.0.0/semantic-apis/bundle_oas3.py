#!/usr/bin/env python3
"""Bundle OAS3 YAML files into NotebookLM-friendly Markdown chunks."""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(BASE, "oas3 ", "yamls")
OUT = os.path.join(BASE, "bundled")
LIMIT = 400_000

os.makedirs(OUT, exist_ok=True)
files = sorted(f for f in os.listdir(SRC) if f.endswith(".yaml"))

chunks, cur, cur_words, total = [], [], 0, 0
for name in files:
    with open(os.path.join(SRC, name), encoding="utf-8") as fh:
        body = fh.read()
    block = f"# FILE: {name}\n\n```yaml\n{body.rstrip()}\n```\n\n"
    w = len(block.split())
    total += w
    if cur and cur_words + w > LIMIT:
        chunks.append(cur)
        cur, cur_words = [], 0
    cur.append(block)
    cur_words += w
if cur:
    chunks.append(cur)

names = ["oas3_yamls.md"] if len(chunks) == 1 else [
    f"oas3_yamls_part{i}.md" for i in range(1, len(chunks) + 1)]
for n, c in zip(names, chunks):
    with open(os.path.join(OUT, n), "w", encoding="utf-8") as fh:
        fh.write("".join(c))
print(f"files={len(files)} words={total} outputs={names}")
