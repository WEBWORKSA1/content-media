# -*- coding: utf-8 -*-
"""Benchmarks, guides, video library, job board."""
import re
from config import SITE, PROOF
from layout import page, ad
from components import (breadcrumbs, section_head, faq, cta_band, newsletter_block,
                        helpful_poll, byline, toc, simple_form)
from guides import GUIDES, BY_SLUG

# ---------------------------------------------------------------------------
# Benchmarks — the recurring data product
# ---------------------------------------------------------------------------
RPM_ROWS = [
    ("Personal finance &amp; investing", 15.00, 38.00, 28, 70),
    ("B2B software &amp; SaaS", 14.00, 34.00, 26, 64),
    ("Real estate &amp; mortgage", 12.00, 45.00, 24, 84),
    ("Marketing &amp; business", 10.00, 26.00, 20, 48),
    ("Technology &amp; gadget reviews", 8.00, 22.00, 16, 42),
    ("Education &amp; how-to", 5.00, 14.00, 10, 26),
    ("Health, fitness &amp; wellness", 4.00, 12.00, 8, 23),
    ("Travel", 4.00, 11.00, 8, 21),
    ("Food &amp; cooking", 3.50, 9.00, 7, 17),
    ("Beauty &amp; fashion", 3.50, 10.00, 7, 19),
    ("Entertainment &amp; vlogs", 1.50, 6.00, 3, 12),
    ("Gaming", 1.20, 5.50, 3, 11),
    ("Kids &amp; family", 1.00, 4.00, 2, 8),
    ("Music", 1.00, 3.50, 2, 7),
]


