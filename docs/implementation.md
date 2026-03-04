# Implementation: SocialAI Knowledge Hub

## Kontextsteuerung (Selective Context Loading)

Nicht alle Docs gleichzeitig laden — je nach Aufgabe die relevanten wählen:

| Aufgabe | Laden | Weglassen |
|---------|-------|-----------|
| Hub aufsetzen (Docsify, Repo) | architecture.md + implementation.md | knowledge.md, requirements.md, journal.md |
| Hub-Inhalte schreiben (AP-Seiten, Glossar) | knowledge.md + relevante Epics aus requirements.md | architecture.md, implementation.md |
| Neue Seite/Feature planen | requirements.md + architecture.md | knowledge.md (Details), journal.md |
| Debugging / Docsify-Probleme | architecture.md (Plugins, Hooks) + implementation.md | knowledge.md, requirements.md |
| Fortschritt reviewen / Session starten | journal.md | alles andere initial |

---

## Phase 1: Repo-Setup und Grundstruktur

### 1.1 GitHub-Repo erstellen

```bash
# Auf github.com/Digitalesozialearbeit:
# New repository -> socialai-knowledge-hub -> Public -> CC BY 4.0 -> Create
```

### 1.2 Lokales Setup

```bash
git clone https://github.com/Digitalesozialearbeit/socialai-knowledge-hub.git
cd socialai-knowledge-hub
mkdir -p docs/projekt docs/glossar docs/wissen docs/recht docs/assets/img
touch docs/.nojekyll
```

### 1.3 docs/index.html (Docsify Entry-Point)

Vollständige Konfiguration mit allen Plugins und Obsidian-Kompatibilitäts-Hooks.
Sprache: Deutsch. Theme: Darklight (automatischer Dark Mode).

### 1.4 docs/_sidebar.md

```markdown
* **Projekt**
  * [Übersicht](projekt/uebersicht.md)
  * [Arbeitspakete](projekt/arbeitspakete.md)
  * [Zusammenarbeit](projekt/zusammenarbeit.md)

* **Glossar**
  * [Begriffe A-Z](glossar/)

* **Wissen**
  * [Übersicht](wissen/)

* **Recht & Compliance**
  * [Übersicht](recht/)
```

### 1.5 GitHub Pages aktivieren

Settings > Pages > Source: Deploy from branch > Branch: `main`, Folder: `/ (root)`

## Phase 2: Initiale Inhalte

Reihenfolge nach Priorität (requirements.md):

1. **projekt/uebersicht.md** -Projektsteckbrief, Partner, Timeline (aus knowledge.md destillieren)
2. **projekt/arbeitspakete.md** -Alle 9 APs (Kick-off-Stand aus knowledge.md)
3. **projekt/zusammenarbeit.md** -Agreements aus Kick-off (Kommunikation, Entscheidungen)
4. **glossar/README.md** -Begriffe aus Kick-off-Diskussion (Bias, Intersektionalität, etc.)
5. **docs/README.md** -Startseite mit Willkommen und Quick-Navigation

## Phase 3: Wachsende Inhalte

Diese Seiten werden im Projektverlauf ergänzt:

| Wann | Inhalt | Quelle |
|------|--------|--------|
| Nach AP 2 | Literatur-Review Zusammenfassung | Review-Bericht |
| Nach AP 3 | Workshop-Erkenntnisse, Praxisfragen der FKs | Workshop-Dokumentation |
| Nach AP 4 | Prompt-Analyse-Ergebnisse | Auswertungsbericht |
| Nach AP 5 | Prompting-Framework-Dokumentation | Framework-Konzept |
| Laufend | Rechtliche Informationen (AI Act, DSGVO) | RI-Materialien |
| Laufend | Glossar-Ergänzungen | Alle Partner |

## CLAUDE.md für das Hub-Repo

Folgende Konventionen sollen im CLAUDE.md des Hub-Repos festgehalten werden:

```markdown
# CLAUDE.md -socialai-knowledge-hub

## Projekt
Interner Knowledge Hub des SocialAI-Projekts (FFG Laura Bassi 4.0).
Docsify-basiert, Obsidian-kompatibel.

## Tech-Stack
- **Docsify v4** -kein Build, client-side Rendering
- **GitHub Pages** -Deployment aus /docs auf main-Branch
- **Markdown** -alle Inhalte als .md-Dateien

## Konventionen
- Sprache: Deutsch, gendergerechte Sprache mit Doppelpunkt (z.B. Forscher:innen)
- Links: relative Pfade (`../glossar/README.md`), Wikilinks erlaubt
- Callouts: `> [!NOTE]`, `> [!WARNING]`, `> [!TIP]`
- Bilder: in `docs/assets/img/`, referenziert als `![](assets/img/datei.png)`
- Kein YAML Frontmatter nötig (wird gestrippt), aber erlaubt
- Sidebar: manuell in `docs/_sidebar.md` pflegen bei neuen Seiten

## Ordnerstruktur
- `docs/projekt/` -Projektübersicht, APs, Zusammenarbeit
- `docs/glossar/` -Begriffsdefinitionen
- `docs/wissen/` -Projektergebnisse und Wissensartikel
- `docs/recht/` -AI Act, DSGVO, rechtliche Infos
- `docs/assets/img/` -Bilder

## Wichtige Dateien
- `docs/index.html` -Docsify-Konfiguration (Plugins, Hooks)
- `docs/_sidebar.md` -Navigation
- `docs/.nojekyll` -GitHub Pages Konfiguration
```

## Abhängigkeiten

Keine lokalen Abhängigkeiten. Alle Libraries werden über CDN geladen:
- docsify v4
- docsify-wikilink v1
- docsify-plugin-flexible-alerts
- docsify-copy-code
- docsify-darklight-theme

Kein `package.json`, kein `npm install`, kein Build.

## Testbarkeit

Lokale Vorschau mit docsify-cli (optional):
```bash
npm i -g docsify-cli
docsify serve docs
# -> http://localhost:3000
```

Oder einfach: `npx docsify-cli serve docs`

Alternative ohne docsify-cli: Jeder HTTP-Server funktioniert (z.B. VS Code Live Server, Python `http.server`).
