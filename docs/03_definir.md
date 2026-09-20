---
title: "Entregable 3: Fase de Definición (IHC)"
author: "_Milena Castaño_ & _Daniela Torres_ & _Sebastian Sanchez_ & _Kevin Hidalgo_"
date: "14 de Septiembre de 2026"
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
<h3><center>Entregable #3</center></h3>

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

**Instrucciones generales** Esta plantilla guía al equipo a través de las cuatro actividades del
paso Definir del proceso de pensamiento de diseño, en el orden en que se desarrollan en el capítulo
de referencia:

- Persona
- Mapa de experiencia del usuario
- Declaración del problema y declaración de posibilidades
- Investigación competitiva

Completen cada sección con base en la investigación de usuarios ya realizada (entrevistas, mapa de
afinidad, declaraciones en primera persona). Al finalizar, la plantilla completa constituye el
entregable consolidado del paso Definir.

---

## 1. Persona

### 1.1 Insumos previos

- [x] Entrevistas de usuario realizadas
- [x] Mapa de afinidad elaborado
- [x] Declaraciones en primera persona generadas a partir del mapa de afinidad

### 1.2 Nombre y foto

- **Nombre de la persona:** El Analista de Calidad Operativa
- **Foto o ícono representativo (adjuntar o describir):** Foco en verificación diaria de alertas,
  correos y cruce de datos ![analista_de_calidad_operativa][img_analista_de_calidad_operativa]

- **Nombre de la persona:** El Ingeniero de Configuración y Metadatos
- **Foto o ícono representativo (adjuntar o describir):** Foco en la gestión manual de archivos
  CSV, parámetros y ajustes de queries SQL
  ![ingeniero_de_configuración_y_metadatos][img_ingeniero_de_configuración_y_metadatos]

- **Nombre de la persona:** Especialista de Monitoreo Multifuente
- **Foto o ícono representativo (adjuntar o describir):** Foco en la supervisión de ejecuciones,
  Data Lakes, recargues y resolución de cuellos de botella
  ![especialista_de_monitoreo_multifuente][img_especialista_de_monitoreo_multifuente]

> _Nota: si el equipo considera que un nombre o foto reales pueden introducir sesgos de identidad
> (por ejemplo, de género), pueden optar por un nombre abstracto (por ejemplo, “el inversionista
> tecnológico”) y un ícono en lugar de una foto._

### 1.3 Panorama general

<!-- prettier-ignore -->
| Campo | Descripción |
| :--- | :--- |
| Profesión / ocupación | Ingeniero de Datos / Analista de Calidad de Datos |
| Edad | 28 años |
| Intereses / juegos / marcas afines | Intereses: Acampar los fines de semana, asistir a conciertos de música en vivo y festivales, pedir comida a domicilio en días de alta carga laboral. Juegos: Cult of the Lamb, Mario Kart. Marcas afines: Nintendo, Rappi, Domino's Pizza, Cine Colombia. |

<!-- prettier-ignore -->
| Campo | Descripción |
| :--- | :--- |
| Profesión / ocupación | Desarrollador Python / Arquitecto Cloud |
| Edad | 32 años |
| Intereses / juegos / marcas afines | Intereses: Motociclismo de aventura y planeación de rutas largas por el país, preparación de café de especialidad con métodos de filtrado, cocina con ingredientes vegetales. Juegos: Videojuegos independientes y simuladores. Marcas afines: Royal Enfield, Microsoft Azure, Victoria (hierro fundido), Supermercado Vaquita. |

<!-- prettier-ignore -->
| Campo | Descripción |
| :--- | :--- |
| Profesión / ocupación | Científico de Datos / Estudiante de Maestría en Analítica |
| Edad | 30 años |
| Intereses / juegos / marcas afines | Intereses: Senderismo por reservas naturales y cascadas, viajes a pueblos patrimonio, cuidado de plantas de interior y patios. Juegos: Juegos tipo MMO (Albion) y MOBA. Marcas afines: Samsung, Decathlon, Mercado Libre, Frutos & Semillas. |

### 1.4 Antecedentes y biografía

