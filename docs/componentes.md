# Documentación de componentes — UI Intranet CGN

Catálogo de la biblioteca de componentes (templates Django + Tailwind) construida
para la intranet de la CGN, con su mapeo a bloques de Wagtail para la integración
del equipo de desarrollo. Guía visual en vivo: **/componentes** del sitio.

## Cómo construir / desplegar

```bash
npm install            # una vez
npm run build:css      # compila static/css/app.css (Tailwind)
python build_static.py # genera dist/ (todas las páginas)
```
El sitio se sirve estático desde `dist/` (Vercel). Detalle en el [README](../README.md).

## Sistema de diseño

- **Tokens de color** (tema Tailwind, `tailwind.config.js`): `cgn-verde/verdeos/verdehondo/gris/naranja/naranjaos/negro/grisos`, `hacienda`, `govco-cobalt/cobaltos/solitude/smoke/silver`, `estado-error/alerta/alertatext/exito`. **No usar valores de color arbitrarios.**
- **Tipografía**: `font-titulo` (Nunito Sans) para títulos, `font-cuerpo` (Verdana) para texto.
- **Contenedor**: `max-w-contenido` (1320 px); banner intranet 1300 × 600 px.
- **Accesibilidad**: WCAG 2.1 / Resolución 1519 de 2020 — verificado con axe-core (0 violaciones).

## Componentes ↔ bloques de Wagtail

| Componente (archivo) | Propósito | Parámetros clave | Bloque Wagtail |
|---|---|---|---|
| `hero.html` | Banner de sección (1 pieza) | title, text, eyebrow, buttons, fecha, proceso | `HeroBlock` |
| `carousel.html` + `_carousel_slide.html` | Carrusel de banners | slides (título, texto, CTA, fecha, proceso) | `CarouselBlock` (ListBlock) |
| `card.html` | Tarjeta de acceso (ícono+texto) | title, text, url, color, icon | `StructBlock` |
| `news_card.html` | Tarjeta de noticia (destacada/estándar) | title, excerpt, url, fecha, categoria, image, featured | `StructBlock` |
| `cover.html` | Portada de revista/boletín | title, url, image, color, tag | `StructBlock` (ImageChooser) |
| `button.html` | Botón / CTA | label, url, variant (primario/contorno/contorno_inverso) | `ButtonBlock` |
| `rich_text.html` | Texto enriquecido | title, body (HTML) | `RichTextBlock` |
| `image.html` | Imagen con leyenda | src, alt, caption, ratio | `ImageChooserBlock` |
| `section_header.html` | Encabezado de sección | title, subtitle, link_url | inline |
| `nav.html` + `_nav_list.html` | Menú principal (mega-menú, responsive) | `nav` (data/nav.json) | menú del CMS |
| `breadcrumb.html` | Miga de pan | current / crumbs | automático |
| `footer.html` | Pie de página | — | transversal |
| `tag.html` | Etiqueta (estado/filtro) | label, variant (info/exito/pendiente/error/filtro) | inline |
| `notification.html` | Aviso / notificación (toast) | variant, title, message, time | — |
| `modal.html` | Ventana emergente | id, variant, title, message, confirm/cancel_label | — |
| `tooltip.html` | Mensaje de ayuda | label, text, pos | — |
| `app_gallery.html` | Galería de aplicaciones | apps (label, url) | `ListBlock` |
| `pagination.html` | Paginación | pages, current | automático |
| `accordion.html` | Secciones plegables | items (title, body), numbered | `StreamBlock` |
| `tabs.html` | Pestañas | tabs (label, body) | `StreamBlock` |
| `table.html` | Tabla de datos | columns, rows, caption, zebra | `TableBlock` |
| `spinner.html` | Indicador de carga | label, modal, size | — |
| `stepper.html` | Indicador de pasos (trámite) | steps, current | — |
| `input.html` | Campo de texto | id, label, type, state, error/valid_msg, required | `FormField` |
| `choice.html` | Casilla / radio / interruptor | type, label, name, checked | `FormField` |
| `select.html` | Lista desplegable | id, label, options, required | `FormField` |
| `file_upload.html` | Subir archivos | id, label, help, accept | `FormField` |
| `login.html` | Inicio de sesión | (natural/jurídica) | — |
| `service_area.html` | Área de ayuda del trámite | telefono, correo, tutoriales_url | — |

## Páginas de ejemplo (en `dist/`)

- `index.html` — Inicio (banner, accesos, publicaciones).
- `en-casa`, `normativa`, `sigi`, `procesos`, `comites`, `publicaciones`, `recursos` — secciones del mapa del sitio (plantilla `pages/seccion.html`).
- `tramite.html` — trámite de ejemplo (pasos + formularios + ayuda).
- `componentes.html` — guía visual de todos los componentes.

## Datos de navegación

`data/nav.json` define el mapa del sitio (secciones, subsecciones y publicaciones).
El menú, la home y las páginas de sección se generan a partir de este archivo.

## Notas de integración (Wagtail/Django)

- Cada componente recibe sus datos por contexto/variables; no hay contenido "hardcodeado" salvo los ejemplos de la guía.
- El responsive se resuelve con Tailwind (mobile-first). El menú y la home leen `data/nav.json`; en Wagtail se reemplaza por el menú/StreamField del CMS.
- Los puntos de conexión están marcados en las plantillas.
