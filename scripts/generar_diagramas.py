"""Renderiza los diagramas Mermaid de scripts/diagramas/*.mmd a PNG en docs/img/entregable_final/.

Usa Chrome en modo headless (mermaid se carga desde CDN) y recorta el espacio en blanco con Pillow.
Uso: python scripts/generar_diagramas.py
"""
import html
import subprocess
import tempfile
from pathlib import Path

from PIL import Image, ImageChops

RAIZ = Path(__file__).resolve().parents[1]
FUENTES = RAIZ / "scripts" / "diagramas"
SALIDA = RAIZ / "docs" / "img" / "entregable_final"
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

PLANTILLA = """<!doctype html><html><head><meta charset="utf-8">
<style>body{{margin:20px;background:#fff;font-family:Arial,sans-serif}}</style>
<script src="https://cdn.jsdelivr.net/npm/mermaid@10.9.1/dist/mermaid.min.js"></script>
</head><body><pre class="mermaid">{codigo}</pre>
<script>mermaid.initialize({{startOnLoad:true,theme:"default",
flowchart:{{useMaxWidth:false,htmlLabels:true}},themeVariables:{{fontSize:"16px"}}}});</script>
</body></html>"""


def recortar(ruta: Path, margen: int = 24) -> None:
    img = Image.open(ruta).convert("RGB")
    fondo = Image.new("RGB", img.size, (255, 255, 255))
    caja = ImageChops.difference(img, fondo).getbbox()
    if caja:
        x0, y0, x1, y1 = caja
        img = img.crop((max(x0 - margen, 0), max(y0 - margen, 0),
                        min(x1 + margen, img.width), min(y1 + margen, img.height)))
    img.save(ruta, optimize=True)


def renderizar(fuente: Path) -> Path:
    destino = SALIDA / f"{fuente.stem}.png"
    with tempfile.TemporaryDirectory() as tmp:
        pagina = Path(tmp) / "diagrama.html"
        pagina.write_text(PLANTILLA.format(codigo=html.escape(fuente.read_text(encoding="utf-8"))),
                          encoding="utf-8")
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                        "--force-device-scale-factor=2", "--window-size=3200,3200",
                        "--virtual-time-budget=15000", f"--screenshot={destino}",
                        pagina.as_uri()], check=True, capture_output=True)
    recortar(destino)
    return destino


if __name__ == "__main__":
    SALIDA.mkdir(parents=True, exist_ok=True)
    for fuente in sorted(FUENTES.glob("*.mmd")):
        print(renderizar(fuente).relative_to(RAIZ))