def build_benchmarks():
    rpm = "".join(
        f"<tr><td>{n}</td><td>${lo:.2f}</td><td>${hi:.2f}</td><td>${cl}–${ch}</td></tr>"
        for n, lo, hi, cl, ch in RPM_ROWS)

    body = f'''<section class="band">
  <div class="wrap">
    {breadcrumbs([("Home", "/"), ("Benchmarks", "/benchmarks/")])}
    <span class="eyebrow">Updated quarterly &middot; September 2026</span>
    <h1>The 2026 Creator Economy Benchmarks</h1>
    <p class="lede">Every constant used by every calculator on this site, published in full and
    free to cite. {PROOF['niches']} niches, {PROOF['geographies']} audience geographies,
    {PROOF['tiers']} follower tiers and {PROOF['deliverables']} deliverable types. If you think a number is wrong, <a href="/contact/">tell us</a>
    and we will show our working or change it.</p>
    <div class="chipset" style="margin:1rem 0 1.6rem">
      <a class="chip" href="#rpm">YouTube RPM</a>
      <a class="chip" href="#geo">Geography</a>
      <a class="chip" href="#engagement">Engagement bands</a>
      <a class="chip" href="#rates">Sponsorship rates</a>
      <a class="chip" href="#podcast">Podcast &amp; newsletter</a>
      <a class="chip" href="#display">Display RPM</a>
      <a class="chip" href="#costs">Production costs</a>
    </div>
    {byline()}
    {ad("leaderboard", style="leaderboard")}
  </div>
</section>

<section class="band" style="padding-top:0">
  <div class="wrap article-layout">
    <article class="prose">
      <h2 id="rpm">YouTube RPM by niche</h2>
      <p>Creator take-home per 1,000 monetised views, already net of YouTube's 45% share.
      Advertiser CPM shown for comparison — it is roughly double the creator RPM, which is why
      quoting CPM as "what YouTube pays" overstates earnings by 2×.</p>
      <table>
        <thead><tr><th>Niche</th><th>RPM low</th><th>RPM high</th><th>Advertiser CPM</th></tr></thead>
        <tbody>{rpm}</tbody>
      </table>
      <p class="small muted">Tier-1 audience assumed. Apply the geography multiplier below.
      Model it live in the <a href="/tools/youtube-money-calculator/">YouTube money calculator</a>.</p>

      <h2 id="geo">Audience geography multipliers</h2>
      <table>
        <thead><tr><th>Audience concentration</th><th>Multiplier</th><th>Effect on a $10 RPM</th></tr></thead>
        <tbody>
          <tr><td>Mostly United States</td><td>×1.00</td><td>$10.00</td></tr>
          <tr><td>Mixed tier-1 (US/UK/CA/AU)</td><td>×0.86</td><td>$8.60</td></tr>
          <tr><td>Mostly Western Europe</td><td>×0.72</td><td>$7.20</td></tr>
          <tr><td>Global mix</td><td>×0.48</td><td>$4.80</td></tr>
          <tr><td>Mostly South Asia / SEA / LATAM</td><td>×0.22</td><td>$2.20</td></tr>
        </tbody>
      </table>
      <div class="callout"><h4>Monetised view share</h4><p>Only <strong>55%–78%</strong> of views
      serve a paid ad impression. Multiply total views by that share before applying any RPM figure.
      This is the most common reason real earnings land below calculator estimates.</p></div>

      <h2 id="shorts">Short-form pool rates</h2>
      <table>
        <thead><tr><th>Format</th><th>RPM</th><th>Per 1M views</th></tr></thead>
        <tbody>
          <tr><td>YouTube Shorts</td><td>$0.03 – $0.12</td><td>$30 – $120</td></tr>
          <tr><td>Long-form, same niche</td><td>$1.00 – $38.00</td><td>$1,000 – $38,000</td></tr>
          <tr><td>TikTok Creator Rewards</td><td>$0.02 – $0.06</td><td>$20 – $60</td></tr>
        </tbody>
      </table>

      {ad("in_article")}

      <h2 id="engagement">Engagement rate bands</h2>
      <h3>Instagram — (likes + comments) ÷ followers</h3>
      <table>
        <thead><tr><th>Tier</th><th>Benchmark ER</th><th>Sponsored post band</th></tr></thead>
        <tbody>
          <tr><td>Nano, under 1K</td><td>6.5% – 8.5%</td><td>$10 – $100</td></tr>
          <tr><td>Nano, 1K – 5K</td><td>4.8% – 6.4%</td><td>$50 – $250</td></tr>
          <tr><td>Micro, 5K – 10K</td><td>3.4% – 4.6%</td><td>$100 – $400</td></tr>
          <tr><td>Micro, 10K – 100K</td><td>2.0% – 3.2%</td><td>$200 – $2,500</td></tr>
          <tr><td>Macro, 100K – 1M</td><td>1.4% – 2.2%</td><td>$2,000 – $12,000</td></tr>
          <tr><td>Mega, 1M+</td><td>1.0% – 1.7%</td><td>$10,000+</td></tr>
        </tbody>
      </table>
      <h3>TikTok — likes ÷ (followers × videos)</h3>
      <table>
        <thead><tr><th>Tier</th><th>Benchmark ER</th></tr></thead>
        <tbody>
          <tr><td>Under 5K</td><td>12.0% – 18.0%</td></tr>
          <tr><td>5K – 10K</td><td>10.5% – 15.0%</td></tr>
          <tr><td>10K – 50K</td><td>9.0% – 13.5%</td></tr>
          <tr><td>50K – 100K</td><td>8.0% – 12.0%</td></tr>
          <tr><td>100K – 1M</td><td>7.0% – 11.0%</td></tr>
          <tr><td>1M+</td><td>6.0% – 10.5%</td></tr>
        </tbody>
      </table>

      <h2 id="rates">Sponsorship rate anchors</h2>
      <p>US dollars per deliverable, per 1,000 followers, before multipliers.</p>
      <table>
        <thead><tr><th>Deliverable</th><th>Low</th><th>High</th></tr></thead>
        <tbody>
          <tr><td>Instagram Reel</td><td>$12</td><td>$30</td></tr>
          <tr><td>Instagram in-feed post</td><td>$8</td><td>$20</td></tr>
          <tr><td>Instagram Story frame</td><td>$4</td><td>$10</td></tr>
          <tr><td>TikTok video</td><td>$10</td><td>$26</td></tr>
          <tr><td>YouTube integration (60–90s)</td><td>$18</td><td>$55</td></tr>
          <tr><td>YouTube dedicated video</td><td>$30</td><td>$90</td></tr>
          <tr><td>YouTube Short</td><td>$8</td><td>$22</td></tr>
          <tr><td>X / Twitter post</td><td>$3</td><td>$10</td></tr>
          <tr><td>LinkedIn post</td><td>$15</td><td>$45</td></tr>
          <tr><td>Newsletter primary slot (per 1,000 opens)</td><td>$25</td><td>$90</td></tr>
          <tr><td>Podcast mid-roll (per 1,000 downloads)</td><td>$18</td><td>$50</td></tr>
        </tbody>
      </table>
      <h3>Multipliers</h3>
      <table>
        <thead><tr><th>Lever</th><th>Multiplier</th></tr></thead>
        <tbody>
          <tr><td>B2B / professional niche</td><td>×1.55</td></tr>
          <tr><td>Finance niche</td><td>×1.60</td></tr>
          <tr><td>Technology niche</td><td>×1.30</td></tr>
          <tr><td>Gaming niche</td><td>×0.85</td></tr>
          <tr><td>Paid usage rights, 30 days</td><td>×1.35</td></tr>
          <tr><td>Paid usage rights, 90 days</td><td>×1.60</td></tr>
          <tr><td>Perpetual usage, all channels</td><td>×2.10</td></tr>
          <tr><td>Category exclusivity, 30 days</td><td>×1.20</td></tr>
          <tr><td>Category exclusivity, 12 months</td><td>×1.80</td></tr>
        </tbody>
      </table>

      <h2 id="podcast">Podcast &amp; newsletter CPM</h2>
      <table>
        <thead><tr><th>Inventory</th><th>CPM</th><th>Basis</th></tr></thead>
        <tbody>
          <tr><td>Podcast pre-roll</td><td>$15 – $25</td><td>IAB v2.1 downloads</td></tr>
          <tr><td>Podcast mid-roll</td><td>$22 – $40</td><td>IAB v2.1 downloads</td></tr>
          <tr><td>Podcast post-roll</td><td>$10 – $18</td><td>IAB v2.1 downloads</td></tr>
          <tr><td>Host-read premium</td><td>+35%</td><td>Applied to any slot</td></tr>
          <tr><td>Newsletter classified</td><td>$8 – $18</td><td>Opens</td></tr>
          <tr><td>Newsletter primary slot</td><td>$25 – $60</td><td>Opens</td></tr>
          <tr><td>Newsletter dedicated send</td><td>$45 – $120</td><td>Opens</td></tr>
          <tr><td>B2B decision-maker premium</td><td>×1.80</td><td>Applied to any slot</td></tr>
        </tbody>
      </table>

      <h2 id="display">Display advertising page RPM</h2>
      <table>
        <thead><tr><th>Content category</th><th>Page RPM, tier-1</th></tr></thead>
        <tbody>
          <tr><td>Finance &amp; insurance</td><td>$28 – $60</td></tr>
          <tr><td>B2B software / SaaS</td><td>$26 – $62</td></tr>
          <tr><td>Technology</td><td>$20 – $44</td></tr>
          <tr><td>Marketing &amp; business</td><td>$18 – $42</td></tr>
          <tr><td>Health</td><td>$14 – $34</td></tr>
          <tr><td>Education</td><td>$9 – $20</td></tr>
          <tr><td>General / lifestyle</td><td>$5 – $12</td></tr>
          <tr><td>Entertainment</td><td>$3 – $9</td></tr>
        </tbody>
      </table>
      <p class="small muted">A realistic expectation for a new marketing or business site with mixed
      geography traffic is <strong>$8–$20 page RPM</strong>, not the headline figures.</p>

      <h2 id="costs">Production cost anchors</h2>
      <table>
        <thead><tr><th>Deliverable</th><th>Cost range (USD)</th></tr></thead>
        <tbody>
          <tr><td>SEO article, 1,500 words, expert-written</td><td>$350 – $1,200</td></tr>
          <tr><td>Pillar page / 4,000-word guide</td><td>$1,200 – $4,500</td></tr>
          <tr><td>Short-form video (per Reel/Short)</td><td>$150 – $700</td></tr>
          <tr><td>Long-form YouTube video, scripted</td><td>$1,500 – $9,000</td></tr>
          <tr><td>Podcast episode, edited with clips</td><td>$400 – $1,800</td></tr>
          <tr><td>Full monthly retainer, 12–20 pieces</td><td>$5,000 – $30,000</td></tr>
        </tbody>
      </table>

      <h2 id="funnel">Funnel constants</h2>
      <table>
        <thead><tr><th>Metric</th><th>Benchmark</th></tr></thead>
        <tbody>
          <tr><td>Organic CTR, positions 1–3</td><td>24%</td></tr>
          <tr><td>Organic CTR, positions 4–10</td><td>6%</td></tr>
          <tr><td>Visitor → lead (content with a relevant offer)</td><td>2.2%</td></tr>
          <tr><td>Visitor → lead (no offer on page)</td><td>0.3% – 0.8%</td></tr>
          <tr><td>Lead → customer (B2B blended)</td><td>14%</td></tr>
        </tbody>
      </table>

      <h2 id="method">Methodology</h2>
      <p>Figures are assembled from public platform disclosures and payout terms, aggregated
      rate-card data contributed by creators and media buyers, publicly reported advertiser CPMs,
      and our own client work. Ranges are 20th to 80th percentile, not absolute extremes. They are
      refreshed quarterly and the raw constants file used by the calculators is served at
      <code>/assets/js/benchmarks.js</code> — read it, fork it, argue with it.</p>
      <p><strong>Citation:</strong> Content.Media, <em>2026 Creator Economy Benchmarks</em>,
      {SITE['base_url']}/benchmarks/ — free to cite and reproduce with a link.</p>
      {helpful_poll("benchmarks")}
    </article>
    <aside class="sidebar">
      {toc([("rpm", "YouTube RPM by niche"), ("geo", "Geography multipliers"),
            ("shorts", "Short-form pool rates"), ("engagement", "Engagement bands"),
            ("rates", "Sponsorship rate anchors"), ("podcast", "Podcast &amp; newsletter"),
            ("display", "Display RPM"), ("costs", "Production costs"),
            ("funnel", "Funnel constants"), ("method", "Methodology")])}
      {ad("sidebar", style="sidebar")}
      <div class="panel panel--compact">
        <h3 style="font-size:1rem">Need the raw dataset?</h3>
        <p class="small muted">CSV exports and custom cuts for analysts, journalists and agencies.</p>
        <a class="btn btn--primary btn--block" href="/contact/?topic=data">Request the data</a>
      </div>
    </aside>
  </div>
</section>
<section class="band band--alt"><div class="wrap">{newsletter_block()}</div></section>
{cta_band("Benchmarks tell you where you stand. We build the thing that moves you.",
          "Costed content plan in one business day.")}'''

    return page("2026 Creator Economy Benchmarks — RPM, Rates & Engagement Data | Content.Media",
                "Free creator economy benchmark database: YouTube RPM by niche, engagement rate "
                "bands, sponsorship rate anchors, podcast and newsletter CPM, display RPM.",
                "/benchmarks/", body, active="benchmarks",
                schema={"@context": "https://schema.org", "@type": "Dataset",
                        "name": "2026 Creator Economy Benchmarks",
                        "description": "RPM, engagement and sponsorship rate benchmarks for the creator economy.",
                        "url": SITE["base_url"] + "/benchmarks/",
                        "license": "https://creativecommons.org/licenses/by/4.0/",
                        "creator": {"@type": "Organization", "name": SITE["name"]},
                        "temporalCoverage": "2026"})


