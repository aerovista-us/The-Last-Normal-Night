from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageFilter
import math

ISSUE = Path(__file__).resolve().parents[1]
PAGES = ISSUE / "pages"
W, H = 2063, 3150
WHITE = "#f4f2ec"
INK = "#071018"
CREAM = "#f3ead0"
BORDER = "#eceff1"

FONT_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_R = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_I = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf"


def F(path, size):
    return ImageFont.truetype(path, size)


def fit(im, size=(W, H), crop=None, centering=(0.5, 0.5)):
    if crop is not None:
        im = im.crop(crop)
    return ImageOps.fit(im.convert("RGB"), size, method=Image.Resampling.LANCZOS, centering=centering)


def open_page(name):
    return fit(Image.open(PAGES / name))


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


def patch_neighbor(im, target, source):
    sx0, sy0, sx1, sy1 = source
    tx0, ty0, tx1, ty1 = target
    patch = im.crop((sx0, sy0, sx1, sy1)).resize((tx1 - tx0, ty1 - ty0), Image.Resampling.LANCZOS)
    patch = patch.filter(ImageFilter.GaussianBlur(5))
    im.paste(patch, (tx0, ty0))


def save(im, n):
    out = PAGES / f"p{n:02d}.png"
    im.convert("RGB").save(out, "PNG", optimize=True)
    print(f"wrote {out}")


# PAGE 07 — promote the approved convenience-store candidate.
p07 = open_page("p07-candidate.png")
save(p07, 7)


# PAGE 08 — promote approved candidate, remove the stray phone time from both phone panels.
p08 = open_page("p08-candidate.png")
d = ImageDraw.Draw(p08)
# Candidate is the approved four-beat page. Time readouts are not part of canon here.
for box in [(218, 2070, 390, 2142), (1240, 2070, 1415, 2142)]:
    d.rounded_rectangle(box, radius=18, fill="#08101a")
save(p08, 8)


# PAGE 09 — preserve good white-sedan/red-signal art, remove erroneous 10:47 PM location stamp.
p09 = open_page("p09.png")
# Replace the upper-left time stamp with nearby rainy background; no replacement timestamp.
patch_neighbor(p09, (24, 20, 560, 270), (560, 20, 1096, 270))
save(p09, 9)


# PAGE 10 — preserve strong 11:59 convergence art and restore the two canonical reaction lines.
p10 = open_page("p10.png")
d = ImageDraw.Draw(p10)
bubble(d, 1590, 2220, "Okay.", width=270, fs=36)
bubble(d, 1570, 2400, "That’s not funny.", width=470, fs=36)
save(p10, 10)


# PAGE 11 — preserve strong frozen-time art, restore canonical SFX/caption.
p11 = open_page("p11.png")
d = ImageDraw.Draw(p11)
# Dark repair fields cover earlier approximate SFX while keeping the art intact.
d.rounded_rectangle((58, 1120, 650, 1500), radius=24, fill=(7, 12, 16))
sfx(d, (110, 1260), "RRRRMM", 64)
d.rounded_rectangle((300, 1970, 760, 2250), radius=24, fill=(7, 12, 16))
sfx(d, (390, 2070), "KRRK", 62)
caption(d, 1370, 2740, "Eleven fifty-nine.", width=520, fs=36)
save(p11, 11)


# PAGE 12 — deterministic canonical 3-panel proximity page.
# No countdown yet, no doorway, no stranger, no Frequency Three.
base_street = fit(Image.open(ISSUE / "2026-09-10__19-30-37__Moonlit-Lakeside-Town-Reflections__file_00000000a43c8230a403848b7670b888.png"))
source_p11 = open_page("p11.png")
source_p09 = open_page("p09.png")

p12 = Image.new("RGB", (W, H), WHITE)
d = ImageDraw.Draw(p12)
margin = 20
gap = 14
# white comic-page border language matching pages 9–13
p1 = (margin, margin, W - margin, 1330)
p2 = (margin, p1[3] + gap, W - margin, 1835)
p3 = (margin, p2[3] + gap, W - margin, H - 76)

