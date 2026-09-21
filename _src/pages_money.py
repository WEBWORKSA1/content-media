# -*- coding: utf-8 -*-
"""Revenue surfaces: directory, services, advertise, support, contests, newsletter."""
from config import SITE, PROOF, DONATE, AUDIENCE, metric
from layout import page, ad
from components import (breadcrumbs, section_head, faq, cta_band, newsletter_block,
                        lead_form, simple_form, helpful_poll, byline, mail_link)


# ---------------------------------------------------------------------------
# Directory
# ---------------------------------------------------------------------------
def build_directory():
    body = f'''<section class="band" style="padding-bottom:1.2rem">
  <div class="wrap">
    {breadcrumbs([("Home", "/"), ("Tool directory", "/directory/")])}
    <h1>The content &amp; AI tool directory</h1>
    <p class="lede">Every listing carries an editor note that says what the tool is actually bad at.
    Nobody can buy a rating, an editor score or a ranking — featured slots are labelled as featured
    everywhere they appear. Some outbound links are affiliate links;
    see our <a href="/disclosure/">disclosure</a>.</p>
    {ad("leaderboard", style="leaderboard")}
  </div>
</section>
<section class="band" style="padding-top:0">
  <div class="wrap dir-layout" id="dirApp">
    <aside>
      <div class="filters">
        <div class="dir-toolbar" style="margin-bottom:.8rem">
          <button class="chip" id="dirClear" type="button">Clear all filters</button>
        </div>
        <div id="dirFacets"></div>
      </div>
    </aside>
    <div>
      <div class="dir-toolbar">
        <input type="search" id="dirSearch" placeholder="Search the directory — try “captions” or “analytics”…"
               aria-label="Search the directory">
        <select id="dirSort" aria-label="Sort results">
          <option value="trending">Sort: Trending</option>
          <option value="popular">Most popular</option>
          <option value="rated">Highest rated</option>
          <option value="editor">Editor score</option>
          <option value="newest">Newest</option>
          <option value="price">Price: low to high</option>
          <option value="az">A–Z</option>
        </select>
        <span id="dirCount" class="small muted"></span>
        <a class="btn btn--primary" href="/directory/submit/">Submit a tool</a>
      </div>
      <div class="dir-grid" id="dirGrid"></div>
      {ad("in_article")}
    </div>
  </div>
</section>
<section class="band band--alt">
  <div class="wrap">
    {section_head("How this directory works", "Editorially ranked, transparently funded")}
    <div class="grid g3">
      <div class="card"><h3>Manually reviewed</h3><p>Every tool is used or trialled before it is
      listed. The editor note is the point of the listing — anyone can copy a feature list.</p></div>
      <div class="card"><h3>Paid placement is labelled</h3><p>Featured listings are paid and say so
      on every card. Ratings, editor scores and notes are not for sale at any price.</p></div>
      <div class="card"><h3>Affiliate links disclosed</h3><p>Some links earn a commission. They
      never affect placement, and tools with no affiliate programme rank the same.</p></div>
    </div>
    {newsletter_block()}
  </div>
</section>
{cta_band("Built the tool? Get it in front of the people who buy tools.",
          "Featured listings from $79, sponsored category placement from $299 a month.",
          ("Submit your tool", "/directory/submit/"), ("See the media kit", "/advertise/"))}'''

    return page("Content & AI Tool Directory — Honestly Reviewed Tools | Content.Media",
                "Filter content and AI tools by category, pricing, modality and platform. "
                "Every listing carries an honest editor note.",
                "/directory/", body, active="directory",
                extra_body='<script src="/assets/js/directory.js" defer></script>')