Redactar en 3-5 líneas la historia de la persona: pasatiempos, comportamientos regulares y cómo se
relacionan con el problema que se está explorando.

> - **Analista de Calidad Operativa:** Disfruta desconectarse acampando o asistiendo a conciertos,
>   pero en su día a día sufre de fatiga visual al tener que cruzar manualmente decenas de correos
>   con el administrador SIMEM. Su hábito de pedir comida a domicilio refleja su necesidad de
>   soluciones rápidas y convenientes, algo de lo que carece su flujo de trabajo actual, donde un
>   solo dato erróneo le consume toda la mañana. Busca alertas claras y centralizadas que le eviten
>   el desgaste repetitivo de buscar problemas dispersos y le dejen tiempo para tareas de mayor
>   valor.
> - **Ingeniero de Configuración y Metadatos:** Es un apasionado de las rutas largas en motocicleta
>   y la preparación metódica del café de especialidad, actividades que exigen precisión y
>   paciencia. En su trabajo, aplica esa misma meticulosidad para configurar manualmente variables
>   en archivos Excel/CSV y ajustar queries SQL, pero le frustra profundamente lo "artesanal" y
>   propenso a errores que es este proceso. El tener que "apagar incendios" por configuraciones
>   desactualizadas le roba energía que preferiría invertir en automatizar procesos y diseñar
>   arquitecturas más robustas.
> - **Especialista de Monitoreo Multifuente:** Acostumbrado a explorar extensos senderos en la
>   naturaleza y a coordinar estrategias complejas en juegos MMO, tiene gran capacidad para manejar
>   múltiples frentes a la vez. Sin embargo, en el trabajo, abrir simultáneamente el administrador
>   SIMEM, el Data Lake, Visual Studio Code y múltiples pestañas para monitorear recargues le
>   genera una sobrecarga cognitiva insostenible. Sueña con agentes inteligentes que sinteticen las
>   alertas por Teams, para que el miedo a olvidar una configuración temporal no le quite la
>   tranquilidad durante sus fines de semana.

### 1.5 Gustos y metas

Enumerar las metas de la persona, distinguiendo motivación interna (satisfacción personal) de
motivación externa (recompensas).

> **Analista de Calidad Operativa:**
>
> > - **Meta 1:** Centralizar la recepción y visualización de alertas en un solo lugar.
> >   - Motivación interna: Reducir la fatiga visual y el desgaste mental de saltar entre el correo
> >     electrónico, archivos CSV y el administrador SIMEM.
> >   - Motivación externa: Disminuir el tiempo de resolución de incidentes y evitar que una alerta
> >     crítica pase desapercibida por la saturación de correos.
> > - **Meta 2:** Identificar de un vistazo el origen exacto del fallo (SIMEM, Data Lake o fuente
> >   original).
> >   - Motivación interna: Sentir seguridad y control sobre el flujo de trabajo, eliminando la
> >     incertidumbre de no saber por dónde empezar a buscar.
> >   - Motivación externa: Reducir las horas de la mañana dedicadas al "apagado de incendios" y
> >     delegar el problema rápidamente al área responsable.
> > - **Meta 3:** Transicionar hacia un rol más estratégico y menos operativo.
> >   - Motivación interna: Satisfacción intelectual al dejar atrás tareas repetitivas y monótonas.
> >   - Motivación externa: Obtener reconocimiento por generar análisis de mayor valor para el
> >     negocio, dashboards e informes en lugar de solo auditar datos.

