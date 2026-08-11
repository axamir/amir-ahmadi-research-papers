#!/usr/bin/env python3
"""Build the Research Hub into _site.

The public website is a reading layer over the canonical Markdown archive. English
pages render only English source Markdown; Persian pages render only Persian source
Markdown. GitHub remains the source of truth and every article links to its canonical
file and source directory.
"""
from __future__ import annotations

import html
import json
import re
import shutil
from pathlib import Path

import markdown

SOURCE = Path(__file__).resolve().parent
ROOT = SOURCE.parent
OUT = ROOT / "_site"
BASE = "https://axamir.github.io/amir-ahmadi-research-papers"
GITHUB = "https://github.com/axamir/amir-ahmadi-research-papers"
RAW = "https://raw.githubusercontent.com/axamir/amir-ahmadi-research-papers/main"
OG_IMAGE = f"{BASE}/assets/og-default.svg"

PAPERS = [
    {
        "slug": "living-decision-governance",
        "title_en": "Living Decision Governance",
        "title_fa": "حکمرانی زنده تصمیم",
        "source_en": "papers/2026-living-decision-governance/LDG_COMPLETE.md",
        "source_fa": "papers/2026-living-decision-governance/LDG_COMPLETE.fa.md",
        "repo": "papers/2026-living-decision-governance",
        "cover": "ldg",
        "kicker_en": "Executable Research Artifact · LDG",
        "kicker_fa": "اثر پژوهشی اجرایی · LDG",
        "date_en": "August 2026",
        "date_fa": "اوت ۲۰۲۶",
    },
    {
        "slug": "beyond-intelligence-ai-evolution",
        "title_en": "Beyond Intelligence — AI Evolution",
        "title_fa": "فراتر از هوشمندی — تکامل هوش مصنوعی",
        "source_en": "papers/beyond-intelligence-ai-evolution/paper-en.md",
        "source_fa": "papers/beyond-intelligence-ai-evolution/paper-fa.md",
        "repo": "papers/beyond-intelligence-ai-evolution",
        "cover": "beyond",
        "kicker_en": "Research Paper",
        "kicker_fa": "مقاله پژوهشی",
        "date_en": "August 2026",
        "date_fa": "اوت ۲۰۲۶",
        "image_en": "papers/beyond-intelligence-ai-evolution/figures/cover-beyond-intelligence-en-v1.0.png",
        "image_fa": "papers/beyond-intelligence-ai-evolution/figures/cover-beyond-intelligence-fa-v1.0.png",
    },
    {
        "slug": "relational-co-evolution",
        "title_en": "From Green Personalisation to Relational Co-Evolution",
        "title_fa": "از شخصی‌سازی سبز تا هم‌تکاملی رابطه‌ای",
        "source_en": "papers/2026-relational-co-evolution/paper.en.md",
        "source_fa": "papers/2026-relational-co-evolution/paper.fa.md",
        "repo": "papers/2026-relational-co-evolution",
        "cover": "relation",
        "kicker_en": "Public Working Paper",
        "kicker_fa": "مقاله کاری عمومی",
        "date_en": "July 2026",
        "date_fa": "ژوئیه ۲۰۲۶",
        "image_en": "papers/2026-relational-co-evolution/cover.linkedin.png",
        "image_fa": "papers/2026-relational-co-evolution/cover.linkedin.png",
    },
    {
        "slug": "reflections-and-their-owners",
        "title_en": "Reflections and Their Owners",
        "title_fa": "بازتاب‌ها و صاحبانشان",
        "source_en": "papers/2026-reflections-and-their-owners/paper.md",
        "source_fa": "papers/2026-reflections-and-their-owners/paper.fa.md",
        "repo": "papers/2026-reflections-and-their-owners",
        "cover": "reflect",
        "kicker_en": "Research Paper",
        "kicker_fa": "مقاله پژوهشی",
        "date_en": "July 2026",
        "date_fa": "ژوئیه ۲۰۲۶",
    },
    {
        "slug": "from-stamp-to-alliance",
        "title_en": "From Stamp to Alliance: Redefining AI Certification",
        "title_fa": "از مُهر تا اتحاد: بازتعریف گواهی هوش مصنوعی",
        "source_en": "papers/2026-from-stamp-to-alliance/paper.en.md",
        "source_fa": "papers/2026-from-stamp-to-alliance/paper.fa.md",
        "repo": "papers/2026-from-stamp-to-alliance",
        "cover": "stamp",
        "kicker_en": "Published Research",
        "kicker_fa": "پژوهش منتشرشده",
        "date_en": "July 2026",
        "date_fa": "ژوئیه ۲۰۲۶",
    },
    {
        "slug": "from-money-to-pledge",
        "title_en": "From Money to Pledge",
        "title_fa": "از پول تا پیمان",
        "source_en": "papers/2026-from-pledge-to-sovereignty/paper.en.md",
        "source_fa": "papers/2026-from-pledge-to-sovereignty/paper.fa.md",
        "repo": "papers/2026-from-pledge-to-sovereignty",
        "cover": "pledge",
        "kicker_en": "Published Research",
        "kicker_fa": "پژوهش منتشرشده",
        "date_en": "July 2026",
        "date_fa": "ژوئیه ۲۰۲۶",
    },
    {
        "slug": "i-you-and-we",
        "title_en": "I, You, and We",
        "title_fa": "من، تو و ما",
        "source_en": "papers/2026-human-ai-co-creation-manifesto/paper.en.md",
        "source_fa": "papers/2026-human-ai-co-creation-manifesto/paper.fa.md",
        "repo": "papers/2026-human-ai-co-creation-manifesto",
        "cover": "manifesto",
        "kicker_en": "Human–AI Co-Creation Manifesto",
        "kicker_fa": "مانیفست هم‌آفرینی انسان–هوش مصنوعی",
        "date_en": "July 2026",
        "date_fa": "ژوئیه ۲۰۲۶",
    },
    {
        "slug": "designing-rest",
        "title_en": "Designing Rest",
        "title_fa": "طراحی استراحت",
        "source_en": "papers/2026-designing-rest/paper.en.md",
        "source_fa": "papers/2026-designing-rest/paper.fa.md",
        "repo": "papers/2026-designing-rest",
        "cover": "rest",
        "kicker_en": "Research Essay",
        "kicker_fa": "جستار پژوهشی",
        "date_en": "July 2026",
        "date_fa": "ژوئیه ۲۰۲۶",
    },
    {
        "slug": "before-the-first-chapter",
        "title_en": "Before the First Chapter",
        "title_fa": "پیش از فصل اول",
        "source_en": "papers/2026-before-the-first-chapter/paper.en.md",
        "source_fa": "papers/2026-before-the-first-chapter/paper.fa.md",
        "repo": "papers/2026-before-the-first-chapter",
        "cover": "chapter",
        "kicker_en": "Research Essay",
        "kicker_fa": "جستار پژوهشی",
        "date_en": "July 2026",
        "date_fa": "ژوئیه ۲۰۲۶",
    },
    {
        "slug": "from-genesis-to-witness",
        "title_en": "From Genesis to Witness",
        "title_fa": "از پیدایش تا شاهد",
        "source_en": "papers/2026-from-genesis-to-witness/paper.md",
        "source_fa": "papers/2026-from-genesis-to-witness/paper.fa.md",
        "repo": "papers/2026-from-genesis-to-witness",
        "cover": "genesis",
        "kicker_en": "Research Paper",
        "kicker_fa": "مقاله پژوهشی",
        "date_en": "June 2026",
        "date_fa": "ژوئن ۲۰۲۶",
    },
    {
        "slug": "beyond-models-hacs",
        "title_en": "Beyond Models: Toward Enduring Human–AI Collaborative Systems",
        "title_fa": "فراتر از مدل‌ها: به‌سوی سامانه‌های پایدار همکاری انسان–هوش مصنوعی",
        "source_en": "2026/beyond-models-hacs/paper.en.md",
        "source_fa": "2026/beyond-models-hacs/paper.fa.md",
        "repo": "2026/beyond-models-hacs",
        "cover": "hacs",
        "kicker_en": "HACS Framework",
        "kicker_fa": "چارچوب HACS",
        "date_en": "2026",
        "date_fa": "۲۰۲۶",
    },
]


