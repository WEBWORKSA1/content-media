/* ===========================================================================
   Content.Media — site runtime
   No build step, no dependencies, works on GitHub Pages static hosting.
   =========================================================================== */
(function () {
  'use strict';

  /* ---------------------------------------------------------------------
     Contact address. The address is stored XOR-masked + base64 encoded in
     window.CM.t and is only reassembled inside the browser at runtime, so
     it never appears in the HTML source, the repository or any crawler's
     view of the page. Every mailto link and every form endpoint is built
     from this function.
     --------------------------------------------------------------------- */
  function addr() {
    try {
      var raw = atob(window.CM.t), out = '';
      for (var i = 0; i < raw.length; i++) {
        out += String.fromCharCode(raw.charCodeAt(i) ^ window.CM.k);
      }
      return out;
    } catch (e) { return ''; }
  }
  function endpoint() {
    return window.CM.alias ? window.CM.gw + window.CM.alias : window.CM.gw + addr();
  }

  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  /* --------------------------------------------------------- base path
     When served from a sub-path (e.g. username.github.io/content-media/),
     prefix every root-relative URL in page bodies. On the custom domain the
     base is empty and this does nothing. */
  var BASE = (window.CM && window.CM.base) || '';
  window.cmUrl = function (u) { return (BASE && u.charAt(0) === '/' && u.charAt(1) !== '/') ? BASE + u : u; };
  if (BASE) {
    $$('main a[href^="/"], .mobile-menu a[href^="/"]').forEach(function (a) {
      var h = a.getAttribute('href');
      if (h.charAt(1) !== '/' && h.indexOf(BASE + '/') !== 0) a.setAttribute('href', BASE + h);
    });
    $$('main img[src^="/"]').forEach(function (i) { i.setAttribute('src', window.cmUrl(i.getAttribute('src'))); });
  }

  /* ------------------------------------------------ active nav (shared) */
  (function () {
    var path = location.pathname;
    $$('.nav-link').forEach(function (a) {
      var h = a.getAttribute('href');
      if (h && h !== '/' && path.indexOf(h) === 0) a.classList.add('is-active');
    });
  })();

  /* ------------------------------------------------------------- theme */
  var themeBtn = $('#themeToggle');
  if (themeBtn) {
    themeBtn.addEventListener('click', function () {
      var cur = document.documentElement.getAttribute('data-theme');
      var prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
      var next;
      if (cur === 'dark') next = 'light';
      else if (cur === 'light') next = 'dark';
      else next = prefersDark ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', next);
      try { localStorage.setItem('cm-theme', next); } catch (e) {}
    });
  }

  /* --------------------------------------------------------- mobile nav */
  var burger = $('#burger'), menu = $('#mobileMenu');
  if (burger && menu) {
    burger.addEventListener('click', function () {
      var open = burger.getAttribute('aria-expanded') === 'true';
      burger.setAttribute('aria-expanded', String(!open));
      menu.hidden = open;
      document.body.style.overflow = open ? '' : 'hidden';
    });
    $$('a', menu).forEach(function (a) {
      a.addEventListener('click', function () {
        burger.setAttribute('aria-expanded', 'false');
        menu.hidden = true; document.body.style.overflow = '';
      });
    });
  }

  /* ---------------------------------------------- scroll progress + CTA */
  var prog = $('#scrollProgress'), sticky = $('#stickyCta');
  var dismissed = false;
  try { dismissed = localStorage.getItem('cm-cta') === 'off'; } catch (e) {}
  var closeBtn = $('#stickyClose');
  if (closeBtn) closeBtn.addEventListener('click', function () {
    sticky.classList.remove('is-up');
    try { localStorage.setItem('cm-cta', 'off'); } catch (e) {}
  });
  function onScroll() {
    var h = document.documentElement.scrollHeight - window.innerHeight;
    var pct = h > 0 ? (window.scrollY / h) : 0;
    if (prog) prog.style.width = (pct * 100).toFixed(2) + '%';
    if (sticky && !dismissed) {
      if (pct > 0.45) { sticky.hidden = false; sticky.classList.add('is-up'); }
      else { sticky.classList.remove('is-up'); }
    }
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* -------------------------------------------------------- mail links */
  $$('[data-mail]').forEach(function (a) {
    var e = addr(); if (!e) return;
    var s = a.getAttribute('data-subject') || 'Content.Media enquiry';
    a.setAttribute('href', 'mailto:' + e + '?subject=' + encodeURIComponent(s));
    a.setAttribute('rel', 'nofollow');
  });

  /* ------------------------------------------------------------- forms */
  function serialize(form) {
    var data = {};
    new FormData(form).forEach(function (v, k) {
      if (data[k]) { data[k] = [].concat(data[k], v); } else { data[k] = v; }
    });
    data._subject = 'Content.Media — ' + (form.dataset.form || 'form') + ' submission';
    data._template = 'table';
    data._captcha = 'false';
    data.page = location.pathname;
    data.referrer = document.referrer || 'direct';
    data.submitted_at = new Date().toISOString();
    return data;
  }

  function status(form, msg, ok) {
    var el = $('.form-status', form);
    if (!el) return;
    el.textContent = msg;
    el.className = 'form-status ' + (ok ? 'ok' : 'err');
  }

  function validate(scope) {
    var bad = null;
    $$('input,select,textarea', scope).forEach(function (f) {
      if (f.offsetParent === null && f.type !== 'radio') return;
      if (!f.checkValidity()) { if (!bad) bad = f; }
    });
    if (bad) { bad.reportValidity && bad.reportValidity(); return false; }
    return true;
  }

  $$('form.cm-form').forEach(function (form) {
    /* multi-step */
    var steps = $$('.step', form);
    if (steps.length > 1) {
      var idx = 0;
      var bar = $('.progress-bar', form), dots = $$('.dot', form);
      var show = function (n) {
        steps.forEach(function (s, i) { s.hidden = i !== n; });
        if (bar) bar.style.width = ((n + 1) / steps.length * 100) + '%';
        dots.forEach(function (d, i) { d.classList.toggle('is-on', i <= n); });
        idx = n;
        form.scrollIntoView({ behavior: 'smooth', block: 'start' });
      };
      $$('[data-step-next]', form).forEach(function (b) {
        b.addEventListener('click', function () {
          if (!validate(steps[idx])) return;
          show(Math.min(idx + 1, steps.length - 1));
        });
      });
      $$('[data-step-back]', form).forEach(function (b) {
        b.addEventListener('click', function () { show(Math.max(idx - 1, 0)); });
      });
      /* auto-advance on the first card-choice step */
      $$('.choice input', steps[0]).forEach(function (r) {
        r.addEventListener('change', function () { setTimeout(function () { show(1); }, 220); });
      });
    }

    form.addEventListener('submit', function (ev) {
      ev.preventDefault();
      if (!validate(form)) return;
      var btn = $('button[type=submit]', form);
      var label = btn ? btn.textContent : '';
      if (btn) { btn.disabled = true; btn.textContent = 'Sending…'; }
      status(form, 'Sending…', true);

      fetch(endpoint(), {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
        body: JSON.stringify(serialize(form))
      }).then(function (r) { return r.json().catch(function () { return {}; }); })
        .then(function () {
          form.reset();
          status(form, '✓ Received. Check your inbox — we reply within one business day.', true);
          if (btn) { btn.disabled = false; btn.textContent = label; }
          if (form.dataset.form === 'lead') {
            setTimeout(function () { location.href = window.cmUrl('/services/thank-you/'); }, 700);
          } else if (form.dataset.form === 'newsletter') {
            setTimeout(function () { location.href = window.cmUrl('/newsletter/thank-you/'); }, 700);
          }
        })
        .catch(function () {
          status(form, 'That did not go through. Please try again, or use the contact page.', false);
          if (btn) { btn.disabled = false; btn.textContent = label; }
        });
    });
  });

  /* -------------------------------------------------------------- poll */
  $$('[data-poll]').forEach(function (p) {
    $$('button', p).forEach(function (b) {
      b.addEventListener('click', function () {
        $('.poll-btns', p).hidden = true;
        $('.poll-thanks', p).hidden = false;
        try { localStorage.setItem('cm-poll-' + p.dataset.poll, b.dataset.v); } catch (e) {}
      });
    });
  });

  /* ------------------------------------------------------ lazy youtube */
  $$('.video-embed[data-yt]').forEach(function (box) {
    box.addEventListener('click', function () {
      var id = box.dataset.yt;
      box.innerHTML = '<iframe src="https://www.youtube-nocookie.com/embed/' + id +
        '?autoplay=1&rel=0" title="YouTube video player" allow="accelerometer; autoplay; ' +
        'clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>';
    });
  });

  /* ------------------------------------------------------------ search */
  var modal = $('#searchModal'), input = $('#searchInput'), results = $('#searchResults');
  var index = null, sel = -1;
  function openSearch() {
    if (!modal) return;
    modal.hidden = false; input.focus();
    if (!index) {
      fetch(window.cmUrl('/assets/data/search-index.json')).then(function (r) { return r.json(); })
        .then(function (j) { index = j; render(input.value); })
        .catch(function () { index = []; });
    }
  }
  function closeSearch() { if (modal) modal.hidden = true; sel = -1; }
  function render(q) {
    if (!results) return;
    q = (q || '').trim().toLowerCase();
    var list = (index || []);
    if (q) {
      list = list.filter(function (it) {
        return (it.t + ' ' + it.d + ' ' + (it.k || '')).toLowerCase().indexOf(q) > -1;
      });
    }
    list = list.slice(0, 12);
    results.innerHTML = list.length
      ? list.map(function (it) {
          return '<li><a href="' + window.cmUrl(it.u) + '"><strong>' + it.t + '</strong><small>' + it.d + '</small></a></li>';
        }).join('')
      : '<li class="empty">Nothing matched. Try “RPM”, “rate card” or “sponsorship”.</li>';
    sel = -1;
  }
  if ($('#searchOpen')) $('#searchOpen').addEventListener('click', openSearch);
  if (input) input.addEventListener('input', function () { render(input.value); });
  document.addEventListener('keydown', function (e) {
    if (e.key === '/' && !/input|textarea|select/i.test(document.activeElement.tagName)) {
      e.preventDefault(); openSearch();
    }
    if ((e.key === 'k' || e.key === 'K') && (e.metaKey || e.ctrlKey)) { e.preventDefault(); openSearch(); }
    if (e.key === 'Escape') closeSearch();
    if (modal && !modal.hidden && (e.key === 'ArrowDown' || e.key === 'ArrowUp')) {
      e.preventDefault();
      var items = $$('li', results);
      if (!items.length) return;
      items.forEach(function (i) { i.classList.remove('is-sel'); });
      sel = e.key === 'ArrowDown' ? Math.min(sel + 1, items.length - 1) : Math.max(sel - 1, 0);
      items[sel].classList.add('is-sel');
      var a = $('a', items[sel]); if (a) a.focus();
    }
  });
  if (modal) modal.addEventListener('click', function (e) { if (e.target === modal) closeSearch(); });

  /* ----------------------------------------------------- count-up stats */
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        en.target.classList.add('seen');
        io.unobserve(en.target);
      });
    }, { threshold: 0.2 });
    $$('.stat-row, .card, .tier').forEach(function (el) { io.observe(el); });
  }

  /* ------------------------------------------------------ countdown(s) */
  $$('[data-countdown]').forEach(function (el) {
    var end = new Date(el.dataset.countdown).getTime();
    function tick() {
      var d = end - Date.now();
      if (d < 0) { el.innerHTML = '<p><strong>Entries are closed.</strong> Winners announced shortly.</p>'; return; }
      var days = Math.floor(d / 864e5), h = Math.floor(d / 36e5) % 24,
          m = Math.floor(d / 6e4) % 60, s = Math.floor(d / 1e3) % 60;
      el.innerHTML = [[days, 'days'], [h, 'hours'], [m, 'mins'], [s, 'secs']].map(function (p) {
        return '<div class="cd-cell"><b>' + String(p[0]).padStart(2, '0') + '</b><span>' + p[1] + '</span></div>';
      }).join('');
      setTimeout(tick, 1000);
    }
    tick();
  });

  /* ------------------------------------------------------- copy result */
  document.addEventListener('click', function (e) {
    var b = e.target.closest('[data-copy]');
    if (!b) return;
    var t = $(b.dataset.copy);
    var txt = t ? t.innerText : location.href;
    navigator.clipboard.writeText(txt + '\n\nSource: ' + location.href).then(function () {
      var old = b.textContent; b.textContent = 'Copied ✓';
      setTimeout(function () { b.textContent = old; }, 1600);
    });
  });

  /* ------------------------------------------------------ share button */
  document.addEventListener('click', function (e) {
    var b = e.target.closest('[data-share]');
    if (!b) return;
    var data = { title: document.title, url: location.href };
    if (navigator.share) { navigator.share(data).catch(function () {}); }
    else { navigator.clipboard.writeText(location.href); b.textContent = 'Link copied ✓'; }
  });
})();
