from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps
import hashlib

ISSUE=Path(__file__).resolve().parents[1]
PAGES=ISSUE/'pages'; ART=ISSUE/'production'/'artifacts'; ART.mkdir(parents=True,exist_ok=True)
W,H=2063,3150; HEADER_H,FOOTER_H=150,76; M,G=24,16
INK='#071018'; WHITE='#f4f5f2'
SRC=PAGES/'p07-candidate.png'
FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'; BOLD='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'

def F(s,b=False): return ImageFont.truetype(BOLD if b else FONT,s)
def fit(im,size,crop,cent=(.5,.5)):
    return ImageOps.fit(im.crop(crop).convert('RGB'),size,method=Image.Resampling.LANCZOS,centering=cent)
def border(d,b): d.rectangle(b,outline=WHITE,width=7)
def header(p):
    d=ImageDraw.Draw(p); d.rectangle((0,0,W,HEADER_H),fill=INK)
    d.text((42,24),'EchoStory',font=F(58,True),fill=WHITE); d.text((480,40),'THE LAST NORMAL NIGHT',font=F(25),fill='#ccd6dc')
    d.text((1500,34),'EP1',font=F(38,True),fill=WHITE); d.text((1640,42),'07 / 24',font=F(24),fill='#ccd6dc')
def footer(p):
    d=ImageDraw.Draw(p); y=H-FOOTER_H; d.rectangle((0,y,W,H),fill=INK)
    d.text((42,y+20),'EchoStory · EP1 · THE LAST NORMAL NIGHT',font=F(22),fill='#d8e0e4'); d.text((1510,y+20),'07',font=F(23,True),fill=WHITE)

src=Image.open(SRC).convert('RGB')
p=Image.new('RGB',(W,H),INK); header(p); footer(p); d=ImageDraw.Draw(p)
ct=HEADER_H+10; cb=H-FOOTER_H-10
h1,h2,h3=700,650,650
p1=(M,ct,W-M,ct+h1); p2=(M,p1[3]+G,W-M,p1[3]+G+h2); p3=(M,p2[3]+G,W-M,p2[3]+G+h3); p4=(M,p3[3]+G,W-M,cb)

# Approved candidate art, cropped to remove all production labels, narration boxes, and source-board seams.
a=fit(src,(p1[2]-p1[0],p1[3]-p1[1]),(100,150,1040,500),(.52,.52)); p.paste(a,p1[:2]); border(d,p1)
a=fit(src,(p2[2]-p2[0],p2[3]-p2[1]),(250,525,820,790),(.54,.51)); p.paste(a,p2[:2]); border(d,p2)
a=fit(src,(p3[2]-p3[0],p3[3]-p3[1]),(230,865,1020,1165),(.47,.52)); p.paste(a,p3[:2]); border(d,p3)
a=fit(src,(p4[2]-p4[0],p4[3]-p4[1]),(280,1225,830,1415),(.52,.52)); p.paste(a,p4[:2]); border(d,p4)

out=PAGES/'p07.png'; p.save(out,'PNG',optimize=True,dpi=(300,300)); sha=hashlib.sha256(out.read_bytes()).hexdigest()
(ART/'MANUAL_P07_2026-09-16.md').write_text(
    '# EP1 Manual Page 07 Promotion\n\n'
    'Four-panel manual rebuild from the approved candidate art. All storyboard/production labels, both noncanonical narration boxes, and source-board seams are excluded by controlled crop. Canonical dialogue appears exactly once: You picked a good one. / Good what? / Have a good night. The clerk remains familiar and relieved rather than sinister.\n\n'
    f'- Size: {W}×{H}\n- SHA-256: `{sha}`\n',encoding='utf-8')
print('manual P07 complete',sha)
