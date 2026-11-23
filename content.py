"""Contenido extra de la web (lo usa build.py). Aqui se editan:
precios, numeros de licencia, horarios, resenas, servicios y la guia de Lajares."""

# ------------------------------------------------------------ datos que faltan
# Precio "desde" por noche (en euros). Deja None para no mostrar precio.
PRICES = {"mali": 220, "dudi": None}
# Numero de registro de vivienda vacacional (Canarias), p. ej. "VV-35-2-0001234".
# Es obligatorio mostrarlo en la publicidad de la vivienda. Deja "" mientras no lo tengas.
LICENSES = {"mali": "", "dudi": ""}
# Horarios de entrada / salida, p. ej. "16:00". Deja "" para no mostrarlos.
CHECKIN, CHECKOUT = "16:00", "10:00"

# Fotos del mosaico de cada casa (posicion en la galeria, la primera es la grande)
COLLAGE = {"mali": [0, 1, 5, 11, 3], "dudi": [0, 4, 8, 2, 1]}

COORDS = {"mali": (28.6816791, -13.9405905), "dudi": (28.680881, -13.9397515)}
MAPS_LINK = {
    "mali": "https://www.google.com/maps/search/?api=1&query=MALI+HOUSE+Lajares",
    "dudi": "https://www.google.com/maps/search/?api=1&query=DUDI+HOUSE+Lajares",
    "lajares": "https://www.google.com/maps/search/?api=1&query=Lajares+Fuerteventura",
}
MAP_EMBED = {
    "mali": "https://www.google.com/maps?q=28.6816791,-13.9405905&z=17&output=embed",
    "dudi": "https://www.google.com/maps?q=28.680881,-13.9397515&z=17&output=embed",
    "lajares": "https://www.google.com/maps?q=Lajares,+Fuerteventura&z=13&output=embed",
}

# ------------------------------------------------------------ logo e iconos
LOGO = ('<svg class="logo" viewBox="0 0 48 48" aria-hidden="true"><circle cx="24" cy="24" r="22.6" fill="none" '
        'stroke="currentColor" stroke-width="1.2"/><circle cx="31.5" cy="16.5" r="3.1" fill="currentColor"/>'
        '<path d="M6.5 31.5 16.5 19.5l5.5 6.5 5-5 14.5 10.5" fill="none" stroke="currentColor" stroke-width="1.4" '
        'stroke-linejoin="round"/><path d="M9 36.5q15-5 30 0" fill="none" stroke="currentColor" stroke-width="1.2"/></svg>')

