/* ===========================================================================
   Content.Media — calculator engine
   One generic runtime; each tool page supplies data-calc="<engine>".
   Results are always shown as LOW–HIGH ranges: single numbers are a lie.
   =========================================================================== */
(function () {
  'use strict';
  var B = window.CMB;
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  var usd = function (n) {
    if (!isFinite(n)) n = 0;
    var abs = Math.abs(n);
    if (abs >= 1e6) return '$' + (n / 1e6).toFixed(abs >= 1e7 ? 1 : 2) + 'M';
    if (abs >= 1e4) return '$' + Math.round(n).toLocaleString('en-US');
    if (abs >= 100) return '$' + Math.round(n).toLocaleString('en-US');
    return '$' + n.toFixed(abs < 10 ? 2 : 0);
  };
  var num = function (n) { return Math.round(n).toLocaleString('en-US'); };
  var pct = function (n) { return n.toFixed(n < 10 ? 2 : 1) + '%'; };
  var rng = function (a, b, f) { f = f || usd; return f(a) + ' – ' + f(b); };
  var find = function (arr, k) { for (var i = 0; i < arr.length; i++) if (arr[i].key === k) return arr[i]; return arr[0]; };
  var band = function (arr, v) { for (var i = 0; i < arr.length; i++) if (v <= arr[i].max) return arr[i]; return arr[arr.length - 1]; };

  /* ------------------------------------------------------------ engines */
  var ENGINES = {

    youtube: function (v) {
      var n = find(B.niches, v.niche), g = find(B.geo, v.geo);
      var views = +v.views || 0;              // views per month
      var mLo = views * B.monetisedShare.lo, mHi = views * B.monetisedShare.hi;
      var lo = (mLo / 1000) * n.rpmLo * g.mult;
      var hi = (mHi / 1000) * n.rpmHi * g.mult;
      var memb = (+v.subs || 0) * 0.004 * 3.4;      // ~0.4% join a $4.99 tier, 68% net
      var spon = (views / 1000) * ((B.rateCard.youtube_integration.lo + B.rateCard.youtube_integration.hi) / 2) * 0.12;
      return {
        big: ['Estimated monthly AdSense revenue', lo, hi],
        cells: [
          ['Per day', lo / 30.4, hi / 30.4],
          ['Per month', lo, hi],
          ['Per year', lo * 12, hi * 12]
        ],
        bars: [
          ['AdSense', lo, hi],
          ['Sponsorships', spon * 0.7, spon * 1.6],
          ['Memberships', memb * 0.6, memb * 1.5],
          ['Affiliate', lo * 0.15, hi * 0.6]
        ],
        total: ['Total monthly earning potential, all rails',
          lo + spon * 0.7 + memb * 0.6 + lo * 0.15,
          hi + spon * 1.6 + memb * 1.5 + hi * 0.6],
        notes: [
          n.label + ' carries an RPM of ' + usd(n.rpmLo) + '–' + usd(n.rpmHi) +
            ' per 1,000 monetised views before geography.',
          'Geography factor applied: ×' + g.mult.toFixed(2) + ' (' + g.label + ').',
          'Only ' + Math.round(B.monetisedShare.lo * 100) + '–' + Math.round(B.monetisedShare.hi * 100) +
            '% of views serve a paid impression. YouTube keeps 45% of in-stream ad revenue; ' +
            'the RPM figures above are already your 55% share.'
        ]
      };
    },

    shorts: function (v) {
      var views = +v.views || 0, g = find(B.geo, v.geo);
      var lo = (views / 1000) * B.shorts.rpmLo * g.mult * 1000 / 1000;
      var hi = (views / 1000) * B.shorts.rpmHi * g.mult;
      lo = (views / 1000) * B.shorts.rpmLo * g.mult;
      var brand = (views / 1000) * ((B.rateCard.youtube_short.lo + B.rateCard.youtube_short.hi) / 2) * 0.05;
      var longEquivLo = (views / 1000) * 4 * g.mult, longEquivHi = (views / 1000) * 12 * g.mult;
      return {
        big: ['Estimated monthly Shorts revenue', lo, hi],
        cells: [
          ['Per 1M Shorts views', (1e6 / 1000) * B.shorts.rpmLo * g.mult, (1e6 / 1000) * B.shorts.rpmHi * g.mult],
          ['Per month', lo, hi],
          ['Per year', lo * 12, hi * 12]
        ],
        bars: [
          ['Shorts pool', lo, hi],
          ['Brand deals', brand * 0.6, brand * 1.8],
          ['Same views, long-form', longEquivLo, longEquivHi]
        ],
        total: ['Shorts + brand deals, monthly', lo + brand * 0.6, hi + brand * 1.8],
        notes: [
          'Shorts pay from a revenue pool at roughly ' + B.shorts.rpmLo.toFixed(2) + '–' +
            B.shorts.rpmHi.toFixed(2) + ' RPM — 30–100× below long-form.',
          'The third bar shows what the same view count would earn as long-form video. ' +
            'That gap is the entire argument for repurposing Shorts audiences into long-form.',
          'Creators keep 45% of the Shorts pool after music licensing is deducted.'
        ]
      };
    },

    tiktok: function (v) {
      var f = +v.followers || 0, likes = +v.likes || 0, vids = Math.max(+v.videos || 1, 1);
      var er = f > 0 ? (likes / (f * vids)) * 100 : 0;
      var bd = band(B.ttBands, f);
      var base = f / 1000;
      var mod = (B.rateMods.niche[v.niche] || 1);
      var lo = base * B.rateCard.tiktok_video.lo * mod * (er / ((bd.lo + bd.hi) / 2));
      var hi = base * B.rateCard.tiktok_video.hi * mod * (er / ((bd.lo + bd.hi) / 2));
      lo = Math.max(lo, base * B.rateCard.tiktok_video.lo * mod * 0.45);
      hi = Math.max(hi, lo * 1.5);
      var fund = (+v.monthlyViews || 0) / 1000 * 0.04;
      return {
        big: ['Estimated rate per sponsored video', lo, hi],
        cells: [
          ['Engagement rate', er, er, pct],
          ['Per video', lo, hi],
          ['4 videos / month', lo * 4, hi * 4]
        ],
        bars: [
          ['Sponsored video', lo, hi],
          ['Creator Rewards', fund * 0.6, fund * 1.6],
          ['Affiliate / Shop', lo * 0.2, hi * 0.9]
        ],
        total: ['Monthly potential at 4 sponsored videos', lo * 4 + fund * 0.6, hi * 4 + fund * 1.6],
        notes: [
          'Your tier: ' + bd.tier + '. Typical engagement for this tier is ' +
            bd.lo.toFixed(1) + '%–' + bd.hi.toFixed(1) + '%. You are at ' + pct(er) + '.',
          'Engagement rate formula used: (total likes ÷ (followers × videos)) × 100.',
          'Rates scale with engagement, not follower count alone — a 20K account at 15% ER ' +
            'out-earns a 60K account at 4%.'
        ]
      };
    },

    instagram: function (v) {
      var f = +v.followers || 0, likes = +v.likes || 0, comments = +v.comments || 0;
      var er = f > 0 ? ((likes + comments) / f) * 100 : 0;
      var bd = band(B.igBands, f);
      var mid = (bd.lo + bd.hi) / 2;
      var quality = mid > 0 ? Math.min(Math.max(er / mid, 0.4), 2.2) : 1;
      var mod = (B.rateMods.niche[v.niche] || 1);
      var base = f / 1000;
      var reelLo = base * B.rateCard.instagram_reel.lo * mod * quality;
      var reelHi = base * B.rateCard.instagram_reel.hi * mod * quality;
      var postLo = base * B.rateCard.instagram_post.lo * mod * quality;
      var postHi = base * B.rateCard.instagram_post.hi * mod * quality;
      var stLo = base * B.rateCard.instagram_story.lo * mod * quality;
      var stHi = base * B.rateCard.instagram_story.hi * mod * quality;
      return {
        big: ['Your engagement rate', er, er, pct],
        cells: [
          ['Reel', reelLo, reelHi],
          ['In-feed post', postLo, postHi],
          ['Story frame', stLo, stHi]
        ],
        bars: [
          ['Reel', reelLo, reelHi],
          ['Feed post', postLo, postHi],
          ['3-frame story', stLo * 3, stHi * 3],
          ['Bundle (1 reel + 1 post + 3 stories)', reelLo + postLo + stLo * 3, reelHi + postHi + stHi * 3]
        ],
        total: ['Recommended bundle rate', (reelLo + postLo + stLo * 3) * 0.9, (reelHi + postHi + stHi * 3) * 1.05],
        notes: [
          'Your tier: ' + bd.tier + '. Benchmark engagement is ' + bd.lo.toFixed(1) + '%–' + bd.hi.toFixed(1) +
            '%. You are at ' + pct(er) + ' — that is a ×' + quality.toFixed(2) + ' rate multiplier.',
          'Engagement rate formula: (likes + comments) ÷ followers × 100.',
          'Always quote a bundle, never a single asset. Bundles close at a higher blended rate ' +
            'and stop the buyer comparing you line-by-line against cheaper accounts.'
        ]
      };
    },

    ratecard: function (v) {
      var f = +v.followers || 0;
      var asset = B.rateCard[v.asset] || B.rateCard.instagram_reel;
      var niche = B.rateMods.niche[v.niche] || 1;
      var usage = B.rateMods.usage[v.usage] || 1;
      var excl = B.rateMods.exclusivity[v.exclusivity] || 1;
      var qty = Math.max(+v.quantity || 1, 1);
      var eng = Math.min(Math.max((+v.engagement || 3) / 3, 0.5), 2.4);
      var base = (f / 1000);
      var lo = base * asset.lo * niche * usage * excl * eng * qty;
      var hi = base * asset.hi * niche * usage * excl * eng * qty;
      var bulk = qty >= 3 ? 0.88 : 1;
      return {
        big: ['Quote this deal at', lo * bulk, hi * bulk],
        cells: [
          ['Per deliverable', lo / qty, hi / qty],
          ['Full package (' + qty + ')', lo * bulk, hi * bulk],
          ['Walk-away floor', lo * bulk * 0.8, lo * bulk * 0.8]
        ],
        bars: [
          ['Base rate', base * asset.lo * qty, base * asset.hi * qty],
          ['+ Niche premium', base * asset.lo * niche * qty, base * asset.hi * niche * qty],
          ['+ Usage rights', base * asset.lo * niche * usage * qty, base * asset.hi * niche * usage * qty],
          ['+ Exclusivity', lo, hi]
        ],
        total: ['Open the negotiation here (ask high, land mid)', hi * bulk, hi * bulk * 1.15],
        notes: [
          'Multipliers applied — niche ×' + niche.toFixed(2) + ', usage rights ×' + usage.toFixed(2) +
            ', exclusivity ×' + excl.toFixed(2) + ', engagement ×' + eng.toFixed(2) +
            (qty >= 3 ? ', bulk −12%' : '') + '.',
          'Usage rights are the most under-charged line in creator deals. Perpetual paid usage ' +
            'is worth roughly double an organic-only post — never grant it inside the base fee.',
          'Send the high end. Buyers expect to negotiate 10–25% off the opening number.'
        ]
      };
    },

    cpm: function (v) {
      var imp = +v.impressions || 0, spend = +v.spend || 0, clicks = +v.clicks || 0,
          conv = +v.conversions || 0, rev = +v.revenue || 0, sessions = +v.sessions || 0,
          pageviews = +v.pageviews || 0;
      var cpm = imp ? (spend / imp) * 1000 : 0;
      var cpc = clicks ? spend / clicks : 0;
      var ctr = imp ? (clicks / imp) * 100 : 0;
      var cpa = conv ? spend / conv : 0;
      var roas = spend ? rev / spend : 0;
      var rpm = pageviews ? (rev / pageviews) * 1000 : 0;
      var ppv = sessions ? pageviews / sessions : 0;
      return {
        big: ['Page RPM', rpm, rpm],
        cells: [
          ['CPM', cpm, cpm], ['CPC', cpc, cpc], ['CTR', ctr, ctr, pct]
        ],
        bars: [],
        table: [
          ['CPM — cost per 1,000 impressions', usd(cpm)],
          ['CPC — cost per click', usd(cpc)],
          ['CTR — click-through rate', pct(ctr)],
          ['CPA — cost per acquisition', usd(cpa)],
          ['ROAS — return on ad spend', roas.toFixed(2) + '×'],
          ['RPM — revenue per 1,000 pageviews', usd(rpm)],
          ['Pages per session', ppv.toFixed(2)],
          ['Revenue per session', usd(sessions ? rev / sessions : 0)]
        ],
        total: ['Annualised revenue at this RPM', rev * 12, rev * 12],
        notes: [
          'RPM is the only number that compares a publisher to a publisher. CPM compares a buyer to a buyer.',
          'Pages per session below 1.4 means your internal linking is the cheapest revenue fix available.'
        ]
      };
    },

    podcast: function (v) {
      var dl = +v.downloads || 0, eps = Math.max(+v.episodes || 1, 1);
      var slots = { preroll: +v.preroll || 0, midroll: +v.midroll || 0, postroll: +v.postroll || 0 };
      var hostRead = v.hostread === 'yes' ? B.podcast.host_read_premium : 1;
      var lo = 0, hi = 0;
      Object.keys(slots).forEach(function (k) {
        lo += (dl / 1000) * B.podcast[k].lo * slots[k];
        hi += (dl / 1000) * B.podcast[k].hi * slots[k];
      });
      lo *= hostRead; hi *= hostRead;
      var monthlyLo = lo * eps, monthlyHi = hi * eps;
      return {
        big: ['Revenue per episode', lo, hi],
        cells: [
          ['Per episode', lo, hi],
          ['Per month (' + eps + ' eps)', monthlyLo, monthlyHi],
          ['Per year', monthlyLo * 12, monthlyHi * 12]
        ],
        bars: [
          ['Pre-roll', (dl / 1000) * B.podcast.preroll.lo * slots.preroll * hostRead, (dl / 1000) * B.podcast.preroll.hi * slots.preroll * hostRead],
          ['Mid-roll', (dl / 1000) * B.podcast.midroll.lo * slots.midroll * hostRead, (dl / 1000) * B.podcast.midroll.hi * slots.midroll * hostRead],
          ['Post-roll', (dl / 1000) * B.podcast.postroll.lo * slots.postroll * hostRead, (dl / 1000) * B.podcast.postroll.hi * slots.postroll * hostRead]
        ],
        total: ['Annual sponsorship potential', monthlyLo * 12, monthlyHi * 12],
        notes: [
          'CPMs used: pre-roll $' + B.podcast.preroll.lo + '–$' + B.podcast.preroll.hi +
            ', mid-roll $' + B.podcast.midroll.lo + '–$' + B.podcast.midroll.hi +
            ', post-roll $' + B.podcast.postroll.lo + '–$' + B.podcast.postroll.hi + ' per 1,000 downloads.',
          'Host-read spots carry a ' + Math.round((B.podcast.host_read_premium - 1) * 100) + '% premium over produced spots.',
          'Downloads are counted in the first 30 days (IAB v2.1). Anything else is not sellable inventory.'
        ]
      };
    },

    newsletter: function (v) {
      var subs = +v.subscribers || 0;
      var open = (+v.openrate || 42) / 100;
      var opens = subs * open;
      var type = v.slot || 'primary';
      var t = B.newsletter[type] || B.newsletter.primary;
      var b2b = v.audience === 'b2b' ? B.newsletter.b2bPremium : 1;
      var lo = (opens / 1000) * t.lo * b2b, hi = (opens / 1000) * t.hi * b2b;
      var issues = Math.max(+v.issues || 4, 1);
      return {
        big: ['Rate per sponsored slot', lo, hi],
        cells: [
          ['Per issue', lo, hi],
          ['Per month (' + issues + ')', lo * issues, hi * issues],
          ['Per year', lo * issues * 12, hi * issues * 12]
        ],
        bars: [
          ['Classified', (opens / 1000) * B.newsletter.classified.lo * b2b, (opens / 1000) * B.newsletter.classified.hi * b2b],
          ['Primary slot', (opens / 1000) * B.newsletter.primary.lo * b2b, (opens / 1000) * B.newsletter.primary.hi * b2b],
          ['Dedicated send', (opens / 1000) * B.newsletter.dedicated.lo * b2b, (opens / 1000) * B.newsletter.dedicated.hi * b2b]
        ],
        total: ['Annual newsletter revenue ceiling', lo * issues * 12, hi * issues * 12],
        notes: [
          'Priced on opens (' + num(opens) + '), never on list size. Selling on sends is how newsletters get churned by advertisers.',
          v.audience === 'b2b' ? 'B2B decision-maker audiences carry a ×' + B.newsletter.b2bPremium + ' premium.'
            : 'A B2B or decision-maker audience would raise these numbers by ~80%.',
          'Publish a media kit with subscribers, open rate, click rate and audience mix. Gating it captures the advertiser as a lead.'
        ]
      };
    },

    roi: function (v) {
      var pieces = +v.pieces || 0, cost = +v.cost || 0, months = Math.max(+v.months || 12, 1);
      var vol = +v.searchvol || 0, rank = v.rank || 'top3';
      var value = +v.dealvalue || 0, close = (+v.closerate || 14) / 100;
      var ctr = rank === 'top3' ? B.funnel.ctrTop3 : B.funnel.ctr4to10;
      var visitors = pieces * vol * ctr;
      var leads = visitors * B.funnel.visitorToLead;
      var customers = leads * close;
      var revenue = customers * value;
      var spend = pieces * cost;
      var adsenseLo = (visitors / 1000) * 18, adsenseHi = (visitors / 1000) * 42;
      var roiLo = spend ? ((revenue + adsenseLo * months - spend) / spend) * 100 : 0;
      var roiHi = spend ? ((revenue * 1.4 + adsenseHi * months - spend) / spend) * 100 : 0;
      return {
        big: ['Projected monthly pipeline value', revenue, revenue * 1.4],
        cells: [
          ['Monthly organic visitors', visitors, visitors, num],
          ['Monthly leads', leads, leads, num],
          ['Monthly customers', customers, customers, function (n) { return n.toFixed(1); }]
        ],
        bars: [
          ['Pipeline revenue', revenue, revenue * 1.4],
          ['Display ad revenue', adsenseLo, adsenseHi],
          ['Content investment', spend / months, spend / months]
        ],
        table: [
          ['Total content investment', usd(spend)],
          ['Payback period', spend && revenue ? (spend / Math.max(revenue, 1)).toFixed(1) + ' months' : '—'],
          ['12-month return', rng(roiLo, roiHi, function (n) { return n.toFixed(0) + '%'; })],
          ['Cost per lead', leads ? usd(spend / (leads * months)) : '—'],
          ['Cost per customer', customers ? usd(spend / (customers * months)) : '—']
        ],
        total: ['12-month combined return on this content programme', roiLo, roiHi, function (n) { return n.toFixed(0) + '%'; }],
        notes: [
          'Assumptions published: top-3 CTR ' + (B.funnel.ctrTop3 * 100).toFixed(0) + '%, positions 4–10 CTR ' +
            (B.funnel.ctr4to10 * 100).toFixed(0) + '%, visitor→lead ' + (B.funnel.visitorToLead * 100).toFixed(1) +
            '%, lead→customer ' + (close * 100).toFixed(0) + '%.',
          'Display revenue assumes an $18–$42 page RPM, which is the marketing/business band for tier-1 traffic.',
          'Content compounds. This model is deliberately flat — real programmes accelerate after month 7.'
        ]
      };
    },

    growth: function (v) {
      var subs = +v.subs || 0, rate = (+v.growth || 6) / 100, months = +v.horizon || 12;
      var viewsPerSub = +v.viewsper || 2.2;
      var n = find(B.niches, v.niche), g = find(B.geo, v.geo);
      var series = [], s = subs;
      for (var i = 1; i <= months; i++) { s = s * (1 + rate); series.push(s); }
      var end = series[series.length - 1] || subs;
      var viewsEnd = end * viewsPerSub;
      var lo = (viewsEnd * B.monetisedShare.lo / 1000) * n.rpmLo * g.mult;
      var hi = (viewsEnd * B.monetisedShare.hi / 1000) * n.rpmHi * g.mult;
      return {
        big: ['Projected monthly revenue in month ' + months, lo, hi],
        cells: [
          ['Subscribers in ' + months + ' mo', end, end, num],
          ['Monthly views then', viewsEnd, viewsEnd, num],
          ['Added subscribers', end - subs, end - subs, num]
        ],
        bars: series.filter(function (_, i) { return i % Math.max(Math.floor(months / 6), 1) === 0; })
          .map(function (val, i) { return ['Month ' + ((i * Math.max(Math.floor(months / 6), 1)) + 1), val, val]; }),
        barFormat: num,
        total: ['Cumulative revenue over ' + months + ' months',
          series.reduce(function (a, x) { return a + (x * viewsPerSub * B.monetisedShare.lo / 1000) * n.rpmLo * g.mult; }, 0),
          series.reduce(function (a, x) { return a + (x * viewsPerSub * B.monetisedShare.hi / 1000) * n.rpmHi * g.mult; }, 0)],
        notes: [
          'Compounding at ' + (rate * 100).toFixed(1) + '% per month. Sustained monthly growth above 10% is rare beyond 100K subscribers.',
          'Views-per-subscriber is the honest health metric: above 2.0 means the audience still shows up. Below 0.8 means a dead list.',
          'Revenue modelled on ' + n.label + ' RPM with a ×' + g.mult.toFixed(2) + ' geography factor.'
        ]
      };
    }
  };

  /* ------------------------------------------------------------ runtime */
  function readInputs(root) {
    var v = {};
    $$('[name]', root).forEach(function (el) {
      if (el.type === 'radio') { if (el.checked) v[el.name] = el.value; }
      else if (el.type === 'checkbox') { v[el.name] = el.checked ? el.value : ''; }
      else v[el.name] = el.value;
    });
    return v;
  }

  function paint(root, r) {
    var out = $('[data-out]', root);
    if (!out) return;
    var bigFmt = r.big[3] || usd;
    var html = '<p class="result-label">' + r.big[0] + '</p>' +
      '<p class="result-big">' + (Math.abs(r.big[1] - r.big[2]) < 0.005
        ? bigFmt(r.big[1]) : bigFmt(r.big[1]) + ' – ' + bigFmt(r.big[2])) + '</p>';

    if (r.cells && r.cells.length) {
      html += '<div class="result-grid">' + r.cells.map(function (c) {
        var f = c[3] || usd;
        return '<div class="result-cell"><b>' + (Math.abs(c[1] - c[2]) < 0.005 ? f(c[1]) : f(c[1]) + '–' + f(c[2])) +
          '</b><span>' + c[0] + '</span></div>';
      }).join('') + '</div>';
    }

    if (r.bars && r.bars.length) {
      var max = Math.max.apply(null, r.bars.map(function (b) { return b[2]; }).concat([1]));
      var bf = r.barFormat || usd;
      html += '<div class="bars">' + r.bars.map(function (b) {
        return '<div class="bar-row"><span>' + b[0] + '</span>' +
          '<span class="bar-track"><span class="bar-fill" style="width:' +
          Math.max((b[2] / max) * 100, 2).toFixed(1) + '%"></span></span>' +
          '<span>' + (Math.abs(b[1] - b[2]) < 0.005 ? bf(b[1]) : bf(b[1]) + '–' + bf(b[2])) + '</span></div>';
      }).join('') + '</div>';
    }

    if (r.table && r.table.length) {
      html += '<table class="mini-table"><tbody>' + r.table.map(function (t) {
        return '<tr><td>' + t[0] + '</td><td style="text-align:right;font-weight:700">' + t[1] + '</td></tr>';
      }).join('') + '</tbody></table>';
    }

    if (r.total) {
      var tf = r.total[3] || usd;
      html += '<div class="callout" style="margin-top:1.1rem"><h4>' + r.total[0] + '</h4><p class="result-big" ' +
        'style="font-size:1.55rem">' + (Math.abs(r.total[1] - r.total[2]) < 0.005
          ? tf(r.total[1]) : tf(r.total[1]) + ' – ' + tf(r.total[2])) + '</p></div>';
    }

    if (r.notes && r.notes.length) {
      html += '<div class="assumptions"><h4>Assumptions used</h4><ul>' +
        r.notes.map(function (n) { return '<li>' + n + '</li>'; }).join('') + '</ul></div>';
    }
    out.innerHTML = html;
  }

  $$('.calc[data-calc]').forEach(function (root) {
    var engine = ENGINES[root.dataset.calc];
    if (!engine) return;
    function run() {
      $$('output.val', root).forEach(function (o) {
        var src = $('[name="' + o.dataset.for + '"]', root);
        if (src) o.textContent = (o.dataset.prefix || '') +
          (+src.value).toLocaleString('en-US') + (o.dataset.suffix || '');
      });
      try { paint(root, engine(readInputs(root))); } catch (e) { /* keep the page alive */ }
    }
    root.addEventListener('input', run);
    root.addEventListener('change', run);
    $$('[data-reset]', root).forEach(function (b) {
      b.addEventListener('click', function () {
        $$('input,select', root).forEach(function (el) {
          if (el.dataset.def !== undefined) el.value = el.dataset.def;
        });
        run();
      });
    });
    run();
  });
})();
