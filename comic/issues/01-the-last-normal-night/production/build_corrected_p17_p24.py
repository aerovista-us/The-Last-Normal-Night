from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageEnhance, ImageFilter, ImageChops
from urllib.request import urlopen
from io import BytesIO
import hashlib, json, math

ISSUE = Path(__file__).resolve().parents[1]
PAGES = ISSUE / 'pages'
ART = ISSUE / 'production' / 'artifacts'
ART.mkdir(parents=True, exist_ok=True)
W,H = 2063,3150
INK='#0a0d10'; PAPER='#f3f0e8'; WHITE='#ffffff'; CREAM='#f4e9cf'; COLD='#d9f2ff'; WARM='#f2b873'
FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
FONT_B='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
NOIR=ISSUE/'2026-09-10__20-58-21__Rainy-Noir-in-Downtown-Coeur-dAlene__file_00000000706481fdb43883c8c8ec1289.png'
RAINY=ISSUE/'2026-09-10__21-02-04__Rainy-Lakeside-Nightfall__file_00000000e1ec81fda0870c76f82c5096.png'
BAR=ISSUE/'2026-09-10__21-01-42__Moose-Mug-Rainy-Lakeside-Night__file_00000000683c82309af8f598a7113737.png'
LAKE=ISSUE/'2026-09-10__19-30-37__Moonlit-Lakeside-Town-Reflections__file_00000000a43c8230a403848b7670b888.png'
OFF=ISSUE/'cda.off.streets.png'
BASE='953e9f9964599e21212dfbdca0024a85358b9e58'
RAW='https://raw.githubusercontent.com/aerovista-us/The-Last-Normal-Night/'+BASE+'/comic/issues/01-the-last-normal-night/pages/'

font=lambda s,b=False: ImageFont.truetype(FONT_B if b else FONT,s)
def fetch_baseline(name):
    with urlopen(RAW+name,timeout=90) as r: return Image.open(BytesIO(r.read())).convert('RGB')
def fit(im,size,cent=(.5,.5)):
    return ImageOps.fit(im.convert('RGB'), size, method=Image.Resampling.LANCZOS, centering=cent)
def panel(page,src,box,cent=(.5,.5),bright=1.0,warm=0.0,cold=0.0):
    x1,y1,x2,y2=box; art=fit(src,(x2-x1,y2-y1),cent)
    if bright!=1: art=ImageEnhance.Brightness(art).enhance(bright)
    if warm:
        ov=Image.new('RGB',art.size,(255,143,72)); art=Image.blend(art,ov,warm)
    if cold:
        ov=Image.new('RGB',art.size,(75,125,160)); art=Image.blend(art,ov,cold)
    page.paste(art,(x1,y1)); ImageDraw.Draw(page).rectangle(box,outline=INK,width=8)
def txt(d,xy,s,size=42,b=False,fill=WHITE,stroke=2,anchor=None):
    d.text(xy,s,font=font(size,b),fill=fill,stroke_width=stroke,stroke_fill=INK,anchor=anchor)
def caption(d,box,s,size=34):
    d.rounded_rectangle(box,12,fill=(240,235,215),outline=INK,width=4)
    txt(d,(box[0]+18,box[1]+14),s,size,b=False,fill=INK,stroke=0)
def bubble(d,box,s,size=36):
    d.ellipse(box,fill='white',outline=INK,width=5); bb=d.textbbox((0,0),s,font=font(size,True));
    x=(box[0]+box[2]-bb[2])/2; y=(box[1]+box[3]-bb[3])/2-4; d.text((x,y),s,font=font(size,True),fill=INK)
