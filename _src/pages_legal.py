# -*- coding: utf-8 -*-
"""Trust, legal and utility pages. AdSense requires most of these to exist."""
from config import SITE, PROOF
from layout import page, ad
from components import (breadcrumbs, section_head, faq, cta_band, newsletter_block,
                        simple_form, mail_link, stat_row)

UPDATED = "21 September 2026"


def _legal(title, desc, slug, inner, crumb):
    body = f'''<section class="band">
  <div class="wrap" style="max-width:820px">
    {breadcrumbs([("Home", "/"), (crumb, f"/{slug}/")])}
    <h1>{title}</h1>
    <p class="small muted">Last updated {UPDATED}</p>
    <article class="prose">{inner}</article>
  </div>
</section>'''
    return page(f"{title} | {SITE['name']}", desc, f"/{slug}/", body)


def build_about():
    body = f'''<section class="band">
  <div class="wrap" style="max-width:900px">
    {breadcrumbs([("Home", "/"), ("About", "/about/")])}
    <h1>About Content.Media</h1>
    <p class="lede">We are an independent research desk for the creator economy. We publish the
    numbers people usually keep private — RPM by niche, sponsorship rates, engagement benchmarks,
    production costs — and we build free tools on top of them.</p>
    {stat_row([(PROOF['niches'], "Niches benchmarked", "Refreshed quarterly"),
               (PROOF['tools_indexed'], "Tools reviewed", "None paid for their rating"),
               (PROOF['calculators'], "Free calculators", "No email gate"),
               (PROOF['guides'], "Reference guides", "All free, none gated")])}
    <article class="prose" style="margin-top:2rem">
      <h2 id="why">Why this exists</h2>
      <p>Most creators are undercharging, and most publishers are leaving revenue on the table,
      for the same reason: nobody publishes the numbers. Rate cards are private, RPM is anecdotal,
      and every "calculator" online is a lead magnet that multiplies your views by an invented
      constant. We decided to publish the constants instead.</p>
      <p>Everything on this site is free. There is no paywall, no gated PDF holding your own
      numbers hostage, and no "book a call to find out pricing".</p>

      <h2 id="how">How we make money</h2>
      <p>Four ways, all visible:</p>
      <ol>
        <li><strong>Display advertising.</strong> Standard ad units on content pages.</li>
        <li><strong>Labelled sponsorships and featured listings.</strong> Visibility is for sale.
        Ratings, editor scores and editor notes are not, at any price.</li>
        <li><strong>Our services business.</strong> We build and run content programmes for brands
        and publishers, using the models published here.</li>
        <li><strong>Reader support.</strong> Voluntary, from $5 a month, with a published breakdown
        of where it goes.</li>
      </ol>
      <p>Full detail in our <a href="/disclosure/">advertising and affiliate disclosure</a>.</p>

      <h2 id="transparency">Transparency</h2>
      <p>We publish a revenue and cost post every quarter, including the things that did not work.
      Fourteen percent of everything that comes in goes into the contest prize pool, which goes
      back to independent creators — many of whom contributed the rate data in the first place.</p>

      <h2 id="standards">Editorial standards</h2>
      <p>Every benchmark prints its methodology. Every calculator prints its constants. Every
      directory listing carries an honest note about what the tool is bad at, and we ask founders
      to tell us themselves on the submission form. When we get something wrong we correct it in
      place, with a note. Read the full <a href="/editorial-policy/">editorial policy</a>.</p>

      <h2 id="contact">Talk to us</h2>
      <p>Corrections, data requests, press enquiries and partnership questions all go through the
      <a href="/contact/">contact page</a>. We read everything and reply to most things within a
      business day.</p>

      <h2 id="domain">About this domain</h2>
      <p>Enquiries about acquiring this website or the <strong>content.media</strong> domain name
      go through the bar at the top of every page, or directly at
      <a href="{SITE['owner_contact_url']}" rel="noopener" target="_blank">web.works/contact</a>.</p>
    </article>
    {newsletter_block()}
  </div>
</section>
{cta_band("Want us to build your content operation?",
          "Costed plan in one business day, using the models published on this site.")}'''
    return page("About Content.Media — Independent Creator Economy Research",
                "Who we are, how we make money, and the editorial standards behind every "
                "benchmark and calculator on this site.",
                "/about/", body)


