/* Shop page · Lajares Tee Club
   moving LAJARES rows, shuffling deck, scroll-skew marquee, cursor-reveal cards,
   colour filter (FLIP), pinned horizontal lookbook, draggable stickers, product sheet */
(() => {
  const es = document.documentElement.lang === 'es';
  const root = es ? '../' : '';
  const EMAIL = 'lajaresvillarental@gmail.com';
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const fine = matchMedia('(hover: hover) and (pointer: fine)').matches;
  const mobile = () => innerWidth <= 860;
  const $ = (id) => document.getElementById(id);

  const T = es ? {
    all: 'Todas', back: 'Espalda', front: 'Delante', price: 'Precio a consultar', design: 'Diseño',
    colour: 'Color', frontRow: 'Delante', frontVal: 'Mali House y Dudi House, en pequeño', priceRow: 'Precio', onReq: 'A consultar',
    marq: ['No se viene, se vuelve', 'Drop 01', 'Hecho en Lajares', 'North shore', 'Muy pronto'],
    body: (n, name) => `¡Hola! Me interesa la camiseta ${n} (${name}). Mi talla es: `
  } : {
    all: 'All', back: 'Back', front: 'Front', price: 'Price on request', design: 'Design',
    colour: 'Colour', frontRow: 'Front', frontVal: 'Small Mali House & Dudi House print', priceRow: 'Price', onReq: 'On request',
    marq: ['No se viene, se vuelve', 'Drop 01', 'Made in Lajares', 'North shore', 'Coming soon'],
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
  const grid = $('teeGrid');
  if (!grid) return;

  /* ---------- scroll velocity (shared by rows + marquee) ---------- */
  let vel = 0, lastY = scrollY;
  const rows = $('rows'), marq = $('marq');
  const word = '<span>Lajares</span>'.repeat(8);
  rows.innerHTML = [1, -1, 1, -1, 1].map((d) => `<div class="sx-row" data-d="${d}">${word}${word}</div>`).join('');
  const mset = T.marq.map((t, i) => `<span>${i % 2 ? `<b>${t}</b>` : t}<i>✦</i></span>`).join('');
  marq.innerHTML = mset + mset + mset + mset;
  const movers = [...rows.children].map((el, i) => ({ el, d: +el.dataset.d, x: -i * 140, speed: 0.35 + (i % 3) * 0.12 }));
  const mq = { el: marq, x: 0 };
  const loop = () => {
    const y = scrollY; const dy = y - lastY; lastY = y;
    vel += (dy - vel) * 0.12;
    const boost = Math.min(Math.abs(vel) * 0.25, 14);
    movers.forEach((m) => {
      const half = m.el.scrollWidth / 2;
      m.x += m.d * (m.speed + boost);
      if (m.x <= -half) m.x += half; if (m.x > 0) m.x -= half;
      m.el.style.transform = `translate3d(${m.x}px,0,0)`;
    });
    const mhalf = marq.scrollWidth / 4;
    mq.x -= 1.1 + boost * (vel < 0 ? -1 : 1);
    if (mq.x <= -mhalf) mq.x += mhalf; if (mq.x > 0) mq.x -= mhalf;
    const skew = Math.max(-12, Math.min(12, -vel * 0.5));
    marq.style.transform = `translate3d(${mq.x}px,0,0) skewX(${skew}deg)`;
    requestAnimationFrame(loop);
  };
  if (!reduce) requestAnimationFrame(loop);

  /* ---------- shuffling deck ---------- */
  const deck = $('deck'), stage = $('stage');
  const DECK = ['10', '01', '06', '05', '04'];
  deck.innerHTML = DECK.map((n) => `<div class="sx-card"><img src="${img(n, 'back')}" alt=""></div>`).join('');
  let order = [...deck.children];
  const ROT = [-4, 3, -2, 5, -6];
  const place = () => order.forEach((c, i) => {
    c.style.zIndex = 10 - i;
    c.style.transform = `translate3d(${i * 14}px,${-i * 12}px,${-i * 40}px) rotate(${ROT[i]}deg)`;
    c.style.filter = `brightness(${1 - i * 0.07})`;
  });
  place();
  let busy = false;
  const shuffle = () => {
    if (busy) return; busy = true;
    const top = order[0];
    top.classList.add('is-fly');
    top.style.transform = `translate3d(118%,-10%,80px) rotate(24deg)`;
    setTimeout(() => {
      top.classList.remove('is-fly');
      order = [...order.slice(1), top];
      top.style.zIndex = 0; place();
      setTimeout(() => { busy = false; }, 500);
    }, 560);
  };
  if (!reduce) {
    let auto = setInterval(shuffle, 2800);
    stage.addEventListener('click', () => { shuffle(); clearInterval(auto); auto = setInterval(shuffle, 2800); });
    stage.style.cursor = 'pointer';
    if (fine) {
      const hero = $('sxHero');
      hero.addEventListener('mousemove', (e) => {
        const x = e.clientX / innerWidth - 0.5, y = e.clientY / innerHeight - 0.5;
        deck.style.transform = `rotateY(${x * 16}deg) rotateX(${-y * 12}deg)`;
      });
      hero.addEventListener('mouseleave', () => { deck.style.transform = ''; });
    }
  }

  /* ---------- collection grid ---------- */
  grid.innerHTML = TEES.map(([n, name, c]) => `
    <article class="tee rv" data-c="${c}" data-n="${n}" data-cursor="view" tabindex="0" role="button" aria-label="${name}">
      <div class="tee__card">
        <img class="b" src="${img(n, 'back')}" alt="${name}, ${T.back.toLowerCase()}" loading="lazy" width="800" height="800">
        <img class="f" src="${img(n, 'front')}" alt="${name}, ${T.front.toLowerCase()}" loading="lazy" width="800" height="800">
        <span class="tee__num">${n}</span><span class="tee__flip" data-back="${T.back}" data-front="${T.front}"></span>
      </div>
      <div class="tee__meta"><h3 class="tee__name">${name}</h3><span class="tee__col"><i class="dot" style="background:${COLORS[c][1]}"></i>${COLORS[c][0]}</span></div>
      <p class="tee__ask">${T.price}</p>
    </article>`).join('');
  // the front is revealed in a circle that grows from where the cursor enters
  grid.querySelectorAll('.tee').forEach((t) => {
    const f = t.querySelector('.f'), card = t.querySelector('.tee__card');
    const setXY = (e) => {
      const r = card.getBoundingClientRect();
      f.style.setProperty('--x', `${((e.clientX - r.left) / r.width) * 100}%`);
      f.style.setProperty('--y', `${((e.clientY - r.top) / r.height) * 100}%`);
    };
    t.addEventListener('mouseenter', setXY);
    t.addEventListener('mouseleave', setXY);
  });

  /* colour filter with FLIP animation */
  const chips = $('chips');
  chips.innerHTML = `<button type="button" class="chip is-on" data-c="all">${T.all}</button>` +
    Object.entries(COLORS).map(([k, [l, h]]) => `<button type="button" class="chip" data-c="${k}"><i class="dot" style="background:${h}"></i>${l}</button>`).join('');
  chips.addEventListener('click', (e) => {
    const b = e.target.closest('.chip'); if (!b) return;
    chips.querySelectorAll('.chip').forEach((x) => x.classList.toggle('is-on', x === b));
    const items = [...grid.children];
    const first = new Map(items.map((el) => [el, el.getBoundingClientRect()]));
    items.forEach((el) => { el.classList.toggle('is-out', b.dataset.c !== 'all' && el.dataset.c !== b.dataset.c); el.classList.add('in'); });
    if (reduce) return;
    items.forEach((el, i) => {
      if (el.classList.contains('is-out')) return;
      const f = first.get(el), l = el.getBoundingClientRect();
      if (!f.width) el.animate([{ opacity: 0, transform: 'translateY(30px) scale(.94)' }, { opacity: 1, transform: 'none' }], { duration: 600, delay: i * 30, easing: 'cubic-bezier(.2,.7,.1,1)', fill: 'backwards' });
      else el.animate([{ transform: `translate(${f.left - l.left}px,${f.top - l.top}px)` }, { transform: 'none' }], { duration: 700, easing: 'cubic-bezier(.2,.7,.1,1)' });
    });
  });

  /* ---------- lookbook: pinned horizontal scroll ---------- */
  const look = $('look'), track = $('lookTrack'), bar = $('lookBar'), count = $('lookCount');
  track.innerHTML = TEES.map(([n, name, c], i) => `
    <figure class="lk" data-n="${n}" data-cursor="view" style="--r:${[-2.5, 2, -1.5, 3, -3, 1.5, -2, 2.5, -1, 3][i]}deg">
      <span class="lk__num">${n}</span>
      <div class="lk__img"><img src="${img(n, 'back')}" alt="${name}" loading="lazy" width="800" height="800"></div>
      <figcaption class="lk__cap"><b>${name}</b><span>${COLORS[c][0]}</span></figcaption>
    </figure>`).join('');
  const cards = [...track.children];
  const sizeLook = () => {
    look.style.height = mobile() ? '' : `${track.scrollWidth - innerWidth + innerHeight}px`;
    onLook();
  };
  const onLook = () => {
    if (mobile()) { track.style.transform = ''; return; }
    const r = look.getBoundingClientRect();
    const span = look.offsetHeight - innerHeight;
    const p = Math.max(0, Math.min(1, -r.top / (span || 1)));
    const dist = track.scrollWidth - innerWidth;
    track.style.transform = `translate3d(${-p * dist}px,0,0)`;
    bar.style.transform = `scaleX(${p})`;
    count.textContent = `${String(Math.round(p * (TEES.length - 1)) + 1).padStart(2, '0')} / ${TEES.length}`;
    if (!reduce) cards.forEach((c) => {
      const b = c.getBoundingClientRect();
      const off = (b.left + b.width / 2 - innerWidth / 2) / innerWidth;
      c.querySelector('img').style.setProperty('--px', `${off * -40}px`);
    });
  };
  addEventListener('scroll', onLook, { passive: true });
  addEventListener('resize', sizeLook);
  addEventListener('load', sizeLook);
  sizeLook();
  track.addEventListener('scroll', () => {
    if (!mobile()) return;
    const p = track.scrollLeft / (track.scrollWidth - track.clientWidth || 1);
    bar.style.transform = `scaleX(${p})`;
    count.textContent = `${String(Math.round(p * (TEES.length - 1)) + 1).padStart(2, '0')} / ${TEES.length}`;
  }, { passive: true });

  /* ---------- stickers you can drag around ---------- */
  const ST = [ // name, left%, top%, width, rotation, mobile left%, mobile top% (null = hidden on phones)
    ['cabra', 5, 10, 175, -12, 3, 3], ['fuerte', 79, 7, 165, 9, 66, 5], ['lajares_x5', 9, 60, 150, 7, 5, 82],
    ['magazine', 83, 56, 150, -8, 72, 84], ['lighthouse', 27, 79, 180, -4, null, null], ['polaroid', 63, 78, 140, 11, null, null],
    ['logo', 3, 42, 110, 0, 41, 90]
  ];
  const sWrap = $('stickers');
  let zTop = 10;
  const drawStickers = () => {
    sWrap.innerHTML = '';
    ST.forEach(([name, l, t, w, r, ml, mt], i) => {
      if (mobile() && ml === null) return;
      const s = document.createElement('img');
      s.className = 'stk'; s.alt = ''; s.draggable = false;
      s.src = `${root}img/shop/stickers/${name}.webp`;
      s.style.left = `${mobile() ? ml : l}%`; s.style.top = `${mobile() ? mt : t}%`;
      s.style.setProperty('--w', `${w}px`); s.style.setProperty('--r', `${r}deg`); s.style.setProperty('--d', `${i * 0.12}s`);
      sWrap.appendChild(s);
    });
  };
  drawStickers();
  let lastMobile = mobile();
  addEventListener('resize', () => { if (mobile() !== lastMobile) { lastMobile = mobile(); drawStickers(); slap(); } });
  const slap = () => sWrap.querySelectorAll('.stk').forEach((s) => s.classList.add('is-in'));
  new IntersectionObserver((es2, o) => es2.forEach((e) => { if (e.isIntersecting) { slap(); o.disconnect(); } }), { threshold: 0.3 }).observe($('ask'));
  let drag = null;
  sWrap.addEventListener('pointerdown', (e) => {
    const s = e.target.closest('.stk'); if (!s) return;
    e.preventDefault(); s.setPointerCapture(e.pointerId);
    const dx = parseFloat(s.style.getPropertyValue('--dx')) || 0, dy = parseFloat(s.style.getPropertyValue('--dy')) || 0;
    drag = { s, x: e.clientX - dx, y: e.clientY - dy };
    s.classList.add('is-drag', 'was-dragged'); s.style.zIndex = ++zTop;
  });
  sWrap.addEventListener('pointermove', (e) => {
    if (!drag) return;
    drag.s.style.setProperty('--dx', `${e.clientX - drag.x}px`);
    drag.s.style.setProperty('--dy', `${e.clientY - drag.y}px`);
    drag.s.style.setProperty('--r', `${Math.max(-25, Math.min(25, e.movementX * 1.5))}deg`);
  });
  const drop = () => { if (!drag) return; drag.s.classList.remove('is-drag'); drag = null; };
  sWrap.addEventListener('pointerup', drop); sWrap.addEventListener('pointercancel', drop);

  /* ---------- product sheet ---------- */
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
  const pick = (e) => { const t = e.target.closest('[data-n]'); if (t) open(t.dataset.n); };
  grid.addEventListener('click', pick);
  track.addEventListener('click', pick);
  grid.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' || e.key === ' ') { const t = e.target.closest('.tee'); if (t) { e.preventDefault(); open(t.dataset.n); } }
  });
  modal.addEventListener('click', (e) => {
    if (e.target === modal || e.target.closest('.tmodal__close')) close();
    const b = e.target.closest('.tmodal__sides button'); if (b) side(b.dataset.side);
  });
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && modal.classList.contains('open')) close(); });
})();