# ---------------------------------------------------------------------------
# Guides
# ---------------------------------------------------------------------------
def _heads(body_html):
    return [(m.group(1), re.sub("<[^>]+>", "", m.group(2)))
            for m in re.finditer(r'<h2 id="([^"]+)">(.*?)</h2>', body_html)]


def build_guide(g):
    others = [x for x in GUIDES if x["slug"] != g["slug"]][:3]
    rel = "".join(
        f'<article class="card"><span class="tag tag--brand">{o["cat"]}</span>'
        f'<h3><a class="stretch" href="/guides/{o["slug"]}/">{o["title"]}</a></h3>'
        f'<p>{o["desc"]}</p></article>' for o in others)

    body = f'''<section class="band" style="padding-bottom:1rem">
  <div class="wrap" style="max-width:860px">
    {breadcrumbs([("Home", "/"), ("Guides", "/guides/"), (g["cat"], "/guides/")])}
    <span class="eyebrow">{g["cat"]} &middot; {g["read"]} min read</span>
    <h1>{g["title"]}</h1>
    <p class="lede">{g["desc"]}</p>
    {byline()}
  </div>
</section>
<section class="band" style="padding-top:0">
  <div class="wrap article-layout">
    <article class="prose">
      <div class="callout"><h4>The short version</h4><p>{g["sum"]}</p></div>
      {ad("in_article")}
      {g["body"]}
      {ad("in_article")}
      {helpful_poll(g["slug"])}
    </article>
    <aside class="sidebar">
      {toc(_heads(g["body"]))}
      {ad("sidebar", style="sidebar")}
      <div class="panel panel--compact">
        <h3 style="font-size:1rem">Free weekly brief</h3>
        <p class="small muted">Benchmark changes and payout shifts, every Tuesday. Free.</p>
        <form class="cm-form" data-form="newsletter">
          <input name="email" type="email" required placeholder="you@company.com">
          <button class="btn btn--primary btn--block" type="submit" style="margin-top:.5rem">Subscribe</button>
          <div class="form-status" role="status" aria-live="polite"></div>
        </form>
      </div>
      <div class="panel panel--compact">
        <h3 style="font-size:1rem">Want this done for you?</h3>
        <p class="small muted">We build and run content programmes end to end.</p>
        <a class="btn btn--primary btn--block" href="/services/#quote">Get a costed plan</a>
      </div>
    </aside>
  </div>
</section>
<section class="band band--alt">
  <div class="wrap">
    {section_head("Keep reading", "Related guides", href="/guides/", link_label="All guides")}
    <div class="grid g3">{rel}</div>
  </div>
</section>
{cta_band("Stop reading about it. Have it built.",
          "Tell us the shape of the problem and we come back with scope and a number.")}'''

    schema = {"@context": "https://schema.org", "@type": "Article",
              "headline": g["title"], "description": g["desc"],
              "url": f"{SITE['base_url']}/guides/{g['slug']}/",
              "datePublished": "2026-09-01", "dateModified": "2026-09-21",
              "author": {"@type": "Organization", "name": SITE["name"]},
              "publisher": {"@type": "Organization", "name": SITE["name"]},
              "articleSection": g["cat"]}

    return page(f"{g['title']} | Content.Media", g["desc"],
                f"/guides/{g['slug']}/", body, active="guides", schema=schema)


