# Glossar (gesamt)

> *Anmerkung zu den juridischen Definitionen*: Da der Gesetzgeber im Normtext überwiegend das generische Maskulinum verwendet, folgt das Glossar in seinen rechtlichen Ausführungen dieser Terminologie, um eine eindeutige Zuordnung zum Gesetzeswortlaut zu gewährleisten.

> *Anmerkung zu den technologischen Definitionen*: KI- und Technologie-Begriffe, verständlich erklärt. Übernommen und adaptiert vom [Legal History Hub Tutorial](https://github.com/DigitalHumanitiesCraft/legal-history-hub).

---

## A

### AI Act / KI-Verordnung

Verordnung der Europäischen Union zur Regulierung von Künstlicher Intelligenz (AI Act, Verordnung (EU) 2024/1689). Sie regelt die Entwicklung und den Betrieb von KI und folgt dabei einem "risikobasierten Ansatz" - je höher das Risiko, das von einem KI-System ausgeht, desto strenger die Verpflichtungen. Dabei kennt sie folgende Risikokategorien: verbotene Praktiken (zB Emotionserkennung am Arbeitsplatz und social scoring), Hochrisiko-KI (zB KI im Personalmanagement, in der Zuerkennung öffentlicher Leistungen oder in der Justiz), Transparenzrisiken (Wenn KI mit Personen interagiert, Deepfakes oder sonstige Inhalte generiert) und minimale Risiken (alle übrigen Systeme). Die KI-Verordnung unterscheidet folgende zentrale Rollen, nach denen sich wiederum die konkreten Pflichten messen: **Anbieter** (entwickelt/vermarktet KI-Systeme), **Betreiber** (setzt KI-Systeme zu beruflichen Zwecken ein) und **Nutzer:in** (verwendet KI). Relevant für die Soziale Arbeit, da der Einsatz von KI im Kontext vulnerabler Gruppen besondere Pflichten mit sich bringt.

### AI Agents / Agentic AI

KI-Systeme, die eigenständig Teilaufgaben planen und ausführen können, über einfache Frage-Antwort-Interaktion hinaus. Im Projektkontext eine offene Frage: Inwieweit werden agentenbasierte KI-Systeme für die Soziale Arbeit relevant, und welche Chancen und Risiken bringen sie mit sich?

### Alignment
Der Prozess, ein KI-Modell so zu trainieren, dass es hilfreich, harmlos und ehrlich antwortet. Methoden wie [RLHF](#rlhf) und [Constitutional AI](#constitutional-ai) sind Teil davon.

### API
**Application Programming Interface**. Eine Schnittstelle, über die Programme miteinander kommunizieren. Relevant für die Anbindung von KI-Modellen an Anwendungen.

### Autoregressive Generierung
Das Prinzip, nach dem [LLMs](#llm) Text erzeugen. Jedes vorhergesagte [Token](#token) wird Teil des Kontexts für die nächste Vorhersage. Das Modell baut seinen Output Wort für Wort auf.

### Automation Bias

Eine Unterkategorie von [Bias](#Bias). Die Tendenz, sich in bestimmten Situationen übermäßig auf automationsunterstützte Entscheidungsfindungssysteme zu verlassen, ohne deren Output kritisch zu prüfen (Wickens/Clegg/Vieane/Sebok 2015, 729).
Demnach werden automationsunterstützte Entscheidungen oder Empfehlungen im praktischen Einsatz eher für gültig und berechtigt gehalten, wenngleich diese möglicherweise falsche oder unvollständige Informationen liefern (Research Institute 2025, 122).
- **Rechtlich:** Neigung zu einem automatischen oder übermäßigen Vertrauen in eine von einem KI-System hervorgebrachte Ausgabe (Art 14 Abs 4 lit b KI-VO)

---

## B

### Benchmark
Standardisierte Testsätze zur Vergleichsmessung der Leistungsfähigkeit von KI-Modellen. Benchmarks bilden die Grundlage für Aussagen wie „Modell X ist besser als Modell Y", sind aber methodisch begrenzt. Ein zentrales Problem ist Data Contamination, wenn Testdaten unbeabsichtigt im Training enthalten waren. Hohe Benchmark-Werte korrelieren nicht zwingend mit guter Leistung in realen Anwendungen.

### Bias

Systematische Verzerrung in Daten, Modellen oder Entscheidungen. Im Projekt in mehreren Dimensionen relevant:
- **Soziologisch:** gesellschaftliche Vorurteile und strukturelle Diskriminierung
- **Technisch:** Systematische Verzerrung in den Antworten eines [LLM](#llm), die aus Trainingsdaten und Trainingsprozess stammt.[^bias] Bias zeigt sich etwa in Geschlechter- und Altersstereotypen oder in der Bevorzugung bestimmter Perspektiven. Die Forschung unterscheidet repräsentative Schäden (Stereotypisierung) und allokative Schäden (ungleiche Ressourcenverteilung). Bias lässt sich nicht vollständig beseitigen, sondern nur sichtbar machen und reflektiert kompensieren. 
- **Intersektional:** Überschneidung und Verstärkung mehrerer Diskriminierungsdimensionen
- **Unconscious/implizit:** unbewusste Voreingenommenheit von Nutzer:innen und Entwickler:innen

---

## C

### Chancengerechtigkeit

Bewusst abgegrenzt von **Chancengleichheit**. Während Chancengleichheit formale Gleichbehandlung meint, zielt Chancengerechtigkeit darauf ab, unterschiedliche Ausgangsbedingungen auszugleichen -also faire Ergebnisse statt gleicher Behandlung. Zentrales Leitkonzept des SocialAI-Projekts.

### Chain of Thought
**CoT**, eine Prompting-Technik, bei der das Modell aufgefordert wird, schrittweise zu denken, etwa durch „let's think step by step". Verbessert die Qualität bei komplexen Aufgaben, weil Zwischenschritte explizit werden. Mit der Verbreitung von [Reasoning-Modellen](#reasoning-modell) verliert die manuelle CoT-Aufforderung an Bedeutung, weil diese Modelle das Verhalten internalisiert haben.

### Chatbot
Eine Anwendung, die eine Konversationsoberfläche um ein Sprachmodell legt. Bekannte Beispiele sind ChatGPT, Claude und Gemini. Der Chatbot ist nicht das Modell selbst, sondern die Schnittstelle dazu. Zwischen Eingabe und Modellantwort liegen weitere Schritte, etwa Sicherheitsprüfungen, Tool-Anbindungen oder Suchfunktionen.

### Constitutional AI
Ein Trainingsverfahren von Anthropic, bei dem ein Modell anhand einer natürlichsprachigen „Verfassung" aus Prinzipien geformt wird, statt nur auf menschliche Bewertungen angewiesen zu sein.[^cai] In zwei Phasen wird das Modell zunächst zu Selbstkritik gegen die Prinzipien angeleitet und anschließend per Reinforcement Learning aus den eigenen Bewertungen weitertrainiert. Das Verfahren reduziert die Menge benötigter menschlicher Labels und ist Teil des [Alignment](#alignment).


### Context / Kontext

Die Rahmenbedingungen, die einen KI-Output beeinflussen. Umfasst den Prompt selbst, System-Instruktionen, Konversationshistorie und implizite Annahmen des Modells. Für die Soziale Arbeit besonders relevant, weil Kontextinformationen über Klient:innen die Qualität und Fairness der KI-Antworten stark beeinflussen.

### Context Engineering
Die systematische Gestaltung des Kontexts, den ein [LLM](#llm) erhält. Auswahl, Kompression und Strukturierung von Informationen im [Context Window](#context-window). Geht über [Prompt Engineering](#prompt-engineering) hinaus, weil nicht nur die Frage, sondern der gesamte mitgegebene Kontext optimiert wird.

### Context Rot
Die Leistung eines [LLM](#llm) verschlechtert sich, je mehr Text im [Context Window](#context-window) steht, auch bei inhaltlich einfachen Aufgaben. Irrelevante Informationen lenken die Aufmerksamkeitsmechanismen ab. Mehr Kontext bedeutet nicht automatisch bessere Ergebnisse.

### Context Window
Das Arbeitsgedächtnis eines [LLM](#llm). Der maximale Textumfang in [Tokens](#token), den das Modell bei einer Anfrage verarbeiten kann. Umfasst Input (Anfrage und Kontext) und Output (generierte Antwort). Aktuelle Modelle bieten zwischen rund 100.000 und einer Million Tokens. Inhalte außerhalb dieses Fensters sind dem Modell nicht zugänglich.


---

## D

### Datenschutz / DSGVO

Datenschutz-Grundverordnung der Europäischen Union (DSGVO, Verordnung (EU) 2016/679). Im Projektkontext zentrale Frage: Welche personenbezogenen Daten dürfen in KI-Tools eingegeben werden? Besondere Relevanz bei Daten von Klient:innen der Sozialen Arbeit, die oft zu vulnerablen Gruppen gehören.

### Deskilling

Risiko, dass Fachkräfte durch KI-Nutzung professionelle Kompetenzen verlieren. Wenn KI-generierte Texte, Einschätzungen oder Empfehlungen unkritisch übernommen werden, kann das fachliche Urteilsvermögen abnehmen -ein relevantes Risiko für die Qualität Sozialer Arbeit.

### Diversität

Vielfalt in verschiedenen Dimensionen (Geschlecht, Alter, ethnische Zugehörigkeit, Behinderung etc.). Im Projekt sowohl als Forschungsgegenstand (Wie bildet generative KI Diversität ab? Wo entstehen Verzerrungen?) als auch als Gestaltungsprinzip für inklusive KI-Nutzung relevant.

### Distillation
Ein Verfahren, bei dem ein kleineres, schnelleres Modell aus einem größeren abgeleitet wird, indem es lernt, dessen Outputs nachzubilden. Distillierte Modelle laufen mit deutlich weniger Rechenleistung, erreichen aber meist nicht die volle Qualität des Ursprungsmodells. Viele frei verfügbare Open-Weights-Modelle sind Distillationen größerer kommerzieller Modelle.

---

## E

### Embedding
Eine mathematische Darstellung von Text als Zahlenvektor in einem hochdimensionalen Raum. Ähnliche Bedeutungen liegen nahe beieinander. „Hund" und „Katze" sind näher als „Hund" und „Stein". So kann ein [LLM](#llm) Bedeutung mathematisch verarbeiten. Embeddings sind die Grundlage von [RAG](#rag) und semantischer Suche.

### Explainable AI (XAI)
Methoden und Werkzeuge, die Entscheidungen von KI-Systemen nachvollziehbar machen. Bei klassischem Machine Learning durch Verfahren wie SHAP oder LIME. Bei [LLMs](#llm) ist Erklärbarkeit nur eingeschränkt möglich, weil die Entscheidungsprozesse über Milliarden von Parametern verteilt sind. Das Feld der Mechanistic Interpretability untersucht, welche internen Strukturen welche Verhaltensweisen erzeugen. Im regulatorischen Kontext bleibt Erklärbarkeit eine zentrale Anforderung.

---

## F

### Fairness (im KI-Kontext)

*Definition folgt aus AP 2 (Literatur-Review).* Vorläufig: die Eigenschaft eines KI-Systems, keine systematische Benachteiligung bestimmter Gruppen in seinen Outputs zu erzeugen. Im Projektkontext eng verknüpft mit Bias und Chancengerechtigkeit.

### Feminist AI Literacies

*Definition folgt aus AP 2 (Literatur-Review).* Vorläufig: ein intersektional-feministischer Ansatz zum Verständnis und zur kritischen Nutzung von KI, der Machtstrukturen und Geschlechterverhältnisse in der Technologieentwicklung und -anwendung reflektiert.

### Few-Shot Prompting
Eine [Prompting-Technik](#prompt-engineering), bei der dem Modell einige Beispiele im Prompt mitgegeben werden, die das gewünschte Eingabe-Ausgabe-Format zeigen. Das Modell lernt das Muster aus dem Kontext, ohne neu trainiert zu werden.

### Fine-Tuning
Die Anpassung eines vortrainierten [LLM](#llm) auf einen spezifischen Anwendungsbereich oder Stil durch zusätzliches Training mit ausgewählten Daten. Fine-Tuning verändert die Modellgewichte und prägt das Modell dauerhaft. Es ist aufwendig und erfordert geeignete Daten. Für viele Anwendungsfälle sind [Prompt Engineering](#prompt-engineering) und [RAG](#rag) effizientere Wege, weil sie ohne Eingriff in das Modell auskommen.

### Frontier Model
Bezeichnung für die jeweils leistungsfähigsten Modelle einer Generation, etwa GPT-5, Claude Opus oder Gemini 2.5 Pro. Der Begriff hat regulatorische Bedeutung, weil der EU AI Act und vergleichbare Regelwerke an Frontier-Modelle besondere Pflichten knüpfen, etwa systemische Risikoanalyse und Cybersicherheitsstandards. Welche Modelle als Frontier gelten, verschiebt sich kontinuierlich.

---
## G

### Guardrails
Schutzmechanismen, die unerwünschte Antworten eines [LLM](#llm) verhindern sollen. Sie reichen von Filtern für problematische Inhalte über Themensperren bis zu Plausibilitätsprüfungen vor und nach der Modellantwort. Guardrails sind technisch nicht perfekt und lassen sich teilweise umgehen, siehe [Jailbreaking](#jailbreaking) und [Prompt Injection](#prompt-injection). Sie ergänzen redaktionelle und fachliche Kontrolle, ersetzen sie nicht.

---

## H

### Halluzination
Siehe [Konfabulation](#konfabulation). Der ältere und gebräuchlichere Begriff für dasselbe Phänomen.

---

## I

### Intersektionalität

Konzept, das die Überschneidung und Wechselwirkung verschiedener Diskriminierungsdimensionen beschreibt. Im Projekt fokussiert auf die Achsen: Geschlecht, Alter und Migration. Als Visualisierung wird ein Venn-Diagramm verwendet, um die Überlappung und gegenseitige Verstärkung sichtbar zu machen.

---

## J

### Jailbreaking
Techniken, mit denen Schutzmechanismen eines [LLM](#llm) umgangen werden, etwa um Antworten zu sensiblen oder sicherheitskritischen Themen zu erzwingen. Jailbreaks nutzen sprachliche Umwege, Rollenspiele oder formale Tricks. Die Abwehr ist ein laufendes Wettrennen zwischen Anbietern und Nutzer:innen. Schutzmechanismen sind nicht zuverlässig, in sensiblen Anwendungsfeldern bleiben zusätzliche Kontrollebenen nötig.

---

## K

### KI-Literacy
Die Fähigkeit, KI-Systeme informiert zu nutzen, kritisch zu beurteilen und ihre Wirkungen einzuordnen. KI-Literacy umfasst technisches Grundverständnis, einen Blick für [Bias](#bias) und [Konfabulation](#konfabulation), Kenntnis rechtlicher Rahmen sowie die Fähigkeit, Einsatzentscheidungen zu reflektieren. Der Begriff ist analog zu Medienkompetenz konzipiert und seit 2024 auch im EU AI Act als organisationale Pflicht verankert. Eine breitere Behandlung findet sich im [Hauptglossar](README.md#ki-kompetenz) unter KI-Kompetenz.

### Knowledge Cutoff
Der Wissensstichtag eines [LLM](#llm). Das Datum, bis zu dem die Trainingsdaten reichen. Alles danach kennt das Modell nicht, sofern es keine externen Tools wie Websuche oder [RAG](#rag) nutzt.

### Konfabulation
Wenn ein [LLM](#llm) plausibel klingende, aber erfundene Informationen erzeugt. Falsche Zitate, nicht existierende Quellen, fehlerhafte Zahlen. Kein Fehler, sondern ein strukturelles Merkmal der Wahrscheinlichkeitsvorhersage über [Next Token Prediction](#next-token-prediction). Auch „Halluzination" genannt. Der Begriff Konfabulation beschreibt das Phänomen sachlich treffender, weil das Modell Lücken im verfügbaren Wissen mit plausiblem Material auffüllt, statt etwas wahrzunehmen, das nicht da ist.[^konfabulation]

---

## L

### LLM
**Large Language Model**. Ein KI-Modell, das auf riesigen Textmengen trainiert wurde und menschenähnlichen Text generieren kann. Beispiele sind Claude, GPT und Gemini. Kernfunktion ist [Next Token Prediction](#next-token-prediction). Aktuelle LLMs basieren auf der [Transformer](#transformer)-Architektur.

### LLM as a Judge
Ein Verfahren, bei dem ein [LLM](#llm) die Outputs eines anderen Modells (oder eigene frühere Outputs) bewertet, etwa in Evaluationen, Vergleichstests oder Filterpipelines.[^judge] LLM-as-a-Judge ist deutlich kostengünstiger als menschliche Bewertung und skaliert gut, hat aber systematische Schwächen. Bewertende Modelle bevorzugen eigene Schreibstile, längere Antworten und die zuerst gezeigte Option (Position Bias). Im Kontext von Auditing und Fairnessprüfung gilt deshalb, dass LLM-as-a-Judge kein Ersatz für menschliche Validierung ist, sondern ein vorgelagertes Filter- und Skalierungswerkzeug.

---

## M

### Matthäus-Effekt

"Wer hat, dem wird gegeben" -das Phänomen, dass Weiterbildungsangebote überproportional von bereits gut qualifizierten Personen genutzt werden. Relevant für die Frage, wie KI-Kompetenz in der Sozialen Arbeit vermittelt wird und wie bestehende Ungleichheiten im Zugang zu digitaler Bildung nicht verstärkt werden.

### MCP
**Model Context Protocol**. Ein offener Standard, der im November 2024 von Anthropic vorgestellt wurde und die Verbindung von KI-Anwendungen mit externen Datenquellen, Tools und Diensten vereinheitlicht. Wird oft als „USB-C für KI-Anwendungen" beschrieben, weil eine Schnittstelle viele unterschiedliche Anbindungen ersetzt. Hat sich 2025 rasch als Industriestandard etabliert und wird auch von OpenAI, Google und Microsoft unterstützt.


### Menschliche Aufsicht / Human Oversight 

- **rechtlich:** KI-Systeme müssen so entwickelt werden, dass sie während ihres Einsatzes von geeigneten Personen wirksam beaufsichtigt werden können. Dadurch sollen Risiken für Gesundheit, Sicherheit oder Grundrechte Betroffener verhindert oder zumindest minimiert werden. Die Aufsichtsmaßnahmen müssen sich dabei an dem Kontext des KI-Einsatzes, an dem Autonomiegrad des Systems und an den Risiken, die sich durch die Nutzung ergeben können, orientieren. Aufsichtspersonen müssen insbesondere in der Lage sein, die Fähigkeiten und Grenzen des KI-Systems zu verstehen, seinen Betrieb ordnungsgemäß zu überwachen, Fehlfunktionen zu erkennen, KI-Ausgaben nicht ungeprüft zu vertrauen ("Automation Bias") KI-Ergebnisse richtig zu interpretieren, und erforderlichenfalls den Systembetrieb mit einer „Stopptaste“ zu unterbrechen (siehe Art 14 KI-VO)


### Multimodalität
Die Fähigkeit eines KI-Systems, mehrere Medien gleichzeitig zu verarbeiten, etwa Text, Bild, Audio und Video. Multimodale Modelle können ein Foto beschreiben, eine Tonaufnahme transkribieren oder ein Diagramm interpretieren. Vision-Language-Modelle bilden den verbreitetsten Untertyp. Multimodalität vergrößert den Datenschutzaufwand, weil sensible Daten in mehr Formaten verarbeitet werden.

---

## N

### Next Token Prediction
Die Kernfunktion von [LLMs](#llm). Das nächste [Token](#token) in einer Sequenz vorhersagen, basierend auf dem bisherigen Kontext. Dieser einfache Mechanismus, massiv skaliert, erzeugt das Verhalten, das wir beobachten.

---

## O

### Open Source / Open Weights
**Open Source** bedeutet, dass der gesamte Quellcode öffentlich ist und frei verwendet werden darf. **Open Weights** bedeutet, dass nur die trainierten Modellgewichte veröffentlicht werden, nicht der Trainingscode oder die Daten. Die meisten „offenen" LLMs sind Open Weights, nicht wirklich Open Source.

---

## S

### Soziale Arbeit

Professionelles Handlungsfeld, das im Projekt als Anwendungskontext für KI untersucht wird. Besonderheiten: Arbeit mit vulnerablen Gruppen, hohe ethische Anforderungen, frauendominiertes Berufsfeld, vielfältige Einsatzgebiete (Jugendhilfe, Beratung, Gemeinwesenarbeit u.a.).


---

