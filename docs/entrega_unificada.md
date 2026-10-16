---
title: "Entrega unificada: Plataforma de calidad de datos SIMEM (IHC)"
author: "_Milena Castaño_ & _Daniela Torres_ & _Sebastian Sanchez_ & _Kevin Hidalgo_"
date: "14 de Octubre de 2026"
institute: "Universidad Nacional de Colombia, Sede Medellín"
description:
  "Documento consolidado de los entregables 1 a 6 del curso Interacción Humano-Computador:
  caracterización del problema, empatía, definición, ideación y prototipado, evaluación de
  prototipos con MoSCoW y evaluación de usabilidad con usuarios."

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
<h2><center>Plataforma de monitoreo y gestión de la calidad de datos del SIMEM</center></h2>
<h3><center>Entrega unificada — Entregables #1 a #6</center></h3>

<a id="conte"></a>

<hr style="border:2px solid #CC00FF"> </hr>

**Elaborado por:** _Milena Castaño_ & _Daniela Torres_ & _Sebastian Sanchez_ & _Kevin Hidalgo_

**Correos:** _lmcastanoh@unal.edu.co_ & _datorresgom@unal.edu.co_ & _sebsanchezar@unal.edu.co_ &
_kfhidalgoh@unal.edu.co_

**Grupo:** 5

**Fecha de elaboración:** _2026 Septiembre 02_

**Fecha última modificación:** _2026 Octubre 15_

---

<h2><center>Tabla de contenido</center></h2>

