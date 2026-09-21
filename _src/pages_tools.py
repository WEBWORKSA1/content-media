# -*- coding: utf-8 -*-
"""The calculator cluster — the site's organic traffic engine."""
import json
from config import SITE
from layout import page, ad
from components import (breadcrumbs, section_head, faq, cta_band, newsletter_block,
                        helpful_poll, byline, toc, simple_form)

NICHE_OPTS = [
    ("finance", "Personal finance &amp; investing"), ("saas", "B2B software &amp; SaaS"),
    ("realestate", "Real estate &amp; mortgage"), ("marketing", "Marketing &amp; business"),
    ("tech", "Technology &amp; gadget reviews"), ("education", "Education &amp; how-to"),
    ("health", "Health, fitness &amp; wellness"), ("travel", "Travel"),
    ("food", "Food &amp; cooking"), ("beauty", "Beauty &amp; fashion"),
    ("gaming", "Gaming"), ("entertain", "Entertainment &amp; vlogs"),
    ("music", "Music"), ("kids", "Kids &amp; family"),
]
GEO_OPTS = [
    ("us", "Mostly United States"), ("tier1", "Mixed tier-1 (US/UK/CA/AU)"),
    ("europe", "Mostly Western Europe"), ("mixed", "Global mix"),
    ("tier3", "Mostly South Asia / SEA / LATAM"),
]


def _rng(name, label, mn, mx, step, default, suffix=""):
    return {"kind": "range", "name": name, "label": label, "min": mn, "max": mx,
            "step": step, "default": default, "suffix": suffix}


def _sel(name, label, options, default=None):
    return {"kind": "select", "name": name, "label": label, "options": options,
            "default": default}


def _numf(name, label, default, placeholder=""):
    return {"kind": "number", "name": name, "label": label, "default": default,
            "placeholder": placeholder}