def build_guides_hub():
    cats = sorted({g["cat"] for g in GUIDES})
    chips = "".join(f'<button class="chip" data-gfilter="{c}">{c}</button>' for c in cats)
    cards = "".join(
        f'<article class="card" data-cat="{g["cat"]}">'
        f'<span class="tag tag--brand">{g["cat"]}</span>'
        f'<h3><a class="stretch" href="/guides/{g["slug"]}/">{g["title"]}</a></h3>'
        f'<p>{g["desc"]}</p>'
        f'<div class="tool-card__foot" style="margin-top:.9rem"><span>{g["read"]} min read</span>'
        f'<span>Updated Sep 2026</span></div></article>' for g in GUIDES)

    body = f'''<section class="band">
  <div class="wrap">
    {breadcrumbs([("Home", "/"), ("Guides", "/guides/")])}
    <h1>Guides</h1>
    <p class="lede">Reference pages for people who make content for a living. Opinionated,
    specific, and updated when the numbers change. No gated PDFs.</p>
    <div class="chipset" style="margin:1.2rem 0">
      <button class="chip is-on" data-gfilter="all">All</button>{chips}
    </div>
    {ad("leaderboard", style="leaderboard")}
    <div class="grid g3" id="guideGrid">{cards}</div>
  </div>
</section>
<section class="band band--alt"><div class="wrap">{newsletter_block()}</div></section>
{cta_band("Want the version where we do the work?",
          "Costed content plan in one business day.")}
<script>
(function(){{
  var chips=[].slice.call(document.querySelectorAll('[data-gfilter]'));
  var cards=[].slice.call(document.querySelectorAll('#guideGrid [data-cat]'));
  chips.forEach(function(c){{c.addEventListener('click',function(){{
    chips.forEach(function(x){{x.classList.remove('is-on');}});c.classList.add('is-on');
    var f=c.dataset.gfilter;
    cards.forEach(function(k){{k.style.display=(f==='all'||k.dataset.cat===f)?'':'none';}});
  }});}});
}})();
</script>'''

    return page("Creator Economy Guides — Monetisation, Pricing, SEO & Operations | Content.Media",
                "Opinionated reference guides on AdSense approval, rate cards, newsletter "
                "monetisation, programmatic SEO, contests, AI workflows and more.",
                "/guides/", body, active="guides")


