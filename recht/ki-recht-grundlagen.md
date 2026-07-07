# KI und Recht: Grundlagen für die Soziale Arbeit

> [!NOTE]
> Diese Seite fasst die rechtlichen Kernthemen des zweiten Innovationsworkshops (30.06.2026, geleitet von Dr. Heidi Scheichenbauer und Dr. Madeleine Müller, [Research Institute](https://researchinstitute.at)) in eigenen Worten zusammen. Die öffentliche Nachlese zum Workshop liegt im Repo [SocialAI Workshops](https://digitalesozialearbeit.github.io/socialai-workshops/#/workshops/innovationsworkshop-2026-06-30). Diese Seite ersetzt keine Rechtsberatung: Im Zweifel entscheidet die datenschutzverantwortliche Person der eigenen Organisation.

## Zwei Regelwerke, die einander ergänzen

Beim KI-Einsatz in der Sozialen Arbeit greifen zwei EU-Verordnungen ineinander. Die [DSGVO](/glossar/README.md#datenschutz--dsgvo) schützt Menschen bei der Verarbeitung ihrer personenbezogenen Daten, egal ob KI im Spiel ist oder nicht. Der [AI Act (KI-VO)](/glossar/README.md#ai-act--ki-verordnung) reguliert KI-Systeme nach ihrem Risikopotenzial, egal ob personenbezogene Daten verarbeitet werden. Viele KI-Anwendungen in der Praxis fallen unter beide Regelwerke gleichzeitig: Wer etwa Falldaten in ein KI-Tool eingibt, muss DSGVO und KI-VO zusammen denken.

Die KI-VO (Verordnung (EU) 2024/1689) ist seit August 2024 in Kraft; die Anwendungsfristen sind gestaffelt und wurden durch das Omnibus-Paket teils bis 2027/2028 verschoben.

## Rollen: Wer trägt welche Pflichten?

Vor jedem KI-Einsatz steht die Frage, welche rechtliche Rolle die eigene Organisation einnimmt, denn daran hängen die konkreten Pflichten.

**Nach DSGVO:**

- **Verantwortlicher** (Art 4 Nr 7) ist in der Regel der Träger selbst: Er entscheidet über Zwecke und Mittel der Datenverarbeitung. Daran hängen Rechenschaftspflicht, Betroffenenrechte, Verarbeitungsverzeichnis, Meldepflichten und Datensicherheitsmaßnahmen.
- **Auftragsverarbeiter** (Art 4 Nr 8, Art 28) ist der KI-Anbieter, wenn er personenbezogene Daten im Auftrag verarbeitet. Dann braucht es eine Auftragsverarbeitervereinbarung.
- **Mitarbeitende** sind datenschutzrechtlich Teil der Verarbeitungsstruktur des Trägers, solange sie im Rahmen ihrer beruflichen Aufgaben handeln. Wer personenbezogene Daten eigenmächtig verarbeitet (etwa in einem privaten KI-Konto), kann selbst zur verantwortlichen Person werden.

**Nach KI-VO:**

- **Anbieter** (Art 3 Z 3) entwickelt ein KI-System oder lässt es entwickeln und bringt es unter eigenem Namen in Verkehr.
- **Betreiber** (Art 3 Z 4) verwendet ein KI-System in eigener Verantwortung zu beruflichen Zwecken. Das ist die typische Rolle von Organisationen der Sozialen Arbeit.
- Achtung **Rollenwechsel**: Wer ein KI-System wesentlich verändert oder unter eigenem Namen einsetzt, kann über die Anbieterfiktion (Art 25 KI-VO) selbst zum Anbieter mit strengeren Pflichten werden. Das betrifft etwa organisationseigene Chatbots auf Basis fremder Modelle.

Die Rolleneinstufung sollte dokumentiert und bei jedem neuen Anwendungsfall neu geprüft werden. Einen Überblick über die Pflichten je Rolle und Risikoklasse bietet die [KI-Servicestelle der RTR](https://ki.rtr.at).

## Die Risikopyramide der KI-VO

Die KI-VO stuft KI-Systeme nach Risiko ab:

| Stufe | Was fällt darunter | Folge |
|---|---|---|
| Verbotene Praktiken (Art 5) | u. a. Systeme, die Vulnerabilität ausnutzen (Alter, Behinderung, soziale Situation), Social Scoring, Emotionserkennung am Arbeitsplatz | Einsatz untersagt |
| Hochrisiko (Art 6, Anhang III) | u. a. KI zur Beurteilung von Ansprüchen auf grundlegende öffentliche Unterstützungsleistungen | umfangreiche Pflichten für Anbieter und Betreiber |
| Begrenztes Risiko (Art 50) | Chatbots, Deepfakes, KI-generierte Inhalte | Transparenz- und Kennzeichnungspflichten |
| Minimales Risiko | alles Übrige, z. B. übliche Assistenz-Tools | kaum Pflichten, aber: KI-Kompetenz (Art 4) gilt immer |

Für die Soziale Arbeit ist die Hochrisiko-Einstufung teils noch offen: Die Kommissionsleitlinien zu Hochrisiko-KI nennen „Social Services" ausdrücklich (Rz 288, 293, etwa Priorisierung von Betreuungsleistungen oder Chatbots zur Antragsbewertung), die finalen Leitlinien stehen aber noch aus. Wer solche Einsätze plant, sollte die Hochrisiko-Frage von Beginn an mitdenken.

## KI-Kompetenz (Art 4 KI-VO): die Pflicht, die alle trifft

Unabhängig von der Risikoklasse müssen Anbieter und Betreiber sicherstellen, dass ihr Personal über ein ausreichendes Maß an [KI-Kompetenz](/glossar/README.md#ai-literacies--ki-kompetenzen) verfügt (Art 4; Definition in Art 3 Z 56). Gemeint sind Fähigkeiten und Verständnis, um KI-Systeme sachkundig einzusetzen und sich ihrer Chancen und Risiken bewusst zu sein. Kompetenzaufbau ist dabei als laufende, zielgruppenorientierte Aufgabe angelegt, kein einmaliges Training: Fachkräfte brauchen anderes Wissen als Führungskräfte oder IT-Personal. Als Umsetzung empfehlen sich interne KI-Richtlinien und eine benannte zuständige Stelle (KI-Beauftragte:r); Orientierung bieten die Best-Practice-Beispiele im [Living Repository der EU](https://digital-strategy.ec.europa.eu/en/policies/ai-literacy).

## Was darf ich eingeben? Datenschutz in der Praxis

Eingaben in kommerzielle KI-Tools verlassen den eigenen Rechner. Daraus folgen die praktischen Kernregeln:

1. **Fallbezogene, personenidentifizierbare Daten gehören nicht in frei zugängliche KI-Tools.** Das gilt verschärft für sensible Daten nach Art 9 DSGVO (Gesundheit, Herkunft, sexuelle Orientierung u. a.) und strafrechtsbezogene Daten, mit denen die Soziale Arbeit laufend zu tun hat.
2. **Datenweg klären:** Bei jedem Tool ist zu prüfen, wo die Eingaben landen (Organisation, Anbieter, Drittland). Bei US-Anbietern ist zu prüfen, ob die Drittlandsübermittlung gerechtfertigt ist (etwa über das Data Privacy Framework).
3. **Vertragsbasis schaffen:** Zulässiger Einsatz mit Klient:innendaten setzt eine Auftragsverarbeitervereinbarung (Art 28 DSGVO) voraus und den Ausschluss, dass Eingaben für das KI-Training verwendet werden. Solche Vereinbarungen gibt es meist nur bei kostenpflichtigen Diensten; kostenlose Consumer-Tools sind mit echten Klient:innendaten regelmäßig nicht datenschutzkonform nutzbar.
4. **Bei erhöhtem Schutzbedarf** lokal betriebene Modelle prüfen, bei denen Daten die eigene Infrastruktur nicht verlassen.

> [!TIP]
> Ein intern gepflegter, geprüfter Tool-Katalog übersetzt diese Prüfschritte in eine Entscheidungshilfe für den Alltag: Pro Werkzeug wird dokumentiert, wo Daten verarbeitet werden, ob eine Auftragsverarbeitervereinbarung besteht, ob Training mit Eingabedaten ausgeschlossen ist und für welche Datenkategorien es freigegeben ist. Das verhindert auch „Schatten-KI", also die unkontrollierte Nutzung privater Tools.

## Folgenabschätzungen vor der Einführung

Vor der Einführung eines KI-Systems ist zu prüfen, ob eine Folgenabschätzung nötig ist:

- Die **Datenschutz-Folgenabschätzung** (Art 35 DSGVO) ist bei voraussichtlich hohem Risiko verpflichtend. Die österreichische DSFA-Verordnung nennt den Einsatz künstlicher Intelligenz ausdrücklich als auslösendes Kriterium (§ 2 Abs 2 Z 4); die DSGVO hebt die Schutzbedürftigkeit von Kindern hervor (ErwGr 75).
- Die **Grundrechte-Folgenabschätzung** (Art 27 KI-VO) trifft bei der ersten Verwendung eigenständiger Hochrisiko-KI-Systeme unter anderem private Einrichtungen, die öffentliche Dienste erbringen. Das kann Träger der Sozialen Arbeit einschließen.

Beide Instrumente lassen sich kombinieren und sind laufend zu aktualisieren. Als Vorbilder für die praktische Umsetzung dienen der ELI-Report und das kanadische Algorithmic Impact Assessment; das AI Office arbeitet an einem Muster-Fragebogen.

## Automatisierte Einzelentscheidungen (Art 22 DSGVO)

Niemand darf einer rein automatisierten Entscheidung unterworfen werden, die rechtliche Folgen hat oder erheblich beeinträchtigt, etwa beim Zugang zu Leistungen. Der EuGH hat im SCHUFA-Urteil (C-634/21, 2023) klargestellt: Art 22 greift auch dann, wenn ein automatisiert erstellter Score die nachgelagerte menschliche Entscheidung maßgeblich bestimmt. Für die Soziale Arbeit heißt das: Wo KI-gestützte Risiko- oder Gefährdungseinschätzungen faktisch durchgewunken werden, liegt rechtlich unter Umständen bereits eine automatisierte Einzelentscheidung vor. Die Fachkraft muss eigenständig prüfen, nicht nur abnicken.

## Urheberrecht in Kürze

- **Urheber:in kann nur ein Mensch sein** (§ 10 UrhG). Reine Maschinenschöpfungen sind nicht urheberrechtlich geschützt; KI-Outputs sind es daher möglicherweise nicht.
- **Prompts** können geschützt sein, wenn sie die Werkhöhe erreichen: Funktionale Anweisungen eher nicht, kreativ gestaltete Prompts im Einzelfall schon.
- **KI-Training** mit geschützten Werken kann über die Text-und-Data-Mining-Ausnahme (§ 42h UrhG) zulässig sein, sofern der Zugang rechtmäßig ist und kein maschinenlesbarer Nutzungsvorbehalt entgegensteht.
- **Stil ist nicht geschützt, Wiedererkennbarkeit schon:** Reproduziert ein Output erkennbare Elemente eines bestehenden Werks, drohen Ansprüche wegen Urheberrechtsverletzung. Der EuGH hat 2026 zur Pastiche-Ausnahme beim Sampling konkretisiert (C-590/23), dass schon kurze, wiedererkennbare Übernahmen verletzen können.

## Haftung: Wer haftet, wenn etwas schiefgeht?

- Die **neue Produkthaftungsrichtlinie** (RL (EU) 2024/2853) erfasst Software und damit KI eindeutig als Produkt, auch als Software-as-a-Service. Ein Hinweis „KI-generiert" schließt die Haftung nicht aus.
- Auf Betreiberseite kommen **vertragliche und deliktische Haftung** in Betracht (§§ 1295, 1313a ABGB); ein Chatbot im Beratungskontext kann als Erfüllungsgehilfe des Trägers gelten. Fachkräfte, die KI einsetzen, könnten am Sachverständigenmaßstab (§ 1299 ABGB) gemessen werden.
- Die KI-VO droht bei Verstößen Sanktionen bis 35 Mio. Euro oder 7 % des weltweiten Jahresumsatzes an (Art 99).
- Ein Warnbeispiel aus Österreich: Der OGH wies 2025 eine offenbar KI-erstellte Nichtigkeitsbeschwerde zurück, die erfundene Entscheidungen zitierte (OGH 7.10.2025, 14 Os 95/25i). Die ungeprüfte Übernahme von KI-Output verletzte die anwaltliche Sorgfaltspflicht; die Kosten trug der Mandant.

## Automation Bias: Die Prüfpflicht bleibt beim Menschen

[Sprachmodelle halluzinieren](/glossar/README.md#halluzination): Sie erzeugen plausibel klingende, aber erfundene Inhalte, weil sie auf sprachliche Kohärenz optimieren, nicht auf Wahrheit. Der [Automation Bias](/glossar/README.md#automation-bias-automatisierungsverzerrung), also das übermäßige Vertrauen in maschinelle Ausgaben, ist in der KI-VO mehrfach adressiert: über die KI-Kompetenzpflicht (Art 4), die menschliche Aufsicht einschließlich der Wachsamkeit gegenüber Übervertrauen (Art 14), die Anforderungen an Genauigkeit (Art 15) und die Kennzeichnungspflichten (Art 50).

Praktisch heißt das: Für jeden Arbeitsschritt mit KI-Einsatz sollte festgelegt sein, **wer den Output prüft, freigibt und dokumentiert**. Das Projekt fasst dieses Prinzip als *Critical Expert in the Loop*: Eine qualifizierte Fachkraft mit Domänenwissen prüft, ob das Modell Annahmen hinterfragt oder nur bestätigt hat, ob Angaben unabhängig verifizierbar sind und ob die Fragestellung Raum für Widerspruch ließ.

## Weiterführend

- [KI-Servicestelle der RTR](https://ki.rtr.at): Pflichtenüberblick für Anbieter und Betreiber (CC BY 4.0)
- [Nachlese Workshop Tag 2](https://digitalesozialearbeit.github.io/socialai-workshops/#/workshops/innovationsworkshop-2026-06-30) im öffentlichen Workshop-Repo
- [Anwendungsfelder generativer KI](/wissen/anwendungsfelder.md) im Wissensbereich dieses Hubs
- Glossar: [AI Act / KI-Verordnung](/glossar/README.md#ai-act--ki-verordnung) · [Datenschutz / DSGVO](/glossar/README.md#datenschutz--dsgvo) · [Automation Bias](/glossar/README.md#automation-bias-automatisierungsverzerrung) · [Chatbot](/glossar/README.md#chatbot)