def build_contact():
    form = simple_form("contact", "Send us a message", [
        {"name": "name", "label": "Name", "type": "text", "required": True, "autocomplete": "name"},
        {"name": "email", "label": "Email", "type": "email", "required": True, "autocomplete": "email"},
        {"name": "topic", "label": "What is this about?", "type": "select", "required": True,
         "options": ["A correction — a number looks wrong",
                     "Data request — CSV or a custom cut",
                     "Advertising or sponsorship",
                     "Submitting or updating a tool listing",
                     "Services — I want a content plan",
                     "Press or interview request",
                     "Contest question",
                     "Buying this website or domain name",
                     "Something else"]},
        {"name": "company", "label": "Company (optional)", "type": "text", "required": False,
         "autocomplete": "organization"},
        {"name": "message", "label": "Message", "type": "textarea", "required": True,
         "placeholder": "Be specific — it gets you a faster and better answer."},
    ], button="Send message",
       note="We reply to most messages within one business day. Corrections get priority over "
            "everything else.")

    body = f'''<section class="band">
  <div class="wrap article-layout">
    <article>
      {breadcrumbs([("Home", "/"), ("Contact", "/contact/")])}
      <h1>Contact</h1>
      <p class="lede">One inbox, monitored on business days. Corrections jump the queue — if a
      number on this site is wrong, telling us is the single most useful thing you can do.</p>
      {form}
      <p class="small muted" style="margin-top:1rem">Prefer email?
      {mail_link("Open a message in your mail app", "Content.Media enquiry")} — the address is
      assembled in your browser, which is how we keep it away from scrapers.</p>
    </article>
    <aside class="sidebar">
      <div class="panel panel--compact">
        <h3 style="font-size:1rem">Buying this website or domain?</h3>
        <p class="small muted">Enquiries about acquiring <strong>content.media</strong> go here.</p>
        <a class="btn btn--primary btn--block" href="{SITE['owner_contact_url']}"
           rel="noopener" target="_blank">web.works/contact</a>
      </div>
      <div class="panel panel--compact">
        <h3 style="font-size:1rem">Fastest routes</h3>
        <ul class="ticks small">
          <li><a href="/services/#quote">Content plan</a> — one business day</li>
          <li><a href="/advertise/">Media kit</a> — rate card by email</li>
          <li><a href="/directory/submit/">Tool submission</a> — 48h on paid tiers</li>
          <li><a href="/jobs/post/">Post a job</a> — reviewed same day</li>
        </ul>
      </div>
      {ad("sidebar", style="sidebar")}
    </aside>
  </div>
</section>'''
    return page("Contact Content.Media",
                "Corrections, data requests, advertising, services and domain enquiries. "
                "We reply within one business day.",
                "/contact/", body)


