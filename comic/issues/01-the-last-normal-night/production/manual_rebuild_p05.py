from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageEnhance, ImageFilter
import hashlib

ISSUE=Path(__file__).resolve().parents[1]
PAGES=ISSUE/'pages'; ART=ISSUE/'production'/'artifacts'; ART.mkdir(parents=True,exist_ok=True)
W,H=2063,3150; HEADER_H,FOOTER_H=150,76; M,G=24,16
INK='#071018'; PAPER='#f3ead0'; WHITE='#f4f5f2'
MYSTERY=ISSUE/'2026-09-10__21-01-40__Rainy-Lakeside-Mystery__file_00000000bbec81fdaa4852d0305d3a1e.png'
MOOSE=ISSUE/'2026-09-10__21-01-42__Moose-Mug-Rainy-Lakeside-Night__file_00000000683c82309af8f598a7113737.png'
NOIR=ISSUE/'2026-09-10__20-58-21__Rainy-Noir-in-Downtown-Coeur-dAlene__file_00000000706481fdb43883c8c8ec1289.png'
UNCANNY=ISSUE/'2026-09-10__19-32-34__Uncanny-Moonlit-Lakeside-Town__file_00000000509c81f78c8b2d089f59c42c.png'
FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'; BOLD='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'; ITAL='/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf'

def F(s,b=False,i=False): return ImageFont.truetype(ITAL if i else (BOLD if b else FONT),s)
def fit(im,size,crop=None,cent=(.5,.5)):
    if crop: im=im.crop(crop)
    return ImageOps.fit(im.convert('RGB'),size,method=Image.Resampling.LANCZOS,centering=cent)
def border(d,b): d.rectangle(b,outline=WHITE,width=7)
def bubble(d,cx,cy,text,w=330,fs=28,outline='#111'):
    f=F(fs); bb=d.textbbox((0,0),text,font=f); h=78; x=cx-w//2; y=cy-h//2
    d.rounded_rectangle((x,y,x+w,y+h),radius=34,fill='white',outline=outline,width=4)
    d.text((cx-(bb[2]-bb[0])/2,cy-(bb[3]-bb[1])/2-3),text,font=f,fill='#111')
def whisper(d,cx,cy,text,w=360,fs=26):
    f=F(fs,i=True); bb=d.textbbox((0,0),text,font=f); h=70; x=cx-w//2; y=cy-h//2
    d.rounded_rectangle((x,y,x+w,y+h),radius=30,fill=(242,242,236),outline='#555',width=2)
    d.text((cx-(bb[2]-bb[0])/2,cy-(bb[3]-bb[1])/2-2),text,font=f,fill='#222')
def header(p):
    d=ImageDraw.Draw(p); d.rectangle((0,0,W,HEADER_H),fill=INK); d.text((42,24),'EchoStory',font=F(58,True),fill=WHITE); d.text((480,40),'THE LAST NORMAL NIGHT',font=F(25),fill='#ccd6dc'); d.text((1500,34),'EP1',font=F(38,True),fill=WHITE); d.text((1640,42),'05 / 24',font=F(24),fill='#ccd6dc')
def footer(p):
    d=ImageDraw.Draw(p); y=H-FOOTER_H; d.rectangle((0,y,W,H),fill=INK); d.text((42,y+20),'EchoStory · EP1 · THE LAST NORMAL NIGHT',font=F(22),fill='#d8e0e4'); d.text((1510,y+20),'05',font=F(23,True),fill=WHITE)
def signal_box(img,box):
    d=ImageDraw.Draw(img); x0,y0,x1,y1=box
    d.rounded_rectangle(box,radius=24,fill='#081018',outline='#dce6e8',width=3)
    d.text((x0+22,y0+18),'SIGNAL',font=F(22,True),fill='#e7eef0')
    base=y1-34; cols=[('1',1),('5',4),('NONE',0)]
    x=x0+35
    for label,n in cols:
        for i in range(4):
            h=12+18*i; xx=x+i*18
            fill='#eef4f5' if i<n else '#39434a'
            d.rectangle((xx,base-h,xx+10,base),fill=fill)
        d.text((x-2,base+7),label,font=F(16,True),fill='#c9d3d8')
        x+=112
        if label!='NONE': d.text((x-24,base-15),'→',font=F(20,True),fill='#9fb0b8')

