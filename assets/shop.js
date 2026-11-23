/* Shop page: collection grid, colour filter, card tilt, product sheet */
(() => {
  const es = document.documentElement.lang === 'es';
  const root = es ? '../' : '';
  const EMAIL = 'lajaresvillarental@gmail.com';
  const T = es ? {
    all: 'Todas', back: 'Espalda', front: 'Delante', price: 'Precio a consultar', design: 'Diseño',
    colour: 'Color', frontRow: 'Delante', frontVal: 'Logo pequeño de Lajares Houses', priceRow: 'Precio', onReq: 'A consultar',
    body: (n, name) => `¡Hola! Me interesa la camiseta ${n} (${name}). Mi talla es: `
  } : {
    all: 'All', back: 'Back', front: 'Front', price: 'Price on request', design: 'Design',
    colour: 'Colour', frontRow: 'Front', frontVal: 'Small Lajares Houses logo', priceRow: 'Price', onReq: 'On request',
    body: (n, name) => `Hi! I'd like the tee ${n} (${name}). My size is: `
  };
  const COLORS = {
    black: [es ? 'Negro' : 'Black', '#1a1918'], navy: [es ? 'Azul marino' : 'Navy', '#1e2c4a'],
    white: [es ? 'Blanco' : 'White', '#ffffff'], cream: [es ? 'Crudo' : 'Cream', '#f4ecd9']
  };
  const TEES = [
    ['01', 'Lajares ×5 · Volcano', 'black', 'Five rows of LAJARES filled with a session at the volcano.', 'Cinco filas de LAJARES rellenas con una sesión en el volcán.'],
    ['02', 'Lajares ×5 · Outline', 'navy', 'Photo rows and outline letters, one after the other.', 'Filas de foto y letras con borde, una tras otra.'],
    ['03', 'Lajares ×5 · Sunset', 'white', 'The north shore sunset on all five rows.', 'El atardecer del norte en las cinco filas.'],
    ['04', 'Lajares Magazine', 'white', 'A surf magazine cover made in Lajares, barcode included.', 'Una portada de revista de surf hecha en Lajares, con código de barras y todo.'],
    ['05', 'The Lighthouse Peak', 'black', 'A panoramic strip of the wave by El Tostón lighthouse.', 'Una banda panorámica de la ola junto al faro de El Tostón.'],
    ['06', 'Fuerte / Ventura', 'cream', 'Big letters and a band of photo running through VENTURA.', 'Letras grandes y una banda de foto que atraviesa VENTURA.'],
    ['07', 'North Shore Polaroid', 'white', 'One instant photo of the north shore.', 'Una foto instantánea del norte de la isla.'],
    ['08', 'Lajares ×5', 'black', 'Type only. The classic.', 'Solo letras. La clásica.'],
    ['09', 'Lajares ×5 · Photo Row', 'black', 'The middle row is a window onto the waves.', 'La fila del centro es una ventana a las olas.'],
    ['10', 'Majorero', 'black', 'The island goat and two crossed boards.', 'La cabra de la isla y dos tablas cruzadas.']
  ];
  const img = (n, s) => `${root}img/shop/tee-${n}-${s}.jpg`;
  const $ = (id) => document.getElementById(id);

  const grid = $('teeGrid');
  if (!grid) return;
  grid.innerHTML = TEES.map(([n, name, c]) => `
    <article class="tee rv" data-c="${c}" data-n="${n}" tabindex="0" role="button" aria-label="${name}">
      <div class="tee__card">
        <img class="b" src="${img(n, 'back')}" alt="${name}, ${T.back.toLowerCase()}" loading="lazy" width="800" height="800">
        <img class="f" src="${img(n, 'front')}" alt="${name}, ${T.front.toLowerCase()}" loading="lazy" width="800" height="800">
        <span class="tee__num">${n}</span><span class="tee__flip" data-back="${T.back}" data-front="${T.front}"></span>
      </div>
      <div class="tee__meta"><h3 class="tee__name">${name}</h3><span class="tee__col"><i class="dot" style="background:${COLORS[c][1]}"></i>${COLORS[c][0]}</span></div>
      <p class="tee__ask">${T.price}</p>
    </article>`).join('');

  // colour filter
  const chips = $('chips');
  chips.innerHTML = `<button type="button" class="chip is-on" data-c="all">${T.all}</button>` +
    Object.entries(COLORS).map(([k, [l, h]]) => `<button type="button" class="chip" data-c="${k}"><i class="dot" style="background:${h}"></i>${l}</button>`).join('');
  chips.addEventListener('click', (e) => {
    const b = e.target.closest('.chip'); if (!b) return;
    chips.querySelectorAll('.chip').forEach((x) => x.classList.toggle('is-on', x === b));
    grid.querySelectorAll('.tee').forEach((t) => t.classList.toggle('is-out', b.dataset.c !== 'all' && t.dataset.c !== b.dataset.c));
  });

  // gentle 3D tilt (mouse only)
  if (matchMedia('(hover:hover)').matches && !matchMedia('(prefers-reduced-motion:reduce)').matches) {
    grid.querySelectorAll('.tee').forEach((t) => {
      const card = t.querySelector('.tee__card');
      t.addEventListener('mousemove', (e) => {
        const r = card.getBoundingClientRect(), x = (e.clientX - r.left) / r.width - .5, y = (e.clientY - r.top) / r.height - .5;
        card.style.transform = `rotateY(${x * 10}deg) rotateX(${-y * 10}deg) translateY(-6px)`;
      });
      t.addEventListener('mouseleave', () => { card.style.transform = ''; });
    });
  }

  // moving strip
  const set = TEES.map(([n]) => `<img src="${img(n, 'back')}" alt="" loading="lazy" width="170" height="170">`).join('');
  $('strip').innerHTML = set + set;

  // hero: rotating tees
  const hero = $('heroTee');
  hero.innerHTML = ['10', '01', '06', '05', '04'].map((n, i) => `<img src="${img(n, 'back')}" alt="" class="${i ? '' : 'on'}">`).join('');
  const hs = hero.querySelectorAll('img'); let hi = 0;
  setInterval(() => { hs[hi].classList.remove('on'); hi = (hi + 1) % hs.length; hs[hi].classList.add('on'); }, 3200);

  // product sheet
  const modal = $('tmodal');
  $('mColL').textContent = T.colour; $('mFrontL').textContent = T.frontRow; $('mFrontV').textContent = T.frontVal;
  $('mPriceL').textContent = T.priceRow; $('mPriceV').textContent = T.onReq;
  const sides = modal.querySelectorAll('.tmodal__sides button');
  sides[0].textContent = T.back; sides[1].textContent = T.front;
  const side = (s) => {
    $('mFront').style.opacity = s === 'front' ? 1 : 0; $('mBack').style.opacity = s === 'front' ? 0 : 1;
    sides.forEach((b) => b.classList.toggle('is-on', b.dataset.side === s));
  };
  let last = null;
  const open = (n) => {
    const [num, name, c, en, esd] = TEES.find((t) => t[0] === n);
    $('mBack').src = img(num, 'back'); $('mFront').src = img(num, 'front');
    $('mBack').alt = `${name}, ${T.back.toLowerCase()}`; $('mFront').alt = `${name}, ${T.front.toLowerCase()}`;
    $('mNum').textContent = `${T.design} ${num}`; $('mName').textContent = name;
    $('mDesc').textContent = es ? esd : en; $('mCol').textContent = COLORS[c][0];
    $('mMail').href = `mailto:${EMAIL}?subject=${encodeURIComponent('Lajares Tee Club · ' + num + ' ' + name)}&body=${encodeURIComponent(T.body(num, name))}`;
    side('back'); last = document.activeElement;
    modal.classList.add('open'); modal.setAttribute('aria-hidden', 'false');
    modal.querySelector('.tmodal__close').focus();
  };
  const close = () => {
    modal.classList.remove('open'); modal.setAttribute('aria-hidden', 'true');
    if (last) last.focus();
  };
  grid.addEventListener('click', (e) => { const t = e.target.closest('.tee'); if (t) open(t.dataset.n); });
  grid.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' || e.key === ' ') { const t = e.target.closest('.tee'); if (t) { e.preventDefault(); open(t.dataset.n); } }
  });
  modal.addEventListener('click', (e) => {
    if (e.target === modal || e.target.closest('.tmodal__close')) close();
    const b = e.target.closest('.tmodal__sides button'); if (b) side(b.dataset.side);
  });
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && modal.classList.contains('open')) close(); });
})();
