# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Internal Knowledge Hub for the SocialAI research project (FFG Laura Bassi 4.0, 02/2026 -- 01/2029). Five consortium partners collaborate on AI equity in social work. The hub is a docsify-based documentation site hosted on GitHub Pages.

## Tech Stack

- **Docsify v4** -- no build step, client-side Markdown rendering, all config in `index.html`
- **GitHub Pages** -- deployed from repo root on `main` branch (not `/docs`)
- **No dependencies** -- no `package.json`, no `npm install`. All libraries loaded via CDN

## Local Preview

```bash
npx docsify-cli serve .
# or any HTTP server at repo root
```

## Scripts

- `python scripts/check-links.py` -- validates all internal Markdown links (docsify-aware path resolution)
- `python scripts/convert_pdfs.py` -- converts PDFs in `docs/sources/pdf/` to Markdown via docling

## Architecture

### Docsify Site (repo root)

Content served by docsify lives at the repo root:

- `index.html` -- docsify config, plugins, Obsidian compatibility hooks (frontmatter stripping, `%%comment%%` removal)
- `_sidebar.md` -- navigation using **absolute paths** (`/projekt/uebersicht.md`), shared across all subdirectories via alias redirect
- `README.md` -- docsify homepage
- `projekt/` -- project overview, work packages (APs), collaboration agreements
- `glossar/` -- terminology definitions
- `wissen/` -- knowledge articles, papers (cleaned of Obsidian syntax)
- `recht/` -- legal/compliance (AI Act, DSGVO)
- `assets/` -- images, surveys

### Promptotyping Docs (not part of site)

`docs/` contains internal planning documents that are **not rendered by docsify**:

- `docs/knowledge.md` -- authoritative project knowledge distilled from PDFs and meetings
- `docs/requirements.md` -- epics and user stories
- `docs/architecture.md` -- tech decisions and conventions
- `docs/implementation.md` -- phased implementation plan with context-loading guide
- `docs/journal.md` -- session journal tracking decisions and progress
- `docs/sources/` -- converted source PDFs and originals

## Conventions

### Language & Formatting

- All content in **German**
- Gender-inclusive: Doppelpunkt notation (Forscher:innen, Fachkräfte)
- Never use em dashes or double hyphens. Use German Gedankenstriche (` – `, en dash with spaces) or restructure sentences

### Markdown

- Obsidian-compatible: wikilinks (`[[Link]]`), callouts (`> [!NOTE]`, `> [!TIP]`, `> [!WARNING]`), YAML frontmatter (gets stripped)
- Avoid Obsidian-only features: block references, dataview queries, inline `#tags`
- Images go in `assets/` and are referenced as `![](assets/img/file.png)`

### Navigation

- When adding new pages, update `_sidebar.md` manually
- Sidebar uses absolute paths from root (e.g., `/projekt/uebersicht.md`)
- Links within content pages use relative paths (`../glossar/README.md`)

### Link Checking

- `scripts/check-links.py` distinguishes docsify files (root-resolved) from docs/ files (relative-resolved)
- Does not check external URLs or anchor links
