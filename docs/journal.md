# Journal: SocialAI Knowledge Hub

## 2026-03-03 -- Promptotyping Phase 1-3: Preparation bis Distillation

### Ausgangslage
- Projektverzeichnis `socialAI` enthielt nur 2 PDFs (Kick-off-Folien + Fotoprotokoll)
- Umfangreicher Obsidian-Vault existiert bei DHC (27 .md-Dateien), aber DH Craft AP-spezifisch
- Bestehende Team-Website auf `digitalesozialearbeit.github.io` (HTML/CSS/JS, kein SSG)
- Orientierungsleitfaden bereits online als eigenstandige Sub-App

### Entscheidungen

| # | Entscheidung | Begrundung | Alternativen verworfen |
|---|-------------|------------|----------------------|
| 1 | Eigenes Repo (`socialai-knowledge-hub`) | Saubere Trennung von Website, eigener Zweck | Im bestehenden Repo als Subdirectory |
| 2 | Public Repository | Konsistent mit Open-Source-Ansatz (MIT-Lizenz), Transparenz | Private (hatte Zugangsmanagement erfordert) |
| 3 | Docsify als Site-Generator | Kein Build-Schritt, .md-Dateien direkt, Obsidian-kompatibel mit Plugins | MkDocs (braucht Build), Jekyll (Ruby-Dependency), reine HTML (wie Website) |
| 4 | Obsidian-Kompatibilitat uber Konventionen + Plugins | Ermoglicht lokales Editing in Obsidian, erzwingt es aber nicht | Obsidian Publish (kostenpflichtig), reines Standard-Markdown (kein Wikilink-Support) |
| 5 | Kick-off-Stand als aktuelle Referenz | Modifikationen beim Kick-off beschlossen, sind der gultige Plan | Original-Planung + Anderungshistorie (zu komplex fur Startphase) |
| 6 | Vault-Inhalte NICHT portieren | Hub startet mit destilliertem Wissen aus den Kick-off-PDFs, Vault ist DHC-intern | Gesamten Vault ins Hub (zu viel, zu spezifisch) |
| 7 | architecture.md statt design.md | design.md vorbehalten fur visuelles Design | design.md fur technische Entscheidungen (user-Feedback) |

### Erstellte Dokumente
- `docs/knowledge.md` -- Projektwissen aus beiden PDFs destilliert
- `docs/requirements.md` -- 5 Epics mit User Stories
- `docs/architecture.md` -- Tech-Stack, Plugins, Ordnerstruktur, Konventionen
- `docs/implementation.md` -- 3-Phasen-Implementierungsplan
- `docs/journal.md` -- dieses Dokument

### Offene Fragen

| # | Frage | Blockiert | Status |
|---|-------|-----------|--------|
| 1 | Gemeinsame Plattform (Teams/Slack)? Entscheidung steht aus. | Beeinflusst Rolle des Hubs (erganzend vs. zentral) | Offen -- klaren mit SOS-KD & JAW |
| 2 | Obsidian-Kompatibilitat: docsify-wikilink-Plugin tatsachlich getestet? | architecture.md Annahme | Offen -- vor Go-Live validieren |
| 3 | GitHub Web UI Editing: Hat jemand bei SOS-KD/JAW einen GitHub-Account? | US-4.3 | Offen -- Feldzugang klaren |
| 4 | Redaktioneller Workflow: Wer schreibt was, wer reviewt? | Langfristige Hub-Pflege | Offen -- Epic 6 in requirements.md angelegt |
| 5 | Glossar-Definitionen: Akademisch vs. verstandlich -- wer entscheidet Formulierung? | US-2.2 | Offen -- mit Praxispartnern klaren |

### Nicht Dokumentierte Exploration (Lucke)

Phase 2 (Exploration) wurde nicht separat dokumentiert. Folgende Entscheidungen wurden ohne dokumentierte Alternativen-Erprobung getroffen:
- Docsify-Plugin-Auswahl (nur Recherche, kein Hands-on-Test dokumentiert)
- Obsidian-Konventionen (theoretisch hergeleitet, nicht mit echten Inhalten getestet)
- Darklight-Theme (keine Alternative verglichen)

Bei nachster Gelegenheit nachholen: Testseite mit Wikilinks, Callouts, Frontmatter in Docsify rendern und Ergebnis dokumentieren.

### Nachste Schritte (Phase 4: Implementation)
1. GitHub-Repo erstellen auf Digitalesozialearbeit
2. Docsify-Grundstruktur aufsetzen (index.html, _sidebar.md, .nojekyll)
3. Initiale Hub-Inhalte aus knowledge.md in Hub-Seiten transformieren
4. GitHub Pages aktivieren und testen
5. Team informieren und Feedback einholen
6. Offene Fragen (oben) mit Konsortium klaren
