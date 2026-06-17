# Inventario funcional de componentes UI/UX — Intranet CGN

**Rol asumido:** revisión externa de UI/UX  
**Producto:** descripción de componentes, funcionalidad y criterio de diseño integrado  
**Sitio revisado:** Intranet CGN — Contaduría General de la Nación  
**Fuentes de referencia:** capturas suministradas y revisión de las secciones públicas visibles en la intranet: Inicio, En Casa, Normativa, Plantillas, SIGI, Comités, Procesos y Revistas.

---

## 1. Lectura general de la experiencia

La intranet funciona como un portal institucional interno orientado a tres objetivos principales:

1. **Comunicar información institucional vigente**, como campañas, noticias, actualizaciones y publicaciones internas.
2. **Facilitar el acceso a herramientas y sistemas de trabajo**, mediante accesos rápidos, enlaces externos y un panel lateral de aplicaciones.
3. **Centralizar documentos, normativas, plantillas, procesos y publicaciones**, organizados por módulos, categorías, años y repositorios documentales.

Desde una mirada UI/UX, la página debe entenderse como un **ecosistema de consulta y autoservicio interno**. Por eso, sus componentes deben ayudar a que el usuario encuentre rápido lo que necesita, entienda dónde está ubicado, distinga contenido actualizado de contenido histórico y pueda acceder a documentos o sistemas sin fricción.

---

## 2. Arquitectura funcional de la intranet

La experiencia se puede organizar en cinco capas funcionales:

| Capa | Función dentro de la intranet |
|---|---|
| **Identidad y navegación global** | Mantiene la marca institucional, el menú principal, el acceso de usuario, la búsqueda global y los accesos persistentes. |
| **Comunicación institucional** | Presenta campañas, banners, noticias, publicaciones recientes y actualizaciones relevantes. |
| **Accesos rápidos y sistemas internos** | Permite entrar a herramientas de trabajo como correo, ORFEO, mesa de servicio, aula virtual, catálogo de cuentas y otros sistemas. |
| **Contenido estructurado por módulos** | Organiza información de SIGI, Comités, Procesos, Revistas, Boletín, En Casa, Normativa y Plantillas. |
| **Repositorio documental** | Permite consultar carpetas, documentos, anexos, archivos modificados, plantillas y normogramas. |

---

# 3. Componentes globales

## 3.1 Header institucional

**Descripción funcional**  
Es la franja superior que agrupa el logo de la entidad, el nombre de la intranet, el menú principal, el acceso de usuario, los enlaces sociales, el buscador y la fecha. Es el punto de orientación permanente para toda la experiencia.

**Funcionalidad**

- Identifica que el usuario está dentro de la Intranet CGN.
- Permite navegar hacia las secciones principales.
- Da acceso a autenticación o funcionalidades restringidas.
- Incluye búsqueda general.
- Presenta enlaces a canales institucionales externos.
- Muestra la fecha actual.

**Criterio de diseño integrado**  
Este componente debe actuar como ancla de navegación, no como una zona saturada de acciones. La jerarquía visual debería priorizar: identidad institucional, navegación principal y búsqueda. Los elementos secundarios, como redes sociales o fecha, deben ocupar un nivel visual más discreto para evitar competir con la navegación funcional.

---

## 3.2 Logo institucional

**Descripción funcional**  
Elemento de identidad visual ubicado en la parte superior izquierda. Refuerza la pertenencia institucional y permite reconocer el portal como un entorno oficial.

**Funcionalidad**

- Representa la marca de la Contaduría General de la Nación.
- Puede funcionar como acceso de retorno al inicio.
- Da legitimidad al entorno digital.

**Criterio de diseño integrado**  
Debe mantenerse visible y legible en todos los tamaños de pantalla. Al estar acompañado por el nombre “Intranet CGN”, su tamaño debe equilibrarse para evitar que el encabezado consuma demasiado espacio vertical o genere una lectura fragmentada.

---

## 3.3 Nombre del sitio: “Intranet CGN”

**Descripción funcional**  
Título principal del entorno interno. Funciona como etiqueta de contexto y diferencia la intranet del sitio público de la entidad.

**Funcionalidad**

- Indica al usuario que está en el portal interno.
- Refuerza la ubicación dentro del ecosistema digital de la entidad.
- Ayuda a distinguir la intranet frente a otros sistemas institucionales.

**Criterio de diseño integrado**  
Debe ser visible, pero no competir con el contenido activo de cada página. Su rol es contextual; por tanto, puede mantenerse como parte del header y permitir que los títulos de sección tengan mayor relevancia en la zona de contenido.

---

## 3.4 Menú principal superior

**Descripción funcional**  
Navegación primaria que conecta con las secciones de mayor nivel: Inicio, En Casa, Normativa y Plantillas.

**Funcionalidad**

- Permite moverse entre áreas principales de contenido.
- Sirve como estructura base de la arquitectura de información.
- Indica la sección activa mediante estado visual.

**Criterio de diseño integrado**  
El menú debe reflejar las tareas principales del usuario interno. Las etiquetas deben ser claras, consistentes y orientadas a intención. Cuando existan módulos importantes que no estén en esta navegación, como SIGI, Procesos, Comités o Revistas, el sistema debe dejar claro si son accesos secundarios, módulos transversales o categorías internas para evitar que el usuario perciba una estructura duplicada.

---

## 3.5 Estado activo del menú

**Descripción funcional**  
Indicador visual que muestra en qué sección se encuentra el usuario. En las capturas se observa un cambio de color en opciones como En Casa o Plantillas.

**Funcionalidad**

- Orienta al usuario dentro de la navegación global.
- Reduce la sensación de pérdida entre páginas similares.
- Refuerza la relación entre URL, menú y contenido.

