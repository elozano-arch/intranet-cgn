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

# Páginas de sección (plantilla genérica, datos reales del mapa del sitio)
for label, out in SECTIONS:
    node = find_section(label) or {"label": label, "children": []}
    children = node.get("children", [])
    grupos = [c for c in children if c.get("children")]   # subsecciones con hijos
    hojas = [c for c in children if not c.get("children")]  # enlaces directos
    write(out, render_to_string("pages/seccion.html", {
        **CONTEXT, "active_nav": label, "seccion": node, "grupos": grupos, "hojas": hojas,
    }))

print("Build listo en:", DIST)
