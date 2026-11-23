"""
Genera la web completa a partir de templates/:
  index.html, mali-house.html, dudi-house.html  (ingles)
  es/...                                                          (espanol)
  sitemap.xml, robots.txt

Uso:  python build.py
Despues de cambiar un texto en templates/ o aqui, vuelve a ejecutarlo.
"""
import json
import re
from datetime import date
from pathlib import Path

# >>> Cambia esto por el dominio definitivo cuando la web este publicada <<<
SITE_URL = "https://www.lajareshouses.com"

PHONE = "+34644871336"
EMAIL = "lajaresvillarental@gmail.com"
INSTAGRAM = "https://www.instagram.com/lajaresrental/"
ADDRESS = {"@type": "PostalAddress", "streetAddress": "Calle la Costilla", "addressLocality": "Lajares",
           "addressRegion": "Las Palmas", "postalCode": "35650", "addressCountry": "ES"}

ROOT = Path(__file__).parent
TPL = ROOT / "templates"
PHOTOS = json.loads((ROOT / "assets" / "photos.js").read_text(encoding="utf-8").split("=", 1)[1].rstrip().rstrip(";"))

# ---------------------------------------------------------------- textos ES
ES = {
    'nav.houses': 'Las casas', 'nav.gallery': 'Galería', 'nav.availability': 'Disponibilidad', 'nav.lajares': 'Lajares', 'nav.contact': 'Contacto', 'nav.book': 'Reserva directa',
    'hero.h1': 'Casas y villas con piscina climatizada en Lajares, Fuerteventura', 'hero.t1': 'Calma volcánica,', 'hero.t2': 'tu piscina climatizada.',
    'hero.lead': 'Dos villas de diseño con piscina climatizada en el pueblo más auténtico de Fuerteventura, a pocos minutos de las playas de El Cotillo y del mejor surf de la isla.',
    'quick.house': 'Casa', 'quick.guests': 'Huéspedes', 'quick.cta': 'Ver disponibilidad',
    'intro.kicker': 'Reserva directa con los propietarios',
    'intro.statement': 'Paredes encaladas, piedra de lava negra y palmeras que se mecen con los alisios. <em>Nuestras casas están hechas para días lentos</em>, pelo salado y cenas largas bajo las estrellas.',
    'intro.seo': 'Lajares Houses son dos villas de alquiler vacacional en Lajares, al norte de Fuerteventura: <a href="mali-house.html">Mali House</a>, para 4 personas, y <a href="dudi-house.html">Dudi House</a>, para 6 personas, ambas con piscina privada climatizada. Reserva directamente con los propietarios al mejor precio.',
    'stat.homes': 'villas en Lajares', 'stat.pools': 'piscinas privadas climatizadas', 'stat.beach': 'minutos a las playas de El Cotillo', 'stat.sun': 'días de clima primaveral',
    'houses.kicker': 'Las casas', 'houses.title': 'Dos villas, <em>una forma de vivir</em>',
    'mali.tag': 'Villa minimalista · piscina climatizada · barbacoa',
    'mali.desc': 'Una villa luminosa de una planta que rodea su piscina y un jardín volcánico de palmeras y cactus. Salón, cocina y dormitorios se abren a la tarima, para que el día fluya del desayuno a la puesta de sol sin paredes de por medio.',
    'mali.a1': 'Porche, barbacoa y solárium privado', 'mali.a2': 'Cocina totalmente equipada y lavandería', 'mali.a3': 'Ducha exterior para la vuelta de la playa', 'mali.a4': 'A pie de los cafés y restaurantes de Lajares',
    'dudi.tag': 'Villa familiar · piscina climatizada · patio interior',
    'dudi.desc': 'Espacio para todos: tres dormitorios dobles, un amplio salón-comedor abierto y una gran terraza alrededor de la piscina. Un patio de piedra volcánica da sombra y calma cuando aprieta el sol de la tarde.',
    'dudi.a1': 'Gran terraza con solárium', 'dudi.a2': 'Patio interior privado', 'dudi.a3': 'Cocina, salón y comedor abiertos', 'dudi.a4': 'Ducha exterior y sitio para las tablas',
    'spec.guests': 'huéspedes', 'spec.bedrooms': 'dormitorios', 'spec.bathrooms': 'baños', 'spec.bedroom': 'dormitorio', 'spec.bathroom': 'baño', 'spec.heated': 'piscina climat.', 'spec.terrace': 'terraza',
    'cta.dates': 'Ver fechas', 'cta.ask': 'Consultar fechas', 'cta.gallery': 'Fotos',
    'cta.disc_mali': 'Descubre Mali House', 'cta.disc_dudi': 'Descubre Dudi House',
    'gallery.kicker': 'Galería', 'gallery.title': 'Echa un <em>vistazo dentro</em>',
    'avail.kicker': 'Disponibilidad en tiempo real', 'avail.title': 'Elige tus <em>fechas</em>',
    'legend.free': 'Disponible', 'legend.busy': 'Reservado', 'legend.sel': 'Tu estancia',
    'req.in': 'Entrada', 'req.out': 'Salida', 'req.nights': 'Noches', 'req.hint': 'Toca tu día de llegada y después el de salida.',
    'req.name': 'Nombre', 'req.email': 'Email', 'req.guests': 'Huéspedes', 'req.msg': 'Mensaje (opcional)',
    'req.send': 'Enviar solicitud de reserva', 'req.ig': 'O escríbenos por Instagram',
    'req.small': 'Sin pago ahora. Te respondemos en 24 horas con el precio y cómo confirmar.',
    'place.kicker': 'El pueblo', 'place.title': 'Lajares, el <em>alma del norte</em>',
    'place.p1': 'Entre el volcán Calderón Hondo y el Atlántico, Lajares es donde surfistas, artistas y familias vienen a bajar el ritmo. Mercadillo artesanal los sábados, pequeños cafés, escuelas de surf y pistas de tierra hacia los campos de lava, todo a pie o en bici.',
    'dist.cotillo': 'Playas y lagunas de El Cotillo', 'dist.corralejo': 'Corralejo y sus dunas', 'dist.ferry': 'Ferry a Lobos y Lanzarote', 'dist.airport': 'Aeropuerto de Fuerteventura',
    'pc.1': 'Jardines volcánicos', 'pc.2': 'Conchas de El Cotillo', 'pc.3': 'Libros para tardes lentas',
    'faq.kicker': 'Bueno saberlo', 'faq.title': 'Preguntas, <em>respondidas</em>',
    'faq.q1': '¿Por qué reservar directo y no en una plataforma?', 'faq.a1': 'Hablas directamente con los propietarios, recibes una bienvenida personal y te ahorras las comisiones de la plataforma. El calendario de esta página está sincronizado con nuestras reservas, así que las fechas que ves son reales.',
    'faq.q2': '¿La piscina está climatizada todo el año?', 'faq.a2': 'Sí. Mali House y Dudi House tienen cada una su piscina privada climatizada, así que puedes bañarte a gusto también en invierno.',
    'faq.q3': '¿Necesito coche?', 'faq.a3': 'En Lajares puedes ir andando a restaurantes, cafés y tiendas. Para explorar las playas de El Cotillo, Corralejo y el resto de la isla, un coche o una bici lo hacen fácil.',
    'faq.q4': '¿Cómo funciona la solicitud de reserva?', 'faq.a4': 'Elige tus fechas en el calendario y envía la solicitud. Te respondemos en 24 horas con el precio total y los pasos para confirmar. No se cobra nada hasta que estés de acuerdo.',
    'contact.kicker': 'Contacto', 'contact.title': 'Tu <em>casa en la isla</em> te espera.', 'contact.phone': 'Teléfono', 'contact.address': 'Dirección',
    'foot.top': 'Volver arriba ↑',
    'house.amen': 'Lo que encontrarás', 'others.kicker': 'También en Lajares', 'others.title': 'Nuestras otras <em>casas</em>',
}

