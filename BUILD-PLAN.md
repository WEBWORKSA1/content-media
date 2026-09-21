# Content.Media — Phase-Wise Build Prompts

The business case, the architecture, and the exact prompts that built this site and will extend it.
Every phase is written so it can be pasted into an AI coding agent as a standalone instruction.

---

## 0. The business decision

**Domain:** `content.media` — reads as "Content Media", two of the highest-commercial-intent words
in marketing.

**The concept chosen: an independent research desk for the creator economy, monetised on five rails.**

The play is not "a blog about content". It is a **data asset with tools bolted on top**, because
that is the only structure in this category that compounds:

| Asset | Why it wins |
|---|---|
| Benchmark database | Expensive to assemble, cheap to distribute, earns citations and links forever |
| Free calculators | Rank for the highest-intent queries in the niche ("how much does YouTube pay") with no competition from listicles |
| Tool directory | Recurring visits, affiliate + paid-listing revenue, programmatically expandable |
| Guides | Convert the traffic and hold the rankings |
| Services funnel | Turns $0.02-a-visit traffic into $6,000-a-month clients |

**Why this niche over the alternatives:** marketing and business content carries an **$18–$42 page
RPM** for tier-1 traffic versus $5–$12 for general lifestyle — a 3–4× revenue multiplier on the
same traffic volume. And a single qualified services lead is worth more than a month of AdSense at
this stage, which is why the lead form, not the ad slot, is the primary conversion surface.

**Revenue stack, ranked by expected contribution in year one:**

1. **Lead generation** for content/media services — 4-step qualified form, $2,500/mo floor
2. **Display advertising** — AdSense on calculators, guides and benchmarks
3. **Directory listings** — $79 featured one-time, $299/month sponsored
4. **Affiliate** — tool directory outbound links, disclosed, never affecting rank
5. **Newsletter + video sponsorship** — priced on opens, one slot per issue
6. **Job board** — $149 standard, $299 featured, $595 bundle
7. **Reader support** — Stripe / Buy Me a Coffee / Ko-fi / GitHub Sponsors

**Research base:** 28 comparable sites were analysed before a line was written — creator-economy
publishers, AI tool directories, high-traffic calculator pages, and agency lead-gen funnels. The
patterns that survived into this build are noted per phase.

---

## Phase 1 — Foundation and design system

> Build a static site generator in Python that emits plain HTML to the repository root so GitHub
> Pages can serve it from `main` / `(root)` on the free plan. No frameworks, no build toolchain, no
> runtime server. Create `_src/config.py` holding site metadata, navigation, footer columns, ad
> slot IDs, donation rails and proof numbers — every hard-coded string on the site must resolve
> back to this one file.
>
> Write a CSS design system at `assets/css/site.css` using custom properties for colour, spacing,
> radius and type. Support light and dark themes three ways: `prefers-color-scheme`, an explicit
> `data-theme` attribute, and a persisted user toggle. Include a `[hidden] { display: none
> !important }` rule — without it a hidden fixed-position overlay silently swallows clicks across
> the entire site.
>
> Build a page shell function that takes title, description, canonical URL, body HTML and optional
> JSON-LD, and returns a complete document with Open Graph tags, Twitter card, canonical link,
> favicon, sitemap and RSS links.
>
> **Non-negotiable:** the top of *every* page carries a gradient bar reading
> "Contact, if you are interested in this website/domain name", linked to `https://web.works/contact`.

## Phase 2 — Hidden contact address and form plumbing

> The site's single contact address must never appear in any file in the repository, in
> any rendered HTML, in the sitemap, or in any JSON asset. Store it XOR-masked with key `0x5A` then
> base64-encoded as a single token in config. In `assets/js/site.js`, reassemble it at runtime only
> inside the browser.
>
> Every form on the site posts as JSON to the FormSubmit AJAX gateway, with the endpoint URL built
> from that runtime-decoded token. Every `mailto:` link is written into the DOM at runtime by the
> same function, never present in source. Add `_subject`, `_template`, page path, referrer and
> timestamp to every submission so the inbox is sortable.
>
> Provide a `FORM_ALIAS` config slot so the address can be swapped for FormSubmit's `/el/<alias>`
> once activated, removing it from the wire entirely.
>
> **Verify with:** have the build decode the token in memory and scan every file for the address,
> failing the build on any match — so the check itself never writes the address down.

## Phase 3 — The calculator engine (the traffic engine)

