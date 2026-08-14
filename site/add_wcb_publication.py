#!/usr/bin/env python3
"""Add ARP-WCB-2026-01 to the generated Research Hub publication artifact."""
from pathlib import Path
import html, json, re
import markdown

ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'_site'
BASE='https://axamir.github.io/amir-ahmadi-research-papers'
GITHUB='https://github.com/axamir/amir-ahmadi-research-papers'
ORCID='https://orcid.org/0009-0000-0614-6869'
SLUG='we-are-code-that-breathes'
EN=ROOT/'papers/2026-we-are-code-that-breathes/manuscript-core.md'
FA=ROOT/'papers/2026-we-are-code-that-breathes/manuscript.fa.md'
REPO_PATH='papers/2026-we-are-code-that-breathes'

META={
'en':dict(title='We Are Code That Breathes',subtitle='A Provenance-Preserving Case Study of Claim Evolution in Persistent Human–Generative-AI Collaboration',kicker='Protocol Construction · Case Demonstration',status='Release Candidate v0.3',date='August 2026',date_iso='2026-08-14',topics=['Research Provenance','Human–AI Collaboration','Claim Evolution','PRCEP']),
'fa':dict(title='ما کدی هستیم که نفس می‌کشد',subtitle='مطالعه‌ی موردیِ حفظ منشأ درباره‌ی تکامل ادعا در همکاری پایدار انسان و هوش مصنوعی مولد',kicker='ساخت پروتکل · نمایش موردی',status='نسخه کاندید انتشار v0.3',date='اوت ۲۰۲۶',date_iso='2026-08-14',topics=['منشأ پژوهش','همکاری انسان و هوش مصنوعی','تکامل ادعا','PRCEP'])}

def render(path):
    raw=path.read_text(encoding='utf-8')
    body=markdown.markdown(raw,extensions=['extra','tables','fenced_code','sane_lists','toc'],output_format='html5')
    plain=re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',body)).strip()
    return body,plain,len(raw)

