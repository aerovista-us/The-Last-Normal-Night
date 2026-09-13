from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageFilter, ImageEnhance
from io import BytesIO
from urllib.request import urlopen
import hashlib
import math

ISSUE = Path(__file__).resolve().parents[1]
PAGES = ISSUE / "pages"
ARTIFACTS = ISSUE / "production" / "artifacts"
ARTIFACTS.mkdir(parents=True, exist_ok=True)
W, H = 2063, 3150
SW, SH = 4050, 3150
OVERLAP = 76
ART_H = 3040
MOONLIT = ISSUE / "2026-09-10__19-30-37__Moonlit-Lakeside-Town-Reflections__file_00000000a43c8230a403848b7670b888.png"
RAINY = ISSUE / "2026-09-10__21-02-04__Rainy-Lakeside-Nightfall__file_00000000e1ec81fda0870c76f82c5096.png"
P16_BASELINE = "93aefd4583cb4b6be774cc21a36d029f1658f431"
RAW16 = f"https://raw.githubusercontent.com/aerovista-us/The-Last-Normal-Night/{P16_BASELINE}/comic/issues/01-the-last-normal-night/pages/p16.png"
FONT_R = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf"


def fit(im, size, centering=(0.5, 0.5)):
    return ImageOps.fit(im.convert("RGB"), size, method=Image.Resampling.LANCZOS, centering=centering)


def feather_mask(size, feather=80):
    mask = Image.new("L", size, 255)
    d = ImageDraw.Draw(mask)
    for i in range(feather):
        v = int(255 * i / max(1, feather-1))
        d.rectangle((i, i, size[0]-i-1, size[1]-i-1), outline=v)
    return mask.filter(ImageFilter.GaussianBlur(feather / 2))


def caption(draw, x, y, text, width=430, fs=34):
    font = ImageFont.truetype(FONT_R, fs)
    box = draw.textbbox((0,0), text, font=font)
    tw, th = box[2]-box[0], box[3]-box[1]
    w = max(width, tw + 40)
    h = th + 32
    draw.rectangle((x, y, x+w, y+h), fill="#f3ead0", outline="#111", width=4)
    draw.text((x+18, y+12), text, font=font, fill="#111")


# ---- P14-P15 continuous rupture spread ----
moonlit = Image.open(MOONLIT).convert("RGB")
rainy = Image.open(RAINY).convert("RGB")
base = fit(moonlit, (SW, ART_H), centering=(0.5, 0.55))
spread = Image.new("RGB", (SW, SH), "white")
spread.paste(base, (0, 0))

# Keep the hero/truck grounded in the same recognizable CDA geometry.
# Source panel 3 is the canonical worn Ford on wet downtown pavement.
truck = rainy.crop((0, 650, rainy.width, min(965, rainy.height)))
truck = fit(truck, (1700, 980), centering=(0.30, 0.53))
truck = ImageEnhance.Brightness(truck).enhance(0.93)
spread.paste(truck, (0, ART_H-1020), feather_mask(truck.size, 90))

# Reality misregistration: copies shift by inches/pixels rather than destroying the city.
rgba = spread.convert("RGBA")
band = spread.crop((1100, 1150, 3900, 2800)).convert("RGBA")
band.putalpha(70)
rgba.alpha_composite(band, (1160, 1170))
sky = spread.crop((850, 220, 3550, 1120)).convert("RGBA")
sky.putalpha(50)
rgba.alpha_composite(sky, (810, 235))
moon = spread.crop((2750, 180, 3300, 700)).convert("RGBA")
moon.putalpha(70)
rgba.alpha_composite(moon, (2850, 215))
spread = rgba.convert("RGB")