def build_privacy():
    inner = f'''
<p>This policy explains what Content.Media collects, why, and what you can do about it. It applies
to everything served from content.media.</p>

<h2 id="collect">What we collect</h2>
<ul>
<li><strong>Information you give us.</strong> When you submit a form — a content plan request, a
newsletter signup, a tool submission, a job posting, a contest entry or a contact message — we
receive the fields you completed, plus the page you submitted from and the time of submission.</li>
<li><strong>Usage data.</strong> Standard analytics: pages viewed, approximate location derived
from IP, device type, referring site. We do not attempt to identify individuals from this.</li>
<li><strong>Calculator inputs are not collected.</strong> Every calculator on this site runs
entirely in your browser. Nothing you type into a calculator is transmitted to us or to anyone
else, ever.</li>
</ul>

<h2 id="use">How we use it</h2>
<p>To answer you, to deliver what you asked for, to run the site, and to understand which pages are
useful. We do not sell personal information. We do not share your email address with advertisers or
sponsors — sponsors buy a placement inside an email, never the list behind it.</p>

<h2 id="advertising">Advertising and third-party cookies</h2>
<p>We use Google AdSense to serve advertising. Third-party vendors, including Google, use cookies
to serve ads based on your prior visits to this and other websites.</p>
<ul>
<li>Google's use of advertising cookies enables it and its partners to serve ads to you based on
your visit to this site and other sites on the internet.</li>
<li>You may opt out of personalised advertising by visiting
<a href="https://www.google.com/settings/ads" rel="nofollow noopener" target="_blank">Google Ads Settings</a>.</li>
<li>You can opt out of third-party vendor cookies for personalised advertising at
<a href="https://www.aboutads.info/choices/" rel="nofollow noopener" target="_blank">aboutads.info/choices</a>
or <a href="https://www.youronlinechoices.com/" rel="nofollow noopener" target="_blank">youronlinechoices.com</a>.</li>
<li>Visitors in the EEA, the UK and Switzerland are served a Google-certified consent management
platform and advertising cookies are not set without consent.</li>
</ul>

<h2 id="processors">Who processes data for us</h2>
<table>
<thead><tr><th>Processor</th><th>Purpose</th></tr></thead>
<tbody>
<tr><td>Google AdSense</td><td>Advertising delivery and measurement</td></tr>
<tr><td>Google Analytics</td><td>Aggregate usage analytics</td></tr>
<tr><td>Form delivery service</td><td>Relays form submissions to our inbox</td></tr>
<tr><td>Email service provider</td><td>Sends the weekly brief</td></tr>
<tr><td>Payment provider</td><td>Processes supporter contributions — we never see card details</td></tr>
<tr><td>Static hosting provider</td><td>Serves this website</td></tr>
<tr><td>Video platform</td><td>Serves embedded video, only after you click play</td></tr>
</tbody></table>

<h2 id="video">Embedded video</h2>
<p>Video embeds on this site load only when you click them, and use the privacy-enhanced
domain. Until you press play, no video-platform cookie is set.</p>

<h2 id="storage">Local storage</h2>
<p>We store a small number of preferences in your browser: your colour-theme choice, whether you
dismissed the bottom call-to-action, and your answer to the "was this helpful" poll. These never
leave your device and are not readable by us.</p>

<h2 id="rights">Your rights</h2>
<p>Depending on where you live, you may have the right to access, correct, delete or port your
personal information, to object to processing, and to withdraw consent. Residents of the EEA and
UK have these rights under the GDPR; residents of California have rights under the CCPA/CPRA,
including the right not to be discriminated against for exercising them; residents of Canada have
rights under PIPEDA and applicable provincial law. To exercise any of them, use the
<a href="/contact/">contact form</a> and select "Something else" — we action requests within 30 days.</p>

<h2 id="retention">Retention</h2>
<p>Form submissions are retained for as long as needed to answer you and for our business records,
typically 24 months. Newsletter subscriptions are retained until you unsubscribe. Aggregate
analytics are retained for 14 months.</p>

<h2 id="children">Children</h2>
<p>This site is not directed at children under 13 (or under 16 in the EEA) and we do not knowingly
collect their personal information. Contest entry requires you to be 18 or older.</p>

<h2 id="changes">Changes</h2>
<p>If this policy changes materially we will update the date at the top and note the change on this
page. Continued use after that constitutes acceptance.</p>

<h2 id="contactus">Contact</h2>
<p>Privacy questions go through the <a href="/contact/">contact form</a>, or
{mail_link("by email", "Privacy request")}.</p>
'''
    return _legal("Privacy policy",
                  "What Content.Media collects, how advertising cookies are used, who processes "
                  "data for us, and how to exercise your privacy rights.",
                  "privacy", inner, "Privacy")


