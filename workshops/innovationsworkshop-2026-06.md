# Innovationsworkshop – Tag 1 (29.06.2026)

> [!NOTE]
> Begleitseite zum ersten Innovationsworkshop des Projekts **SocialAI** am 29.06.2026, 9–13 Uhr, Universität Graz (Raum SR 03.K1). Ablauf, die wichtigsten Begriffe und ein Spickzettel zum Prompten – zum Nachschlagen während und nach dem Workshop.

Tag 1 dreht sich um **Technik und Methode**: Wie funktioniert generative KI, wie schreibt man gute Prompts, und wo liegen die Grenzen (Bias)? Die Anwendung auf konkrete Arbeitsfelder und die rechtliche Seite folgen an Tag 2 (30.06.) mit dem Research Institute.

## Was du mitbringst

- Einen **Laptop**.
- Ein **kostenloses KI-Tool**, idealerweise vorab eingeloggt. Am einfachsten [Gemini](https://gemini.google.com) (mit einem Google-Konto), alternativ [Claude](https://claude.ai). Wenn du eine eigene Lizenz (z. B. ChatGPT, Copilot) hast, gern damit.

## Ablauf

| Block | Zeit | Thema |
|-------|------|-------|
| Ankommen | 15 Min. | Begrüßung, Ziele, Vorwissensabfrage |
| A | 50 Min. | Grundlagen: Wie funktioniert ein Sprachmodell? |
| Pause | 15 Min. | |
| B | 50 Min. | Vom Prompt zum Kontext: Context Engineering |
| C | 40 Min. | Hands-on: selbst prompten |
| D | 15 Min. | Demo: Was agentische KI heute schon kann |
| Pause | 10 Min. | |
| E | 35 Min. | Bias und Fairness |

## Die wichtigsten Begriffe

Alle Begriffe aus dem Workshop sind im [Gesamtglossar](glossar/README.md) erklärt (mit Kategorie-Filter und A–Z-Leiste), darunter: LLM, Token, Context Window, Next Token Prediction, Prompt Engineering, Context Engineering, Halluzination, Bias und KI-Agenten.

## Spickzettel: gutes Prompten in 3 Schichten

**Merksatz:** Ein schlechtes Ergebnis ist meist kein KI-Problem, sondern ein **Kontextproblem**. Gutes Prompten heißt: der KI den Kontext geben, den auch ein Mensch für die Aufgabe bräuchte.

Bevor du absendest, beantworte drei Fragen:

1. **Rolle / System** – Wer soll die KI sein? (Perspektive, Ton, für wen)
   > „Du bist eine erfahrene Moderatorin für Teamentwicklung."
2. **Auftrag / Format** – Was genau soll herauskommen? (Ziel, Umfang, Form – also z. B. Tabelle, Stichpunkte oder Fließtext, und wie lang)
   > „Erstelle einen Ablaufplan für einen 6-stündigen Team-Tag als Tabelle mit Uhrzeit, Programmpunkt und Ziel. Ton: konkret, nicht werblich."
3. **Wissen / Daten** – Was muss die KI über deinen konkreten Fall wissen, das sie nicht erraten kann?
   > „Das Team hat 12 Personen, zuletzt gab es Spannungen nach einer Umstrukturierung. Ort: Seminarhaus am Land, Budget 1.500 €. Kein Outdoor-Programm."

**Vorher → Nachher**

*Vorher (naiv):* „Plane mir eine Team-Klausur." → ein Plan, der auf jedes Team passt und auf keins.

*Nachher:* Die drei Schichten einfach hintereinander ergeben einen Prompt:

> Du bist eine erfahrene Moderatorin für Teamentwicklung. Erstelle einen Ablaufplan für einen 6-stündigen Team-Tag als Tabelle mit Uhrzeit, Programmpunkt und Ziel. Ton: konkret, nicht werblich. Das Team hat 12 Personen, zuletzt gab es Spannungen nach einer Umstrukturierung. Ort: Seminarhaus am Land, Budget 1.500 €. Kein Outdoor-Programm.

Ergebnis: ein Plan, der die 12 Personen, die Spannungen, Ort, Budget und No-Gos berücksichtigt – statt Einheitsbrei.

**Faustregeln**

- Lieber zu viel Kontext als zu wenig – die KI rät sonst.
- Format explizit vorgeben (Tabelle, Stichpunkte, Länge), sonst kommt Fließtext.
- Iterieren ist normal: nachschärfen statt neu anfangen.

**Ergebnis prüfen** – die KI liefert immer eine Antwort, aber nicht immer eine gute:

- Stimmt es fachlich? Nicht ungeprüft übernehmen – KI erfindet manchmal Plausibles (Zahlen, Namen, Quellen).
- Passt es wirklich zu meinem Fall (die 12 Personen, die Spannungen, das Budget) oder ist es generisch geblieben?
- Fehlt etwas? Dann gezielt nachschärfen statt neu anfangen.

## Weiterführend

- [Orientierungsleitfaden](https://digitalesozialearbeit.github.io/orientierungsleitfaden/) – ausführliche Beispiele mit vollständigen Prompting-Prozessen.
- [Anwendungsfelder generativer KI](wissen/anwendungsfelder.md) – die vier Felder, die an Tag 2 vertieft werden.
- **Gemeinsames Pad** – Link folgt am Workshop-Tag.

## Ergebnisse

> [!NOTE]
> Wird nach dem Workshop ergänzt: die gemeinsam gesammelten Prompts und die wichtigsten Erkenntnisse aus Block C.
