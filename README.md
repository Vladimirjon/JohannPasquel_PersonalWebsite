# Johann Pasquel — Portafolio

Sitio estático bilingüe (español e inglés) sobre desarrollo de software y soluciones de datos.

**En línea:** https://vladimirjon.github.io/JohannPasquel_PersonalWebsite/

## Estructura

| Ruta | Contenido |
| --- | --- |
| `index.html`, `en/index.html` | Páginas en español e inglés (generadas, no se editan a mano) |
| `tools/build.py` | Contenido y plantillas; genera los HTML, `sitemap.xml` y `robots.txt` |
| `assets/css/styles.css` | Estilos: tokens de color, tipografía y espaciado al inicio |
| `assets/js/main.js` | Solo el botón «Copiar correo» |
| `assets/fonts/` | Schibsted Grotesk y JetBrains Mono (SIL OFL), servidas localmente |
| `assets/Pasquel_Johann_CV.pdf` | CV descargable |
| `assets/img/` | Retrato, favicon e imagen para redes (`og.png`) |

## Actualizar el contenido

1. Edita los textos en `tools/build.py` (cada texto está junto a su traducción con `tr(es, en)`).
2. Ejecuta `python3 tools/build.py`.
3. Para previsualizar: `python3 -m http.server` y abre http://localhost:8000.
4. Haz commit de los HTML generados; GitHub Pages publica desde la rama principal.

Para actualizar el CV, reemplaza `assets/Pasquel_Johann_CV.pdf` conservando el nombre.

`.nojekyll` evita que GitHub Pages procese el sitio con Jekyll; no es necesario editarlo.