**Criterio de diseño integrado**  
El estado activo debe ser inequívoco y accesible. Debe funcionar no solo por color, sino también con peso tipográfico, subrayado o indicador visual adicional, para que pueda ser comprendido por usuarios con diferentes condiciones de visualización.

---

## 3.6 Acceso / Login

**Descripción funcional**  
Acción ubicada en el header que permite iniciar sesión o acceder a funcionalidades protegidas.

**Funcionalidad**

- Habilita ingreso de usuarios autorizados.
- Puede desbloquear permisos, administración documental o funcionalidades internas.
- Diferencia navegación pública de experiencia autenticada.

**Criterio de diseño integrado**  
Debe comunicar claramente si el usuario está fuera o dentro de sesión. Cuando el usuario haya ingresado, el componente debería evolucionar hacia un estado de cuenta: nombre, rol, opciones personales, cierre de sesión o accesos permitidos.

---

## 3.7 Buscador global

**Descripción funcional**  
Campo de búsqueda ubicado en la parte superior. Permite al usuario consultar contenidos de la intranet desde cualquier página.

**Funcionalidad**

- Busca información transversal en el portal.
- Reduce la dependencia de navegación por menús.
- Sirve como atajo para usuarios que conocen el nombre de un documento, norma, plantilla o módulo.

**Criterio de diseño integrado**  
Debe comportarse como una herramienta central de consulta. Conviene que la búsqueda permita reconocer tipos de resultado —documentos, noticias, normas, plantillas, carpetas, sistemas— y que ofrezca resultados con contexto: título, sección, fecha, tipo de archivo y ruta.

---

## 3.8 Iconos de redes sociales

**Descripción funcional**  
Conjunto de iconos ubicados en el header que enlazan a canales externos de la entidad, como LinkedIn, Facebook, X/Twitter y YouTube.

**Funcionalidad**

- Conecta la intranet con canales institucionales públicos.
- Permite consultar contenidos externos o comunicacionales.
- Refuerza presencia digital institucional.

**Criterio de diseño integrado**  
Al ser enlaces externos, deben tener menor prioridad visual que las acciones internas. Su comportamiento debe indicar que abren una plataforma distinta, idealmente en una nueva pestaña, para no interrumpir la tarea principal dentro de la intranet.

---

## 3.9 Fecha actual

**Descripción funcional**  
Texto informativo ubicado en la parte superior derecha que muestra el día y la fecha.

**Funcionalidad**

- Aporta contexto temporal.
- Refuerza la idea de portal institucional actualizado.
- Puede acompañar contenidos sensibles a vigencia.

**Criterio de diseño integrado**  
Debe ser un elemento discreto. Su valor es contextual, por lo que no debe competir visualmente con navegación, búsqueda o acciones principales. Si se mantiene, debe alinearse correctamente y evitar superponerse con otros elementos en resoluciones pequeñas.

---

## 3.10 Botón flotante “APPS”

**Descripción funcional**  
Botón flotante ubicado en el lateral derecho. Actúa como lanzador de aplicaciones y sistemas internos.

**Funcionalidad**

- Permite abrir el panel de aplicaciones.
- Da acceso persistente a herramientas institucionales.
- Facilita saltar desde contenido informativo hacia sistemas operativos de trabajo.

**Criterio de diseño integrado**  
Debe comportarse como un acceso rápido persistente, pero sin obstruir el contenido ni las tablas. Su ubicación debe contemplar estados de escritorio, tablet y móvil. Debe incluir etiqueta legible, estado abierto/cerrado y navegación por teclado.

---

## 3.11 Panel lateral de aplicaciones

**Descripción funcional**  
Panel desplegable asociado al botón “APPS”. Muestra accesos a sistemas como Página Web, Aula Virtual, ControDoc, Catálogo de Cuentas, Correo Institucional, ORFEO, Mesa de Servicio, Nómina, Inventarios y Plantillas.

**Funcionalidad**

- Centraliza accesos a herramientas operativas.
- Reduce el tiempo para ingresar a sistemas frecuentes.
- Funciona como menú transversal independiente de la sección visitada.

**Criterio de diseño integrado**  
Este panel debe organizar las aplicaciones por intención de uso: comunicación, gestión documental, soporte, talento humano, consulta contable y servicios administrativos. Cada acceso debe incluir nombre claro, icono consistente y, cuando aplique, descripción corta para usuarios nuevos.

---

## 3.12 Footer de enlaces externos

**Descripción funcional**  
Barra inferior gris con enlaces como EDL, Compensar, Cootradian, Fempha, FNA y Positiva.

**Funcionalidad**

- Da acceso a servicios o aliados externos asociados al funcionario.
- Mantiene enlaces disponibles en varias páginas.
- Funciona como bloque de salida hacia servicios complementarios.

**Criterio de diseño integrado**  
Debe diferenciar claramente entre enlaces internos y externos. Como footer persistente, debe ser útil sin parecer navegación principal. Puede agruparse bajo una etiqueta como “Servicios para funcionarios” para que el usuario entienda por qué aparecen esos enlaces.

---

## 3.13 Banner de cookies

**Descripción funcional**  
Aviso inferior o emergente que informa sobre uso de cookies, configuración y opciones de aceptación o rechazo.

**Funcionalidad**

- Cumple función legal/informativa.
- Permite aceptar, rechazar o configurar cookies.
- Informa sobre tratamiento de datos y política de privacidad.

**Criterio de diseño integrado**  
Debe ser visible sin bloquear tareas críticas de consulta. Sus acciones deben ser claras, equivalentes y fáciles de entender. Una vez gestionado, no debería reaparecer innecesariamente en sesiones posteriores.

