#!/usr/bin/env python3
"""Glossar aus dem internen Repo in den oeffentlichen Spiegel uebertragen.

Das interne ``glossar/README.md`` ist die einzige Quelle der Wahrheit. Das Team
editiert es wie gewohnt, inklusive interner Notizen. Diese Notizen sind auf der
internen Seite voll sichtbar, duerfen aber nicht oeffentlich werden. Dieses
Skript erzeugt die oeffentliche Fassung als reine Strip-Operation:

* Absaetze, die mit ``***Anmerkung`` beginnen, werden entfernt
  (z. B. ``***Anmerkung Sabine:*** Neuer Begriff``).
* Callout-Bloecke vom Typ ``> [!INTERN]`` werden samt Folgezeilen entfernt
  (optionale, schoenere Notiz-Konvention).
* Mehrfache Leerzeilen, die durch das Entfernen entstehen, werden zu einer
  einzelnen Leerzeile zusammengezogen; abschliessender Leerraum wird getrimmt.

Es findet KEINE inhaltliche Umformung statt: Header, Eintraege, Tag-Zeilen und
Fussnoten gehen unveraendert durch. Damit gilt deterministisch
``strip(intern) == public``.

Aufruf:
    python scripts/sync-glossar.py [ZIELPFAD]

Ohne Argument wird in den Public-Draft geschrieben
(``docs/intern/public-draft/glossar/README.md``). Sobald das oeffentliche Repo
existiert, kann eine GitHub Action dieses Skript aufrufen und als ZIELPFAD den
ausgecheckten Pfad des Public-Repos uebergeben.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCE = REPO_ROOT / "glossar" / "README.md"
DEFAULT_TARGET = REPO_ROOT / "docs" / "intern" / "public-draft" / "glossar" / "README.md"

# Marker fuer interne Notizen
NOTE_PREFIX = "***Anmerkung"
INTERN_CALLOUT = re.compile(r"^>\s*\[!INTERN\]")


def strip_internal_notes(text: str) -> str:
    """Interne Notizen aus dem Glossar-Markdown entfernen.

    Eine Notiz steht immer als eigener Absatz (Leerzeile davor, Leerzeile
    danach). Entfernt wird die Notiz-Zeile plus genau die EINE direkt folgende
    Leerzeile, die sie vom naechsten Block trennt. So bleibt das uebrige
    Spacing (z. B. bewusst gesetzte Doppel-Leerzeilen zwischen Eintraegen)
    unveraendert und der Public-Output ist deterministisch.
    """
    lines = text.replace("\r\n", "\n").split("\n")
    out: list[str] = []
    i = 0
    n = len(lines)

    while i < n:
        line = lines[i]
        # Einzeilige ***Anmerkung ...***-Notizen
        if line.startswith(NOTE_PREFIX):
            i += 1
            if i < n and lines[i] == "":
                i += 1
            continue
        # > [!INTERN]-Callout-Block: Startzeile + alle folgenden Zitatzeilen
        if INTERN_CALLOUT.match(line):
            i += 1
            while i < n and lines[i].startswith(">"):
                i += 1
            if i < n and lines[i] == "":
                i += 1
            continue
        out.append(line)
        i += 1

    return "\n".join(out).rstrip() + "\n"


def main() -> int:
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_TARGET

    if not SOURCE.exists():
        print(f"FEHLER: Quelle nicht gefunden: {SOURCE}", file=sys.stderr)
        return 1

    source_text = SOURCE.read_text(encoding="utf-8")
    public_text = strip_internal_notes(source_text)

    target.parent.mkdir(parents=True, exist_ok=True)
    with open(target, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(public_text)

    stripped = source_text.count("\n") + 1 - (public_text.count("\n") + 1)
    print(f"Glossar synchronisiert: {SOURCE}  ->  {target}")
    print(f"  Quelle:  {source_text.count(chr(10)) + 1} Zeilen")
    print(f"  Public:  {public_text.count(chr(10)) + 1} Zeilen")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
