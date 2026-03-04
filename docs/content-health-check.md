# Content Health Check: SocialAI Knowledge Hub

> Arbeitsanweisung für Claude Code. Aufruf: "Führe den Content Health Check durch" oder "Lies `docs/content-health-check.md` und führe ihn aus."

## Zweck

Sicherstellen, dass das Wissen aus den Quelldokumenten (`docs/sources/`) korrekt, vollständig und konsistent in den publizierten Seiten des Knowledge Hub abgebildet ist. Stille Wissensverluste aufdecken: fehlende Inhalte, abweichende Zahlen, vergessene Kick-off-Beschlüsse.

## Methodik

Dieser Health Check folgt der **Promptotyping**-Methodik ("Documents as Source of Truth, Code as Disposable Artifact"). Die Quelldokumente in `docs/sources/` sind die Wahrheit; die publizierten Seiten sind Destillate. Wenn Quelle und Destillat abweichen, ist das Destillat zu korrigieren (es sei denn, die Abweichung war eine bewusste redaktionelle Entscheidung).

**Autoritative Referenz:** `docs/knowledge.md` ist das bereinigte Extrakt aus den Quellen. Prüfe zuerst `knowledge.md` gegen die Quellen, dann die publizierten Seiten gegen `knowledge.md`.

## Quellinventar

| Quelle | Datei | Enthält |
|--------|-------|---------|
| FFG-Antrag (Narrativ) | `docs/sources/antrag-narrativ.md` | Forschungsfragen, Methodik, theoretischer Rahmen, Ausgangslage, Konsortium, Ressourcen |
| FFG-Antrag (Arbeitsplan) | `docs/sources/antrag-arbeitsplan.md` | Alle 9 APs mit Aufgaben, Deliverables, Stunden, Zeiträumen |
| Kick-off-Folien | `docs/sources/kick-off-folien.md` | Präsentierte Inhalte, Timeline, AP-Übersicht |
| Kick-off-Fotoprotokoll | `docs/sources/kick-off-fotoprotokoll.md` | Vereinbarungen, Änderungen gegenüber Antrag, Glossarbegriffe, nächste Schritte |

## Zielseiten-Mapping

| Zielseite | Hauptquellen | Prüfschwerpunkt |
|-----------|-------------|-----------------|
| `projekt/uebersicht.md` | knowledge.md, antrag-narrativ.md, kick-off-folien.md | Steckbrief, Konsortium, Partner-Rollen, Timeline, Meilensteine |
| `projekt/arbeitspakete.md` | knowledge.md, antrag-arbeitsplan.md, kick-off-fotoprotokoll.md | Alle 9 APs: Zeiträume, Aufgaben, Deliverables, Stunden, Kick-off-Änderungen |
| `projekt/zusammenarbeit.md` | knowledge.md, kick-off-fotoprotokoll.md | Dos/Don'ts, Entscheidungsregeln, nächste Schritte |
| `glossar/README.md` | knowledge.md, kick-off-fotoprotokoll.md, antrag-narrativ.md | Alle beim Kick-off gesammelten Begriffe vorhanden und korrekt definiert |
| `glossar/technisch.md` | (eigenständig, kein direktes Quell-Mapping) | Fachliche Korrektheit, Konsistenz mit Projektbegriffen |
| `wissen/README.md` | knowledge.md | Geplante Inhalte decken alle APs ab, Zeiträume stimmen |
| `recht/README.md` | knowledge.md, antrag-narrativ.md | Geplante Materialien decken RI-Aufgaben ab |

## Prüfschritte

### Schritt 1: Faktenabgleich (Zahlen und Daten)

Prüfe die folgenden harten Fakten auf Konsistenz zwischen Quelle und Zielseite:

- [ ] **Projektsteckbrief:** Titel, Förderprogramm, Projektnummer, Laufzeit, Kick-off-Datum
- [ ] **Konsortium:** Alle 5 Partner mit korrekten Kürzeln und Hauptaufgaben
- [ ] **AP-Leads:** Alle 9 APs mit korrekter Lead-Zuordnung (Kick-off-Stand)
- [ ] **Zeiträume:** Alle AP-Zeiträume stimmen (inkl. Kick-off-Änderungen: AP 2 verlängert, AP 3 vorgezogen)
- [ ] **Stunden:** Stundenverteilung pro AP und Partner (Gesamttabelle in arbeitspakete.md prüfen)
- [ ] **Meilensteine:** Alle Meilenstein-Daten korrekt und vollständig
- [ ] **Deliverables:** Alle Deliverables pro AP vorhanden

### Schritt 2: Kick-off-Beschlüsse

Prüfe, ob alle beim Kick-off beschlossenen Änderungen und Vereinbarungen dokumentiert sind:

