# Technisches Glossar

> KI- und Technologie-Begriffe, verständlich erklärt. Übernommen und adaptiert vom [Legal History Hub Tutorial](https://github.com/DigitalHumanitiesCraft/legal-history-hub).

---

## A

### Alignment
Der Prozess, ein KI-Modell so zu trainieren, dass es hilfreich, harmlos und ehrlich antwortet. Methoden wie RLHF und Constitutional AI sind Teil davon.

### API
**Application Programming Interface** – eine Schnittstelle, über die Programme miteinander kommunizieren. Relevant für die Anbindung von KI-Modellen an Anwendungen.

### Autoregressive Generierung
Das Prinzip, nach dem LLMs Text erzeugen: Jedes vorhergesagte Token wird Teil des Kontexts für die nächste Vorhersage. Das Modell baut seinen Output Wort für Wort auf.

---

## C

### Chain of Thought
**CoT** – eine Prompting-Technik, bei der man das Modell auffordert, schrittweise zu denken (z.B. „let's think step by step"). Verbessert die Qualität bei komplexen Aufgaben, weil Zwischenschritte explizit werden.

### Context Engineering
Die systematische Gestaltung des Kontexts, den ein LLM erhält: Auswahl, Kompression und Strukturierung von Informationen im Context Window. Geht über Prompt Engineering hinaus, weil nicht nur die Frage, sondern der gesamte mitgegebene Kontext optimiert wird.

### Context Rot
Die Leistung eines LLM verschlechtert sich, je mehr Text im Context Window steht – auch bei inhaltlich einfachen Aufgaben. Irrelevante Informationen lenken die Aufmerksamkeitsmechanismen ab. Mehr Kontext ≠ bessere Ergebnisse.

### Context Window
Das „Arbeitsgedächtnis" eines LLM: der maximale Textumfang (in Tokens), den das Modell bei einer Anfrage verarbeiten kann. Umfasst Input (Anfrage + Kontext) und Output (generierte Antwort).

---

## E

### Embedding
Eine mathematische Darstellung von Text als Zahlenvektor in einem hochdimensionalen Raum. Ähnliche Bedeutungen liegen nahe beieinander: „Hund" und „Katze" sind näher als „Hund" und „Stein". So kann ein LLM Bedeutung mathematisch verarbeiten.

---

## F

### Few-Shot Prompting
Eine Prompting-Technik, bei der man dem Modell einige Beispiele im Prompt mitgibt, die das gewünschte Eingabe-Ausgabe-Format zeigen. Das Modell lernt das Muster aus dem Kontext, ohne neu trainiert zu werden.

---

## H

### Halluzination
Siehe [Konfabulation](#konfabulation). Der ältere, aber gebräuchlichere Begriff für dasselbe Phänomen.

---

## K

### Konfabulation
Wenn ein LLM plausibel klingende, aber erfundene Informationen erzeugt: falsche Zitate, nicht existierende Quellen, fehlerhafte Zahlen. Kein Fehler, sondern ein strukturelles Merkmal der Wahrscheinlichkeitsvorhersage. Auch „Halluzination" genannt.

### Knowledge Cutoff
Der Wissensstichtag eines LLM: das Datum, bis zu dem die Trainingsdaten reichen. Alles danach kennt das Modell nicht, sofern es keine externen Tools (z.B. Websuche) nutzt.

---

## L

### LLM
**Large Language Model** – ein KI-Modell, das auf riesigen Textmengen trainiert wurde und menschenähnlichen Text generieren kann. Beispiele: Claude, GPT, Gemini. Kernfunktion: Next Token Prediction.

---

## N

### Next Token Prediction
Die Kernfunktion von LLMs: das nächste Token in einer Sequenz vorhersagen, basierend auf dem bisherigen Kontext. Dieser einfache Mechanismus, massiv skaliert, erzeugt das Verhalten, das wir beobachten.

---

## O

### Open Source / Open Weights
**Open Source** bedeutet, dass der gesamte Quellcode öffentlich ist und frei verwendet werden darf. **Open Weights** bedeutet, dass nur die trainierten Modellgewichte veröffentlicht werden, nicht der Trainingscode oder die Daten. Die meisten „offenen" LLMs sind Open Weights, nicht wirklich Open Source.

---

## P

### Post-Training
Die Phase nach dem Pre-Training, in der ein LLM zum hilfreichen Assistenten geformt wird. Umfasst Supervised Fine-Tuning (SFT) und RLHF. Fügt kein neues Wissen hinzu, sondern formt das Verhalten.

### Pre-Training
Die erste Trainingsphase eines LLM: Das Modell lernt aus Billionen von Tokens, Muster in Sprache zu erkennen. Das Ergebnis ist eine verlustbehaftete, probabilistische Kompression der Trainingsdaten.

### Prompt Brittleness
Das Phänomen, dass minimale Änderungen an einem Prompt (ein Komma, ein Synonym) die Ergebnisse eines LLM stark beeinflussen können, obwohl die Bedeutung identisch ist. Prompting ist keine exakte Wissenschaft.

### Prompt Engineering
Die Technik, Anfragen an ein KI-Modell so zu formulieren, dass nützliche Ergebnisse entstehen. Umfasst Techniken wie Chain of Thought, Few-Shot Prompting und System Prompts.

### Promptotyping
Eine Methodik für die iterative Zusammenarbeit zwischen Mensch und KI. Kernprinzip: Dokumente sind die Quelle der Wahrheit, Code ist ein austauschbares Artefakt. Vier Phasen: Preparation → Exploration → Distillation → Implementation.

---

## R

### RLHF
**Reinforcement Learning from Human Feedback** – eine Methode im Post-Training von LLMs. Menschen bewerten Modellantworten, das Modell lernt aus diesem Feedback. Teil des Alignment-Prozesses.

---

## S

### Slop
Minderwertiger, formelhafter KI-Text. Erkennbar an: „Delve into", „It is crucial to note", „Furthermore", inflationärer Verwendung von Em-Dashes, Buzzwords wie „ever-evolving". Gegenmittel: kritisches Lesen und klare Anweisungen im Prompt.

### Sycophancy
Die Tendenz von LLMs, Nutzer:innen zuzustimmen statt zu widersprechen. Das Modell priorisiert Zustimmung über Wahrheit, weil es im Post-Training für nutzerfreundliche Antworten belohnt wurde. Gegenmittel: kritisches Hinterfragen.

### System Prompt
Vorab-Anweisungen, die das Verhalten eines LLM für die gesamte Konversation steuern. Werden vor der eigentlichen Nutzeranfrage gesetzt und definieren Rolle, Tonfall und Regeln.

---

## T

### Token
Die kleinste Einheit, in die ein LLM Text zerlegt. Ein Token ist oft ein Wort oder ein Wortteil. 100 Tokens ≈ 75 englische Wörter. Relevant für: Kosten, Context Window, Verarbeitungsgeschwindigkeit.

### Tokenizer
Das Werkzeug, das Text in Tokens zerlegt. Verschiedene Modelle verwenden verschiedene Tokenizer – deshalb kann dasselbe Wort unterschiedlich viele Tokens kosten.

### Transformer
Die Architektur hinter modernen LLMs (vorgestellt 2017, „Attention Is All You Need"). Der zentrale Mechanismus ist Attention: Das Modell lernt, welche Teile des Eingabetexts füreinander relevant sind.
