"""Genera el PDF de la entrega unificada a partir de docs/entrega_unificada.md.

Uso (desde la raíz del repositorio):
    python scripts/generar_pdf.py

Requiere el paquete `markdown` (pip install markdown) y Google Chrome o Microsoft Edge instalados.
"""

import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

import markdown

RAIZ = pathlib.Path(__file__).resolve().parent.parent
ORIGEN = RAIZ / "docs" / "entrega_unificada.md"
DESTINO = RAIZ / "docs" / "Entrega_Unificada_IHC_Grupo5.pdf"

NAVEGADORES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    "google-chrome",
    "chromium",
    "msedge",
]

CSS = """
@page { size: letter; margin: 2.2cm 2.2cm 2.2cm 2.5cm; }
body { font-family: 'Segoe UI', Arial, sans-serif; font-size: 10.5pt; line-height: 1.45; color: #1a1a1a; }
h1 { font-size: 20pt; color: #5b2a86; border-bottom: 2px solid #CC00FF; padding-bottom: 4px; page-break-before: always; }
h1:first-of-type { page-break-before: avoid; }
h2 { font-size: 15pt; color: #3d1d5c; margin-top: 1.4em; }
h3 { font-size: 12.5pt; } h4 { font-size: 11pt; }
center h1, center h2, center h3 { border: none; page-break-before: avoid; }
blockquote { margin: 0.6em 0; padding: 0.2em 0.9em; border-left: 3px solid #d9c2ec; color: #222; }
table { border-collapse: collapse; width: 100%; margin: 0.8em 0; font-size: 9pt; }
tr { page-break-inside: avoid; }
th, td { border: 1px solid #c9c0d3; padding: 4px 6px; vertical-align: top; }
th { background: #efe7f7; }
img { max-width: 100%; display: block; margin: 0.5em auto; page-break-inside: avoid; }
td img { max-width: 160px; }
code { font-size: 9pt; background: #f3f0f6; padding: 0 3px; }
hr { border: none; border-top: 1px solid #ccc; }
a { color: #5b2a86; }
.footnote { font-size: 9pt; }
"""


def buscar_navegador():
    for candidato in NAVEGADORES:
        ruta = shutil.which(candidato) or (candidato if pathlib.Path(candidato).exists() else None)
        if ruta:
            return ruta
    sys.exit("No se encontró Chrome ni Edge. Instale uno de los dos o ajuste la lista NAVEGADORES.")


def markdown_a_html(texto):
    texto = re.sub(r"^---\n.*?\n---\n", "", texto, count=1, flags=re.S)  # front matter de Pandoc
    texto = re.sub(r"<!--.*?-->", "", texto, flags=re.S)
    cuerpo = markdown.markdown(
        texto, extensions=["tables", "footnotes", "attr_list", "md_in_html", "sane_lists"]
    )
    base = ORIGEN.parent.as_uri() + "/"  # para que las rutas img/... se resuelvan desde docs/
    return (
        f'<!doctype html><html lang="es"><head><meta charset="utf-8"><base href="{base}">'
        f"<title>Entrega unificada IHC Grupo 5</title><style>{CSS}</style></head>"
        f"<body>{cuerpo}</body></html>"
    )


def main():
    html = markdown_a_html(ORIGEN.read_text(encoding="utf-8"))
    with tempfile.TemporaryDirectory() as tmp:
        archivo_html = pathlib.Path(tmp) / "entrega_unificada.html"
        archivo_html.write_text(html, encoding="utf-8")
        subprocess.run(
            [
                buscar_navegador(),
                "--headless=new",
                "--disable-gpu",
                "--no-pdf-header-footer",
                "--allow-file-access-from-files",
                f"--print-to-pdf={DESTINO}",
                archivo_html.as_uri(),
            ],
            check=True,
            capture_output=True,
        )
    print(f"PDF generado: {DESTINO}")


if __name__ == "__main__":
    main()
