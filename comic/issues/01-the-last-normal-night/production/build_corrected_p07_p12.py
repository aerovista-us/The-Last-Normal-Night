from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageFilter
from io import BytesIO
from urllib.request import urlopen
import math

ISSUE = Path(__file__).resolve().parents[1]
PAGES = ISSUE / "pages"
W, H = 2063, 3150
WHITE = "#f4f2ec"
CREAM = "#f3ead0"
FONT_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_R = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_I = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf"
BASELINE = "17d51b11a37d5b31838228fcf2e1de3ab96ab439"
RAW = f"https://raw.githubusercontent.com/aerovista-us/The-Last-Normal-Night/{BASELINE}/comic/issues/01-the-last-normal-night/pages"


def F(path, size):
    return ImageFont.truetype(path, size)


def fit(im, size=(W, H), crop=None, centering=(0.5, 0.5)):
    if crop is not None:
        im = im.crop(crop)
    return ImageOps.fit(im.convert("RGB"), size, method=Image.Resampling.LANCZOS, centering=centering)


def baseline_page(n):
    with urlopen(f"{RAW}/p{n:02d}.png", timeout=60) as r:
        return fit(Image.open(BytesIO(r.read())))


def local_image(name):
    return Image.open(ISSUE / name).convert("RGB")


def bubble(draw, cx, cy, text, width=460, fs=34):
    font = F(FONT_R, fs)
    words = text.split()
    lines, cur = [], ""
    for word in words:
        test = (cur + " " + word).strip()
        if draw.textbbox((0, 0), test, font=font)[2] <= width - 48:
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
        tw = draw.textbbox((0, 0), line, font=font)[2]
        draw.text((cx - tw / 2, yy), line, font=font, fill="#111")
        yy += lh


def caption(draw, x, y, text, width=520, fs=34):
    font = F(FONT_I, fs)
    words = text.split()
    lines, cur = [], ""
    for word in words:
        test = (cur + " " + word).strip()
        if draw.textbbox((0, 0), test, font=font)[2] <= width - 34:
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
        draw.text((x + 16, yy), line, font=font, fill="#111")
        yy += lh


def sfx(draw, xy, text, fs=58, fill=WHITE):
    draw.text(xy, text, font=F(FONT_B, fs), fill=fill, stroke_width=3, stroke_fill="#111")


def alpha_round(im, box, fill=(4, 10, 15, 190), radius=28):
    overlay = Image.new("RGBA", im.size, (0,0,0,0))
    od = ImageDraw.Draw(overlay)
    od.rounded_rectangle(box, radius=radius, fill=fill)
    return Image.alpha_composite(im.convert("RGBA"), overlay).convert("RGB")


def feather_paste(base, insert, xy, feather=28):
    insert = insert.convert("RGB")
    mask = Image.new("L", insert.size, 255)
    # feather edge inward
    for i in range(feather):
        val = int(255 * i / max(1, feather-1))
        ImageDraw.Draw(mask).rectangle((i, i, insert.width-i-1, insert.height-i-1), outline=val)
    mask = mask.filter(ImageFilter.GaussianBlur(feather/2))
    base.paste(insert, xy, mask)


def save(im, n):
    out = PAGES / f"p{n:02d}.png"
    im.convert("RGB").save(out, "PNG", optimize=True)
    print(f"wrote {out}")


# P07 — approved convenience-store candidate. Keep candidate art untouched.
p07 = fit(Image.open(PAGES / "p07-candidate.png"))
save(p07, 7)

# P08 — approved candidate; remove ONLY the two tiny 10:47 readouts inside phone screens.
p08 = fit(Image.open(PAGES / "p08-candidate.png"))
d = ImageDraw.Draw(p08)
# Coordinates target phone screen top-left, not panel headers.
for box in [(208, 2115, 335, 2172), (1230, 2115, 1357, 2172)]:
    d.rounded_rectangle(box, radius=13, fill="#07101a")
save(p08, 8)

# P09 — always start from immutable baseline. Replace bad time stamp with intentional location slug.
p09 = baseline_page(9)
p09 = alpha_round(p09, (28, 22, 560, 245), fill=(5, 12, 18, 225), radius=18)
d = ImageDraw.Draw(p09)
d.text((62, 58), "SHERMAN AVENUE", font=F(FONT_B, 33), fill="#f4f2ec")
d.text((62, 106), "COEUR D’ALENE, IDAHO", font=F(FONT_R, 28), fill="#f4f2ec")
# No clock time here.
save(p09, 9)

# P10 — immutable source + exact canonical dialogue.
p10 = baseline_page(10)
d = ImageDraw.Draw(p10)
bubble(d, 1590, 2220, "Okay.", width=270, fs=36)
bubble(d, 1570, 2400, "That’s not funny.", width=470, fs=36)
save(p10, 10)

