from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageEnhance, ImageFilter

ROOT = Path(__file__).resolve().parents[1]
PAGES = ROOT / 'pages'
PAGES.mkdir(parents=True, exist_ok=True)

W, H = 2063, 3150
HEADER_H, FOOTER_H = 170, 110
MARGIN, GAP = 26, 14
INK = '#071018'
CREAM = '#f3ead0'
WHITE = '#f4f5f2'
BLUE = '#a9d8f5'
LINE = '#e8edf1'

MOONLIT = ROOT / '2026-09-10__19-30-37__Moonlit-Lakeside-Town-Reflections__file_00000000a43c8230a403848b7670b888.png'
MOOSE = ROOT / '2026-09-10__21-01-42__Moose-Mug-Rainy-Lakeside-Night__file_00000000683c82309af8f598a7113737.png'
RAINY = ROOT / '2026-09-10__21-02-04__Rainy-Lakeside-Nightfall__file_00000000e1ec81fda0870c76f82c5096.png'
OLD_P05 = PAGES / 'p05-rejected-concept.png'
OLD_P06 = PAGES / 'p06-rejected-concept.png'
OLD_P09 = PAGES / 'p09-legacy-concept.png'

for required in [MOONLIT, MOOSE, RAINY, OLD_P05, OLD_P06, OLD_P09]:
    if not required.exists():
        raise FileNotFoundError(required)


def font(name, size):
    return ImageFont.truetype(name, size)

SERIF_B = 'DejaVuSerif-Bold.ttf'
SANS_B = 'DejaVuSans-Bold.ttf'
SANS = 'DejaVuSans.ttf'
SANS_I = 'DejaVuSans-Oblique.ttf'


def cover(im, size, crop=None, centering=(0.5, 0.5)):
    if crop:
        im = im.crop(crop)
    return ImageOps.fit(im, size, method=Image.Resampling.LANCZOS, centering=centering)


def header(page, n):
    d = ImageDraw.Draw(page)
    d.rectangle((0, 0, W, HEADER_H), fill=INK)
    d.text((42, 20), 'EchoStory', font=font(SERIF_B, 72), fill=WHITE)
    d.text((45, 105), 'T H E   L A S T   N O R M A L   N I G H T', font=font(SANS, 23), fill='#c8d2d9')
    d.line((640, 62, 1020, 62), fill='#6bb2d8', width=3)
    d.text((1120, 24), 'EP1', font=font(SERIF_B, 52), fill=WHITE)
    d.text((1122, 98), f'{n:02d} / 24', font=font(SANS, 29), fill='#c6d6df')
    d.line((1290, 22, 1290, 150), fill='#617989', width=2)
    d.text((1330, 38), 'COEUR D’ALENE, IDAHO', font=font(SANS_B, 25), fill=WHITE)
    d.text((1330, 83), 'SAME STREETS. DIFFERENT TOMORROW.', font=font(SANS, 21), fill='#c5d0d7')
    d.text((1842, 36), 'NORTH IDAHO', font=font(SANS_B, 18), fill='#c7d7e0')
    for x in (1885, 1920, 1955):
        d.polygon([(x, 76), (x-14, 106), (x-5, 106), (x-18, 131), (x+18, 131), (x+5, 106), (x+14, 106)], fill=BLUE)


def footer(page):
    d = ImageDraw.Draw(page)
    y = H - FOOTER_H
    d.rectangle((0, y, W, H), fill=INK)
    d.text((42, y+24), 'EchoStory', font=font(SERIF_B, 38), fill=WHITE)
    d.text((295, y+42), 'EP1 - THE LAST NORMAL NIGHT', font=font(SANS, 19), fill='#b9ccd7')
    d.text((1260, y+33), '“Same places. Different tomorrow.”', font=font(SANS_I, 26), fill='#d7d7d0')


def border(d, box):
    d.rectangle(box, outline=LINE, width=7)


def wrap(draw, text, ff, maxw):
    lines, cur = [], ''
    for word in text.split():
        test = (cur + ' ' + word).strip()
        if draw.textbbox((0, 0), test, font=ff)[2] <= maxw:
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def panel_label(d, x, y, code, title, subtitle=None, w=520):
    h = 104 if subtitle else 72
    cw = 96
    d.rectangle((x, y, x+w, y+h), fill=CREAM, outline='#111', width=4)
    d.rectangle((x, y, x+cw, y+h), fill='#0b1015', outline='#111', width=3)
    d.text((x+18, y+12), code, font=font(SANS_B, 31), fill=WHITE)
    d.text((x+cw+16, y+10), title, font=font(SANS_B, 24), fill='#111')
    if subtitle:
        d.text((x+cw+16, y+50), subtitle, font=font(SANS, 19), fill='#111')


