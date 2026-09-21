# -*- coding: utf-8 -*-
"""Global configuration for the Content.Media static site generator."""

SITE = {
    "name": "Content.Media",
    "domain": "content.media",
    "base_url": "https://content.media",
    "tagline": "The Creator Economy Operating System",
    "description": (
        "Free calculators, benchmark data, and a curated directory of content and AI "
        "tools for creators, publishers and brands. Know what your content is worth."
    ),
    "founded": 2026,
    "locale": "en_US",
    "twitter": "@contentdotmedia",
    "youtube_channel": "https://www.youtube.com/@contentdotmedia",
    "owner_contact_url": "https://web.works/contact",
    # Where GitHub Pages serves the site. Project-site URL for now:
    #   https://webworksa1.github.io/content-media/
    # When content.media's DNS points at GitHub, set BASEURL = "" and
    # CUSTOM_DOMAIN = True, rebuild, push. (Or just edit baseurl in _config.yml
    # and add a CNAME file on GitHub — that is all the switch requires.)
}
BASEURL = "/content-media"
CUSTOM_DOMAIN = False

# ---------------------------------------------------------------------------
# Contact email is NEVER written to disk in plaintext.
# It is XOR-masked (key 0x5A) then base64-encoded, and reassembled in the
# browser at runtime by assets/js/site.js. Nothing in the HTML source, the
# sitemap, the JSON data files or the repository contains the address.
# ---------------------------------------------------------------------------
CONTACT_TOKEN = "LT84LTUoMSk7axo9NzszNnQ5NTc="
CONTACT_KEY = 90  # 0x5A

# FormSubmit.co AJAX gateway. The endpoint is assembled client-side from the
# masked token, so the destination address never appears in the markup.
# After the first submission is confirmed, swap FORM_ALIAS to the /el/<alias>
# string FormSubmit issues, which removes the address from the wire entirely.
FORM_GATEWAY = "https://formsubmit.co/ajax/"
FORM_ALIAS = ""  # e.g. "el/xxxxxxxx" -> https://formsubmit.co/ajax/el/xxxxxxxx

# ---------------------------------------------------------------------------
# Monetisation configuration. Replace the publisher / slot IDs once AdSense
# approves the domain; every ad unit on the site reads from here.
# ---------------------------------------------------------------------------
ADS = {
    "enabled": True,
    "publisher": "ca-pub-0000000000000000",
    "ads_txt": "google.com, pub-0000000000000000, DIRECT, f08c47fec0942fa0",
    "slots": {
        "leaderboard": "1000000001",
        "in_article": "1000000002",
        "sidebar": "1000000003",
        "footer": "1000000004",
        "tool_result": "1000000005",
    },
}

ANALYTICS = {
    "ga4_id": "",           # e.g. G-XXXXXXXXXX
    "plausible_domain": "",  # optional, privacy-first alternative
}

# Supporter counter is read by /support/. Keep it truthful — update it from the
# payment provider, never by hand-waving.
DONATE = {
    "buymeacoffee": "contentmedia",
    "kofi": "contentmedia",
    "paypal_button_id": "",          # hosted button id
    "stripe_monthly": "",            # https://buy.stripe.com/...
    "stripe_oneoff": "",
    "github_sponsors": "WEBWORKSA1",
    "opencollective": "",
    "goal_supporters": 3000,
    "current_supporters": 0,
}

# ---------------------------------------------------------------------------
# Navigation
# ---------------------------------------------------------------------------
NAV = [
    {"label": "Free Tools", "href": "/tools/", "children": [
        {"label": "All calculators", "href": "/tools/"},
        {"label": "YouTube money calculator", "href": "/tools/youtube-money-calculator/"},
        {"label": "YouTube Shorts RPM", "href": "/tools/youtube-shorts-rpm-calculator/"},
        {"label": "TikTok earnings", "href": "/tools/tiktok-earnings-calculator/"},
        {"label": "Instagram engagement", "href": "/tools/instagram-engagement-calculator/"},
        {"label": "Creator rate card", "href": "/tools/creator-rate-card-calculator/"},
        {"label": "CPM / RPM / CPC", "href": "/tools/cpm-rpm-cpc-calculator/"},
        {"label": "Podcast sponsorship", "href": "/tools/podcast-sponsorship-calculator/"},
        {"label": "Newsletter sponsorship", "href": "/tools/newsletter-sponsorship-calculator/"},
        {"label": "Content ROI", "href": "/tools/content-roi-calculator/"},
        {"label": "Channel growth forecast", "href": "/tools/channel-growth-forecaster/"},
    ]},
    {"label": "Benchmarks", "href": "/benchmarks/"},
    {"label": "Tool Directory", "href": "/directory/"},
    {"label": "Guides", "href": "/guides/"},
    {"label": "Video", "href": "/videos/"},
    {"label": "Jobs", "href": "/jobs/"},
    {"label": "Services", "href": "/services/", "cta": True},
]