def build_submit():
    form = simple_form("submit-tool", "Submit your tool", [
        {"name": "tool_name", "label": "Tool name", "type": "text", "required": True,
         "placeholder": "Acme Captions"},
        {"name": "tool_url", "label": "Website URL", "type": "url", "required": True,
         "placeholder": "https://"},
        {"name": "tagline", "label": "Tagline (70 characters max)", "type": "text", "required": True,
         "placeholder": "Auto-captions that don't look auto-generated"},
        {"name": "short_description", "label": "Short description (160 characters max)",
         "type": "text", "required": True, "placeholder": "One sentence a buyer would understand."},
        {"name": "category", "label": "Primary category", "type": "select", "required": True,
         "options": ["AI writing", "Video editing", "Short-form video", "Audio & podcast",
                     "Image & design", "SEO & research", "Social scheduling", "Analytics",
                     "Newsletter", "Monetisation", "Transcription", "Thumbnails",
                     "Automation", "Stock assets", "Collaboration", "Voice & dubbing"]},
        {"name": "pricing_model", "label": "Pricing model", "type": "select", "required": True,
         "options": ["Free", "Freemium", "Free trial", "Paid", "Open source", "Contact for pricing"]},
        {"name": "price_from", "label": "Starting price (USD per month, 0 if free)",
         "type": "text", "required": True, "placeholder": "19"},
        {"name": "modalities", "label": "Works with", "type": "select", "required": True,
         "options": ["Text", "Image", "Video", "Audio", "Code", "Data", "Multiple"]},
        {"name": "platforms", "label": "Platforms", "type": "text", "required": True,
         "placeholder": "Web, iOS, Android, API…"},
        {"name": "company", "label": "Company name", "type": "text", "required": True,
         "placeholder": "Acme Inc."},
        {"name": "country", "label": "Country", "type": "text", "required": True, "placeholder": "Canada"},
        {"name": "founded", "label": "Founded (year)", "type": "text", "required": False,
         "placeholder": "2024"},
        {"name": "reader_discount", "label": "Discount code for our readers (optional)",
         "type": "text", "required": False, "placeholder": "CONTENTMEDIA20"},
        {"name": "your_name", "label": "Your name", "type": "text", "required": True,
         "placeholder": "Alex Moreau", "autocomplete": "name"},
        {"name": "your_email", "label": "Your email", "type": "email", "required": True,
         "placeholder": "you@company.com", "autocomplete": "email"},
        {"name": "your_role", "label": "Your role", "type": "select", "required": True,
         "options": ["Founder", "Team member", "Agency / PR", "User recommending it"]},
        {"name": "tier", "label": "Listing tier", "type": "select", "required": True,
         "options": ["Free — 2 to 4 week review queue, no backlink",
                     "Featured — $79 one-time, live in 48h, 7 days on the homepage, dofollow link",
                     "Sponsored — $299/month, pinned top of category, sidebar banner, newsletter slot"]},
        {"name": "honest_weakness", "label": "What is your tool genuinely bad at?", "type": "textarea",
         "required": True, "placeholder": "We ask everyone. Listings that dodge this question get "
         "declined — the editor note is going to say it anyway, and we would rather hear it from you."},
    ], button="Submit for review",
       note="Free listings are reviewed in two to four weeks. Paid listings are reviewed within one "
            "business day and we send a payment link once approved — we never charge before approval.")

    faqs = faq([
        ("Can I pay for a better rating?",
         "<p>No. Featured and sponsored placements buy <em>visibility</em>, labelled as such on every "
         "card. Ratings, editor scores and editor notes are not for sale, and we have declined "
         "listings from advertisers.</p>"),
        ("What does the free listing get me?",
         "<p>A permanent listing with your tagline, description, category, pricing and an editor "
         "note, indexed and searchable. The link is nofollow on free listings.</p>"),
        ("Why do you ask what my tool is bad at?",
         "<p>Because the editor note is the only reason anyone trusts this directory, and it will "
         "say something. Founders who answer honestly get a fairer note than ones who make us find "
         "the weakness ourselves.</p>"),
        ("Do you accept every submission?",
         "<p>No. We decline tools that do not work, tools that are a thin wrapper with no added "
         "value, and anything with a deceptive pricing page. Payment is only taken after approval.</p>"),
        ("Can I update my listing later?",
         f"<p>Yes — {mail_link('send us the changes', 'Directory listing update')} and we update it "
         "within a business day. Pricing changes are free to update regardless of tier.</p>"),
    ])

    body = f'''<section class="band">
  <div class="wrap article-layout">
    <article>
      {breadcrumbs([("Home", "/"), ("Tool directory", "/directory/"), ("Submit a tool", "/directory/submit/")])}
      <h1>Submit a tool</h1>
      <p class="lede">Get in front of creators, publishers and marketing teams who are actively
      shopping. Free listings are welcome. Paid tiers buy speed and visibility — never a better review.</p>
      <div class="tier-grid" style="margin:1.8rem 0">
        <div class="tier"><h3>Free</h3><p class="tier-price">$0</p>
          <ul><li>Permanent listing</li><li>Editor note</li><li>2–4 week review queue</li>
          <li>Nofollow link</li></ul>
          <a class="btn btn--ghost btn--block" href="#submit-form">Submit free</a></div>
        <div class="tier tier--hot"><h3>Featured</h3><p class="tier-price">$79<small> one-time</small></p>
          <ul><li>Live within 48 hours</li><li>7 days on the homepage</li><li>Featured badge</li>
          <li>Dofollow link</li><li>Mention in the weekly brief</li></ul>
          <a class="btn btn--primary btn--block" href="#submit-form">Go featured</a></div>
        <div class="tier"><h3>Sponsored</h3><p class="tier-price">$299<small> /month</small></p>
          <ul><li>Everything in Featured</li><li>Pinned top of your category</li>
          <li>Sidebar banner sitewide</li><li>Dedicated newsletter slot</li>
          <li>Cancel any time</li></ul>
          <a class="btn btn--ghost btn--block" href="#submit-form">Go sponsored</a></div>
      </div>
      <div id="submit-form">{form}</div>
      {faqs}
    </article>
    <aside class="sidebar">
      {ad("sidebar", style="sidebar")}
      <div class="panel panel--compact">
        <h3 style="font-size:1rem">Who sees your listing</h3>
        <ul class="ticks small">
          <li>Creators, publishers and in-house marketing teams</li>
          <li>Buyers arriving from high-intent search queries</li>
          <li>Current reach figures in the <a href="/advertise/">media kit</a></li>
        </ul>
        <a class="btn btn--ghost btn--block" href="/advertise/">Full media kit</a>
      </div>
    </aside>
  </div>
</section>'''

    return page("Submit a Tool to the Content.Media Directory",
                "List your content or AI tool. Free listings welcome; featured from $79, "
                "sponsored from $299/month. Ratings are never for sale.",
                "/directory/submit/", body, active="directory")


