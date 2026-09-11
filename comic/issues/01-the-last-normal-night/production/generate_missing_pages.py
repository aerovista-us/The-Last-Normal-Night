from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageOps
import random

ROOT = Path(__file__).resolve().parents[4]
ISSUE = ROOT / 'comic/issues/01-the-last-normal-night'
OUT = ISSUE / 'pages'
OUT.mkdir(parents=True, exist_ok=True)
W,H = 2063,3150
BG=(14,16,20)
WHITE=(244,244,240)
INK=(20,20,24)
CAP=(240,232,210)

sources = [
 ISSUE/'2026-09-10__20-58-21__Rainy-Noir-in-Downtown-Coeur-dAlene__file_00000000706481fdb43883c8c8ec1289.png',
 ISSUE/'2026-09-10__21-01-40__Rainy-Lakeside-Mystery__file_00000000bbec81fdaa4852d0305d3a1e.png',
 ISSUE/'2026-09-10__21-02-04__Rainy-Lakeside-Nightfall__file_00000000e1ec81fda0870c76f82c5096.png',
 ISSUE/'ep1.visual-reference.png',
 ISSUE/'wp1.vis-ref.png',
 ISSUE/'pages/p07-candidate.png',
 ISSUE/'pages/p08-candidate.png',
 ISSUE/'pages/p01-concept-b.png',
]
sources=[p for p in sources if p.exists()]

try:
    FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
    BOLD='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
    f32=ImageFont.truetype(FONT,32); f38=ImageFont.truetype(BOLD,38); f46=ImageFont.truetype(BOLD,46); f58=ImageFont.truetype(BOLD,58)
except Exception:
    f32=f38=f46=f58=ImageFont.load_default()

def canvas(): return Image.new('RGB',(W,H),BG)
def art(i, size):
    p=sources[i%len(sources)]
    im=Image.open(p).convert('RGB')
    im=ImageOps.fit(im,size,method=Image.Resampling.LANCZOS)
    im=ImageEnhance.Color(im).enhance(.78)
    im=ImageEnhance.Contrast(im).enhance(1.08)
    return im

def panel(pg,box,i,dim=.0):
    x,y,w,h=box; im=art(i,(w,h))
    if dim: im=ImageEnhance.Brightness(im).enhance(1-dim)
    pg.paste(im,(x,y)); d=ImageDraw.Draw(pg); d.rectangle((x,y,x+w,y+h),outline=WHITE,width=8)

def wrap(draw,text,font,maxw):
    words=text.split(); lines=[]; cur=''
    for w in words:
        t=(cur+' '+w).strip()
        if draw.textbbox((0,0),t,font=font)[2] <= maxw: cur=t
        else:
            if cur: lines.append(cur)
            cur=w
    if cur: lines.append(cur)
    return lines

def boxtext(pg,xy,text,font=f32,maxw=720,fill=CAP,textfill=INK,pad=18):
    d=ImageDraw.Draw(pg); lines=wrap(d,text,font,maxw-pad*2)
    lh=font.size+9 if hasattr(font,'size') else 40
    w=max(d.textbbox((0,0),ln,font=font)[2] for ln in lines)+pad*2
    h=len(lines)*lh+pad*2
    x,y=xy; d.rounded_rectangle((x,y,x+w,y+h),radius=10,fill=fill,outline=INK,width=4)
    yy=y+pad
    for ln in lines: d.text((x+pad,yy),ln,font=font,fill=textfill); yy+=lh

def bubble(pg,xy,text,maxw=520): boxtext(pg,xy,text,font=f38,maxw=maxw,fill=WHITE)
def phone(pg,box,text,sub=None):
    d=ImageDraw.Draw(pg); x,y,w,h=box
    d.rounded_rectangle((x,y,x+w,y+h),radius=45,fill=(12,16,22),outline=(120,130,145),width=9)
    d.text((x+40,y+50),text,font=f46,fill=WHITE)
    if sub: d.text((x+40,y+130),sub,font=f32,fill=(190,200,210))
def sedan(pg,box):
    d=ImageDraw.Draw(pg); x,y,w,h=box
    d.rounded_rectangle((x+w*.12,y+h*.42,x+w*.88,y+h*.78),radius=36,fill=(225,225,218),outline=(30,30,30),width=9)
    d.ellipse((x+w*.22,y+h*.68,x+w*.38,y+h*.86),fill=(25,25,25)); d.ellipse((x+w*.64,y+h*.68,x+w*.80,y+h*.86),fill=(25,25,25))
    d.rectangle((x+w*.18,y+h*.52,x+w*.28,y+h*.60),fill=(180,20,15)); d.rectangle((x+w*.72,y+h*.52,x+w*.82,y+h*.60),fill=(105,20,18))