---

# 4. Componentes de la página de inicio

## 4.1 Carrusel principal de comunicaciones

**Descripción funcional**  
Área visual destacada de la página de inicio donde se muestran campañas, piezas gráficas, mensajes institucionales, fechas especiales y contenidos destacados.

**Funcionalidad**

- Comunica temas prioritarios de la entidad.
- Da visibilidad a campañas internas.
- Puede enlazar a noticias, documentos, videos o publicaciones.
- Permite rotación de varias piezas mediante indicadores.

**Criterio de diseño integrado**  
Debe funcionar como un bloque editorial de alto impacto, pero con control claro para el usuario. Cada lámina debería tener propósito, fecha, autor o dependencia responsable, y acción asociada cuando corresponda. Las piezas deben mantener legibilidad en diferentes pantallas y no depender exclusivamente de texto dentro de imagen.

---

## 4.2 Indicadores del carrusel

**Descripción funcional**  
Pequeños controles visuales que indican la cantidad de láminas disponibles y cuál está activa.

**Funcionalidad**

- Permiten reconocer que el banner es rotativo.
- Facilitan navegar entre mensajes destacados.
- Ayudan a ubicar al usuario dentro del conjunto de piezas.

**Criterio de diseño integrado**  
Los indicadores deben ser suficientemente visibles y clicables. Además de puntos o cuadros, el carrusel debería contar con controles de anterior/siguiente y pausa, especialmente porque contiene información institucional que puede requerir lectura detenida.

---

## 4.3 Bloque “Últimas Actualizaciones”

**Descripción funcional**  
Lista ubicada en la página de inicio que presenta documentos o contenidos modificados recientemente.

**Funcionalidad**

- Informa qué contenidos han cambiado.
- Permite acceso rápido a novedades documentales.
- Ayuda a funcionarios que necesitan mantenerse al día.

**Criterio de diseño integrado**  
Debe presentar cada actualización con suficiente contexto: título entendible, tipo de contenido, módulo al que pertenece, fecha/hora de modificación y responsable si aplica. Los nombres técnicos o códigos deben acompañarse de una descripción para que sean útiles a usuarios no expertos.

---

## 4.4 Ícono de elemento actualizado

**Descripción funcional**  
Pequeño ícono que acompaña cada fila de la lista de actualizaciones.

**Funcionalidad**

- Diferencia visualmente cada registro.
- Puede indicar tipo de contenido o estado.
- Ayuda al escaneo rápido de la lista.

**Criterio de diseño integrado**  
El ícono debe comunicar algo funcional, no ser solo decorativo. Puede representar documento, noticia, carpeta, imagen, normativa o plantilla. Esto permitiría reconocer de inmediato qué tipo de actualización se está consultando.

---

## 4.5 Botones de acceso rápido secundarios

**Descripción funcional**  
Conjunto de botones ubicados en la página de inicio, como Calendario de Eventos, Matriz de Publicaciones, Doctrina al Día y SINTRA-CGN.

**Funcionalidad**

- Permiten llegar a secciones o herramientas de consulta frecuente.
- Agrupan accesos que no están en el menú principal.
- Complementan la navegación por módulos.

**Criterio de diseño integrado**  
Deben tener jerarquía clara y consistencia visual. Cada botón debería indicar si lleva a una página interna, documento, sistema externo o módulo especializado. La ubicación y el estilo deben ayudar a entender que son acciones rápidas de uso frecuente.

---

## 4.6 Tarjetas principales de módulos

**Descripción funcional**  
Accesos visuales a módulos como SIGI, Comités, Procesos, Revistas y Boletín.

**Funcionalidad**

- Actúan como puerta de entrada a áreas de contenido institucional.
- Permiten navegar sin depender del menú superior.
- Ayudan a segmentar contenidos por necesidad del usuario.

**Criterio de diseño integrado**  
Estas tarjetas deben comportarse como accesos principales de autoservicio. Cada una debería tener título, ícono, color consistente, una breve descripción del contenido y estado visual de clic. Esto ayuda a que el usuario entienda qué encontrará antes de ingresar.

---

## 4.7 Espaciado y zona de contenido de inicio

**Descripción funcional**  
Área central donde conviven banner, actualizaciones, accesos rápidos y tarjetas de módulos.

**Funcionalidad**

- Distribuye la información inicial.
- Define la prioridad visual de contenidos.
- Organiza las acciones de entrada a la intranet.

**Criterio de diseño integrado**  
La página de inicio debe comportarse como un tablero de entrada. La distribución debería priorizar tareas frecuentes: buscar, consultar novedades, entrar a sistemas y acceder a documentos. El espacio en blanco debe usarse para separar grupos funcionales, no para dispersar elementos relacionados.

---

# 5. Componentes de navegación interna

## 5.1 Menú lateral por categorías

**Descripción funcional**  
Lista vertical ubicada a la izquierda en secciones como SIGI, En Casa, Procesos, Comités, Revistas y Normativa.

**Funcionalidad**

- Permite navegar dentro de un módulo específico.
- Agrupa opciones por tema, año, proceso o categoría.
- Funciona como navegación secundaria.

**Criterio de diseño integrado**  
Debe indicar claramente la sección activa, diferenciar grupos y mantener etiquetas legibles. Cuando el menú tenga muchas opciones o años, conviene permitir colapsar grupos, mantener encabezados visibles y evitar que todos los ítems tengan el mismo peso visual.

---

## 5.2 Menú lateral por años

**Descripción funcional**  
Variante del menú lateral usada en Revistas, Coworking y Normativa para consultar contenidos por vigencia.