# ---------------------------------------------------------------- casas
HOUSES = {
  "mali": {
    "page": "mali-house.html", "name": "Mali House", "guests": 4, "bedrooms": 2, "bathrooms": 2, "pool": True,
    "hero": "img/mali/mali-03.jpg", "card": "img/mali/mali-01-sm.jpg",
    "en": {
      "title": "Mali House · Villa with heated pool in Lajares, Fuerteventura",
      "desc": "Mali House is a 2-bedroom villa for 4 guests with a private heated pool, barbecue and volcanic garden in Lajares, Fuerteventura. Check live availability and book direct.",
      "h1": "Villa with private heated pool in Lajares, Fuerteventura · 4 guests",
      "kicker": "Villa for 4 · Lajares", "htitle": "A minimalist villa <em>around its pool</em>",
      "paras": [
        "Mali House is a bright, single-storey villa in a quiet residential street of Lajares, in the north of Fuerteventura. White walls, timber decking and big sliding windows wrap around a private heated saltwater pool, open all year and sheltered from the wind, in a fenced garden of palms, cacti and black volcanic stone.",
        "Inside there are two bedrooms and two bathrooms, an open living and dining room and a fully equipped kitchen with laundry area. Everything opens to the porch, so breakfast, siestas by the pool and barbecue dinners all happen outdoors.",
        "Lajares is a laid-back surf village where you can walk everywhere: cafés, restaurants and the supermarket are a short stroll away. The beaches and lagoons of El Cotillo are about 10 minutes by car and Corralejo about 15. Guests rate Mali House 4.93 out of 5 on Airbnb, where it is a Guest Favourite.",
      ],
      "amen": ["Private heated pool, usable all year", "Porch with outdoor dining table", "Barbecue and private solarium", "Sun loungers and volcanic garden", "Fully equipped kitchen", "Laundry area with washing machine", "Outdoor shower", "Smart TV in the living room", "Walking distance to the village"],
      "gtitle": "Mali House <em>in pictures</em>",
    },
    "es": {
      "title": "Mali House · Villa con piscina climatizada en Lajares, Fuerteventura",
      "desc": "Mali House: villa de 2 dormitorios para 4 personas con piscina privada climatizada, barbacoa y jardín volcánico en Lajares, Fuerteventura. Consulta disponibilidad y reserva directa.",
      "h1": "Villa con piscina privada climatizada en Lajares, Fuerteventura · 4 personas",
      "kicker": "Villa para 4 · Lajares", "htitle": "Una villa minimalista <em>alrededor de su piscina</em>",
      "paras": [
        "Mali House es una villa luminosa de una sola planta en una calle tranquila de Lajares, al norte de Fuerteventura. Paredes blancas, tarima de madera y grandes ventanales rodean una piscina privada climatizada de agua salada, abierta todo el año y protegida del viento, en un jardín vallado de palmeras, cactus y piedra volcánica negra.",
        "Dentro tiene dos dormitorios y dos baños, un salón-comedor abierto y una cocina totalmente equipada con zona de lavandería. Todo se abre al porche, así que desayunos, siestas junto a la piscina y cenas de barbacoa se hacen al aire libre.",
        "Lajares es un pueblo surfero y tranquilo donde se va andando a todas partes: cafés, restaurantes y supermercado están a un paseo. Las playas y lagunas de El Cotillo están a unos 10 minutos en coche y Corralejo a unos 15. Los huéspedes valoran Mali House con un 4,93 sobre 5 en Airbnb, donde es Favorito de los viajeros.",
      ],
      "amen": ["Piscina privada climatizada todo el año", "Porche con mesa de comedor exterior", "Barbacoa y solárium privado", "Tumbonas y jardín volcánico", "Cocina totalmente equipada", "Lavandería con lavadora", "Ducha exterior", "Smart TV en el salón", "A pie del centro del pueblo"],
      "gtitle": "Mali House <em>en fotos</em>",
    },
  },
  "dudi": {
    "page": "dudi-house.html", "name": "Dudi House", "guests": 6, "bedrooms": 3, "bathrooms": 2, "pool": True,
    "hero": "img/dudi/dudi-01.jpg", "card": "img/dudi/dudi-01-sm.jpg",
    "en": {
      "title": "Dudi House · Family villa with heated pool in Lajares, Fuerteventura",
      "desc": "Dudi House is a 3-bedroom villa for 6 guests with a private heated pool, large terrace and inner courtyard in Lajares, Fuerteventura. Check live availability and book direct.",
      "h1": "Family villa with private heated pool in Lajares, Fuerteventura · 6 guests",
      "kicker": "Villa for 6 · Lajares", "htitle": "Room for everyone, <em>sun all day</em>",
      "paras": [
        "Dudi House is a spacious family villa in Lajares, in the north of Fuerteventura, built around a private heated pool and a big terrace with solarium. Lava-stone walls and palms give it privacy, and an inner courtyard offers shade when the afternoon sun is strong.",
        "It has three double bedrooms and two full bathrooms, a generous open-plan living and dining area and a modern, fully equipped kitchen. It's ideal for families or groups of friends travelling together.",
        "Outside there is a covered terrace with sun loungers, a charcoal barbecue and an outdoor dining table. Lajares village, with its cafés, bakeries, supermarket and Saturday craft market, is a short walk away; El Cotillo's beaches are about 10 minutes by car and Corralejo about 15. Guests rate Dudi House 4.95 out of 5 on Airbnb, where it is a Guest Favourite.",
      ],
      "amen": ["Private heated pool, usable all year", "Large terrace with solarium and sun loungers", "Covered outdoor dining area", "Private inner courtyard", "Open-plan living and dining room", "Modern fully equipped kitchen", "Outdoor shower", "Space to store surfboards", "Smart TV"],
      "gtitle": "Dudi House <em>in pictures</em>",
    },
    "es": {
      "title": "Dudi House · Villa familiar con piscina climatizada en Lajares, Fuerteventura",
      "desc": "Dudi House: villa de 3 dormitorios para 6 personas con piscina privada climatizada, gran terraza y patio interior en Lajares, Fuerteventura. Consulta disponibilidad y reserva directa.",
      "h1": "Villa familiar con piscina privada climatizada en Lajares, Fuerteventura · 6 personas",
      "kicker": "Villa para 6 · Lajares", "htitle": "Espacio para todos, <em>sol todo el día</em>",
      "paras": [
        "Dudi House es una amplia villa familiar en Lajares, al norte de Fuerteventura, construida alrededor de una piscina privada climatizada y una gran terraza con solárium. Los muros de piedra volcánica y las palmeras le dan intimidad, y un patio interior ofrece sombra cuando el sol de la tarde aprieta.",
        "Tiene tres dormitorios dobles y dos baños completos, un salón-comedor abierto muy amplio y una cocina moderna totalmente equipada. Es ideal para familias o grupos de amigos que viajan juntos.",
        "Fuera hay una terraza cubierta con tumbonas, barbacoa de carbón y comedor al aire libre. El pueblo de Lajares, con sus cafés, panaderías, supermercado y el mercadillo artesanal de los sábados, está a un paseo; las playas de El Cotillo están a unos 10 minutos en coche y Corralejo a unos 15. Los huéspedes valoran Dudi House con un 4,95 sobre 5 en Airbnb, donde es Favorito de los viajeros.",
      ],
      "amen": ["Piscina privada climatizada todo el año", "Gran terraza con solárium y tumbonas", "Comedor exterior cubierto", "Patio interior privado", "Salón-comedor abierto", "Cocina moderna totalmente equipada", "Ducha exterior", "Sitio para guardar las tablas de surf", "Smart TV"],
      "gtitle": "Dudi House <em>en fotos</em>",
    },
  }
}

