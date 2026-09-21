# -*- coding: utf-8 -*-
"""Reusable UI blocks shared by every page."""
import json
from config import SITE, PROOF, SUBS_LINE


def breadcrumbs(trail):
    """trail = [(label, href), ... ] last item is current page."""
    items, ld = [], []
    for i, (label, href) in enumerate(trail):
        last = i == len(trail) - 1
        items.append(
            f'<li aria-current="page"><span>{label}</span></li>' if last
            else f'<li><a href="{href}">{label}</a></li>'
        )
        ld.append({"@type": "ListItem", "position": i + 1, "name": label,
                   "item": SITE["base_url"] + href})
    schema = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": ld}
    return (f'<nav class="crumbs" aria-label="Breadcrumb"><ol>{"".join(items)}</ol></nav>'
            f'<script type="application/ld+json">{json.dumps(schema, separators=(",", ":"))}</script>')


def section_head(eyebrow, title, sub="", href=None, link_label="View all"):
    link = f'<a class="sec-link" href="{href}">{link_label} &rarr;</a>' if href else ""
    subp = f'<p class="sec-sub">{sub}</p>' if sub else ""
    return f'''<div class="sec-head">
  <div><span class="eyebrow">{eyebrow}</span><h2>{title}</h2>{subp}</div>{link}
</div>'''


def stat_row(stats):
    """stats = [(value, label, note)]"""
    cells = "".join(
        f'<div class="stat"><span class="stat-v">{v}</span><span class="stat-l">{l}</span>'
        f'{f"<span class=stat-n>{n}</span>" if n else ""}</div>'
        for v, l, n in stats
    )
    return f'<div class="stat-row">{cells}</div>'


def faq(items, heading="Frequently asked questions"):
    """items = [(question, answer_html)] — renders accordion + FAQPage schema."""
    rows = "".join(
        f'<details class="faq-item"{" open" if i == 0 else ""}>'
        f'<summary><span>{q}</span><span class="faq-plus" aria-hidden="true"></span></summary>'
        f'<div class="faq-body">{a}</div></details>'
        for i, (q, a) in enumerate(items)
    )
    schema = {
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": _strip(a)}}
            for q, a in items
        ],
    }
    return (f'<section class="faq" id="faq"><h2>{heading}</h2><div class="faq-list">{rows}</div>'
            f'<script type="application/ld+json">{json.dumps(schema, separators=(",", ":"))}</script></section>')


def _strip(html):
    import re
    return re.sub(r"<[^>]+>", "", html).strip()


def helpful_poll(topic):
    return f'''<div class="poll" data-poll="{topic}">
  <span>Did this page solve your problem?</span>
  <div class="poll-btns">
    <button type="button" data-v="yes">Yes</button>
    <button type="button" data-v="no">No</button>
  </div>
  <p class="poll-thanks" hidden>Thanks — noted. <a href="/contact/">Tell us what was missing</a>.</p>
</div>'''


def byline(author="The Content.Media research desk", reviewer="Editorial board",
           updated="September 2026"):
    return f'''<div class="byline">
  <div class="byline-av" aria-hidden="true">CM</div>
  <div>
    <p class="byline-name">{author}</p>
    <p class="byline-meta">Reviewed by {reviewer} &middot; Updated {updated} &middot;
    <a href="/editorial-policy/">How we research</a></p>
  </div>
</div>'''


def cta_band(title, sub, primary=("Get my content plan", "/services/#quote"),
             secondary=("See what we charge", "/services/#pricing")):
    return f'''<section class="cta-band">
  <div class="wrap cta-band__inner">
    <div>
      <h2>{title}</h2>
      <p>{sub}</p>
    </div>
    <div class="cta-band__actions">
      <a class="btn btn--primary btn--lg" href="{primary[1]}">{primary[0]}</a>
      <a class="btn btn--ghost btn--lg" href="{secondary[1]}">{secondary[0]}</a>
    </div>
  </div>
</section>'''


def newsletter_block(variant="wide", heading=None, sub=None, magnet=True):
    heading = heading or "The weekly Content.Media brief"
    sub = sub or (
        "Benchmarks, rate changes and platform payout shifts — decoded in five minutes. "
        + SUBS_LINE
    )
    bonus = (
        '<ul class="magnet-list">'
        '<li>The <strong>2026 benchmark dataset</strong> as a CSV — '
        '<a href="/assets/data/creator-benchmarks-2026.csv" download>download it now, no signup</a></li>'
        '<li>Every back issue, from the first one</li>'
        '<li>Reader discount codes when tools offer them</li>'
        '<li>First look at contests and prize drops</li>'
        '</ul>' if magnet else ""
    )
    return f'''<section class="newsletter newsletter--{variant}" id="newsletter">
  <div class="newsletter__copy">
    <span class="eyebrow">Free weekly</span>
    <h2>{heading}</h2>
    <p>{sub}</p>
    {bonus}
  </div>
  <form class="cm-form newsletter__form" data-form="newsletter" novalidate>
    <label class="sr-only" for="nl-email-{variant}">Email address</label>
    <input id="nl-email-{variant}" name="email" type="email" required
           placeholder="you@company.com" autocomplete="email">
    <label class="sr-only" for="nl-role-{variant}">I am a…</label>
    <select id="nl-role-{variant}" name="role" required>
      <option value="">I am a…</option>
      <option>Creator / channel owner</option>
      <option>Publisher / media owner</option>
      <option>Brand or in-house marketer</option>
      <option>Agency / freelancer</option>
      <option>Investor / analyst</option>
    </select>
    <button class="btn btn--primary btn--block" type="submit">Send me the brief</button>
    <label class="checkline">
      <input type="checkbox" name="consent" value="yes" required>
      <span>Email me the weekly brief and the rate card database. I can unsubscribe any time.</span>
    </label>
    <div class="form-status" role="status" aria-live="polite"></div>
  </form>
</section>'''


