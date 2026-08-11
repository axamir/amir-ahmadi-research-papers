#!/usr/bin/env python3
"""Publication-surface policy.

English is the canonical international research surface and contains no visible
Persian-edition affordances. Persian pages are an interpretive layer that point
back to the canonical English research record.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "_site"
BASE = "https://axamir.github.io/amir-ahmadi-research-papers"


def clean_english_page(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    # Remove visible bilingual badges and Persian-edition calls to action.
    text = text.replace('<span>EN / FA</span>', '')
    text = text.replace('<span>EN/FA</span>', '')
    text = re.sub(r'<a class="btn" href="[^"]*/fa/papers/[^"]+/">نسخه فارسی ↗</a>', '', text)
    text = re.sub(r'<a[^>]+href="[^"]*/fa/[^"]*"[^>]*>.*?</a>', '', text, flags=re.S)
    # English publication pages should not announce or advertise a Persian edition.
    text = text.replace('This page is generated only from the canonical English Markdown; the Persian edition is published separately.',
                        'Canonical full-text research record generated from the maintained English source.')
    # Remove Persian alternate metadata from the international surface.
    text = re.sub(r'<link rel="alternate" hreflang="fa"[^>]*>', '', text)
    path.write_text(text, encoding="utf-8")


def enrich_persian_page(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    slug = path.parent.name
    english = f"{BASE}/papers/{slug}/"
    # Reframe Persian as the author's interpretive layer, not a competing canonical edition.
    text = text.replace('این صفحه فقط از Markdown فارسی نهایی ساخته شده و نسخه انگلیسی در مسیر انگلیسی مستقل است.',
                        'این صفحه لایهٔ فارسیِ فهم، تفسیر و صورت‌بندی پژوهش است. رکورد علمی و مرجع اصلی پژوهش در نسخهٔ انگلیسی نگهداری می‌شود.')
    text = text.replace('English edition ↗', 'مشاهده پژوهش مرجع انگلیسی ↗')
    # Persian pages explicitly point to the canonical English research record.
    if '<link rel="canonical"' in text:
        text = re.sub(r'<link rel="canonical" href="[^"]+">', f'<link rel="canonical" href="{english}">', text, count=1)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    home = OUT / 'index.html'
    if home.exists():
        clean_english_page(home)
    papers = OUT / 'papers'
    if papers.exists():
        for page in papers.glob('*/index.html'):
            clean_english_page(page)
    fa = OUT / 'fa' / 'papers'
    if fa.exists():
        for page in fa.glob('*/index.html'):
            enrich_persian_page(page)
    print('Applied international/Persian publication-surface policy.')


if __name__ == '__main__':
    main()
