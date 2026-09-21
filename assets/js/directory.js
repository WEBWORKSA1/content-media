/* ===========================================================================
   Content.Media — tool directory runtime
   Client-side facets over /assets/data/tools.json. No backend required.
   State is mirrored to the URL so any filtered view is shareable and
   individually indexable.
   =========================================================================== */
(function () {
  'use strict';
  var root = document.getElementById('dirApp');
  if (!root) return;

  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  var grid = $('#dirGrid'), count = $('#dirCount'), search = $('#dirSearch'),
      sort = $('#dirSort'), facets = $('#dirFacets'), clear = $('#dirClear');
  var DATA = [], VIEW = [];
  var PALETTE = ['#4f46e5', '#db2777', '#0891b2', '#ea580c', '#059669', '#7c3aed', '#c026d3', '#0284c7'];

  var state = { q: '', cats: [], pricing: [], modal: [], platform: [], rating: 0, verified: false,
                featured: false, free: false, sort: 'trending' };

  function hash(s) { var h = 0; for (var i = 0; i < s.length; i++) h = (h * 31 + s.charCodeAt(i)) | 0; return Math.abs(h); }

  function price(t) {
    if (t.p === 'free') return 'Free';
    if (t.p === 'open_source') return 'Open source';
    if (t.p === 'contact') return 'Contact for pricing';
    if (t.from === 0) return t.p === 'freemium' ? 'Free plan available' : 'Free';
    return (t.p === 'freemium' ? 'Free plan, paid from $' : 'From $') + t.from + '/mo';
  }

  function card(t) {
    var col = PALETTE[hash(t.s) % PALETTE.length];
    var badges = [];
    if (t.feat) badges.push('<span class="badge-feat">Featured</span>');
    var tags = t.cats.slice(0, 2).map(function (c) { return '<span class="tag">' + c + '</span>'; }).join('');
    var pr = '<span class="tag ' + (t.p === 'free' || t.p === 'open_source' ? 'tag--free' : 'tag--brand') + '">' +
      price(t) + '</span>';
    return '<article class="card tool-card">' + badges.join('') +
      '<div class="tool-card__top">' +
        '<span class="tool-logo" style="background:' + col + '">' + t.n.slice(0, 1) + '</span>' +
        '<div><h3 style="margin:0"><a class="stretch" href="' + t.u + '" rel="nofollow sponsored noopener" target="_blank">' +
        t.n + '</a></h3><p style="font-size:.86rem;margin:.1rem 0 0">' + t.t + '</p></div>' +
      '</div>' +
      '<p style="font-size:.85rem">' + t.note + '</p>' +
      '<div class="tool-card__meta">' + pr + tags + (t.ver ? '<span class="tag tag--gold">Verified</span>' : '') + '</div>' +
      '<div class="tool-card__foot">' +
        '<span class="votes">▲ ' + t.v.toLocaleString('en-US') + '</span>' +
        '<span>★ ' + t.r.toFixed(1) + ' · editor ' + t.ed + '/100</span>' +
      '</div></article>';
  }

  function matches(t) {
    var q = state.q.toLowerCase();
    if (q && (t.n + ' ' + t.t + ' ' + t.note + ' ' + t.cats.join(' ')).toLowerCase().indexOf(q) === -1) return false;
    if (state.cats.length && !state.cats.some(function (c) { return t.cats.indexOf(c) > -1; })) return false;
    if (state.pricing.length && state.pricing.indexOf(t.p) === -1) return false;
    if (state.modal.length && !state.modal.some(function (m) { return t.m.indexOf(m) > -1; })) return false;
    if (state.platform.length && !state.platform.some(function (p) { return t.pf.indexOf(p) > -1; })) return false;
    if (state.rating && t.r < state.rating) return false;
    if (state.verified && !t.ver) return false;
    if (state.featured && !t.feat) return false;
    if (state.free && !(t.p === 'free' || t.p === 'freemium' || t.p === 'open_source')) return false;
    return true;
  }

  var SORTS = {
    trending:  function (a, b) { return (b.v * 0.6 + b.ed * 40) - (a.v * 0.6 + a.ed * 40); },
    popular:   function (a, b) { return b.v - a.v; },
    rated:     function (a, b) { return (b.r * Math.log10(b.v + 10)) - (a.r * Math.log10(a.v + 10)); },
    editor:    function (a, b) { return b.ed - a.ed; },
    newest:    function (a, b) { return b.yr - a.yr; },
    price:     function (a, b) { return (a.from || 0) - (b.from || 0); },
    az:        function (a, b) { return a.n.localeCompare(b.n); }
  };

  function render() {
    VIEW = DATA.filter(matches).sort(SORTS[state.sort] || SORTS.trending);
    /* featured listings always surface first within the current view */
    VIEW = VIEW.filter(function (t) { return t.feat; }).concat(VIEW.filter(function (t) { return !t.feat; }));
    grid.innerHTML = VIEW.length ? VIEW.map(card).join('')
      : '<div class="empty"><p><strong>No tools match those filters.</strong></p>' +
        '<p>Try clearing a filter, or <a href="' + (window.cmUrl || String)('/directory/submit/') + '">submit the tool you were looking for</a>.</p></div>';
    count.textContent = VIEW.length + ' of ' + DATA.length + ' tools';
    syncUrl();
  }

  function syncUrl() {
    var p = new URLSearchParams();
    if (state.q) p.set('q', state.q);
    if (state.cats.length) p.set('cat', state.cats.join(','));
    if (state.pricing.length) p.set('price', state.pricing.join(','));
    if (state.sort !== 'trending') p.set('sort', state.sort);
    var qs = p.toString();
    history.replaceState(null, '', qs ? '?' + qs : location.pathname);
  }

  function readUrl() {
    var p = new URLSearchParams(location.search);
    state.q = p.get('q') || '';
    state.cats = p.get('cat') ? p.get('cat').split(',') : [];
    state.pricing = p.get('price') ? p.get('price').split(',') : [];
    state.sort = p.get('sort') || 'trending';
    if (search) search.value = state.q;
    if (sort) sort.value = state.sort;
  }

  function buildFacets() {
    var counts = {};
    DATA.forEach(function (t) { t.cats.forEach(function (c) { counts[c] = (counts[c] || 0) + 1; }); });
    var cats = Object.keys(counts).sort(function (a, b) { return counts[b] - counts[a]; });
    var catHtml = cats.map(function (c) {
      return '<label><input type="checkbox" data-facet="cats" value="' + c + '"' +
        (state.cats.indexOf(c) > -1 ? ' checked' : '') + '> ' + c +
        '<span class="filter-count">' + counts[c] + '</span></label>';
    }).join('');

    var pricing = [['free', 'Free'], ['freemium', 'Freemium'], ['paid', 'Paid'],
                   ['open_source', 'Open source'], ['contact', 'Contact for pricing']];
    var priceHtml = pricing.map(function (p) {
      var n = DATA.filter(function (t) { return t.p === p[0]; }).length;
      return '<label><input type="checkbox" data-facet="pricing" value="' + p[0] + '"' +
        (state.pricing.indexOf(p[0]) > -1 ? ' checked' : '') + '> ' + p[1] +
        '<span class="filter-count">' + n + '</span></label>';
    }).join('');

    var mods = ['text', 'image', 'video', 'audio', 'code', 'data'];
    var modHtml = mods.map(function (m) {
      var n = DATA.filter(function (t) { return t.m.indexOf(m) > -1; }).length;
      return '<label><input type="checkbox" data-facet="modal" value="' + m + '"> ' +
        m.charAt(0).toUpperCase() + m.slice(1) + '<span class="filter-count">' + n + '</span></label>';
    }).join('');

    var plats = [['web', 'Web'], ['ios', 'iOS'], ['android', 'Android'], ['mac', 'macOS'],
                 ['windows', 'Windows'], ['api', 'API'], ['chrome_extension', 'Chrome extension'], ['cli', 'CLI']];
    var platHtml = plats.map(function (p) {
      var n = DATA.filter(function (t) { return t.pf.indexOf(p[0]) > -1; }).length;
      if (!n) return '';
      return '<label><input type="checkbox" data-facet="platform" value="' + p[0] + '"> ' + p[1] +
        '<span class="filter-count">' + n + '</span></label>';
    }).join('');

    facets.innerHTML =
      '<div class="filter-group"><h4>Category</h4>' + catHtml + '</div>' +
      '<div class="filter-group"><h4>Pricing model</h4>' + priceHtml + '</div>' +
      '<div class="filter-group"><h4>Works with</h4>' + modHtml + '</div>' +
      '<div class="filter-group"><h4>Platform</h4>' + platHtml + '</div>' +
      '<div class="filter-group"><h4>Minimum rating</h4>' +
        [0, 4, 4.5].map(function (r) {
          return '<label><input type="radio" name="rating" data-facet="rating" value="' + r + '"' +
            (r === 0 ? ' checked' : '') + '> ' + (r === 0 ? 'Any rating' : '★ ' + r + ' and up') + '</label>';
        }).join('') + '</div>' +
      '<div class="filter-group"><h4>Quality</h4>' +
        '<label><input type="checkbox" data-facet="verified"> Verified listings only</label>' +
        '<label><input type="checkbox" data-facet="featured"> Featured only</label>' +
        '<label><input type="checkbox" data-facet="free"> Has a free tier</label>' +
      '</div>';

    facets.addEventListener('change', function (e) {
      var el = e.target, f = el.dataset.facet;
      if (!f) return;
      if (f === 'rating') state.rating = +el.value;
      else if (f === 'verified' || f === 'featured' || f === 'free') state[f] = el.checked;
      else {
        var arr = state[f];
        var i = arr.indexOf(el.value);
        if (el.checked && i === -1) arr.push(el.value);
        if (!el.checked && i > -1) arr.splice(i, 1);
      }
      render();
    });
  }

  if (search) {
    var timer;
    search.addEventListener('input', function () {
      clearTimeout(timer);
      timer = setTimeout(function () { state.q = search.value; render(); }, 140);
    });
  }
  if (sort) sort.addEventListener('change', function () { state.sort = sort.value; render(); });
  if (clear) clear.addEventListener('click', function () {
    state = { q: '', cats: [], pricing: [], modal: [], platform: [], rating: 0,
              verified: false, featured: false, free: false, sort: 'trending' };
    if (search) search.value = ''; if (sort) sort.value = 'trending';
    buildFacets(); render();
  });

  fetch((window.cmUrl || String)('/assets/data/tools.json'))
    .then(function (r) { return r.json(); })
    .then(function (j) {
      DATA = j;
      readUrl();
      buildFacets();
      render();
    })
    .catch(function () {
      grid.innerHTML = '<div class="empty">The directory could not load. ' +
        '<a href="' + (window.cmUrl || String)('/contact/') + '">Tell us</a> and we will fix it.</div>';
    });
})();