def footer(page,n):
    d=ImageDraw.Draw(page); d.rectangle((0,H-58,W,H),fill='#f8f6ef'); txt(d,(W//2,H-38),str(n),24,fill=INK,stroke=0,anchor='mm')
def doorway(page,box,inside,glow=18,alpha=1.0):
    x1,y1,x2,y2=box; art=fit(inside,(x2-x1,y2-y1),(.5,.5)); art=ImageEnhance.Color(art).enhance(1.12); art=ImageEnhance.Brightness(art).enhance(1.18)
    page.paste(art,(x1,y1)); d=ImageDraw.Draw(page)
    for i in range(glow,0,-2):
        col=(205,235,255,max(18,90-i*2));
        overlay=Image.new('RGBA',page.size,(0,0,0,0)); od=ImageDraw.Draw(overlay); od.rectangle((x1-i,y1-i,x2+i,y2+i),outline=col,width=max(2,i//3)); page.paste(overlay,(0,0),overlay)
    d.rectangle(box,outline='#eaf8ff',width=10)
def save(page,n):
    footer(page,n); p=PAGES/f'p{n:02d}.png'; page.save(p,'PNG',optimize=True,dpi=(300,300)); return p

def crop_band(im,y1,y2): return im.crop((0,int(im.height*y1),im.width,int(im.height*y2)))
noir=Image.open(NOIR).convert('RGB'); rainy=Image.open(RAINY).convert('RGB'); bar=Image.open(BAR).convert('RGB'); lake=Image.open(LAKE).convert('RGB'); off=Image.open(OFF).convert('RGB'); old17=fetch_baseline('p17.png'); old18=fetch_baseline('p18.png')
oldworld=bar.crop((0,0,1015,390))

# P17 — 4 beats: watchers / self-start / key still out / 03
p=Image.new('RGB',(W,H),PAPER); d=ImageDraw.Draw(p)
panel(p,old17.crop((20,15,1015,1110)),(22,22,1017,1080),(.5,.5),.90)
panel(p,rainy.crop((0,610,1015,1005)),(1034,22,2041,1080),(.48,.5),.86)
# Preserve the real hand/key from the baseline, but replace the wrong vehicle grille with the canonical Ford.
mid=fit(old17.crop((20,1120,2040,2130)),(2019,1047),(.5,.5)); p.paste(mid,(22,1098))
ford=fit(rainy.crop((0,610,1015,1005)),(960,1047),(.40,.5)); mask=Image.new('L',(960,1047),0); md=ImageDraw.Draw(mask)
for x in range(960): md.line((x,0,x,1047),fill=max(0,min(255,int((x-60)/280*255))))
p.paste(ford,(1081,1098),mask)
d.rectangle((22,1098,2041,2145),outline=INK,width=8)
# Cover only the Toyota emblem on the key fob; preserve the photographed hand and metal key.
d.ellipse((760,1810,850,1900),fill='#15171a',outline='#5d6166',width=3)
caption(d,(80,1960,690,2060),'Key still in his hand.',30)
panel(p,old17.crop((22,2160,2040,3010)),(22,2163,2041,3072),(.5,.55),.84)
txt(d,(1190,875),'RRRRMM',54,True); bubble(d,(1120,930,1425,1055),'No.',34); txt(d,(105,2860),'KSSSSHHH',42,True)
save(p,17)

# P18 — exact 5 beats from immutable baseline, plus the scripted 03-then-dark beat.
p=Image.new('RGB',(W,H),PAPER); d=ImageDraw.Draw(p)
boxes=[(22,22,1017,890),(1034,22,2041,890),(22,908,2041,1695),(22,1713,2041,2380),(22,2398,2041,3072)]
src=[old18.crop((20,15,1015,965)), old18.crop((1025,15,2040,965)), old18.crop((20,985,2040,1905)), old18.crop((20,1900,2040,3000)), old17.crop((50,2160,2010,3010))]
for s0,b0 in zip(src,boxes): panel(p,s0,b0,(.5,.5),.90)
# Fifth beat: display holds 03 for one beat, then the right side dies.
d.rectangle((1390,2430,2015,3035),fill='#050607'); txt(d,(1250,2520),'03',84,True,fill='#bfead4',stroke=1); txt(d,(1690,2770),'—',84,True,fill='#2a2d30',stroke=0)
save(p,18)

# P19 — curiosity wins
p=Image.new('RGB',(W,H),PAPER); d=ImageDraw.Draw(p)
panel(p,off,(22,22,2041,870),(.5,.50),.90,cold=.08)
panel(p,rainy.crop((0,0,1015,310)),(22,888,1008,1715),(.45,.50),.82,cold=.08)
panel(p,noir.crop((505,390,1015,760)),(1026,888,2041,1715),(.5,.52),.88)
panel(p,noir.crop((0,390,1015,760)),(22,1733,2041,3072),(.67,.5),.90,cold=.05)
# unreadable date field / story lettering
caption(d,(1250,1030,1920,1150),'20?—??',36); bubble(d,(650,1330,955,1470),'Shit.',34); bubble(d,(1390,2340,1835,2505),'Of course.',34)
caption(d,(90,2770,700,2870),"I should’ve run.",30); caption(d,(90,2890,680,2990),'Instead I laughed.',30)
save(p,19)

# P20 — doorway opens, 3 panels
p=Image.new('RGB',(W,H),INK); d=ImageDraw.Draw(p)
panel(p,off,(0,0,W,905),(.50,.52),.78,cold=.12); txt(d,(1320,730),'KRRRNNNN',44,True)
# thin tear
for x in range(1510,1520,2): d.line((x,170,x+2,760),fill='#e7fbff',width=2)
panel(p,off,(0,923,W,1770),(.50,.50),.72,cold=.16); doorway(p,(1350,1020,1710,1680),oldworld)
panel(p,off,(0,1788,W,3150),(.5,.52),.70,cold=.18); doorway(p,(960,1900,1885,3000),oldworld)
caption(d,(120,2860,470,2970),'Home.',42)
save(p,20)

# P21 — temptation, 4 panels
p=Image.new('RGB',(W,H),PAPER); d=ImageDraw.Draw(p)
# altered CDA behind, warm threshold advancing
panel(p,noir.crop((0,380,1015,860)),(22,22,2041,900),(.5,.62),.82,cold=.10); doorway(p,(1260,90,1870,825),oldworld)
panel(p,bar.crop((0,300,1015,810)),(22,918,1008,1800),(.35,.48),1.0,warm=.05)
panel(p,rainy.crop((0,610,1015,1000)),(1026,918,2041,1800),(.45,.5),.95,warm=.04)
panel(p,off,(22,1818,2041,3072),(.5,.54),.72,cold=.12); doorway(p,(900,1895,1880,2970),oldworld)
caption(d,(95,2790,960,2920),'All I had to do was walk back through.',30)
save(p,21)

# P22 — defining choice, 5 panels
p=Image.new('RGB',(W,H),PAPER); d=ImageDraw.Draw(p)
# 1 step
panel(p,noir.crop((0,770,1015,1230)),(22,22,1008,950),(.56,.5),.78,cold=.08); doorway(p,(500,130,930,860),oldworld); caption(d,(80,750,390,850),'One step.',28)
# 2 steps, warm world dominant
panel(p,oldworld,(1026,22,2041,950),(.5,.52),.98,warm=.05); d.rectangle((1050,60,2015,925),outline='#eaf8ff',width=10); caption(d,(1100,750,1370,850),'Two.',28)
# boots stop at threshold: abstract grounded close-up from protagonist lower body
panel(p,noir.crop((0,760,1015,1230)),(22,968,2041,1530),(.50,.86),.72,cold=.06); d.line((1030,1000,1030,1490),fill='#eefaff',width=12)
# look toward altered CDA
panel(p,off,(22,1548,1008,2360),(.55,.52),.73,cold=.18)
panel(p,noir.crop((490,380,1015,780)),(1026,1548,2041,2360),(.52,.52),.90,cold=.05)
# sideways choice
panel(p,off,(22,2378,2041,3072),(.5,.54),.68,cold=.12); doorway(p,(1320,2420,1885,2990),oldworld); bubble(d,(960,2670,1245,2820),'Nah.',36)
save(p,22)

# P23 — collapse and wrong dawn begins
p=Image.new('RGB',(W,H),PAPER); d=ImageDraw.Draw(p)
panel(p,off,(0,0,W,920),(.5,.52),.72,cold=.12); doorway(p,(1130,100,1760,850),oldworld); # shiver lines
for dx in (-18,-9,9,18): d.rectangle((1130+dx,100,1760+dx,850),outline=(210,235,245),width=2)
panel(p,off,(0,938,W,1760),(.5,.52),.66,cold=.18); d.line((1440,1050,1440,1640),fill='#f2fbff',width=10); txt(d,(1510,1510),'TCHK',38,True)
# bottom dawn: cold altered CDA with wrong warm edge at left
base=fit(lake,(W,1390),(.5,.58)); dawn=Image.new('RGB',base.size,(78,110,135)); base=Image.blend(base,dawn,.18)
# wrong-side dawn as a soft horizontal wash, never a rectangular block
ov=Image.new('RGBA',base.size,(0,0,0,0)); od=ImageDraw.Draw(ov)
for x in range(0,900,6):
    a=max(0,70-int(x/13)); od.rectangle((x,0,x+6,1390),fill=(238,137,85,a))
base=Image.alpha_composite(base.convert('RGBA'),ov).convert('RGB')
p.paste(base,(0,1760)); d.rectangle((0,1760,W,3150),outline=INK,width=8)
# small grounded protagonist/truck cue
truck=fit(noir.crop((0,0,1015,390)),(700,300),(.30,.5)); p.paste(truck,(80,2730)); bubble(d,(980,2740,1850,2920),"I ain’t going back.",34)
save(p,23)

# P24 — wrong-side morning / WELCOME HOME full splash
bg=fit(off,(W,H),(.52,.5)); bg=ImageEnhance.Brightness(bg).enhance(.93); bg=ImageEnhance.Color(bg).enhance(.72)
# cold dawn wash with impossible warm light from left
wash=Image.new('RGBA',(W,H),(74,125,155,45)); bg=Image.alpha_composite(bg.convert('RGBA'),wash)
grad=Image.new('RGBA',(W,H),(0,0,0,0)); gd=ImageDraw.Draw(grad)
for x in range(0,900,8):
    a=max(0,100-int(x/9)); gd.rectangle((x,0,x+8,H),fill=(250,152,96,a))
bg=Image.alpha_composite(bg,grad).convert('RGB'); p=bg; d=ImageDraw.Draw(p)
# fading moon halo opposite dawn
mx,my=1845,250
for r,a in [(120,45),(90,65),(58,100)]: d.ellipse((mx-r,my-r,mx+r,my+r),outline=(225,236,240),width=3)
# small truck/protagonist in foreground, not dominant
truck=fit(rainy.crop((0,610,1015,1000)),(760,360),(.48,.52)); truck=ImageEnhance.Brightness(truck).enhance(.74)
# feather truck into foreground so the splash stays one composition rather than adding a second panel
mask=Image.new('L',truck.size,0); md=ImageDraw.Draw(mask); md.rounded_rectangle((18,18,truck.width-18,truck.height-18),50,fill=230); mask=mask.filter(ImageFilter.GaussianBlur(24)); p.paste(truck,(55,2510),mask)
# phone inset, readable but secondary
phone=(1370,1900,1900,2780); d.rounded_rectangle(phone,55,fill='#0c0e12',outline='#d8dde3',width=7); d.rounded_rectangle((1415,1980,1855,2665),28,fill='#101823',outline='#2d3947',width=4)
txt(d,(1470,2040),'FULL',34,True,fill='#d8f2e1',stroke=0); txt(d,(1635,2240),'WELCOME',42,True,fill='#eaf3f5',stroke=0,anchor='mm'); txt(d,(1635,2310),'HOME',54,True,fill='#eaf3f5',stroke=0,anchor='mm'); bubble(d,(1160,2780,1455,2915),'Figures.',30)
txt(d,(95,3040),'END ISSUE #1',34,True,fill='#e9edf0',stroke=2)
save(p,24)

# QA + manifest
manifest=['# EP1 ending promotion — P17–P24','', 'Controlled assembly; exact scripted panel counts; intentional doorway recurrence P20–P23.']
for n in range(17,25):
    path=PAGES/f'p{n:02d}.png'; im=Image.open(path); assert im.size==(W,H); im.verify(); sha=hashlib.sha256(path.read_bytes()).hexdigest(); manifest.append(f'- P{n}: `{sha}`')
(ART/'PROMOTION_P17_P24_2026-09-14.md').write_text('\n'.join(manifest)+'\n',encoding='utf-8')
print('P17-P24 build complete')
