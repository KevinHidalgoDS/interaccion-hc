<hr style="border:2px solid #CC00FF"> </hr>
<a><img src="https://www.vhv.rs/dpng/d/313-3134285_logo-de-la-universidad-nacional-de-colombia-png.png" width="100" align="center"></a>
<a><img src="https://minaslap.net/pluginfile.php/1/core_admin/logo/0x200/1770226238/Logo%20MinasLAP-3%20%281%29.png" width="100" align="center"></a>
<h1><center>Interacción Humano-Computador</center></h1>
<h2><center>Introducción a la Interacción Humano-Computador</center></h2>
<h3><center>Entregable #1 Caracterización del problema</center></h3>

<a name="conte"></a>

<hr style="border:2px solid #CC00FF"> </hr>

**Elaborado por:** _Milena Castaño_ & _Daniela Torres_ & _Sebastian Sanchez_ & _Kevin Hidalgo_

**Correos:** _lmcastanoh@unal.edu.co_ & _datorresgom@unal.edu.co_ & _sebsanchezar@unal.edu.co_ &
_kfhidalgoh@unal.edu.co_

**Grupo:** 5

**Fecha de elaboración:** _2026 Septiembre 02_

**Fecha última modificación:** _2026 Septiembre 06_

---

## 1. Descripción del Problema

### Paso 1: Contextualización del problema

**¿Dónde y cuándo ocurre el problema?**