# P11 — immutable source. Preserve its attractive native SFX art; add only missing canonical caption.
p11 = baseline_page(11)
d = ImageDraw.Draw(p11)
caption(d, 1370, 2740, "Eleven fifty-nine.", width=520, fs=36)
save(p11, 11)

# P12 — canonical 3-panel proximity page assembled only from clean immutable/source art.
base_env = fit(local_image("2026-09-10__19-30-37__Moonlit-Lakeside-Town-Reflections__file_00000000a43c8230a403848b7670b888.png"))
rainy = local_image("2026-09-10__21-02-04__Rainy-Lakeside-Nightfall__file_00000000e1ec81fda0870c76f82c5096.png")
old09 = baseline_page(9)
old10 = baseline_page(10)
old11 = baseline_page(11)

p12 = Image.new("RGB", (W, H), WHITE)
d = ImageDraw.Draw(p12)
margin, gap = 20, 14
p1 = (margin, margin, W-margin, 1330)
p2 = (margin, p1[3]+gap, W-margin, 1835)
p3 = (margin, p2[3]+gap, W-margin, H-76)

# 12.1 — empty lake-end street, subtle optical compression; real Ford crop blended into foreground.
street = fit(base_env, (p1[2]-p1[0], p1[3]-p1[1]), crop=(190, 620, 1870, 2680), centering=(0.5,0.62))
street = street.resize((int(street.width*0.92), street.height), Image.Resampling.LANCZOS)
canvas = Image.new("RGB", (p1[2]-p1[0], p1[3]-p1[1]), "#050a0f")
canvas.paste(street, ((canvas.width-street.width)//2, 0))
# real hero Ford from source montage panel 3 (no generated geometric placeholder)
rw, rh = rainy.size
truck_crop = rainy.crop((int(rw*0.04), int(rh*0.445), int(rw*0.62), int(rh*0.635)))
truck_crop = fit(truck_crop, (920, 430), centering=(0.43,0.55))
feather_paste(canvas, truck_crop, ((canvas.width-920)//2, canvas.height-445), 34)
p12.paste(canvas, (p1[0],p1[1]))
d.rectangle(p1, outline="#111", width=7)
sfx(d, (66, 58), "12.1", 36)

# 12.2 — use a clean full-body street frame; add only the impossible shadow.
body = fit(old09, (p2[2]-p2[0], p2[3]-p2[1]), crop=(0, 2240, 2063, 3060), centering=(0.43,0.63))
p12.paste(body, (p2[0],p2[1]))
d.rectangle(p2, outline="#111", width=7)
# shadow deliberately cuts across expected lamp direction; translucent, not solid geometry.
ov = Image.new("RGBA", p12.size, (0,0,0,0)); od = ImageDraw.Draw(ov)
od.polygon([(850,p2[1]+255),(990,p2[1]+290),(1930,p2[3]-55),(1810,p2[3]-12)], fill=(0,0,0,145))
ov = ov.filter(ImageFilter.GaussianBlur(12)); p12 = Image.alpha_composite(p12.convert("RGBA"), ov).convert("RGB"); d = ImageDraw.Draw(p12)
sfx(d, (66, p2[1]+38), "12.2", 36)

# 12.3 — glass / dashboard plastic / puddled street / lake, one waveform crossing all surfaces.
ph, pw = p3[3]-p3[1], p3[2]-p3[0]
q = pw//4
# clean crops chosen to avoid any original printed SFX text
glass = fit(old11, (q,ph), crop=(0,2320,1000,3070), centering=(0.55,0.55))
dash = fit(old10, (q,ph), crop=(0,0,1000,930), centering=(0.5,0.5))
puddle = fit(old09, (q,ph), crop=(820,1500,2060,2240), centering=(0.5,0.65))
lake = fit(base_env, (pw-3*q,ph), crop=(520,170,1820,2050), centering=(0.58,0.42))
for idx,part in enumerate([glass,dash,puddle,lake]):
    p12.paste(part,(p3[0]+idx*q,p3[1]))
d = ImageDraw.Draw(p12); d.rectangle(p3, outline="#111", width=7)
pts=[]; sx=p3[0]+55; ex=p3[2]-55; cy=p3[1]+ph//2
for i in range(241):
    x=sx+(ex-sx)*i/240
    amp=19+8*math.sin(i*.17)
    y=cy+math.sin(i*.42)*amp+math.sin(i*.11)*8
    pts.append((x,y))
for width,color in [(16,"#17313e"),(8,"#9ac2d2"),(3,"#eefaff")]:
    d.line(pts, fill=color, width=width, joint="curve")
sfx(d,(78,p3[1]+78),"12.3",36)
sfx(d,(125,p3[1]+160),"WOOOOAARRRNNN",58,fill="#eaf8ff")
bubble(d,1645,p3[3]-260,"What the hell—",width=500,fs=38)
font=F(FONT_R,28); tw=d.textbbox((0,0),"12",font=font)[2]
d.text(((W-tw)//2,H-58),"12",font=font,fill="#111")
save(p12,12)

print("P07-P12 clean correction build complete")
