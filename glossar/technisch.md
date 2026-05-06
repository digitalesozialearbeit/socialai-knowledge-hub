# Technisches Glossar

> KI- und Technologie-Begriffe, verständlich erklärt. Übernommen und adaptiert vom [Legal History Hub Tutorial](https://github.com/DigitalHumanitiesCraft/legal-history-hub).

---

## A

### Alignment
Der Prozess, ein KI-Modell so zu trainieren, dass es hilfreich, harmlos und ehrlich antwortet. Methoden wie [RLHF](#rlhf) und [Constitutional AI](#constitutional-ai) sind Teil davon.

### API
**Application Programming Interface**. Eine Schnittstelle, über die Programme miteinander kommunizieren. Relevant für die Anbindung von KI-Modellen an Anwendungen.

### Autoregressive Generierung
Das Prinzip, nach dem [LLMs](#llm) Text erzeugen. Jedes vorhergesagte [Token](#token) wird Teil des Kontexts für die nächste Vorhersage. Das Modell baut seinen Output Wort für Wort auf.

---

## B

### Benchmark
Standardisierte Testsätze zur Vergleichsmessung der Leistungsfähigkeit von KI-Modellen. Benchmarks bilden die Grundlage für Aussagen wie „Modell X ist besser als Modell Y", sind aber methodisch begrenzt. Ein zentrales Problem ist Data Contamination, wenn Testdaten unbeabsichtigt im Training enthalten waren. Hohe Benchmark-Werte korrelieren nicht zwingend mit guter Leistung in realen Anwendungen.

### Bias
Systematische Verzerrung in den Antworten eines [LLM](#llm), die aus Trainingsdaten und Trainingsprozess stammt.[^bias] Bias zeigt sich etwa in Geschlechter- und Altersstereotypen oder in der Bevorzugung bestimmter Perspektiven. Die Forschung unterscheidet repräsentative Schäden (Stereotypisierung) und allokative Schäden (ungleiche Ressourcenverteilung). Bias lässt sich nicht vollständig beseitigen, sondern nur sichtbar machen und reflektiert kompensieren. Eine breitere sozialwissenschaftliche Behandlung des Begriffs findet sich im [Hauptglossar](README.md#bias).

---

## C

### Chain of Thought
**CoT**, eine Prompting-Technik, bei der das Modell aufgefordert wird, schrittweise zu denken, etwa durch „let's think step by step". Verbessert die Qualität bei komplexen Aufgaben, weil Zwischenschritte explizit werden. Mit der Verbreitung von [Reasoning-Modellen](#reasoning-modell) verliert die manuelle CoT-Aufforderung an Bedeutung, weil diese Modelle das Verhalten internalisiert haben.

### Chatbot
Eine Anwendung, die eine Konversationsoberfläche um ein Sprachmodell legt. Bekannte Beispiele sind ChatGPT, Claude und Gemini. Der Chatbot ist nicht das Modell selbst, sondern die Schnittstelle dazu. Zwischen Eingabe und Modellantwort liegen weitere Schritte, etwa Sicherheitsprüfungen, Tool-Anbindungen oder Suchfunktionen.

### Constitutional AI
Ein Trainingsverfahren von Anthropic, bei dem ein Modell anhand einer natürlichsprachigen „Verfassung" aus Prinzipien geformt wird, statt nur auf menschliche Bewertungen angewiesen zu sein.[^cai] In zwei Phasen wird das Modell zunächst zu Selbstkritik gegen die Prinzipien angeleitet und anschließend per Reinforcement Learning aus den eigenen Bewertungen weitertrainiert. Das Verfahren reduziert die Menge benötigter menschlicher Labels und ist Teil des [Alignment](#alignment).

### Context Engineering
Die systematische Gestaltung des Kontexts, den ein [LLM](#llm) erhält. Auswahl, Kompression und Strukturierung von Informationen im [Context Window](#context-window). Geht über [Prompt Engineering](#prompt-engineering) hinaus, weil nicht nur die Frage, sondern der gesamte mitgegebene Kontext optimiert wird.

### Context Rot
Die Leistung eines [LLM](#llm) verschlechtert sich, je mehr Text im [Context Window](#context-window) steht, auch bei inhaltlich einfachen Aufgaben. Irrelevante Informationen lenken die Aufmerksamkeitsmechanismen ab. Mehr Kontext bedeutet nicht automatisch bessere Ergebnisse.

### Context Window
Das Arbeitsgedächtnis eines [LLM](#llm). Der maximale Textumfang in [Tokens](#token), den das Modell bei einer Anfrage verarbeiten kann. Umfasst Input (Anfrage und Kontext) und Output (generierte Antwort). Aktuelle Modelle bieten zwischen rund 100.000 und einer Million Tokens. Inhalte außerhalb dieses Fensters sind dem Modell nicht zugänglich.

---

## D

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

### MCP
**Model Context Protocol**. Ein offener Standard, der im November 2024 von Anthropic vorgestellt wurde und die Verbindung von KI-Anwendungen mit externen Datenquellen, Tools und Diensten vereinheitlicht. Wird oft als „USB-C für KI-Anwendungen" beschrieben, weil eine Schnittstelle viele unterschiedliche Anbindungen ersetzt. Hat sich 2025 rasch als Industriestandard etabliert und wird auch von OpenAI, Google und Microsoft unterstützt.

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

## P

### Post-Training
Die Phase nach dem [Pre-Training](#pre-training), in der ein [LLM](#llm) zum hilfreichen Assistenten geformt wird. Umfasst Supervised Fine-Tuning und [RLHF](#rlhf). Fügt kein neues Wissen hinzu, sondern formt das Verhalten. Viele systematische Verhaltensweisen wie [Sycophancy](#sycophancy) entstehen in dieser Phase.

### Pre-Training
Die erste Trainingsphase eines [LLM](#llm). Das Modell lernt aus Billionen von [Tokens](#token), Muster in Sprache zu erkennen. Das Ergebnis ist eine verlustbehaftete, probabilistische Kompression der Trainingsdaten.

### Prompt Brittleness
Das Phänomen, dass minimale Änderungen an einem Prompt (ein Komma, ein Synonym) die Ergebnisse eines [LLM](#llm) stark beeinflussen können, obwohl die Bedeutung identisch ist. [Prompting](#prompt-engineering) ist keine exakte Wissenschaft.

### Prompt Engineering
Die Technik, Anfragen an ein KI-Modell so zu formulieren, dass nützliche Ergebnisse entstehen. Umfasst Verfahren wie [Chain of Thought](#chain-of-thought), [Few-Shot Prompting](#few-shot-prompting) und [System Prompts](#system-prompt). Form und Reihenfolge der Information beeinflussen das Ergebnis erheblich.

### Prompt Injection
Ein Angriff, bei dem schädliche Anweisungen in Inhalte eingeschleust werden, die ein [LLM](#llm) verarbeitet.[^injection] Eine Webseite, ein Dokument oder eine E-Mail kann versteckte Anweisungen enthalten, die das Modell beim Lesen als Befehle interpretiert. Der Angriff funktioniert, weil ein LLM zwischen Inhalt und Anweisung nicht zuverlässig trennt. Besonders kritisch bei Anwendungen mit Tool-Zugriff oder [MCP](#mcp)-Anbindung.

### Promptotyping
Eine Methodik für die iterative Zusammenarbeit zwischen Mensch und KI.[^promptotyping] Kernprinzip ist, dass Dokumente die Quelle der Wahrheit sind und Code ein austauschbares Artefakt darstellt. Vier Phasen prägen den Ablauf, Preparation, Exploration, Distillation und Implementation.

---

## Q

### Quantisierung
Ein Verfahren, das die Präzision der Modellgewichte reduziert, etwa von 16 auf 8 oder 4 Bit, um Speicher- und Rechenbedarf zu senken. Quantisierte Modelle laufen auf günstigerer Hardware, teilweise sogar lokal auf dem eigenen Rechner. Die Qualität sinkt nur moderat. Praxisrelevant überall dort, wo Daten den eigenen Rechner oder das eigene Netzwerk nicht verlassen sollen.

---

## R

### RAG
**Retrieval-Augmented Generation**.[^rag] Ein Verfahren, das ein [LLM](#llm) mit externen Wissensquellen verbindet. Vor der Antwortgenerierung werden passende Dokumente aus einer Datenbank gesucht und dem Modell als Kontext mitgegeben. RAG ist die Standardarchitektur für KI-Werkzeuge, die mit organisationsspezifischem Wissen arbeiten, etwa internen Leitlinien oder Fachliteratur. RAG verringert [Konfabulation](#konfabulation), beseitigt sie aber nicht.

### Reasoning Modell
Eine Modellklasse, die seit 2024 verbreitet ist und vor der eigentlichen Antwort einen längeren internen Denkprozess erzeugt.[^reasoning] Beispiele sind OpenAI o1 und o3, DeepSeek R1 und Claude-Modelle mit aktiviertem Thinking-Modus. Reasoning-Modelle erreichen bei mathematischen, logischen und Programmieraufgaben deutlich bessere Ergebnisse als klassische [LLMs](#llm), benötigen dafür aber erheblich mehr Rechenzeit und Tokens. Sie konfabulieren weiterhin, mit dem Unterschied, dass auch der Denkprozess selbst halluziniert sein kann.

### RLHF
**Reinforcement Learning from Human Feedback**. Eine Methode im [Post-Training](#post-training) von [LLMs](#llm). Menschen bewerten Modellantworten, das Modell lernt aus diesem Feedback. Teil des [Alignment](#alignment)-Prozesses und Mitursache von [Sycophancy](#sycophancy).

---

## S

### Slop
Minderwertiger, formelhafter KI-Text. Erkennbar an Wendungen wie „Delve into", „It is crucial to note" oder „Furthermore", inflationärer Verwendung von Em-Dashes und Buzzwords wie „ever-evolving". Gegenmittel sind kritisches Lesen und klare Anweisungen im Prompt.

### Stochastic Parrot
Eine kritische Charakterisierung von [LLMs](#llm) als Systeme, die sprachliche Muster aus ihren Trainingsdaten rekombinieren, ohne deren Bedeutung zu erfassen.[^parrot] Der Begriff geht auf Bender, Gebru und Kolleginnen zurück und wurde 2021 in einem Aufsatz zur Kritik großer Sprachmodelle eingeführt. Die These lautet, dass LLMs aufgrund ihrer Architektur kein Verstehen leisten, sondern statistische Imitation produzieren. Die Charakterisierung ist umstritten, prägt aber die kritische Debatte um LLM-Fähigkeiten und wird in Diskussionen um Verantwortung und Vertrauen häufig herangezogen.

### Sycophancy
Die Tendenz von [LLMs](#llm), Nutzer:innen zuzustimmen statt zu widersprechen.[^sycophancy] Das Modell priorisiert Zustimmung über Wahrheit, weil es im [Post-Training](#post-training) für nutzerfreundliche Antworten belohnt wurde. Eine als Selbsteinschätzung formulierte Frage erhält häufig genau diese Einschätzung gespiegelt zurück. Gegenmittel sind kritisches Hinterfragen und bewusst widersprüchlich gestellte Kontrollanfragen.

### System Prompt
Vorab-Anweisungen, die das Verhalten eines [LLM](#llm) für die gesamte Konversation steuern. Werden vor der eigentlichen Nutzeranfrage gesetzt und definieren Rolle, Tonfall und Regeln. Für Nutzer:innen meist unsichtbar, beeinflussen aber jede Antwort.

---

## T

### Temperatur
Ein Parameter, der steuert, wie zufällig das Modell aus möglichen Fortsetzungen auswählt. Eine niedrige Temperatur (gegen 0) führt zu deterministischen, gleichbleibenden Antworten. Eine hohe Temperatur (gegen 1 oder höher) erzeugt mehr Variation und Kreativität, aber auch mehr Fehler. Für reproduzierbare Aufgaben wie Klassifikation eignet sich niedrige Temperatur, für kreative Aufgaben wie Texterzeugung höhere.

### Token
Die kleinste Einheit, in die ein [LLM](#llm) Text zerlegt. Ein Token ist oft ein Wort oder ein Wortteil. 100 Tokens entsprechen etwa 75 englischen Wörtern. Relevant für Kosten, [Context Window](#context-window) und Verarbeitungsgeschwindigkeit.

### Tokenizer
Das Werkzeug, das Text in [Tokens](#token) zerlegt. Verschiedene Modelle verwenden verschiedene Tokenizer, deshalb kann dasselbe Wort unterschiedlich viele Tokens kosten.

### Transformer
Die Architektur hinter modernen [LLMs](#llm), 2017 in „Attention Is All You Need" vorgestellt.[^transformer] Der zentrale Mechanismus ist Attention. Das Modell lernt, welche Teile des Eingabetexts füreinander relevant sind. Self-Attention ersetzt rekurrente Strukturen früherer Architekturen und ermöglicht parallele Verarbeitung langer Sequenzen.

---

[^bias]: Gallegos, Isabel O. et al. „Bias and Fairness in Large Language Models. A Survey". *Computational Linguistics* 50.3 (2024), 1097–1179. https://doi.org/10.1162/coli_a_00524

[^cai]: Bai, Yuntao et al. „Constitutional AI. Harmlessness from AI Feedback". arXiv:2212.08073, Dezember 2022. https://arxiv.org/abs/2212.08073

[^injection]: Greshake, Kai et al. „Not what you've signed up for. Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection". *Proceedings of the 16th ACM Workshop on Artificial Intelligence and Security*, 2023. https://doi.org/10.1145/3605764.3623985

[^judge]: Zheng, Lianmin et al. „Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena". *Advances in Neural Information Processing Systems 36 (NeurIPS 2023)*. https://arxiv.org/abs/2306.05685

[^konfabulation]: Smith, Andrew L., Frank Greaves und Trevor Panch. „Hallucination or Confabulation? Neuroanatomy as Metaphor in Large Language Models". *PLOS Digital Health* 2.11 (2023). https://doi.org/10.1371/journal.pdig.0000388

[^parrot]: Bender, Emily M., Timnit Gebru, Angelina McMillan-Major und Shmargaret Shmitchell. „On the Dangers of Stochastic Parrots. Can Language Models Be Too Big?". *Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency (FAccT '21)*, 610–623. https://doi.org/10.1145/3442188.3445922

[^promptotyping]: Pollin, Christopher. „Promptotyping. A Context Engineering Method for Building Research Artifacts with Frontier LLMs". Digital Humanities Craft, Universität Graz, 2026. Lehr- und Begleitmaterial unter https://digitalhumanitiescraft.github.io/ai-coding-literacy

[^rag]: Lewis, Patrick et al. „Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks". *Advances in Neural Information Processing Systems 33 (NeurIPS 2020)*. https://arxiv.org/abs/2005.11401

[^reasoning]: Xu, Fengli et al. „Towards Large Reasoning Models. A Survey of Reinforced Reasoning with Large Language Models". *Patterns* 6.10 (2025), 101370. https://doi.org/10.1016/j.patter.2025.101370

[^sycophancy]: Malmqvist, Lars. „Sycophancy in Large Language Models. Causes and Mitigations". *Intelligent Computing, CompCom 2025*, Springer 2024. arXiv:2411.15287. https://arxiv.org/abs/2411.15287

[^transformer]: Vaswani, Ashish et al. „Attention Is All You Need". *Advances in Neural Information Processing Systems 30 (NeurIPS 2017)*. https://arxiv.org/abs/1706.03762