> Publish every benchmark constant the site uses in a single readable file at
> `assets/js/benchmarks.js`: RPM by 14 niches, geography multipliers, monetised-view share,
> Shorts pool rates, Instagram and TikTok engagement bands across 6 follower tiers, rate-card
> anchors for 11 deliverable types, niche/usage/exclusivity multipliers, podcast and newsletter
> CPM by slot, display RPM by category, production cost anchors, funnel constants.
>
> Build one generic engine at `assets/js/calc.js` driven by a `data-calc="<engine>"` attribute.
> Each engine returns a headline range, three summary cells, a comparison bar chart, an optional
> table, a total, and an array of plain-English assumptions. Render the assumptions on the page
> under every result — this is the differentiator and it doubles as the SEO body copy.
>
> **Rules taken from the research:**
> - Always return a LOW–HIGH range. Never a single number. Fake precision destroys trust.
> - Widget first, above the fold. Prose after. (Omnicalculator pattern.)
> - Never gate the headline number. Gate the deeper artefact instead.
> - Print daily / monthly / yearly breakdowns.
> - Add Reset, Copy result and Share controls, plus a "was this helpful" micro-poll.
>
> Ship ten calculators: YouTube money, Shorts RPM, TikTok earnings, Instagram engagement, creator
> rate card, CPM/RPM/CPC/ROAS, podcast sponsorship, newsletter sponsorship, content ROI, channel
> growth forecast. Each gets a methodology section, a benchmark table, FAQ with `FAQPage` schema,
> `WebApplication` schema, a related-tools strip, and a sidebar with table of contents and a
> conversion panel.

## Phase 4 — Benchmark database (the citation magnet)

> Build `/benchmarks/` as a single long reference page publishing every constant from Phase 3 in
> formatted tables, with a methodology section, a `Dataset` JSON-LD block, a CC-BY licence line and
> an explicit citation string. Generate a real downloadable CSV of the whole dataset at build time
> and link it — never promise a download that does not exist.
>
> This is the recurring data product (the Tubefilter Charts pattern): one fixed URL, refreshed
> quarterly, infinitely re-linkable, and it is what earns the backlinks that make everything else
> rank.

## Phase 5 — Tool directory

> Build a client-side faceted directory over a JSON dataset. Card anatomy: logo, name, tagline,
> editor note, pricing badge, category tags, verified badge, vote count, rating, editor score.
>
> Ten filters: category with live counts, pricing model, price range, free-tier toggle, modality,
> platform, integrations, use case, minimum rating, verified/featured. Seven sorts: trending,
> popular, highest rated (log-weighted), editor score, newest, price, A–Z. Debounced instant
> search. Mirror all state to the URL so every filtered view is shareable.
>
> **The differentiator:** every listing carries an editor note saying what the tool is genuinely
> bad at, and the submission form asks founders that question directly. Listings that dodge it are
> declined.
>
> Build `/directory/submit/` with three tiers — free, $79 featured, $299/month sponsored — and
> state in writing that ratings, editor scores and notes are never for sale.

## Phase 6 — The lead generation funnel (the highest-value surface)

> Build a 4-step progressive form. **Step 1 asks zero personal information** — a single
> card-style choice that auto-advances on click. Commitment-consistency does more for completion
> than any field-count optimisation.
>
> - Step 1: what kind of content work (6 card options)
> - Step 2: monthly volume, timeline, primary goal
> - Step 3: budget band, company size, industry — the qualifier
> - Step 4: name, work email, company, URL, optional phone, optional notes
>
> Progress bar plus "Step N of 4". Per-step validation only on visible fields. Button copy names
> the outcome: "Send my custom content plan", never "Submit".
>
> **The graceful downsell:** microcopy on step 3 reads "We work best from $2,500/month. Below
> that, we'll send you our DIY playbook instead — free." This anchors price, filters without
> insulting anyone, and converts unqualified traffic into a list.
>
> Redirect to a dedicated `/services/thank-you/` page — a real URL for conversion tracking, a
> second offer, and a spam-folder nudge.
>
> Add a sticky bottom CTA that appears at 45% scroll and is dismissible with a persisted
> preference. Publish pricing openly on `/services/` — hiding it wastes everyone's time and
> costs more leads than it protects.

## Phase 7 — Monetisation surfaces