TOOLS = {
"youtube-money-calculator": {
    "engine": "youtube",
    "h1": "YouTube money calculator",
    "title": "YouTube Money Calculator 2026 — Real RPM by Niche and Country",
    "desc": "Estimate YouTube AdSense earnings with published RPM ranges for 14 niches and "
            "5 audience geographies. Free, no sign-up, formula shown.",
    "intro": "Most YouTube earnings calculators multiply your views by one invented number. "
             "This one uses a published RPM range for your actual niche, applies an audience-geography "
             "factor, and accounts for the fact that only 55–78% of views ever serve a paid ad. "
             "The assumptions print underneath the result.",
    "inputs": [
        _rng("views", "Monthly views", 1000, 20000000, 1000, 250000),
        _sel("niche", "Content niche", NICHE_OPTS, "marketing"),
        _sel("geo", "Audience geography", GEO_OPTS, "tier1"),
        _rng("subs", "Subscribers", 0, 10000000, 100, 50000),
    ],
    "method": """
<h2 id="formula">The formula</h2>
<div class="code">monetised_views = monthly_views × monetised_share (0.55 – 0.78)
adsense_revenue = (monetised_views ÷ 1000) × niche_RPM × geography_multiplier</div>
<p>The RPM figures used are <strong>creator take-home</strong>, i.e. already net of YouTube's
45% share of in-stream advertising revenue. If a calculator quotes you a $30 "RPM" for gaming,
it is quoting the advertiser's CPM, not your payout.</p>
<h2 id="rpm">Why the range is so wide</h2>
<p>Three variables move YouTube RPM more than anything else, and none of them is subscriber count:</p>
<ul>
<li><strong>Niche.</strong> A finance channel and a music channel with identical view counts differ
by 10× in revenue, because advertisers bidding on finance are buying a customer worth thousands.</li>
<li><strong>Audience geography.</strong> A view from the United States is worth roughly 4–5× a view
from a tier-3 market. This is the single most common reason a creator's real earnings come in below
every calculator they tried.</li>
<li><strong>Format and length.</strong> Long-form video with mid-roll breaks carries multiple ad
impressions per view. Shorts pay from a pool at roughly 1–3% of that rate — use the
<a href="/tools/youtube-shorts-rpm-calculator/">Shorts calculator</a> instead.</li>
</ul>
<h2 id="beyond">AdSense is the floor, not the ceiling</h2>
<p>On a healthy channel, advertising is typically 25–45% of total revenue. The bar chart in the
result models the other rails: sponsorships priced from our
<a href="/tools/creator-rate-card-calculator/">rate card builder</a>, channel memberships at a
realistic 0.4% conversion, and affiliate income. If AdSense is 90% of your revenue you do not have
a business, you have a lottery ticket tied to one algorithm.</p>
""",
    "faq": [
        ("How much does YouTube pay per 1,000 views in 2026?",
         "<p>Between roughly $1.00 and $38.00 to the creator, depending almost entirely on niche and "
         "audience country. Personal finance and B2B software sit at the top ($14–$38). Gaming, music "
         "and general entertainment sit at the bottom ($1.00–$6.00). The often-quoted '$3–$5 per 1,000 "
         "views' is a global average that describes almost nobody accurately.</p>"),
        ("How many views do I need to make $1,000 a month?",
         "<p>In a marketing or business niche at a $10–$26 RPM with a tier-1 audience, roughly 55,000 "
         "to 145,000 monthly views. In gaming at a $1.20–$5.50 RPM, 250,000 to 1.1 million. Set the "
         "calculator to your niche and drag the view slider until the monthly figure reads $1,000.</p>"),
        ("Do I need 1,000 subscribers to earn anything?",
         "<p>For the YouTube Partner Programme, yes — 1,000 subscribers plus 4,000 valid public watch "
         "hours in 12 months, or 10 million valid Shorts views in 90 days. But sponsorships, affiliate "
         "income and memberships have no threshold at all, and micro-channels routinely out-earn "
         "mid-size channels on brand deals because their engagement is higher.</p>"),
        ("Why is my real RPM lower than this estimate?",
         "<p>Four usual causes: a large share of views from low-CPM countries; a high proportion of "
         "Shorts inside your total view count; heavy ad-blocker usage in a tech-literate audience; or "
         "videos flagged as limited-monetisation. Check the geography breakdown in YouTube Analytics "
         "first — it explains the gap about 70% of the time.</p>"),
        ("Is this calculator accurate?",
         "<p>It is a model, and it prints its assumptions so you can audit them. Treat the range as a "
         "planning band, not a forecast. If your actual RPM sits outside the range for your niche and "
         "geography, something structural is different about your channel and it is worth investigating.</p>"),
    ],
},

"youtube-shorts-rpm-calculator": {
    "engine": "shorts",
    "h1": "YouTube Shorts RPM calculator",
    "title": "YouTube Shorts RPM Calculator — What Shorts Actually Pay in 2026",
    "desc": "Estimate YouTube Shorts revenue from the creator pool, and see what the same view "
            "count would have earned as long-form video.",
    "intro": "Shorts do not run classic in-stream ads. They pay from a revenue pool, after music "
             "licensing is deducted, at a rate 30–100× below long-form video. This calculator shows "
             "you both numbers side by side, because the gap is the entire strategic argument.",
    "inputs": [
        _rng("views", "Monthly Shorts views", 10000, 100000000, 10000, 2000000),
        _sel("geo", "Audience geography", GEO_OPTS, "tier1"),
    ],
    "method": """
<h2 id="formula">How Shorts monetisation works</h2>
<div class="code">pool_revenue = ads_served_between_shorts − music_licensing_costs
creator_share  = 45% of the allocated pool
effective_RPM  = $0.03 – $0.12 per 1,000 views (tier-1)</div>
<p>Two things follow from that structure. First, your payout is diluted by every other creator in
the pool, so it moves even when your own performance does not. Second, using licensed music directly
reduces your share, because licensing is deducted before allocation.</p>
<h2 id="strategy">What Shorts are actually for</h2>
<p>Shorts are a discovery instrument, not a revenue instrument. The third bar in the result shows
what the same view count would have earned as long-form. If you are running Shorts without a
long-form catalogue, a newsletter or a product to convert that attention into, you are renting
an audience and paying for the privilege.</p>
<ul>
<li>End every Short on an unresolved question the long-form video answers.</li>
<li>Pin a comment linking the full video — it outperforms an on-screen card.</li>
<li>Track <em>viewed-to-subscribed</em> per Short, not view count. A Short with 2M views and 40 subs is a failure.</li>
<li>Repurpose in one direction only: long-form first, then cut. The reverse produces thin long-form.</li>
</ul>
""",
    "faq": [
        ("What is a good RPM for YouTube Shorts?",
         "<p>$0.03 to $0.12 per 1,000 views for a tier-1 audience. A million Shorts views is typically "
         "$30–$120. The same million views on long-form in the same niche would be $1,000–$12,000.</p>"),
        ("Do Shorts count towards YouTube Partner Programme requirements?",
         "<p>Yes, via a separate threshold: 1,000 subscribers plus 10 million valid public Shorts views "
         "in the preceding 90 days, as an alternative to 4,000 watch hours.</p>"),
        ("Does using popular music reduce my Shorts revenue?",
         "<p>Yes. Music licensing is deducted from the pool before creator allocation, so tracks with "
         "licensing costs reduce the amount available to share. Original or library audio avoids that deduction.</p>"),
        ("Should I stop making Shorts?",
         "<p>No — but stop treating them as a revenue line. Judge them on subscriber conversion and "
         "long-form click-through. If a Short does not move either, it earned you roughly $6 per million "
         "views and cost you a production day.</p>"),
    ],
},

"tiktok-earnings-calculator": {
    "engine": "tiktok",
    "h1": "TikTok earnings calculator",
    "title": "TikTok Money Calculator 2026 — Engagement-Weighted Sponsorship Rates",
    "desc": "Work out your TikTok engagement rate and what a sponsored video should cost, "
            "weighted by engagement rather than raw follower count.",
    "intro": "Brands do not buy followers, they buy attention. This calculator derives your "
             "engagement rate from likes, videos and followers, compares it to the benchmark band "
             "for your tier, and prices a sponsored video accordingly.",
    "inputs": [
        _rng("followers", "Followers", 500, 20000000, 500, 50000),
        _rng("likes", "Total likes across the account", 1000, 500000000, 1000, 850000),
        _rng("videos", "Total videos published", 1, 3000, 1, 120),
        _rng("monthlyViews", "Monthly views", 0, 100000000, 10000, 1500000),
        _sel("niche", "Niche", [("generic", "General / lifestyle"), ("b2b", "B2B / professional"),
                                ("finance", "Finance"), ("tech", "Technology"),
                                ("beauty", "Beauty"), ("gaming", "Gaming"),
                                ("entertainment", "Entertainment")], "generic"),
    ],
    "method": """
<h2 id="formula">Engagement rate formula</h2>
<div class="code">ER = (total_likes ÷ (followers × total_videos)) × 100</div>
<p>This is the account-level formula brands and agencies use when they cannot see your analytics.
It is deliberately conservative — it divides by every video you have ever posted, including the
ones that flopped. A per-video ER calculated on your last nine posts will read higher, and that is
the number you should put in a media kit, with the method stated.</p>
<h2 id="bands">Benchmark bands by tier</h2>
<table>
<thead><tr><th>Follower tier</th><th>Typical ER</th><th>What it means</th></tr></thead>
<tbody>
<tr><td>Under 5K</td><td>12.0% – 18.0%</td><td>Highest intimacy, smallest reach</td></tr>
<tr><td>5K – 10K</td><td>10.5% – 15.0%</td><td>The sweet spot for first brand deals</td></tr>
<tr><td>10K – 50K</td><td>9.0% – 13.5%</td><td>Micro tier; agencies start calling</td></tr>
<tr><td>50K – 100K</td><td>8.0% – 12.0%</td><td>Rate cards become negotiable</td></tr>
<tr><td>100K – 1M</td><td>7.0% – 11.0%</td><td>Macro; usage rights matter most here</td></tr>
<tr><td>1M+</td><td>6.0% – 10.5%</td><td>Reach play; ER naturally compresses</td></tr>
</tbody></table>
<h2 id="rates">How to use the number in a negotiation</h2>
<p>Send the high end of the range, itemised. Never quote a single figure and never quote a single
deliverable — a bundle closes at a higher blended rate and stops the buyer line-item shopping you
against a cheaper account. Our <a href="/tools/creator-rate-card-calculator/">rate card builder</a>
adds usage rights and exclusivity, which is where most creators leave 40% on the table.</p>
""",
    "faq": [
        ("What is a good engagement rate on TikTok?",
         "<p>Above 9% for an account under 100K followers, above 7% above that. TikTok engagement runs "
         "far higher than Instagram because the feed is interest-based rather than follow-based. "
         "An ER below 4% on TikTok suggests bought followers or a dead account.</p>"),
        ("How much do brands pay per TikTok video?",
         "<p>Roughly $10–$26 per 1,000 followers for a general audience, before niche, usage and "
         "exclusivity multipliers. A 50K-follower creator with healthy engagement in a general niche "
         "is in the $500–$1,300 band; the same account in B2B or finance is 1.5–1.6× that.</p>"),
        ("Does the TikTok Creator Rewards programme pay well?",
         "<p>Around $0.02–$0.06 per 1,000 qualified views, and only on videos over one minute that meet "
         "originality requirements. It is a rounding error next to brand deals and TikTok Shop commission. "
         "Build the account for deals and commerce, not for the fund.</p>"),
        ("Should I show my engagement rate in a media kit?",
         "<p>Yes, with the formula written next to it. Stating your method is a credibility signal to "
         "media buyers, most of whom have been burned by inflated numbers.</p>"),
    ],
},

"instagram-engagement-calculator": {
    "engine": "instagram",
    "h1": "Instagram engagement rate & rate calculator",
    "title": "Instagram Engagement Rate Calculator 2026 + Sponsored Post Pricing",
    "desc": "Calculate your Instagram engagement rate, compare it to the benchmark for your "
            "follower tier, and price reels, posts and stories.",
    "intro": "Your engagement rate against the benchmark for your tier is a direct rate multiplier. "
             "Beat the band and you can defensibly charge above the card. This tool does both halves: "
             "the rate, then the price.",
    "inputs": [
        _rng("followers", "Followers", 500, 20000000, 500, 25000),
        _rng("likes", "Average likes per post", 0, 2000000, 10, 900),
        _rng("comments", "Average comments per post", 0, 100000, 1, 45),
        _sel("niche", "Niche", [("generic", "General / lifestyle"), ("b2b", "B2B / professional"),
                                ("finance", "Finance"), ("tech", "Technology"),
                                ("beauty", "Beauty"), ("gaming", "Gaming"),
                                ("entertainment", "Entertainment")], "generic"),
    ],
    "method": """
<h2 id="formula">Formula</h2>
<div class="code">ER = ((average_likes + average_comments) ÷ followers) × 100</div>
<p>Use your last nine to twelve non-sponsored posts. Excluding sponsored posts matters: they
typically under-perform organic by 20–35%, and including them understates your real audience health.</p>
<h2 id="bands">Instagram engagement benchmarks, 2026</h2>
<table>
<thead><tr><th>Tier</th><th>Benchmark ER</th><th>Sponsored post band</th></tr></thead>
<tbody>
<tr><td>Nano, under 1K</td><td>6.5% – 8.5%</td><td>$10 – $100</td></tr>
<tr><td>Nano, 1K – 5K</td><td>4.8% – 6.4%</td><td>$50 – $250</td></tr>
<tr><td>Micro, 5K – 10K</td><td>3.4% – 4.6%</td><td>$100 – $400</td></tr>
<tr><td>Micro, 10K – 100K</td><td>2.0% – 3.2%</td><td>$200 – $2,500</td></tr>
<tr><td>Macro, 100K – 1M</td><td>1.4% – 2.2%</td><td>$2,000 – $12,000</td></tr>
<tr><td>Mega, 1M+</td><td>1.0% – 1.7%</td><td>$10,000+</td></tr>
</tbody></table>
<p>Engagement falls as follower count rises. That is normal and expected — it is not a sign your
account is dying. What matters is where you sit <em>relative to your own tier</em>, which is what the
multiplier in the result measures.</p>
<h2 id="bundle">Always quote the bundle</h2>
<p>The result gives you reel, post and story rates separately and then a recommended bundle. Quote
the bundle. It raises the blended rate, it gives the buyer one number to approve, and it removes
the line-by-line comparison that always ends with you discounting.</p>
""",
    "faq": [
        ("What is a good Instagram engagement rate in 2026?",
         "<p>Around 3% is the platform-wide average. Under 10K followers, 4%+ is healthy. Between 10K "
         "and 100K, 2.4% is the benchmark. Above 1M, anything over 1.4% is strong. Judge yourself "
         "against your tier, not against a nano account.</p>"),
        ("Should reels and static posts be priced the same?",
         "<p>No. Reels command roughly 1.5× a static in-feed post because they reach non-followers. "
         "Stories are the cheapest per frame but sell in threes and drive the most measurable click-through.</p>"),
        ("How do I raise my engagement rate?",
         "<p>Post fewer, better. Engagement rate is a ratio — publishing more mediocre posts lowers it. "
         "Reply to every comment in the first hour, ask a question that costs the reader nothing to "
         "answer, and cut posting frequency until average performance rises.</p>"),
        ("Do brands check engagement rate themselves?",
         "<p>Almost always, through a third-party audit tool, and they will also check your follower "
         "growth curve for spikes. Inflated followers are detected immediately and end the conversation.</p>"),
    ],
},

"creator-rate-card-calculator": {
    "engine": "ratecard",
    "h1": "Creator rate card builder",
    "title": "Creator Rate Card Calculator — Price Sponsorships With Usage Rights",
    "desc": "Build a defensible sponsorship rate card across 11 deliverable types, with niche, "
            "engagement, usage rights and exclusivity priced in.",
    "intro": "Most creators price a post and give away the two things worth the most money: paid "
             "usage rights and category exclusivity. This builder prices them explicitly, so you can "
             "see exactly what you are handing over when a brand asks for 'perpetual usage'.",
    "inputs": [
        _rng("followers", "Followers / subscribers on the platform", 500, 20000000, 500, 40000),
        _sel("asset", "Deliverable", [
            ("instagram_reel", "Instagram Reel"), ("instagram_post", "Instagram in-feed post"),
            ("instagram_story", "Instagram Story frame"), ("tiktok_video", "TikTok video"),
            ("youtube_integration", "YouTube integration (60–90s)"),
            ("youtube_dedicated", "YouTube dedicated video"), ("youtube_short", "YouTube Short"),
            ("x_post", "X / Twitter post"), ("linkedin_post", "LinkedIn post"),
            ("newsletter_slot", "Newsletter primary slot"), ("podcast_midroll", "Podcast mid-roll")],
            "youtube_integration"),
        _rng("quantity", "Number of deliverables", 1, 20, 1, 1),
        _rng("engagement", "Your engagement rate (%)", 0.2, 25, 0.1, 4.0),
        _sel("niche", "Niche", [("generic", "General / lifestyle"), ("b2b", "B2B / professional"),
                                ("finance", "Finance"), ("tech", "Technology"),
                                ("beauty", "Beauty"), ("gaming", "Gaming"),
                                ("entertainment", "Entertainment")], "generic"),
        _sel("usage", "Paid usage rights", [
            ("organic", "Organic only — no paid amplification"),
            ("whitelist_30d", "Whitelisting / paid ads, 30 days"),
            ("whitelist_90d", "Whitelisting / paid ads, 90 days"),
            ("perpetual", "Perpetual, all channels")], "organic"),
        _sel("exclusivity", "Category exclusivity", [
            ("none", "None"), ("cat_30d", "Category exclusive, 30 days"),
            ("cat_90d", "Category exclusive, 90 days"),
            ("cat_1y", "Category exclusive, 12 months")], "none"),
    ],
    "method": """
<h2 id="formula">The pricing model</h2>
<div class="code">base = (followers ÷ 1000) × asset_rate
rate = base × niche_mod × usage_mod × exclusivity_mod × engagement_mod × quantity
      (−12% when quantity ≥ 3)</div>
<h2 id="multipliers">The multipliers that actually matter</h2>
<table>
<thead><tr><th>Lever</th><th>Multiplier</th><th>Why</th></tr></thead>
<tbody>
<tr><td>B2B / professional niche</td><td>×1.55</td><td>Higher customer value behind every impression</td></tr>
<tr><td>Finance niche</td><td>×1.60</td><td>Highest advertiser competition of any category</td></tr>
<tr><td>Paid usage, 30 days</td><td>×1.35</td><td>Your face becomes their ad creative</td></tr>
<tr><td>Paid usage, 90 days</td><td>×1.60</td><td>A quarter of paid media off your likeness</td></tr>
<tr><td>Perpetual usage</td><td>×2.10</td><td>Never grant this inside a base fee. Ever.</td></tr>
<tr><td>Category exclusivity, 12 months</td><td>×1.80</td><td>You are declining every competitor for a year</td></tr>
</tbody></table>
<h2 id="negotiation">How to send it</h2>
<ol>
<li><strong>Send the high end.</strong> Buyers expect to negotiate 10–25% off the opening number. Anchor accordingly.</li>
<li><strong>Itemise the rights.</strong> Show the base fee and the usage fee as separate lines, so removing the rights removes the cost rather than the deal.</li>
<li><strong>Put a floor in writing for yourself.</strong> The result prints a walk-away number at 80% of the low end. Below that, decline — a cheap deal sets your price for every future buyer in that category.</li>
<li><strong>Charge for the second and third round of revisions.</strong> Two included, then hourly.</li>
<li><strong>Net 30, 50% up front for anything over $5,000.</strong> Non-negotiable with new clients.</li>
</ol>
""",
    "faq": [
        ("What should I charge per 1,000 followers?",
         "<p>As a starting anchor: Instagram Reels $12–$30, TikTok $10–$26, YouTube integrations $18–$55, "
         "YouTube dedicated videos $30–$90, LinkedIn posts $15–$45, newsletter slots $25–$90 per 1,000 "
         "<em>opens</em>. Then apply the niche and rights multipliers — they move the number more than the base does.</p>"),
        ("What are usage rights and why do they cost extra?",
         "<p>Usage rights let the brand run your content as paid advertising. That converts an organic "
         "post reaching your audience into ad creative reaching millions, using your face and your "
         "credibility. Perpetual all-channel usage is worth roughly double the organic fee, and it is "
         "the single most common thing creators give away for free.</p>"),
        ("Should I ever work for free product?",
         "<p>Only when the product retail value clearly exceeds your calculated rate and you wanted the "
         "product anyway. 'Exposure' is not consideration. Gifting is a marketing expense for the brand; "
         "treat it as one.</p>"),
        ("How do I justify my rate when the brand says it's too high?",
         "<p>Send the working, not the number: engagement rate versus tier benchmark, audience geography "
         "and demographics, past campaign click-through or promo-code redemptions. Buyers discount vibes. "
         "They rarely discount a spreadsheet.</p>"),
        ("Do rates differ by country?",
         "<p>Substantially — rates track where your <em>audience</em> is, not where you are. A creator in "
         "Manila with a 70% US audience prices against US rates. Apply a 0.3–0.5 factor for audiences "
         "concentrated in low-CPM markets.</p>"),
    ],
},

"cpm-rpm-cpc-calculator": {
    "engine": "cpm",
    "h1": "CPM, RPM, CPC & ROAS calculator",
    "title": "CPM RPM CPC CTR ROAS Calculator — All Ad Metrics in One Tool",
    "desc": "Convert between CPM, RPM, CPC, CTR, CPA and ROAS, and work out page RPM and revenue "
            "per session for a publisher site.",
    "intro": "Eight advertising metrics, one set of inputs. Publishers should be watching RPM and "
             "revenue per session; buyers should be watching CPA and ROAS. Everyone confuses CPM with RPM.",
    "inputs": [
        _numf("impressions", "Ad impressions", 500000),
        _numf("spend", "Ad spend or cost ($)", 4200),
        _numf("clicks", "Clicks", 6500),
        _numf("conversions", "Conversions", 140),
        _numf("revenue", "Revenue attributed ($)", 18500),
        _numf("pageviews", "Pageviews", 420000),
        _numf("sessions", "Sessions", 260000),
    ],
    "method": """
<h2 id="formula">Every formula on one screen</h2>
<div class="code">CPM  = (spend ÷ impressions) × 1000
RPM  = (revenue ÷ pageviews) × 1000
CPC  = spend ÷ clicks
CTR  = (clicks ÷ impressions) × 100
CPA  = spend ÷ conversions
ROAS = revenue ÷ spend
RPS  = revenue ÷ sessions</div>
<h2 id="difference">CPM versus RPM, once and for all</h2>
<p><strong>CPM</strong> is what an advertiser pays per thousand <em>ad impressions</em>. <strong>RPM</strong>
is what a publisher earns per thousand <em>pageviews</em>. They are different denominators. A page
carrying three ad units at a $12 CPM produces roughly a $36 page RPM at 100% fill — which is why
comparing your RPM to someone else's CPM tells you nothing.</p>
<h2 id="benchmarks">Display RPM benchmarks by category</h2>
<table>
<thead><tr><th>Category</th><th>Page RPM, tier-1 traffic</th></tr></thead>
<tbody>
<tr><td>Finance &amp; insurance</td><td>$28 – $60</td></tr>
<tr><td>B2B software / SaaS</td><td>$26 – $62</td></tr>
<tr><td>Technology</td><td>$20 – $44</td></tr>
<tr><td>Marketing &amp; business</td><td>$18 – $42</td></tr>
<tr><td>Health</td><td>$14 – $34</td></tr>
<tr><td>Education</td><td>$9 – $20</td></tr>
<tr><td>General / lifestyle</td><td>$5 – $12</td></tr>
<tr><td>Entertainment</td><td>$3 – $9</td></tr>
</tbody></table>
<p>These assume a tier-1 traffic mix. At 30% US traffic, expect roughly a third of these figures.
A realistic expectation for a new marketing site with mixed geography is $8–$20 page RPM, not the
headline numbers you see quoted in case studies.</p>
<h2 id="lever">The cheapest revenue lever you have</h2>
<p>Pages per session is in the result for a reason. Raising it from 1.2 to 1.8 raises revenue per
session by 50% with no new traffic and no new ad units. Internal linking, a "most read" module and
a related-tools strip at the end of every page are the three highest-return changes on any
content site.</p>
""",
    "faq": [
        ("What is a good CTR for display advertising?",
         "<p>0.05%–0.15% for standard display. Native and in-feed placements run 0.3%–1.0%. Search ads "
         "are a different universe at 2%–6%. If your display CTR is above 1%, check for accidental "
         "clicks — that is a policy risk, not a win.</p>"),
        ("What ROAS should I target?",
         "<p>Break-even depends on margin. At a 50% gross margin, 2.0× ROAS is break-even and 3.0×+ is "
         "healthy. E-commerce with thin margins often needs 4×–6×. For a subscription product, judge "
         "on payback period against LTV instead.</p>"),
        ("How do I increase page RPM without more traffic?",
         "<p>Three levers, in order of return: raise pages per session with internal linking; shift "
         "traffic mix toward tier-1 countries by targeting higher-value search terms; and add a "
         "high-viewability in-content unit above the fold. Adding more ad units below the fold is the "
         "worst of the options and risks a policy strike.</p>"),
        ("Why is my RPM lower on mobile?",
         "<p>Fewer viewable units, lower average viewability, and a heavier share of low-intent social "
         "traffic. A 30–45% gap between desktop and mobile RPM is normal.</p>"),
    ],
},

"podcast-sponsorship-calculator": {
    "engine": "podcast",
    "h1": "Podcast sponsorship calculator",
    "title": "Podcast Sponsorship Rate Calculator — Pre-roll, Mid-roll & Post-roll CPM",
    "desc": "Price podcast ad inventory on IAB v2.1 downloads with real CPM ranges by slot "
            "position and host-read premium.",
    "intro": "Podcast advertising is sold on downloads, per slot, on a CPM basis. Position matters "
             "more than most hosts realise: a mid-roll is worth roughly double a post-roll.",
    "inputs": [
        _rng("downloads", "Average downloads per episode (30-day, IAB v2.1)", 100, 2000000, 100, 12000),
        _rng("episodes", "Episodes per month", 1, 30, 1, 4),
        _rng("preroll", "Pre-roll slots per episode", 0, 3, 1, 1),
        _rng("midroll", "Mid-roll slots per episode", 0, 4, 1, 2),
        _rng("postroll", "Post-roll slots per episode", 0, 2, 1, 1),
        _sel("hostread", "Host-read or produced spot?",
             [("yes", "Host-read (+35%)"), ("no", "Produced / dynamic insertion")], "yes"),
    ],
    "method": """
<h2 id="cpm">CPM by slot position</h2>
<table>
<thead><tr><th>Slot</th><th>CPM range</th><th>Notes</th></tr></thead>
<tbody>
<tr><td>Pre-roll</td><td>$15 – $25</td><td>Highest delivery, lowest attention</td></tr>
<tr><td>Mid-roll</td><td>$22 – $40</td><td>The premium inventory. Sell these first.</td></tr>
<tr><td>Post-roll</td><td>$10 – $18</td><td>Bundle it; rarely sells alone</td></tr>
</tbody></table>
<p>Host-read spots carry a ~35% premium over produced or dynamically inserted spots, because the
endorsement is the product. That premium disappears if you read copy you obviously do not believe.</p>
<h2 id="downloads">Count downloads honestly</h2>
<p>Use IAB Tech Lab v2.1 certified numbers: unique downloads in the first 30 days, filtered for bots
and partial requests. Anything else — raw requests, lifetime totals, "listens" — is not sellable
inventory, and a buyer with an agency behind them will catch it on the first reconciliation.</p>
<h2 id="selling">Selling above the calculator</h2>
<ul>
<li><strong>Sell quarters, not episodes.</strong> A 12-episode package at a 10% discount beats
chasing four one-offs, and advertisers need frequency to see a result anyway.</li>
<li><strong>Offer a promo code or vanity URL.</strong> Attribution is podcasting's weakness; solving
it for the buyer is worth more than a CPM point.</li>
<li><strong>Publish audience composition.</strong> Job titles and seniority move B2B rates more than
download counts do. A 4,000-download show with a room full of CTOs outsells a 40,000-download
general-interest show.</li>
<li><strong>Bundle the newsletter and the YouTube cut.</strong> Price the bundle with our
<a href="/tools/newsletter-sponsorship-calculator/">newsletter calculator</a>.</li>
</ul>
""",
    "faq": [
        ("How many downloads do I need to get sponsors?",
         "<p>Networks typically start around 5,000 downloads per episode. Direct sales work far earlier "
         "— at 1,000 downloads in a tight B2B niche you can sell a quarter-long package to a relevant "
         "vendor at a premium CPM, because the audience is precisely the one they want.</p>"),
        ("Should I use dynamic ad insertion?",
         "<p>Yes, once you have a back catalogue. It lets you sell the archive and swap expired "
         "campaigns out. Keep host-read copy for your best inventory and use DAI for the rest.</p>"),
        ("What's a realistic fill rate?",
         "<p>Independent shows selling direct run at 30–60% fill. Assume 50% when you model revenue, "
         "and treat the calculator's output as gross inventory value, not guaranteed revenue.</p>"),
        ("Do video podcasts earn more?",
         "<p>They earn from more places — YouTube ads, Shorts clips, and higher sponsorship rates for "
         "on-screen product placement. Production cost rises roughly 40–60%. It is usually worth it "
         "above 5,000 downloads.</p>"),
    ],
},

"newsletter-sponsorship-calculator": {
    "engine": "newsletter",
    "h1": "Newsletter sponsorship calculator",
    "title": "Newsletter Sponsorship Rate Calculator — Price on Opens, Not List Size",
    "desc": "Price newsletter ad slots on opens with CPM ranges for classified, primary and "
            "dedicated placements, plus the B2B premium.",
    "intro": "Sell on opens, never on list size. Advertisers who buy on sends and get burned once "
             "never come back, and word travels fast in a small market.",
    "inputs": [
        _rng("subscribers", "Subscribers", 500, 5000000, 500, 25000),
        _rng("openrate", "Open rate (%)", 5, 90, 1, 42),
        _rng("issues", "Issues per month", 1, 30, 1, 4),
        _sel("slot", "Placement", [
            ("classified", "Classified / text link"),
            ("primary", "Primary sponsor slot"),
            ("dedicated", "Dedicated send")], "primary"),
        _sel("audience", "Audience type",
             [("consumer", "Consumer / general"), ("b2b", "B2B decision-makers (+80%)")], "consumer"),
    ],
    "method": """
<h2 id="cpm">CPM by placement, on opens</h2>
<table>
<thead><tr><th>Placement</th><th>CPM on opens</th><th>Format</th></tr></thead>
<tbody>
<tr><td>Classified / text link</td><td>$8 – $18</td><td>One line, 2–4 per issue</td></tr>
<tr><td>Primary sponsor slot</td><td>$25 – $60</td><td>One per issue, ~350 characters + image + tracked link</td></tr>
<tr><td>Dedicated send</td><td>$45 – $120</td><td>Whole email; cap at one per month</td></tr>
</tbody></table>
<p>B2B decision-maker audiences carry roughly an 80% premium. A 12,000-subscriber operations
newsletter read by heads of function outsells a 100,000-subscriber consumer list, and both sides
know it.</p>
<h2 id="mediakit">The media kit is a lead magnet</h2>
<p>Publish four numbers openly — subscribers, open rate, click rate, audience composition — and gate
the full rate card behind a short form. The form captures the advertiser as a lead; the open numbers
pre-qualify them so you stop taking calls from people who cannot afford you. Copy the structure:</p>
<ul>
<li>Three headline metrics above the fold, with growth rate</li>
<li>Audience composition: seniority, function, company size, country split</li>
<li>Format specs with exact character limits and image dimensions</li>
<li>A price floor and a minimum term — "from $X per issue, three-issue minimum"</li>
<li>A logo wall of past sponsors, and a waitlist line if you are booked</li>
</ul>
<h2 id="ethics">Two rules that protect the asset</h2>
<p>Label every sponsored slot unambiguously, and cap sponsored volume at one primary slot per issue.
The list is the asset; a burned list cannot be rebuilt with money.</p>
""",
    "faq": [
        ("How much can I charge for a newsletter sponsorship?",
         "<p>A 25,000-subscriber list at a 42% open rate has ~10,500 opens. At a $25–$60 primary-slot "
         "CPM that is $263–$630 per issue, or $1,050–$2,520 a month at weekly cadence. Double it for "
         "a B2B decision-maker audience.</p>"),
        ("Should I price on subscribers or opens?",
         "<p>Opens. Pricing on list size rewards you for dead addresses and punishes you for cleaning "
         "the list. Sophisticated buyers price on opens regardless of what you quote, so quoting it "
         "first makes you look like you know the market.</p>"),
        ("How many sponsors per issue is too many?",
         "<p>One primary plus two classifieds is the ceiling before unsubscribes rise measurably. "
         "Dedicated sends should be capped at one a month and clearly labelled.</p>"),
        ("What open rate should I report after privacy changes?",
         "<p>Report it, state that it includes Apple Mail Privacy Protection inflation, and lead with "
         "click rate as the honest engagement metric. Buyers respect the disclosure and it defuses "
         "the objection before they raise it.</p>"),
    ],
},

"content-roi-calculator": {
    "engine": "roi",
    "h1": "Content marketing ROI calculator",
    "title": "Content Marketing ROI Calculator — Pipeline, Ad Revenue & Payback",
    "desc": "Model organic traffic, leads, customers, ad revenue and payback period for a content "
            "programme, with every funnel assumption published.",
    "intro": "Content is an asset purchase with a delayed return. This model takes your keyword "
             "volume, production cost and close rate and gives you traffic, leads, pipeline, ad "
             "revenue, cost per customer and payback period.",
    "inputs": [
        _rng("pieces", "Pieces of content per month", 1, 100, 1, 8),
        _rng("cost", "Cost per piece ($)", 50, 10000, 50, 650),
        _rng("searchvol", "Average monthly searches per target keyword", 50, 100000, 50, 1200),
        _sel("rank", "Realistic ranking position",
             [("top3", "Top 3 (24% CTR)"), ("top10", "Positions 4–10 (6% CTR)")], "top10"),
        _rng("dealvalue", "Average deal or order value ($)", 10, 100000, 10, 2400),
        _rng("closerate", "Lead-to-customer close rate (%)", 1, 60, 1, 14),
        _rng("months", "Programme length (months)", 3, 36, 1, 12),
    ],
    "method": """
<h2 id="formula">Published assumptions</h2>
<div class="code">visitors  = pieces × search_volume × CTR
leads     = visitors × 2.2%            (visitor → lead)
customers = leads × close_rate
pipeline  = customers × deal_value
ad_rev    = (visitors ÷ 1000) × $18–$42 page RPM</div>
<p>Change any of these in the inputs. The 2.2% visitor-to-lead rate is a blended B2B benchmark for
content with a relevant offer attached; a page with no offer converts at 0.3–0.8%, which is the
real reason most content programmes look like they failed.</p>
<h2 id="honest">This model is deliberately pessimistic</h2>
<p>It treats every month as flat. Real content programmes compound: pages published in month one
keep earning in month eighteen, internal links lift older pages, and topical authority raises the
ceiling for everything published afterwards. A 12-month flat model typically understates a
well-run programme's third-year return by 2–4×.</p>
<h2 id="twoways">Content pays twice</h2>
<p>The bar chart separates <strong>pipeline revenue</strong> from <strong>display ad revenue</strong>.
Most brands ignore the second entirely, which is a mistake once a site clears 100,000 monthly
sessions — at an $18–$42 page RPM that is $1,800–$4,200 a month that was already being earned and
simply not collected. Our <a href="/guides/adsense-approval-checklist/">AdSense approval checklist</a>
covers what has to be in place first.</p>
<h2 id="payback">What to do with the payback number</h2>
<p>If payback is under 9 months, increase volume. Between 9 and 18 months, hold volume and improve
conversion — the offer is the bottleneck, not the traffic. Over 18 months, your keyword targets are
too competitive or your deal value is too low, and adding content will not fix either.</p>
""",
    "faq": [
        ("How long before content marketing shows a return?",
         "<p>Six to twelve months for the first meaningful organic traffic, twelve to twenty-four for "
         "pipeline that a CFO recognises. Anyone promising 90 days is selling paid media with a "
         "content label on it.</p>"),
        ("What is a good cost per lead from content?",
         "<p>It depends entirely on deal value. As a rule of thumb, cost per customer under 25% of "
         "first-year revenue is healthy. The calculator prints both cost per lead and cost per "
         "customer so you can check against your own economics.</p>"),
        ("Should I count ad revenue in content ROI?",
         "<p>Yes, if you run ads and your content is genuinely useful to a wide audience. Ignoring it "
         "understates the return on top-of-funnel content, which is exactly the content most likely "
         "to get cut in a budget review.</p>"),
        ("Is AI-written content cheaper enough to change the model?",
         "<p>It lowers cost per piece and raises the risk of producing nothing that ranks. Search "
         "engines penalise scaled low-value content explicitly. Use AI for research, outlining and "
         "first drafts, then pay a human for the information gain — the part that actually earns the ranking.</p>"),
    ],
},

"channel-growth-forecaster": {
    "engine": "growth",
    "h1": "Channel growth forecaster",
    "title": "YouTube Channel Growth Forecaster — Subscribers and Revenue Projection",
    "desc": "Project subscriber growth, monthly views and revenue over 3–36 months with "
            "compounding growth and honest views-per-subscriber assumptions.",
    "intro": "Compounding is the whole game, and views-per-subscriber is the honest health metric. "
             "This projects both, plus the revenue that follows.",
    "inputs": [
        _rng("subs", "Current subscribers", 0, 5000000, 100, 12000),
        _rng("growth", "Monthly growth rate (%)", 0.5, 40, 0.5, 6),
        _rng("viewsper", "Monthly views per subscriber", 0.2, 15, 0.1, 2.2),
        _rng("horizon", "Forecast horizon (months)", 3, 36, 1, 12),
        _sel("niche", "Niche", NICHE_OPTS, "marketing"),
        _sel("geo", "Audience geography", GEO_OPTS, "tier1"),
    ],
    "method": """
<h2 id="metric">Views per subscriber is the number that matters</h2>
<table>
<thead><tr><th>Views per sub / month</th><th>What it means</th></tr></thead>
<tbody>
<tr><td>Above 3.0</td><td>Strong; audience actively returns and the algorithm is pushing you</td></tr>
<tr><td>2.0 – 3.0</td><td>Healthy for most niches</td></tr>
<tr><td>1.0 – 2.0</td><td>Drifting; publishing cadence or topic focus has slipped</td></tr>
<tr><td>Below 0.8</td><td>Effectively a dead list. Subscriber count is vanity at this point.</td></tr>
</tbody></table>
<h2 id="rates">What growth rates are actually achievable</h2>
<ul>
<li><strong>Under 10,000 subs:</strong> 10–30% a month is achievable with consistent publishing and a working format.</li>
<li><strong>10,000 – 100,000:</strong> 5–12% a month is a good programme.</li>
<li><strong>100,000 – 1M:</strong> 2–6% a month. Sustained double digits at this size is exceptional.</li>
<li><strong>Above 1M:</strong> 1–3% a month, and increasingly driven by format changes rather than volume.</li>
</ul>
<p>Set the slider to what you have actually averaged over the last six months, not what you hope for.
The forecast is only useful if the input is honest.</p>
<h2 id="plan">Turning the forecast into a plan</h2>
<p>Take the month-12 revenue figure and work backwards. If the number is too small, you have exactly
three levers: raise growth rate (better packaging and formats), raise views per subscriber (better
cadence and series), or raise RPM (shift niche or audience geography). Volume alone changes the
least of the three.</p>
""",
    "faq": [
        ("What's a realistic YouTube growth rate?",
         "<p>It scales inversely with size. Under 10K subscribers, 10–30% a month is normal for a "
         "channel that is working. Above 100K, 2–6% a month is a strong programme. Growth rates quoted "
         "in case studies are almost always from the sub-10K phase.</p>"),
        ("Why are my views falling while subscribers rise?",
         "<p>Your views-per-subscriber is collapsing, which usually means subscribers arrived from one "
         "viral video that does not represent your regular content. The subscribers are real; the "
         "interest match is not. Fix the format before fixing the funnel.</p>"),
        ("Do subscribers even matter anymore?",
         "<p>Less than they did — most views on most channels now come from browse and suggested, not "
         "from subscription feeds. Subscribers matter as a proxy for repeat interest, which is why "
         "views-per-subscriber is the better metric to manage.</p>"),
        ("How do I model a channel that just started?",
         "<p>Set subscribers to your actual number, growth to 15–25%, and views-per-subscriber to 3–5 "
         "(new channels over-index because every subscriber is recent). Re-run it every quarter with "
         "real numbers instead of trusting a 24-month projection made on day one.</p>"),
    ],
},
}

