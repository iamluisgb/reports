#!/usr/bin/env python3
"""Social/SEO build step: Open Graph images + meta tags for every report.

Two jobs, both idempotent so they converge to a no-op once applied:

1. **OG images** — a branded 1200x630 PNG per report under ``og/`` (plus a
   site-wide ``og/og-default.png`` fallback). These are what X/LinkedIn/
   WhatsApp/Slack show as the large card image when a link is shared.

2. **Meta tags** — injects ``<meta property="og:*">`` / ``twitter:card`` /
   ``description`` / ``canonical`` into each report's ``<head>``. Without these
   a shared link renders as a naked URL with no preview.

Metadata (title, date, summary, type) is derived by reusing ``build_entry``
from ``generate_manifest.py`` so there is a single source of truth.

Fonts are bundled under ``assets/fonts/`` (OFL) so rendering is identical
locally and in CI. If Pillow is missing the image step is skipped and meta
tags fall back to the default image — meta injection still runs.

Run from the repo root:  python3 scripts/build_social.py
"""

from __future__ import annotations

import hashlib
import html
import re
from datetime import datetime
from pathlib import Path

from generate_manifest import BASE_URL, REPORTS_DIR, ROOT, build_entry

OG_DIR = ROOT / "og"
FONTS_DIR = ROOT / "assets" / "fonts"
SERIF = FONTS_DIR / "DMSerifDisplay-Regular.ttf"
SANS = FONTS_DIR / "Inter-Regular.ttf"  # variable: weight axis 100-900

# Brand palette (matches styles.css dark theme).
# Dark "Musgo" tokens from styles.css. Bump CARD_DESIGN when they change so every card is redrawn.
CARD_DESIGN = "musgo-2"
BG = (12, 15, 14)          # --bg            #0c0f0e
CARD = (29, 35, 33)        # --bg-card-hover #1d2321 (hairline)
GREEN = (143, 191, 154)    # --primary       #8fbf9a
INK = (233, 238, 235)      # --on-surface    #e9eeeb
MUTED = (173, 183, 177)    # --on-surface-variant #adb7b1

W, H = 1200, 630
MARGIN = 80

OG_IMAGE_DEFAULT = f"{BASE_URL}/og/og-default.png"

# ----- meta injection ------------------------------------------------------

# Markers let us replace a previously-injected block instead of duplicating it.
META_START = "<!-- og:start -->"
META_END = "<!-- og:end -->"
BLOCK_RE = re.compile(re.escape(META_START) + r".*?" + re.escape(META_END), re.DOTALL)


def report_url(file: str) -> str:
    return f"{BASE_URL}/reports/{file}"


def og_image_url(file: str) -> str:
    png = OG_DIR / (Path(file).stem + ".png")
    return f"{BASE_URL}/og/{png.name}" if png.exists() else OG_IMAGE_DEFAULT


def pretty_date(date_str: str) -> str:
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").strftime("%-d %b %Y")
    except ValueError:
        return date_str


def social_title(entry: dict) -> str:
    if entry["type"] == "daily":
        return f"AI News Daily — {pretty_date(entry['date'])}"
    return entry["title"]


def social_description(entry: dict) -> str:
    desc = entry["summary"].strip()
    if desc:
        return desc
    return ("Daily AI news briefing — models, agents, security and AI engineering."
            if entry["type"] == "daily"
            else "In-depth AI analysis from Luis GB.")


def meta_block(entry: dict) -> str:
    url = report_url(entry["file"])
    title = html.escape(social_title(entry))
    desc = html.escape(social_description(entry))
    img = og_image_url(entry["file"])
    og_type = "website" if entry["type"] == "daily" else "article"
    return "\n".join([
        META_START,
        f'<meta name="description" content="{desc}">',
        f'<link rel="canonical" href="{url}">',
        f'<meta property="og:type" content="{og_type}">',
        '<meta property="og:site_name" content="AI Reports — Luis GB">',
        f'<meta property="og:title" content="{title}">',
        f'<meta property="og:description" content="{desc}">',
        f'<meta property="og:url" content="{url}">',
        f'<meta property="og:image" content="{img}">',
        '<meta property="og:image:width" content="1200">',
        '<meta property="og:image:height" content="630">',
        '<meta name="twitter:card" content="summary_large_image">',
        '<meta name="twitter:site" content="@iamluisgb">',
        '<meta name="twitter:creator" content="@iamluisgb">',
        f'<meta name="twitter:title" content="{title}">',
        f'<meta name="twitter:description" content="{desc}">',
        f'<meta name="twitter:image" content="{img}">',
        META_END,
    ])


