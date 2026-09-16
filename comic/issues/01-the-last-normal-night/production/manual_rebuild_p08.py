from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps
import hashlib

ISSUE=Path(__file__).resolve().parents[1]
PAGES=ISSUE/'pages'; ART=ISSUE/'production'/'artifacts'; ART.mkdir(parents=True,exist_ok=True)
W,H=2063,3150; HEADER_H,FOOTER_H=150,76; M,G=24,16
INK='#071018'; WHITE='#f4f5f2'
SRC=PAGES/'p08-candidate.png'
FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'; BOLD='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'

def F(s,b=False): return ImageFont.truetype(BOLD if b else FONT,s)
def fit(im,size,crop,cent=(.5,.5)):
    return ImageOps.fit(im.crop(crop).convert('RGB'),size,method=Image.Resampling.LANCZOS,centering=cent)
def border(d,b): d.rectangle(b,outline=WHITE,width=7)
def header(p):
    d=ImageDraw.Draw(p); d.rectangle((0,0,W,HEADER_H),fill=INK)
    d.text((42,24),'EchoStory',font=F(58,True),fill=WHITE); d.text((480,40),'THE LAST NORMAL NIGHT',font=F(25),fill='#ccd6dc')
    d.text((1500,34),'EP1',font=F(38,True),fill=WHITE); d.text((1640,42),'08 / 24',font=F(24),fill='#ccd6dc')
def footer(p):
    d=ImageDraw.Draw(p); y=H-FOOTER_H; d.rectangle((0,y,W,H),fill=INK)
    d.text((42,y+20),'EchoStory · EP1 · THE LAST NORMAL NIGHT',font=F(22),fill='#d8e0e4'); d.text((1510,y+20),'08',font=F(23,True),fill=WHITE)

src=Image.open(SRC).convert('RGB')
# Candidate phone art contains a generated 10:47. Mask it on the source plate before any crop/scale.
sd=ImageDraw.Draw(src)
sd.polygon([(126,1046),(177,1040),(182,1075),(132,1082)],fill='#071018')
sd.polygon([(620,1046),(675,1040),(680,1075),(625,1082)],fill='#071018')

p=Image.new('RGB',(W,H),INK); header(p); footer(p); d=ImageDraw.Draw(p)
ct=HEADER_H+10; cb=H-FOOTER_H-10
h1,h2=700,650
p1=(M,ct,W-M,ct+h1); p2=(M,p1[3]+G,W-M,p1[3]+G+h2)
y3=p2[3]+G; mid=W//2; p3=(M,y3,mid-G//2,cb); p4=(mid+G//2,y3,W-M,cb)

# 08.1 — lit storefronts and lamps, but Sherman has emptied out.
a=fit(src,(p1[2]-p1[0],p1[3]-p1[1]),(0,145,1015,555),(.52,.52)); p.paste(a,p1[:2]); border(d,p1)
# 08.2 — the lake is impossibly flat, with no fantasy glow or altered shoreline.
a=fit(src,(p2[2]-p2[0],p2[3]-p2[1]),(0,635,1015,945),(.50,.52)); p.paste(a,p2[:2]); border(d,p2)
# 08.3 / 08.4 — controlled phone close-ups retain the canonical NO SERVICE / WELCOME BACK flash and dialogue, while the noncanonical source clock is removed.
a=fit(src,(p3[2]-p3[0],p3[3]-p3[1]),(0,1020,500,1475),(.52,.50)); p.paste(a,p3[:2]); border(d,p3)
a=fit(src,(p4[2]-p4[0],p4[3]-p4[1]),(510,1020,1015,1475),(.50,.50)); p.paste(a,p4[:2]); border(d,p4)

out=PAGES/'p08.png'; p.save(out,'PNG',optimize=True,dpi=(300,300)); sha=hashlib.sha256(out.read_bytes()).hexdigest()
(ART/'MANUAL_P08_2026-09-16.md').write_text(
    '# EP1 Manual Page 08 Promotion\n\n'
    'Four-panel rebuild from the approved candidate art. All production labels are excluded by crop. The generated 10:47 phone time is masked before scaling; the canonical NO SERVICE, transient WELCOME BACK, and What the fuck was that? beats are preserved exactly once. No premature 11:59 appears.\n\n'
    f'- Size: {W}×{H}\n- SHA-256: `{sha}`\n',encoding='utf-8')
print('manual P08 complete',sha)
