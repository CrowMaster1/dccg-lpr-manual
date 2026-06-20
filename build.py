#!/usr/bin/env python3
"""
build.py  –  docs/*.md  →  index.html
Run:  python3 build.py
"""
import re, subprocess
from pathlib import Path

DOCS = Path("docs")
OUT  = Path("index.html")

# ── helpers ──────────────────────────────────────────────────────────────────

def parse_frontmatter(text):
    m = re.match(r'^---\s*\n(.+?)\n---\s*\n', text, re.DOTALL)
    if not m:
        return {}, text
    fm = {}
    for line in m.group(1).splitlines():
        k, _, v = line.partition(':')
        if k.strip():
            fm[k.strip()] = v.strip()
    return fm, text[m.end():]

def slugify(s):
    for a, b in [('æ','ae'),('ø','oe'),('å','aa'),('–','-'),('—','-')]:
        s = s.replace(a, b)
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')

def md_to_html(md):
    r = subprocess.run(
        ['pandoc', '-f', 'markdown', '-t', 'html', '--no-highlight'],
        input=md.encode(), capture_output=True
    )
    return r.stdout.decode()

def inject_ids(html, used):
    headings = []
    def repl(m):
        lvl, inner = m.group(1), m.group(2)
        text = re.sub(r'<[^>]+>', '', inner).strip()
        base = slugify(text) or 'h'
        n = used.get(base, 0)
        used[base] = n + 1
        hid = base if n == 0 else f'{base}-{n}'
        headings.append((int(lvl), text, hid))
        return f'<h{lvl} id="{hid}">{inner}</h{lvl}>'
    html = re.sub(r'<h([1-4])>(.*?)</h\1>', repl, html, flags=re.DOTALL)
    return html, headings

# ── load and sort chapters ────────────────────────────────────────────────────

chapters = []
for f in [Path('index.md')] + sorted(DOCS.glob('*.md')):
    if not f.exists():
        continue
    fm, body = parse_frontmatter(f.read_text())
    chapters.append({
        'title':     fm.get('title', f.stem),
        'nav_order': int(fm.get('nav_order', 99)),
        'body':      body,
    })
chapters.sort(key=lambda c: c['nav_order'])

# ── convert ───────────────────────────────────────────────────────────────────

used_ids  = {}
nav_items = []
sections  = []

for ch in chapters:
    sid = slugify(ch['title']) + '-sec'
    n = used_ids.get(sid, 0); used_ids[sid] = n + 1
    if n: sid = f'{sid}-{n}'

    html, headings = inject_ids(md_to_html(ch['body']), used_ids)

    subs = ''.join(
        f'<a href="#{hid}" class="ns">{txt}</a>'
        for lvl, txt, hid in headings if lvl == 2
    )
    nav_items.append(
        f'<div class="nc">'
        f'<a href="#{sid}" class="nt">{ch["title"]}</a>'
        + (f'<div class="nsub">{subs}</div>' if subs else '') +
        f'</div>'
    )
    sections.append(f'<section id="{sid}">\n{html}\n</section>')

NAV     = '\n'.join(nav_items)
CONTENT = '\n'.join(sections)

# ── CSS ───────────────────────────────────────────────────────────────────────