def inject_meta(path: Path, entry: dict) -> bool:
    """Insert/replace the OG block right before </head>. Returns True if changed."""
    text = path.read_text(encoding="utf-8", errors="replace")
    block = meta_block(entry)

    if META_START in text:
        new = BLOCK_RE.sub(lambda _: block, text, count=1)
    else:
        if "</head>" not in text:
            return False
        new = text.replace("</head>", block + "\n</head>", 1)

    if new != text:
        path.write_text(new, encoding="utf-8")
        return True
    return False


# ----- Shared report UI -------------------------------------------------------
# Every report preloads the self-hosted fonts and loads site.js (theme, audio player) and report.js
# (top bar, reading progress, section index, prev/next). Injected here, like the
# meta block, so hand-written specials and older dailies get it without being edited.

UI_START = "<!-- ui:start -->"
UI_END = "<!-- ui:end -->"
UI_RE = re.compile(re.escape(UI_START) + r".*?" + re.escape(UI_END), re.S)
UI_BLOCK = "\n".join([
    UI_START,
    # Fonts are self-hosted (assets/fonts/web). Preload all four (81 KB): the italic is in
    # every title and the mono in every label, and swapping them late shifts the page.
    *[f'<link rel="preload" href="../assets/fonts/web/{f}" as="font" type="font/woff2" crossorigin>'
      for f in ("InstrumentSerif-normal.woff2", "InstrumentSerif-italic.woff2", "Geist-normal.woff2", "GeistMono-normal.woff2")],
    # Apply the reader's theme, or the system's, before first paint so the page never flashes.
    "<script>try{var t=localStorage.getItem('ai-reports-theme');if(t==='light'||(!t&&"
    "matchMedia('(prefers-color-scheme: light)').matches))document.documentElement.setAttribute('data-theme','light')}catch(e){}</script>",
    # Prerender a report or the index when the reader shows intent (hover, pointer down).
    '<script type="speculationrules">{"prerender":[{"where":{"or":[{"href_matches":"/reports/"},'
    '{"href_matches":"/reports/reports/*.html"},{"href_matches":"/reports/about.html"}]},"eagerness":"moderate"}]}</script>',
    # Umami (cloud), served through the domain root like the rest of luisgonzalezbernal.com.
    '<script defer src="/u/s.js" data-website-id="08c1619b-4bb8-471b-9dc9-9b6cda88e8ae" data-host-url="https://cloud.umami.is" data-domains="luisgonzalezbernal.com"></script>',
    '<script src="../site.js" defer></script>',
    '<script src="../report.js" defer></script>',
    UI_END,
])


def ui_block(path: Path) -> str:
    """The shared block plus this report's markdown twin (written by build_agent_files.py)."""
    alt = f'<link rel="alternate" type="text/markdown" href="{path.stem}.md">'
    return UI_BLOCK.replace(UI_START, UI_START + "\n" + alt, 1)


def inject_ui(path: Path) -> bool:
    """Insert/replace the UI block right before </head>. Returns True if changed."""
    text = path.read_text(encoding="utf-8", errors="replace")
    block = ui_block(path)
    if UI_START in text:
        new = UI_RE.sub(lambda _: block, text, count=1)
    elif "</head>" in text:
        new = text.replace("</head>", block + "\n</head>", 1)
    else:
        return False
    if new != text:
        path.write_text(new, encoding="utf-8")
        return True
    return False


# ----- OG image ------------------------------------------------------------

def _load_fonts():
    from PIL import ImageFont

    def sans(size: int, weight: int = 400):
        f = ImageFont.truetype(str(SANS), size)
        try:
            f.set_variation_by_axes([14, weight])  # [opsz, wght]
        except Exception:
            pass
        return f

    return {
        "serif": lambda s: ImageFont.truetype(str(SERIF), s),
        "sans": sans,
    }


