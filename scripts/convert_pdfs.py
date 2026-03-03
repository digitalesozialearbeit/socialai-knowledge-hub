"""
PDF -> Markdown Konvertierung mit Bildextraktion via docling.

Konvertiert PDFs aus dem Projektverzeichnis nach docs/sources/.
Bilder werden als PNG in docs/sources/img/ gespeichert und im
Markdown korrekt referenziert.

Nutzung:
    python scripts/convert_pdfs.py                    # Alle PDFs
    python scripts/convert_pdfs.py "MeinPDF.pdf"      # Einzelnes PDF
"""

import sys
import io
import re

# Windows: stdout auf UTF-8 setzen
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

from pathlib import Path

from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling_core.types.doc.document import DocItemLabel, ImageRef, PictureItem
from docling_core.types.doc.base import ImageRefMode


# --- Pfade ---
PROJECT_ROOT = Path(__file__).resolve().parent.parent
SOURCES_DIR = PROJECT_ROOT / "docs" / "sources"
PDF_DIR = SOURCES_DIR / "pdf"
IMG_DIR = SOURCES_DIR / "img"


def slugify(name: str) -> str:
    """Dateiname-freundlichen Slug erzeugen."""
    return (
        name.lower()
        .replace(" ", "-")
        .replace("(", "")
        .replace(")", "")
        .replace("ä", "ae")
        .replace("ö", "oe")
        .replace("ü", "ue")
        .replace("ß", "ss")
    )


def convert_pdf(pdf_path: Path) -> Path:
    """
    Einzelnes PDF konvertieren.

    1. Docling mit generate_picture_images=True aufrufen
    2. Bilder extrahieren und in img/ speichern
    3. URI auf PictureItems setzen (relativ zu sources/)
    4. Markdown mit ImageRefMode.REFERENCED exportieren
    """
    slug = slugify(pdf_path.stem)
    print(f"\n{'='*60}")
    print(f"Konvertiere: {pdf_path.name} → {slug}.md")
    print(f"{'='*60}")

    # Pipeline mit Bildextraktion
    pipeline_options = PdfPipelineOptions()
    pipeline_options.generate_picture_images = True
    pipeline_options.generate_table_images = True

    converter = DocumentConverter(
        format_options={
            InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
        }
    )

    result = converter.convert(str(pdf_path))

    # Bilder extrahieren und URIs setzen
    IMG_DIR.mkdir(parents=True, exist_ok=True)
    img_count = 0

    for item, _level in result.document.iterate_items():
        if not isinstance(item, PictureItem):
            continue
        if item.image is None:
            continue

        # PIL-Bild holen (direkt vom item oder via get_image)
        pil_img = None
        if hasattr(item.image, '_pil') and item.image._pil is not None:
            pil_img = item.image._pil
        else:
            pil_img = item.get_image(doc=result.document)

        if pil_img is None:
            print(f"  ⚠ Bild {img_count} hat kein PIL-Image, überspringe")
            continue

        # Speichern
        img_filename = f"{slug}_{img_count}.png"
        img_path = IMG_DIR / img_filename
        pil_img.save(str(img_path))

        # URI setzen: relativ zum Markdown-File (das in sources/ liegt)
        # Markdown liegt in docs/sources/slug.md, Bilder in docs/sources/img/
        relative_path = Path("img") / img_filename
        item.image = ImageRef(
            mimetype="image/png",
            dpi=item.image.dpi,
            size=item.image.size,
            uri=relative_path,
        )

        img_count += 1

    print(f"  → {img_count} Bilder extrahiert nach docs/sources/img/")

    # Markdown exportieren
    md_content = result.document.export_to_markdown(
        image_mode=ImageRefMode.REFERENCED,
    )

    # Windows: Backslashes in Bildpfaden zu Forward-Slashes korrigieren
    md_content = re.sub(
        r"!\[Image\]\(img\\",
        "![Image](img/",
        md_content,
    )

    # Bildreferenzen zaehlen
    ref_count = md_content.count("![Image]")
    print(f"  → {ref_count} Bildreferenzen im Markdown")

    # Speichern
    md_path = SOURCES_DIR / f"{slug}.md"
    md_path.write_text(md_content, encoding="utf-8")
    print(f"  → Gespeichert: {md_path.relative_to(PROJECT_ROOT)}")

    # Statistik
    char_count = len(md_content)
    line_count = md_content.count("\n")
    print(f"  → {char_count:,} Zeichen, {line_count:,} Zeilen")

    return md_path


def main():
    """Alle PDFs oder ein einzelnes konvertieren."""
    SOURCES_DIR.mkdir(parents=True, exist_ok=True)

    if len(sys.argv) > 1:
        # Einzelnes PDF (sucht in pdf/ und root)
        pdf_name = sys.argv[1]
        pdf_path = PDF_DIR / pdf_name
        if not pdf_path.exists():
            pdf_path = PROJECT_ROOT / pdf_name
        if not pdf_path.exists():
            print(f"Fehler: {pdf_name} nicht gefunden")
            sys.exit(1)
        convert_pdf(pdf_path)
    else:
        # Alle PDFs in docs/sources/pdf/
        pdfs = sorted(PDF_DIR.glob("*.pdf"))
        if not pdfs:
            print("Keine PDFs im Projektverzeichnis gefunden.")
            sys.exit(0)

        print(f"Gefunden: {len(pdfs)} PDFs")
        for pdf in pdfs:
            print(f"  - {pdf.name}")

        results = []
        for pdf in pdfs:
            try:
                md_path = convert_pdf(pdf)
                results.append((pdf.name, md_path, True))
            except Exception as e:
                print(f"  ✗ Fehler bei {pdf.name}: {e}")
                results.append((pdf.name, None, False))

        # Zusammenfassung
        print(f"\n{'='*60}")
        print("Zusammenfassung")
        print(f"{'='*60}")
        for name, md_path, success in results:
            status = "✓" if success else "✗"
            target = md_path.name if md_path else "—"
            print(f"  {status} {name} → {target}")


if __name__ == "__main__":
    main()
