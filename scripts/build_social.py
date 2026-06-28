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
BG = (13, 17, 23)          # --bg            #0d1117
CARD = (22, 27, 34)        # --bg-card       #161b22
GREEN = (63, 185, 80)      # --primary       #3fb950
INK = (230, 237, 243)      # --on-surface    #e6edf3
MUTED = (177, 186, 196)    # --on-surface-variant #b1bac4

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


def make_og_image(entry: dict, out: Path) -> None:
    from PIL import Image, ImageDraw

    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    fonts = _load_fonts()

    # Accent bar down the left edge + a soft top hairline.
    d.rectangle([0, 0, 12, H], fill=GREEN)
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
        d.text((x, sy), ln, font=sfont, fill=MUTED)
        sy += 42

    # Footer brand line.
    ffont = fonts["sans"](26, weight=600)
    d.text((x, H - 70), "luisgonzalezbernal.com/reports", font=ffont, fill=INK)
    handle = "@iamluisgb"
    hw = d.textlength(handle, font=ffont)
    d.text((W - MARGIN - hw, H - 70), handle, font=ffont, fill=MUTED)

    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out, "PNG")


def make_default_image(out: Path) -> None:
    from PIL import Image, ImageDraw

    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    fonts = _load_fonts()
    d.rectangle([0, 0, 12, H], fill=GREEN)
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
            if not out.exists():
                make_og_image(entry, out)
                images += 1

    # Inject meta after images exist so og:image points at the real per-report PNG.
    changed = 0
    for entry in entries:
        if inject_meta(REPORTS_DIR / entry["file"], entry):
            changed += 1

    print(f"OG images generated: {images} (+ default) | reports meta updated: {changed}/{len(entries)}")


if __name__ == "__main__":
    main()