> **Ingeniero de Configuración y Metadatos:**
>
> > - **Meta 1:** Automatizar el registro y creación de nuevas variables de calidad.
> >   - Motivación interna: Sentir orgullo por mantener un proceso técnico limpio, estandarizado y
> >     libre del trabajo "artesanal".
> >   - Motivación externa: Reducir los errores humanos derivados de copiar, pegar y modificar
> >     filas en múltiples archivos de Excel y CSV.
> > - **Meta 2:** Eliminar las modificaciones manuales de consultas (queries) y configuraciones
> >   temporales.
> >   - Motivación interna: Tranquilidad al no depender de configuraciones "quemadas" o ajustes
> >     complejos que aumentan el riesgo de equivocarse.
> >   - Motivación externa: Disminuir la tasa de alertas falsas generadas en SIMEM causadas por
> >     queries desactualizados.
> > - **Meta 3:** Contar con visibilidad completa del historial de incidentes y métricas de
> >   calidad.
> >   - Motivación interna: Sentir respaldo y confianza en sus decisiones técnicas basadas en datos
> >     empíricos de evolución de inconsistencias.
> >   - Motivación externa: Demostrar con indicadores claros (porcentaje de calidad, tiempos de
> >     resolución) la mejora continua de la plataforma ante los directivos.

> **Especialista de Monitoreo Multifuente:**
>
> > - **Meta 1:** Consolidar el monitoreo de recargues y ejecuciones en una interfaz única.
> >   - Motivación interna: Reducir drásticamente la sobrecarga cognitiva generada por tener
> >     demasiadas pestañas, archivos y administradores abiertos simultáneamente.
> >   - Motivación externa: Prevenir fallas en la entrega de información, garantizando que no
> >     queden configuraciones temporales olvidadas tras un recargue.
> > - **Meta 2:** Implementar notificaciones inteligentes y resumidas (ej. vía Teams con agentes
> >   IA).
> >   - Motivación interna: Recuperar la capacidad de concentración al no ser interrumpido por
> >     decenas de correos electrónicos aislados que ya ni siquiera revisa completos.
> >   - Motivación externa: Agilizar la comunicación con el equipo de soporte mediante información
> >     sintetizada y lista para generar incidentes accionables.
> > - **Meta 3:** Reejecutar procesos fallidos automáticamente tras intermitencias de la fuente.
> >   - Motivación interna: Proteger su tiempo de descanso (noches y fines de semana) y evitar la
> >     ansiedad de dejar actividades pendientes.
> >   - Motivación externa: Mantener la continuidad y confiabilidad del Data Lake y SIMEM sin
> >     requerir intervención manual constante.

### 1.6 Disgustos y frustraciones

Enumerar qué obstaculiza a la persona, qué le resulta complicado o dónde falla actualmente su
experiencia.

> **Analista de Calidad Operativa:**
>
> > - **Frustración 1:** La información necesaria para resolver un solo incidente está severamente
> >   fragmentada; debe saltar constantemente entre correos, tablas de alertas, el administrador
> >   SIMEM, bases de datos y archivos Excel/CSV.
> > - **Frustración 2:** Perder gran parte de la mañana (de 8:00 a.m. a 11:00 a.m.) lidiando con
> >   tareas repetitivas y revisando falsas alertas provocadas por configuraciones desactualizadas
> >   o queries "quemados".
> > - **Frustración 3:** El proceso manual de investigación es tan demandante que un solo dato
> >   erróneo le consume horas de revisión, impidiéndole dedicar tiempo a tareas de mayor valor
> >   como la creación de informes y visualizaciones.

> **Ingeniero de Configuración y Metadatos:**
>
> > - **Frustración 1:** El proceso de agregar o modificar una variable es completamente
> >   "artesanal"; requiere copiar y pegar filas en un archivo CSV, buscar rutas en el FTP a mano y
> >   configurar parámetros uno a uno.
> > - **Frustración 2:** La necesidad de realizar ajustes manuales frecuentes directamente sobre
> >   los queries SQL (por ejemplo, en Oracle o para históricos), lo cual es complejo, rompe la
> >   estandarización y aumenta el riesgo de cometer errores.
> > - **Frustración 3:** Tener que manipular manualmente los archivos de configuración para
> >   desactivar temporalmente otras variables cuando necesita probar o validar únicamente una.