def _wrap(draw, text, font, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = f"{cur} {w}".strip()
        if draw.textlength(trial, font=font) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def _fit_title(draw, text, fonts, max_w, max_lines, start=78, min_size=46):
    """Shrink the serif title until it wraps within max_lines."""
    size = start
    while size >= min_size:
        font = fonts["serif"](size)
        lines = _wrap(draw, text, font, max_w)
        if len(lines) <= max_lines:
            return font, lines, size
        size -= 4
    font = fonts["serif"](min_size)
    return font, _wrap(draw, text, font, max_w)[:max_lines], min_size


# A card is redrawn whenever the text it shows changes, not only when the PNG is
# missing: a rebuilt day used to keep its old card forever. The fingerprint of
# the drawn text lives in the PNG's own metadata, so there is no sidecar to sync.
OG_KEY = "og-fingerprint"


def card_fingerprint(entry: dict) -> str:
    text = "\x1f".join([CARD_DESIGN, entry["type"], entry["date"], entry["title"], social_description(entry)])
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def card_is_current(entry: dict, out: Path) -> bool:
    if not out.exists():
        return False
    from PIL import Image
    try:
        with Image.open(out) as img:
            return img.text.get(OG_KEY) == card_fingerprint(entry)
    except OSError:
        return False


def make_og_image(entry: dict, out: Path) -> None:
    from PIL import Image, ImageDraw
    from PIL.PngImagePlugin import PngInfo

    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    fonts = _load_fonts()

    # A soft top hairline. No side accent bar: the design system has none.
    d.line([MARGIN, 150, W - MARGIN, 150], fill=CARD, width=2)

    x = MARGIN
    # Category / kicker (green, uppercase, tracked).
    kicker = "AI NEWS DAILY" if entry["type"] == "daily" else "SPECIAL REPORT"
    kfont = fonts["sans"](26, weight=700)
    d.text((x, 84), " ".join(kicker), font=kfont, fill=GREEN)

    # Title.
    headline = pretty_date(entry["date"]) + " · AI Briefing" if entry["type"] == "daily" \
        else entry["title"]
    max_lines = 3 if entry["type"] == "special" else 1
    tfont, lines, tsize = _fit_title(d, headline, fonts, W - 2 * MARGIN, max_lines)
    y = 196
    for ln in lines:
        d.text((x, y), ln, font=tfont, fill=INK)
        y += int(tsize * 1.18)

    # Summary (muted, a couple of lines).
    summary = social_description(entry)
    sfont = fonts["sans"](30, weight=400)
    sy = max(y + 18, 430)
    for ln in _wrap(d, summary, sfont, W - 2 * MARGIN)[:2]:
        if sy + 42 > H - 96:   # keep clear of the footer line
            break
        d.text((x, sy), ln, font=sfont, fill=MUTED)
        sy += 42

    # Footer brand line.
    ffont = fonts["sans"](26, weight=600)
    d.text((x, H - 70), "luisgonzalezbernal.com/reports", font=ffont, fill=INK)
    handle = "@iamluisgb"
    hw = d.textlength(handle, font=ffont)
    d.text((W - MARGIN - hw, H - 70), handle, font=ffont, fill=MUTED)

    meta = PngInfo()
    meta.add_text(OG_KEY, card_fingerprint(entry))
    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out, "PNG", pnginfo=meta)


def make_default_image(out: Path) -> None:
    from PIL import Image, ImageDraw

    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    fonts = _load_fonts()
    kfont = fonts["sans"](28, weight=700)
    d.text((MARGIN, 180), " ".join("AI REPORTS"), font=kfont, fill=GREEN)
    tfont = fonts["serif"](96)
    d.text((MARGIN, 230), "AI Reports", font=tfont, fill=INK)
    sfont = fonts["sans"](34, weight=400)
    d.text((MARGIN, 360),
           "Daily news & in-depth analysis on AI", font=sfont, fill=MUTED)
    ffont = fonts["sans"](26, weight=600)
    d.text((MARGIN, H - 70), "luisgonzalezbernal.com/reports", font=ffont, fill=INK)
    handle = "@iamluisgb"
    hw = d.textlength(handle, font=ffont)
    d.text((W - MARGIN - hw, H - 70), handle, font=ffont, fill=MUTED)
    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out, "PNG")


# ----- main ----------------------------------------------------------------

def main() -> None:
    try:
        import PIL  # noqa: F401
        have_pillow = True
    except ImportError:
        have_pillow = False
        print("Pillow not available — skipping OG images (meta falls back to default).")

    entries = [build_entry(p) for p in sorted(REPORTS_DIR.glob("*.html"))]

    images = 0
    if have_pillow:
        OG_DIR.mkdir(exist_ok=True)
        default = OG_DIR / "og-default.png"
        if not default.exists():
            make_default_image(default)
        for entry in entries:
            out = OG_DIR / (Path(entry["file"]).stem + ".png")
            if not card_is_current(entry, out):
                make_og_image(entry, out)
                images += 1

    # Inject meta after images exist so og:image points at the real per-report PNG.
    changed = 0
    for entry in entries:
        if inject_meta(REPORTS_DIR / entry["file"], entry):
            changed += 1

    ui = sum(inject_ui(REPORTS_DIR / entry["file"]) for entry in entries)

    print(f"OG images generated: {images} (+ default) | reports meta updated: {changed}/{len(entries)}"
          f" | ui updated: {ui}")


if __name__ == "__main__":
    main()
