from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageFilter
from io import BytesIO
from urllib.request import urlopen

ISSUE = Path(__file__).resolve().parents[1]
PAGES = ISSUE / "pages"
W, H = 2063, 3150
WHITE = "#f4f2ec"
CREAM = "#f3ead0"
FONT_B = "/usr/share/fonts/truetype/dejavu/DejaVuSansCondensed-Bold.ttf"
FONT_R = "/usr/share/fonts/truetype/dejavu/DejaVuSansCondensed.ttf"
FONT_I = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf"
BASELINE = "17d51b11a37d5b31838228fcf2e1de3ab96ab439"
CLEAN_SOURCE = "93aefd4583cb4b6be774cc21a36d029f1658f431"
RAW = "https://raw.githubusercontent.com/aerovista-us/The-Last-Normal-Night/{ref}/comic/issues/01-the-last-normal-night/pages/p{n:02d}.png"


def F(path, size):
    return ImageFont.truetype(path, size)


def fit(im, size=(W, H), crop=None, centering=(0.5, 0.5)):
    if crop is not None:
        im = im.crop(crop)
    return ImageOps.fit(im.convert("RGB"), size, method=Image.Resampling.LANCZOS, centering=centering)


def immutable_page(n, ref=BASELINE):
    with urlopen(RAW.format(ref=ref, n=n), timeout=90) as r:
        return fit(Image.open(BytesIO(r.read())))


def bubble(draw, cx, cy, text, width=460, fs=34):
    ff = F(FONT_R, fs)
    words, lines, cur = text.split(), [], ""
    for word in words:
        test = (cur + " " + word).strip()
        if draw.textbbox((0, 0), test, font=ff)[2] <= width - 48:
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    lh = fs + 8
    height = 38 + lh * len(lines)
    x0, y0 = cx - width // 2, cy - height // 2
    draw.rounded_rectangle((x0, y0, x0 + width, y0 + height), radius=36, fill="white", outline="#111", width=5)
    yy = y0 + 17
    for line in lines:
        tw = draw.textbbox((0, 0), line, font=ff)[2]
        draw.text((cx - tw / 2, yy), line, font=ff, fill="#111")
        yy += lh


def caption(draw, x, y, text, width=520, fs=34):
    ff = F(FONT_I, fs)
    words, lines, cur = text.split(), [], ""
    for word in words:
        test = (cur + " " + word).strip()
        if draw.textbbox((0, 0), test, font=ff)[2] <= width - 34:
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    lh = fs + 8
    height = 28 + lh * len(lines)
    draw.rectangle((x, y, x + width, y + height), fill=CREAM, outline="#111", width=4)
    yy = y + 12
    for line in lines:
        draw.text((x + 16, yy), line, font=ff, fill="#111")
        yy += lh


def save(im, n):
    out = PAGES / f"p{n:02d}.png"
    im.convert("RGB").save(out, "PNG", optimize=True)
    print(f"wrote {out}")


# P07 — approved convenience-store candidate, untouched.
p07 = fit(Image.open(PAGES / "p07-candidate.png"))
save(p07, 7)

# P08 — approved candidate; clean inherited label fragments and remove inconsistent 10:47 readouts.
p08 = fit(Image.open(PAGES / "p08-candidate.png"))
d = ImageDraw.Draw(p08)
edge = "#0f0f0f"
cream = "#f4ebd1"
white = "#f4f5f2"
font_num = F(FONT_B, 54)
font_title = F(FONT_B, 44)
font_sub = F(FONT_R, 34)
# Replace the full lower label groups so no old text can bleed through.
d.rectangle((20, 1948, 155, 2115), fill="#05090d", outline=white, width=4)
d.text((42, 1991), "8.3", font=font_num, fill=white)
d.rectangle((165, 1948, 500, 2115), fill=cream, outline=edge, width=4)
d.text((190, 1972), "NO SERVICE.", font=font_title, fill=edge)
d.text((190, 2034), "NOT EVEN ONE BAR.", font=font_sub, fill=edge)
d.rectangle((1030, 1948, 1150, 2115), fill="#05090d", outline=white, width=4)
d.text((1046, 1991), "8.4", font=font_num, fill=white)
d.rectangle((1155, 1948, 1690, 2115), fill=cream, outline=edge, width=4)
d.text((1175, 1972), "WELCOME BACK.", font=font_title, fill=edge)
d.text((1175, 2034), "FOR LESS THAN A SECOND.", font=font_sub, fill=edge)
# Remove the stale 10:47 clock readouts; the story is already past the 11:58 -> 11:57 anomaly.
for box in [(245, 2168, 360, 2245), (1225, 2168, 1355, 2245)]:
    d.rounded_rectangle(box, radius=13, fill="#050f1b")