> **AdSense:** main script in `<head>` on every page from a config publisher ID; responsive
> display, in-article fluid and sidebar units rendered from one helper. Write `ads.txt` at the
> domain root with `google.com, pub-XXXX, DIRECT, f08c47fec0942fa0` (note: `pub-` in ads.txt,
> `ca-pub-` in the script tag). While the publisher ID is still a placeholder, render an HTML
> comment instead of an empty box — blank reserved inventory looks broken and reads as low-value.
>
> Safe density: 3–5 units on a long desktop article; on mobile one above the fold, 1–2 in-content,
> one anchor maximum.
>
> **Donations** at `/support/`: three tiers with the middle one highlighted, annual default with
> the saving shown, a monthly/one-time segmented toggle, a supporter-count goal bar, a published
> breakdown of where the money goes, and four rails that work without a backend — Stripe Payment
> Links, Buy Me a Coffee, Ko-fi, GitHub Sponsors. Frame the pitch as independence, never charity.
>
> **Advertise page** at `/advertise/`: publish audience metrics openly, gate the full rate card
> behind a five-field form, state a price floor and a minimum term. Never print an audience number
> you have not measured — render "current figure on request" until it is real.
>
> **Contests** at `/contests/` with a countdown, plus a separate permanent `/contests/official-rules/`
> carrying all twelve required US elements, the Canadian skill-testing question, the free alternate
> method of entry, published odds, and the tax note. An unbundled marketing opt-in, per CASL.
>
> **Job board** at `/jobs/` with a paid posting funnel, and a published rule that listings without
> a salary range are declined.

## Phase 8 — Editorial library

> Write twelve reference guides that pass the information-gain test: AdSense approval checklist,
> creator rate card guide, YouTube RPM by niche, lead generation for content sites, newsletter
> monetisation, content repurposing, programmatic SEO, donation-funded media, running a legal
> contest, media kits, AI content workflow, creator economy outlook.
>
> Each carries: a "short version" callout, `Article` schema, a table of contents built from the
> H2s, a byline with reviewer and updated date, in-article ad slots, a helpful-poll, related
> guides, and internal links into the calculators. Filterable hub page by category.

## Phase 9 — SEO, search and trust pages

> Generate `sitemap.xml` with per-page priority and change frequency, `robots.txt` excluding
> thank-you and search pages, `feed.xml`, and a JSON search index powering both a `/` keyboard
> overlay (with `⌘K` support and arrow-key navigation) and a standalone `/search/` page.
>
> Ship every page AdSense requires before review: About, Contact, Privacy (naming Google's
> advertising cookies explicitly and covering GDPR/CCPA/PIPEDA), Cookie policy, Terms, Advertising
> & affiliate disclosure, Editorial policy, DMCA, and a useful 404.

## Phase 10 — Ship

> Build, then verify before pushing:
> - the build's own address scan passes (it fails the build on any exposure)
> - every internal `href` resolves to a built file
> - every page contains the domain-enquiry bar and the `web.works/contact` link
> - calculators recompute on input change, in a real browser
> - directory loads and filters
> - the lead form advances between steps
> - `document.documentElement.scrollWidth <= 390` at phone width
> - screenshot desktop, mobile and dark mode and actually look at them
>
> Then: `.nojekyll`, `CNAME`, `.github/FUNDING.yml`, commit, push to
> `github.com/webworksa1/content-media`, enable Pages on `main` / `(root)`.

---

## Post-launch sequence

| When | Do this |
|---|---|
| Day 0 | Point `content.media` DNS at GitHub Pages, enable HTTPS |
| Day 0 | Verify in Search Console, submit `sitemap.xml` |
| Week 1 | Set real IDs in `_src/config.py`: AdSense publisher + slots, GA4, Stripe links |
| Week 1 | Activate FormSubmit by submitting one form, then set `FORM_ALIAS` |
| Week 2 | Add a Google-certified CMP before taking EEA/UK traffic |
| Week 2–4 | Publish 8–10 more guides — 20–30 substantial pages is the practical AdSense bar |
| Week 4 | Apply for AdSense once there is organic traffic and no placeholder pages |
| Month 2 | Expand the directory past 200 tools; open paid listings |
| Month 2 | Launch the newsletter; set real `AUDIENCE` figures once measured |
| Month 3 | First quarterly benchmark refresh + a press push on the data |
| Ongoing | Add calculators. Each one is a new high-intent entry point at near-zero marginal cost. |

## Expandability

Everything is data-driven. To extend:

| To add | Edit | Effort |
|---|---|---|
| A calculator | `_src/pages_tools.py` spec + an engine in `assets/js/calc.js` | ~30 min |
| A guide | One dict in `_src/guides.py` | ~1 hour |
| Directory tools | Rows in `_src/data/tools.py` | seconds each |
| A job listing | `JOBS` in `_src/pages_content.py` | seconds |
| A video | `VIDEOS` in `_src/pages_content.py` | seconds |
| Nav, footer, ads, donations | `_src/config.py` | seconds |

Then `python3 build.py` and push. The sitemap, search index, RSS feed and benchmark CSV all
regenerate themselves.
