# -*- coding: utf-8 -*-
"""Page shell: head, global contact bar, header, footer, ad units."""
import json
from config import SITE, NAV, FOOTER, ADS, ANALYTICS, CONTACT_TOKEN, CONTACT_KEY, \
    FORM_GATEWAY, FORM_ALIAS, PROOF, SUBS_LINE

LOGO = (
    '<a class="brand" href="/" aria-label="Content.Media home">'
    '<span class="brand-mark" aria-hidden="true">'
    '<svg viewBox="0 0 32 32" width="30" height="30" role="presentation">'
    '<rect x="1" y="1" width="30" height="30" rx="9" fill="url(#bg)"/>'
    '<path d="M12.5 10.2v11.6l9.4-5.8z" fill="#fff"/>'
    '<defs><linearGradient id="bg" x1="0" y1="0" x2="32" y2="32">'
    '<stop stop-color="#4f46e5"/><stop offset="1" stop-color="#db2777"/>'
    '</linearGradient></defs></svg></span>'
    '<span class="brand-text">Content<span class="brand-dot">.</span>Media</span></a>'
)


def ad(slot="in_article", label="Advertisement", style="in-article"):
    """Render an AdSense unit placeholder that becomes live once IDs are set."""
    if not ADS["enabled"]:
        return ""
    # Until a real publisher ID is set, render nothing visible: an empty
    # reserved box looks broken and, worse, AdSense treats pages built around
    # blank inventory as low-value.
    if ADS["publisher"].endswith("0000000000000000"):
        return f"<!-- ad slot: {slot} ({style}) — set ADS['publisher'] in _src/config.py -->"
    slot_id = ADS["slots"].get(slot, ADS["slots"]["in_article"])
    fmt = {
        "leaderboard": ('data-ad-format="auto" data-full-width-responsive="true"', "display:block"),
        "in-article": ('data-ad-layout="in-article" data-ad-format="fluid"', "display:block;text-align:center"),
        "sidebar": ('data-ad-format="auto" data-full-width-responsive="true"', "display:block"),
    }.get(style, ('data-ad-format="auto"', "display:block"))
    return f'''<aside class="ad ad--{style}" role="complementary" aria-label="{label}">
  <span class="ad-label">{label}</span>
  <ins class="adsbygoogle" style="{fmt[1]}" data-ad-client="{ADS['publisher']}"
       data-ad-slot="{slot_id}" {fmt[0]}></ins>
  <script>(adsbygoogle = window.adsbygoogle || []).push({{}});</script>
</aside>'''


def _nav_html(active):
    out = []
    for item in NAV:
        cls = "nav-link"
        if item.get("cta"):
            cls += " nav-link--cta"
        if active and item["href"].strip("/") and active.startswith(item["href"].strip("/")):
            cls += " is-active"
        if item.get("children"):
            kids = "".join(
                f'<li><a href="{c["href"]}">{c["label"]}</a></li>' for c in item["children"]
            )
            out.append(
                f'<li class="has-sub"><a class="{cls}" href="{item["href"]}" '
                f'aria-haspopup="true" aria-expanded="false">{item["label"]}'
                f'<svg class="caret" width="10" height="10" viewBox="0 0 10 10" aria-hidden="true">'
                f'<path d="M1 3l4 4 4-4" stroke="currentColor" stroke-width="1.6" fill="none" '
                f'stroke-linecap="round"/></svg></a>'
                f'<ul class="subnav">{kids}</ul></li>'
            )
        else:
            out.append(f'<li><a class="{cls}" href="{item["href"]}">{item["label"]}</a></li>')
    return "".join(out)