**Funcionalidad**

- Permite filtrar publicaciones o normas por año.
- Facilita consulta histórica.
- Agrupa contenido periódico o normativo.

**Criterio de diseño integrado**  
Debe mostrar el año activo y permitir volver fácilmente al año vigente. La navegación histórica debe evitar que el usuario confunda contenido actual con archivo histórico, especialmente en normativas y plantillas.

---

## 5.3 Menú lateral por procesos

**Descripción funcional**  
Estructura de navegación que agrupa procesos estratégicos, misionales, de apoyo y de evaluación.

**Funcionalidad**

- Permite acceder a áreas funcionales de la entidad.
- Refleja el mapa de procesos institucional.
- Conecta cada proceso con su descripción y productos asociados.

**Criterio de diseño integrado**  
Debe representar la estructura organizacional sin volverla pesada. Los encabezados de grupo deben diferenciarse de los enlaces. Cada proceso debería tener una etiqueta clara y, cuando sea posible, una descripción corta o tooltip que ayude a usuarios que no conocen la sigla o dependencia.

---

## 5.4 Breadcrumb / ruta de navegación

**Descripción funcional**  
Elemento que muestra la ubicación del usuario dentro del repositorio o módulo, normalmente como “Inicio” o una ruta de carpetas.

**Funcionalidad**

- Ayuda a entender dónde está ubicado el usuario.
- Permite regresar a niveles anteriores.
- Complementa la navegación lateral y la tabla documental.

**Criterio de diseño integrado**  
La ruta debe mostrar la jerarquía completa, no solo “Inicio”, cuando el usuario está dentro de carpetas o subcarpetas. Debe ser clicable, legible y coherente con los nombres del menú lateral.

---

## 5.5 Título de página o sección

**Descripción funcional**  
Encabezado principal del contenido, por ejemplo “Plantillas Institucionales”, “GIT Planeación”, “Comité de Convivencia Laboral”, “Revistas le cuento que (2024)” o “Coworking 2024”.

**Funcionalidad**

- Identifica la sección actual.
- Da contexto al contenido visible.
- Refuerza la relación entre navegación y contenido.

**Criterio de diseño integrado**  
Debe tener jerarquía clara y estar alineado con el contenido que introduce. Cuando hay menú lateral y panel documental, el título debe permitir entender si se está viendo una categoría, una carpeta, un proceso, una publicación o un repositorio.

---

## 5.6 Página de contenido textual

**Descripción funcional**  
Bloque central que presenta textos descriptivos, normativos o institucionales, como en GIT Planeación, Comité de Convivencia Laboral o Plan Institucional de Capacitación.

**Funcionalidad**

- Explica contexto, objetivos, funciones, normativa o lineamientos.
- Da soporte al repositorio documental asociado.
- Permite informar antes de entregar archivos o productos.

**Criterio de diseño integrado**  
Debe facilitar lectura escaneable. Los textos largos deben dividirse en secciones, subtítulos, listas, enlaces relacionados y llamados a documentos clave. El usuario debe poder identificar rápidamente qué es la sección, para qué sirve y qué documento necesita consultar.

---

# 6. Componentes de repositorio documental

## 6.1 Contenedor de biblioteca documental

**Descripción funcional**  
Área donde se listan carpetas, documentos, plantillas, informes, anexos o publicaciones.

**Funcionalidad**

- Centraliza archivos por sección.
- Permite consultar, abrir o descargar documentos.
- Soporta carpetas y documentos en una misma estructura.

**Criterio de diseño integrado**  
Debe comportarse como un repositorio claro y confiable. Cada elemento debería mostrar nombre entendible, tipo de archivo, fecha de modificación, ubicación y acción principal. Cuando existan códigos o nombres técnicos, debe incluirse una descripción que permita comprender el contenido.

---

## 6.2 Barra de herramientas del repositorio

**Descripción funcional**  
Conjunto de controles sobre la tabla documental: selección, filtrar y ordenar, buscador, vista, información y otras acciones.

**Funcionalidad**

- Permite manipular o consultar el listado.
- Da acceso a filtros, ordenamiento y búsqueda local.
- Ofrece controles de vista o información.

**Criterio de diseño integrado**  
La barra debe ordenar las acciones de izquierda a derecha según frecuencia: búsqueda, filtro, ordenamiento y vista. Las acciones poco usadas deben agruparse en un menú secundario. Los iconos deben incluir etiquetas o ayudas para evitar ambigüedad.

---

## 6.3 Buscador interno del repositorio

**Descripción funcional**  
Campo de búsqueda dentro de listados documentales o tablas.

**Funcionalidad**

- Filtra documentos dentro de la sección actual.
- Ayuda a encontrar archivos por nombre o contenido visible.
- Complementa la búsqueda global.

**Criterio de diseño integrado**  
Debe indicar su alcance con claridad: “Buscar en Plantillas”, “Buscar en Normativa 2026” o “Buscar en esta carpeta”. Esto evita confusión entre búsqueda local y búsqueda global del sitio.

---

## 6.4 Filtro y ordenamiento

**Descripción funcional**  
Control que permite aplicar criterios de filtro u ordenar los elementos visibles.

**Funcionalidad**

- Ordena documentos por fecha, nombre, tipo o criterio disponible.
- Permite reducir el listado según necesidades del usuario.
- Apoya búsquedas en repositorios extensos.

**Criterio de diseño integrado**  
Debe mostrar qué filtros están activos y permitir limpiarlos fácilmente. En contenidos documentales, los filtros más útiles suelen ser tipo de archivo, vigencia, fecha, dependencia, categoría y estado.

---

## 6.5 Selector de vista

