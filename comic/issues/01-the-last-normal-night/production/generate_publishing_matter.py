from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageOps
from io import BytesIO
import zipfile

ROOT = Path(__file__).resolve().parents[4]
ISSUE = ROOT / 'comic/issues/01-the-last-normal-night'
PAGES = ISSUE / 'pages'
W,H = 2063,3150
MAX_ARCHIVE = 95 * 1024 * 1024

FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
BOLD='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
try:
    title=ImageFont.truetype(BOLD,118); sub=ImageFont.truetype(BOLD,50); body=ImageFont.truetype(FONT,38); small=ImageFont.truetype(FONT,30)
except Exception:
    title=sub=body=small=ImageFont.load_default()

def fit(path):
    return ImageOps.fit(Image.open(path).convert('RGB'),(W,H),method=Image.Resampling.LANCZOS)

def shade(im,amount=.35):
    return ImageEnhance.Brightness(im).enhance(1-amount)

def text(draw,xy,s,font,fill=(245,245,240),anchor=None):
    draw.text(xy,s,font=font,fill=fill,anchor=anchor)

# Front cover: use clean CDA noir environment art rather than Track 1 album art.
# The album art contains baked title text, which caused the duplicate/ghost title
# visible on The Rack thumbnail. Keep comic typography authored here only.
cover_src = ISSUE/'2026-09-10__20-58-21__Rainy-Noir-in-Downtown-Coeur-dAlene__file_00000000706481fdb43883c8c8ec1289.png'
front=shade(fit(cover_src),.16)
d=ImageDraw.Draw(front)
# Strong, clean title field that remains readable at Rack-thumbnail size.
d.rectangle((0,0,W,760),fill=(7,9,12))
d.line((95,760,W-95,760),fill=(57,67,78),width=3)
text(d,(103,92),'ECHOSTORY',sub,fill=(190,202,212))
text(d,(103,195),'THE LAST',title)
text(d,(103,332),'NORMAL NIGHT',title)
text(d,(103,545),'ISSUE 1 · THE CROSSING',sub,fill=(214,221,228))
text(d,(103,628),'A NORTH IDAHO REALITY-FRACTURE STORY',small,fill=(146,158,170))
# Minimal footer mark; leave the image itself dominant.
d.rectangle((0,H-150,W,H),fill=(7,9,12))
text(d,(103,H-103),'VESPERA PUBLISHING · ECHOSTORY',small,fill=(154,165,176))
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

# Package reader-quality JPEGs inside CBZ while retaining full-resolution PNG masters in the repo.
archive=ISSUE/'EP1-The-Last-Normal-Night.cbz'
ordered=[PAGES/'00-cover-front.png',PAGES/'01-inside-front.png']
ordered += [PAGES/f'p{n:02d}.png' for n in range(1,25)]
ordered += [PAGES/'26-cover-back.png']
for p in ordered:
    if not p.exists(): raise SystemExit(f'missing publishing asset: {p}')

def build_cbz(quality):
    if archive.exists(): archive.unlink()
    with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_STORED) as z:
        for idx,p in enumerate(ordered):
            with Image.open(p) as im:
                im=im.convert('RGB')
                buf=BytesIO()
                im.save(buf,format='JPEG',quality=quality,optimize=True,progressive=True,subsampling=1)
                if p.name.startswith('p'):
                    n=int(p.stem[1:]); arc=f'{n+1:02d}-p{n:02d}.jpg'
                elif p.name=='00-cover-front.png': arc='00-cover-front.jpg'
                elif p.name=='01-inside-front.png': arc='01-inside-front.jpg'
                else: arc='26-cover-back.jpg'
                z.writestr(arc,buf.getvalue())
    return archive.stat().st_size

for quality in (90,86,82,78):
    size=build_cbz(quality)
    print(f'CBZ quality {quality}: {size/1024/1024:.2f} MB')
    if size <= MAX_ARCHIVE:
        break
else:
    raise SystemExit(f'CBZ remains too large: {size/1024/1024:.2f} MB')

print('publishing assets generated:', PAGES/'00-cover-front.png', PAGES/'01-inside-front.png', PAGES/'26-cover-back.png', archive)
