#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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
 dict(slug='continuity-governance',title_en='Continuity Governance for Long-Duration Critical Infrastructure',title_fa='حکمرانی تداوم برای زیرساخت‌های حیاتی بلندمدت',source_en='papers/2026-continuity-governance/paper.en.md',source_fa='papers/2026-continuity-governance/paper.fa.md',repo='papers/2026-continuity-governance',cover='continuity',kicker_en='Public Working Paper',kicker_fa='مقالهٔ کاری عمومی',date_en='26 August 2026',date_fa='۲۶ اوت ۲۰۲۶',date_iso='2026-08-26',status_en='Public Working Paper',status_fa='مقالهٔ کاری عمومی',version='v0.1.0',topics=['Critical Infrastructure','Continuity Governance','Lunar Governance','Accountability'],image_en='papers/2026-continuity-governance/assets/cover.linkedin.en.png',image_fa='papers/2026-continuity-governance/assets/cover.linkedin.en.png',artifacts=[('English LinkedIn cover','papers/2026-continuity-governance/assets/cover.linkedin.en.png'),('Conceptual architecture','papers/2026-continuity-governance/assets/continuity-architecture.svg'),('Citation metadata','papers/2026-continuity-governance/CITATION.cff')]),
 dict(slug='when-a-claim-meets-a-test',title_en='When a Claim Meets a Test: A Reproducible Case Study of TCSAI, Evidence, Falsifiability, and Human–AI Co-Inquiry',title_fa='وقتی یک ادعا با آزمون روبه‌رو می‌شود',source_en='papers/2026-when-a-claim-meets-a-test/manuscript.en.md',source_fa='papers/2026-when-a-claim-meets-a-test/manuscript.fa.md',repo='papers/2026-when-a-claim-meets-a-test',cover='tcsai',kicker_en='Reproducible Research Case Study',kicker_fa='مطالعهٔ موردی بازتولیدپذیر',date_en='22 August 2026',date_fa='۲۲ اوت ۲۰۲۶',date_iso='2026-08-22',status_en='Documented research record',status_fa='رکورد پژوهشی مستند',version='v1.0 research draft',topics=['Reproducibility','Falsifiability','Evidence Assessment','Human–AI Co-Inquiry'],dossier_fa=[('Record','راهنمای فارسیِ پروندهٔ پژوهش','papers/2026-when-a-claim-meets-a-test/publication/RESEARCH-DOSSIER-GUIDE.fa.md')],artifacts=[('Screen recording (public compressed copy)',f'{BASE}/assets/evidence/tcsai-screen-recording-2026-08-22.m4v'),('Visual session capture (PDF)',f'{BASE}/assets/evidence/tcsai-interface-visual-capture-2026-08-22.pdf'),('Experimental record','papers/2026-when-a-claim-meets-a-test/evidence/transcripts/experimental-record.md'),('Claim–evidence ledger','papers/2026-when-a-claim-meets-a-test/ledger/claim-evidence-ledger.md'),('Reader replication protocol','papers/2026-when-a-claim-meets-a-test/methods/reader-replication-protocol.md'),('Public evidence manifest','papers/2026-when-a-claim-meets-a-test/publication/PUBLIC-EVIDENCE-MANIFEST.md')]),
 dict(slug='we-are-code-that-breathes',title_en='We Are Code That Breathes',title_fa='ما کدی هستیم که نفس می‌کشد',source_en='papers/2026-we-are-code-that-breathes/manuscript-core.md',source_fa='papers/2026-we-are-code-that-breathes/manuscript.fa.md',repo='papers/2026-we-are-code-that-breathes',cover='wcb',kicker_en='Protocol Construction · Case Demonstration',kicker_fa='ساخت پروتکل · نمایش موردی',date_en='August 2026',date_fa='اوت ۲۰۲۶',date_iso='2026-08-14',status_en='Release Candidate v0.3',status_fa='نسخه کاندید انتشار v0.3',version='RC v0.3',topics=['Research Provenance','Human–AI Collaboration','Claim Evolution','PRCEP']),
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
PALETTES={'continuity':('#0b1721','#274754','#9fd9d3'),'tcsai':('#111a20','#294c57','#b9d9cf'),'wcb':('#13252d','#3c6c72','#aad7cf'),'ldg':('#101b25','#315a55','#a7d7cf'),'beyond':('#10161c','#2d495f','#8bbec0'),'relation':('#261c2d','#704b64','#d2a58e'),'reflect':('#161923','#353b5c','#b1a0bf'),'stamp':('#2b241f','#7c624a','#e1bd7e'),'pledge':('#121d24','#325267','#c0a064'),'manifesto':('#17151b','#5b4056','#c98b82'),'rest':('#172026','#49666a','#b8d3c7'),'chapter':('#181b22','#455266','#c1bcaa'),'genesis':('#171a1d','#544638','#d0a067'),'hacs':('#0f2427','#315b57','#a9c9b7')}

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
    rows=''.join(f'<a href="{path if path.startswith("http") else f"{GITHUB}/blob/main/{path}"}" target="_blank" rel="noopener"><span>{html.escape(label)}</span><b>↗</b></a>' for label,path in arts)
    return f'<section class="artifact-panel"><div class="side-label">{heading}</div>{rows}</section>'

