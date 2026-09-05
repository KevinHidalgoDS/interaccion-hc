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