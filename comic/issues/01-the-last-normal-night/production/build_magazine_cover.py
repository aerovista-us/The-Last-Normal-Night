from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import hashlib

ISSUE=Path(__file__).resolve().parents[1]; P=ISSUE/'pages'
W,H=2063,3150
BG=Image.open(P/'p01.png').convert('RGB')
# Crop away comic furniture, then cover the full bleed canvas with the CDA night art.
art=BG.crop((26,170,2037,3040)).resize((W,H),Image.Resampling.LANCZOS)
# Cinematic dark editorial grade.
art=ImageEnhance.Contrast(art).enhance(1.08); art=ImageEnhance.Color(art).enhance(.82); art=ImageEnhance.Brightness(art).enhance(.72)
# Use canonical protagonist/truck art as a grounded foreground anchor.
src=Image.open(P/'p16.png').convert('RGB')
hero=src.crop((0,180,1040,3030)).resize((880,2415),Image.Resampling.LANCZOS)
mask=Image.new('L',hero.size,255); md=ImageDraw.Draw(mask)
for i in range(95):
    v=int(255*i/94); md.rectangle((i,i,hero.width-i-1,hero.height-i-1),outline=v)
mask=mask.filter(ImageFilter.GaussianBlur(40)); art.paste(hero,(0,735),mask)
d=ImageDraw.Draw(art)
FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'; BOLD='/usr/share/fonts/truetype/dejavu/DejaVuSansCondensed-Bold.ttf'
def F(p,s): return ImageFont.truetype(p,s)
def center(text,y,font,fill='white',stroke=0):
    b=d.textbbox((0,0),text,font=font,stroke_width=stroke); x=(W-(b[2]-b[0]))//2
    d.text((x,y),text,font=font,fill=fill,stroke_width=stroke,stroke_fill='#05080c')
def fit_size(text,maxw,start=190,minsize=70):
    s=start
    while s>minsize and d.textbbox((0,0),text,font=F(BOLD,s))[2]>maxw: s-=2
    return F(BOLD,s)
# Premium magazine/comic cover frame.
d.rectangle((18,18,W-19,H-19),outline='#e7e0d3',width=5)
d.rectangle((31,31,W-32,H-32),outline='#6c7880',width=2)
# Issue slug.
d.rounded_rectangle((72,92,330,390),radius=10,fill='#a72921',outline='#f1e7d4',width=3)
d.text((98,118),'ISSUE',font=F(BOLD,43),fill='white'); d.text((96,172),'#1',font=F(BOLD,108),fill='white'); d.text((98,315),'SEP 2026',font=F(BOLD,29),fill='white')
center('ECHOSTORY  •  AEROVISTA PRESENTS',88,F(BOLD,34),'#9fc6dc')
# Masthead block gets its own dark atmospheric field for legibility.
ov=Image.new('RGBA',(W,H),(0,0,0,0)); od=ImageDraw.Draw(ov); od.rectangle((0,430,W,1050),fill=(2,7,12,185)); ov=ov.filter(ImageFilter.GaussianBlur(8)); art=Image.alpha_composite(art.convert('RGBA'),ov).convert('RGB'); d=ImageDraw.Draw(art)
center('THE LAST',470,fit_size('THE LAST',1770,230),'#f1ede4',2)
center('NORMAL NIGHT',690,fit_size('NORMAL NIGHT',1870,220),'#f1ede4',2)
center('COEUR D’ALENE WAS ONLY THE BEGINNING.',955,F(BOLD,34),'#d7e0e4')
d=ImageDraw.Draw(art)
# Editorial cover lines: specific enough to sell the premise, no ending spoilers.
d.rounded_rectangle((70,1110,650,1495),radius=12,fill=(3,9,14),outline='#8aaabd',width=2)
d.text((100,1145),'A SMALL TOWN.',font=F(BOLD,43),fill='#a9cee1'); d.text((100,1210),'A LATE NIGHT.',font=F(BOLD,43),fill='#a9cee1'); d.text((100,1275),'ONE MINUTE',font=F(BOLD,43),fill='#a9cee1'); d.text((100,1340),'THAT REFUSED',font=F(BOLD,43),fill='#a9cee1'); d.text((100,1405),'TO END.',font=F(BOLD,43),fill='#a9cee1')
d.rounded_rectangle((1430,1170,1988,1470),radius=12,fill=(3,9,14),outline='#8aaabd',width=2)
d.text((1460,1205),'AT 11:59,',font=F(BOLD,46),fill='#f0e5cf'); d.text((1460,1270),'COEUR D’ALENE',font=F(BOLD,38),fill='#f0e5cf'); d.text((1460,1330),'STOPPED',font=F(BOLD,46),fill='#f0e5cf'); d.text((1460,1395),'MAKING SENSE.',font=F(BOLD,38),fill='#f0e5cf')
# Real periodical furniture: price, UPC-style bars, publisher mark.
d.rectangle((72,2610,365,3030),fill='#f3efe5',outline='#111',width=3); d.text((100,2640),'$4.99 US',font=F(BOLD,34),fill='#111')
for i,wid in enumerate([5,2,7,3,3,8,2,5,4,7,2,3,8,3,5,2,7,4,2,6,3,8,2,4]):
    x=100+i*9; d.rectangle((x,2700,x+wid,2930),fill='#111')
d.text((100,2950),'0  22978  11370  5',font=F(FONT,22),fill='#111')
d.text((93,3065),'VESPERA PUBLISHING  •  ECHOSTORY',font=F(BOLD,27),fill='#dce4e8')
center('SAME PLACES. DIFFERENT TOMORROW.',3060,F(BOLD,28),'#dce4e8')
# Export print master and web/Rack cover.
out=P/'00-cover-front.png'; art.save(out,'PNG',optimize=True)
web=art.resize((1310,2000),Image.Resampling.LANCZOS); web.save(P/'00-cover-front-web.jpg','JPEG',quality=91,optimize=True,progressive=True)
print(out, hashlib.sha256(out.read_bytes()).hexdigest()); print(P/'00-cover-front-web.jpg')
