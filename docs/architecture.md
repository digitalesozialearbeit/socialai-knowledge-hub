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

### Plugins

| Plugin | Zweck | CDN |
|--------|-------|-----|
| search | Volltextsuche über alle Seiten | `docsify/lib/plugins/search.min.js` |
| docsify-wikilink | `[[Wikilinks]]` für Obsidian-Kompatibilität | `docsify-wikilink@1` |
| flexible-alerts | `> [!NOTE]` Callouts (Obsidian-Syntax) | `docsify-plugin-flexible-alerts` |
| copy-code | Code-Blöcke kopierbar | `docsify-copy-code` |
| zoom-image | Bilder klickbar vergrößern | `docsify/lib/plugins/zoom-image.min.js` |

### Custom Hooks (Obsidian-Kompatibilität)

```javascript
// In index.html als docsify-Plugin
function(hook) {
  hook.beforeEach(function(content) {
    // 1. YAML Frontmatter strippen
    content = content.replace(/^---[\s\S]*?---\s*\n/, '');
    // 2. Obsidian-Kommentare %%...%% entfernen
    content = content.replace(/%%[\s\S]*?%%/g, '');
    return content;
  });
}
```

### Schlüsselkonfiguration

```javascript
window.$docsify = {
  name: 'SocialAI Knowledge Hub',
  loadSidebar: true,        // _sidebar.md für Navigation
  subMaxLevel: 3,           // Headings in Sidebar als TOC
  relativePath: true,       // Obsidian-kompatible Pfadauflösung
  search: { paths: 'auto' },
  auto2top: true,
};
```

## Ordnerstruktur (Hub-Repo)

```
socialai-knowledge-hub/
  index.html                # Docsify Entry-Point
  README.md                 # Startseite / Home (= docsify Homepage)
  _sidebar.md               # Navigation
  .nojekyll                 # GitHub Pages: _-Dateien nicht ignorieren

  projekt/
    uebersicht.md           # Projektsteckbrief, Partner, Timeline
    arbeitspakete.md         # Alle 9 APs im Überblick
    zusammenarbeit.md        # Kick-off-Agreements, Kommunikation

  glossar/
    README.md               # Alphabetisches Glossar

  wissen/
    README.md               # Index der Wissensartikel

  recht/
    README.md               # Index Recht & Compliance

  assets/
    img/                    # Bilder, Diagramme

  docs/                     # Promptotyping-Dokumente (nicht Teil der Website)
    knowledge.md
    requirements.md
    architecture.md
    implementation.md
    journal.md
    sources/                # Konvertierte Quelldokumente + Original-PDFs

  scripts/                  # Hilfsskripte (z.B. PDF-Konvertierung)

  .gitignore
  LICENSE                   # CC BY 4.0
```

## Obsidian-Kompatibilität: Konventionen

### Erlaubt (funktioniert in Docsify UND Obsidian)

- Standard-Markdown (Headings, Listen, Tabellen, Code-Blöcke)
- YAML Frontmatter (wird von docsify gestrippt, Obsidian nutzt es)
- Relative Links: `[Text](../pfad/datei.md)`
- Wikilinks: `[[Dateiname]]` (via Plugin)
- Callouts: `> [!NOTE]`, `> [!WARNING]`, `> [!TIP]` (identische Syntax)
- Bilder: `![Alt](assets/img/bild.png)`

### Vermeiden (funktioniert nur in Obsidian)

- Block-Referenzen: `[[seite#^block-id]]`
- Dataview-Queries: `` ```dataview ... ``` ``
- Inline-Tags: `#tag` im Fließtext (wird als Heading interpretiert)
- Obsidian-Kommentare: `%%text%%` (werden gestrippt, also unsichtbar)

### Obsidian-Einstellungen (Empfehlung)

Wer den Hub in Obsidian bearbeitet, sollte folgendes einstellen:
- **Dateien & Links > Neues Link-Format:** Relativer Pfad zur Datei
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

## Beziehung zu bestehenden Systemen

| System | Rolle | Abgrenzung |
|--------|-------|-----------|
| digitalesozialearbeit.github.io | Öffentliche Team-Website | Anderer Zweck (extern), anderer Tech-Stack (HTML/Bootstrap) |
| Orientierungsleitfaden | Öffentlicher Praxis-Leitfaden | Sub-App der Website, eigenes CSS/JS, kein docsify |
| Obsidian-Vault (DHC) | Internes DH Craft Wissensmanagement | AP-spezifisch, nicht teamübergreifend |
| Knowledge Hub (dieses Repo) | Internes Nachschlagewerk für ALLE Partner | Teamübergreifend, docsify, Obsidian-kompatibel |
