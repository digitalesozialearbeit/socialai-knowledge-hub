# Requirements: SocialAI Knowledge Hub

## Projektziel

Zentrales, internes Nachschlagewerk für das SocialAI-Projektteam. Verwaltet als .md-Dateien, gerendert mit docsify, gehostet auf GitHub Pages, kompatibel mit Obsidian.

**Repo:** `Digitalesozialearbeit/socialai-knowledge-hub` (public)
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

**Priorität:** Must-have (beim Kick-off als "Next Step" definiert)
**Erfolgskriterium:** Alle beim Kick-off gesammelten Begriffe sind definiert. Definitionen sind von Praxispartner:innen als verständlich bestätigt.

---

## Epic 3: Wissenssammlung

> Als Teammitglied will ich Projektwissen an einem Ort finden, damit ich nicht in E-Mails, Folien und verschiedenen Dokumenten suchen muss.

### User Stories

- **US-3.1:** Als Teammitglied will ich Ergebnisse aus abgeschlossenen APs (z.B. Literatur-Review, Workshop-Dokumentationen) als aufbereitete Zusammenfassungen lesen können.
- **US-3.2:** Als Teammitglied will ich Vorlagen und Leitfaden (z.B. für Prompt-Erstellung, Workshop-Konzeption) finden, damit ich auf bestehendem Wissen aufbauen kann.
- **US-3.3:** Als Teammitglied will ich über eine Suchfunktion über alle Inhalte des Hubs suchen können.

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

**Priorität:** Must-have (organisatorisch wichtiger als technische Plattform)
**Erfolgskriterium:** Jede Hub-Seite hat eine:n benannte:n Verantwortliche:n. Update-Zyklen werden eingehalten.

---

## Nicht im Scope (explizit ausgeschlossen)

- DH Craft-interne Projektdokumentation (Antrag, interne AP-Planung)
- Paper-Drafts und Konferenzabstracts (bleiben im jeweiligen Arbeitskontext)
- Meeting-Protokolle (bleiben im Kommunikationstool)
- Personenbezogene Daten / Befragungsergebnisse
- Inhalte des bestehenden Orientierungsleitfadens (bleibt auf digitalesozialearbeit.github.io)