> **Especialista de Monitoreo Multifuente:**
>
> > - **Frustración 1:** La saturación excesiva de notificaciones por correo electrónico; el
> >   sistema envía tantos mensajes que resulta imposible revisarlos todos, lo que lo lleva a
> >   ignorarlos o leerlos solo de manera aleatoria.
> > - **Frustración 2:** El alto riesgo de error humano al realizar recargues manuales, ya que es
> >   muy fácil olvidar devolver las configuraciones temporales (como los deltas) a su estado
> >   original, obligándolo a conectarse en noches o fines de semana para corregirlo.
> > - **Frustración 3:** El severo agotamiento cognitivo y mental que le produce gestionar
> >   conjuntos de datos multifuente, pues lo obliga a mantener abiertas múltiples ventanas,
> >   pestañas y extracciones hijas simultáneamente sin perder el hilo de lo que está haciendo.

---

## 2. Mapa de experiencia del usuario


## 2.1 Persona y antecedentes del recorrido
* **Persona que protagoniza el recorrido:** Analista de Operación y Calidad de Datos del SIMEM (Perfil experto con alta competencia técnica pero sometido a procesos manuales fragmentados).
* **Cita o frase que resume por qué realiza este recorrido:** "Todo el día estoy enfocado/enfocada en la revisión de la calidad de datos y observando correos en lugar de analizar la información del mercado energético."

## 2.2 Fases

| Fase | Descripción |
| :--- | :--- |
| **1. Inicio de jornada** | Revisión inicial del estado general de las cargas y bandejas de entrada de correos electrónicos para detectar novedades o fallas críticas. |
| **2. Diagnóstico** | Acá se realiza la investigación a nivel detallado de inconsistencias mediante la apertura simultánea de múltiples herramientas, bases de datos y archivos de configuración. |
| **3. Ejecución** | Correcciones manuales debido a mala calidad de datos, backfills, coordinación de ajustes con los equipos de soporte o agentes. |
| **4. Cierre** | Verificación final del estado de los datos, archivo de incidencias y cierre de la jornada con alta fatiga operativa. |

## 2.3 Acciones, problemas y emociones por fase

| Fase | Acciones | Problemas encontrados | Satisfacción del usuario |
| :--- | :--- | :--- | :--- |
| **Inicio de jornada** | Revisar correo electrónico y monitor de ejecuciones. Identificar si falló alguna carga crítica o hay alertas regulatorias pendientes. | Alertas dispersas sin jerarquía. Saturación de correos electrónicos que dificulta la priorización de las actividades propias de los analistas. | Baja |
| **Diagnóstico** | Abrir bases de datos, scripts SQL y archivos CSV locales. Cruzar manualmente datos publicados en SIMEM con las fuentes originales. Investigar si el error es por retraso de la información o por datos corruptos. | Falsas alarmas recurrentes por consultas SQL desactualizadas. Fragmentación de la información en múltiples pantallas y pestañas. Alto desgaste cognitivo y fatiga visual. | Baja |
| **Ejecución** | Modificar manualmente parámetros de delta para realización de backfills de información. Editar archivos CSV de configuración y redactar sentencias SQL a mano. Reportar anomalías a soporte o agentes externos. | Procesos artesanales altamente propensos al error humano. Riesgo crítico de olvidar configuraciones temporales. | Baja |
| **Cierre** | Verificar el estado final de los conjuntos corregidos. Archivar correos y dar por terminada la revisión operativa diaria. | Falta de un historial centralizado de incidentes resueltos. Se encuentra con una sensación constante de gestión reactiva o apagado de incendios. | Media |

## 2.4 Pensamientos y sentimientos

| Fase | Hallazgo |
| :--- | :--- |
| **Inicio de jornada** | Me frustra que no a hora llegó el correo ni voy a abrir el csv... Me siento abrumada. |
| **Diagnóstico** | La información está regada en muchas partes; pierdo tiempo buscando y abriendo varias pestañas. |
| **Ejecución** | El cambio temporal de deltas y archivos de configuración me obliga a recordar que debo revertir configuraciones para que las próximas ejecuciones del proceso no presenten fallos. En ocasiones, me acuerdo de noche o en fines de semana que lo dejé mal. |
| **Cierre** | Quisiera un panel único donde las métricas, alertas e indicadores de calidad estén juntos sin tener que escribir código SQL para poder revisar. |

## 2.5 Hallazgos y oportunidades (opcional)

