#!/usr/bin/env python3
"""Build the static Research Hub into _site with publication metadata.

Source files stay readable and source-first in /site. The build step copies them and
injects canonical URLs, social metadata, favicon/manifest links, and ScholarlyArticle
JSON-LD into public paper pages.
"""
from __future__ import annotations

import html
import json
import re
import shutil
from pathlib import Path

SOURCE = Path(__file__).resolve().parent
ROOT = SOURCE.parent
OUT = ROOT / "_site"
BASE = "https://axamir.github.io/amir-ahmadi-research-papers"
OG_IMAGE = f"{BASE}/assets/og-default.svg"


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


def inject(path: Path, rel: Path) -> None:
    text = path.read_text(encoding="utf-8")
    if "</head>" not in text.lower():
        return

    title = match(r"<title>(.*?)</title>", text, "Amir Ahmadi Research")
    desc = match(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']\s*/?>', text,
                 "Independent research on human–AI systems, governance, identity and verifiable architectures.")
    canonical = canonical_for(rel)
    is_paper = rel.parts[:1] == ("papers",) and rel.name == "index.html"

    # Normalize OG metadata so each output page has one authoritative set.
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
        '<meta property="og:image:width" content="1200">',
        '<meta property="og:image:height" content="630">',
        '<meta name="twitter:card" content="summary_large_image">',
        f'<meta name="twitter:title" content="{html.escape(title, quote=True)}">',
        f'<meta name="twitter:description" content="{html.escape(desc, quote=True)}">',
        f'<meta name="twitter:image" content="{OG_IMAGE}">',
    ]

    if is_paper:
        paper_title = title.split(" — Amir Ahmadi Research")[0]
        schema = {
            "@context": "https://schema.org",
            "@type": "ScholarlyArticle",
            "headline": paper_title,
            "description": desc,
            "url": canonical,
            "author": {
                "@type": "Person",
                "name": "Amir Ahmadi",
                "sameAs": [
                    "https://orcid.org/0009-0000-0614-6869",
                    "https://github.com/axamir",
                ],
            },
            "isPartOf": {"@type": "CollectionPage", "name": "Amir Ahmadi Research", "url": f"{BASE}/"},
            "inLanguage": "en",
        }
        meta.append('<script type="application/ld+json">' + json.dumps(schema, ensure_ascii=False) + '</script>')

    block = "\n" + "\n".join(meta) + "\n"
    text = re.sub(r"</head>", block + "</head>", text, count=1, flags=re.I)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    shutil.copytree(SOURCE, OUT, ignore=shutil.ignore_patterns("build.py", "validate.py", "__pycache__"))
    for page in OUT.rglob("*.html"):
        inject(page, page.relative_to(OUT))
    print(f"Built Research Hub: {OUT}")


if __name__ == "__main__":
    main()
