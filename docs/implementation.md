# Implementation: SocialAI Knowledge Hub

> Stand Juli 2026. Der Hub ist produktiv; dieses Dokument beschreibt den Ist-Zustand und die Inhalts-Roadmap. Die ursprüngliche Setup-Anleitung (02/2026) ist abgearbeitet; Abweichungen sind im Journal dokumentiert.

## Kontextsteuerung (Selective Context Loading)

Nicht alle Docs gleichzeitig laden — je nach Aufgabe die relevanten wählen:

| Aufgabe | Laden | Weglassen |
|---------|-------|-----------|
| Docsify-Konfiguration ändern | architecture.md + implementation.md | knowledge.md, requirements.md, journal.md |
| Hub-Inhalte schreiben (AP-Seiten, Glossar) | knowledge.md + relevante Epics aus requirements.md | architecture.md, implementation.md |
| Neue Seite/Feature planen | requirements.md + architecture.md | knowledge.md (Details), journal.md |
| Debugging / Docsify-Probleme | architecture.md (Plugins, Hooks) + implementation.md | knowledge.md, requirements.md |
| Fortschritt reviewen / Session starten | journal.md | alles andere initial |

---

## Ist-Zustand

- **Live-Site:** GitHub Pages, Branch `main`, Ordner `/ (root)`. Die docsify-Site liegt im **Repo-Root**, nicht in `/docs` — dort liegen die Promptotyping-Dokumente. Push = Live, kein Build, kein CI/CD.
- **Konfiguration:** vollständig in `index.html` (Theme docsify-themeable, CDN-Plugins, drei Custom Plugins — Details in architecture.md).
- **Navigation:** `_sidebar.md` im Root mit absoluten Pfaden; ein Alias leitet Sidebar-Anfragen aus Unterordnern auf die Root-Sidebar um.
- **Konventionen:** verbindlich in `CLAUDE.md` im Repo-Root (Sprache, Link-Regeln, Callout-Typen, Glossar-Tag-Zeilen). Frühere Entwürfe in diesem Dokument sind obsolet.

### Hilfsskripte

| Skript | Zweck | Aufruf |
|--------|-------|--------|
| `scripts/check-links.py` | Alle internen Markdown-Links prüfen (docsify-aware: Root-Auflösung für Site-Dateien, relative Auflösung für `docs/`) | `python scripts/check-links.py` (im Repo-Root) |
| `scripts/convert_pdfs.py` | PDFs aus `docs/sources/pdf/` nach Markdown konvertieren (docling) | `python scripts/convert_pdfs.py` |
| `scripts/sync-glossar.py` | Öffentliche Glossar-Fassung erzeugen (interne `***Anmerkung***`-Absätze und `[!INTERN]`-Callouts strippen) | `python scripts/sync-glossar.py [ZIELPFAD]` |

### Abhängigkeiten

Keine lokalen Abhängigkeiten, alle Libraries per CDN (Versionen siehe `index.html`):

- docsify v4 (+ Core-Plugins search, zoom-image)
- docsify-themeable (Theme)
- docsify-plugin-flexible-alerts, docsify-copy-code, docsify-pagination
- prismjs (Syntax-Highlighting)

Kein `package.json`, kein `npm install`, kein Build. Entfernt: docsify-wikilink (06/2026, ungenutzt).

### Lokale Vorschau

```bash
npx docsify-cli serve .
# oder jeder HTTP-Server im Repo-Root (VS Code Live Server, python -m http.server)
```

## Inhalts-Roadmap

| Wann | Inhalt | Quelle | Status |
|------|--------|--------|--------|
| Nach AP 3 (07/2026) | Workshop-Erkenntnisse, Anwendungsfelder, Recht-Grundlagen | Workshop-Dokumentation | ✅ online (`workshops/`, `wissen/anwendungsfelder.md`, `recht/ki-recht-grundlagen.md`) |
| Nach AP 2 (Ende 2026) | Literatur-Review Zusammenfassung | Review-Bericht | Offen |
| Nach AP 4 (01/2027) | Prompt-Analyse-Ergebnisse | Auswertungsbericht | Offen |
| Nach AP 5 (05/2027) | Prompting-Framework-Dokumentation | Framework-Konzept | Offen |
| Laufend | Rechtliche Informationen (AI Act, DSGVO) | RI-Materialien | Erste Fassung online |
| Laufend | Glossar-Ergänzungen | Alle Partner | Laufend (Endversion Mitte Juli 2026) |

## Qualitätssicherung

- Vor jedem Push mit Link-Änderungen: `python scripts/check-links.py`
- Content Health Check (Quellen vs. publizierte Seiten): Arbeitsanweisung in `docs/tests/content-health-check.md`, quartalsweise oder nach größeren Überarbeitungen ausführen (zuletzt 10.07.2026, alle Bereiche OK)
