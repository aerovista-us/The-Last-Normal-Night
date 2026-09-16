from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageEnhance, ImageFilter
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
def signal_states(img,x,y):
    d=ImageDraw.Draw(img); card=(x,y,x+580,y+160)
    d.rounded_rectangle(card,radius=25,fill='#081018',outline='#dce6e8',width=3)
    starts=[x+48,x+235,x+422]; counts=[1,4,0]
    for idx,(sx,count) in enumerate(zip(starts,counts)):
        base=y+112
        for i in range(4):
            bh=18+20*i; fill='#eef4f5' if i<count else '#445058'
            d.rectangle((sx+i*22,base-bh,sx+i*22+13,base),fill=fill)
        if idx<2: d.text((sx+112,y+64),'→',font=F(26,True),fill='#9fb0b8')

mystery=Image.open(MYSTERY).convert('RGB'); noir=Image.open(NOIR).convert('RGB')
p=Image.new('RGB',(W,H),INK); header(p); footer(p); d=ImageDraw.Draw(p)
ct=HEADER_H+10; cb=H-FOOTER_H-10
h1,h2,h3=650,600,720
p1=(M,ct,W-M,ct+h1); p2=(M,p1[3]+G,W-M,p1[3]+G+h2); p3=(M,p2[3]+G,W-M,p2[3]+G+h3); p4=(M,p3[3]+G,W-M,cb)

# 05.1 — same street, lamp on, protagonist approaching.
a=fit(mystery,(p1[2]-p1[0],p1[3]-p1[1]),(0,0,1015,360),(.47,.56)); p.paste(a,p1[:2]); border(d,p1)
# 05.2 — same location in close continuity; lamp is visibly dead.
a=fit(mystery,(p2[2]-p2[0],p2[3]-p2[1]),(0,360,1015,645),(.43,.52)); a=ImageEnhance.Brightness(a).enhance(.34); a=ImageEnhance.Color(a).enhance(.72)
ov=Image.new('RGBA',a.size,(0,0,0,0)); od=ImageDraw.Draw(ov); od.ellipse((1180,-120,1770,390),fill=(2,7,11,205)); ov=ov.filter(ImageFilter.GaussianBlur(60)); a=Image.alpha_composite(a.convert('RGBA'),ov).convert('RGB'); p.paste(a,p2[:2]); border(d,p2)
d.text((1430,p2[1]+330),'TCHK',font=F(44,True),fill=WHITE,stroke_width=2,stroke_fill='#111')
# 05.3 — phone remains in his hand on the street. Crop excludes the source-board gutter.
mid=p3[0]+760
left=fit(mystery,(760,p3[3]-p3[1]),(220,1220,820,1535),(.56,.50)); p.paste(left,(p3[0],p3[1]))
right=fit(noir,(p3[2]-mid,p3[3]-p3[1]),(0,1210,1015,1548),(.64,.52)); p.paste(right,(mid,p3[1]))
d.line((mid,p3[1],mid,p3[3]),fill=WHITE,width=7); border(d,p3)
# The controlled bar strip covers the generated source time and depicts 1 → 5 → none without debug labels.
signal_states(p,p3[0]+75,p3[1]+115); bubble(d,1500,p3[1]+405,'Come on.',300,27)
# 05.4 — same ordinary street continuity, now read as empty of any possible speaker.
a=fit(mystery,(p4[2]-p4[0],p4[3]-p4[1]),(0,645,1015,905),(.42,.54)); p.paste(a,p4[:2]); border(d,p4)
whisper(d,1420,p4[1]+250,'Don’t go home.',420,26); bubble(d,470,p4[1]+390,'Hello?',250,27)

out=PAGES/'p05.png'; p.save(out,'PNG',optimize=True,dpi=(300,300)); sha=hashlib.sha256(out.read_bytes()).hexdigest()
(ART/'MANUAL_P05_2026-09-16.md').write_text(
    '# EP1 Manual Page 05 Promotion\n\n'
    'Four-panel manual rebuild from the locked script. Lamp-on/lamp-off continuity is intentional. The phone stays in the protagonist’s hand on the street; its source time and board gutter are removed beneath controlled 1-to-5-to-none signal-state artwork. The whisper panel remains ordinary pre-rupture street geography with no visible speaker. No storyboard or production-note lettering is rendered.\n\n'
    f'- Size: {W}×{H}\n- SHA-256: `{sha}`\n',encoding='utf-8')
print('manual P05 complete',sha)
