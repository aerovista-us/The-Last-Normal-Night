from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps
import hashlib

ISSUE = Path(__file__).resolve().parents[1]
PAGES = ISSUE / 'pages'
ART = ISSUE / 'production' / 'artifacts'
ART.mkdir(parents=True, exist_ok=True)
W, H = 2063, 3150
HEADER_H, FOOTER_H = 150, 76
MARGIN, GAP = 24, 16
INK = '#071018'; PAPER = '#f3ead0'; WHITE = '#f4f5f2'
SRC = ISSUE / '2026-09-10__21-01-42__Moose-Mug-Rainy-Lakeside-Night__file_00000000683c82309af8f598a7113737.png'
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
FONT_B = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
FONT_I = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf'

def font(size, bold=False, italic=False):
    return ImageFont.truetype(FONT_I if italic else (FONT_B if bold else FONT), size)

def fit(im, size, crop=None, centering=(.5,.5)):
    if crop: im = im.crop(crop)
    return ImageOps.fit(im.convert('RGB'), size, method=Image.Resampling.LANCZOS, centering=centering)

def border(d, box): d.rectangle(box, outline=WHITE, width=7)

def wrap(d, text, f, maxw):
    lines=[]; cur=''
    for word in text.split():
        test=(cur+' '+word).strip()
        if d.textbbox((0,0), test, font=f)[2] <= maxw: cur=test
        else:
            if cur: lines.append(cur)
            cur=word
    if cur: lines.append(cur)
    return lines

def bubble(d, cx, cy, text, width=560, fs=27):
    f=font(fs); lines=wrap(d,text,f,width-52); lh=fs+8; h=38+lh*len(lines)
    x=cx-width//2; y=cy-h//2
    d.rounded_rectangle((x,y,x+width,y+h), radius=34, fill='white', outline='#111', width=4)
    yy=y+18
    for line in lines:
        tw=d.textbbox((0,0),line,font=f)[2]
        d.text((cx-tw/2,yy),line,font=f,fill='#111'); yy+=lh

def caption(d, x, y, text, width=580, fs=27):
    f=font(fs, italic=True); lines=wrap(d,text,f,width-34); lh=fs+8; h=28+lh*len(lines)
    d.rectangle((x,y,x+width,y+h), fill=PAPER, outline='#111', width=3)
    yy=y+12
    for line in lines:
        d.text((x+16,yy),line,font=f,fill='#111'); yy+=lh

def header(page):
    d=ImageDraw.Draw(page); d.rectangle((0,0,W,HEADER_H),fill=INK)
    d.text((42,24),'EchoStory',font=font(58,True),fill=WHITE)
    d.text((480,40),'THE LAST NORMAL NIGHT',font=font(25),fill='#ccd6dc')
    d.text((1500,34),'EP1',font=font(38,True),fill=WHITE)
    d.text((1640,42),'02 / 24',font=font(24),fill='#ccd6dc')

def footer(page):
    d=ImageDraw.Draw(page); y=H-FOOTER_H; d.rectangle((0,y,W,H),fill=INK)
    d.text((42,y+20),'EchoStory · EP1 · THE LAST NORMAL NIGHT',font=font(22),fill='#d8e0e4')
    d.text((1510,y+20),'02',font=font(23,True),fill=WHITE)

src=Image.open(SRC).convert('RGB')
p=Image.new('RGB',(W,H),INK); header(p); footer(p); d=ImageDraw.Draw(p)
ct=HEADER_H+10; cb=H-FOOTER_H-10
p1=(MARGIN,ct,W-MARGIN,ct+800)
mt=p1[3]+GAP; mh=760
p2=(MARGIN,mt,W//2-GAP//2,mt+mh)
p3=(W//2+GAP//2,mt,W-MARGIN,mt+mh)
p4=(MARGIN,mt+mh+GAP,W-MARGIN,cb)

# Clean source crops only; no storyboard/production labels are rendered.
# P1: social table scene.
art=fit(src,(p1[2]-p1[0],p1[3]-p1[1]),(0,390,590,745),(.53,.55)); p.paste(art,p1[:2]); border(d,p1)
# P2: protagonist listening with beer/friends.
art=fit(src,(p2[2]-p2[0],p2[3]-p2[1]),(0,390,590,745),(.48,.56)); p.paste(art,p2[:2]); border(d,p2)
# P3: relationship conversation close-up.
art=fit(src,(p3[2]-p3[0],p3[3]-p3[1]),(0,745,560,1120),(.54,.50)); p.paste(art,p3[:2]); border(d,p3)
# P4: warm bar / friends / laughter beat.
art=fit(src,(p4[2]-p4[0],p4[3]-p4[1]),(0,0,1015,390),(.49,.52)); p.paste(art,p4[:2]); border(d,p4)

# Canonical script lettering only.
bubble(d,620,430,'You still coming Monday or you gonna mysteriously become unavailable again?',690,25)
bubble(d,1455,620,'Depends how committed I am to disappointing everybody.',650,25)
bubble(d,335,1285,'That’s healthy.',300,25)
bubble(d,730,1455,'It’s efficient.',290,25)
bubble(d,1385,1225,'I’m telling you, she said “we need space” and then sent me twelve paragraphs.',655,23)
bubble(d,1635,1575,'That sounds like a lot of space.',510,24)
caption(d,1335,p4[3]-145,'Old friends killing borrowed time.',610,27)

out=PAGES/'p02.png'; p.save(out,'PNG',optimize=True,dpi=(300,300))
sha=hashlib.sha256(out.read_bytes()).hexdigest()
(ART/'MANUAL_P02_2026-09-16.md').write_text(
    '# EP1 Manual Page 02 Promotion\n\n'
    'Rebuilt one page at a time from the locked script. Storyboard notes and production labels are intentionally excluded from final lettering.\n\n'
    f'- Size: {W}×{H}\n- SHA-256: `{sha}`\n', encoding='utf-8')
print('manual P02 complete', sha)
