---
title: "Konferenzabstract: Vorläufige Befunde zu Prompting-Effekten in deutschsprachiger Sozialarbeits-KI"
authors:
  - Christopher Pollin
  - Susanne Sackl-Sharif
  - Sabine Klinger
  - Christian Steiner
year: 2026
project: SocialAI
tags:
  - LLM
  - Bias
  - Soziale-Arbeit
  - FAIR-SW-Bench
  - Abstract
status: complete
---

# Konferenzabstract: Vorläufige Befunde zu Prompting-Effekten in deutschsprachiger Sozialarbeits-KI

> Verkürzte Zusammenfassung der Pilotstudie für Konferenzeinreichungen.
>
> **Vollständiges Paper:** [Pollin et al. (2025): Wenn gute Absichten nach hinten losgehen](/wissen/papers/pollin-et-al-2025-pilotstudie-bias-diversitaetssensible-prompts.md)

---

## Abstract

**Kontext:** Bestehende LLM-Bias-Benchmarks wie BBQ und BOLD fokussieren auf englischsprachige Kontexte. Deutschsprachige Evaluierungsrahmen für Sozialarbeitsanwendungen sind bisher wenig entwickelt, trotz regulatorischer Aufmerksamkeit durch den EU AI Act 2026. Bisherige Forschung zu Debiasing-Strategien zeigt sprachspezifische Variationen in der Wirksamkeit.

**Forschungsfragen:** Diese Pilotstudie untersucht zwei Fragen: Wie reagieren LLMs auf unterschiedliche Prompt-Formulierungen in deutschsprachigen Sozialarbeitskontexten? Können Debiasing-Strategien aus der englischsprachigen Forschung auf deutschsprachige Anwendungen übertragen werden?

**Methode:** Die Studie testete 30 von 50 geplanten Prompts in drei Bedingungen: Base-Prompts mit expliziten demografischen Markern, Neutral-Prompts mit automatisierter Marker-Entfernung und Diversity-aware-Prompts mit Reasoning-Instruktionen und inklusivem Framing. Die Evaluierung verwendete LLM-as-Judge-Methodologie. Technische Einschränkungen begrenzten die Datenerhebung auf einen Anbieter (Anthropic Claude-3.5), da andere getestete Systeme (OpenAI, Mistral) nicht auswertbare Ausgaben produzierten und ein System (Google) alle Anfragen blockierte. Der Studie fehlen menschliche Annotationen und Inter-Rater-Reliabilitätsmessungen, zudem werden englischsprachige Evaluierungs-Prompts für deutschsprachige Outputs verwendet. Die Datenerhebung blieb unvollständig, und systematische Verzerrungen im Judge-Modell können nicht ausgeschlossen werden.

**Beobachtungen:** Diversity-aware-Prompts erhielten höhere Bias-Scores als Base- und Neutral-Bedingungen über mehrere Dimensionen hinweg, einschließlich Agency Attribution und Problem Framing. Neutral-Prompts erhielten niedrigere Scores als andere Bedingungen. Mehrere Erklärungen sind zu berücksichtigen: systematische Evaluierungsverzerrungen im Judge-Modell, Salienz-Effekte durch explizite Diversitätsreferenzen, Überkorrektur-Phänomene, sprachspezifische Aktivierungsmuster oder Stichprobenverzerrungen durch unvollständige Datenerhebung.

**Diskussion:** Die beobachteten Muster erfordern Validierung, bevor Implikationen für die Praxis abgeleitet werden können. Sollten sich die Muster unter kontrollierten Bedingungen mit menschlicher Validierung replizieren, würden sie auf Grenzen bei der Übertragung von Debiasing-Ansätzen zwischen Sprachen ohne empirische Überprüfung hinweisen. Die geplante Vollstudie adressiert gegenwärtige methodische Einschränkungen durch vollständige Prompt-Implementierung, Expert:innen-Annotation mit Krippendorff's Alpha ≥0.7, Multi-Provider-Validierung und Power-Analyse für Stichprobengrößen von 100-400 pro Bedingung. Das Benchmark-Repository steht für Community-Validierung zur Verfügung.

**Ethische Überlegungen:** Das Studienprotokoll behandelt sensible Szenarien einschließlich Suizidalität und Gewalt ohne Publikation adversarialer Prompts. Praxispartner sind SOS-Kinderdorf und Jugend am Werk.
