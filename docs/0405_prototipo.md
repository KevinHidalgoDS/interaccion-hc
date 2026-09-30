---
title: "Entregable 4 y 5: Prototipado (IHC)"
author: "_Milena Castaño_ & _Daniela Torres_ & _Sebastian Sanchez_ & _Kevin Hidalgo_"
date: "29 de Septiembre de 2026"
institute: "Universidad Nacional de Colombia, Sede Medellín"
description:
  "Este entregable documenta el paso Definir del proceso de pensamiento de diseño (Design
  Thinking). A partir de la investigación de usuarios y la fase de empatía, se consolidan cuatro
  actividades clave: la creación de la Persona, el diseño del Mapa de experiencia del usuario, la
  formulación de la Declaración del problema y de posibilidades, y el desarrollo de la
  Investigación competitiva. El propósito es enmarcar el problema de manera estructurada para
  orientar la fase de ideación."

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
<h2><center>Definiendo el problema</center></h2>
<h3><center>Entregable #4 y #5</center></h3>

<a name="conte"></a>

<hr style="border:2px solid #CC00FF"> </hr>

**Elaborado por:** _Milena Castaño_ & _Daniela Torres_ & _Sebastian Sanchez_ & _Kevin Hidalgo_

**Correos:** _lmcastanoh@unal.edu.co_ & _datorresgom@unal.edu.co_ & _sebsanchezar@unal.edu.co_ &
_kfhidalgoh@unal.edu.co_

**Grupo:** 5

**Fecha de elaboración:** _2026 Septiembre 29_

**Fecha última modificación:** _2026 Septiembre 29_

---

<h2><center>Tabla de contenido</center></h2>