| Fase | Oportunidad |
| :--- | :--- |
| **Inicio de jornada** | Implementar un sistema de notificaciones inteligentes y priorizadas (con resúmenes ejecutivos automatizados) en lugar de saturar las bandejas de correo con alertas sueltas. |
| **Diagnóstico** | Desarrollar un panel centralizado (Torre de Control o dashboard) con una vista comparativa que cruce automáticamente SIMEM y fuentes de información, eliminando la navegación multifuente. |
| **Ejecución** | Automatizar la gestión de backfills mediante asistentes transaccionales que manejen los deltas de forma segura y reviertan cambios automáticamente, eliminando el error humano. |
| **Cierre** | Integrar un repositorio histórico y un sistema de trazabilidad de incidentes que permita auditar el comportamiento pasado sin depender de registros manuales no centralizados. |

## 3. Declaración del problema

### 3.1 Primer borrador (fórmula base)

> Como **administrador del SIMEM** necesito **monitorear** los errores de calidad de datos antes de que lleguen a los usuarios para poder **garantizar** la integridad de los datos según la ley de transparencia y del derecho de acceso a la información pública nacional.

### 3.2 Iteraciones

El capítulo señala que escribir una buena declaración del problema es un proceso repetitivo y
progresivo. Completar al menos tres iteraciones, aplicando en cada una un criterio de mejora.

- **Iteración 1 — Primer intento:** **Como** administrador del SIMEM, **quiero** garantizar la calidad de los datos que se publican en el sitio **para** dar tranquilidad a los usuarios finales de que el portal es confiable para la toma de decisiones.

- **Iteración 2 — Aplicando “ser específico”:** **Como** administrador del SIMEM **quiero**un monitor de datos del sitio **para prevenir requerimientos constantes y prevenir que se expongan datos incorrectos con los cuales los usuarios tomen decisiones, lo cual conlleva a una falta de confianza en la plataforma y un sobreesfuerzo en analizar manualmente los datos con múltiples herramientas.

  - _¿Es demasiado específica? ¿Ya incluye una solución dentro del problema? Justificar:_ 
  Contiene en sí una posible solución al problema al mencionar el monitor de datos, sin embargo, está enfocada en el problema de negocio detrás. 

- **Iteración 3 — Aplicando “dejar espacio para explorar” y “no asumir una solución”:** **Cómo** administrador del SIMEM, **quiero** garantizar la calidad y oportunidad de los datos que se exponen en el sitio, **para** prevenir que se tomen decisiones en base a datos incorrectos y prevenir el alto flujo de requerimientos de los clientes, lo cual se traduce en una falta de confianza en la plataforma y en un sobreesfuerzo en analizar manualmente los datos. 

  - _Verificar: ¿la necesidad está expresada como verbo (necesidad real) o como sustantivo
    (solución encubierta)?_ 
- **Iteración final — Aplicando “escribir con empatía”: 
**Como** administrador de SIMEM, **quiero** contar con una visión centralizada, clara y oportuna del estado de calidad de los datos y de los conjuntos con retrasos en su publicación,
 **para** detectar y gestionar incidentes de forma proactiva y así evitar requerimientos, reducir el tiempo invertido en investigaciones manuales, prevenir impactos sobre los usuarios y mantener la confianza en la información publicada.


### 3.3 Declaración de posibilidades

A partir de la declaración del problema final, redactar una o más preguntas que orienten la
ideación, con la forma “¿Cómo podríamos...?”.

- **Pregunta base:**
•	¿Cómo podríamos mostrar los errores cuando se presentan y que sean accionables, es decir, el cómo solucionarlos?

•	¿Cómo podríamos mostrar qué versiones de la liquidación del mercado se han subido a la plataforma?

•	¿Cómo podemos mostrar los indicadores de calidad del sitio?

•	¿Cómo podemos mostrar un seguimiento a los errores de calidad en el tiempo?

•	¿Cómo podemos reejecutar un conjunto atrasado? ¿Cómo hacerlo masivo?

•	¿Cómo podemos automatizar el registro de nuevas variables?

•	¿Cómo podemos revertir configuraciones de conjuntos de datos que olvidaron de reconfigurar?