**Descripción funcional**  
Iconos que sugieren cambio de visualización, como vista de lista, cuadrícula o detalles.

**Funcionalidad**

- Permite adaptar la forma en que se presentan los documentos.
- Puede facilitar exploración visual o lectura tabular.
- Ayuda en repositorios con muchos tipos de contenido.

**Criterio de diseño integrado**  
Debe indicar cuál vista está activa y qué cambia al seleccionarla. En una intranet documental, la vista de lista con metadatos suele ser la predeterminada; la vista de tarjetas puede ser útil para publicaciones, videos o piezas gráficas.

---

## 6.6 Checkbox de selección

**Descripción funcional**  
Casillas de selección ubicadas en encabezados y filas del listado documental.

**Funcionalidad**

- Permite seleccionar uno o varios elementos.
- Puede habilitar acciones masivas según permisos.
- Apoya operaciones de administración documental.

**Criterio de diseño integrado**  
Debe aparecer cuando exista una acción clara asociada. Si el usuario final no puede ejecutar acciones masivas, el checkbox puede generar ruido. Cuando se use, debe activar una barra contextual con acciones disponibles.

---

## 6.7 Tabla documental

**Descripción funcional**  
Estructura tabular que muestra carpetas o documentos mediante columnas como Nombre/Título, Descripción y Fecha de modificación.

**Funcionalidad**

- Organiza archivos de manera consultable.
- Permite comparar fechas y tipos de contenido.
- Facilita navegación en carpetas.

**Criterio de diseño integrado**  
La tabla debe priorizar la comprensión del documento. Nombre, tipo, fecha, dependencia y acción principal deben estar claramente visibles. En pantallas pequeñas, debe transformarse en tarjetas o filas adaptativas para evitar desplazamientos horizontales excesivos.

---

## 6.8 Fila de carpeta

**Descripción funcional**  
Registro que representa una carpeta dentro del repositorio, por ejemplo “Documentos SGC”, “Sensibilización”, “Auditorías”, “Capacitación” o “PIC Vigente”.

**Funcionalidad**

- Permite ingresar a agrupaciones de documentos.
- Estructura el contenido por temas o categorías.
- Diferencia contenedores de archivos individuales.

**Criterio de diseño integrado**  
Debe identificarse claramente como carpeta y mostrar cuántos elementos contiene cuando sea posible. También debería informar si la carpeta está vacía o si contiene documentos desactualizados, vigentes o archivados.

---

## 6.9 Fila de documento

**Descripción funcional**  
Registro que representa un archivo específico, como una plantilla, resolución, revista, informe, presentación o imagen.

**Funcionalidad**

- Permite abrir o descargar el documento.
- Presenta metadatos básicos como título y fecha.
- Puede incluir acciones adicionales.

**Criterio de diseño integrado**  
Debe comunicar claramente qué pasará al hacer clic: abrir vista previa, descargar archivo, abrir PDF, abrir documento Word o navegar a otra página. El título debe ser legible y consistente, evitando nombres técnicos cuando el documento tenga un nombre de usuario más claro.

---

## 6.10 Ícono de tipo de archivo

**Descripción funcional**  
Indicador visual que diferencia carpetas, PDFs, documentos Word, presentaciones, imágenes u otros formatos.

**Funcionalidad**

- Permite reconocer el formato antes de abrir.
- Ayuda a escanear el listado.
- Reduce errores al seleccionar documentos.

**Criterio de diseño integrado**  
Debe usar una convención visual consistente y accesible. El ícono debe complementarse con texto o etiqueta de formato, especialmente para usuarios que no distinguen formatos solo por color o símbolo.

---

## 6.11 Fecha de modificación

**Descripción funcional**  
Columna que informa cuándo fue actualizado o modificado un documento o carpeta.

**Funcionalidad**

- Ayuda a evaluar vigencia del contenido.
- Permite identificar documentos recientes o antiguos.
- Sirve como criterio de ordenamiento.

**Criterio de diseño integrado**  
Debe combinar fecha relativa y fecha exacta cuando sea útil. Por ejemplo: “Hace 22 días — 26 de mayo de 2026”. Esto permite lectura rápida y precisión documental.

---

## 6.12 Menú de acciones por fila

**Descripción funcional**  
Icono de tres puntos ubicado al final de cada fila.

**Funcionalidad**

- Agrupa acciones secundarias del elemento.
- Puede permitir descargar, ver detalles, copiar enlace, compartir o administrar.
- Mantiene la tabla limpia.

**Criterio de diseño integrado**  
Debe reservarse para acciones menos frecuentes. La acción principal debe ser evidente en el título o botón principal. El menú debe mostrar opciones según permisos del usuario y evitar acciones que no estén disponibles.

---

## 6.13 Selector de cantidad de registros

**Descripción funcional**  
Control que permite elegir cuántos elementos se muestran por página, por ejemplo 4, 10, 20, 40 o 60 registros.

**Funcionalidad**

- Personaliza la densidad de información.
- Facilita exploración en listados largos.
- Reduce o amplía la necesidad de paginar.

**Criterio de diseño integrado**  
Debe estar ubicado cerca de la paginación y mostrar claramente el total de resultados. El valor predeterminado debe responder al tipo de contenido: más registros para documentos, menos para publicaciones con vista visual.

---

## 6.14 Paginación

**Descripción funcional**  
Control inferior que permite navegar entre páginas de resultados.

**Funcionalidad**

- Divide listados extensos.
- Permite avanzar, retroceder o seleccionar página.
- Informa el intervalo visible y el total de resultados.

**Criterio de diseño integrado**  
Debe estar siempre asociada al total de resultados y al selector de cantidad de registros. En búsquedas internas, debe mantenerse el filtro aplicado al cambiar de página.