# 12.1: compressed empty intersection with lake beyond; rear of truck added as grounded silhouette.
street = fit(base_street, (p1[2]-p1[0], p1[3]-p1[1]), crop=(240, 520, 1820, 2560), centering=(0.5, 0.63))
street = street.resize((int(street.width * 0.88), street.height), Image.Resampling.LANCZOS)
canvas = Image.new("RGB", (p1[2]-p1[0], p1[3]-p1[1]), "#070b10")
canvas.paste(street, ((canvas.width-street.width)//2, 0))
p12.paste(canvas, (p1[0], p1[1]))
d.rectangle(p1, outline="#111", width=7)
cx = W // 2
truck_y = 970
d.rounded_rectangle((cx-255, truck_y, cx+255, truck_y+235), radius=30, fill="#101417", outline="#343c42", width=5)
d.rectangle((cx-205, truck_y+35, cx+205, truck_y+125), fill="#182126")
d.rectangle((cx-210, truck_y+162, cx-145, truck_y+202), fill="#b91f27")
d.rectangle((cx+145, truck_y+162, cx+210, truck_y+202), fill="#b91f27")
d.text((74, 72), "12.1", font=F(FONT_B, 36), fill="white", stroke_width=2, stroke_fill="#111")

# 12.2: wet pavement / lower body + impossible shadow angled across all plausible light directions.
road = fit(source_p09, (p2[2]-p2[0], p2[3]-p2[1]), crop=(40, 2280, 2020, 3040), centering=(0.5, 0.7))
p12.paste(road, (p2[0], p2[1]))
d.rectangle(p2, outline="#111", width=7)
midy = p2[1] + 115
d.rectangle((cx-55, midy, cx-15, midy+190), fill="#090b0d")
d.rectangle((cx+15, midy, cx+55, midy+190), fill="#090b0d")
d.polygon([(cx-30, midy+170), (cx+10, midy+182), (W-110, p2[3]-58), (W-170, p2[3]-20)], fill="#050607")
d.text((74, p2[1]+32), "12.2", font=F(FONT_B, 36), fill="white", stroke_width=2, stroke_fill="#111")

# 12.3: dashboard/glass/puddle/lake surfaces crossed by one continuous pressure waveform.
ph = p3[3]-p3[1]
pw = p3[2]-p3[0]
third = pw // 3
left = fit(source_p11, (third, ph), crop=(0, 1820, 820, 3040), centering=(0.5,0.5))
mid = fit(source_p11, (third, ph), crop=(0, 930, 1030, 1850), centering=(0.4,0.5))
right = fit(base_street, (pw-2*third, ph), crop=(650, 300, 1800, 2100), centering=(0.55,0.4))
p12.paste(left, (p3[0], p3[1]))
p12.paste(mid, (p3[0]+third, p3[1]))
p12.paste(right, (p3[0]+2*third, p3[1]))
d.rectangle(p3, outline="#111", width=7)
pts=[]
start_x=p3[0]+60
end_x=p3[2]-60
center_y=p3[1]+ph//2
for i in range(0, 241):
    x=start_x + (end_x-start_x)*i/240
    amp=18 + 9*math.sin(i*0.17)
    y=center_y + math.sin(i*0.42)*amp + math.sin(i*0.11)*9
    pts.append((x,y))
for width, fill in [(15, "#203743"), (8, "#9fc6d5"), (3, "#eef8fb")]:
    d.line(pts, fill=fill, width=width, joint="curve")
sfx(d, (120, p3[1]+115), "WOOOOAARRRNNN", 62, fill="#eaf8ff")
bubble(d, 1630, p3[3]-270, "What the hell—", width=500, fs=38)
d.text((74, p3[1]+32), "12.3", font=F(FONT_B, 36), fill="white", stroke_width=2, stroke_fill="#111")
num = "12"
font = F(FONT_R, 28)
tw = d.textbbox((0,0), num, font=font)[2]
d.text(((W-tw)//2, H-58), num, font=font, fill="#111")
save(p12, 12)

print("P07-P12 corrected build complete")
# trigger-build: 2026-09-13
