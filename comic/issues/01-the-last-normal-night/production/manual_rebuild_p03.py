from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps
import hashlib

ISSUE=Path(__file__).resolve().parents[1]
PAGES=ISSUE/'pages'; ART=ISSUE/'production'/'artifacts'; ART.mkdir(parents=True,exist_ok=True)
W,H=2063,3150; HEADER_H,FOOTER_H=150,76; M,G=24,16
INK='#071018'; PAPER='#f3ead0'; WHITE='#f4f5f2'
MOOSE=ISSUE/'2026-09-10__21-01-42__Moose-Mug-Rainy-Lakeside-Night__file_00000000683c82309af8f598a7113737.png'
MYSTERY=ISSUE/'2026-09-10__21-01-40__Rainy-Lakeside-Mystery__file_00000000bbec81fdaa4852d0305d3a1e.png'
RAINY=ISSUE/'2026-09-10__21-02-04__Rainy-Lakeside-Nightfall__file_00000000e1ec81fda0870c76f82c5096.png'
NOIR=ISSUE/'2026-09-10__20-58-21__Rainy-Noir-in-Downtown-Coeur-dAlene__file_00000000706481fdb43883c8c8ec1289.png'
FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'; BOLD='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'; ITAL='/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf'

def F(s,b=False,i=False): return ImageFont.truetype(ITAL if i else (BOLD if b else FONT),s)
def fit(im,size,crop=None,cent=(.5,.5)):
    if crop: im=im.crop(crop)
    return ImageOps.fit(im.convert('RGB'),size,method=Image.Resampling.LANCZOS,centering=cent)
def border(d,b): d.rectangle(b,outline=WHITE,width=7)
def wrap(d,t,f,mw):
    out=[]; cur=''
    for w in t.split():
        q=(cur+' '+w).strip()
        if d.textbbox((0,0),q,font=f)[2]<=mw: cur=q
        else:
            if cur: out.append(cur)
            cur=w
    if cur: out.append(cur)
    return out
def bubble(d,cx,cy,t,w=520,fs=27):
    f=F(fs); lines=wrap(d,t,f,w-52); lh=fs+8; h=38+lh*len(lines); x=cx-w//2; y=cy-h//2
    d.rounded_rectangle((x,y,x+w,y+h),radius=34,fill='white',outline='#111',width=4); yy=y+18
    for line in lines:
        tw=d.textbbox((0,0),line,font=f)[2]; d.text((cx-tw/2,yy),line,font=f,fill='#111'); yy+=lh
def caption(d,x,y,t,w=600,fs=27):
    f=F(fs,i=True); lines=wrap(d,t,f,w-34); lh=fs+8; h=28+lh*len(lines)
    d.rectangle((x,y,x+w,y+h),fill=PAPER,outline='#111',width=3); yy=y+12
    for line in lines: d.text((x+16,yy),line,font=f,fill='#111'); yy+=lh
def header(p):
    d=ImageDraw.Draw(p); d.rectangle((0,0,W,HEADER_H),fill=INK); d.text((42,24),'EchoStory',font=F(58,True),fill=WHITE); d.text((480,40),'THE LAST NORMAL NIGHT',font=F(25),fill='#ccd6dc'); d.text((1500,34),'EP1',font=F(38,True),fill=WHITE); d.text((1640,42),'03 / 24',font=F(24),fill='#ccd6dc')
def footer(p):
    d=ImageDraw.Draw(p); y=H-FOOTER_H; d.rectangle((0,y,W,H),fill=INK); d.text((42,y+20),'EchoStory · EP1 · THE LAST NORMAL NIGHT',font=F(22),fill='#d8e0e4'); d.text((1510,y+20),'03',font=F(23,True),fill=WHITE)

moose=Image.open(MOOSE).convert('RGB'); mystery=Image.open(MYSTERY).convert('RGB'); rainy=Image.open(RAINY).convert('RGB'); noir=Image.open(NOIR).convert('RGB')
p=Image.new('RGB',(W,H),INK); header(p); footer(p); d=ImageDraw.Draw(p); ct=HEADER_H+10; cb=H-FOOTER_H-10
p1=(M,ct,W-M,ct+630); r2=p1[3]+G; p2=(M,r2,W//2-G//2,r2+560); p3=(W//2+G//2,r2,W-M,r2+560); r3=p2[3]+G; p4=(M,r3,W-M,r3+620); p5=(M,p4[3]+G,W-M,cb)

# Five distinct authored beats from four separate source plates.
art=fit(mystery,(p1[2]-p1[0],p1[3]-p1[1]),(0,0,1015,360),(.44,.55)); p.paste(art,p1[:2]); border(d,p1)
art=fit(moose,(p2[2]-p2[0],p2[3]-p2[1]),(585,390,1015,745),(.56,.55)); p.paste(art,p2[:2]); border(d,p2)
art=fit(rainy,(p3[2]-p3[0],p3[3]-p3[1]),(0,670,1015,965),(.36,.53)); p.paste(art,p3[:2]); border(d,p3)
art=fit(noir,(p4[2]-p4[0],p4[3]-p4[1]),(0,0,1015,390),(.28,.53)); p.paste(art,p4[:2]); border(d,p4)
art=fit(noir,(p5[2]-p5[0],p5[3]-p5[1]),(0,1180,1015,1548),(.72,.53)); p.paste(art,p5[:2]); border(d,p5)

# Locked-script lettering only.
bubble(d,510,420,'Text when you get home.',430,25); bubble(d,1320,545,'Sure.',220,25)
caption(d,85,r2+420,'Phone said twelve percent.',520,26)
d.text((p3[0]+160,p3[1]+360),'WHUMM—WHUMM',font=F(42,True),fill=WHITE,stroke_width=2,stroke_fill='#111')
caption(d,1270,p4[3]-130,'Cool lake wind moving through the air.',650,26)

out=PAGES/'p03.png'; p.save(out,'PNG',optimize=True,dpi=(300,300)); sha=hashlib.sha256(out.read_bytes()).hexdigest()
(ART/'MANUAL_P03_2026-09-16.md').write_text('# EP1 Manual Page 03 Promotion\n\nFive-beat rebuild from the locked script. Uses four separate source plates; no storyboard labels are rendered.\n\n'+f'- Size: {W}×{H}\n- SHA-256: `{sha}`\n',encoding='utf-8')
print('manual P03 complete',sha)