# Three cold-white pressure faults, one off the center fold. No rubble, crater, or exploding buildings.
ov = Image.new("RGBA", (SW, SH), (0,0,0,0))
d = ImageDraw.Draw(ov)
for base_x, alpha in ((1935,155), (2285,120), (2460,90)):
    left, right = [], []
    for y in range(0, ART_H+1, 35):
        wob = math.sin(y/130.0)*26 + math.sin(y/47.0)*8
        width = 7 + 3*math.sin(y/80.0)
        left.append((base_x+wob-width, y))
        right.append((base_x+wob+width, y))
    d.polygon(left + right[::-1], fill=(210,238,255,alpha))
    center = [((a[0]+b[0])/2, a[1]) for a,b in zip(left,right)]
    d.line(center, fill=(245,250,255,min(220,alpha+60)), width=3)
# The wooden-flute pressure language traverses road/lake reflection as one continuous signal.
pts = []
for i in range(600):
    x = 300 + i*(3400/599)
    y = 2460 + math.sin(i*0.18)*12 + math.sin(i*0.043)*24
    pts.append((x,y))
d.line(pts, fill=(215,240,255,110), width=8)
d.line(pts, fill=(255,255,255,150), width=2)
ov = ov.filter(ImageFilter.GaussianBlur(1.2))
spread = Image.alpha_composite(spread.convert("RGBA"), ov).convert("RGB")

# Subtle fold and print footer with page numbers.
d = ImageDraw.Draw(spread)
d.line((2025, 0, 2025, ART_H), fill=(255,255,255), width=2)
d.rectangle((0, ART_H, SW, SH), fill="white")
numfont = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)
for x, text in ((1015, "14"), (3035, "15")):
    bbox = d.textbbox((0,0), text, font=numfont)
    d.text((x-(bbox[2]-bbox[0])/2, ART_H+35), text, font=numfont, fill="#111")

spread_path = ARTIFACTS / "p14-p15-spread-master.png"
spread.save(spread_path, "PNG", optimize=True)
p14 = spread.crop((0, 0, W, H))
p15 = spread.crop((SW-W, 0, SW, H))  # 4050-2063=1987 => 76px overlap
assert p14.size == (W,H) and p15.size == (W,H)
p14.save(PAGES / "p14.png", "PNG", optimize=True)
p15.save(PAGES / "p15.png", "PNG", optimize=True)

# ---- P16 quiet aftermath ----
# Preserve the existing strong two-panel art from the immutable baseline and restore only canonical captions.
with urlopen(RAW16, timeout=90) as r:
    p16 = fit(Image.open(BytesIO(r.read())), (W,H))
d = ImageDraw.Draw(p16)
caption(d, 145, 125, "Opened my eyes.", width=420, fs=34)
caption(d, 1450, 2620, "Same damn street.", width=450, fs=34)
caption(d, 1615, 2740, "Almost.", width=300, fs=34)
p16.save(PAGES / "p16.png", "PNG", optimize=True)

# Promotion manifest: the spread is the authority for P14/P15 and P13 is intentionally untouched.
manifest = ARTIFACTS / "PROMOTION_2026-09-13.md"
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
manifest.write_text(
    "# EP1 Corrected Promotion — 2026-09-13\n\n"
    "Canonical corrected promotion through Page 16.\n\n"
    "- P08: stale phone time and inherited label artifacts removed.\n"
    "- P09: location slug only; erroneous clock removed.\n"
    "- P12: rebuilt as a clean three-panel reality-proximity page.\n"
    "- P13: intentionally preserved unchanged.\n"
    "- P14/P15: derived from one 4050×3150 continuous CDA spread master with 76 px overlap.\n"
    "- P16: preserved aftermath art with canonical captions restored.\n\n"
    f"Spread SHA-256: `{sha(spread_path)}`\n"
    f"P14 SHA-256: `{sha(PAGES/'p14.png')}`\n"
    f"P15 SHA-256: `{sha(PAGES/'p15.png')}`\n"
    f"P16 SHA-256: `{sha(PAGES/'p16.png')}`\n"
    f"P13 SHA-256 at promotion: `{sha(PAGES/'p13.png')}`\n",
    encoding="utf-8",
)

print("P14-P16 corrected promotion build complete")
