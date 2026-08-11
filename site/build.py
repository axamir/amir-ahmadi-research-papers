#!/usr/bin/env python3
"""Build the Amir Ahmadi Research Hub into _site."""
from __future__ import annotations
import html, json, re, shutil, textwrap
from pathlib import Path
import markdown
from PIL import Image, ImageDraw, ImageFont
SOURCE=Path(__file__).resolve().parent
ROOT=SOURCE.parent
OUT=ROOT/'_site'
BASE='https://axamir.github.io/amir-ahmadi-research-papers'
GITHUB='https://github.com/axamir/amir-ahmadi-research-papers'
RAW='https://raw.githubusercontent.com/axamir/amir-ahmadi-research-papers/main'
ORCID='https://orcid.org/0009-0000-0614-6869'
PAPERS=[
 dict(slug='living-decision-governance',title_en='Living Decision Governance',title_fa='حکمرانی زنده تصمیم',source_en='papers/2026-living-decision-governance/LDG_COMPLETE.md',source_fa='papers/2026-living-decision-governance/LDG_COMPLETE.fa.md',repo='papers/2026-living-decision-governance',cover='ldg',kicker_en='Executable Research Artifact · LDG',kicker_fa='اثر پژوهشی اجرایی · LDG',date_en='August 2026',date_fa='اوت ۲۰۲۶',date_iso='2026-08-11',status_en='Public Working Paper / Executable Artifact',status_fa='مقاله کاری عمومی / اثر اجرایی',version='v0.2.0-draft',topics=['AI Governance','Decision Intelligence','Human Oversight'],artifacts=[('Python model','papers/2026-living-decision-governance/src/ldg_v02.py'),('Tests','papers/2026-living-decision-governance/tests/test_ldg_v02.py'),('Verification protocol','papers/2026-living-decision-governance/machine-readable/verification-protocol.json'),('AI verification guide','papers/2026-living-decision-governance/machine-readable/AI-README.md')]),
 dict(slug='beyond-intelligence-ai-evolution',title_en='Beyond Intelligence — AI Evolution',title_fa='فراتر از هوشمندی — تکامل هوش مصنوعی',source_en='papers/beyond-intelligence-ai-evolution/paper-en.md',source_fa='papers/beyond-intelligence-ai-evolution/paper-fa.md',repo='papers/beyond-intelligence-ai-evolution',cover='beyond',kicker_en='Research Paper',kicker_fa='مقاله پژوهشی',date_en='August 2026',date_fa='اوت ۲۰۲۶',date_iso='2026-08-02',status_en='Evolving Research Draft',status_fa='پیش‌نویس پژوهشی در حال توسعه',version='v1.0 Draft',topics=['AI Evolution','Co-Creation','Governance'],image_en='papers/beyond-intelligence-ai-evolution/figures/cover-beyond-intelligence-en-v1.0.png',image_fa='papers/beyond-intelligence-ai-evolution/figures/cover-beyond-intelligence-fa-v1.0.png'),
 dict(slug='relational-co-evolution',title_en='From Green Personalisation to Relational Co-Evolution',title_fa='از شخصی‌سازی سبز تا هم‌تکاملی رابطه‌ای',source_en='papers/2026-relational-co-evolution/paper.en.md',source_fa='papers/2026-relational-co-evolution/paper.fa.md',repo='papers/2026-relational-co-evolution',cover='relation',kicker_en='Public Working Paper',kicker_fa='مقاله کاری عمومی',date_en='July 2026',date_fa='ژوئیه ۲۰۲۶',date_iso='2026-07-31',status_en='Public Working Paper',status_fa='مقاله کاری عمومی',version='v0.2',topics=['Human–AI Collaboration','Relational Systems','Personalisation'],image_en='papers/2026-relational-co-evolution/cover.linkedin.png',image_fa='papers/2026-relational-co-evolution/cover.linkedin.png'),
 dict(slug='reflections-and-their-owners',title_en='Reflections and Their Owners',title_fa='بازتاب‌ها و صاحبانشان',source_en='papers/2026-reflections-and-their-owners/paper.md',source_fa='papers/2026-reflections-and-their-owners/paper.fa.md',repo='papers/2026-reflections-and-their-owners',cover='reflect',kicker_en='Research Paper',kicker_fa='مقاله پژوهشی',date_en='July 2026',date_fa='ژوئیه ۲۰۲۶',date_iso='2026-07-23',status_en='Draft Research Paper',status_fa='پیش‌نویس مقاله پژوهشی',version='Draft',topics=['Identity','Authorship','Human–AI Co-Creation']),
 dict(slug='from-stamp-to-alliance',title_en='From Stamp to Alliance: Redefining AI Certification',title_fa='از مُهر تا اتحاد: بازتعریف گواهی هوش مصنوعی',source_en='papers/2026-from-stamp-to-alliance/paper.en.md',source_fa='papers/2026-from-stamp-to-alliance/paper.fa.md',repo='papers/2026-from-stamp-to-alliance',cover='stamp',kicker_en='Published Research',kicker_fa='پژوهش منتشرشده',date_en='July 2026',date_fa='ژوئیه ۲۰۲۶',date_iso='2026-07-18',status_en='Published Research',status_fa='پژوهش منتشرشده',version='2026 Edition',topics=['Certification','Assurance','AI Governance']),
 dict(slug='from-money-to-pledge',title_en='From Money to Pledge',title_fa='از پول تا پیمان',source_en='papers/2026-from-pledge-to-sovereignty/paper.en.md',source_fa='papers/2026-from-pledge-to-sovereignty/paper.fa.md',repo='papers/2026-from-pledge-to-sovereignty',cover='pledge',kicker_en='Published Research',kicker_fa='پژوهش منتشرشده',date_en='July 2026',date_fa='ژوئیه ۲۰۲۶',date_iso='2026-07-15',status_en='Published Research',status_fa='پژوهش منتشرشده',version='2026 Edition',topics=['Decentralized Governance','Commitment','Verifiable Systems']),
 dict(slug='i-you-and-we',title_en='I, You, and We',title_fa='من، تو و ما',source_en='papers/2026-human-ai-co-creation-manifesto/paper.en.md',source_fa='papers/2026-human-ai-co-creation-manifesto/paper.fa.md',repo='papers/2026-human-ai-co-creation-manifesto',cover='manifesto',kicker_en='Human–AI Co-Creation Manifesto',kicker_fa='مانیفست هم‌آفرینی انسان–هوش مصنوعی',date_en='July 2026',date_fa='ژوئیه ۲۰۲۶',date_iso='2026-07-13',status_en='Publication-ready Manifesto',status_fa='مانیفست آماده انتشار',version='2026 Edition',topics=['Co-Creation','Human Agency','Collective Intelligence']),
 dict(slug='designing-rest',title_en='Designing Rest',title_fa='طراحی استراحت',source_en='papers/2026-designing-rest/paper.en.md',source_fa='papers/2026-designing-rest/paper.fa.md',repo='papers/2026-designing-rest',cover='rest',kicker_en='Research Essay',kicker_fa='جستار پژوهشی',date_en='July 2026',date_fa='ژوئیه ۲۰۲۶',date_iso='2026-07-10',status_en='Research Essay',status_fa='جستار پژوهشی',version='2026 Edition',topics=['Human Systems','Recovery','Design']),
 dict(slug='before-the-first-chapter',title_en='Before the First Chapter',title_fa='پیش از فصل اول',source_en='papers/2026-before-the-first-chapter/paper.en.md',source_fa='papers/2026-before-the-first-chapter/paper.fa.md',repo='papers/2026-before-the-first-chapter',cover='chapter',kicker_en='Research Essay · Archival Recovery',kicker_fa='جستار پژوهشی',date_en='July 2026',date_fa='ژوئیه ۲۰۲۶',date_iso='2026-07-06',status_en='Draft · Bilingual Record Restored',status_fa='پیش‌نویس · رکورد دوزبانه کامل',version='Paper No. 4',topics=['Independent Research','Agent Architecture','Research History']),
 dict(slug='from-genesis-to-witness',title_en='From Genesis to Witness',title_fa='از پیدایش تا شاهد',source_en='papers/2026-from-genesis-to-witness/paper.md',source_fa='papers/2026-from-genesis-to-witness/paper.fa.md',repo='papers/2026-from-genesis-to-witness',cover='genesis',kicker_en='Research Paper',kicker_fa='مقاله پژوهشی',date_en='June 2026',date_fa='ژوئن ۲۰۲۶',date_iso='2026-06-27',status_en='Research Paper',status_fa='مقاله پژوهشی',version='2026 Edition',topics=['Continuity','Witnessing','AI Lineage']),
 dict(slug='beyond-models-hacs',title_en='Beyond Models: Toward Enduring Human–AI Collaborative Systems',title_fa='فراتر از مدل‌ها: به‌سوی سامانه‌های پایدار همکاری انسان–هوش مصنوعی',source_en='2026/beyond-models-hacs/paper.en.md',source_fa='2026/beyond-models-hacs/paper.fa.md',repo='2026/beyond-models-hacs',cover='hacs',kicker_en='HACS Framework',kicker_fa='چارچوب HACS',date_en='2026',date_fa='۲۰۲۶',date_iso='2026-06-20',status_en='Initial Research Release',status_fa='انتشار اولیه پژوهش',version='v1.0.0',topics=['Human–AI Collaboration','Context Continuity','Governance'],artifacts=[('HACS definition','2026/beyond-models-hacs/framework/definition.md'),('Architecture','2026/beyond-models-hacs/framework/architecture.md'),('Evaluation','2026/beyond-models-hacs/framework/evaluation.md'),('Governance','2026/beyond-models-hacs/framework/governance.md')]),
]
PALETTES={'ldg':('#101b25','#315a55','#a7d7cf'),'beyond':('#10161c','#2d495f','#8bbec0'),'relation':('#261c2d','#704b64','#d2a58e'),'reflect':('#161923','#353b5c','#b1a0bf'),'stamp':('#2b241f','#7c624a','#e1bd7e'),'pledge':('#121d24','#325267','#c0a064'),'manifesto':('#17151b','#5b4056','#c98b82'),'rest':('#172026','#49666a','#b8d3c7'),'chapter':('#181b22','#455266','#c1bcaa'),'genesis':('#171a1d','#544638','#d0a067'),'hacs':('#0f2427','#315b57','#a9c9b7')}

