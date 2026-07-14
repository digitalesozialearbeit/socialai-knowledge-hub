# Architecture: SocialAI Knowledge Hub

## Tech-Stack

| Komponente | Entscheidung | Begründung |
|-----------|-------------|------------|
| Content-Format | Markdown (.md) | Universell, versionierbar, Obsidian-kompatibel |
| Site-Generator | docsify (v4) | Kein Build-Schritt, client-side Rendering, GitHub Pages nativ |
| Hosting | GitHub Pages | Kostenlos, public, CDN, automatisch bei Push |
| Versionierung | Git / GitHub | Standard für das Team, bestehende Org vorhanden |
| Org | `Digitalesozialearbeit` | Bestehende GitHub-Organisation |
| Repo | `socialai-knowledge-hub` | Eigenes Repo, getrennt von der Website |
| Lizenz | CC BY 4.0 | Konsistent mit Projektansatz (Open Source, passend für Inhalte) |
| Lokales Editing | Obsidian (optional) | Für Teammitglieder die es nutzen, kein Muss |
| Web-Editing | GitHub Web UI | Für nicht-technische Teammitglieder |

## Docsify-Konfiguration

> Stand Juli 2026. Die autoritative Quelle ist `index.html`; dieser Abschnitt beschreibt die Struktur.

### Theme und CDN-Plugins

| Komponente | Zweck | CDN |
|--------|-------|-----|
| docsify-themeable (theme-simple) | Theme, per CSS-Variablen angepasst (Themenfarbe `#2c5aa0`) | `docsify-themeable@0` |
| search | Volltextsuche über alle Seiten | `docsify@4/lib/plugins/search.min.js` |
| zoom-image | Bilder klickbar vergrößern | `docsify@4/lib/plugins/zoom-image.min.js` |
| flexible-alerts | `> [!NOTE]` / `> [!TIP]` Callouts (Obsidian-Syntax) | `docsify-plugin-flexible-alerts@1` |
| copy-code | Code-Blöcke kopierbar | `docsify-copy-code@2` |
| pagination | Zurück/Weiter-Navigation am Seitenende | `docsify-pagination@2` |
| prismjs | Syntax-Highlighting (javascript, json, markdown, bash) | `prismjs@1` |

### Custom Plugins (inline in index.html)

| Plugin | Hook | Zweck |
|--------|------|-------|
| Obsidian-Kompatibilität | `beforeEach` | YAML-Frontmatter und `%%Kommentare%%` strippen |
| Fußnoten-Renderer | `beforeEach` + `doneEach` | Markdown-Fußnoten (`[^id]` / `[^id]: Definition`) in nummerierte hochgestellte Links + „Literatur“-Liste mit Rücksprung-Ankern umschreiben (marked kennt die Syntax nicht) |
| Glossar-Filter | `doneEach` (nur `/glossar/`) | Kategorie-Filter-Buttons mit Zählern und A–Z-Sprungleiste aus den Tag-Zeilen (Inline-Code-Chips) der Einträge bauen |

### Schlüsselkonfiguration

```javascript
window.$docsify = {
  name: 'SocialAI Knowledge Hub',
  nameLink: '/',
  logo: '/assets/logos/socialai-logo-rgb.png',
  loadSidebar: true,        // _sidebar.md für Navigation
  subMaxLevel: 3,           // Headings in Sidebar als TOC
  auto2top: true,
  alias: { '/.*/_sidebar.md': '/_sidebar.md' },  // eine Sidebar für alle Unterordner
  search: { paths: 'auto', depth: 3 },
  pagination: { crossChapter: true },
  copyCode: { buttonText: 'Kopieren' },
};
```

**Wichtig:** `relativePath` ist bewusst NICHT gesetzt (docsify-Default: false). Alle Links in Inhalten und Sidebar verwenden absolute Root-Pfade (`/projekt/uebersicht.md`); ein `../`-relativer Link aus einem Unterordner zeigt über die Site-Root hinaus und liefert live einen 404. `scripts/check-links.py` prüft genau diese Auflösung.

## Ordnerstruktur (Hub-Repo)

```
socialai-knowledge-hub/
  index.html                # Docsify Entry-Point (Config, Plugins, Custom Hooks)
  README.md                 # Startseite / Home (= docsify Homepage)
  _sidebar.md               # Navigation (absolute Root-Pfade)
  .nojekyll                 # GitHub Pages: _-Dateien nicht ignorieren

  projekt/
    uebersicht.md           # Projektsteckbrief, Partner, Timeline
    arbeitspakete.md        # Alle 9 APs im Überblick
    zusammenarbeit.md       # Kick-off-Agreements, Kommunikation

  glossar/
    README.md               # Gesamtglossar (85+ Begriffe, Tag-Zeilen für Filter)

  wissen/
    README.md               # Index der Wissensartikel
    anwendungsfelder.md     # 4 Use-Case-Felder (AP 3)
    papers/                 # Projektbezogene Papers (bereinigt)

  recht/
    README.md               # Index Recht & Compliance
    ki-recht-grundlagen.md  # KI und Recht (aus Workshop-Tag 2)

  workshops/                # Begleitseiten Innovationsworkshops (AP 3)
    innovationsworkshop-2026-06-29.md
    innovationsworkshop-2026-06-30.md

  assets/
    img/                    # Bilder, Diagramme
    logos/                  # SocialAI-Logos (RGB-PNG)
    surveys/                # Umfrage-Previews

  docs/                     # Promptotyping-Dokumente (nicht Teil der Website)
    knowledge.md
    requirements.md
    architecture.md
    implementation.md
    journal.md
    sources/                # Konvertierte Quelldokumente + Original-PDFs
    tests/                  # Arbeitsanweisungen für Checks (content-health-check.md)
    intern/                 # GITIGNORED: Partnerdaten, Workshop-Pläne, Redaktion

  scripts/
    check-links.py          # Interne Links prüfen (docsify-aware)
    convert_pdfs.py         # PDF -> Markdown (docling)
    sync-glossar.py         # Öffentliche Glossar-Fassung erzeugen (Anmerkungen strippen)

  .gitignore                # schließt docs/intern/ aus
  LICENSE                   # CC BY 4.0
```

