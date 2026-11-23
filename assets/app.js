(() => {
  'use strict';
  const $ = (s, el = document) => el.querySelector(s);
  const $$ = (s, el = document) => [...el.querySelectorAll(s)];
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const lang = document.documentElement.lang === 'es' ? 'es' : 'en';
  const locale = lang === 'es' ? 'es-ES' : 'en-GB';

  const CONTACT_EMAIL = 'lajaresvillarental@gmail.com';
  const INSTAGRAM = 'lajaresrental';
  const HOUSES = {
    mali: { name: 'Mali House', max: 4 },
    dudi: { name: 'Dudi House', max: 6 },
  };

  /* ---------------- strings ---------------- */
  const STR = {
    en: {
      synced: (x) => `Synced with our bookings · ${x}`, studioNote: 'Send us your dates and we will confirm by email.',
      pickIn: 'Choose your arrival day.', pickOut: 'Now choose your departure day.', blocked: 'Those dates overlap a booking. Try other days.',
      needDates: 'Please choose your dates in the calendar first.', needName: 'Please add your name and a valid email.',
      mailOpened: 'Your email app is opening with the request ready to send.', copied: 'Message copied. Paste it in our Instagram chat.',
      guests: (n) => `${n} guest${n === 1 ? '' : 's'}`,
      add: 'Add date', free: 'Available for your dates', busy: 'Booked on these dates', ask: 'Ask us for these dates', tooMany: (n) => `Sleeps up to ${n}`,
      searchNeed: 'Choose your check-in and check-out first.',
      subject: (h, a, b) => `Booking request · ${h} · ${a} → ${b}`,
      body: (d) => `Hi! I'd like to book ${d.house}.\n\nCheck-in: ${d.inn}\nCheck-out: ${d.out}\nNights: ${d.nights}\nGuests: ${d.guests}\nName: ${d.name}\nEmail: ${d.email}\n\n${d.msg}`,
    },
    es: {
      synced: (x) => `Sincronizado con nuestras reservas · ${x}`, studioNote: 'Envíanos tus fechas y te confirmamos por email.',
      pickIn: 'Elige tu día de llegada.', pickOut: 'Ahora elige tu día de salida.', blocked: 'Esas fechas coinciden con una reserva. Prueba otros días.',
      needDates: 'Primero elige tus fechas en el calendario.', needName: 'Añade tu nombre y un email válido.',
      mailOpened: 'Se está abriendo tu email con la solicitud lista para enviar.', copied: 'Mensaje copiado. Pégalo en nuestro chat de Instagram.',
      guests: (n) => `${n} huésped${n === 1 ? '' : 'es'}`,
      add: 'Añadir fecha', free: 'Libre en tus fechas', busy: 'Ocupada en esas fechas', ask: 'Consúltanos esas fechas', tooMany: (n) => `Máximo ${n} personas`,
      searchNeed: 'Elige primero la entrada y la salida.',
      subject: (h, a, b) => `Solicitud de reserva · ${h} · ${a} → ${b}`,
      body: (d) => `¡Hola! Me gustaría reservar ${d.house}.\n\nEntrada: ${d.inn}\nSalida: ${d.out}\nNoches: ${d.nights}\nHuéspedes: ${d.guests}\nNombre: ${d.name}\nEmail: ${d.email}\n\n${d.msg}`,
    },
  };
  const t = (k, ...a) => { const v = STR[lang][k]; return typeof v === 'function' ? v(...a) : v; };
  const toast = (msg) => {
    const el = $('#toast'); el.textContent = msg; el.classList.add('is-on');
    clearTimeout(el._t); el._t = setTimeout(() => el.classList.remove('is-on'), 4200);
  };

  /* ---------------- loader ---------------- */
  const start = performance.now();
  let seen = false;
  try { seen = sessionStorage.getItem('lh-seen') === '1'; sessionStorage.setItem('lh-seen', '1'); } catch (e) { /* ignore */ }
  if (seen) document.body.classList.add('quick-load');
  let readyDone = false;
  const ready = () => {
    if (readyDone) return; readyDone = true;
    const wait = seen ? 0 : Math.max(0, 1200 - (performance.now() - start));
    setTimeout(() => {
      document.body.classList.remove('is-loading');
      setTimeout(() => document.body.classList.add('is-ready'), reduce ? 0 : 450);
    }, reduce ? 0 : wait);
  };
  if (document.readyState === 'complete') ready(); else addEventListener('load', ready);
  setTimeout(ready, 3500);

  /* ---------------- nav ---------------- */
  const nav = $('#nav');
  const subnav = $('#subnav');
  let lastY = 0;
  const onScroll = () => {
    const y = scrollY;
    nav.classList.toggle('is-solid', y > innerHeight * 0.6);
    const hide = y > lastY && y > innerHeight && !document.body.classList.contains('menu-open');
    const underSub = !!subnav && subnav.getBoundingClientRect().top < nav.offsetHeight;
    nav.classList.toggle('is-hidden', hide || underSub);
    lastY = y;
  };
  addEventListener('scroll', onScroll, { passive: true });
  onScroll();
  const burger = $('.nav__burger');
  const toggleMenu = (open) => {
    document.body.classList.toggle('menu-open', open);
    burger.setAttribute('aria-expanded', open);
    $('#menu').setAttribute('aria-hidden', !open);
  };
  burger.addEventListener('click', () => toggleMenu(!document.body.classList.contains('menu-open')));
  $$('#menu a').forEach((a) => a.addEventListener('click', () => toggleMenu(false)));

  /* sticky sub-navigation on house pages */
  if (subnav) {
    const links = $$('a[href^="#"]:not(.subnav__cta)', subnav);
    const secs = links.map((a) => $(a.getAttribute('href'))).filter(Boolean);
    const sentinel = document.createElement('div');
    subnav.before(sentinel);
    new IntersectionObserver(([e]) => {
      subnav.classList.toggle('is-stuck', !e.isIntersecting && e.boundingClientRect.top < 0);
      onScroll();
    }).observe(sentinel);
    addEventListener('scroll', () => {
      const y = scrollY + 160;
      let curSec = null;
      secs.forEach((s) => { if (s.offsetTop <= y) curSec = s; });
      links.forEach((a) => a.classList.toggle('is-active', !!curSec && a.getAttribute('href') === '#' + curSec.id));
    }, { passive: true });
  }

  /* ---------------- hero slideshow ---------------- */
  const slides = $$('.hero__slide');
  const dotsWrap = $('.hero__dots') || document.createElement('div');
  let cur = 0, timer;
  slides.forEach((s, i) => {
    const b = document.createElement('button');
    b.setAttribute('aria-label', `Slide ${i + 1}`);
    b.innerHTML = '<i></i>';
    b.addEventListener('click', () => go(i));
    dotsWrap.appendChild(b);
  });
  const dots = $$('button', dotsWrap);
  function load(s) { if (s.dataset.bg) { s.style.backgroundImage = `url(${s.dataset.bg})`; delete s.dataset.bg; } }
  function go(i) {
    slides[cur].classList.remove('is-active'); dots[cur].classList.remove('is-active');
    cur = (i + slides.length) % slides.length;
    load(slides[cur]); load(slides[(cur + 1) % slides.length]);
    slides[cur].classList.add('is-active');
    void dots[cur].offsetWidth; dots[cur].classList.add('is-active');
    clearTimeout(timer); timer = setTimeout(() => go(cur + 1), 6000);
  }
  if (slides.length > 1) {
    dots[0].classList.add('is-active');
    setTimeout(() => load(slides[1]), 1200);
    if (!reduce) timer = setTimeout(() => go(1), 6000);
  }

  /* ---------------- reveal + counters ---------------- */
  const io = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (!e.isIntersecting) return;
      const el = e.target;
      const sib = el.parentElement ? $$(':scope > .rv', el.parentElement).indexOf(el) : 0;
      el.style.transitionDelay = `${Math.min(Math.max(sib, 0), 6) * 0.08}s`;
      el.classList.add('in');
      io.unobserve(el);
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
  /* split headlines into words so they rise one by one */
  if (!reduce) {
    $$('.h2, .statement, .contact__title, .phead__title').forEach((el) => {
      let i = 0;
      const walk = (node) => {
        [...node.childNodes].forEach((n) => {
          if (n.nodeType === 3) {
            const frag = document.createDocumentFragment();
            n.textContent.split(/(\s+)/).forEach((part) => {
              if (!part) return;
              if (/^\s+$/.test(part)) { frag.appendChild(document.createTextNode(part)); return; }
              const w = document.createElement('span'); w.className = 'w';
              const inner = document.createElement('span'); inner.textContent = part; inner.style.setProperty('--i', i++);
              w.appendChild(inner); frag.appendChild(w);
            });
            n.replaceWith(frag);
          } else if (n.nodeType === 1) walk(n);
        });
      };
      walk(el);
      el.classList.add('split');
    });
  }
  $$('.rv, .split, .house__img--main, .collage').forEach((el) => io.observe(el));

  const cio = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (!e.isIntersecting) return;
      const el = e.target, end = +el.dataset.count, dur = 1600, t0 = performance.now();
      const step = (now) => {
        const p = Math.min(1, (now - t0) / dur), v = 1 - Math.pow(1 - p, 3);
        el.textContent = Math.round(end * v);
        if (p < 1) requestAnimationFrame(step);
      };
      reduce ? (el.textContent = end) : requestAnimationFrame(step);
      cio.unobserve(el);
    });
  }, { threshold: 0.6 });
  $$('[data-count]').forEach((el) => cio.observe(el));

  /* ---------------- parallax ---------------- */
  const px = $$('[data-parallax]');
  let ticking = false;
  function parallax() {
    ticking = false;
    const vh = innerHeight;
    px.forEach((el) => {
      const r = el.getBoundingClientRect();
      if (r.bottom < -100 || r.top > vh + 100) return;
      const off = (r.top + r.height / 2 - vh / 2) * parseFloat(el.dataset.parallax);
      const target = el.matches('.place__img') ? $('img', el) : el;
      target.style.transform = `translate3d(0, ${(-off).toFixed(1)}px, 0)`;
    });
  }
  if (!reduce && px.length) {
    addEventListener('scroll', () => { if (!ticking) { ticking = true; requestAnimationFrame(parallax); } }, { passive: true });
    parallax();
  }

  /* ---------------- maps: only load Google when the visitor asks ---------------- */
  $$('.map--lazy').forEach((m) => {
    const btn = $('.map__btn', m);
    if (btn) btn.addEventListener('click', () => {
      const tabs = m.dataset.tabs ? JSON.parse(m.dataset.tabs) : null;
      m.innerHTML = (tabs ? `<div class="map__tabs">${tabs.map((x, i) => `<button type="button" class="${i ? '' : 'is-active'}" data-i="${i}">${x.name}</button>`).join('')}</div>` : '')
        + `<iframe title="Map" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="${m.dataset.src}"></iframe>`;
      m.classList.add('is-loaded');
      if (tabs) $$('.map__tabs button', m).forEach((b) => b.addEventListener('click', () => {
        $$('.map__tabs button', m).forEach((x) => x.classList.toggle('is-active', x === b));
        $('iframe', m).src = tabs[+b.dataset.i].src;
      }));
    });
  });

  /* ---------------- gallery + lightbox ---------------- */
  const grid = $('#grid');
  const root = lang === 'es' ? '../' : '';
  const gio = new IntersectionObserver((entries) => entries.forEach((e) => {
    if (e.isIntersecting) { e.target.classList.add('in'); gio.unobserve(e.target); }
  }), { threshold: 0.1 });
  function wireGrid() {
    $$('figure', grid).forEach((f, i) => {
      f.style.transitionDelay = `${(i % 3) * 0.08}s`;
      f.onclick = () => openLb(i);
      gio.observe(f);
    });
  }
  function renderGallery(key) {
    $$('#galleryTabs button').forEach((b) => b.classList.toggle('is-active', b.dataset.g === key));
    grid.innerHTML = '';
    ((window.PHOTOS || {})[key] || []).forEach((p) => {
      const alt = (lang === 'es' && p.alt_es) || p.alt;
      const f = document.createElement('figure');
      f.dataset.full = root + p.src;
      f.innerHTML = `<img src="${root + p.sm}" alt="${alt}" loading="lazy" ${p.o === 'p' ? 'width="720" height="950"' : 'width="720" height="480"'}><figcaption>${alt}</figcaption>`;
      grid.appendChild(f);
    });
    wireGrid();
  }
  if (grid) {
    $$('#galleryTabs button').forEach((b) => b.addEventListener('click', () => renderGallery(b.dataset.g)));
    if (grid.hasAttribute('data-static')) wireGrid(); else renderGallery('mali');
  }
  const lb = $('#lb'), lbImg = $('img', lb), lbCap = $('figcaption', lb);
  let lbIdx = 0;
  function showLb(i) {
    const list = $$('figure', grid);
    lbIdx = (i + list.length) % list.length;
    const f = list[lbIdx], alt = $('figcaption', f).textContent, src = f.dataset.full;
    lbImg.style.opacity = 0;
    const im = new Image();
    im.onload = () => { lbImg.src = src; lbImg.alt = alt; lbImg.style.opacity = 1; };
    im.src = src;
    lbCap.textContent = `${alt} · ${lbIdx + 1} / ${list.length}`;
  }
  function openLb(i) { showLb(i); lb.classList.add('is-open'); lb.setAttribute('aria-hidden', 'false'); document.body.style.overflow = 'hidden'; }
  function closeLb() { lb.classList.remove('is-open'); lb.setAttribute('aria-hidden', 'true'); if (!document.querySelector('.tour.is-open')) document.body.style.overflow = ''; }
  $('.lb__close').addEventListener('click', closeLb);
  $('.lb__prev').addEventListener('click', () => showLb(lbIdx - 1));
  $('.lb__next').addEventListener('click', () => showLb(lbIdx + 1));
  lb.addEventListener('click', (e) => { if (e.target === lb) closeLb(); });
  addEventListener('keydown', (e) => {
    if (!lb.classList.contains('is-open')) return;
    if (e.key === 'Escape') closeLb();
    if (e.key === 'ArrowLeft') showLb(lbIdx - 1);
    if (e.key === 'ArrowRight') showLb(lbIdx + 1);
  });
  let tx = null;
  lb.addEventListener('touchstart', (e) => { tx = e.touches[0].clientX; }, { passive: true });
  lb.addEventListener('touchend', (e) => {
    if (tx == null) return;
    const dx = e.changedTouches[0].clientX - tx;
    if (Math.abs(dx) > 40) showLb(lbIdx + (dx < 0 ? 1 : -1));
    tx = null;
  });

  /* ---------------- dates & availability ---------------- */
  const AV = window.AVAILABILITY || { houses: {} };
  const iso = (d) => `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`;
  const parse = (s) => { const [y, m, d] = s.split('-').map(Number); return new Date(y, m - 1, d); };
  const addDays = (d, n) => new Date(d.getFullYear(), d.getMonth(), d.getDate() + n);
  const today = new Date(); today.setHours(0, 0, 0, 0);
  const todayIso = iso(today);
  const fmt = (d, o = { day: 'numeric', month: 'short' }) => (typeof d === 'string' ? parse(d) : d).toLocaleDateString(locale, o);
  const nightsBetween = (a, b) => Math.round((parse(b) - parse(a)) / 864e5);
  const hasData = (h) => Array.isArray(AV.houses[h]);
  const busyNight = (h, d) => (AV.houses[h] || []).some(([s, e]) => d >= s && d < e);
  const firstBusyAfter = (h, d) => (AV.houses[h] || []).map(([s]) => s).filter((s) => s > d).sort()[0] || null;
  const rangeFree = (h, a, b) => !(AV.houses[h] || []).some(([s, e]) => s < b && e > a);

  /* the stay being planned, shared between pages during the visit */
  const stay = (() => {
    let v = {};
    try { v = JSON.parse(sessionStorage.getItem('lh-stay') || '{}'); } catch (e) { /* ignore */ }
    if (v.in && v.in < todayIso) v = {};
    return v;
  })();
  const saveStay = () => { try { sessionStorage.setItem('lh-stay', JSON.stringify(stay)); } catch (e) { /* ignore */ } };

  /* Range picker drawing months into a box. house = null shows no bookings. */
  class Picker {
    constructor(box, opts) {
      this.box = box; this.house = opts.house || null; this.months = opts.months || 2;
      this.onChange = opts.onChange || (() => {});
      this.inD = opts.inD || null; this.outD = opts.outD || null; this.hover = null;
      const base = this.inD ? parse(this.inD) : today;
      this.view = new Date(base.getFullYear(), base.getMonth(), 1);
      box.addEventListener('click', (e) => { const b = e.target.closest('.day'); if (b && !b.disabled) this.pick(b.dataset.d); });
      box.addEventListener('mouseover', (e) => {
        const b = e.target.closest('.day');
        if (!b || !this.inD || this.outD || this.hover === b.dataset.d) return;
        this.hover = b.dataset.d; this.paint();
      });
      box.addEventListener('mouseleave', () => { if (this.inD && !this.outD) { this.hover = null; this.paint(); } });
    }
    busy(d) { return this.house ? busyNight(this.house, d) : false; }
    limit() { return this.inD && !this.outD && this.house ? firstBusyAfter(this.house, this.inD) : null; }
    canPrev() { return this.view > new Date(today.getFullYear(), today.getMonth(), 1); }
    step(n) {
      const v = new Date(this.view.getFullYear(), this.view.getMonth() + n, 1);
      if (v < new Date(today.getFullYear(), today.getMonth(), 1) || v > new Date(today.getFullYear(), today.getMonth() + 16, 1)) return;
      this.view = v; this.render(true);
    }
    render(fade) {
      const draw = () => {
        this.box.innerHTML = '';
        for (let m = 0; m < this.months; m++) this.box.appendChild(this.month(new Date(this.view.getFullYear(), this.view.getMonth() + m, 1)));
        this.paint();
        this.box.classList.remove('is-fading');
      };
      if (fade && !reduce) { this.box.classList.add('is-fading'); setTimeout(draw, 180); } else draw();
    }
    month(first) {
      const wrap = document.createElement('div');
      wrap.className = 'month';
      wrap.innerHTML = `<p class="month__name">${fmt(first, { month: 'long', year: 'numeric' })}</p>`;
      const g = document.createElement('div');
      g.className = 'month__grid';
      const mon = new Date(2024, 0, 1);
      for (let i = 0; i < 7; i++) g.insertAdjacentHTML('beforeend', `<span class="month__dow">${fmt(addDays(mon, i), { weekday: 'short' }).slice(0, 2)}</span>`);
      for (let i = 0; i < (first.getDay() + 6) % 7; i++) g.appendChild(document.createElement('span'));
      const days = new Date(first.getFullYear(), first.getMonth() + 1, 0).getDate();
      const limit = this.limit();
      for (let d = 1; d <= days; d++) {
        const k = iso(new Date(first.getFullYear(), first.getMonth(), d));
        const b = document.createElement('button');
        b.type = 'button'; b.className = 'day'; b.textContent = d; b.dataset.d = k;
        const busy = this.busy(k);
        const canBeOut = this.inD && !this.outD && k > this.inD && (!limit || k <= limit);
        if (k < todayIso) { b.classList.add('is-past'); b.disabled = true; }
        else if (busy) { b.classList.add('is-busy'); if (!canBeOut) b.disabled = true; }
        if (k === todayIso) b.classList.add('is-today');
        b.setAttribute('aria-label', fmt(k, { weekday: 'long', day: 'numeric', month: 'long', year: 'numeric' }));
        g.appendChild(b);
      }
      wrap.appendChild(g);
      return wrap;
    }
    paint() {
      const limit = this.limit();
      const endSel = this.outD || (this.inD && this.hover && this.hover > this.inD && (!limit || this.hover <= limit) ? this.hover : null);
      $$('.day', this.box).forEach((b) => {
        const k = b.dataset.d;
        b.classList.toggle('is-start', this.inD === k);
        b.classList.toggle('is-end', endSel === k);
        b.classList.toggle('is-range', !!(this.inD && endSel && k > this.inD && k < endSel));
      });
    }
    pick(k) {
      let why;
      if (!this.inD || this.outD || k <= this.inD) {
        if (this.busy(k)) return;
        this.inD = k; this.outD = null;
      } else {
        const limit = this.limit();
        if (limit && k > limit) { why = 'blocked'; this.inD = this.busy(k) ? null : k; this.outD = null; }
        else this.outD = k;
      }
      this.hover = null;
      this.render(false);
      this.onChange(why);
    }
    set(inD, outD) {
      this.inD = inD; this.outD = outD;
      if (inD) this.view = new Date(parse(inD).getFullYear(), parse(inD).getMonth(), 1);
      this.render(false);
    }
  }

  /* availability badges on the house cards (home) */
  function badges() {
    $$('.house[data-key]').forEach((card) => {
      const k = card.dataset.key, b = $('[data-badge]', card);
      if (!b) return;
      if (!stay.in || !stay.out) { b.hidden = true; return; }
      let cls, txt;
      if (stay.guests > HOUSES[k].max) { cls = 'is-no'; txt = t('tooMany', HOUSES[k].max); }
      else if (!hasData(k)) { cls = 'is-ask'; txt = t('ask'); }
      else if (rangeFree(k, stay.in, stay.out)) { cls = 'is-ok'; txt = t('free'); }
      else { cls = 'is-no'; txt = t('busy'); }
      b.className = `badge ${cls}`;
      b.innerHTML = `<i></i>${txt} · ${fmt(stay.in)} → ${fmt(stay.out)}`;
      b.hidden = false;
    });
  }

  /* ---------------- home: date search in the hero ---------------- */
  const search = $('#search');
  if (search) {
    const pop = $('#pop'), sIn = $('#sIn'), sOut = $('#sOut'), sGuests = $('#sGuests');
    const months = () => (innerWidth < 760 ? 1 : 2);
    const labels = () => {
      sIn.textContent = picker.inD ? fmt(picker.inD, { weekday: 'short', day: 'numeric', month: 'short' }) : t('add');
      sOut.textContent = picker.outD ? fmt(picker.outD, { weekday: 'short', day: 'numeric', month: 'short' }) : t('add');
      $('#popHint').textContent = !picker.inD || picker.outD ? t('pickIn') : t('pickOut');
    };
    const close = () => { pop.classList.remove('is-open'); setTimeout(() => { pop.hidden = true; }, 250); };
    const open = () => { picker.months = months(); picker.render(false); pop.hidden = false; requestAnimationFrame(() => pop.classList.add('is-open')); labels(); };
    const picker = new Picker($('#popMonths'), {
      months: months(), inD: stay.in, outD: stay.out,
      onChange: () => { labels(); if (picker.inD && picker.outD) setTimeout(close, 350); },
    });
    if (stay.guests) sGuests.value = stay.guests;
    $$('[data-open]', search).forEach((b) => b.addEventListener('click', () => (pop.hidden ? open() : close())));
    $$('[data-step]', pop).forEach((b) => b.addEventListener('click', () => picker.step(+b.dataset.step)));
    $('#popClear').addEventListener('click', () => { picker.set(null, null); labels(); });
    $('#popDone').addEventListener('click', close);
    document.addEventListener('click', (e) => { if (!pop.hidden && !search.contains(e.target)) close(); });
    addEventListener('keydown', (e) => { if (e.key === 'Escape' && !pop.hidden) close(); });
    labels();
    search.addEventListener('submit', (e) => {
      e.preventDefault();
      if (!picker.inD || !picker.outD) { open(); toast(t('searchNeed')); return; }
      stay.in = picker.inD; stay.out = picker.outD; stay.guests = +sGuests.value; saveStay();
      badges();
      if (window.__cal) window.__cal.useStay();
      $('#houses').scrollIntoView({ behavior: reduce ? 'auto' : 'smooth' });
    });
  }
  badges();

  /* ---------------- booking calendar ---------------- */
  const calBox = $('#calMonths');
  if (calBox) {
    const fixed = $('#availability').dataset.house;
    const cal = {
      house: fixed || 'mali',
      init() {
        this.picker = new Picker(calBox, {
          house: this.house, months: innerWidth < 640 ? 1 : 2,
          onChange: (why) => { if (why === 'blocked') this.shake(); this.update(); },
        });
        if (fixed) { const tabs = $('#calTabs'); if (tabs) tabs.style.display = 'none'; }
        this.useStay();
      },
      useStay() {
        const ok = stay.in && stay.out && (!hasData(this.house) || rangeFree(this.house, stay.in, stay.out));
        this.picker.set(ok ? stay.in : null, ok ? stay.out : null);
        if (stay.guests) $('#reqGuests').dataset.want = stay.guests;
        this.update();
      },
      setHouse(h) {
        if (!HOUSES[h]) return;
        this.house = h; this.picker.house = h;
        $$('#calTabs button').forEach((b) => b.classList.toggle('is-active', b.dataset.h === h));
        this.useStay();
      },
      shake() {
        const c = $('.cal'); c.classList.remove('is-shake'); void c.offsetWidth; c.classList.add('is-shake');
        setTimeout(() => { $('#calNote').textContent = t('blocked'); }, 0);
      },
      update() {
        const p = this.picker;
        $('#calPrev').disabled = !p.canPrev();
        const sync = $('#calSync');
        if (hasData(this.house) && AV.updated) {
          sync.textContent = t('synced', new Date(AV.updated).toLocaleString(locale, { day: 'numeric', month: 'short', hour: '2-digit', minute: '2-digit' }));
          sync.style.display = '';
        } else sync.style.display = 'none';
        $('#calNote').textContent = hasData(this.house) ? (p.inD && !p.outD ? t('pickOut') : '') : t('studioNote');
        $('#reqHouse').textContent = HOUSES[this.house].name;
        const f = (k) => (k ? fmt(k, { weekday: 'short', day: 'numeric', month: 'short' }) : '—');
        $('#reqIn').textContent = f(p.inD);
        $('#reqOut').textContent = f(p.outD);
        $('#reqNights').textContent = p.inD && p.outD ? nightsBetween(p.inD, p.outD) : '—';
        $('#reqHint').style.display = p.inD && p.outD ? 'none' : '';
        $$('[data-stay="in"]').forEach((el) => { el.textContent = f(p.inD); });
        $$('[data-stay="out"]').forEach((el) => { el.textContent = f(p.outD); });
        const sel = $('#reqGuests');
        const want = +(sel.dataset.want || sel.value || 2);
        sel.innerHTML = '';
        for (let i = 1; i <= HOUSES[this.house].max; i++) sel.insertAdjacentHTML('beforeend', `<option value="${i}">${t('guests', i)}</option>`);
        sel.value = Math.min(want, HOUSES[this.house].max);
        if (p.inD && p.outD) { stay.in = p.inD; stay.out = p.outD; saveStay(); badges(); }
      },
    };
    window.__cal = cal;
    cal.init();
    $('#reqGuests').addEventListener('change', (e) => { e.target.dataset.want = e.target.value; stay.guests = +e.target.value; saveStay(); });
    $('#calPrev').addEventListener('click', () => { cal.picker.step(-1); setTimeout(() => cal.update(), 200); });
    $('#calNext').addEventListener('click', () => { cal.picker.step(1); setTimeout(() => cal.update(), 200); });
    $$('#calTabs button').forEach((b) => b.addEventListener('click', () => cal.setHouse(b.dataset.h)));
    $$('[data-house]').forEach((a) => a.addEventListener('click', () => cal.setHouse(a.dataset.house)));

    const requestData = (requireContact) => {
      const form = $('#req'), err = $('#reqError'), p = cal.picker;
      err.textContent = '';
      if (!p.inD || !p.outD) { err.textContent = t('needDates'); cal.shake(); $('.cal').scrollIntoView({ behavior: 'smooth', block: 'center' }); return null; }
      const name = form.name.value.trim(), email = form.email.value.trim();
      if (requireContact && (!name || !/^\S+@\S+\.\S+$/.test(email))) { err.textContent = t('needName'); return null; }
      const long = { weekday: 'short', day: 'numeric', month: 'short', year: 'numeric' };
      return {
        house: HOUSES[cal.house].name, inn: fmt(p.inD, long), out: fmt(p.outD, long),
        nights: nightsBetween(p.inD, p.outD), guests: form.guests.value,
        name: name || '-', email: email || '-', msg: form.msg.value.trim(),
      };
    };
    $('#req').addEventListener('submit', (e) => {
      e.preventDefault();
      const d = requestData(true);
      if (!d) return;
      location.href = `mailto:${CONTACT_EMAIL}?subject=${encodeURIComponent(t('subject', d.house, d.inn, d.out))}&body=${encodeURIComponent(t('body', d))}`;
      toast(t('mailOpened'));
    });
    $('#reqIg').addEventListener('click', async () => {
      const d = requestData(false);
      if (!d) return;
      try { await navigator.clipboard.writeText(t('body', d)); toast(t('copied')); } catch (e) { /* clipboard blocked */ }
      window.open(`https://ig.me/m/${INSTAGRAM}`, '_blank', 'noopener');
    });
  }


  /* ---------------- photo tour (Airbnb style) ---------------- */
  const tour = $('#tour');
  if (tour) {
    const openTour = (i) => {
      tour.classList.add('is-open'); tour.setAttribute('aria-hidden', 'false');
      document.body.style.overflow = 'hidden';
      const f = $$('figure', tour)[i];
      requestAnimationFrame(() => { tour.scrollTop = i && f ? f.offsetTop - 90 : 0; });
    };
    const closeTour = () => {
      tour.classList.remove('is-open'); tour.setAttribute('aria-hidden', 'true');
      document.body.style.overflow = '';
    };
    $$('[data-tour]').forEach((b) => b.addEventListener('click', () => openTour(+b.dataset.tour)));
    $('.tour__close', tour).addEventListener('click', closeTour);
    $('.tour__book', tour).addEventListener('click', closeTour);
    $$('#subnav a[href="#photos"]').forEach((a) => a.addEventListener('click', (e) => { e.preventDefault(); openTour(0); }));
    addEventListener('keydown', (e) => { if (e.key === 'Escape' && tour.classList.contains('is-open') && !lb.classList.contains('is-open')) closeTour(); });
  }

  /* ---------------- scroll progress ---------------- */
  const bar = document.createElement('div');
  bar.className = 'progress';
  document.body.appendChild(bar);
  const prog = () => {
    const h = document.documentElement.scrollHeight - innerHeight;
    bar.style.transform = `scaleX(${h > 0 ? Math.min(1, scrollY / h) : 0})`;
  };
  addEventListener('scroll', prog, { passive: true }); prog();

  const fine = matchMedia('(hover: hover) and (pointer: fine)').matches;

  /* ---------------- custom cursor ---------------- */
  if (fine && !reduce) {
    const c = document.createElement('div');
    c.className = 'cursor';
    c.innerHTML = `<span>${lang === 'es' ? 'Ver' : 'View'}</span>`;
    document.body.appendChild(c);
    let mx = -100, my = -100, cx = -100, cy = -100;
    addEventListener('mousemove', (e) => { mx = e.clientX; my = e.clientY; c.classList.add('is-on'); }, { passive: true });
    document.addEventListener('mouseleave', () => c.classList.remove('is-on'));
    const loop = () => {
      cx += (mx - cx) * 0.2; cy += (my - cy) * 0.2;
      c.style.transform = `translate3d(${cx}px, ${cy}px, 0)`;
      requestAnimationFrame(loop);
    };
    loop();
    document.addEventListener('mouseover', (e) => {
      const view = e.target.closest('[data-cursor="view"], #grid figure, .other__img');
      const link = !view && e.target.closest('a, button, select, .day');
      c.classList.toggle('is-view', !!view);
      c.classList.toggle('is-link', !!link);
    });
  }

  /* ---------------- magnetic buttons + tilting cards ---------------- */
  if (fine && !reduce) {
    $$('.btn--teal, .btn--dark, .collage__all, .cal__nav').forEach((b) => {
      b.addEventListener('mousemove', (e) => {
        const r = b.getBoundingClientRect();
        const x = (e.clientX - r.left - r.width / 2) * 0.22, y = (e.clientY - r.top - r.height / 2) * 0.35;
        b.style.transform = `translate(${x}px, ${y}px)`;
      });
      b.addEventListener('mouseleave', () => { b.style.transform = ''; });
    });
    $$('.other, .gitem, .why__item, .rev').forEach((card) => {
      card.addEventListener('mousemove', (e) => {
        const r = card.getBoundingClientRect();
        const x = (e.clientX - r.left) / r.width - 0.5, y = (e.clientY - r.top) / r.height - 0.5;
        card.style.transform = `perspective(900px) rotateY(${x * 5}deg) rotateX(${-y * 5}deg) translateY(-4px)`;
      });
      card.addEventListener('mouseleave', () => { card.style.transform = ''; });
    });
  }

  /* ---------------- page transitions ---------------- */
  const curtain = document.createElement('div');
  curtain.className = 'curtain';
  document.body.appendChild(curtain);
  document.addEventListener('click', (e) => {
    const a = e.target.closest('a');
    if (!a || a.target === '_blank' || e.metaKey || e.ctrlKey || e.shiftKey || e.defaultPrevented) return;
    const href = a.getAttribute('href') || '';
    if (!href || href.startsWith('#') || /^(mailto|tel):/.test(href)) return;
    const url = new URL(a.href, location.href);
    if (url.origin !== location.origin) return;
    if (url.pathname === location.pathname && url.hash) return;
    if (reduce) return;
    e.preventDefault();
    document.body.classList.add('is-leaving');
    setTimeout(() => { location.href = a.href; }, 620);
  });
  addEventListener('pageshow', (e) => { if (e.persisted) document.body.classList.remove('is-leaving'); });

  $('#year').textContent = new Date().getFullYear();
})();
