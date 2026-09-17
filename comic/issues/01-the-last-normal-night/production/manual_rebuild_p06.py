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
def caption(d,x,y,text,w=700,fs=27):
    f=F(fs,i=True); bb=d.textbbox((0,0),text,font=f); h=bb[3]-bb[1]+32
    d.rectangle((x,y,x+w,y+h),fill=PAPER,outline='#111',width=3)
    d.text((x+16,y+12),text,font=f,fill='#111')
def bubble(d,cx,cy,text,w=250,fs=28):
    f=F(fs); bb=d.textbbox((0,0),text,font=f); h=76; x=cx-w//2; y=cy-h//2
    d.rounded_rectangle((x,y,x+w,y+h),radius=34,fill='white',outline='#111',width=4)
    d.text((cx-(bb[2]-bb[0])/2,cy-(bb[3]-bb[1])/2-3),text,font=f,fill='#111')
def header(p):
    d=ImageDraw.Draw(p); d.rectangle((0,0,W,HEADER_H),fill=INK)
    d.text((42,24),'EchoStory',font=F(58,True),fill=WHITE)
    d.text((480,40),'THE LAST NORMAL NIGHT',font=F(25),fill='#ccd6dc')
    d.text((1500,34),'EP1',font=F(38,True),fill=WHITE)
    d.text((1640,42),'06 / 24',font=F(24),fill='#ccd6dc')
def footer(p):
    d=ImageDraw.Draw(p); y=H-FOOTER_H; d.rectangle((0,y,W,H),fill=INK)
    d.text((42,y+20),'EchoStory · EP1 · THE LAST NORMAL NIGHT',font=F(22),fill='#d8e0e4')
    d.text((1510,y+20),'06',font=F(23,True),fill=WHITE)
def clock_plate(panel,time,subject=False):
    x0,y0,x1,y1=panel
    # grounded dark street/sign environment
    src=noir if subject else mystery
    crop=(0,1180,1015,1548) if subject else (0,645,1015,905)
    bg=fit(src,(x1-x0,y1-y0),crop,(.55,.5))
    bg=ImageEnhance.Brightness(bg).enhance(.58)
    p.paste(bg,(x0,y0)); border(d,panel)
    # controlled sign surface
    sw,sh=470,185; sx=x0+(x1-x0-sw)//2; sy=y0+120
    d.rounded_rectangle((sx,sy,sx+sw,sy+sh),radius=25,fill='#080c0f',outline='#5e6a70',width=5)
    f=F(86,True); bb=d.textbbox((0,0),time,font=f)
    d.text((sx+sw/2-(bb[2]-bb[0])/2,sy+sh/2-(bb[3]-bb[1])/2-5),time,font=f,fill='#ffb546')
    return sx,sy,sw,sh

mystery=Image.open(MYSTERY).convert('RGB'); noir=Image.open(NOIR).convert('RGB')
p=Image.new('RGB',(W,H),INK); header(p); footer(p); d=ImageDraw.Draw(p)
ct=HEADER_H+10; cb=H-FOOTER_H-10
# Five panels: top wide, two sedan beats, two time beats.
p1=(M,ct,W-M,ct+620)
mid_y=p1[3]+G
half=(W-2*M-G)//2
p2=(M,mid_y,M+half,mid_y+720)
p3=(M+half+G,mid_y,W-M,mid_y+720)
bot_y=p2[3]+G
p4=(M,bot_y,M+half,cb)
p5=(M+half+G,bot_y,W-M,cb)

# 06.1 — Sherman feels stretched, still believable.
a=fit(mystery,(p1[2]-p1[0],p1[3]-p1[1]),(0,645,1015,905),(.50,.48))
a=ImageEnhance.Contrast(a).enhance(1.03)
p.paste(a,p1[:2]); border(d,p1)
caption(d,1220,p1[3]-110,'Walked downtown but the road felt stretched.',720,27)

# 06.2 — first pass of the white sedan.
sedan_crop=(0,900,1015,1195)
a=fit(mystery,(p2[2]-p2[0],p2[3]-p2[1]),sedan_crop,(.66,.54))
p.paste(a,p2[:2]); border(d,p2)

# 06.3 — same car, same direction, visibly repeated but not copy-pasted framing.
a=fit(mystery,(p3[2]-p3[0],p3[3]-p3[1]),sedan_crop,(.50,.58))
a=ImageEnhance.Brightness(a).enhance(.92)
p.paste(a,p3[:2]); border(d,p3)

# 06.4 / 06.5 — controlled sign values only, no 11:59 yet.
clock_plate(p4,'11:58',False)
clock_plate(p5,'11:57',True)

# Put protagonist recognition only in the second time beat.
# Use a clean close crop without introducing another dialogue/narration layer.
face=fit(mystery,(390,420),(0,360,520,645),(.42,.52))
# feather by simple rectangular inset; keeps sign readable.
fx=p5[0]+35; fy=p5[3]-455
p.paste(face,(fx,fy))
d.rectangle((fx,fy,fx+390,fy+420),outline=WHITE,width=5)
bubble(d,p5[0]+690,p5[3]-250,'Wait.',220,27)

out=PAGES/'p06.png'; p.save(out,'PNG',optimize=True,dpi=(300,300))
sha=hashlib.sha256(out.read_bytes()).hexdigest()
(ART/'MANUAL_P06_2026-09-17.md').write_text(
    '# EP1 Manual Page 06 Promotion\n\n'
    'Five-panel deterministic rebuild from the locked script. Production labels are removed. '
    'The white sedan is presented twice from the same direction with distinct framing, and the controlled digital sign reverses from 11:58 to 11:57. '
    'No 11:59 appears on this page.\n\n'
    f'- Size: {W}×{H}\n- SHA-256: \`{sha}\`\n',encoding='utf-8')
print('manual P06 complete',sha)