ALT_ES = {
 'mali': ['Piscina y porche de Mali House','Jardín y piscina de Mali House','Mali House desde el jardín','Mali House de noche desde el aire','Comedor exterior junto a la piscina','Salón abierto a la piscina','Salón','Comedor y cocina','Salón-comedor con vistas a la piscina','Dormitorio principal','Dormitorio principal','Dormitorio doble con vistas a la piscina','Dormitorio con dos camas','Baño con ventana al jardín','Escalera de la piscina','Ducha exterior','Piscina privada climatizada','Jardín volcánico','Barbacoa y solárium','Entrada de Mali House'],
 'dudi': ['Piscina y terraza de Dudi House','Dudi House de noche desde el aire','Comedor en la terraza cubierta','Piscina y tumbonas','Salón-comedor abierto','Comedor y cocina','Salón','Zona de estar','Dormitorio principal','Dormitorio principal','Dormitorio con tabla de surf','Dormitorio con dos camas','Rincón de la piscina','Ducha exterior','Escalera de la piscina','Patio interior','Comedor exterior','Cartel de Dudi House','Baño','Dudi House de noche'],
}

INDEX = {
  "en": {"title": "Lajares Houses · Holiday villas with heated pool in Lajares, Fuerteventura",
         "desc": "Holiday villas in Lajares, Fuerteventura: Mali House (4 guests) and Dudi House (6 guests) with private heated pools. Live availability, book direct with the owners."},
  "es": {"title": "Lajares Houses · Casas y villas con piscina climatizada en Lajares, Fuerteventura",
         "desc": "Alquiler vacacional en Lajares, Fuerteventura: Mali House (4 personas) y Dudi House (6 personas) con piscina privada climatizada. Disponibilidad en tiempo real y reserva directa."},
}
SPEC = {"en": ("guests", "bedrooms", "bedroom", "bathrooms", "bathroom", "heated pool", "terrace"),
        "es": ("huéspedes", "dormitorios", "dormitorio", "baños", "baño", "piscina climatizada", "terraza")}