def artifact_showcase(p,fa):
    """Put the primary, inspectable TCSAI evidence in the reader's path."""
    if p['slug'] != 'when-a-claim-meets-a-test':
        return ''
    video=f'{BASE}/assets/evidence/tcsai-screen-recording-2026-08-22.m4v'
    pdf=f'{BASE}/assets/evidence/tcsai-interface-visual-capture-2026-08-22.pdf'
    preview=f'{BASE}/assets/evidence/previews/tcsai-visual-capture-preview.png'
    records=[
        ('Experimental record', 'Exact prompts, preserved responses, observations, and test logic.', 'evidence/transcripts/experimental-record.md', 'رکورد آزمایش', 'پرامپت‌های دقیق، پاسخ‌های حفظ‌شده، مشاهده‌ها و منطق آزمون.'),
        ('Claim–evidence ledger', 'Claim-by-claim status, evidence, permitted inference, and limitations.', 'ledger/claim-evidence-ledger.md', 'دفتر ادعا و شواهد', 'وضعیت هر ادعا، شواهد، استنباط مجاز و محدودیت‌ها.'),
        ('Reader replication protocol', 'A practical route for independently repeating the tests.', 'methods/reader-replication-protocol.md', 'پروتکل بازتولید برای خواننده', 'مسیر عملی برای تکرار مستقل آزمون‌ها.'),
        ('Public evidence manifest', 'The public archive, release boundaries, and integrity references.', 'publication/PUBLIC-EVIDENCE-MANIFEST.md', 'فهرست عمومی شواهد', 'آرشیو عمومی، مرزهای انتشار و ارجاع‌های یکپارچگی.'),
    ]
    record_cards=''.join(
        f'<a class="artifact-record" href="{GITHUB}/blob/main/{p["repo"]}/{path}" target="_blank" rel="noopener"><span class="artifact-record-kicker">{html.escape(fa_label if fa else label)}</span><strong>{html.escape(fa_desc if fa else desc)}</strong><b>↗</b></a>'
        for label,desc,path,fa_label,fa_desc in records
    )
    label='شواهدِ قابل‌بررسی' if fa else 'Research artifacts'
    heading='ببینید، بررسی کنید، و آزمون را تکرار کنید.' if fa else 'Watch, inspect, and repeat the test.'
    intro='این‌ها پیوستِ کم‌اهمیت نیستند؛ خودِ مسیرِ قابل‌راستی‌آزمایی پژوهش‌اند.' if fa else 'These are not peripheral attachments; they are the inspectable path through the study.'
    video_title='ویدیوی ضبط جلسهٔ آزمون' if fa else 'Screen recording of the test session'
    video_desc='نسخهٔ فشردهٔ عمومی؛ نسخهٔ خام محلی در سوابق پژوهش ثبت شده است.' if fa else 'Public compressed copy; the local raw recording is logged in the research record.'
    pdf_title='گرفتن تصویری از جلسه (PDF)' if fa else 'Visual session capture (PDF)'
    pdf_desc='پیش‌نمایشِ سند تصویریِ جلسه؛ برای مشاهدهٔ کامل PDF را باز کنید.' if fa else 'Preview of the visual record; open the PDF for the full capture.'
    open_label='باز کردن ↗' if fa else 'Open ↗'
    return f'''<section class="artifact-showcase" aria-label="{label}"><header class="artifact-showcase-head"><div><div class="side-label">{label}</div><h2>{heading}</h2><p>{intro}</p></div></header><div class="artifact-feature-grid"><article class="artifact-feature artifact-feature-video"><video controls preload="metadata" aria-label="{video_title}"><source src="{video}" type="video/mp4">Your browser does not support the video element.</video><div class="artifact-feature-copy"><div class="artifact-card-label">01 · {'ویدیو' if fa else 'Video evidence'}</div><h3>{video_title}</h3><p>{video_desc}</p><a href="{video}" target="_blank" rel="noopener">{open_label}</a></div></article><article class="artifact-feature artifact-feature-pdf"><a class="artifact-preview" href="{pdf}" target="_blank" rel="noopener"><img src="{preview}" alt="{'پیش‌نمایش PDF ثبت تصویری جلسه' if fa else 'Preview of the visual session capture PDF'}"><span>{'۲۲ صفحه ثبت تصویری' if fa else '22-page visual record'}</span></a><div class="artifact-feature-copy"><div class="artifact-card-label">02 · PDF</div><h3>{pdf_title}</h3><p>{pdf_desc}</p><a href="{pdf}" target="_blank" rel="noopener">{open_label}</a></div></article></div><div class="artifact-record-grid">{record_cards}</div></section>'''

