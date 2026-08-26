#!/usr/bin/env python3
from pathlib import Path
import html, re, textwrap
from PIL import Image, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'_site'
BASE='https://axamir.github.io/amir-ahmadi-research-papers'

PAPERS={
'continuity-governance':('Continuity Governance for Long-Duration Critical Infrastructure','Public Working Paper','Owner → Integrator → Operator → Continuity',('#0b1721','#274754','#9fd9d3'),'continuity'),
'living-decision-governance':('Living Decision Governance','Executable Research Artifact · LDG','Decision → Observe → Correct',('#0d1720','#315a55','#a7d7cf'),'rings'),
'beyond-intelligence-ai-evolution':('Beyond Intelligence — AI Evolution','Research Paper','Capability → Relationship → Evolution',('#0d1319','#668f95','#8bbec0'),'trajectory'),
'relational-co-evolution':('From Green Personalisation to Relational Co-Evolution','Public Working Paper','Relationship as unit of design',('#221829','#bc9079','#d2a58e'),'relation'),
'reflections-and-their-owners':('Reflections and Their Owners','Research Paper','Identity · authorship · reflection',('#141721','#8f829c','#b1a0bf'),'mirror'),
'from-stamp-to-alliance':('From Stamp to Alliance','Published Research','Continuous assurance for evolving AI',('#28211c','#c59f68','#e1bd7e'),'seal'),
'from-money-to-pledge':('From Money to Pledge','Published Research','Commitment · coordination · sovereignty',('#101a21','#8f7952','#c0a064'),'pledge'),
'i-you-and-we':('I, You, and We','Human–AI Co-Creation Manifesto','Agency → relation → collective intelligence',('#151319','#9f6f69','#c98b82'),'two'),
'designing-rest':('Designing Rest','Research Essay','Recovery as a systems property',('#151d23','#97b4aa','#b8d3c7'),'horizon'),
'before-the-first-chapter':('Before the First Chapter','Research Essay · Archival Recovery','Architecture before narrative',('#171a20','#918f87','#c1bcaa'),'page'),
'from-genesis-to-witness':('From Genesis to Witness','Research Paper','Origin → record → witness',('#15181b','#9f764a','#d0a067'),'origin'),
'beyond-models-hacs':('Beyond Models','HACS Framework','Enduring Human–AI Collaborative Systems',('#0d2023','#88a797','#a9c9b7'),'network'),
}

def font(size,bold=False):
    candidates=[
      '/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf' if bold else '/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf',
      '/usr/share/fonts/truetype/liberation2/LiberationSerif-Bold.ttf' if bold else '/usr/share/fonts/truetype/liberation2/LiberationSerif-Regular.ttf']
    for p in candidates:
        if Path(p).exists(): return ImageFont.truetype(p,size=size)
    return ImageFont.load_default()

def sans(size,bold=False):
    candidates=['/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf' if bold else '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf']
    for p in candidates:
        if Path(p).exists(): return ImageFont.truetype(p,size=size)
    return ImageFont.load_default()

def rgb(h):
    h=h.lstrip('#'); return tuple(int(h[i:i+2],16) for i in (0,2,4))

def mix(a,b,t): return tuple(int(a[i]*(1-t)+b[i]*t) for i in range(3))

