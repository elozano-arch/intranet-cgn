#!/usr/bin/env python3
"""
Build estático de la UI (solo presentación, sin backend).
Renderiza las plantillas Django a HTML estático en dist/ y copia los estáticos,
para desplegar en Vercel como sitio estático (sin servidor).

Uso:  python build_static.py
Requisitos:  pip install Django
"""
import os, shutil, json, re, unicodedata, django
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

# --- Generar una página de detalle por CADA enlace del mapa del sitio ---
# Asigna una URL real a cada hoja que apuntaba a "#", para poder previsualizar el
# diseño de las páginas internas. El contenido es de ejemplo (lo conecta el CMS).
DETALLES = []
_slugs = set()

# Datos de EJEMPLO reutilizados por las páginas de detalle (los conecta el CMS).
DEMO = {
    "ficha": [["Fecha de publicación", "(ejemplo)"], ["Versión", "1.0 (ejemplo)"],
              ["Responsable", "Dependencia responsable"], ["Formato", "PDF · 2.4 MB (ejemplo)"]],
    "tabla": [[f"Documento de ejemplo {i:02d}", f"Ref-2026-{i:03d}", "Vigente"] for i in range(1, 7)],
    "ediciones": [str(i) for i in range(1, 7)],
    "galeria": list(range(1, 10)),
    "noticias": list(range(1, 6)),
    "funciones": list(range(1, 5)),
    "eventos": [["12", "Reunión de ejemplo"], ["18", "Capacitación de ejemplo"], ["25", "Evento de ejemplo"]],
    "dias": ["", ""] + list(range(1, 31)),
}

def tipo_de(label, top):
    """Asigna el tipo de página según el contenido (mapea a page types de Wagtail)."""
    if label.startswith("Normograma") or label in ("Años anteriores", "Matriz de Publicaciones"):
        return "tabla"
    if label in ("Le Cuento Que", "Codex", "SIINERGIA Contable", "Coworking"):
        return "publicacion"
    if label == "Videos CGN":
        return "galeria_video"
    if label == "Condecoraciones CGN":
        return "galeria_foto"
    if label in ("Presentaciones del Contador General", "Plantillas"):
        return "galeria_doc"
    if label == "Doctrina al Día":
        return "noticias"
    if label == "Calendario de Eventos":
        return "calendario"
    if label == "Clasificados":
        return "clasificados"
    if label == "Mapa de sitio":
        return "mapa"
    if (label.startswith("GIT") or label.startswith("Gestión") or label.startswith("Comité")
            or label.startswith("Sistema de Gestión") or label.startswith("Seguridad")
            or label in ("Planeación", "Comunicación Pública", "Control y Evaluación", "SINTRA-CGN")):
        return "area"
    return "documento"

def slugify(text):
    t = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    t = re.sub(r"[^a-zA-Z0-9]+", "-", t).strip("-").lower()
    return t or "pagina"

def _nueva_url(label):
    base = slugify(label); s, i = base, 2
    while s in _slugs:
        s, i = f"{base}-{i}", i + 1
    _slugs.add(s)
    return s + ".html"

def _detalle(child, crumbs, hojas, active_nav, volver_url):
    out = _nueva_url(child["label"])
    child["url"] = out
    DETALLES.append({
        "out": out, "titulo": child["label"], "eyebrow": crumbs[-1]["label"],
        "crumbs": [{"label": "Inicio", "url": "/"}] + crumbs + [{"label": child["label"], "url": out}],
        "siblings": hojas, "active_nav": active_nav, "volver_url": volver_url,
        "tipo": tipo_de(child["label"], active_nav),
    })

def _collect(section):
    top_label, top_url = section["label"], section.get("url", "#")
    def rec(parent, crumbs):
        kids = parent.get("children", [])
        hojas = [c for c in kids if not c.get("children")]
        for child in kids:
            if child.get("children"):
                rec(child, crumbs + [{"label": child["label"], "url": top_url}])
            elif child.get("url", "#") == "#":
                _detalle(child, crumbs, hojas, top_label, top_url)
    rec(section, [{"label": top_label, "url": top_url}])

for _sec in NAV:
    if _sec.get("label") != "Inicio" and _sec.get("children"):
        _collect(_sec)

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
_manual_estilo = {"label": "Manual de Estilo de la CGN",
    "desc": "Guía de escritura, tono y voz institucional de la Contaduría General de la Nación.", "children": [
    {"label": "Presentación", "icon": "doctrina", "url": "#"},
    {"label": "Principios de escritura", "icon": "estilo", "url": "#"},
    {"label": "Tono y voz institucional", "icon": "identidad", "url": "#"},
    {"label": "Capacitaciones", "icon": "capacitacion", "url": "#"},
]}
# Detalle para las subsecciones del Manual de Estilo
_me_crumbs = [{"label": "En Casa", "url": "en-casa.html"},
              {"label": "Manual de Estilo de la CGN", "url": "manual-estilo.html"}]
for _ch in _manual_estilo["children"]:
    if _ch.get("url", "#") == "#":
        _detalle(_ch, _me_crumbs, _manual_estilo["children"], "En Casa", "manual-estilo.html")
write("manual-estilo.html", render_to_string("pages/seccion.html", {
    **CONTEXT, "active_nav": "En Casa", "seccion": _manual_estilo,
    "grupos": [], "hojas": _manual_estilo["children"],
}))

# Páginas de detalle (una por enlace) — contenido de ejemplo para ver el diseño
for d in DETALLES:
    write(d["out"], render_to_string("pages/detalle.html", {
        **CONTEXT, "active_nav": d["active_nav"], "titulo": d["titulo"],
        "eyebrow": d["eyebrow"], "crumbs": d["crumbs"],
        "siblings": d["siblings"], "volver_url": d["volver_url"],
        "tipo": d["tipo"], "demo": DEMO,
    }))
_tipos = {}
for d in DETALLES:
    _tipos[d["tipo"]] = _tipos.get(d["tipo"], 0) + 1
print(f"Páginas de detalle generadas: {len(DETALLES)} · por tipo: {_tipos}")

print("Build listo en:", DIST)