_P = {
 "pool": '<path d="M3 17c2 1.3 4 1.3 6 0s4-1.3 6 0 4 1.3 6 0M3 21c2 1.3 4 1.3 6 0s4-1.3 6 0 4 1.3 6 0M8 15V5a2 2 0 0 1 4 0M16 15V5a2 2 0 0 1 4 0M8 8h8M8 12h8"/>',
 "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>',
 "bbq": '<path d="M4 10h16a8 8 0 0 1-16 0zM8 18l-2 4M16 18l2 4M9 3c0 1.5 1.5 1.5 1.5 3M13.5 3c0 1.5 1.5 1.5 1.5 3"/>',
 "kitchen": '<path d="M6 3v7a2 2 0 0 0 4 0V3M8 10v11M17 3c-2 0-3 2-3 6s1 5 3 5v7"/>',
 "washer": '<rect x="4" y="2.5" width="16" height="19" rx="2"/><circle cx="12" cy="13" r="5"/><path d="M7 6h.01M10 6h.01"/>',
 "shower": '<path d="M4 21V8a5 5 0 0 1 10 0M10 8h8M12 12v1M15 12v1M18 12v1M12 16v1M15 16v1M18 16v1"/>',
 "tv": '<rect x="2.5" y="5" width="19" height="13" rx="2"/><path d="M8 21h8M9 2l3 3 3-3"/>',
 "terrace": '<path d="M12 3a9 9 0 0 1 9 7H3a9 9 0 0 1 9-7zM12 10v11M7 21h10"/>',
 "garden": '<path d="M12 21V11M12 11C8 11 5 8 5 4c4 0 7 3 7 7zM12 13c3 0 6-2 6-6-3 0-6 2-6 6zM7 21h10"/>',
 "bed": '<path d="M3 18V7M3 13h18v5M21 13a3 3 0 0 0-3-3h-7v3M7 10.5a1.5 1.5 0 1 0 0-.01"/>',
 "bath": '<path d="M4 12h16v3a5 5 0 0 1-5 5H9a5 5 0 0 1-5-5zM6 12V5a2 2 0 0 1 4 0M7 20l-1 2M17 20l1 2"/>',
 "surf": '<path d="M17 3c-6 2-12 9-13 17 7-2 14-8 16-15l-3-2zM8 16l3 3"/>',
 "walk": '<circle cx="13" cy="4" r="2"/><path d="M10 22l2-7 3 3v6M9 12l2-5 3 2 3 1M8 13l1-4"/>',
 "court": '<rect x="3" y="3" width="18" height="18" rx="1"/><path d="M3 9h18M9 21V9"/>',
 "sofa": '<path d="M4 11V8a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v3M2 13a2 2 0 0 1 4 0v2h12v-2a2 2 0 0 1 4 0v5H2zM5 18v2M19 18v2"/>',
 "tag": '<path d="M3 12V3h9l9 9-9 9zM7.5 7.5h.01"/>',
 "chat": '<path d="M21 12a8 8 0 0 1-11.8 7L3 21l2-6A8 8 0 1 1 21 12z"/>',
 "calendar": '<rect x="3" y="4.5" width="18" height="16.5" rx="2"/><path d="M3 9.5h18M8 2.5v4M16 2.5v4M8 14l2.5 2.5L16 12"/>',
 "map": '<path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
 "volcano": '<path d="M2 20 9 8h6l7 12zM9 8l2 3 2-2 2-1M12 4V2M9 5 8 3.5M15 5l1-1.5"/>',
 "market": '<path d="M3 9l2-5h14l2 5M3 9h18v2a3 3 0 0 1-6 0 3 3 0 0 1-6 0 3 3 0 0 1-6 0zM5 13v8h14v-8"/>',
 "boat": '<path d="M3 17l2 4h14l2-4H3zM12 3v12M12 3l7 10h-7"/>',
 "dune": '<path d="M2 18c4-6 8-8 12-4 2-2 5-3 8 1M2 21h20"/>',
 "fish": '<path d="M3 12c3-5 10-6 14-2l4-3v10l-4-3c-4 4-11 3-14-2zM14 11h.01"/>',
 "plane": '<path d="M10.5 3.5a1.5 1.5 0 0 1 3 0V9l8 5v2l-8-2.5V18l2.5 2v1.5L12 20.5 8 21.5V20l2.5-2v-4.5L2.5 16v-2l8-5z"/>',
 "car": '<path d="M5 17h14M3 17v-4l2-5h14l2 5v4h-2M5 17H3M7.5 17a1.5 1.5 0 1 1-3 0M19.5 17a1.5 1.5 0 1 1-3 0M3 13h18"/>',
 "key": '<circle cx="8" cy="15" r="4"/><path d="M11 12l9-9M17 6l3 3M15 8l2 2"/>',
 "doc": '<path d="M6 2h9l5 5v15H6zM14 2v6h6M9 13h8M9 17h8"/>',
 "card": '<rect x="2.5" y="5" width="19" height="14" rx="2"/><path d="M2.5 10h19M6 15h4"/>',
 "heart": '<path d="M12 20s-8-4.6-8-10a4.5 4.5 0 0 1 8-2.8A4.5 4.5 0 0 1 20 10c0 5.4-8 10-8 10z"/>',
 "grid": '<rect x="3" y="3" width="7.5" height="7.5" rx="1"/><rect x="13.5" y="3" width="7.5" height="7.5" rx="1"/><rect x="3" y="13.5" width="7.5" height="7.5" rx="1"/><rect x="13.5" y="13.5" width="7.5" height="7.5" rx="1"/>',
 "back": '<path d="M15 5l-7 7 7 7"/>',
 "star":'<path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1L3.2 9.5l6.1-.9z"/>',
}
def icon(name):
    return ('<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{_P[name]}</svg>')

