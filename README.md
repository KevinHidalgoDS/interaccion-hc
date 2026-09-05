# 🖥️ Interacción Humano Computador (HCI) - 3009669

[![Python Version](https://img.shields.io/badge/python-3.14%2B-blue.svg)](https://www.python.org/)
[![UI/UX Prototyping](https://img.shields.io/badge/Prototyping-Streamlit_|_Gradio-FF4B4B.svg)](https://streamlit.io/)
[![Metodología](https://img.shields.io/badge/Metodolog%C3%ADa-%C3%81gil_|_Design_Thinking-brightgreen.svg)](https://agilemanifesto.org/)

## 📖 Descripción del Proyecto

Este repositorio define los estándares arquitectónicos y metodológicos para el desarrollo de
productos de datos centrados en el usuario, diseñado específicamente para la asignatura
**Interacción Humano Computador** (3009669) de la **Facultad de Minas, Universidad Nacional de
Colombia, Sede Medellín**.

El objetivo principal es profundizar en el intercambio de información entre las personas y los
computadores a través del diseño de interfaces para aplicaciones de ciencia de datos. El
proyecto integra el ciclo de vida de HCI desde la perspectiva de la ingeniería de software y
metodologías ágiles, analizando modelos mentales, aprendizaje humano y percepción.

---

## 📂 Estructura de Directorios

La estructura del repositorio refleja la integración de los pipelines tradicionales de _Machine
Learning_ con las fases metodológicas de diseño de interfaces basadas en el curso:

```text
├── data/
│   ├── raw/             # Datos crudos.
│   └── processed/       # Datos transformados listos para visualización.
├── docs/                # Documentación y reportes de lecturas.
│   ├── 01_empatizar/    # [Fase 1] Investigación de usuarios y empatía.
│   ├── 02_definir/      # [Fase 2] Definición del problema y modelos mentales.
│   ├── 03_idear/        # [Fase 3] Lluvia de ideas y diagramas de flujo.
│   └── lecturas/        # Reportes de lecturas semanales.
├── models/              # Modelos de ML serializados listos para inferencia.
├── notebooks/           # Análisis exploratorio (EDA) y validación de datos.
├── src/
│   ├── app/             # [Fase 4 & 6] Código fuente del prototipo y la implementación (ej. Streamlit).
│   ├── evaluation/      # [Fase 5] Scripts y métricas para evaluar el desempeño de las HCI.
│   └── models/          # Scripts de inferencia de los modelos subyacentes.
├── tests/               # Pruebas unitarias y de usabilidad automatizadas.
├── environment.yml      # Dependencias para Conda.
├── requirements.txt     # Dependencias para Pip.
└── README.md            # Este archivo.
```

---

## ⚙️ Requisitos y Dependencias

Para el desarrollo de interfaces (HCI) orientadas a la ciencia de datos utilizando herramientas
modernas e integrando metodologías ágiles, el proyecto requiere los siguientes componentes:

| Categoría              | Herramientas Sugeridas            | Propósito                                                                                                       |
| :--------------------- | :-------------------------------- | :-------------------------------------------------------------------------------------------------------------- |
| **Prototipado Rápido** | `streamlit`, `gradio`, `dash`     | Creación de interfaces web ágiles para modelos analíticos sin necesidad de usar frameworks de frontend pesados. |
| **Ciencia de Datos**   | `pandas`, `scikit-learn`, `numpy` | Procesamiento de datos en el backend de la aplicación.                                                          |
| **Calidad de Código**  | `black`, `flake8`, `pytest`       | Mantenimiento de los estándares de ingeniería de software.                                                      |

---

## 🚀 Instalación y Configuración

Asegúrate de replicar el entorno correctamente para facilitar las entregas semanales del proyecto.

**1. Clonar el repositorio:**

```bash
git clone https://github.com/KevinHidalgoDS/interaccion-hc.git
cd interaccion-hc
```

**2. Configurar el entorno virtual (usando venv o conda):**

```bash
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

---

## 💻 Uso y Ejecución

El ciclo de ejecución sigue las etapas de prototipado, evaluación e implementación del modelo de
ciclo de vida HCI.

Para desplegar la interfaz gráfica de usuario (GUI) localmente:

```bash
# Ejecutar el prototipo interactivo (Fase de Prototipar e Implementar)
streamlit run src/app/main.py
```

Para ejecutar las métricas de evaluación de desempeño de la interfaz (Fase de Evaluar):

```bash
python src/evaluation/usability_metrics.py
```

---

## 📏 Estándares de Código

- **Ingeniería de Software:** Todo el código debe adherirse a las prácticas estándar de ingeniería
  de software, utilizando convenciones de nombrado claras en inglés (o español, según el consenso
  del equipo) e implementando manejo de excepciones para evitar bloqueos en la interfaz.
- **Linting y Formateo:** Usa `Black` para el auto-formateo y `Flake8` para detectar errores
  lógicos.
- **Documentación en Código:** Utiliza _docstrings_ (formato Google) enfocados no solo en la lógica
  matemática, sino en la experiencia de usuario (ej. documentar qué espera recibir un componente de
  UI).

---

## 📦 Versionado de Datos y Modelos

- **Código fuente:** Controlado puramente con **Git**.
- **Modelos y Datos:** Si los modelos (ej. `.pkl`, `.onnx`) o los datasets sobrepasan los 50MB,
  utiliza **DVC (Data Version Control)** o **Git LFS**. Los repositorios analíticos orientados a
  interfaces no deben estar sobrecargados de datos estáticos para asegurar un despliegue ágil.

---

## 🧪 Testing y Validación

La validación en este proyecto es doble: técnica y humana.

1. **Testing de Software:** Utiliza `pytest` para probar el backend de los datos y las funciones
   auxiliares.
2. **Evaluación de la HCI:** Aplica metodologías que permitan evaluar el desempeño de la interfaz.
   Esto incluye:
   - Pruebas heurísticas.
   - Tests A/B simulados.
   - Recolección de métricas de uso (tiempos de respuesta, tasas de error del usuario).

---

## 📚 Documentación y Evaluación del Curso

La documentación debe mantenerse al día según la planeación del semestre.

La evaluación de este repositorio y del curso se distribuye de la siguiente manera:

- **Entregas semanales del Proyecto:** 30%. (Deben reflejarse mediante Pull Requests o _tags_ en el
  repositorio).
- **Reportes de lecturas:** 30%. (Se almacenarán en la carpeta `docs/lecturas/` en formato Markdown
  o PDF).
- **Entrega Final:** 40%. (Corresponde a la Sesión 8, donde se realizará la presentación final del
  prototipo implementado).

---

## 🤝 Contribuciones (Metodologías Ágiles)

El equipo de desarrollo utilizará metodologías ágiles para iterar sobre el producto.

1. Se trabajará en _sprints_ de una semana, alineados a las fases: Empatizar, Definir, Idear,
   Prototipar, Evaluar e Implementar.
2. Crea ramas descriptivas: `git checkout -b feature/fase5-prototipo-dashboard`.
3. Todo Pull Request debe ser revisado bajo la óptica técnica (código limpio) y bajo la óptica de
   usabilidad.

---

## 📄 Licencia y Atribuciones

Proyecto desarrollado bajo los lineamientos del profesor **Albeiro Espinosa Bedoya, Ph.D. Ms.C.**,
del Departamento de Ciencias de la Computación y de la Decisión de la **Universidad Nacional de
Colombia, Sede Medellín**.

**Licencia:** MIT License.
