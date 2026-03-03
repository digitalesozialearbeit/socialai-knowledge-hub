# Architecture: SocialAI Knowledge Hub

## Tech-Stack

| Komponente | Entscheidung | Begrundung |
|-----------|-------------|------------|
| Content-Format | Markdown (.md) | Universell, versionierbar, Obsidian-kompatibel |
| Site-Generator | docsify (v4) | Kein Build-Schritt, client-side Rendering, GitHub Pages nativ |
| Hosting | GitHub Pages | Kostenlos, public, CDN, automatisch bei Push |
| Versionierung | Git / GitHub | Standard fur das Team, bestehende Org vorhanden |
| Org | `Digitalesozialearbeit` | Bestehende GitHub-Organisation |
| Repo | `socialai-knowledge-hub` | Eigenes Repo, getrennt von der Website |
| Lizenz | CC BY 4.0 | Konsistent mit Projektansatz (Open Source, passend fuer Inhalte) |
| Lokales Editing | Obsidian (optional) | Fur Teammitglieder die es nutzen, kein Muss |
| Web-Editing | GitHub Web UI | Fur nicht-technische Teammitglieder |

## Docsify-Konfiguration

### Plugins

| Plugin | Zweck | CDN |
|--------|-------|-----|
| search | Volltextsuche uber alle Seiten | `docsify/lib/plugins/search.min.js` |
| docsify-wikilink | `[[Wikilinks]]` fur Obsidian-Kompatibilitat | `docsify-wikilink@1` |
| flexible-alerts | `> [!NOTE]` Callouts (Obsidian-Syntax) | `docsify-plugin-flexible-alerts` |
| copy-code | Code-Bloecke kopierbar | `docsify-copy-code` |
| zoom-image | Bilder klickbar vergroessern | `docsify/lib/plugins/zoom-image.min.js` |

### Custom Hooks (Obsidian-Kompatibilitat)

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

### Schlusselkonfiguration

```javascript
window.$docsify = {
  name: 'SocialAI Knowledge Hub',
  loadSidebar: true,        // _sidebar.md fur Navigation
  subMaxLevel: 3,           // Headings in Sidebar als TOC
  relativePath: true,       // Obsidian-kompatible Pfadauflosung
  search: { paths: 'auto' },
  auto2top: true,
};
```

## Ordnerstruktur (Hub-Repo)

```
socialai-knowledge-hub/
  docs/
    index.html              # Docsify Entry-Point
    README.md               # Startseite / Home
    _sidebar.md             # Navigation
    .nojekyll               # GitHub Pages: _-Dateien nicht ignorieren

    projekt/
      uebersicht.md         # Projektsteckbrief, Partner, Timeline
      arbeitspakete.md      # Alle 9 APs im Uberblick
      zusammenarbeit.md     # Kick-off-Agreements, Kommunikation

    glossar/
      README.md             # Alphabetisches Glossar

    wissen/
      README.md             # Index der Wissensartikel
      (wachst mit dem Projekt: Lit-Review-Ergebnisse, Frameworks, etc.)

    recht/
      README.md             # Index Recht & Compliance
      (AI Act, DSGVO -- Inhalte von RI)

    assets/
      img/                  # Bilder, Diagramme

  .gitignore
  LICENSE                   # CC BY 4.0
  README.md                 # Repo-README (nicht Hub-Inhalt)
  CLAUDE.md                 # Projektkonventionen fur Claude Code
```

## Obsidian-Kompatibilitat: Konventionen

### Erlaubt (funktioniert in Docsify UND Obsidian)

- Standard-Markdown (Headings, Listen, Tabellen, Code-Blocke)
- YAML Frontmatter (wird von docsify gestrippt, Obsidian nutzt es)
- Relative Links: `[Text](../pfad/datei.md)`
- Wikilinks: `[[Dateiname]]` (via Plugin)
- Callouts: `> [!NOTE]`, `> [!WARNING]`, `> [!TIP]` (identische Syntax)
- Bilder: `![Alt](assets/img/bild.png)`

### Vermeiden (funktioniert nur in Obsidian)

- Block-Referenzen: `[[seite#^block-id]]`
- Dataview-Queries: `` ```dataview ... ``` ``
- Inline-Tags: `#tag` im Fliesstext (wird als Heading interpretiert)
- Obsidian-Kommentare: `%%text%%` (werden gestrippt, also unsichtbar)

### Obsidian-Einstellungen (Empfehlung)

Wer den Hub in Obsidian bearbeitet, sollte folgendes einstellen:
- **Dateien & Links > Neues Link-Format:** Relativer Pfad zur Datei
- **Dateien & Links > Standard-Speicherort fur Anhange:** `assets/img/`

## Deployment-Workflow

```
Teammitglied bearbeitet .md  -->  git push  -->  GitHub Pages rendert automatisch
        |                                              |
        v                                              v
  (Obsidian oder                               docsify ladt .md
   GitHub Web UI)                              client-side im Browser
```

Kein Build-Schritt. Kein CI/CD notwendig. Push = Live.

## Beziehung zu bestehenden Systemen

| System | Rolle | Abgrenzung |
|--------|-------|-----------|
| digitalesozialearbeit.github.io | Offentliche Team-Website | Anderer Zweck (extern), anderer Tech-Stack (HTML/Bootstrap) |
| Orientierungsleitfaden | Offentlicher Praxis-Leitfaden | Sub-App der Website, eigenes CSS/JS, kein docsify |
| Obsidian-Vault (DHC) | Internes DH Craft Wissensmanagement | AP-spezifisch, nicht teamubergreifend |
| Knowledge Hub (dieses Repo) | Internes Nachschlagewerk fur ALLE Partner | Teamubergreifend, docsify, Obsidian-kompatibel |
