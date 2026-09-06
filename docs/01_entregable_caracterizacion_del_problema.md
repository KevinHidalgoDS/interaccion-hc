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

**Fecha última modificación:** _2026 Septiembre 04_

_Nota: Este entregable tiene como objetivo detallar el problema desde la perspectiva de Interacción
Humano-Computador (IHC). Recuerda identificar y referenciar trabajos previos usando Google Scholar
o bases de datos como Scopus, IEEE o Science Direct._

---

## 1. Descripción del Problema

### Paso 1: Contextualización del problema

**¿Dónde y cuándo ocurre el problema?** _Instrucción: Describe el entorno específico en el que se
presenta el problema (por ejemplo, una aplicación móvil, un sistema de escritorio, un sitio web,
dispositivos de asistencia para personas con discapacidades, etc.)._

> [Escribe tu respuesta aquí...]

**Antecedentes** _Instrucción: Menciona brevemente los sistemas actuales o las soluciones previas
que existen en el ámbito del problema. Esto puede incluir una breve revisión de trabajos previos,
investigaciones o proyectos que hayan intentado abordar el problema._

> [Escribe tu respuesta aquí...]

---

### Paso 2: Identificación de los usuarios afectados

**¿Quiénes son los usuarios principales?** _Instrucción: Define claramente quiénes son los usuarios
afectados por el problema. Esto incluye la descripción de su perfil (por ejemplo, usuarios novatos,
expertos, personas con discapacidad, etc.)._

> Los usuarios principales son el personal interno de XM (analistas de datos, ingenieros y
> operadores del mercado) encargados de monitorear y velar por la calidad de los datos publicados en
> el portal del [SIMEM](https://www.simem.co) (_Sistema de información para el Mercado de Enegía
> Mayorista_).
> **Perfil del usuario:**
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
> - **Accesibilidad y ergonomía:** Debido a las largas jornadas frente a pantallas analizando tablas
>   y tableros de control (dashboards), son altamente susceptibles a la fatiga visual y motora.
>   Requieren interfaces que prioricen la claridad tipográfica en datos numéricos, alto contraste, y
>   atajos de teclado o flujos de trabajo optimizados que minimicen la dependencia de clics
>   repetitivos con el ratón.

**¿Cómo interactúan estos usuarios con el sistema?** _Instrucción: Explica las tareas o actividades
que los usuarios realizan con el sistema y cómo la interacción actual les resulta ineficiente o
frustrante._

> Actualmente, la interacción no ocurre en una plataforma centralizada, sino a través de un
> ecosistema fragmentado (correo electrónico, hojas de cálculo locales, portal web). El flujo de
> tareas principal consiste en la validación y corrección de datos suministrados por los agentes
> generadores, enfrentando severas deficiencias de usabilidad:
> **Flujo de interacción actual y sus puntos de fricción:**
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
>    - Fricción (IHC): **Abismo de Evaluación (Gulf of Evaluation)[^3] y cuellos de botella**. El ciclo
>      de retroalimentación (feedback loop) está roto. El usuario no recibe confirmación en tiempo
>      real de su acción, generando tiempos muertos, ansiedad y rompiendo por completo la
>      continuidad de la tarea (ruptura del estado de flujo).

---

### Paso 3: Definición de las necesidades no satisfechas

**¿Qué necesitan los usuarios?** 

* **Visibilidad del estado de los datos:** Saber si los datos consultados están correctos, completos y cumplen con los estándares de calidad definidos por la organización.
* **Agilidad:** No tener que realizar tareas manuales de validación de datos, lo cual permite a los usuarios dedicar el tiempo a la extracción del conocimiento que hay en los datos, el valor del negocio y la interpretación y generación de *insights*.
* **Alertas proactivas:** Ser notificados de manera automática sobre los errores en los datos, permitiendo así saber con seguridad qué usar y qué no.
* **Canales eficientes de comunicación y gestión de errores en el *datalake*:** Al tener la calidad de datos centralizada, será más fácil la gestión de *backfills* para datos faltantes o la implementación de controles o flujos automatizados para la carga de información faltante.
* **Fuentes de confianza:** El usuario necesita conocer de primera mano la calidad que tienen los datos que está usando, así como la calidad de los procesos de carga de datos desde las fuentes.

**Problemas actuales** 