•	¿Cómo facilitar el habilitar/deshabilitar conjuntos durante las pruebas de investigación histórica?

•	¿Cómo mantener las alertas inmediatas (por correo) sin entrar a una plataforma?

•	¿Cómo evitar que queden queries desactualizados?

•	¿Cómo ayudar a saber si una persona ya está revisando una inconsistencia?

•	¿Cómo poder consultar el estado de calidad de una fecha específica para una variable?

•	¿Cómo separar los conjuntos atrasados de los que tienen errores de calidad y de los que tienen errores por ejecución de la misma herramienta?


- **Variante 1 (usando el nombre de la persona en lugar de “usuarios”):** 
•	¿Cómo podríamos ayudar al analista de Calidad Operativa a que vea los errores de calidad de forma más accionable?

•	¿Cómo podríamos ayudar al analista de Calidad Operativa a que encuentre qué versiones de la liquidación del mercado están cargadas y cuáles faltan?

•	¿Cómo podríamos ayudar al analista de Calidad Operativa a ver el seguimiento de los indicadores de calidad en el tiempo?

•	¿Cómo podríamos ayudar a ingeniero de Configuración y Metadatos a automatizar el registro de nuevas variables?

•	¿Cómo podríamos ayudar al analista de Calidad Operativa a saber si un problema de calidad ya fue resuelto o alguien lo está atendiendo?

•	¿Cómo podríamos ayudar al analista de Calidad Operativa a actualizar masivamente los conjuntos atrasados?

•	¿Cómo podríamos ayudar al analista de Calidad Operativa a realizar calidad histórica sin que interfiera con la ejecución diaria? 

•	¿Cómo podríamos ayudar al ingeniero de Configuración y Metadatos a que no queden queries desactualizados o conjuntos con configuraciones atrasadas? 


- **Variante 2 (explorando otro ángulo del mismo problema):** ¿Cómo podríamos **[ ]**?

•	¿Cómo podríamos ayudar a los administradores de SIMEM a identificar rápidamente qué conjuntos presentan errores de calidad o retrasos en la publicación? 

•	¿Cómo podríamos reducir el tiempo y esfuerzo necesario para investigar y resolver incidentes de calidad de datos? 

•	¿Cómo podríamos centralizar la información necesaria para analizar un incidente sin depender de múltiples herramientas y fuentes? 

•	¿Cómo podríamos proporcionar alertas claras y accionables que permitan actuar antes de que los usuarios detecten los problemas? 

•	¿Cómo podríamos mejorar la visibilidad y trazabilidad de los incidentes para evitar esfuerzos duplicados y facilitar su seguimiento?

---

## 4. Investigación competitiva

### 4.1 Definir el objetivo de la investigación

- **Objetivo de la investigación competitiva:** 

> _Ejemplo de guía: ¿buscan entender fortalezas y debilidades de la competencia? ¿buscan
> inspiración para la ideación? ¿buscan auditar características o precios de la competencia?_

- **Técnica(s) seleccionada(s):**
  - [ ] Análisis de fortalezas, oportunidades, debilidades y amenazas
  - [ ] Demostración relámpago
  - [ ] Análisis competitivo

### 4.2 Análisis de fortalezas, oportunidades, debilidades y amenazas (si aplica)

<!-- prettier-ignore -->
| | Factores internos | Factores externos |
| :--- | :--- | :--- |
| **Positivos** | **Fortalezas:** [Escribir aquí] | **Oportunidades:** [Escribir aquí] |
| **Negativos** | **Debilidades:** [Escribir aquí] | **Amenazas:** [Escribir aquí] |

**Ideas de producto derivadas del análisis:**

- **Idea 1:** [Escribir aquí]
- **Idea 2:** [Escribir aquí]

### 4.3 Demostración relámpago (si aplica)

Reunir entre 8 y 10 ejemplos de productos: competidores directos, productos relacionados y
productos inspiradores sin relación directa.

