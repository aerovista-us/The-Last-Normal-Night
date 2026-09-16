from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageEnhance
import hashlib

ISSUE=Path(__file__).resolve().parents[1]
PAGES=ISSUE/'pages'; ART=ISSUE/'production'/'artifacts'; ART.mkdir(parents=True,exist_ok=True)
W,H=2063,3150; HEADER_H,FOOTER_H=150,76; M,G=24,16
INK='#071018'; PAPER='#f3ead0'; WHITE='#f4f5f2'; AMBER='#ffb347'
MYSTERY=ISSUE/'2026-09-10__21-01-40__Rainy-Lakeside-Mystery__file_00000000bbec81fdaa4852d0305d3a1e.png'
NOIR=ISSUE/'2026-09-10__20-58-21__Rainy-Noir-in-Downtown-Coeur-dAlene__file_00000000706481fdb43883c8c8ec1289.png'
FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'; BOLD='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'; ITAL='/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf'

def F(s,b=False,i=False): return ImageFont.truetype(ITAL if i else (BOLD if b else FONT),s)
def fit(im,size,crop=None,cent=(.5,.5)):
    if crop: im=im.crop(crop)
    return ImageOps.fit(im.convert('RGB'),size,method=Image.Resampling.LANCZOS,centering=cent)
def border(d,b): d.rectangle(b,outline=WHITE,width=7)
def caption(d,x,y,text,w=760,fs=27):
    f=F(fs,i=True); bb=d.textbbox((0,0),text,font=f); h=bb[3]-bb[1]+32
    d.rectangle((x,y,x+w,y+h),fill=PAPER,outline='#111',width=3); d.text((x+16,y+12),text,font=f,fill='#111')
def bubble(d,cx,cy,text,w=250,fs=28):
    f=F(fs); bb=d.textbbox((0,0),text,font=f); h=76; x=cx-w//2; y=cy-h//2
    d.rounded_rectangle((x,y,x+w,y+h),radius=34,fill='white',outline='#111',width=4)
    d.text((cx-(bb[2]-bb[0])/2,cy-(bb[3]-bb[1])/2-3),text,font=f,fill='#111')
def header(p):
    d=ImageDraw.Draw(p); d.rectangle((0,0,W,HEADER_H),fill=INK)
    d.text((42,24),'EchoStory',font=F(58,True),fill=WHITE); d.text((480,40),'THE LAST NORMAL NIGHT',font=F(25),fill='#ccd6dc')
    d.text((1500,34),'EP1',font=F(38,True),fill=WHITE); d.text((1640,42),'06 / 24',font=F(24),fill='#ccd6dc')
def footer(p):
    d=ImageDraw.Draw(p); y=H-FOOTER_H; d.rectangle((0,y,W,H),fill=INK)
    d.text((42,y+20),'EchoStory · EP1 · THE LAST NORMAL NIGHT',font=F(22),fill='#d8e0e4'); d.text((1510,y+20),'06',font=F(23,True),fill=WHITE)
def sign(d,box,value):
    x0,y0,x1,y1=box; d.rounded_rectangle(box,radius=28,fill='#060a0d',outline='#48555d',width=5)
    f=F(90,True); bb=d.textbbox((0,0),value,font=f)
    d.text(((x0+x1-(bb[2]-bb[0]))/2,(y0+y1-(bb[3]-bb[1]))/2-10),value,font=f,fill=AMBER)

mystery=Image.open(MYSTERY).convert('RGB'); noir=Image.open(NOIR).convert('RGB')
p=Image.new('RGB',(W,H),INK); header(p); footer(p); d=ImageDraw.Draw(p)
ct=HEADER_H+10; cb=H-FOOTER_H-10
p1=(M,ct,W-M,ct+610)
y2=p1[3]+G; mid=W//2
p2=(M,y2,mid-G//2,y2+760); p3=(mid+G//2,y2,W-M,y2+760)
y3=p2[3]+G; p4=(M,y3,mid-G//2,cb); p5=(mid+G//2,y3,W-M,cb)

# 06.1 — recognizable Sherman axis, subtly stretched rather than fantastically altered.
a=fit(mystery,(p1[2]-p1[0],p1[3]-p1[1]),(0,0,1015,350),(.54,.54)); a=a.resize((int(a.width*1.06),a.height),Image.Resampling.LANCZOS); a=ImageOps.fit(a,(p1[2]-p1[0],p1[3]-p1[1]),Image.Resampling.LANCZOS,centering=(.52,.5)); p.paste(a,p1[:2]); border(d,p1)
caption(d,1210,p1[1]+455,'Walked downtown but the road felt stretched.',760,27)

# 06.2 / 06.3 — same sedan, same direction; second view tightens on the rear damage and tail lights.
car_crop=(0,930,1015,1170)
a=fit(mystery,(p2[2]-p2[0],p2[3]-p2[1]),car_crop,(.62,.53)); p.paste(a,p2[:2]); border(d,p2)
tight=(430,930,1015,1170)
a=fit(mystery,(p3[2]-p3[0],p3[3]-p3[1]),tight,(.62,.53)); a=ImageEnhance.Contrast(a).enhance(1.04); p.paste(a,p3[:2]); border(d,p3)

# 06.4 — ordinary downtown plate with one controlled digital sign reading 11:58.
a=fit(noir,(p4[2]-p4[0],p4[3]-p4[1]),(0,820,1015,1180),(.48,.56)); p.paste(a,p4[:2]); border(d,p4)
sign(d,(p4[0]+150,p4[1]+160,p4[2]-120,p4[1]+390),'11:58')

# 06.5 — same sign has moved backward to 11:57; protagonist is now visibly looking back.
a=fit(noir,(p5[2]-p5[0],p5[3]-p5[1]),(600,420,1015,775),(.55,.52)); p.paste(a,p5[:2]); border(d,p5)
sign(d,(p5[0]+150,p5[1]+155,p5[2]-120,p5[1]+385),'11:57')
bubble(d,p5[0]+650,p5[1]+525,'Wait.',230,28)

out=PAGES/'p06.png'; p.save(out,'PNG',optimize=True,dpi=(300,300)); sha=hashlib.sha256(out.read_bytes()).hexdigest()
(ART/'MANUAL_P06_2026-09-16.md').write_text(
    '# EP1 Manual Page 06 Promotion\n\n'
    'Five-panel rebuild from the locked script. Sherman is only subtly stretched. The same white sedan repeats from the same direction, with the second crop tightening on the rear damage and tail lights. Source-board gutters are excluded. The clock contradiction is typeset in layout as 11:58 then 11:57; 11:59 is not introduced early. No storyboard or production-note lettering is rendered.\n\n'
    f'- Size: {W}×{H}\n- SHA-256: `{sha}`\n',encoding='utf-8')
print('manual P06 complete',sha)