RELATED = list(TOOLS.keys())


def _input_html(f, slug):
    fid = f"{slug}-{f['name']}"
    if f["kind"] == "range":
        step = f["step"]
        return (f'<div class="calc-row"><label for="{fid}">{f["label"]}'
                f'<output class="val" data-for="{f["name"]}" data-suffix="{f.get("suffix","")}"></output></label>'
                f'<input id="{fid}" name="{f["name"]}" type="range" min="{f["min"]}" max="{f["max"]}" '
                f'step="{step}" value="{f["default"]}" data-def="{f["default"]}"></div>')
    if f["kind"] == "select":
        opts = "".join(
            f'<option value="{v}"{" selected" if v == f["default"] else ""}>{l}</option>'
            for v, l in f["options"])
        return (f'<div class="calc-row"><label for="{fid}">{f["label"]}</label>'
                f'<select id="{fid}" name="{f["name"]}" data-def="{f["default"]}">{opts}</select></div>')
    return (f'<div class="calc-row"><label for="{fid}">{f["label"]}</label>'
            f'<input id="{fid}" name="{f["name"]}" type="number" value="{f["default"]}" '
            f'data-def="{f["default"]}" min="0" step="any"></div>')


def _related(slug):
    others = [s for s in RELATED if s != slug][:6]
    items = "".join(
        f'<a href="/tools/{s}/"><span class="n">{i+1}</span>{TOOLS[s]["h1"]}</a>'
        for i, s in enumerate(others))
    return f'''<section class="band" style="padding-top:1rem">
  <h2>Related calculators</h2>
  <div class="tool-strip">{items}</div>
</section>'''


