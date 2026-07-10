# Requirements: SocialAI Knowledge Hub

## Projektziel

Zentrales, internes Nachschlagewerk für das SocialAI-Projektteam. Verwaltet als .md-Dateien, gerendert mit docsify, gehostet auf GitHub Pages, kompatibel mit Obsidian.

**Repo:** `Digitalesozialearbeit/socialai-knowledge-hub` (derzeit public; Beschluss vom 24.06.2026: wird privat gestellt, ausgewählte Inhalte erscheinen künftig in einem öffentlichen Spiegel-Repo nach Whitelist-Prinzip, siehe Epic 7)
**Zielgruppe:** Projektteam intern (Forscher:innen und Fachkräfte aller 5 Partner-Organisationen)

---

## Epic 1: Projektübersicht

> Als Projektmitglied will ich schnell die Struktur und den Stand des Projekts erfassen, damit ich mich orientieren kann.

### User Stories

- **US-1.1:** Als neues Teammitglied will ich eine Übersichtsseite mit Projektsteckbrief, Partner:innen und Timeline sehen, damit ich das Projekt verstehe.
- **US-1.2:** Als Teammitglied will ich für jedes AP eine eigene Seite mit Aufgaben, Meilensteinen, Deliverables und Leads finden, damit ich weiß, was wann von wem zu liefern ist.
- **US-1.3:** Als Teammitglied will ich die beim Kick-off vereinbarten Zusammenarbeits-Regeln nachlesen können, damit Absprachen verbindlich dokumentiert sind.

**Priorität:** Must-have
**Erfolgskriterium:** Jede:r im Team findet in < 30 Sekunden die Info zu einem bestimmten AP.

---

## Epic 2: Glossar

> Als Teammitglied will ich zentrale Begriffe nachschlagen können, damit alle im Projekt die gleiche Sprache sprechen.

### User Stories

- **US-2.1:** Als Teammitglied will ich ein alphabetisches Glossar mit Definitionen der Projektbegriffe (Bias, Intersektionalität, Chancengerechtigkeit, etc.), damit Missverständnisse vermieden werden.
- **US-2.2:** Als Fachkraft bei SOS-KD/JAW will ich Erklärungen in verständlicher Sprache (nicht nur akademisch), damit ich die Begriffe in meinem Arbeitsalltag anwenden kann.
- **US-2.3:** Als Nutzer:in des Glossars will ich Begriffe nach Kategorie (Technik, Recht, Sozialwissenschaft, Soziale Arbeit) filtern und über eine A–Z-Leiste springen können, damit ich unter 85+ Begriffen schnell finde, was ich brauche. *(Umgesetzt 06/2026: Tag-Zeilen + Filter-Plugin)*

**Priorität:** Must-have (beim Kick-off als "Next Step" definiert)
**Erfolgskriterium:** Alle beim Kick-off gesammelten Begriffe sind definiert. Definitionen sind von Praxispartner:innen als verständlich bestätigt. *(Stand 07/2026: Bestätigung noch nicht erhoben – bei den Innovationsworkshops im Juni nicht abgefragt; nächste Gelegenheit sind die Co-Creation-Workshops in AP 7.)*

---

## Epic 3: Wissenssammlung

> Als Teammitglied will ich Projektwissen an einem Ort finden, damit ich nicht in E-Mails, Folien und verschiedenen Dokumenten suchen muss.

### User Stories

- **US-3.1:** Als Teammitglied will ich Ergebnisse aus abgeschlossenen APs (z.B. Literatur-Review, Workshop-Dokumentationen) als aufbereitete Zusammenfassungen lesen können.
- **US-3.2:** Als Teammitglied will ich Vorlagen und Leitfaden (z.B. für Prompt-Erstellung, Workshop-Konzeption) finden, damit ich auf bestehendem Wissen aufbauen kann.
- **US-3.3:** Als Teammitglied will ich über eine Suchfunktion über alle Inhalte des Hubs suchen können.
- **US-3.4:** Als Workshop-Teilnehmer:in will ich zu jedem Innovationsworkshop eine Begleitseite mit Programm, Materialien und Nachlese finden, damit ich Inhalte nachschlagen kann. *(Umgesetzt 06/2026: `workshops/`)*

**Priorität:** Must-have (wächst mit dem Projekt)
**Erfolgskriterium:** Suchfunktion liefert relevante Treffer. Inhalte sind aktuell (max. 1 Monat Verzug).

---

## Epic 4: Technische Plattform

> Als Teammitglied will ich den Hub einfach nutzen und pflegen können, ohne technisches Vorwissen.

### User Stories

- **US-4.1:** Als Teammitglied will ich den Hub im Browser aufrufen und darin navigieren können (Sidebar, Suche).
- **US-4.2:** Als Teammitglied will ich Inhalte in Obsidian bearbeiten und sie anschliessend per Git-Push veröffentlichen können.
- **US-4.3:** Als nicht-technisches Teammitglied will ich Inhalte direkt über die GitHub-Weboberfläche bearbeiten können (analog zur bestehenden Website).
- **US-4.4:** Als Teammitglied will ich den Hub auch auf dem Handy lesbar nutzen können (responsive).

