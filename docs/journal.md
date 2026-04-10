# Journal: SocialAI Knowledge Hub

## 2026-04-09 -Update nach 1. Quartalstreffen

### Anlass
Erstes Quartalstreffen (Jour fixe) des SocialAI-Konsortiums. Transkript bereinigt und als Grundlage für Doc-Updates verwendet.

### Aktualisierte Dokumente

| Dokument | Änderungen |
|----------|------------|
| `docs/knowledge.md` | AP3 konkretisiert (Termine, Format, Begleitinstrumente), Kommunikationstool entschieden, Kick-off-Schritte als erledigt markiert, neue Schritte aus Jour fixe ergänzt |
| `docs/journal.md` | Dieser Eintrag |
| `projekt/arbeitspakete.md` | AP2 + AP3 mit Jour-fixe-Updates ergänzt |
| `projekt/zusammenarbeit.md` | Kommunikationstool-Entscheidung, Kick-off-Schritte als erledigt markiert, neue Action Items |
| `projekt/uebersicht.md` | Martin Baumann als SOS-KD-Kontakt, Jugend am Werk – Steiermark GmbH |

### Entscheidungen (Jour fixe)

| # | Entscheidung | Begründung |
|---|-------------|------------|
| 1 | E-Mail + Uni-Cloud (Nextcloud) als Kommunikation/Ablage | Slack zu teuer (3.000 EUR/a), Teams an Uni nicht unterstützt, Uni-Cloud DSGVO-konform |
| 2 | AP3-Termine: 29.06. (9–13h) + 30.06. (13–17h) in Graz | Räumliche Nähe, beide Praxispartner in Graz erreichbar |
| 3 | Martin Baumann übernimmt päd. Leitung SOS-KD | Anna bleibt für Abrechnung, Martin hat päd. Expertise und Feldzugang |
| 4 | Vorab-Registrierung mit Kurzfragebogen + async Frage-Plattform | Ethikvotum-Anforderung, gleichzeitig Vorwissen-Erhebung und Verbindlichkeit |

### Status offener Fragen (aus 2026-03-03)

| # | Frage | Neuer Status |
|---|-------|-------------|
| 1 | Gemeinsame Plattform? | **Geklärt:** E-Mail + Uni-Cloud |
| 2 | Docsify-Wikilink-Plugin getestet? | Offen |
| 3 | GitHub-Accounts bei SOS-KD/JAW? | Offen |
| 4 | Redaktioneller Workflow? | Offen |
| 5 | Glossar-Formulierung? | Teilweise: internes Meeting am 22.04.2026 angesetzt |

---

## 2026-03-03 -Promptotyping Phase 1-3: Preparation bis Distillation

### Ausgangslage
- Projektverzeichnis `socialAI` enthielt nur 2 PDFs (Kick-off-Folien + Fotoprotokoll)
- Umfangreicher Obsidian-Vault existiert bei DHC (27 .md-Dateien), aber DH Craft AP-spezifisch
- Bestehende Team-Website auf `digitalesozialearbeit.github.io` (HTML/CSS/JS, kein SSG)
- Orientierungsleitfaden bereits online als eigenständige Sub-App

### Entscheidungen

| # | Entscheidung | Begründung | Alternativen verworfen |
|---|-------------|------------|----------------------|
| 1 | Eigenes Repo (`socialai-knowledge-hub`) | Saubere Trennung von Website, eigener Zweck | Im bestehenden Repo als Subdirectory |
| 2 | Public Repository | Konsistent mit Open-Source-Ansatz (MIT-Lizenz), Transparenz | Private (hatte Zugangsmanagement erfordert) |
| 3 | Docsify als Site-Generator | Kein Build-Schritt, .md-Dateien direkt, Obsidian-kompatibel mit Plugins | MkDocs (braucht Build), Jekyll (Ruby-Dependency), reine HTML (wie Website) |
| 4 | Obsidian-Kompatibilität über Konventionen + Plugins | Ermöglicht lokales Editing in Obsidian, erzwingt es aber nicht | Obsidian Publish (kostenpflichtig), reines Standard-Markdown (kein Wikilink-Support) |
| 5 | Kick-off-Stand als aktuelle Referenz | Modifikationen beim Kick-off beschlossen, sind der gültige Plan | Original-Planung + Änderungshistorie (zu komplex für Startphase) |
| 6 | Vault-Inhalte NICHT portieren | Hub startet mit destilliertem Wissen aus den Kick-off-PDFs, Vault ist DHC-intern | Gesamten Vault ins Hub (zu viel, zu spezifisch) |
| 7 | architecture.md statt design.md | design.md vorbehalten für visuelles Design | design.md für technische Entscheidungen (user-Feedback) |

### Erstellte Dokumente
- `docs/knowledge.md` -Projektwissen aus beiden PDFs destilliert
- `docs/requirements.md` -5 Epics mit User Stories
- `docs/architecture.md` -Tech-Stack, Plugins, Ordnerstruktur, Konventionen
- `docs/implementation.md` -3-Phasen-Implementierungsplan
- `docs/journal.md` -dieses Dokument

### Offene Fragen

| # | Frage | Blockiert | Status |
|---|-------|-----------|--------|
| 1 | Gemeinsame Plattform (Teams/Slack)? Entscheidung steht aus. | Beeinflusst Rolle des Hubs (ergänzend vs. zentral) | Offen -klären mit SOS-KD & JAW |
| 2 | Obsidian-Kompatibilität: docsify-wikilink-Plugin tatsächlich getestet? | architecture.md Annahme | Offen -vor Go-Live validieren |
| 3 | GitHub Web UI Editing: Hat jemand bei SOS-KD/JAW einen GitHub-Account? | US-4.3 | Offen -Feldzugang klären |
| 4 | Redaktioneller Workflow: Wer schreibt was, wer reviewt? | Langfristige Hub-Pflege | Offen -Epic 6 in requirements.md angelegt |
| 5 | Glossar-Definitionen: Akademisch vs. verständlich -wer entscheidet Formulierung? | US-2.2 | Offen -mit Praxispartnern klären |

### Nicht Dokumentierte Exploration (Lücke)

Phase 2 (Exploration) wurde nicht separat dokumentiert. Folgende Entscheidungen wurden ohne dokumentierte Alternativen-Erprobung getroffen:
- Docsify-Plugin-Auswahl (nur Recherche, kein Hands-on-Test dokumentiert)
- Obsidian-Konventionen (theoretisch hergeleitet, nicht mit echten Inhalten getestet)
- Darklight-Theme (keine Alternative verglichen)

Bei nächster Gelegenheit nachholen: Testseite mit Wikilinks, Callouts, Frontmatter in Docsify rendern und Ergebnis dokumentieren.

### Nächste Schritte (Phase 4: Implementation)
1. GitHub-Repo erstellen auf Digitalesozialearbeit
2. Docsify-Grundstruktur aufsetzen (index.html, _sidebar.md, .nojekyll)
3. Initiale Hub-Inhalte aus knowledge.md in Hub-Seiten transformieren
4. GitHub Pages aktivieren und testen
5. Team informieren und Feedback einholen
6. Offene Fragen (oben) mit Konsortium klären
