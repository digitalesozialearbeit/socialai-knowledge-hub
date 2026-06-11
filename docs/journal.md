# Journal: SocialAI Knowledge Hub

## 2026-06-11 – Fußnoten-Rendering für docsify

Das Glossar nutzt Standard-Markdown-Fußnoten (`[^id]` im Text, `[^id]: Definition` am Seitenende). GitHub und Obsidian rendern die Syntax nativ, docsify/marked nicht – auf der Website erschien sie als roher Text. Neues docsify-Plugin in `index.html` (beforeEach, gleiche Machart wie Frontmatter-Strip und Glossar-Filter): Definitionen werden eingesammelt, Verweise in nummerierte hochgestellte Links umgeschrieben, am Seitenende entsteht eine „Literatur"-Liste mit Ankern und Rücksprung-Links (↩). Quelldateien bleiben unverändert GitHub-/Obsidian-kompatibel. Verifiziert per Node-Test gegen das echte Glossar: alle 53 Definitionen aufgelöst, 55 Verweise, keine Waisen, keine rohe Syntax übrig.

---

## 2026-06-11 – docsify-wikilink-Plugin entfernt

Der offene Punkt „Wikilink-Plugin vor Go-Live testen" (seit 03/2026) ist damit aufgelöst: In drei Monaten Betrieb hat niemand Wikilink-Syntax geschrieben, alle Querverweise (auch die ~20 neuen im Glossar) sind Standard-Markdown-Links. Das ungetestete Plugin wurde aus `index.html` entfernt, Konventionen in `docs/architecture.md` und `CLAUDE.md` angepasst (Wikilinks jetzt unter „Vermeiden"). Bei Bedarf mit einer Zeile reaktivierbar.

---

## 2026-06-11 – JAW-Prompt-Auswertung intern abgelegt

### Anlass
Elke Maurer (JAW) hatte am 06.03.2026 die Auswertung der MyJaW-Prompts vom Februar 2026 geschickt (606 kategorisierte Prompts aus QMS-Channel und Free Chat, gefiltert um Kund:innen-Bezüge). Sie bedient das offene Kick-off-Item „AP 3/4: Prompts sammeln".

### Entscheidung
**Interne Nutzungsdaten von JAW werden nicht veröffentlicht.** Das Repo ist public, daher liegen Quell-PDF und aufbereitete Auswertung (Kategorien-Tabellen, Tätigkeitstypen, Beispiel-Prompts, Projektrelevanz für AP 3/4/5) nur lokal in `docs/intern/` (gitignored).

### Änderungen

| Dokument | Änderungen |
|----------|------------|
| `docs/intern/` (lokal) | Quell-PDF + aufbereitete Auswertung `jaw-prompts-auswertung-2026-02.md` |
| `.gitignore` | `docs/intern/` ausgeschlossen |
| `projekt/zusammenarbeit.md` | Kick-off-Item 4 „Prompts sammeln" auf „Teilweise" gesetzt (JAW intern vorliegend, SOS-KD offen) |
| `docs/knowledge.md` | AP 4 um Stand März 2026 ergänzt |

### Offene Punkte
- Frage von Sabine (06.03.): Wurde in MyJaW iterativ gepromptet oder nur Einzel-Prompts? Antwort von Elke/JAW-IT steht aus
- Prompts von SOS-KD fehlen noch
- Nebenbei geklärt (Mail Christian an Sabine, 03.06.): USt-Frage bei den Förderraten. Es gibt keine USt, DHC stellt keine Rechnung (FFG fördert direkt, Uni Graz ist nur Treuhänderin), Beträge sind netto; 16.502,21 € korrekt (vgl. § 5.4 Förderungsvertrag)

---

## 2026-06-11 – Sync mit uniCLOUD-Arbeitsordner und Glossar-Überarbeitung

### Anlass
Der uniCLOUD-Share (Link intern bekannt, nicht im Repo) wurde als Zusatz-Arbeitsordner des Konsortiums analysiert (Struktur nach APs, Protokolle 4+5, Anwendungsfelder, Logos). Zusammen mit dem Mail-Kontext (Susi, 09.06.: Glossar-Review-Bitte an DHC) ergaben sich konkrete Arbeitsaufträge.

### Aktualisierte Dokumente