# ---------------------------------------------------------------- helpers
from content import (RATINGS, HOST, COLLAGE, PRICES, LICENSES, CHECKIN, CHECKOUT, COORDS, MAPS_LINK, MAP_EMBED, LOGO, icon,
                     AMENITIES, REVIEWS, ES_EXTRA, INFO, LOC, GUIDE)
ES.update(ES_EXTRA)

def url(lang, page):
    page = "" if page == "index.html" else page
    return f"{SITE_URL}/{'es/' if lang == 'es' else ''}{page}"

def apply_es(html):
    pat = re.compile(r'(<(\w+)\b[^>]*?\bdata-i18n="([^"]+)"[^>]*>)(.*?)(</\2>)', re.S)
    return pat.sub(lambda m: m.group(1) + ES.get(m.group(3), m.group(4)) + m.group(5), html)

def jsonld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + "</script>"

def business():
    return {"@type": "LodgingBusiness", "@id": SITE_URL + "/#business", "name": "Lajares Houses",
            "alternateName": ["Mali & Dudi Houses", "Lajares Villa Rental"], "url": SITE_URL + "/",
            "telephone": PHONE, "email": EMAIL, "address": ADDRESS, "sameAs": [INSTAGRAM],
            "geo": {"@type": "GeoCoordinates", "latitude": COORDS["mali"][0], "longitude": COORDS["mali"][1]},
            "image": [SITE_URL + "/img/hero/hero-02.jpg", SITE_URL + "/img/hero/hero-01.jpg"],
            "priceRange": "€€", "areaServed": "Lajares, Fuerteventura"}