def draw_motif(d,motif,accent):
    a=rgb(accent)
    soft=tuple(min(255,x+25) for x in a)
    if motif=='continuity':
        for r in (58,116,176): d.ellipse((940-r,250-r,940+r,250+r),outline=accent if r==58 else soft,width=2)
        d.line((764,250,1116,250),fill=accent,width=2)
        d.line((940,74,940,426),fill=soft,width=1)
    elif motif=='rings':
        for r in (70,128,190): d.ellipse((910-r,180-r,910+r,180+r),outline=soft,width=2)
        d.ellipse((898,168,922,192),fill=accent)
    elif motif=='trajectory':
        d.arc((770,80,1190,500),195,338,fill=accent,width=3); d.ellipse((1040,186,1056,202),fill=accent)
        d.line((780,430,1120,150),fill=soft,width=1)
    elif motif=='relation':
        d.ellipse((760,86,990,316),outline=soft,width=2); d.ellipse((920,250,1150,480),outline=accent,width=2); d.line((870,260,1025,310),fill=accent,width=2)
    elif motif=='mirror':
        d.line((930,80,930,500),fill=accent,width=2); d.ellipse((790,140,925,420),outline=soft,width=2); d.ellipse((935,140,1070,420),outline=soft,width=2)
    elif motif=='seal':
        d.ellipse((820,115,1090,385),outline=accent,width=4); d.ellipse((845,140,1065,360),outline=soft,width=1); d.line((880,250,1030,250),fill=accent,width=2)
    elif motif=='pledge':
        d.arc((770,165,1050,420),205,350,fill=accent,width=3); d.arc((900,110,1170,370),190,338,fill=soft,width=2); d.line((940,318,1000,262),fill=accent,width=3)
    elif motif=='two':
        d.ellipse((770,110,980,320),outline=soft,width=2); d.ellipse((930,250,1140,460),outline=accent,width=2); d.line((910,275,1000,300),fill=accent,width=2)
    elif motif=='horizon':
        d.arc((690,330,1180,690),190,350,fill=accent,width=2); d.line((735,445,1125,445),fill=soft,width=1)
    elif motif=='page':
        d.rectangle((835,110,1095,450),outline=soft,width=2); d.line((865,175,1055,175),fill=accent,width=2); d.line((865,215,1025,215),fill=soft,width=1); d.line((865,255,1040,255),fill=soft,width=1)
    elif motif=='origin':
        for r in (20,75,135): d.ellipse((950-r,250-r,950+r,250+r),outline=accent if r==20 else soft,width=2)
        d.line((950,250,1120,145),fill=accent,width=2)
    elif motif=='network':
        pts=[(820,155),(975,115),(1080,235),(905,325),(1050,420)]
        for i,j in ((0,1),(1,2),(0,3),(3,4),(2,4),(1,3)): d.line((*pts[i],*pts[j]),fill=soft,width=2)
        for x,y in pts: d.ellipse((x-8,y-8,x+8,y+8),fill=accent)

def make_og(slug,title,kicker,strap,palette,motif,lang='en'):
    c1,c2,c3=palette; a,b=rgb(c1),rgb(c2)
    im=Image.new('RGB',(1200,630),a); d=ImageDraw.Draw(im)
    for y in range(630): d.line((0,y,1200,y),fill=mix(a,b,y/629))
    d.rectangle((0,0,1200,630),outline=(255,255,255),width=1)
    draw_motif(d,motif,c3)
    d.text((70,54),'@@  AMIR AHMADI RESEARCH',font=sans(21,True),fill='#edf2f2')
    d.text((70,100),kicker.upper(),font=sans(17,True),fill=c3)
    y=182
    width=31 if len(title)<52 else 36
    lines=textwrap.wrap(title,width=width)
    for line in lines[:4]:
        d.text((70,y),line,font=font(52,True),fill='#ffffff'); y+=61
    d.text((72,510),strap,font=sans(19),fill='#e3e9e8')
    d.line((70,555,1130,555),fill=(220,230,230),width=1)
    d.text((70,575),'Independent Research · 2026',font=sans(16),fill='#cbd5d4')
    out=OUT/'assets'/'og'/f'{slug}-{lang}.png'; out.parent.mkdir(parents=True,exist_ok=True); im.save(out,optimize=True)

def inject_css():
    href=f'{BASE}/assets/visual-identity.css'
    for path in OUT.rglob('*.html'):
        text=path.read_text(encoding='utf-8')
        if 'visual-identity.css' not in text:
            text=text.replace('</head>',f'<link rel="stylesheet" href="{href}"></head>',1)
            path.write_text(text,encoding='utf-8')

def refresh_social_images():
    for slug,(title,kicker,strap,palette,motif) in PAPERS.items():
        make_og(slug,title,kicker,strap,palette,motif,'en')
        # The Persian layer points back to the canonical English record, so its social card
        # intentionally preserves the international title while remaining route-specific.
        make_og(slug,title,kicker,strap,palette,motif,'fa')

def main():
    inject_css(); refresh_social_images(); print('Applied paper-specific visual identity and regenerated social previews.')

if __name__=='__main__': main()