CSS = """
:root {
  --w: 285px;
  --top: 52px;
  --blue: #005b99;
  --blue-light: #e8f0f8;
  --bg: #f7f8fa;
  --border: #dde2e8;
  --text: #1c2333;
  --muted: #4a5568;
}
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }
body { font: 16px/1.75 system-ui, -apple-system, sans-serif; color: var(--text); background: #fff; }

/* ── Top bar (mobile) ── */
#topbar {
  display: none;
  position: fixed; top: 0; left: 0; right: 0; height: var(--top);
  background: var(--blue); color: #fff;
  align-items: center; gap: 0.8rem; padding: 0 1rem;
  z-index: 200; font-weight: 600; font-size: 0.95rem;
}
#hbtn { background: none; border: none; color: #fff; font-size: 1.5rem; cursor: pointer; line-height: 1; padding: 2px 6px; }

/* ── Sidebar ── */
#sidebar {
  position: fixed; top: 0; left: 0;
  width: var(--w); height: 100vh;
  background: var(--bg); border-right: 1px solid var(--border);
  display: flex; flex-direction: column;
  z-index: 150;
}
#sb-head {
  padding: 1.1rem 1.2rem;
  border-bottom: 1px solid var(--border);
  display: flex; justify-content: space-between; align-items: center;
  background: var(--blue); color: #fff;
  font-size: 0.85rem; font-weight: 700; letter-spacing: 0.02em;
}
#sbclose { display: none; background: none; border: none; color: #fff; font-size: 1.2rem; cursor: pointer; }
#sb-nav { overflow-y: auto; flex: 1; padding: 0.4rem 0; }

/* ── Nav items ── */
.nc { border-bottom: 1px solid var(--border); }
.nt {
  display: block; padding: 0.65rem 1.2rem;
  font-size: 0.83rem; font-weight: 600; color: var(--text);
  text-decoration: none; transition: background 0.15s, color 0.15s;
  border-left: 3px solid transparent;
}
.nt:hover { background: var(--blue-light); color: var(--blue); }
.nt.active { color: var(--blue); border-left-color: var(--blue); background: var(--blue-light); }
.nsub { display: none; background: #fff; }
.nc.open .nsub { display: block; }
.ns {
  display: block; padding: 0.4rem 1.2rem 0.4rem 2rem;
  font-size: 0.78rem; color: var(--muted);
  text-decoration: none; transition: background 0.15s, color 0.15s;
}
.ns:hover { background: var(--blue-light); color: var(--blue); }
.ns.active { color: var(--blue); font-weight: 500; }

/* ── Main content ── */
#main { margin-left: var(--w); padding: 2.5rem 4rem; }
section { max-width: 820px; padding-bottom: 3rem; margin-bottom: 3rem; border-bottom: 2px solid var(--border); }
section:last-child { border-bottom: none; }

/* ── Typography ── */
h1 {
  font-size: 1.75rem; font-weight: 700; color: var(--blue);
  padding-bottom: 0.6rem; border-bottom: 2px solid var(--blue);
  margin-bottom: 1.5rem;
}
h2 {
  font-size: 1.2rem; font-weight: 700;
  margin: 2.2rem 0 0.7rem;
  padding-bottom: 0.35rem; border-bottom: 1px solid var(--border);
}
h3 { font-size: 1.05rem; font-weight: 600; margin: 1.6rem 0 0.5rem; color: #2d3748; }
h4 { font-size: 0.95rem; font-weight: 600; margin: 1.2rem 0 0.4rem; color: var(--muted); text-transform: uppercase; letter-spacing: 0.04em; }
p { margin-bottom: 0.85rem; }
ul, ol { margin: 0.4rem 0 0.85rem 1.6rem; }
li { margin-bottom: 0.25rem; }
a { color: var(--blue); }
strong, b { font-weight: 600; }

/* ── Tables ── */
table { border-collapse: collapse; width: 100%; margin: 1.2rem 0; font-size: 0.875rem; }
th {
  background: var(--blue); color: #fff;
  padding: 0.55rem 0.9rem; text-align: left; font-weight: 600;
  white-space: nowrap;
}
td { padding: 0.5rem 0.9rem; border: 1px solid var(--border); vertical-align: top; }
tr:nth-child(even) td { background: #f2f6fb; }
tr:hover td { background: #e4eef8; }
table p { margin: 0; }

/* ── Images ── */
img { max-width: 100%; height: auto; display: block; margin: 1.2rem 0; border: 1px solid var(--border); border-radius: 4px; }

/* ── Mobile ── */
@media (max-width: 860px) {
  #topbar { display: flex; }
  #sidebar { transform: translateX(-100%); transition: transform 0.25s ease; top: 0; }
  #sidebar.open { transform: translateX(0); box-shadow: 4px 0 20px rgba(0,0,0,0.15); }
  #sbclose { display: block; }
  #overlay { display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.35); z-index: 140; }
  #overlay.show { display: block; }
  #main { margin-left: 0; padding: 1.5rem 1.2rem; margin-top: var(--top); }
  section { max-width: 100%; }
  table { font-size: 0.8rem; display: block; overflow-x: auto; }
  h1 { font-size: 1.4rem; }
}
"""

# ── JS ────────────────────────────────────────────────────────────────────────

JS = """
const sb  = document.getElementById('sidebar');
const ov  = document.getElementById('overlay');

function openSb()  { sb.classList.add('open');  ov.classList.add('show'); }
function closeSb() { sb.classList.remove('open'); ov.classList.remove('show'); }

document.getElementById('hbtn').addEventListener('click', openSb);
document.getElementById('sbclose').addEventListener('click', closeSb);
ov.addEventListener('click', closeSb);

// Close drawer on nav click (mobile)
document.querySelectorAll('.nt, .ns').forEach(a =>
  a.addEventListener('click', () => { if (window.innerWidth <= 860) closeSb(); })
);

// Expand/collapse sub-items when chapter title clicked
document.querySelectorAll('.nt').forEach(a => {
  a.addEventListener('click', e => {
    const nc = a.closest('.nc');
    const wasOpen = nc.classList.contains('open');
    document.querySelectorAll('.nc.open').forEach(n => n.classList.remove('open'));
    if (!wasOpen) nc.classList.add('open');
  });
});

// Highlight active section while scrolling
const allSections = document.querySelectorAll('section[id]');
const allLinks    = document.querySelectorAll('#sb-nav a[href^="#"]');

const io = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (!entry.isIntersecting) return;
    const id = entry.target.id;
    allLinks.forEach(a => {
      const on = a.getAttribute('href') === '#' + id;
      a.classList.toggle('active', on);
      if (on && a.classList.contains('nt')) {
        a.closest('.nc').classList.add('open');
      }
    });
  });
}, { rootMargin: '-15% 0px -75% 0px' });

allSections.forEach(s => io.observe(s));
"""

# ── assemble ──────────────────────────────────────────────────────────────────

PAGE = f"""<!DOCTYPE html>
<html lang="da">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>DCCG-LPR Databasemanual</title>
<style>{CSS}</style>
</head>
<body>

<header id="topbar">
  <button id="hbtn" aria-label="Menu">&#9776;</button>
  <span>DCCG-LPR Databasemanual</span>
</header>

<div id="overlay"></div>

<nav id="sidebar">
  <div id="sb-head">
    <span>DCCG&#8209;LPR Manual</span>
    <button id="sbclose" aria-label="Luk">&#10005;</button>
  </div>
  <div id="sb-nav">
{NAV}
  </div>
</nav>

<main id="main">
{CONTENT}
</main>

<script>{JS}</script>
</body>
</html>"""

OUT.write_text(PAGE)
print(f"✓  {OUT}  ({len(PAGE):,} bytes, {len(chapters)} chapters)")