def strip_frontmatter(text):
    if text.startswith('---\n'):
        end=text.find('\n---\n',4)
        if end!=-1:return text[end+5:]
    return text

def rewrite_relative_targets(text,source_path):
    source_dir=source_path.parent.as_posix()
    def repl(m):
        prefix,target,suffix=m.group(1),m.group(2),m.group(3); t=target.strip()
        if re.match(r'^(https?://|mailto:|#|data:)',t,re.I):return m.group(0)
        clean=(Path(source_dir)/t).as_posix(); url=f'{RAW}/{clean}' if prefix.startswith('!') else f'{GITHUB}/blob/main/{clean}'
        return f'{prefix}{url}{suffix}'
    return re.sub(r'(!?\[[^\]]*\]\()([^\)]+)(\))',repl,text)

def render_markdown(source_rel):
    path=ROOT/source_rel
    if not path.exists():raise RuntimeError(f'Missing canonical source: {source_rel}')
    raw=path.read_text(encoding='utf-8')
    if len(raw.strip())<80 or raw.strip().lower() in {'test content','placeholder'}:raise RuntimeError(f'Canonical source is placeholder/incomplete: {source_rel}')
    body=rewrite_relative_targets(strip_frontmatter(raw),Path(source_rel))
    rendered=markdown.markdown(body,extensions=['extra','tables','fenced_code','sane_lists','toc'],output_format='html5')
    plain=re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',rendered)).strip()
    return rendered,plain,len(raw)