WCB_DOSSIER=[
    ('Record', 'Study overview', 'README.md'),
    ('Record', 'Contribution ledger', 'CONTRIBUTIONS.md'),
    ('Record', 'AI disclosure', 'AI_DISCLOSURE.md'),
    ('Record', 'Discussion record', 'DISCUSSION_RECORD.en.md'),
    ('Record', 'References', 'REFERENCES.md'),
    ('Evidence', 'Chronology', 'data/chronology.md'),
    ('Evidence', 'Bilingual alignment', 'data/bilingual-alignment.md'),
    ('Evidence', 'Citation alignment', 'data/citation-alignment.md'),
    ('Evidence', 'Claim–source matrix', 'data/claim-source-matrix.md'),
    ('Evidence', 'Discussion map', 'data/discussion-map.md'),
    ('Evidence', 'Worked claim transitions', 'data/worked-claim-transitions.md'),
    ('Evidence', 'PRCEP schema', 'data/prcep-schema.md'),
    ('Evidence', 'Model mediation manifest', 'data/model-mediation-manifest.md'),
    ('Evidence', 'Formal model', 'data/formal-model-v0.1.md'),
    ('Evidence', 'Literature gap matrix', 'data/literature-gap-matrix.md'),
    ('Evidence', 'Literature audit', 'data/literature-audit-2026-08.md'),
    ('Evidence', 'Literature gate closure', 'data/literature-gate-closure.md'),
    ('Evidence', 'Prior-lineage audit', 'data/prior-lineage-audit.md'),
    ('Evidence', 'Provenance gap audit', 'data/provenance-gap-audit.md'),
    ('Evidence', 'Quote verification matrix', 'data/quote-verification-matrix.md'),
    ('Evidence', 'Evidence policy', 'data/release-evidence-policy.md'),
    ('Meta', 'Meta index', 'meta/README.md'),
    ('Meta', 'Fact-check ledger', 'meta/FACT_CHECK.md'),
    ('Meta', 'Evidence ledger', 'meta/evidence-ledger.md'),
    ('Meta', 'LinkedIn analytics snapshot', 'meta/post-analytics-snapshot.md'),
    ('Meta', 'Temporal provenance investigation', 'meta/temporal-provenance-investigation.md'),
    ('Meta', 'Temporal provenance investigation (Persian)', 'meta/temporal-provenance-investigation.fa.md'),
    ('Evaluation', 'Evaluation plan', 'data/evaluation-plan.md'),
    ('Evaluation', 'Adversarial review', 'data/final-adversarial-review.md'),
    ('Evaluation', 'Pilot protocol', 'evaluation/pilot-protocol.md'),
    ('Evaluation', 'Pilot registry', 'evaluation/pilot-registry.md'),
    ('Evaluation', 'Pilot run template', 'evaluation/pilot-run-template.md'),
    ('Evaluation', 'Preregistration', 'evaluation/preregistration.md'),
    ('Evaluation', 'Condition P', 'evaluation/condition-p.md'),
    ('Evaluation', 'Condition C', 'evaluation/condition-c.md'),
    ('Evaluation', 'Condition C2', 'evaluation/condition-c2.md'),
    ('Evaluation', 'Evaluator instructions', 'evaluation/evaluator-instructions.md'),
    ('Evaluation', 'Scoring rubric', 'evaluation/scoring-rubric.md'),
    ('Evaluation', 'Gold standard', 'evaluation/gold-standard.md'),
    ('Evaluation', 'Matching audit', 'evaluation/matching-audit.md'),
    ('Evaluation', 'Evaluation index', 'evaluation/README.md'),
    ('Evaluation', 'Evaluation questions', 'evaluation/questions.md'),
    ('Evaluation', 'Report template', 'evaluation/report-template.md'),
    ('Evaluation', 'Stimulus freeze manifest', 'evaluation/stimulus-freeze-manifest.md'),
    ('Release', 'Final release audit', 'FINAL_RELEASE_AUDIT.md'),
    ('Release', 'Publication QA', 'data/publication-qa.md'),
    ('Release', 'Freeze gap register', 'data/freeze-gap-register.md'),
]