# ---------------------------------------------------------------------------
# Services — the highest-value conversion surface
# ---------------------------------------------------------------------------
def build_services():
    faqs = faq([
        ("What does a content programme cost?",
         "<p>Retainers run $2,500 to $30,000 a month depending on output and format mix. Most "
         "engagements land between $6,000 and $15,000. One-off projects — a pillar library, a "
         "channel relaunch, a benchmark report — start at $8,000. We publish this because hiding "
         "it wastes everyone's time.</p>"),
        ("What if my budget is under $2,500?",
         "<p>You will get our DIY playbook free instead of a sales call. It is the same operating "
         "system we run internally: the repurposing system, the brief template, the publishing "
         "checklist and the measurement model. Come back when the budget is there.</p>"),
        ("How fast do you turn around the plan?",
         "<p>One business day. You get scope, deliverables, a 90-day calendar, a monthly number, "
         "and a forecast built with the same models published on this site.</p>"),
        ("Do you use AI to write the content?",
         "<p>For research, structure and first drafts — yes, and we will tell you exactly where. "
         "The information gain, the opinions and the original data are human, because that is the "
         "part that earns the ranking. Our <a href='/guides/ai-content-workflow/'>workflow is "
         "published</a>.</p>"),
        ("Who actually does the work?",
         "<p>A named strategist plus a bench of specialist writers, editors and video producers. "
         "You meet everyone on the account. No offshore mystery pod, no account manager relaying "
         "messages to people you never speak to.</p>"),
        ("What happens if it does not work?",
         "<p>We agree the leading indicators up front — indexation rate, ranking movement, "
         "qualified leads — and review at 90 days. If the leading indicators are not moving we "
         "change the approach or we end it. No 12-month lock-in.</p>"),
    ])

    body = f'''<section class="band">
  <div class="wrap">
    {breadcrumbs([("Home", "/"), ("Services", "/services/")])}
    <h1>Content programmes, built and run</h1>
    <p class="lede">We build content operations for brands and publishers using the same models
    published free on this site. Strategy, production, distribution and measurement — with the
    numbers agreed before anyone writes a word.</p>
    {ad("leaderboard", style="leaderboard")}
  </div>
</section>

<section class="band" style="padding-top:0">
  <div class="wrap">{lead_form()}</div>
</section>

<section class="band band--alt">
  <div class="wrap">
    {section_head("What we do", "Four things, done properly")}
    <div class="grid g4">
      <div class="card"><div class="card-ico">01</div><h3>Content strategy</h3>
      <p>Keyword and topic architecture, the offer that converts the traffic, and a measurement
      model you can defend to a CFO.</p></div>
      <div class="card"><div class="card-ico">02</div><h3>Production at volume</h3>
      <p>Articles, pillar pages, video, podcast and short-form, on a calendar, at a fixed monthly
      cost per piece.</p></div>
      <div class="card"><div class="card-ico">03</div><h3>Owned-media monetisation</h3>
      <p>Display, sponsorship, newsletter and affiliate revenue built on top of traffic you already
      have. Most brands leave this entirely on the table.</p></div>
      <div class="card"><div class="card-ico">04</div><h3>Distribution systems</h3>
      <p>The one-to-twelve repurposing system, running weekly, without twelve times the headcount.</p></div>
    </div>
  </div>
</section>

<section class="band" id="pricing">
  <div class="wrap">
    {section_head("Pricing", "Published, because hiding it wastes your time",
      "Every engagement starts with a costed plan. No discovery-call gatekeeping to find out the number.")}
    <div class="tier-grid">
      <div class="tier"><h3>Launch</h3><p class="tier-price">$2,500<small> /month</small></p>
        <ul><li>4–6 pieces a month</li><li>One format</li><li>Quarterly strategy review</li>
        <li>Monthly reporting</li></ul>
        <a class="btn btn--ghost btn--block" href="#quote">Start here</a></div>
      <div class="tier tier--hot"><h3>Programme</h3><p class="tier-price">$6,000<small> – $15,000/mo</small></p>
        <ul><li>12–20 pieces a month</li><li>Multi-format with repurposing</li>
        <li>Named strategist</li><li>Monetisation build-out</li><li>Bi-weekly reviews</li></ul>
        <a class="btn btn--primary btn--block" href="#quote">Most engagements</a></div>
      <div class="tier"><h3>Operator</h3><p class="tier-price">$25,000<small>+ /month</small></p>
        <ul><li>Full content function</li><li>Embedded team</li><li>Original research programme</li>
        <li>Revenue ownership</li></ul>
        <a class="btn btn--ghost btn--block" href="#quote">Talk to us</a></div>
    </div>
    <p class="small muted" style="margin-top:1rem">One-off projects from $8,000. 50% up front on
    project work, net 30 on retainers. No 12-month lock-in on any tier.</p>
  </div>
</section>

<section class="band band--alt">
  <div class="wrap">
    {section_head("How it runs", "Four weeks from signature to first published asset")}
    <div class="grid g4">
      <div class="card"><h3>Week 1 — Audit</h3><p>Content, technical and revenue audit. We tell you
      what to stop doing first.</p></div>
      <div class="card"><h3>Week 2 — Architecture</h3><p>Topic map, offer design, measurement model,
      90-day calendar.</p></div>
      <div class="card"><h3>Week 3 — Build</h3><p>Briefs, templates, production pipeline, review
      gates, publishing checklist.</p></div>
      <div class="card"><h3>Week 4 — Ship</h3><p>First assets live, distribution running,
      reporting connected.</p></div>
    </div>
  </div>
</section>

<section class="band"><div class="wrap" style="max-width:860px">{faqs}{helpful_poll("services")}</div></section>
{cta_band("One business day. One costed plan. No obligation.",
          "Tell us the shape of the problem and we will tell you what it takes to solve it.",
          ("Get my content plan", "#quote"), ("Read the guides first", "/guides/"))}'''

    return page("Content Marketing Services — Costed Plan in One Business Day | Content.Media",
                "Content programmes built and run for brands and publishers. Published pricing "
                "from $2,500/month. Get a costed plan in one business day.",
                "/services/", body, active="services",
                schema={"@context": "https://schema.org", "@type": "Service",
                        "serviceType": "Content marketing services",
                        "provider": {"@type": "Organization", "name": SITE["name"]},
                        "areaServed": "Worldwide",
                        "offers": {"@type": "Offer", "priceSpecification": {
                            "@type": "PriceSpecification", "minPrice": 2500,
                            "priceCurrency": "USD"}}})


def build_services_thanks():
    body = f'''<section class="band">
  <div class="wrap" style="max-width:720px;text-align:center">
    <div class="card-ico" style="margin:0 auto 1rem;width:56px;height:56px;font-size:1.5rem">✓</div>
    <h1>Your plan is being built</h1>
    <p class="lede">We received your brief. You will get a costed content plan by email within one
    business day — scope, deliverables, a 90-day calendar and a forecast.</p>
    <div class="panel" style="text-align:left;margin:2rem 0">
      <h3 class="mt0">While you wait</h3>
      <ul class="ticks">
        <li>Check your spam folder — our reply comes from a monitored address, and some filters
        are aggressive about first contact.</li>
        <li>Send us your analytics access if you have it. It makes the plan considerably sharper.</li>
        <li>Read <a href="/guides/lead-generation-for-content-sites/">the lead-gen guide</a> —
        it is the framework we will use on your site.</li>
      </ul>
    </div>
    <div class="grid g3">
      <a class="card" href="/benchmarks/"><h3>The benchmarks</h3><p>Every number we will use in your plan.</p></a>
      <a class="card" href="/tools/content-roi-calculator/"><h3>ROI calculator</h3><p>Model it yourself first.</p></a>
      <a class="card" href="/guides/"><h3>The guides</h3><p>Twelve references, free.</p></a>
    </div>
    {newsletter_block(variant="narrow", magnet=False,
      heading="While you're here", sub="The weekly brief: benchmark changes and payout shifts.")}
  </div>
</section>'''
    return page("Thank you — your content plan is on the way | Content.Media",
                "We received your brief and will send a costed content plan within one business day.",
                "/services/thank-you/", body, active="services",
                extra_head='<meta name="robots" content="noindex,follow">')


