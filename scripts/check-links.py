#!/usr/bin/env python3
"""Check all internal markdown links for broken targets.

Resolution rules:
- Docsify site files (top-level and projekt/, glossar/, wissen/, recht/):
  Absolute links (/foo) resolve from ROOT, relative links resolve from ROOT too
  (docsify without relativePath).
- Other files (docs/, etc.): Links resolve relative to the source file's directory.
- Links ending in / map to README.md in that directory.
- Links inside fenced code blocks (``` ... ```) and inline code (`...`) are ignored.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LINK_RE = re.compile(r'\[(?:[^\]]*)\]\(([^)]+)\)')
CODE_FENCE_RE = re.compile(r'^```', re.MULTILINE)
ERRORS = 0

# Docsify site directories (links resolve from ROOT)
DOCSIFY_DIRS = {'projekt', 'glossar', 'wissen', 'recht'}


def strip_code(content: str) -> str:
    """Remove fenced code blocks and inline code so we don't check links inside them."""
    # Remove fenced code blocks
    result = []
    in_code = False
    for line in content.splitlines():
        if CODE_FENCE_RE.match(line.strip()):
            in_code = not in_code
            continue
        if not in_code:
            result.append(line)
    content = '\n'.join(result)
    # Remove inline code (backtick-wrapped)
    content = re.sub(r'`[^`]+`', '', content)
    return content


def is_docsify_file(source: Path) -> bool:
    """Check if a file is part of the docsify site (links resolve from ROOT)."""
    try:
        rel = source.relative_to(ROOT)
    except ValueError:
        return False
    parts = rel.parts
    # Top-level .md files (_sidebar.md, README.md)
    if len(parts) == 1:
        return True
    # Files in docsify content directories
    if parts[0] in DOCSIFY_DIRS:
        return True
    return False


def check_target(source: Path, link: str) -> bool:
    global ERRORS

    # Skip external, mailto, anchor-only, empty
    if re.match(r'^https?://', link) or link.startswith('mailto:') or link.startswith('#') or not link:
        return True

    # Strip anchor fragment
    link = link.split('#')[0]
    if not link:
        return True

    if is_docsify_file(source):
        # Docsify mode: resolve from ROOT
        clean = link.lstrip('/')
        if clean.endswith('/') or clean == '':
            clean += 'README.md'
        target = ROOT / clean
    else:
        # Regular mode: resolve relative to source file's directory
        if link.startswith('/'):
            clean = link.lstrip('/')
        else:
            clean = link
        if clean.endswith('/') or clean == '':
            clean += 'README.md'

        if link.startswith('/'):
            target = ROOT / clean
        else:
            target = (source.parent / clean).resolve()

    if not target.is_file():
        rel_source = source.relative_to(ROOT)
        if link.startswith('/'):
            display_target = link.lstrip('/')
        else:
            try:
                display_target = target.relative_to(ROOT)
            except ValueError:
                display_target = target
        print(f"  BROKEN: {rel_source} -> {display_target}")
        ERRORS += 1
        return False
    return True


def main():
    print(f"Checking links in: {ROOT}\n")

    md_files = sorted(ROOT.rglob('*.md'))
    md_files = [f for f in md_files if '.git' not in f.parts and 'node_modules' not in f.parts]

    for md_file in md_files:
        content = md_file.read_text(encoding='utf-8', errors='replace')
        content = strip_code(content)
        links = LINK_RE.findall(content)
        for link in links:
            check_target(md_file, link)

    print()
    if ERRORS > 0:
        print(f"Found {ERRORS} broken link(s).")
        sys.exit(1)
    else:
        print("All links OK.")


if __name__ == '__main__':
    main()