def paper_url(p,lang):return f"{BASE}/{'fa/' if lang=='fa' else ''}papers/{p['slug']}/"
def citation_text(p,lang):return f"Ahmadi, Amir. (2026). {p[f'title_{lang}']}. Amir Ahmadi Research. {paper_url(p,lang)}"
def og_image(p,lang):return f"{BASE}/assets/og/{p['slug']}-{lang}.png"
def _font(size,bold=False):
    candidates=['/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf' if bold else '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf','/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf' if bold else '/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf']
    for p in candidates:
        if Path(p).exists():return ImageFont.truetype(p,size=size)
    return ImageFont.load_default()

def generate_og(p,lang):
    title=p['title_en']; kicker=p['kicker_en']; status=f"{p['version']}  ·  {p['status_en']}"; c1,c2,c3=PALETTES[p['cover']]
    im=Image.new('RGB',(1200,630),c1); d=ImageDraw.Draw(im)
    a=tuple(int(c1.lstrip('#')[j:j+2],16) for j in (0,2,4)); b=tuple(int(c2.lstrip('#')[j:j+2],16) for j in (0,2,4))
    for i in range(630):
        t=i/629; col=tuple(int(a[k]*(1-t)+b[k]*t) for k in range(3)); d.line((0,i,1200,i),fill=col)
    d.ellipse((850,-110,1270,310),outline=c3,width=2); d.ellipse((-100,440,190,730),outline=c3,width=1)
    d.text((72,64),'@@  AMIR AHMADI RESEARCH',font=_font(24,True),fill='#e8eff0'); d.text((72,112),kicker.upper(),font=_font(18,True),fill=c3)
    y=190
    for line in textwrap.wrap(title,width=30): d.text((72,y),line,font=_font(54,True),fill='#ffffff'); y+=66
    d.line((72,520,1128,520),fill='#dbe6e6',width=1); d.text((72,546),status,font=_font(19),fill='#dce5e5'); d.text((1035,546),'2026',font=_font(19,True),fill=c3)
    out=OUT/'assets'/'og'/f"{p['slug']}-{lang}.png"; out.parent.mkdir(parents=True,exist_ok=True); im.save(out,optimize=True)

