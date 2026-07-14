# Journal: SocialAI Knowledge Hub

## 2026-07-14 – SOS-Unterlagen + Reorganisation docs/intern

**SOS-Lieferung (AP 4):** Martin Baumann (SOS-KD/4Raum) hat am 13.07. abends per Mail geliefert („Unterlagen KI SOS Kinderdorf"): KI-Richtlinie (03/2025), drei Risikoassessments nach AI Act (01/2026: allgemein, Chatbot **JOSY**, Midjourney) und Auszüge aus der internen Online-Schulung. Alles entpackt, mit docling konvertiert und unter `docs/intern/ap4-partnerdaten/sos/` abgelegt (Original + Markdown). Aus der Mail außerdem: Der 4Raum-Datenbankanbieter setzt mehrere Modelle ein, sichtbar v. a. **GPT-OSS** (Open-Weight, self-hosted); die SOS-IT hat einen neuen Leiter, der KI-Zuständige ist evtl. ab September weg – IT-One-Pager-Anfrage daher vor September stellen. Antwort-Draft mit vier Präzisierungsfragen an den Anbieter liegt in Christians Gmail-Drafts.

**Reorganisation `docs/intern/`:** Flache Ablage in semantische Unterordner umgebaut: `meetings/` (+ `transkripte-roh/`), `vertraege-finanzen/`, `workshops-2026-06/` (+ `begleitforschung/`), `ap2-literatur/` (+ `paper-quellen/`), `ap4-partnerdaten/` (`jaw/`, `sos/`). Alle Dateien kebab-case mit ISO-Datum benannt; `docs/intern/README.md` neu als Wegweiser mit Ablage-Konventionen. Pfad-Referenzen nachgezogen in `docs/knowledge.md`, `docs/architecture.md`, `scripts/sync-glossar.py` und im Memory. Das SOS-Zip wurde nach dem Entpacken gelöscht; die Bild-Pfade im Begleitforschungsbericht wurden auf den neuen Ordnernamen umgeschrieben. Historische Journal-Einträge nennen teils noch die alten Dateinamen; das README bildet den aktuellen Stand ab.

**Public-Draft gelöscht:** Der Ordner `docs/intern/public-repo/` (Strategie, Redaktionsplan, Glossar-Draft) wurde auf Christians Bestätigung hin gelöscht – das öffentliche Repo `socialai-workshops` ist live und hat die Draft-Struktur übernommen. `scripts/sync-glossar.py` zielt jetzt standardmäßig auf den lokalen Klon (`../socialai-workshops/glossar/README.md`); Achtung-Notiz im Skript: vor dem Sync prüfen, ob der Glossar-Stand publikationsreif ist (der Hub-Stand enthält den noch nicht reviewten Eintrag „Sensible Daten"). architecture.md-Abschnitt „Öffentlicher Spiegel" entsprechend aktualisiert.

---

## 2026-07-13 21:35 – handoff

**Summary:** uniCLOUD-Share komplett abgeglichen und 11 neue Dateien per docling konvertiert (7 Konvertate nach `docs/intern/`); RI-Folien-PDF mit expliziter Genehmigung im public Workshops-Repo veröffentlicht und auf der Tag-2-Nachlese verlinkt (Commits `1c32e5b`, `9b65312` dort); die beiden Transkripte des Quartalsmeetings vom selben Tag bereinigt, zu einem internen Protokoll zusammengeführt und in knowledge.md destilliert.

**Decisions:**
- **RI-Folien öffentlich:** Genehmigung wurde im Quartalsmeeting erteilt; Veröffentlichung mit ©-Kennzeichnung als Werk Dritter (bestehende LICENSE-CONTENT-Ausnahme greift). Intern hat das Konsortium ohnehin uneingeschränkte Nutzungserlaubnis.
- **Erster FFG-Zwischenbericht: Ende Februar 2027** (ASR-Stelle unleserlich, von Christian bestätigt).
- **Jour-fixe-Punkte** (AP-5-Stunden, AP-6-Zeitplan, AP-9-Policy, Glossar-Titel, KI-Richtlinie) blieben am 13.07. unbehandelt → Agenda für das Quartalsmeeting am 06.10.2026, 13:00–14:30.
- **Partner-Interna** (JAW-Dienstleister, interne Arbeitsgruppen, Studierendennamen) bewusst nur im internen Protokoll, nicht in knowledge.md (Repo noch public).
- **Protokolle** liegen künftig nur noch in der uniCLOUD (kein Mailversand mehr).

**Dead ends:** Keine. Einzelne Transkriptpassagen waren nur sinngemäß rekonstruierbar (im bereinigten Protokoll gekennzeichnet).

**Phase:** Implementation (Iteration). Alle fünf Kern-Docs existieren; knowledge.md und journal.md sind auf Stand 13.07. (Quartalsmeeting eingearbeitet); requirements/architecture/implementation unverändert gültig.

**Open issues:**
- FoWi-Paper (Pollin/Sackl-Sharif/Klinger) ist laut Meeting erschienen; Zitation fehlt noch, `wissen/README.md` listet es weiter als unveröffentlicht.
- Zweck des `AP2/Personas/`-Ordners am Share ungeklärt (offener Kernteam-Punkt).
- AP-2-Kernteam-Protokoll vom 01.07. weiterhin nicht am Share.
- SOS-Prompts für das AP-4-Prompt-Set stehen aus (bis Oktober klären).
- Glossar-Endversion (Mitte Juli) weiter blockiert durch RI-Review „Sensible Daten" und Literacies-Titelfrage.
- Die rohen Transkript-`.txt` liegen noch in `docs/intern/` (Löschung nicht entschieden; bereinigte Fassung ersetzt sie inhaltlich).

**Next steps:**
1. FoWi-Zitation besorgen und den Eintrag in `wissen/README.md` auf „veröffentlicht" umstellen
2. Action Points aus dem Quartalsmeeting verfolgen (IT-One-Pager-Anfragen Elke/Martin, RI-Fristen Mitte/Ende Oktober, Rückmeldungen zum Begleitforschungsbericht)
3. Glossar: RI-Review und Titelfrage klären, dann Endversion als Git-Tag markieren
4. AP-4-Vorbereitung ab Oktober (Klagenfurt-Fallvignetten mit Prompt-Set-Auftrag zusammenführen, Kontakt zur interessierten Studentin)
5. Entscheiden, ob die rohen Transkript-`.txt` gelöscht werden

---

## 2026-07-13 – uniCLOUD-Sync: Begleitforschungs-Protokolle und AP-2-Berichtsstruktur

Komplettes Share-Listing (WebDAV, mit Änderungsdaten) gegen den Hub-Stand vom 11.06. abgeglichen; 11 neue bzw. geänderte Dateien mit docling nach Markdown konvertiert und gesichtet. Sieben Konvertate nach `docs/intern/` übernommen (gitignored):

- `protokoll-innoworkshop-tag1-2026-06-29.md` + `protokoll-innoworkshop-tag2-2026-06-30.md` – Beobachtungsprotokolle der Begleitforschung, folienweise mit Wortmeldungen; enthalten Klarnamen, nie veröffentlichen
- `wiss-begleitung-methodenkonzept.md` – Inhaltsanalyse nach Kuckartz, MAXQDA24
- `kurzfragebogen-innoworkshops.md` – Erhebungsinstrument (Forms-Design-Link entfernt)
- `ablauf-innoworkshop-ri-tag2.md` – RI-Drehbuch Tag 2 (Herbstlaub-Methode)
- `ap2-ffg-bericht-gliederung.md` – Berichtsskelett mit Zuständigkeiten
- `anastasiadis-lembacher-2024-soziale-innovation.md` – Fremdpaper (soziales_kapital Bd. 28), Kontextliteratur der Begleitforschung

knowledge.md ergänzt: FFG-Berichtsstruktur mit RI-Deadline **Ende Oktober 2026**, PRISMA-Analysekategorien (4 technische + 6 soziale), Personas-Fund als offener Kernteam-Punkt, Begleitforschungs-Fundorte (AP 3).

Nicht übernommen: `Teilnehmende/`-Dateien (personenbezogen), Personas-Posterbeispiele (Spanischunterricht, kein Projektbezug), MDPI-Werbemail (nur Randnotiz bei den offenen Punkten). Weiterhin nicht am Share: AP-2-Kernteam-Protokoll vom 01.07.; der AP4-Ordner ist leer.

**Klarstellung (Christian, 13.07.):** Die Copyright-Sperre der RI-Folien gilt nur nach außen; intern hat das Konsortium uneingeschränkte Nutzungserlaubnis (im Memory notiert).

**Nachtrag (gleicher Tag):** Christian hat die explizite Genehmigung des RI, das Folien-PDF auf der öffentlichen Tag-2-Nachlese-Seite zu veröffentlichen. Umgesetzt im socialai-workshops-Repo: PDF als `slides/innovationsworkshop-2-recht-ethik-2026-06-30.pdf`, TIP-Callout nach Tag-1-Muster mit ©-Kennzeichnung (Werk Dritter, nicht CC BY, gedeckt durch die bestehende Ausnahme in LICENSE-CONTENT); Hub-Seite `workshops/innovationsworkshop-2026-06-30.md` entsprechend aktualisiert. (Die Genehmigung wurde, wie sich aus dem Meeting-Transkript ergab, im Quartalsmeeting erteilt.)

**Nachtrag 2 (gleicher Tag) – Quartalsmeeting 13.07. verarbeitet:** Zwei ASR-Transkripte (Vorbesprechung 10:08, Quartalsmeeting 10:33) bereinigt und zu `docs/intern/meetings/quartalsmeeting-2026-07-13-bereinigt.md` zusammengeführt (Beschlüsse + Action Points vorangestellt; Rohtranskripte stark verrauscht, sinngemäße Rekonstruktion). knowledge.md nachgezogen:

- **AP 2:** Erste Publikation (Deep-Research) erschienen, zweite bis Ende 2026; PRISMA-Fokus Bias-Detection in der Sozialen Arbeit; Glossar wird FFG-Berichts-Anhang; erster FFG-Zwischenbericht Ende Februar 2027 (ASR-Stelle unleserlich, von Christian bestätigt); Sprachregelung „Anwendungsfelder" statt „Use Cases"
- **AP 3:** RI-Infomaterialien (DSGVO/Soziale Arbeit) bis Mitte Oktober 2026 mit Feedback-Schleife der Praxispartner; Gender-Beobachtung (TN überwiegend männlich gelesen) als Learning für Co-Creation; Begleitforschungsbericht bleibt FFG-intern
- **AP 4:** Klagenfurt-Publikationspläne (3–4 Fallvignetten zu Bias-Detection, ggf. zwei Papers: Methoden/Workflow + Inhalte/Transfer; public license + symbolischer Vertrag); Kernprinzip Reproduzierbarkeit; Deliverable-Lesart „Empfehlungen statt striktes Set" in Diskussion; geplante Erhebungen bei den Partnern (IT-One-Pager ggf. mit NDA, Think-Aloud-Beobachtungen, Exkursion, SOS-Vernetzungstreffen)
- **Termine/Prozess:** Nächstes Quartalsmeeting 06.10.2026, 13:00–14:30; Protokolle künftig nur noch via uniCLOUD (kein Mailversand). Die offenen Jour-fixe-Punkte (AP-5-Stunden, AP-6-Zeitplan, AP-9-Policy, Glossar-Titel, KI-Richtlinie) wurden nicht behandelt und stehen jetzt als Agenda für den 06.10.

Offen daraus: FoWi-Paper-Eintrag in `wissen/README.md` von „unveröffentlicht" auf „veröffentlicht" umstellen, sobald die Zitation vorliegt; Partnerdaten aus dem Meeting (JAW-Dienstleister, interne Arbeitsgruppen) bewusst nur im internen Protokoll, nicht in knowledge.md.

---

## 2026-07-10 10:55 – handoff

**Summary:** Promptotyping-Docs per `/promptotyping check` auf den Ist-Stand gebracht und die offenen Fragen in vier Runden mit Christian geklärt. knowledge.md dokumentiert jetzt den AP-3-Abschluss, den AP-2-Stand und die Klagenfurt-LV als AP-4-Input; architecture.md und implementation.md beschreiben wieder die reale Konfiguration; das Glossar wurde redaktionell bereinigt und um einen Entwurf „Sensible Daten" erweitert (86 Einträge).

**Nachtrag 12.06.–07.07. (bisher nicht journaliert):** Innovationsworkshops am 29./30.06. durchgeführt (14 TN, Begleitforschungsbericht liegt seit 07/2026 vor, beide AP-3-Meilensteine vorzeitig erreicht); Workshop-Begleitseiten (`workshops/`) und Recht-Wissensseite (`recht/ki-recht-grundlagen.md`) publiziert; Public-Repo-Strategie „Ansatz A" beschlossen (24.06.) und `scripts/sync-glossar.py` als Spiegel-Baustein gebaut; `glossar/technisch.md` entfernt; Content-Health-Check am 07.07. (3 Commits: Projektnummer, AP-6/7-Meilensteine, AP-3-Abschluss auf Projektseiten).

**Decisions:**
- **Glossar-Redaktion (Christian, 10.07.):** Die drei „Neuer Begriff"-Notizen und Susis Demo-Notiz entfernt; die Anmerkungs-Konvention steht jetzt in der Redaktionsnotiz am Seitenanfang. Sabines Vorschlag zur Umbenennung von „AI Literacies / KI-Kompetenzen" bleibt bis zur Endversion offen. „Sensible Daten" (Art. 9 DSGVO) als DHC-Entwurf angelegt, RI reviewt.
- **Glossar-Endversion Mitte Juli:** wird als Git-Tag im Hub-Repo markiert; der öffentliche Spiegel folgt unabhängig davon (Split-Termin offen).
- **Klarstellung:** `socialai-workshops` ist das bestehende Workshop-Nachlese-Repo, NICHT das geplante Spiegel-Repo (neues Repo, leere History, Whitelist). In architecture.md dokumentiert.
- **Hub-Pflege bis AP-4-Start:** bleibt bei DHC (Status quo bestätigt); Epic-6-Zuständigkeitsfragen offen bis Konsortiumsentscheidung.
- **Sichtbarkeit interner Anmerkungen** im noch öffentlichen Repo: bekannt und akzeptiert bis zum Split.
- **AP 4:** Studentische Arbeiten der Klagenfurt-LV „Gender, Diversity & AI" (SS 2026, Sackl-Sharif/Steiner) fließen in die experimentelle Analyse ein (knowledge.md + arbeitspakete.md).
- **content-health-check.md bleibt bestehen:** nicht redundant zu `/promptotyping check` (prüft publizierte Seiten gegen Quellen statt Promptotyping-Docs gegeneinander); Abgrenzungsnotiz im Dokument ergänzt.

**Dead ends:** keine.

**Phase:** Implementation (Iteration). Alle fünf Kern-Docs existieren und sind aktuell (knowledge, requirements, architecture, implementation, journal); Health-Check-Mapping aktualisiert. Site produktiv, Link-Checker grün, sync-glossar-Testlauf sauber (strip: 3 Anmerkungen → 0).

**Open issues:**
- Glossar-Endversion blockiert durch: RI-Review „Sensible Daten" + Literacies-Titelentscheidung (Sabine). Danach Git-Tag setzen.
- AP-2-Kernteam-Treffen vom 01.07. fand statt; Ergebnisse/Protokoll fehlen im Hub (ggf. uniCLOUD). PRISMA-Update läuft planmäßig.
- Glossar-Verständlichkeits-Bestätigung durch Praxispartner:innen (Erfolgskriterium Epic 2) wurde bei den Workshops nicht erhoben; nächste Gelegenheit AP 7.
- Jour-fixe-Agenda in knowledge.md („Offene Punkte", Stand 10.07.): AP-5-RI-Stunden, AP-6-Zeitplan, AP-9-Publikations-Policy, AP-2-Protokoll.
- AP 4 (ab 10/2026): JAW-Antwort zur Iterativ-Frage und SOS-KD-Prompts stehen weiter aus.

**Next steps:**
1. RI-Review für „Sensible Daten" anstoßen und Literacies-Frage mit Sabine klären (Mail oder nächstes Treffen)
2. Nach beiden Klärungen: Glossar-Endversion als Git-Tag markieren
3. AP-2-Protokoll vom 01.07. besorgen und Ergebnisse in knowledge.md nachtragen
4. Jour-fixe-Agenda-Punkte (siehe knowledge.md) beim nächsten Quartalstreffen einbringen

**Nachtrag (gleicher Tag, nach dem Handoff):**
- **Remote-Sync:** Sabines Web-UI-Commit vom 08.07. (Literacies-Eintrag + Fußnote Long/Magerko) per Rebase integriert. Zwei Rendering-Fehler daraus repariert (Zeilenumbruch im Wort, führendes Leerzeichen vor der Fußnoten-Definition, das das Fußnoten-Plugin aushebelte); der unvollständige Satzanfang liegt als `***Anmerkung DHC:***` bei Sabine (Commit e87767e)
- **Content Health Check durchgeführt** (3 parallele Prüf-Agenten): Faktenabgleich OK (alle Stunden/Summen/Termine korrekt), Glossar 14/14 Kick-off-Begriffe, Struktur OK. Mechanische Befunde umgesetzt (Commit f411c7e): Homepage-Projektnummer korrekt gelabelt, AP-4-Versuchsdesign aus dem Antrag destilliert, Urheberrecht als RI-Aufgabe ergänzt, AP-2-Meilenstein-Verschiebung vermerkt, Context/Kontext-Sortierung. Neue Klärungspunkte in der Jour-fixe-Liste: Antrags-Deliverable „KI-Richtlinie für Organisationen" (AP 3) verschwunden?; Lizenz-Diskrepanz CC BY-SA vs. MIT und 3 vs. 2 Publikationen (AP 8/9)

---

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