# ---------------------------------------------------------------------------
# Video library
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# Add real YouTube video IDs here and the library renders itself. Leave the list
# empty and the page shows an honest "channel launching" state rather than
# embedding placeholder videos.
#   ("VIDEO_ID", "Title", "Category", "12:34"),
# ---------------------------------------------------------------------------
VIDEOS = []

PLANNED = [
    ("How YouTube RPM really works", "Monetisation"),
    ("Pricing a sponsorship: live rate card build", "Pricing"),
    ("Getting approved for AdSense in 2026", "Monetisation"),
    ("Repurposing one video into twelve assets", "Operations"),
    ("Newsletter sponsorships: what to charge", "Pricing"),
    ("Programmatic SEO without a penalty", "SEO"),
]


def build_videos():
    if VIDEOS:
        cards = "".join(f'''<article class="video-card">
  <div class="video-embed" data-yt="{vid}" role="button" tabindex="0" aria-label="Play {title}">
    <img src="https://i.ytimg.com/vi/{vid}/hqdefault.jpg" alt="" loading="lazy" width="480" height="360">
    <span class="play"><span></span></span>
  </div>
  <div class="video-meta">
    <span class="tag tag--brand">{cat}</span>
    <h3 style="margin-top:.5rem">{title}</h3>
    <p>{dur} &middot; Content.Media</p>
  </div>
</article>''' for vid, title, cat, dur in VIDEOS)
    else:
        planned = "".join(
            f'<li><strong>{t}</strong> <span class="tag">{c}</span></li>' for t, c in PLANNED)
        cards = f'''<div class="panel" style="grid-column:1/-1">
  <h3 class="mt0">The channel is being built</h3>
  <p class="muted">Rather than pad this page with embedded videos that are not ours, here is what
  is actually in production. Each one walks through a benchmark or a calculator already published
  on this site.</p>
  <ul class="ticks">{planned}</ul>
  <p class="small muted">Subscribe below or on YouTube and the first one will reach you.</p>
</div>'''

    body = f'''<section class="band">
  <div class="wrap">
    {breadcrumbs([("Home", "/"), ("Video", "/videos/")])}
    <h1>Video library</h1>
    <p class="lede">Every benchmark and calculator on this site, explained on camera. Videos load
    only when you click them — no tracking cookies until you choose to play.
    <a href="{SITE['youtube_channel']}" rel="noopener" target="_blank">Subscribe on YouTube &rarr;</a></p>
    {ad("leaderboard", style="leaderboard")}
    <div class="video-grid">{cards}</div>
  </div>
</section>
<section class="band band--alt">
  <div class="wrap split">
    <div>
      <span class="eyebrow">Sponsor the channel</span>
      <h2>Reach an audience that buys tools and hires agencies</h2>
      <p class="lede">Pre-roll, integration and dedicated video formats, sold alongside the
      newsletter and the directory. Current audience figures are in the media kit and are
      refreshed monthly.</p>
      <a class="btn btn--primary btn--lg" href="/advertise/">See the media kit</a>
    </div>
    {newsletter_block(variant="narrow", heading="Get new videos by email",
                      sub="One email a week with the new video, the benchmark changes and anything "
                          "that moved in creator payouts.", magnet=False)}
  </div>
</section>
{cta_band("Prefer we just build it?", "Costed content plan in one business day.")}'''

    return page("Video Library — Creator Economy Explainers | Content.Media",
                "Video explainers on YouTube RPM, sponsorship pricing, AdSense approval, "
                "repurposing systems and programmatic SEO.",
                "/videos/", body, active="videos")


