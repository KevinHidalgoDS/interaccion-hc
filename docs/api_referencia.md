<link
  rel="stylesheet"
  href="https://cdn.jsdelivr.net/gh/dracula/markdown-css/dracula-markdown.css"
/>

# Referencia de la API

Esta sección contiene la documentación automática de las funciones de ingeniería de características.

::: src.features.clean_transactions

# Welcome to MkDocs

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.

```bash
npx prettier --write docs/02_empatia.md
pandoc entregable.md --citeproc -o entregable.pdf
```
en caso de que no funcione lo anterior
```bash
# 1. Generar el archivo fuente de LaTeX (.tex) con Pandoc
pandoc docs/02_empatia.md --citeproc -s -o docs/02_empatia.tex

# 2. Corregir el error antiguo de LaTeX3 (el que solucionamos en el paso anterior)
(Get-Content docs/02_empatia.tex) -replace '\.initial:e', '.initial:n' | Set-Content docs/02_empatia.tex
# Ejecuta este comando en tu PowerShell. Esto modificará la configuración interna de MiKTeX para habilitar la instalación silenciosa:
initexmf --set-config-value [MPM]AutoInstall=1

# 3. Compilar el PDF indicándole explícitamente a MiKTeX que no abra ventanas
pdflatex -interaction=nonstopmode -output-directory=docs docs/02_empatia.tex
pdflatex -interaction=nonstopmode -output-directory=docs docs/02_empatia.tex
```