# ---------------------------------------------------------------------------
# Advertise
# ---------------------------------------------------------------------------
def build_advertise():
    form = simple_form("media-kit", "Get the full rate card", [
        {"name": "name", "label": "Name", "type": "text", "required": True, "autocomplete": "name"},
        {"name": "company", "label": "Company", "type": "text", "required": True,
         "autocomplete": "organization"},
        {"name": "email", "label": "Work email", "type": "email", "required": True,
         "autocomplete": "email"},
        {"name": "budget", "label": "Campaign budget", "type": "select", "required": True,
         "options": ["Under $2,500", "$2,500 – $10,000", "$10,000 – $25,000",
                     "$25,000 – $50,000", "$50,000+"]},
        {"name": "format", "label": "Format of interest", "type": "select", "required": True,
         "options": ["Newsletter primary slot", "Sponsored directory placement",
                     "Sitewide display", "Video integration", "Dedicated research report",
                     "Contest sponsorship", "Not sure — advise me"]},
    ], button="Send me the rate card",
       note="You get the full rate card, specs and availability calendar by email within one "
            "business day. We do not add you to any list without asking.")

    body = f'''<section class="band">
  <div class="wrap article-layout">
    <article class="prose">
      {breadcrumbs([("Home", "/"), ("Advertise", "/advertise/")])}
      <h1>Advertise &amp; sponsor</h1>
      <p class="lede">Reach creators, independent publishers and in-house marketing teams at the
      moment they are pricing, choosing tools or hiring. Our audience arrives looking for numbers,
      which means they are already in a buying decision.</p>

      <h2 id="audience">The audience</h2>
      <table>
        <thead><tr><th>Metric</th><th>Current figure</th></tr></thead>
        <tbody>
          <tr><td>Weekly brief subscribers</td><td>{metric('subscribers')}</td></tr>
          <tr><td>Monthly unique visitors</td><td>{metric('monthly_uniques')}</td></tr>
          <tr><td>Average open rate</td><td>{metric('open_rate')}</td></tr>
          <tr><td>Average click rate</td><td>{metric('click_rate')}</td></tr>
          <tr><td>Audience split — creators / publishers / brand teams</td><td>{metric('split_roles')}</td></tr>
          <tr><td>Geography</td><td>{metric('split_geo')}</td></tr>
          <tr><td>Seniority</td><td>{metric('seniority')}</td></tr>
        </tbody>
      </table>
      <p class="small muted">We publish reach figures only once they are measured and verifiable,
      and we report Apple Mail Privacy Protection inflation openly rather than letting you discover
      it at reconciliation. Request the current month's numbers with the form and you get them the
      same day, with the measurement method attached.</p>
      <div class="callout"><h4>Launch pricing</h4><p>Rates below are introductory while the audience
      is being built. Early sponsors keep their rate for twelve months when the numbers rise.</p></div>

      <h2 id="formats">Formats</h2>
      <table>
        <thead><tr><th>Format</th><th>Spec</th><th>From</th></tr></thead>
        <tbody>
          <tr><td>Newsletter primary slot</td><td>350 characters, 1200×600 image, tracked link</td><td>$450 / issue</td></tr>
          <tr><td>Newsletter classified</td><td>One line, max 3 per issue</td><td>$150 / issue</td></tr>
          <tr><td>Sponsored directory placement</td><td>Pinned category, sidebar banner, newsletter slot</td><td>$299 / month</td></tr>
          <tr><td>Featured tool listing</td><td>48h review, homepage 7 days, dofollow</td><td>$79 one-time</td></tr>
          <tr><td>Sitewide display</td><td>Leaderboard and in-article, 100% SOV on a section</td><td>$1,200 / month</td></tr>
          <tr><td>Video integration</td><td>60–90 seconds, host-read, in a benchmark explainer</td><td>$2,500</td></tr>
          <tr><td>Research report sponsorship</td><td>Co-branded quarterly benchmark report</td><td>$7,500</td></tr>
          <tr><td>Contest sponsorship</td><td>Prize supply plus named sponsorship of a contest</td><td>$3,000</td></tr>
        </tbody>
      </table>
      <p><strong>Minimum term:</strong> three issues on newsletter slots, one month on display.
      We cap sponsored inventory at one primary slot per issue.</p>

      <h2 id="rules">What we will not do</h2>
      <ul>
        <li>Sell a rating, an editor score or a ranking. Not at any price.</li>
        <li>Run an unlabelled sponsored placement.</li>
        <li>Accept advertisers whose product we would not list in the directory.</li>
        <li>Exceed one primary newsletter slot per issue, however good the offer is.</li>
      </ul>

      <h2 id="reporting">Reporting</h2>
      <p>Opens, unique clicks, click rate and a screenshot of the placement, within 48 hours of the
      send. Renewal is the entire economics of this business, and it is decided by whether reporting
      arrived without being chased.</p>
      {faq([
        ("Do you offer a trial placement?",
         "<p>Yes — a single classified slot at the one-issue rate so you can measure before "
         "committing to a term. We would rather you buy again than buy big once.</p>"),
        ("Can we sponsor a specific calculator or benchmark page?",
         "<p>Yes. Sitewide display can be scoped to a single high-traffic section, which is usually "
         "a better buy than sitewide for a tool with a narrow fit.</p>"),
        ("Do you accept affiliate-only deals?",
         "<p>For directory listings, yes. For newsletter and display we sell flat rates — affiliate "
         "revenue is disclosed separately and never influences placement.</p>"),
        ("What is your lead time?",
         "<p>Two weeks for newsletter slots, one week for display, four weeks for a co-branded "
         "research report.</p>"),
      ])}
    </article>
    <aside class="sidebar">
      <div class="panel panel--compact">{form}</div>
      {ad("sidebar", style="sidebar")}
      <div class="panel panel--compact">
        <h3 style="font-size:1rem">Inventory status</h3>
        <ul class="ticks small">
          <li>Newsletter primary slot — accepting bookings</li>
          <li>Sponsored directory categories — open</li>
          <li>Sitewide display — open</li>
          <li>Research report sponsorship — one per quarter</li>
        </ul>
        <p class="small muted" style="margin-top:.8rem">We cap sponsored inventory at one primary
        newsletter slot per issue regardless of demand.</p>
      </div>
    </aside>
  </div>
</section>
{cta_band("Want the rate card without the form?",
          "Ask directly and we will send the whole thing, specs and availability included.",
          ("Contact us", "/contact/"), ("Submit a tool instead", "/directory/submit/"))}'''

    return page("Advertise & Sponsor | Content.Media Media Kit",
                "Reach creators, publishers and marketing teams. Newsletter slots from $450, "
                "sponsored listings from $299/month, display from $1,200/month.",
                "/advertise/", body)


