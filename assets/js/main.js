(function () {
  'use strict';

  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var canAnimate = typeof window.anime === 'function' && !reduce;
  var finePointer = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
  var DOT_BASE = 0.4;
  var slice = Array.prototype.slice;

  if (canAnimate) document.documentElement.classList.add('anim');

  // ---------------------------------------------------------------- utilidades
  function visibleOnce(nodes, fn, options) {
    var list = slice.call(nodes);
    if (!list.length) return;
    if (!('IntersectionObserver' in window)) { list.forEach(fn); return; }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        io.unobserve(entry.target);
        fn(entry.target);
      });
    }, options || { threshold: 0.12, rootMargin: '0px 0px -6% 0px' });
    list.forEach(function (n) { io.observe(n); });
  }

  function format(value, decimals, sep) {
    return value.toFixed(decimals).replace('.', sep || '.');
  }

  function tween(el, end, options) {
    options = options || {};
    var decimals = options.decimals || 0;
    var sep = options.sep || '.';
    var suffix = options.suffix || '';
    if (!canAnimate) { el.textContent = format(end, decimals, sep) + suffix; return; }
    var state = { v: 0 };
    anime({
      targets: state,
      v: end,
      round: Math.pow(10, decimals),
      duration: options.duration || 1800,
      easing: 'easeOutExpo',
      update: function () { el.textContent = format(state.v, decimals, sep) + suffix; }
    });
  }

  // Dibuja los trazos de los iconos como si se escribieran.
  function draw(scope, delay) {
    if (!canAnimate) return;
    var els = slice.call(scope.querySelectorAll('.glyph path, .glyph circle, .glyph rect, .glyph ellipse, .glyph line, .glyph polyline'))
      .filter(function (el) { return typeof el.getTotalLength === 'function'; });
    if (!els.length) return;
    anime({
      targets: els,
      strokeDashoffset: [anime.setDashoffset, 0],
      easing: 'easeInOutSine',
      duration: 1100,
      delay: anime.stagger(35, { start: delay || 0 })
    });
  }

  // ---------------------------------------------------------------- copiar correo
  var button = document.getElementById('copy-email');
  var toast = document.getElementById('toast');
  var email = document.querySelector('.email');
  if (button && toast && email) {
    var timer;
    var say = function (message) {
      toast.textContent = message;
      clearTimeout(timer);
      timer = setTimeout(function () { toast.textContent = ''; }, 3200);
    };
    button.addEventListener('click', function () {
      var text = email.textContent.trim();
      if (!navigator.clipboard) { say(button.dataset.failed); return; }
      navigator.clipboard.writeText(text).then(
        function () { say(button.dataset.copied); },
        function () { say(button.dataset.failed); }
      );
    });
  }

  // ---------------------------------------------------------------- titulares palabra por palabra
  function splitWords(root) {
    root.setAttribute('aria-label', root.textContent.replace(/\s+/g, ' ').trim());
    (function walk(node) {
      slice.call(node.childNodes).forEach(function (child) {
        if (child.nodeType === 1) { walk(child); return; }
        if (child.nodeType !== 3) return;
        var frag = document.createDocumentFragment();
        child.textContent.split(/(\s+)/).forEach(function (part) {
          if (!part) return;
          if (/^\s+$/.test(part)) { frag.appendChild(document.createTextNode(' ')); return; }
          var outer = document.createElement('span');
          var inner = document.createElement('span');
          outer.className = 'w';
          outer.setAttribute('aria-hidden', 'true');
          inner.className = 'wi';
          inner.textContent = part;
          outer.appendChild(inner);
          frag.appendChild(outer);
        });
        node.replaceChild(frag, child);
      });
    })(root);
    return root.querySelectorAll('.wi');
  }

  var h1 = document.querySelector('.hero h1');
  if (h1) {
    if (canAnimate) {
      var heroWords = splitWords(h1);
      h1.classList.add('ready');
      anime({
        targets: heroWords,
        translateY: ['108%', '0%'],
        duration: 1100,
        easing: 'easeOutExpo',
        delay: anime.stagger(90, { start: 120 })
      });
    } else {
      h1.classList.add('ready');
    }
  }

  if (canAnimate) {
    slice.call(document.querySelectorAll('.section-title, .contact h2')).forEach(function (title) {
      var words = splitWords(title);
      anime.set(words, { translateY: '108%' });
      visibleOnce([title], function () {
        anime({ targets: words, translateY: ['108%', '0%'], duration: 1000, easing: 'easeOutExpo', delay: anime.stagger(70) });
      }, { threshold: 0.5 });
    });

    // Tarjeta del hero: filas en cascada y trazos de los iconos.
    var ledger = document.querySelector('.ledger');
    if (ledger) {
      anime({
        targets: ledger.querySelectorAll('.s'),
        opacity: [0, 1],
        translateX: [-18, 0],
        duration: 900,
        easing: 'easeOutQuad',
        delay: anime.stagger(150, { start: 750 })
      });
      draw(ledger, 900);
    }

    // Bloques de contenido: entrada escalonada al leerlos.
    visibleOnce(document.querySelectorAll('.stagger'), function (container) {
      anime({
        targets: container.querySelectorAll('.s'),
        opacity: [0, 1],
        translateY: [30, 0],
        duration: 1000,
        easing: 'easeOutExpo',
        delay: anime.stagger(90)
      });
      draw(container, 150);
    });

    // Contadores y flujo del proyecto.
    slice.call(document.querySelectorAll('[data-count]')).forEach(function (el) {
      visibleOnce([el], function () {
        tween(el, parseFloat(el.dataset.count), {
          decimals: parseInt(el.dataset.decimals, 10) || 0,
          sep: el.dataset.sep,
          suffix: el.dataset.suffix,
          duration: 2000
        });
      }, { threshold: 0.6 });
    });
    slice.call(document.querySelectorAll('.pipeline')).forEach(function (list) {
      slice.call(list.children).forEach(function (li) { li.style.opacity = 0; });
      visibleOnce([list], function () {
        anime({
          targets: list.children,
          opacity: [0, 1],
          translateX: [-14, 0],
          duration: 700,
          easing: 'easeOutQuad',
          delay: anime.stagger(170, { start: 300 })
        });
      }, { threshold: 0.6 });
    });
  }

  // ---------------------------------------------------------------- progreso de lectura
  var progress = document.querySelector('.progress');
  if (progress) {
    var ticking = false;
    var update = function () {
      ticking = false;
      var max = document.documentElement.scrollHeight - window.innerHeight;
      progress.style.transform = 'scaleX(' + (max > 0 ? Math.min(1, window.scrollY / max) : 0) + ')';
    };
    window.addEventListener('scroll', function () {
      if (!ticking) { ticking = true; requestAnimationFrame(update); }
    }, { passive: true });
    update();
  }

  // ---------------------------------------------------------------- cuadrícula de puntos (anime.js)
  function DotGrid(host) {
    var size = 36;
    var parent = host.parentElement;
    var cols = 1;
    var rows = 1;
    var dots = [];
    var visible = false;
    var lastMove = 0;

    function build() {
      cols = Math.max(1, Math.ceil(host.clientWidth / size));
      rows = Math.max(1, Math.ceil(host.clientHeight / size));
      host.style.setProperty('--cols', cols);
      host.style.setProperty('--cell', size + 'px');
      host.textContent = '';
      var frag = document.createDocumentFragment();
      for (var i = 0; i < cols * rows; i++) frag.appendChild(document.createElement('i'));
      host.appendChild(frag);
      dots = host.children;
    }

    function pulse(index, strong) {
      if (!canAnimate || !visible) return;
      anime.remove(dots);
      anime({
        targets: dots,
        scale: [
          { value: strong ? 3.2 : 2.5, duration: 260, easing: 'easeOutSine' },
          { value: 1, duration: 750, easing: 'easeInOutQuad' }
        ],
        opacity: [
          { value: 1, duration: 260, easing: 'easeOutSine' },
          { value: DOT_BASE, duration: 750, easing: 'easeInOutQuad' }
        ],
        delay: anime.stagger(strong ? 28 : 42, { grid: [cols, rows], from: index })
      });
    }

    function indexAt(clientX, clientY) {
      var rect = host.getBoundingClientRect();
      var col = Math.min(cols - 1, Math.max(0, Math.floor((clientX - rect.left) / size)));
      var row = Math.min(rows - 1, Math.max(0, Math.floor((clientY - rect.top) / size)));
      return row * cols + col;
    }

    build();
    if (!canAnimate) return;

    new IntersectionObserver(function (entries) {
      var wasVisible = visible;
      visible = entries[0].isIntersecting;
      if (visible && !wasVisible) pulse(Math.floor(rows / 2) * cols + Math.floor(cols * 0.7), false);
    }).observe(host);

    setInterval(function () {
      if (!visible || document.hidden) return;
      pulse(Math.floor(Math.random() * cols * rows), false);
    }, 3600);

    parent.addEventListener('pointermove', function (ev) {
      var now = performance.now();
      if (now - lastMove < 280) return;
      lastMove = now;
      pulse(indexAt(ev.clientX, ev.clientY), false);
    });
    parent.addEventListener('pointerdown', function (ev) {
      lastMove = performance.now();
      pulse(indexAt(ev.clientX, ev.clientY), true);
    });

    var resizeTimer;
    window.addEventListener('resize', function () {
      clearTimeout(resizeTimer);
      resizeTimer = setTimeout(build, 200);
    });
  }

  slice.call(document.querySelectorAll('[data-dotgrid]')).forEach(DotGrid);

  // ---------------------------------------------------------------- anillos que laten (anime.js)
  function Rings(svg) {
    var loop = anime({
      targets: svg.querySelectorAll('circle'),
      r: [60, 470],
      opacity: [{ value: 0.55, duration: 700, easing: 'easeOutSine' }, { value: 0, duration: 5300, easing: 'easeInSine' }],
      duration: 6000,
      easing: 'easeOutSine',
      delay: anime.stagger(1200),
      loop: true,
      autoplay: false
    });
    new IntersectionObserver(function (entries) {
      if (entries[0].isIntersecting) loop.play(); else loop.pause();
    }).observe(svg);
  }
  if (canAnimate) slice.call(document.querySelectorAll('.rings')).forEach(Rings);

  // ---------------------------------------------------------------- foco de luz en el hero
  var hero = document.querySelector('.hero');
  if (hero && finePointer && !reduce) {
    hero.addEventListener('pointermove', function (ev) {
      var rect = hero.getBoundingClientRect();
      hero.style.setProperty('--mx', (ev.clientX - rect.left) + 'px');
      hero.style.setProperty('--my', (ev.clientY - rect.top) + 'px');
    });
  }

  // ---------------------------------------------------------------- interacciones con anime.js
  if (canAnimate && finePointer) {
    // Botones magnéticos
    slice.call(document.querySelectorAll('.button.primary')).forEach(function (btn) {
      btn.addEventListener('pointermove', function (ev) {
        var r = btn.getBoundingClientRect();
        anime.remove(btn);
        anime({
          targets: btn,
          translateX: (ev.clientX - (r.left + r.width / 2)) * 0.25,
          translateY: (ev.clientY - (r.top + r.height / 2)) * 0.4,
          duration: 200,
          easing: 'easeOutQuad'
        });
      });
      btn.addEventListener('pointerleave', function () {
        anime.remove(btn);
        anime({ targets: btn, translateX: 0, translateY: 0, duration: 900, easing: 'easeOutElastic(1, .5)' });
      });
    });

    // Inclinación 3D de las tarjetas de proyecto
    slice.call(document.querySelectorAll('.project')).forEach(function (card) {
      card.addEventListener('pointermove', function (ev) {
        var r = card.getBoundingClientRect();
        var px = (ev.clientX - r.left) / r.width - 0.5;
        var py = (ev.clientY - r.top) / r.height - 0.5;
        anime.remove(card);
        anime({ targets: card, rotateY: px * 5, rotateX: py * -5, duration: 250, easing: 'easeOutQuad' });
      });
      card.addEventListener('pointerleave', function () {
        anime.remove(card);
        anime({ targets: card, rotateX: 0, rotateY: 0, duration: 900, easing: 'easeOutElastic(1, .6)' });
      });
    });

    // Los iconos reaccionan al pasar por encima
    slice.call(document.querySelectorAll('.project, .principles > div, .skills > div, .tile, .edu-row')).forEach(function (el) {
      var icon = el.querySelector('.icon-box, .glyph');
      if (!icon) return;
      el.addEventListener('pointerenter', function () {
        anime.remove(icon);
        anime({ targets: icon, scale: [1, 1.18, 1], rotate: [0, -10, 0], duration: 800, easing: 'easeOutElastic(1, .6)' });
      });
    });
  }

  // ---------------------------------------------------------------- GitHub en vivo
  var gh = document.getElementById('gh');
  if (gh) {
    visibleOnce([gh], function () { loadGitHub(gh); }, { threshold: 0, rootMargin: '300px 0px' });
  }

  function loadGitHub(root) {
    var user = root.dataset.user;
    var t = JSON.parse(root.dataset.i18n);
    var api = 'https://api.github.com/users/' + user;
    var CACHE = 'gh-live:' + user;
    var TTL = 30 * 60 * 1000;
    var list = root.querySelector('.gh-repos');
    var errorBox = root.querySelector('.gh-error');
    var heat = root.querySelector('.heat');

    function readCache() {
      try {
        var c = JSON.parse(sessionStorage.getItem(CACHE));
        if (c && Date.now() - c.t < TTL) return c.d;
      } catch (e) { /* sin almacenamiento */ }
      return null;
    }
    function writeCache(d) {
      try { sessionStorage.setItem(CACHE, JSON.stringify({ t: Date.now(), d: d })); } catch (e) { /* sin almacenamiento */ }
    }
    function getJson(url) {
      return fetch(url, { headers: { Accept: 'application/vnd.github+json' } }).then(function (r) {
        if (!r.ok) throw new Error('HTTP ' + r.status);
        return r.json();
      });
    }

    function dayKey(date) {
      return date.getFullYear() + '-' + (date.getMonth() + 1) + '-' + date.getDate();
    }

    function ago(iso) {
      var days = Math.floor((Date.now() - new Date(iso).getTime()) / 86400000);
      var amount;
      var unit;
      if (days < 1) return t.today;
      if (days < 60) { amount = days; unit = t.d; }
      else if (days < 730) { amount = Math.floor(days / 30); unit = t.m; }
      else { amount = Math.floor(days / 365); unit = t.y; }
      return t.locale === 'es' ? t.ago + ' ' + amount + ' ' + unit : amount + ' ' + unit + ' ' + t.ago;
    }

    function summarize(profile, repos, events) {
      var counts = {};
      var total = 0;
      var limit = Date.now() - 91 * 86400000;
      (events || []).forEach(function (ev) {
        if (ev.type !== 'PushEvent') return;
        var when = new Date(ev.created_at);
        if (when.getTime() < limit) return;
        var n = (ev.payload && (ev.payload.size || (ev.payload.commits && ev.payload.commits.length))) || 1;
        counts[dayKey(when)] = (counts[dayKey(when)] || 0) + n;
        total += n;
      });
      return {
        repos: profile.public_repos,
        followers: profile.followers,
        commits: total,
        counts: counts,
        list: Object.keys(t.featured).map(function (name) {
          return repos.filter(function (r) { return r.name === name; })[0];
        }).filter(Boolean).map(function (r) {
          return { name: r.name, url: r.html_url, desc: t.featured[r.name], lang: r.language, pushed: r.pushed_at };
        })
      };
    }

    function renderStats(data) {
      slice.call(root.querySelectorAll('[data-stat]')).forEach(function (el) {
        tween(el, data[el.dataset.stat] || 0, { duration: 1600 });
      });
    }

    function renderHeat(data) {
      var today = new Date();
      today.setHours(0, 0, 0, 0);
      var start = new Date(today);
      start.setDate(today.getDate() - today.getDay() - 12 * 7);
      var max = 0;
      var cells = [];
      for (var i = 0; i < 91; i++) {
        var day = new Date(start);
        day.setDate(start.getDate() + i);
        var c = day > today ? -1 : (data.counts[dayKey(day)] || 0);
        if (c > max) max = c;
        cells.push({ day: day, c: c });
      }
      heat.textContent = '';
      cells.forEach(function (cell) {
        var el = document.createElement('i');
        if (cell.c < 0) {
          el.className = 'future';
        } else {
          el.dataset.l = cell.c === 0 ? 0 : Math.max(1, Math.ceil(4 * cell.c / max));
          el.title = cell.c + ' ' + (cell.c === 1 ? t.commit : t.commitsWord) + ' · ' +
            cell.day.toLocaleDateString(t.locale, { day: 'numeric', month: 'short' });
        }
        heat.appendChild(el);
      });
      heat.setAttribute('aria-label', heat.getAttribute('aria-label') + ': ' + data.commits);
      if (!data.commits) {
        var note = root.querySelector('.heat-note');
        if (note) note.textContent = t.empty;
      }
      if (canAnimate) {
        anime({
          targets: heat.children,
          scale: [0, 1],
          opacity: [0, 1],
          duration: 600,
          easing: 'easeOutBack',
          delay: anime.stagger(9)
        });
      }
    }

    function renderRepos(data) {
      list.textContent = '';
      data.list.forEach(function (r) {
        var li = document.createElement('li');
        li.className = 'repo';
        var icon = document.createElement('span');
        icon.className = 'repo-icon';
        icon.innerHTML = '<svg class="glyph" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H19a1 1 0 0 1 1 1v18a1 1 0 0 1-1 1H6.5a1 1 0 0 1 0-5H20"/></svg>';
        var body = document.createElement('div');
        var link = document.createElement('a');
        link.className = 'repo-name';
        link.href = r.url;
        link.target = '_blank';
        link.rel = 'noopener';
        link.textContent = r.name;
        var hint = document.createElement('span');
        hint.className = 'sr-only';
        hint.textContent = ' ' + t.newTab;
        link.appendChild(hint);
        var desc = document.createElement('p');
        desc.textContent = r.desc || t.noDesc;
        var meta = document.createElement('span');
        meta.className = 'meta';
        meta.textContent = (r.lang ? r.lang + ' · ' : '') + t.updated + ' ' + ago(r.pushed);
        body.appendChild(link);
        body.appendChild(desc);
        body.appendChild(meta);
        li.appendChild(icon);
        li.appendChild(body);
        list.appendChild(li);
      });
      if (canAnimate) {
        anime({
          targets: list.children,
          opacity: [0, 1],
          translateX: [-16, 0],
          duration: 800,
          easing: 'easeOutQuad',
          delay: anime.stagger(110)
        });
        draw(list, 100);
      }
    }

    function show(data) {
      renderStats(data);
      renderHeat(data);
      renderRepos(data);
      root.setAttribute('aria-busy', 'false');
    }

    function fail() {
      list.hidden = true;
      errorBox.hidden = false;
      root.setAttribute('aria-busy', 'false');
    }

    var cached = readCache();
    if (cached) { show(cached); return; }

    Promise.all([
      getJson(api),
      getJson(api + '/repos?per_page=100&sort=pushed'),
      getJson(api + '/events/public?per_page=100').catch(function () { return []; })
    ]).then(function (res) {
      var data = summarize(res[0], res[1], res[2]);
      writeCache(data);
      show(data);
    }).catch(fail);
  }
})();
