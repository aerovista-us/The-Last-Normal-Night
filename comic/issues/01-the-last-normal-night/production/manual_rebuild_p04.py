from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageEnhance
import hashlib

ISSUE=Path(__file__).resolve().parents[1]
PAGES=ISSUE/'pages'; ART=ISSUE/'production'/'artifacts'; ART.mkdir(parents=True,exist_ok=True)
W,H=2063,3150; HEADER_H,FOOTER_H=150,76; M,G=24,16
INK='#071018'; PAPER='#f3ead0'; WHITE='#f4f5f2'
MYSTERY=ISSUE/'2026-09-10__21-01-40__Rainy-Lakeside-Mystery__file_00000000bbec81fdaa4852d0305d3a1e.png'
NOIR=ISSUE/'2026-09-10__20-58-21__Rainy-Noir-in-Downtown-Coeur-dAlene__file_00000000706481fdb43883c8c8ec1289.png'
FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'; BOLD='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'; ITAL='/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf'

def F(s,b=False,i=False): return ImageFont.truetype(ITAL if i else (BOLD if b else FONT),s)
def fit(im,size,crop=None,cent=(.5,.5)):
    if crop: im=im.crop(crop)
    return ImageOps.fit(im.convert('RGB'),size,method=Image.Resampling.LANCZOS,centering=cent)
def border(d,b): d.rectangle(b,outline=WHITE,width=7)
def bubble(d,cx,cy,text,w=250,fs=28):
    f=F(fs); bb=d.textbbox((0,0),text,font=f); h=72; x=cx-w//2; y=cy-h//2
    d.rounded_rectangle((x,y,x+w,y+h),radius=34,fill='white',outline='#111',width=4)
    d.text((cx-(bb[2]-bb[0])/2,cy-(bb[3]-bb[1])/2-3),text,font=f,fill='#111')
def caption(d,x,y,text,w=620,fs=27):
    f=F(fs,i=True); bb=d.textbbox((0,0),text,font=f); h=bb[3]-bb[1]+30
    d.rectangle((x,y,x+w,y+h),fill=PAPER,outline='#111',width=3); d.text((x+16,y+12),text,font=f,fill='#111')
def header(p):
    d=ImageDraw.Draw(p); d.rectangle((0,0,W,HEADER_H),fill=INK); d.text((42,24),'EchoStory',font=F(58,True),fill=WHITE); d.text((480,40),'THE LAST NORMAL NIGHT',font=F(25),fill='#ccd6dc'); d.text((1500,34),'EP1',font=F(38,True),fill=WHITE); d.text((1640,42),'04 / 24',font=F(24),fill='#ccd6dc')
def footer(p):
    d=ImageDraw.Draw(p); y=H-FOOTER_H; d.rectangle((0,y,W,H),fill=INK); d.text((42,y+20),'EchoStory · EP1 · THE LAST NORMAL NIGHT',font=F(22),fill='#d8e0e4'); d.text((1510,y+20),'04',font=F(23,True),fill=WHITE)

mystery=Image.open(MYSTERY).convert('RGB'); noir=Image.open(NOIR).convert('RGB')
p=Image.new('RGB',(W,H),INK); header(p); footer(p); d=ImageDraw.Draw(p); ct=HEADER_H+10; cb=H-FOOTER_H-10
# Four horizontal beats. Panels 1 and 2 deliberately repeat the exact framing.
h=660; p1=(M,ct,W-M,ct+h); p2=(M,p1[3]+G,W-M,p1[3]+G+h); p3=(M,p2[3]+G,W-M,p2[3]+G+610); p4=(M,p3[3]+G,W-M,cb)

walk=fit(mystery,(p1[2]-p1[0],p1[3]-p1[1]),(0,0,1015,360),(.45,.58))
p.paste(walk,p1[:2]); border(d,p1)
# Intentional exact repeated composition: the silence is the change.
p.paste(walk,p2[:2]); border(d,p2)
close=fit(mystery,(p3[2]-p3[0],p3[3]-p3[1]),(0,360,1015,645),(.36,.55)); p.paste(close,p3[:2]); border(d,p3)
empty=fit(noir,(p4[2]-p4[0],p4[3]-p4[1]),(0,1180,1015,1548),(.36,.52)); empty=ImageEnhance.Brightness(empty).enhance(.80); p.paste(empty,p4[:2]); border(d,p4)

# Locked-script lettering only. No panel labels or production directions.
d.text((1510,540),'WOOF. WOOF.',font=F(42,True),fill=WHITE,stroke_width=2,stroke_fill='#111')
bubble(d,1490,p3[1]+300,'Huh.',230,28)
caption(d,1230,p4[3]-190,'Then everything went still.',690,27)
caption(d,1330,p4[3]-105,'Didn’t notice then.',520,27)

out=PAGES/'p04.png'; p.save(out,'PNG',optimize=True,dpi=(300,300)); sha=hashlib.sha256(out.read_bytes()).hexdigest()
(ART/'MANUAL_P04_2026-09-16.md').write_text(
    '# EP1 Manual Page 04 Promotion\n\n'
    'Four-beat rebuild from the locked script. Panels 1 and 2 intentionally reuse the exact framing because the script calls for the same shot one beat later; this is documented repetition, not accidental source reuse. No storyboard labels are rendered.\n\n'
    f'- Size: {W}×{H}\n- SHA-256: `{sha}`\n',encoding='utf-8')
print('manual P04 complete',sha)