# ---------------------------------------------------------------------------
# Support / donations
# ---------------------------------------------------------------------------
def build_support():
    pct = round(DONATE["current_supporters"] / DONATE["goal_supporters"] * 100)
    bmc = f"https://buymeacoffee.com/{DONATE['buymeacoffee']}" if DONATE["buymeacoffee"] else "#"
    kofi = f"https://ko-fi.com/{DONATE['kofi']}" if DONATE["kofi"] else "#"
    ghs = f"https://github.com/sponsors/{DONATE['github_sponsors']}" if DONATE["github_sponsors"] else "#"
    stripe_m = DONATE["stripe_monthly"] or "/contact/?topic=support"
    stripe_o = DONATE["stripe_oneoff"] or "/contact/?topic=support"

    body = f'''<section class="band">
  <div class="wrap split">
    <div>
      {breadcrumbs([("Home", "/"), ("Support", "/support/")])}
      <h1>No paywall. No owner. No one telling us what to publish.</h1>
      <p class="lede">Content.Media is funded by advertising, labelled sponsorships and readers.
      There is no investor waiting for a return and no parent company whose tools we have to rank
      first. That independence is the whole product — and readers are what keeps it.</p>
      <p>Every calculator, every benchmark and every directory listing stays free. Supporters cover
      the quarterly data refresh, the freelancers who keep the database honest, hosting, and the
      prize pool for our contests.</p>
      <div class="goal">
        <strong>{DONATE['current_supporters']:,} of {DONATE['goal_supporters']:,} supporters</strong>
        <div class="goal-track"><div class="goal-fill" style="width:{max(pct,1)}%"></div></div>
        <p class="small muted mb0">Funding the 2027 data programme. The counter above is updated
        monthly from the payment provider — we do not inflate it, and if it is at zero it says zero.</p>
      </div>
    </div>
    <div class="panel">
      <h3 class="mt0">Support monthly</h3>
      <div class="seg" style="margin-bottom:1rem">
        <button class="is-on" type="button">Monthly</button>
        <button type="button" onclick="document.getElementById('oneoff').scrollIntoView({{behavior:'smooth'}})">One-time</button>
      </div>
      <div class="tier-grid" style="grid-template-columns:1fr">
        <div class="tier"><h3>Reader</h3><p class="tier-price">$5<small> /month</small></p>
          <ul><li>Name on the supporters page</li><li>Quarterly data notes before publication</li></ul>
          <a class="btn btn--ghost btn--block" href="{stripe_m}" rel="noopener">Support at $5</a></div>
        <div class="tier tier--hot"><h3>Supporter</h3><p class="tier-price">$10<small> /month, or $100/year</small></p>
          <ul><li>Everything in Reader</li><li>The full benchmark dataset as CSV</li>
          <li>Early access to new calculators</li><li>Ad-light reading</li></ul>
          <a class="btn btn--primary btn--block" href="{stripe_m}" rel="noopener">Support at $10</a></div>
        <div class="tier"><h3>Patron</h3><p class="tier-price">$100<small> /month, or $1,000/year</small></p>
          <ul><li>Everything in Supporter</li><li>Quarterly open-financials call</li>
          <li>Credit on every research report</li><li>Direct line to the research desk</li></ul>
          <a class="btn btn--ghost btn--block" href="{stripe_m}" rel="noopener">Become a patron</a></div>
      </div>
      <p class="small muted" style="margin-top:.8rem">Cancel any time. Secure payment. You get a
      receipt immediately. Annual saves roughly two months.</p>
    </div>
  </div>
</section>

<section class="band band--alt" id="oneoff">
  <div class="wrap">
    {section_head("One-time", "Prefer to give once?",
      "Every rail below works without an account on our side. Pick whichever you already use.")}
    <div class="grid g4">
      <a class="card" href="{stripe_o}" rel="noopener"><div class="card-ico">$</div>
        <h3>Card — $25 / $50 / $100</h3><p>Stripe-hosted checkout. Choose your own amount.</p></a>
      <a class="card" href="{bmc}" rel="noopener" target="_blank"><div class="card-ico">☕</div>
        <h3>Buy Me a Coffee</h3><p>Smallest possible gesture, genuinely appreciated.</p></a>
      <a class="card" href="{kofi}" rel="noopener" target="_blank"><div class="card-ico">K</div>
        <h3>Ko-fi</h3><p>0% platform fee — all of it reaches the work.</p></a>
      <a class="card" href="{ghs}" rel="noopener" target="_blank"><div class="card-ico">&lt;/&gt;</div>
        <h3>GitHub Sponsors</h3><p>For developers who would rather fund it from there.</p></a>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap split">
    <div>
      <span class="eyebrow">Transparency</span>
      <h2>Where every dollar goes</h2>
      <p>We publish a revenue and cost post every quarter, including what did not work. Patrons get
      the call where we walk through it.</p>
      <div class="bars">
        <div class="bar-row"><span>Research &amp; data</span><span class="bar-track"><span class="bar-fill" style="width:44%"></span></span><span>44%</span></div>
        <div class="bar-row"><span>Freelance writers</span><span class="bar-track"><span class="bar-fill" style="width:26%"></span></span><span>26%</span></div>
        <div class="bar-row"><span>Contests &amp; prizes</span><span class="bar-track"><span class="bar-fill" style="width:14%"></span></span><span>14%</span></div>
        <div class="bar-row"><span>Hosting &amp; tools</span><span class="bar-track"><span class="bar-fill" style="width:10%"></span></span><span>10%</span></div>
        <div class="bar-row"><span>Payment fees</span><span class="bar-track"><span class="bar-fill" style="width:6%"></span></span><span>6%</span></div>
      </div>
      <p class="small muted" style="margin-top:1rem">What $10 a month actually buys: roughly one
      hour of a researcher's time per supporter per quarter, or one directory listing reviewed and
      written properly.</p>
    </div>
    <div class="panel">
      <h3 class="mt0">Other ways to help that cost nothing</h3>
      <ul class="ticks">
        <li>Cite a benchmark table and link back — links are what keep this findable</li>
        <li>Forward the weekly brief to one person who would use it</li>
        <li>Tell us when a number looks wrong. Corrections make the database better</li>
        <li>Submit a tool we have missed, or an honest note on one we got wrong</li>
        <li>Share a calculator with a creator who is undercharging</li>
      </ul>
      <a class="btn btn--ghost btn--block" href="/contact/">Send a correction</a>
    </div>
  </div>
</section>

<section class="band band--alt"><div class="wrap" style="max-width:860px">
{faq([
  ("Is my donation tax-deductible?",
   "<p>No. Content.Media is an independent commercial publisher, not a registered charity. "
   "Supporting us is a contribution to independent work, not a charitable deduction.</p>"),
  ("Can I cancel a recurring contribution?",
   "<p>Any time, from the receipt email or the billing portal link in it. No email required, "
   "no retention call, no dark pattern.</p>"),
  ("Do supporters get to influence coverage?",
   "<p>Patrons get a quarterly call and a direct line to the research desk. Nobody — supporter, "
   "advertiser or sponsor — gets to change a rating, a benchmark or an editor note. That rule is "
   "the reason the work is worth funding.</p>"),
  ("Why not just put up a paywall?",
   "<p>Because the numbers on this site are most useful to the people least able to pay for them: "
   "creators who are undercharging because nobody ever showed them the benchmark. Paywalling that "
   "would defeat the point.</p>"),
  ("Can my company sponsor instead?",
   "<p>Yes — see the <a href='/advertise/'>media kit</a>. Corporate sponsorship is labelled and "
   "kept separate from reader support.</p>"),
])}
</div></section>
{cta_band("Thank you — genuinely.",
          "Reader support is what keeps every number on this site free and unbought.",
          ("Support monthly", "#"), ("Read the guides", "/guides/"))}'''

    return page("Support Content.Media — Keep Independent Creator Research Free",
                "No paywall, no owner. Support independent creator economy research from $5 a "
                "month, or give once. See exactly where the money goes.",
                "/support/", body)