def page(lang):
    fa=lang=='fa'; m=META[lang]; source=FA if fa else EN; article,plain,chars=render(source)
    words=max(1,len(plain.split()) if not fa else chars//5); mins=max(1,round(words/(210 if not fa else 170)))
    url=f"{BASE}/{'fa/' if fa else ''}papers/{SLUG}/"; canonical=f'{BASE}/papers/{SLUG}/'; alt=f"{BASE}/{'papers' if fa else 'fa/papers'}/{SLUG}/"
    home=f"{BASE}/{'fa/' if fa else ''}"; source_url=f"{GITHUB}/blob/main/{REPO_PATH}/{source.name}"; repo=f'{GITHUB}/tree/main/{REPO_PATH}'
    desc=(plain[:260]+'…') if len(plain)>260 else plain
    pills=''.join(f'<span class="pill">{html.escape(x)}</span>' for x in m['topics'])
    direction=' dir="rtl"' if fa else ''
    read='خواندن مقاله' if fa else 'Read full paper'; allp='همه مقالات' if fa else 'All papers'; src='Markdown اصلی' if fa else 'Canonical Markdown'; folder='فولدر پژوهش' if fa else 'Research folder'
    read_label=f'حدود {mins} دقیقه مطالعه' if fa else f'~{mins} min read'
    boundary=('این نسخه فارسی از نظر قدرت ادعا، عدم‌قطعیت و مرزهای علمی با نسخه انگلیسی هم‌تراز است. مرجع علمی canonical نسخه انگلیسی است.' if fa else 'Protocol-construction and case-demonstration study. PRCEP is a protocol candidate, not a validated protocol.')
    og=f"{BASE}/assets/og/we-are-code-that-breathes-{'fa' if fa else 'en'}.svg"
    citation=f"Ahmadi, Amir. (2026). {m['title']}. Amir Ahmadi Research. {canonical}"
    schema={'@context':'https://schema.org','@type':'ScholarlyArticle','headline':m['title'],'alternativeHeadline':m['subtitle'],'description':desc,'datePublished':m['date_iso'],'dateModified':m['date_iso'],'inLanguage':lang,'author':{'@type':'Person','name':'Amir Ahmadi','sameAs':[ORCID,'https://github.com/axamir']},'url':canonical if fa else url,'image':og,'version':'RC v0.3','identifier':'ARP-WCB-2026-01','keywords':m['topics']}
    return f'''<!doctype html><html lang="{lang}"{direction}><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(m['title'])} — Amir Ahmadi Research</title><meta name="description" content="{html.escape(desc,quote=True)}"><link rel="canonical" href="{canonical}"><link rel="alternate" hreflang="en" href="{BASE}/papers/{SLUG}/"><link rel="alternate" hreflang="fa" href="{BASE}/fa/papers/{SLUG}/"><link rel="alternate" hreflang="x-default" href="{canonical}"><link rel="stylesheet" href="{BASE}/assets/paper.css"><link rel="stylesheet" href="{BASE}/assets/polish.css"><meta property="og:type" content="article"><meta property="og:title" content="{html.escape(m['title'],quote=True)}"><meta property="og:description" content="{html.escape(desc,quote=True)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{og}"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{html.escape(m['title'],quote=True)}"><meta name="twitter:description" content="{html.escape(desc,quote=True)}"><meta name="twitter:image" content="{og}"><meta name="citation_title" content="{html.escape(m['title'],quote=True)}"><meta name="citation_author" content="Amir Ahmadi"><meta name="citation_publication_date" content="2026-08-14"><meta name="citation_fulltext_html_url" content="{canonical}"><meta name="citation_technical_report_number" content="ARP-WCB-2026-01"><script type="application/ld+json">{json.dumps(schema,ensure_ascii=False)}</script></head><body class="reading-page {'rtl' if fa else ''}" data-paper-slug="{SLUG}"><div class="reading-progress" aria-hidden="true"><span></span></div><header class="top"><div class="shell nav"><a class="brand" href="{home}">@@ Amir Ahmadi Research</a><nav class="navlinks"><a href="{home}">{allp}</a><a href="{repo}" target="_blank" rel="noopener">GitHub ↗</a></nav></div></header><main><section class="reading-hero"><div class="shell reading-shell"><div class="eyebrow">{html.escape(m['kicker'])}</div><h1>{html.escape(m['title'])}</h1><p class="lede">{html.escape(m['subtitle'])}</p><p class="reading-note">{html.escape(boundary)}</p><div class="reading-meta"><span>{m['date']}</span><span>ARP-WCB-2026-01</span><span>{html.escape(m['status'])}</span><span>{read_label}</span></div><div class="topic-row">{pills}</div><div class="actions"><a class="btn primary" href="#paper">{read} ↓</a><a class="btn" href="{alt}">{'English edition' if fa else 'نسخه فارسی'} ↗</a><a class="btn" href="{source_url}" target="_blank" rel="noopener">{src} ↗</a></div><div class="reading-cover relation"><span>PRCEP · PROVENANCE · CLAIM EVOLUTION</span><strong>{html.escape(m['title'])}</strong><small>ARP-WCB-2026-01 · RC v0.3</small></div></div></section><section class="shell reading-shell reading-layout" id="paper"><article class="markdown-body">{article}</article><aside class="reading-side"><div class="side-card publication-card"><div class="side-label">{'هویت انتشار' if fa else 'Publication identity'}</div><dl><dt>{'نویسنده' if fa else 'Author'}</dt><dd>Amir Ahmadi</dd><dt>ORCID</dt><dd><a href="{ORCID}" target="_blank" rel="noopener">0009-0000-0614-6869 ↗</a></dd><dt>{'سند' if fa else 'Document'}</dt><dd>ARP-WCB-2026-01</dd><dt>{'وضعیت' if fa else 'Status'}</dt><dd>{html.escape(m['status'])}</dd></dl></div><div class="side-card citation-card"><div class="side-label">{'استناد پیشنهادی' if fa else 'Suggested citation'}</div><p>{html.escape(citation)}</p><button class="copy-citation" data-citation="{html.escape(citation,quote=True)}">{'کپی استناد' if fa else 'Copy citation'}</button></div><div class="side-card provenance-card"><div class="side-label">{'رکورد پژوهش' if fa else 'Research record'}</div><a href="{repo}" target="_blank" rel="noopener">{folder} ↗</a><a href="{source_url}" target="_blank" rel="noopener">{src} ↗</a><a href="{GITHUB}/blob/main/{REPO_PATH}/REFERENCES.md" target="_blank" rel="noopener">References ↗</a><a href="{GITHUB}/blob/main/{REPO_PATH}/AI_DISCLOSURE.md" target="_blank" rel="noopener">AI disclosure ↗</a><a href="{GITHUB}/commits/main/{REPO_PATH}/{source.name}" target="_blank" rel="noopener">{'تاریخچه نسخه' if fa else 'Revision history'} ↗</a></div></aside></section></main><footer><div class="shell">© 2026 Amir Ahmadi · Independent Research · <a href="{GITHUB}">Source archive</a></div></footer><script src="{BASE}/assets/app.js"></script></body></html>'''

def card(lang):
    fa=lang=='fa'; m=META[lang]; href=f"{BASE}/{'fa/' if fa else ''}papers/{SLUG}/"
    return f'''<article class="paper-card featured-wcb"><a href="{href}" aria-label="{html.escape(m['title'],quote=True)}"><div class="card-cover relation"><span>{html.escape(m['kicker'])}</span><strong>{html.escape(m['title'])}</strong><small>ARP-WCB-2026-01 · RC v0.3</small></div><div class="card-body"><div class="paper-date">{m['date']}</div><h2>{html.escape(m['title'])}</h2><p>{html.escape(m['subtitle'])}</p><div class="paper-status">{html.escape(m['status'])}</div></div></a></article>'''

def inject_card(path,lang):
    text=path.read_text(encoding='utf-8')
    if SLUG in text:return
    c=card(lang)
    markers=['<div class="papers-grid">','<div class="paper-grid">','<section class="papers-grid">']
    for marker in markers:
        if marker in text:
            text=text.replace(marker,marker+c,1); path.write_text(text,encoding='utf-8'); return
    text=text.replace('</main>',f'<section class="shell"><h2>{"جدیدترین پژوهش" if lang=="fa" else "Latest research"}</h2>{c}</section></main>',1)
    path.write_text(text,encoding='utf-8')

def patch_sitemap():
    p=OUT/'sitemap.xml'; text=p.read_text(encoding='utf-8')
    urls=[f'{BASE}/papers/{SLUG}/',f'{BASE}/fa/papers/{SLUG}/']
    add=''.join(f'  <url><loc>{u}</loc><lastmod>2026-08-14</lastmod></url>\n' for u in urls if u not in text)
    text=text.replace('</urlset>',add+'</urlset>'); p.write_text(text,encoding='utf-8')

def main():
    if not OUT.exists():raise RuntimeError('_site missing; run site/build.py first')
    for lang in ('en','fa'):
        target=OUT/(Path('fa') if lang=='fa' else Path())/'papers'/SLUG/'index.html'; target.parent.mkdir(parents=True,exist_ok=True); target.write_text(page(lang),encoding='utf-8')
    inject_card(OUT/'index.html','en'); inject_card(OUT/'fa'/'index.html','fa'); patch_sitemap()
    print('Added ARP-WCB-2026-01 publication pages, scholarly metadata, social previews, and landing entry.')
if __name__=='__main__':main()