**Priorität:** Must-have
**Erfolgskriterium:** Änderungen sind nach Push innerhalb von 2 Minuten online. Bearbeitung über GitHub Web funktioniert ohne lokale Tools.

---

## Epic 5: Rechtliches & Compliance

> Als Teammitglied will ich Informationen zu AI Act und DSGVO im Kontext Sozialer Arbeit nachlesen können.

### User Stories

- **US-5.1:** Als Fachkraft will ich verstehen, welche Pflichten der AI Act für den Einsatz von KI in der Sozialen Arbeit mit sich bringt.
- **US-5.2:** Als Teammitglied will ich Datenschutz-Leitlinien für die Arbeit mit KI-Tools finden.

**Priorität:** Should-have (Inhalte kommen aus AP3 und RI-Arbeit)
**Erfolgskriterium:** Informationsmaterialien von RI sind im Hub verfügbar und verlinkt.

---

## Epic 6: Redaktioneller Workflow

> Als Projektteam wollen wir klare Zuständigkeiten für Hub-Inhalte, damit der Hub aktuell bleibt und nicht verwaist.

### User Stories

- **US-6.1:** Als AP-Lead will ich wissen, welche Hub-Seiten in meiner Verantwortung liegen, damit ich weiß, was ich nach Abschluss meiner Arbeit aktualisieren muss.
- **US-6.2:** Als Teammitglied will ich wissen, wer Inhalte reviewt bevor sie live gehen, damit keine fehlerhaften Informationen im Hub stehen.
- **US-6.3:** Als nicht-technisches Teammitglied will ich eine kurze Anleitung zum Bearbeiten über GitHub Web UI, damit ich ohne Hilfe beitragen kann.

### Offene Fragen (zu klären mit Konsortium)

| Frage | Betrifft | Vorschlag |
|-------|----------|-----------|
| Wer schreibt Glossar-Einträge? | Alle Partner | Jede:r kann vorschlagen, Uni Graz finalisiert |
| Wer pflegt AP-Seiten nach Abschluss? | AP-Leads | AP-Lead liefert Zusammenfassung, DHC formatiert |
| Review-Prozess für RI-Inhalte (Recht)? | RI, Uni Graz | RI schreibt, Uni Graz prüft Verständlichkeit |
| Update-Rhythmus? | Alle | Nach jedem Meilenstein, spätestens quartalsweise |
| Wie mit Merge-Konflikten bei paralleler Bearbeitung? | Technisch | Unwahrscheinlich bei GitHub Web UI, DHC löst bei Bedarf |

**Zwischenstand (07/2026):** Die laufende redaktionelle Pflege des Hubs liegt bis auf Weiteres bei DHC (Status quo bestätigt); die Partner liefern Inhalte zu. Die Fragen in der Tabelle bleiben bis zur Konsortiumsentscheidung offen.

**Priorität:** Must-have (organisatorisch wichtiger als technische Plattform)
**Erfolgskriterium:** Jede Hub-Seite hat eine:n benannte:n Verantwortliche:n. Update-Zyklen werden eingehalten.

---

## Epic 7: Öffentlicher Spiegel

> Als Konsortium wollen wir interne Arbeitsnotizen vom öffentlichen Auftritt trennen, damit das Team offen im Quelldokument arbeiten kann, ohne dass Interna publiziert werden.

### User Stories

- **US-7.1:** Als Redaktion will ich, dass interne Notizen (`***Anmerkung ...***`-Absätze, `[!INTERN]`-Callouts) automatisch aus der öffentlichen Glossar-Fassung entfernt werden, damit Review-Kommentare direkt im Glossar stehen können. *(Umgesetzt: `scripts/sync-glossar.py`, deterministische Strip-Operation)*
- **US-7.2:** Als Konsortium wollen wir ein öffentliches Repo, das ausschließlich redaktionell freigegebene Inhalte enthält (Whitelist-Prinzip), während dieses Repo privat wird. *(Beschlossen 24.06.2026, Umsetzung offen; Redaktionsplan-Entwurf liegt intern vor)*

**Priorität:** Must-have (Konsortiumsbeschluss)
**Erfolgskriterium:** Die öffentliche Fassung enthält keine internen Anmerkungen; `strip(intern) == public` ist deterministisch prüfbar.

---

## Nicht im Scope (explizit ausgeschlossen)

- DH Craft-interne Projektdokumentation (Antrag, interne AP-Planung)
- Paper-Drafts und Konferenzabstracts (bleiben im jeweiligen Arbeitskontext)
- Meeting-Protokolle (bleiben im Kommunikationstool)
- Personenbezogene Daten / Befragungsergebnisse
- Inhalte des bestehenden Orientierungsleitfadens (bleibt auf digitalesozialearbeit.github.io)