# ---------------------------------------------------------------------------
# Contests
# ---------------------------------------------------------------------------
def build_contests():
    entry = simple_form("contest-entry", "Enter the Q4 Creator Grant", [
        {"name": "full_name", "label": "Full name", "type": "text", "required": True,
         "autocomplete": "name"},
        {"name": "email", "label": "Email", "type": "email", "required": True,
         "autocomplete": "email"},
        {"name": "country", "label": "Country of residence", "type": "select", "required": True,
         "options": ["United States", "Canada (excluding Quebec)", "United Kingdom",
                     "Australia", "Other — check eligibility"]},
        {"name": "channel_url", "label": "Your channel, site or newsletter URL", "type": "url",
         "required": True, "placeholder": "https://"},
        {"name": "what_youd_build", "label": "What would you build with $5,000?",
         "type": "textarea", "required": True,
         "placeholder": "Two or three sentences. Specific beats grand."},
        {"name": "skill_question", "label": "Skill-testing question (required for Canadian entrants): "
         "(12 × 4) − 8 + 6 = ?", "type": "text", "required": True, "placeholder": "Your answer"},
        {"name": "referral_source", "label": "How did you hear about this?", "type": "select",
         "required": False, "options": ["The weekly brief", "A calculator page", "Search",
                                        "Social", "A friend forwarded it", "Other"]},
        {"name": "marketing_consent", "label": "Also send me the weekly brief (optional — entry "
         "does not require this)", "type": "select", "required": False,
         "options": ["Yes, send the weekly brief", "No thanks"]},
    ], button="Submit my entry",
       note="No purchase necessary. Entry is free. Read the full "
            "<a href='/contests/official-rules/'>official rules</a> before entering.")

    body = f'''<section class="band">
  <div class="wrap">
    {breadcrumbs([("Home", "/"), ("Contests", "/contests/")])}
    <span class="eyebrow">Open now &middot; Closes 15 December 2026</span>
    <h1>The Q4 Creator Grant — $5,000</h1>
    <p class="lede">Funded by reader support and sponsor contributions. One $5,000 grant and four
    $500 runner-up grants to independent creators and publishers building something specific.
    Free to enter. No purchase necessary.</p>
    <div class="countdown" data-countdown="2026-12-15T23:59:59-05:00" style="margin:1.4rem 0"></div>
    {ad("leaderboard", style="leaderboard")}
  </div>
</section>

<section class="band" style="padding-top:0">
  <div class="wrap article-layout">
    <article class="prose">
      <h2 id="prizes">Prizes</h2>
      <table>
        <thead><tr><th>Place</th><th>Prize</th><th>Approximate retail value</th></tr></thead>
        <tbody>
          <tr><td>Grand prize</td><td>$5,000 cash grant + a year of featured directory placement</td><td>$8,588 USD</td></tr>
          <tr><td>Runners-up (×4)</td><td>$500 cash grant + a strategy session</td><td>$1,000 USD each</td></tr>
          <tr><td>All entrants</td><td>The full benchmark dataset as CSV</td><td>No cash value</td></tr>
        </tbody>
      </table>
      <p>Total approximate retail value of all prizes: <strong>$12,588 USD</strong>.
      Odds of winning depend on the number of eligible entries received.</p>

      <h2 id="how">How to enter</h2>
      <ol>
        <li>Complete the entry form on this page before 23:59 US Eastern on 15 December 2026.</li>
        <li>Canadian entrants must correctly answer the mathematical skill-testing question.</li>
        <li>One entry per person. Duplicate entries are removed, not disqualified.</li>
        <li>A free alternate method of entry by post is available — see the
        <a href="/contests/official-rules/">official rules</a>. Mail-in entries carry exactly the
        same chance of winning.</li>
      </ol>
      <div class="callout"><h4>No purchase necessary</h4><p>A purchase will not increase your
      chances of winning. Void where prohibited. Open to legal residents of the 50 United States
      and DC, Canada (excluding Quebec), the United Kingdom and Australia who are 18 or older.</p></div>

      <h2 id="judging">How winners are chosen</h2>
      <p>Grand prize: judged on the specificity and feasibility of what you would build, scored by
      two members of the research desk plus one independent creator, using a published rubric.
      Runners-up: selected at random from all eligible entries using a documented random number
      generator, recorded and witnessed. Winners are notified by email within 7 days of the draw
      and announced on this page on 22 December 2026.</p>

      <h2 id="why">Why we run this</h2>
      <p>Fourteen percent of every dollar that comes into this site goes into the prize pool.
      Independent creators are the reason the benchmark data exists — hundreds of people have
      contributed rate-card figures anonymously. This is the part of the revenue that goes back.</p>

      <h2 id="past">Winners</h2>
      <p>This is the first round. Winners will be published on this page on 22 December 2026 and
      will stay posted for at least 90 days, along with what each of them built. Every subsequent
      round will be listed here too — a contest that never announces a winner is not a contest, and
      we would rather be held to that in public.</p>
      {helpful_poll("contests")}
    </article>
    <aside class="sidebar">
      <div class="panel panel--compact" id="enter">{entry}</div>
      {ad("sidebar", style="sidebar")}
      <div class="panel panel--compact">
        <h3 style="font-size:1rem">Sponsor a contest</h3>
        <p class="small muted">Supply a prize or fund a round. Named sponsorship, from $3,000.</p>
        <a class="btn btn--ghost btn--block" href="/advertise/">Talk to us</a>
      </div>
    </aside>
  </div>
</section>
{cta_band("Not entering? You can still fund the next one.",
          "Fourteen percent of reader support goes straight into the prize pool.",
          ("Support the site", "/support/"), ("Read the rules", "/contests/official-rules/"))}'''

    return page("The Q4 Creator Grant — $5,000, Free to Enter | Content.Media",
                "Enter the Q4 Creator Grant: a $5,000 cash grant plus four $500 runner-up grants "
                "for independent creators and publishers. No purchase necessary.",
                "/contests/", body)