## Obsidian-Kompatibilität: Konventionen

### Erlaubt (funktioniert in Docsify UND Obsidian)

- Standard-Markdown (Headings, Listen, Tabellen, Code-Blöcke)
- YAML Frontmatter (wird von docsify gestrippt, Obsidian nutzt es)
- Links auf andere Hub-Seiten: **absolute Root-Pfade** `[Text](/pfad/datei.md)`, auch mit Anker (`/glossar/README.md#anchor`). Keine `../`-relativen Pfade (404 auf der Live-Site, siehe Docsify-Konfiguration)
- Callouts: nur `> [!NOTE]` (Info) und `> [!TIP]` (Hervorhebung); WARNING/IMPORTANT werden nicht verwendet
- Markdown-Fußnoten: `[^id]` im Text, `[^id]: Definition` am Seitenende (Custom Plugin rendert sie)
- Bilder: `![Alt](assets/img/bild.png)`

### Vermeiden (funktioniert nur in Obsidian)

- Wikilinks: `[[Dateiname]]` (das Plugin `docsify-wikilink` wurde im Juni 2026 entfernt: in 3 Monaten Betrieb hat niemand Wikilinks geschrieben, alle Querverweise sind Standard-Markdown-Links; bei Bedarf reaktivierbar)
- Block-Referenzen: `[[seite#^block-id]]`
- Dataview-Queries: `` ```dataview ... ``` ``
- Inline-Tags: `#tag` im Fließtext (wird als Heading interpretiert)
- Obsidian-Kommentare: `%%text%%` (werden gestrippt, also unsichtbar)

### Obsidian-Einstellungen (Empfehlung)

Wer den Hub in Obsidian bearbeitet, sollte folgendes einstellen:
- **Dateien & Links > Neues Link-Format:** Absoluter Pfad im Vault; Links auf Hub-Seiten anschließend mit führendem `/` schreiben (`/projekt/uebersicht.md`). Vor dem Push `python scripts/check-links.py` laufen lassen
- **Dateien & Links > Standard-Speicherort für Anhänge:** `assets/img/`

## Deployment-Workflow

```
Teammitglied bearbeitet .md  -->  git push  -->  GitHub Pages rendert automatisch
        |                                              |
        v                                              v
  (Obsidian oder                               docsify lädt .md
   GitHub Web UI)                              client-side im Browser
```

Kein Build-Schritt. Kein CI/CD notwendig. Push = Live.

## Öffentlicher Spiegel

Beschluss vom 24.06.2026: Dieses Repo wird mittelfristig privat gestellt; ausgewählte Inhalte erscheinen öffentlich (Whitelist-Prinzip). Diese Rolle füllt das öffentliche Repo **`socialai-workshops`** (Workshop-Nachlesen, gespiegeltes Glossar, Impressum, Lizenzen) – es ist live und hat den früheren lokalen Public-Draft abgelöst, der am 14.07.2026 aus `docs/intern/` gelöscht wurde.

Technischer Baustein ist `scripts/sync-glossar.py`: erzeugt aus `glossar/README.md` die öffentliche Fassung als reine Strip-Operation. Absätze, die mit `***Anmerkung` beginnen, und `> [!INTERN]`-Callouts werden entfernt, alles andere geht unverändert durch. Standardziel ist seit 14.07.2026 der lokale Klon des öffentlichen Repos (`../socialai-workshops/glossar/README.md`). Vor dem Ausführen prüfen, ob der Glossar-Stand publikationsreif ist (Endversion = Git-Tag).

Zeitplan für die Privatstellung dieses Hub-Repos: offen (Stand Juli 2026).

## Beziehung zu bestehenden Systemen

| System | Rolle | Abgrenzung |
|--------|-------|-----------|
| digitalesozialearbeit.github.io | Öffentliche Team-Website | Anderer Zweck (extern), anderer Tech-Stack (HTML/Bootstrap) |
| Orientierungsleitfaden | Öffentlicher Praxis-Leitfaden | Sub-App der Website, eigenes CSS/JS, kein docsify |
| Obsidian-Vault (DHC) | Internes DH Craft Wissensmanagement | AP-spezifisch, nicht teamübergreifend |
| Knowledge Hub (dieses Repo) | Internes Nachschlagewerk für ALLE Partner | Teamübergreifend, docsify, Obsidian-kompatibel |
