from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse, unquote

ROOT = Path(__file__).resolve().parent

class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__(); self.links=[]
    def handle_starttag(self, tag, attrs):
        if tag not in {"a","link","script","img"}: return
        d=dict(attrs)
        for key in ("href","src"):
            if d.get(key): self.links.append(d[key])

def resolve(base: Path, href: str):
    href = unquote(href.split("#",1)[0].split("?",1)[0])
    if not href or href.startswith(("http://","https://","mailto:","tel:","data:","javascript:")): return None
    p=(base.parent / href).resolve()
    if href.endswith("/"): p=p/"index.html"
    return p

errors=[]
html_files=list(ROOT.rglob("*.html"))
for html in html_files:
    parser=LinkParser(); parser.feed(html.read_text(encoding="utf-8"))
    for href in parser.links:
        target=resolve(html, href)
        if target is None: continue
        # Links intentionally leaving /site for paper source artifacts are validated at repository level.
        repo_root=ROOT.parent
        if not (str(target).startswith(str(ROOT)) or str(target).startswith(str(repo_root))): continue
        if not target.exists(): errors.append(f"{html.relative_to(ROOT)} -> {href} (missing {target})")

if errors:
    print("Broken local links:")
    print("\n".join(errors))
    raise SystemExit(1)
print(f"Validated {len(html_files)} HTML files: local links OK")