def build_tool(slug):
    t = TOOLS[slug]
    inputs = "".join(_input_html(f, slug) for f in t["inputs"])
    crumbs = breadcrumbs([("Home", "/"), ("Free tools", "/tools/"), (t["h1"], f"/tools/{slug}/")])

    calc = f'''<div class="calc" data-calc="{t['engine']}">
  <div class="calc-head">
    <h2 style="font-size:1rem">{t['h1']}</h2>
    <div class="chipset">
      <button class="chip" type="button" data-reset>Reset</button>
      <button class="chip" type="button" data-copy="[data-out]">Copy result</button>
      <button class="chip" type="button" data-share>Share</button>
    </div>
  </div>
  <div class="calc-body">
    <div class="calc-inputs">{inputs}
      <p class="calc-note">Nothing you type is sent anywhere. Everything runs in your browser.</p>
    </div>
    <div class="calc-output" data-out></div>
  </div>
</div>'''

    toc_items = [("formula", "The formula")] + [
        (h.split('id="')[1].split('"')[0], h.split(">", 1)[1].split("<")[0])
        for h in t["method"].split("\n") if h.startswith("<h2 id=")
    ][1:]

    schema = [
        {"@context": "https://schema.org", "@type": "WebApplication",
         "name": t["h1"], "url": f"{SITE['base_url']}/tools/{slug}/",
         "applicationCategory": "BusinessApplication",
         "operatingSystem": "Any", "description": t["desc"],
         "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
         "publisher": {"@type": "Organization", "name": SITE["name"]}},
    ]

    body = f'''<section class="band" style="padding-bottom:1.5rem">
  <div class="wrap">
    {crumbs}
    <h1>{t['h1']}</h1>
    <p class="lede">{t['intro']}</p>
    {byline()}
    {calc}
    {ad("tool_result", style="leaderboard")}
  </div>
</section>

<section class="band" style="padding-top:0">
  <div class="wrap article-layout">
    <article class="prose">
      {t['method']}
      {ad("in_article")}
      {faq(t['faq'])}
      {helpful_poll(slug)}
    </article>
    <aside class="sidebar">
      {toc(toc_items)}
      {ad("sidebar", style="sidebar")}
      <div class="panel panel--compact">
        <h3 style="font-size:1rem">Want this done for you?</h3>
        <p class="small muted">We build and run content programmes using these exact models.</p>
        <a class="btn btn--primary btn--block" href="/services/#quote">Get a costed plan</a>
      </div>
      <div class="panel panel--compact">
        <h3 style="font-size:1rem">Free weekly brief</h3>
        <p class="small muted">Benchmark changes and payout shifts, every Tuesday.</p>
        <form class="cm-form" data-form="newsletter">
          <input name="email" type="email" required placeholder="you@company.com">
          <button class="btn btn--primary btn--block" type="submit" style="margin-top:.5rem">Subscribe</button>
          <div class="form-status" role="status" aria-live="polite"></div>
        </form>
      </div>
    </aside>
  </div>
</section>

<section class="band band--alt">
  <div class="wrap">
    {_related(slug)}
    {newsletter_block(variant="narrow")}
  </div>
</section>
{cta_band("Numbers are the easy part. Shipping the content is the hard part.",
          "Hand us the programme and we will build it, staff it and run it.")}'''

    return page(t["title"], t["desc"], f"/tools/{slug}/", body,
                active="tools", schema=schema,
                extra_body='<script src="/assets/js/benchmarks.js"></script>'
                           '<script src="/assets/js/calc.js" defer></script>')