- [1. Persona](#1-persona)
  - [1.1 Insumos previos](#11-insumos-previos)
  - [1.2 Nombre y foto](#12-nombre-y-foto)
  - [1.3 Panorama general](#13-panorama-general)
  - [1.4 Antecedentes y biografía](#14-antecedentes-y-biografía)
  - [1.5 Gustos y metas](#15-gustos-y-metas)
  - [1.6 Disgustos y frustraciones](#16-disgustos-y-frustraciones)
- [2. Mapa de experiencia del usuario](#2-mapa-de-experiencia-del-usuario)
  - [2.1 Persona y antecedentes del recorrido](#21-persona-y-antecedentes-del-recorrido)
  - [2.2 Fases](#22-fases)
  - [2.3 Acciones, problemas y emociones por fase](#23-acciones-problemas-y-emociones-por-fase)
  - [2.4 Pensamientos y sentimientos](#24-pensamientos-y-sentimientos)
  - [2.5 Hallazgos y oportunidades (opcional)](#25-hallazgos-y-oportunidades-opcional)
- [3. Declaración del problema](#3-declaración-del-problema)
  - [3.1 Primer borrador (fórmula base)](#31-primer-borrador-fórmula-base)
  - [3.2 Iteraciones](#32-iteraciones)
  - [3.3 Declaración de posibilidades](#33-declaración-de-posibilidades)
- [4. Investigación competitiva](#4-investigación-competitiva)
  - [4.1 Definir el objetivo de la investigación](#41-definir-el-objetivo-de-la-investigación)
  - [4.2 Análisis de fortalezas, oportunidades, debilidades y amenazas (si aplica)](#42-análisis-de-fortalezas-oportunidades-debilidades-y-amenazas-si-aplica)
  - [4.3 Demostración relámpago (si aplica)](#43-demostración-relámpago-si-aplica)
  - [4.4 Análisis competitivo (si aplica)](#44-análisis-competitivo-si-aplica)
- [5. Consolidación del entregable — Paso Definir](#5-consolidación-del-entregable--paso-definir)
  - [5.1 Persona (resumen)](#51-persona-resumen)
  - [5.2 Mapa de experiencia del usuario (resumen)](#52-mapa-de-experiencia-del-usuario-resumen)
  - [5.3 Declaración del problema final](#53-declaración-del-problema-final)
  - [5.4 Declaración de posibilidades, final](#54-declaración-de-posibilidades-final)
  - [5.5 Hallazgos clave de la investigación competitiva](#55-hallazgos-clave-de-la-investigación-competitiva)

---

## Stitch

### prompt 1

```text
Analiza el documento adjunto e identifica todas las necesidades, requisitos funcionales,
restricciones técnicas, usuarios objetivo y objetivos del negocio expresados en él.

Con base en ese análisis, actúa como un ingeniero de prompts especializado en desarrollo de
plataformas digitales. Tu tarea es crear un prompt detallado y ejecutable que un desarrollador o
equipo de desarrollo pueda usar directamente para construir un prototipo funcional que satisfaga
todas las necesidades identificadas.

El prompt que generes debe:

- **Definir claramente la plataforma**: qué es, para quién es, qué problemas resuelve
- **Especificar funcionalidades clave**: lista todas las características que el prototipo debe
  incluir, ordenadas por prioridad
- **Establecer requisitos técnicos**: stack tecnológico recomendado, integraciones necesarias,
  consideraciones de seguridad o escalabilidad mencionadas
- **Detallar flujos de usuario**: cómo los usuarios objetivo interactuarán con la plataforma
- **Incluir limitaciones y restricciones**: presupuesto, timeline, limitaciones técnicas u
  organizacionales
- **Proporcionar criterios de éxito**: qué hace que el prototipo sea considerado exitoso
- **Ser específico y accionable**: que el desarrollador no tenga que hacer interpretaciones, el
  prompt debe ser tan claro que cualquiera pueda construir directamente sobre él

El prompt final debe estar listo para ser usado inmediatamente por un desarrollador, sin necesidad
de clarificaciones adicionales. Escríbelo en español, dirigido directamente al desarrollador que lo
usará.
```

### prompt 2

```text
Actúa como un Desarrollador Full-Stack y Arquitecto de Datos. Tu objetivo es construir un prototipo
funcional para una nueva plataforma de monitoreo y calidad de datos. A continuación, se detallan las
especificaciones exactas, el contexto y los requerimientos para la ejecución del desarrollo.

## 1. Definición de la Plataforma

* **Nombre del Proyecto:** Plataforma de monitoreo, observabilidad y gestión de calidad de datos
  para el Sistema de Información para el Mercado de Energía Mayorista (SIMEM).


* **Usuarios Objetivo:** Personal interno de XM, compuesto por analistas de datos, ingenieros y
  operadores del mercado energético. Estos usuarios poseen un alto conocimiento técnico del dominio,
  operan en entornos de múltiples monitores y manejan una carga cognitiva crítica.


* **Problema que Resuelve:** La arquitectura actual fragmenta la revisión de calidad mediante
  notificaciones pasivas por correo electrónico, hojas de cálculo locales y un script de validación
  en Python configurado por archivos `.CSV`. Esto ocasiona detecciones reactivas de registros
  erróneos, pérdida de trazabilidad en versiones secuenciales de datos (ej. liquidaciones
  preliminares TX1 vs. TX2) e incertidumbre sobre la actualización real de los datos publicados. El
  prototipo centralizará la información para detectar anomalías de manera proactiva, evitando que
  los usuarios finales reporten errores a través de los canales de CRM.



## 2. Funcionalidades Clave (Ordenadas por Prioridad)

1. **Dashboard de Inteligencia de Negocios (BI) Unificado:** Implementar una capa de visualización
   gráfica e intuitiva que muestre el porcentaje de calidad global y por conjunto de datos, además
   de permitir la identificación temprana de tendencias inusuales.


2. **Módulo de Configuración Ágil:** Construir una interfaz que permita la configuración y
   parametrización de nuevos conjuntos de datos a evaluar, eliminando por completo la dependencia
   actual de editar archivos `.CSV` manualmente.


3. **Monitor de Completitud y Versionado:** Crear un verificador algorítmico que valide que los
   conjuntos de datos de liquidación del mercado cuentan con todas sus versiones cronológicas
   correspondientes publicadas.


4. **Control de Oportunidad y Remediación:** Desarrollar un sistema de monitoreo que cruce la fecha
   de publicación esperada contra la real, integrando un mecanismo para relanzar masivamente los
   procesos de carga que se detecten como atrasados.


5. **Catálogo de Gestión de Inconsistencias:** Implementar un repositorio estructurado que
   caracterice automáticamente los hallazgos según su tipología, frecuencia, criticidad, origen e
   impacto.



## 3. Requisitos Técnicos e Integraciones

* **Stack Tecnológico Recomendado:** Utiliza Python para estructurar la lógica del backend y escalar
  los validadores actuales. Emplea SQL para las consultas directas de contrastación y despliega la
  solución utilizando servicios de Microsoft Azure (como Azure Data Factory y Azure Functions) para
  garantizar una orquestación fluida con la infraestructura en la nube.


* **Fuentes de Integración:** El sistema debe conectarse a un *dataLake* que recibe aproximadamente
  un millón de registros diarios. El prototipo debe ser capaz de orquestar conexiones hacia
  repositorios alternos como servidores FTP (para recuperar históricos perdidos), bases de datos
  transaccionales, archivos Excel y APIs.


* **Ergonomía e Interfaz (IHC):** La interfaz gráfica debe diseñarse con una curva de aprendizaje
  baja. Es obligatorio incluir alto contraste visual, claridad tipográfica estricta para el
  renderizado de datos numéricos y atajos de teclado que minimicen la dependencia de clics
  repetitivos, mitigando la fatiga motora y visual del usuario.



## 4. Flujos de Usuario Detallados

* **Flujo de Detección:** El sistema evalúa el *dataLake* e identifica una inconsistencia, generando
  una alerta visual priorizada en el dashboard central en lugar de enviar un correo
  descontextualizado.


* **Flujo de Contrastación (Data Diffing):** El analista selecciona la alerta y accede a una vista
  consolidada que cruza y compara de forma directa la información entregada por el agente generador
  (fuente) frente al resultado fallido de la ETL.


* **Flujo de Resolución y Feedback:** El usuario corrige la anomalía o relanza el proceso desde la
  misma plataforma, recibiendo retroalimentación síncrona e inmediata del sistema para confirmar la
  disponibilidad y calidad del dato, manteniendo intacto su estado de flujo mental.



## 5. Limitaciones y Restricciones

* **Desempeño y Escalabilidad:** El procesamiento de validación no debe generar cuellos de botella
  técnicos sobre las bases de datos fuente ni en el *dataLake* al manejar el millón de registros
  diarios.


* **Restricciones Operativas:** Los datos históricos frecuentemente dejan de estar disponibles en
  bases de datos rápidas, obligando al sistema a interactuar de forma segura con repositorios
  alternos legados sin aumentar el riesgo de errores.



## 6. Criterios de Éxito del Prototipo

* La plataforma erradica los "Abismos de Ejecución", evitando que el usuario deba abandonar el flujo
  de trabajo para extraer datos hacia Excel, Notepad o redactar correos de soporte a terceros para
  validar cargas.


* El dashboard proporciona visibilidad inmediata (en menos de 3 clics) para responder preguntas
  críticas del negocio, tales como: "¿Cuáles hallazgos ya fueron gestionados?" o "¿Están correctos
  los vertimientos del embalse X para el día de hoy?".


* Se elimina la sobrecarga cognitiva al requerir que el usuario memorice datos entre múltiples
  pantallas de validación.
```

### prompt 3

```text
Actúa como un Desarrollador Frontend y Diseñador UI/UX especializado en la creación rápida de
prototipos. Tu objetivo es construir la interfaz gráfica (frontend) de una nueva plataforma de
monitoreo y calidad de datos utilizando herramientas de generación de UI como Canvas o
[https://stitch.google.com](https://stitch.google.com). Para este prototipo, asume que todos los
datos provendrán de un backend simulado (mocked data). A continuación, se detallan las
especificaciones exactas para la ejecución del desarrollo del frontend.

## 1. Definición de la Plataforma

* **Nombre del Proyecto:** Interfaz frontend para la plataforma de monitoreo, observabilidad y
  gestión de calidad de datos del Sistema de Información para el Mercado de Energía Mayorista
  (SIMEM).


* **Usuarios Objetivo:** Personal interno de XM (analistas de datos, ingenieros y operadores del
  mercado). Estos usuarios poseen un alto conocimiento técnico, pero sufren de fatiga visual y alta
  carga cognitiva. Utilizan configuraciones de múltiples monitores y operan bajo restricciones de
  tiempo crítico.


* **Problema que Resuelve:** La interfaz actualiza una experiencia fragmentada (basada en correos
  masivos, tablas en CSV y bases de datos aisladas) hacia un entorno unificado y visual. El objetivo
  del frontend es consolidar alertas, métricas y herramientas de diagnóstico en una sola pantalla
  para evitar la sobrecarga de la memoria de trabajo del usuario.



## 2. Funcionalidades Clave (Ordenadas por Prioridad)

Crea los siguientes componentes visuales:

1. **Torre de Control (Dashboard Principal):** Un panel unificado que consolide métricas de calidad
   global y alertas priorizadas en tiempo real. Debe incluir componentes gráficos (ej. series de
   tiempo) para identificar tendencias visualmente.


2. **Sistema Visual de Alertas (Semáforo):** Las tablas o listas de alertas deben diferenciar
   claramente, mediante etiquetas e indicadores visuales (colores/íconos), tres estados distintos:
   conjuntos "atrasados", conjuntos con "errores de calidad" y "errores de configuración de la
   herramienta" (falsas alertas).


3. **Vista de Contrastación (Data Diffing):** Un componente modal o panel lateral de detalle
   contextual que muestre frente a frente el valor publicado en SIMEM versus el valor registrado en
   la fuente. Las diferencias y valores faltantes deben estar resaltados visualmente (similar a un
   *diff* de código).


4. **Asistente Visual de Configuración:** Un formulario guiado paso a paso (wizard) para dar de
   alta nuevas variables y configurar conjuntos de datos. Este componente reemplaza por completo la
   necesidad de editar archivos `.CSV` o código SQL manualmente.


5. **Controles de Remediación Integrados:** Botones de acción directa (Call to Action) dentro del
   panel de detalle para "Reejecutar proceso", "Actualizar masivamente" o "Aprobar", cerrando el
   ciclo de evaluación sin salir de la vista.



## 3. Requisitos Técnicos y de Diseño (IHC)

* **Herramientas:** Utiliza componentes compatibles con Canvas, Stitch (React/Tailwind u otras
  librerías web estándar) para prototipado rápido.
* **Ergonomía y Accesibilidad:** La interfaz debe minimizar la dependencia de clics repetitivos
  mediante atajos de teclado.


* **Claridad Visual:** Es estrictamente obligatorio usar alto contraste y dar prioridad a la
  claridad tipográfica (fuentes monoespaciadas o tabulares) para el renderizado de datos numéricos.


* **Simulación de Datos:** Utiliza datos de prueba (mock data) relacionados con el dominio
  energético, como versiones de liquidación (TX1, TX2), variables de embalses (ej. ESMERALDA) y
  métricas de completitud.



## 4. Flujos de Usuario Detallados (Navegación del Prototipo)

* **Paso 1 (Inicio):** El usuario ingresa a la "Torre de Control" y visualiza un resumen ejecutivo
  de las anomalías del día, ordenadas por severidad, sin necesidad de abrir su correo electrónico.


* **Paso 2 (Diagnóstico):** El usuario hace clic en un indicador en rojo (ej. "Error de Calidad").
  La pantalla no recarga completamente, sino que despliega la "Vista de Contrastación" donde
  observa el dato original resaltado junto al dato erróneo del Data Lake.


* **Paso 3 (Acción):** El usuario presiona un botón de "Relanzar carga" y visualiza un componente
  de feedback inmediato (ej. *toast notification* o *spinner*) que confirma que el proceso se está
  ejecutando, manteniendo la continuidad de la tarea.



## 5. Limitaciones y Restricciones

* **Entorno de Visualización:** El diseño debe estar optimizado para formato de escritorio
  (Desktop), ya que los analistas operan en oficinas con monitores amplios; la vista móvil no es
  prioridad para este prototipo.


* **Carga Visual:** Evitar la saturación de colores. Utilizar el color de forma semántica
  únicamente para indicar estados (rojo para errores, amarillo para atrasos, verde para éxitos).



## 6. Criterios de Éxito del Prototipo Frontend

* **Navegación Eficiente:** Cualquier detalle sobre el estado de un dato o hallazgo de
  inconsistencia debe ser accesible en menos de 3 clics desde la pantalla principal.


* **Auto-contención:** El prototipo debe demostrar que la interfaz por sí sola es suficiente para
  identificar la falla, comparar los datos y ordenar la remediación sin sugerir que el usuario abra
  herramientas de terceros.


* **Comprensión Inmediata:** Un usuario que observe la vista de alertas debe poder distinguir al
  instante, gracias a las etiquetas visuales, si un problema se debe a que un dato no llegó
  (atraso) o a que llegó incorrecto (calidad).
```