FOOTER = [
    ("Free tools", [
        ("All calculators", "/tools/"),
        ("YouTube money calculator", "/tools/youtube-money-calculator/"),
        ("TikTok earnings calculator", "/tools/tiktok-earnings-calculator/"),
        ("Creator rate card builder", "/tools/creator-rate-card-calculator/"),
        ("Content ROI calculator", "/tools/content-roi-calculator/"),
        ("Search the site", "/search/"),
    ]),
    ("Research & data", [
        ("Creator Economy Benchmarks", "/benchmarks/"),
        ("RPM by niche", "/benchmarks/#rpm"),
        ("Engagement rate bands", "/benchmarks/#engagement"),
        ("Sponsorship rate index", "/benchmarks/#rates"),
        ("Guides library", "/guides/"),
        ("Video library", "/videos/"),
    ]),
    ("Work with us", [
        ("Content & media services", "/services/"),
        ("Advertise & sponsor", "/advertise/"),
        ("Submit a tool", "/directory/submit/"),
        ("Post a job", "/jobs/post/"),
        ("Support the site", "/support/"),
        ("Contests & prizes", "/contests/"),
    ]),
    ("Company", [
        ("About", "/about/"),
        ("Contact", "/contact/"),
        ("Editorial policy", "/editorial-policy/"),
        ("Privacy policy", "/privacy/"),
        ("Cookie policy", "/cookies/"),
        ("Terms of use", "/terms/"),
        ("Affiliate & ad disclosure", "/disclosure/"),
        ("DMCA", "/dmca/"),
    ]),
]

# ---------------------------------------------------------------------------
# Proof numbers. Anything here is rendered into public copy and into the media
# kit, so every value must be TRUE. Counts marked "auto" are computed from the
# real dataset at build time — do not hand-edit them.
# Set AUDIENCE values once you have real figures; until then the media kit
# says "available on request" rather than inventing a number.
# ---------------------------------------------------------------------------
import tools as _tools          # _src/data/tools.py — no back-imports, safe
import guides as _guides        # _src/guides.py    — no back-imports, safe

CALCULATORS = 10                # asserted against pages_tools.TOOLS at build time

PROOF = {
    "tools_indexed": f"{len(_tools.TOOLS)}",
    "calculators": str(CALCULATORS),
    "guides": f"{len(_guides.GUIDES)}",
    "niches": "14",
    "deliverables": "11",
    "tiers": "6",
    "geographies": "5",
    "subscribers": None,         # set once true; copy adapts automatically
}

AUDIENCE = {
    "subscribers": None,         # weekly brief subscribers
    "open_rate": None,           # e.g. "44%"
    "click_rate": None,          # e.g. "6.1%"
    "monthly_uniques": None,
    "split_roles": None,         # e.g. "38% creators / 24% publishers / 38% brand teams"
    "split_geo": None,           # e.g. "41% US / 29% UK+EU / 13% CA+AU / 17% other"
    "seniority": None,           # e.g. "52% founder, head of, director or above"
}


def metric(key, fallback="Current figure on request &mdash; updated monthly"):
    """Never print an invented audience number to an advertiser."""
    v = AUDIENCE.get(key)
    return v if v else f'<span class="muted">{fallback}</span>'


# Social-proof line for newsletter blocks. Falls back to a true statement
# when no subscriber count has been set.
if PROOF["subscribers"]:
    SUBS_LINE = f"Join {PROOF['subscribers']} creators, publishers and brand marketers."
    SUBS_SHORT = f"{PROOF['subscribers']} subscribers."
else:
    SUBS_LINE = ("Read by creators, publishers and brand marketers. "
                 "One email a week, unsubscribe in one click.")
    SUBS_SHORT = "One email a week. Unsubscribe in one click."