def dossier_files(p,fa=False):
    if fa and p.get('dossier_fa'): return p['dossier_fa']
    base=p['repo']+'/'
    if p['slug']=='we-are-code-that-breathes':
        return [(group,label,base+path) for group,label,path in WCB_DOSSIER]
    canonical={p['source_en']}
    if p.get('source_fa'): canonical.add(p['source_fa'])
    def usable(path):
        raw=path.read_text(encoding='utf-8').strip()
        return len(raw)>=80 and raw.lower() not in {'test content','placeholder'}
    files=sorted(path for path in (ROOT/p['repo']).rglob('*.md') if path.as_posix().removeprefix(ROOT.as_posix()+'/') not in canonical and usable(path))
    if len(files)<2:return []
    def group_for(path):
        parts=path.relative_to(ROOT/p['repo']).parts
        name=path.name.lower()
        if 'evaluation' in parts or name.startswith('test') or name.startswith('condition-'):return 'Evaluation'
        if any(part in {'data','framework','machine-readable'} for part in parts):return 'Evidence'
        if name in {'changelog.md','license.md'}:return 'Release'
        return 'Record'
    def title_for(path):
        rel=path.relative_to(ROOT/p['repo']).with_suffix('')
        return ' · '.join(part.replace('_',' ').replace('-',' ').title() for part in rel.parts)
    return [(group_for(path),title_for(path),path.relative_to(ROOT).as_posix()) for path in files]

def dossier_key(path):
    return re.sub(r'[^a-z0-9]+','-',path.lower()).strip('-').replace('-md','')

def write_dossier_fragments(p):
    paths={path for _,_,path in dossier_files(p)} | {path for _,_,path in dossier_files(p,fa=True)}
    for path in paths:
        article,_,_=render_markdown(path)
        target=OUT/'dossiers'/p['slug']/(dossier_key(path)+'.html')
        target.parent.mkdir(parents=True,exist_ok=True)
        target.write_text(f'<article class="dossier-document">{article}</article>',encoding='utf-8')

