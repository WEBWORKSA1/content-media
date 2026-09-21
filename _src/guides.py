# -*- coding: utf-8 -*-
"""Editorial library. Each guide is a real, opinionated reference page —
the kind that earns links and holds a ranking."""

GUIDES = [
{
 "slug": "adsense-approval-checklist",
 "cat": "Monetisation",
 "title": "The AdSense Approval Checklist That Actually Works in 2026",
 "desc": "Every page, policy and signal Google looks for before approving a site for AdSense, "
         "plus the two rejection reasons that account for almost everything.",
 "read": 9,
 "sum": "Two rejection reasons cover almost every failed application: “Low value content” and "
        "“Site does not comply with Google policies”. Both are fixable, and both are about "
        "structure as much as writing.",
 "body": """
<h2 id="before">Before you apply</h2>
<p>Google's published eligibility bar is thin — be 18, own the site, have original content, comply
with policy. The real bar is higher, and it is enforced by a reviewer who spends about ninety
seconds on your site. Everything below is aimed at that ninety seconds.</p>

<h3>The pages that must exist</h3>
<ul>
<li><strong>Privacy policy</strong> — must disclose third-party cookies and Google's use of
advertising cookies by name. This is non-negotiable and is checked.</li>
<li><strong>Terms of use</strong></li>
<li><strong>About</strong> — who publishes this, and why they are credible on the subject.</li>
<li><strong>Contact</strong> — a real, working method. A form is fine; a dead mailto is not.</li>
<li><strong>Cookie / consent notice</strong> — required for EEA, UK and Swiss traffic, and it must
be a Google-certified CMP. Applications with EEA traffic and no CMP are rejected on policy grounds.</li>
<li><strong>Editorial or advertising disclosure</strong> — not formally required, but it is the
cheapest trust signal on the list.</li>
</ul>

<h3>Content volume and quality</h3>
<p>There is no published minimum. In practice, twenty to thirty substantial original pages is the
working threshold, and "substantial" means information the reader cannot get from the first result
on the same query. Google's <em>scaled content abuse</em> policy is explicitly hostile to bulk
AI-rewritten pages, and it is enforced with automated classifiers before a human ever looks.</p>

<blockquote>The test that matters: could a reader who already read the top three results learn
something new from your page? If not, it is not "low value" by accident — it is low value by design.</blockquote>

<h3>Technical and structural signals</h3>
<ul>
<li>Custom domain. Free subdomains are rejected almost automatically.</li>
<li>HTTPS, mobile-responsive, no layout shift disasters.</li>
<li>Clear top-level navigation. A reviewer must reach any section in one click.</li>
<li>No placeholder pages, no "coming soon", no empty category archives.</li>
<li>Indexed in Google Search Console with a submitted sitemap.</li>
<li>Some organic traffic. Zero-traffic sites are commonly deferred.</li>
<li><code>ads.txt</code> at the domain root once approved.</li>
</ul>

<h2 id="snippets">The code, exactly</h2>
<p>Site verification and the main library go in <code>&lt;head&gt;</code> on every page:</p>
<div class="code">&lt;script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-XXXXXXXXXXXXXXXX"
        crossorigin="anonymous"&gt;&lt;/script&gt;</div>
<p>A responsive display unit:</p>
<div class="code">&lt;ins class="adsbygoogle" style="display:block"
     data-ad-client="ca-pub-XXXXXXXXXXXXXXXX" data-ad-slot="1234567890"
     data-ad-format="auto" data-full-width-responsive="true"&gt;&lt;/ins&gt;
&lt;script&gt;(adsbygoogle = window.adsbygoogle || []).push({});&lt;/script&gt;</div>
<p>An in-article unit, which is the highest-RPM manual placement on most content sites:</p>
<div class="code">&lt;ins class="adsbygoogle" style="display:block; text-align:center;"
     data-ad-layout="in-article" data-ad-format="fluid"
     data-ad-client="ca-pub-XXXXXXXXXXXXXXXX" data-ad-slot="5678901234"&gt;&lt;/ins&gt;
&lt;script&gt;(adsbygoogle = window.adsbygoogle || []).push({});&lt;/script&gt;</div>
<p>And <code>ads.txt</code>, one line, at the domain root:</p>
<div class="code">google.com, pub-XXXXXXXXXXXXXXXX, DIRECT, f08c47fec0942fa0</div>
<p>Note the difference: the script tag uses <code>ca-pub-</code>, the ads.txt line uses <code>pub-</code>.
Getting this wrong triggers the "earnings at risk" warning and silently suppresses your revenue.</p>

<h2 id="placement">Placement and density, post-cap</h2>
<p>Google removed the hard per-page unit cap years ago and replaced it with a qualitative
<em>valuable inventory</em> policy: content must outweigh ads. What is still explicitly banned:</p>
<ul>
<li>Ads on pages with little or no content, error pages or thank-you pages</li>
<li>Ads styled to look like content or navigation</li>
<li>Units placed adjacent to buttons in a way that induces accidental clicks</li>
<li>More than one sticky or anchor unit</li>
<li>Auto-refreshing units, and any encouragement to click</li>
</ul>
<p>A safe production density: three to five units on a long desktop article; on mobile, one above
the fold, one or two in-content, and a single anchor. Better Ads Standards also bans full-screen
mobile interstitials and ad density above roughly 30% of viewport height.</p>

<h2 id="auto">Auto Ads or manual units?</h2>
<p>Auto Ads is one snippet and Google decides everything. It is the fastest route to revenue and the
only way to get anchor and vignette formats, but it causes layout shift and puts units where you
would not. The common production setup is manual in-article units for the body, with Auto Ads
enabled but restricted to anchor and vignette only.</p>

<h2 id="rpm">What to expect</h2>
<p>Headline RPM figures by niche assume tier-1 traffic. For marketing and business content with a
mixed-geography audience, a realistic expectation for a new site is <strong>$8–$20 page RPM</strong>,
not the $30+ figures quoted in case studies. Run your own numbers in the
<a href="/tools/cpm-rpm-cpc-calculator/">CPM/RPM calculator</a>.</p>

<h2 id="rejected">If you get rejected</h2>
<ol>
<li>Read which of the two reasons it was. They need completely different fixes.</li>
<li>"Policy": check the legal pages, the CMP, and any page with thin or duplicated content.</li>
<li>"Low value": add depth to your ten best pages rather than adding twenty new ones. Original data,
original screenshots, a calculator, a table nobody else has — information gain, not word count.</li>
<li>Wait at least two weeks between applications and change something material each time.</li>
</ol>
"""},

{
 "slug": "creator-rate-card-guide",
 "cat": "Pricing",
 "title": "How to Build a Creator Rate Card You Can Defend",
 "desc": "A complete pricing framework for sponsorships: base rates, the multipliers that matter, "
         "usage rights, exclusivity, and the negotiation script.",
 "read": 11,
 "sum": "Creators lose more money to unpriced usage rights than to low base rates. Price the "
        "rights separately, quote a bundle, and send the high end.",
 "body": """
<h2 id="base">Start with a base, not a feeling</h2>
<p>Every credible rate card starts from a dollar figure per thousand followers, then applies
multipliers. Current anchors:</p>
<table>
<thead><tr><th>Deliverable</th><th>Per 1,000 followers</th></tr></thead>
<tbody>
<tr><td>Instagram Reel</td><td>$12 – $30</td></tr>
<tr><td>Instagram in-feed post</td><td>$8 – $20</td></tr>
<tr><td>Instagram Story frame</td><td>$4 – $10</td></tr>
<tr><td>TikTok video</td><td>$10 – $26</td></tr>
<tr><td>YouTube integration (60–90s)</td><td>$18 – $55</td></tr>
<tr><td>YouTube dedicated video</td><td>$30 – $90</td></tr>
<tr><td>LinkedIn post</td><td>$15 – $45</td></tr>
<tr><td>Newsletter primary slot</td><td>$25 – $90 per 1,000 opens</td></tr>
<tr><td>Podcast mid-roll</td><td>$18 – $50 per 1,000 downloads</td></tr>
</tbody></table>
<p>Run your own combination in the <a href="/tools/creator-rate-card-calculator/">rate card builder</a>,
which applies all the multipliers below automatically.</p>

<h2 id="multipliers">The four multipliers</h2>
<h3>1. Niche</h3>
<p>B2B and finance audiences carry a 55–60% premium over general lifestyle, because the customer
behind each impression is worth more. Gaming and entertainment carry a discount for the same reason.
This is not a judgement about your work; it is a judgement about the advertiser's unit economics.</p>

<h3>2. Engagement relative to your tier</h3>
<p>Beat the benchmark for your follower tier and you have a defensible reason to charge above card.
Use the <a href="/tools/instagram-engagement-calculator/">engagement calculator</a> and show the
working in the media kit.</p>

<h3>3. Usage rights — the big one</h3>
<p>Organic posting reaches your audience. Paid usage turns your face into ad creative reaching
millions. These are not the same product and must not carry the same price.</p>
<table>
<thead><tr><th>Grant</th><th>Multiplier</th></tr></thead>
<tbody>
<tr><td>Organic only</td><td>×1.00</td></tr>
<tr><td>Whitelisting / paid ads, 30 days</td><td>×1.35</td></tr>
<tr><td>Whitelisting / paid ads, 90 days</td><td>×1.60</td></tr>
<tr><td>Perpetual, all channels</td><td>×2.10</td></tr>
</tbody></table>
<p>Never grant perpetual rights inside a base fee. If a contract says "in perpetuity, in all media
now known or hereafter devised", that is a separate line item worth roughly the value of the post
again.</p>

<h3>4. Exclusivity</h3>
<p>Category exclusivity means declining every competitor for the term. Twelve months of exclusivity
in a category you regularly work in can cost you more than the deal pays. Price it at ×1.8 minimum,
and scope it narrowly — "direct competitors named in Schedule A", not "the beverage category".</p>

<h2 id="bundle">Quote bundles, never single assets</h2>
<p>A bundle closes at a higher blended rate, gives the buyer one number to approve, and removes the
line-by-line comparison that always ends in a discount. A standard bundle: one hero asset, one
supporting asset, three story frames, 30-day organic usage, no exclusivity.</p>

<h2 id="script">The negotiation script</h2>
<p><strong>They ask for your rates.</strong> Send a one-page PDF with the bundle price, the
itemisation, and the working: audience size, geography split, engagement versus tier benchmark,
and one past result. Send the high end.</p>
<p><strong>They say it's over budget.</strong> Do not discount. Remove scope instead: "I can hit
$X by dropping the stories and the paid usage." This teaches the buyer that price tracks value.</p>
<p><strong>They ask for perpetual usage "as standard".</strong> "Happy to — perpetual usage is
priced at an additional 110% of the base fee. Or we can do 30 days at 35%, which covers most
campaign flights."</p>
<p><strong>They offer product instead of money.</strong> Accept only if retail value clearly exceeds
your rate and you wanted it anyway. Gifting is a marketing expense for them; treat it as one.</p>

<h2 id="terms">Terms that protect you</h2>
<ul>
<li>50% up front on anything over $5,000, balance net 30.</li>
<li>Two rounds of revisions included, then hourly.</li>
<li>Kill fee of 50% if the campaign is cancelled after brief acceptance.</li>
<li>You keep final say on anything that materially misrepresents your opinion.</li>
<li>Disclosure is mandatory and non-negotiable — it protects both sides legally.</li>
</ul>

<h2 id="floor">Set a floor and hold it</h2>
<p>Decide the number below which you decline, and write it down. A cheap deal does not just cost you
the difference — it sets your price for every buyer that brand talks to. In a small market, your
floor is public information within a quarter.</p>
"""},

{
 "slug": "youtube-rpm-by-niche",
 "cat": "Data",
 "title": "YouTube RPM by Niche: The 2026 Numbers",
 "desc": "Creator take-home RPM for 14 niches with geography multipliers, and the three variables "
         "that move it more than anything else.",
 "read": 8,
 "sum": "Niche and audience geography explain most of the variance in YouTube earnings. "
        "Subscriber count explains almost none of it.",
 "body": """
<h2 id="table">RPM by niche, creator take-home</h2>
<p>These figures are what lands in your account per 1,000 monetised views, already net of YouTube's
45% share of in-stream advertising revenue. Tier-1 audience assumed.</p>
<table>
<thead><tr><th>Niche</th><th>RPM low</th><th>RPM high</th><th>Advertiser CPM</th></tr></thead>
<tbody>
<tr><td>Personal finance &amp; investing</td><td>$15.00</td><td>$38.00</td><td>$28 – $70</td></tr>
<tr><td>B2B software &amp; SaaS</td><td>$14.00</td><td>$34.00</td><td>$26 – $64</td></tr>
<tr><td>Real estate &amp; mortgage</td><td>$12.00</td><td>$45.00</td><td>$24 – $84</td></tr>
<tr><td>Marketing &amp; business</td><td>$10.00</td><td>$26.00</td><td>$20 – $48</td></tr>
<tr><td>Technology &amp; reviews</td><td>$8.00</td><td>$22.00</td><td>$16 – $42</td></tr>
<tr><td>Education &amp; how-to</td><td>$5.00</td><td>$14.00</td><td>$10 – $26</td></tr>
<tr><td>Health &amp; fitness</td><td>$4.00</td><td>$12.00</td><td>$8 – $23</td></tr>
<tr><td>Travel</td><td>$4.00</td><td>$11.00</td><td>$8 – $21</td></tr>
<tr><td>Food &amp; cooking</td><td>$3.50</td><td>$9.00</td><td>$7 – $17</td></tr>
<tr><td>Beauty &amp; fashion</td><td>$3.50</td><td>$10.00</td><td>$7 – $19</td></tr>
<tr><td>Entertainment &amp; vlogs</td><td>$1.50</td><td>$6.00</td><td>$3 – $12</td></tr>
<tr><td>Gaming</td><td>$1.20</td><td>$5.50</td><td>$3 – $11</td></tr>
<tr><td>Kids &amp; family</td><td>$1.00</td><td>$4.00</td><td>$2 – $8</td></tr>
<tr><td>Music</td><td>$1.00</td><td>$3.50</td><td>$2 – $7</td></tr>
</tbody></table>

<h2 id="geo">Then multiply by geography</h2>
<table>
<thead><tr><th>Audience</th><th>Multiplier</th></tr></thead>
<tbody>
<tr><td>Mostly United States</td><td>×1.00</td></tr>
<tr><td>Mixed tier-1 (US/UK/CA/AU)</td><td>×0.86</td></tr>
<tr><td>Mostly Western Europe</td><td>×0.72</td></tr>
<tr><td>Global mix</td><td>×0.48</td></tr>
<tr><td>Mostly South Asia / SEA / LATAM</td><td>×0.22</td></tr>
</tbody></table>
<p>A gaming channel with a tier-3 audience earns roughly $0.26–$1.21 per 1,000 views. A finance
channel with a US audience earns $15–$38. That is a 60× spread on identical view counts, and it is
why "how much does YouTube pay per 1,000 views" has no useful single answer.</p>

<h2 id="monetised">The third variable nobody accounts for</h2>
<p>Only 55–78% of views serve a paid impression. Ad blockers, unmonetisable content, unsold
inventory and viewers who skip before the impression counts all eat into it. Every figure above is
per <em>monetised</em> view, so multiply your total views by that share before applying RPM.</p>

<h2 id="fix">What to do about a low RPM</h2>
<ol>
<li><strong>Check the geography split first.</strong> It explains the gap about 70% of the time.
If 60% of your views come from low-CPM markets, no amount of optimisation changes the arithmetic.</li>
<li><strong>Check your Shorts share.</strong> Shorts inside a blended RPM figure drag it toward zero.
Look at long-form RPM separately.</li>
<li><strong>Lengthen past eight minutes</strong> so mid-rolls become available, but only where the
content justifies it. Padding gets punished by retention.</li>
<li><strong>Move up-funnel within your niche.</strong> A gaming channel covering "best gaming laptop
2026" earns tech RPM on that video. The subject decides the auction, not the channel.</li>
<li><strong>Stop optimising RPM and build the other rails.</strong> On a healthy channel advertising
is 25–45% of revenue. Sponsorships, memberships and products are where the rest lives.</li>
</ol>

<p>Model your own numbers in the <a href="/tools/youtube-money-calculator/">YouTube money
calculator</a>, which applies all three variables together.</p>
"""},

{
 "slug": "lead-generation-for-content-sites",
 "cat": "Growth",
 "title": "Lead Generation for Content Sites: The Funnel That Converts",
 "desc": "The multi-step form structure, qualifying questions and microcopy that turn content "
         "traffic into qualified pipeline.",
 "read": 10,
 "sum": "Ask for zero personal information on step one. Commitment-consistency does more for "
        "completion rate than any amount of form-field optimisation.",
 "body": """
<h2 id="structure">Why multi-step beats single-step</h2>
<p>A single form asking for nine fields is a wall. The same nine fields split across four steps,
where the first step asks only a low-effort multiple-choice question with no personal information,
converts materially better. The mechanism is commitment-consistency: once someone has answered one
question, abandoning feels like wasting their own effort.</p>

<h3>The four-step structure</h3>
<p><strong>Step 1 — Intent, no PII.</strong> One question, card-style options, auto-advance on
click. "What kind of content work are you hiring for?" Microcopy: <em>Takes 45 seconds. No sales
call required to get a number.</em></p>
<p><strong>Step 2 — Scope.</strong> Volume and timeline. Microcopy: <em>Rough answers are fine.</em></p>
<p><strong>Step 3 — Fit.</strong> Budget band and company size. This is the qualifier.</p>
<p><strong>Step 4 — Contact.</strong> Name, work email, company, URL, optional phone. Button copy
names the outcome: <em>Send my custom content plan</em>, never "Submit".</p>

<h2 id="budget">The budget question, and the graceful downsell</h2>
<p>Budget band is the universal qualifier. The mistake is treating under-threshold leads as waste.
Put the threshold in the microcopy and offer something real below it:</p>
<blockquote>We work best from $2,500/month. Below that, we'll send you our DIY playbook instead —
free.</blockquote>
<p>That single line does three jobs: it anchors your price, it filters without insulting anyone, and
it converts the unqualified traffic into an email list that will be qualified in eighteen months.</p>

<h2 id="proof">What goes next to the form</h2>
<p>Hard numbers, not adjectives. Pieces produced, clients served, years operating, a third-party
rating, a partner badge, one named case study with a metric. Proof placed beside the form
outperforms the same proof placed elsewhere on the page.</p>

<h2 id="cta">CTA copy that works</h2>
<table>
<thead><tr><th>Instead of</th><th>Use</th></tr></thead>
<tbody>
<tr><td>Submit</td><td>Send my content plan</td></tr>
<tr><td>Contact us</td><td>Get a costed plan</td></tr>
<tr><td>Learn more</td><td>See what we charge</td></tr>
<tr><td>Sign up</td><td>Grade my website</td></tr>
<tr><td>Request a demo</td><td>Show me how it works on my site</td></tr>
</tbody></table>
<p>Verb plus the user's noun. Every time.</p>

<h2 id="tools">Free tools are the top of the funnel</h2>
<p>An ungated calculator earns links, ranks for high-intent queries, and gives you a conversion
surface that is not an article. Never gate the headline number — gate the <em>deeper</em> artefact:
the twelve-month projection PDF, the full rate card database, the benchmark CSV.</p>

<h2 id="after">After the submit</h2>
<p>A bare thank-you page wastes the highest-intent moment you will ever get from that person. Use it
for: an instant download of the promised asset, a calendar embed to book the call now, and a
deliverability nudge ("check your spam folder, we come from a monitored address"). A separate
success URL also gives you a clean conversion event to optimise against.</p>

<h2 id="placement">Placement rules</h2>
<ul>
<li>Sticky header CTA sitewide.</li>
<li>Engagement-triggered bar at roughly 45% scroll — better than exit-intent, which fires when the
decision is already made.</li>
<li>An inline CTA at the end of every article, matched to that article's topic.</li>
<li>One newsletter block mid-page, one in the footer. Three impressions a session is the ceiling
before it reads as desperate.</li>
<li>Subscriber count next to the email field. It is the single highest-leverage edit available and
costs nothing.</li>
</ul>
"""},

{
 "slug": "newsletter-monetisation-playbook",
 "cat": "Monetisation",
 "title": "The Newsletter Monetisation Playbook",
 "desc": "Sponsorship pricing, media kits, ad load limits and the four revenue models that work "
         "for independent newsletters.",
 "read": 9,
 "sum": "Price on opens, cap ad load at one primary slot, gate the media kit to capture the "
        "advertiser as a lead, and publish your numbers before anyone asks.",
 "body": """
<h2 id="models">Four models, ranked by durability</h2>
<ol>
<li><strong>Sponsorship.</strong> Fastest to start, scales with audience, no product needed. Ceiling
is set by list size and niche.</li>
<li><strong>Paid subscriptions.</strong> Highest margin, hardest to start. Needs a reason the free
version cannot serve.</li>
<li><strong>Products and courses.</strong> Highest revenue per subscriber, highest operational load.</li>
<li><strong>Affiliate.</strong> Easiest to add, quickest to erode trust. Cap it and label it.</li>
</ol>
<p>Most independent newsletters that reach real money run one and a half of these, not four.</p>

<h2 id="pricing">Price on opens</h2>
<table>
<thead><tr><th>Placement</th><th>CPM on opens</th><th>Format</th></tr></thead>
<tbody>
<tr><td>Classified / text link</td><td>$8 – $18</td><td>One line, 2–4 per issue</td></tr>
<tr><td>Primary sponsor slot</td><td>$25 – $60</td><td>~350 characters, image, tracked link</td></tr>
<tr><td>Dedicated send</td><td>$45 – $120</td><td>Whole email, max one per month</td></tr>
</tbody></table>
<p>B2B decision-maker audiences carry roughly an 80% premium. Run your own numbers in the
<a href="/tools/newsletter-sponsorship-calculator/">newsletter sponsorship calculator</a>.</p>

<h2 id="mediakit">The media kit</h2>
<p>Publish these openly: subscribers, open rate, click rate, growth rate, audience composition by
seniority, function, company size and country. Gate the full rate card behind a short form — it
captures the advertiser as a lead and the open numbers pre-qualify them so you stop taking calls
from people who cannot afford you.</p>
<p>Include a price floor and a minimum term. "From $X per issue, three-issue minimum" kills the
one-off tyre-kicker conversation before it starts. If you are booked out, say so — scarcity is the
most effective line in any media kit.</p>

<h2 id="adload">Ad load discipline</h2>
<p>One primary slot plus two classifieds is the ceiling before unsubscribes rise measurably. Every
sponsored slot must be labelled unambiguously. The list is the asset; a burned list cannot be
rebuilt with money, and you will notice the damage two quarters after you caused it.</p>

<h2 id="growth">Growth that does not poison the list</h2>
<ul>
<li><strong>A real lead magnet.</strong> A physical or high-perceived-value asset — a book, a
database, a template pack — converts far above "join our newsletter".</li>
<li><strong>Archive access as a benefit.</strong> "Unlimited access to every back issue" costs
nothing and converts.</li>
<li><strong>Cross-promotion swaps</strong> with adjacent newsletters. Highest-quality growth
available to a small list.</li>
<li><strong>Paid acquisition only with a known payback.</strong> If you cannot state revenue per
subscriber per year, you cannot price a subscriber acquisition.</li>
<li><strong>Avoid giveaway-sourced subscribers</strong> unless the prize is relevant to the niche.
Generic prizes buy a list that never opens.</li>
</ul>

<h2 id="reporting">Reporting that gets you renewed</h2>
<p>Send the advertiser opens, unique clicks, click rate, and a screenshot of the placement, within
48 hours. Include a plain-language note on what worked. Renewal rate is the entire economics of a
sponsorship business, and it is decided by whether reporting arrived without being chased.</p>
"""},

{
 "slug": "content-repurposing-system",
 "cat": "Operations",
 "title": "The One-to-Twelve Content Repurposing System",
 "desc": "Turn one long-form asset into twelve distribution units without producing twelve times "
         "the work — and without thinning the original.",
 "read": 8,
 "sum": "Repurpose in one direction only: long-form first, then cut. The reverse produces thin "
        "long-form that ranks for nothing.",
 "body": """
<h2 id="principle">The direction rule</h2>
<p>Every durable content operation produces a deep artefact first and derives everything else from
it. Teams that work the other way — stitching short-form ideas into a long post — produce content
with no spine, and search engines are good at detecting exactly that.</p>

<h2 id="system">One asset, twelve units</h2>
<p>From a single 2,500-word researched piece or a 20-minute video:</p>
<ol>
<li><strong>The pillar page</strong> — the canonical asset, internally linked from everything else.</li>
<li><strong>A long-form video</strong> of the same argument, if the original was written.</li>
<li><strong>Three to five short clips</strong>, each built on one self-contained point with a hook
in the first 1.5 seconds.</li>
<li><strong>A carousel</strong> for LinkedIn and Instagram — one idea per card, 7–10 cards.</li>
<li><strong>A newsletter issue</strong> that adds a framing or a story the pillar does not have.
Never paste the article.</li>
<li><strong>Two to three standalone text posts</strong> for X and LinkedIn, each a complete thought.</li>
<li><strong>A data visual</strong> — the one table or chart from the research, designed properly.
This is the unit most likely to earn links.</li>
<li><strong>A podcast segment</strong> or an audio version.</li>
<li><strong>An FAQ block</strong> harvested from the questions the piece raised, added back to the
pillar for schema.</li>
<li><strong>A downloadable</strong> — checklist, template, or the raw dataset.</li>
<li><strong>A community post</strong> or comment answer where the question is already being asked.</li>
<li><strong>A refresh</strong> of the pillar six months later with new data, republished.</li>
</ol>

<h2 id="cadence">A realistic weekly cadence for a team of one</h2>
<table>
<thead><tr><th>Day</th><th>Work</th></tr></thead>
<tbody>
<tr><td>Monday</td><td>Research and outline the week's pillar</td></tr>
<tr><td>Tuesday</td><td>Write or record the pillar</td></tr>
<tr><td>Wednesday</td><td>Edit, publish, internal links, schema</td></tr>
<tr><td>Thursday</td><td>Cut clips and build the carousel</td></tr>
<tr><td>Friday</td><td>Newsletter, text posts, schedule the week ahead</td></tr>
</tbody></table>
<p>One pillar a week is twelve distribution units a week and fifty-two durable assets a year. That
is a serious library. Two pillars a week for a team of one is how people burn out in month five.</p>

<h2 id="quality">Where repurposing goes wrong</h2>
<ul>
<li><strong>Cross-posting instead of adapting.</strong> A vertical video with a horizontal crop and
a caption written for another platform reads as spam on every platform.</li>
<li><strong>Repurposing weak originals.</strong> Twelve units of a mediocre idea is twelve times the
mediocrity, not twelve times the reach.</li>
<li><strong>No canonical home.</strong> If the clips do not point back at the pillar, you are
building someone else's audience.</li>
<li><strong>Automating the cut without re-writing the hook.</strong> Auto-clipping tools find the
segment; they cannot write the first line. That line is 80% of the performance.</li>
</ul>

<h2 id="measure">Measure the right thing</h2>
<p>Judge short-form on <em>conversion to the owned asset</em> — subscribers gained, clicks to the
pillar, newsletter signups — not on views. A clip with two million views and forty subscribers is a
failure that looks like a success on a dashboard.</p>
"""},

{
 "slug": "programmatic-seo-for-publishers",
 "cat": "SEO",
 "title": "Programmatic SEO Without Getting Penalised",
 "desc": "How to build templated pages at scale that still pass the information-gain test, and "
         "where the line is under scaled content abuse policy.",
 "read": 10,
 "sum": "Programmatic pages survive when each one carries data that exists nowhere else. "
        "Templated prose around an identical dataset is the definition of scaled content abuse.",
 "body": """
<h2 id="line">Where the line is</h2>
<p>Search engines do not penalise templates. They penalise pages that add nothing. A programmatic
page passes when a reader arriving on it gets a specific, correct answer they could not assemble
themselves in under a minute. It fails when the only thing that changes between two pages is a
noun in the headline.</p>

<h3>The test</h3>
<blockquote>Strip the template. What is left? If the answer is "a city name", you have a penalty
waiting. If the answer is "a unique dataset, a calculation, a comparison, or a verified list", you
have a business.</blockquote>

<h2 id="patterns">Patterns that hold up</h2>
<table>
<thead><tr><th>Pattern</th><th>Unique element per page</th></tr></thead>
<tbody>
<tr><td>Calculator variants</td><td>A different formula and a different result set</td></tr>
<tr><td>Tool comparisons (X vs Y)</td><td>Verified feature and price matrix for that pair</td></tr>
<tr><td>Benchmark by segment</td><td>Real measured data for that segment</td></tr>
<tr><td>Directory category pages</td><td>A curated, editorially-noted list</td></tr>
<tr><td>Alternatives pages</td><td>Researched substitutes with reasons, not a scraped list</td></tr>
<tr><td>Rate cards by platform and tier</td><td>Distinct pricing tables and multipliers</td></tr>
</tbody></table>

<h2 id="build">Building it</h2>
<ol>
<li><strong>Get the data first.</strong> If you do not have a proprietary or laboriously assembled
dataset, stop. There is no programmatic strategy without one.</li>
<li><strong>Design one page properly</strong> and make it genuinely useful before templating anything.</li>
<li><strong>Vary structure, not just values.</strong> Sections that appear only when relevant; FAQs
generated from the actual data; comparisons that only render when a meaningful difference exists.</li>
<li><strong>Publish in batches</strong> and watch indexation. If 30% of a batch is not indexed after
six weeks, the pages are not clearing the bar — fix them before publishing the next batch.</li>
<li><strong>Internal-link laterally.</strong> Related pages, parent category, and a hub. Orphaned
programmatic pages get crawled once and forgotten.</li>
<li><strong>Prune ruthlessly.</strong> Pages with no impressions after six months should be merged
or removed. A large index of dead pages drags the whole site.</li>
</ol>

<h2 id="tech">Technical requirements</h2>
<ul>
<li>Unique title and meta description generated from the data, not from a single string with a variable.</li>
<li>Structured data appropriate to the page type — FAQPage, ItemList, SoftwareApplication, Dataset.</li>
<li>A real XML sitemap segmented by page type so you can measure indexation per segment.</li>
<li>Static rendering. If the unique content only exists after JavaScript runs, assume it does not exist.</li>
<li>Canonical tags that handle filter and sort parameters, or you will index ten thousand near-duplicates.</li>
</ul>

<h2 id="honest">The honest economics</h2>
<p>Programmatic SEO is a data-acquisition problem wearing an SEO costume. The build is two weeks;
the dataset is two years. Sites that win here — comparison sites, directories, benchmark
publishers — win because assembling and maintaining the data is genuinely hard, not because the
templating was clever.</p>
"""},

{
 "slug": "donation-funded-media",
 "cat": "Monetisation",
 "title": "How Donation-Funded Media Actually Works",
 "desc": "Tier design, price points, transparency and the persuasion patterns that make reader "
         "support work — plus the embeds that run on a static site.",
 "read": 8,
 "sum": "Three tiers, the middle one highlighted, annual shown by default, and a published "
        "breakdown of where the money goes. Independence is the pitch.",
 "body": """
<h2 id="pitch">The pitch is independence, not charity</h2>
<p>Reader-funded publications that work all say a version of the same thing: no owner, no
shareholders, no paywall. The reader is not being asked for a donation; they are being asked to
keep a thing independent. That framing outperforms every variation of "support our work".</p>
<p>Three patterns recur across the publications that fund themselves this way:</p>
<ul>
<li><strong>Scarcity of funder.</strong> "Founded and owned by the journalists who run it."</li>
<li><strong>Cost anchoring to something trivial.</strong> "$1 a week", "less than a coffee".</li>
<li><strong>Collective-action framing.</strong> "If everyone reading this gave $3, we'd be funded
by Friday." It makes a small contribution feel decisive rather than pointless.</li>
</ul>

<h2 id="tiers">Tier design</h2>
<p>Three tiers maximum. Middle tier visually highlighted and labelled "most popular". Annual shown
as the default with the monthly equivalent in small text and an explicit saving. Typical current
shape for an independent publication:</p>
<table>
<thead><tr><th>Tier</th><th>Monthly</th><th>Annual</th><th>What it buys</th></tr></thead>
<tbody>
<tr><td>Free</td><td>$0</td><td>$0</td><td>Everything. The free tier makes paying a choice, not a gate.</td></tr>
<tr><td>Supporter</td><td>$8 – $10</td><td>$79 – $100</td><td>Name on the supporters page, early access, ad-light reading</td></tr>
<tr><td>Superfan / Patron</td><td>$80 – $100</td><td>$800 – $1,000</td><td>Quarterly open financials call, direct line, credit</td></tr>
</tbody></table>
<p>One-off amounts should be four to ten times the monthly tier: $25 / $50 / $100 / other.</p>

<h2 id="ux">Frequency toggle and defaults</h2>
<p>A segmented pill control — Monthly | Annual | One-time — that swaps the amount chips in place
without navigating. Pre-select recurring. Put a "save 17%" badge on annual. Under the button:
"Cancel any time. Secure payment. You'll get a receipt."</p>

<h2 id="transparency">Publish where the money goes</h2>
<p>Three formats work. A percentage breakdown; a named-cost list ("$60 covers one day of a
researcher's time"); or a quarterly public revenue post. The last is the strongest and the least
used — it converts supporters into people who feel like shareholders, because functionally they are.</p>

<h2 id="goals">Goals and progress bars</h2>
<p>Use them for campaigns, not on the evergreen page. Count-based goals ("1,842 of 3,000
supporters") outperform dollar goals for small publications because the denominator looks
reachable. Always attach a deadline — a bar with no end date reads as static and stops converting
within a week.</p>

<h2 id="embeds">What works on a static site</h2>
<p>No backend required for any of these:</p>
<ul>
<li><strong>Stripe Payment Links</strong> — create a product with one-time and recurring prices in
the dashboard, optionally "customer chooses price", and use the resulting URL as a plain link. The
cleanest option, and the one to build the primary button on.</li>
<li><strong>Buy Me a Coffee</strong> — a static image link, or a floating widget script.</li>
<li><strong>Ko-fi</strong> — an inline iframe panel or an overlay widget. 0% platform fee on donations.</li>
<li><strong>PayPal hosted button</strong> — a plain HTML form posting a hosted button ID.</li>
<li><strong>GitHub Sponsors</strong> — a link, plus <code>FUNDING.yml</code> in the repo.</li>
<li><strong>Open Collective</strong> — donate button, contributor banner and backers badge, all
script or object tags, with every expense public by default.</li>
</ul>
<p>Run at least two rails. Payment preference is regional, and a single provider is a single point
of failure for your entire revenue line.</p>
"""},

{
 "slug": "running-a-legal-contest",
 "cat": "Growth",
 "title": "Running a Contest or Giveaway Without Breaking the Law",
 "desc": "The official rules elements required in the US and Canada, entry mechanics that survive "
         "a challenge, and how to run it all from a static site.",
 "read": 9,
 "sum": "No purchase necessary, a free alternate method of entry, published odds and a named "
        "sponsor. In Canada, a skill-testing question is mandatory or it is an illegal lottery.",
 "body": """
<div class="callout"><h4>Not legal advice</h4><p>This is a practitioner's checklist, not counsel.
Prize pools above a few thousand dollars, or contests open across many jurisdictions, need a lawyer
and possibly registration and bonding. Get that review before you publish.</p></div>

<h2 id="structure">The three legal shapes</h2>
<table>
<thead><tr><th>Type</th><th>Winner chosen by</th><th>Consideration allowed?</th></tr></thead>
<tbody>
<tr><td>Sweepstakes</td><td>Chance</td><td>No — must be free to enter</td></tr>
<tr><td>Contest</td><td>Skill, judged</td><td>Sometimes, jurisdiction-dependent</td></tr>
<tr><td>Lottery</td><td>Chance</td><td>Yes — and illegal for you to run</td></tr>
</tbody></table>
<p>If entry requires payment <em>and</em> the winner is chosen at random, you are running a lottery.
Remove one of the two. In practice that means: free to enter, always.</p>

<h2 id="rules">Official rules: the elements</h2>
<ol>
<li>"NO PURCHASE NECESSARY. A PURCHASE WILL NOT INCREASE YOUR CHANCES OF WINNING."</li>
<li>"VOID WHERE PROHIBITED."</li>
<li>Eligibility — age, residency, and exclusion of employees, contractors and immediate family.</li>
<li>Entry period with start and end dates <strong>and the time zone</strong>.</li>
<li>A free alternate method of entry (AMOE) with equal standing — typically a mail-in entry.</li>
<li>Prize description, approximate retail value, and "odds of winning depend on the number of
eligible entries received".</li>
<li>Winner selection method and notification timeline.</li>
<li>Sponsor's full legal name and address.</li>
<li>Publicity and privacy release.</li>
<li>Governing law and dispute resolution.</li>
<li>How to request the winners list.</li>
<li>Tax note — in the US, prizes of $600 or more trigger a 1099-MISC.</li>
</ol>
<p>New York and Florida require registration and bonding when total prize value exceeds $5,000.
Rhode Island has its own threshold for retail sweepstakes.</p>

<h2 id="canada">Canada adds three things</h2>
<ul>
<li><strong>A mathematical skill-testing question is mandatory.</strong> Without it, a chance-based
promotion is an illegal lottery under the Criminal Code. A four-step arithmetic question is the
convention.</li>
<li><strong>Odds must be disclosed</strong> and prize value stated in CAD.</li>
<li><strong>Quebec</strong> requires French-language materials and RACJ registration with fees —
which is why most small publishers write "excluding Quebec".</li>
</ul>
<p>CASL also means entry is not marketing consent. You need a separate, unbundled opt-in checkbox
if you intend to email entrants afterwards.</p>

<h2 id="mechanics">Entry mechanics that survive a challenge</h2>
<p>Only award bonus entries for actions you can actually verify. "Follow us on three platforms" is
unverifiable at scale and indefensible if a losing entrant complains. Referral links with unique
codes are verifiable and drive the most growth. Cap daily bonus entries to keep the leaderboard
from being farmed.</p>

<h2 id="static">Running it on a static site</h2>
<ul>
<li><strong>Entries:</strong> an embedded form service, with responses landing in a spreadsheet.
Sufficient for a documented random draw.</li>
<li><strong>Draw:</strong> use a documented RNG with a witness, and publish the method in the rules
before the contest opens. Record it if the prize is significant.</li>
<li><strong>Referrals and leaderboards:</strong> a third-party giveaway platform gives you referral
tracking, fraud screening and a live leaderboard from a single embed. Self-rolled leaderboards on a
static site cannot dedupe and will be gamed.</li>
<li><strong>Winner announcement:</strong> a permanent URL, published on the date you promised, with
the winners list available on request. Nothing damages a small publication faster than a contest
that quietly never announced a winner.</li>
</ul>

<h2 id="worth">Is it worth it?</h2>
<p>Only if the prize is relevant to the niche. A generic tech giveaway buys a list of people who
enter giveaways. A prize that only your actual audience wants — a year of the tool they already
use, a paid consultation, a production budget — buys subscribers who open.</p>
"""},

{
 "slug": "media-kit-that-sells",
 "cat": "Pricing",
 "title": "The Media Kit That Actually Sells Sponsorships",
 "desc": "What advertisers look for, the numbers to publish openly, what to gate, and the exact "
         "structure that shortens the sales cycle.",
 "read": 7,
 "sum": "Publish three numbers openly, gate the rate card, state a price floor and a minimum term. "
        "The media kit's job is to disqualify people before they book a call.",
 "body": """
<h2 id="job">What a media kit is for</h2>
<p>Not to impress. To disqualify. A good media kit ends more conversations than it starts, and the
ones that survive it are with buyers who can afford you and want what you sell. That is the entire
economic function.</p>

<h2 id="open">Publish these openly</h2>
<ul>
<li>Audience size — subscribers, downloads, monthly uniques, whichever you actually sell against.</li>
<li>Engagement — open rate, click rate, average view duration. Disclose known inflation rather than
waiting to be caught.</li>
<li>Growth rate year on year. Advertisers buy trajectory.</li>
<li>Audience composition — seniority, function, company size, country split. In B2B this moves rates
more than audience size does.</li>
</ul>

<h2 id="gate">Gate this</h2>
<p>The full rate card, format specs and availability calendar. The form captures the advertiser as a
lead and gives you the first-mover advantage in the conversation. Ask for: name, company, email,
budget band, and which format they are interested in. Five fields, no more.</p>

<h2 id="specs">Specs sell competence</h2>
<p>Buyers are running six campaigns at once. Exact constraints save them work and make you look
like a professional operation:</p>
<blockquote>Primary newsletter slot: 350 characters maximum, one image at 1200×600, one tracked
link. Copy due Thursday for the following Tuesday's send.</blockquote>

<h2 id="price">State a floor and a minimum term</h2>
<p>"From $X per issue, three-issue minimum." This does two things at once: it anchors your price
before negotiation starts, and it eliminates the one-off tyre-kicker who was going to consume four
emails and buy nothing. If you are booked, say so — a waitlist line is the most effective sentence
in any media kit.</p>

<h2 id="proof">Proof, in order of persuasiveness</h2>
<ol>
<li>A named past sponsor who renewed, with the metric.</li>
<li>A logo wall.</li>
<li>A quote from a buyer, with their title.</li>
<li>Third-party audience verification.</li>
<li>Awards and press mentions — last, and briefly.</li>
</ol>

<h2 id="structure">One-page structure that works</h2>
<ol>
<li>Who reads this, in one sentence.</li>
<li>Three headline numbers with growth.</li>
<li>Audience composition chart.</li>
<li>Formats with specs and a price floor.</li>
<li>Logo wall and one renewal case study.</li>
<li>Availability and how to book — one CTA, one form.</li>
</ol>
<p>Use our <a href="/tools/newsletter-sponsorship-calculator/">newsletter</a> and
<a href="/tools/podcast-sponsorship-calculator/">podcast</a> calculators to set the numbers
before you write it.</p>
"""},

{
 "slug": "ai-content-workflow",
 "cat": "Operations",
 "title": "An AI Content Workflow That Doesn't Produce Slop",
 "desc": "Where AI belongs in a content pipeline, where it does not, and the review gates that "
         "keep quality and rankings intact.",
 "read": 9,
 "sum": "Use AI for research, structure and first drafts. Pay a human for information gain — the "
        "part that earns the ranking and the link.",
 "body": """
<h2 id="where">Where AI genuinely helps</h2>
<table>
<thead><tr><th>Stage</th><th>AI role</th><th>Human role</th></tr></thead>
<tbody>
<tr><td>Topic research</td><td>Cluster queries, summarise sources, find gaps</td><td>Pick the angle</td></tr>
<tr><td>Outlining</td><td>Propose structures, surface missing sections</td><td>Decide the argument</td></tr>
<tr><td>First draft</td><td>Produce a complete, boring draft fast</td><td>Supply the facts and opinions</td></tr>
<tr><td>Editing</td><td>Tighten, catch inconsistencies, vary rhythm</td><td>Judge whether it is true</td></tr>
<tr><td>Repurposing</td><td>Cut clips, draft variants, write alt text</td><td>Write the hook</td></tr>
<tr><td>Metadata</td><td>Titles, descriptions, schema, internal link suggestions</td><td>Approve</td></tr>
</tbody></table>

<h2 id="not">Where it does not belong</h2>
<ul>
<li><strong>Original data.</strong> If the number was not measured, it is not a number.</li>
<li><strong>Opinions and judgement calls.</strong> The reason to read you is your view. A model does
not have one.</li>
<li><strong>Anything YMYL without expert review.</strong> Health, finance, legal — an expert
reviewer with a name and credentials, on the page.</li>
<li><strong>Volume for its own sake.</strong> Scaled content abuse policy exists specifically for
this, and enforcement is automated.</li>
</ul>

<h2 id="gates">Four review gates</h2>
<ol>
<li><strong>Information gain.</strong> Name one thing on this page that is not in the current top
three results. If you cannot, do not publish.</li>
<li><strong>Verification.</strong> Every statistic traced to a primary source and linked. Model
output is a lead, not a citation.</li>
<li><strong>Voice.</strong> Read it aloud. If it sounds like everything else, it will perform like
everything else.</li>
<li><strong>Accountability.</strong> A named author and a named reviewer, with a link to your
editorial policy.</li>
</ol>

<h2 id="disclosure">On disclosure</h2>
<p>Search engines do not require disclosure of AI assistance; they require quality. Readers,
increasingly, do care. A single line in your editorial policy describing how you use AI and what a
human is always responsible for costs nothing and defuses the objection permanently.</p>

<h2 id="economics">The economics, honestly</h2>
<p>AI lowers cost per piece and raises the risk of producing nothing that ranks. The winning
position is not "cheaper content" — it is <em>the same budget spent on fewer, deeper pieces, with
the drafting cost removed</em>. Teams that pocket the saving produce twice the volume at half the
quality and wonder why traffic fell. Model the trade-off in the
<a href="/tools/content-roi-calculator/">content ROI calculator</a>: halve cost per piece, then
halve the ranking probability, and watch the return go down, not up.</p>
"""},

{
 "slug": "creator-economy-2026-outlook",
 "cat": "Data",
 "title": "The Creator Economy in 2026: What Changed and What Pays",
 "desc": "Platform payout shifts, where rates moved, and the structural changes that matter for "
         "anyone making content for a living.",
 "read": 10,
 "sum": "Attention got cheaper, trust got more expensive, and the money moved toward owned "
        "audiences and away from platform payouts.",
 "body": """
<h2 id="shift">The structural shift</h2>
<p>Three things are true at once in 2026. Distribution has never been easier. Attention has never
been cheaper per unit. And the premium on trusted, identifiable voices has never been higher. Those
are not contradictions — they are the same fact seen from different ends. When production cost
collapses, scarcity moves to credibility.</p>

<h2 id="payouts">Platform payouts</h2>
<ul>
<li><strong>Long-form video advertising</strong> remains the most reliable platform payout, and the
niche and geography spread has widened rather than narrowed. See
<a href="/guides/youtube-rpm-by-niche/">RPM by niche</a>.</li>
<li><strong>Short-form pools</strong> continue to pay 30–100× less than long-form per view. Treat
them as distribution, never as revenue.</li>
<li><strong>Newsletter sponsorship</strong> is the healthiest per-impression market in the category,
because the inventory is scarce and the audience is verifiable.</li>
<li><strong>Podcast advertising</strong> holds firm at the premium end and is soft in the middle.
Niche B2B shows out-earn general-interest shows many times their size.</li>
</ul>

<h2 id="owned">Owned beats rented, measurably</h2>
<p>The gap between creators who own a distribution channel and creators who do not has become the
main dividing line in the category. An email list or a direct app relationship converts at
multiples of a platform follower, does not depend on a ranking system, and is an asset that can be
valued and sold. Every platform-native audience is a lease.</p>
<blockquote>The practical test: if your largest platform disabled your account tonight, how much of
your revenue survives to next month? If the answer is under 40%, that is the only problem worth
working on this quarter.</blockquote>

<h2 id="rates">Where rates moved</h2>
<table>
<thead><tr><th>Market</th><th>Direction</th><th>Why</th></tr></thead>
<tbody>
<tr><td>B2B creator sponsorships</td><td>Up</td><td>Buyers chasing attributable pipeline as paid search costs rise</td></tr>
<tr><td>General lifestyle sponsorships</td><td>Flat to down</td><td>Oversupply of comparable inventory</td></tr>
<tr><td>Usage rights / whitelisting</td><td>Up sharply</td><td>Brands using creator content as their primary ad creative</td></tr>
<tr><td>Display RPM, tier-1</td><td>Up modestly</td><td>Consolidation of quality supply</td></tr>
<tr><td>Display RPM, mixed geography</td><td>Flat</td><td>Structural, not cyclical</td></tr>
</tbody></table>
<p>The usage-rights line is the one most creators are still not charging for. It is the single
biggest unpriced asset in the category — see the
<a href="/tools/creator-rate-card-calculator/">rate card builder</a>.</p>

<h2 id="bets">Four defensible positions</h2>
<ol>
<li><strong>Own a dataset.</strong> Benchmark publishers, comparison sites and directories win
because the data is expensive to assemble and cheap to distribute.</li>
<li><strong>Own a distribution channel.</strong> Email, or a direct relationship of any kind.</li>
<li><strong>Serve a narrow, high-value audience.</strong> Twelve thousand heads of function beat a
hundred thousand general readers on every revenue line.</li>
<li><strong>Be accountable.</strong> A name, a face, a correction policy. It is the one thing
infinite content supply cannot replicate.</li>
</ol>

<h2 id="do">What to do about it this quarter</h2>
<ul>
<li>Audit revenue concentration by platform. Anything over 60% from one source is fragile.</li>
<li>Price usage rights separately on every deal from now on.</li>
<li>Start or clean the email list. Publish something worth subscribing for.</li>
<li>Pick one dataset you can assemble that nobody else has, and start collecting it.</li>
</ul>
"""},
]

BY_SLUG = {g["slug"]: g for g in GUIDES}