def build_cookies():
    inner = '''
<p>A cookie is a small file a website stores in your browser. This page explains which ones this
site uses and how to control them.</p>

<h2 id="categories">Categories we use</h2>
<table>
<thead><tr><th>Category</th><th>Purpose</th><th>Set without consent?</th></tr></thead>
<tbody>
<tr><td>Strictly necessary</td><td>Security and basic delivery of the site</td><td>Yes</td></tr>
<tr><td>Preferences (local storage, not cookies)</td><td>Theme choice, dismissed banners, poll answers</td><td>Yes — never leaves your device</td></tr>
<tr><td>Analytics</td><td>Aggregate page and traffic measurement</td><td>No in the EEA/UK/CH</td></tr>
<tr><td>Advertising</td><td>Ad delivery, frequency capping, personalisation</td><td>No in the EEA/UK/CH</td></tr>
<tr><td>Video</td><td>Set by the video platform, only after you press play</td><td>No</td></tr>
</tbody></table>

<h2 id="consent">Consent</h2>
<p>Visitors in the European Economic Area, the United Kingdom and Switzerland are shown a
Google-certified consent management platform on first visit. Analytics and advertising cookies are
not set until consent is given, and you can change or withdraw your choice at any time from the
link in the site footer of the consent tool.</p>

<h2 id="control">Controlling cookies yourself</h2>
<ul>
<li>Every major browser lets you block or delete cookies in its privacy settings.</li>
<li>Personalised advertising can be turned off at
<a href="https://www.google.com/settings/ads" rel="nofollow noopener" target="_blank">Google Ads Settings</a>.</li>
<li>Industry-wide opt-outs are available at
<a href="https://www.aboutads.info/choices/" rel="nofollow noopener" target="_blank">aboutads.info/choices</a>
and <a href="https://www.youronlinechoices.com/" rel="nofollow noopener" target="_blank">youronlinechoices.com</a>.</li>
</ul>
<p>Blocking advertising cookies does not remove the advertising — it makes it less relevant and
lowers what it earns. That is a trade-off you are entitled to make.</p>

<h2 id="calculators">One thing worth repeating</h2>
<p>The calculators on this site run entirely in your browser. Nothing you type into them is stored,
transmitted or associated with any cookie.</p>
'''
    return _legal("Cookie policy",
                  "Which cookies Content.Media uses, which require consent, and how to control "
                  "or opt out of them.",
                  "cookies", inner, "Cookies")


def build_terms():
    inner = f'''
<p>By using content.media you agree to these terms. If you do not agree, please do not use the site.</p>

<h2 id="use">1. Use of the site</h2>
<p>You may read, share and cite this site freely. You may not scrape it at a volume that degrades
service for others, republish substantial portions wholesale, or present our research as your own
work. Automated access to the calculators or the directory data for commercial resale is not
permitted without written agreement.</p>

<h2 id="content">2. Our content and your licence to use it</h2>
<p>Text, data tables, calculators and code on this site are the property of the site operator.
Benchmark tables may be quoted and reproduced with attribution and a link to the source page —
journalists, analysts, students and creators are explicitly welcome to do this. Everything else
requires permission.</p>

<h2 id="estimates">3. Estimates are estimates</h2>
<p><strong>Every figure on this site is a modelled estimate, not a guarantee.</strong> RPM ranges,
rate cards, engagement benchmarks, ROI projections and cost anchors are built from aggregated data
and stated assumptions, and your actual results will differ. Nothing here is financial, legal, tax
or investment advice. Decisions you make using these numbers are yours.</p>

<h2 id="thirdparty">4. Third-party links and listings</h2>
<p>The directory links to third-party products. We do not control them, we are not responsible for
them, and a listing is not a warranty. Some links are affiliate links — see our
<a href="/disclosure/">disclosure</a>. Always evaluate a tool against your own requirements.</p>

<h2 id="submissions">5. Submissions</h2>
<p>When you submit a tool, a job, a contest entry or a correction, you grant us a non-exclusive
right to publish and edit that submission. You confirm you have the right to submit it. We may
decline, edit or remove any submission at our discretion, and paid submissions are only charged
after approval.</p>

<h2 id="services">6. Services engagements</h2>
<p>Content plans supplied through the services form are non-binding proposals. Any engagement is
governed by a separate written agreement, which takes precedence over these terms.</p>

<h2 id="contests">7. Contests</h2>
<p>Contests are governed by their own
<a href="/contests/official-rules/">official rules</a>, which take precedence over these terms for
matters relating to that promotion.</p>

<h2 id="liability">8. Limitation of liability</h2>
<p>To the fullest extent permitted by law, the site operator is not liable for any indirect,
incidental or consequential loss arising from use of this site or reliance on its figures. The site
is provided "as is" without warranties of any kind.</p>

<h2 id="changes">9. Changes</h2>
<p>We may update these terms. Material changes will be noted with an updated date at the top of
this page.</p>

<h2 id="law">10. Governing law</h2>
<p>These terms are governed by the laws of the Province of Quebec, Canada, without regard to
conflict-of-law principles.</p>

<h2 id="contact">11. Contact</h2>
<p>Questions about these terms go through the <a href="/contact/">contact form</a>. Enquiries about
acquiring this website or the domain name go to
<a href="{SITE['owner_contact_url']}" rel="noopener" target="_blank">web.works/contact</a>.</p>
'''
    return _legal("Terms of use",
                  "Terms governing use of Content.Media, including citation rights, the estimate "
                  "disclaimer, submissions and limitation of liability.",
                  "terms", inner, "Terms")