# ------------------------------------------------------------ servicios por casa
AMENITIES = {
 "mali": [("pool", "Heated saltwater pool, all year", "Piscina climatizada de agua salada, todo el año"), ("terrace", "Porch & outdoor dining", "Porche y comedor exterior"),
          ("bbq", "Barbecue", "Barbacoa"), ("sun", "Private solarium & loungers", "Solárium privado y tumbonas"),
          ("garden", "Fenced garden, sheltered from the wind", "Jardín vallado y protegido del viento"), ("kitchen", "Fully equipped kitchen & dishwasher", "Cocina equipada y lavavajillas"),
          ("washer", "Washing machine", "Lavadora"), ("shower", "Outdoor shower", "Ducha exterior"),
          ("tv", "Smart TV", "Smart TV"), ("bed", "2 bedrooms", "2 dormitorios"), ("bath", "2 bathrooms", "2 baños"),
          ("walk", "Walk to cafés, restaurants & supermarket", "A pie de cafés, restaurantes y súper")],
 "dudi": [("pool", "Private heated pool", "Piscina privada climatizada"), ("sun", "Terrace with solarium", "Terraza con solárium"),
          ("terrace", "Covered terrace with loungers & dining", "Terraza cubierta con tumbonas y comedor"), ("bbq", "Charcoal barbecue", "Barbacoa de carbón"), ("court", "Private inner courtyard", "Patio interior privado"),
          ("sofa", "Open-plan living & dining", "Salón-comedor abierto"), ("kitchen", "Modern equipped kitchen", "Cocina moderna equipada"),
          ("shower", "Outdoor shower", "Ducha exterior"), ("surf", "Space for surfboards", "Sitio para las tablas"),
          ("tv", "Smart TV", "Smart TV"), ("bed", "3 double bedrooms", "3 dormitorios dobles"), ("bath", "2 full bathrooms", "2 baños completos"),
          ("walk", "Walk to cafés, bakeries & supermarket", "A pie de cafés, panaderías y súper")],
}