# ---------------------------------------------------------------------------
# The money page: 4-step qualified lead form
# ---------------------------------------------------------------------------
LEAD_STEPS = [
    {
        "title": "What do you need built?",
        "hint": "Takes about 45 seconds. No PII on this step, and no sales call required to get a number.",
        "fields": [
            {"name": "service", "label": "What kind of content work are you hiring for?",
             "type": "cards", "required": True, "options": [
                 ("Video production", "YouTube, brand film, explainer"),
                 ("Short-form social", "Reels, Shorts, TikTok at volume"),
                 ("Podcast production", "Recording, edit, clips, distribution"),
                 ("Written content & SEO", "Articles, landing pages, programmatic"),
                 ("Full-service content retainer", "Strategy plus production"),
                 ("Not sure yet", "Help me scope it"),
             ]},
        ],
    },
    {
        "title": "How much, and how soon?",
        "hint": "Rough answers are fine — we refine them on the plan.",
        "fields": [
            {"name": "volume", "label": "Output you need each month", "type": "select",
             "required": True, "options": [
                 "1–2 pieces", "3–8 pieces", "9–20 pieces", "20+ pieces", "One-off project"]},
            {"name": "timeline", "label": "When do you want to start?", "type": "select",
             "required": True, "options": [
                 "ASAP — this month", "Next 30–60 days", "Next quarter", "Just researching"]},
            {"name": "goal", "label": "Primary goal", "type": "select", "required": True,
             "options": ["Pipeline / qualified leads", "Organic search traffic",
                         "Audience & subscriber growth", "Brand awareness",
                         "Ad revenue from owned media", "Product launch"]},
        ],
    },
    {
        "title": "Is this a fit?",
        "hint": "We work best from $2,500/month. Below that we will send you our DIY playbook "
                "free instead of wasting your time.",
        "fields": [
            {"name": "budget", "label": "Monthly budget for content", "type": "select",
             "required": True, "options": [
                 "Under $2,500", "$2,500–$5,000", "$5,000–$10,000",
                 "$10,000–$25,000", "$25,000+", "Not sure yet"]},
            {"name": "company_size", "label": "Company size", "type": "select", "required": True,
             "options": ["Just me", "2–10", "11–50", "51–200", "200+"]},
            {"name": "industry", "label": "Industry", "type": "select", "required": False,
             "options": ["SaaS / software", "Finance & fintech", "Health & wellness",
                         "E-commerce / DTC", "Education", "Real estate", "Travel",
                         "Gaming", "Professional services", "Media & publishing", "Other"]},
        ],
    },
    {
        "title": "Where do we send the plan?",
        "hint": "We email your costed plan within one business day. No spam, and we never resell your details.",
        "fields": [
            {"name": "name", "label": "Full name", "type": "text", "required": True,
             "placeholder": "Alex Moreau", "autocomplete": "name"},
            {"name": "email", "label": "Work email", "type": "email", "required": True,
             "placeholder": "you@company.com", "autocomplete": "email"},
            {"name": "company", "label": "Company", "type": "text", "required": True,
             "placeholder": "Company name", "autocomplete": "organization"},
            {"name": "url", "label": "Website or channel URL", "type": "url", "required": True,
             "placeholder": "https://", "autocomplete": "url"},
            {"name": "phone", "label": "Phone (optional)", "type": "tel", "required": False,
             "placeholder": "+1", "autocomplete": "tel"},
            {"name": "notes", "label": "Anything we should know? (optional)", "type": "textarea",
             "required": False, "placeholder": "Links, deadlines, constraints…"},
        ],
    },
]


