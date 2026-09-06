<link
  rel="stylesheet"
  href="https://cdn.jsdelivr.net/gh/dracula/markdown-css/dracula-markdown.css"
/>
<hr style="border:2px solid #CC00FF"> </hr>
<a><img src="https://www.vhv.rs/dpng/d/313-3134285_logo-de-la-universidad-nacional-de-colombia-png.png" width="100" align="center"></a>
<a><img src="https://minaslap.net/pluginfile.php/1/core_admin/logo/0x200/1770226238/Logo%20MinasLAP-3%20%281%29.png" width="100" align="center"></a>
<h1><center>Interacción Humano-Computador</center></h1>
<h2><center>Introducción a la Interacción Humano-Computador</center></h2>
<h3><center>Entregable #1</center></h3>

<a name="conte"></a>

<hr style="border:2px solid #CC00FF"> </hr>

**Elaborado por:** _Milena Castaño_ & _Daniela Torres_ & _Sebastian Sanchez_ & _Kevin Hidalgo_

**Correos:** _correo@unal.edu.co_ & _datorresgom@unal.edu.co_ & _correo@unal.edu.co_ &
_kfhidalgoh@unal.edu.co_

**Fecha de elaboración:** _2026 Septiembre 02_

**Fecha última modificación:** _2026 Septiembre 02_

_Nota: Este entregable tiene como objetivo detallar el problema desde la perspectiva de Interacción
Humano-Computador (IHC). Recuerda identificar y referenciar trabajos previos usando Google Scholar
o bases de datos como Scopus, IEEE o Science Direct._

---

## 1. Descripción del Problema

### Paso 1: Contextualización del problema

**¿Dónde y cuándo ocurre el problema?** _Instrucción: Describe el entorno específico en el que se
presenta el problema (por ejemplo, una aplicación móvil, un sistema de escritorio, un sitio web,
dispositivos de asistencia para personas con discapacidades, etc.)._

El problema se presenta en SIMEM (simem.co), una plataforma web de datos abiertos que pone a disposición de usuarios internos y externos información relacionada con el Mercado de Energía Mayorista (MEM) y la operación del Sistema Interconectado Nacional (SIN).

La plataforma ofrece acceso a los datos mediante consultas web y una API pública, la cual es utilizada por diferentes tipos de usuarios para realizar análisis, desarrollos tecnológicos y procesos de toma de decisiones. La información publicada se alimenta desde un Data Lake, que recibe aproximadamente un millón de registros diarios provenientes de múltiples fuentes de información, incluyendo bases de datos transaccionales, archivos Excel, APIs y otros sistemas de la organización.

Actualmente, existen mecanismos para monitorear la ejecución de los procesos de carga hacia el Data Lake y hacia SIMEM. Sin embargo, estos controles se enfocan principalmente en verificar la finalización técnica de los procesos y no en validar integralmente la calidad, completitud, oportunidad, consistencia y confiabilidad de los datos publicados.

Como consecuencia, pueden presentarse situaciones en las que los datos son cargados exitosamente desde el punto de vista técnico, pero contienen errores o inconsistencias que pasan desapercibidos para los administradores de la plataforma. Entre los problemas más frecuentes se encuentran registros erróneos, valores atípicos, retrasos en las publicaciones y pérdida de información histórica. En numerosos casos, estas situaciones son identificadas únicamente cuando los usuarios consumen la información y reportan novedades a través de los canales de atención (CRM), generando un aumento en los requerimientos gestionados por el equipo administrador y afectando la confianza de los usuarios en la plataforma.