# ------------------------------------------------------------ resenas reales (Airbnb y Google)
# "home": True = sale tambien en la portada
REVIEWS = [
 {"house": "mali", "name": "Julio", "src": "Airbnb", "home": True,
  "es": "Totalmente recomendable. Borja y Nicoletta fueron muy atentos en todo momento. La casa es genial, tal como se muestra en las fotos, y muy bien ubicada con todo lo necesario cerca. Vamos todos los años a Fuerteventura y es una de las mejores viviendas donde nos hemos quedado. Repetiremos sin dudarlo.",
  "en": "Highly recommended. Borja and Nicoletta were very attentive at all times. The house is great, just as it looks in the photos, and very well located with everything you need nearby. We come to Fuerteventura every year and it's one of the best homes we've stayed in. We'll definitely be back."},
 {"house": "mali", "name": "Richard", "src": "Airbnb", "home": True,
  "es": "¡Tuvimos una estancia muy relajada en Villa Mali, aún más porque la villa está bien equipada con un gran jardín, terraza y una preciosa piscina! Se encuentra en una ubicación muy tranquila, a pocos pasos del centro de Lajares y del supermercado local, y con las increíbles playas de El Cotillo a solo 10 minutos en coche. ¡Gracias, Borja!",
  "en": "We had a very relaxing stay at Villa Mali, even more so because it's so well equipped, with a big garden, terrace and a beautiful pool! The location is very quiet, a few steps from the centre of Lajares and the local supermarket, with El Cotillo's amazing beaches just 10 minutes away by car. Thanks, Borja!"},
 {"house": "mali", "name": "Joel", "src": "Airbnb", "home": True,
  "es": "Estancia fabulosa en Mali House. ¡Probablemente una de las mejores opciones en Lajares!",
  "en": "A fabulous stay at Mali House. Probably one of the best options in Lajares!"},
 {"house": "mali", "name": "Monique", "src": "Airbnb",
  "es": "Fue una estancia maravillosa en Lajares. Para nosotros la ubicación era perfecta: una playa con olas y otra sin olas, ambas cerca.",
  "en": "A wonderful stay in Lajares. For us the location was perfect: one beach with waves and one without, both close by."},
 {"house": "mali", "name": "Dominik", "src": "Airbnb",
  "es": "Pasamos una semana en la casa Mali y fue increíble. Hay todo lo necesario para pasar las vacaciones.",
  "en": "We spent a week at Mali House and it was amazing. It has everything you need for a holiday."},
 {"house": "mali", "name": "Michael", "src": "Airbnb",
  "es": "Alojamiento bonito y espacioso, a pocos minutos a pie de una gran variedad de buenos restaurantes.",
  "en": "A lovely, spacious place, a few minutes' walk from a great choice of good restaurants."},
 {"house": "dudi", "name": "Janna", "src": "Airbnb", "home": True,
  "es": "Nos lo pasamos muy bien en casa de Borja. Estuvimos allí con 4 adultos y un niño pequeño. Tienes mucho espacio, el lugar es acogedor y muy adecuado para niños.",
  "en": "We had a great time at Borja's house. We were 4 adults and a toddler: there's lots of space, it's cosy and very well suited to children."},
 {"house": "dudi", "name": "Samantha", "src": "Airbnb", "home": True,
  "es": "Tuvimos una estancia muy agradable en la Casa Dudi. La comunicación con el anfitrión funcionó a la perfección. La casa está limpia, bien cuidada y ofrece mucho espacio. La zona exterior invita a relajarte, con la piscina privada como lo más destacado. ¡Muy recomendable!",
  "en": "We had a really lovely stay at Dudi House. Communication with the host was perfect. The house is clean, well looked after and very spacious, and the outdoor area invites you to relax, with the private pool as the highlight. Highly recommended!"},
 {"house": "dudi", "name": "Adam", "src": "Airbnb", "home": True,
  "es": "Una villa realmente encantadora, limpia y bien equipada. Los propietarios fueron muy receptivos y la ubicación era perfecta, con muchos lugares fantásticos para comer.",
  "en": "A truly charming villa, clean and well equipped. The owners were very responsive and the location was perfect, with lots of great places to eat."},
 {"house": "dudi", "name": "Anina", "src": "Airbnb",
  "es": "Pasamos unos días muy agradables en la villa de Borja. ¡La ubicación es genial! Muy céntrica, pero privada y tranquila. Borja siempre nos atendió muy bien.",
  "en": "We spent some lovely days at Borja's villa. The location is great! Very central, yet private and quiet. Borja always looked after us very well."},
 {"house": "dudi", "name": "Louise", "src": "Airbnb",
  "es": "Disfrutamos de una estancia fabulosa en Dudi House. La ubicación es perfecta, muy tranquila y segura.",
  "en": "We had a fabulous stay at Dudi House. The location is perfect, very quiet and safe."},
 {"house": "dudi", "name": "Diogo", "src": "Airbnb",
  "es": "Borja fue un anfitrión fantástico durante toda nuestra estancia en Lajares. La comunicación siempre fue fácil, rápida y clara.",
  "en": "Borja was a fantastic host throughout our stay in Lajares. Communication was always easy, quick and clear."},
 {"house": "dudi", "name": "Fabio", "src": "Airbnb",
  "es": "La casa estaba muy limpia y disfrutamos mucho de la terraza protegida del viento y de la piscina. Todo lo que necesitas (cafeterías, restaurantes, bares, supermercado, farmacia) está a poca distancia a pie. ¡Gracias por todo!",
  "en": "The house was very clean and we really enjoyed the wind-sheltered terrace and the pool. Everything you need (cafés, restaurants, bars, supermarket, pharmacy) is a short walk away. Thanks for everything!"},
 {"house": "dudi", "name": "Francesca", "src": "Airbnb",
  "es": "¡Vacaciones perfectas en casa de Borja! La casa está en Lajares, que para nosotros era muy conveniente para explorar la isla. Sin duda regresaremos.",
  "en": "A perfect holiday at Borja's house! It's in Lajares, which was very convenient for exploring the island. We'll definitely be back."},
 {"house": "dudi", "name": "Judith D.", "src": "Google",
  "en": "The house is modern, very tastefully furnished, and boasts a fantastic layout.",
  "es": "La casa es moderna, está decorada con muchísimo gusto y tiene una distribución fantástica."},
 {"house": "dudi", "name": "Ati F.", "src": "Google",
  "en": "A beautiful, bright house! Borja gave us a warm welcome and was always available to answer any questions.",
  "es": "¡Una casa preciosa y luminosa! Borja nos dio una cálida bienvenida y siempre estuvo disponible para cualquier duda."},
]