def build_disclosure():
    inner = '''
<p>This page exists so you never have to guess whether money influenced something you read here.</p>

<h2 id="ads">Display advertising</h2>
<p>We run display advertising, including Google AdSense. Advertisers have no input into editorial
content, cannot see what we are working on, and cannot buy placement next to specific coverage
beyond standard section targeting.</p>

<h2 id="affiliate">Affiliate links</h2>
<p>Some outbound links to tools earn us a commission if you subscribe. This costs you nothing.
Critically:</p>
<ul>
<li>Affiliate status <strong>never</strong> affects whether a tool is listed, its rating, its
editor score or its position in the directory.</li>
<li>Tools with no affiliate programme are listed and ranked identically.</li>
<li>Several tools we rate highly pay us nothing. Several that pay well are rated poorly.</li>
<li>Affiliate links carry <code>rel="sponsored"</code>.</li>
</ul>

<h2 id="featured">Featured and sponsored listings</h2>
<p>Tools can pay for a featured listing ($79 one-time) or a sponsored category placement
($299/month). These buy <em>visibility</em>, and they are labelled as featured or sponsored
everywhere they appear, including on the card itself.</p>
<p><strong>What is not for sale, at any price:</strong> ratings, editor scores, editor notes,
benchmark figures, inclusion in a "best of" list, or removal of a criticism. We have declined
listings from paying advertisers and will again.</p>

<h2 id="newsletter">Newsletter sponsorship</h2>
<p>The weekly brief carries a maximum of one labelled primary sponsor slot and up to three
classifieds. Sponsors never receive the subscriber list, and never see editorial content before
publication.</p>

<h2 id="services">Our services business</h2>
<p>We sell content strategy and production services. That is a conflict worth naming: we publish
research that makes the case for investing in content, and we sell content services. We manage it
by publishing our pricing openly, publishing the models and constants so you can run the numbers
without us, and telling prospects when a retainer is the wrong answer.</p>

<h2 id="contests">Contests</h2>
<p>Contest prize pools are funded by reader support (14% of contributions) and by named sponsors.
Sponsors have no say in who wins. Judging criteria are published before entry opens.</p>

<h2 id="corrections">Corrections</h2>
<p>When we get something wrong we correct it in place and add a dated note. Nobody can pay to have
a correction removed or a criticism softened. If you think something here is wrong, the
<a href="/contact/">contact form</a> is the fastest route and corrections jump the queue.</p>
'''
    return _legal("Advertising & affiliate disclosure",
                  "How Content.Media makes money, what advertisers can and cannot buy, and why "
                  "ratings and editor notes are never for sale.",
                  "disclosure", inner, "Disclosure")


