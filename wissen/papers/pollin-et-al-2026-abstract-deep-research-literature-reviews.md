---
title: "Deep-Research-gestützte Literature Reviews im Praxistest. Epistemische Asymmetrien und Qualitätssicherung zwischen Large Language Models und Expert:innenwissen"
authors:
  - Christopher Pollin
  - Susanne Sackl-Sharif
  - Sabine Klinger
  - Christian Steiner
year: 2026
project: SocialAI
tags:
  - Literature-Review
  - Deep-Research
  - Co-Intelligence
  - PRISMA
  - Methodik
status: draft
affiliations:
  - Digital Humanities Craft
  - Universität Graz
context: Elisabeth-List-Fellowship-Projekt (Universität Graz, 2025-2026)
---

# Deep-Research-gestützte Literature Reviews im Praxistest

**Epistemische Asymmetrien und Qualitätssicherung zwischen Large Language Models und Expert:innenwissen**

**Christopher Pollin, Susanne Sackl-Sharif, Sabine Klinger, Christian Steiner**

**Repository:** [FemPrompt_SozArb](https://github.com/chpollin/FemPrompt_SozArb)

---

## Abstract

Der zunehmende Einsatz von Künstlicher Intelligenz (KI), insbesondere von Large Language Models (LLMs), in der Wissenschaft greift tief in die akademische Wissensproduktion ein. KI verändert dabei nicht nur die methodischen Werkzeuge und Forschungspraktiken, sondern auch deren epistemische Grundlagen (Hauswald, 2025). Diese doppelte Transformation zeigt sich besonders deutlich bei systematischen Literature Reviews, bei denen KI auf unterschiedlichen Ebenen als Werkzeug eingesetzt werden kann und gleichzeitig die Evidenzbasis für ganze Forschungsfelder konstituiert (Bolaños et al., 2024). Damit wird KI in der Wissenschaft zunehmend zu einer epistemischen Infrastruktur, die Bewertungsmaßstäbe, Sichtbarkeiten und Legitimationslogiken wissenschaftlichen Wissens strukturiert. Der Einsatz von KI wirft dabei nicht nur technische, sondern auch politische und institutionelle Verantwortungsfragen auf.

Vor diesem Hintergrund untersuchen wir im Rahmen des laufenden Elisabeth-List-Fellowship-Projekts "Diversitätssensibler Umgang mit Künstlicher Intelligenz. Digital / AI Literacies und feministisches Prompting in der Sozialen Arbeit" (Universität Graz, 2025-2026), wie sich Deep Research bei systematischen Literature Reviews in der Praxis bewährt. Unser Literature Review knüpft inhaltlich an dieses Projekt an und fokussiert auf das Thema "Feministische AI Literacies im Feld der Sozialen Arbeit". Unter feministischen AI Literacies verstehen wir diversitätssensible, intersektionale und Bias-erkennende Fähigkeiten und Fertigkeiten, die Fachkräfte der Sozialen Arbeit im Umgang mit generativer KI benötigen (aktuelle Arbeitsdefinition).

Im Zentrum dieses Beitrags steht die Frage, wie und in welchen Phasen sich die Stärken von LLM-gestützten Recherchen und -Bewertungen mit menschlichem Expert:innenwissen verbinden lassen und wo hierbei die Grenzen liegen. Diese Form der Zusammenarbeit entspricht dem Konzept der Co-Intelligence nach Ethan Mollick (2024), bei der Menschen und KI-Systeme komplementäre Stärken einbringen, wobei menschliche Expertise für Kontextualisierung, Qualitätsurteil und Verantwortungsübernahme unverzichtbar bleibt. Wesentlich ist hierbei somit die Frage, wer in diesem Prozess die Verantwortung für Auswahl, Ausschluss und Gewichtung von Evidenz trägt und wie diese Entscheidungen nachvollziehbar und überprüfbar bleiben. Die Bewertung erfolgt hierbei sowohl von der KI als auch von den Expert:innen auf den PRISMA-Richtlinien, die für eine systematische Analyse von Literatur und Metadaten entwickelt wurden (PRISMA, 2020).

## Workflow

Der Workflow gliedert sich in drei Phasen:

### Phase 1: Identifikation und Import

Die erste Phase umfasst die Identifikation und den Import von Literatur, wobei vier Deep-Research-Modelle (Gemini, Claude, ChatGPT und Perplexity) zum Einsatz kommen. Deep Research bezeichnet die Fähigkeit von LLMs, eigenständig Datenbanken zu durchsuchen, Quellen zu triangulieren und bibliographische Metadaten zu extrahieren. Diese Modelle erhalten identische parametrische Prompts, also strukturierte Anweisungen für unsere Forschungsfragen, den Untersuchungszeitraum und das Ausgabeformat. Ein LLM konvertiert die heterogenen Outputs in standardisiertes RIS-Format für den Import in die Literaturverwaltungssoftware Zotero.

### Phase 2: Bewertung (Kernphase)

Die zweite Phase ist die wichtigste Phase unseres Praxistests und betrifft die Bewertung der Literatursuche und der Literatur selbst. Im automatisierten Pfad übernimmt ein LLM-basiertes PRISMA-Assessment die Bewertung mit 5-dimensionalen Relevanz-Scores, während im manuellen Pfad wissenschaftliche Expert:innen aus den Bereichen der Sozialarbeitsforschung, Gender und Diversitätsforschung sowie Technikforschung das Screening, die Qualitäts- und Relevanzbewertung nach denselben Kriterien durchführen. Der methodische Vergleich zwischen automatisiertem und manuellem Pfad dient darauf aufbauend der kritischen Validierung proprietärer Werkzeuge, die bei unserem Literature Review zum Einsatz kommen. Für die Wissenschaft entsteht hier ein Spannungsfeld zwischen praktischer Nutzbarkeit fortgeschrittener KI-Funktionen und der Abhängigkeit von intransparenten kommerziellen Systemen, deren Trainingsdaten, Modellarchitekturen und Entscheidungslogiken nicht offengelegt werden und somit der wissenschaftlichen Kontrolle weitgehend entzogen sind.

### Phase 3: Synthese

In der dritten Phase werden die Ergebnisse synthetisiert. In einem ersten Schritt werden alle relevanten Volltexte beschafft und in ein maschinenlesbares Format konvertiert. In einem zweiten Schritt generiert ein LLM anschließend strukturierte Zusammenfassungen in mehreren analytischen Durchgängen, in denen Expert:innen die Zusammenfassungen kontrollieren und anpassen. Die Ergebnisse fließen abschließend in eine vernetzte Wissensrepräsentation ein, die Konzepte, Schlagworte und thematische Verbindungen zwischen den Texten abbildet. Bei diesem Schritt wird die Software Obsidian verwendet.

---

## Literatur

- Bolaños, F., Salatino, A., Osborne, F. & Motta, E. (2024). Artificial intelligence for Literature Reviews: Opportunities and Challenges. *Artif Intell Rev 57*. https://doi.org/10.1007/s10462-024-10902-3
- Hauswald, R. (2025). Artificial Epistemic Authorities. *Social Epistemology, 39*(6), 716-725. https://doi.org/10.1080/02691728.2025.2449602
- Mollick, E. (2024). *Co-Intelligence: Living and Working with AI*. Portfolio.
- PRISMA (2020). PRISMA 2020. https://www.prisma-statement.org/prisma-2020