- [Parte I. Caracterización del problema](#parte-1)
- [Parte II. Empatía](#parte-2)
- [Parte III. Definición del problema](#parte-3)
- [Parte IV. Ideación, prototipado y evaluación MoSCoW](#parte-4)
- [Parte V. Evaluación de usabilidad](#parte-5)
- [Parte VI. Prototipo final](#parte-6)
- [Referencias bibliográficas](#referencias)

---

<a id="parte-1"></a>

# Parte I. Caracterización del problema

## 1. Descripción del Problema

### Paso 1: Contextualización del problema

**¿Dónde y cuándo ocurre el problema?**

El problema se presenta en el _Sistema de información para el Mercado de Energía Mayorista_
[SIMEM](https://www.simem.co), una plataforma web de datos abiertos que pone a disposición de
usuarios internos y externos información relacionada con el Mercado de Energía Mayorista (_MEM_)
y la operación del Sistema Interconectado Nacional (_SIN_).

La plataforma ofrece acceso a los datos mediante consultas web y una Interfaz de Programación de
Aplicaciones (_API_) pública, la cual es utilizada por diferentes tipos de usuarios para realizar
análisis, desarrollos tecnológicos y procesos de toma de decisiones. La información publicada se
alimenta desde un lago de datos (_dataLake_), que recibe aproximadamente un millón de registros
diarios provenientes de múltiples fuentes de información, incluyendo bases de datos
transaccionales, archivos _Excel_, _API's_ y otros sistemas de la organización. Actualmente, existen
mecanismos para monitorear la ejecución de los procesos de carga hacia el _dataLake_ y hacia
_SIMEM_. Sin embargo, estos controles se enfocan principalmente en verificar la finalización
técnica de los procesos y no en validar integralmente la calidad, completitud, oportunidad,
consistencia y confiabilidad de los datos publicados.

Como consecuencia, pueden presentarse situaciones en las que los datos son cargados exitosamente
desde el punto de vista técnico, pero contienen errores o inconsistencias que pasan
desapercibidos para los administradores de la plataforma. Entre los problemas más frecuentes se
encuentran registros erróneos, valores atípicos, retrasos en las publicaciones y pérdida de
información histórica. En numerosos casos, estas situaciones son identificadas únicamente cuando
los usuarios consumen la información y reportan novedades a través de los canales de atención _CRM_
(Customer Relationship Management o Gestión de Relaciones con el Cliente), generando un aumento
en los requerimientos gestionados por el equipo administrador y afectando la confianza de los
usuarios en la plataforma. Uno de los escenarios más críticos corresponde a la ausencia de
versiones específicas de información que deben publicarse de manera secuencial. Por ejemplo,
algunas variables asociadas a los procesos de liquidación del mercado cuentan con distintas
versiones publicadas en momentos diferentes. Puede ocurrir que la primera versión de una
liquidación (TX1 versión preliminar) sea cargada correctamente, mientras que la versión que sale
2 días después (TX2) no sea incorporada al Data Lake. La recuperación de estas versiones
faltantes representa un reto operativo significativo, ya que en muchos casos las versiones
históricas dejan de estar disponibles en las bases de datos fuente.

Para reconstruirlas es necesario acudir a repositorios alternos, como servidores FTP (File
Transfer Protocol o Protocolo de Transferencia de Archivos), y ejecutar procesos manuales de
búsqueda, validación y cargue, los cuales consumen tiempo, requieren conocimiento especializado y
aumentan el riesgo de errores operativos. Otro problema recurrente está relacionado con la
pérdida de sincronización entre la fecha de publicación esperada y la fecha real de los datos
disponibles. Por ejemplo, existen variables que deben publicar diariamente la información
correspondiente al día inmediatamente anterior, por ejemplo, el precio de bolsa del mercado. Si
por una intermitencia una ejecución no incorpora los datos esperados, el proceso puede continuar
ejecutándose sin errores aparentes, pero publicando información desactualizada. En este
escenario, los administradores observan que las cargas continúan ejecutándose correctamente,
cuando en realidad los usuarios están consultando datos con uno o varios días de retraso. Esta
situación puede mantenerse durante largos períodos sin ser detectada. Esta limitación es aún más
evidente en los conjuntos de datos con actualizaciones esporádicas, ya que actualmente no existe
una vista consolidada que permita conocer la frecuencia esperada de publicación, la última
actualización realizada o la existencia de posibles retrasos e incumplimientos.

Adicionalmente, la plataforma carece de una capa de analítica y visualización _BI_ (Business
Intelligence) que permita monitorear el comportamiento de los datos de forma gráfica e intuitiva.
La información disponible se encuentra principalmente en formatos estructurados, lo que dificulta
la identificación temprana de tendencias inusuales. Como resultado, los responsables de la
plataforma carecen de una visión centralizada y proactiva sobre la calidad y el estado de los
datos publicados, lo que limita su capacidad para detectar problemas antes de que impacten a los
usuarios finales.

**Antecedentes:**

Actualmente, los administradores de la plataforma cuentan con una herramienta desarrollada en
Python para realizar validaciones de consistencia entre los datos de las fuentes originales y los
datos almacenados en el Data Lake de SIMEM. La validación se hace posterior a la carga de
información del sistema, aunque también se puede ejecutar para validar datos históricos a
demanda. La configuración de los conjuntos de datos a evaluar se hace a través de un archivo
`.CSV`. Cuando la herramienta identifica diferencias o inconsistencias durante las validaciones
ejecutadas, genera automáticamente una notificación por correo electrónico dirigida a los
administradores de la plataforma. Adicionalmente, los hallazgos detectados son almacenados en
archivos `.CSV` para su posterior revisión.

Además, el sistema cuenta con metadatos de cada uno de los conjuntos como son: última fecha de
actualización, si la última ejecución fue exitosa o no, qué fechas indexadas se cargaron con cada
ejecución, la fecha indexada máxima disponible, periodicidad (diario, semanal, mensual,
trimestral, semestral, anual), la clasificación (si carga datos del día anterior, de la semana
siguiente, del mes en curso, etc) y la próxima fecha de ejecución programada. Sin embargo, a día
de hoy no existe una plataforma centralizada que permita consolidar los hallazgos, visualizar
tendencias, generar indicadores o medir la evolución de la calidad de los datos a lo largo del
tiempo. Adicionalmente, no se dispone de un catálogo o repositorio estructurado de
inconsistencias que permita clasificarlas según su tipología, impacto, criticidad o causa raíz.
Esto limita la capacidad de identificar patrones recurrentes, priorizar acciones de mejora y
construir una visión global de la calidad de los datos publicados.

**Artículos Académicos:** Como parte del análisis de antecedentes y soluciones existentes en el
ámbito de la calidad de datos, se revisaron los siguientes artículos: **An Intelligent Linked
Data Quality Dashboard** **[1]**. En este trabajo los autores plantean la siguiente pregunta de
investigación: ¿En qué medida un dashboard inteligente, basado en grafos de conocimiento y
análisis de causa raíz, puede ayudar a los usuarios a comprender los problemas de calidad de los
datos, identificar las correcciones necesarias y priorizar las acciones de mejora? Para abordar
esta problemática, en el artículo proponen un dashboard enfocado en facilitar la comprensión y
gestión de los problemas de calidad de datos mediante mecanismos visuales. Las funcionalidades
más relevantes son:

1. Visualización de problemas por métrica: Mecanismos que les permitan evaluar el estado de
   calidad de los datos de forma periódica y sistemática.
2. Indicadores visuales y tableros de control: Necesarios para que los usuarios pueden conocer
   rápidamente el estado de salud de la información.
3. Priorización de hallazgos: El sistema organiza automáticamente los problemas según su impacto
   sobre la calidad del conjunto de datos.
4. Múltiples vistas de análisis: Incluye vistas por recurso y por tipo de problema.
5. Análisis de causa raíz: Servicios que relacionan las métricas, los datos afectados y los
   reportes de errores. A partir de estas relaciones se aplican técnicas de análisis de causa
   raíz para identificar conexiones entre diferentes problemas y determinar su origen común.
6. Caracterización del impacto global de una anomalía: Los defectos encontrados no se muestran de
   forma aislada, sino dentro del contexto de otros problemas relacionados.

**DataLens: ML-Oriented Interactive Tabular Data Quality Dashboard** **[2]**. Este artículo
presenta **DataLens**, una plataforma orientada a la administración de la calidad de datos
mediante un dashboard interactivo. Tiene dos módulos que destacan y que son diferentes al
propuesto por el artículo de Vaidyambath:

1. Módulo de limpieza iterativa con ML: La plataforma incluye un mecanismo de limpieza iterativa,
   capaz de seleccionar automáticamente las herramientas o técnicas de limpieza más apropiadas
   para mejorar la calidad de los datos.
2. Visualización gráfica de inconsistencias: Generación automática de visualizaciones que
   muestran la distribución de errores detectados en el conjunto de datos. Con esto se facilita
   identificar visualmente dónde se concentran los errores y priorizar su corrección.

---

### Paso 2: Identificación de los usuarios afectados

**¿Quiénes son los usuarios principales?**

Los usuarios principales son el personal interno de XM (analistas de datos, ingenieros y
operadores del mercado) encargados de monitorear y velar por la calidad de los datos publicados
en el portal del [SIMEM](https://www.simem.co) (_Sistema de información para el Mercado de Energía
Mayorista_).

**Perfil del usuario:**

- **Conocimiento y experiencia:** Son **usuarios expertos en el dominio** (poseen un alto
  conocimiento técnico del mercado energético y la estructura de los datos) y tienen una alta
  literacidad digital[^literacidad]. Sin embargo, no necesariamente son expertos en la adopción
  de nuevas herramientas de software, por lo que la curva de aprendizaje de la interfaz debe ser
  baja.
- **Frecuencia y contexto de uso:** Son usuarios **intensivos/frecuentes**. Su interacción con el
  sistema es diaria y prolongada. Operan principalmente en entornos de oficina (a menudo con
  configuraciones de múltiples monitores) para poder cruzar e inspeccionar grandes volúmenes de
  información simultáneamente.
- **Carga cognitiva:** Manejan una **alta carga cognitiva**. Su tarea de asegurar la calidad de
  los datos requiere concentración extrema para identificar anomalías, patrones o valores
  atípicos, a menudo bajo restricciones de tiempo crítico antes de la publicación oficial.
- **Accesibilidad y ergonomía:** Debido a las largas jornadas frente a pantallas analizando
  tablas y tableros de control (dashboards), son altamente susceptibles a la fatiga visual y
  motora. Requieren interfaces que prioricen la claridad tipográfica en datos numéricos, alto
  contraste, y atajos de teclado o flujos de trabajo optimizados que minimicen la dependencia de
  clics repetitivos con el ratón.

**¿Cómo interactúan estos usuarios con el sistema?**

Actualmente, la interacción no ocurre en una plataforma centralizada, sino a través de un
ecosistema fragmentado (correo electrónico, hojas de cálculo locales, portal web). El flujo de
tareas principal consiste en la validación y corrección de datos suministrados por los agentes
generadores, enfrentando severas deficiencias de usabilidad: **Flujo de interacción actual y sus
puntos de fricción:**

1. **Notificación pasiva y descontextualizada:** El sistema ETL notifica los errores mediante
   correos electrónicos.
   - Fricción (IHC): **Baja visibilidad del estado del sistema**. El usuario recibe una alerta
     fuera de contexto, sin un enlace directo o interfaz que lo lleve inmediatamente al entorno
     del error para su evaluación.
2. **Comparación manual de datos (Búsqueda a ciegas):** Al carecer de una interfaz de
   contrastación (tipo data diffing), el usuario debe buscar manualmente el dato erróneo cruzando
   la información entregada por el agente con el resultado fallido de la ETL.
   - Fricción (IHC): **Sobrecarga cognitiva y de la memoria de trabajo**. Obligar al usuario a
     recordar o cruzar visualmente datos entre múltiples ventanas o archivos genera fatiga visual
     severa y alta probabilidad de error humano (slips y mistakes).
3. **Corrección mediante "Workarounds" (Soluciones informales):** Para corregir el error, el
   usuario debe extraer el dato, estructurar un archivo CSV de forma manual y redactar un correo
   al equipo de soporte.
   - Fricción (IHC): **Alto Abismo de Ejecución (Gulf of Execution)**[^abismo-ejecucion]. Falta
     de manipulación directa. El usuario sabe qué quiere corregir, pero el sistema no le da la
     herramienta para hacerlo por sí mismo, obligándolo a abandonar su flujo de trabajo y usar
     herramientas de terceros (_Excel/Notepad, Outlook_).
4. **Dependencia de terceros y Feedback Asíncrono:** El equipo de soporte actualiza la base de
   datos y re-ejecuta la ETL. El usuario debe esperar y posteriormente entrar de nuevo al portal
   _SIMEM_ para validar.
   - Fricción (IHC): **Abismo de Evaluación (Gulf of Evaluation)[^abismo-evaluacion] y cuellos
     de botella**. El ciclo de retroalimentación (feedback loop) está roto. El usuario no recibe
     confirmación en tiempo real de su acción, generando tiempos muertos, ansiedad y rompiendo
     por completo la continuidad de la tarea (ruptura del estado de flujo).

---

### Paso 3: Definición de las necesidades no satisfechas

**¿Qué necesitan los usuarios?**

- **Visibilidad del estado de los datos:** Saber si los datos consultados están correctos,
  completos y cumplen con los estándares de calidad definidos por la organización. [3]
- **Agilidad:** No tener que realizar tareas manuales de validación de datos, lo cual permite a
  los usuarios dedicar el tiempo a la extracción del conocimiento que hay en los datos, el valor
  del negocio y la interpretación y generación de _insights_.
- **Alertas proactivas:** Ser notificados de manera automática sobre los errores en los datos,
  permitiendo así saber con seguridad qué usar y qué no.
- **Canales eficientes de comunicación y gestión de errores en el _datalake_:** Al tener la
  calidad de datos centralizada, será más fácil la gestión de _backfills_ para datos faltantes o
  la implementación de controles o flujos automatizados para la carga de información faltante.
- **Fuentes de confianza:** El usuario necesita conocer de primera mano la calidad que tienen los
  datos que está usando, así como la calidad de los procesos de carga de datos desde las fuentes.

**Problemas actuales:**

- **Inexistencia de un centro de control de calidad de datos unificado:** Al no tener una
  herramienta unificada de control de calidad de datos y cargas de información, los usuarios no
  pueden conocer el estado real de la información del _datalake_, lo que genera pérdida de
  confianza en los datos, gestión reactiva en lugar de preventiva, y adicionalmente no hay
  gobernanza de datos o trazabilidad clara de los mismos. [4]
- **Sobrecarga cognitiva por revisión manual:** La inspección de errores de cargas o revisión de
  calidad de datos se convierte en un problema al ser ejecutado de forma manual, ya que se pueden
  presentar problemas de errores por omisión, desgaste de los analistas, falta de enfoque en el
  rol de análisis de información del mercado energético y dependencia de intermediarios. [5]
- **Procesamiento y análisis lento:** En ocasiones, no se pueden analizar los datos completamente
  por la falta de personal operativo que revise la calidad de los datos.
- **Incertidumbre y falta de confianza en los datos:** Al no tener un repositorio centralizado
  que mida la completitud, consistencia, precisión e integridad de la información, se vuelve
  difícil confiar plenamente en la información presentada.

---

### Paso 4: Impacto del problema

**Consecuencias para los usuarios:**

La ausencia de una interfaz centralizada para monitorear la calidad, disponibilidad y estado de
los datos del _datalake_ genera consecuencias directas sobre las actividades realizadas por los
analistas, ingenieros y operadores de _XM_. El impacto no se limita únicamente a aspectos técnicos
relacionados con los datos, sino que también afecta la experiencia de interacción, la eficiencia
operativa y la capacidad de los usuarios para tomar decisiones oportunas.

- Incremento de la carga cognitiva: Los usuarios deben revisar diferentes fuentes de información,
  correos electrónicos, archivos CSV, tablas y resultados de procesos de carga para determinar si
  existe algún problema con los datos. Esta fragmentación obliga al usuario a mantener
  información en su memoria de trabajo y realizar comparaciones manuales, aumentando el esfuerzo
  mental requerido para completar una tarea que podría ser soportada directamente por una
  interfaz.
- Mayor probabilidad de error humano: La revisión manual de grandes cantidades de información
  aumenta la posibilidad de omitir inconsistencias, interpretar incorrectamente un dato o no
  identificar oportunamente un conjunto que no fue actualizado. Esto resulta especialmente
  relevante cuando existen múltiples conjuntos de datos que deben ser supervisados diariamente.
- Reducción de la productividad: Una parte del tiempo de los usuarios debe destinarse a
  localizar, verificar, reportar y hacer seguimiento a errores de calidad o fallos en las cargas.
  En consecuencia, disminuye el tiempo disponible para actividades de mayor valor, como el
  análisis del comportamiento del mercado energético, la identificación de tendencias y la
  generación de conocimiento a partir de los datos.
- Aumento del tiempo para diagnosticar y resolver errores: La ausencia de un monitor que indique
  de manera visual qué conjunto presenta problemas, cuál es la causa, desde cuándo ocurre y cuál
  es su estado de gestión obliga al usuario a investigar manualmente el incidente. Además, cuando
  la solución depende de comunicaciones por correo electrónico y de la intervención de otros
  equipos, el ciclo de resolución se prolonga.
- Pérdida de continuidad en la interacción: El usuario debe cambiar constantemente entre
  herramientas y contextos —por ejemplo, _SIMEM_, archivos locales, correo electrónico y sistemas
  internos— para completar una misma tarea. Desde la perspectiva de Interacción
  Humano-Computador, esta fragmentación interrumpe el flujo de trabajo, aumenta el número de
  acciones necesarias y dificulta mantener el contexto de la actividad.
- Incertidumbre sobre la confiabilidad de los datos: Si el usuario no dispone de indicadores
  visibles sobre completitud, consistencia, precisión, vigencia o estado de carga de un conjunto
  de datos, no puede determinar rápidamente si la información disponible es suficientemente
  confiable para utilizarla. Esto puede provocar que los analistas recurran a fuentes
  alternativas, como archivos `.txt` obtenidos directamente de otros procesos, aunque los datos
  también se encuentren publicados posteriormente en _SIMEM_.
- Frustración y disminución de la confianza en el sistema: Cuando los usuarios detectan
  repetidamente datos faltantes, cargas atrasadas o inconsistencias sin contar con mecanismos
  claros para identificar su causa y seguimiento, se deteriora la percepción de confiabilidad del
  sistema. Como resultado, pueden desarrollarse mecanismos de trabajo alternativos o workarounds
  que reducen aún más la utilización de la plataforma como fuente principal de información.
- Dificultad para priorizar incidentes: Actualmente, la falta de clasificación visual de los
  errores y de indicadores de severidad dificulta distinguir rápidamente entre un problema menor
  y uno que puede afectar de forma importante la disponibilidad o confiabilidad de la
  información. Esto obliga a los usuarios a evaluar manualmente cada situación antes de
  determinar su prioridad.

**Impacto en la organización o contexto**

El problema también tiene repercusiones organizacionales para _XM_, considerando su responsabilidad
en la administración del Mercado de Energía Mayorista y en la disponibilidad de información
utilizada por diferentes actores del sector energético.

- Gestión reactiva de la calidad de datos: Al no existir un centro de monitoreo unificado con
  indicadores, alertas y mecanismos de seguimiento, muchos problemas se gestionan después de ser
  detectados por un usuario. Esto limita la posibilidad de anticiparse a fallos de carga,
  conjuntos atrasados o degradaciones progresivas de la calidad.
- Incremento de los costos operativos: Las actividades manuales de identificación, comunicación,
  corrección, seguimiento y re-ejecución de procesos consumen tiempo de analistas, ingenieros y
  equipos de soporte. Tareas que podrían ser detectadas, clasificadas o incluso corregidas
  automáticamente requieren actualmente intervención humana.
- Dependencia de personas y conocimiento tácito: Parte del procedimiento para identificar y
  solucionar problemas puede depender de la experiencia individual de determinados analistas o
  integrantes del equipo. Esto representa un riesgo operativo debido a que el conocimiento sobre
  qué revisar, cómo interpretar un error o cómo solicitar una corrección puede no encontrarse
  centralizado en el sistema.
- Dificultades de trazabilidad y gobernanza: Sin una plataforma que mantenga el historial de
  errores, versiones, reglas de calidad, acciones realizadas y responsables de cada incidente,
  resulta más difícil reconstruir lo ocurrido con un conjunto de datos y determinar cuándo
  apareció el problema, cómo fue corregido y si volvió a presentarse.
- Riesgo de publicación o utilización de información incompleta: Una carga tardía, incompleta o
  incorrecta puede hacer que determinados conjuntos de datos no estén disponibles en el momento
  esperado. Esto puede afectar los análisis realizados por los equipos internos y por los
  diferentes agentes del sector que dependen de información confiable y oportuna.
- Uso de fuentes alternativas y duplicación de esfuerzos: Cuando los datos disponibles en el
  _datalake_ o en _SIMEM_ no se actualizan oportunamente, algunos usuarios pueden preferir consultar
  archivos `txt` u otras fuentes que se encuentren disponibles con mayor anticipación. Esto genera
  duplicidad de procesos, dificulta establecer una única fuente de verdad y reduce el
  aprovechamiento de la infraestructura de datos existente.
- Menor capacidad para evaluar el desempeño de la calidad de los datos: La inexistencia de
  métricas consolidadas impide responder fácilmente preguntas como qué porcentaje de los
  conjuntos presenta problemas, cuáles son los errores más frecuentes, cuánto tarda su
  resolución, qué fuentes presentan mayores incidencias o cuál ha sido la evolución de la calidad
  de los datos a lo largo del tiempo.

En consecuencia, el problema identificado no consiste únicamente en la existencia de errores
dentro del _datalake_, sino en la dificultad que tienen los usuarios para percibir, comprender,
diagnosticar y gestionar el estado de calidad de los datos mediante las interfaces y herramientas
actuales. Desde la perspectiva de la Interacción Humano-Computador, existe una brecha entre la
información que el sistema posee sobre sus procesos de carga y calidad y la información que
presenta de manera comprensible y accionable al usuario. Por esta razón, una interfaz de
monitoreo de calidad de datos permitiría transformar un proceso actualmente fragmentado y
reactivo en un flujo de trabajo más visible, centralizado y orientado a la toma de decisiones,
facilitando que los usuarios identifiquen anomalías, comprendan su impacto, prioricen incidentes
y hagan seguimiento a su resolución desde un único entorno.

---

### Paso 5: Objetivos del proyecto

**¿Qué se quiere lograr?**

El aplicativo debe ser capaz de responder preguntas como:

- ¿Cuántas inconsistencias se presentan por período?
- ¿Cuáles son las fuentes de datos con mayor cantidad de errores?
- ¿Qué tipos de inconsistencias ocurren con mayor frecuencia y cuándo?
- ¿Cuánto tiempo tarda la resolución de una inconsistencia?
- ¿Cuáles hallazgos ya fueron gestionados y cuáles permanecen pendientes?
- ¿Qué conjuntos están atrasados en las cargas y por cuanto tiempo han estado así?
- ¿Los conjuntos versionados disponen de todas las versiones disponibles?
- ¿Cuál es el porcentaje global de calidad de datos del sitio y por conjunto de datos?
- ¿Cómo puedo ver gráficamente una variable para identificar tendencias?
- Ejemplo: ¿Los vertimientos del embalse ESMERALDA están correctos para el día 2026-09-01 o hay
  errores de calidad?

**Objetivos:**

Diseñar e implementar una plataforma de monitoreo, observabilidad y gestión de calidad de datos
para el **Sistema de Información del Mercado de Energía Mayorista (SIMEM)** que permita detectar
oportunamente anomalías e inconsistencias, facilitar su análisis y seguimiento, y mejorar la
confiabilidad de la información publicada a los usuarios internos y externos. La plataforma debe
contar con las siguientes características:

1. Centralizar la gestión de inconsistencias de calidad de datos
2. Módulo de configuración de nuevos conjuntos de datos a ser evaluados por la herramienta
3. Monitoreo de la oportunidad de publicación de los conjuntos de datos y con posibilidad de
   relanzar masivamente los que estén atrasados.
4. Verificador de la completitud de los conjuntos de datos de la liquidación del mercado de
   energía y si cuentan con todas sus versiones.
5. Implementar indicadores y métricas de calidad de sistema, tanto global como por conjunto de
   datos.
6. Visualizar la evolución de la calidad de los datos en el tiempo, facilitando la identificación
   de tendencias.
7. Caracterizar y clasificar las inconsistencias detectadas, identificando su tipología,
   frecuencia, criticidad, origen e impacto.
8. Proporcionar trazabilidad de los hallazgos.

---

<a id="parte-2"></a>

# Parte II. Empatía

## 1. Claridad del objetivo

**Propósito del proceso de empatía y contexto general del proyecto:**

El proceso de empatía se realizó con el propósito de comprender las necesidades, dificultades,
comportamientos y expectativas de los administradores y analistas encargados de la operación de
SIMEM, particularmente en las actividades relacionadas con el monitoreo de la calidad,
disponibilidad y actualización de los datos publicados en la plataforma.

Actualmente, la información asociada al estado de los datos y a las validaciones de calidad se
encuentra distribuida en múltiples mecanismos independientes: correos electrónicos, archivos
CSV, consultas manuales a las bases de datos de SIMEM, monitor de carga de datos diario y una
alerta de conjuntos de datos con publicaciones definidas en plazos regulatorios[^creg]. Esta
situación genera una experiencia fragmentada que dificulta la identificación temprana de
incidentes, el seguimiento de problemas y la priorización de acciones correctivas.

A través de este estudio se busca comprender: Cómo identifican actualmente los usuarios los
problemas de calidad de datos. Qué información necesitan para investigar y resolver un
incidente de calidad. Cuáles son las principales dificultades para monitorear la integridad,
completitud y oportunidad de los datos publicados. Qué factores generan retrasos en la
detección y resolución de problemas. Cómo debería ser una herramienta centralizada que facilite
la supervisión operativa y reduzca la dependencia de procesos manuales.

El objetivo final es generar los insumos necesarios para diseñar una aplicación web con enfoque
centrado en el usuario, que permita consolidar métricas, alertas, hallazgos e indicadores de
calidad de datos en un único punto de consulta, facilitando una gestión más proactiva,
eficiente que permita un análisis más concreto y la toma rápida de decisiones frente a los
incidentes de calidad, antes de que estos impacten a los consumidores de información de SIMEM.
Además, busca reducir la carga operativa que conlleva la atención de requerimientos por parte
de los usuarios finales.

---

## 2. Descripción del perfil de usuario

**Caracterización general:**

Los usuarios involucrados en la operación y monitoreo de SIMEM son profesionales entre 25 y 45
años, con formación universitaria o de posgrado en áreas como ingeniería eléctrica, ingeniería
física, ingeniería de sistemas, ciencia de datos o disciplinas afines.

Sus principales objetivos son:

1. Garantizar la disponibilidad y confiabilidad de los datos publicados.
2. Detectar oportunamente errores e inconsistencias.
3. Investigar causas raíz de incidentes.
4. Realizar seguimiento al estado de las cargas de información.
5. Atención de requerimientos de los usuarios finales.
6. Cumplir con los tiempos regulatorios y operativos establecidos para la publicación de
   información, entre otros.

**Segmentación de usuarios:**

- **Soporte SIMEM**: Personal con conocimiento técnico avanzado sobre la infraestructura,
  cargas de datos, procesos de integración, API's y componentes tecnológicos de la plataforma.
- **Analista SIMEM Experto**: Usuarios con amplio conocimiento de las reglas de negocio, la
  operación del Mercado de Energía Mayorista y los diferentes conjuntos de datos publicados en
  SIMEM.
- **Analista SIMEM Novato**: Personal recientemente vinculado al equipo o con experiencia
  limitada en la plataforma, que participa en actividades operativas específicas y requiere un
  proceso rápido de aprendizaje. Debido a la rotación frecuente de este rol, los usuarios
  suelen depender de documentación, acompañamiento y procesos manuales para comprender el
  funcionamiento del sistema.

**Personas o Arquetipos:**

A partir de la segmentación y los patrones identificados en el proceso de empatía, se
construyeron los siguientes arquetipos enfocados en las dimensiones cognitivas y emocionales de
los usuarios frente al monitoreo de SIMEM:

**Arquetipo 1: El Analista Experto (Ej. Camilo, 38 años)**

- **Contexto:** Ingeniero con amplio conocimiento de las reglas de negocio del Mercado de
  Energía Mayorista y la arquitectura de los conjuntos de datos en SIMEM. Lidera la
  investigación de incidentes complejos.
- **Metas:** Garantizar la total confiabilidad de los datos publicados, cumplir estrictamente
  con los plazos regulatorios y resolver incidentes antes de que impacten a los consumidores
  finales.
- **Frustraciones:** Lidiar con información fragmentada distribuida en correos electrónicos,
  archivos CSV y alertas independientes. Siente que la falta de una herramienta centralizada le
  hace perder tiempo valioso en tareas operativas manuales.
- **Emociones predominantes:** Estrés ante la presión de los plazos regulatorios, frustración
  por la carga operativa que requiere cruzar datos manualmente, pero orgullo y satisfacción
  cuando logra identificar la causa raíz de un problema complejo.
- **Comportamientos:** Revisa múltiples pantallas y fuentes de información de forma simultánea,
  realiza consultas manuales a las bases de datos para validar discrepancias y prioriza la
  revisión del monitor de carga a primera hora del día.

**Arquetipo 2: El Analista Novato / Soporte Operativo (Ej. Manuela, 26 años)**

- **Contexto:** Recién vinculada al equipo de operaciones. Al pertenecer a un rol con rotación
  frecuente, se encuentra en una curva de aprendizaje acelerada respecto a la infraestructura y
  componentes tecnológicos de la plataforma.
- **Metas:** Comprender rápidamente el flujo de los datos, realizar el seguimiento diario al
  estado de las cargas y atender de manera eficaz los requerimientos y tickets de los usuarios
  finales.
- **Frustraciones:** Depender excesivamente de la documentación existente o del acompañamiento
  de los analistas expertos. Se confunde fácilmente al tener que revisar múltiples mecanismos
  independientes de alerta.
- **Emociones predominantes:** Inseguridad al tomar decisiones sobre la integridad de un dato,
  sensación de estar abrumada por la arquitectura fragmentada del sistema y alivio cuando logra
  validar correctamente una carga.
- **Comportamientos:** Consulta constantemente los manuales, pregunta con frecuencia a sus
  compañeros de mayor experiencia para confirmar si una alerta es real o un falso positivo, y
  revisa de manera cautelosa y secuencial antes de dar respuesta a un requerimiento de un usuario.

---

## 3. Metodología utilizada

**Técnicas empleadas:**

**Entrevistas cualitativas y actitudinales**: Se acudió directamente al usuario para recoger
relatos, emociones, comportamientos y contextos, buscando comprender el porqué y el cómo de sus
acciones. Se utilizaron preguntas abiertas para fomentar la elaboración de respuestas y evitar
sesgos. En el guion figuraban las siguientes preguntas núcleo:

- Cuéntame sobre la última vez que tuviste que investigar un incidente complejo de calidad de
  datos en SIMEM. ¿Cómo fue el proceso paso a paso?
- ¿Cómo te sientes o qué pasa por tu mente cuando la información para resolver un incidente de
  calidad está fragmentada en múltiples correos, alertas en el administrador y archivos de csv?
- Si la plataforma centralizada fuera perfecta y nunca se te pasara por alto un error de
  datos, ¿cómo cambiaría tu día a día y tu nivel de estrés? (Aplicando la técnica de
  storytelling inverso).
- ¿Cómo resuelves un error de calidad de datos que llega por el correo electrónico? (muestra
  paso a paso)
- ¿Cómo configuras una nueva variable en la herramienta de calidad de datos? (muestra paso a
  paso)
- ¿Qué te gustaría que tuviera una herramienta de calidad de datos centralizada?
- ¿Qué herramientas, aplicaciones o pantallas tienes que abrir y consultar simultáneamente para
  poder cruzar esa información y entender qué falló?
- ¿En qué momento exacto de tu jornada sientes que el cansancio mental o la fatiga visual
  empiezan a pasar factura?
- Si pudieras eliminar una sola tarea manual, repetitiva o de 'apagado de incendios' de tu
  rutina diaria de validación, ¿cuál elegirías y por qué?
- Cuando necesitas corregir un dato, ¿cómo es el proceso de interacción con el equipo de
  soporte y cuánto tiempo suele tardar ese ciclo de retroalimentación?

**Mapeo de Afinidad**: Se utilizó para agrupar las observaciones clave de las entrevistas en
temas y patrones consistentes.

**Mapas de Empatía y Creación de Personas:** Técnicas de síntesis empleadas para traducir la
información dispersa en un retrato emocional que refleja lo que el usuario dice, piensa, hace y
siente. Se utilizó la herramienta de Figma para este ejercicio.

**Proceso de aplicación:**

El proceso se estructuró siguiendo las buenas prácticas de la investigación cualitativa
(directa), dividido en las siguientes fases:

- **Participantes y Contexto:** Se seleccionó una muestra cualitativa de 3 participantes que
  representan fielmente al público objetivo: Analistas Expertos, Analistas Novatos y personal
  de Soporte SIMEM. El equipo actualmente se conforma de 4 personas en total. Las sesiones se
  llevaron a cabo entre el 2026-09-08 y el 2026-09-10, en una llamada por Teams de manera
  individual.
- **Ejecución:** Cada entrevista tuvo una duración aproximada de 30 minutos. Se inició
  explicando claramente el propósito del estudio y se solicitó el consentimiento informado para
  transcribir la sesión, garantizando la confidencialidad y el anonimato de los datos. El
  facilitador utilizó un guion estructurado, pero flexible, prestando especial atención al
  silencio y a las preguntas de seguimiento (indagando con "¿por qué?") para descubrir
  fricciones no declaradas superficialmente.
- **Herramientas y Síntesis:** Se emplearon herramientas de transcripción para capturar con
  precisión las citas literales de los usuarios. Durante y después de las sesiones, se tomaron
  notas en una pizarra digital
  [Figma](https://www.figma.com/board/pQEPSOq8GjVXWQMWtwcZKo/02_entrega?node-id=0-1&t=zNVi0B00uq4236BK-1).
  Esta organización de datos permitió construir posteriormente los arquetipos empáticos
  presentados en la sección anterior.

**Justificación metodológica:**

La entrevista actitudinal fue seleccionada como método principal debido a que el objetivo fue
entender cómo los usuarios experimentan actualmente la gestión de incidentes de calidad dentro
de SIMEM. Esta técnica permitió profundizar en aspectos como:

Frustraciones durante la búsqueda de información. Dificultades para identificar incidentes
críticos y priorizarlos. Necesidades de seguimiento y trazabilidad. Percepciones sobre la
efectividad de las herramientas actuales de monitoreo. Expectativas frente a una plataforma
centralizada de gestión de calidad de datos.

La elección de una metodología también estuvo motivada por las características del equipo de
trabajo: un grupo reducido de analistas con amplio conocimiento del proceso. Además, la
existencia de una herramienta preliminar de calidad permitió enfocar las conversaciones en la
experiencia de uso actual.

---

## 4. Análisis y síntesis de la información

**Procesamiento de datos:**

Para transformar el volumen de datos recopilados en las entrevistas y observaciones en
información procesable, se aplicó la técnica de Mapeo de Afinidad. El proceso se estructuró en
tres fases metodológicas:

1. **Extracción de observaciones:** Cada intervención y respuesta clave de las entrevistas se
   desglosó en notas individuales que contenían hechos, citas literales y comportamientos
   observados.
2. **Agrupación temática:** Las notas fueron agrupadas de manera colaborativa buscando
   similitudes conceptuales y relacionales, permitiendo aislar temas recurrentes sobre la
   operación diaria de SIMEM (tales como fuentes de información, fricciones técnicas, tiempos
   de respuesta y dependencia de procesos manuales).
3. **Formulación de declaraciones ("Declaraciones Yo"):** A partir de cada categoría
   consolidada, se redactaron premisas en primera persona que reflejan la perspectiva vivencial
   de los analistas, sirviendo como puente directo para la construcción de los arquetipos y la
   definición de requerimientos.

**Identificación de patrones:**

Del análisis sintético de la información emergieron tres patrones y ejes temáticos principales
que describen la realidad operativa del monitoreo en SIMEM:

- **Fragmentación y sobrecarga cognitiva:** Se identificó como un patrón constante que los
  analistas deben alternar entre múltiples canales desconectados (correos, reportes en CSV,
  consultas SQL directas y alertas aisladas). Esto genera un esfuerzo cognitivo elevado y un
  riesgo latente de pasar por alto incidentes críticos en los plazos establecidos.
- **Reactividad frente a proactividad:** Debido a la ausencia de una vista centralizada, la
  detección de errores de calidad de datos suele ser reactiva (impulsada por reportes de los
  usuarios finales o por la inminencia de un vencimiento regulatorio), limitando la capacidad
  de anticipación del equipo.
- **Brecha de conocimiento y dependencia de soporte:** Los analistas novatos experimentan una
  curva de aprendizaje pronunciada y demandan un alto acompañamiento por parte del personal
  experto, debido a que el conocimiento crítico del negocio y de las reglas de validación se
  encuentra disperso o no está centralizado en herramientas intuitivas.

**Representaciones visuales:**

Como parte de la síntesis gráfica y conceptual del estudio, se desarrollaron los siguientes
artefactos de visualización, disponibles en la pizarra de
[Figma](https://www.figma.com/board/pQEPSOq8GjVXWQMWtwcZKo/02_entrega?node-id=0-1&t=zNVi0B00uq4236BK-1):

- **Mapas de Empatía:** Construidos para contrastar lo que los analistas dicen que hacen frente
  a lo que realmente piensan, hacen y sienten (por ejemplo, la dualidad entre la calma aparente
  en los reportes diarios y la ansiedad oculta ante la auditoría de los plazos regulatorios).
- **Mapa del Viaje del Usuario (Journey Map - Monitoreo de Datos):** Trazó cronológicamente la
  experiencia del analista desde el inicio de su jornada (revisión de alertas matutinas) hasta
  la resolución de un incidente, evidenciando los "picos de frustración" asociados a la
  búsqueda manual de información y los "valles de alivio" al momento de certificar una carga
  exitosa.

---

## 5. Hallazgos clave (Insights)

- **Descubrimientos principales:**
  - **Fragmentación operativa como detonante de fatiga:** La resolución de incidentes obliga a los
    analistas y personas encargadas a alternar sus tareas entre correos electrónicos,
    administradores del SIMEM, bases de datos, archivos CSV locales y scripts en Visual Studio
    Code, lo cual fragmenta la atención y genera un desgaste cognitivo que no se relaciona con las
    tareas propias de los analistas.
  - **Dependencia de la configuración artesanal:** Ajustar las reglas de calidad o dar de alta
    nuevas variables les exige a los analistas la realización de procesos manuales repetitivos
    (como por ejemplo redactar sentencias SQL a mano, copiar filas en CSVs y modificar parámetros
    de delta) lo que introduce un alto riesgo de error humano y olvidos de configuración.
  - **Paradoja del sistema de alertas:** Se observa que aunque los correos electrónicos resultan
    útiles para captar atención inmediata, la cantidad de correos, la saturación y falta de
    contextualización directa (por tener un diseño no amigable con el usuario) provocan que los
    analistas terminen ignorando mensajes completos incluso por semanas o recurriendo a revisiones
    aleatorias por falta de priorización.
  - **Gestión reactiva ante los vacíos de trazabilidad:** La ausencia de un dashboard o panel de
    control unificado impide a los analistas conocer el estado de salud de las cargas en una sola
    pantalla, relegando al equipo a un rol pasivo de "apagado de incendios" frente a las
    inconsistencias del mercado energético.

- **Relación con los objetivos:**
  - Estos hallazgos evidencian que los problemas de calidad de datos en el proceso de análisis de
    datos del portal SIMEM no son solo técnicos, sino que se relacionan con la experiencia del
    usuario y la usabilidad. Estos problemas demuestran la urgencia de centralizar el monitoreo
    para mitigar la sobrecarga cognitiva de los analistas expertos y alinear la plataforma hacia
    una gobernanza de datos preventiva y ágil.

- **Puntos fuertes y de mejora:**
  - **Aspectos positivos:** Se observa un alto dominio técnico del equipo de analistas y un
    profundo conocimiento de la estructura del mercado energético, asimismo, una sólida capacidad
    analítica para rastrear y resolver fallas complejas hasta su causa raíz.
  - **Dificultades detectadas:** Procesos manuales y desconectados entre sí, ausencia de
    automatización para la reejecución de procesos (_backfills_) y fatiga por gestión de
    información en diversas fuentes.
  - **Incertidumbre ante las falsas alertas:** El testimonio del entrevistado 1 evidencia que
    algunas alertas se originan en configuraciones desactualizadas o en cambios de consultas que
    no se reflejan en la herramienta. Esta situación exige que el analista compruebe si el aviso
    corresponde a una inconsistencia real en los datos o a un problema de configuración. Por ello,
    se identifica la necesidad de comprender el origen de las alertas para interpretar su
    relevancia y decidir qué acciones realizar.
  - **Necesidad de contexto y comparación para el diagnóstico:** El entrevistado 2 señala la
    importancia de visualizar el valor publicado en SIMEM junto con el valor registrado en la
    fuente. Este testimonio evidencia que detectar una diferencia no proporciona, por sí solo,
    información suficiente para comprender el problema. El analista necesita conocer los datos
    involucrados y su contexto para distinguir entre valores faltantes, diferencias menores y
    errores que requieren una intervención.

---

## 6. Implicaciones para el diseño

- **Criterios y recomendaciones:**
  - **Centralización de la interfaz (Torre de Control):** Diseño de un panel unificado (tipo
    dashboard o panel de control) el cual consolide métricas de calidad, alertas priorizadas y el
    estado de las cargas en tiempo real donde se eliminen los procesos de navegar por múltiples
    herramientas desconectadas.
  - **Automatización de configuraciones:** Generar asistentes internos o flujos automatizados para
    el alta y modificación de variables y así evitar la edición manual directa de archivos CSV y
    scripts SQL aislados.
  - **Optimización ergonómica y visual:** Priorizar la claridad tipográfica en datos numéricos,
    indicadores visuales de impacto (tipo semáforos) y proveer resúmenes automatizados que reduzcan
    el esfuerzo de los analistas.

- **Orientación para futuras fases:**
  - **Definición del problema e ideación:** Priorizar los flujos automatizados que estén orientados
    a la reducción de tareas repetitivas de configuración y a la visualización centralizada de
    datos y errores frente a los datos fuente.
  - **Prototipado y pruebas:** Desarrollar prototipos amigables con el usuario centrados en el
    panel de control único y evaluar su capacidad para reducir los tiempos de diagnóstico. De esta
    manera, mitigar la fatiga visual de los analistas en sesiones de prueba controladas.
  - **Diferenciación de los tipos de problemas:** Presentar de forma separada el estado de
    actualización de los conjuntos, los resultados de las validaciones de calidad y los errores de
    configuración de la herramienta. Cada categoría deberá contar con etiquetas e indicadores
    visuales claros que permitan reconocer el tipo de incidente, considerando que un conjunto
    atrasado no necesariamente contiene datos incorrectos. Esta distinción busca facilitar la
    interpretación de las alertas y orientar al analista hacia la acción correspondiente.
  - **Detalle contextual de las inconsistencias:** Incorporar una vista de detalle para cada
    alerta que incluya el conjunto de datos afectado, la fecha de los datos evaluados, la regla de
    validación aplicada y una comparación directa entre el valor publicado en SIMEM y el valor
    registrado en la fuente. Las diferencias y los valores faltantes deberán resaltarse de manera
    comprensible, con el propósito de facilitar el diagnóstico y reducir la necesidad de consultar
    múltiples herramientas para entender una misma inconsistencia.

---

## 7. Evidencias y documentación

#### Mapa de empatía y diagrama de afinidad

- Disponible en
  [Figma](https://www.figma.com/board/pQEPSOq8GjVXWQMWtwcZKo/02_entrega?node-id=0-1&t=zNVi0B00uq4236BK-1).

#### Capturas de entrevistas

![Entrevista_1](img/entrevista_1.png)
![Entrevista_2](img/entrevista_2.png)

**Figura 1.** Evidencias de las sesiones de entrevista realizadas con usuarios del proceso.

#### Fragmentos relevantes de las entrevistas

A continuación, se presentan algunas respuestas representativas recopiladas durante las
entrevistas realizadas a los usuarios del proceso.

**👤 Entrevistado 1:**

**¿Cómo te sientes o qué pasa por tu mente cuando la información para resolver un incidente de
calidad está fragmentada en múltiples correos, alertas y archivos?**

"Considero que las herramientas actuales son útiles y me ayudan en el proceso de validación, pero
todavía tienen algunas limitaciones. Me ha pasado que la herramienta genera alertas de
inconsistencias que realmente no corresponden a problemas de calidad de datos. Esto suele ocurrir
cuando se modifican consultas (queries) y esos cambios no se actualizan en la herramienta, cuando
hay errores durante la configuración de nuevas variables o cuando quedan configuraciones
desactualizadas que generan falsas alertas de forma recurrente."

"Para analizar los incidentes normalmente me apoyo tanto en los correos electrónicos como en la
tabla de alertas. Desde mi perspectiva, ambas herramientas se complementan y me permiten tener
una mejor visión de lo que está ocurriendo."

**👤 Entrevistado 2:**

**¿Qué te gustaría que tuviera una herramienta de calidad de datos centralizada?**

Me gustaría que la herramienta me permitiera diferenciar claramente entre los conjuntos que están
atrasados y los conjuntos que realmente tienen errores de calidad. Para mí son problemas
distintos: un conjunto atrasado no necesariamente tiene datos incorrectos, mientras que un error
de calidad implica que existen diferencias frente a la fuente, datos nulos o información
incompleta. Por eso, quisiera poder identificar rápidamente qué tipo de problema tiene cada
conjunto.

También me gustaría poder visualizar los errores de calidad de forma inmediata, sin tener que
revisar múltiples herramientas o fuentes de información. Idealmente, la herramienta debería
mostrarme directamente cuál es el valor publicado en SIMEM y cuál es el valor que existe en la
fuente, para entender rápidamente si la diferencia corresponde a un error, a un dato faltante o a
una inconsistencia menor.

Sería muy útil poder consultar el estado de calidad para una fecha específica. Por ejemplo, hacer
una búsqueda sobre un conjunto de datos para una fecha determinada y verificar fácilmente si la
validación fue exitosa, si presentó errores o si esas inconsistencias ya fueron corregidas
posteriormente.

Otro aspecto importante es tener visibilidad completa sobre las versiones de los datos. Me
gustaría saber si todas las versiones esperadas fueron cargadas, identificar rápidamente
versiones faltantes y responder preguntas como: "¿ayer se cargaron todas las versiones de este
conjunto?" sin tener que hacer investigaciones manuales.

**👤 Entrevistado 3:**

**¿Si pudieras eliminar una sola tarea manual, repetitiva o de "apagado de incendios" de tu
rutina diaria de validación, cuál elegirías y por qué?**

Inicialmente no se me ocurre una única tarea específica que eliminaría, pero sí hay varias
actividades que considero muy manuales y que podrían automatizarse para facilitar el trabajo
diario.

Una de ellas es la configuración de nuevos conjuntos o variables. Actualmente debo registrar
manualmente la información en archivos CSV, crear los archivos SQL necesarios para las
validaciones y realizar varios ajustes de configuración. Son tareas repetitivas que consumen
tiempo y que podrían hacerse de una forma más automatizada.

También me genera una carga importante trabajar con conjuntos multifuente. En esos casos termino
con muchas ventanas y pestañas abiertas al mismo tiempo, revisando diferentes extracciones
relacionadas entre sí. Cuando un conjunto tiene múltiples fuentes y cada una tiene varias
extracciones hijas, el seguimiento se vuelve complejo y requiere mucha concentración para no
perder el contexto de lo que estoy revisando.

Otro aspecto que me gustaría eliminar son las tareas asociadas a los recargues. Frecuentemente
debo modificar temporalmente los deltas para ejecutar una recarga específica y después devolver
esas configuraciones a su estado original. Como normalmente estoy trabajando en varios conjuntos
al mismo tiempo, existe el riesgo de olvidar alguno de esos cambios. De hecho, me ha pasado que
después de llegar a casa recuerdo que dejé una configuración modificada y debo volver a
conectarme para corregirla, incluso en ocasiones durante la noche o los fines de semana que me
acuerdo que la dejé mal configurada.

---

## 8. Conclusión y reflexión

- **Resumen de aprendizajes:**
  - Con el análisis de las entrevistas y demás artefactos, se observó que los operadores del SIMEM
    son usuarios expertos con alta capacidad técnica que están expuestos a un entorno operativo
    muy manual y que debe cumplir altos estándares regulatorios. La interacción actual basada en
    procesos manuales, correos masivos y múltiples pantallas influye directamente en el ritmo de
    trabajo y limita su capacidad para enfocarse en la generación de valor analítico para el
    negocio.

- **Limitaciones del proceso:**
  - Muestra reducida de entrevistas.
  - Mapas de empatía orientados a un rol muy específico dentro de XM.

---

<a id="parte-3"></a>

# Parte III. Definición del problema

Esta fase documenta el paso Definir del proceso de pensamiento de diseño (Design Thinking). A
partir de la investigación de usuarios y la fase de empatía, se consolidan cuatro actividades
clave: la creación de la Persona, el diseño del Mapa de experiencia del usuario, la formulación de
la Declaración del problema y de posibilidades, y el desarrollo de la Investigación competitiva.

## 1. Persona

**De los arquetipos a las personas.** Los arquetipos de la Parte II (Analista Experto y Analista
Novato) agrupaban a los usuarios por nivel de experiencia. En la fase Definir, el mapa de
afinidad se reorganizó según las tareas que más fricción generan, lo que dio origen a tres
personas: el **Analista de Calidad Operativa** reúne la revisión diaria de alertas que comparten
el Analista Experto y el Novato; el **Ingeniero de Configuración y Metadatos** representa la
configuración de variables y reglas que realiza el equipo de Soporte SIMEM; y el **Especialista
de Monitoreo Multifuente** concentra el seguimiento de recargues y conjuntos multifuente. Las
necesidades del perfil novato (curva de aprendizaje baja y menor dependencia de los expertos) se
mantienen como criterio transversal de diseño. En la declaración del problema (sección 3) se usa
el término **administrador de SIMEM** para referirse en conjunto a las tres personas, que son
quienes administran la calidad de los datos publicados.

### 1.1 Insumos previos

- [x] Entrevistas de usuario realizadas
- [x] Mapa de afinidad elaborado
- [x] Declaraciones en primera persona generadas a partir del mapa de afinidad

### 1.2 Nombre y foto

- **Nombre de la persona:** El Analista de Calidad Operativa
- **Foto o ícono representativo:** Foco en verificación diaria de alertas, correos y cruce de datos

  ![analista_de_calidad_operativa](img/analista_de_calidad_operativa.jpg)

- **Nombre de la persona:** El Ingeniero de Configuración y Metadatos
- **Foto o ícono representativo:** Foco en la gestión manual de archivos CSV, parámetros y ajustes
  de queries SQL

  ![ingeniero_de_configuración_y_metadatos](img/ingeniero_de_configuración_y_metadatos.jpg)

- **Nombre de la persona:** Especialista de Monitoreo Multifuente
- **Foto o ícono representativo:** Foco en la supervisión de ejecuciones, Data Lakes, recargues y
  resolución de cuellos de botella

  ![especialista_de_monitoreo_multifuente](img/especialista_de_monitoreo_multifuente.jpg)

### 1.3 Panorama general

**Analista de Calidad Operativa**

<!-- prettier-ignore -->
| Campo | Descripción |
| :--- | :--- |
| Profesión / ocupación | Ingeniero de Datos / Analista de Calidad de Datos |
| Edad | 28 años |
| Intereses / juegos / marcas afines | Intereses: Acampar los fines de semana, asistir a conciertos de música en vivo y festivales, pedir comida a domicilio en días de alta carga laboral. Juegos: Cult of the Lamb, Mario Kart. Marcas afines: Nintendo, Rappi, Domino's Pizza, Cine Colombia. |

**Ingeniero de Configuración y Metadatos**

<!-- prettier-ignore -->
| Campo | Descripción |
| :--- | :--- |
| Profesión / ocupación | Desarrollador Python / Arquitecto Cloud |
| Edad | 32 años |
| Intereses / juegos / marcas afines | Intereses: Motociclismo de aventura y planeación de rutas largas por el país, preparación de café de especialidad con métodos de filtrado, cocina con ingredientes vegetales. Juegos: Videojuegos independientes y simuladores. Marcas afines: Royal Enfield, Microsoft Azure, Victoria (hierro fundido), Supermercado Vaquita. |

**Especialista de Monitoreo Multifuente**

<!-- prettier-ignore -->
| Campo | Descripción |
| :--- | :--- |
| Profesión / ocupación | Científico de Datos / Estudiante de Maestría en Analítica |
| Edad | 30 años |
| Intereses / juegos / marcas afines | Intereses: Senderismo por reservas naturales y cascadas, viajes a pueblos patrimonio, cuidado de plantas de interior y patios. Juegos: Juegos tipo MMO (Albion) y MOBA. Marcas afines: Samsung, Decathlon, Mercado Libre, Frutos & Semillas. |

### 1.4 Antecedentes y biografía

- **Analista de Calidad Operativa:** Disfruta desconectarse acampando o asistiendo a conciertos,
  pero en su día a día sufre de fatiga visual al tener que cruzar manualmente decenas de correos
  con el administrador SIMEM. Su hábito de pedir comida a domicilio refleja su necesidad de
  soluciones rápidas y convenientes, algo de lo que carece su flujo de trabajo actual, donde un
  solo dato erróneo le consume toda la mañana. Busca alertas claras y centralizadas que le eviten
  el desgaste repetitivo de buscar problemas dispersos y le dejen tiempo para tareas de mayor
  valor.
- **Ingeniero de Configuración y Metadatos:** Es un apasionado de las rutas largas en motocicleta
  y la preparación metódica del café de especialidad, actividades que exigen precisión y
  paciencia. En su trabajo, aplica esa misma meticulosidad para configurar manualmente variables
  en archivos Excel/CSV y ajustar queries SQL, pero le frustra profundamente lo "artesanal" y
  propenso a errores que es este proceso. El tener que "apagar incendios" por configuraciones
  desactualizadas le roba energía que preferiría invertir en automatizar procesos y diseñar
  arquitecturas más robustas.
- **Especialista de Monitoreo Multifuente:** Acostumbrado a explorar extensos senderos en la
  naturaleza y a coordinar estrategias complejas en juegos MMO, tiene gran capacidad para manejar
  múltiples frentes a la vez. Sin embargo, en el trabajo, abrir simultáneamente el administrador
  SIMEM, el Data Lake, Visual Studio Code y múltiples pestañas para monitorear recargues le
  genera una sobrecarga cognitiva insostenible. Sueña con agentes inteligentes que sinteticen las
  alertas por Teams, para que el miedo a olvidar una configuración temporal no le quite la
  tranquilidad durante sus fines de semana.

### 1.5 Gustos y metas

**Analista de Calidad Operativa:**

- **Meta 1:** Centralizar la recepción y visualización de alertas en un solo lugar.
  - Motivación interna: Reducir la fatiga visual y el desgaste mental de saltar entre el correo
    electrónico, archivos CSV y el administrador SIMEM.
  - Motivación externa: Disminuir el tiempo de resolución de incidentes y evitar que una alerta
    crítica pase desapercibida por la saturación de correos.
- **Meta 2:** Identificar de un vistazo el origen exacto del fallo (SIMEM, Data Lake o fuente
  original).
  - Motivación interna: Sentir seguridad y control sobre el flujo de trabajo, eliminando la
    incertidumbre de no saber por dónde empezar a buscar.
  - Motivación externa: Reducir las horas de la mañana dedicadas al "apagado de incendios" y
    delegar el problema rápidamente al área responsable.
- **Meta 3:** Transicionar hacia un rol más estratégico y menos operativo.
  - Motivación interna: Satisfacción intelectual al dejar atrás tareas repetitivas y monótonas.
  - Motivación externa: Obtener reconocimiento por generar análisis de mayor valor para el
    negocio, dashboards e informes en lugar de solo auditar datos.

**Ingeniero de Configuración y Metadatos:**

- **Meta 1:** Automatizar el registro y creación de nuevas variables de calidad.
  - Motivación interna: Sentir orgullo por mantener un proceso técnico limpio, estandarizado y
    libre del trabajo "artesanal".
  - Motivación externa: Reducir los errores humanos derivados de copiar, pegar y modificar
    filas en múltiples archivos de Excel y CSV.
- **Meta 2:** Eliminar las modificaciones manuales de consultas (queries) y configuraciones
  temporales.
  - Motivación interna: Tranquilidad al no depender de configuraciones "quemadas" o ajustes
    complejos que aumentan el riesgo de equivocarse.
  - Motivación externa: Disminuir la tasa de alertas falsas generadas en SIMEM causadas por
    queries desactualizados.
- **Meta 3:** Contar con visibilidad completa del historial de incidentes y métricas de
  calidad.
  - Motivación interna: Sentir respaldo y confianza en sus decisiones técnicas basadas en datos
    empíricos de evolución de inconsistencias.
  - Motivación externa: Demostrar con indicadores claros (porcentaje de calidad, tiempos de
    resolución) la mejora continua de la plataforma ante los directivos.

**Especialista de Monitoreo Multifuente:**

- **Meta 1:** Consolidar el monitoreo de recargues y ejecuciones en una interfaz única.
  - Motivación interna: Reducir drásticamente la sobrecarga cognitiva generada por tener
    demasiadas pestañas, archivos y administradores abiertos simultáneamente.
  - Motivación externa: Prevenir fallas en la entrega de información, garantizando que no
    queden configuraciones temporales olvidadas tras un recargue.
- **Meta 2:** Implementar notificaciones inteligentes y resumidas (ej. vía Teams con agentes
  IA).
  - Motivación interna: Recuperar la capacidad de concentración al no ser interrumpido por
    decenas de correos electrónicos aislados que ya ni siquiera revisa completos.
  - Motivación externa: Agilizar la comunicación con el equipo de soporte mediante información
    sintetizada y lista para generar incidentes accionables.
- **Meta 3:** Reejecutar procesos fallidos automáticamente tras intermitencias de la fuente.
  - Motivación interna: Proteger su tiempo de descanso (noches y fines de semana) y evitar la
    ansiedad de dejar actividades pendientes.
  - Motivación externa: Mantener la continuidad y confiabilidad del Data Lake y SIMEM sin
    requerir intervención manual constante.

### 1.6 Disgustos y frustraciones

**Analista de Calidad Operativa:**

- **Frustración 1:** La información necesaria para resolver un solo incidente está severamente
  fragmentada; debe saltar constantemente entre correos, tablas de alertas, el administrador
  SIMEM, bases de datos y archivos Excel/CSV.
- **Frustración 2:** Perder gran parte de la mañana (de 8:00 a.m. a 11:00 a.m.) lidiando con
  tareas repetitivas y revisando falsas alertas provocadas por configuraciones desactualizadas
  o queries "quemados".
- **Frustración 3:** El proceso manual de investigación es tan demandante que un solo dato
  erróneo le consume horas de revisión, impidiéndole dedicar tiempo a tareas de mayor valor
  como la creación de informes y visualizaciones.

**Ingeniero de Configuración y Metadatos:**

- **Frustración 1:** El proceso de agregar o modificar una variable es completamente
  "artesanal"; requiere copiar y pegar filas en un archivo CSV, buscar rutas en el FTP a mano y
  configurar parámetros uno a uno.
- **Frustración 2:** La necesidad de realizar ajustes manuales frecuentes directamente sobre
  los queries SQL (por ejemplo, en Oracle o para históricos), lo cual es complejo, rompe la
  estandarización y aumenta el riesgo de cometer errores.
- **Frustración 3:** Tener que manipular manualmente los archivos de configuración para
  desactivar temporalmente otras variables cuando necesita probar o validar únicamente una.

**Especialista de Monitoreo Multifuente:**

- **Frustración 1:** La saturación excesiva de notificaciones por correo electrónico; el
  sistema envía tantos mensajes que resulta imposible revisarlos todos, lo que lo lleva a
  ignorarlos o leerlos solo de manera aleatoria.
- **Frustración 2:** El alto riesgo de error humano al realizar recargues manuales, ya que es
  muy fácil olvidar devolver las configuraciones temporales (como los deltas) a su estado
  original, obligándolo a conectarse en noches o fines de semana para corregirlo.
- **Frustración 3:** El severo agotamiento cognitivo y mental que le produce gestionar
  conjuntos de datos multifuente, pues lo obliga a mantener abiertas múltiples ventanas,
  pestañas y extracciones hijas simultáneamente sin perder el hilo de lo que está haciendo.

---

## 2. Mapa de experiencia del usuario

### 2.1 Persona y antecedentes del recorrido

- **Persona que protagoniza el recorrido:** El Analista de Calidad Operativa del SIMEM
  (Perfil experto con alta competencia técnica pero sometido a procesos manuales fragmentados).
- **Cita o frase que resume por qué realiza este recorrido:** "Todo el día estoy enfocado/enfocada
  en la revisión de la calidad de datos y observando correos en lugar de analizar la información
  del mercado energético."

### 2.2 Fases

| Fase | Descripción |
| :--- | :--- |
| **1. Inicio de jornada** | Revisión inicial del estado general de las cargas y bandejas de entrada de correos electrónicos para detectar novedades o fallas críticas. |
| **2. Diagnóstico** | Acá se realiza la investigación a nivel detallado de inconsistencias mediante la apertura simultánea de múltiples herramientas, bases de datos y archivos de configuración. |
| **3. Ejecución** | Correcciones manuales debido a mala calidad de datos, backfills, coordinación de ajustes con los equipos de soporte o agentes. |
| **4. Cierre** | Verificación final del estado de los datos, archivo de incidencias y cierre de la jornada con alta fatiga operativa. |

### 2.3 Acciones, problemas y emociones por fase

| Fase | Acciones | Problemas encontrados | Satisfacción del usuario |
| :--- | :--- | :--- | :--- |
| **Inicio de jornada** | Revisar correo electrónico y monitor de ejecuciones. Identificar si falló alguna carga crítica o hay alertas regulatorias pendientes. | Alertas dispersas sin jerarquía. Saturación de correos electrónicos que dificulta la priorización de las actividades propias de los analistas. | Baja |
| **Diagnóstico** | Abrir bases de datos, scripts SQL y archivos CSV locales. Cruzar manualmente datos publicados en SIMEM con las fuentes originales. Investigar si el error es por retraso de la información o por datos corruptos. | Falsas alarmas recurrentes por consultas SQL desactualizadas. Fragmentación de la información en múltiples pantallas y pestañas. Alto desgaste cognitivo y fatiga visual. | Baja |
| **Ejecución** | Modificar manualmente parámetros de delta para realización de backfills de información. Editar archivos CSV de configuración y redactar sentencias SQL a mano. Reportar anomalías a soporte o agentes externos. | Procesos artesanales altamente propensos al error humano. Riesgo crítico de olvidar configuraciones temporales. | Baja |
| **Cierre** | Verificar el estado final de los conjuntos corregidos. Archivar correos y dar por terminada la revisión operativa diaria. | Falta de un historial centralizado de incidentes resueltos. Se encuentra con una sensación constante de gestión reactiva o apagado de incendios. | Media |

### 2.4 Pensamientos y sentimientos

| Fase | Hallazgo |
| :--- | :--- |
| **Inicio de jornada** | Me frustra que no ha llegado el correo ni voy a abrir el csv... Me siento abrumado/abrumada. |
| **Diagnóstico** | La información está regada en muchas partes; pierdo tiempo buscando y abriendo varias pestañas. |
| **Ejecución** | El cambio temporal de deltas y archivos de configuración me obliga a recordar que debo revertir configuraciones para que las próximas ejecuciones del proceso no presenten fallos. En ocasiones, me acuerdo de noche o en fines de semana que lo dejé mal. |
| **Cierre** | Quisiera un panel único donde las métricas, alertas e indicadores de calidad estén juntos sin tener que escribir código SQL para poder revisar. |

### 2.5 Hallazgos y oportunidades

| Fase | Oportunidad |
| :--- | :--- |
| **Inicio de jornada** | Implementar un sistema de notificaciones inteligentes y priorizadas (con resúmenes ejecutivos automatizados) en lugar de saturar las bandejas de correo con alertas sueltas. |
| **Diagnóstico** | Desarrollar un panel centralizado (Torre de Control o dashboard) con una vista comparativa que cruce automáticamente SIMEM y fuentes de información, eliminando la navegación multifuente. |
| **Ejecución** | Automatizar la gestión de backfills mediante asistentes transaccionales que manejen los deltas de forma segura y reviertan cambios automáticamente, eliminando el error humano. |
| **Cierre** | Integrar un repositorio histórico y un sistema de trazabilidad de incidentes que permita auditar el comportamiento pasado sin depender de registros manuales no centralizados. |

---

## 3. Declaración del problema

### 3.1 Primer borrador (fórmula base)

Como **administrador del SIMEM** necesito **monitorear** los errores de calidad de datos antes de
que lleguen a los usuarios para poder **garantizar** la integridad de los datos según la ley de
transparencia y del derecho de acceso a la información pública nacional.

### 3.2 Iteraciones

- **Iteración 1 — Primer intento:** **Como** administrador del SIMEM, **quiero** garantizar la
  calidad de los datos que se publican en el sitio **para** dar tranquilidad a los usuarios finales
  de que el portal es confiable para la toma de decisiones.

- **Iteración 2 — Aplicando "ser específico":** **Como** administrador del SIMEM **quiero** un
  monitor de datos del sitio **para** prevenir requerimientos constantes y prevenir que se expongan
  datos incorrectos con los cuales los usuarios tomen decisiones, lo cual conlleva a una falta de
  confianza en la plataforma y un sobreesfuerzo en analizar manualmente los datos con múltiples
  herramientas.
  - _¿Es demasiado específica? ¿Ya incluye una solución dentro del problema?_ Contiene en sí una
    posible solución al problema al mencionar el monitor de datos, sin embargo, está enfocada en el
    problema de negocio detrás.

- **Iteración 3 — Aplicando "dejar espacio para explorar" y "no asumir una solución":** **Como**
  administrador del SIMEM, **quiero** garantizar la calidad y oportunidad de los datos que se
  exponen en el sitio, **para** prevenir que se tomen decisiones en base a datos incorrectos y
  prevenir el alto flujo de requerimientos de los clientes, lo cual se traduce en una falta de
  confianza en la plataforma y en un sobreesfuerzo en analizar manualmente los datos.

- **Iteración final — Aplicando "escribir con empatía":** **Como** administrador de SIMEM,
  **quiero** contar con una visión centralizada, clara y oportuna del estado de calidad de los
  datos y de los conjuntos con retrasos en su publicación, **para** detectar y gestionar incidentes
  de forma proactiva y así evitar requerimientos, reducir el tiempo invertido en investigaciones
  manuales, prevenir impactos sobre los usuarios y mantener la confianza en la información
  publicada.

### 3.3 Declaración de posibilidades

**Pregunta base:**

- ¿Cómo podríamos mostrar los errores cuando se presentan y que sean accionables, es decir, el
  cómo solucionarlos?
- ¿Cómo podríamos mostrar qué versiones de la liquidación del mercado se han subido a la
  plataforma?
- ¿Cómo podemos mostrar los indicadores de calidad del sitio?
- ¿Cómo podemos mostrar un seguimiento a los errores de calidad en el tiempo?
- ¿Cómo podemos reejecutar un conjunto atrasado? ¿Cómo hacerlo masivo?
- ¿Cómo podemos automatizar el registro de nuevas variables?
- ¿Cómo podemos revertir configuraciones de conjuntos de datos que olvidaron de reconfigurar?
- ¿Cómo facilitar el habilitar/deshabilitar conjuntos durante las pruebas de investigación
  histórica?
- ¿Cómo mantener las alertas inmediatas (por correo) sin entrar a una plataforma?
- ¿Cómo evitar que queden queries desactualizados?
- ¿Cómo ayudar a saber si una persona ya está revisando una inconsistencia?
- ¿Cómo poder consultar el estado de calidad de una fecha específica para una variable?
- ¿Cómo separar los conjuntos atrasados de los que tienen errores de calidad y de los que tienen
  errores por ejecución de la misma herramienta?

**Variante 1 (usando el nombre de la persona en lugar de "usuarios"):**

- ¿Cómo podríamos ayudar al Analista de Calidad Operativa a que vea los errores de calidad de
  forma más accionable?
- ¿Cómo podríamos ayudar al Analista de Calidad Operativa a que encuentre qué versiones de la
  liquidación del mercado están cargadas y cuáles faltan?
- ¿Cómo podríamos ayudar al Analista de Calidad Operativa a ver el seguimiento de los indicadores
  de calidad en el tiempo?
- ¿Cómo podríamos ayudar al Ingeniero de Configuración y Metadatos a automatizar el registro de
  nuevas variables?
- ¿Cómo podríamos ayudar al Analista de Calidad Operativa a saber si un problema de calidad ya fue
  resuelto o alguien lo está atendiendo?
- ¿Cómo podríamos ayudar al Analista de Calidad Operativa a actualizar masivamente los conjuntos
  atrasados?
- ¿Cómo podríamos ayudar al Analista de Calidad Operativa a realizar calidad histórica sin que
  interfiera con la ejecución diaria?
- ¿Cómo podríamos ayudar al Ingeniero de Configuración y Metadatos a que no queden queries
  desactualizados o conjuntos con configuraciones atrasadas?

**Variante 2 (explorando otro ángulo del mismo problema):**

- ¿Cómo podríamos ayudar a los administradores de SIMEM a identificar rápidamente qué conjuntos
  presentan errores de calidad o retrasos en la publicación?
- ¿Cómo podríamos reducir el tiempo y esfuerzo necesario para investigar y resolver incidentes de
  calidad de datos?
- ¿Cómo podríamos centralizar la información necesaria para analizar un incidente sin depender de
  múltiples herramientas y fuentes?
- ¿Cómo podríamos proporcionar alertas claras y accionables que permitan actuar antes de que los
  usuarios detecten los problemas?
- ¿Cómo podríamos mejorar la visibilidad y trazabilidad de los incidentes para evitar esfuerzos
  duplicados y facilitar su seguimiento?

---

## 4. Investigación competitiva

### 4.1 Definir el objetivo de la investigación

- **Objetivo de la investigación competitiva:** Identificar cómo las plataformas de calidad y
  observabilidad de datos resuelven la centralización del estado de los conjuntos, la gestión de
  alertas, la configuración de reglas de validación y el seguimiento de incidentes, con el fin de
  reconocer buenas prácticas, vacíos y oportunidades de diferenciación para un centro de control
  de calidad de datos de SIMEM. Los criterios de comparación se derivan directamente de las
  frustraciones de las tres personas definidas en la sección 1.6.

- **Técnica(s) seleccionada(s):**
  - [x] Análisis de fortalezas, oportunidades, debilidades y amenazas
  - [x] Demostración relámpago
  - [x] Análisis competitivo

_Justificación: el FODA se aplica a la herramienta actual de validación (desarrollada en Python)
frente al mercado; la demostración relámpago busca inspiración para la fase de ideación; y el
análisis competitivo audita, con criterios homogéneos, qué tan bien cubren las soluciones
existentes las necesidades de nuestras personas._

### 4.2 Análisis de fortalezas, oportunidades, debilidades y amenazas

El análisis se realiza sobre la **herramienta actual de validación de calidad de SIMEM** (script
en Python, configurado mediante archivos `.CSV` y con notificaciones por correo), comparándola con
las soluciones identificadas en el mercado.

<!-- prettier-ignore -->
| | Factores internos | Factores externos |
| :--- | :--- | :--- |
| **Positivos** | **Fortalezas:** (1) Ya existe un motor que compara la fuente contra el Data Lake, tanto posterior a la carga como a demanda para históricos. (2) Se dispone de metadatos ricos por conjunto: periodicidad, clasificación, última fecha de actualización, fecha indexada máxima y próxima ejecución programada. (3) Equipo con alto dominio del Mercado de Energía Mayorista y de la estructura de los datos. (4) Conocimiento de necesidades propias del dominio (versiones de liquidación TX1/TX2, plazos regulatorios CREG) que las herramientas genéricas no contemplan. | **Oportunidades:** (1) La organización ya trabaja sobre el ecosistema Microsoft (Azure, Teams), lo que facilita notificaciones resumidas por Teams y el uso de agentes de IA. (2) Existen herramientas de código abierto (Great Expectations, Soda Core) cuyos patrones pueden reutilizarse sin costo de licencia. (3) Las dimensiones estándar de calidad (completitud, consistencia, oportunidad, exactitud) permiten construir indicadores comparables. (4) Reducir los requerimientos que hoy llegan por el CRM al detectar errores antes que el usuario final. |
| **Negativos** | **Debilidades:** (1) Las alertas llegan solo por correo, sin agrupación ni priorización, lo que genera saturación. (2) La configuración de variables es manual (filas en CSV, archivos SQL, parámetros uno a uno). (3) No existe historial consolidado ni indicadores de calidad en el tiempo. (4) No distingue un conjunto **atrasado** de uno **con errores de calidad** ni de un **error de configuración** (falsas alertas). (5) Los recargues requieren modificar deltas a mano y recordar revertirlos. | **Amenazas:** (1) Plataformas comerciales maduras (Monte Carlo, Microsoft Purview) pueden percibirse como alternativa "lista para usar", aunque con costo de licencia y menor ajuste al dominio. (2) Sanciones por incumplimiento de los plazos de publicación definidos por la CREG. (3) Rotación del rol de analista novato, que depende de conocimiento tácito no documentado. (4) Complejidad técnica de los conjuntos multifuente y de las fuentes heterogéneas (Oracle, FTP, Excel, APIs). |

**Ideas de producto derivadas del análisis:**

- **Idea 1 — Torre de control con tres estados diferenciados:** aprovechar los metadatos ya
  existentes para mostrar, en una sola vista, si un conjunto está _atrasado_, si tiene _errores de
  calidad_ o si la alerta proviene de un _error de configuración_ de la herramienta, con indicadores
  tipo semáforo.
- **Idea 2 — Asistente de configuración y recargues seguros:** un formulario guiado para dar de
  alta variables que genere la configuración y el SQL, permita una prueba en seco de una sola
  variable y revierta automáticamente los deltas temporales al terminar un recargue.
- **Idea 3 — Resumen inteligente por Teams:** reemplazar los correos individuales por un resumen
  diario agrupado por conjunto y severidad, con enlace directo al detalle de cada incidente.

### 4.3 Demostración relámpago

**Nota sobre la evidencia visual.** Las plataformas comerciales incluidas (Monte Carlo, Soda,
Microsoft Purview, Azure Data Factory y PagerDuty) exigen cuenta corporativa, licencia o un
despliegue propio, por lo que no fue posible capturar sus interfaces en un entorno productivo.
En esos casos la evidencia es la **documentación oficial del fabricante**, que contiene las
capturas de la función descrita y permite verificar la afirmación de forma independiente. En los
ejemplos de acceso libre se adjunta captura propia. Todas las fuentes fueron consultadas el
**20 de septiembre de 2026**.

<!-- prettier-ignore -->
| # | Producto o ejemplo | Tipo (competidor/relacionado/inspirador) | Evidencia (captura propia o fuente oficial) | ¿Qué inspira de este ejemplo? |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Monte Carlo — vista de incidentes | Competidor | Documentación oficial: <https://docs.getmontecarlo.com/docs/incident-management> | Agrupar varias alertas relacionadas en un solo incidente y mostrar su impacto aguas abajo; aplicable para indicar si el fallo se originó en la fuente, el Data Lake o SIMEM. |
| 2 | Soda Cloud — creación de _checks_ | Competidor | Documentación oficial: <https://docs.soda.io/soda-documentation/soda-v3/use-case-guides/quick-start-end-user> | Reglas de validación declarativas y legibles, creadas desde la interfaz; inspira un asistente para dar de alta variables sin editar CSV. |
| 3 | Great Expectations — _Data Docs_ | Competidor | Documentación oficial: <https://docs.greatexpectations.io/docs/0.18/reference/learn/terms/data_docs/> | Reporte de cada validación con el valor esperado frente al observado; inspira la vista de detalle "valor en la fuente vs. valor publicado en SIMEM". |
| 4 | Microsoft Purview — Data Quality | Competidor | Documentación oficial: <https://learn.microsoft.com/purview/unified-catalog-data-quality> | Puntaje de calidad por activo y por dimensión; inspira el indicador de porcentaje de calidad global y por conjunto de datos. |
| 5 | Azure Data Factory — monitor de ejecuciones | Relacionado | Documentación oficial: <https://learn.microsoft.com/azure/data-factory/monitor-visually> | Listado de ejecuciones con su estado y opción de reejecutar; inspira el relanzamiento masivo de conjuntos atrasados. |
| 6 | Grafana — paneles y reglas de alerta | Relacionado | ![grafana](img/competencia/06_grafana.png) <https://play.grafana.org> | Series de tiempo y silenciamiento de alertas conocidas; inspira la gráfica de evolución de una variable y silenciar falsas alertas ya identificadas. |
| 7 | Atlassian Statuspage | Inspirador | ![statuspage](img/competencia/07_statuspage.png) <https://status.atlassian.com> | Estado por componente con una barra histórica de disponibilidad; inspira un semáforo por conjunto con su historial de cumplimiento de publicación. |
| 8 | PagerDuty — agrupación de alertas | Inspirador | Documentación oficial: <https://support.pagerduty.com/main/docs/alert-grouping> | Deduplicación y agrupación de alertas para reducir ruido; inspira el resumen diario por Teams en lugar de decenas de correos. |
| 9 | GitHub — vista de diferencias (_diff_) | Inspirador | ![github](img/competencia/09_github.png) <https://github.com/KevinHidalgoDS/interaccion-hc/pull/18/files> | Resaltado visual de lo que cambió; inspira la comparación resaltada entre el dato de la fuente y el dato publicado. |

### 4.4 Análisis competitivo

- **Paso 1 — Objetivo del análisis:** Evaluar qué tan bien cubren las plataformas de calidad y
  observabilidad de datos las necesidades de las tres personas (Analista de Calidad Operativa,
  Ingeniero de Configuración y Metadatos, Especialista de Monitoreo Multifuente) para identificar
  qué prácticas adoptar y en qué aspectos puede diferenciarse la solución para SIMEM.
- **Paso 2 — Criterios de comparación establecidos:**
  - **Criterio 1 — Vista centralizada del estado:** existencia de un panel único que diferencie
    conjuntos atrasados de conjuntos con errores de calidad. _(Origen: fragmentación del Analista
    de Calidad y testimonio del Entrevistado 2)._
  - **Criterio 2 — Gestión y contexto de alertas:** agrupación, priorización, detalle del error y
    notificación por canales como Teams. _(Origen: saturación de correos del Especialista de
    Monitoreo)._
  - **Criterio 3 — Configuración de reglas sin edición manual:** alta y modificación de
    validaciones desde la interfaz o de forma declarativa. _(Origen: proceso "artesanal" del
    Ingeniero de Configuración)._
  - **Criterio 4 — Trazabilidad e indicadores:** historial de incidentes y métricas de calidad en
    el tiempo. _(Origen: Meta 3 del Ingeniero de Configuración)._
  - **Criterio 5 — Remediación:** posibilidad de reejecutar cargas o hacer _backfills_ desde la
    misma herramienta. _(Origen: recargues manuales del Especialista de Monitoreo)._

- **Paso 3 — Compañías a analizar (directas e indirectas):**

<!-- prettier-ignore -->
| Compañía | Tipo (directa/indirecta/comparador) | Enlace / acceso | ¿Requiere inicio de sesión? |
| :--- | :--- | :--- | :--- |
| Monte Carlo | Directa | <https://www.montecarlodata.com> | Sí (demo bajo solicitud) |
| Soda | Directa | <https://www.soda.io> | Sí (prueba gratuita) |
| Great Expectations (GX) | Directa | <https://greatexpectations.io> | No (GX Core es de código abierto) |
| Microsoft Purview — Data Quality | Directa | <https://learn.microsoft.com/purview/> | Sí (requiere cuenta de Azure) |
| Azure Data Factory | Indirecta | <https://learn.microsoft.com/azure/data-factory/> | Sí (requiere cuenta de Azure) |
| Grafana | Comparador | <https://play.grafana.org> | No (demo pública) |

- **Paso 4 — Recolección de datos:**

Cada celda se verificó contra la documentación oficial del fabricante consultada el 20 de
septiembre de 2026; la última columna registra la fuente exacta. Aplica la misma nota sobre
evidencia visual de la sección 4.3: solo Grafana ofrece una demo pública que permita captura
propia.

_Leyenda: **Sí** = lo cubre; **Parcial** = lo cubre con limitaciones o requiere desarrollo
adicional; **No** = no lo cubre._

<!-- prettier-ignore -->
| Compañía | C1. Vista centralizada | C2. Alertas con contexto | C3. Configuración sin edición manual | C4. Trazabilidad e indicadores | C5. Remediación | Evidencia (captura/video) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Monte Carlo | Sí — monitores de tabla (frescura y volumen) separados de los monitores de validación de calidad | Sí — agrupa alertas relacionadas en incidentes con dueño y severidad; notifica por Slack/Teams | Parcial — monitores automáticos y de métrica desde la interfaz; las validaciones específicas requieren SQL propio | Sí — historial de incidentes y agrupación por linaje | No — la reejecución ocurre en el orquestador | <https://docs.getmontecarlo.com/docs/monitors-overview> y <https://docs.getmontecarlo.com/docs/incident-management> |
| Soda | Parcial — resultados por conjunto de datos; la frescura es un tipo de _check_ más, no una vista consolidada de atrasos | Sí — notificaciones a Slack/Teams definidas en el acuerdo | Sí — _checks_ declarativos (SodaCL) y creación sin código desde la interfaz | Sí — historial de resultados de los _checks_ | No | <https://docs.soda.io/soda-documentation/soda-v3/use-case-guides/quick-start-end-user> |
| Great Expectations | Parcial — los _Data Docs_ son un reporte por validación, no un panel operativo | Parcial — acciones de notificación configurables en el _Checkpoint_ | Parcial — expectativas definidas en código; GX Cloud agrega interfaz | Parcial — historial de validaciones en los _Data Docs_ | No | <https://docs.greatexpectations.io/docs/0.18/reference/learn/terms/data_docs/> |
| Microsoft Purview | Parcial — puntaje de calidad agregado por activo, producto de datos y dominio; la frescura es una de las seis dimensiones, no una vista de atrasos | Parcial — alertas por correo o grupo de distribución al incumplir el umbral de calidad; sin agrupación en incidentes ni envío nativo a Teams | Sí — reglas predefinidas, personalizadas y generadas con IA, sin código o con poco código | Sí — puntajes de calidad en el tiempo e historial de ejecuciones | No — el Centro de acciones sugiere la corrección, pero no reejecuta la carga | <https://learn.microsoft.com/purview/unified-catalog-data-quality> |
| Azure Data Factory | Parcial — solo estado técnico de la ejecución, no calidad del dato | Parcial — reglas de alerta por métrica con notificación por correo, SMS o notificación automática mediante Azure Monitor | No aplica | Parcial — historial de ejecuciones y vista Gantt, con retención limitada | Sí — reejecución individual o masiva, y reejecución desde la actividad fallida | <https://learn.microsoft.com/azure/data-factory/monitor-visually> |
| Grafana | Parcial — requiere construir el tablero | Sí — agrupación, silenciamiento y envío a Teams | No | Sí — series de tiempo | No | ![grafana](img/competencia/06_grafana.png) <https://play.grafana.org> |

- **Paso 5 — Resumen de resultados:**

1. **Separar "atrasado" de "erróneo" solo está resuelto a medias:** Monte Carlo es la única
   plataforma revisada que trata la frescura y el volumen como monitores distintos de las
   validaciones de calidad; Soda y Microsoft Purview la incorporan como un _check_ o una
   dimensión más dentro del mismo puntaje, de modo que un conjunto que no llegó y uno que llegó
   con errores se muestran mezclados. Esto valida la necesidad expresada por el Entrevistado 2 y,
   además, ninguna herramienta modela de forma nativa las **versiones de liquidación**
   (TX1, TX2, …) ni los **plazos regulatorios de la CREG**, lo que constituye el principal
   espacio de diferenciación para SIMEM.
2. **La reducción de ruido es tan importante como la detección:** agrupar alertas en
   incidentes, priorizarlas y enviarlas por canales de chat es una práctica común, y responde
   directamente a la saturación de correos que lleva al Especialista de Monitoreo a ignorarlos.
3. **La configuración declarativa o sin código es el estándar:** Soda y Purview permiten crear
   reglas desde la interfaz, lo que respalda la idea de un asistente que elimine la edición
   manual de archivos CSV y SQL del Ingeniero de Configuración.
4. **La remediación está desconectada del monitoreo:** las herramientas de calidad detectan
   pero no reejecutan; la reejecución vive en el orquestador (Azure Data Factory). Integrar el
   relanzamiento masivo en la misma interfaz cerraría el ciclo de retroalimentación roto
   identificado (abismo de evaluación).
5. **Costo y ajuste al dominio:** las soluciones comerciales implican licencias y adaptación a
   fuentes heterogéneas (Oracle, FTP, Excel). Construir sobre la herramienta Python existente,
   adoptando los patrones de interacción observados, resulta una alternativa viable.

---

## 5. Consolidación — Paso Definir

### 5.1 Persona (resumen)

- **Nombre:** El Analista de Calidad Operativa (persona que protagoniza el mapa de experiencia).
- **Meta principal:** Centralizar la recepción y visualización de alertas en un solo lugar e
  identificar de un vistazo el origen exacto del fallo (SIMEM, Data Lake o fuente original).
- **Frustración principal:** La información necesaria para resolver un solo incidente está
  fragmentada entre correos, tablas de alertas, el administrador SIMEM, bases de datos y archivos
  Excel/CSV, lo que le consume buena parte de la mañana en tareas repetitivas y falsas alertas.

### 5.2 Mapa de experiencia del usuario (resumen)

- **Fases identificadas:** Inicio de jornada, Diagnóstico, Ejecución, Cierre.
- **Punto más bajo de satisfacción:** La fase de Diagnóstico y Ejecución, debido a la
  fragmentación de la información en múltiples pantallas y pestañas, las falsas alarmas
  recurrentes por consultas SQL desactualizadas, y el alto desgaste cognitivo y fatiga visual al
  realizar procesos artesanales propensos al error humano.
- **Principal oportunidad detectada:** Desarrollar un panel centralizado (Torre de Control o
  dashboard) que cruce automáticamente las fuentes de información, acompañado de un sistema de
  notificaciones inteligentes y priorizadas, y la automatización de la gestión de backfills para
  eliminar el error humano.

### 5.3 Declaración del problema final

**Como** administrador de SIMEM, **quiero** contar con una visión centralizada, clara y oportuna
del estado de calidad de los datos y de los conjuntos con retrasos en su publicación, **para**
detectar y gestionar incidentes de forma proactiva y así evitar requerimientos, reducir el tiempo
invertido en investigaciones manuales, prevenir impactos sobre los usuarios y mantener la
confianza en la información publicada.

### 5.4 Declaración de posibilidades, final

- ¿Cómo podríamos ayudar a los administradores de SIMEM a identificar rápidamente qué conjuntos
  presentan errores de calidad o retrasos en la publicación?
- ¿Cómo podríamos reducir el tiempo y esfuerzo necesario para investigar y resolver incidentes de
  calidad de datos?
- ¿Cómo podríamos centralizar la información necesaria para analizar un incidente sin depender de
  múltiples herramientas y fuentes?
- ¿Cómo podríamos proporcionar alertas claras y accionables que permitan actuar antes de que los
  usuarios detecten los problemas?
- ¿Cómo podríamos mejorar la visibilidad y trazabilidad de los incidentes para evitar esfuerzos
  duplicados y facilitar su seguimiento?

### 5.5 Hallazgos clave de la investigación competitiva

- **Hallazgo 1 — El mercado no distingue con claridad un dato atrasado de un dato erróneo, y
  ninguna herramienta entiende el dominio regulatorio.** De las seis plataformas comparadas
  (sección 4.4), solo Monte Carlo trata la frescura y el volumen como monitores distintos de las
  validaciones de calidad; Soda y Microsoft Purview las agregan como un _check_ o una dimensión
  más dentro del mismo puntaje. Ninguna modela de forma nativa las versiones de liquidación
  (TX1, TX2, …) ni los plazos de la CREG. Este es el principal espacio de diferenciación para la
  solución de SIMEM: un estado que responda "¿llegó?" y "¿llegó bien?" en el vocabulario del
  negocio eléctrico.
- **Hallazgo 2 — Reducir el ruido vale tanto como detectar el error.** Agrupar alertas
  relacionadas en un solo incidente con dueño y severidad, y notificar por canales de chat en
  lugar de correo, es una práctica común a Monte Carlo, Soda, Grafana y PagerDuty. Responde
  directamente a la saturación de correos que lleva al Especialista de Monitoreo Multifuente a
  ignorarlos, por lo que la solución debe entregar un resumen agrupado por Teams antes que
  notificaciones individuales.
- **Hallazgo 3 — La detección está desconectada de la corrección.** Ninguna de las herramientas
  de calidad revisadas permite reejecutar una carga: esa capacidad vive en el orquestador (Azure
  Data Factory, criterio C5 de la sección 4.4), en una interfaz distinta de la que reporta el
  fallo. Integrar el relanzamiento masivo en el mismo lugar donde se detecta el problema cierra
  el ciclo de retroalimentación roto que se identificó como abismo de
  evaluación, y es una ventaja alcanzable construyendo sobre la herramienta en Python existente.

---

<a id="parte-4"></a>

# Parte IV. Ideación, prototipado y evaluación MoSCoW

Esta fase tiene como objetivo desarrollar la ideación y el prototipado de la herramienta de
monitoreo de la calidad de datos del SIMEM. Durante el proceso se aplicaron las técnicas de
brainstorming, mapa mental y sketching, que permitieron materializar tres prototipos, descritos a
continuación:

| # | Prototipo | Herramienta | Alcance | Enlace |
| :--- | :--- | :--- | :--- | :--- |
| P1 | XM Data Observability | Google AI Studio | 5 módulos | [Abrir](https://ai.studio/apps/c23be026-a328-4074-a049-1c4858f74945) |
| P2 | Torre de Control SIMEM | Artefacto web (Claude) | 7 vistas | [Abrir](https://claude.ai/artifact/NXogD8U3Xhq1nyDqkngWpn) |
| P3 | Monitor de Calidad Datalake SIMEM | Figma Make | 10 pantallas | [Abrir](https://www.figma.com/make/7juxDjDFwWXH6TbzPp9v9J/Monitor-de-Calidad-Datalake-SIMEM?p=f&t=F7gER4RC5Pjejmvl-0) |

Para la generación de los prototipos se tomaron como base los objetivos ya planteados (Parte I, Paso 5), que se presentan a continuación:

| Código | Objetivo |
| :--- | :--- |
| O1 | Centralizar la gestión de inconsistencias |
| O2 | Módulo de configuración de nuevos conjuntos de datos |
| O3 | Monitoreo de la oportunidad de publicación con relanzamiento masivo |
| O4 | Verificador de completitud de versiones de la liquidación (TX1, TX2, …, TXF) |
| O5 | Indicadores y métricas de calidad, globales y por conjunto |
| O6 | Evolución de la calidad en el tiempo y tendencias |
| O7 | Caracterización y clasificación de inconsistencias |
| O8 | Trazabilidad de los hallazgos |

## 1. P1 – Prototipo 1: XM Data Observability (Google AI Studio)

Para el prototipo 1 se elaboró un mapa mental con el tema central de la observabilidad de la
calidad de datos del SIMEM. A un lado se agruparon los problemas, los usuarios y las necesidades
definidos en los entregables anteriores y al otro las soluciones que se concretaron en cinco
módulos: Torre de Control, Monitor de alertas y semáforo, Diff y contrastación, Asistente de
ingesta y Auditoría y logs, además de elementos transversales de navegación. Así se estableció una
relación directa entre cada dolor identificado y la funcionalidad que lo resuelve.

### 1.1 Mapa mental

![P1 – Mapa mental](img/entregable4_5/p1_mapa_mental.png)

### 1.2 Capturas de pantalla del prototipo

**Torre de control**

![P1 – Torre de control](img/entregable4_5/p1_torre_de_control.png)

**Monitor de alertas y semáforo**

![P1 – Monitor de alertas y semáforo](img/entregable4_5/p1_monitor_alertas.png)

**Diff y contrastación**

![P1 – Diff y contrastación](img/entregable4_5/p1_diff_contrastacion.png)

**Asistente de ingesta**

![P1 – Asistente de ingesta](img/entregable4_5/p1_asistente_ingesta.png)

**Auditoría y logs**

![P1 – Auditoría y logs](img/entregable4_5/p1_auditoria_logs.png)

### 1.3 Ventajas y desventajas

| Objetivo | Cobertura | Ventaja | Desventaja |
| :--- | :--- | :--- | :--- |
| O1 Centralizar inconsistencias | Parcial | Las alertas traen causa raíz y el diff aporta contexto para diagnosticar | No hay casos ni responsables; la gestión no queda concentrada en un solo lugar |
| O2 Configurar conjuntos | Total | Asistente de 4 pasos con origen, mapeo de esquema y reglas de calidad | No se identificó prueba en seco ni reversión de cambios |
| O3 Oportunidad y relanzamiento masivo | Parcial | Panel de remediación para relanzar o recuperar | No se identificó relanzamiento masivo ni próxima ejecución |
| O4 Versiones de la liquidación | Parcial | Cuenta regresiva de la ventana TX2 | No hay matriz que muestre qué versiones faltan por día |
| O5 Indicadores de calidad | Parcial | Curva de completitud y anomalías priorizadas | No se identificaron indicadores globales ni por conjunto |
| O6 Evolución en el tiempo | Parcial | Curva de completitud horaria | No se identificó histórico de largo plazo |
| O7 Clasificar inconsistencias | Parcial | Separa tres causas raíz: calidad, atraso y configuración | No hay tipología con frecuencia, criticidad ni impacto |
| O8 Trazabilidad | Total | Registro de auditoría con hash | No se identificó línea de tiempo por incidente |

En general, el prototipo 1 diagnostica el contexto de la situación de forma clara, tiene una
configuración guiada y separa las tres causas de alerta. Sin embargo, tiene poca medición de los
indicadores de calidad, no tiene matriz de versiones y tampoco cuenta con gestión de casos que
apunte directamente al objetivo O1.

## 2. P2 – Prototipo 2: Torre de Control SIMEM (artefacto web Claude)

Para el prototipo 2, se realizó un brainstorming en siete rondas: problemas, usuarios, preguntas,
ideas sueltas, agrupación por afinidad, votación y preguntas abiertas. Las ideas generadas se
agruparon en ocho temas, que se consolidaron en las siete vistas del prototipo. La votación definió lo prioritario:
separar los tipos de problema, una sola pantalla de inicio, incidentes con dueño visible,
comparación entre la fuente y lo publicado, relanzamiento en bloque y reversión de
configuraciones. El resultado fue un prototipo de siete vistas: Torre de Control, Incidentes,
Oportunidad de publicación, Versiones de liquidación, Indicadores, Configuración y Trazabilidad.

### 2.1 Brainstorming

![P2 – Brainstorming (1)](img/entregable4_5/p2_brainstorming_1.png)
![P2 – Brainstorming (2)](img/entregable4_5/p2_brainstorming_2.png)
![P2 – Brainstorming (3)](img/entregable4_5/p2_brainstorming_3.png)
![P2 – Brainstorming (4)](img/entregable4_5/p2_brainstorming_4.png)

### 2.2 Capturas de pantalla del prototipo

**Torre de control**

![P2 – Torre de control (1)](img/entregable4_5/p2_torre_de_control_1.png)
![P2 – Torre de control (2)](img/entregable4_5/p2_torre_de_control_2.png)

**Incidentes (lista y detalle)**

![P2 – Incidentes](img/entregable4_5/p2_incidentes.png)

**Oportunidad de publicación**

![P2 – Oportunidad de publicación](img/entregable4_5/p2_oportunidad_publicacion.jpeg)

**Versiones de liquidación**

![P2 – Versiones de liquidación](img/entregable4_5/p2_versiones_liquidacion.jpeg)

**Indicadores**

![P2 – Indicadores (1)](img/entregable4_5/p2_indicadores_1.jpeg)
![P2 – Indicadores (2)](img/entregable4_5/p2_indicadores_2.png)
![P2 – Indicadores (3)](img/entregable4_5/p2_indicadores_3.png)

**Configuración**

![P2 – Configuración](img/entregable4_5/p2_configuracion.png)

**Trazabilidad**

![P2 – Trazabilidad](img/entregable4_5/p2_trazabilidad.png)

### 2.3 Ventajas y desventajas

| Objetivo | Cobertura | Ventaja | Desventaja |
| :--- | :--- | :--- | :--- |
| O1 Centralizar inconsistencias | Total | Incidentes con responsable visible, fuente vs publicado y acciones sugeridas | No se identificaron SLA por severidad ni escalamiento de incidentes sin dueño |
| O2 Configurar conjuntos | Total | Prueba en seco, reversión de versiones y control de deltas temporales | Falta validar que cubra el alta completa de una variable nueva, como lo hace el asistente de P1 |
| O3 Oportunidad y relanzamiento masivo | Total | Relanzar en bloque y ver la próxima ejecución | No se identificaron reintentos automáticos |
| O4 Versiones de la liquidación | Total | Matriz TX1/TX2/TXF y recuperación de la versión faltante | La recuperación desde FTP depende de una integración real; hoy son datos de ejemplo |
| O5 Indicadores de calidad | Total | Tiempo medio de resolución y porcentaje de falsas alertas | Datos de ejemplo; falta validar el porcentaje de calidad global y por conjunto |
| O6 Evolución en el tiempo | Parcial | Calendario de 30 días, mapa de calor horario y explorador de variable con gráfica de 30 días | No hay tendencias de largo plazo ni comparación entre periodos |
| O7 Clasificar inconsistencias | Parcial | Separa atrasados, calidad y configuración | No hay catálogo con causa raíz, criticidad e impacto |
| O8 Trazabilidad | Total | Línea de tiempo, historial de cambios y bitácora por incidente | No se identificó exportación de evidencia |

El prototipo 2 cubre completamente el ciclo de detección, corrección y medición. Su desventaja más
clara es que no tiene catálogo de inconsistencias.

## 3. P3 – Prototipo 3: Monitor de Calidad Datalake SIMEM (Figma Make)

Para el prototipo 3, se realizó un sketching de seis bocetos que definieron la estructura de la
herramienta: navegación con barra lateral, pantalla de inicio con indicadores y sincronización XM
vs SIMEM, tabla de validación con columna de diferencia, pestañas por periodicidad para los
conjuntos atrasados, matriz de versiones de la liquidación y una plantilla de indicadores y tabla
para las pantallas de gestión. Estas decisiones se llevaron a Figma Make en un prototipo de diez
pantallas.

### 3.1 Sketch

![P3 – Sketch](img/entregable4_5/p3_sketch.png)

### 3.2 Capturas de pantalla del prototipo

**Centro de Situación**

![P3 – Centro de Situación (1)](img/entregable4_5/p3_centro_situacion_1.png)
![P3 – Centro de Situación (2)](img/entregable4_5/p3_centro_situacion_2.png)
![P3 – Centro de Situación (3)](img/entregable4_5/p3_centro_situacion_3.png)

**Validación Fuente vs SIMEM**

![P3 – Validación Fuente vs SIMEM](img/entregable4_5/p3_validacion_fuente_simem.png)

**Conjuntos Atrasados**

![P3 – Conjuntos Atrasados](img/entregable4_5/p3_conjuntos_atrasados.png)

**Versiones de la liquidación**

![P3 – Versiones de la liquidación](img/entregable4_5/p3_versiones_liquidacion.png)

**Validación de Calidad**

![P3 – Validación de Calidad](img/entregable4_5/p3_validacion_calidad.png)

**Auditoría Operativa**

![P3 – Auditoría Operativa](img/entregable4_5/p3_auditoria_operativa.png)

**Configuración de Conjuntos**

![P3 – Configuración de Conjuntos](img/entregable4_5/p3_configuracion_conjuntos.png)

**Credenciales**

![P3 – Credenciales](img/entregable4_5/p3_credenciales.png)

**Métricas SIMEM**

![P3 – Métricas SIMEM](img/entregable4_5/p3_metricas_simem.png)

**Gestión de inconsistencias**

![P3 – Gestión de inconsistencias](img/entregable4_5/p3_gestion_inconsistencias.png)

### 3.3 Ventajas y desventajas

| Objetivo | Cobertura | Ventaja | Desventaja |
| :--- | :--- | :--- | :--- |
| O1 Centralizar inconsistencias | Total | Pantalla de gestión de inconsistencias, validación contra la fuente y exportación de evidencia | La pantalla de casos usa una plantilla de tabla genérica, sin detalle contextual propio |
| O2 Configurar conjuntos | Parcial | Pantalla de configuración con fuente oficial y réplica, y gestión de credenciales | Es una tabla; no hay asistente guiado ni prueba en seco |
| O3 Oportunidad y relanzamiento masivo | Parcial | Atrasados por periodicidad, con contador y columna de próxima ejecución | Falta confirmar que la selección múltiple tenga una acción masiva definida |
| O4 Versiones de la liquidación | Parcial | Matriz de cobertura por día con leyenda de colores | No se identificó una acción para recuperar la versión faltante |
| O5 Indicadores de calidad | Total | KPI en el inicio, calidad global y detalle por regla | La pantalla Métricas SIMEM mide consumo (usuarios API, descargas), no calidad |
| O6 Evolución en el tiempo | Parcial | Evolución histórica, mapa de calor y rankings | Ventana corta (7 días) y sin comparación entre periodos |
| O7 Clasificar inconsistencias | Parcial | Tipo y severidad en los casos y detalle por regla | No hay catálogo ni causa raíz |
| O8 Trazabilidad | Total | Auditoría operativa con pipeline, error, severidad y usuario | Comparte la plantilla genérica; sin línea de tiempo por incidente |

El prototipo 3 tiene la pantalla de inicio más clara, junto con su matriz de versiones y una
navegación clara a través de 10 módulos.

## 4. Evaluación de prototipos (técnica MoSCoW)

### 4.1 Criterios de evaluación

Para la evaluación de cada prototipo, se aplicó la priorización MoSCoW, que clasifica cada
funcionalidad como Must (debe), Should (debería), Could (podría) o Won't (no se incluirá por
ahora). Los criterios se basaron en los ocho objetivos del proyecto, las personas definidas y los
hallazgos de los entregables anteriores, lo que permitió decidir qué funciones incluir y cuáles
dejar fuera.

**Reglas MoSCoW aplicadas**

- **Must (Debe):** sin ella no se resuelve la declaración del problema ni un objetivo explícito.
- **Should (Debería):** reduce de forma clara la carga cognitiva o el ruido, pero el producto
  funciona sin ella.
- **Could (Podría):** mejora la experiencia, sin evidencia directa en entrevistas u objetivos.
- **Won't (No por ahora):** no responde a una necesidad documentada o desvía el alcance.

En las justificaciones, «hallazgo 1», «hallazgo 2» y «hallazgo 3» se refieren a los hallazgos de
la investigación competitiva (Parte III, sección 5.5), y «pregunta de posibilidades 5» a la quinta
pregunta de la declaración de posibilidades final (Parte III, sección 5.4).

### 4.2 P1 – Prototipo 1: XM Data Observability (AI Studio)

#### 4.2.1 Flujo de trabajo

![P1 – Flujo de trabajo](img/entregable4_5/p1_flujo_trabajo.jpeg)

#### 4.2.2 Priorización MoSCoW

| Categoría | Funcionalidad | Justificación |
| :--- | :--- | :--- |
| Must | Torre de Control con estado de pipelines y anomalías priorizadas | Panel centralizado, implicación de diseño principal (O1, O5) |
| Must | Monitor de alertas con 3 causas raíz (calidad, atraso, configuración) | Un conjunto atrasado no es un dato erróneo (O7) |
| Must | Diff SIMEM vs fuente hora a hora con la regla quebrantada | Insight del entrevistado 2: ver valor publicado junto al de la fuente (O1) |
| Must | Panel de remediación (relanzar o recuperar) | Cierra la brecha entre detectar y corregir (hallazgo 3) (O3) |
| Must | Asistente de ingesta de 4 pasos | Elimina CSV y SQL a mano, frustración del Ingeniero de Configuración (O2) |
| Must | Registro de auditoría (quién, qué, cuándo) | Trazabilidad de hallazgos (O8) |
| Should | Cuenta regresiva de la ventana TX2 | Apoya las versiones de liquidación, pero no verifica completitud (O4 parcial) |
| Should | Silenciar alertas | Reduce el ruido (hallazgo 2) |
| Should | Filtros por severidad | Permite priorizar la jornada |
| Should | Mapeo visual de esquema y reglas de calidad en el asistente | Estandariza la creación de variables (O2) |
| Should | Sondeo automático o manual | Evita revisiones aleatorias |
| Could | Curva de completitud horaria | Ayuda a ver tendencias, con alcance limitado (O6) |
| Could | Búsqueda global Ctrl + K y atajos | El perfil pide atajos de teclado para reducir clics repetitivos; no surgió en las entrevistas |
| Could | Modo multi-monitor | Se documenta el uso de varios monitores, pero no es crítico para los objetivos |
| Won't | Verificación de certificado y hash en los logs | Sobreingeniería respecto a los objetivos (O8 se cubre sin ella) |
| Won't | Perfil de usuario | No responde a necesidades documentadas |

**Brechas:** No se identificó catálogo o tipología de inconsistencias (O7), indicadores globales y
por conjunto (O5), matriz de versiones por día (O4) ni resumen por Teams.

Es el prototipo más fuerte en diagnóstico y configuración; es débil en medición, versiones y
comunicación.

### 4.3 P2 – Prototipo 2: Torre de Control SIMEM (artefacto web)

#### 4.3.1 Flujo de trabajo

![P2 – Flujo de trabajo](img/entregable4_5/p2_flujo_trabajo.png)

#### 4.3.2 Priorización MoSCoW

| Categoría | Funcionalidad | Justificación |
| :--- | :--- | :--- |
| Must | Torre con resumen del día y separación atrasados, calidad y configuración | Panel unificado y diferenciación de tipos (O1, O7) |
| Must | Incidentes con responsable visible | Evita esfuerzos duplicados y casos sin dueño (pregunta de posibilidades 5) (O1, O8) |
| Must | Comparación fuente vs publicado dentro del incidente | Detalle contextual, implicación de diseño |
| Must | Relanzar en bloque y próxima ejecución | Objetivo 3 y hallazgo 3 (O3) |
| Must | Matriz de versiones TX1/TX2/TXF y recuperar versión faltante | Escenario más crítico (O4) |
| Must | Configuración con prueba en seco y revertir | Mitiga falsas alertas y el olvido de revertir deltas (O2) |
| Must | Trazabilidad: línea de tiempo e historial de cambios | O8 |
| Should | Indicadores: tiempo medio de resolución y % de falsas alertas | Responde a O5 y a las preguntas del objetivo |
| Should | Resumen diario por Teams y campana | Hallazgo 2: menos correo, más resumen agrupado |
| Should | Calendario de 30 días y mapa de calor horario | Tendencias y horas críticas (O6) |
| Should | Acciones sugeridas por tipo de incidente | Reduce el tiempo de diagnóstico |
| Should | Explorador de variable con gráfica de 30 días | Responde a la pregunta del objetivo "¿cómo puedo ver gráficamente una variable?" (O6) |
| Could | Atajos 1 a 7 y búsqueda Ctrl + K | El perfil pide atajos de teclado; no surgió en las entrevistas |
| Could | Tema claro y oscuro | Fatiga visual |
| Could | Silenciar o posponer alertas con caducidad | Útil con mantenimientos, no es crítico |
| Won't | Predicción de incidentes | Requiere histórico que aún no se tiene |
| Won't | Página pública de estado e integración con tickets | Fuera del alcance del equipo administrador |

**Brechas:** No se identificó un catálogo de inconsistencias con causa raíz y criticidad (O7
completo). El explorador de variable responde a la pregunta del objetivo "¿cómo puedo ver
gráficamente una variable?", pero solo con 30 días de historia. Los indicadores se muestran con
datos de ejemplo y deben validarse con datos reales.

Es el prototipo con mejor cobertura del flujo completo.

### 4.4 P3 – Prototipo 3: Monitor de Calidad Datalake SIMEM (Figma Make)

#### 4.4.1 Flujo de trabajo

![P3 – Flujo de trabajo](img/entregable4_5/p3_flujo_trabajo.png)

#### 4.4.2 Priorización MoSCoW

| Categoría | Funcionalidad | Justificación |
| :--- | :--- | :--- |
| Must | Centro de Situación con KPI de calidad, errores y atrasos | Panel unificado (O1, O5) |
| Must | Validación Fuente vs SIMEM con diferencia, faltantes y exportar evidencia | Contexto para distinguir faltante, diferencia menor o error (entrevistado 2) |
| Must | Conjuntos Atrasados con pestañas por periodicidad | Usa los metadatos que ya existen (periodicidad, próxima ejecución) (O3) |
| Must | Versiones de la liquidación en matriz | O4 |
| Must | Gestión de inconsistencias con responsable y severidad | O1, O7, O8 |
| Must | Configuración de Conjuntos (fuentes oficial y réplica) | O2 |
| Should | Sincronización XM vs SIMEM con diferencia temporal | Responde "¿llegó?" en vocabulario del negocio (hallazgo 1) |
| Should | Validación de Calidad con detalle de reglas | O5 y O7 parcial |
| Should | Auditoría Operativa (pipeline, error, severidad, usuario) | O8 |
| Should | Evolución histórica, mapa de calor y rankings | O6; falta definir el periodo útil |
| Should | Filtros globales y vistas guardadas | Menos pestañas y menos carga cognitiva |
| Could | Credenciales | Necesaria para operar, pero fuera de los objetivos centrales |
| Could | Barra lateral contraíble e indicador de estado de sistemas | Comodidad |
| Won't | Métricas SIMEM (usuarios API, descargas, datos procesados) | Mide el consumo, no la calidad de datos |

**Brechas:** Cinco pantallas (Auditoría, Configuración, Credenciales, Métricas e Inconsistencias)
usan la misma plantilla de tabla, lo que contradice la implicación de diseño de dar a cada alerta
un detalle contextual propio. No se identificó el envío de resumen por Teams.

Es el prototipo con más cobertura de pantallas y mejor orientado a la navegación por módulos; es
el más débil en el detalle del incidente y en la acción correctiva.

## 5. Síntesis comparativa de los prototipos

| Objetivo | P1 AI Studio | P2 Torre de Control | P3 Figma Make |
| :--- | :---: | :---: | :---: |
| O1 Centralizar inconsistencias | ◐ | ● | ● |
| O2 Configurar conjuntos | ● | ● | ◐ |
| O3 Oportunidad y relanzamiento masivo | ◐ | ● | ◐ |
| O4 Versiones de la liquidación | ◐ | ● | ◐ |
| O5 Indicadores de calidad | ◐ | ● | ● |
| O6 Evolución en el tiempo | ◐ | ◐ | ◐ |
| O7 Clasificar inconsistencias | ◐ | ◐ | ◐ |
| O8 Trazabilidad | ● | ● | ● |

_Leyenda: ● cubre, ◐ cubre parcialmente, ○ no se identificó._

## 6. Conclusiones de la fase de prototipado

El prototipo 2, Torre de Control SIMEM, es la mejor base para la versión final porque cubre el
ciclo completo de detectar, clasificar, corregir y medir. Se recomienda complementarlo con el
Centro de Situación, las pestañas por periodicidad y los filtros globales del prototipo 3, y con la
comparación hora a hora y el asistente de ingesta del prototipo 1. Queda pendiente en los tres
el catálogo de inconsistencias. La gráfica de una variable individual y el resumen agrupado por
Teams solo están en el prototipo 2, por lo que deben conservarse en la versión final.
Estas decisiones deberán validarse con los tres usuarios entrevistados, midiendo el tiempo en
tareas como ubicar un conjunto atrasado, distinguir un dato atrasado de uno erróneo y recuperar
una versión faltante.

---

<a id="parte-5"></a>

# Parte V. Evaluación de usabilidad

## 1. Introducción

El presente apartado documenta la planeación y los resultados de las pruebas de usabilidad de tres
prototipos de una aplicación web orientada al monitoreo, diagnóstico y gestión de la calidad de los datos de
SIMEM.

SIMEM es una plataforma web de datos abiertos relacionada con el Mercado de Energía Mayorista
(MEM) y la operación del Sistema Interconectado Nacional (SIN). La información publicada proviene
de un lago de datos de origen que recibe registros de diferentes fuentes. Sin embargo, pueden
presentarse retrasos en las publicaciones, errores e inconsistencias en los datos, ausencia de
versiones específicas y dificultades para identificar oportunamente incidentes de calidad.

Actualmente, estas situaciones pueden requerir investigaciones manuales en múltiples
herramientas, archivos y fuentes de información, lo que incrementa el tiempo de diagnóstico y el
riesgo de cometer errores operativos.

Por esta razón, se evaluaron tres prototipos de una aplicación web que busca centralizar el
monitoreo, facilitar la identificación de problemas y mejorar la gestión de incidentes. Las
pruebas permitieron observar cómo interactúan los usuarios con cada propuesta, identificar
dificultades de uso y determinar qué alternativa responde mejor a sus necesidades.

La evaluación se realizó mediante pruebas de usabilidad moderadas, ejecución de tareas
representativas del contexto operativo y aplicación del cuestionario System Usability Scale (SUS).

## 2. Objetivos de la prueba

### 2.1 Objetivo general

Evaluar y comparar la usabilidad de tres prototipos de una aplicación web para la gestión y el
monitoreo de la calidad de los datos de SIMEM, mediante la observación de usuarios que ejecutan
tareas representativas del contexto operativo y la aplicación de la escala SUS, con el propósito
de identificar dificultades de interacción y oportunidades de mejora.

## 3. Alcance de la evaluación

La prueba comprendió la evaluación de los tres prototipos descritos en la Parte IV, creados en
Google AI Studio, como artefacto web de Claude y en Figma Make:

| # | Nombre | Herramienta | Alcance | Enlace |
| :--- | :--- | :--- | :--- | :--- |
| P1 | XM Data Observability | Google AI Studio | 5 módulos | [Abrir](https://aistudio.google.com/apps/c23be026-a328-4074-a049-1c4858f74945?showAssistant=true&showPreview=true&fullscreenApplet=true) |
| P2 | Torre de Control SIMEM | Artefacto web (Claude) | 7 vistas | [Abrir](https://claude.ai/artifact/NXogD8U3Xhq1nyDqkngWpn) |
| P3 | Monitor de Calidad Datalake SIMEM | Figma Make | 10 pantallas | [Abrir](https://www.figma.com/make/7juxDjDFwWXH6TbzPp9v9J/Monitor-de-Calidad-Datalake-SIMEM?fullscreen=1&t=8Tx5etxMkZFdPQX6-1&code-node-id=0-6) |

Los participantes realizaron las mismas siete tareas en cada prototipo, bajo condiciones
equivalentes. Se evaluaron la navegación, la comprensión de la información, la identificación de
estados, la ejecución de acciones y la percepción general de usabilidad.

Las tareas abarcaron:

- Identificación y recarga de conjuntos de datos atrasados.
- Verificación de la carga de una de las versiones de una liquidación.
- Consulta y validación de alertas de calidad de datos.
- Identificación de los conjuntos de datos con mayor número de fallos.
- Asignación de un error a una persona responsable.
- Creación de una conexión a una API.
- Configuración de un conjunto de datos para ejecución diaria.

La evaluación se centró en la interacción con los prototipos y no en la calidad técnica de los
procesos de carga o de los servicios externos.

Cuando los prototipos no contaban con funcionalidades operativas, las acciones se evaluaron
mediante las interacciones que permitían simular. En estos casos, se registró si el usuario
identificaba correctamente la acción y comprendía el resultado esperado, sin asumir que una operación técnica se
ejecutó realmente.

## 4. Preguntas de investigación

La evaluación buscó responder las siguientes preguntas:

1. ¿Cuál de los tres prototipos permite identificar con mayor facilidad los conjuntos de datos
   atrasados?
2. ¿Qué propuesta facilita la comprensión de los estados de ejecución, las versiones y las alertas
   de calidad?
3. ¿Cuál permite completar las tareas con menos tiempo, errores y solicitudes de ayuda?
4. ¿Qué dificultades encuentran los usuarios durante el diagnóstico y la gestión de incidentes?
5. ¿Qué tan fácil resulta crear conexiones y configurar conjuntos de datos en cada propuesta?
6. ¿Cuál obtiene la mejor puntuación promedio de usabilidad percibida mediante SUS?
7. ¿Qué elementos de cada prototipo deberían modificarse para mejorar la experiencia de uso?

## 5. Metodología

Se utilizó una metodología de pruebas de usabilidad moderadas, con un enfoque comparativo entre
los tres prototipos.

El moderador proporcionó un escenario contextual y solicitó al participante que realizara una
serie de tareas. Durante la ejecución, observó el comportamiento del usuario sin indicarle dónde
hacer clic ni cómo resolver cada situación.

Se utilizó la técnica de pensamiento en voz alta, mediante la cual el participante expresaba qué
buscaba, qué esperaba encontrar y qué dudas surgían durante la interacción.

Al finalizar las tareas de cada prototipo, el participante respondió el cuestionario SUS y
participó en una breve entrevista sobre su experiencia.

La evaluación se planeó para combinar datos cuantitativos y cualitativos (ver las limitaciones en
la sección 7.4).

**Datos cuantitativos:**

- Tiempo de ejecución de las tareas.
- Tasa de éxito.
- Número de errores.
- Número de solicitudes de ayuda.
- Puntuación SUS.

**Datos cualitativos:**

- Dificultades observadas.
- Dudas e interpretaciones incorrectas.
- Comentarios expresados durante la prueba.
- Problemas de navegación.
- Oportunidades de mejora identificadas.

## 6. Materiales y recursos

Antes de iniciar las sesiones, se prepararon los siguientes materiales:

1. Los tres prototipos de la aplicación web, accesibles desde los dispositivos de prueba.
2. Un computador con conexión estable y un navegador compatible.
3. Un documento con las instrucciones y los escenarios de las tareas.
4. Una ficha para registrar los tiempos, errores, resultados y observaciones.
5. El cuestionario SUS para cada prototipo.
6. Un cronómetro o herramienta de registro de tiempo.
7. Una hoja de cálculo para consolidar los resultados.
8. Un conjunto de datos de prueba que permita identificar los resultados esperados de cada tarea.
9. Un formato de consentimiento para participar y, cuando corresponda, para grabar la sesión.

### 6.1 Lista de tareas

**Tarea 1. Identificar y recuperar conjuntos atrasados**

Resultado esperado: el participante identifica los conjuntos semanales atrasados, verifica la
disponibilidad de los datos en origen y ejecuta la recarga masiva con un mismo rango de fechas.

**Tarea 2. Verificar una versión de la liquidación**

Resultado esperado: el participante identifica la versión TX2 de la liquidación correspondiente al
5 de octubre y comunica correctamente su estado de carga según los datos de prueba.

**Tarea 3. Revisar la calidad de un conjunto de datos**

Resultado esperado: el participante localiza el conjunto aportes_a_embalses, revisa los datos del
embalse TOMINE del 3 de agosto de 2026, identifica la alerta y verifica la corrección mediante una
nueva ejecución de la herramienta de calidad cuando corresponda.

**Tarea 4. Identificar los conjuntos que más fallan**

Resultado esperado: el participante identifica los conjuntos con más fallos y las causas
registradas en el sistema de prueba.

**Tarea 5. Asignar un error**

Resultado esperado: el participante localiza el error indicado, lo asigna a la persona
especificada en el escenario y comprueba que la asignación quede registrada.

**Tarea 6. Crear una nueva conexión**

Resultado esperado: el participante crea una conexión con los parámetros ficticios suministrados y
verifica su estado.

**Tarea 7. Configurar un conjunto de datos**

Resultado esperado: el participante registra un nuevo conjunto de datos con los parámetros
establecidos y configura su ejecución diaria.

## 7. Resultados generales de las entrevistas

Los comentarios de los participantes muestran diferencias claras entre las propuestas. El
prototipo P1 ofrece herramientas especializadas para diagnóstico y configuración, pero presenta
dificultades de organización y gestión de incidentes. P2 destaca por integrar la detección,
asignación y corrección de problemas. P3 facilita la consulta visual de estados, atrasos y
versiones, aunque algunas acciones correctivas y de configuración no están suficientemente
desarrolladas.

### 7.1 Resultados por tarea

#### 7.1.1 Tarea 1: detectar retrasos y recuperar información

**Hallazgo principal:** P2 y P3 permiten identificar los conjuntos atrasados con mayor claridad
que P1, pero P2 presenta el flujo más completo para seleccionarlos y relanzarlos masivamente.

- **P1:** en una entrevista, la tarea tomó aproximadamente 10 minutos. No se encontró la opción
  para ejecutar una recarga masiva y fue necesario invertir tiempo en localizar filtros. También
  se identificaron problemas de contraste, exceso de información y falta de claridad sobre la
  periodicidad y la próxima ejecución. En otra entrevista, se encontraron los atrasos, pero
  mezclados con información adicional y sin indicar claramente desde cuándo ocurrían.
- **P2:** permite identificar los conjuntos atrasados, verificar si la información está disponible
  en el Data Lake de origen y seleccionar varios conjuntos para relanzarlos con fechas
  recomendadas. Se observó que parte de la información presentada puede ser innecesaria y que no
  siempre queda claro cuánto tiempo lleva un conjunto atrasado.
- **P3:** facilita reconocer los atrasos y entender desde cuándo un conjunto semanal no se ejecuta
  correctamente. También permite identificar diferencias de sincronización entre SIMEM y el
  origen. Sin embargo, se recomienda incorporar la acción de relanzamiento directamente en esa
  vista y utilizar colores para destacar la criticidad.

**Oportunidad de mejora:** combinar la visualización clara de atrasos de P3 con las acciones de
recarga masiva y las fechas recomendadas de P2. Mostrar la periodicidad, la última ejecución
correcta, la disponibilidad en origen y la próxima ejecución esperada.

#### 7.1.2 Tarea 2: verificar las versiones de la liquidación

**Hallazgo principal:** P2 fue el prototipo más efectivo para localizar una versión específica y
determinar su estado.

- **P1:** un participante no encontró la información solicitada. La interfaz no permite consultar
  de manera clara las versiones faltantes para un conjunto y una fecha específicos, y confunde el
  estado del conjunto con la completitud de las versiones de liquidación.
- **P2:** la versión TX2 se encontró en aproximadamente 10 segundos en una entrevista. La matriz
  permite distinguir versiones cargadas, futuras e inconsistentes. También se valora el acceso al
  repositorio FTP para recuperar versiones que ya no estén disponibles en la fuente. Como
  dificultad, puede ser necesario entrar conjunto por conjunto para conocer las inconsistencias.
- **P3:** un participante encontró la versión en aproximadamente 20 segundos, aunque consideró el
  proceso más enredado. Su representación visual permite identificar rápidamente conjuntos con
  errores, pero presenta limitaciones para escalar cuando existen muchas versiones y no ofrece una
  acción identificada para recuperarlas desde FTP.

**Oportunidad de mejora:** utilizar la matriz de versiones de P2 como base, complementándola con
una vista consolidada similar a la de P3. La interfaz debe permitir consultar la fecha, el
conjunto y la versión concreta, sin asumir que un conjunto actualizado tiene todas las versiones
de liquidación disponibles.

#### 7.1.3 Tarea 3: diagnosticar y verificar una alerta de calidad

**Hallazgo principal:** P2 facilita mejor el paso de identificar un error a gestionarlo; P3
permite encontrar visualmente inconsistencias, pero necesita mayor capacidad de filtrado y
contexto.

- **P1:** permite encontrar valores erróneos y consultar la causa reportada. Sin embargo, algunas
  acciones como "Relanzar", "Sobreescribir partición" o "Generar parche" no resultan claras desde
  el punto de vista del negocio. Tampoco es evidente cómo asignar un incidente a una persona.
- **P2:** permite navegar entre los conjuntos con errores, entender la causa y asignar el
  incidente a un responsable. Los participantes encontraron el error solicitado.
- **P3:** permite reconocer valores correctos e incorrectos y volver a ejecutar la validación de
  calidad para generar evidencia. Sin embargo, muestra también los datos correctos, lo que
  dificulta concentrarse en los errores; además, puede requerir revisar los conjuntos uno por uno.

**Oportunidad de mejora:** incorporar filtros por errores, una explicación contextual de la causa,
un responsable visible, el estado de gestión y una acción diferenciada entre recargar datos y
volver a ejecutar la herramienta de calidad.

#### 7.1.4 Tarea 4: identificar los conjuntos con más fallos

**Hallazgo principal:** P2 y P3 ofrecen mejores posibilidades de análisis comparativo, mientras
que P1 presenta limitaciones para identificar los conjuntos más problemáticos a lo largo del
tiempo.

- **P1:** permite consultar el seguimiento de inconsistencias y distinguir niveles de criticidad,
  pero no ofrece un análisis retrospectivo suficiente para identificar cuáles conjuntos fallan con
  mayor frecuencia.
- **P2:** permite consultar conjuntos con menor calidad, evolución temporal, fuentes con más
  incidentes y porcentaje de calidad por conjunto. Los participantes reportaron que podían
  encontrar la información con facilidad.
- **P3:** permite reconocer rápidamente el conjunto con mayor tasa de mala calidad y localizar los
  conjuntos más problemáticos.

**Oportunidad de mejora:** integrar los indicadores comparativos y la evolución temporal de P2 con
los rankings visuales de P3. Mostrar el número de fallos, la tasa de mala calidad, la causa
recurrente y la evolución por periodo.

#### 7.1.5 Tarea 5: asignar un error a una persona

**Hallazgo principal:** P2 presenta el flujo más claro para asignar responsables, mientras que P1
permite visualizar responsables existentes sin facilitar su asignación y P3 presenta problemas de
encontrabilidad.

- **P1:** permite ver quién gestiona los errores, pero no resulta claro cómo asignar un incidente.
- **P2:** permite asignar o autoasignar un incidente rápidamente. La limitación identificada es que
  no muestra de forma consolidada qué persona está atendiendo cada error.
- **P3:** consolida errores y permite consultar quién los gestiona, pero la ubicación de la
  funcionalidad no es evidente. En una entrevista, la búsqueda superó los dos minutos y se reportó
  dificultad para crear un caso de seguimiento.

**Oportunidad de mejora:** incluir un botón de asignación visible en el detalle del incidente,
permitir autoasignación y ofrecer una vista consolidada por responsable, estado y conjunto de
datos.

#### 7.1.6 Tarea 6: crear una conexión a una API

**Hallazgo principal:** P1 es el único prototipo en el que las entrevistas describen un flujo de
configuración de fuentes y prueba de conectividad. P2 y P3 no permiten completar la creación de
una nueva conexión según los resultados registrados.

- **P1:** permite configurar conexiones a API, FTP y bases de datos, mapear esquemas y establecer
  reglas de calidad. También se menciona una prueba de conectividad al terminar la configuración.
  Como dificultad, la pantalla presenta demasiada información y mezcla la configuración con las
  alertas de calidad.
- **P2:** se reporta que no es posible crear una conexión nueva, sino consultar configuraciones
  existentes.
- **P3:** permite administrar credenciales, pero no se identifica un flujo para configurar una
  nueva conexión.

**Oportunidad de mejora:** conservar la capacidad de configuración de P1, pero simplificarla
mediante pasos guiados, separación entre configuración y monitoreo, validaciones claras y
confirmación del resultado de la conexión.

#### 7.1.7 Tarea 7: configurar un conjunto de datos nuevo

**Hallazgo principal:** P2 ofrece el flujo más completo para administrar configuraciones
existentes y preparar una nueva configuración, aunque debe verificarse la creación efectiva de un
conjunto nuevo.

- **P1:** permite establecer la frecuencia de ejecución, pero no ofrece un catálogo claro de
  conjuntos ya configurados. Esto dificulta saber si el conjunto ya existe.
- **P2:** presenta una lista de configuraciones con fuente, periodicidad, última modificación y
  estado. Permite editar parámetros, configurar consultas y reglas de calidad, y realizar una
  prueba en seco.
- **P3:** permite consultar conjuntos existentes y atributos como fuente oficial, réplica y estado
  de activación, pero no permite crear uno nuevo en el flujo observado.

**Oportunidad de mejora:** partir del catálogo y la prueba en seco de P2, e incorporar un
asistente de configuración como el de P1. Antes de dar por completada la tarea, debe confirmarse
que el nuevo conjunto quedó registrado con periodicidad diaria.

### 7.2 Interpretación de los resultados SUS

| Participante | P1: XM Data Observability | P2: Torre de Control SIMEM | P3: Monitor de Calidad Datalake SIMEM |
| :--- | :---: | :---: | :---: |
| Entrevistado 1 | 35 | 87,5 | 67,5 |
| Entrevistado 2 | 40 | 70 | 65 |
| Entrevistado 3 | 27,5 | 82,5 | 67,5 |
| **Promedio** | **34,17** | **80** | **66,67** |

- **P1 — 34,17 puntos:** la evaluación sugiere dificultades importantes para encontrar
  funcionalidades, comprender algunas acciones y gestionar incidencias. Conviene simplificar la
  interfaz y aclarar el significado de las opciones.
- **P2 — 80 puntos:** obtiene el mejor resultado promedio. Su fortaleza está en la cobertura del
  flujo de trabajo, desde la detección y asignación hasta el análisis de calidad y la
  configuración.
- **P3 — 66,67 puntos:** presenta una usabilidad intermedia, con una vista general clara y buen
  seguimiento de versiones, pero oportunidades de mejora en la asignación de responsables y la
  configuración de nuevos conjuntos de datos.

### 7.3 Respuesta a las preguntas de investigación

1. **¿Cuál permite identificar con mayor facilidad los conjuntos atrasados?** P2 y P3. P3 muestra
   con más claridad desde cuándo está atrasado un conjunto, y P2 ofrece el flujo más completo para
   seleccionarlos y relanzarlos (tarea 1).
2. **¿Qué propuesta facilita la comprensión de estados, versiones y alertas?** P2: su matriz
   distingue versiones cargadas, futuras e inconsistentes, y permite pasar de la alerta a la
   gestión del incidente (tareas 2 y 3).
3. **¿Cuál permite completar las tareas con menos tiempo, errores y solicitudes de ayuda?** Los
   tiempos observados apuntan a P2 (la versión TX2 se encontró en unos 10 segundos frente a unos 20
   en P3, y la tarea 1 tomó unos 10 minutos en P1), pero esta pregunta solo se responde de forma
   parcial porque esas métricas no se registraron de forma sistemática (sección 7.4).
4. **¿Qué dificultades encuentran los usuarios?** Acciones con lenguaje técnico poco claro, exceso
   de información y bajo contraste (P1); funciones difíciles de encontrar, como la asignación de
   responsables, y errores mezclados con datos correctos (P3); y falta de una vista consolidada por
   responsable (P2).
5. **¿Qué tan fácil es crear conexiones y configurar conjuntos?** Solo P1 permitió crear una
   conexión nueva; P2 ofrece la mejor administración de configuraciones existentes, con prueba en
   seco. Ningún prototipo cubre ambos flujos de punta a punta (tareas 6 y 7).
6. **¿Cuál obtiene la mejor puntuación SUS?** P2, con 80 puntos, seguido de P3 (66,67) y P1
   (34,17).
7. **¿Qué elementos deberían modificarse?** Llevar el relanzamiento a la vista de atrasos de P3,
   simplificar P1 separando configuración y monitoreo, hacer visible la asignación y agregar una
   vista por responsable, filtrar por errores en la validación de calidad e incorporar a P2 un
   asistente guiado de configuración (oportunidades de mejora de la sección 7.1).

### 7.4 Limitaciones de la evaluación

- No se registraron de forma sistemática el tiempo por tarea, la tasa de éxito, el número de
  errores ni las solicitudes de ayuda previstos en la metodología. Los resultados cuantitativos se
  limitan a la escala SUS y a tiempos puntuales observados en algunas sesiones.
- La muestra es de tres participantes y no todas las observaciones por tarea quedaron registradas
  para cada participante y prototipo.
- Los prototipos usan datos de ejemplo, por lo que acciones como el relanzamiento o la recuperación
  desde FTP solo se simularon.

## 8. Conclusiones de la evaluación de usabilidad

La evaluación de los tres prototipos muestra que la Torre de Control SIMEM (P2) constituye la
alternativa más prometedora para continuar el diseño de la herramienta de monitoreo de calidad de
datos del SIMEM. Este prototipo obtuvo el mayor promedio SUS, con 80 puntos, y destacó en tareas
que requieren identificar conjuntos atrasados, verificar versiones de liquidación, asignar
incidentes y ejecutar acciones de recuperación.

El Monitor de Calidad Datalake SIMEM (P3) presenta fortalezas en la visualización de estados, la
identificación de atrasos y la consulta de conjuntos con problemas de calidad y en las versiones
de la liquidación. Por su parte, XM Data Observability (P1) aporta capacidades relevantes para el
diagnóstico de errores y la configuración de fuentes y reglas de calidad.

En consecuencia, se recomienda tomar P2 como base para la propuesta final e incorporar elementos
de P3 que faciliten la navegación, la consulta de atrasos y la visualización de versiones, junto
con el asistente guiado de P1, el único que permitió crear una conexión nueva (tarea 6). Esta
conclusión es consistente con la evaluación MoSCoW de la Parte IV, que ya identificaba a P2 como
el prototipo con mejor cobertura del flujo completo.

La evaluación también ajusta una estimación de la Parte IV: en el análisis de ventajas y
desventajas, P2 tenía cobertura total del objetivo O2 (configurar conjuntos), pero las pruebas
mostraron que permite administrar configuraciones existentes y no crear conexiones nuevas, por lo
que su cobertura real de O2 es parcial.

---

<a id="parte-6"></a>

# Parte VI. Prototipo final

El prototipo final (PF), Monitor de Calidad SIMEM, consolida las decisiones de la Parte IV y los
resultados de la evaluación de usabilidad de la Parte V. Toma como base P2, Torre de Control SIMEM
(SUS 80), e incorpora la vista general y la lectura de atrasos y versiones de P3, y el asistente
guiado de configuración de P1, tal como se recomendó en la sección 8 de la Parte V.

El PF es una aplicación web navegable de una sola página (HTML, CSS y JavaScript) con datos de
ejemplo. Las acciones de relanzamiento, recuperación de versiones, validación, prueba de conexión,
envío a Teams y gestión de credenciales son simuladas: muestran el resultado esperado, pero no se
conectan a ninguna fuente real.

| # | Prototipo | Herramienta | Alcance | Enlace |
| :--- | :--- | :--- | :--- | :--- |
| PF | Monitor de Calidad SIMEM | Artefacto web (HTML) | 8 vistas y detalle de incidente | _Pendiente_ |

**Vistas del prototipo final**

| Vista | Propósito | Objetivos |
| :--- | :--- | :--- |
| Torre de Control | Indicadores del sitio, alertas separadas en pestañas (atrasados, errores de calidad, errores de configuración) y resumen del día para Teams | O1, O5, O7 |
| Detalle del incidente | Recorrido Fuente → Data Lake → SIMEM, evidencia según el tipo de alerta, estado de gestión, responsable, acciones sugeridas y bitácora | O1, O8 |
| Oportunidad de publicación | Fecha indexada esperada frente a la publicada, atraso en días, última y próxima ejecución, y relanzamiento masivo | O3 |
| Versiones de liquidación | Matriz de versiones por día (TX1, TX2, TXR, TXF, TX3), indicador de completitud y recuperación desde la fuente alterna FTP | O4 |
| Validación Fuente vs SIMEM | Inconsistencias entre la fuente oficial y SIMEM, tasa de inconsistencias, marca de solucionado y validación histórica | O1, O5, O7 |
| Indicadores y tendencias | Cantidad y tasa de inconsistencias por conjunto, fuentes con más errores, calendario de ejecución, tipos por semana, ranking y explorador de variable | O5, O6 |
| Configuración de conjuntos | Catálogo de variables, activación y pausa, advertencias de configuración y asistente de cuatro pasos con prueba en seco | O2 |
| Trazabilidad | Historial de hallazgos con tipo, origen, causa raíz, responsable, estado y recurrencia | O7, O8 |
| Credenciales | Accesos a las fuentes con contraseña enmascarada, validación y renovación | O2 |

**Origen de las decisiones de diseño**

| Elemento del PF | Origen | Hallazgo o tarea que atiende |
| :--- | :--- | :--- |
| Pestañas por tipo de alerta y resumen del día para Teams | P2 | Separar atraso de error (hallazgo 1) y reducir correos (hallazgo 2) |
| Fila de indicadores en la Torre de Control | P3 (Centro de Situación) | Vista general clara (Parte V, sección 8) |
| Filtro por periodicidad, atraso en días, selección de atrasados y relanzamiento masivo con rango de fechas | P2 y P3 | Tarea 1 |
| Reversión automática de la configuración temporal al relanzar | P2 | Olvido de revertir deltas (O2) |
| Matriz de versiones con filtros, completitud del mes, plazo por versión y recuperación desde FTP con confirmación | P2 y P3 | Tarea 2 |
| Tabla de validación que muestra solo inconsistencias, con su estado y la marca de solucionado | P3, ajustado | Tarea 3: los datos correctos dificultaban concentrarse en los errores |
| Reejecución de la validación separada de la recarga de datos | Nuevo | Tarea 3: diferenciar recargar datos de volver a validar |
| Gráfica de cantidad y tasa por conjunto, ranking de conjuntos y fuentes | P2 y P3 | Tarea 4 |
| Selector «Asignar a», botón «Tomar incidente» y responsable visible en las tablas | P2 | Tarea 5 |
| Asistente de cuatro pasos con prueba de conexión, fuente alterna opcional, reglas, ejecución y prueba en seco | P1 y P2 | Tareas 6 y 7 |
| Credenciales con validación y renovación | P3 | Tarea 6 |
| Tipo, origen, causa raíz y recurrencia en Trazabilidad | P2, ampliado | O7 y O8 |

## 1. Diagrama de flujo

El diagrama muestra la estructura del PF y los caminos principales entre vistas. Todas las vistas
son accesibles desde el menú lateral y con los atajos de teclado 1 a 8; las flechas representan los
recorridos que el prototipo propone dentro de la operación diaria.

![PF – Diagrama de flujo](img/entregable_final/01_diagrama_de_flujo_pf.png)

## 2. Capturas de pantalla del prototipo final

Las capturas se guardan en `docs/img/prototipo_final/` con los nombres indicados en cada imagen.

**Torre de Control**

![PF – Torre de Control (1)](img/prototipo_final/pf_torre_de_control_1.png)

**Oportunidad de publicación**

![PF – Oportunidad de publicación](img/prototipo_final/pf_oportunidad_publicacion.png)
![PF – Relanzamiento masivo](img/prototipo_final/pf_relanzamiento_masivo.png)

**Versiones de liquidación**

![PF – Versiones de liquidación](img/prototipo_final/pf_versiones_liquidacion.png)
![PF – Detalle y recuperación de versión](img/prototipo_final/pf_versiones_detalle.png)

**Validación Fuente vs SIMEM**

![PF – Validación Fuente vs SIMEM](img/prototipo_final/pf_validacion_fuente_simem.png)
![PF – Validación Fuente vs SIMEM](img/prototipo_final/pf_validacion_fuente_simem_2.png)
![PF – Validación histórica personalizada](img/prototipo_final/pf_validacion_historica.png)

**Indicadores y tendencias**

![PF – Indicadores y tendencias (1)](img/prototipo_final/pf_indicadores_1.png)
![PF – Indicadores y tendencias (2)](img/prototipo_final/pf_indicadores_2.png)
![PF – Indicadores y tendencias (2)](img/prototipo_final/pf_indicadores_3.png)

**Configuración de conjuntos**

![PF – Configuración de conjuntos](img/prototipo_final/pf_configuracion.png)
![PF – Asistente de nueva variable](img/prototipo_final/pf_asistente_variable.png)
![PF – Asistente de nueva variable](img/prototipo_final/pf_asistente_variable_2.png)


**Trazabilidad**

![PF – Trazabilidad](img/prototipo_final/pf_trazabilidad.png)
![PF – Trazabilidad](img/prototipo_final/pf_trazabilidad_detalle_calidad.png)
![PF – Trazabilidad](img/prototipo_final/pf_trazabilidad_detalle_atraso.png)
![PF – Trazabilidad](img/prototipo_final/pf_trazabilidad_detalle_configuracion.png)

**Credenciales**

![PF – Credenciales](img/prototipo_final/pf_credenciales.png)

**Notificaciones**

![PF – Notificaciones](img/prototipo_final/pf_notificaciones.png)

## 3. Flujo de tareas

El flujo de tareas describe la ruta lineal que sigue un usuario en el PF para completar cada una de
las siete tareas de la evaluación de usabilidad (Parte V, sección 6.1). A diferencia del flujo de
usuario, no incluye decisiones: muestra el camino esperado cuando todo sale bien.

### 3.1 Tarea 1: identificar y recuperar conjuntos atrasados

![Flujo de tareas – Tarea 1](img/entregable_final/02_tarea1_conjuntos_atrasados.png)

La disponibilidad del dato en el Data Lake se consulta en el detalle del incidente abierto desde
Trazabilidad (panel «Disponibilidad del dato»).

### 3.2 Tarea 2: verificar una versión de la liquidación

![Flujo de tareas – Tarea 2](img/entregable_final/03_tarea2_version_liquidacion.png)

### 3.3 Tarea 3: revisar la calidad de un conjunto de datos

![Flujo de tareas – Tarea 3](img/entregable_final/04_tarea3_calidad_conjunto.png)

### 3.4 Tarea 4: identificar los conjuntos que más fallan

![Flujo de tareas – Tarea 4](img/entregable_final/05_tarea4_conjuntos_que_mas_fallan.png)

### 3.5 Tarea 5: asignar un error

![Flujo de tareas – Tarea 5](img/entregable_final/06_tarea5_asignar_error.png)

Desde la Torre de Control, el botón «Tomar incidente» permite la autoasignación.

### 3.6 Tarea 6: crear una conexión a una API

![Flujo de tareas – Tarea 6](img/entregable_final/07_tarea6_conexion_api.png)

### 3.7 Tarea 7: configurar un conjunto de datos

![Flujo de tareas – Tarea 7](img/entregable_final/08_tarea7_configurar_conjunto.png)

## 4. Flujo de usuario

El flujo de usuario muestra cómo cada persona de la Parte III recorre el PF desde su punto de
entrada, incluyendo las decisiones que toma según lo que encuentra.

### 4.1 Analista de Calidad Operativa

Entra por el resumen diario de Teams o por la Torre de Control, y su objetivo es que ninguna alerta
quede sin dueño ni sin diagnóstico.

![Flujo de usuario – Analista de Calidad Operativa](img/entregable_final/09_flujo_analista_calidad.png)

### 4.2 Ingeniero de Configuración y Metadatos

Su punto de entrada es una alerta de configuración o la solicitud de un conjunto nuevo. Su objetivo
es que la configuración no genere falsas alertas y que cada cambio quede registrado.

![Flujo de usuario – Ingeniero de Configuración y Metadatos](img/entregable_final/10_flujo_ingeniero_configuracion.png)

### 4.3 Especialista de Monitoreo Multifuente

Supervisa las ejecuciones, los atrasos y las versiones de la liquidación. Su objetivo es que los
datos y las versiones obligatorias queden publicados dentro del plazo.

![Flujo de usuario – Especialista de Monitoreo Multifuente](img/entregable_final/11_flujo_especialista_monitoreo.png)

## 5. Historias de usuario para la implementación

Las historias de usuario traducen el PF en requisitos para la implementación real. Siguen el
formato «Como [persona], quiero [acción], para [beneficio]», se asocian a los objetivos O1 a O8 y
se priorizan con MoSCoW. Los criterios de aceptación usan la forma «Dado / Cuando / Entonces».

Las personas son las definidas en la Parte III: Analista de Calidad Operativa (AC), Ingeniero de
Configuración y Metadatos (IC) y Especialista de Monitoreo Multifuente (EM). Las historias marcadas
como _mejora_ no están en el PF y responden a brechas detectadas en la Parte V.

### 5.1 Resumen del backlog

| ID | Épica | Historia | Persona | Prioridad | Objetivo |
| :--- | :--- | :--- | :--- | :--- | :--- |
| HU-01 | Torre de Control | Ver el estado general del sitio | AC | Must | O1, O5 |
| HU-02 | Torre de Control | Ver las alertas separadas por tipo | AC | Must | O1, O7 |
| HU-03 | Torre de Control | Recibir el resumen diario en Teams | AC | Should | O1 |
| HU-04 | Incidentes | Ver la evidencia del incidente según su tipo | AC | Must | O1 |
| HU-05 | Incidentes | Tomar o asignar un incidente | AC | Must | O1, O8 |
| HU-06 | Incidentes | Avanzar el estado de gestión | AC | Must | O8 |
| HU-07 | Incidentes | Ejecutar acciones sugeridas | AC | Should | O1 |
| HU-08 | Incidentes | Ver mis incidentes y los de cada responsable (_mejora_) | AC | Should | O1 |
| HU-09 | Oportunidad | Ver el atraso real de cada conjunto | EM | Must | O3 |
| HU-10 | Oportunidad | Relanzar varios conjuntos a la vez | EM | Must | O3 |
| HU-11 | Oportunidad | Revertir la configuración temporal al terminar | IC | Must | O2, O3 |
| HU-12 | Versiones | Ver la matriz de versiones del mes | EM | Must | O4 |
| HU-13 | Versiones | Recuperar una versión faltante desde FTP | EM | Must | O4 |
| HU-14 | Validación | Comparar la fuente con SIMEM | AC | Must | O1, O7 |
| HU-15 | Validación | Re-ejecutar la validación de calidad | AC | Must | O1 |
| HU-16 | Validación | Marcar una inconsistencia como solucionada | AC | Should | O1, O8 |
| HU-17 | Validación | Ejecutar una validación histórica | AC | Should | O6 |
| HU-18 | Indicadores | Ver la tendencia de inconsistencias por conjunto | AC | Must | O5, O6 |
| HU-19 | Indicadores | Ver los conjuntos y fuentes con más fallos | AC | Should | O5, O7 |
| HU-20 | Indicadores | Ver el calendario de ejecución de la herramienta | EM | Should | O6 |
| HU-21 | Indicadores | Explorar una variable en un rango de fechas | AC | Should | O6 |
| HU-22 | Configuración | Consultar y pausar conjuntos configurados | IC | Must | O2 |
| HU-23 | Configuración | Crear una variable con el asistente | IC | Must | O2 |
| HU-24 | Configuración | Editar una variable y conservar el historial | IC | Must | O2, O8 |
| HU-25 | Configuración | Corregir configuraciones con advertencia | IC | Should | O2 |
| HU-26 | Configuración | Gestionar las credenciales de las fuentes | IC | Must | O2 |
| HU-27 | Trazabilidad | Consultar el historial de hallazgos | AC | Must | O8 |
| HU-28 | Trazabilidad | Administrar el catálogo de inconsistencias (_mejora_) | IC | Should | O7 |
| HU-29 | Trazabilidad | Exportar un reporte de evidencia | AC | Should | O8 |
| HU-30 | Transversal | Recibir notificaciones en la aplicación | AC | Should | O1 |
| HU-31 | Transversal | Ingresar con mi usuario corporativo y mi rol | Todas | Must | — |
| HU-32 | Transversal | Usar la herramienta con teclado y en tema claro u oscuro | Todas | Could | — |

### 5.2 Épica 1: Torre de Control

**HU-01 · Ver el estado general del sitio** (Must · O1, O5)

Como Analista de Calidad Operativa, quiero ver al iniciar la jornada la calidad global, los
conjuntos monitoreados, los atrasados y los errores de calidad y de configuración, para saber en
segundos si hay algo que atender.

- Dado que ingreso a la herramienta, cuando se carga la Torre de Control, entonces veo los cinco
  indicadores con la fecha y hora de corte de la última validación.
- Dado un indicador, cuando lo comparo con el listado de su pestaña, entonces el número coincide.
- Dado que la calidad global cambió frente a la semana anterior, entonces se muestra la variación.

**HU-02 · Ver las alertas separadas por tipo** (Must · O1, O7)

Como Analista de Calidad Operativa, quiero ver las alertas separadas en atrasados, errores de
calidad y errores de configuración, para no confundir un dato atrasado con uno erróneo.

- Dado que hay alertas abiertas, cuando reviso la Torre, entonces cada pestaña muestra su conteo y
  una tabla con conjunto, criticidad, fuente, antigüedad, responsable e identificador.
- Dada una fila, cuando la selecciono con el ratón o con Enter, entonces se abre el detalle del
  incidente.
- Dado un incidente sin responsable, entonces se muestra «Sin asignar».

**HU-03 · Recibir el resumen diario en Teams** (Should · O1)

Como Analista de Calidad Operativa, quiero recibir un único resumen diario en el canal de Teams,
para dejar de revisar correos individuales por cada alerta.

- Dada la hora configurada (07:30 por defecto), entonces el sistema publica en el canal un resumen
  con los incidentes críticos nuevos, los atrasos, las alertas de configuración y los cierres del
  día anterior.
- Cuando uso «Enviar resumen a Teams», entonces el resumen se publica de inmediato.
- Si el envío falla, entonces veo el error y puedo reintentar.

### 5.3 Épica 2: Gestión de incidentes

**HU-04 · Ver la evidencia del incidente según su tipo** (Must · O1)

Como Analista de Calidad Operativa, quiero ver la evidencia adecuada a cada tipo de alerta, para
diagnosticar sin consultar otras herramientas.

- Dado un error de calidad, entonces veo la comparación hora a hora entre la fuente y SIMEM, con las
  diferencias y los faltantes resaltados.
- Dado un atraso, entonces veo la fecha indexada esperada frente a la publicada y el resultado de
  cada ejecución.
- Dado un error de configuración, entonces veo el cambio sugerido con el valor anterior y el nuevo.
- En todos los casos veo el recorrido Fuente → Data Lake → SIMEM con el punto donde se originó el
  fallo y la serie de los últimos 30 días.

**HU-05 · Tomar o asignar un incidente** (Must · O1, O8)

Como Analista de Calidad Operativa, quiero tomar un incidente o asignarlo a un compañero, para que
ningún problema quede sin dueño ni se atienda dos veces.

- Cuando uso «Tomar incidente», entonces quedo como responsable y el estado pasa a «En revisión».
- Cuando elijo una persona en «Asignar a», entonces la asignación se guarda, se notifica a esa
  persona y queda en la bitácora con usuario, fecha y hora.
- La lista de «Asignar a» muestra solo usuarios activos con permiso para gestionar incidentes.
- El responsable se actualiza en la Torre de Control y en Trazabilidad.

**HU-06 · Avanzar el estado de gestión** (Must · O8)

Como Analista de Calidad Operativa, quiero mover el incidente por los estados Nuevo, En revisión,
Corregido, Verificado y Cerrado, para que el equipo sepa en qué punto está cada caso.

- Solo el responsable puede avanzar el estado.
- Un incidente no puede pasar a «Cerrado» sin responsable ni sin haber estado en «Verificado».
- Cuando la siguiente ejecución de la herramienta de calidad confirma la corrección, entonces el
  incidente pasa a «Verificado» automáticamente.

**HU-07 · Ejecutar acciones sugeridas** (Should · O1)

Como Analista de Calidad Operativa, quiero acciones sugeridas según el tipo de incidente, para
pasar del diagnóstico a la corrección sin buscar en otro lugar.

- Dado un error de calidad, entonces puedo reejecutar la carga de la fecha, marcar falsa alerta,
  silenciar la regla 7 días o crear un requerimiento a soporte.
- Cuando marco una falsa alerta, entonces debo escribir el motivo y la regla queda en revisión.
- Cuando silencio una regla, entonces se muestra la fecha en que se reactiva.
- Cuando creo un requerimiento, entonces se genera en la mesa de ayuda con la evidencia adjunta y
  su número queda en la bitácora.

**HU-08 · Ver mis incidentes y los de cada responsable** (Should · O1 · _mejora_)

Como Analista de Calidad Operativa, quiero una vista consolidada por responsable, estado y
conjunto, para saber quién atiende cada error.

- Cuando filtro por responsable, entonces veo sus incidentes abiertos con estado y antigüedad.
- Existe un acceso directo «Mis incidentes».

### 5.4 Épica 3: Oportunidad de publicación

**HU-09 · Ver el atraso real de cada conjunto** (Must · O3)

Como Especialista de Monitoreo Multifuente, quiero comparar la fecha indexada esperada con la
publicada, para detectar atrasos aunque la ejecución reporte éxito.

- La fecha esperada se calcula a partir de la periodicidad y la clasificación del conjunto.
- La tabla muestra periodicidad, clasificación, última actualización, fecha indexada máxima, fecha
  esperada, atraso en días, resultado de la última ejecución y próxima ejecución.
- Dado un conjunto con ejecución exitosa y datos desactualizados, entonces se resalta con una nota.
- Puedo filtrar por periodicidad, estado y nombre.

**HU-10 · Relanzar varios conjuntos a la vez** (Must · O3)

Como Especialista de Monitoreo Multifuente, quiero seleccionar varios conjuntos atrasados y
relanzarlos en una sola acción, para recuperar la publicación sin hacerlo uno por uno.

- Cuando uso «Seleccionar los atrasados», entonces quedan marcados todos los conjuntos con atraso.
- Antes de confirmar, veo y puedo ajustar el rango desde y hasta de cada conjunto.
- Durante la ejecución veo el avance de cada conjunto y, al terminar, el resultado de cada uno.
- Cada relanzamiento queda registrado en Trazabilidad.
- Puedo programar la reejecución para una hora posterior (Could).

**HU-11 · Revertir la configuración temporal al terminar** (Must · O2, O3)

Como Ingeniero de Configuración y Metadatos, quiero que el delta temporal usado en un recargue se
revierta solo al terminar, para no dejar configuraciones olvidadas que generen falsas alertas.

- La opción de reversión automática está marcada por defecto.
- Al terminar el relanzamiento, el delta vuelve a su valor estándar y el cambio queda en
  Trazabilidad con el valor anterior y el nuevo.

### 5.5 Épica 4: Versiones de liquidación

**HU-12 · Ver la matriz de versiones del mes** (Must · O4)

Como Especialista de Monitoreo Multifuente, quiero una matriz por conjunto y día con el estado de
las versiones obligatorias, para saber qué versiones faltan sin revisar conjunto por conjunto.

- Puedo filtrar por mes, conjunto de liquidación y tema, y limpiar los filtros.
- Cada celda indica si la fecha está completa, si falta la última versión y venció su plazo, si
  faltan versiones anteriores o si hay versiones pendientes dentro del plazo.
- Los plazos de cada versión (TX1, TX2, TXR, TXF, TX3) se toman de la regulación vigente y son
  parametrizables.
- Se muestra la completitud del mes como versiones publicadas sobre publicadas más faltantes.
- Al seleccionar una celda, veo cada versión con su plazo, su fecha de publicación y su estado.

**HU-13 · Recuperar una versión faltante desde FTP** (Must · O4)

Como Especialista de Monitoreo Multifuente, quiero recuperar una versión faltante desde la fuente
alterna FTP, para completar la liquidación cuando la fuente principal ya no la tiene.

- Dada una versión faltante, entonces veo si el archivo existe en la ruta alterna configurada.
- La recuperación pide confirmación antes de descargar y cargar.
- El archivo se valida antes de cargarlo a SIMEM; si no existe o no es válido, veo el error y la
  opción de cargarlo manualmente.
- Al terminar, el estado de la celda se actualiza y la acción queda en Trazabilidad.

### 5.6 Épica 5: Validación Fuente vs SIMEM

**HU-14 · Comparar la fuente con SIMEM** (Must · O1, O7)

Como Analista de Calidad Operativa, quiero ver solo los registros en los que la fuente y SIMEM no
coinciden, para concentrarme en los errores.

- Puedo filtrar por fuente de origen, conjunto y rango de fechas; un rango inválido muestra un
  mensaje y no ejecuta la consulta.
- Veo la configuración del conjunto: fuente oficial, réplica, fecha de indexación, campos
  identificadores y campo comparado.
- Cada inconsistencia muestra fecha, identificadores, valor en la fuente, valor en SIMEM, diferencia
  y estado (diferente, faltante en SIMEM o faltante en la fuente).
- Veo la cantidad de registros, la cantidad de inconsistencias y la tasa de inconsistencias.

**HU-15 · Re-ejecutar la validación de calidad** (Must · O1)

Como Analista de Calidad Operativa, quiero volver a ejecutar la validación sin recargar los datos,
para comprobar si una corrección resolvió la inconsistencia.

- La acción es distinta de la recarga de datos y así se nombra en la interfaz.
- Mientras se ejecuta, el botón queda deshabilitado y se muestra el progreso.
- Al terminar, se actualiza la hora de la última validación; si falla, veo el error y puedo
  reintentar.

**HU-16 · Marcar una inconsistencia como solucionada** (Should · O1, O8)

Como Analista de Calidad Operativa, quiero marcar una inconsistencia como solucionada, para llevar
la cuenta de lo pendiente.

- El indicador muestra cuántas están solucionadas y cuántas por solucionar.
- El cambio registra usuario, fecha y hora.

**HU-17 · Ejecutar una validación histórica** (Should · O6)

Como Analista de Calidad Operativa, quiero validar un conjunto en un rango de fechas pasado, sin
afectar la validación principal, para revisar periodos anteriores.

- El rango no puede ser futuro, la fecha inicial no puede ser posterior a la final y el máximo es de
  366 días.
- Se muestran los estados de ejecución, error, sin inconsistencias y con resultados.

### 5.7 Épica 6: Indicadores y tendencias

**HU-18 · Ver la tendencia de inconsistencias por conjunto** (Must · O5, O6)

Como Analista de Calidad Operativa, quiero comparar la cantidad y la tasa de inconsistencias de
varios conjuntos en el tiempo, para saber cuáles empeoran.

- Puedo seleccionar uno o varios conjuntos; siempre queda al menos uno seleccionado.
- La gráfica muestra la cantidad y la tasa por semana, con dos ejes identificados.
- Puedo cambiar el periodo entre 30 días, 90 días y 6 meses.
- Cada punto muestra su valor con el cursor y con el teclado.

**HU-19 · Ver los conjuntos y fuentes con más fallos** (Should · O5, O7)

Como Analista de Calidad Operativa, quiero ver qué conjuntos tienen menor calidad, qué fuentes
generan más incidentes y qué tipos de inconsistencia predominan, para priorizar mejoras.

- Veo el ranking de conjuntos con su calidad, el cambio y la tendencia de 12 semanas.
- Veo las fuentes con más incidentes de los últimos 90 días y los tipos de inconsistencia por
  semana.

**HU-20 · Ver el calendario de ejecución de la herramienta** (Should · O6)

Como Especialista de Monitoreo Multifuente, quiero ver en un calendario qué días se ejecutó la
herramienta de calidad, para detectar días sin validación.

- Cada día indica si se ejecutó, si no se ejecutó o si es una fecha futura.
- Al seleccionar un día veo cuántas ejecuciones tuvo.

**HU-21 · Explorar una variable en un rango de fechas** (Should · O6)

Como Analista de Calidad Operativa, quiero consultar si una variable es correcta en un rango de
fechas, para responder rápido a quien pregunte por un dato.

- La respuesta indica «Correcto», «Con errores de calidad» o «Sin publicar», con una explicación y
  un enlace al incidente cuando existe.
- La gráfica marca el punto con error.

### 5.8 Épica 7: Configuración de conjuntos y conexiones

**HU-22 · Consultar y pausar conjuntos configurados** (Must · O2)

Como Ingeniero de Configuración y Metadatos, quiero ver el catálogo de conjuntos con su tema,
fuentes, periodicidad, fechas de validación, última modificación y advertencias, para saber si un
conjunto ya existe antes de crearlo.

- Puedo activar o pausar un conjunto sin afectar la ejecución de los demás.
- La pausa registra quién la hizo y cuándo.

**HU-23 · Crear una variable con el asistente** (Must · O2)

Como Ingeniero de Configuración y Metadatos, quiero un asistente de cuatro pasos (datos generales,
conexión, reglas de calidad y ejecución), para dejar de editar CSV y consultas SQL a mano.

- La fecha inicial de validación no puede ser posterior a la final.
- La consulta usa el parámetro `:fecha_indexada`, de modo que no hay que editarla para recargar
  históricos.
- La prueba de conexión se ejecuta contra la fuente real y muestra el número de filas o el error.
- La fuente alterna FTP es opcional.
- No se puede guardar una variable nueva sin una prueba en seco exitosa.
- Al guardar, la variable aparece activa en el catálogo y se valida en la siguiente ejecución.

**HU-24 · Editar una variable y conservar el historial** (Must · O2, O8)

Como Ingeniero de Configuración y Metadatos, quiero editar una variable existente sin perder los
datos que no cambio, para ajustar la configuración con seguridad.

- El asistente se abre con los valores actuales.
- Al guardar, se registra el valor anterior y el nuevo de cada campo modificado, con usuario y
  fecha.
- Puedo volver a una versión anterior de la configuración.

**HU-25 · Corregir configuraciones con advertencia** (Should · O2)

Como Ingeniero de Configuración y Metadatos, quiero que la herramienta detecte configuraciones
desactualizadas, para evitar falsas alertas.

- Se detectan al menos: tabla renombrada en la consulta, delta temporal sin revertir y ruta FTP
  inexistente.
- Cada advertencia ofrece la acción correspondiente (revertir delta o aplicar corrección) y su
  resultado queda en Trazabilidad.

**HU-26 · Gestionar las credenciales de las fuentes** (Must · O2)

Como Ingeniero de Configuración y Metadatos, quiero administrar los accesos a Oracle, API, Data Lake,
FTP y archivos compartidos, para que las conexiones no fallen por credenciales vencidas.

- Las contraseñas se guardan en un gestor de secretos y nunca se muestran ni se registran en claro.
- Una contraseña nueva debe tener al menos 8 caracteres.
- Puedo validar el acceso a la fuente y renovar la credencial.
- Solo los usuarios con rol de configuración pueden ver y editar esta vista.

### 5.9 Épica 8: Trazabilidad

**HU-27 · Consultar el historial de hallazgos** (Must · O8)

Como Analista de Calidad Operativa, quiero consultar todos los hallazgos con su tipo, origen, fecha
de indexación, detección, resolución, responsable y estado, para saber cómo se atendió cada uno.

- Puedo buscar por identificador, conjunto o causa y filtrar por tipo, criticidad y estado.
- Los filtros activos se muestran y se pueden quitar uno por uno.
- Al abrir un hallazgo, veo su detalle, puedo asignarlo y vuelvo a Trazabilidad con un botón.
- Un conjunto con hallazgos repetidos en el mes muestra cuántas veces ocurrió.

**HU-28 · Administrar el catálogo de inconsistencias** (Should · O7 · _mejora_)

Como Ingeniero de Configuración y Metadatos, quiero un catálogo de tipos de inconsistencia con su
causa raíz, criticidad e impacto, para clasificar los hallazgos de forma uniforme.

- Cada hallazgo se clasifica con un tipo del catálogo.
- Puedo crear, editar y desactivar tipos sin perder la clasificación de los hallazgos anteriores.

**HU-29 · Exportar un reporte de evidencia** (Should · O8)

Como Analista de Calidad Operativa, quiero exportar los hallazgos filtrados, para entregar evidencia
a otras áreas.

- El reporte incluye los mismos filtros que la tabla y se descarga en CSV o Excel.

### 5.10 Épica 9: Requisitos transversales

**HU-30 · Recibir notificaciones en la aplicación** (Should · O1)

Como Analista de Calidad Operativa, quiero ver las alertas recientes en la campana de
notificaciones, para enterarme sin salir de la vista en la que trabajo.

- La campana indica cuando hay notificaciones nuevas.
- Cada notificación abre el incidente correspondiente.

**HU-31 · Ingresar con mi usuario corporativo y mi rol** (Must)

Como usuario de la herramienta, quiero ingresar con mi cuenta corporativa, para que mis acciones
queden registradas a mi nombre y solo vea lo que me corresponde.

- El ingreso usa el inicio de sesión único de la organización.
- Existen al menos los roles de consulta, gestión de incidentes y configuración.
- Toda acción que modifica datos o configuración registra usuario, fecha y hora.

**HU-32 · Usar la herramienta con teclado y en tema claro u oscuro** (Could)

Como usuario de la herramienta, quiero navegar con el teclado y elegir el tema, para trabajar con
menos clics y menos fatiga visual.

- Los atajos 1 a 8 abren las vistas y Esc cierra paneles y menús.
- El tema elegido se conserva entre sesiones.
- La interfaz cumple el nivel AA de las pautas de accesibilidad WCAG 2.1.

### 5.11 Consideraciones para la implementación real

- **Integraciones:** las acciones simuladas en el PF requieren conexión real con Oracle, la API de
  XM, el Data Lake, el FTP alterno, Microsoft Teams y la mesa de ayuda.
- **Datos:** los indicadores, la matriz de versiones y la validación deben calcularse con datos
  reales; los valores del PF son de ejemplo.
- **Regulación:** los plazos de las versiones de liquidación del PF son de ejemplo y deben tomarse
  de la regulación vigente.
- **Definición de terminado:** cada historia se considera terminada cuando cumple sus criterios de
  aceptación, registra sus acciones en Trazabilidad y supera una prueba con al menos un usuario de
  la persona correspondiente.

## 6. Conclusión final y trabajo futuro

### 6.1 Conclusión final

El proyecto partió de un problema concreto: el equipo que administra la calidad de los datos del
SIMEM detecta y corrige las inconsistencias revisando correos, archivos CSV, consultas SQL y varias
herramientas a la vez, sin distinguir con claridad un dato atrasado de uno erróneo ni saber quién
atiende cada caso. A lo largo de las cinco partes anteriores, ese problema se caracterizó, se
investigó con los usuarios, se sintetizó en tres personas y una declaración del problema, se
exploró con tres prototipos y se evaluó con pruebas de usabilidad.

El prototipo final reúne lo que mejor funcionó en cada etapa. Conserva de P2 el ciclo completo de
detectar, asignar, corregir y verificar, que obtuvo el mejor resultado SUS (80 puntos). Incorpora de
P3 la vista general y la lectura clara de atrasos y versiones, y de P1 el asistente guiado que fue
el único en permitir crear una conexión nueva. Además, responde a las oportunidades de mejora de la
Parte V: muestra solo las inconsistencias en la validación, separa la reejecución de la validación
de la recarga de datos, hace visible la asignación de responsables y cubre la creación de
conexiones y conjuntos de punta a punta.

| Objetivo | P2 | PF |
| :--- | :---: | :---: |
| O1 Centralizar inconsistencias | ● | ● |
| O2 Configurar conjuntos | ◐ | ● |
| O3 Oportunidad y relanzamiento masivo | ● | ● |
| O4 Versiones de la liquidación | ● | ● |
| O5 Indicadores de calidad | ● | ● |
| O6 Evolución en el tiempo | ◐ | ◐ |
| O7 Clasificar inconsistencias | ◐ | ◐ |
| O8 Trazabilidad | ● | ● |

_Leyenda: ● cubre, ◐ cubre parcialmente. La cobertura de P2 en O2 es la ajustada en la Parte V,
sección 8. La cobertura del PF es una estimación de diseño que aún no se ha validado con usuarios._

O6 y O7 siguen siendo parciales: el PF amplía la historia disponible (validación histórica de hasta
366 días y explorador de variable) y clasifica los hallazgos por tipo, origen, causa raíz y
recurrencia, pero no permite comparar periodos ni administrar un catálogo de inconsistencias.

### 6.2 Trabajo futuro

1. **Evaluar el PF con usuarios.** Repetir las siete tareas de la Parte V con los tres
   participantes y aplicar SUS, registrando esta vez de forma sistemática el tiempo por tarea, la
   tasa de éxito, los errores y las solicitudes de ayuda (limitación de la sección 7.4 de la
   Parte V).
2. **Implementar las historias Must.** Construir primero las historias Must del backlog, con
   integraciones reales a Oracle, la API de XM, el Data Lake, el FTP alterno y Teams.
3. **Completar O7.** Diseñar el catálogo de inconsistencias con causa raíz, criticidad e impacto
   (HU-28).
4. **Completar O6.** Agregar la comparación entre periodos y tendencias de largo plazo.
5. **Gestión por responsable.** Agregar la vista «Mis incidentes» (HU-08), acuerdos de tiempo de
   respuesta por criticidad y escalamiento de incidentes sin dueño.
6. **Seguridad y roles.** Definir los roles, el inicio de sesión único y el gestor de secretos para
   las credenciales (HU-26 y HU-31).
7. **Accesibilidad.** Auditar la interfaz frente a WCAG 2.1 nivel AA.
8. **Predicción de incidentes.** Cuando exista suficiente histórico, explorar la anticipación de
   atrasos y errores recurrentes, funcionalidad que se dejó como Won't en la Parte IV.

---

<a id="referencias"></a>

# Referencias bibliográficas

[1] Vaidyambath, R., Debattista, J., Srivatsa, N., & Brennan, R. (2019). _An Intelligent Linked
Data Quality Dashboard_. ADAPT Centre, School of Computing, Dublin City University; TopQuadrant;
Northern Kentucky University. Disponible en:
https://doras.dcu.ie/24121/1/AICSDashboardv02-cameraReady.pdf

[2] Abdelaal, M., Lokadjaja, S., Kreuz, A., & Schöning, H. (2025). _DataLens: ML-Oriented
Interactive Tabular Data Quality Dashboard_. arXiv preprint arXiv:2501.17074. Disponible en:
https://arxiv.org/abs/2501.17074

[3] F. Ridzuan and W. M. N. Wan Zainon, "A Review on Data Quality Dimensions for Big Data,"
Procedia Computer Science, vol. 234, pp. 341–348, 2024, doi: 10.1016/j.procs.2024.03.008.
Disponible en: https://www.sciencedirect.com/science/article/pii/S187705092400365X?via%3Dihub

[4] M. Souibgui, F. Atigui, S. Zammali, S. Cherfi, and S. Ben Yahia, "Data quality in ETL process:
A preliminary study," Procedia Computer Science, vol. 159, pp. 676–687, 2019, doi:
10.1016/j.procs.2019.09.222. Disponible en:
https://www.sciencedirect.com/science/article/pii/S1877050919314097

[5] B. G. da S. Cezar and A. C. G. Maçada, "Data literacy and the cognitive challenges of a
data-rich business environment: an analysis of perceived data overload, technostress and their
relationship to individual performance," Aslib Journal of Information Management, vol. 73, no. 5,
pp. 618–638, Jul. 2021, doi: 10.1108/AJIM-01-2021-0015. Disponible en:
https://www.sciencedirect.com/org/science/article/abs/pii/S2050380621000235

Las fuentes de la investigación competitiva (documentación oficial de Monte Carlo, Soda, Great
Expectations, Microsoft Purview, Azure Data Factory, Grafana, Atlassian Statuspage, PagerDuty y
GitHub) se citan en línea en las secciones 4.3 y 4.4 de la Parte III, consultadas el 20 de
septiembre de 2026.

[^literacidad]: Es la capacidad de una persona para buscar, comprender, evaluar, crear y utilizar
    información mediante tecnologías digitales de manera crítica, segura y responsable.

[^abismo-ejecucion]: Abismo de Ejecución: la dificultad de hacer que el sistema haga lo que
    quiero. Don Norman.

[^abismo-evaluacion]: Abismo de Evaluación: la dificultad de saber si el sistema hizo lo que le
    pedí. Don Norman.

[^creg]: Los conjuntos de datos regulatorios están definidos en la resolución CREG 101 018 del
    2022, por la cual se crea el Sistema de Información del Mercado de Energía Mayorista, SIMEM.
    Estos tienen fechas exactas en las que se debe publicar la información. En caso contrario
    pueden existir sanciones por incumplimiento de la normatividad.