Uno de los escenarios más críticos corresponde a la ausencia de versiones específicas de información que deben publicarse de manera secuencial. Por ejemplo, algunas variables asociadas a los procesos de liquidación del mercado cuentan con distintas versiones publicadas en momentos diferentes. Puede ocurrir que la primera versión de una liquidación (TX1 versión preliminar) sea cargada correctamente, mientras que la versión que sale 2 días después (TX2) no sea incorporada al Data Lake. La recuperación de estas versiones faltantes representa un reto operativo significativo, ya que en muchos casos las versiones históricas dejan de estar disponibles en las bases de datos fuente. Para reconstruirlas es necesario acudir a repositorios alternos, como servidores FTP, y ejecutar procesos manuales de búsqueda, validación y cargue, los cuales consumen tiempo, requieren conocimiento especializado y aumentan el riesgo de errores operativos.

Otro problema recurrente está relacionado con la pérdida de sincronización entre la fecha de publicación esperada y la fecha real de los datos disponibles. Por ejemplo, existen variables que deben publicar diariamente la información correspondiente al día inmediatamente anterior, por ejemplo, el Precio de bolsa del mercado. Si por una intermitencia una ejecución no incorpora los datos esperados, el proceso puede continuar ejecutándose sin errores aparentes, pero publicando información desactualizada. En este escenario, los administradores observan que las cargas continúan ejecutándose correctamente, cuando en realidad los usuarios están consultando datos con uno o varios días de retraso. Esta situación puede mantenerse durante largos períodos sin ser detectada.

Esta limitación es aún más evidente en los conjuntos de datos con actualizaciones esporádicas, ya que actualmente no existe una vista consolidada que permita conocer la frecuencia esperada de publicación, la última actualización realizada o la existencia de posibles retrasos e incumplimientos.

Adicionalmente, la plataforma carece de una capa de analítica y visualización (BI) que permita monitorear el comportamiento de los datos de forma gráfica e intuitiva. La información disponible se encuentra principalmente en formatos estructurados, lo que dificulta la identificación temprana de tendencias inusuales.

Como resultado, los responsables de la plataforma carecen de una visión centralizada y proactiva sobre la calidad y el estado de los datos publicados, lo que limita su capacidad para detectar problemas antes de que impacten a los usuarios finales.


**Antecedentes** _Instrucción: Menciona brevemente los sistemas actuales o las soluciones previas
que existen en el ámbito del problema. Esto puede incluir una breve revisión de trabajos previos,
investigaciones o proyectos que hayan intentado abordar el problema._

Actualmente, los administradores de la plataforma cuentan con una herramienta desarrollada en Python para realizar validaciones de consistencia entre los datos de las fuentes originales y los datos almacenados en el Data Lake de SIMEM. La validación se hace posterior a la carga de información del sistema, aunque también se puede ejecutar para validar datos históricos a demanda. La configuración de los conjuntos de datos a evaluar se hace a través de un archivo .CSV. 

Cuando la herramienta identifica diferencias o inconsistencias durante las validaciones ejecutadas, genera automáticamente una notificación por correo electrónico dirigida a los administradores de la plataforma. Adicionalmente, los hallazgos detectados son almacenados en archivos .CSV para su posterior revisión.

Además, el sistema cuenta con metadatos de cada uno de los conjuntos como son: última fecha de actualización, si la última ejecución fue exitosa o no, qué fechas indexadas se cargaron con cada ejecución, la fecha indexada máxima disponible, perioridicidad (diario, semanal, mensual, trimestral, semestral, anual),la clasificación (si carga datos del día anterior, de la semana siguiente, del mes en curso, etc) y la próxima fecha de ejecución programada. 

Sin embargo, a día de hoy no existe una plataforma centralizada que permita consolidar los hallazgos, visualizar tendencias, generar indicadores o medir la evolución de la calidad de los datos a lo largo del tiempo. 

Adicionalmente, no se dispone de un catálogo o repositorio estructurado de inconsistencias que permita clasificarlas según su tipología, impacto, criticidad o causa raíz. Esto limita la capacidad de identificar patrones recurrentes, priorizar acciones de mejora y construir una visión global de la calidad de los datos publicados.

**Artículos Académicos:**

Como parte del análisis de antecedentes y soluciones existentes en el ámbito de la calidad de datos, se revisaron los siguientes artículos:

