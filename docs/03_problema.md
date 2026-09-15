---
title: "Entregable 3: Fase de Definición (IHC)"
author: "_Milena Castaño_ & _Daniela Torres_ & _Sebastian Sanchez_ & _Kevin Hidalgo_"
date: "14 de Septiembre de 2026"
institute: "Universidad Nacional de Colombia, Sede Medellín"
description:
  "Este entregable documenta el paso Definir del proceso de pensamiento de diseño (Design Thinking). 
  A partir de la investigación de usuarios y la fase de empatía, se consolidan cuatro actividades clave: 
  la creación de la Persona, el diseño del Mapa de experiencia del usuario, la formulación de la 
  Declaración del problema y de posibilidades, y el desarrollo de la Investigación competitiva. 
  El propósito es enmarcar el problema de manera estructurada para orientar la fase de ideación."

# --- Configuraciones para Pandoc (PDF) ---
lang: es-CO
bibliography: docs/referencias.bib
csl: docs/ieee.csl

# Formato visual del PDF (LaTeX)
geometry:
  - top=2.5cm
  - bottom=2.5cm
  - left=3cm
  - right=2.5cm
fontsize: 12pt
linestretch: 1.15
papersize: letter
toc: true
toc-depth: 2
---

<hr style="border:2px solid #CC00FF"> </hr>
<a><img src="https://www.vhv.rs/dpng/d/313-3134285_logo-de-la-universidad-nacional-de-colombia-png.png" width="100" align="center"></a>
<a><img src="https://minaslap.net/pluginfile.php/1/core_admin/logo/0x200/1770226238/Logo%20MinasLAP-3%20%281%29.png" width="100" align="center"></a>
<h1><center>Interacción Humano-Computador</center></h1>
<h2><center>Introducción a la Interacción Humano-Computador</center></h2>
<h3><center>Entregable #2 Empatia</center></h3>

<a name="conte"></a>

<hr style="border:2px solid #CC00FF"> </hr>

**Elaborado por:** _Milena Castaño_ & _Daniela Torres_ & _Sebastian Sanchez_ & _Kevin Hidalgo_

**Correos:** _lmcastanoh@unal.edu.co_ & _datorresgom@unal.edu.co_ & _sebsanchezar@unal.edu.co_ &
_kfhidalgoh@unal.edu.co_

**Grupo:** 5

**Fecha de elaboración:** _2026 Septiembre 14_

**Fecha última modificación:** _2026 Septiembre 14_

---

<h2><center>Tabla de contenido</center></h2>

