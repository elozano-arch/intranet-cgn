#!/usr/bin/env bash
# Descarga los logos oficiales de las aplicaciones de la intranet CGN a
# static/img/apps/, para auto-hospedarlos en lugar de enlazarlos al servidor.
# Uso:  bash scripts/descargar-logos-apps.sh
# Luego, en data/apps.json cambia cada "logo" a "/static/img/apps/<archivo>.png".
set -euo pipefail
cd "$(dirname "$0")/.."
DEST="static/img/apps"; mkdir -p "$DEST"
BASE="https://www.contaduria.gov.co/o/intra-cgn-theme/images"

# nombre-local : archivo-remoto
MAP="
pagina-web:logo-web-cgn-1.png
aula-virtual:aula-virtual-ico-1.png
contadoc:controldoc.png
catalogo-cuentas:Catalago-cuentas.png
correo:correo175px-02.png
orfeo-consulta:orfeo150px-02.png
orfeo-v5:orfeov5-2.png
glpi:glpi150px.png
nomina:nomina-ico.png
inventarios:inventarios150px-02.png
plantillas:plantillas150px-02.png
"
for pair in $MAP; do
  name="${pair%%:*}"; remote="${pair##*:}"
  echo "→ $name.png"
  curl -fsSL -A "Mozilla/5.0" --connect-timeout 15 --max-time 60 "$BASE/$remote" -o "$DEST/$name.png"
done
echo "Listo. Logos en $DEST/"