__An Intelligent Linked Data Quality Dashboard__  [**1**](#art_1). En este trabajo los autores plantean la siguiente pregunta de investigación: 

> ¿En qué medida un dashboard inteligente, basado en grafos de conocimiento y análisis de causa raíz, puede ayudar a los usuarios a comprender los problemas de calidad de los datos, identificar las correcciones necesarias y priorizar las acciones de mejora?

Para abordar esta problemática, en el artículo proponen un dashboard enfocado en facilitar la comprensión y gestión de los problemas de calidad de datos mediante mecanismos visuales. Las funcionalidades más relevantes son:

1. Visualización de problemas por métrica: Mecanismos que les permitan evaluar el estado de calidad de los datos de forma periódica y sistemática. 
2. Indicadores visuales y tableros de control: Necesarios para que los usuarios pueden conocer rápidamente el estado de salud de la información.
3. Priorización de hallazgos: El sistema organiza automáticamente los problemas según su impacto sobre la calidad del conjunto de datos.
4. Múltiples vistas de análisis: Incluye vistas por recurso y por tipo de problema. 
5. Análisis de causa raíz: Servicios que relacionan las métricas, los datos afectados y los reportes de errores. A partir de estas relaciones se aplican técnicas de análisis de causa raíz para identificar conexiones entre diferentes problemas y determinar su origen común. 
6. Caracterización del impacto global de una anomalía: Los defectos encontrados no se muestran de forma aislada, sino dentro del contexto de otros problemas relacionados.


__DataLens: ML-Oriented Interactive Tabular Data Quality Dashboard__ [**2**](#art_2). Este artículo presenta **DataLens**, una plataforma orientada a la administración de la calidad de datos mediante un dashboard interactivo. Tiene dos módulos que destacan y que son diferentes al propuesto por el artículo de Vaidyambath:

1. Módulo de limpieza iterativa con ML: La plataforma incluye un mecanismo de limpieza iterativa, capaz de seleccionar automáticamente las herramientas o técnicas de limpieza más apropiadas para mejorar la calidad de los datos. 

2. Visualización gráfica de inconsistencias: Generación automática de visualizaciones que muestran la distribución de errores detectados en el conjunto de datos. Con esto identificar: 

* Qué atributos presentan más inconsistencias.
* Qué tipos de errores son más frecuentes.
* Cuáles hallazgos fueron detectados automáticamente.
* Cuáles observaciones fueron reportadas por usuarios.


---

### Paso 2: Identificación de los usuarios afectados

**¿Quiénes son los usuarios principales?** _Instrucción: Define claramente quiénes son los usuarios
afectados por el problema. Esto incluye la descripción de su perfil (por ejemplo, usuarios novatos,
expertos, personas con discapacidad, etc.)._

> [Escribe tu respuesta aquí...]

**¿Cómo interactúan estos usuarios con el sistema?** _Instrucción: Explica las tareas o actividades
que los usuarios realizan con el sistema y cómo la interacción actual les resulta ineficiente o
frustrante._

> [Escribe tu respuesta aquí...]

---

### Paso 3: Definición de las necesidades no satisfechas

**¿Qué necesitan los usuarios?** _Instrucción: Enumera las necesidades o expectativas que los
usuarios tienen, las cuales no están siendo atendidas por las interfaces o sistemas actuales. Esto
puede incluir facilidad de uso, rapidez, accesibilidad, personalización, etc._

> [Escribe tu respuesta aquí...]

**Problemas actuales** _Instrucción: Expón los problemas que surgen debido a las deficiencias de
las interfaces actuales (por ejemplo, dificultades de navegación, sobrecarga de información,
problemas de accesibilidad para personas con discapacidades)._

> [Escribe tu respuesta aquí...]

---

### Paso 4: Impacto del problema

**Consecuencias para los usuarios** _Instrucción: Explica cómo este problema afecta negativamente a
los usuarios. Esto puede incluir aspectos como baja productividad, frustración, errores frecuentes,
abandono del sistema, o incluso consecuencias más graves como exclusión digital._

> [Escribe tu respuesta aquí...]

**Impacto en la organización o contexto** _Instrucción: Si es relevante, también puedes mencionar
cómo el problema afecta a la organización, empresa o comunidad que usa el sistema (por ejemplo,
pérdida de clientes, costes adicionales, insatisfacción general)._

> [Escribe tu respuesta aquí...]

---

### Paso 5: Objetivos del proyecto

**Qué se quiere lograr** _Instrucción: Establece claramente los objetivos que esperas cumplir al
resolver el problema. Estos deben ser concretos y medibles (por ejemplo, mejorar la tasa de éxito
en tareas específicas, reducir los errores, aumentar la satisfacción de los usuarios)._

El aplicativo debe ser capaz de responder preguntas como:

* ¿Cuántas inconsistencias se presentan por período?
* ¿Cuáles son las fuentes de datos con mayor cantidad de errores?
* ¿Qué tipos de inconsistencias ocurren con mayor frecuencia y cuándo?
* ¿Cuánto tiempo tarda la resolución de una inconsistencia?
* ¿Cuáles hallazgos ya fueron gestionados y cuáles permanecen pendientes?
* ¿Qué conjuntos están atrasados en las cargas y por cuanto tiempo han estado así?
* ¿Los conjuntos versionados disponen de todas las versiones disponibles?
* ¿Cuál es el porcentaje global de calidad de datos del sitio y por conjunto de datos?
* ¿Cómo puedo ver gráficamente una variable para identificar tendencias?
* Ejemplo: ¿Los vertimientos del embalse ESMERALDA están correctos para el día 2026-09-01 o hay errores de calidad?

**Objetivos:**

Diseñar e implementar una plataforma de monitoreo, observabilidad y gestión de calidad de datos para el **Sistema de Información del Mercado de Energía Mayorista (SIMEM)** que permita detectar oportunamente anomalías e inconsistencias, facilitar su análisis y seguimiento, y mejorar la confiabilidad de la información publicada a los usuarios internos y externos. 

La plataforma debe contar con las siguientes características:

1. Centralizar la gestión de inconsistencias de calidad de datos
2. Módulo de configuración de nuevos conjuntos de datos a ser evaludados por la herramienta 
3. Monitoreo de la oportunidad de publicación de los conjuntos de datos y con posibilidad de relanzar masivamente los que estén atrasados.
4. Verificador de la completitud de los conjuntos de datos de la liquidación del mercado de energía y si cuentan con todas sus versiones.
5. Implementar indicadores y métricas de calidad de sistema, tanto global como por conjunto de datos.
6. Visualizar la evolución de la calidad de los datos en el tiempo, facilitando la identificación de tendencias,
7. Caracterizar y clasificar las inconsistencias detectadas, identificando su tipología, frecuencia, criticidad, origen e impacto.
8. Proporcionar trazabilidad de los hallazgos.


---

## Referencias Bibliográficas

_Instrucción: Agrega aquí las referencias de los trabajos previos consultados en Google Scholar,
Scopus, IEEE, Science Direct, etc._

<a id="art_1"></a>
**[1]** Vaidyambath, R., Debattista, J., Srivatsa, N., & Brennan, R. (2019). *An Intelligent Linked Data Quality Dashboard*. ADAPT Centre, School of Computing, Dublin City University; TopQuadrant; Northern Kentucky University. Disponible en: https://doras.dcu.ie/24121/1/AICSDashboardv02-cameraReady.pdf

<a id="art_2"> [1] </a>
**[2]** Abdelaal, M., Lokadjaja, S., Kreuz, A., & Schöning, H. (2025). *DataLens: ML-Oriented Interactive Tabular Data Quality Dashboard*. arXiv preprint arXiv:2501.17074. Disponible en: https://arxiv.org/abs/2501.17074
