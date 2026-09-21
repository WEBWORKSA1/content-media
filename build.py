#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Content.Media static site generator.

    python3 build.py

Writes plain HTML to the repository root so GitHub Pages can serve it from
`main` / `(root)` on the free plan. Nothing here needs a server at runtime.
"""
import json
import os
import sys
import shutil
from datetime import date

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ROOT, "_src"))
sys.path.insert(0, os.path.join(ROOT, "_src", "data"))

from config import SITE, ADS, DONATE, PROOF          # noqa: E402
import pages_home, pages_tools, pages_content, pages_money, pages_legal  # noqa: E402
from guides import GUIDES                             # noqa: E402
import tools as tooldata                              # noqa: E402

PAGES = {}     # url path -> html
SITEMAP = []   # (url, priority, changefreq)
INDEX = []     # search index records


def emit(path, html, priority=0.6, freq="monthly", index=True,
         title=None, desc=None, keywords=""):
    PAGES[path] = html
    if index:
        SITEMAP.append((path, priority, freq))
    if title:
        INDEX.append({"t": title, "d": desc or "", "u": path, "k": keywords})


def minify(html):
    """Strip indentation and blank lines outside <div class="code"> blocks.
    Code blocks keep their whitespace (they render with white-space: pre)."""
    import re
    parts = re.split(r'(<div class="code">.*?</div>)', html, flags=re.S)
    out = []
    for i, part in enumerate(parts):
        if i % 2:
            out.append(part)
        else:
            lines = [ln.strip() for ln in part.split("\n")]
            out.append("\n".join(ln for ln in lines if ln))
    return "".join(out)


def write_all():
    written = 0
    for path, html in PAGES.items():
        if path.endswith(".html"):
            target = os.path.join(ROOT, path.lstrip("/"))
        else:
            target = os.path.join(ROOT, path.strip("/"), "index.html")
        os.makedirs(os.path.dirname(target), exist_ok=True)
        with open(target, "w", encoding="utf-8") as f:
            f.write(minify(html))
        written += 1
    return written


# ---------------------------------------------------------------------------
def build_pages():
    # Home
    emit("/", pages_home.build(), 1.0, "weekly",
         title="Content.Media — The Creator Economy Operating System",
         desc="Free calculators, benchmarks and a curated tool directory.",
         keywords="home creator economy rpm benchmarks")

    # Tools
    emit("/tools/", pages_tools.build_hub(), 0.9, "weekly",
         title="Free creator economy calculators",
         desc="Ten free calculators. No sign-up, formulas published.",
         keywords="calculators tools free")
    for slug, t in pages_tools.TOOLS.items():
        emit(f"/tools/{slug}/", pages_tools.build_tool(slug), 0.9, "monthly",
             title=t["h1"], desc=t["desc"], keywords=f"calculator {slug.replace('-', ' ')}")

    # Benchmarks
    emit("/benchmarks/", pages_content.build_benchmarks(), 1.0, "weekly",
         title="2026 Creator Economy Benchmarks",
         desc="RPM by niche, engagement bands, rate anchors, display RPM, production costs.",
         keywords="benchmarks rpm cpm rates data engagement")

    # Directory
    emit("/directory/", pages_money.build_directory(), 0.9, "daily",
         title="Content & AI tool directory",
         desc="Tools filtered by category, pricing, modality and platform.",
         keywords="directory tools ai software")
    emit("/directory/submit/", pages_money.build_submit(), 0.7, "monthly",
         title="Submit a tool", desc="List your tool. Free, featured $79, sponsored $299/month.",
         keywords="submit listing directory")

    # Guides
    emit("/guides/", pages_content.build_guides_hub(), 0.9, "weekly",
         title="Guides", desc="Reference guides on monetisation, pricing, SEO and operations.",
         keywords="guides articles reference")
    for g in GUIDES:
        emit(f"/guides/{g['slug']}/", pages_content.build_guide(g), 0.8, "monthly",
             title=g["title"], desc=g["desc"], keywords=f"{g['cat']} guide {g['slug'].replace('-', ' ')}")

    # Video, jobs
    emit("/videos/", pages_content.build_videos(), 0.7, "weekly",
         title="Video library", desc="Benchmark and calculator explainers on video.",
         keywords="video youtube explainers")
    emit("/jobs/", pages_content.build_jobs(), 0.8, "daily",
         title="Creator economy jobs", desc="Content, video, newsletter and SEO roles.",
         keywords="jobs hiring careers")
    emit("/jobs/post/", pages_content.build_post_job(), 0.6, "monthly",
         title="Post a job", desc="Post a role from $149.", keywords="post job hiring")

    # Money surfaces
    emit("/services/", pages_money.build_services(), 1.0, "monthly",
         title="Content services — costed plan in one business day",
         desc="Content programmes built and run. Pricing published from $2,500/month.",
         keywords="services agency retainer content marketing")
    emit("/services/thank-you/", pages_money.build_services_thanks(), index=False)
    emit("/advertise/", pages_money.build_advertise(), 0.8, "monthly",
         title="Advertise & sponsor", desc="Media kit, formats and rates.",
         keywords="advertise sponsor media kit")
    emit("/support/", pages_money.build_support(), 0.8, "monthly",
         title="Support Content.Media", desc="Keep independent creator research free.",
         keywords="support donate membership")
    emit("/contests/", pages_money.build_contests(), 0.8, "weekly",
         title="The Q4 Creator Grant — $5,000", desc="Free to enter. No purchase necessary.",
         keywords="contest giveaway grant prize")
    emit("/contests/official-rules/", pages_money.build_rules(), 0.4, "yearly",
         title="Contest official rules", desc="Eligibility, entry, odds and winner selection.",
         keywords="rules contest legal")
    emit("/newsletter/", pages_money.build_newsletter(), 0.8, "monthly",
         title="The weekly brief", desc="Benchmark changes and payout shifts, every Tuesday.",
         keywords="newsletter email subscribe")
    emit("/newsletter/thank-you/", pages_money.build_newsletter_thanks(), index=False)

    # Trust / legal / utility
    emit("/about/", pages_legal.build_about(), 0.6, "monthly",
         title="About", desc="Who we are and how we make money.", keywords="about company")
    emit("/contact/", pages_legal.build_contact(), 0.7, "monthly",
         title="Contact", desc="Corrections, data requests, advertising and services.",
         keywords="contact email support")
    emit("/privacy/", pages_legal.build_privacy(), 0.3, "yearly",
         title="Privacy policy", desc="What we collect and your rights.", keywords="privacy gdpr ccpa")
    emit("/cookies/", pages_legal.build_cookies(), 0.3, "yearly",
         title="Cookie policy", desc="Which cookies we use and how to control them.", keywords="cookies consent")
    emit("/terms/", pages_legal.build_terms(), 0.3, "yearly",
         title="Terms of use", desc="Terms governing use of this site.", keywords="terms legal")
    emit("/disclosure/", pages_legal.build_disclosure(), 0.4, "yearly",
         title="Advertising & affiliate disclosure", desc="How we make money and what is not for sale.",
         keywords="disclosure affiliate advertising")
    emit("/editorial-policy/", pages_legal.build_editorial(), 0.4, "yearly",
         title="Editorial policy", desc="How we research and correct.", keywords="editorial policy corrections")
    emit("/dmca/", pages_legal.build_dmca(), 0.2, "yearly",
         title="DMCA & copyright", desc="Copyright notices and counter-notices.", keywords="dmca copyright")
    emit("/search/", pages_legal.build_search(), index=False)
    emit("/404.html", pages_legal.build_404(), index=False)


# ---------------------------------------------------------------------------
def write_assets():
    data_dir = os.path.join(ROOT, "assets", "data")
    img_dir = os.path.join(ROOT, "assets", "img")
    os.makedirs(data_dir, exist_ok=True)
    os.makedirs(img_dir, exist_ok=True)

    # Directory dataset
    with open(os.path.join(data_dir, "tools.json"), "w", encoding="utf-8") as f:
        json.dump(tooldata.to_json(), f, separators=(",", ":"), ensure_ascii=False)

    # Search index
    with open(os.path.join(data_dir, "search-index.json"), "w", encoding="utf-8") as f:
        json.dump(INDEX, f, separators=(",", ":"), ensure_ascii=False)

    # Favicon / OG image
    fav = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">'
           '<rect width="32" height="32" rx="9" fill="url(#g)"/>'
           '<path d="M12.5 10.2v11.6l9.4-5.8z" fill="#fff"/>'
           '<defs><linearGradient id="g" x1="0" y1="0" x2="32" y2="32">'
           '<stop stop-color="#4f46e5"/><stop offset="1" stop-color="#db2777"/>'
           '</linearGradient></defs></svg>')
    with open(os.path.join(img_dir, "favicon.svg"), "w", encoding="utf-8") as f:
        f.write(fav)

    og = ('<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630">'
          '<defs><linearGradient id="bg" x1="0" y1="0" x2="1200" y2="630">'
          '<stop stop-color="#0c0e16"/><stop offset="1" stop-color="#2a1a4a"/></linearGradient>'
          '<linearGradient id="a" x1="0" y1="0" x2="1" y2="1">'
          '<stop stop-color="#7c74ff"/><stop offset="1" stop-color="#f472b6"/></linearGradient></defs>'
          '<rect width="1200" height="630" fill="url(#bg)"/>'
          '<circle cx="1010" cy="130" r="230" fill="url(#a)" opacity=".18"/>'
          '<rect x="80" y="150" width="86" height="86" rx="24" fill="url(#a)"/>'
          '<path d="M113 176v34l27-17z" fill="#fff"/>'
          '<text x="80" y="330" font-family="Inter,Arial,sans-serif" font-size="76" font-weight="800" '
          'fill="#fff">Content<tspan fill="#f472b6">.</tspan>Media</text>'
          '<text x="80" y="398" font-family="Inter,Arial,sans-serif" font-size="34" '
          'fill="#c6cbdd">The Creator Economy Operating System</text>'
          '<text x="80" y="500" font-family="Inter,Arial,sans-serif" font-size="26" '
          'fill="#99a0b8">Free calculators · Benchmark data · 1,240+ tools reviewed</text>'
          '</svg>')
    with open(os.path.join(img_dir, "og-default.svg"), "w", encoding="utf-8") as f:
        f.write(og)


def write_benchmark_csv():
    """A real, downloadable dataset — the newsletter incentive has to exist."""
    import csv
    rows = [("section", "item", "low", "high", "unit", "notes")]
    for n, lo, hi, cl, ch in pages_content.RPM_ROWS:
        name = n.replace("&amp;", "&")
        rows.append(("youtube_rpm_by_niche", name, lo, hi, "USD per 1000 monetised views",
                     f"advertiser CPM {cl}-{ch}"))
    for k, label, mult in [("us", "Mostly United States", 1.00),
                           ("tier1", "Mixed tier-1 (US/UK/CA/AU)", 0.86),
                           ("europe", "Mostly Western Europe", 0.72),
                           ("mixed", "Global mix", 0.48),
                           ("tier3", "Mostly South Asia / SEA / LATAM", 0.22)]:
        rows.append(("geography_multiplier", label, mult, mult, "multiplier", ""))
    for label, lo, hi in [("Instagram nano <1K", 6.5, 8.5), ("Instagram 1K-5K", 4.8, 6.4),
                          ("Instagram 5K-10K", 3.4, 4.6), ("Instagram 10K-100K", 2.0, 3.2),
                          ("Instagram 100K-1M", 1.4, 2.2), ("Instagram 1M+", 1.0, 1.7),
                          ("TikTok <5K", 12.0, 18.0), ("TikTok 5K-10K", 10.5, 15.0),
                          ("TikTok 10K-50K", 9.0, 13.5), ("TikTok 50K-100K", 8.0, 12.0),
                          ("TikTok 100K-1M", 7.0, 11.0), ("TikTok 1M+", 6.0, 10.5)]:
        rows.append(("engagement_rate_band", label, lo, hi, "percent", ""))
    for label, lo, hi in [("Instagram Reel", 12, 30), ("Instagram in-feed post", 8, 20),
                          ("Instagram Story frame", 4, 10), ("TikTok video", 10, 26),
                          ("YouTube integration", 18, 55), ("YouTube dedicated video", 30, 90),
                          ("YouTube Short", 8, 22), ("X post", 3, 10), ("LinkedIn post", 15, 45),
                          ("Newsletter primary slot", 25, 90), ("Podcast mid-roll", 18, 50)]:
        rows.append(("sponsorship_rate_anchor", label, lo, hi, "USD per 1000 followers", ""))
    for label, lo, hi in [("Finance & insurance", 28, 60), ("B2B software / SaaS", 26, 62),
                          ("Technology", 20, 44), ("Marketing & business", 18, 42),
                          ("Health", 14, 34), ("Education", 9, 20),
                          ("General / lifestyle", 5, 12), ("Entertainment", 3, 9)]:
        rows.append(("display_page_rpm", label, lo, hi, "USD per 1000 pageviews", "tier-1 traffic"))
    for label, lo, hi in [("SEO article 1500 words", 350, 1200), ("Pillar page 4000 words", 1200, 4500),
                          ("Short-form video", 150, 700), ("Long-form YouTube video", 1500, 9000),
                          ("Podcast episode edited", 400, 1800), ("Monthly retainer 12-20 pieces", 5000, 30000)]:
        rows.append(("production_cost", label, lo, hi, "USD", ""))
    for label, v in [("Organic CTR positions 1-3", 24), ("Organic CTR positions 4-10", 6),
                     ("Visitor to lead with offer", 2.2), ("Visitor to lead no offer", 0.5),
                     ("Lead to customer B2B", 14)]:
        rows.append(("funnel_constant", label, v, v, "percent", ""))

    path = os.path.join(ROOT, "assets", "data", "creator-benchmarks-2026.csv")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        csv.writer(f, lineterminator="\n").writerows(rows)
    return len(rows) - 1


def write_meta():
    today = date.today().isoformat()

    urls = "".join(
        f"<url><loc>{SITE['base_url']}{p}</loc><lastmod>{today}</lastmod>"
        f"<changefreq>{freq}</changefreq><priority>{pri}</priority></url>"
        for p, pri, freq in sorted(SITEMAP, key=lambda x: -x[1]))
    sitemap = ('<?xml version="1.0" encoding="UTF-8"?>'
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
               f'{urls}</urlset>')
    open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write(sitemap)

    robots = (f"User-agent: *\nAllow: /\n\n"
              f"Disallow: /services/thank-you/\n"
              f"Disallow: /newsletter/thank-you/\n"
              f"Disallow: /search/\n\n"
              f"Sitemap: {SITE['base_url']}/sitemap.xml\n")
    open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8").write(robots)

    open(os.path.join(ROOT, "ads.txt"), "w", encoding="utf-8").write(ADS["ads_txt"] + "\n")

    items = "".join(
        f"<item><title>{g['title']}</title>"
        f"<link>{SITE['base_url']}/guides/{g['slug']}/</link>"
        f"<guid>{SITE['base_url']}/guides/{g['slug']}/</guid>"
        f"<description><![CDATA[{g['desc']}]]></description></item>" for g in GUIDES)
    feed = ('<?xml version="1.0" encoding="UTF-8"?>'
            '<rss version="2.0"><channel>'
            f"<title>{SITE['name']}</title><link>{SITE['base_url']}</link>"
            f"<description>{SITE['description']}</description>"
            f"<language>en-us</language>{items}</channel></rss>")
    open(os.path.join(ROOT, "feed.xml"), "w", encoding="utf-8").write(feed)

    # GitHub Pages: in --static mode skip Jekyll; in the default (Jekyll) mode
    # Pages assembles the shared layout itself.
    nj = os.path.join(ROOT, ".nojekyll")
    if "--static" in sys.argv:
        open(nj, "w").write("")
    elif os.path.exists(nj):
        os.remove(nj)
    from config import CUSTOM_DOMAIN
    cname = os.path.join(ROOT, "CNAME")
    if CUSTOM_DOMAIN:
        open(cname, "w").write(SITE["domain"] + "\n")
    elif os.path.exists(cname):
        os.remove(cname)

    os.makedirs(os.path.join(ROOT, ".github"), exist_ok=True)
    funding = f"github: [{DONATE['github_sponsors']}]\n"
    if DONATE["kofi"]:
        funding += f"ko_fi: {DONATE['kofi']}\n"
    if DONATE["buymeacoffee"]:
        funding += f"buy_me_a_coffee: {DONATE['buymeacoffee']}\n"
    open(os.path.join(ROOT, ".github", "FUNDING.yml"), "w", encoding="utf-8").write(funding)


def verify_no_exposed_address():
    """Decode the masked contact token in memory and scan every file in the
    repository for it. The address is never written down, even here."""
    import base64
    from config import CONTACT_TOKEN, CONTACT_KEY
    needle = bytes(b ^ CONTACT_KEY for b in base64.b64decode(CONTACT_TOKEN)).lower()
    hits = []
    for d, dirs, files in os.walk(ROOT):
        dirs[:] = [x for x in dirs if x not in (".git", "node_modules", "__pycache__")]
        for f in files:
            fp = os.path.join(d, f)
            try:
                if needle in open(fp, "rb").read().lower():
                    hits.append(os.path.relpath(fp, ROOT))
            except OSError:
                pass
    if hits:
        raise SystemExit("BUILD FAILED — contact address exposed in: " + ", ".join(hits))
    print("Address scan: clean (0 files expose the contact address)")


def write_jekyll_layout():
    """Render the shell once with marker tokens, then swap in Liquid."""
    import layout, re
    from config import BASEURL
    layout.JEKYLL["on"] = False
    shell = layout.page("@@TITLE@@", "@@DESC@@", "@@CANON@@", "@@BODY@@",
                        extra_head="@@HEAD@@",
                        extra_body='<script src="/assets/js/benchmarks.js" defer></script>'
                                   '<script src="/assets/js/calc.js" defer></script>'
                                   '<script src="/assets/js/directory.js" defer></script>@@FOOT@@')
    layout.JEKYLL["on"] = True
    shell = minify(shell)
    shell = re.sub(r'(href|src)="/(?!/)', r'\1="{{ site.baseurl }}/', shell)
    shell = shell.replace('base: ""', 'base: "{{ site.baseurl }}"')
    for a, b in [("@@TITLE@@", "{{ page.title }}"), ("@@DESC@@", "{{ page.description }}"),
                 ("@@CANON@@", "{{ page.canonical }}"), ("@@BODY@@", "{{ content }}"),
                 ("@@HEAD@@", "{{ page.head_extra }}"), ("@@FOOT@@", "{{ page.body_extra }}")]:
        assert a in shell, a
        shell = shell.replace(a, b)
    os.makedirs(os.path.join(ROOT, "_layouts"), exist_ok=True)
    open(os.path.join(ROOT, "_layouts", "default.html"), "w", encoding="utf-8").write(shell)
    cfg = ("# GitHub Pages builds this site with Jekyll automatically.\n"
           "# Every page shares _layouts/default.html (header, footer, domain bar).\n"
           "title: Content.Media\n"
           "url: \"https://content.media\"\n"
           f"baseurl: \"{BASEURL}\"   # set to \"\" once content.media points at GitHub Pages\n"
           "exclude: [README.md, BUILD-PLAN.md, build.py, _src, node_modules, package.json, package-lock.json]\n")
    open(os.path.join(ROOT, "_config.yml"), "w", encoding="utf-8").write(cfg)


def main():
    import layout
    static = "--static" in sys.argv
    layout.JEKYLL["on"] = not static
    build_pages()
    n = write_all()
    write_assets()
    n_rows = write_benchmark_csv()
    write_meta()
    assert len(pages_tools.TOOLS) == __import__("config").CALCULATORS, \
        "CALCULATORS in config.py does not match the number of calculator pages"
    print(f"Benchmark CSV rows: {n_rows}")
    if not static:
        write_jekyll_layout()
    verify_no_exposed_address()
    print(f"Built {n} pages, {len(tooldata.TOOLS)} directory listings, "
          f"{len(GUIDES)} guides, {len(pages_tools.TOOLS)} calculators.")
    print(f"Sitemap entries: {len(SITEMAP)} | Search index records: {len(INDEX)}")


if __name__ == "__main__":
    main()