# Nota de Airbnb de cada casa (deja None si no hay)
RATINGS = {
 "mali": {"score": 4.93, "count": 86, "fav": True,
          "cats": [("Cleanliness", "Limpieza", 4.9), ("Accuracy", "Veracidad", 4.9), ("Check-in", "Llegada", 4.9),
                   ("Communication", "Comunicación", 5.0), ("Location", "Ubicación", 5.0), ("Value", "Calidad", 4.8)]},
 "dudi": {"score": 4.95, "count": 75, "fav": True,
          "cats": [("Cleanliness", "Limpieza", 4.8), ("Accuracy", "Veracidad", 4.9), ("Check-in", "Llegada", 5.0),
                   ("Communication", "Comunicación", 5.0), ("Location", "Ubicación", 5.0), ("Value", "Calidad", 4.8)]},
}

# Anfitrion
HOST = {"name": "Borja", "years": 8,
        "en": "Superhost on Airbnb with 8 years of experience. Guests highlight his local tips and his quick, friendly replies throughout their stay.",
        "es": "Superanfitrión en Airbnb con 8 años de experiencia. Los huéspedes destacan sus recomendaciones locales y lo rápido y amable que responde durante toda la estancia."}

# ------------------------------------------------------------ textos nuevos ES
ES_EXTRA = {
 'search.add': 'Añadir fecha', 'search.cta': 'Buscar', 'search.clear': 'Borrar fechas', 'search.done': 'Listo',
 'why.kicker': 'Por qué reservar directo', 'why.title': 'Mejor para ti, <em>mejor para nosotros</em>',
 'why.t1': 'Sin comisiones', 'why.p1': 'Reservando aquí te ahorras las comisiones de servicio que las plataformas añaden al precio.',
 'why.t2': 'Habla con los dueños', 'why.p2': 'Dudas, peticiones especiales o vuelos que llegan tarde: hablas directamente con nosotros, no con un call center.',
 'why.t3': 'Disponibilidad real', 'why.p3': 'Nuestro calendario se sincroniza con cada reserva, así que las fechas libres que ves están libres de verdad.',
 'why.t4': 'Consejos locales', 'why.p4': 'La mejor playa según el viento del día, dónde comer, qué escuela de surf: vivimos la isla.',
 'rev.kicker': 'Lo que cuentan', 'rev.title': 'Lo que dicen nuestros <em>huéspedes</em>',
 'place.guide': 'Lee nuestra guía de Lajares',
 'foot.tag': 'Villas con piscina climatizada en Lajares, norte de Fuerteventura. Reserva directa con los propietarios.',
 'foot.discover': 'Descubre', 'foot.guide': 'Guía de Lajares', 'foot.reviews': 'Opiniones',
 'sub.overview': 'Resumen', 'sub.amenities': 'Servicios', 'sub.photos': 'Fotos', 'sub.availability': 'Disponibilidad',
 'sub.location': 'Ubicación', 'sub.reviews': 'Opiniones', 'sub.info': 'Información',
 'card.cta': 'Ver disponibilidad', 'card.small': 'Sin pago ahora · respuesta en 24 h', 'card.from': 'desde', 'card.night': '/ noche',
 'amen.title': 'Todo para unos <em>días fáciles</em>', 'loc.title': 'En el corazón de <em>Lajares</em>',
 'info.title': 'Antes de <em>llegar</em>', 'map.load': 'Ver mapa', 'map.open': 'Abrir en Google Maps',
 'map.note': 'El mapa se carga desde Google al pulsar.',
}