def _field(f, step_i):
    req = " required" if f.get("required") else ""
    fid = f"lf-{f['name']}"
    star = ' <span class="req" aria-hidden="true">*</span>' if f.get("required") else ""
    if f["type"] == "cards":
        opts = "".join(
            f'<label class="choice"><input type="radio" name="{f["name"]}" value="{o}"{req}>'
            f'<span class="choice-box"><strong>{o}</strong><em>{d}</em></span></label>'
            for o, d in f["options"]
        )
        return (f'<fieldset class="field"><legend>{f["label"]}{star}</legend>'
                f'<div class="choice-grid">{opts}</div></fieldset>')
    if f["type"] == "select":
        opts = "".join(f"<option>{o}</option>" for o in f["options"])
        return (f'<div class="field"><label for="{fid}">{f["label"]}{star}</label>'
                f'<select id="{fid}" name="{f["name"]}"{req}>'
                f'<option value="">Choose one…</option>{opts}</select></div>')
    if f["type"] == "textarea":
        return (f'<div class="field"><label for="{fid}">{f["label"]}</label>'
                f'<textarea id="{fid}" name="{f["name"]}" rows="3" '
                f'placeholder="{f.get("placeholder", "")}"></textarea></div>')
    return (f'<div class="field"><label for="{fid}">{f["label"]}{star}</label>'
            f'<input id="{fid}" name="{f["name"]}" type="{f["type"]}"{req} '
            f'placeholder="{f.get("placeholder", "")}" '
            f'autocomplete="{f.get("autocomplete", "on")}"></div>')


def lead_form():
    steps_html = []
    for i, s in enumerate(LEAD_STEPS):
        fields = "".join(_field(f, i) for f in s["fields"])
        nav = []
        if i > 0:
            nav.append('<button type="button" class="btn btn--ghost" data-step-back>Back</button>')
        if i < len(LEAD_STEPS) - 1:
            nav.append('<button type="button" class="btn btn--primary" data-step-next>Continue</button>')
        else:
            nav.append('<button type="submit" class="btn btn--primary btn--lg">'
                       'Send my custom content plan</button>')
        steps_html.append(
            f'<div class="step" data-step="{i}"{"" if i == 0 else " hidden"}>'
            f'<p class="step-count">Step {i+1} of {len(LEAD_STEPS)}'
            f'{" — last question" if i == len(LEAD_STEPS)-1 else ""}</p>'
            f'<h3>{s["title"]}</h3><p class="step-hint">{s["hint"]}</p>'
            f'{fields}<div class="step-nav">{"".join(nav)}</div></div>'
        )
    dots = "".join(f'<span class="dot{" is-on" if i == 0 else ""}"></span>'
                   for i in range(len(LEAD_STEPS)))
    return f'''<div class="leadform-shell" id="quote">
  <div class="leadform-side">
    <span class="eyebrow">Free, no obligation</span>
    <h2>Get a costed content plan in one business day</h2>
    <p>Tell us what you need. We come back with scope, a monthly number, a sample calendar and
    the projected traffic and revenue — built on the same benchmark data published on this site.</p>
    <ul class="ticks">
      <li>A real number, not "contact us for pricing"</li>
      <li>Scope, deliverables and a 90-day calendar</li>
      <li>Forecast traffic, RPM and pipeline impact</li>
      <li>Under $2,500/month? You get our DIY playbook free instead</li>
    </ul>
    <div class="side-proof">
      <div><strong>{PROOF['niches']}</strong><span>niches benchmarked</span></div>
      <div><strong>{PROOF['tools_indexed']}</strong><span>tools reviewed</span></div>
      <div><strong>1 day</strong><span>turnaround on every plan</span></div>
    </div>
  </div>
  <form class="cm-form leadform" data-form="lead" novalidate>
    <div class="progress"><div class="progress-bar" style="width:25%"></div></div>
    <div class="dots">{dots}</div>
    {''.join(steps_html)}
    <p class="legal-note">By sending this you agree to our <a href="/terms/">terms</a> and
    <a href="/privacy/">privacy policy</a>. We reply from a monitored inbox and never sell your data.</p>
    <div class="form-status" role="status" aria-live="polite"></div>
  </form>
</div>'''


def simple_form(form_id, title, fields, button="Send", note="", compact=False):
    """fields = list of dicts like LEAD_STEPS fields."""
    body = "".join(_field(f, 0) for f in fields)
    note_html = f'<p class="microcopy">{note}</p>' if note else ""
    return f'''<form class="cm-form panel{' panel--compact' if compact else ''}" data-form="{form_id}" novalidate>
  <h3>{title}</h3>
  {body}
  <button class="btn btn--primary btn--block btn--lg" type="submit">{button}</button>
  {note_html}
  <div class="form-status" role="status" aria-live="polite"></div>
</form>'''


def mail_link(label, subject="Content.Media enquiry", cls="maillink"):
    """Renders a link whose href is built in the browser — no address in the HTML."""
    return (f'<a class="{cls}" href="/contact/" data-mail="1" '
            f'data-subject="{subject}">{label}</a>')


def toc(items):
    lis = "".join(f'<li><a href="#{i}">{t}</a></li>' for i, t in items)
    return f'<nav class="toc" aria-label="On this page"><p>On this page</p><ul>{lis}</ul></nav>'
