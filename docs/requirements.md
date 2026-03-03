# Requirements: SocialAI Knowledge Hub

## Projektziel

Zentrales, internes Nachschlagewerk fur das SocialAI-Projektteam. Verwaltet als .md-Dateien, gerendert mit docsify, gehostet auf GitHub Pages, kompatibel mit Obsidian.

**Repo:** `Digitalesozialearbeit/socialai-knowledge-hub` (public)
**Zielgruppe:** Projektteam intern (Forscher:innen und Fachkrafte aller 5 Partner-Organisationen)

---

## Epic 1: Projektubersicht

> Als Projektmitglied will ich schnell die Struktur und den Stand des Projekts erfassen, damit ich mich orientieren kann.

### User Stories

- **US-1.1:** Als neues Teammitglied will ich eine Ubersichtsseite mit Projektsteckbrief, Partner:innen und Timeline sehen, damit ich das Projekt verstehe.
- **US-1.2:** Als Teammitglied will ich fur jedes AP eine eigene Seite mit Aufgaben, Meilensteinen, Deliverables und Leads finden, damit ich weiss, was wann von wem zu liefern ist.
- **US-1.3:** Als Teammitglied will ich die beim Kick-off vereinbarten Zusammenarbeits-Regeln nachlesen konnen, damit Absprachen verbindlich dokumentiert sind.

**Prioritat:** Must-have
**Erfolgskriterium:** Jede:r im Team findet in < 30 Sekunden die Info zu einem bestimmten AP.

---

## Epic 2: Glossar

> Als Teammitglied will ich zentrale Begriffe nachschlagen konnen, damit alle im Projekt die gleiche Sprache sprechen.

### User Stories

- **US-2.1:** Als Teammitglied will ich ein alphabetisches Glossar mit Definitionen der Projektbegriffe (Bias, Intersektionalitat, Chancengerechtigkeit, etc.), damit Missverstandnisse vermieden werden.
- **US-2.2:** Als Fachkraft bei SOS-KD/JAW will ich Erklarungen in verstandlicher Sprache (nicht nur akademisch), damit ich die Begriffe in meinem Arbeitsalltag anwenden kann.

**Prioritat:** Must-have (beim Kick-off als "Next Step" definiert)
**Erfolgskriterium:** Alle beim Kick-off gesammelten Begriffe sind definiert. Definitionen sind von Praxispartner:innen als verstandlich bestatigt.

---

## Epic 3: Wissenssammlung

> Als Teammitglied will ich Projektwissen an einem Ort finden, damit ich nicht in E-Mails, Folien und verschiedenen Dokumenten suchen muss.

### User Stories

- **US-3.1:** Als Teammitglied will ich Ergebnisse aus abgeschlossenen APs (z.B. Literatur-Review, Workshop-Dokumentationen) als aufbereitete Zusammenfassungen lesen konnen.
- **US-3.2:** Als Teammitglied will ich Vorlagen und Leitfaden (z.B. fur Prompt-Erstellung, Workshop-Konzeption) finden, damit ich auf bestehendem Wissen aufbauen kann.
- **US-3.3:** Als Teammitglied will ich uber eine Suchfunktion uber alle Inhalte des Hubs suchen konnen.

**Prioritat:** Must-have (wachst mit dem Projekt)
**Erfolgskriterium:** Suchfunktion liefert relevante Treffer. Inhalte sind aktuell (max. 1 Monat Verzug).

---

## Epic 4: Technische Plattform

> Als Teammitglied will ich den Hub einfach nutzen und pflegen konnen, ohne technisches Vorwissen.

### User Stories

- **US-4.1:** Als Teammitglied will ich den Hub im Browser aufrufen und darin navigieren konnen (Sidebar, Suche).
- **US-4.2:** Als Teammitglied will ich Inhalte in Obsidian bearbeiten und sie anschliessend per Git-Push veroffentlichen konnen.
- **US-4.3:** Als nicht-technisches Teammitglied will ich Inhalte direkt uber die GitHub-Weboberflache bearbeiten konnen (analog zur bestehenden Website).
- **US-4.4:** Als Teammitglied will ich den Hub auch auf dem Handy lesbar nutzen konnen (responsive).

**Prioritat:** Must-have
**Erfolgskriterium:** Anderungen sind nach Push innerhalb von 2 Minuten online. Bearbeitung uber GitHub Web funktioniert ohne lokale Tools.

---

## Epic 5: Rechtliches & Compliance

> Als Teammitglied will ich Informationen zu AI Act und DSGVO im Kontext Sozialer Arbeit nachlesen konnen.

### User Stories

- **US-5.1:** Als Fachkraft will ich verstehen, welche Pflichten der AI Act fur den Einsatz von KI in der Sozialen Arbeit mit sich bringt.
- **US-5.2:** Als Teammitglied will ich Datenschutz-Leitlinien fur die Arbeit mit KI-Tools finden.

**Prioritat:** Should-have (Inhalte kommen aus AP3 und RI-Arbeit)
**Erfolgskriterium:** Informationsmaterialien von RI sind im Hub verfugbar und verlinkt.

---

## Epic 6: Redaktioneller Workflow

> Als Projektteam wollen wir klare Zustandigkeiten fur Hub-Inhalte, damit der Hub aktuell bleibt und nicht verwaist.

### User Stories

- **US-6.1:** Als AP-Lead will ich wissen, welche Hub-Seiten in meiner Verantwortung liegen, damit ich weiss, was ich nach Abschluss meiner Arbeit aktualisieren muss.
- **US-6.2:** Als Teammitglied will ich wissen, wer Inhalte reviewt bevor sie live gehen, damit keine fehlerhaften Informationen im Hub stehen.
- **US-6.3:** Als nicht-technisches Teammitglied will ich eine kurze Anleitung zum Bearbeiten uber GitHub Web UI, damit ich ohne Hilfe beitragen kann.

### Offene Fragen (zu klaren mit Konsortium)

| Frage | Betrifft | Vorschlag |
|-------|----------|-----------|
| Wer schreibt Glossar-Eintrage? | Alle Partner | Jede:r kann vorschlagen, Uni Graz finalisiert |
| Wer pflegt AP-Seiten nach Abschluss? | AP-Leads | AP-Lead liefert Zusammenfassung, DHC formatiert |
| Review-Prozess fur RI-Inhalte (Recht)? | RI, Uni Graz | RI schreibt, Uni Graz pruft Verstandlichkeit |
| Update-Rhythmus? | Alle | Nach jedem Meilenstein, spatestens quartalsweise |
| Wie mit Merge-Konflikten bei paralleler Bearbeitung? | Technisch | Unwahrscheinlich bei GitHub Web UI, DHC lost bei Bedarf |

**Prioritat:** Must-have (organisatorisch wichtiger als technische Plattform)
**Erfolgskriterium:** Jede Hub-Seite hat eine:n benannte:n Verantwortliche:n. Update-Zyklen werden eingehalten.

---

## Nicht im Scope (explizit ausgeschlossen)

- DH Craft-interne Projektdokumentation (Antrag, interne AP-Planung)
- Paper-Drafts und Konferenzabstracts (bleiben im jeweiligen Arbeitskontext)
- Meeting-Protokolle (bleiben im Kommunikationstool)
- Personenbezogene Daten / Befragungsergebnisse
- Inhalte des bestehenden Orientierungsleitfadens (bleibt auf digitalesozialearbeit.github.io)