---

## 6.15 Estado vacío del repositorio

**Descripción funcional**  
Mensaje que aparece cuando una carpeta no contiene documentos o archivos multimedia.

**Funcionalidad**

- Informa que no hay contenido disponible.
- Evita que el usuario interprete el espacio vacío como error de carga.
- Puede orientar hacia otra acción.

**Criterio de diseño integrado**  
Debe explicar el estado con lenguaje claro y ofrecer una salida: volver al nivel anterior, buscar en todo el módulo o contactar al responsable del contenido si aplica.

---

# 7. Componentes por módulo

## 7.1 Módulo Inicio

**Descripción funcional**  
Página de entrada de la intranet. Agrupa comunicaciones destacadas, actualizaciones recientes, accesos rápidos, módulos principales y sistemas externos.

**Funcionalidad**

- Presenta novedades institucionales.
- Facilita acceso a módulos clave.
- Conecta con herramientas de uso frecuente.

**Criterio de diseño integrado**  
Debe comportarse como un dashboard operativo. La primera pantalla debería responder a las tareas más comunes: buscar un documento, ver novedades, ingresar a una aplicación, consultar una norma, descargar una plantilla o revisar una publicación.

---

## 7.2 Módulo SIGI

**Descripción funcional**  
Sección asociada a sistemas de gestión institucional, con opciones como Sistema de Gestión de Calidad, Sistema de Gestión Ambiental, Seguridad y Salud en el Trabajo y Seguridad de la Información.

**Funcionalidad**

- Organiza documentos por sistema de gestión.
- Permite acceder a carpetas de documentos transversales, SGC, sensibilización y auditorías.
- Centraliza información de cumplimiento y gestión interna.

**Criterio de diseño integrado**  
Debe permitir diferenciar claramente cada sistema de gestión y sus documentos vigentes. La experiencia debería ayudar a responder preguntas como: qué sistema estoy consultando, qué documento necesito, cuál es la versión vigente y qué documentos son históricos.

---

## 7.3 Módulo Comités

**Descripción funcional**  
Sección informativa y documental sobre comités institucionales, como Comité de Convivencia Laboral y Comité Paritario de Seguridad y Salud en el Trabajo.

**Funcionalidad**

- Explica el propósito y normatividad de cada comité.
- Presenta objetivos, designación, representantes, funciones y periodo.
- Agrupa productos o informes relacionados.

**Criterio de diseño integrado**  
Debe combinar contenido explicativo con acceso documental. La estructura ideal debe permitir escanear rápidamente: qué es el comité, para qué sirve, quiénes lo integran, cómo se contacta, cuáles son sus funciones y qué documentos están disponibles.

---

## 7.4 Módulo Procesos

**Descripción funcional**  
Sección que representa el mapa de procesos institucional y páginas asociadas a grupos internos de trabajo, como GIT Planeación.

**Funcionalidad**

- Organiza procesos estratégicos, misionales, de apoyo y de evaluación.
- Presenta funciones o responsabilidades del proceso seleccionado.
- Vincula productos documentales relacionados.

**Criterio de diseño integrado**  
Debe ayudar a comprender la estructura operativa de la entidad. Cada proceso debería incluir descripción resumida, responsables, productos clave, documentos vigentes y relación con otros procesos. El menú lateral debe guiar sin requerir conocimiento previo de la estructura interna.

---

## 7.5 Módulo Revistas

**Descripción funcional**  
Sección de publicaciones internas, organizada por tipos de publicación y años. Incluye categorías como “Le Cuento Que”, “SIINERGIA Contable”, “Codex”, “Coworking”, videos, presentaciones y condecoraciones.

**Funcionalidad**

- Permite consultar publicaciones periódicas.
- Agrupa ediciones por año.
- Lista documentos como revistas o piezas editoriales.

**Criterio de diseño integrado**  
Debe comportarse como una biblioteca editorial. Cada publicación debería mostrar portada o identificador visual, edición, fecha, tipo de contenido y acción de lectura o descarga. La navegación por años debe hacer evidente qué contenidos son recientes y cuáles pertenecen a archivo histórico.

---

## 7.6 Módulo Boletín

**Descripción funcional**  
Acceso desde la página de inicio orientado a boletines institucionales o publicaciones informativas.

**Funcionalidad**

- Reúne boletines de comunicación interna.
- Permite consultar ediciones o documentos relacionados.
- Puede funcionar como canal periódico de novedades.

**Criterio de diseño integrado**  
Debe diferenciarse de Revistas si su propósito editorial es distinto. El usuario debería entender si el boletín es una publicación periódica, un resumen de novedades, una comunicación oficial o un archivo documental.

---

## 7.7 Módulo En Casa

**Descripción funcional**  
Sección orientada a contenidos internos de interés para funcionarios, como Plan Institucional de Capacitación, Manual de Identidad Visual, Políticas Contables, Comisión de Personal, Evaluación de Desempeño y Nombramientos.

**Funcionalidad**

- Agrupa información administrativa y de talento humano.
- Presenta textos explicativos y productos asociados.
- Permite consultar documentos de uso interno.

**Criterio de diseño integrado**  
Debe funcionar como una zona de autoservicio para el funcionario. Las categorías deberían estar organizadas por necesidad: capacitación, identidad institucional, desempeño, nombramientos, comisiones y lineamientos. Cada página debe indicar qué puede hacer el usuario y qué documento debe consultar.

---

## 7.8 Módulo Normativa

**Descripción funcional**  
Sección para consultar normogramas por año, con tabla de normas, descripciones, fechas de expedición y anexos.

**Funcionalidad**