# ---------------------------------------------------------------------------
# Jobs board
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# Live job listings. Add approved postings here:
#   ("Role title", "Location", "Type", "Pay range", "Company")
# A posting without a pay range is not accepted — that rule is published on the
# board and applies to us too. An empty list renders an honest empty state.
# ---------------------------------------------------------------------------
JOBS = []


def build_jobs():
    rows = "".join(f'''<article class="job-row">
  <span class="tool-logo" style="background:linear-gradient(140deg,var(--brand),var(--accent))">{t[0]}</span>
  <div><h3>{t}</h3><p>{co} &middot; {loc} &middot; {typ}</p></div>
  <span class="job-pay">{pay}</span>
</article>''' for t, loc, typ, pay, co in JOBS) or '''<div class="panel">
  <h3 class="mt0">The board opens with its first posting</h3>
  <p class="muted">We are not filling this page with scraped listings or roles we cannot verify.
  Every posting here will be one a real employer paid to place, with a published salary range and
  a working application link.</p>
  <p><a class="btn btn--primary" href="/jobs/post/">Post the first role</a>
     <a class="btn btn--ghost" href="/newsletter/">Get roles by email instead</a></p>
</div>'''

    body = f'''<section class="band">
  <div class="wrap">
    {breadcrumbs([("Home", "/"), ("Jobs", "/jobs/")])}
    <h1>Creator economy jobs</h1>
    <p class="lede">Content, video, newsletter and SEO roles at companies that take content
    seriously. Every listing shows a salary range — postings without one are not accepted.</p>
    <div class="dir-toolbar">
      <input type="search" id="jobSearch" placeholder="Search roles, companies, locations…" aria-label="Search jobs">
      <a class="btn btn--primary" href="/jobs/post/">Post a job — $149</a>
    </div>
    {ad("leaderboard", style="leaderboard")}
    <div class="grid" id="jobList" style="gap:.7rem">{rows}</div>
    <p class="small muted" style="margin-top:1.2rem">Listings refresh weekly. Hiring?
    <a href="/jobs/post/">Post a role</a> — 30 days, newsletter inclusion, no agency spam.</p>
  </div>
</section>
<section class="band band--alt"><div class="wrap">
  {newsletter_block(heading="Jobs in your inbox",
    sub="New roles every Tuesday alongside the benchmark brief. No recruiter spam, ever.",
    magnet=False)}
</div></section>
{cta_band("Hiring a whole content function?",
          "Sometimes a retainer beats a headcount. We will tell you honestly which one you need.",
          ("Talk to us", "/services/#quote"), ("Post a job instead", "/jobs/post/"))}
<script>
(function(){{
  var s=document.getElementById('jobSearch'),rows=[].slice.call(document.querySelectorAll('#jobList .job-row'));
  if(!s)return;
  s.addEventListener('input',function(){{
    var q=s.value.toLowerCase();
    rows.forEach(function(r){{r.style.display=r.textContent.toLowerCase().indexOf(q)>-1?'':'none';}});
  }});
}})();
</script>'''

    return page("Creator Economy Jobs — Content, Video, Newsletter & SEO Roles | Content.Media",
                "Curated content, video, newsletter and SEO jobs. Every listing shows a salary range.",
                "/jobs/", body, active="jobs")


