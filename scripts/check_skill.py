"""Pre-release checks for the paywall-ab-test-assistant skill.

Run: python3 scripts/check_skill.py
Exits non-zero if the skill would fail to upload or breaks its own honesty rules.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT / "skills" / "paywall-ab-test-assistant"
SKILL = SKILL_DIR / "SKILL.md"
LIBRARY = SKILL_DIR / "references" / "evidence-library.md"

errors = []

text = SKILL.read_text(encoding="utf-8")
m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
if not m:
    errors.append("SKILL.md: missing YAML frontmatter")
else:
    front = m.group(1)
    name = re.search(r"^name:\s*(\S+)", front, re.M)
    if not name or name.group(1) != SKILL_DIR.name:
        errors.append("SKILL.md: frontmatter name must match the folder name")
    desc_block = re.search(r"^description:\s*>-?\n((?:  .*\n?)+)", front, re.M)
    desc = " ".join(l.strip() for l in desc_block.group(1).splitlines()) if desc_block else ""
    if not desc:
        errors.append("SKILL.md: description missing")
    elif len(desc) > 1024:
        errors.append(f"SKILL.md: description is {len(desc)} chars, limit is 1024")
    if "<" in desc or ">" in desc:
        errors.append("SKILL.md: description must not contain angle brackets")

if not LIBRARY.exists():
    errors.append("evidence-library.md is missing")
else:
    lib = LIBRARY.read_text(encoding="utf-8")
    # Rule: never state how many tests.
    for pat in [r"\b\d+\s+(?:A/B\s+)?tests?\b", r"\b\d+\s+experiments?\b", r"\bn\s*=\s*\d+"]:
        for hit in re.findall(pat, lib + text, re.I):
            errors.append(f"test count found: '{hit}'")
    # Rule: every element section carries an evidence label.
    labels = ("Strong", "Solid", "Mixed", "Thin")
    for section in re.split(r"\n### ", lib)[1:]:
        title = section.splitlines()[0]
        if not any(f"**{l}" in section for l in labels):
            errors.append(f"library section '{title}' has no evidence label")

if errors:
    print("FAILED")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print(f"OK: description {len(desc)} chars, library sections labelled")