- Permite consultar resoluciones, circulares y otros actos administrativos.
- Organiza la información por vigencia anual.
- Muestra anexos cuando existen.
- Incluye buscador y tabla consultable.

**Criterio de diseño integrado**  
Debe operar como un buscador normativo confiable. Cada norma debe mostrar tipo, número, año, descripción, fecha, estado, anexos y acción principal. Las descripciones largas deben ser legibles sin romper la tabla, y los anexos deben ser claramente identificables.

---

## 7.9 Módulo Plantillas

**Descripción funcional**  
Biblioteca de archivos institucionales reutilizables, como plantillas de comunicación externa, comunicación interna, presentación CGN, piezas gráficas, noticias web, comunicados de prensa y actos administrativos.

**Funcionalidad**

- Centraliza formatos oficiales.
- Permite descargar o abrir archivos reutilizables.
- Ayuda a mantener consistencia institucional en documentos y comunicaciones.

**Criterio de diseño integrado**  
Debe funcionar como una biblioteca de recursos oficiales. Cada plantilla debería indicar formato, uso recomendado, dependencia responsable, fecha de actualización y versión. La búsqueda debe permitir encontrar plantillas por necesidad, no solo por nombre exacto.

---

# 8. Componentes complementarios y accesos especiales

## 8.1 Calendario de Eventos

**Descripción funcional**  
Acceso rápido a una agenda institucional o calendario de actividades.

**Funcionalidad**

- Permite consultar eventos internos.
- Puede centralizar fechas importantes, capacitaciones, reuniones o actividades institucionales.

**Criterio de diseño integrado**  
Debe presentar eventos por fecha, tipo, dependencia y modalidad. El usuario debería poder identificar próximos eventos, eventos del día y actividades relevantes para su rol.

---

## 8.2 Matriz de Publicaciones

**Descripción funcional**  
Acceso a una matriz o repositorio relacionado con publicaciones institucionales.

**Funcionalidad**

- Permite consultar planificación, estado o inventario de publicaciones.
- Puede servir como herramienta de control editorial.

**Criterio de diseño integrado**  
Debe aclarar si la matriz es de consulta, seguimiento o gestión. Sus datos deberían organizarse por publicación, responsable, fecha, estado y canal.

---

## 8.3 Doctrina al Día

**Descripción funcional**  
Acceso a contenido doctrinal o técnico actualizado.

**Funcionalidad**

- Facilita consulta especializada.
- Permite mantenerse actualizado sobre doctrina o lineamientos.

**Criterio de diseño integrado**  
Debe comunicar vigencia y relevancia. El usuario debería identificar si el contenido corresponde a doctrina reciente, archivo histórico, actualización técnica o documento oficial.

---

## 8.4 SINTRA-CGN

**Descripción funcional**  
Acceso rápido relacionado con el sindicato o información asociada a SINTRA-CGN.

**Funcionalidad**

- Permite consultar información sindical o institucional vinculada.
- Actúa como punto de acceso directo desde la página de inicio.

**Criterio de diseño integrado**  
Debe indicar con claridad el tipo de contenido al que conduce y si se trata de una sección interna, enlace externo o repositorio documental.

---

# 9. Componentes de contenido y lectura

## 9.1 Bloques de texto institucional

**Descripción funcional**  
Fragmentos extensos que explican políticas, funciones, normativas, objetivos o contexto de un área.

**Funcionalidad**

- Entregan información formal.
- Soportan la interpretación de documentos anexos.
- Ayudan a contextualizar procesos o comités.

**Criterio de diseño integrado**  
Deben estar estructurados para lectura rápida: introducción breve, subtítulos, bullets, enlaces relacionados y documentos clave. Los párrafos extensos deben evitarse cuando el contenido pueda convertirse en secciones o tarjetas informativas.

---

## 9.2 Sección “Productos”

**Descripción funcional**  
Bloque documental asociado a páginas de contenido, como procesos, comités o En Casa.

**Funcionalidad**

- Relaciona la información textual con archivos consultables.
- Permite acceder a informes, documentos, imágenes, formatos o carpetas.
- Conecta contenido institucional con evidencia documental.

**Criterio de diseño integrado**  
Debe entenderse como “documentos relacionados” o “recursos disponibles”. El título “Productos” puede mantenerse si es lenguaje interno, pero debería acompañarse de una descripción que explique qué encontrará el usuario en ese bloque.

---

## 9.3 Enlaces dentro del contenido

**Descripción funcional**  
Textos clicables que llevan a resoluciones, documentos, carpetas o recursos relacionados.

**Funcionalidad**

- Permiten ampliar información.
- Conectan textos institucionales con documentos oficiales.
- Facilitan consulta puntual.

**Criterio de diseño integrado**  
Deben ser descriptivos y no depender de textos genéricos. El usuario debería saber si abrirá un PDF, una página interna, una carpeta o un sitio externo antes de hacer clic.

---

# 10. Estados de interacción esperados

## 10.1 Estado hover / foco

**Descripción funcional**  
Estado visual que aparece al pasar el cursor o navegar con teclado sobre botones, enlaces, tarjetas o filas.

**Funcionalidad**

- Indica qué elementos son interactivos.
- Mejora accesibilidad.
- Reduce errores de navegación.

**Criterio de diseño integrado**  
Todos los elementos clicables deben tener estado hover y foco visible. Esto incluye tarjetas de módulos, botones, enlaces de tablas, menú lateral, paginación y botón de aplicaciones.

---

## 10.2 Estado activo / seleccionado

**Descripción funcional**  
Estado que indica la sección, filtro, año, menú o documento actualmente seleccionado.

**Funcionalidad**

