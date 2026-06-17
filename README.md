# Intranet CGN — UI

UI (capa de presentación) de la **Intranet de la Contaduría General de la Nación (CGN)**,
alineada al dominio **GOV.CO** y al **Kit UI 9.2**.

> **Alcance:** solo UI (HTML + Tailwind como templates Django). El backend
> (Wagtail CMS 7 · Django 6 · PostgreSQL) lo desarrolla otro equipo; aquí solo se
> dejan los puntos de conexión a los bloques de Wagtail.

## Stack de presentación

- **Templates Django** organizados como componentes = bloques de Wagtail.
- **Tailwind CSS** (Play CDN para previsualización; en producción se compila con CLI).
- Tipografía **Nunito Sans** (títulos) + **Verdana** (cuerpo). Paleta CGN + GOV.CO.
- Accesibilidad: WCAG 2.1 + Resolución 1519 de 2020.

## Estructura

```
templates/
  base.html                 # layout: cabecera GOV.CO/CGN, menú, footer, accesibilidad
  components/                # hero, carrusel, card, news_card, button, rich_text, image…
  pages/home.html            # ensamblaje del home
static/img/                  # logos institucionales
dist/                        # build estático (lo que sirve Vercel)
build_static.py              # genera dist/ a partir de las plantillas
styles-rules/                # documentación normativa (Kit UI, identidad CGN, doc técnico)
```

## Previsualizar / construir

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install Django
python build_static.py        # genera dist/index.html + dist/static
# abrir dist/index.html en el navegador
```

## Despliegue en Vercel

El sitio es estático: Vercel sirve la carpeta `dist/` (ver `vercel.json`).
Para conectar: vercel.com → **Add New → Project** → importar este repo →
Framework **Other**, Output Directory **dist**.

## Componentes ↔ bloques Wagtail

| Componente UI    | Bloque Wagtail              |
| ---------------- | --------------------------- |
| Hero / Banner    | `HeroBlock` / `CarouselBlock` |
| Sección de texto | `RichTextBlock`             |
| Tarjetas         | `StructBlock` + `ListBlock` |
| Imagen           | `ImageChooserBlock`         |
| Botón / CTA      | `ButtonBlock`               |
