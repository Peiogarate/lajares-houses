# Web Lajares Houses: guía rápida

## Qué hay en esta carpeta
- `index.html` es la página (en inglés y español, con botón EN/ES arriba).
- `assets/` contiene el diseño (`style.css`), el funcionamiento (`app.js`) y la lista de fotos de la galería (`photos.js`).
- `img/` guarda 72 fotos de Rafal y Mario, ya optimizadas para la web (unos 23 MB en total).
- `data/availability.js` son los días ocupados de cada casa. Lo genera `sync_calendar.py`.
- `.github/workflows/sync-calendar.yml` actualiza el calendario solo, cada 3 horas, si la web está en GitHub.

## Verla en tu ordenador
Haz doble clic en `index.html`. Funciona sin instalar nada.

## Cómo funciona el calendario
1. Airbnb exporta el iCal y Google Calendar lo importa. La web usa esos mismos dos calendarios públicos (Mali y Dudi).
2. `sync_calendar.py` los descarga y escribe `data/availability.js`.
3. La web pinta los días ocupados. El cliente elige entrada y salida, y la web no le deja coger noches reservadas.
4. Al pulsar **Enviar solicitud de reserva**, se abre su email con todo rellenado para enviarlo a lajaresvillarental@gmail.com. También puede copiar el mensaje y abrir vuestro chat de Instagram.

Para actualizar el calendario a mano: `python sync_calendar.py`.

También podéis poner en `sync_calendar.py` directamente los enlaces iCal de Airbnb de Mali y Dudi, en lugar de los de Google.

## Publicarla gratis (recomendado: GitHub Pages)
1. Crea una cuenta en github.com y un repositorio nuevo, por ejemplo `lajares-houses`.
2. Sube **todo el contenido** de esta carpeta, incluida la carpeta oculta `.github`.
3. En el repositorio, entra en Settings → Pages → Source: *Deploy from a branch* → `main` / root → Save.
4. En Settings → Actions → General → Workflow permissions, marca *Read and write permissions*.
5. En unos minutos la web estará en `https://TU-USUARIO.github.io/lajares-houses/`. El calendario se actualizará solo cada 3 horas.
6. Opcional: compra un dominio (por ejemplo `lajareshouses.com`) y conéctalo en Settings → Pages → Custom domain.

Alternativa rápida: Netlify Drop (app.netlify.com/drop). Arrastras la carpeta y queda publicada, pero el calendario no se actualiza solo. Habría que volver a subirla después de ejecutar `python sync_calendar.py`.

## Páginas que tiene la web
| Inglés | Español |
|---|---|
| `index.html` (portada) | `es/index.html` |
| `mali-house.html` | `es/mali-house.html` |
| `dudi-house.html` | `es/dudi-house.html` |

Estas páginas **se generan** con `python build.py`. No las edites a mano, porque se sobrescriben al volver a generarlas.

## Cambiar textos o fotos
- **Portada en inglés:** `templates/index.html`. Cabecera, pie, calendario y contacto están en `templates/_*.html`.
- **Textos en español de la portada:** `build.py`, en el bloque `ES = { ... }`.
- **Textos de cada casa** (en inglés y español): `build.py`, en el bloque `HOUSES`.
- **Precios, números de licencia (VV), horarios de entrada y salida, reseñas, servicios de cada casa y guía de Lajares:** `content.py`. Si un dato está vacío, no aparece en la web.
- **Teléfono, email, dominio:** al principio de `build.py`. El teléfono está también en `templates/_contact.html`.
- **Fotos:** sustituye un archivo de `img/` por otro con el mismo nombre.
- Después de cualquier cambio, ejecuta `python build.py`.

## Para salir arriba en Google (búsquedas de Lajares, Mali House y Dudi House)
Lo que ya lleva la web:
- Una página propia para cada casa. El título y el encabezado principal (H1) incluyen el nombre de la casa y "Lajares, Fuerteventura".
- Las páginas en español son de verdad, no traducidas por JavaScript. Así Google las encuentra al buscar "alquiler vacacional Lajares" o "villa con piscina Lajares".
- Datos estructurados (schema.org) que le dicen a Google que es un alojamiento, con dirección, teléfono, capacidad, fotos y preguntas frecuentes.
- `sitemap.xml`, `robots.txt`, URL canónicas, etiquetas hreflang EN/ES y descripciones de cada foto (texto alternativo) con "Lajares".

Lo que hay que hacer al publicar (no se puede hacer desde la web):
1. **Dominio propio.** Por ejemplo `lajareshouses.com`. Ponlo en `SITE_URL` dentro de `build.py` y vuelve a ejecutar `python build.py`.
2. **Google Search Console** (search.google.com/search-console). Añade el dominio y envía `sitemap.xml`. Sin esto, Google puede tardar semanas en encontrar la web.
3. **Ficha de Google Business Profile** ("Lajares Houses", categoría *Alquiler vacacional*, con la web y el teléfono). Es lo que más ayuda a salir en Google Maps y en las búsquedas de "Lajares".
4. **Enlaces hacia la web.** Bio de Instagram, Facebook, guías locales, escuelas de surf amigas... Cada enlace ayuda.
5. **Reseñas** en la ficha de Google. Pídeselas a los huéspedes al irse.

Nadie puede garantizar el primer puesto en Google. Con el nombre propio ("Mali House Lajares", "Dudi House Lajares") es fácil salir primero en pocas semanas. Con "Lajares" a secas hay más competencia, y ahí cuentan mucho la ficha de Google y las reseñas.

## Cosas que conviene revisar
- La web promete: *"Te respondemos en 24 horas"*. Si no lo vais a cumplir, cambiadlo.
- Las distancias de la sección Lajares son aproximadas: El Cotillo 10 min, Corralejo 15, ferry 20 y aeropuerto 40.
- No hay precios ni reseñas, porque no tenía datos reales. Si me los pasáis, los añado.