- [ ] AP 2 Verlängerung (urspr. 07/2026, jetzt 12/2026) + RI-Stunden-Verteilung
- [ ] AP 3 Vorziehen (urspr. 07-10/2026, jetzt 06-07/2026) + Format-Details (2 Halbtage, Vorab-Online-Meeting, N~10-12)
- [ ] AP 4 unabhängig von AP 3 (Kick-off-Beschluss)
- [ ] AP 5 RI-Stunden (10-20h für rechtliche Aspekte)
- [ ] AP 6 doppelte Erhebung (2x statt 1x)
- [ ] AP 7 SOS-KD & JAW übergreifend, Gender-Aspekt
- [ ] Zusammenarbeit: Alle Dos/Don'ts vollständig
- [ ] Nächste Schritte: Alle 9 Punkte aus dem Fotoprotokoll vorhanden

### Schritt 3: Glossar-Vollständigkeit

Prüfe gegen die beim Kick-off gesammelte Begriffsliste (`knowledge.md`, Abschnitt "Zentrale Begriffe"):

- [ ] Bias (soziologisch vs. technisch, intersektional, unconscious/implizit)
- [ ] Chancengerechtigkeit vs. Chancengleichheit
- [ ] Fairness (im KI-Kontext)
- [ ] Intersektionalität (Geschlecht, Alter, Migration)
- [ ] Diversität
- [ ] Feminist AI Literacies
- [ ] KI-Kompetenz
- [ ] Deskilling
- [ ] Context / Kontext
- [ ] AI Act (Anbieter / Betreiber / User)
- [ ] Datenschutz / DSGVO
- [ ] Erwachsenenbildung / Matthäus-Effekt
- [ ] Soziale Arbeit
- [ ] AI Agents / Agentic AI

### Schritt 4: Inhaltliche Tiefenprüfung (LLM-gestützt)

Lies die Quelldokumente abschnittsweise und prüfe:

1. **Antrag-Narrativ:** Wurden die zentralen Forschungsfragen, die Methodik und der theoretische Rahmen irgendwo im Hub aufgegriffen? (Aktuell möglicherweise nicht, da der Hub Projektorganisation fokussiert; ggf. Lücke identifizieren.)
2. **Antrag-Arbeitsplan:** Gibt es Aufgaben oder Deliverables in den APs, die in `arbeitspakete.md` fehlen oder vereinfacht wurden?
3. **Kick-off-Folien:** Wurden präsentierte Informationen korrekt übernommen? Gibt es Inhalte auf den Folien, die nirgends dokumentiert sind?
4. **Kick-off-Fotoprotokoll:** Gibt es Diskussionspunkte oder Vereinbarungen, die nicht in `zusammenarbeit.md` oder den AP-Seiten gelandet sind?

### Schritt 5: Strukturelle Fragen

- [ ] Sind alle geplanten Inhalte in `wissen/README.md` mit den korrekten AP-Zeiträumen aufgeführt?
- [ ] Deckt `recht/README.md` alle rechtlichen Deliverables aus den APs ab?
- [ ] Gibt es Inhalte im Antrag, die für das Team relevant wären, aber noch nirgends im Hub geplant sind?
- [ ] Ist die Sidebar-Navigation (`_sidebar.md`) vollständig und aktuell?

## Output-Format

Erstelle einen strukturierten Report mit folgenden Abschnitten:

### 1. Scorecard

| Bereich | Status | Anmerkung |
|---------|--------|-----------|
| Faktenabgleich | OK / Abweichung | ... |
| Kick-off-Beschlüsse | OK / Fehlt | ... |
| Glossar | X/14 Begriffe | ... |
| Inhaltliche Tiefe | OK / Lücken | ... |
| Struktur | OK / Anpassung nötig | ... |

### 2. Befunde

Für jeden gefundenen Befund:
- **Was:** Beschreibung der Abweichung oder Lücke
- **Wo:** Quelldatei (mit Zitat) vs. Zielseite
- **Empfehlung:** Korrektur, Ergänzung, oder bewusst ignorieren (mit Begründung)

### 3. Zusammenfassung

3-4 Sätze Gesamtbewertung. Wie viel Prozent der Quellinhalte sind korrekt abgebildet? Was sind die kritischsten Lücken?

## Output-Konvention

Der Health-Check-Report ist ein **temporales Prozessartefakt**, keine stabile Wissensquelle:

1. **Report** wird als Issue-Kommentar oder direkt im Chat ausgegeben (nicht als .md-Datei in `docs/`)
2. **Befunde** mit Handlungsbedarf werden als konkrete Aufgaben formuliert
3. Der Report selbst kann nach Abarbeitung der Befunde verworfen werden

## Wann diesen Check durchführen

- Nach Änderungen an `docs/sources/` (neue oder korrigierte Quelldokumente)
- Nach grösseren Überarbeitungen der publizierten Seiten
- Nach Projekttreffen, bei denen neue Beschlüsse gefasst wurden
- Quartalsweise als Routine-Check