def _footer_html():
    cols = []
    for title, links in FOOTER:
        items = "".join(f'<li><a href="{h}">{t}</a></li>' for t, h in links)
        cols.append(f'<div class="foot-col"><h3>{title}</h3><ul>{items}</ul></div>')
    year = 2026
    return f'''<footer class="site-footer" id="footer">
  <div class="wrap">
    <div class="foot-top">
      <div class="foot-brand">
        {LOGO}
        <p class="foot-pitch">Independent research, free tools and honest benchmarks for the
        people who make content for a living. No paywall. No investor telling us what to publish.</p>
        <form class="cm-form foot-sub" data-form="newsletter-footer" novalidate>
          <label class="sr-only" for="foot-email">Email address</label>
          <div class="inline-field">
            <input id="foot-email" name="email" type="email" required placeholder="you@company.com" autocomplete="email">
            <button class="btn btn--primary" type="submit">Get the weekly brief</button>
          </div>
          <p class="microcopy">{SUBS_LINE}</p>
          <div class="form-status" role="status" aria-live="polite"></div>
        </form>
        <div class="foot-social">
          <a href="{SITE['youtube_channel']}" rel="noopener" target="_blank" aria-label="YouTube">YouTube</a>
          <a href="/videos/">Video library</a>
          <a href="/support/">Support us</a>
          <a href="/contact/">Contact</a>
        </div>
      </div>
      <nav class="foot-cols" aria-label="Footer">{''.join(cols)}</nav>
    </div>
    <div class="foot-bottom">
      <p>&copy; {year} {SITE['name']}. Published independently. Figures on this site are
      estimates — read our <a href="/editorial-policy/">editorial policy</a> and
      <a href="/disclosure/">disclosure</a>.</p>
      <p class="foot-domain"><a href="{SITE['owner_contact_url']}" rel="noopener" target="_blank">
      This domain and website may be available &rarr;</a></p>
    </div>
  </div>
</footer>'''


def _head(title, description, canonical, schema, extra_head, image):
    ads_script = (
        f'<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js'
        f'?client={ADS["publisher"]}" crossorigin="anonymous"></script>'
        if ADS["enabled"] else ""
    )
    ga = ""
    if ANALYTICS["ga4_id"]:
        ga = (f'<script async src="https://www.googletagmanager.com/gtag/js?id={ANALYTICS["ga4_id"]}"></script>'
              f'<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}'
              f'gtag("js",new Date());gtag("config","{ANALYTICS["ga4_id"]}");</script>')
    schema_html = ""
    if schema:
        blocks = schema if isinstance(schema, list) else [schema]
        schema_html = "".join(
            f'<script type="application/ld+json">{json.dumps(b, separators=(",", ":"))}</script>'
            for b in blocks
        )
    full = f"{SITE['base_url']}{canonical}"
    og_image = image or f"{SITE['base_url']}/assets/img/og-default.svg"
    return f'''<!doctype html>
<html lang="en" data-theme="auto">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{full}">
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{SITE['name']}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{full}">
<meta property="og:image" content="{og_image}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="{SITE['twitter']}">
<meta name="theme-color" content="#0b0d17" media="(prefers-color-scheme: dark)">
<meta name="theme-color" content="#ffffff" media="(prefers-color-scheme: light)">
<link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/assets/img/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500&display=swap">
<link rel="stylesheet" href="/assets/css/site.css">
<link rel="sitemap" type="application/xml" href="/sitemap.xml">
<link rel="alternate" type="application/rss+xml" title="{SITE['name']}" href="/feed.xml">
<script>
  window.CM = {{
    t: "{CONTACT_TOKEN}", k: {CONTACT_KEY},
    gw: "{FORM_GATEWAY}", alias: "{FORM_ALIAS}", base: ""
  }};
  (function(){{try{{var s=localStorage.getItem('cm-theme');
   if(s){{document.documentElement.setAttribute('data-theme',s);}}}}catch(e){{}}}})();
</script>
{schema_html}{ads_script}{ga}{extra_head}
</head>'''


JEKYLL = {"on": False}


def _schema_html(schema):
    if not schema:
        return ""
    blocks = schema if isinstance(schema, list) else [schema]
    return "".join(
        f'<script type="application/ld+json">{json.dumps(b, separators=(",", ":"))}</script>'
        for b in blocks)


