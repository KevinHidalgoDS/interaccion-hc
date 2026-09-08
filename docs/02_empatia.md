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
    > El proceso de empatía se realizó con el propósito de comprender las necesidades, dificultades, comportamientos y expectativas de los administradores y analistas encargados de la operación de SIMEM, particularmente en las actividades relacionadas con el monitoreo de la calidad, disponibilidad y actualización de los datos publicados en la plataforma.

    > Actualmente, la información asociada al estado de los datos y a las validaciones de calidad se encuentra distribuida en múltiples mecanismos independientes: correos electrónicos, archivos CSV, consultas manuales a las bases de datos de SIMEM, monitor de carga de datos diario y una alerta de conjuntos de datos con publicaciones definidas en plazos regulatorios [**[1]**](#regulatorio). Esta situación genera una experiencia fragmentada que dificulta la identificación temprana de incidentes, el seguimiento de problemas y la priorización de acciones correctivas.

    > A través de este estudio se busca comprender:

    > Cómo identifican actualmente los usuarios los problemas de calidad de datos.
    > Qué información necesitan para investigar y resolver un incidente de calidad.
    > Cuáles son las principales dificultades para monitorear la integridad, completitud y oportunidad de los datos publicados.
    > Qué factores generan retrasos en la detección y resolución de problemas.
    > Cómo debería ser una herramienta centralizada que facilite la supervisión operativa y reduzca la dependencia de procesos manuales.

    > El objetivo final es generar los insumos necesarios para diseñar una aplicación web con enfoque centrado en el usuario, que permita consolidar métricas, alertas, hallazgos e indicadores de calidad de datos en un único punto de consulta, facilitando una gestión más proactiva, eficiente que permita un análisis más concreto y la toma ráida de desiciones frente a los incidentes de calidad, antes de que estos impacten a los consumidores de información de SIMEM. Además, busca reducir la carga operativa que conlleva la atención de requerimientos por parte de los usuarios finales. 


---

## 2. Descripción del perfil de usuario

- **Caracterización general:**
  - [Describe a los usuarios estudiados: edad, ocupación, entorno tecnológico, nivel de experiencia
    y objetivos de uso.]
    > Los usuarios involucrados en la operación y monitoreo de SIMEM son profesionales entre 25 y 45 años, con formación universitaria o de posgrado en áreas como ingeniería eléctrica, ingeniería física, ingeniería de sistemas, ciencia de datos o disciplinas afines.

    Sus principales objetivos son:

    > 1. Garantizar la disponibilidad y confiabilidad de los datos publicados.
    > 2. Detectar oportunamente errores e inconsistencias.
    > 3. Investigar causas raíz de incidentes.
    > 4. Realizar seguimiento al estado de las cargas de información.
    > 5. Atención de requierimientos de los usuarios finales.
    > 6. Cumplir con los tiempos regulatorios y operativos establecidos para la publicación de información, entre otros.

- **Segmentación de usuarios:**
  - [Si aplica, divide a los usuarios en grupos distintos: ej. novatos, expertos, ocasionales.]
    > **Soporte SIMEM**: Personal con conocimiento técnico avanzado sobre la infraestructura, cargas de datos, procesos de integración, APIs y componentes tecnológicos de la plataforma.

    > **Analista SIMEM Experto**: Usuarios con amplio conocimiento de las reglas de negocio, la operación del Mercado de Energía Mayorista y los diferentes conjuntos de datos publicados en SIMEM.

    > **Analista SIMEM Novato**:  Personal recientemente vinculado al equipo o con experiencia limitada en la plataforma, que participa en actividades operativas específicas y requiere un proceso rápido de aprendizaje. Debido a la rotación frecuente de este rol, los usuarios suelen depender de documentación, acompañamiento y procesos manuales para comprender el funcionamiento del sistema.

- **Personas o Arquetipos:**
  - [Presenta aquí los perfiles representativos basados en los patrones identificados durante el
    estudio.]
    > [Escribe tu respuesta aquí...]

---

## 3. Metodología utilizada

- **Técnicas empleadas:**
  - [Enumera las técnicas: entrevistas, observación contextual, mapas de empatía, shadowing,
    diarios, cuestionarios, etc.]
    > **Entrevista actitudinal**:
    > Se realizaron entrevistas donde figuraban las siguientes preguntas:
- **Proceso de aplicación:**
  - [Explica cómo y cuándo se realizaron, cantidad de participantes, contexto y herramientas
    utilizadas.]
    > [Escribe tu respuesta aquí...]
- **Justificación metodológica:**
  - [Argumenta por qué se eligieron estos métodos de acuerdo con los objetivos del proyecto.]
    > La entrevista actitudinal fue seleccionada como método principal debido a que el objetivo fue entender cómo los usuarios experimentan actualmente la gestión de incidentes de calidad dentro de SIMEM. Esta técnica permitió profundizar en aspectos como:

    > Frustraciones durante la búsqueda de información.
    > Dificultades para identificar incidentes críticos y priorizarlos.
    > Necesidades de seguimiento y trazabilidad.
    > Percepciones sobre la efectividad de las herramientas actuales de monitoreo.
    > Expectativas frente a una plataforma centralizada de gestión de calidad de datos.

    > La elección de una metodología también estuvo motivada por las características del equipo de trabajo: un grupo reducido de analistas con amplio conocimiento del proceso. Además, la existencia de una herramienta preliminar de calidad permitió enfocar las conversaciones en la experiencia de uso actual.

---

## 4. Análisis y síntesis de la información

- **Procesamiento de datos:**
  - [Explica cómo se organizaron, interpretaron y sintetizaron los datos recolectados.]
    > [Escribe tu respuesta aquí...]
- **Identificación de patrones:**
  - [Describe los comportamientos comunes, necesidades, motivaciones y frustraciones detectadas.]
    > [Escribe tu respuesta aquí...]
- **Representaciones visuales:**
  - [Inserta aquí tus representaciones: mapas de empatía, journey maps o diagramas de afinidad.]
    > [Escribe tu respuesta aquí...]

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

 <a id="regulatorio">[1]</a> Los conjuntos de datos regulatorios están definidos en la resolución CREG 101 018 del 2022, por la cual se crea el Sistema de Información del Mercado de Energía Mayorista, SIMEM. Estos tienen fechas exactas en las que se debe publicar la información. En caso contrario pueden existir sanciones por incumplimiento de la normatividad.