def artifact_links(p,fa):
    arts=p.get('artifacts',[])
    if not arts:return ''
    heading='آثار و فایل‌های همراه' if fa else 'Research artifacts'
    rows=''.join(f'<a href="{GITHUB}/blob/main/{path}" target="_blank" rel="noopener"><span>{html.escape(label)}</span><b>↗</b></a>' for label,path in arts)
    return f'<section class="artifact-panel"><div class="side-label">{heading}</div>{rows}</section>'

def paper_page(p,lang):
    fa=lang=='fa'; source=p[f'source_{lang}']; title=p[f'title_{lang}']; kicker=p[f'kicker_{lang}']; date=p[f'date_{lang}']; status=p[f'status_{lang}']
    article,plain,chars=render_markdown(source); words=max(1,len(plain.split()) if not fa else chars//5); mins=max(1,round(words/(210 if not fa else 170)))
    source_url=f'{GITHUB}/blob/main/{source}'; repo_url=f"{GITHUB}/tree/main/{p['repo']}"; home=f'{BASE}/fa/' if fa else f'{BASE}/'; alt=paper_url(p,'en' if fa else 'fa'); url=paper_url(p,lang); og=og_image(p,lang)
    summary=(plain[:250]+'…') if len(plain)>250 else plain; topics=''.join(f'<span class="pill">{html.escape(t)}</span>' for t in p['topics']); citation=citation_text(p,lang)
    read_label=f'حدود {mins} دقیقه مطالعه' if fa else f'~{mins} min read'; back='همه مقالات' if fa else 'All papers'; source_label='Markdown اصلی' if fa else 'Canonical Markdown'; repo_label='فولدر پژوهش' if fa else 'Research folder'; cite_label='استناد پیشنهادی' if fa else 'Suggested citation'
    provenance='این صفحه فقط از Markdown فارسی نهایی ساخته شده و نسخه انگلیسی در مسیر انگلیسی مستقل است.' if fa else 'This page is generated only from the canonical English Markdown; the Persian edition is published separately.'
    direction=' dir="rtl"' if fa else ''
    image_rel=p.get(f'image_{lang}')
    cover=f'<figure class="paper-image-cover"><img src="{RAW}/{image_rel}" alt="{html.escape(title)} cover"></figure>' if image_rel else f'<div class="reading-cover {p["cover"]}"><span>{html.escape(kicker)}</span><strong>{html.escape(title)}</strong><small>{html.escape(date)}</small></div>'
    schema={'@context':'https://schema.org','@type':'ScholarlyArticle','headline':title,'description':summary,'datePublished':p['date_iso'],'dateModified':'2026-08-12','inLanguage':lang,'author':{'@type':'Person','name':'Amir Ahmadi','sameAs':[ORCID,'https://github.com/axamir']},'url':url,'image':og,'version':p['version'],'keywords':p['topics'],'isPartOf':{'@type':'CollectionPage','name':'Amir Ahmadi Research','url':home}}
    return f'''<!doctype html><html lang="{lang}"{direction}><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)} — Amir Ahmadi Research</title><meta name="description" content="{html.escape(summary,quote=True)}"><link rel="canonical" href="{url}"><link rel="alternate" hreflang="en" href="{paper_url(p,'en')}"><link rel="alternate" hreflang="fa" href="{paper_url(p,'fa')}"><link rel="alternate" hreflang="x-default" href="{paper_url(p,'en')}"><link rel="icon" href="{BASE}/assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="{BASE}/assets/paper.css"><link rel="stylesheet" href="{BASE}/assets/polish.css"><meta property="og:type" content="article"><meta property="og:title" content="{html.escape(title,quote=True)}"><meta property="og:description" content="{html.escape(summary,quote=True)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{og}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:image" content="{og}"><meta name="citation_title" content="{html.escape(title,quote=True)}"><meta name="citation_author" content="Amir Ahmadi"><meta name="citation_publication_date" content="{p['date_iso']}"><meta name="citation_fulltext_html_url" content="{url}"><script type="application/ld+json">{json.dumps(schema,ensure_ascii=False)}</script></head><body class="reading-page {'rtl' if fa else ''}" data-paper-slug="{p['slug']}"><div class="reading-progress" aria-hidden="true"><span></span></div><header class="top"><div class="shell nav"><a class="brand" href="{home}">@@ Amir Ahmadi Research</a><nav class="navlinks"><a href="{home}">{back}</a><a href="{repo_url}" target="_blank" rel="noopener">GitHub ↗</a></nav></div></header><main><section class="reading-hero"><div class="shell reading-shell"><div class="eyebrow">{html.escape(kicker)}</div><h1>{html.escape(title)}</h1><p class="reading-note">{html.escape(provenance)}</p><div class="reading-meta"><span>{html.escape(date)}</span><span>{html.escape(p['version'])}</span><span>{html.escape(status)}</span><span>{read_label}</span></div><div class="topic-row">{topics}</div><div class="actions"><a class="btn primary" href="#paper">{'خواندن مقاله' if fa else 'Read full paper'} ↓</a><a class="btn" href="{alt}">{'English edition' if fa else 'نسخه فارسی'} ↗</a><a class="btn" href="{source_url}" target="_blank" rel="noopener">{source_label} ↗</a></div>{cover}</div></section><section class="shell reading-shell reading-layout" id="paper"><article class="markdown-body">{article}</article><aside class="reading-side"><div class="side-card publication-card"><div class="side-label">{'هویت انتشار' if fa else 'Publication identity'}</div><dl><dt>{'نویسنده' if fa else 'Author'}</dt><dd>Amir Ahmadi</dd><dt>ORCID</dt><dd><a href="{ORCID}" target="_blank" rel="noopener">0009-0000-0614-6869 ↗</a></dd><dt>{'نسخه' if fa else 'Version'}</dt><dd>{html.escape(p['version'])}</dd><dt>{'وضعیت' if fa else 'Status'}</dt><dd>{html.escape(status)}</dd><dt>{'زبان' if fa else 'Language'}</dt><dd>{'فارسی' if fa else 'English'}</dd></dl></div><div class="side-card citation-card"><div class="side-label">{cite_label}</div><p>{html.escape(citation)}</p><button class="copy-citation" data-citation="{html.escape(citation,quote=True)}">{'کپی استناد' if fa else 'Copy citation'}</button></div><div class="side-card provenance-card"><div class="side-label">{'منبع و شواهد' if fa else 'Source & provenance'}</div><a href="{source_url}" target="_blank" rel="noopener">{source_label} ↗</a><a href="{repo_url}" target="_blank" rel="noopener">{repo_label} ↗</a><a href="{GITHUB}/commits/main/{source}" target="_blank" rel="noopener">{'تاریخچه نسخه' if fa else 'Revision history'} ↗</a></div>{artifact_links(p,fa)}</aside></section></main><footer><div class="shell">© 2026 Amir Ahmadi · Independent Research · <a href="{GITHUB}">Source archive</a></div></footer><script src="{BASE}/assets/app.js"></script></body></html>'''

def inject_home_metadata(path,lang):
    text=path.read_text(encoding='utf-8'); fa=lang=='fa'; url=f'{BASE}/fa/' if fa else f'{BASE}/'; title='پژوهش‌های امیر احمدی' if fa else 'Amir Ahmadi Research'; desc='آرشیو پژوهش‌های مستقل درباره سامانه‌های انسان–هوش مصنوعی، حکمرانی، هویت و معماری‌های قابل راستی‌آزمایی.' if fa else 'Independent research on human–AI systems, governance, identity, decision intelligence and verifiable architectures.'
    text=re.sub(r'<link rel="canonical"[^>]*>\s*','',text,flags=re.I)
    block=f'<link rel="canonical" href="{url}"><link rel="alternate" hreflang="en" href="{BASE}/"><link rel="alternate" hreflang="fa" href="{BASE}/fa/"><link rel="alternate" hreflang="x-default" href="{BASE}/"><link rel="stylesheet" href="{BASE}/assets/polish.css"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:type" content="website"><meta property="og:url" content="{url}"><meta property="og:image" content="{BASE}/assets/og-default.svg">'
    text=re.sub(r'</head>',block+'</head>',text,count=1,flags=re.I); path.write_text(text,encoding='utf-8')

def write_sitemap():
    urls=[f'{BASE}/',f'{BASE}/fa/']
    for p in PAPERS:urls += [paper_url(p,'en'),paper_url(p,'fa')]
    lines=['<?xml version="1.0" encoding="UTF-8"?>','<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']+[f'  <url><loc>{html.escape(u)}</loc><lastmod>2026-08-12</lastmod></url>' for u in urls]+['</urlset>']; (OUT/'sitemap.xml').write_text('\n'.join(lines),encoding='utf-8')

def main():
    for p in PAPERS: render_markdown(p['source_en']); render_markdown(p['source_fa'])
    if OUT.exists():shutil.rmtree(OUT)
    shutil.copytree(SOURCE,OUT,ignore=shutil.ignore_patterns('build.py','validate.py','__pycache__'))
    inject_home_metadata(OUT/'index.html','en'); inject_home_metadata(OUT/'fa'/'index.html','fa')
    for p in PAPERS:
        for lang in ('en','fa'):
            generate_og(p,lang); target=OUT/(Path('fa') if lang=='fa' else Path())/'papers'/p['slug']/'index.html'; target.parent.mkdir(parents=True,exist_ok=True); target.write_text(paper_page(p,lang),encoding='utf-8')
    write_sitemap(); print(f'Built publication-grade bilingual Research Hub with {len(PAPERS)} papers × 2 languages.')
if __name__=='__main__':main()