* **Inexistencia de un centro de control de calidad de datos unificado:** Al no tener una herramienta unificada de control de calidad de datos y cargas de información, los usuarios no pueden conocer el estado real de la información del *datalake*, lo que genera pérdida de confianza en los datos, gestión reactiva en lugar de preventiva, y adicionalmente no hay gobernanza de datos o trazabilidad clara de los mismos.
* **Sobrecarga cognitiva por revisión manual:** La inspección de errores de cargas o revisión de calidad de datos se convierte en un problema al ser ejecutado de forma manual, ya que se pueden presentar problemas de errores por omisión, desgaste de los analistas, falta de enfoque en el rol de análisis de información del mercado energético y dependencia de intermediarios.
* **Procesamiento y análisis lento:** En ocasiones, no se pueden analizar los datos completamente por la falta de personal operativo que revise la calidad de los datos.
* **Incertidumbre y falta de confianza en los datos:** Al no tener un repositorio centralizado que mida la completitud, consistencia, precisión e integridad de la información, se vuelve difícil confiar plenamente en la información presentada.


---

### Paso 4: Impacto del problema

**Consecuencias para los usuarios** _Instrucción: Explica cómo este problema afecta negativamente a
los usuarios. Esto puede incluir aspectos como baja productividad, frustración, errores frecuentes,
abandono del sistema, o incluso consecuencias más graves como exclusión digital._

> La ausencia de una interfaz centralizada para monitorear la calidad, disponibilidad y estado de los datos del datalake genera consecuencias directas sobre las actividades realizadas por los analistas, ingenieros y operadores de XM. El impacto no se limita únicamente a aspectos técnicos relacionados con los datos, sino que también afecta la experiencia de interacción, la eficiencia operativa y la capacidad de los usuarios para tomar decisiones oportunas.

*  Incremento de la carga cognitiva: Los usuarios deben revisar diferentes fuentes de información, correos electrónicos, archivos CSV, tablas y resultados de procesos de carga para determinar si existe algún problema con los datos. Esta fragmentación obliga al usuario a mantener información en su memoria de trabajo y realizar comparaciones manuales, aumentando el esfuerzo mental requerido para completar una tarea que podría ser soportada directamente por una interfaz.

* Mayor probabilidad de error humano: La revisión manual de grandes cantidades de información aumenta la posibilidad de omitir inconsistencias, interpretar incorrectamente un dato o no identificar oportunamente un conjunto que no fue actualizado. Esto resulta especialmente relevante cuando existen múltiples conjuntos de datos que deben ser supervisados diariamente.

* Reducción de la productividad: Una parte del tiempo de los usuarios debe destinarse a localizar, verificar, reportar y hacer seguimiento a errores de calidad o fallos en las cargas. En consecuencia, disminuye el tiempo disponible para actividades de mayor valor, como el análisis del comportamiento del mercado energético, la identificación de tendencias y la generación de conocimiento a partir de los datos.

* Aumento del tiempo para diagnosticar y resolver errores: La ausencia de un monitor que indique de manera visual qué conjunto presenta problemas, cuál es la causa, desde cuándo ocurre y cuál es su estado de gestión obliga al usuario a investigar manualmente el incidente. Además, cuando la solución depende de comunicaciones por correo electrónico y de la intervención de otros equipos, el ciclo de resolución se prolonga.

* Pérdida de continuidad en la interacción: El usuario debe cambiar constantemente entre herramientas y contextos —por ejemplo, SIMEM, archivos locales, correo electrónico y sistemas internos— para completar una misma tarea. Desde la perspectiva de Interacción Humano-Computador, esta fragmentación interrumpe el flujo de trabajo, aumenta el número de acciones necesarias y dificulta mantener el contexto de la actividad.

* Incertidumbre sobre la confiabilidad de los datos: Si el usuario no dispone de indicadores visibles sobre completitud, consistencia, precisión, vigencia o estado de carga de un conjunto de datos, no puede determinar rápidamente si la información disponible es suficientemente confiable para utilizarla. Esto puede provocar que los analistas recurran a fuentes alternativas, como archivos TXT obtenidos directamente de otros procesos, aunque los datos también se encuentren publicados posteriormente en SIMEM.

* Frustración y disminución de la confianza en el sistema: Cuando los usuarios detectan repetidamente datos faltantes, cargas atrasadas o inconsistencias sin contar con mecanismos claros para identificar su causa y seguimiento, se deteriora la percepción de confiabilidad del sistema. Como resultado, pueden desarrollarse mecanismos de trabajo alternativos o workarounds que reducen aún más la utilización de la plataforma como fuente principal de información.

* Dificultad para priorizar incidentes: Actualmente, la falta de clasificación visual de los errores y de indicadores de severidad dificulta distinguir rápidamente entre un problema menor y uno que puede afectar de forma importante la disponibilidad o confiabilidad de la información. Esto obliga a los usuarios a evaluar manualmente cada situación antes de determinar su prioridad.