<!-- prettier-ignore -->
| # | Producto o ejemplo | Tipo (competidor/relacionado/inspirador) | Captura de pantalla (adjuntar) | ¿Qué inspira de este ejemplo? |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [Escribir producto] | [Escribir tipo] | [Adjuntar captura] | [Escribir inspiración] |
| 2 | [Escribir producto] | [Escribir tipo] | [Adjuntar captura] | [Escribir inspiración] |

### 4.4 Análisis competitivo (si aplica)

- **Paso 1 — Objetivo del análisis:** [Escribir aquí]
- **Paso 2 — Criterios de comparación establecidos:**
  - Criterio 1: [Escribir aquí]
  - Criterio 2: [Escribir aquí]
  - Criterio 3: [Escribir aquí]

- **Paso 3 — Compañías a analizar (directas e indirectas):**

<!-- prettier-ignore -->
| Compañía | Tipo (directa/indirecta/comparador) | Enlace / acceso | ¿Requiere inicio de sesión? |
| :--- | :--- | :--- | :--- |
| [Escribir compañía] | [Escribir tipo] | [Escribir enlace] | [Sí/No] |

- **Paso 4 — Recolección de datos:**

<!-- prettier-ignore -->
| Compañía | Criterio 1 | Criterio 2 | Criterio 3 | Evidencia (captura/video) |
| :--- | :--- | :--- | :--- | :--- |
| [Escribir compañía] | [Dato] | [Dato] | [Dato] | [Adjuntar evidencia] |

- **Paso 5 — Resumen de resultados:** Redactar aquí las conclusiones y hallazgos clave del
  análisis, con referencia a las evidencias visuales recolectadas.

> [Escribir aquí]

---

## 5. Consolidación del entregable — Paso Definir

Resumen final que integra los resultados de las cuatro secciones anteriores. Este es el entregable
a presentar.

### 5.1 Persona (resumen)

- **Nombre:** [Escribir aquí]
- **Meta principal:** [Escribir aquí]
- **Frustración principal:** [Escribir aquí]

### 5.2 Mapa de experiencia del usuario (resumen)

- **Fases identificadas:** [Escribir aquí]
- **Punto más bajo de satisfacción:** [Escribir aquí]
- **Principal oportunidad detectada:** [Escribir aquí]

### 5.3 Declaración del problema final

**Como** administrador de SIMEM, **quiero** contar con una visión centralizada, clara y oportuna del estado de calidad de los datos y de los conjuntos con retrasos en su publicación,
 **para** detectar y gestionar incidentes de forma proactiva y así evitar requerimientos, reducir el tiempo invertido en investigaciones manuales, prevenir impactos sobre los usuarios y mantener la confianza en la información publicada.

### 5.4 Declaración de posibilidades, final

•	¿Cómo podríamos ayudar a los administradores de SIMEM a identificar rápidamente qué conjuntos presentan errores de calidad o retrasos en la publicación? 

•	¿Cómo podríamos reducir el tiempo y esfuerzo necesario para investigar y resolver incidentes de calidad de datos? 

•	¿Cómo podríamos centralizar la información necesaria para analizar un incidente sin depender de múltiples herramientas y fuentes? 

•	¿Cómo podríamos proporcionar alertas claras y accionables que permitan actuar antes de que los usuarios detecten los problemas? 

•	¿Cómo podríamos mejorar la visibilidad y trazabilidad de los incidentes para evitar esfuerzos duplicados y facilitar su seguimiento?

### 5.5 Hallazgos clave de la investigación competitiva

- **Hallazgo 1:** [Escribir aquí]
- **Hallazgo 2:** [Escribir aquí]
- **Hallazgo 3:** [Escribir aquí]

---

[img_analista_de_calidad_operativa]:
  docs/img/analista_de_calidad_operativa.jpg
  "analista_de_calidad_operativa"
[img_ingeniero_de_configuración_y_metadatos]:
  docs/img/ingeniero_de_configuración_y_metadatos.jpg
  "ingeniero_de_configuración_y_metadatos"
[img_especialista_de_monitoreo_multifuente]:
  docs/img/especialista_de_monitoreo_multifuente.jpg
  "especialista_de_monitoreo_multifuente"