save(p08, 8)

# P09 — immutable source; remove the bad time slug and keep location only.
p09 = immutable_page(9)
ov = Image.new("RGBA", p09.size, (0, 0, 0, 0))
od = ImageDraw.Draw(ov)
od.rounded_rectangle((28, 22, 560, 245), radius=18, fill=(5, 12, 18, 225))
p09 = Image.alpha_composite(p09.convert("RGBA"), ov).convert("RGB")
d = ImageDraw.Draw(p09)
d.text((62, 58), "SHERMAN AVENUE", font=F(FONT_B, 33), fill=WHITE)
d.text((62, 106), "COEUR D’ALENE, IDAHO", font=F(FONT_R, 28), fill=WHITE)
save(p09, 9)

# P10 — immutable source + exact canonical reaction dialogue.
p10 = immutable_page(10)
d = ImageDraw.Draw(p10)
bubble(d, 1590, 2220, "Okay.", width=270, fs=36)
bubble(d, 1570, 2400, "That’s not funny.", width=470, fs=36)
save(p10, 10)

# P11 — immutable source; preserve native SFX art and add the missing canonical caption only.
p11 = immutable_page(11)
d = ImageDraw.Draw(p11)
caption(d, 1370, 2740, "Eleven fifty-nine.", width=520, fs=36)
save(p11, 11)

# P12 — clean 3-panel proximity page built from immutable art. No CLICK/Nope leftovers.
source12 = immutable_page(12, CLEAN_SOURCE)
source09 = immutable_page(9, CLEAN_SOURCE)
p12 = Image.new("RGB", (W, H), "#050a0f")
# Preserve source header/footer.
p12.paste(source12.crop((0, 0, W, 175)), (0, 0))
p12.paste(source12.crop((0, 3065, W, H)), (0, 3065))

# 12.1: recognizable truck/intersection/lake. Crop before the old 12.2 begins.
p1 = (20, 175, 2043, 1330)
art1 = source12.crop((20, 175, 2043, 1068))
art1 = fit(art1, (p1[2]-p1[0], p1[3]-p1[1]), centering=(0.5, 0.55))
p12.paste(art1, (p1[0], p1[1]))
d = ImageDraw.Draw(p12)
d.rectangle(p1, outline=white, width=7)
d.rectangle((20, 175, 515, 345), fill=cream, outline=edge, width=4)
d.text((38, 205), "12.1", font=F(FONT_B, 40), fill=edge)
d.text((145, 205), "ONE POINT.", font=F(FONT_B, 42), fill=edge)

# 12.2: protagonist by the truck; shadow pulls sideways toward the lake, inconsistent with the lamps.
p2 = (20, 1344, 2043, 1840)
art2 = source09.crop((0, 2540, 2063, 3060))
art2 = fit(art2, (p2[2]-p2[0], p2[3]-p2[1]), centering=(0.5, 0.52))
p12.paste(art2, (p2[0], p2[1]))
d = ImageDraw.Draw(p12)
d.rectangle(p2, outline=white, width=7)
d.rectangle((40, 1362, 600, 1467), fill=cream, outline=edge, width=4)
d.text((57, 1381), "12.2", font=F(FONT_B, 40), fill=edge)
d.text((170, 1381), "WRONG SHADOW.", font=F(FONT_B, 42), fill=edge)
shadow = Image.new("RGBA", p12.size, (0, 0, 0, 0))
sd = ImageDraw.Draw(shadow)
sd.polygon([(590,1776),(720,1770),(1770,1635),(1910,1685),(1800,1740),(715,1830)], fill=(0,0,0,150))
shadow = shadow.filter(ImageFilter.GaussianBlur(14))
p12 = Image.alpha_composite(p12.convert("RGBA"), shadow).convert("RGB")

# 12.3: preserve the clean growl/waveform panel from the immutable source.
p3 = (20, 1854, 2043, 3065)
art3 = source12.crop((20, 1848, 2043, 3065))
art3 = fit(art3, (p3[2]-p3[0], p3[3]-p3[1]))
p12.paste(art3, (p3[0], p3[1]))
ImageDraw.Draw(p12).rectangle(p3, outline=white, width=7)
save(p12, 12)

print("P07-P12 clean correction build complete")
