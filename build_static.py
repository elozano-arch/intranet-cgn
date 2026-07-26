#!/usr/bin/env python3
"""
Build estático de la UI (solo presentación, sin backend).
Renderiza las plantillas Django a HTML estático en dist/ y copia los estáticos,
para desplegar en Vercel como sitio estático (sin servidor).

Uso:  python build_static.py
Requisitos:  pip install Django
"""
import os, shutil, json, django
from django.conf import settings

BASE = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(BASE, "dist")

# Navegación real de la intranet (data/nav.json) → contexto de las plantillas.
with open(os.path.join(BASE, "data", "nav.json"), encoding="utf-8") as _f:
    NAV = json.load(_f)
CONTEXT = {"nav": NAV}

settings.configure(
    DEBUG=False,
    INSTALLED_APPS=["django.contrib.staticfiles"],
    STATIC_URL="/static/",
    STATICFILES_DIRS=[os.path.join(BASE, "static")],
    TEMPLATES=[{
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE, "templates")],
        "APP_DIRS": False,
        "OPTIONS": {"builtins": ["django.templatetags.static"]},
    }],
)
django.setup()
from django.template.loader import render_to_string

# Secciones del menú → páginas internas (label del nav, archivo de salida)
SECTIONS = [
    ("En Casa", "en-casa.html"),
    ("Normativa", "normativa.html"),
    ("SIGI", "sigi.html"),
    ("Procesos", "procesos.html"),
    ("Comités", "comites.html"),
    ("Publicaciones", "publicaciones.html"),
    ("Recursos", "recursos.html"),
]

def find_section(label):
    for n in NAV:
        if n.get("label") == label:
            return n
    return None

def write(out, html):
    with open(os.path.join(DIST, out), "w", encoding="utf-8") as f:
        f.write(html)
    print("✓", out)

# Limpiar y recrear dist/
if os.path.isdir(DIST):
    shutil.rmtree(DIST)
os.makedirs(DIST)

# Copiar estáticos -> dist/static
shutil.copytree(os.path.join(BASE, "static"), os.path.join(DIST, "static"))

# Home
write("index.html", render_to_string("pages/home.html", {**CONTEXT, "active_nav": "Inicio"}))

# Guía de componentes (biblioteca UI) con datos de ejemplo
COMPONENTES_CTX = {
    "apps": [
        {"label": "CHIP", "url": "#"}, {"label": "Correo", "url": "#"}, {"label": "SIGI", "url": "#"},
        {"label": "Plantillas", "url": "#"}, {"label": "Calendario", "url": "#"}, {"label": "Directorio", "url": "#"},
    ],
    "acordeon_items": [
        {"title": "¿Cómo accedo a los aplicativos de la CGN?", "body": "Desde el menú principal, en las secciones correspondientes, o desde los accesos rápidos de la página de inicio."},
        {"title": "¿Dónde consulto la normativa vigente?", "body": "En la sección Normativa encontrarás los normogramas por año, desde 2015 hasta 2026 y años anteriores."},
        {"title": "¿Cómo reporto una novedad?", "body": "Utiliza los canales de contacto disponibles en el pie de página del sitio."},
    ],
    "tabs_items": [
        {"label": "Descripción", "body": "Contenido de la primera pestaña. Las pestañas organizan información relacionada sin recargar la página."},
        {"label": "Requisitos", "body": "Contenido de la segunda pestaña con los requisitos del trámite o servicio."},
        {"label": "Contacto", "body": "Contenido de la tercera pestaña con los datos de contacto de la dependencia."},
    ],
    "tabla_columns": ["Nombre", "Dependencia", "Estado"],
    "tabla_rows": [
        ["Solicitud 0123", "Gestión Humana", "Aprobada"],
        ["Solicitud 0124", "Gestión Administrativa", "En trámite"],
        ["Solicitud 0125", "Gestión Jurídica", "Pendiente"],
        ["Solicitud 0126", "Gestión TICs", "Aprobada"],
    ],
    "paginas": [1, 2, 3, 4, "…", 20],
    "pasos": ["Inicio", "Confirmar identidad", "Generar solicitud", "Datos adicionales"],
    "opciones_demo": ["Opción 1", "Opción 2", "Opción 3"],
}
write("componentes.html", render_to_string("pages/componentes.html", {**CONTEXT, "active_nav": "", **COMPONENTES_CTX}))

# Página de trámite (ejemplo) — integra pasos + formularios + área de ayuda
write("tramite.html", render_to_string("pages/tramite.html", {
    **CONTEXT, "active_nav": "",
    "pasos": ["Inicio", "Confirmar identidad", "Generar solicitud", "Datos adicionales"],
    "tipos_doc": ["Cédula de ciudadanía", "Cédula de extranjería", "Tarjeta de identidad", "Pasaporte"],
}))

# Páginas de sección (plantilla genérica, datos reales del mapa del sitio)
for label, out in SECTIONS:
    node = find_section(label) or {"label": label, "children": []}
    children = node.get("children", [])
    grupos = [c for c in children if c.get("children")]   # subsecciones con hijos
    hojas = [c for c in children if not c.get("children")]  # enlaces directos
    write(out, render_to_string("pages/seccion.html", {
        **CONTEXT, "active_nav": label, "seccion": node, "grupos": grupos, "hojas": hojas,
    }))

# Página "Manual de Estilo de la CGN" (nuevo espacio de la intranet)
_manual_estilo = {"label": "Manual de Estilo de la CGN", "children": [
    {"label": "Presentación", "url": "#"},
    {"label": "Principios de escritura", "url": "#"},
    {"label": "Tono y voz institucional", "url": "#"},
    {"label": "Capacitaciones", "url": "#"},
]}
write("manual-estilo.html", render_to_string("pages/seccion.html", {
    **CONTEXT, "active_nav": "En Casa", "seccion": _manual_estilo,
    "grupos": [], "hojas": _manual_estilo["children"],
}))

print("Build listo en:", DIST)
