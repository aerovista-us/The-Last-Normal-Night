from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageOps
import zipfile

ROOT = Path(__file__).resolve().parents[4]
ISSUE = ROOT / 'comic/issues/01-the-last-normal-night'
PAGES = ISSUE / 'pages'
W,H = 2063,3150

FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
BOLD='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
try:
    title=ImageFont.truetype(BOLD,122); sub=ImageFont.truetype(BOLD,54); body=ImageFont.truetype(FONT,38); small=ImageFont.truetype(FONT,30)
except Exception:
    title=sub=body=small=ImageFont.load_default()

def fit(path):
    return ImageOps.fit(Image.open(path).convert('RGB'),(W,H),method=Image.Resampling.LANCZOS)

def shade(im,amount=.35):
    return ImageEnhance.Brightness(im).enhance(1-amount)

def text(draw,xy,s,font,fill=(245,245,240),anchor=None):
    draw.text(xy,s,font=font,fill=fill,anchor=anchor)

# Front cover from Track 1 visual language.
cover_src = ROOT/'tracks/01-the-last-normal-night/01-the-last-normal-night.png'
front=shade(fit(cover_src),.18)
d=ImageDraw.Draw(front)
d.rectangle((0,0,W,600),fill=(8,10,14,205))
text(d,(103,105),'ECHOSTORY',sub)
text(d,(103,200),'THE LAST',title)
text(d,(103,335),'NORMAL NIGHT',title)
text(d,(103,505),'ISSUE 1 · THE CROSSING',sub,fill=(210,218,225))
d.rectangle((0,H-220,W,H),fill=(8,10,14))
text(d,(103,H-158),'A North Idaho reality-fracture story',body,fill=(205,210,215))
front.save(PAGES/'00-cover-front.png',optimize=True)

# Inside-front publishing matter.
inside=Image.new('RGB',(W,H),(12,14,18)); d=ImageDraw.Draw(inside)
text(d,(W//2,350),'THE LAST NORMAL NIGHT',title,anchor='mm')
text(d,(W//2,520),'Issue 1 · The Crossing',sub,anchor='mm',fill=(200,208,216))
d.line((270,700,W-270,700),fill=(90,96,108),width=4)
lines=[
 'Story / concept: AeroVista · EchoStory',
 'Setting: Coeur d’Alene, Idaho',
 '24 story pages · print-first master edition',
 '',
 'Continuity anchors: the truck · the white sedan · 11:59',
 'the lake · Frequency Three · WELCOME messages',
 '',
 'This issue ends with a choice, not an explanation.',
]
y=900
for line in lines:
    text(d,(W//2,y),line,body,anchor='mm',fill=(224,226,228)); y+=92
text(d,(W//2,H-300),'ECHOSTORY',sub,anchor='mm',fill=(150,160,175))
inside.save(PAGES/'01-inside-front.png',optimize=True)

# Back cover uses the established lake/night mood.
back_src = ISSUE/'2026-09-10__21-02-04__Rainy-Lakeside-Nightfall__file_00000000e1ec81fda0870c76f82c5096.png'
back=shade(fit(back_src),.30); d=ImageDraw.Draw(back)
d.rectangle((120,180,W-120,760),fill=(7,9,13))
text(d,(W//2,310),'END ISSUE #1',title,anchor='mm')
text(d,(W//2,500),'THE LAST NORMAL NIGHT',sub,anchor='mm',fill=(205,213,221))
text(d,(W//2,650),'Continues: Issue 2 · The Wrong Side of Morning',body,anchor='mm',fill=(205,213,221))
d.rectangle((120,H-520,W-120,H-160),fill=(7,9,13))
text(d,(W//2,H-390),'WELCOME HOME',sub,anchor='mm')
text(d,(W//2,H-275),'EchoStory · AeroVista',body,anchor='mm',fill=(180,188,198))
back.save(PAGES/'26-cover-back.png',optimize=True)

# Package the complete issue in publishing order.
archive=ISSUE/'EP1-The-Last-Normal-Night.cbz'
ordered=[PAGES/'00-cover-front.png',PAGES/'01-inside-front.png']
ordered += [PAGES/f'p{n:02d}.png' for n in range(1,25)]
ordered += [PAGES/'26-cover-back.png']
for p in ordered:
    if not p.exists(): raise SystemExit(f'missing publishing asset: {p}')
with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for idx,p in enumerate(ordered):
        if p.name.startswith('p'):
            n=int(p.stem[1:]); arc=f'{n+1:02d}-p{n:02d}.png'
        else:
            arc=p.name
        z.write(p,arc)
print('publishing assets generated:', PAGES/'00-cover-front.png', PAGES/'01-inside-front.png', PAGES/'26-cover-back.png', archive)