INFO = {
 "en": [("key", "Check-in & check-out", "Check-in from 16:00 and check-out by 10:00. Times are flexible: tell Borja your flight times and he will do his best to make it easy."),
        ("card", "Booking & payment", "Send a request with your dates: we reply within 24 hours with the total price and how to confirm. Nothing is charged until you agree."),
        ("car", "Getting around", "Restaurants, cafés and shops are walkable. For beaches and the rest of the island, a hire car is the easiest option."),
        ("heart", "Pets & special requests", "Travelling with a pet, a baby or a special occasion? Tell us in your request and we'll do our best.")],
 "es": [("key", "Entrada y salida", "Entrada a partir de las 16:00 y salida antes de las 10:00. Los horarios son flexibles: cuéntale a Borja tus vuelos y hará lo posible por ponértelo fácil."),
        ("card", "Reserva y pago", "Envía una solicitud con tus fechas: te respondemos en 24 horas con el precio total y cómo confirmar. No se cobra nada hasta que estés de acuerdo."),
        ("car", "Moverse", "Restaurantes, cafés y tiendas están a pie. Para las playas y el resto de la isla, lo más cómodo es alquilar un coche."),
        ("heart", "Mascotas y peticiones", "¿Viajas con mascota, con un bebé o celebras algo? Cuéntanoslo en la solicitud y haremos lo posible.")],
}

LOC = {
 "mali": {"en": "Mali House sits on Calle la Costilla, a quiet residential street of Lajares, a short walk from the village centre.",
          "es": "Mali House está en la calle la Costilla, una calle residencial tranquila de Lajares, a un paseo del centro del pueblo."},
 "dudi": {"en": "Dudi House is on Calle la Costilla in Lajares, a peaceful residential area a short walk from the village centre.",
          "es": "Dudi House está en la calle la Costilla de Lajares, una zona residencial tranquila a un paseo del centro del pueblo."},
}

