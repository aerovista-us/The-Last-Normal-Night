from pathlib import Path
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps
import math

ISSUE = Path(__file__).resolve().parents[1]
PAGES = ISSUE / 'pages'
W, H = 2063, 3150

OFF = ISSUE / 'cda.off.streets.png'
RAINY = ISSUE / '2026-09-10__21-02-04__Rainy-Lakeside-Nightfall__file_00000000e1ec81fda0870c76f82c5096.png'
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
BOLD = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
OBLIQUE = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf'


def font(size, bold=False, oblique=False):
    path = BOLD if bold else OBLIQUE if oblique else FONT
    return ImageFont.truetype(path, size)


def fit(im, size, centering=(0.5, 0.5)):
    return ImageOps.fit(im.convert('RGB'), size, method=Image.Resampling.LANCZOS, centering=centering)


def wrapped(draw, text, xy, max_width, face, fill, spacing=16):
    words = text.split()
    lines, line = [], ''
    for word in words:
        test = f'{line} {word}'.strip()
        if draw.textlength(test, font=face) <= max_width or not line:
            line = test
        else:
            lines.append(line)
            line = word
    if line:
        lines.append(line)
    x, y = xy
    ascent, descent = face.getmetrics()
    step = ascent + descent + spacing
    for row in lines:
        draw.text((x, y), row, font=face, fill=fill)
        y += step
    return y


# Recognizable Coeur d'Alene remains the dominant image. Wrong-side dawn enters
# from the left while the moon still hangs over the opposite side of the frame.
base = fit(Image.open(OFF), (W, H), centering=(0.54, 0.48))
base = ImageEnhance.Brightness(base).enhance(0.74)
base = ImageEnhance.Color(base).enhance(0.78)
page = base.convert('RGBA')

# Cold night wash plus a warm dawn intrusion from the wrong side.
wash = Image.new('RGBA', (W, H), (15, 29, 42, 70))
page = Image.alpha_composite(page, wash)
dawn = Image.new('RGBA', (W, H), (0, 0, 0, 0))
dd = ImageDraw.Draw(dawn)
for x in range(0, 900, 6):
    alpha = max(0, 94 - int(x / 11))
    dd.rectangle((x, 0, x + 6, H), fill=(242, 142, 84, alpha))
page = Image.alpha_composite(page, dawn)

# Ground the back cover with the canonical Ford/protagonist from the rainy CDA
# continuity plate. Feathering keeps this one composition rather than an inset.
rainy = Image.open(RAINY).convert('RGB')
foreground = rainy.crop((0, int(rainy.height * 0.79), rainy.width, rainy.height))
foreground = fit(foreground, (1320, 730), centering=(0.50, 0.55))
foreground = ImageEnhance.Brightness(foreground).enhance(0.70)
mask = Image.new('L', foreground.size, 0)
md = ImageDraw.Draw(mask)
md.rounded_rectangle((30, 30, foreground.width - 30, foreground.height - 30), 90, fill=220)
mask = mask.filter(ImageFilter.GaussianBlur(52))
page.paste(foreground, (690, 2220), mask)

# Editorial text field: readable at print size and Rack thumbnail scale.
overlay = Image.new('RGBA', (W, H), (0, 0, 0, 0))
od = ImageDraw.Draw(overlay)
od.rounded_rectangle((92, 118, 920, 2790), 34, fill=(4, 8, 13, 224), outline=(83, 113, 137, 150), width=3)
od.rectangle((92, 2470, 920, 2790), fill=(4, 8, 13, 244))
page = Image.alpha_composite(page, overlay)
d = ImageDraw.Draw(page)

ice = (203, 230, 246, 255)
white = (242, 245, 244, 255)
muted = (171, 188, 201, 255)
warm = (239, 182, 121, 255)

# Small series mark.
d.text((145, 175), 'ECHOSTORY · ISSUE #1', font=font(40, True), fill=ice)
d.text((145, 255), 'THE LAST NORMAL NIGHT', font=font(62, True), fill=white)
d.line((145, 345, 860, 345), fill=(116, 145, 165, 210), width=3)

# Hook and synopsis.
y = 430
for line in ('SMALL TOWN.', 'LATE NIGHT.', 'WRONG REALITY.'):
    d.text((145, y), line, font=font(46, True), fill=ice)
    y += 64

y += 44
synopsis = (
    "When an ordinary night in Coeur d'Alene slips out of alignment, one man "
    "finds familiar streets behaving like they remember him. The clocks stop. "
    "The radio wakes on Frequency Three. And a doorway offers the life he just left."
)
y = wrapped(d, synopsis, (145, y), 705, font(34), white, spacing=12)
y += 44
d.text((145, y), 'Some doors only open once.', font=font(35, True), fill=warm)

# Frequency Three signature waveform.
wave_y = 1780
points = []
for i in range(650):
    x = 150 + i * (700 / 649)
    amp = 10 + 48 * math.exp(-((i - 330) / 150) ** 2)
    yv = wave_y + math.sin(i * 0.17) * amp * 0.45 + math.sin(i * 0.051) * amp * 0.35
    points.append((x, yv))
d.line(points, fill=(123, 211, 245, 210), width=4)
d.text((145, 1850), 'FREQUENCY THREE', font=font(30, True), fill=ice)
d.text((145, 1900), 'SAME PLACE. DIFFERENT YOU.', font=font(24), fill=muted)

# Main back-cover statement on the open image side.
d.text((1010, 210), 'SOME NIGHTS', font=font(62, True), fill=white)
d.text((1010, 288), 'CHANGE EVERYTHING.', font=font(62, True), fill=white)

# Clean publishing footer — no invented ISBN/barcode.
d.text((145, 2530), 'VESPERA PUBLISHING', font=font(34, True), fill=white)
d.text((145, 2590), 'COEUR D’ALENE · NORTH IDAHO', font=font(24), fill=muted)
d.text((145, 2660), 'CONTINUES IN ISSUE 2', font=font(27, True), fill=ice)
d.text((145, 2710), 'THE WRONG SIDE OF MORNING', font=font(25), fill=white)

# Quiet lower imprint line.
d.rectangle((0, H - 120, W, H), fill=(4, 7, 10, 238))
d.text((W // 2, H - 76), 'ECHOSTORY · REAL PLACES. STRANGER STORIES.', font=font(25), fill=muted, anchor='mm')

out = page.convert('RGB')
out.save(PAGES / '26-cover-back.png', 'PNG', optimize=True, dpi=(300, 300))
assert out.size == (W, H)
print('back cover built', PAGES / '26-cover-back.png', out.size)