def canonical_for(rel: Path) -> str:
    posix = rel.as_posix()
    if posix == "index.html":
        return f"{BASE}/"
    if posix.endswith("/index.html"):
        return f"{BASE}/{posix[:-10]}"
    return f"{BASE}/{posix}"


def match(pattern: str, text: str, default: str = "") -> str:
    m = re.search(pattern, text, flags=re.I | re.S)
    return html.unescape(m.group(1).strip()) if m else default


def strip_frontmatter(text: str) -> str:
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            return text[end + 5 :]
    return text


def rewrite_relative_targets(text: str, source_path: Path) -> str:
    """Make relative Markdown links/images work from the generated website."""
    source_dir = source_path.parent.as_posix()

    def repl(m: re.Match[str]) -> str:
        prefix, target, suffix = m.group(1), m.group(2), m.group(3)
        t = target.strip()
        if re.match(r"^(https?://|mailto:|#|data:)", t, flags=re.I):
            return m.group(0)
        clean = (Path(source_dir) / t).as_posix()
        if prefix.startswith("!"):
            url = f"{RAW}/{clean}"
        else:
            url = f"{GITHUB}/blob/main/{clean}"
        return f"{prefix}{url}{suffix}"

    return re.sub(r"(!?\[[^\]]*\]\()([^\)]+)(\))", repl, text)