**Impacto en la organización o contexto** _Instrucción: Si es relevante, también puedes mencionar
cómo el problema afecta a la organización, empresa o comunidad que usa el sistema (por ejemplo,
pérdida de clientes, costes adicionales, insatisfacción general)._

> El problema también tiene repercusiones organizacionales para XM, considerando su responsabilidad en la administración del Mercado de Energía Mayorista y en la disponibilidad de información utilizada por diferentes actores del sector energético.

* Gestión reactiva de la calidad de datos: Al no existir un centro de monitoreo unificado con indicadores, alertas y mecanismos de seguimiento, muchos problemas se gestionan después de ser detectados por un usuario. Esto limita la posibilidad de anticiparse a fallos de carga, conjuntos atrasados o degradaciones progresivas de la calidad.

* Incremento de los costos operativos: Las actividades manuales de identificación, comunicación, corrección, seguimiento y reejecución de procesos consumen tiempo de analistas, ingenieros y equipos de soporte. Tareas que podrían ser detectadas, clasificadas o incluso corregidas automáticamente requieren actualmente intervención humana.

* Dependencia de personas y conocimiento tácito: Parte del procedimiento para identificar y solucionar problemas puede depender de la experiencia individual de determinados analistas o integrantes del equipo. Esto representa un riesgo operativo debido a que el conocimiento sobre qué revisar, cómo interpretar un error o cómo solicitar una corrección puede no encontrarse centralizado en el sistema.

* Dificultades de trazabilidad y gobernanza: Sin una plataforma que mantenga el historial de errores, versiones, reglas de calidad, acciones realizadas y responsables de cada incidente, resulta más difícil reconstruir lo ocurrido con un conjunto de datos y determinar cuándo apareció el problema, cómo fue corregido y si volvió a presentarse.

* Riesgo de publicación o utilización de información incompleta: Una carga tardía, incompleta o incorrecta puede hacer que determinados conjuntos de datos no estén disponibles en el momento esperado. Esto puede afectar los análisis realizados por los equipos internos y por los diferentes agentes del sector que dependen de información confiable y oportuna.

* Uso de fuentes alternativas y duplicación de esfuerzos: Cuando los datos disponibles en el datalake o en SIMEM no se actualizan oportunamente, algunos usuarios pueden preferir consultar archivos TXT u otras fuentes que se encuentren disponibles con mayor anticipación. Esto genera duplicidad de procesos, dificulta establecer una única fuente de verdad y reduce el aprovechamiento de la infraestructura de datos existente.

* Menor capacidad para evaluar el desempeño de la calidad de los datos: La inexistencia de métricas consolidadas impide responder fácilmente preguntas como qué porcentaje de los conjuntos presenta problemas, cuáles son los errores más frecuentes, cuánto tarda su resolución, qué fuentes presentan mayores incidencias o cuál ha sido la evolución de la calidad de los datos a lo largo del tiempo.

En consecuencia, el problema identificado no consiste únicamente en la existencia de errores dentro del datalake, sino en la dificultad que tienen los usuarios para percibir, comprender, diagnosticar y gestionar el estado de calidad de los datos mediante las interfaces y herramientas actuales. Desde la perspectiva de la Interacción Humano-Computador, existe una brecha entre la información que el sistema posee sobre sus procesos de carga y calidad y la información que presenta de manera comprensible y accionable al usuario.

Por esta razón, una interfaz de monitoreo de calidad de datos permitiría transformar un proceso actualmente fragmentado y reactivo en un flujo de trabajo más visible, centralizado y orientado a la toma de decisiones, facilitando que los usuarios identifiquen anomalías, comprendan su impacto, prioricen incidentes y hagan seguimiento a su resolución desde un único entorno.

---

### Paso 5: Objetivos del proyecto

**Qué se quiere lograr** _Instrucción: Establece claramente los objetivos que esperas cumplir al
resolver el problema. Estos deben ser concretos y medibles (por ejemplo, mejorar la tasa de éxito
en tareas específicas, reducir los errores, aumentar la satisfacción de los usuarios)._

> [Escribe tu respuesta aquí...]

---

## Referencias Bibliográficas

_Instrucción: Agrega aquí las referencias de los trabajos previos consultados en Google Scholar,
Scopus, IEEE, Science Direct, etc._

1. [Referencia 1...]
2. [Referencia 2...]
3. [Referencia 3...]

[^1]: es la capacidad de una persona para buscar, comprender, evaluar, crear y utilizar información
mediante tecnologías digitales de manera crítica, segura y responsable.
[^2]: Abismo de Ejecución: la dificultad de hacer que el sistema haga lo que quiero. Don Norman
[^3]: Abismo de Evaluación: la dificultad de saber si el sistema hizo lo que le pedí. Don Norman