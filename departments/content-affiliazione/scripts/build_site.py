#!/usr/bin/env python3
"""
Build the static site from markdown articles in content/articles/.
Usage: python3 scripts/build_site.py
Reads:  content/articles/*.md  (with YAML-ish front matter)
        data/affiliate-links.json (optional, for {{affiliate:slug}} substitution)
Writes: site/*.html, site/sitemap.xml, site/robots.txt
"""
import json
import re
import sys
from datetime import date
from pathlib import Path

import markdown
from jinja2 import Environment, FileSystemLoader
from slugify import slugify

ROOT = Path(__file__).resolve().parent.parent  # departments/content-affiliazione/
COMPANY_ROOT = ROOT.parent.parent  # radice del repo (income-project)
CONTENT_DIR = ROOT / "content" / "articles"
ABOUT_FILE = ROOT / "content" / "about.md"
SITE_DIR = COMPANY_ROOT / "docs"  # docs/ alla radice del repo, cosi' GitHub Pages lo serve senza configurazioni particolari
TEMPLATES_DIR = ROOT / "scripts" / "templates"
AFFILIATE_LINKS_FILE = ROOT / "data" / "affiliate-links.json"

SITE_URL = "https://REPLACE-WITH-YOUR-GITHUB-PAGES-URL"  # aggiornato dopo il primo deploy

env = Environment(loader=FileSystemLoader(str(TEMPLATES_DIR)))


def parse_front_matter(text):
    """Very small front-matter parser: expects a --- block at the top with key: value lines."""
    meta = {}
    body = text
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            fm, body = parts[1], parts[2]
            for line in fm.strip().splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    meta[k.strip()] = v.strip()
    return meta, body


def inject_affiliate_links(html, affiliate_links):
    def repl(match):
        slug = match.group(1)
        url = affiliate_links.get(slug)
        if url:
            return url
        # placeholder visibile finché non abbiamo il link reale, cosi' non pubblichiamo link rotti
        return "#todo-affiliate-link-" + slug
    return re.sub(r"\{\{affiliate:([a-z0-9_-]+)\}\}", repl, html)


def build():
    affiliate_links = {}
    if AFFILIATE_LINKS_FILE.exists():
        affiliate_links = json.loads(AFFILIATE_LINKS_FILE.read_text())

    SITE_DIR.mkdir(exist_ok=True)
    (SITE_DIR / "style.css").write_text((TEMPLATES_DIR / "style.css").read_text())

    articles = []
    base_tpl = env.get_template("base.html")

    md_files = sorted(CONTENT_DIR.glob("*.md"))
    if not md_files:
        print("Nessun articolo trovato in content/articles/. Niente da costruire.")
        return

    for md_path in md_files:
        raw = md_path.read_text()
        meta, body = parse_front_matter(raw)
        title = meta.get("title", md_path.stem)
        pub_date = meta.get("date", str(date.today()))
        art_type = meta.get("type", "article")
        description = meta.get("description", "")

        html_body = markdown.markdown(body, extensions=["extra", "toc"])
        html_body = inject_affiliate_links(html_body, affiliate_links)

        slug = meta.get("slug") or slugify(title)
        url_path = f"{slug}.html"

        rendered = base_tpl.render(
            page_title=f"{title} | SoloStack",
            meta_description=description,
            site_url=SITE_URL,
            url_path=url_path,
            root="",
            content=f"<h1>{title}</h1>\n{html_body}",
            year=date.today().year,
        )
        (SITE_DIR / url_path).write_text(rendered)

        articles.append({
            "title": title,
            "url": url_path,
            "date": pub_date,
            "type": art_type,
        })
        print(f"Costruito: {url_path}")

    # Ordina per data decrescente (le stringhe YYYY-MM-DD si ordinano correttamente)
    articles.sort(key=lambda a: a["date"], reverse=True)

    index_tpl = env.get_template("index.html")
    index_html = index_tpl.render(articles=articles, year=date.today().year)
    (SITE_DIR / "index.html").write_text(index_html)

    # sitemap.xml minimale
    urls = ["index.html"] + [a["url"] for a in articles]
    sitemap_items = "\n".join(
        f"  <url><loc>{SITE_URL}/{u}</loc></url>" for u in urls
    )
    sitemap = f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{sitemap_items}\n</urlset>\n'
    (SITE_DIR / "sitemap.xml").write_text(sitemap)

    (SITE_DIR / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n")

    if ABOUT_FILE.exists():
        meta, body = parse_front_matter(ABOUT_FILE.read_text())
        html_body = markdown.markdown(body, extensions=["extra"])
        rendered = base_tpl.render(
            page_title=f"{meta.get('title', 'About')} | SoloStack",
            meta_description=meta.get("description", ""),
            site_url=SITE_URL,
            url_path="about.html",
            root="",
            content=f"<h1>{meta.get('title', 'About')}</h1>\n{html_body}",
            year=date.today().year,
        )
        (SITE_DIR / "about.html").write_text(rendered)
        print("Costruito: about.html")

    print(f"\nSito costruito: {len(articles)} articoli in {SITE_DIR}")


if __name__ == "__main__":
    build()