def page(title, description, canonical, body, active="", schema=None,
         extra_head="", extra_body="", image=None, wide=False):
    """Assemble a complete HTML document — or, in Jekyll mode, a page with
    front matter whose shell comes from _layouts/default.html."""
    if JEKYLL["on"]:
        fm = {
            "layout": "default",
            "title": title,
            "description": description,
            "canonical": canonical,
            "head_extra": _schema_html(schema) + extra_head,
            # calc/directory/benchmark scripts are loaded by the shared layout
            # on every page (each no-ops when its widget is absent), so the
            # base path is applied to them by Liquid.
            "body_extra": "",
        }
        front = "---\n" + "".join(f"{k}: {json.dumps(v, ensure_ascii=False)}\n" for k, v in fm.items()) + "---\n"
        return front + "{% raw %}" + body + "{% endraw %}\n"
    head = _head(title, description, canonical, schema, extra_head, image)
    return f'''{head}
<body class="{'wide' if wide else ''}">
<a class="skip" href="#main">Skip to content</a>

<!-- Global domain-enquiry bar: present at the top of every page -->
<div class="domain-bar" role="region" aria-label="Domain enquiry">
  <div class="wrap domain-bar__inner">
    <a class="domain-bar__link" href="{SITE['owner_contact_url']}" rel="noopener" target="_blank">
      <span class="domain-bar__dot" aria-hidden="true"></span>
      <strong>Contact, if you are interested in this website/domain name</strong>
      <span class="domain-bar__arrow" aria-hidden="true">&rarr;</span>
    </a>
  </div>
</div>

<header class="site-header" id="siteHeader">
  <div class="wrap header-inner">
    {LOGO}
    <nav class="mainnav" aria-label="Main">
      <ul>{_nav_html(active)}</ul>
    </nav>
    <div class="header-actions">
      <button class="icon-btn" id="searchOpen" aria-label="Search the site" title="Search (press /)">
        <svg width="18" height="18" viewBox="0 0 20 20" fill="none" aria-hidden="true">
          <circle cx="9" cy="9" r="6" stroke="currentColor" stroke-width="2"/>
          <path d="M13.5 13.5L18 18" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
        </svg>
      </button>
      <button class="icon-btn" id="themeToggle" aria-label="Switch colour theme" title="Theme">
        <svg width="18" height="18" viewBox="0 0 20 20" fill="none" aria-hidden="true">
          <path d="M16 11.5A6.5 6.5 0 018.5 4a6.5 6.5 0 107.5 7.5z" stroke="currentColor" stroke-width="1.8"
                stroke-linejoin="round"/>
        </svg>
      </button>
      <a class="btn btn--ghost hide-sm hide-md" href="/support/">Support us</a>
      <a class="btn btn--primary hide-sm" href="/services/#quote">Get a content plan</a>
      <button class="burger" id="burger" aria-label="Open menu" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
  <div class="scroll-progress" id="scrollProgress" aria-hidden="true"></div>
</header>

<div class="mobile-menu" id="mobileMenu" hidden>
  <nav aria-label="Mobile"><ul>{_nav_html(active)}</ul></nav>
  <div class="mobile-menu__cta">
    <a class="btn btn--primary btn--block" href="/services/#quote">Get a content plan</a>
    <a class="btn btn--ghost btn--block" href="/support/">Support the site</a>
  </div>
</div>

<div class="search-modal" id="searchModal" hidden role="dialog" aria-modal="true" aria-label="Site search">
  <div class="search-modal__panel">
    <div class="search-modal__bar">
      <svg width="18" height="18" viewBox="0 0 20 20" fill="none" aria-hidden="true">
        <circle cx="9" cy="9" r="6" stroke="currentColor" stroke-width="2"/>
        <path d="M13.5 13.5L18 18" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
      <input id="searchInput" type="search" placeholder="Search tools, guides, benchmarks…" autocomplete="off">
      <kbd>Esc</kbd>
    </div>
    <ul class="search-results" id="searchResults"></ul>
  </div>
</div>

<main id="main">{body}</main>

<div class="sticky-cta" id="stickyCta" hidden>
  <div class="wrap sticky-cta__inner">
    <p><strong>Want this done for you?</strong> Get a costed content plan in one business day.</p>
    <div class="sticky-cta__actions">
      <a class="btn btn--primary" href="/services/#quote">Get my plan</a>
      <button class="icon-btn" id="stickyClose" aria-label="Dismiss">&times;</button>
    </div>
  </div>
</div>

{_footer_html()}
<script src="/assets/js/site.js" defer></script>
{extra_body}
</body>
</html>'''
