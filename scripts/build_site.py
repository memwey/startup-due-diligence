#!/usr/bin/env python3
"""Build the static site published to GitHub Pages.

Reads the repository's Markdown (README, GUIDE, companies/*/README*) and
renders a bilingual static site into the output directory. New company
folders are picked up automatically from the tables in companies/README.md
and companies/README.zh-CN.md.

Usage: python3 scripts/build_site.py [--out _site]
"""

import argparse
import html
import os
import posixpath
import re
import shutil
from pathlib import Path

import markdown
from markdown.extensions.toc import slugify_unicode

ROOT = Path(__file__).resolve().parent.parent
SITE_ASSETS = ROOT / "site"
# In GitHub Actions, GITHUB_REPOSITORY makes forks link to their own copy.
REPO_SLUG = os.environ.get("GITHUB_REPOSITORY", "memwey/startup-due-diligence")
REPO_URL = f"https://github.com/{REPO_SLUG}"

STRINGS = {
    "en": {
        "html_lang": "en",
        "site_name": "Startup Due Diligence",
        "hero_title": "Due diligence, for engineers.",
        "hero_sub": (
            "Sourced, dated public evidence on technology startups: product, "
            "founders, funding, and engineering. Read it before you sign the offer."
        ),
        "companies": "Companies",
        "guide": "Guide",
        "guide_title": "Research guide",
        "contents": "Contents",
        "updated": "Last updated",
        "footer_1": (
            "Independent research notes based on publicly available information. "
            "Not affiliated with the companies covered. Verify important "
            "information against primary sources before relying on it."
        ),
        "footer_2": 'MIT License · Source on <a href="{repo}">GitHub</a>',
        "meta_home": "{n} companies · English / 中文",
    },
    "zh": {
        "html_lang": "zh-CN",
        "site_name": "Startup Due Diligence",
        "hero_title": "写给工程师的尽职调查",
        "hero_sub": (
            "关于科技创业公司的公开证据，每条都有出处和日期：产品、创始人、"
            "融资与工程。签 offer 之前先读一读。"
        ),
        "companies": "公司",
        "guide": "指南",
        "guide_title": "调研指南",
        "contents": "目录",
        "updated": "最后更新",
        "footer_1": (
            "基于公开资料的独立调研笔记，与所涉公司均无关联。"
            "做重要决定前请回查一手来源。"
        ),
        "footer_2": 'MIT 许可证 · <a href="{repo}">GitHub</a> 源码',
        "meta_home": "{n} 家公司 · English / 中文",
    },
}

LANG_SWITCH_LINE = re.compile(
    r"^(\*\*English\*\*|\[English\]\([^)]*\))\s*\|\s*(\*\*简体中文\*\*|\[简体中文\]\([^)]*\))\s*$",
    re.M,
)
UPDATED_RE = {
    "en": re.compile(r"Last updated:\s*(\d{4}-\d{2}-\d{2})"),
    "zh": re.compile(r"最后更新：\s*(\d{4}-\d{2}-\d{2})"),
}


def make_md():
    return markdown.Markdown(
        extensions=["tables", "fenced_code", "sane_lists", "toc"],
        extension_configs={
            "toc": {"slugify": slugify_unicode, "toc_depth": "2-3", "anchorlink": False}
        },
    )


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


def strip_title_and_langline(text):
    """Remove the first H1 and the English|中文 switch line; return (title, rest)."""
    m = re.search(r"^# (.+)$", text, re.M)
    title = m.group(1).strip() if m else ""
    if m:
        text = text[: m.start()] + text[m.end():]
    text = LANG_SWITCH_LINE.sub("", text)
    return title, text.lstrip("\n")


def strip_leading_blockquote(text):
    lines = text.lstrip("\n").split("\n")
    i = 0
    while i < len(lines) and lines[i].startswith(">"):
        i += 1
    return "\n".join(lines[i:]).lstrip("\n")


def repo_to_site(path, slugs):
    """Map a repo-relative file path to a site-relative directory URL."""
    table = {
        "README.md": "",
        "README.zh-CN.md": "zh/",
        "GUIDE.md": "guide/",
        "GUIDE.zh-CN.md": "zh/guide/",
        "companies/README.md": "",
        "companies/README.zh-CN.md": "zh/",
        "companies": "",
        "companies/": "",
    }
    if path in table:
        return table[path]
    m = re.match(r"^companies/([\w-]+)/?(README\.md)?$", path)
    if m and m.group(1) in slugs:
        return f"companies/{m.group(1)}/"
    m = re.match(r"^companies/([\w-]+)/README\.zh-CN\.md$", path)
    if m and m.group(1) in slugs:
        return f"zh/companies/{m.group(1)}/"
    return None


