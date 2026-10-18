# Sistema de diseño del portafolio

Referencia: estilo **Seline Analytics** de Refero (<https://styles.refero.design/style/7967c6d9-e50c-42b5-b4d1-74003ba41781>). Los tokens originales están en `tokens.json` y `variables.css`; `assets/css/styles.css` los aplica.

Idea: una mesa de analista sobre papel cálido. Superficies blancas con borde fino, texto grande y ligero, y un único acento cian que solo aparece donde hay una acción o una palabra clave.

## Color

| Rol | Valor | Uso |
| --- | --- | --- |
| Lienzo | `#fafaf9` | Fondo de página |
| Tarjeta | `#ffffff` | Superficies elevadas, sin sombra |
| Tinta | `#0c0a09` | Titulares y texto fuerte |
| Texto | `#57534e` | Párrafos (derivado de la misma familia piedra) |
| Apagado | `#78716c` | Metadatos y navegación |
| Borde fino | `#e8e6e5` | Estructura principal: bordes, no divisores gruesos |
| Hollín | `#1c1917` | Única superficie oscura: la tarjeta de contacto |
| Cian | `#3ba6f1` | Botón principal y puntos de estado |
| Cian de texto | `#1a73b5` | Cian con contraste AA para texto |
| Cielo | `#c1e1f7` | Resaltador de una palabra en el titular |

Regla: un solo acento. El botón principal es el elemento más llamativo de cada vista.

## Tipografía

- **Schibsted Grotesk 400** para titulares, con tracking negativo. Sustituye a Roobert (de pago). Nunca en negrita.
- **Inter** para cuerpo e interfaz. Variable, alojada en `assets/fonts/`.
- **JetBrains Mono** para fechas, estados y etiquetas técnicas.

## Forma

- Botones y etiquetas: píldora (`9999px`).
- Tarjetas grandes: `16px`. Tarjetas pequeñas: `10px`. Cajas de flujo: `6px`.
- Sin sombras. La profundidad la dan la superficie y el borde.

## Espaciado

Base de 4 px. Escala usada: 4, 8, 12, 16, 24, 32, 40, 48, 64, 96. Secciones separadas por 96 px en escritorio (64 px en móvil).

## Movimiento

Todo con [anime.js](https://animejs.com) 3.2.2 (`assets/js/anime.min.js`, local): cuadrícula de puntos que se propaga desde el cursor, anillos que laten, titulares palabra por palabra, trazos de iconos que se dibujan, entradas en cascada, contadores, botones magnéticos e inclinación 3D en tarjetas. Se desactiva con `prefers-reduced-motion`. Sin JavaScript todo es visible.

## Datos en vivo

La sección GitHub consulta la API pública (`api.github.com`, sin clave) al abrir la página y guarda el resultado 30 minutos en `sessionStorage`. Los repositorios mostrados se eligen en `render_github()` de `tools/build.py`. Si la API falla, se muestra un estado de error con enlace al perfil.

## Contenido

El contenido y sus traducciones viven en `tools/build.py`. Los estados de los proyectos son reales (por ejemplo, "En desarrollo" con la ingesta marcada como pendiente) y no se inflan cifras.
