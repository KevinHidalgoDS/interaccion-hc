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

**Correos:** _datorresgom@unal.edu.co_ & _correo@unal.edu.co_ & _correo@unal.edu.co_ &
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

> El problema se presenta en SIMEM (simem.co), una plataforma web de datos abiertos que pone a disposición de usuarios internos y externos información relacionada con el Mercado de Energía Mayorista (MEM) y la operación del Sistema Interconectado Nacional (SIN).

> La plataforma ofrece acceso a los datos mediante consultas web y una API pública, la cual es utilizada por diferentes tipos de usuarios para realizar análisis, desarrollos tecnológicos y procesos de toma de decisiones. La información publicada se alimenta desde un Data Lake, que recibe aproximadamente un millón de registros diarios provenientes de múltiples fuentes de información, incluyendo bases de datos transaccionales, archivos Excel, APIs y otros sistemas de la organización.

> Actualmente, existen mecanismos para monitorear la ejecución de las cargas de datos hacia el Data Lake y hacia la plataforma; sin embargo, dichos controles están enfocados principalmente en verificar que los procesos se ejecuten correctamente, sin validar de forma integral la calidad, consistencia, oportunidad y confiabilidad de los datos publicados.

> Esta situación genera que problemas como registros erróneos, datos atípicos, inconsistencias entre fuentes, retrasos en la publicación o fallas intermitentes en los procesos de carga no sean detectados oportunamente por los administradores de la plataforma. En numerosos casos, son los propios usuarios quienes identifican y reportan las anomalías después de consumir la información, lo que afecta la confianza en los datos y la experiencia de uso del portal.

> Adicionalmente, la plataforma carece de una capa de analítica y visualización (BI) que permita monitorear el comportamiento de los datos de forma gráfica e intuitiva. La información disponible se encuentra principalmente en formatos estructurados, lo que dificulta la identificación temprana de tendencias inusuales.

> Esta limitación es aún más evidente en los conjuntos de datos con actualizaciones esporádicas, ya que actualmente no existe una vista consolidada que permita conocer la frecuencia esperada de publicación, la última actualización realizada o la existencia de posibles retrasos e incumplimientos.

> Como resultado, los responsables de la plataforma carecen de una visión centralizada y proactiva sobre la calidad y el estado de los datos publicados, lo que limita su capacidad para detectar problemas antes de que impacten a los usuarios finales.


**Antecedentes** _Instrucción: Menciona brevemente los sistemas actuales o las soluciones previas
que existen en el ámbito del problema. Esto puede incluir una breve revisión de trabajos previos,
investigaciones o proyectos que hayan intentado abordar el problema._

> Actualmente, los administradores de la plataforma cuentan con una herramienta desarrollada en Python para realizar validaciones de consistencia entre los datos de las fuentes originales y los datos almacenados en el Data Lake de SIMEM.

> Cuando la herramienta identifica diferencias o inconsistencias durante las validaciones ejecutadas, genera automáticamente una notificación por correo electrónico dirigida a los administradores de la plataforma. Adicionalmente, los hallazgos detectados son almacenados en archivos CSV para su posterior revisión.


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

> [Escribe tu respuesta aquí...]

---

## Referencias Bibliográficas

_Instrucción: Agrega aquí las referencias de los trabajos previos consultados en Google Scholar,
Scopus, IEEE, Science Direct, etc._

1. [Referencia 1...]
2. [Referencia 2...]
3. [Referencia 3...]