def build_editorial():
    inner = '''
<p>How we research, what we will not do, and how to hold us to it.</p>

<h2 id="sources">Sources</h2>
<p>Benchmark figures are assembled from four kinds of source: public platform disclosures and
payout terms; publicly reported advertiser CPMs; rate-card data contributed by creators and media
buyers, anonymised and aggregated; and our own client work. Ranges published are the 20th to 80th
percentile of what we see, not absolute extremes.</p>

<h2 id="publish">We publish our constants</h2>
<p>Every calculator prints the exact figures it used underneath the result, and the full constants
file is served at <code>/assets/js/benchmarks.js</code>. You can read it, fork it, or use it to
show that we are wrong. That is the point.</p>

<h2 id="ai">How we use AI</h2>
<p>We use AI assistants for research, outlining, first drafts and metadata. We do not use them for
original data, opinions, or anything published without a human verifying it against a primary
source. A named human is responsible for every page. Our full
<a href="/guides/ai-content-workflow/">workflow is published as a guide</a>.</p>

<h2 id="independence">Independence</h2>
<ul>
<li>Advertisers and sponsors never see content before publication.</li>
<li>Ratings, editor scores and editor notes are not for sale.</li>
<li>We decline listings for tools we would not recommend, including from paying advertisers.</li>
<li>Reader supporters get access and a call, never influence over a figure.</li>
</ul>

<h2 id="corrections">Corrections policy</h2>
<p>Errors are corrected in place, with a dated note at the foot of the page explaining what changed.
Substantive corrections to a benchmark figure are also noted in the next weekly brief. We do not
quietly edit numbers.</p>
<p>To report an error, use the <a href="/contact/">contact form</a> and select "A correction".
Corrections are handled ahead of everything else, including sales enquiries.</p>

<h2 id="reviews">How directory listings are written</h2>
<p>Every tool is used or trialled before listing. The editor note is required to say something
specific about what the tool is bad at — we ask founders to answer that question themselves on the
submission form, and submissions that dodge it are declined. Listings are re-checked when a tool
materially changes its pricing or feature set.</p>

<h2 id="standards">What we will not publish</h2>
<ul>
<li>A figure we cannot source or model transparently.</li>
<li>A "best of" list assembled from affiliate payouts.</li>
<li>Screenshots or data we do not have the right to use.</li>
<li>Content written to fill a keyword gap with nothing new in it.</li>
</ul>
'''
    return _legal("Editorial policy",
                  "How Content.Media researches, how we use AI, our corrections policy, and the "
                  "independence rules that govern every benchmark and listing.",
                  "editorial-policy", inner, "Editorial policy")


def build_dmca():
    inner = f'''
<p>We respect copyright and expect the same from others. If you believe material on this site
infringes your copyright, this page explains how to tell us.</p>

<h2 id="notice">Submitting a notice</h2>
<p>Send a written notice through the <a href="/contact/">contact form</a>, or
{mail_link("by email", "DMCA notice")}, including all of the following:</p>
<ol>
<li>A physical or electronic signature of the copyright owner or a person authorised to act on
their behalf.</li>
<li>Identification of the copyrighted work claimed to have been infringed.</li>
<li>The URL of the material on this site that you claim is infringing, specific enough for us to
locate it.</li>
<li>Your name, postal address, telephone number and email address.</li>
<li>A statement that you have a good-faith belief that the use is not authorised by the copyright
owner, its agent, or the law.</li>
<li>A statement, made under penalty of perjury, that the information in your notice is accurate and
that you are the copyright owner or authorised to act on their behalf.</li>
</ol>

<h2 id="response">What happens next</h2>
<p>We review every notice and, where it is complete and appears valid, remove or disable access to
the material promptly and notify whoever posted it. Incomplete notices will be returned with an
explanation of what is missing.</p>

<h2 id="counter">Counter-notice</h2>
<p>If your material was removed and you believe that was a mistake or a misidentification, you may
send a counter-notice containing your signature, identification of the removed material and its
location before removal, a statement under penalty of perjury that you have a good-faith belief the
removal was a mistake, your contact details, and your consent to the jurisdiction of the relevant
court.</p>

<h2 id="repeat">Repeat infringers</h2>
<p>Accounts, submitters or contributors who repeatedly infringe are removed and barred from further
submissions.</p>

<h2 id="citation">A note on our own content</h2>
<p>Our benchmark tables may be quoted and reproduced with attribution and a link. You do not need
permission for that, and we would rather you cite us than paraphrase us badly.</p>
'''
    return _legal("DMCA & copyright",
                  "How to submit a copyright infringement notice or counter-notice to "
                  "Content.Media, and what happens next.",
                  "dmca", inner, "DMCA")


