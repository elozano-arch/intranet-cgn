# Intranet CGN — UI

UI (capa de presentación) de la **Intranet de la Contaduría General de la Nación
(CGN)**, sitio institucional alineado al dominio **GOV.CO** del Estado colombiano.

## Alcance — IMPORTANTE

**En este proyecto SOLO se construye la UI.** No se desarrolla backend:
- ❌ No se crean modelos, migraciones, vistas con lógica, settings de Django,
  conexión a base de datos, ni configuración de Wagtail.
- ✅ Sí se crean **templates HTML con Tailwind**, listos para que el equipo
  backend los conecte a su stack.

La UI debe quedar **lista para conectarse** a la tecnología que usarán ellos
(ver abajo): por eso se entrega como templates de Django y se estructura por
componentes que mapean 1:1 a los bloques de Wagtail. Pensamos en la tecnología
destino, pero no la implementamos.

## Tecnología destino (a la que se conectará la UI)

- **Wagtail CMS 7** — contenido por bloques (StreamField).
- **Django 6** — renderizado server-side con templates.
- **Tailwind CSS** — sistema de estilos (lo que sí usamos aquí).
- **PostgreSQL** — base de datos (fuera de alcance).

Principio rector: la página **no es una maqueta fija**, sino una **composición
flexible de bloques** reutilizables que el editor combina desde el CMS. La UI
debe funcionar aunque el contenido sea corto, largo o vacío, y aunque el editor
use los bloques "mal".

## Formato del entregable

Templates **Django + Tailwind**, organizados como componentes = bloques de Wagtail.
El backend solo los conecta; nosotros entregamos el HTML/estilo.

```
templates/
  base.html                # layout: cabecera GOV.CO, pie, barra accesibilidad
  components/
    hero.html              # → HeroBlock
    rich_text.html         # → RichTextBlock
    card.html              # → StructBlock + ListBlock
    button.html            # → ButtonBlock
    image.html             # → ImageChooserBlock
  pages/                   # ensamblajes de página de ejemplo
static/
  css/                     # entrada/salida de Tailwind
  img/                     # logos institucionales (ver assets/)
```

Convenciones de template:
- Usar sintaxis Django (`{% %}`, `{{ }}`), `{% include %}` para componentes y
  `{% block %}` para herencia desde `base.html`.
- Cada componente recibe sus datos por contexto/variables; no "hardcodear"
  contenido salvo placeholders claramente marcados.
- Diseñar estados vacíos/largos/cortos y variantes (normal, destacada, secundaria).

## Arquitectura componente ↔ bloque

| Componente UI     | Bloque Wagtail (destino)    |
| ----------------- | --------------------------- |
| Hero principal    | `HeroBlock`                 |
| Sección de texto  | `RichTextBlock`             |
| Cards             | `StructBlock` + `ListBlock` |
| Imagen            | `ImageChooserBlock`         |
| CTA               | `ButtonBlock`               |

Un componente = un bloque, con variantes claras, reglas de uso y límites de
contenido. El responsive se resuelve 100% en la UI con Tailwind (mobile-first).

## Sistema de diseño: GOV.CO Kit UI 9.2

Toda interfaz **debe** adoptar el Kit UI de GOV.CO (Agosto 2025).
Fuente: [styles-rules/kit-ui-9-2.pdf](styles-rules/kit-ui-9-2.pdf).

**Tipografía** (solo 2 familias):
- **Nunito Sans** — títulos (H1–H6, Bold) y descripciones de sección (SemiBold).
- **Verdana** — párrafos, leyendas y pies de foto (Regular).
- Medidas relativas (rem/em), no px fijos. Líneas de 45–75 caracteres. No justificar.

**Paleta GOV.CO** (prioritaria, cumple la normativa):
- Principales: Cobalt `#0943B5`, Black, Matterhorn, Grey, White.
- Universales informativos: Red (peligro), Yellow (advertencia), Green (éxito).
- Deshabilitados: Silver. Fondos: Solitude, Corn Silk, White Smoke, Portage.
- Logo GOV.CO de la barra superior: Cobalt `#0943B5`, enlaza a https://www.gov.co/home/.

→ Definir estos valores como tema de Tailwind (colores, fuentes) en lugar de
clases con valores arbitrarios.

**Cuadrícula**: base Bootstrap 5 (12 columnas, gutter 24px). Breakpoints
≥576/768/992/1200/1400px — replicar con utilidades responsive de Tailwind.

