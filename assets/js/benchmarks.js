/* ===========================================================================
   Content.Media — published benchmark constants (2026 edition)
   Every calculator on this site reads from this file. Nothing is hidden:
   if you disagree with an assumption you can see it, cite it, or fork it.
   Ranges are low/high estimates for tier-1 (US/CA/UK/AU) audiences unless
   stated. Multiply by the geo factor for mixed-geography audiences.
   =========================================================================== */
window.CMB = {
  updated: 'September 2026',

  /* Long-form YouTube RPM (creator take-home per 1,000 monetised views,
     i.e. after YouTube's 45% share on in-stream ads). */
  niches: [
    { key: 'finance',    label: 'Personal finance & investing', rpmLo: 15.0, rpmHi: 38.0, cpmLo: 28, cpmHi: 70 },
    { key: 'saas',       label: 'B2B software & SaaS',          rpmLo: 14.0, rpmHi: 34.0, cpmLo: 26, cpmHi: 64 },
    { key: 'realestate', label: 'Real estate & mortgage',       rpmLo: 12.0, rpmHi: 45.0, cpmLo: 24, cpmHi: 84 },
    { key: 'marketing',  label: 'Marketing & business',         rpmLo: 10.0, rpmHi: 26.0, cpmLo: 20, cpmHi: 48 },
    { key: 'tech',       label: 'Technology & gadget reviews',  rpmLo:  8.0, rpmHi: 22.0, cpmLo: 16, cpmHi: 42 },
    { key: 'education',  label: 'Education & how-to',           rpmLo:  5.0, rpmHi: 14.0, cpmLo: 10, cpmHi: 26 },
    { key: 'health',     label: 'Health, fitness & wellness',   rpmLo:  4.0, rpmHi: 12.0, cpmLo:  8, cpmHi: 23 },
    { key: 'travel',     label: 'Travel',                       rpmLo:  4.0, rpmHi: 11.0, cpmLo:  8, cpmHi: 21 },
    { key: 'food',       label: 'Food & cooking',               rpmLo:  3.5, rpmHi:  9.0, cpmLo:  7, cpmHi: 17 },
    { key: 'beauty',     label: 'Beauty & fashion',             rpmLo:  3.5, rpmHi: 10.0, cpmLo:  7, cpmHi: 19 },
    { key: 'gaming',     label: 'Gaming',                       rpmLo:  1.2, rpmHi:  5.5, cpmLo:  3, cpmHi: 11 },
    { key: 'entertain',  label: 'Entertainment & vlogs',        rpmLo:  1.5, rpmHi:  6.0, cpmLo:  3, cpmHi: 12 },
    { key: 'music',      label: 'Music',                        rpmLo:  1.0, rpmHi:  3.5, cpmLo:  2, cpmHi:  7 },
    { key: 'kids',       label: 'Kids & family',                rpmLo:  1.0, rpmHi:  4.0, cpmLo:  2, cpmHi:  8 }
  ],

  /* Audience geography multiplier applied to RPM. */
  geo: [
    { key: 'us',     label: 'Mostly United States',        mult: 1.00 },
    { key: 'tier1',  label: 'Mixed tier-1 (US/UK/CA/AU)',  mult: 0.86 },
    { key: 'europe', label: 'Mostly Western Europe',       mult: 0.72 },
    { key: 'mixed',  label: 'Global mix',                  mult: 0.48 },
    { key: 'tier3',  label: 'Mostly South Asia / SEA / LATAM', mult: 0.22 }
  ],

  /* Share of views that actually serve a monetised ad impression. */
  monetisedShare: { lo: 0.55, hi: 0.78 },

  /* YouTube Shorts: paid from the creator pool, not classic in-stream ads. */
  shorts: { rpmLo: 0.03, rpmHi: 0.12, poolShare: 0.45 },

  /* Instagram engagement-rate bands by follower tier (likes+comments/followers). */
  igBands: [
    { max: 1000,     lo: 6.5, hi: 8.5,  tier: 'Nano (<1K)' },
    { max: 5000,     lo: 4.8, hi: 6.4,  tier: 'Nano (1K–5K)' },
    { max: 10000,    lo: 3.4, hi: 4.6,  tier: 'Micro (5K–10K)' },
    { max: 100000,   lo: 2.0, hi: 3.2,  tier: 'Micro (10K–100K)' },
    { max: 1000000,  lo: 1.4, hi: 2.2,  tier: 'Macro (100K–1M)' },
    { max: Infinity, lo: 1.0, hi: 1.7,  tier: 'Mega (1M+)' }
  ],

  /* TikTok engagement-rate bands (likes+comments+shares/followers). */
  ttBands: [
    { max: 5000,     lo: 12.0, hi: 18.0, tier: 'Nano (<5K)' },
    { max: 10000,    lo: 10.5, hi: 15.0, tier: 'Nano (5K–10K)' },
    { max: 50000,    lo:  9.0, hi: 13.5, tier: 'Micro (10K–50K)' },
    { max: 100000,   lo:  8.0, hi: 12.0, tier: 'Micro (50K–100K)' },
    { max: 1000000,  lo:  7.0, hi: 11.0, tier: 'Macro (100K–1M)' },
    { max: Infinity, lo:  6.0, hi: 10.5, tier: 'Mega (1M+)' }
  ],

  /* Sponsored-post rate anchors, US dollars per deliverable, per 1,000 followers.
     These are the "CPM-on-followers" figures brands actually negotiate against. */
  rateCard: {
    instagram_reel:   { lo: 12, hi: 30 },
    instagram_post:   { lo:  8, hi: 20 },
    instagram_story:  { lo:  4, hi: 10 },
    tiktok_video:     { lo: 10, hi: 26 },
    youtube_integration: { lo: 18, hi: 55 },
    youtube_dedicated:   { lo: 30, hi: 90 },
    youtube_short:    { lo:  8, hi: 22 },
    x_post:           { lo:  3, hi: 10 },
    linkedin_post:    { lo: 15, hi: 45 },
    newsletter_slot:  { lo: 25, hi: 90 },
    podcast_midroll:  { lo: 18, hi: 50 }
  },

  /* Multipliers applied to rate-card base. */
  rateMods: {
    niche:  { generic: 1.0, b2b: 1.55, finance: 1.6, tech: 1.3, beauty: 1.1, gaming: 0.85, entertainment: 0.8 },
    usage:  { organic: 1.0, whitelist_30d: 1.35, whitelist_90d: 1.6, perpetual: 2.1 },
    exclusivity: { none: 1.0, cat_30d: 1.2, cat_90d: 1.4, cat_1y: 1.8 }
  },

  /* Podcast advertising, US dollars CPM on downloads. */
  podcast: {
    preroll:  { lo: 15, hi: 25 },
    midroll:  { lo: 22, hi: 40 },
    postroll: { lo: 10, hi: 18 },
    host_read_premium: 1.35
  },

  /* Newsletter sponsorship, US dollars CPM on opens (not sends). */
  newsletter: {
    classified:  { lo:  8, hi: 18 },
    primary:     { lo: 25, hi: 60 },
    dedicated:   { lo: 45, hi: 120 },
    b2bPremium:  1.8,
    openRateDefault: 0.42
  },

  /* Display advertising page RPM by content category, tier-1 traffic. */
  displayRpm: [
    { label: 'Finance & insurance',    lo: 28, hi: 60 },
    { label: 'B2B software / SaaS',    lo: 26, hi: 62 },
    { label: 'Technology',             lo: 20, hi: 44 },
    { label: 'Marketing & business',   lo: 18, hi: 42 },
    { label: 'Health',                 lo: 14, hi: 34 },
    { label: 'Education',              lo:  9, hi: 20 },
    { label: 'General / lifestyle',    lo:  5, hi: 12 },
    { label: 'Entertainment',          lo:  3, hi:  9 }
  ],

  /* Content production cost anchors, US dollars per finished piece. */
  costs: [
    { label: 'SEO article, 1,500 words, expert-written', lo: 350,  hi: 1200 },
    { label: 'Pillar page / 4,000-word guide',           lo: 1200, hi: 4500 },
    { label: 'Short-form video (per Reel/Short)',        lo: 150,  hi: 700 },
    { label: 'Long-form YouTube video, scripted',        lo: 1500, hi: 9000 },
    { label: 'Podcast episode, edited + clips',          lo: 400,  hi: 1800 },
    { label: 'Full monthly retainer, 12–20 pieces',      lo: 5000, hi: 30000 }
  ],

  /* Search / funnel defaults used by the ROI calculator. */
  funnel: { ctrTop3: 0.24, ctr4to10: 0.06, visitorToLead: 0.022, leadToCustomer: 0.14 }
};