def head(lang, page, title, desc, image, ld):
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url(lang, page)}">
<link rel="alternate" hreflang="en" href="{url('en', page)}">
<link rel="alternate" hreflang="es" href="{url('es', page)}">
<link rel="alternate" hreflang="x-default" href="{url('en', page)}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Lajares Houses">
<meta property="og:locale" content="{'es_ES' if lang == 'es' else 'en_GB'}">
<meta property="og:locale:alternate" content="{'en_GB' if lang == 'es' else 'es_ES'}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url(lang, page)}">
<meta property="og:image" content="{SITE_URL}/{image}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#1F1D1B">
{jsonld(ld)}'''

def partial(name):
    return (TPL / f"_{name}.html").read_text(encoding="utf-8")

def map_block(key, lang):
    t = (lambda k: ES[k]) if lang == "es" else (lambda k: {"map.load": "Show map", "map.open": "Open in Google Maps",
                                                          "map.note": "The map loads from Google when you click."}[k])
    # the home page map shows the exact pin of each house, switchable with tabs
    if key == "lajares":
        tabs = json.dumps([{"name": "Mali House", "src": MAP_EMBED["mali"]}, {"name": "Dudi House", "src": MAP_EMBED["dudi"]}])
        src, link, attr = MAP_EMBED["mali"], MAPS_LINK["mali"], f" data-tabs='{tabs}'"
        label = "Mali House &amp; Dudi House · C. la Costilla · Lajares"
    else:
        src, link, attr = MAP_EMBED[key], MAPS_LINK[key], ""
        label = (HOUSES[key]["name"] + " · " if COORDS.get(key) else "") + "C. la Costilla · 35650 Lajares"
    return (f'<div class="map map--lazy rv" data-src="{src}"{attr}>'
            f'<div class="map__ph">{icon("map")}<p>{label}</p>'
            f'<button type="button" class="btn btn--dark btn--sm map__btn">{t("map.load")}</button>'
            f'<a class="link" href="{link}" target="_blank" rel="noopener">{t("map.open")}</a>'
            f'<small>{t("map.note")}</small></div></div>')

def num(x, lang):
    return f"{x:.2f}".rstrip("0").rstrip(".") .replace(".", ",") if lang == "es" else f"{x:.2f}".rstrip("0").rstrip(".")

def rating_block(key, lang):
    r = RATINGS.get(key)
    if not r:
        return ""
    fav = ("Guest favourite on Airbnb" if lang == "en" else "Favorito de los viajeros en Airbnb") if r["fav"] else "Airbnb"
    cats = "".join(f'<div class="rating__cat"><span>{en if lang == "en" else es}</span><b>{num(v, lang) if v % 1 else f"{v:.1f}".replace(".", "," if lang == "es" else ".")}</b>'
                   f'<i style="--v:{v / 5:.3f}"></i></div>' for en, es, v in r["cats"])
    return (f'<div class="rating rv"><div class="rating__main"><svg class="rating__laurel" viewBox="0 0 32 64" aria-hidden="true"><path d="M24 60C10 52 6 36 10 18" fill="none" stroke="currentColor" stroke-width="2"/><g fill="currentColor"><ellipse cx="7" cy="20" rx="3" ry="7" transform="rotate(-20 7 20)"/><ellipse cx="5" cy="33" rx="3" ry="7" transform="rotate(-40 5 33)"/><ellipse cx="8" cy="45" rx="3" ry="7" transform="rotate(-60 8 45)"/><ellipse cx="15" cy="54" rx="3" ry="6.5" transform="rotate(-75 15 54)"/><ellipse cx="15" cy="26" rx="2.6" ry="6" transform="rotate(25 15 26)"/><ellipse cx="15" cy="39" rx="2.6" ry="6" transform="rotate(10 15 39)"/></g></svg>'
            f'<b>{num(r["score"], lang)}</b><svg class="rating__laurel rating__laurel--r" viewBox="0 0 32 64" aria-hidden="true"><path d="M24 60C10 52 6 36 10 18" fill="none" stroke="currentColor" stroke-width="2"/><g fill="currentColor"><ellipse cx="7" cy="20" rx="3" ry="7" transform="rotate(-20 7 20)"/><ellipse cx="5" cy="33" rx="3" ry="7" transform="rotate(-40 5 33)"/><ellipse cx="8" cy="45" rx="3" ry="7" transform="rotate(-60 8 45)"/><ellipse cx="15" cy="54" rx="3" ry="6.5" transform="rotate(-75 15 54)"/><ellipse cx="15" cy="26" rx="2.6" ry="6" transform="rotate(25 15 26)"/><ellipse cx="15" cy="39" rx="2.6" ry="6" transform="rotate(10 15 39)"/></g></svg></div>'
            f'<div class="rating__txt"><p class="rating__fav">{fav}</p><p>{r["count"]} {"reviews" if lang == "en" else "evaluaciones"} · {"one of the best-rated homes on Airbnb" if lang == "en" else "una de las casas mejor valoradas de Airbnb"}</p></div>'
            f'<div class="rating__cats">{cats}</div></div>')

def reviews_block(lang, house=None):
    items = [r for r in REVIEWS if (r.get("home") if house is None else r["house"] == house)]
    if not items:
        return ""
    stars = icon("star") * 5
    cards = "".join(
        f'<figure class="rev rv"><div class="rev__stars" aria-hidden="true">{stars}</div>'
        f'<blockquote>“{r[lang]}”</blockquote><figcaption><b>{r["name"]}</b>'
        f'<span>{HOUSES[r["house"]]["name"]} · {("Review on " if lang == "en" else "Opinión en ") + r["src"]}</span></figcaption></figure>' for r in items)
    summary = ""
    if house is None:
        rated = [(HOUSES[k]["name"], r) for k, r in RATINGS.items() if r]
        if rated:
            total = sum(r["count"] for _, r in rated)
            parts = " · ".join(f'{n} <b>{num(r["score"], lang)}</b>' for n, r in rated)
            tail = (f'{total} reviews on Airbnb · Guest favourites' if lang == "en"
                    else f'{total} evaluaciones en Airbnb · Favoritos de los viajeros')
            summary = f'<p class="revs__sum rv">{icon("star")}{parts} · {tail}</p>'
    return f'{summary}<div class="revs">{cards}</div>'

def host_block(lang):
    return (f'<div class="host rv"><span class="host__avatar" aria-hidden="true">{HOST["name"][0]}</span><div>'
            f'<p class="host__name">{"Your host" if lang == "en" else "Tu anfitrión"}: <b>{HOST["name"]}</b> · '
            f'{"Superhost" if lang == "en" else "Superanfitrión"}</p><p>{HOST[lang]}</p></div></div>')

def fill(html, vals, lang="en"):
    for _ in range(3):  # partials contain placeholders too
        for k, v in vals.items():
            html = html.replace("{{" + k + "}}", v)
    html = re.sub(r"\{\{icon:(\w+)\}\}", lambda m: icon(m.group(1)), html)
    html = re.sub(r"\{\{map:(\w+)\}\}", lambda m: map_block(m.group(1), lang), html)
    return html

def common(lang, page, license=""):
    other = f"../{page}" if lang == "es" else f"es/{page}"
    lic = ""
    if license:
        lic = f'<span>{"Registro" if lang == "es" else "Tourist licence"}: {license}</span>'
    return {
        "header": partial("header"), "footer": partial("footer"), "contact": partial("contact"),
        "availability": partial("availability"), "logo": LOGO, "regline": lic,
        "root": "../" if lang == "es" else "", "home": "" if page == "index.html" else "index.html",
        "url_en": other if lang == "es" else "#", "url_es": other if lang == "en" else "#",
        "act_en": "is-active" if lang == "en" else "", "act_es": "is-active" if lang == "es" else "",
    }

def write(lang, page, html):
    if lang == "es":
        html = apply_es(html)
    out = ROOT / ("es" if lang == "es" else "") / page
    out.parent.mkdir(exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print("  ", out.relative_to(ROOT))

def house_card(o, lang, extra_cls=""):
    return (f'        <a class="other rv{extra_cls}" href="{o["page"]}"><span class="other__img"><img src="{{{{root}}}}{o["card"]}" alt="{o["name"]}, Lajares" loading="lazy"></span>'
            f'<span class="other__name">{o["name"]}</span><span class="other__meta">{o[lang]["kicker"]}</span></a>')

# ---------------------------------------------------------------- pages
def build_index(lang):
    faq = [("faq.q1", "faq.a1"), ("faq.q2", "faq.a2"), ("faq.q3", "faq.a3"), ("faq.q4", "faq.a4")]
    tpl = (TPL / "index.html").read_text(encoding="utf-8")
    texts = {}
    for q, a in faq:
        texts[q] = re.search(rf'data-i18n="{q}">(.*?)<', tpl).group(1)
        texts[a] = re.search(rf'data-i18n="{a}">(.*?)<', tpl).group(1)
    tr = (lambda k: ES[k]) if lang == "es" else (lambda k: texts[k])
    ld = {"@context": "https://schema.org", "@graph": [
        business(),
        {"@type": "WebSite", "@id": SITE_URL + "/#site", "name": "Lajares Houses", "url": SITE_URL + "/", "inLanguage": lang},
        {"@type": "ItemList", "name": "Lajares Houses", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": h["name"], "url": url(lang, h["page"])} for i, h in enumerate(HOUSES.values())]},
        {"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": tr(q), "acceptedAnswer": {"@type": "Answer", "text": tr(a)}} for q, a in faq]},
    ]}
    vals = common(lang, "index.html")
    vals.update(head=head(lang, "index.html", INDEX[lang]["title"], INDEX[lang]["desc"], "img/hero/hero-02.jpg", ld),
                avail_attr="", reviews=reviews_block(lang))
    write(lang, "index.html", fill(tpl, vals, lang))

def build_house(key, lang):
    h = HOUSES[key]; t = h[lang]; s = SPEC[lang]
    specs = [(h["guests"], s[0]), (h["bedrooms"], s[1] if h["bedrooms"] > 1 else s[2]),
             (h["bathrooms"], s[3] if h["bathrooms"] > 1 else s[4]), ("☀" if h["pool"] else "✦", s[5] if h["pool"] else s[6])]
    alts = ALT_ES[key] if lang == "es" else [p["alt"] for p in PHOTOS[key]]
    photos = PHOTOS[key]
    # photo tour: one wide photo, then two side by side, repeating (Airbnb style)
    gallery = "\n".join(
        f'    <figure class="{"is-wide" if i % 3 == 0 else "is-half"}" data-full="{{{{root}}}}{p["src"]}">'
        f'<img src="{{{{root}}}}{p["src"] if i % 3 == 0 else p["sm"]}" alt="{alts[i]} · {h["name"]}, Lajares" loading="lazy" '
        f'width="{1800 if i % 3 == 0 else 720}" height="{(950 if p["o"] == "p" else 480) * (2.5 if i % 3 == 0 else 1):.0f}">'
        f'<figcaption>{alts[i]}</figcaption></figure>'
        for i, p in enumerate(photos))
    # collage: the first photo big, then the next four landscape ones
    pick = COLLAGE.get(key) or [0] + [i for i, p in enumerate(photos) if i and p["o"] == "l"][:4]
    collage = "\n".join(
        f'        <button type="button" class="collage__item{" collage__item--big" if n == 0 else ""}" data-tour="{i}">'
        f'<img src="{{{{root}}}}{photos[i]["src"] if n == 0 else photos[i]["sm"]}" alt="{alts[i]} · {h["name"]}" '
        f'{"fetchpriority=\"high\"" if n == 0 else "loading=\"lazy\""}></button>'
        for n, i in enumerate(pick))
    count = f'{len(photos)} {"photos" if lang == "en" else "fotos"}'
    allphotos = f'{"Show all" if lang == "en" else "Ver las"} {len(photos)} {"photos" if lang == "en" else "fotos"}'
    others = "\n".join(house_card(o, lang) for k, o in HOUSES.items() if k != key)
    amen = "".join(f'<li class="rv">{icon(ic)}<span>{en if lang == "en" else es}</span></li>' for ic, en, es in AMENITIES[key])
    info = list(INFO[lang])
    if LICENSES[key]:
        info.append(("doc", "Tourist licence" if lang == "en" else "Registro turístico", LICENSES[key]))
    info_html = "".join(f'<div class="info__row">{icon(ic)}<dt>{a}</dt><dd>{b}</dd></div>' for ic, a, b in info)
    price = ""
    if PRICES[key]:
        price = (f'<p class="bookcard__name">{h["name"]}</p><p class="bookcard__price"><span>{"from" if lang == "en" else "desde"}</span> '
                 f'<b>€{PRICES[key]}</b> <span>{"/ night" if lang == "en" else "/ noche"}</span></p>')
    else:
        price = f'<p class="bookcard__name">{h["name"]}</p>'
    if RATINGS.get(key):
        rt = RATINGS[key]
        price += (f'<p class="bookcard__rating">{icon("star")}<b>{num(rt["score"], lang)}</b> · '
                  f'<a href="#reviews">{rt["count"]} {"reviews" if lang == "en" else "evaluaciones"}</a></p>')
    price += (f'<p class="bookcard__times">{"Check-in" if lang == "en" else "Entrada"} {CHECKIN} · '
              f'{"check-out" if lang == "en" else "salida"} {CHECKOUT} · {"flexible" if lang == "en" else "flexibles"}</p>')
    revs = reviews_block(lang, key)
    rev_section = ""
    if revs:
        rev_section = (f'<section class="reviews reviews--house" id="reviews"><div class="wrap">'
                       f'<header class="sec-head"><p class="kicker rv" data-i18n="rev.kicker">Guest stories</p>'
                       f'<h2 class="h2 rv" data-i18n="rev.title">What our guests <em>say</em></h2></header>{rating_block(key, lang)}{revs}</div></section>')
    first_rev = next((r for r in REVIEWS if r["house"] == key), None)
    quote = f'<blockquote class="pull rv">“{first_rev[lang]}”<cite>— {first_rev["name"]}</cite></blockquote>' if first_rev else ""
    page_url = url(lang, h["page"])
    rental = {"@type": "VacationRental", "@id": page_url + "#rental", "name": h["name"], "description": t["desc"], "url": page_url,
              "identifier": key, "brand": {"@id": SITE_URL + "/#business"}, "telephone": PHONE, "address": ADDRESS,
              "image": [f"{SITE_URL}/{p['src']}" for p in PHOTOS[key][:8]],
              "containsPlace": {"@type": "Accommodation", "additionalType": "EntirePlace",
                                "occupancy": {"@type": "QuantitativeValue", "maxValue": h["guests"]},
                                "numberOfBedrooms": h["bedrooms"], "numberOfBathroomsTotal": h["bathrooms"],
                                "amenityFeature": [{"@type": "LocationFeatureSpecification", "name": en, "value": True} for _, en, _ in AMENITIES[key]]}}
    if COORDS[key]:
        rental["geo"] = {"@type": "GeoCoordinates", "latitude": COORDS[key][0], "longitude": COORDS[key][1]}
    if PRICES[key]:
        rental["priceRange"] = f"from €{PRICES[key]} per night"
    ld = {"@context": "https://schema.org", "@graph": [
        business(), rental,
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Lajares Houses", "item": url(lang, "index.html")},
            {"@type": "ListItem", "position": 2, "name": h["name"], "item": page_url}]},
    ]}
    vals = common(lang, h["page"], LICENSES[key])
    vals.update(
        head=head(lang, h["page"], t["title"], t["desc"], h["hero"], ld),
        avail_attr=f' data-house="{key}"', h_key=key,
        h_hero=h["hero"], h_name=h["name"], h_h1=t["h1"], h_kicker=t["kicker"], h_title=t["htitle"],
        h_paras="\n        ".join(f'<p class="rv">{p}</p>' for p in t["paras"]),
        h_specs="".join(f"<li><b>{n}</b><span>{l}</span></li>" for n, l in specs),
        h_amen=amen, h_info=info_html, h_price=price, h_quote=quote + host_block(lang),
        h_subrev='<a href="#reviews" data-i18n="sub.reviews">Reviews</a>' if revs else "",
        h_reviews=rev_section, h_loc=LOC[key][lang], h_map=map_block(key, lang),
        h_gtitle=t["gtitle"], h_gallery=gallery, h_others=others,
        h_collage=collage, h_count=count, h_allphotos=allphotos,
    )
    write(lang, h["page"], fill((TPL / "house.html").read_text(encoding="utf-8"), vals, lang))

def build_guide(lang):
    g = GUIDE[lang]
    items = "\n".join(
        f'        <article class="gitem rv"><span class="gitem__n">{i + 1:02d}</span>{icon(ic)}<h2>{title}</h2><p>{text}</p>'
        f'<p class="gitem__tip"><b>{"Tip" if lang == "en" else "Consejo"}:</b> {tip}</p></article>'
        for i, (ic, title, text, tip) in enumerate(g["items"]))
    get = "".join(f'<div class="info__row">{icon(ic)}<dt>{a}</dt><dd>{b}</dd></div>' for ic, a, b in g["get"])
    houses = "\n".join(house_card(o, lang) for o in HOUSES.values())
    page = "lajares-guide.html"
    ld = {"@context": "https://schema.org", "@graph": [
        business(),
        {"@type": "Article", "headline": g["h1"], "description": g["desc"], "inLanguage": lang, "url": url(lang, page),
         "image": SITE_URL + "/img/island/island-01.jpg", "author": {"@id": SITE_URL + "/#business"},
         "about": {"@type": "Place", "name": "Lajares, Fuerteventura"}},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Lajares Houses", "item": url(lang, "index.html")},
            {"@type": "ListItem", "position": 2, "name": g["crumb"], "item": url(lang, page)}]},
    ]}
    vals = common(lang, page)
    vals.update(head=head(lang, page, g["title"], g["desc"], "img/island/island-01.jpg", ld), avail_attr="",
                g_crumb=g["crumb"], g_big=g["big"], g_h1=g["h1"], g_intro=g["intro"], g_items=items,
                g_get_k=g["get_k"], g_get_t=g["get_t"], g_get=get, g_stay_k=g["stay_k"], g_stay_t=g["stay_t"], g_houses=houses)
    write(lang, page, fill((TPL / "guide.html").read_text(encoding="utf-8"), vals, lang))

def build_seo_files():
    today = date.today().isoformat()
    pages = ["index.html"] + [h["page"] for h in HOUSES.values()] + ["lajares-guide.html"]
    rows = []
    for p in pages:
        for lang in ("en", "es"):
            alts = "".join(f'<xhtml:link rel="alternate" hreflang="{l}" href="{url(l, p)}"/>' for l in ("en", "es"))
            rows.append(f"  <url><loc>{url(lang, p)}</loc><lastmod>{today}</lastmod>{alts}</url>")
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
        'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(rows) + "\n</urlset>\n", encoding="utf-8")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nDisallow: /templates/\n\nSitemap: {SITE_URL}/sitemap.xml\n", encoding="utf-8")
    print("   sitemap.xml, robots.txt")

def write_photos_js():
    data = {k: [dict(p, alt_es=ALT_ES[k][i]) if k in ALT_ES else p for i, p in enumerate(v)] for k, v in PHOTOS.items()}
    (ROOT / "assets" / "photos.js").write_text("window.PHOTOS = " + json.dumps(data, ensure_ascii=False) + ";\n", encoding="utf-8")

if __name__ == "__main__":
    print("Generando web...")
    write_photos_js()
    for lang in ("en", "es"):
        build_index(lang)
        for key in HOUSES:
            build_house(key, lang)
        build_guide(lang)
    (ROOT / "404.html").write_text((TPL / "404.html").read_text(encoding="utf-8").replace("{{logo}}", LOGO), encoding="utf-8")
    print("   404.html")
    build_seo_files()
    print("Listo.")