def caption(d, x, y, text, w=620, fs=29):
    ff = font(SANS_I, fs)
    lines = wrap(d, text, ff, w-28)
    lh = fs + 7
    h = 20 + lh * len(lines)
    d.rectangle((x, y, x+w, y+h), fill=CREAM, outline='#111', width=3)
    yy = y + 9
    for line in lines:
        d.text((x+14, yy), line, font=ff, fill='#111')
        yy += lh
    return h


def bubble(d, cx, cy, text, w=500, fs=25):
    ff = font(SANS, fs)
    lines = wrap(d, text, ff, w-44)
    lh = fs + 7
    h = 36 + lh * len(lines)
    x, y = cx - w//2, cy - h//2
    d.rounded_rectangle((x, y, x+w, y+h), radius=32, fill='white', outline='#111', width=4)
    yy = y + 17
    for line in lines:
        tw = d.textbbox((0, 0), line, font=ff)[2]
        d.text((cx - tw/2, yy), line, font=ff, fill='#111')
        yy += lh


def soft_composite(base, insert, xy, feather=30):
    insert = insert.convert('RGBA')
    mask = Image.new('L', insert.size, 255)
    md = ImageDraw.Draw(mask)
    for i in range(feather):
        alpha = int(255 * i / feather)
        md.rectangle((i, i, insert.width-i-1, insert.height-i-1), outline=alpha)
    mask = mask.filter(ImageFilter.GaussianBlur(feather/2))
    base.paste(insert, xy, mask)


moonlit = Image.open(MOONLIT).convert('RGB')
moose = Image.open(MOOSE).convert('RGB')
rainy = Image.open(RAINY).convert('RGB')
old5 = Image.open(OLD_P05).convert('RGB')
old6 = Image.open(OLD_P06).convert('RGB')
old9 = Image.open(OLD_P09).convert('RGB')

