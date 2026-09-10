---
title: "Entregable 2: Fase de Empatía (IHC)"
author: "_Milena Castaño_ & _Daniela Torres_ & _Sebastian Sanchez_ & _Kevin Hidalgo_"
date: "9 de Septiembre de 2026"
institute: "Universidad Nacional de Colombia, Sede Medellín"
description:
  "En el contexto de Interacción Humano–Computador (IHC), el proceso de empatía corresponde a la
  primera fase del Diseño Centrado en el Usuario (DCU) o del Design Thinking, y su propósito es
  comprender de manera profunda a los usuarios: sus necesidades, comportamientos, motivaciones,
  frustraciones y el contexto en el que interactúan con un sistema o producto. Este entregable del
  proceso de empatía aplicado a un proyecto debe reflejar esa comprensión de forma estructurada,
  clara y sustentada."

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

**Fecha de elaboración:** _2026 Septiembre 07_

**Fecha última modificación:** _2026 Septiembre 07_

---

<h2><center>Tabla de contenido</center></h2>

- [1. Claridad del objetivo](#1-claridad-del-objetivo)
- [2. Descripción del perfil de usuario](#2-descripción-del-perfil-de-usuario)
- [3. Metodología utilizada](#3-metodología-utilizada)
- [4. Análisis y síntesis de la información](#4-análisis-y-síntesis-de-la-información)
- [5. Hallazgos clave (Insights)](#5-hallazgos-clave-insights)
- [6. Implicaciones para el diseño](#6-implicaciones-para-el-diseño)
- [7. Evidencias y documentación](#7-evidencias-y-documentación)
- [8. Conclusión y reflexión](#8-conclusión-y-reflexión)
- [Referencias](#referencias)

---

## 1. Claridad del objetivo

- **Propósito del proceso de empatía y contexto general del proyecto:**
  - [Define con precisión por qué se realizó el estudio y qué se buscaba comprender: ej. mejorar
    experiencia, detectar problemas de accesibilidad, etc.]
  > El proceso de empatía se realizó con el propósito de comprender las necesidades, dificultades,
  > comportamientos y expectativas de los administradores y analistas encargados de la operación de
  > SIMEM, particularmente en las actividades relacionadas con el monitoreo de la calidad,
  > disponibilidad y actualización de los datos publicados en la plataforma.
  >
  > Actualmente, la información asociada al estado de los datos y a las validaciones de calidad se
  > encuentra distribuida en múltiples mecanismos independientes: correos electrónicos, archivos
  > CSV, consultas manuales a las bases de datos de SIMEM, monitor de carga de datos diario y una
  > alerta de conjuntos de datos con publicaciones definidas en plazos regulatorios[^1]. Esta
  > situación genera una experiencia fragmentada que dificulta la identificación temprana de
  > incidentes, el seguimiento de problemas y la priorización de acciones correctivas.
  >
  > A través de este estudio se busca comprender: Cómo identifican actualmente los usuarios los
  > problemas de calidad de datos. Qué información necesitan para investigar y resolver un
  > incidente de calidad. Cuáles son las principales dificultades para monitorear la integridad,
  > completitud y oportunidad de los datos publicados. Qué factores generan retrasos en la
  > detección y resolución de problemas. Cómo debería ser una herramienta centralizada que facilite
  > la supervisión operativa y reduzca la dependencia de procesos manuales.
  >
  > El objetivo final es generar los insumos necesarios para diseñar una aplicación web con enfoque
  > centrado en el usuario, que permita consolidar métricas, alertas, hallazgos e indicadores de
  > calidad de datos en un único punto de consulta, facilitando una gestión más proactiva,
  > eficiente que permita un análisis más concreto y la toma ráida de decisiones frente a los
  > incidentes de calidad, antes de que estos impacten a los consumidores de información de SIMEM.
  > Además, busca reducir la carga operativa que conlleva la atención de requerimientos por parte
  > de los usuarios finales

  <!-- > [@espinosa_empatizar_2026]. -->

---

## 2. Descripción del perfil de usuario

- **Caracterización general:**
  - [Describe a los usuarios estudiados: edad, ocupación, entorno tecnológico, nivel de experiencia
    y objetivos de uso.]
  > Los usuarios involucrados en la operación y monitoreo de SIMEM son profesionales entre 25 y 45
  > años, con formación universitaria o de posgrado en áreas como ingeniería eléctrica, ingeniería
  > física, ingeniería de sistemas, ciencia de datos o disciplinas afines.
  >
  > Sus principales objetivos son:
  >
  > 1. Garantizar la disponibilidad y confiabilidad de los datos publicados.
  > 2. Detectar oportunamente errores e inconsistencias.
  > 3. Investigar causas raíz de incidentes.
  > 4. Realizar seguimiento al estado de las cargas de información.
  > 5. Atención de requerimientos de los usuarios finales.
  > 6. Cumplir con los tiempos regulatorios y operativos establecidos para la publicación de
  >    información, entre otros.

- **Segmentación de usuarios:**
  - [Si aplica, divide a los usuarios en grupos distintos: ej. novatos, expertos, ocasionales.]
  > - **Soporte SIMEM**: Personal con conocimiento técnico avanzado sobre la infraestructura,
  >   cargas de datos, procesos de integración, API's y componentes tecnológicos de la plataforma.
  > - **Analista SIMEM Experto**: Usuarios con amplio conocimiento de las reglas de negocio, la
  >   operación del Mercado de Energía Mayorista y los diferentes conjuntos de datos publicados en
  >   SIMEM.
  > - **Analista SIMEM Novato**: Personal recientemente vinculado al equipo o con experiencia
  >   limitada en la plataforma, que participa en actividades operativas específicas y requiere un
  >   proceso rápido de aprendizaje. Debido a la rotación frecuente de este rol, los usuarios
  >   suelen depender de documentación, acompañamiento y procesos manuales para comprender el
  >   funcionamiento del sistema.

- **Personas o Arquetipos:**
  - [Presenta aquí los perfiles representativos basados en los patrones identificados durante el
    estudio.]
  > A partir de la segmentación y los patrones identificados en el proceso de empatía, se
  > construyeron los siguientes arquetipos enfocados en las dimensiones cognitivas y emocionales de
  > los usuarios frente al monitoreo de SIMEM:
  >
  > **Arquetipo 1: El Analista Experto (Ej. Camilo, 38 años)**
  >
  > - **Contexto:** Ingeniero con amplio conocimiento de las reglas de negocio del Mercado de
  >   Energía Mayorista y la arquitectura de los conjuntos de datos en SIMEM. Lidera la
  >   investigación de incidentes complejos.
  > - **Metas:** Garantizar la total confiabilidad de los datos publicados, cumplir estrictamente
  >   con los plazos regulatorios y resolver incidentes antes de que impacten a los consumidores
  >   finales.
  > - **Frustraciones:** Lidiar con información fragmentada distribuida en correos electrónicos,
  >   archivos CSV y alertas independientes. Siente que la falta de una herramienta centralizada le
  >   hace perder tiempo valioso en tareas operativas manuales.
  > - **Emociones predominantes:** Estrés ante la presión de los plazos regulatorios, frustración
  >   por la carga operativa que requiere cruzar datos manualmente, pero orgullo y satisfacción
  >   cuando logra identificar la causa raíz de un problema complejo.
  > - **Comportamientos:** Revisa múltiples pantallas y fuentes de información de forma simultánea,
  >   realiza consultas manuales a las bases de datos para validar discrepancias y prioriza la
  >   revisión del monitor de carga a primera hora del día.
  >
  > **Arquetipo 2: El Analista Novato / Soporte Operativo (Ej. Manuela, 26 años)**
  >
  > - **Contexto:** Recién vinculada al equipo de operaciones. Al pertenecer a un rol con rotación
  >   frecuente, se encuentra en una curva de aprendizaje acelerada respecto a la infraestructura y
  >   componentes tecnológicos de la plataforma.
  > - **Metas:** Comprender rápidamente el flujo de los datos, realizar el seguimiento diario al
  >   estado de las cargas y atender de manera eficaz los requerimientos y tickets de los usuarios
  >   finales.
  > - **Frustraciones:** Depender excesivamente de la documentación existente o del acompañamiento
  >   de los analistas expertos. Se confunde fácilmente al tener que revisar múltiples mecanismos
  >   independientes de alerta.
  > - **Emociones predominantes:** Inseguridad al tomar decisiones sobre la integridad de un dato,
  >   sensación de estar abrumada por la arquitectura fragmentada del sistema y alivio cuando logra
  >   validar correctamente una carga o resolver un ticket.
  > - **Comportamientos:** Consulta constantemente los manuales, pregunta con frecuencia a sus
  >   compañeros de mayor experiencia para confirmar si una alerta es real o un falso positivo, y
  >   revisa de manera cautelosa y secuencial antes de dar respuesta a un requerimiento.

---

## 3. Metodología utilizada

- **Técnicas empleadas:**

  > **Entrevistas cualitativas y actitudinales**: Se acudió directamente al usuario para recoger
  > relatos, emociones, comportamientos y contextos, buscando comprender el porqué y el cómo de sus
  > acciones. Se utilizaron preguntas abiertas para fomentar la elaboración de respuestas y evitar
  > sesgos. En el guion figuraban las siguientes preguntas núcleo:
  >
  > - "Cuéntame sobre la última vez que tuviste que investigar un incidente complejo de calidad de
  >   datos en SIMEM. ¿Cómo fue el proceso paso a paso?"
  > - "¿Cómo te sientes o qué pasa por tu mente cuando la información para resolver un incidente de calidad está
  >   fragmentada en múltiples correos, alertas en el administrador y archivos de csv?"
  > - "Si la plataforma centralizada fuera perfecta y nunca se te pasara por alto un error de
  >   datos, ¿cómo cambiaría tu día a día y tu nivel de estrés?" (Aplicando la técnica de
  >   storytelling inverso).
  > - "¿Cómo resuelves un error de calidad de datos que llega por el correo electrónico?" (muestra paso a paso)
  > - "¿Cómo configuras una nueva variable en la herramienta de calidad de datos?" (muestra paso a paso)
  > - "¿Qué te gustaría que tuviera una herramienta de calidad de datos centralizada?"
  > - "¿Qué herramientas, aplicaciones o pantallas tienes que abrir y consultar simultáneamente para poder cruzar esa información y entender qué falló?"
  > - "¿En qué momento exacto de tu jornada sientes que el cansancio mental o la fatiga visual empiezan a pasar factura?"
  > - "Si pudieras eliminar una sola tarea manual, repetitiva o de 'apagado de incendios' de tu rutina diaria de validación, ¿cuál elegirías y por qué?"
  > - "Cuando necesitas corregir un dato, ¿cómo es el proceso de interacción con el equipo de soporte y cuánto tiempo suele tardar ese ciclo de retroalimentación?"
  >
  > **Mapeo de Afinidad**: Se utilizó para agrupar las observaciones clave de las entrevistas en
  > temas y patrones consistentes.
  >
  > **Mapas de Empatía y Creación de Personas:** Técnicas de síntesis empleadas para traducir la
  > información dispersa en un retrato emocional que refleja lo que el usuario dice, piensa, hace y
  > siente. Se utilizó la herramienta de [Figma](https://www.figma.com/board/pQEPSOq8GjVXWQMWtwcZKo/Sin-t%C3%ADtulo?node-id=0-1&t=UrgCNLsp4K0MFOkz-1)
  > para este ejercicio.

- **Proceso de aplicación:**
  > El proceso se estructuró siguiendo las buenas prácticas de la investigación cualitativa
  > (directa), dividido en las siguientes fases:
  >
  > - **Participantes y Contexto:** Se seleccionó una muestra cualitativa de 3 participantes que
  >   representan fielmente al público objetivo: Analistas Expertos, Analistas Novatos y personal
  >   de Soporte SIMEM. Las sesiones se llevaron a cabo entre el 2026-09-07 y el 2026-09-10, en un entorno cómodo y
  >   libre de distracciones, en una llamada por Teams para asegurar que el participante pudiera expresarse con tranquilidad.
  > - **Ejecución:** Cada entrevista tuvo una duración aproximada de 20 minutos. Se inició
  >   explicando claramente el propósito del estudio y se solicitó el consentimiento informado para
  >   transcibir la sesión, garantizando la confidencialidad y el anonimato de los datos. El
  >   facilitador utilizó un guion estructurado, pero flexible, prestando especial atención al
  >   silencio y a las preguntas de seguimiento (indagando con "¿por qué?") para descubrir
  >   fricciones no declaradas superficialmente.
  > - **Herramientas y Síntesis:** Se emplearon herramientas de transcripción para capturar con precisión las citas literales de los usuarios. Durante y
  >   después de las sesiones, se tomaron notas inmediatas que luego fueron procesadas en una
  >   pizarra digital [Figma](https://www.figma.com/board/pQEPSOq8GjVXWQMWtwcZKo/Sin-t%C3%ADtulo?node-id=0-1&t=UrgCNLsp4K0MFOkz-1)
  >   mediante el Mapeo de Afinidad. Esta organización de datos permitió construir posteriormente
  >   los arquetipos empáticos presentados en la sección anterior.

- **Justificación metodológica:**
  > La entrevista actitudinal fue seleccionada como método principal debido a que el objetivo fue
  > entender cómo los usuarios experimentan actualmente la gestión de incidentes de calidad dentro
  > de SIMEM. Esta técnica permitió profundizar en aspectos como:
  >
  > Frustraciones durante la búsqueda de información. Dificultades para identificar incidentes
  > críticos y priorizarlos. Necesidades de seguimiento y trazabilidad. Percepciones sobre la
  > efectividad de las herramientas actuales de monitoreo. Expectativas frente a una plataforma
  > centralizada de gestión de calidad de datos.
  >
  > La elección de una metodología también estuvo motivada por las características del equipo de
  > trabajo: un grupo reducido de analistas con amplio conocimiento del proceso. Además, la
  > existencia de una herramienta preliminar de calidad permitió enfocar las conversaciones en la
  > experiencia de uso actual.

---

## 4. Análisis y síntesis de la información

- **Procesamiento de datos:**
  > Para transformar el volumen de datos recopilados en las entrevistas y observaciones en
  > información procesable, se aplicó la técnica de Mapeo de Afinidad. El proceso se estructuró en
  > tres fases metodológicas:
  >
  > 1. **Extracción de observaciones:** Cada intervención y respuesta clave de las entrevistas se
  >    desglosó en notas individuales que contenían hechos, citas literales y comportamientos
  >    observados.
  > 2. **Agrupación temática:** Las notas fueron agrupadas de manera colaborativa buscando
  >    similitudes conceptuales y relacionales, permitiendo aislar temas recurrentes sobre la
  >    operación diaria de SIMEM (tales como fuentes de información, fricciones técnicas, tiempos
  >    de respuesta y dependencia de procesos manuales)
  > 3. **Formulación de declaraciones ("Declaraciones Yo"):** A partir de cada categoría
  >    consolidada, se redactaron premisas en primera persona que reflejan la perspectiva vivencial
  >    de los analistas, sirviendo como puente directo para la construcción de los arquetipos y la
  >    definición de requerimientos

- **Identificación de patrones:**
  > Del análisis sintético de la información emergieron tres patrones y ejes temáticos principales
  > que describen la realidad operativa del monitoreo en SIMEM:
  >
  > - **Fragmentación y sobrecarga cognitiva:** Se identificó como un patrón constante que los
  >   analistas deben alternar entre múltiples canales desconectados (correos, reportes en CSV,
  >   consultas SQL directas y alertas aisladas). Esto genera un esfuerzo cognitivo elevado y un
  >   riesgo latente de pasar por alto incidentes críticos en los plazos establecidos.
  > - **Reactividad frente a proactividad:** Debido a la ausencia de una vista centralizada, la
  >   detección de errores de calidad de datos suele ser reactiva (impulsada por reportes de los
  >   usuarios finales o por la inminencia de un vencimiento regulatorio), limitando la capacidad
  >   de anticipación del equipo.
  > - **Brecha de conocimiento y dependencia de soporte:** Los analistas novatos experimentan una
  >   curva de aprendizaje pronunciada y demandan un alto acompañamiento por parte del personal
  >   experto, debido a que el conocimiento crítico del negocio y de las reglas de validación se
  >   encuentra disperso o no está centralizado en herramientas intuitivas.

- **Representaciones visuales:**

  > Como parte de la síntesis gráfica y conceptual del estudio, se desarrollaron los siguientes
  > artefactos de visualización:
  >
  > - **Diagrama de Afinidad:** Permitió estructurar las observaciones en tres grandes racimos
  >   temáticos (Infraestructura y herramientas actuales, Procesos de validación y control, y
  >   Colaboración y transferencia de conocimiento), facilitando la visualización clara de dónde
  >   ocurren las principales fricciones operativas.
  >   <a href="./diagramaFlujoExcavacionValleReyes.html" target="_blank">Haga clic aquí para abrir
  >   el diagrama de afinidad</a>
  > - **Mapas de Empatía:** Construidos para contrastar lo que los analistas dicen que hacen frente
  >   a lo que realmente piensan, hacen y sienten (por ejemplo, la dualidad entre la calma aparente
  >   en los reportes diarios y la ansiedad oculta ante la auditoría de los plazos regulatorios).
  >   <a href="./diagramaFlujoExcavacionValleReyes.html" target="_blank">Haga clic aquí para abrir
  >   el mapa de empatía</a>
  > - **Mapa del Viaje del Usuario (Journey Map - Monitoreo de Datos):** Trazó cronológicamente la
  >   experiencia del analista desde el inicio de su jornada (revisión de alertas matutinas) hasta
  >   la resolución de un incidente, evidenciando los "picos de frustración" asociados a la
  >   búsqueda manual de información y los "valles de alivio" al momento de certificar una carga
  >   exitosa. <a href="./diagramaFlujoExcavacionValleReyes.html" target="_blank">Haga clic aquí
  >   para abrir el mapa de viaje del usuario</a>

---

## 5. Hallazgos clave (Insights)

- **Descubrimientos principales:**
  - [Enumera los insights obtenidos a partir del análisis.]
  > [Escribe tu respuesta aquí...]
- **Relación con los objetivos:**
  - [Explica cómo estos hallazgos aportan a la comprensión de la experiencia del usuario y se
    alinean al proyecto.]
  > [Escribe tu respuesta aquí...]
- **Puntos fuertes y de mejora:**
  - [Destaca aspectos positivos actuales frente a las dificultades detectadas.]
  > [Escribe tu respuesta aquí...]

---

## 6. Implicaciones para el diseño

- **Criterios y recomendaciones:**
  - [Traduce los hallazgos en requisitos de usabilidad, criterios de diseño o recomendaciones
    concretas.]
  > [Escribe tu respuesta aquí...]
- **Orientación para futuras fases:**
  - [Explica cómo esta información guiará la definición del problema, ideación, prototipado o
    pruebas.]
  > [Escribe tu respuesta aquí...]

---

## 7. Evidencias y documentación

- **Registro del proceso:**
  - [Adjunta o enlaza extractos de entrevistas, fotografías, capturas, fragmentos de observación o
    citas.]
  > [Escribe tu respuesta aquí...]
- **Consideraciones éticas:**
  - [Garantiza y explica cómo se manejó el anonimato y el consentimiento informado de los
    participantes.]
  > [Escribe tu respuesta aquí...]

---

## 8. Conclusión y reflexión

- **Resumen de aprendizajes:**
  - [Sintetiza lo aprendido sobre los usuarios y su interacción con el sistema.]
  > [Escribe tu respuesta aquí...]
- **Limitaciones del proceso:**
  - [Reflexiona sobre posibles sesgos, tamaño de la muestra o limitaciones de las técnicas usadas.]
  > [Escribe tu respuesta aquí...]

## Referencias

<!-- \bibliography -->
<!-- [1]: A. E. Bedoya, «Empatizar». Presentación de clase, Interacción Humano Computador
(3009669), Universidad Nacional de Colombia, Facultad de Minas, Sede Medellín, 2026. -->

[^1]:
    Los conjuntos de datos regulatorios están definidos en la resolución CREG 101 018 del 2022, por
    la cual se crea el Sistema de Información del Mercado de Energía Mayorista, SIMEM. Estos tienen
    fechas exactas en las que se debe publicar la información. En caso contrario pueden existir
    sanciones por incumplimiento de la normatividad.

![dracula][img_dracula]

---
[img_dracula]: docs/img/dracula.png "dracula"