**Componentes del Kit** (transversales / generales / formulario): barra de
accesibilidad, barra superior, cabecera, pie de página, menú de navegación, miga
de pan, botones, alertas/notificaciones, modales, tablas, paginación, pestañas,
acordeón, carrusel, tarjetas, entradas de texto, desplegables, opciones de
selección, carga de archivos, etc. **Reusar siempre el componente del Kit antes
de crear uno nuevo.**

## Banner / Hero — especificación CGN (obligatoria, siempre)

Del **Manual de Identidad Visual Corporativa CGN** (v10, §4.8 "Banner web e
intranet", Figuras 33 y 36). **Respetar siempre** en hero/carrusel:

- **Banner de intranet:** lienzo **1300 × 600 px**. En la UI responsive: altura
  **600 px en desktop** (`lg:min-h-[600px]`) y ancho del contenido ≈ 1300 px
  (`max-w-contenido` = 1320). Tipografía **Nunito Sans**.
- **Botones:** **máximo 3** por pieza, anclados en la **parte inferior** y
  alineados **de derecha a izquierda** (el principal a la derecha). Cada uno mide
  **230 × 56 px** y, en el lienzo de 1300 px, van **separados 225 px** con
  **márgenes laterales de 80 px**:
  `80 + 230 + 225 + 230 + 225 + 230 + 80 = 1300` (Fig. 36). En la UI responsive se
  mantienen 230×56 y la separación de **225 px desde 1300 px de ancho**
  (`min-[1300px]:gap-[225px]`); por debajo se agrupan a la derecha con separación
  menor y en móvil (< 640 px) se apilan. Un 4.º botón va dentro del contenido.
- **Recuadro fecha/proceso (240 px de ancho):** fondo blanco bordeado con
  **fecha (DD de MM de AAAA)** y **nombre del proceso**; se ubica **47,5 px por
  encima del botón derecho** (esquina inferior derecha).
- (Referencia banner web CGN: 1350 × 648 px, separación de botones 50 px.
  Banner CHIP: 1520 × 320 px, un solo botón.)

Implementado en [hero.html](templates/components/hero.html) y
[_carousel_slide.html](templates/components/_carousel_slide.html).

## Accesibilidad (requisito legal, no negociable)

Cumplir **Resolución 1519 de 2020** y **WCAG 2.1**:
- Contraste mínimo **4.5:1** texto normal, **3:1** texto grande.
- Operable 100% por teclado, con foco visible.
- HTML semántico (`<header>`, `<nav>`, `<button>`, jerarquía `<h1>`–`<h6>`).
- `alt` en imágenes; no transmitir información solo por color.
- Enlace "Saltar al contenido principal" (`sr-only sr-only-focusable`).

## Límites de contenido por componente

| Componente        | Restricciones clave |
| ----------------- | ------------------- |
| Slider/Carrusel   | Máx. 5 slides (recom. 3), mensajes relacionados |
| Bloque de texto   | Párrafos máx. 4–5 líneas, usar subtítulos y listas |
| Imagen individual | `alt` obligatorio; sin texto clave dentro de la imagen |
| Galería           | Mín. 3, máx. 10 imágenes, un solo tema |
| Cards             | Título máx. 2 líneas, texto 2–3 líneas, 1 acción por card |
| Botones/CTA       | Texto corto con verbo; priorizar 1 CTA principal |
| Listados/noticias | Máx. 6–8 elementos visibles |
| Menú navegación   | Máx. 7 ítems; máx. 10 opciones internas por ítem |

Principios: un componente = una idea principal; el orden define la jerarquía; no
forzar el diseño con textos largos ni duplicar información.

## Estructura de la carpeta (insumos)

- `assets/` — logotipos institucionales (CGN horizontal blanco/color, GovCO).
- `styles-rules/` — documentación normativa:
  - `documento técnico Intranet.docx` — integración back-end ↔ diseño UI/UX.
  - `kit-ui-9-2.pdf` — Kit UI GOV.CO v9.2.
  - `document.pdf` — documento de diseño/lineamientos (>20MB).

## Convenciones de trabajo

- Idioma del proyecto y de la comunicación: **español**.
- Mobile-first; pensar siempre en estados vacíos/largos/cortos.
- Antes de crear un componente, verificar si ya existe en el Kit UI 9.2.
- No implementar lógica de backend; si algo requiere datos, dejar el punto de
  conexión claro (variable de contexto / `{% block %}`) para el equipo backend.