> El problema se presenta en el _Sistema de información para el Mercado de Energía Mayorista_
> [SIMEM](https://www.simem.co), una plataforma web de datos abiertos que pone a disposición de
> usuarios internos y externos información relacionada con el Mercado de Energía Mayorista (_MEM_)
> y la operación del Sistema Interconectado Nacional (_SIN_).
>
> La plataforma ofrece acceso a los datos mediante consultas web y una Interfaz de Programación de
> Aplicaciones (_API_) pública, la cual es utilizada por diferentes tipos de usuarios para realizar
> análisis, desarrollos tecnológicos y procesos de toma de decisiones. La información publicada se
> alimenta desde un lago de datos (_dataLake_), que recibe aproximadamente un millón de registros
> diarios provenientes de múltiples fuentes de información, incluyendo bases de datos
> transaccionales, archivos _Excel_, _API's_ y otros sistemas de la organización. Actualmente, existen
> mecanismos para monitorear la ejecución de los procesos de carga hacia el _dataLake_ y hacia
> _SIMEM_. Sin embargo, estos controles se enfocan principalmente en verificar la finalización
> técnica de los procesos y no en validar integralmente la calidad, completitud, oportunidad,
> consistencia y confiabilidad de los datos publicados.
>
> Como consecuencia, pueden presentarse situaciones en las que los datos son cargados exitosamente
> desde el punto de vista técnico, pero contienen errores o inconsistencias que pasan
> desapercibidos para los administradores de la plataforma. Entre los problemas más frecuentes se
> encuentran registros erróneos, valores atípicos, retrasos en las publicaciones y pérdida de
> información histórica. En numerosos casos, estas situaciones son identificadas únicamente cuando
> los usuarios consumen la información y reportan novedades a través de los canales de atención _CRM_
> (Customer Relationship Management o Gestión de Relaciones con el Cliente), generando un aumento
> en los requerimientos gestionados por el equipo administrador y afectando la confianza de los
> usuarios en la plataforma. Uno de los escenarios más críticos corresponde a la ausencia de
> versiones específicas de información que deben publicarse de manera secuencial. Por ejemplo,
> algunas variables asociadas a los procesos de liquidación del mercado cuentan con distintas
> versiones publicadas en momentos diferentes. Puede ocurrir que la primera versión de una
> liquidación (TX1 versión preliminar) sea cargada correctamente, mientras que la versión que sale
> 2 días después (TX2) no sea incorporada al Data Lake. La recuperación de estas versiones
> faltantes representa un reto operativo significativo, ya que en muchos casos las versiones
> históricas dejan de estar disponibles en las bases de datos fuente.
>
> Para reconstruirlas es necesario acudir a repositorios alternos, como servidores FTP (File
> Transfer Protocol o Protocolo de Transferencia de Archivos), y ejecutar procesos manuales de
> búsqueda, validación y cargue, los cuales consumen tiempo, requieren conocimiento especializado y
> aumentan el riesgo de errores operativos. Otro problema recurrente está relacionado con la
> pérdida de sincronización entre la fecha de publicación esperada y la fecha real de los datos
> disponibles. Por ejemplo, existen variables que deben publicar diariamente la información
> correspondiente al día inmediatamente anterior, por ejemplo, el precio de bolsa del mercado. Si
> por una intermitencia una ejecución no incorpora los datos esperados, el proceso puede continuar
> ejecutándose sin errores aparentes, pero publicando información desactualizada. En este
> escenario, los administradores observan que las cargas continúan ejecutándose correctamente,
> cuando en realidad los usuarios están consultando datos con uno o varios días de retraso. Esta
> situación puede mantenerse durante largos períodos sin ser detectada. Esta limitación es aún más
> evidente en los conjuntos de datos con actualizaciones esporádicas, ya que actualmente no existe
> una vista consolidada que permita conocer la frecuencia esperada de publicación, la última
> actualización realizada o la existencia de posibles retrasos e incumplimientos.
>
> Adicionalmente, la plataforma carece de una capa de analítica y visualización _BI_ (Business
> Intelligence) que permita monitorear el comportamiento de los datos de forma gráfica e intuitiva.
> La información disponible se encuentra principalmente en formatos estructurados, lo que dificulta
> la identificación temprana de tendencias inusuales. Como resultado, los responsables de la
> plataforma carecen de una visión centralizada y proactiva sobre la calidad y el estado de los
> datos publicados, lo que limita su capacidad para detectar problemas antes de que impacten a los
> usuarios finales.

**Antecedentes:**

> Actualmente, los administradores de la plataforma cuentan con una herramienta desarrollada en
> Python para realizar validaciones de consistencia entre los datos de las fuentes originales y los
> datos almacenados en el Data Lake de SIMEM. La validación se hace posterior a la carga de
> información del sistema, aunque también se puede ejecutar para validar datos históricos a
> demanda. La configuración de los conjuntos de datos a evaluar se hace a través de un archivo
> `.CSV`. Cuando la herramienta identifica diferencias o inconsistencias durante las validaciones
> ejecutadas, genera automáticamente una notificación por correo electrónico dirigida a los
> administradores de la plataforma. Adicionalmente, los hallazgos detectados son almacenados en
> archivos `.CSV` para su posterior revisión.
>
> Además, el sistema cuenta con metadatos de cada uno de los conjuntos como son: última fecha de
> actualización, si la última ejecución fue exitosa o no, qué fechas indexadas se cargaron con cada
> ejecución, la fecha indexada máxima disponible, periodicidad (diario, semanal, mensual,
> trimestral, semestral, anual), la clasificación (si carga datos del día anterior, de la semana
> siguiente, del mes en curso, etc) y la próxima fecha de ejecución programada. Sin embargo, a día
> de hoy no existe una plataforma centralizada que permita consolidar los hallazgos, visualizar
> tendencias, generar indicadores o medir la evolución de la calidad de los datos a lo largo del
> tiempo. Adicionalmente, no se dispone de un catálogo o repositorio estructurado de
> inconsistencias que permita clasificarlas según su tipología, impacto, criticidad o causa raíz.
> Esto limita la capacidad de identificar patrones recurrentes, priorizar acciones de mejora y
> construir una visión global de la calidad de los datos publicados.
>
> **Artículos Académicos:** Como parte del análisis de antecedentes y soluciones existentes en el
> ámbito de la calidad de datos, se revisaron los siguientes artículos: **An Intelligent Linked
> Data Quality Dashboard** **[1]**. En este trabajo los autores plantean la siguiente pregunta de
> investigación: ¿En qué medida un dashboard inteligente, basado en grafos de conocimiento y
> análisis de causa raíz, puede ayudar a los usuarios a comprender los problemas de calidad de los
> datos, identificar las correcciones necesarias y priorizar las acciones de mejora? Para abordar
> esta problemática, en el artículo proponen un dashboard enfocado en facilitar la comprensión y
> gestión de los problemas de calidad de datos mediante mecanismos visuales. Las funcionalidades
> más relevantes son:
>
> 1. Visualización de problemas por métrica: Mecanismos que les permitan evaluar el estado de
>    calidad de los datos de forma periódica y sistemática.
> 2. Indicadores visuales y tableros de control: Necesarios para que los usuarios pueden conocer
>    rápidamente el estado de salud de la información.
> 3. Priorización de hallazgos: El sistema organiza automáticamente los problemas según su impacto
>    sobre la calidad del conjunto de datos.
> 4. Múltiples vistas de análisis: Incluye vistas por recurso y por tipo de problema.
> 5. Análisis de causa raíz: Servicios que relacionan las métricas, los datos afectados y los
>    reportes de errores. A partir de estas relaciones se aplican técnicas de análisis de causa
>    raíz para identificar conexiones entre diferentes problemas y determinar su origen común.
> 6. Caracterización del impacto global de una anomalía: Los defectos encontrados no se muestran de
>    forma aislada, sino dentro del contexto de otros problemas relacionados.
>
> **DataLens: ML-Oriented Interactive Tabular Data Quality Dashboard** **[2]**. Este artículo
> presenta **DataLens**, una plataforma orientada a la administración de la calidad de datos
> mediante un dashboard interactivo. Tiene dos módulos que destacan y que son diferentes al
> propuesto por el artículo de Vaidyambath:
>
> 1. Módulo de limpieza iterativa con ML: La plataforma incluye un mecanismo de limpieza iterativa,
>    capaz de seleccionar automáticamente las herramientas o técnicas de limpieza más apropiadas
>    para mejorar la calidad de los datos.
> 2. Visualización gráfica de inconsistencias: Generación automática de visualizaciones que
>    muestran la distribución de errores detectados en el conjunto de datos. Con esto identificar:

---

### Paso 2: Identificación de los usuarios afectados

**¿Quiénes son los usuarios principales?**

> Los usuarios principales son el personal interno de XM (analistas de datos, ingenieros y
> operadores del mercado) encargados de monitorear y velar por la calidad de los datos publicados
> en el portal del [SIMEM](https://www.simem.co) (_Sistema de información para el Mercado de Enegía
> Mayorista_).
>
> **Perfil del usuario:**
>
> - **Conocimiento y experiencia:** Son **usuarios expertos en el dominio** (poseen un alto
>   conocimiento técnico del mercado energético y la estructura de los datos) y tienen una alta
>   literacidad digital[^1]. Sin embargo, no necesariamente son expertos en la adopción de nuevas
>   herramientas de software, por lo que la curva de aprendizaje de la interfaz debe ser baja.
> - **Frecuencia y contexto de uso:** Son usuarios **intensivos/frecuentes**. Su interacción con el
>   sistema es diaria y prolongada. Operan principalmente en entornos de oficina (a menudo con
>   configuraciones de múltiples monitores) para poder cruzar e inspeccionar grandes volúmenes de
>   información simultáneamente.
> - **Carga cognitiva:** Manejan una **alta carga cognitiva**. Su tarea de asegurar la calidad de
>   los datos requiere concentración extrema para identificar anomalías, patrones o valores
>   atípicos, a menudo bajo restricciones de tiempo crítico antes de la publicación oficial.
> - **Accesibilidad y ergonomía:** Debido a las largas jornadas frente a pantallas analizando
>   tablas y tableros de control (dashboards), son altamente susceptibles a la fatiga visual y
>   motora. Requieren interfaces que prioricen la claridad tipográfica en datos numéricos, alto
>   contraste, y atajos de teclado o flujos de trabajo optimizados que minimicen la dependencia de
>   clics repetitivos con el ratón.

**¿Cómo interactúan estos usuarios con el sistema?**

> Actualmente, la interacción no ocurre en una plataforma centralizada, sino a través de un
> ecosistema fragmentado (correo electrónico, hojas de cálculo locales, portal web). El flujo de
> tareas principal consiste en la validación y corrección de datos suministrados por los agentes
> generadores, enfrentando severas deficiencias de usabilidad: **Flujo de interacción actual y sus
> puntos de fricción:**
>
> 1. **Notificación pasiva y descontextualizada:** El sistema ETL notifica los errores mediante
>    correos electrónicos.
>    - Fricción (IHC): **Baja visibilidad del estado del sistema**. El usuario recibe una alerta
>      fuera de contexto, sin un enlace directo o interfaz que lo lleve inmediatamente al entorno
>      del error para su evaluación.
> 2. **Comparación manual de datos (Búsqueda a ciegas):** Al carecer de una interfaz de
>    contrastación (tipo data diffing), el usuario debe buscar manualmente el dato erróneo cruzando
>    la información entregada por el agente con el resultado fallido de la ETL.
>    - Fricción (IHC): **Sobrecarga cognitiva y de la memoria de trabajo**. Obligar al usuario a
>      recordar o cruzar visualmente datos entre múltiples ventanas o archivos genera fatiga visual
>      severa y alta probabilidad de error humano (slips y mistakes).
> 3. **Corrección mediante "Workarounds" (Soluciones informales):** Para corregir el error, el
>    usuario debe extraer el dato, estructurar un archivo CSV de forma manual y redactar un correo
>    al equipo de soporte.
>    - Fricción (IHC): **Alto Abismo de Ejecución (Gulf of Execution)**[^2]. Falta de manipulación
>      directa. El usuario sabe qué quiere corregir, pero el sistema no le da la herramienta para
>      hacerlo por sí mismo, obligándolo a abandonar su flujo de trabajo y usar herramientas de
>      terceros (_Excel/Notepad, Outlook_).
> 4. **Dependencia de terceros y Feedback Asíncrono:** El equipo de soporte actualiza la base de
>    datos y re-ejecuta la ETL. El usuario debe esperar y posteriormente entrar de nuevo al portal
>    _SIMEM_ para validar.
>    - Fricción (IHC): **Abismo de Evaluación (Gulf of Evaluation)[^3] y cuellos de botella**. El
>      ciclo de retroalimentación (feedback loop) está roto. El usuario no recibe confirmación en
>      tiempo real de su acción, generando tiempos muertos, ansiedad y rompiendo por completo la
>      continuidad de la tarea (ruptura del estado de flujo).

---

### Paso 3: Definición de las necesidades no satisfechas

**¿Qué necesitan los usuarios?**

> - **Visibilidad del estado de los datos:** Saber si los datos consultados están correctos,
>   completos y cumplen con los estándares de calidad definidos por la organización.
> - **Agilidad:** No tener que realizar tareas manuales de validación de datos, lo cual permite a
>   los usuarios dedicar el tiempo a la extracción del conocimiento que hay en los datos, el valor
>   del negocio y la interpretación y generación de _insights_.
> - **Alertas proactivas:** Ser notificados de manera automática sobre los errores en los datos,
>   permitiendo así saber con seguridad qué usar y qué no.
> - **Canales eficientes de comunicación y gestión de errores en el _datalake_:** Al tener la
>   calidad de datos centralizada, será más fácil la gestión de _backfills_ para datos faltantes o
>   la implementación de controles o flujos automatizados para la carga de información faltante.
> - **Fuentes de confianza:** El usuario necesita conocer de primera mano la calidad que tienen los
>   datos que está usando, así como la calidad de los procesos de carga de datos desde las fuentes.

**Problemas actuales:**

> - **Inexistencia de un centro de control de calidad de datos unificado:** Al no tener una
>   herramienta unificada de control de calidad de datos y cargas de información, los usuarios no
>   pueden conocer el estado real de la información del _datalake_, lo que genera pérdida de
>   confianza en los datos, gestión reactiva en lugar de preventiva, y adicionalmente no hay
>   gobernanza de datos o trazabilidad clara de los mismos.
> - **Sobrecarga cognitiva por revisión manual:** La inspección de errores de cargas o revisión de
>   calidad de datos se convierte en un problema al ser ejecutado de forma manual, ya que se pueden
>   presentar problemas de errores por omisión, desgaste de los analistas, falta de enfoque en el
>   rol de análisis de información del mercado energético y dependencia de intermediarios.
> - **Procesamiento y análisis lento:** En ocasiones, no se pueden analizar los datos completamente
>   por la falta de personal operativo que revise la calidad de los datos.
> - **Incertidumbre y falta de confianza en los datos:** Al no tener un repositorio centralizado
>   que mida la completitud, consistencia, precisión e integridad de la información, se vuelve
>   difícil confiar plenamente en la información presentada.

---

### Paso 4: Impacto del problema

**Consecuencias para los usuarios:**

> La ausencia de una interfaz centralizada para monitorear la calidad, disponibilidad y estado de
> los datos del _datalake_ genera consecuencias directas sobre las actividades realizadas por los
> analistas, ingenieros y operadores de _XM_. El impacto no se limita únicamente a aspectos técnicos
> relacionados con los datos, sino que también afecta la experiencia de interacción, la eficiencia
> operativa y la capacidad de los usuarios para tomar decisiones oportunas.
>
> - Incremento de la carga cognitiva: Los usuarios deben revisar diferentes fuentes de información,
>   correos electrónicos, archivos CSV, tablas y resultados de procesos de carga para determinar si
>   existe algún problema con los datos. Esta fragmentación obliga al usuario a mantener
>   información en su memoria de trabajo y realizar comparaciones manuales, aumentando el esfuerzo
>   mental requerido para completar una tarea que podría ser soportada directamente por una
>   interfaz.
> - Mayor probabilidad de error humano: La revisión manual de grandes cantidades de información
>   aumenta la posibilidad de omitir inconsistencias, interpretar incorrectamente un dato o no
>   identificar oportunamente un conjunto que no fue actualizado. Esto resulta especialmente
>   relevante cuando existen múltiples conjuntos de datos que deben ser supervisados diariamente.
> - Reducción de la productividad: Una parte del tiempo de los usuarios debe destinarse a
>   localizar, verificar, reportar y hacer seguimiento a errores de calidad o fallos en las cargas.
>   En consecuencia, disminuye el tiempo disponible para actividades de mayor valor, como el
>   análisis del comportamiento del mercado energético, la identificación de tendencias y la
>   generación de conocimiento a partir de los datos.
> - Aumento del tiempo para diagnosticar y resolver errores: La ausencia de un monitor que indique
>   de manera visual qué conjunto presenta problemas, cuál es la causa, desde cuándo ocurre y cuál
>   es su estado de gestión obliga al usuario a investigar manualmente el incidente. Además, cuando
>   la solución depende de comunicaciones por correo electrónico y de la intervención de otros
>   equipos, el ciclo de resolución se prolonga.
> - Pérdida de continuidad en la interacción: El usuario debe cambiar constantemente entre
>   herramientas y contextos —por ejemplo, _SIMEM_, archivos locales, correo electrónico y sistemas
>   internos— para completar una misma tarea. Desde la perspectiva de Interacción
>   Humano-Computador, esta fragmentación interrumpe el flujo de trabajo, aumenta el número de
>   acciones necesarias y dificulta mantener el contexto de la actividad.
> - Incertidumbre sobre la confiabilidad de los datos: Si el usuario no dispone de indicadores
>   visibles sobre completitud, consistencia, precisión, vigencia o estado de carga de un conjunto
>   de datos, no puede determinar rápidamente si la información disponible es suficientemente
>   confiable para utilizarla. Esto puede provocar que los analistas recurran a fuentes
>   alternativas, como archivos `.txt` obtenidos directamente de otros procesos, aunque los datos
>   también se encuentren publicados posteriormente en _SIMEM_.
> - Frustración y disminución de la confianza en el sistema: Cuando los usuarios detectan
>   repetidamente datos faltantes, cargas atrasadas o inconsistencias sin contar con mecanismos
>   claros para identificar su causa y seguimiento, se deteriora la percepción de confiabilidad del
>   sistema. Como resultado, pueden desarrollarse mecanismos de trabajo alternativos o workarounds
>   que reducen aún más la utilización de la plataforma como fuente principal de información.
> - Dificultad para priorizar incidentes: Actualmente, la falta de clasificación visual de los
>   errores y de indicadores de severidad dificulta distinguir rápidamente entre un problema menor
>   y uno que puede afectar de forma importante la disponibilidad o confiabilidad de la
>   información. Esto obliga a los usuarios a evaluar manualmente cada situación antes de
>   determinar su prioridad.

**Impacto en la organización o contexto**

> El problema también tiene repercusiones organizacionales para _XM_, considerando su responsabilidad
> en la administración del Mercado de Energía Mayorista y en la disponibilidad de información
> utilizada por diferentes actores del sector energético.
>
> - Gestión reactiva de la calidad de datos: Al no existir un centro de monitoreo unificado con
>   indicadores, alertas y mecanismos de seguimiento, muchos problemas se gestionan después de ser
>   detectados por un usuario. Esto limita la posibilidad de anticiparse a fallos de carga,
>   conjuntos atrasados o degradaciones progresivas de la calidad.
> - Incremento de los costos operativos: Las actividades manuales de identificación, comunicación,
>   corrección, seguimiento y re-ejecución de procesos consumen tiempo de analistas, ingenieros y
>   equipos de soporte. Tareas que podrían ser detectadas, clasificadas o incluso corregidas
>   automáticamente requieren actualmente intervención humana.
> - Dependencia de personas y conocimiento tácito: Parte del procedimiento para identificar y
>   solucionar problemas puede depender de la experiencia individual de determinados analistas o
>   integrantes del equipo. Esto representa un riesgo operativo debido a que el conocimiento sobre
>   qué revisar, cómo interpretar un error o cómo solicitar una corrección puede no encontrarse
>   centralizado en el sistema.
> - Dificultades de trazabilidad y gobernanza: Sin una plataforma que mantenga el historial de
>   errores, versiones, reglas de calidad, acciones realizadas y responsables de cada incidente,
>   resulta más difícil reconstruir lo ocurrido con un conjunto de datos y determinar cuándo
>   apareció el problema, cómo fue corregido y si volvió a presentarse.
> - Riesgo de publicación o utilización de información incompleta: Una carga tardía, incompleta o
>   incorrecta puede hacer que determinados conjuntos de datos no estén disponibles en el momento
>   esperado. Esto puede afectar los análisis realizados por los equipos internos y por los
>   diferentes agentes del sector que dependen de información confiable y oportuna.
> - Uso de fuentes alternativas y duplicación de esfuerzos: Cuando los datos disponibles en el
>   _datalake_ o en _SIMEM_ no se actualizan oportunamente, algunos usuarios pueden preferir consultar
>   archivos `txt` u otras fuentes que se encuentren disponibles con mayor anticipación. Esto genera
>   duplicidad de procesos, dificulta establecer una única fuente de verdad y reduce el
>   aprovechamiento de la infraestructura de datos existente.
> - Menor capacidad para evaluar el desempeño de la calidad de los datos: La inexistencia de
>   métricas consolidadas impide responder fácilmente preguntas como qué porcentaje de los
>   conjuntos presenta problemas, cuáles son los errores más frecuentes, cuánto tarda su
>   resolución, qué fuentes presentan mayores incidencias o cuál ha sido la evolución de la calidad
>   de los datos a lo largo del tiempo.
>
> En consecuencia, el problema identificado no consiste únicamente en la existencia de errores
> dentro del _datalake_, sino en la dificultad que tienen los usuarios para percibir, comprender,
> diagnosticar y gestionar el estado de calidad de los datos mediante las interfaces y herramientas
> actuales. Desde la perspectiva de la Interacción Humano-Computador, existe una brecha entre la
> información que el sistema posee sobre sus procesos de carga y calidad y la información que
> presenta de manera comprensible y accionable al usuario. Por esta razón, una interfaz de
> monitoreo de calidad de datos permitiría transformar un proceso actualmente fragmentado y
> reactivo en un flujo de trabajo más visible, centralizado y orientado a la toma de decisiones,
> facilitando que los usuarios identifiquen anomalías, comprendan su impacto, prioricen incidentes
> y hagan seguimiento a su resolución desde un único entorno.

---

### Paso 5: Objetivos del proyecto

**¿Qué se quiere lograr?**

> El aplicativo debe ser capaz de responder preguntas como:
>
> - ¿Cuántas inconsistencias se presentan por período?
> - ¿Cuáles son las fuentes de datos con mayor cantidad de errores?
> - ¿Qué tipos de inconsistencias ocurren con mayor frecuencia y cuándo?
> - ¿Cuánto tiempo tarda la resolución de una inconsistencia?
> - ¿Cuáles hallazgos ya fueron gestionados y cuáles permanecen pendientes?
> - ¿Qué conjuntos están atrasados en las cargas y por cuanto tiempo han estado así?
> - ¿Los conjuntos versionados disponen de todas las versiones disponibles?
> - ¿Cuál es el porcentaje global de calidad de datos del sitio y por conjunto de datos?
> - ¿Cómo puedo ver gráficamente una variable para identificar tendencias?
> - Ejemplo: ¿Los vertimientos del embalse ESMERALDA están correctos para el día 2026-09-01 o hay
>   errores de calidad?
>
> **Objetivos:**
>
> Diseñar e implementar una plataforma de monitoreo, observabilidad y gestión de calidad de datos
> para el **Sistema de Información del Mercado de Energía Mayorista (SIMEM)** que permita detectar
> oportunamente anomalías e inconsistencias, facilitar su análisis y seguimiento, y mejorar la
> confiabilidad de la información publicada a los usuarios internos y externos. La plataforma debe
> contar con las siguientes características:
>
> 1. Centralizar la gestión de inconsistencias de calidad de datos
> 2. Módulo de configuración de nuevos conjuntos de datos a ser evaluados por la herramienta
> 3. Monitoreo de la oportunidad de publicación de los conjuntos de datos y con posibilidad de
>    relanzar masivamente los que estén atrasados.
> 4. Verificador de la completitud de los conjuntos de datos de la liquidación del mercado de
>    energía y si cuentan con todas sus versiones.
> 5. Implementar indicadores y métricas de calidad de sistema, tanto global como por conjunto de
>    datos.
> 6. Visualizar la evolución de la calidad de los datos en el tiempo, facilitando la identificación
>    de tendencias,
> 7. Caracterizar y clasificar las inconsistencias detectadas, identificando su tipología,
>    frecuencia, criticidad, origen e impacto.
> 8. Proporcionar trazabilidad de los hallazgos.

---

## Referencias Bibliográficas

[1] Vaidyambath, R., Debattista, J., Srivatsa, N., & Brennan, R. (2019). _An Intelligent Linked
Data Quality Dashboard_. ADAPT Centre, School of Computing, Dublin City University; TopQuadrant;
Northern Kentucky University. Disponible en:
https://doras.dcu.ie/24121/1/AICSDashboardv02-cameraReady.pdf

[2] Abdelaal, M., Lokadjaja, S., Kreuz, A., & Schöning, H. (2025). _DataLens: ML-Oriented
Interactive Tabular Data Quality Dashboard_. arXiv preprint arXiv:2501.17074. Disponible en:
https://arxiv.org/abs/2501.17074

[^1]: Es la capacidad de una persona para buscar, comprender, evaluar, crear y utilizar información
    mediante tecnologías digitales de manera crítica, segura y responsable.

[^2]: Abismo de Ejecución: la dificultad de hacer que el sistema haga lo que quiero. Don Norman

[^3]: Abismo de Evaluación: la dificultad de saber si el sistema hizo lo que le pedí. Don Norman

<!-- Referencia != nota al pie -->