| Dokument | Änderungen |
|----------|------------|
| `glossar/README.md` | Neuer Begriff **KI-Modell vs. KI-System** (Wunsch Susi/RI für Workshop-Tag 2); Stubs gefüllt: Probabilistische Systeme, Transparenz (technisch), Mind Perception; Literatur ergänzt (Few-Shot, CoT, RLHF, Distillation, Model Cards, Mind Perception); Tippfehler korrigiert; Platzhalter Datenminimierung für RI ergänzt |
| `wissen/anwendungsfelder.md` | **Neu:** bereinigte Fassung des AP3-Arbeitsdokuments Anwendungsfelder (4 Use-Case-Felder) |
| `wissen/README.md` | Link auf Anwendungsfelder-Seite |
| `_sidebar.md` | Navigationseintrag Anwendungsfelder |
| `index.html` | SocialAI-Logo in der Sidebar (docsify `logo`-Option) |
| `assets/logos/` | Offizielles SocialAI-Logo (RGB-PNG: Standard, White, Network Dense) aus uniCLOUD übernommen |
| `docs/knowledge.md` | AP2 + AP3 mit Stand aus Protokoll 4 (27.05.), Protokoll 5 (09.06.) und Mails konkretisiert |

### Beschlüsse aus Protokollen/Mails (übernommen nach knowledge.md)

| # | Beschluss | Quelle |
|---|-----------|--------|
| 1 | Glossar-Endversion bis Mitte Juli; DHC technische, RI juridische, KFU sozialwissenschaftliche Begriffe | Protokoll 4 + Mail Susi 09.06. |
| 2 | PRISMA-Update mit denselben Prompts, Analysezeitraum bis 30.06.2026 | Lit-Review-Überblick (uniCLOUD) |
| 3 | Literaturanalyse erst nach Innovationsworkshops, bis Ende 2026 | Protokoll 4 |
| 4 | AP2-Kernteam Christopher/Sabine/Susi; Treffen 01.07.2026, 10–12 Uhr, Büro Sabine; Christopher bringt PRISMA-Tool-Entwurf | Mail-Thread 09.06. |
| 5 | DHC-Tag unterscheidet KI-System vs. KI-Modell (RI baut darauf auf); Teilnehmende bringen Laptops | Protokoll 5 + Mail Susi |

### Nachtrag: Glossar-Review-Durchgang und Filter-UI (gleicher Tag)

- **Multi-Agent-Review** des Glossars (5 Perspektiven: Sprache, Format, Links, Technik-Fachlichkeit, Kohärenz; inhaltliche Findings adversarial verifiziert): 7 bestätigte inhaltliche Fixes, 4 defekte Anker repariert, ~20 Querverweise ergänzt, Setext-Rendering-Bug im Kopfbereich behoben, alphabetische Sortierung in 6 Abschnitten korrigiert, Perspektiv-Labels vereinheitlicht (**Rechtlich:** / **Sozialwissenschaftlich:** / **Technisch:**), Literaturangaben korrigiert
- **Kategorisierung + Filter:** Jeder der 85 Begriffe trägt jetzt eine Tag-Zeile (`Technik` 57, `Sozialwissenschaft` 30, `Recht` 13, `Soziale Arbeit` 7). Neues docsify-Plugin in `index.html` rendert daraus Filter-Buttons mit Zählern und eine A–Z-Sprungleiste; Tags erscheinen als Chips. Auf GitHub/Obsidian rendern die Tags harmlos als Inline-Code
- **`glossar/technisch.md` stillgelegt:** vollständig redundant zum Gesamtglossar (alle 47 Begriffe übernommen), Datei durch Verweis ersetzt, Sidebar-Eintrag entfernt ("Gesamtglossar" statt zwei Einträge)
- Verifiziert im Browser (localhost-Preview): Filter, A–Z-Leiste und Chips funktionieren, keine Konsolenfehler

### Offene Punkte

| # | Punkt | Status |
|---|-------|--------|
| 1 | Juridische Glossar-Stubs (sensible Daten, Zweckbindung, Datenminimierung, Diskriminierung juridisch, XAI juridisch) | Bei RI |
| 2 | Sozialwissenschaftliche Stubs (Vertrauenswürdige KI „Arndt", Digital Divide 4. Ebene, Vulnerabilität sozialwiss.) | Bei KFU |

---

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