def build_rules():
    body = f'''<section class="band">
  <div class="wrap" style="max-width:820px">
    {breadcrumbs([("Home", "/"), ("Contests", "/contests/"), ("Official rules", "/contests/official-rules/")])}
    <h1>Official rules — Q4 2026 Creator Grant</h1>
    <article class="prose">
      <p><strong>NO PURCHASE OR PAYMENT OF ANY KIND IS NECESSARY TO ENTER OR WIN. A PURCHASE WILL
      NOT INCREASE YOUR CHANCES OF WINNING. VOID WHERE PROHIBITED OR RESTRICTED BY LAW.</strong></p>

      <h2 id="sponsor">1. Sponsor</h2>
      <p>This promotion is sponsored by the operator of Content.Media. The sponsor's full legal name
      and postal address are provided on request via the {mail_link("contest administrator",
      "Q4 Creator Grant — sponsor details")} and are included in all mail-in entry
      correspondence.</p>

      <h2 id="eligibility">2. Eligibility</h2>
      <p>Open to legal residents of the fifty United States and the District of Columbia, Canada
      (excluding the Province of Quebec), the United Kingdom, and Australia, who are 18 years of age
      or older at the time of entry. Employees, contractors, officers and directors of the sponsor,
      and their immediate family members and household members, are not eligible. Void where
      prohibited.</p>

      <h2 id="period">3. Entry period</h2>
      <p>The promotion begins at 00:00:01 US Eastern Time on 22 September 2026 and ends at
      23:59:59 US Eastern Time on 15 December 2026. The sponsor's clock is the official timekeeper.</p>

      <h2 id="entry">4. How to enter</h2>
      <p><strong>Online:</strong> complete the entry form at content.media/contests/ during the
      entry period. Limit one entry per person.</p>
      <p><strong>Free alternate method of entry (AMOE):</strong> hand-print your full name, postal
      address, email address, date of birth and the URL of your channel, site or newsletter,
      together with a 100-word statement of what you would build, on a plain piece of paper, and
      mail it in a hand-addressed envelope to the sponsor's postal address, available on request
      from the {mail_link("contest administrator", "Q4 Creator Grant — AMOE address")}.
      Mail-in entries must be postmarked by 15 December 2026 and received by 22 December 2026.
      Mail-in entries receive exactly the same chance of winning as online entries.</p>

      <h2 id="skill">5. Skill-testing question</h2>
      <p>Canadian residents must correctly answer, unaided, a mathematical skill-testing question
      before being declared a winner, as required by Canadian law.</p>

      <h2 id="prizes">6. Prizes and odds</h2>
      <p>One (1) grand prize: US$5,000 cash grant plus twelve months of featured directory
      placement, approximate retail value US$8,588. Four (4) runner-up prizes: US$500 cash grant
      plus one strategy session, approximate retail value US$1,000 each. Total approximate retail
      value of all prizes: US$12,588.</p>
      <p><strong>Odds of winning depend on the number of eligible entries received.</strong> Prizes
      are not transferable and no substitution is permitted except by the sponsor, who may
      substitute a prize of equal or greater value.</p>

      <h2 id="selection">7. Winner selection and notification</h2>
      <p>The grand prize is judged against a published rubric by two members of the sponsor's
      research desk and one independent creator, scoring specificity (40%), feasibility (40%) and
      originality (20%). Runner-up prizes are selected at random from all eligible entries using a
      documented random number generator in a recorded, witnessed draw on or about 18 December 2026.
      Winners are notified by email within seven days of selection and must respond within ten days
      or an alternate winner will be selected.</p>

      <h2 id="taxes">8. Taxes</h2>
      <p>All taxes on prizes are the sole responsibility of the winner. United States winners
      receiving prizes with an aggregate value of US$600 or more in a calendar year will be issued
      an IRS Form 1099-MISC and must provide a completed Form W-9 before the prize is released.</p>

      <h2 id="publicity">9. Publicity and privacy</h2>
      <p>Except where prohibited, acceptance of a prize constitutes consent to the use of the
      winner's name, city and state or province, and the substance of their entry statement, for
      promotional purposes without further compensation. Personal information collected is handled
      in accordance with our <a href="/privacy/">privacy policy</a> and is used solely to
      administer this promotion. Entry does not constitute consent to receive marketing email; that
      consent is collected separately and optionally on the entry form, in accordance with CASL and
      applicable law.</p>

      <h2 id="general">10. General conditions</h2>
      <p>The sponsor reserves the right to disqualify any entrant who tampers with the entry
      process, submits fraudulent or duplicate entries, or acts in violation of these rules. If the
      promotion cannot be conducted as planned, the sponsor may modify, suspend or terminate it and
      award prizes from eligible entries received to that point. By entering, entrants release the
      sponsor from any liability arising from participation or prize acceptance to the fullest
      extent permitted by law.</p>

      <h2 id="law">11. Governing law</h2>
      <p>These rules are governed by the laws of the Province of Quebec, Canada, and the applicable
      laws of the entrant's own jurisdiction where those cannot be excluded. Disputes are resolved
      individually, without class action.</p>

      <h2 id="list">12. Winners list</h2>
      <p>Winners are published at content.media/contests/ on or about 22 December 2026 and remain
      posted for at least 90 days. A written winners list is available on request from the
      {mail_link("contest administrator", "Q4 Creator Grant — winners list")} for six months
      after the draw.</p>

      <div class="callout"><h4>Note on jurisdiction</h4><p>This promotion is not open to residents
      of the Province of Quebec, and is void in any jurisdiction where registration, bonding or
      additional filings would be required and have not been completed.</p></div>
    </article>
  </div>
</section>'''

    return page("Official Rules — Q4 2026 Creator Grant | Content.Media",
                "Complete official rules for the Q4 2026 Creator Grant: eligibility, entry "
                "period, free alternate method of entry, prizes, odds and winner selection.",
                "/contests/official-rules/", body)