def build_post_job():
    form = simple_form("post-job", "Post a role", [
        {"name": "role_title", "label": "Role title", "type": "text", "required": True,
         "placeholder": "Senior Content Strategist"},
        {"name": "company", "label": "Company", "type": "text", "required": True,
         "placeholder": "Company name"},
        {"name": "company_url", "label": "Company website", "type": "url", "required": True,
         "placeholder": "https://"},
        {"name": "location", "label": "Location", "type": "text", "required": True,
         "placeholder": "Remote (US/EU), or city"},
        {"name": "employment_type", "label": "Employment type", "type": "select", "required": True,
         "options": ["Full-time", "Part-time", "Contract", "Freelance", "Internship"]},
        {"name": "salary_range", "label": "Salary range (required — no exceptions)", "type": "text",
         "required": True, "placeholder": "$90,000 – $120,000"},
        {"name": "category", "label": "Category", "type": "select", "required": True,
         "options": ["Content strategy", "Writing & editing", "Video", "Podcast", "SEO",
                     "Social & community", "Design", "Growth & analytics", "Leadership"]},
        {"name": "apply_url", "label": "Application URL", "type": "url", "required": True,
         "placeholder": "https://"},
        {"name": "description", "label": "Role description", "type": "textarea", "required": True,
         "placeholder": "What the person will actually do, and who they will work with."},
        {"name": "contact_email", "label": "Your email", "type": "email", "required": True,
         "placeholder": "you@company.com"},
        {"name": "package", "label": "Package", "type": "select", "required": True,
         "options": ["Standard — $149 (30 days + newsletter mention)",
                     "Featured — $299 (30 days, pinned, newsletter + social)",
                     "Bundle of 5 — $595 (valid 12 months)"]},
    ], button="Submit the role", note="We review every posting within one business day and send a "
       "payment link once approved. Listings without a salary range are declined.")

    body = f'''<section class="band">
  <div class="wrap article-layout">
    <article>
      {breadcrumbs([("Home", "/"), ("Jobs", "/jobs/"), ("Post a job", "/jobs/post/")])}
      <h1>Post a role</h1>
      <p class="lede">Reach content strategists, video producers, newsletter editors and SEO leads
      who read this site for the benchmarks. No agency spam, no listings without salary ranges.</p>
      <div class="tier-grid" style="margin:1.8rem 0">
        <div class="tier"><h3>Standard</h3><p class="tier-price">$149</p>
          <ul><li>30 days on the board</li><li>Mention in the weekly brief</li>
          <li>Indexed, permanent URL</li></ul>
          <a class="btn btn--ghost btn--block" href="#post-job-form">Choose standard</a></div>
        <div class="tier tier--hot"><h3>Featured</h3><p class="tier-price">$299</p>
          <ul><li>Everything in Standard</li><li>Pinned to the top for 7 days</li>
          <li>Highlighted card</li><li>Newsletter + social post</li></ul>
          <a class="btn btn--primary btn--block" href="#post-job-form">Choose featured</a></div>
        <div class="tier"><h3>Bundle of 5</h3><p class="tier-price">$595<small> /5 roles</small></p>
          <ul><li>Five standard listings</li><li>Valid 12 months</li>
          <li>Company profile page</li></ul>
          <a class="btn btn--ghost btn--block" href="#post-job-form">Choose bundle</a></div>
      </div>
      <div id="post-job-form">{form}</div>
    </article>
    <aside class="sidebar">
      {ad("sidebar", style="sidebar")}
      <div class="panel panel--compact">
        <h3 style="font-size:1rem">Audience</h3>
        <ul class="ticks small">
          <li>Content leads, founders and independent publishers</li>
          <li>People who came here to look up salary and rate benchmarks</li>
          <li>Current reach figures in the <a href="/advertise/">media kit</a></li>
        </ul>
        <a class="btn btn--ghost btn--block" href="/advertise/">Full media kit</a>
      </div>
    </aside>
  </div>
</section>'''

    return page("Post a Creator Economy Job | Content.Media",
                "Post a content, video, newsletter or SEO role to an audience of content leads "
                "and independent publishers. From $149.",
                "/jobs/post/", body, active="jobs")
