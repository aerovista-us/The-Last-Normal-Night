from pathlib import Path
from PIL import Image
import hashlib, io, json, zipfile

ISSUE=Path(__file__).resolve().parents[1]
PAGES=ISSUE/'pages'
ART=ISSUE/'production'/'artifacts'
ART.mkdir(parents=True,exist_ok=True)
CBZ=ISSUE/'EP1-The-Last-Normal-Night.cbz'
W,H=2063,3150
VERSION='20260914-final'
SOURCE_COMMIT='021c0f29ecc0a80e5cb03df11f8e9fcd9b9cccb2'

items=[('00-cover-front.png','00-cover-front.jpg'),('01-inside-front.png','01-inside-front.jpg')]
items += [(f'p{n:02d}.png',f'{n+1:02d}-p{n:02d}.jpg') for n in range(1,25)]
items += [('26-cover-back.png','26-cover-back.jpg')]

def sha(b): return hashlib.sha256(b).hexdigest()
records=[]
with zipfile.ZipFile(CBZ,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for src_name,dst_name in items:
        src=PAGES/src_name
        raw=src.read_bytes()
        with Image.open(io.BytesIO(raw)) as im:
            if im.size != (W,H): raise SystemExit(f'{src}: {im.size}, expected {(W,H)}')
            rgb=im.convert('RGB')
            buf=io.BytesIO(); rgb.save(buf,'JPEG',quality=95,subsampling=0,optimize=True,dpi=(300,300))
            jpg=buf.getvalue()
        zi=zipfile.ZipInfo(dst_name,date_time=(2026,9,14,12,0,0)); zi.compress_type=zipfile.ZIP_DEFLATED
        zi.external_attr=0o644<<16
        z.writestr(zi,jpg,compress_type=zipfile.ZIP_DEFLATED,compresslevel=9)
        records.append({'source':src_name,'archive':dst_name,'sourceSha256':sha(raw),'deliverySha256':sha(jpg),'deliveryBytes':len(jpg)})

focus=json.loads((ISSUE/'focus-regions.json').read_text())
base='content/EchoStory/the-last-normal-night/issue-1/pages/'
sequence=[{'type':'image','src':base+f'00-cover-front.png?v={VERSION}','alt':'The Last Normal Night — Issue 1 front cover','title':'Front cover'},
          {'type':'image','src':base+f'01-inside-front.png?v={VERSION}','alt':'The Last Normal Night — inside front','title':'Inside front'}]
for n in range(1,25):
    key=f'p{n:02d}'
    sequence.append({'type':'image','src':base+f'{key}.png?v={VERSION}','alt':f'The Last Normal Night, page {n}','title':f'Page {n}','focusRegions':focus['pages'][key]})
sequence.append({'type':'image','src':base+f'26-cover-back.png?v={VERSION}','alt':'The Last Normal Night — Issue 1 back cover','title':'Back cover'})
book={'id':'last-normal-night-issue-1','series':'EchoStory — The Last Normal Night','title':'Issue No. 1 — The Crossing','issue':1,'status':'complete','featured':True,'creator':'EchoStory / Vespera Publishing','description':"One ordinary late night in Coeur d'Alene starts slipping out of alignment. Familiar streets, a recurring white sedan, frozen clocks, and a voice on Frequency Three push one man toward a choice the night seems to have already made for him.",'cover':base+f'00-cover-front.png?v={VERSION}','shareImage':'https://therack.aerovista.us/'+base+f'00-cover-front.png?v={VERSION}','shareUrl':'read/last-normal-night-issue-1/','companionUrl':'https://lastnormalnight.aerovista.us/','companionLabel':'Listen to The Last Normal Night','companionShortLabel':'Listen','readerMode':'book','spreadMode':'auto','format':{'width':W,'height':H},'genres':['mystery','science fiction','psychological thriller'],'tags':['echostory',"coeur d'alene",'north idaho','reality fracture','11:59','frequency three','lake','music companion'],'sequence':sequence}
(ART/'rack-issue-1.json').write_text(json.dumps(book,indent=2)+"\n")
manifest={'schemaVersion':1,'issueId':'last-normal-night-issue-1','sourceCommit':SOURCE_COMMIT,'publicationVersion':VERSION,'cbz':{'path':str(CBZ.relative_to(ISSUE)),'sha256':sha(CBZ.read_bytes()),'bytes':CBZ.stat().st_size,'entries':len(records)},'focusRegions':{'path':'focus-regions.json','sha256':sha((ISSUE/'focus-regions.json').read_bytes()),'regions':sum(len(v) for v in focus['pages'].values())},'files':records}
(ART/'PUBLICATION_EP1_2026-09-14.json').write_text(json.dumps(manifest,indent=2)+"\n")
print('CBZ',CBZ.stat().st_size,manifest['cbz']['sha256'])
print('Rack sequence',len(sequence),'Focus regions',manifest['focusRegions']['regions'])
