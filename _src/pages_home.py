# -*- coding: utf-8 -*-
from config import SITE, PROOF
from layout import page, ad
from components import (section_head, stat_row, faq, cta_band, newsletter_block,
                        lead_form, helpful_poll)

TOOL_CARDS = [
    ("YouTube money calculator", "/tools/youtube-money-calculator/", "YT",
     "Real RPM by niche and geography, not a made-up $5 flat rate."),
    ("Creator rate card builder", "/tools/creator-rate-card-calculator/", "RC",
     "Price a sponsorship with usage rights and exclusivity priced in."),
    ("TikTok earnings calculator", "/tools/tiktok-earnings-calculator/", "TT",
     "Engagement-weighted rates, because followers alone do not pay."),
    ("Instagram engagement calculator", "/tools/instagram-engagement-calculator/", "IG",
     "Benchmark against your follower tier, then price the bundle."),
    ("Content ROI calculator", "/tools/content-roi-calculator/", "ROI",
     "Model pipeline, ad revenue and payback on a content programme."),
    ("Newsletter sponsorship calculator", "/tools/newsletter-sponsorship-calculator/", "NL",
     "Price on opens, not list size — the way advertisers actually buy."),
]


def build():
    hero = f'''<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <span class="pill">Updated September 2026 &middot; <b>{PROOF['niches']} niches benchmarked</b></span>
      <h1>Know exactly what your <em>content</em> is worth.</h1>
      <p class="lede">Content.Media is the independent research desk for the creator economy.
      Free calculators built on published assumptions, a benchmark database anyone can audit,
      and a curated directory of {PROOF['tools_indexed']} content and AI tools.
      No paywall, no gated numbers, no vendor writing our rankings.</p>
      <div class="hero-cta">
        <a class="btn btn--primary btn--lg" href="/tools/">Run a free calculator</a>
        <a class="btn btn--ghost btn--lg" href="/benchmarks/">See the 2026 benchmarks</a>
      </div>
      <p class="hero-note">Free forever. No sign-up to use any tool on this site.</p>
    </div>
    <div>
      <div class="calc" style="--r-lg:22px">
        <div class="calc-head"><h2 style="font-size:.98rem">Quick estimate &middot; YouTube long-form</h2>
          <span class="tag tag--brand">Live</span></div>
        <div class="calc" data-calc="youtube" style="border:0;box-shadow:none;border-radius:0">
          <div class="calc-body">
            <div class="calc-inputs">
              <div class="calc-row">
                <label for="h-views">Monthly views
                  <output class="val" data-for="views" id="h-out"></output></label>
                <input id="h-views" name="views" type="range" min="1000" max="5000000" step="1000"
                       value="250000" data-def="250000">
              </div>
              <div class="calc-row">
                <label for="h-niche">Niche</label>
                <select id="h-niche" name="niche">
                  <option value="finance">Personal finance &amp; investing</option>
                  <option value="marketing" selected>Marketing &amp; business</option>
                  <option value="tech">Technology</option>
                  <option value="education">Education &amp; how-to</option>
                  <option value="gaming">Gaming</option>
                  <option value="entertain">Entertainment &amp; vlogs</option>
                </select>
              </div>
              <div class="calc-row">
                <label for="h-geo">Audience geography</label>
                <select id="h-geo" name="geo">
                  <option value="us">Mostly United States</option>
                  <option value="tier1" selected>Mixed tier-1</option>
                  <option value="mixed">Global mix</option>
                  <option value="tier3">Mostly South Asia / SEA / LATAM</option>
                </select>
              </div>
              <input type="hidden" name="subs" value="50000">
              <a class="small" href="/tools/youtube-money-calculator/">Open the full calculator &rarr;</a>
            </div>
            <div class="calc-output" data-out></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>'''

    stats = f'''<section class="band" style="padding-top:0">
  <div class="wrap">
    {stat_row([
        (PROOF['niches'], "Niches benchmarked", f"Across {PROOF['geographies']} audience geographies"),
        (PROOF['tools_indexed'], "Tools in the directory", "Manually reviewed, none pay for rank"),
        (PROOF['calculators'], "Free calculators", "No email required, ever"),
        (PROOF['deliverables'], "Deliverable types priced", "Rate anchors you can quote from"),
    ])}
  </div>
</section>'''

    tools = f'''<section class="band band--alt" id="tools">
  <div class="wrap">
    {section_head("Free tools", "Ten calculators that give you a number, not a sales call",
      "Every one publishes its formula and its assumptions on the same page. "
      "Disagree with a figure? Change the input and watch the model move.",
      "/tools/", "All ten tools")}
    <div class="grid g3">
      {''.join(f"""<article class="card">
        <div class="card-ico">{ic}</div>
        <h3><a class="stretch" href="{href}">{name}</a></h3>
        <p>{desc}</p>
      </article>""" for name, href, ic, desc in TOOL_CARDS)}
    </div>
  </div>
</section>'''

    bench = f'''<section class="band">
  <div class="wrap split">
    <div>
      <span class="eyebrow">The data product</span>
      <h2>The 2026 Creator Economy Benchmarks</h2>
      <p class="lede">RPM by niche. Engagement bands by follower tier. Sponsorship rates by
      platform and deliverable. Production cost anchors. Updated quarterly, published in full,
      free to cite.</p>
      <ul class="ticks">
        <li>14 niches with low/high RPM ranges and geography multipliers</li>
        <li>Instagram and TikTok engagement bands across six follower tiers</li>
        <li>Rate-card anchors per 1,000 followers for 11 deliverable types</li>
        <li>Podcast and newsletter CPM ranges by slot position</li>
        <li>Display ad page RPM by content category</li>
      </ul>
      <a class="btn btn--primary btn--lg" href="/benchmarks/">Open the benchmark database</a>
    </div>
    <div class="media-frame" style="padding:1.3rem">
      <table class="prose" style="width:100%;border-collapse:collapse;font-size:.88rem">
        <thead><tr><th>Niche</th><th style="text-align:right">RPM low</th><th style="text-align:right">RPM high</th></tr></thead>
        <tbody>
          <tr><td>Personal finance</td><td style="text-align:right">$15.00</td><td style="text-align:right">$38.00</td></tr>
          <tr><td>B2B software</td><td style="text-align:right">$14.00</td><td style="text-align:right">$34.00</td></tr>
          <tr><td>Marketing &amp; business</td><td style="text-align:right">$10.00</td><td style="text-align:right">$26.00</td></tr>
          <tr><td>Technology</td><td style="text-align:right">$8.00</td><td style="text-align:right">$22.00</td></tr>
          <tr><td>Education</td><td style="text-align:right">$5.00</td><td style="text-align:right">$14.00</td></tr>
          <tr><td>Gaming</td><td style="text-align:right">$1.20</td><td style="text-align:right">$5.50</td></tr>
          <tr><td>Music</td><td style="text-align:right">$1.00</td><td style="text-align:right">$3.50</td></tr>
        </tbody>
      </table>
      <p class="small muted mb0" style="margin-top:.8rem">Creator take-home per 1,000 monetised
      views, tier-1 audience. Full table with geography factors on the benchmarks page.</p>
    </div>
  </div>
</section>'''

    directory = f'''<section class="band band--alt">
  <div class="wrap">
    {section_head("Directory", f"{PROOF['tools_indexed']} content and AI tools, honestly reviewed",
      "Filter by category, pricing model, modality and platform. Every listing carries an editor "
      "note that says what the tool is actually bad at.", "/directory/", "Browse the directory")}
    <div class="grid g4">
      <article class="card"><div class="card-ico">✎</div><h3><a class="stretch" href="/directory/?cat=AI%20writing">AI writing</a></h3><p>Drafting, briefs and brand voice.</p></article>
      <article class="card"><div class="card-ico">▶</div><h3><a class="stretch" href="/directory/?cat=Short-form%20video">Short-form video</a></h3><p>Clipping, captions and repurposing.</p></article>
      <article class="card"><div class="card-ico">$</div><h3><a class="stretch" href="/directory/?cat=Monetisation">Monetisation</a></h3><p>Ads, memberships, checkout and tips.</p></article>
      <article class="card"><div class="card-ico">⌕</div><h3><a class="stretch" href="/directory/?cat=SEO%20%26%20research">SEO &amp; research</a></h3><p>Keywords, crawls and content scoring.</p></article>
    </div>
  </div>
</section>'''

    services = f'''<section class="band" id="services">
  <div class="wrap">
    {section_head("Work with us", "Or skip the tools and have us build the machine",
      "We run content programmes for brands and publishers using the same models published "
      "on this site. Tell us the shape of the problem and we come back with a costed plan.")}
    {lead_form()}
  </div>
</section>'''

    support = '''<section class="band band--alt">
  <div class="wrap split">
    <div>
      <span class="eyebrow">Keep it free</span>
      <h2>This site has no paywall and no owner telling it what to publish</h2>
      <p class="lede">Every calculator, every benchmark and every directory listing is free and
      always will be. Supporters cover hosting, the quarterly data refresh, the prize pool for
      our contests, and the freelancers who help keep the database honest.</p>
      <a class="btn btn--primary btn--lg" href="/support/">Support Content.Media</a>
      <a class="btn btn--ghost btn--lg" href="/advertise/">Advertise or sponsor</a>
    </div>
    <div class="panel">
      <h3 class="mt0">Where the money goes</h3>
      <div class="bars">
        <div class="bar-row"><span>Research &amp; data</span><span class="bar-track"><span class="bar-fill" style="width:44%"></span></span><span>44%</span></div>
        <div class="bar-row"><span>Freelance writers</span><span class="bar-track"><span class="bar-fill" style="width:26%"></span></span><span>26%</span></div>
        <div class="bar-row"><span>Contests &amp; prizes</span><span class="bar-track"><span class="bar-fill" style="width:14%"></span></span><span>14%</span></div>
        <div class="bar-row"><span>Hosting &amp; tools</span><span class="bar-track"><span class="bar-fill" style="width:10%"></span></span><span>10%</span></div>
        <div class="bar-row"><span>Payment fees</span><span class="bar-track"><span class="bar-fill" style="width:6%"></span></span><span>6%</span></div>
      </div>
      <p class="small muted" style="margin-top:1rem">We publish a revenue and cost post every
      quarter. <a href="/about/#transparency">Read the latest one</a>.</p>
    </div>
  </div>
</section>'''

    faqs = faq([
        ("Is Content.Media free to use?",
         "<p>Yes. Every calculator, benchmark table and directory listing is free with no account "
         "and no email gate. The site is funded by display advertising, affiliate links that never "
         "affect rankings, sponsored listings that are always labelled, our own services business, "
         "and reader donations.</p>"),
        ("Where do your numbers come from?",
         "<p>Public platform disclosures, published payout terms, aggregated rate-card data shared "
         "by creators and buyers, and our own client work. Every calculator prints the exact "
         "constants it used underneath the result, and the full constant file is published at "
         "<a href='/benchmarks/'>/benchmarks/</a>. If you think a figure is wrong, "
         "<a href='/contact/'>tell us</a> and we will show our working or change it.</p>"),
        ("Do tools pay to be listed or ranked higher?",
         "<p>Tools can pay for a <em>featured</em> slot, which is labelled as featured everywhere it "
         "appears. Nobody can buy a rating, an editor score, or a change to the editor note. "
         "Some outbound links are affiliate links — see our <a href='/disclosure/'>disclosure</a>.</p>"),
        ("Can I cite or republish your benchmark data?",
         "<p>Yes, with a link back to the source page. Journalists, analysts and students can use "
         "the tables freely. If you need the raw dataset as CSV or a custom cut, "
         "<a href='/contact/'>ask us</a>.</p>"),
        ("Is the domain content.media for sale?",
         "<p>Enquiries about the website or the domain name go through the bar at the top of every "
         "page, or directly at <a href='" + SITE['owner_contact_url'] + "' rel='noopener' target='_blank'>"
         "web.works/contact</a>.</p>"),
    ])

    body = (hero + stats + ad("leaderboard", style="leaderboard") + tools + bench + directory
            + ad("in_article") + services + support
            + '<section class="band"><div class="wrap">' + faqs + helpful_poll("home")
            + '</div></section>'
            + '<section class="band band--alt"><div class="wrap">' + newsletter_block() + '</div></section>'
            + cta_band("Ready to stop guessing what your content is worth?",
                       "Run the numbers yourself, or have us build and run the programme.",
                       ("Run a calculator", "/tools/"), ("Get a costed plan", "/services/#quote")))

    schema = [
        {"@context": "https://schema.org", "@type": "Organization",
         "name": SITE["name"], "url": SITE["base_url"],
         "description": SITE["description"],
         "logo": SITE["base_url"] + "/assets/img/favicon.svg",
         "sameAs": [SITE["youtube_channel"]]},
        {"@context": "https://schema.org", "@type": "WebSite",
         "name": SITE["name"], "url": SITE["base_url"],
         "potentialAction": {"@type": "SearchAction",
                             "target": SITE["base_url"] + "/search/?q={search_term_string}",
                             "query-input": "required name=search_term_string"}},
    ]

    return page(
        f"{SITE['name']} — {SITE['tagline']}",
        SITE["description"], "/", body, active="", schema=schema,
        extra_body='<script src="/assets/js/benchmarks.js"></script><script src="/assets/js/calc.js" defer></script>',
    )