# ------------------------------------------------------------ guia de Lajares
GUIDE = {
 "en": {
  "title": "Lajares guide · Things to do in Lajares and north Fuerteventura",
  "desc": "Our local guide to Lajares, Fuerteventura: Calderón Hondo volcano, El Cotillo beaches, surf, the Saturday market, Corralejo dunes and Lobos island.",
  "crumb": "Lajares guide", "big": "Lajares guide", "h1": "Things to do in Lajares and the north of Fuerteventura",
  "intro": "Lajares is a small village between volcanoes and the Atlantic, loved by surfers, artists and families. These are the places we always recommend to our guests.",
  "items": [
   ("volcano", "Calderón Hondo volcano", "One of the island's best short hikes starts right by the village. Follow the trail through the lava fields up to the rim of the crater and look straight down into it. Watch out for the friendly Barbary ground squirrels.", "Go early or at sunset, and take water and a windbreaker."),
   ("fish", "El Cotillo", "An old fishing village 10 minutes away with two faces: to the north, the calm turquoise lagoons, perfect for children and snorkelling; to the south, long wild beaches under the cliffs. Fresh fish restaurants by the harbour.", "The lagoons are best at low tide."),
   ("surf", "Surf in the north", "The north shore is one of Europe's surf hotspots. Experienced surfers head to the reef breaks along the coastal track towards Majanicho; beginners learn on the beaches of El Cotillo and Corralejo with local surf schools.", "Ask us which spot works with the day's wind and swell."),
   ("market", "Lajares Saturday market", "Every Saturday morning the village fills with craft stalls, local cheese, music and street food. A relaxed way to start the weekend and take a piece of the island home.", "Try queso majorero, the island's famous goat cheese."),
   ("dune", "Corralejo dunes", "About 15 minutes away, the Corralejo Natural Park is a sea of white sand dunes meeting turquoise water. Long beaches for walking, swimming and kitesurfing.", "Bring shade: there are few trees in the dunes."),
   ("boat", "Lobos island", "A short ferry ride from Corralejo takes you to Lobos, a tiny protected island with a lagoon-like beach and a walking trail around its volcano.", "Visits need a free permit booked online in advance."),
  ],
  "get_k": "Getting here", "get_t": "Easy to <em>reach</em>",
  "get": [("plane", "By plane", "Fuerteventura airport (FUE) is about 40 minutes away by car."),
          ("boat", "From Lanzarote", "Ferries connect Playa Blanca with Corralejo, 15 minutes from Lajares."),
          ("car", "Car hire", "Recommended to explore the island.")],
  "stay_k": "Where to stay", "stay_t": "Our houses in <em>Lajares</em>",
 },
 "es": {
  "title": "Guía de Lajares · Qué hacer en Lajares y el norte de Fuerteventura",
  "desc": "Nuestra guía local de Lajares, Fuerteventura: volcán Calderón Hondo, playas de El Cotillo, surf, el mercadillo de los sábados, las dunas de Corralejo y la isla de Lobos.",
  "crumb": "Guía de Lajares", "big": "Guía de Lajares", "h1": "Qué hacer en Lajares y el norte de Fuerteventura",
  "intro": "Lajares es un pequeño pueblo entre volcanes y el Atlántico, querido por surfistas, artistas y familias. Estos son los sitios que siempre recomendamos a nuestros huéspedes.",
  "items": [
   ("volcano", "Volcán Calderón Hondo", "Una de las mejores rutas cortas de la isla empieza junto al pueblo. Sigue el sendero entre los campos de lava hasta el borde del cráter y asómate a su interior. Atento a las simpáticas ardillas morunas.", "Ve temprano o al atardecer, con agua y cortavientos."),
   ("fish", "El Cotillo", "Un antiguo pueblo pesquero a 10 minutos con dos caras: al norte, las lagunas tranquilas y turquesas, perfectas para niños y snorkel; al sur, largas playas salvajes bajo los acantilados. Restaurantes de pescado fresco junto al puerto.", "Las lagunas están mejor con la marea baja."),
   ("surf", "Surf en el norte", "La costa norte es uno de los destinos de surf más importantes de Europa. Los surfistas con experiencia van a los picos de arrecife de la pista hacia Majanicho; quien empieza aprende en las playas de El Cotillo y Corralejo con escuelas locales.", "Pregúntanos qué pico funciona con el viento y el mar del día."),
   ("market", "Mercadillo de Lajares", "Cada sábado por la mañana el pueblo se llena de puestos de artesanía, queso local, música y comida. Una forma tranquila de empezar el fin de semana y llevarte un trocito de la isla.", "Prueba el queso majorero, el famoso queso de cabra de la isla."),
   ("dune", "Dunas de Corralejo", "A unos 15 minutos, el Parque Natural de Corralejo es un mar de dunas blancas que llega hasta el agua turquesa. Playas largas para pasear, bañarse y hacer kitesurf.", "Lleva sombra: en las dunas casi no hay árboles."),
   ("boat", "Isla de Lobos", "Un trayecto corto en barco desde Corralejo te lleva a Lobos, una pequeña isla protegida con una playa tipo laguna y un sendero alrededor de su volcán.", "Para visitarla hace falta un permiso gratuito que se pide por internet con antelación."),
  ],
  "get_k": "Cómo llegar", "get_t": "Fácil de <em>llegar</em>",
  "get": [("plane", "En avión", "El aeropuerto de Fuerteventura (FUE) está a unos 40 minutos en coche."),
          ("boat", "Desde Lanzarote", "Los ferris unen Playa Blanca con Corralejo, a 15 minutos de Lajares."),
          ("car", "Alquiler de coche", "Recomendado para recorrer la isla.")],
  "stay_k": "Dónde alojarse", "stay_t": "Nuestras casas en <em>Lajares</em>",
 },
}