def streetlight(pg,box,on=True):
    d=ImageDraw.Draw(pg); x,y,w,h=box; cx=x+w*.72
    d.line((cx,y+h*.18,cx,y+h*.84),fill=(45,45,50),width=18)
    d.ellipse((cx-48,y+h*.12,cx+48,y+h*.23),fill=(255,224,140) if on else (55,55,60),outline=(25,25,25),width=5)
def doorway(pg,box,inside=True,lineonly=False):
    d=ImageDraw.Draw(pg); x,y,w,h=box
    if lineonly: d.line((x+w//2,y+40,x+w//2,y+h-40),fill=(245,250,255),width=22); return
    d.rectangle((x+40,y+30,x+w-40,y+h-30),outline=(245,250,255),width=24)
    if inside: d.rectangle((x+70,y+60,x+w-70,y+h-60),fill=(172,112,62))
def save(pg,n): pg.save(OUT/f'p{n:02d}.png',optimize=True)

# P01
p=canvas(); panel(p,(41,63,1980,3024),0); boxtext(p,(95,160),'September air.'); boxtext(p,(95,250),'Lake went black about an hour ago.'); boxtext(p,(95,340),'Same town. Same roads. Same people pretending tomorrow was guaranteed.',maxw=820); boxtext(p,(95,520),'Wasn’t anything special.'); boxtext(p,(95,610),'That’s what gets me.'); save(p,1)
# P02
p=canvas(); boxes=[(83,126,1897,756),(83,1008,908,851),(1073,1008,908,851),(83,1985,1897,1039)]
for i,b in enumerate(boxes): panel(p,b,i+1)
bubble(p,(150,250),'You still coming Monday or you gonna mysteriously become unavailable again?',700); bubble(p,(1130,300),'Depends how committed I am to disappointing everybody.',700)
bubble(p,(130,1110),'That’s healthy.'); bubble(p,(200,1250),'It’s efficient.'); bubble(p,(1120,1110),'I’m telling you, she said “we need space” and then sent me twelve paragraphs.',720); bubble(p,(1170,1400),'That sounds like a lot of space.',690); boxtext(p,(130,2810),'Old friends killing borrowed time.',maxw=700); save(p,2)
# P03
p=canvas(); boxes=[(83,126,1897,630),(83,882,908,788),(1073,882,908,788),(83,1796,908,1228),(1073,1796,908,1228)]
for i,b in enumerate(boxes): panel(p,b,i+2)
bubble(p,(140,220),'Text when you get home.'); bubble(p,(530,310),'Sure.'); phone(p,(220,1040,520,390),'12%','battery'); boxtext(p,(150,1510),'Phone said twelve percent.',maxw=620); boxtext(p,(120,2610),'Cool lake wind moving through the air.',maxw=720); sedan(p,(1140,2040,760,650)); save(p,3)
# P04
p=canvas(); boxes=[(83,126,1897,725),(83,977,1897,630),(83,1733,825,693),(83,2520,1897,504)]
for i,b in enumerate(boxes): panel(p,b,i+3,dim=.08 if i>0 else 0)
boxtext(p,(150,260),'WOOF. WOOF.',maxw=350,fill=WHITE); bubble(p,(170,1900),'Huh.'); boxtext(p,(145,2730),'Then everything went still.'); boxtext(p,(145,2840),'Didn’t notice then.'); save(p,4)
# P05
p=canvas(); boxes=[(83,126,1897,725),(83,977,1897,630),(83,1733,1897,630),(83,2489,1897,535)]
for i,b in enumerate(boxes): panel(p,b,i+4,dim=.13 if i==1 else 0)
streetlight(p,boxes[0],True); streetlight(p,boxes[1],False); streetlight(p,boxes[2],True); phone(p,(1250,1840,540,390),'▮▮▮▮▮ → —','signal'); bubble(p,(250,2060),'Come on.'); bubble(p,(1230,2640),'Don’t go home.',600); bubble(p,(250,2710),'Hello?'); save(p,5)
# P06
p=canvas(); boxes=[(83,126,1897,630),(83,882,908,756),(1073,882,908,756),(83,1764,908,1260),(1073,1764,908,1260)]
for i,b in enumerate(boxes): panel(p,b,i+5)
boxtext(p,(145,560),'Walked downtown but the road felt stretched.',maxw=760); sedan(p,(160,1040,760,540)); sedan(p,(1140,1040,760,540)); phone(p,(200,2100,620,420),'11:58','digital sign'); phone(p,(1190,2100,620,420),'11:57','same sign, seconds later'); bubble(p,(1180,2650),'Wait.'); save(p,6)
# P07 use approved candidate as texture, exact 4-panel lettering
p=canvas(); boxes=[(83,126,1897,756),(83,1008,908,851),(1073,1008,908,851),(83,1985,1897,1039)]
for i,b in enumerate(boxes): panel(p,b,5+i)
boxtext(p,(130,700),'Late-night convenience store. Water. Gum. Anything to break the silence.',maxw=900); bubble(p,(140,1180),'You picked a good one.',650); bubble(p,(1140,1250),'Good what?'); bubble(p,(130,2200),'Have a good night.',650); save(p,7)
# P08
p=canvas(); boxes=[(83,126,1897,693),(83,945,1897,693),(83,1764,908,1260),(1073,1764,908,1260)]
for i,b in enumerate(boxes): panel(p,b,6+i,dim=.05)
boxtext(p,(130,640),'Sherman should not be this empty.',maxw=760); boxtext(p,(130,1450),'The lake looked flat enough to be painted.',maxw=760); phone(p,(190,2100,650,560),'NO SERVICE'); phone(p,(1140,2100,690,560),'WELCOME BACK','no sender · no app'); bubble(p,(1110,2760),'What the fuck was that?',760); save(p,8)

# P19
p=canvas(); boxes=[(83,126,1897,725),(83,977,1897,630),(83,1733,908,1292),(1073,1733,908,1292)]
for i,b in enumerate(boxes): panel(p,b,i+1)
boxtext(p,(130,650),'A building where the empty lot should be. A familiar business half-collapsed.',maxw=950); phone(p,(650,1080,760,420),'20?—??','date glitches before he can read it'); bubble(p,(1500,1290),'Shit.'); boxtext(p,(130,2780),'I should’ve run.'); boxtext(p,(1120,2780),'Instead I laughed.'); bubble(p,(1270,2400),'Of course.'); save(p,19)
# P20
p=canvas(); boxes=[(62,95,1939,851),(62,1071,1939,756),(62,1953,1939,1103)]
for i,b in enumerate(boxes): panel(p,b,i+2,dim=.12)
d=ImageDraw.Draw(p); d.line((1400,220,1360,850),fill=WHITE,width=20); boxtext(p,(100,760),'KRRRNNNN',maxw=400,fill=WHITE); doorway(p,(1230,1160,560,560)); doorway(p,(1030,2100,760,780)); boxtext(p,(150,2730),'Home.',maxw=300); save(p,20)
# P21
p=canvas(); boxes=[(83,126,1897,693),(83,945,908,851),(1073,945,908,851),(83,1922,1897,1103)]
for i,b in enumerate(boxes): panel(p,b,i+3,dim=.08)
doorway(p,(1330,240,500,500)); doorway(p,(260,1100,600,560)); doorway(p,(1200,1100,620,560)); doorway(p,(1250,2100,550,760)); boxtext(p,(150,2750),'All I had to do was walk back through.',maxw=900); save(p,21)
# P22
p=canvas(); boxes=[(83,126,908,693),(1073,126,908,693),(83,945,1897,567),(83,1638,1897,567),(83,2331,1897,693)]
for i,b in enumerate(boxes): panel(p,b,i+4,dim=.08)
doorway(p,(560,250,300,460)); boxtext(p,(150,250),'One step.',maxw=280); doorway(p,(1390,240,420,480)); boxtext(p,(1120,250),'Two.',maxw=220); doorway(p,(1500,1030,300,400)); boxtext(p,(130,1750),'Fear and fascination shared the same face.',maxw=800); doorway(p,(1430,2420,360,450)); bubble(p,(1100,2690),'Nah.'); boxtext(p,(150,2910),'He steps sideways — not backward.',maxw=800); save(p,22)
# P23
p=canvas(); boxes=[(62,95,1939,851),(62,1071,1939,756),(62,1953,1939,1103)]
for i,b in enumerate(boxes): panel(p,b,i+5,dim=.05)
doorway(p,(1220,220,540,600)); doorway(p,(1250,1180,520,520),inside=False,lineonly=True); boxtext(p,(1470,1480),'TCHK',maxw=260,fill=WHITE); bubble(p,(1000,2240),'I ain’t going back.',700); boxtext(p,(120,2860),'Lake wind returned. Dawn began behind the mountains — from the wrong side.',maxw=980); save(p,23)
# P24
p=canvas(); panel(p,(41,63,1980,3024),2); phone(p,(1190,1770,590,850),'FULL','WELCOME HOME'); bubble(p,(650,1900),'Figures.'); boxtext(p,(90,2860),'END ISSUE #1',font=f46,maxw=500,fill=WHITE); save(p,24)
print('Generated:', ', '.join(str(OUT/f'p{n:02d}.png') for n in [1,2,3,4,5,6,7,8,19,20,21,22,23,24]))

# build-trigger: 2026-09-11