- [1.1. Persona\[cite: 6\]](#11-personacite-6)
  - [1.1.1. 1.1 Insumos previos\[cite: 6\]](#111-11-insumos-previoscite-6)
  - [1.1.2. 1.2 Nombre y foto\[cite: 6\]](#112-12-nombre-y-fotocite-6)
  - [1.1.3. 1.3 Panorama general\[cite: 6\]](#113-13-panorama-generalcite-6)
  - [1.1.4. 1.4 Antecedentes y biografía\[cite: 6\]](#114-14-antecedentes-y-biografíacite-6)
  - [1.1.5. 1.5 Gustos y metas\[cite: 6\]](#115-15-gustos-y-metascite-6)
  - [1.1.6. 1.6 Disgustos y frustraciones\[cite: 6\]](#116-16-disgustos-y-frustracionescite-6)
- [1.2. Mapa de experiencia del usuario\[cite: 6\]](#12-mapa-de-experiencia-del-usuariocite-6)
  - [1.2.1. 2.1 Persona y antecedentes del recorrido\[cite: 6\]](#121-21-persona-y-antecedentes-del-recorridocite-6)
  - [1.2.2. 2.2 Fases\[cite: 6\]](#122-22-fasescite-6)
  - [1.2.3. 2.3 Acciones, problemas y emociones por fase\[cite: 6\]](#123-23-acciones-problemas-y-emociones-por-fasecite-6)
  - [1.2.4. 2.4 Pensamientos y sentimientos\[cite: 6\]](#124-24-pensamientos-y-sentimientoscite-6)
  - [1.2.5. 2.5 Hallazgos y oportunidades (opcional)\[cite: 6\]](#125-25-hallazgos-y-oportunidades-opcionalcite-6)
- [1.3. Declaración del problema\[cite: 6\]](#13-declaración-del-problemacite-6)
  - [1.3.1. 3.1 Primer borrador (fórmula base)\[cite: 6\]](#131-31-primer-borrador-fórmula-basecite-6)
  - [1.3.2. 3.2 Iteraciones\[cite: 6\]](#132-32-iteracionescite-6)
  - [1.3.3. 3.3 Declaración de posibilidades\[cite: 6\]](#133-33-declaración-de-posibilidadescite-6)
- [1.4. Investigación competitiva\[cite: 6\]](#14-investigación-competitivacite-6)
  - [1.4.1. 4.1 Definir el objetivo de la investigación\[cite: 6\]](#141-41-definir-el-objetivo-de-la-investigacióncite-6)
  - [1.4.2. 4.2 Análisis de fortalezas, oportunidades, debilidades y amenazas (si aplica)\[cite: 6\]](#142-42-análisis-de-fortalezas-oportunidades-debilidades-y-amenazas-si-aplicacite-6)
  - [1.4.3. 4.3 Demostración relámpago (si aplica)\[cite: 6\]](#143-43-demostración-relámpago-si-aplicacite-6)
  - [1.4.4. 4.4 Análisis competitivo (si aplica)\[cite: 6\]](#144-44-análisis-competitivo-si-aplicacite-6)
- [1.5. Consolidación del entregable — Paso Definir\[cite: 6\]](#15-consolidación-del-entregable--paso-definircite-6)
  - [1.5.1. 5.1 Persona (resumen)\[cite: 6\]](#151-51-persona-resumencite-6)
  - [1.5.2. 5.2 Mapa de experiencia del usuario (resumen)\[cite: 6\]](#152-52-mapa-de-experiencia-del-usuario-resumencite-6)
  - [1.5.3. 5.3 Declaración del problema final\[cite: 6\]](#153-53-declaración-del-problema-finalcite-6)
  - [1.5.4. 5.4 Declaración de posibilidades, final\[cite: 6\]](#154-54-declaración-de-posibilidades-finalcite-6)
  - [1.5.5. 5.5 Hallazgos clave de la investigación competitiva\[cite: 6\]](#155-55-hallazgos-clave-de-la-investigación-competitivacite-6)


---


**Instrucciones generales**
Esta plantilla guía al equipo a través de las cuatro actividades del paso Definir del proceso de pensamiento de diseño, en el orden en que se desarrollan en el capítulo de referencia:
* Persona
* Mapa de experiencia del usuario
* Declaración del problema y declaración de posibilidades
* Investigación competitiva

Completen cada sección con base en la investigación de usuarios ya realizada (entrevistas, mapa de afinidad, declaraciones en primera persona). Al finalizar, la plantilla completa constituye el entregable consolidado del paso Definir.

---

## 1.1. Persona

### 1.1.1. 1.1 Insumos previos
* [ ] Entrevistas de usuario realizadas
* [ ] Mapa de afinidad elaborado
* [ ] Declaraciones en primera persona generadas a partir del mapa de afinidad

### 1.1.2. 1.2 Nombre y foto
* **Nombre de la persona:** [Escribir aquí]
* **Foto o ícono representativo (adjuntar o describir):** [Escribir aquí]

> *Nota: si el equipo considera que un nombre o foto reales pueden introducir sesgos de identidad (por ejemplo, de género), pueden optar por un nombre abstracto (por ejemplo, “el inversionista tecnológico”) y un ícono en lugar de una foto.*

### 1.1.3. 1.3 Panorama general

| Campo | Descripción |
| :--- | :--- |
| Profesión / ocupación | [Escribir aquí] |
| Edad | [Escribir aquí] |
| Intereses / juegos / marcas afines | [Escribir aquí] |

### 1.1.4. 1.4 Antecedentes y biografía
Redactar en 3-5 líneas la historia de la persona: pasatiempos, comportamientos regulares y cómo se relacionan con el problema que se está explorando.
> [Escribir aquí]

### 1.1.5. 1.5 Gustos y metas
Enumerar las metas de la persona, distinguiendo motivación interna (satisfacción personal) de motivación externa (recompensas).
* **Meta 1:** [Escribir aquí]
* **Meta 2:** [Escribir aquí]
* **Meta 3:** [Escribir aquí]

### 1.1.6. 1.6 Disgustos y frustraciones
Enumerar qué obstaculiza a la persona, qué le resulta complicado o dónde falla actualmente su experiencia.
* **Frustración 1:** [Escribir aquí]
* **Frustración 2:** [Escribir aquí]
* **Frustración 3:** [Escribir aquí]

---

## 1.2. Mapa de experiencia del usuario

### 1.2.1. 2.1 Persona y antecedentes del recorrido
* **Persona que protagoniza el recorrido:** [Escribir aquí]
* **Cita o frase que resume por qué realiza este recorrido:** [Escribir aquí]

### 1.2.2. 2.2 Fases
Definir las fases o hitos de alto nivel del recorrido. Agregar filas según se necesiten.

| # | Fase | Descripción breve |
| :--- | :--- | :--- |
| 1 | [Escribir fase] | [Escribir descripción] |
| 2 | [Escribir fase] | [Escribir descripción] |
| 3 | [Escribir fase] | [Escribir descripción] |

### 1.2.3. 2.3 Acciones, problemas y emociones por fase
Para cada fase, detallar las acciones o decisiones de la persona, los problemas que enfrenta y su nivel de satisfacción.

| Fase | Acciones (decisiones) | Problemas encontrados | Satisfacción (Baja/Media/Alta) |
| :--- | :--- | :--- | :--- |
| [Escribir fase] | [Escribir acciones] | [Escribir problemas] | [Escribir nivel] |
| [Escribir fase] | [Escribir acciones] | [Escribir problemas] | [Escribir nivel] |

### 1.2.4. 2.4 Pensamientos y sentimientos
Incluir citas textuales de usuarios reales como evidencia, o abstracciones a manera de hallazgo. Se recomienda priorizar citas directas.

| Fase | Cita o hallazgo |
| :--- | :--- |
| [Escribir fase] | [Escribir cita] |
| [Escribir fase] | [Escribir cita] |

### 1.2.5. 2.5 Hallazgos y oportunidades (opcional)
Interpretaciones de los problemas detectados en cada fase, como posibles oportunidades de diseño para etapas posteriores.

| Fase | Hallazgo u oportunidad detectada |
| :--- | :--- |
| [Escribir fase] | [Escribir hallazgo] |
| [Escribir fase] | [Escribir hallazgo] |

---

## 1.3. Declaración del problema

### 1.3.1. 3.1 Primer borrador (fórmula base)
> Como **[usuario]**, necesito/quiero **[necesidad]** para poder **[meta]**.

### 1.3.2. 3.2 Iteraciones
El capítulo señala que escribir una buena declaración del problema es un proceso repetitivo y progresivo. Completar al menos tres iteraciones, aplicando en cada una un criterio de mejora.

* **Iteración 1 — Primer intento:** Como **[ ]**, quiero **[ ]** para **[ ]**.
* **Iteración 2 — Aplicando “ser específico”:** Como **[ ]**, quiero **[ ]** para **[ ]**.
  * *¿Es demasiado específica? ¿Ya incluye una solución dentro del problema? Justificar:* [Escribir aquí]
* **Iteración 3 — Aplicando “dejar espacio para explorar” y “no asumir una solución”:** Como **[ ]**, quiero **[ ]** para **[ ]**.
  * *Verificar: ¿la necesidad está expresada como verbo (necesidad real) o como sustantivo (solución encubierta)?* [Escribir aquí]
* **Iteración final — Aplicando “escribir con empatía”:** Como **[ ]**, quiero **[ ]** para **[ ]**.

### 1.3.3. 3.3 Declaración de posibilidades
A partir de la declaración del problema final, redactar una o más preguntas que orienten la ideación, con la forma “¿Cómo podríamos...?”.

* **Pregunta base:** ¿Cómo podríamos **[ayudar a la persona o usuario a lograr algo relacionado con su meta]**?
* **Variante 1 (usando el nombre de la persona en lugar de “usuarios”):** ¿Cómo podríamos ayudar a **[Nombre de la persona]** a **[ ]**?
* **Variante 2 (explorando otro ángulo del mismo problema):** ¿Cómo podríamos **[ ]**?

---

## 1.4. Investigación competitiva

### 1.4.1. 4.1 Definir el objetivo de la investigación
* **Objetivo de la investigación competitiva:** [Escribir aquí]
> *Ejemplo de guía: ¿buscan entender fortalezas y debilidades de la competencia? ¿buscan inspiración para la ideación? ¿buscan auditar características o precios de la competencia?*

* **Técnica(s) seleccionada(s):**
  * [ ] Análisis de fortalezas, oportunidades, debilidades y amenazas
  * [ ] Demostración relámpago
  * [ ] Análisis competitivo

### 1.4.2. 4.2 Análisis de fortalezas, oportunidades, debilidades y amenazas (si aplica)

| | Factores internos | Factores externos |
| :--- | :--- | :--- |
| **Positivos** | **Fortalezas:** [Escribir aquí] | **Oportunidades:** [Escribir aquí] |
| **Negativos** | **Debilidades:** [Escribir aquí] | **Amenazas:** [Escribir aquí] |

**Ideas de producto derivadas del análisis:**
* **Idea 1:** [Escribir aquí]
* **Idea 2:** [Escribir aquí]

### 1.4.3. 4.3 Demostración relámpago (si aplica)
Reunir entre 8 y 10 ejemplos de productos: competidores directos, productos relacionados y productos inspiradores sin relación directa.

| # | Producto o ejemplo | Tipo (competidor/relacionado/inspirador) | Captura de pantalla (adjuntar) | ¿Qué inspira de este ejemplo? |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [Escribir producto] | [Escribir tipo] | [Adjuntar captura] | [Escribir inspiración] |
| 2 | [Escribir producto] | [Escribir tipo] | [Adjuntar captura] | [Escribir inspiración] |

### 1.4.4. 4.4 Análisis competitivo (si aplica)
* **Paso 1 — Objetivo del análisis:** [Escribir aquí]
* **Paso 2 — Criterios de comparación establecidos:**
  * Criterio 1: [Escribir aquí]
  * Criterio 2: [Escribir aquí]
  * Criterio 3: [Escribir aquí]

* **Paso 3 — Compañías a analizar (directas e indirectas):**

| Compañía | Tipo (directa/indirecta/comparador) | Enlace / acceso | ¿Requiere inicio de sesión? |
| :--- | :--- | :--- | :--- |
| [Escribir compañía] | [Escribir tipo] | [Escribir enlace] | [Sí/No] |

* **Paso 4 — Recolección de datos:**

| Compañía | Criterio 1 | Criterio 2 | Criterio 3 | Evidencia (captura/video) |
| :--- | :--- | :--- | :--- | :--- |
| [Escribir compañía] | [Dato] | [Dato] | [Dato] | [Adjuntar evidencia] |

* **Paso 5 — Resumen de resultados:**
Redactar aquí las conclusiones y hallazgos clave del análisis, con referencia a las evidencias visuales recolectadas.
> [Escribir aquí]

---

## 1.5. Consolidación del entregable — Paso Definir
Resumen final que integra los resultados de las cuatro secciones anteriores. Este es el entregable a presentar.

### 1.5.1. 5.1 Persona (resumen)
* **Nombre:** [Escribir aquí]
* **Meta principal:** [Escribir aquí]
* **Frustración principal:** [Escribir aquí]

### 1.5.2. 5.2 Mapa de experiencia del usuario (resumen)
* **Fases identificadas:** [Escribir aquí]
* **Punto más bajo de satisfacción:** [Escribir aquí]
* **Principal oportunidad detectada:** [Escribir aquí]

### 1.5.3. 5.3 Declaración del problema final
> Como **[ ]**, quiero **[ ]** para **[ ]**.

### 1.5.4. 5.4 Declaración de posibilidades, final
> ¿Cómo podríamos **[ ]**?

### 1.5.5. 5.5 Hallazgos clave de la investigación competitiva
* **Hallazgo 1:** [Escribir aquí]
* **Hallazgo 2:** [Escribir aquí]
* **Hallazgo 3:** [Escribir aquí]