def dossier_panel(p,fa,hero=False):
    files=dossier_files(p,fa)
    if not files:return ''
    base=p['repo']+'/'
    label='پروندهٔ پژوهش' if fa else 'Research dossier'
    is_wcb=p['slug']=='we-are-code-that-breathes'
    title=('مسیرِ دگرگونیِ ادعا را خودتان بررسی کنید.' if fa else 'Inspect how the claim changed.') if is_wcb else ('رکوردِ پژوهش را ورق بزنید.' if fa else 'Explore the working record.')
    intro=('این یک فهرست منابع نیست؛ رکوردِ قابل‌بررسیِ چالش‌ها، اصلاح‌ها و آزمونی است که استعاره‌ی آغازین را به یک پروتکلِ قابل‌ردشدن تبدیل کرد.' if fa else 'Not a bibliography: an inspectable record of the challenges, corrections, and tests that turned an opening metaphor into a falsifiable protocol.') if is_wcb else ('یادداشت‌های همراه، روش، مدل‌ها و اسناد انتشار را بدون خروج از همین صفحه بخوانید.' if fa else 'Read the companion notes, methods, models, and release records without leaving this page.')
    open_label=('ورود به رکورد شواهد' if fa else 'Enter the evidence record') if is_wcb else ('باز کردن پروندهٔ پژوهش' if fa else 'Open the research dossier')
    grouped={}
    for group,doc_title,path in files: grouped.setdefault(group,[]).append((doc_title,path))
    pathways=([
        ('نقطهٔ آغاز: گاه‌شمار', 'Start: origin chronology', base+'data/chronology.md'),
        ('تغییرها: انتقال‌های ادعا', 'See: claim transitions', base+'data/worked-claim-transitions.md'),
        ('آزمون: طرح ارزیابی', 'Test: evaluation design', base+'data/evaluation-plan.md'),
    ] if is_wcb else [(f'شروع: {items[0][0]}',f'Start: {items[0][0]}',items[0][1]) for _,items in list(grouped.items())[:3]])
    overview=''.join(f'<button type="button" class="dossier-quick" data-dossier-open data-dossier-key="{dossier_key(path)}"><span>{fa_label if fa else en_label}</span><b>↗</b></button>' for fa_label,en_label,path in pathways)
    dialog_groups=[]
    for group,items in grouped.items():
        group_label={'Record':'رکورد اصلی','Evidence':'شواهد و روش','Meta':'فراپژوهش پس از انتشار','Evaluation':'ارزیابی','Release':'کنترل انتشار'}[group] if fa else group
        buttons=''.join(f'<button type="button" data-dossier-load data-dossier-key="{dossier_key(path)}" data-dossier-path="{html.escape(path,quote=True)}" data-dossier-title="{html.escape(title,quote=True)}">{html.escape(title)}</button>' for title,path in items)
        dialog_groups.append(f'<section class="dossier-group"><h3>{group_label}</h3>{buttons}</section>')
    docs={dossier_key(path):path for _,_,path in files}
    dialog=f'''<dialog class="dossier-dialog" data-dossier-dialog><div class="dossier-frame"><aside class="dossier-nav"><div class="dossier-nav-head"><span class="side-label">{label}</span><button type="button" class="dossier-close" data-dossier-close aria-label="{'بستن' if fa else 'Close'}">×</button></div><p>{'نسخه‌های منبع به زبان اصلی حفظ می‌شوند.' if fa else 'Source documents remain in their original language.'}</p>{''.join(dialog_groups)}</aside><section class="dossier-reader"><header><div><span class="side-label">{'سند منبع' if fa else 'Source document'}</span><h2 data-dossier-title>{'یک سند را انتخاب کنید' if fa else 'Choose a document'}</h2></div><a data-dossier-github target="_blank" rel="noopener" hidden>{'مشاهده در GitHub ↗' if fa else 'Open on GitHub ↗'}</a></header><div class="dossier-loading" data-dossier-loading>{'از فهرستِ کناری انتخاب کنید.' if fa else 'Select an item from the left.'}</div><div class="dossier-content" data-dossier-content></div></section></div></dialog>'''
    variant=' dossier-panel--hero' if hero else ''
    proof=('۴۱ سندِ اصلی <i></i> ۷ انتقال ادعا <i></i> ۵ طبقهٔ شواهد' if fa else '41 primary documents <i></i> 7 claim transitions <i></i> 5 evidence classes') if is_wcb else (f'{len(files)} سندِ همراه <i></i> منبع و نسخه‌بندی قابل‌بررسی' if fa else f'{len(files)} supporting documents <i></i> inspectable source and version record')
    first_path=pathways[0][2]
    return f'''<section class="dossier-panel{variant}"><div class="dossier-panel-copy"><div class="side-label">{label}</div><h2>{title}</h2><p>{intro}</p><div class="dossier-proof">{proof}</div></div><button type="button" class="dossier-open" data-dossier-open data-dossier-key="{dossier_key(first_path)}">{open_label} <span>↗</span></button><div class="dossier-quick-list">{overview}</div></section>{dialog}'''

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
    schema={'@context':'https://schema.org','@type':'ScholarlyArticle','headline':title,'description':summary,'datePublished':p['date_iso'],'dateModified':p['date_iso'],'inLanguage':lang,'author':{'@type':'Person','name':'Amir Ahmadi','sameAs':[ORCID,'https://github.com/axamir']},'url':url,'image':og,'version':p['version'],'keywords':p['topics'],'isPartOf':{'@type':'CollectionPage','name':'Amir Ahmadi Research','url':home}}
    return f'''<!doctype html><html lang="{lang}"{direction}><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)} — Amir Ahmadi Research</title><meta name="description" content="{html.escape(summary,quote=True)}"><link rel="canonical" href="{url}"><link rel="alternate" hreflang="en" href="{paper_url(p,'en')}"><link rel="alternate" hreflang="fa" href="{paper_url(p,'fa')}"><link rel="alternate" hreflang="x-default" href="{paper_url(p,'en')}"><link rel="icon" href="{BASE}/assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="{BASE}/assets/paper.css"><link rel="stylesheet" href="{BASE}/assets/polish.css"><meta property="og:type" content="article"><meta property="og:title" content="{html.escape(title,quote=True)}"><meta property="og:description" content="{html.escape(summary,quote=True)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{og}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:image" content="{og}"><meta name="citation_title" content="{html.escape(title,quote=True)}"><meta name="citation_author" content="Amir Ahmadi"><meta name="citation_publication_date" content="{p['date_iso']}"><meta name="citation_fulltext_html_url" content="{url}"><script type="application/ld+json">{json.dumps(schema,ensure_ascii=False)}</script></head><body class="reading-page {'rtl' if fa else ''}" data-paper-slug="{p['slug']}"><div class="reading-progress" aria-hidden="true"><span></span></div><header class="top"><div class="shell nav"><a class="brand" href="{home}">@@ Amir Ahmadi Research</a><nav class="navlinks"><a href="{home}">{back}</a><a href="{repo_url}" target="_blank" rel="noopener">GitHub ↗</a></nav></div></header><main><section class="reading-hero"><div class="shell reading-shell"><div class="eyebrow">{html.escape(kicker)}</div><h1>{html.escape(title)}</h1><p class="reading-note">{html.escape(provenance)}</p><div class="reading-meta"><span>{html.escape(date)}</span><span>{html.escape(p['version'])}</span><span>{html.escape(status)}</span><span>{read_label}</span></div><div class="topic-row">{topics}</div><div class="actions"><a class="btn primary" href="#paper">{'خواندن مقاله' if fa else 'Read full paper'} ↓</a><a class="btn" href="{alt}">{'English edition' if fa else 'نسخه فارسی'} ↗</a><a class="btn" href="{source_url}" target="_blank" rel="noopener">{source_label} ↗</a></div>{dossier_panel(p,fa,hero=True)}{cover}</div></section>{artifact_showcase(p,fa)}<section class="shell reading-shell reading-layout" id="paper"><article class="markdown-body">{article}</article><aside class="reading-side"><div class="side-card publication-card"><div class="side-label">{'هویت انتشار' if fa else 'Publication identity'}</div><dl><dt>{'نویسنده' if fa else 'Author'}</dt><dd>Amir Ahmadi</dd><dt>ORCID</dt><dd><a href="{ORCID}" target="_blank" rel="noopener">0009-0000-0614-6869 ↗</a></dd><dt>{'نسخه' if fa else 'Version'}</dt><dd>{html.escape(p['version'])}</dd><dt>{'وضعیت' if fa else 'Status'}</dt><dd>{html.escape(status)}</dd><dt>{'زبان' if fa else 'Language'}</dt><dd>{'فارسی' if fa else 'English'}</dd></dl></div><div class="side-card citation-card"><div class="side-label">{cite_label}</div><p>{html.escape(citation)}</p><button class="copy-citation" data-citation="{html.escape(citation,quote=True)}">{'کپی استناد' if fa else 'Copy citation'}</button></div><div class="side-card provenance-card"><div class="side-label">{'منبع و شواهد' if fa else 'Source & provenance'}</div><a href="{source_url}" target="_blank" rel="noopener">{source_label} ↗</a><a href="{repo_url}" target="_blank" rel="noopener">{repo_label} ↗</a><a href="{GITHUB}/commits/main/{source}" target="_blank" rel="noopener">{'تاریخچه نسخه' if fa else 'Revision history'} ↗</a></div>{artifact_links(p,fa)}</aside></section></main><footer><div class="shell">© 2026 Amir Ahmadi · Independent Research · <a href="{GITHUB}">Source archive</a></div></footer><script src="{BASE}/assets/app.js"></script></body></html>'''

