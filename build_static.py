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

# Páginas a generar: (plantilla, archivo de salida)
# (plantilla, archivo de salida, sección activa en el menú)
PAGES = [
    ("pages/home.html", "index.html", "Inicio"),
    ("pages/en-casa.html", "en-casa.html", "En Casa"),
]

# Limpiar y recrear dist/
if os.path.isdir(DIST):
    shutil.rmtree(DIST)
os.makedirs(DIST)

# Copiar estáticos -> dist/static
shutil.copytree(os.path.join(BASE, "static"), os.path.join(DIST, "static"))

# Renderizar páginas
for template, out, active in PAGES:
    html = render_to_string(template, {**CONTEXT, "active_nav": active})
    with open(os.path.join(DIST, out), "w", encoding="utf-8") as f:
        f.write(html)
    print("✓", out)

print("Build listo en:", DIST)