- Orienta al usuario.
- Refuerza ubicación dentro del sistema.
- Ayuda a interpretar el contenido mostrado.

**Criterio de diseño integrado**  
Debe ser consistente en toda la intranet. El estado activo del menú superior, menú lateral, año seleccionado, página de paginación y filtro aplicado deben compartir una lógica visual reconocible.

---

## 10.3 Estado sin resultados

**Descripción funcional**  
Mensaje mostrado cuando una búsqueda o filtro no encuentra documentos.

**Funcionalidad**

- Explica que no hay coincidencias.
- Evita que el usuario perciba un error técnico.
- Permite reintentar búsqueda o limpiar filtros.

**Criterio de diseño integrado**  
Debe incluir recomendaciones: revisar ortografía, limpiar filtros, buscar en todo el sitio o volver a la categoría anterior.

---

## 10.4 Estado de carga

**Descripción funcional**  
Indicador temporal mientras se cargan documentos, tablas, banners o resultados.

**Funcionalidad**

- Informa que el sistema está procesando.
- Reduce incertidumbre.
- Evita clics repetidos.

**Criterio de diseño integrado**  
Debe usarse en tablas, búsquedas, panel de apps y carrusel. En repositorios documentales, los esqueletos de carga pueden comunicar mejor la estructura que un spinner aislado.

---

## 10.5 Estado de error o acceso restringido

**Descripción funcional**  
Mensaje que aparece cuando un documento no carga, el usuario no tiene permisos o un sistema externo no está disponible.

**Funcionalidad**

- Explica el problema.
- Orienta sobre próximos pasos.
- Reduce frustración.

**Criterio de diseño integrado**  
Debe informar qué ocurrió, qué puede hacer el usuario y a quién contactar. Para una intranet, es útil incluir acceso a mesa de servicio o soporte institucional.

---

# 11. Componentes priorizados para rediseño funcional

La siguiente priorización no presenta cambios como correcciones aisladas, sino como componentes clave que definen la calidad de la experiencia:

| Prioridad | Componente | Razón funcional |
|---|---|---|
| Alta | Buscador global e interno | Es el camino más rápido para encontrar documentos, normas, plantillas y publicaciones. |
| Alta | Repositorio documental | Es el patrón más repetido y crítico de la intranet. |
| Alta | Navegación lateral | Define la comprensión de módulos, años, procesos y categorías. |
| Alta | Página de inicio | Debe funcionar como tablero de entrada a tareas frecuentes. |
| Media | Panel de aplicaciones | Es clave para conectar la intranet con herramientas operativas. |
| Media | Tarjetas de módulos | Ayudan a orientar usuarios que no conocen la estructura interna. |
| Media | Tablas normativas | Requieren lectura clara, búsqueda confiable y metadatos precisos. |
| Media | Páginas informativas de procesos/comités | Necesitan lectura escaneable y conexión clara con documentos. |
| Baja | Redes sociales y fecha | Son elementos contextuales, pero no tareas principales del usuario interno. |

---

# 12. Propuesta de librería de componentes reutilizables

Para una reconstrucción o rediseño, la intranet puede organizarse con los siguientes componentes reutilizables:

| Componente reusable | Uso principal |
|---|---|
| `HeaderIntranet` | Logo, título, menú, login, búsqueda, redes y fecha. |
| `MainNavigation` | Navegación superior entre secciones principales. |
| `GlobalSearch` | Búsqueda transversal en toda la intranet. |
| `AppsDrawer` | Panel lateral de sistemas y aplicaciones. |
| `HeroCarousel` | Comunicaciones destacadas de la página de inicio. |
| `RecentUpdatesList` | Listado de contenidos modificados recientemente. |
| `QuickAccessGroup` | Botones de accesos frecuentes. |
| `ModuleShortcutCard` | Tarjetas de módulos como SIGI, Comités o Revistas. |
| `SideCategoryMenu` | Menú lateral por tema, año, proceso o categoría. |
| `PageTitleBlock` | Título y contexto de sección. |
| `ContentArticle` | Páginas con texto institucional estructurado. |
| `RelatedResourcesBlock` | Sección de documentos asociados o productos. |
| `DocumentLibrary` | Contenedor de repositorio documental. |
| `DocumentToolbar` | Búsqueda, filtros, ordenamiento y vista. |
| `DocumentTable` | Tabla de carpetas y documentos. |
| `DocumentRow` | Fila de archivo o carpeta con metadatos. |
| `PaginationControls` | Paginación y cantidad de registros. |
| `ExternalLinksFooter` | Enlaces externos de servicios para funcionarios. |
| `EmptyState` | Estado sin documentos o sin resultados. |
| `ErrorState` | Estado de error, permisos o recurso no disponible. |

---

# 13. Resumen ejecutivo

La intranet CGN ya cuenta con una base funcional amplia: navegación superior, módulos documentales, repositorios, actualizaciones, accesos rápidos y panel de aplicaciones. El principal valor del sistema está en centralizar información institucional y documentos de trabajo.

Desde una mirada externa de UI/UX, los componentes deben describirse y diseñarse bajo una lógica de autoservicio: que el usuario pueda encontrar, entender y actuar rápidamente. Esto implica que cada componente debe comunicar su propósito, indicar el contexto, mostrar metadatos suficientes, diferenciar contenidos vigentes de históricos y ofrecer caminos claros hacia documentos o sistemas internos.

El componente más crítico es el **repositorio documental**, porque aparece en múltiples secciones y concentra gran parte de la utilidad de la intranet. Le siguen el **buscador**, la **navegación lateral**, la **página de inicio** y el **panel de aplicaciones**, que en conjunto definen la eficiencia de uso diaria para funcionarios y colaboradores.