mystery=Image.open(MYSTERY).convert('RGB'); moose=Image.open(MOOSE).convert('RGB'); noir=Image.open(NOIR).convert('RGB'); uncanny=Image.open(UNCANNY).convert('RGB')
p=Image.new('RGB',(W,H),INK); header(p); footer(p); d=ImageDraw.Draw(p)
ct=HEADER_H+10; cb=H-FOOTER_H-10
h1,h2,h3=650,600,720
p1=(M,ct,W-M,ct+h1); p2=(M,p1[3]+G,W-M,p1[3]+G+h2); p3=(M,p2[3]+G,W-M,p2[3]+G+h3); p4=(M,p3[3]+G,W-M,cb)

# 05.1 — same street, lamp on, protagonist approaching.
a=fit(mystery,(p1[2]-p1[0],p1[3]-p1[1]),(0,0,1015,360),(.47,.56)); p.paste(a,p1[:2]); border(d,p1)
# 05.2 — close continuity shot, deliberately cooled and darkened to make the lamp failure readable.
a=fit(mystery,(p2[2]-p2[0],p2[3]-p2[1]),(0,360,1015,645),(.43,.52)); a=ImageEnhance.Brightness(a).enhance(.34); a=ImageEnhance.Color(a).enhance(.72)
ov=Image.new('RGBA',a.size,(0,0,0,0)); od=ImageDraw.Draw(ov); od.ellipse((1180,-120,1770,390),fill=(2,7,11,205)); ov=ov.filter(ImageFilter.GaussianBlur(60)); a=Image.alpha_composite(a.convert('RGBA'),ov).convert('RGB'); p.paste(a,p2[:2]); border(d,p2)
d.text((1430,p2[1]+330),'TCHK',font=F(44,True),fill=WHITE,stroke_width=2,stroke_fill='#111')
# 05.3 — distinct phone/table source paired with a different over-shoulder street plate.
mid=(p3[0]+720)
left=fit(moose,(720,p3[3]-p3[1]),(585,390,1015,745),(.54,.56)); p.paste(left,(p3[0],p3[1]))
right=fit(noir,(p3[2]-mid,p3[3]-p3[1]),(0,1210,1015,1548),(.64,.52)); p.paste(right,(mid,p3[1]))
d.line((mid,p3[1],mid,p3[3]),fill=WHITE,width=7); border(d,p3)
signal_box(p,(p3[0]+70,p3[1]+350,p3[0]+620,p3[1]+610)); bubble(d,1500,p3[1]+405,'Come on.',300,27)
# 05.4 — clean, empty-city plate with a feathered over-shoulder foreground from the protagonist continuity source.
bg=fit(uncanny,(p4[2]-p4[0],p4[3]-p4[1]),None,(.48,.62)).convert('RGBA')
fg=fit(mystery,(620,p4[3]-p4[1]),(0,645,310,905),(.10,.58)).convert('RGBA')
mask=Image.new('L',fg.size,255); md=ImageDraw.Draw(mask); md.rectangle((500,0,620,fg.size[1]),fill=0); mask=mask.filter(ImageFilter.GaussianBlur(45)); fg.putalpha(mask); bg.alpha_composite(fg,(0,0))
p.paste(bg.convert('RGB'),p4[:2]); border(d,p4)
whisper(d,1420,p4[1]+250,'Don’t go home.',420,26); bubble(d,470,p4[1]+390,'Hello?',250,27)

out=PAGES/'p05.png'; p.save(out,'PNG',optimize=True,dpi=(300,300)); sha=hashlib.sha256(out.read_bytes()).hexdigest()
(ART/'MANUAL_P05_2026-09-16.md').write_text(
    '# EP1 Manual Page 05 Promotion\n\n'
    'Four-panel manual rebuild from the locked script. The lamp-on/lamp-off sequence preserves location continuity, while the signal and whisper beats deliberately switch source plates to avoid accidental visual repetition. No storyboard or production-note lettering is rendered.\n\n'
    f'- Size: {W}×{H}\n- SHA-256: `{sha}`\n',encoding='utf-8')
print('manual P05 complete',sha)