def relativize(target, page_dir):
    """Relative URL from the page's directory to a site-relative target."""
    rel = posixpath.relpath(target or ".", page_dir or ".")
    if rel == ".":
        return "./"
    return rel + "/" if not rel.endswith("/") else rel


def rewrite_links(body_html, src_dir, page_dir, slugs):
    """Rewrite relative Markdown links to their rendered locations."""

    def repl(m):
        href = m.group(1)
        if re.match(r"^(https?:|mailto:|#|data:)", href):
            return m.group(0)
        target, _, anchor = href.partition("#")
        resolved = posixpath.normpath(posixpath.join(src_dir, target)) if target else ""
        site = repo_to_site(resolved, slugs)
        if site is None:
            new = f"{REPO_URL}/blob/main/{resolved}"
        else:
            new = relativize(site, page_dir)
        if anchor:
            new += "#" + anchor
        return f'href="{new}"'

    return re.sub(r'href="([^"]+)"', repl, body_html)


def wrap_tables(body_html):
    body_html = body_html.replace("<table>", '<div class="table-wrap"><table>')
    return body_html.replace("</table>", "</table></div>")


def render_markdown(text, src_dir, page_dir, slugs):
    md = make_md()
    body = md.convert(text)
    body = wrap_tables(rewrite_links(body, src_dir, page_dir, slugs))
    toc = [t for t in md.toc_tokens if t["level"] == 2]
    return body, toc


def toc_html(tokens, label):
    if len(tokens) < 3:
        return ""
    items = "".join(
        f'<li><a href="#{t["id"]}">{html.escape(t["name"])}</a></li>' for t in tokens
    )
    return (
        f'<nav class="toc" aria-label="{html.escape(label)}">'
        f'<p class="toc-title">{html.escape(label)}</p><ol>{items}</ol></nav>'
    )


def page(lang, page_dir, title, description, main, alt_href, active_nav=None):
    s = STRINGS[lang]
    root = relativize("", page_dir)
    if root == "./":
        root = ""
    home = relativize("zh/" if lang == "zh" else "", page_dir)
    guide = relativize("zh/guide/" if lang == "zh" else "guide/", page_dir)
    en_cls, zh_cls = ("", ' class="on"') if lang == "zh" else (' class="on"', "")
    en_href = alt_href if lang == "zh" else "./"
    zh_href = "./" if lang == "zh" else alt_href
    full_title = (
        s["site_name"] if title == s["site_name"] else f'{title} · {s["site_name"]}'
    )
    return f"""<!doctype html>
<html lang="{s['html_lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(full_title)}</title>
<meta name="description" content="{html.escape(description)}">
<meta name="color-scheme" content="light dark">
<meta property="og:title" content="{html.escape(full_title)}">
<meta property="og:description" content="{html.escape(description)}">
<meta property="og:type" content="article">
<link rel="icon" href="{root}favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{root}style.css">
</head>
<body>
<nav class="nav"><div class="wrap nav-inner">
  <a class="wordmark" href="{home}">{s['site_name']}</a>
  <div class="nav-links">
    <a href="{home}#directory">{s['companies']}</a>
    <a href="{guide}">{s['guide']}</a>
    <a class="hide-sm" href="{REPO_URL}">GitHub</a>
  </div>
  <div class="lang">
    <a{en_cls} href="{en_href}" lang="en">EN</a>
    <a{zh_cls} href="{zh_href}" lang="zh-CN">中文</a>
  </div>
</div></nav>
<main>
{main}
</main>
<footer class="footer"><div class="wrap">
  <p>{s['footer_1']}</p>
  <p>{s['footer_2'].format(repo=REPO_URL)}</p>
</div></footer>
<script src="{root}main.js" defer></script>
</body>
</html>
"""


def parse_companies(lang):
    """Company rows from the index table: [(slug, name, area)] in table order."""
    src = "companies/README.md" if lang == "en" else "companies/README.zh-CN.md"
    rows = []
    for line in read(src).splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != 3 or set(cells[0]) <= {"-", " "} or "](" not in cells[2]:
            continue
        m = re.search(r"\]\(([\w-]+)/", cells[2])
        if not m:
            continue
        rows.append((m.group(1), cells[0], cells[1]))
    return rows


