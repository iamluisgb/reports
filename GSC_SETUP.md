# Google Search Console — Setup Instructions

## Steps (Luis, this is for you)

### 1. Verify domain
1. Go to https://search.google.com/search-console/
2. Click "Add property"
3. Enter: `luisgonzalezbernal.com` (Domain property — covers all subpaths)
4. Choose **HTML tag** verification method
5. Copy the `<meta name="google-site-verification" content="XXXXXX" />` tag
6. Send it to me and I'll inject it into `index.html`

### 2. Submit sitemap
Once verified:
1. Go to Sitemaps → Add sitemap
2. Enter: `https://luisgonzalezbernal.com/reports/sitemap.xml`
3. Submit

### 3. Request indexing for top pages
Go to URL Inspection → Enter each URL → Request Indexing:
- `https://luisgonzalezbernal.com/reports/`
- `https://luisgonzalezbernal.com/reports/reports/palantir-playbook-2026.html`
- `https://luisgonzalezbernal.com/reports/reports/arxiv-trends-2026-06-27.html`
- `https://luisgonzalezbernal.com/reports/reports/sre-2026-06-28.html`
- `https://luisgonzalezbernal.com/reports/reports/ai-model-architecture-2026-06-28.html`
- `https://luisgonzalezbernal.com/reports/reports/enterprise-ai-agent-security-2026-06-02.html`

## What I've prepared (done)
- ✅ JSON-LD `TechArticle` schema on all 10 special reports
- ✅ JSON-LD `WebSite` schema on index.html
- ✅ All 10 specials in RSS feed
- ✅ Sitemap with all 60+ URLs
- ✅ OG images for all reports
- ⏳ Waiting for your verification tag to inject