def build_hub():
    cards = "".join(f'''<article class="card">
      <div class="card-ico">{i+1}</div>
      <h3><a class="stretch" href="/tools/{s}/">{TOOLS[s]['h1']}</a></h3>
      <p>{TOOLS[s]['desc']}</p>
      <div class="tool-card__meta" style="margin-top:.8rem"><span class="tag tag--free">Free</span>
      <span class="tag">No sign-up</span></div>
    </article>''' for i, s in enumerate(TOOLS))

    body = f'''<section class="band">
  <div class="wrap">
    {breadcrumbs([("Home", "/"), ("Free tools", "/tools/")])}
    <h1>Free creator economy calculators</h1>
    <p class="lede">Ten tools that give you a number instead of a sales call. Every one publishes
    its formula and its constants on the same page, and none of them asks for your email. Built on
    the <a href="/benchmarks/">2026 benchmark database</a>.</p>
    {ad("leaderboard", style="leaderboard")}
    <div class="grid g3">{cards}</div>
  </div>
</section>
<section class="band band--alt">
  <div class="wrap">
    {section_head("Why these exist", "Most creator calculators are lead magnets wearing a formula")}
    <div class="grid g3">
      <div class="card"><h3>Published assumptions</h3><p>Every result prints the exact constants
      used. If you disagree with a figure, you can see it and argue with it.</p></div>
      <div class="card"><h3>Ranges, not fake precision</h3><p>Nothing here returns a single number.
      Creator earnings are a band, and anyone telling you otherwise is guessing.</p></div>
      <div class="card"><h3>No email gate</h3><p>The result is free. We monetise with advertising,
      labelled sponsorships and our services business — not by holding your own numbers hostage.</p></div>
    </div>
    {newsletter_block()}
  </div>
</section>
{cta_band("Skip the spreadsheet. Get a costed content plan instead.",
          "Tell us the shape of the problem and we come back in one business day.")}'''

    return page("Free Creator Economy Calculators — 10 Tools, No Sign-Up | Content.Media",
                "Ten free calculators for creators and publishers: YouTube and TikTok earnings, "
                "rate cards, CPM/RPM, podcast and newsletter sponsorship, content ROI.",
                "/tools/", body, active="tools")