def build_404():
    body = f'''<section class="band">
  <div class="wrap" style="max-width:720px;text-align:center">
    <p class="eyebrow">Error 404</p>
    <h1>That page isn't here</h1>
    <p class="lede">Either it moved, or the link was wrong. Here is where most people were going.</p>
    <div class="grid g3" style="margin:2rem 0">
      <a class="card" href="/tools/"><h3>Free calculators</h3><p>Ten of them, no signup.</p></a>
      <a class="card" href="/benchmarks/"><h3>The benchmarks</h3><p>Every number, published.</p></a>
      <a class="card" href="/directory/"><h3>Tool directory</h3><p>Honestly reviewed, filterable.</p></a>
    </div>
    <p><a class="btn btn--primary btn--lg" href="/">Back to the homepage</a>
       <a class="btn btn--ghost btn--lg" href="/contact/">Tell us about the broken link</a></p>
  </div>
</section>'''
    return page("Page not found | Content.Media",
                "That page could not be found.", "/404.html", body,
                extra_head='<meta name="robots" content="noindex,follow">')


def build_search():
    body = f'''<section class="band">
  <div class="wrap" style="max-width:820px">
    {breadcrumbs([("Home", "/"), ("Search", "/search/")])}
    <h1>Search</h1>
    <p class="lede">Everything on this site, searchable. Press <kbd>/</kbd> anywhere to open the
    quick search overlay.</p>
    <div class="panel">
      <input type="search" id="pageSearch" placeholder="Try “RPM”, “rate card”, “AdSense”, “sponsorship”…"
             aria-label="Search the site" autofocus>
      <ul class="search-results" id="pageResults" style="max-height:none"></ul>
    </div>
  </div>
</section>
<script>
(function(){{
  var i=document.getElementById('pageSearch'),r=document.getElementById('pageResults'),data=null;
  function draw(q){{
    q=(q||'').trim().toLowerCase();
    var list=(data||[]);
    if(q) list=list.filter(function(it){{return (it.t+' '+it.d+' '+(it.k||'')).toLowerCase().indexOf(q)>-1;}});
    r.innerHTML=list.length?list.slice(0,40).map(function(it){{
      return '<li><a href="'+(window.cmUrl||String)(it.u)+'"><strong>'+it.t+'</strong><small>'+it.d+'</small></a></li>';
    }}).join(''):'<li class="empty">Nothing matched.</li>';
  }}
  var U=window.cmUrl||String;
  fetch(U('/assets/data/search-index.json')).then(function(x){{return x.json();}}).then(function(j){{
    data=j;
    var p=new URLSearchParams(location.search).get('q');
    if(p){{i.value=p;}} draw(i.value);
  }});
  i.addEventListener('input',function(){{draw(i.value);}});
}})();
</script>'''
    return page("Search | Content.Media", "Search every calculator, guide, benchmark and tool "
                "listing on Content.Media.", "/search/", body,
                extra_head='<meta name="robots" content="noindex,follow">')