def build(out):
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)

    companies = {lang: parse_companies(lang) for lang in ("en", "zh")}
    slugs = [slug for slug, _, _ in companies["en"]]
    areas = {
        lang: {slug: area for slug, _, area in companies[lang]} for lang in ("en", "zh")
    }
    updated = {}

    # ---- company pages ----
    for lang in ("en", "zh"):
        s = STRINGS[lang]
        for slug, name, _ in companies[lang]:
            src = f"companies/{slug}/README.md" if lang == "en" else f"companies/{slug}/README.zh-CN.md"
            if not (ROOT / src).exists():
                print(f"warning: missing {src}, skipped")
                continue
            text = read(src)
            mu = UPDATED_RE[lang].search(text)
            updated[(lang, slug)] = mu.group(1) if mu else ""
            title, rest = strip_title_and_langline(text)
            title = title or name
            page_dir = f"companies/{slug}/" if lang == "en" else f"zh/companies/{slug}/"
            body, toc = render_markdown(rest, f"companies/{slug}", page_dir, slugs)
            area = areas[lang].get(slug, "")
            date = updated[(lang, slug)]
            parts = [html.escape(area)] if area else []
            if date:
                parts.append(f'<span class="date">{s["updated"]} {date}</span>')
            meta = " · ".join(parts)
            main = f"""<div class="wrap"><div class="doc{' has-toc' if toc_html(toc, s['contents']) else ''}">
<article class="prose">
<header class="doc-head">
<h1>{html.escape(title)}</h1>
<p class="doc-meta">{meta}</p>
</header>
{body}
</article>
{toc_html(toc, s['contents'])}
</div></div>"""
            alt = f"../../../companies/{slug}/" if lang == "zh" else f"../../zh/companies/{slug}/"
            dest = out / page_dir / "index.html"
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(
                page(lang, page_dir, title, area or title, main, alt), encoding="utf-8"
            )

    # ---- guide pages ----
    for lang, src, page_dir, alt in (
        ("en", "GUIDE.md", "guide/", "../zh/guide/"),
        ("zh", "GUIDE.zh-CN.md", "zh/guide/", "../../guide/"),
    ):
        s = STRINGS[lang]
        title, rest = strip_title_and_langline(read(src))
        title = title or s["guide_title"]
        body, toc = render_markdown(rest, "", page_dir, slugs)
        main = f"""<div class="wrap"><div class="doc{' has-toc' if toc_html(toc, s['contents']) else ''}">
<article class="prose">
<header class="doc-head"><h1>{html.escape(title)}</h1></header>
{body}
</article>
{toc_html(toc, s['contents'])}
</div></div>"""
        dest = out / page_dir / "index.html"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(
            page(lang, page_dir, s["guide_title"], title, main, alt), encoding="utf-8"
        )

    # ---- home pages ----
    for lang, src, page_dir, alt in (
        ("en", "README.md", "", "zh/"),
        ("zh", "README.zh-CN.md", "zh/", "../"),
    ):
        s = STRINGS[lang]
        _, rest = strip_title_and_langline(read(src))
        rest = strip_leading_blockquote(rest)
        about, _ = render_markdown(rest, "", page_dir, slugs)
        rows = []
        for slug, name, area in companies[lang]:
            date = updated.get((lang, slug), "")
            href = f"companies/{slug}/"
            rows.append(
                f'<a class="dir-row" href="{href}">'
                f'<span class="dir-name">{html.escape(name)}</span>'
                f'<span class="dir-area">{html.escape(area)}</span>'
                f'<span class="dir-date">{date}</span></a>'
            )
        n = len(companies[lang])
        main = f"""<header class="hero"><div class="wrap">
<h1>{s['hero_title']}</h1>
<p>{s['hero_sub']}</p>
<p class="hero-meta">{s['meta_home'].format(n=n)}</p>
</div></header>
<section class="directory"><div class="wrap">
<h2 id="directory">{s['companies']}</h2>
<div class="dir">
{''.join(rows)}
</div>
</div></section>
<section><div class="wrap"><div class="doc"><article class="prose">
{about}
</article></div></div></section>"""
        dest = out / page_dir / "index.html"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(
            page(lang, page_dir, s["site_name"], s["hero_sub"], main, alt),
            encoding="utf-8",
        )

    # ---- static assets ----
    for name in ("style.css", "main.js", "favicon.svg"):
        shutil.copy(SITE_ASSETS / name, out / name)
    shutil.copytree(SITE_ASSETS / "fonts", out / "fonts")
    (out / ".nojekyll").write_text("")
    print(f"built {sum(1 for _ in out.rglob('index.html'))} pages into {out}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="_site", type=Path)
    args = ap.parse_args()
    build(args.out if args.out.is_absolute() else ROOT / args.out)