def inject_home_metadata(path,lang):
    text=path.read_text(encoding='utf-8'); fa=lang=='fa'; url=f'{BASE}/fa/' if fa else f'{BASE}/'; title='پژوهش‌های امیر احمدی' if fa else 'Amir Ahmadi Research'; desc='آرشیو پژوهش‌های مستقل درباره سامانه‌های انسان–هوش مصنوعی، حکمرانی، هویت و معماری‌های قابل راستی‌آزمایی.' if fa else 'Independent research on human–AI systems, governance, identity, decision intelligence and verifiable architectures.'
    text=re.sub(r'<link rel="canonical"[^>]*>\s*','',text,flags=re.I)
    block=f'<link rel="canonical" href="{url}"><link rel="alternate" hreflang="en" href="{BASE}/"><link rel="alternate" hreflang="fa" href="{BASE}/fa/"><link rel="alternate" hreflang="x-default" href="{BASE}/"><link rel="stylesheet" href="{BASE}/assets/polish.css"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:type" content="website"><meta property="og:url" content="{url}"><meta property="og:image" content="{BASE}/assets/og-default.svg"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{title}"><meta name="twitter:description" content="{desc}"><meta name="twitter:image" content="{BASE}/assets/og-default.svg">'
    text=re.sub(r'</head>',block+'</head>',text,count=1,flags=re.I); path.write_text(text,encoding='utf-8')

