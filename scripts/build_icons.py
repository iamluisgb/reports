#!/usr/bin/env python3
"""App icons for the installed web app (PWA).

Writes ``assets/icons/``: the manifest icons (192, 512), a maskable 512 for
Android's shaped masks, the 180 iOS home-screen icon and a small favicon. The
design is the site's own: the moss green italic serif on the near-black
background, i.e. the ``h1 em`` accent the titles use.

Idempotent: each PNG carries a fingerprint of the design that drew it in its
metadata, so a re-run only redraws when the design or the fonts change. Same
pattern as the Open Graph cards in ``build_social.py``.

    python3 scripts/build_icons.py
"""

from __future__ import annotations

import hashlib
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from PIL.PngImagePlugin import PngInfo

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "assets" / "icons"
SERIF_ITALIC = ROOT / "assets" / "fonts" / "DMSerifDisplay-Italic.ttf"

# Dark "Musgo" tokens (styles.css). Bump ICON_DESIGN when they change so every
# icon is redrawn.
ICON_DESIGN = "musgo-1"
BG = (12, 15, 14)          # --bg            #0c0f0e
GREEN = (143, 191, 154)    # --primary       #8fbf9a

MONOGRAM = "AI"
KEY = "icon-fingerprint"


def _font(size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(SERIF_ITALIC), size)


def _draw(size: int, *, radius: float = 0.0, scale: float = 0.56) -> Image.Image:
    """The icon at ``size`` px. ``radius`` rounds the tile (share previews), and
    ``scale`` is the monogram's cap height as a fraction of the tile.

    Maskable icons keep the monogram inside the central 80% circle, so they pass
    ``scale`` a little smaller and never round the tile: the launcher shapes it.
    """
    img = Image.new("RGB", (size, size), BG)
    d = ImageDraw.Draw(img)

    if radius > 0:
        # Redraw onto a rounded mask: the tile edge shows the background of
        # whatever draws it, which is what a rounded launcher icon needs.
        mask = Image.new("L", (size, size), 0)
        ImageDraw.Draw(mask).rounded_rectangle([0, 0, size - 1, size - 1],
                                              radius=int(size * radius), fill=255)
        img = Image.composite(img, Image.new("RGB", (size, size), (0, 0, 0)), mask)

    font = _font(int(size * scale))
    # Draw on an oversized scratch tile, then paste centred by its ink box: the
    # italic's bearings are asymmetric, so measuring text is more reliable than
    # placing it by the nominal anchor.
    scratch = Image.new("L", (size * 2, size * 2), 0)
    sd = ImageDraw.Draw(scratch)
    sd.text((size, size), MONOGRAM, font=font, fill=255)
    box = scratch.getbbox()
    if box:
        ink = scratch.crop(box)
        img.paste(GREEN, ((size - ink.width) // 2, (size - ink.height) // 2), ink)
    return img


def _fingerprint(size: int, radius: float, scale: float) -> str:
    text = "\x1f".join([ICON_DESIGN, str(size), f"{radius:.3f}", f"{scale:.3f}", MONOGRAM])
    return hashlib.sha256(text.encode()).hexdigest()[:16]


# name -> (px, radius, monogram scale)
ICONS = {
    "icon-192.png":            (192, 0.22, 0.60),
    "icon-512.png":            (512, 0.22, 0.60),
    "icon-maskable-512.png":   (512, 0.00, 0.42),
    "apple-touch-icon.png":    (180, 0.00, 0.60),   # iOS applies its own rounding
    "favicon-32.png":          (32, 0.22, 0.66),
}


def is_current(path: Path, fingerprint: str) -> bool:
    if not path.exists():
        return False
    try:
        with Image.open(path) as img:
            return img.text.get(KEY) == fingerprint
    except OSError:
        return False


def write(name: str, spec: tuple[int, float, float]) -> bool:
    size, radius, scale = spec
    out = OUT_DIR / name
    fp = _fingerprint(size, radius, scale)
    if is_current(out, fp):
        return False
    meta = PngInfo()
    meta.add_text(KEY, fp)
    out.parent.mkdir(parents=True, exist_ok=True)
    _draw(size, radius=radius, scale=scale).save(out, "PNG", pnginfo=meta, optimize=True)
    return True


def main() -> None:
    drawn = [name for name, spec in ICONS.items() if write(name, spec)]
    total = sum((OUT_DIR / n).stat().st_size for n in ICONS)
    print(f"icons: {len(drawn)} drawn ({', '.join(drawn) if drawn else 'all current'})"
          f" | {len(ICONS)} files, {total:,} bytes")


if __name__ == "__main__":
    main()