def render_markdown(source_rel: str) -> tuple[str, int]:
    source_path = ROOT / source_rel
    if not source_path.exists():
        return '<div class="source-warning">Canonical Markdown source is not available.</div>', 0
    raw = source_path.read_text(encoding="utf-8")
    if len(raw.strip()) < 80:
        warning = (
            '<div class="source-warning"><strong>Source integrity notice.</strong> '
            'The canonical Markdown currently contains only placeholder text. '
            'This page will automatically render the complete article when the source file is restored.</div>'
        )
        return warning + markdown.markdown(raw, extensions=["extra", "tables", "fenced_code", "sane_lists"]), len(raw)
    body = rewrite_relative_targets(strip_frontmatter(raw), Path(source_rel))
    rendered = markdown.markdown(
        body,
        extensions=["extra", "tables", "fenced_code", "sane_lists", "toc"],
        output_format="html5",
    )
    return rendered, len(raw)


def paper_page(paper: dict, lang: str) -> str:
    fa = lang == "fa"
    source_rel = paper[f"source_{lang}"]
    title = paper[f"title_{lang}"]
    kicker = paper[f"kicker_{lang}"]
    date = paper[f"date_{lang}"]
    article, chars = render_markdown(source_rel)
    words = max(1, chars // (5 if not fa else 4))
    read_minutes = max(1, round(words / (220 if not fa else 180)))
    source_url = f"{GITHUB}/blob/main/{source_rel}"
    repo_url = f"{GITHUB}/tree/main/{paper['repo']}"
    hub_url = "../../" if not fa else "../../../fa/"
    css_url = "../../assets/paper.css" if not fa else "../../../assets/paper.css"
    command_js = "../../assets/app.js" if not fa else "../../../assets/app.js"
    html_lang = "fa" if fa else "en"
    direction = ' dir="rtl"' if fa else ""
    back = "بازگشت به آرشیو" if fa else "All papers"
    source_label = "Markdown منبع" if fa else "Canonical Markdown"
    repo_label = "مخزن مقاله" if fa else "Paper repository"
    full_label = "متن کامل مقاله" if fa else "Full paper"
    reading = f"حدود {read_minutes} دقیقه مطالعه" if fa else f"~{read_minutes} min read"
    note = (
        "این صفحه مستقیماً از نسخه نهایی Markdown فارسی ساخته می‌شود. نسخه انگلیسی در سایت انگلیسی جداست."
        if fa else
        "This page is generated directly from the canonical English Markdown. The Persian text lives only in the Persian site."
    )
    image_rel = paper.get(f"image_{lang}")
    if image_rel:
        cover = f'<figure class="paper-image-cover"><img src="{RAW}/{image_rel}" alt="{html.escape(title)} cover"></figure>'
    else:
        cover = (
            f'<div class="reading-cover {paper["cover"]}"><span>{html.escape(kicker)}</span>'
            f'<strong>{html.escape(title)}</strong><small>{html.escape(date)}</small></div>'
        )
    return f'''<!doctype html>
<html lang="{html_lang}"{direction}>
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)} — Amir Ahmadi Research</title>
<meta name="description" content="{html.escape(note, quote=True)}">
<link rel="stylesheet" href="{css_url}">
</head>
<body class="reading-page {'rtl' if fa else ''}">
<header class="top"><div class="shell nav">
<a class="brand" href="{hub_url}">@@ Amir Ahmadi Research</a>
<nav class="navlinks"><a href="{hub_url}">{back}</a><a href="{repo_url}" target="_blank" rel="noopener">GitHub ↗</a></nav>
</div></header>
<main class="shell reading-shell">
<section class="reading-hero">
<div class="eyebrow">{html.escape(date)} · {html.escape(kicker)}</div>
<h1>{html.escape(title)}</h1>
<p class="reading-note">{note}</p>
<div class="reading-meta"><span>{reading}</span><span>Amir Ahmadi</span><span>ORCID 0009-0000-0614-6869</span></div>
<div class="actions"><a class="btn primary" href="#full-paper">{full_label}</a><a class="btn" href="{source_url}" target="_blank" rel="noopener">{source_label} ↗</a><a class="btn" href="{repo_url}" target="_blank" rel="noopener">{repo_label} ↗</a></div>
</section>
{cover}
<div class="reading-layout" id="full-paper">
<article class="markdown-body">{article}</article>
<aside class="reading-side"><div class="side-card"><div class="eyebrow">Source of truth</div><p>{html.escape(source_rel)}</p><a href="{source_url}" target="_blank" rel="noopener">{source_label} ↗</a></div></aside>
</div>
</main>
<footer><div class="shell">Amir Ahmadi · Independent Researcher · Source-first research archive</div></footer>
<script src="{command_js}"></script>
</body></html>'''


def generate_papers() -> None:
    for paper in PAPERS:
        en_dir = OUT / "papers" / paper["slug"]
        fa_dir = OUT / "fa" / "papers" / paper["slug"]
        en_dir.mkdir(parents=True, exist_ok=True)
        fa_dir.mkdir(parents=True, exist_ok=True)
        (en_dir / "index.html").write_text(paper_page(paper, "en"), encoding="utf-8")
        (fa_dir / "index.html").write_text(paper_page(paper, "fa"), encoding="utf-8")

    # Persian archive cards must stay inside the Persian reading layer.
    fa_index = OUT / "fa" / "index.html"
    if fa_index.exists():
        text = fa_index.read_text(encoding="utf-8")
        text = text.replace('href="../papers/', 'href="papers/')
        fa_index.write_text(text, encoding="utf-8")


def inject(path: Path, rel: Path) -> None:
    text = path.read_text(encoding="utf-8")
    if "</head>" not in text.lower():
        return
    title = match(r"<title>(.*?)</title>", text, "Amir Ahmadi Research")
    desc = match(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']\s*/?>', text,
                 "Independent research on human–AI systems, governance, identity and verifiable architectures.")
    canonical = canonical_for(rel)
    parts = rel.parts
    is_paper = rel.name == "index.html" and (parts[:1] == ("papers",) or parts[:2] == ("fa", "papers"))
    language = "fa" if parts[:1] == ("fa",) else "en"
    text = re.sub(r'<meta\s+property=["\']og:[^>]+>\s*', '', text, flags=re.I)
    text = re.sub(r'<link\s+rel=["\']canonical["\'][^>]*>\s*', '', text, flags=re.I)
    meta = [
        f'<link rel="canonical" href="{canonical}">',
        f'<link rel="icon" href="{BASE}/assets/favicon.svg" type="image/svg+xml">',
        f'<link rel="manifest" href="{BASE}/manifest.webmanifest">',
        f'<meta property="og:title" content="{html.escape(title, quote=True)}">',
        f'<meta property="og:description" content="{html.escape(desc, quote=True)}">',
        f'<meta property="og:type" content="{"article" if is_paper else "website"}">',
        f'<meta property="og:url" content="{canonical}">',
        f'<meta property="og:image" content="{OG_IMAGE}">',
        '<meta name="twitter:card" content="summary_large_image">',
    ]
    if is_paper:
        schema = {
            "@context": "https://schema.org",
            "@type": "ScholarlyArticle",
            "headline": title.split(" — Amir Ahmadi Research")[0],
            "description": desc,
            "url": canonical,
            "author": {"@type": "Person", "name": "Amir Ahmadi", "sameAs": ["https://orcid.org/0009-0000-0614-6869", "https://github.com/axamir"]},
            "isPartOf": {"@type": "CollectionPage", "name": "Amir Ahmadi Research", "url": f"{BASE}/"},
            "inLanguage": language,
        }
        meta.append('<script type="application/ld+json">' + json.dumps(schema, ensure_ascii=False) + '</script>')
    text = re.sub(r"</head>", "\n" + "\n".join(meta) + "\n</head>", text, count=1, flags=re.I)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    shutil.copytree(SOURCE, OUT, ignore=shutil.ignore_patterns("build.py", "validate.py", "__pycache__"))
    generate_papers()
    for page in OUT.rglob("*.html"):
        inject(page, page.relative_to(OUT))
    print(f"Built bilingual full-text Research Hub: {OUT}")


if __name__ == "__main__":
    main()