# PAGE 01 — single full-page splash, exact canonical narration.
p = Image.new('RGB', (W, H), INK)
header(p, 1); footer(p); d = ImageDraw.Draw(p)
art_y = HEADER_H
art_h = H - HEADER_H - FOOTER_H
sw, sh = moonlit.size
crop_w = 700
cx = int(sw * 0.52)
art = cover(moonlit, (W-2*MARGIN, art_h), (cx-crop_w//2, 0, cx+crop_w//2, sh))
p.paste(art, (MARGIN, art_y)); border(d, (MARGIN, art_y, W-MARGIN, art_y+art_h))
# small protagonist/truck anchor from source art, blended into lower right
anchor = rainy.crop((0, 1195, min(760, rainy.width), min(1548, rainy.height)))
anchor = cover(anchor, (520, 245), centering=(0.48, 0.5))
anchor = ImageEnhance.Brightness(anchor).enhance(0.82)
soft_composite(p, anchor, (1260, 2495), 38)
y = 235
for text in [
    'September air.',
    'Lake went black about an hour ago.',
    'Same town. Same roads. Same people pretending tomorrow was guaranteed.'
]:
    h = caption(d, 72, y, text, 710, 31)
    y += h + 17
h = caption(d, 1260, 2250, 'Wasn’t anything special.', 600, 31)
caption(d, 1260, 2250+h+16, 'That’s what gets me.', 600, 31)
p.save(PAGES/'p01.png', optimize=True)

# PAGE 02 — four panels, canonical bar dialogue.
p = Image.new('RGB', (W, H), INK)
header(p, 2); footer(p); d = ImageDraw.Draw(p)
ct, cb = HEADER_H+10, H-FOOTER_H-10
p1 = (MARGIN, ct, W-MARGIN, ct+730)
mt, mh = p1[3]+GAP, 810
p2 = (MARGIN, mt, W//2-GAP//2, mt+mh)
p3 = (W//2+GAP//2, mt, W-MARGIN, mt+mh)
p4 = (MARGIN, mt+mh+GAP, W-MARGIN, cb)
for box, crop_box, centering in [
    (p1, (0, 0, min(1015, moose.width), min(390, moose.height)), (0.45, 0.5)),
    (p2, (45, 420, min(600, moose.width), min(820, moose.height)), (0.58, 0.57)),
    (p3, (0, 725, min(520, moose.width), min(1095, moose.height)), (0.52, 0.5)),
    (p4, (0, 390, min(585, moose.width), min(745, moose.height)), (0.57, 0.58)),
]:
    piece = cover(moose, (box[2]-box[0], box[3]-box[1]), crop_box, centering)
    p.paste(piece, (box[0], box[1])); border(d, box)
panel_label(d, p1[0]+12, p1[1]+12, '2.1', 'NEIGHBORHOOD BAR.', 'WARM. ORDINARY. FAMILIAR.', 570)
bubble(d, 650, 445, 'You still coming Monday or you gonna mysteriously become unavailable again?', 650, 24)
bubble(d, 1360, 585, 'Depends how committed I am to disappointing everybody.', 620, 24)
panel_label(d, p2[0]+12, p2[1]+12, '2.2', 'HALF-FULL DRINK.', 'HE LISTENS MORE THAN HE TALKS.', 560)
bubble(d, 320, 1320, 'That’s healthy.', 310, 24)
bubble(d, 710, 1470, 'It’s efficient.', 290, 24)
panel_label(d, p3[0]+12, p3[1]+12, '2.3', 'RELATIONSHIP DRAMA.', 'HE GLANCES TOWARD THE DARK WINDOW.', 620)
bubble(d, 1390, 1260, 'I’m telling you, she said “we need space” and then sent me twelve paragraphs.', 640, 23)
bubble(d, 1650, 1570, 'That sounds like a lot of space.', 520, 24)
panel_label(d, p4[0]+12, p4[1]+12, '2.4', 'LAUGHTER.', 'WARM ROOM. HIS ATTENTION DRIFTS OUTSIDE.', 620)
caption(d, 1320, p4[3]-155, 'Old friends killing borrowed time.', 580, 29)
p.save(PAGES/'p02.png', optimize=True)

# PAGE 03 — truck, battery, bass, white-car seed.
p = Image.new('RGB', (W, H), INK)
header(p, 3); footer(p); d = ImageDraw.Draw(p)
ct, cb = HEADER_H+10, H-FOOTER_H-10
p31 = (MARGIN, ct, W-MARGIN, ct+610)
r2 = p31[3]+GAP
p32 = (MARGIN, r2, W//2-GAP//2, r2+510)
p33 = (W//2+GAP//2, r2, W-MARGIN, r2+510)
p34 = (MARGIN, r2+510+GAP, W-MARGIN, r2+510+GAP+650)
p35 = (MARGIN, p34[3]+GAP, W-MARGIN, cb)
for box, src, crop_box, centering in [
    (p31, moose, (0,0,min(1015,moose.width),min(390,moose.height)), (0.45,0.5)),
    (p32, moose, (min(585,moose.width-1),390,moose.width,min(745,moose.height)), (0.54,0.48)),
    (p33, rainy, (0,385,min(1015,rainy.width),min(670,rainy.height)), (0.52,0.55)),
    (p34, rainy, (0,min(1185,rainy.height-1),min(1015,rainy.width),rainy.height), (0.52,0.52)),
]:
    piece = cover(src, (box[2]-box[0], box[3]-box[1]), crop_box, centering)
    p.paste(piece,(box[0],box[1])); border(d,box)
panel_label(d,p31[0]+12,p31[1]+12,'3.1','OUTSIDE.','COOL SEPTEMBER NIGHT.',500)
bubble(d,530,500,'Text when you get home.',430,24); bubble(d,1260,585,'Sure.',220,25)
panel_label(d,p32[0]+12,p32[1]+12,'3.2','12%.','NO URGENCY.',400); caption(d,p32[0]+45,p32[3]-125,'Phone said twelve percent.',500,26)
panel_label(d,p33[0]+12,p33[1]+12,'3.3','BASS DOWN THE BLOCK.','WINDOWS DOWN.',520)
d.text((p33[0]+170,p33[1]+335),'WHUMM—WHUMM',font=font(SANS_B,38),fill=WHITE,stroke_width=2,stroke_fill='#111')
panel_label(d,p34[0]+12,p34[1]+12,'3.4','THE TRUCK.','FAMILIAR ANCHOR.',470); caption(d,1300,p34[3]-145,'Cool lake wind moving through the air.',620,28)
sed = old6.crop((300,675,min(845,old6.width),min(870,old6.height)))
piece = cover(sed,(p35[2]-p35[0],p35[3]-p35[1]),centering=(0.55,0.5))
p.paste(piece,(p35[0],p35[1])); border(d,p35); panel_label(d,p35[0]+12,p35[1]+12,'3.5','ACROSS THE STREET.','OLDER WHITE SEDAN.',520)
p.save(PAGES/'p03.png', optimize=True)

# PAGE 04 — dog bark, then deliberate repeated framing with silence.
p = Image.new('RGB',(W,H),INK); header(p,4); footer(p); d=ImageDraw.Draw(p)
ct, cb = HEADER_H+10, H-FOOTER_H-10
boxes=[(MARGIN,ct,W-MARGIN,ct+620),(MARGIN,ct+634,W-MARGIN,ct+1254),(MARGIN,ct+1268,W-MARGIN,ct+1900),(MARGIN,ct+1914,W-MARGIN,cb)]
src_box=(12,88,min(1005,old9.width),min(445,old9.height))
piece=cover(old9,(boxes[0][2]-boxes[0][0],boxes[0][3]-boxes[0][1]),src_box); p.paste(piece,(boxes[0][0],boxes[0][1])); border(d,boxes[0])
panel_label(d,38,195,'4.1','A LITTLE WALK.','DOG BARKS SOMEWHERE UPHILL.',560); d.text((1320,610),'WOOF. WOOF.',font=font(SANS_B,36),fill=WHITE,stroke_width=2,stroke_fill='#111')
piece2=ImageEnhance.Brightness(piece).enhance(.68); p.paste(piece2,(boxes[1][0],boxes[1][1])); border(d,boxes[1]); panel_label(d,38,829,'4.2','ONE BEAT LATER.','NOTHING MOVES.',500)
piece=cover(old9,(boxes[2][2]-boxes[2][0],boxes[2][3]-boxes[2][1]),(12,760,min(1005,old9.width),min(1045,old9.height)),(0.38,0.5)); p.paste(piece,(boxes[2][0],boxes[2][1])); border(d,boxes[2]); panel_label(d,38,1464,'4.3','THE SILENCE.','HE JUST REGISTERS IT.',500); bubble(d,1500,1740,'Huh.',210,28)
piece=cover(old9,(boxes[3][2]-boxes[3][0],boxes[3][3]-boxes[3][1]),(12,1050,min(1005,old9.width),min(1430,old9.height))); p.paste(piece,(boxes[3][0],boxes[3][1])); border(d,boxes[3]); panel_label(d,38,2108,'4.4','KEEP WALKING.','THE STREET FEELS TOO EMPTY.',560); caption(d,1280,2670,'Then everything went still.',600,29); caption(d,1280,2765,'Didn’t notice then.',600,29)
p.save(PAGES/'p04.png', optimize=True)

# PAGE 05 — streetlight / phone signal / whisper.
p = Image.new('RGB',(W,H),INK); header(p,5); footer(p); d=ImageDraw.Draw(p)
ct, cb = HEADER_H+10, H-FOOTER_H-10
boxes=[(MARGIN,ct,W-MARGIN,ct+640),(MARGIN,ct+654,W-MARGIN,ct+1284),(MARGIN,ct+1298,W-MARGIN,ct+2010),(MARGIN,ct+2024,W-MARGIN,cb)]
piece=cover(old5,(boxes[0][2]-boxes[0][0],boxes[0][3]-boxes[0][1]),(10,85,min(1005,old5.width),min(430,old5.height))); p.paste(piece,(boxes[0][0],boxes[0][1])); border(d,boxes[0]); panel_label(d,38,195,'5.1','STREETLIGHT AHEAD.','BURNING NORMALLY.',500)
piece=cover(old5,(boxes[1][2]-boxes[1][0],boxes[1][3]-boxes[1][1]),(10,455,min(1005,old5.width),min(815,old5.height))); piece=ImageEnhance.Brightness(piece).enhance(.62); p.paste(piece,(boxes[1][0],boxes[1][1])); border(d,boxes[1]); panel_label(d,38,849,'5.2','DIRECTLY UNDER IT.','THE LIGHT CLICKS OFF.',500); d.text((1520,1180),'TCHK',font=font(SANS_B,42),fill=WHITE,stroke_width=2,stroke_fill='#111')
piece=cover(old5,(boxes[2][2]-boxes[2][0],boxes[2][3]-boxes[2][1]),(20,825,min(1000,old5.width),min(1120,old5.height)),(0.48,0.5)); p.paste(piece,(boxes[2][0],boxes[2][1])); border(d,boxes[2]); panel_label(d,38,1493,'5.3','PAST THE LIGHT.','IT COMES BACK ON.',500)
d.rounded_rectangle((110,1690,485,1945),radius=34,fill='#0a0f18',outline='#b8c2cc',width=4); d.text((155,1725),'SIGNAL',font=font(SANS_B,24),fill='#cdd8df')
for i,hgt in enumerate([38,68,100,135,0]):
    x=165+i*56
    if hgt>0: d.rectangle((x,1905-hgt,x+34,1905),fill=WHITE)
d.text((150,1915),'1  →  5  →  NONE',font=font(SANS,23),fill='#dce3e7'); bubble(d,1510,1850,'Come on.',270,27)
piece=cover(old5,(boxes[3][2]-boxes[3][0],boxes[3][3]-boxes[3][1]),(10,1135,min(1005,old5.width),min(1475,old5.height)),(0.55,0.5)); p.paste(piece,(boxes[3][0],boxes[3][1])); border(d,boxes[3]); panel_label(d,38,2220,'5.4','OVER HIS SHOULDER.','EMPTY SIDEWALK.',500); bubble(d,1430,2555,'Don’t go home.',420,27); bubble(d,520,2750,'Hello?',260,27)
p.save(PAGES/'p05.png', optimize=True)

# PAGE 06 — measurable contradiction, preserve reveal order: 11:58 then 11:57, not 11:59.
p = Image.new('RGB',(W,H),INK); header(p,6); footer(p); d=ImageDraw.Draw(p)
ct, cb = HEADER_H+10, H-FOOTER_H-10
b1=(MARGIN,ct,W-MARGIN,ct+610); r2=ct+624; b2=(MARGIN,r2,W//2-GAP//2,r2+610); b3=(W//2+GAP//2,r2,W-MARGIN,r2+610); r3=r2+624; b4=(MARGIN,r3,W//2-GAP//2,r3+600); b5=(W//2+GAP//2,r3,W-MARGIN,r3+600); b6=(MARGIN,r3+614,W-MARGIN,cb)
sw,sh=moonlit.size; crop_box=(min(430,sw-2),min(130,sh-2),min(1240,sw),min(940,sh)); piece=cover(moonlit,(b1[2]-b1[0],b1[3]-b1[1]),crop_box,(0.45,0.62)); p.paste(piece,(b1[0],b1[1])); border(d,b1); panel_label(d,38,195,'6.1','SHERMAN AVENUE.','THE BLOCK FEELS TOO LONG.',560); caption(d,1290,625,'Walked downtown but the road felt stretched.',620,28)
sed=old6.crop((300,675,min(845,old6.width),min(870,old6.height))); piece=cover(sed,(b2[2]-b2[0],b2[3]-b2[1]),centering=(0.55,0.5)); p.paste(piece,(b2[0],b2[1])); border(d,b2); panel_label(d,38,r2+14,'6.2','WHITE SEDAN.','FIRST PASS.',390)
piece2=ImageEnhance.Brightness(piece).enhance(.9); p.paste(piece2,(b3[0],b3[1])); border(d,b3); panel_label(d,b3[0]+12,r2+14,'6.3','TWO BLOCKS LATER.','SAME DENT. SAME DIRECTION.',560)
for box,code,tval in [(b4,'6.4','11:58'),(b5,'6.5','11:57')]:
    d.rectangle(box,fill='#121820'); border(d,box); panel_label(d,box[0]+12,box[1]+12,code,'DIGITAL SIGN.','SECONDS APART.',440); d.rounded_rectangle((box[0]+185,box[1]+205,box[2]-185,box[3]-100),radius=36,fill='#050708',outline='#303a40',width=5); ff=font(SANS_B,92); tw=d.textbbox((0,0),tval,font=ff)[2]; d.text(((box[0]+box[2]-tw)/2,box[1]+300),tval,font=ff,fill='#ffbb4b')
piece=cover(old9,(b6[2]-b6[0],b6[3]-b6[1]),(12,760,min(1005,old9.width),min(1045,old9.height)),(0.4,0.5)); p.paste(piece,(b6[0],b6[1])); border(d,b6); panel_label(d,38,b6[1]+14,'6.6','HE LOOKS BACK.','THE NUMBER WENT THE WRONG WAY.',620); bubble(d,1580,b6[1]+340,'Wait.',240,28)
p.save(PAGES/'p06.png', optimize=True)

print('Built corrected EP1 opening pages:', ', '.join(f'p{n:02d}.png' for n in range(1,7)))