def write_sitemap():
    urls=[f'{BASE}/',f'{BASE}/fa/']
    for p in PAPERS:urls += [paper_url(p,lang) for lang in p.get('languages',('en','fa'))]
    lines=['<?xml version="1.0" encoding="UTF-8"?>','<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']+[f'  <url><loc>{html.escape(u)}</loc><lastmod>2026-08-26</lastmod></url>' for u in urls]+['</urlset>']; (OUT/'sitemap.xml').write_text('\n'.join(lines),encoding='utf-8')

def enforce_publication_surfaces():
    """Make the international surface English-only and Persian canonical-to-English."""
    english_pages=[OUT/'index.html', *sorted((OUT/'papers').glob('*/index.html'))]
    for path in english_pages:
        text=path.read_text(encoding='utf-8')
        text=text.replace('<span>EN / FA</span>','').replace('<span>EN/FA</span>','')
        text=re.sub(r'<link rel="alternate" hreflang="fa"[^>]*>','',text)
        text=re.sub(r'<a class="btn" href="[^"]*/fa/papers/[^"]+/">نسخه فارسی ↗</a>','',text)
        text=text.replace('This page is generated only from the canonical English Markdown; the Persian edition is published separately.',
                          'Canonical full-text research record generated from the maintained English source.')
        path.write_text(text,encoding='utf-8')
    for path in sorted((OUT/'fa'/'papers').glob('*/index.html')):
        text=path.read_text(encoding='utf-8'); slug=path.parent.name; canonical=f'{BASE}/papers/{slug}/'
        text=text.replace('این صفحه فقط از Markdown فارسی نهایی ساخته شده و نسخه انگلیسی در مسیر انگلیسی مستقل است.',
                          'این صفحه لایهٔ فارسیِ فهم، تفسیر و صورت‌بندی امیر احمدی است. رکورد علمی و مرجع اصلی پژوهش در نسخهٔ انگلیسی نگهداری می‌شود.')
        text=text.replace('English edition ↗','مشاهده پژوهش مرجع انگلیسی ↗')
        text=re.sub(r'<link rel="canonical" href="[^"]+">',f'<link rel="canonical" href="{canonical}">',text,count=1)
        path.write_text(text,encoding='utf-8')

def main():
    for p in PAPERS:
        for lang in p.get('languages',('en','fa')): render_markdown(p[f'source_{lang}'])
    if OUT.exists():shutil.rmtree(OUT)
    shutil.copytree(SOURCE,OUT,ignore=shutil.ignore_patterns('build.py','validate.py','__pycache__'))
    inject_home_metadata(OUT/'index.html','en'); inject_home_metadata(OUT/'fa'/'index.html','fa')
    for p in PAPERS:
        write_dossier_fragments(p)
        for lang in p.get('languages',('en','fa')):
            generate_og(p,lang); target=OUT/(Path('fa') if lang=='fa' else Path())/'papers'/p['slug']/'index.html'; target.parent.mkdir(parents=True,exist_ok=True); target.write_text(paper_page(p,lang),encoding='utf-8')
    enforce_publication_surfaces(); write_sitemap(); print(f"Built Research Hub with {sum(len(p.get('languages', ('en', 'fa'))) for p in PAPERS)} paper editions.")
if __name__=='__main__':main()
