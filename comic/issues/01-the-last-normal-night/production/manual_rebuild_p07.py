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
def bubble(d,cx,cy,text,w=390,fs=29):
    f=F(fs); lines=text.split('\n'); widths=[]; heights=[]
    for line in lines:
        bb=d.textbbox((0,0),line,font=f); widths.append(bb[2]-bb[0]); heights.append(bb[3]-bb[1])
    h=sum(heights)+24+10*(len(lines)-1); x=cx-w//2; y=cy-h//2
    d.rounded_rectangle((x,y,x+w,y+h),radius=34,fill='white',outline='#111',width=4)
    ty=y+12
    for line,tw,th in zip(lines,widths,heights):
        d.text((cx-tw/2,ty),line,font=f,fill='#111'); ty+=th+10
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

# Candidate art is treated only as a controlled panel source. Crops exclude its production labels and extra narration.
a=fit(src,(p1[2]-p1[0],p1[3]-p1[1]),(110,95,1040,500),(.52,.52)); p.paste(a,p1[:2]); border(d,p1)
a=fit(src,(p2[2]-p2[0],p2[3]-p2[1]),(40,585,880,835),(.56,.50)); p.paste(a,p2[:2]); border(d,p2)
a=fit(src,(p3[2]-p3[0],p3[3]-p3[1]),(175,920,1040,1172),(.50,.48)); p.paste(a,p3[:2]); border(d,p3)
a=fit(src,(p4[2]-p4[0],p4[3]-p4[1]),(35,1230,850,1525),(.55,.48)); p.paste(a,p4[:2]); border(d,p4)

# Locked-script dialogue only.
bubble(d,1450,p2[1]+220,'You picked\na good one.',390,29)
bubble(d,1320,p3[1]+230,'Good what?',300,29)
bubble(d,1360,p4[1]+235,'Have a good night.',390,29)

out=PAGES/'p07.png'; p.save(out,'PNG',optimize=True,dpi=(300,300)); sha=hashlib.sha256(out.read_bytes()).hexdigest()
(ART/'MANUAL_P07_2026-09-16.md').write_text(
    '# EP1 Manual Page 07 Promotion\n\n'
    'Four-panel manual rebuild from the approved candidate art. Production panel labels and noncanonical narration are excluded by crop; only the locked-script dialogue remains. The clerk reads as familiar and relieved rather than sinister.\n\n'
    f'- Size: {W}×{H}\n- SHA-256: `{sha}`\n',encoding='utf-8')
print('manual P07 complete',sha)