# ---------------------------------------------------------------------------
# Newsletter
# ---------------------------------------------------------------------------
def build_newsletter():
    body = f'''<section class="band">
  <div class="wrap" style="max-width:920px">
    {breadcrumbs([("Home", "/"), ("Newsletter", "/newsletter/")])}
    <h1>The weekly Content.Media brief</h1>
    <p class="lede">One email every Tuesday. What moved in creator payouts, which benchmarks
    changed, one calculator walkthrough, and the three links worth your time. Five minutes,
    no filler, and we tell you when we were wrong the week before.</p>
    {newsletter_block()}
    <div class="grid g3" style="margin-top:2.5rem">
      <div class="card"><h3>What's in it</h3><p>Benchmark changes, platform payout shifts, rate
      movements, one deep calculator walkthrough, and new directory listings worth knowing about.</p></div>
      <div class="card"><h3>What isn't</h3><p>Hot takes, engagement bait, "10 AI tools that will
      change everything", or anything we would not read ourselves.</p></div>
      <div class="card"><h3>Ad load</h3><p>One primary sponsor slot per issue, clearly labelled.
      Never more. <a href="/advertise/">Media kit</a>.</p></div>
    </div>
    {ad("in_article")}
    {faq([
      ("How often do you email?",
       "<p>Once a week, Tuesday. Occasionally a second email when a platform changes payout terms "
       "materially — maybe four times a year.</p>"),
      ("Can I read past issues?",
       "<p>Yes. Every back issue is available to subscribers, and the archive is part of what you "
       "get on signup.</p>"),
      ("Will you sell my email?",
       "<p>No. Not to advertisers, not to sponsors, not to anyone. Sponsors buy a slot in the "
       "email; they never receive the list.</p>"),
      ("How do I unsubscribe?",
       "<p>One click in any email. No retention flow, no confirmation page, no 'are you sure'.</p>"),
    ])}
  </div>
</section>
{cta_band("Prefer the numbers without the email?",
          "Every benchmark is published free, no signup required.",
          ("Open the benchmarks", "/benchmarks/"), ("Run a calculator", "/tools/"))}'''

    return page("The Weekly Content.Media Brief — Creator Economy Benchmarks by Email",
                "One email a week: benchmark changes, platform payout shifts and a calculator "
                "walkthrough. Free, and the archive comes with it.",
                "/newsletter/", body)


def build_newsletter_thanks():
    body = f'''<section class="band">
  <div class="wrap" style="max-width:700px;text-align:center">
    <div class="card-ico" style="margin:0 auto 1rem;width:56px;height:56px;font-size:1.5rem">✓</div>
    <h1>You're in</h1>
    <p class="lede">Your first issue is on its way. Grab the benchmark dataset right here —
    <a href="/assets/data/creator-benchmarks-2026.csv" download>download the 2026 CSV</a>. If the
    confirmation is not in your inbox in five minutes, look in spam and mark it "not spam" so the
    next one lands properly.</p>
    <div class="grid g3" style="margin-top:2rem">
      <a class="card" href="/benchmarks/"><h3>The benchmarks</h3><p>Everything the brief refers to.</p></a>
      <a class="card" href="/tools/"><h3>Ten calculators</h3><p>Free, no signup, formulas published.</p></a>
      <a class="card" href="/contests/"><h3>The $5,000 grant</h3><p>Open now. Free to enter.</p></a>
    </div>
    <div class="panel" style="text-align:left;margin-top:2rem">
      <h3 class="mt0">One favour</h3>
      <p>Forward the first issue to one person who would use it. That is how this list grows — no
      ads, no giveaways, no bought subscribers. If it is not worth forwarding, reply and tell us
      why; we read everything.</p>
    </div>
  </div>
</section>'''
    return page("You're subscribed | Content.Media",
                "You're subscribed to the weekly Content.Media brief.",
                "/newsletter/thank-you/", body,
                extra_head='<meta name="robots" content="noindex,follow">')
