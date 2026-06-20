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

def strip_wrapper_tables(html):
    """Remove pandoc's outer single-cell table that wraps an inner table."""
    return re.sub(
        r'<table>\s*<tbody>\s*<tr[^>]*>\s*<td[^>]*>\s*(<table[\s\S]+?</table>)\s*</td>\s*</tr>\s*</tbody>\s*</table>',
        r'\1', html
    )

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

def build_nav_entry(title, sid, headings):
    """Build nested nav: chapter → H2 → H3."""
    h2_groups = []
    cur = None
    for lvl, txt, hid in headings:
        if lvl == 2:
            cur = {'txt': txt, 'id': hid, 'h3s': []}
            h2_groups.append(cur)
        elif lvl == 3 and cur is not None:
            cur['h3s'].append((txt, hid))

    inner = ''
    for h2 in h2_groups:
        if h2['h3s']:
            h3_links = ''.join(
                f'<a href="#{hid}" class="ns3">{txt}</a>'
                for txt, hid in h2['h3s']
            )
            inner += (
                f'<div class="nc2">'
                f'<a href="#{h2["id"]}" class="ns2 has-children">{h2["txt"]}</a>'
                f'<div class="nsub2">{h3_links}</div>'
                f'</div>'
            )
        else:
            inner += f'<a href="#{h2["id"]}" class="ns2">{h2["txt"]}</a>'

    return (
        f'<div class="nc">'
        f'<a href="#{sid}" class="nt">{title}</a>'
        + (f'<div class="nsub">{inner}</div>' if inner else '') +
        f'</div>'
    )

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

    html = md_to_html(ch['body'])
    html = strip_wrapper_tables(html)
    html, headings = inject_ids(html, used_ids)

    nav_items.append(build_nav_entry(ch['title'], sid, headings))
    sections.append(f'<section id="{sid}">\n{html}\n</section>')

NAV     = '\n'.join(nav_items)
CONTENT = '\n'.join(sections)

# ── CSS ───────────────────────────────────────────────────────────────────────

CSS = """
:root {
  --w: 295px;
  --top: 52px;
  --blue: #005b99;
  --blue-light: #e8f0f8;
  --bg: #f7f8fa;
  --border: #dde2e8;
  --text: #1c2333;
  --muted: #4a5568;
  --fs: 16px;
}
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }
body { font-size: var(--fs); line-height: 1.75; font-family: system-ui, -apple-system, sans-serif; color: var(--text); background: #fff; }
body.fs-large  { --fs: 18px; }
body.fs-xlarge { --fs: 20px; }

/* ── Top bar (mobile) ── */
#topbar {
  display: none;
  position: fixed; top: 0; left: 0; right: 0; height: var(--top);
  background: var(--blue); color: #fff;
  align-items: center; gap: 0.8rem; padding: 0 1rem;
  z-index: 200; font-weight: 600; font-size: 0.95rem;
}
#hbtn { background: none; border: none; color: #fff; font-size: 1.5rem; cursor: pointer; padding: 2px 6px; }
#topbar-title { flex: 1; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }

/* ── Sidebar ── */
#sidebar {
  position: fixed; top: 0; left: 0;
  width: var(--w); height: 100vh;
  background: var(--bg); border-right: 1px solid var(--border);
  display: flex; flex-direction: column;
  z-index: 150;
}
#sb-head {
  padding: 0.9rem 1rem;
  border-bottom: 1px solid var(--border);
  background: var(--blue); color: #fff;
  display: flex; align-items: center; gap: 0.5rem;
  font-size: 0.85rem; font-weight: 700; letter-spacing: 0.02em;
  flex-shrink: 0;
}
#sb-title { flex: 1; }
#sb-tools { display: flex; gap: 0.3rem; }
.sb-btn {
  background: rgba(255,255,255,0.15); border: 1px solid rgba(255,255,255,0.3);
  color: #fff; font-size: 0.75rem; font-weight: 700;
  cursor: pointer; padding: 3px 8px; border-radius: 3px;
  transition: background 0.15s;
}
.sb-btn:hover { background: rgba(255,255,255,0.3); }
#sbclose { font-size: 1rem; display: none; }

/* ── Search ── */
#sb-search { padding: 0.6rem 0.8rem; border-bottom: 1px solid var(--border); flex-shrink: 0; }
#search-input {
  width: 100%; padding: 0.4rem 0.7rem;
  border: 1px solid var(--border); border-radius: 4px;
  font-size: 0.82rem; background: #fff; outline: none;
}
#search-input:focus { border-color: var(--blue); box-shadow: 0 0 0 2px rgba(0,91,153,0.15); }
#search-info { font-size: 0.72rem; color: var(--muted); margin-top: 0.3rem; min-height: 1.1rem; display: flex; justify-content: space-between; align-items: center; }
#search-nav { display: none; gap: 0.2rem; }
#search-nav button { background: none; border: 1px solid var(--border); border-radius: 3px; padding: 1px 7px; cursor: pointer; font-size: 0.8rem; }
#search-nav button:hover { background: var(--blue-light); color: var(--blue); }

/* ── Nav ── */
#sb-nav { overflow-y: auto; flex: 1; padding: 0.3rem 0; }
.nc { border-bottom: 1px solid var(--border); }
.nt {
  display: block; padding: 0.6rem 1rem 0.6rem 1.1rem;
  font-size: 0.82rem; font-weight: 600; color: var(--text);
  text-decoration: none; transition: background 0.12s, color 0.12s;
  border-left: 3px solid transparent; cursor: pointer;
}
.nt:hover { background: var(--blue-light); color: var(--blue); }
.nt.active { color: var(--blue); border-left-color: var(--blue); background: var(--blue-light); }

/* H2 sub-items */
.nsub { display: none; background: #fff; }
.nc.open > .nsub { display: block; }
.ns2 {
  display: block; padding: 0.35rem 1rem 0.35rem 1.9rem;
  font-size: 0.78rem; color: var(--muted);
  text-decoration: none; transition: background 0.12s, color 0.12s;
  border-left: 3px solid transparent;
}
.ns2:hover { background: var(--blue-light); color: var(--blue); }
.ns2.active { color: var(--blue); font-weight: 500; border-left-color: #7eb8e0; background: #f0f6fc; }
.ns2.has-children::after { content: ' ›'; opacity: 0.5; font-size: 0.7rem; }
.nc2.open2 > .ns2.has-children::after { content: ' ⌄'; }

/* H3 sub-sub-items */
.nsub2 { display: none; }
.nc2.open2 > .nsub2 { display: block; }
.ns3 {
  display: block; padding: 0.28rem 1rem 0.28rem 2.8rem;
  font-size: 0.74rem; color: #718096;
  text-decoration: none; transition: background 0.12s, color 0.12s;
}
.ns3:hover { background: var(--blue-light); color: var(--blue); }
.ns3.active { color: var(--blue); }

/* ── Sidebar footer (legend) ── */
#sb-footer {
  padding: 0.7rem 1rem;
  border-top: 1px solid var(--border);
  font-size: 0.72rem; color: var(--muted);
  background: var(--bg);
  flex-shrink: 0;
  line-height: 1.5;
}

/* ── Main ── */
#main { margin-left: var(--w); padding: 2.5rem 4rem; }
section { max-width: 820px; padding-bottom: 3rem; margin-bottom: 3rem; border-bottom: 2px solid var(--border); }
section:last-child { border-bottom: none; }

/* ── Typography ── */
h1 { font-size: 1.75em; font-weight: 700; color: var(--blue); padding-bottom: 0.6rem; border-bottom: 2px solid var(--blue); margin-bottom: 1.5rem; }
h2 { font-size: 1.2em; font-weight: 700; margin: 2.2rem 0 0.7rem; padding-bottom: 0.35rem; border-bottom: 1px solid var(--border); }
h3 { font-size: 1.05em; font-weight: 600; margin: 1.6rem 0 0.5rem; color: #2d3748; }
h4 { font-size: 0.92em; font-weight: 600; margin: 1.2rem 0 0.4rem; color: var(--muted); text-transform: uppercase; letter-spacing: 0.04em; }
p { margin-bottom: 0.85rem; }
ul, ol { margin: 0.4rem 0 0.85rem 1.6rem; }
li { margin-bottom: 0.25rem; }
a { color: var(--blue); }
strong, b { font-weight: 600; }

/* ── Tables ── */
table { border-collapse: collapse; width: 100%; margin: 1.2rem 0; font-size: 0.875em; }
th { background: var(--blue); color: #fff; padding: 0.55rem 0.9rem; text-align: left; font-weight: 600; }
td { padding: 0.5rem 0.9rem; border: 1px solid var(--border); vertical-align: top; }
tr:nth-child(even) td { background: #f2f6fb; }
tr:hover td { background: #e4eef8; }
table p { margin: 0; }

/* Code cells — click to copy */
td.code-cell { font-family: monospace; font-size: 0.85em; cursor: pointer; white-space: nowrap; position: relative; }
td.code-cell:hover { background: #dbeeff !important; }
td.code-cell:hover::after { content: '⎘'; position: absolute; right: 4px; top: 50%; transform: translateY(-50%); opacity: 0.5; font-size: 0.85em; }
td.copied { background: #d4edda !important; transition: background 0.3s; }

/* ── Images ── */
img { max-width: 100%; height: auto; display: block; margin: 1.2rem 0; border: 1px solid var(--border); border-radius: 4px; }

/* ── Search highlights ── */
mark.srch { background: #ffe066; color: inherit; border-radius: 2px; padding: 0 1px; }
mark.srch.current { background: #ff9900; }

/* ── Back to top ── */
#totop {
  position: fixed; bottom: 2rem; right: 2rem;
  width: 42px; height: 42px;
  background: var(--blue); color: #fff; border: none; border-radius: 50%;
  cursor: pointer; font-size: 1.3rem;
  display: flex; align-items: center; justify-content: center;
  box-shadow: 0 2px 10px rgba(0,0,0,0.2);
  opacity: 0; pointer-events: none; transition: opacity 0.2s;
  z-index: 90;
}
#totop.visible { opacity: 1; pointer-events: auto; }
#totop:hover { background: #004880; }

/* ── Print ── */
@media print {
  #sidebar, #topbar, #totop { display: none !important; }
  #main { margin-left: 0; padding: 1rem; }
  section { border-bottom: 1px solid #ccc; page-break-inside: avoid; }
  table { page-break-inside: avoid; font-size: 0.8rem; }
  a { color: inherit; text-decoration: none; }
}

/* ── Mobile ── */
@media (max-width: 860px) {
  #topbar { display: flex; }
  #sidebar { transform: translateX(-100%); transition: transform 0.25s ease; }
  #sidebar.open { transform: translateX(0); box-shadow: 4px 0 20px rgba(0,0,0,0.15); }
  #sbclose { display: block; }
  #overlay { display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.35); z-index: 140; }
  #overlay.show { display: block; }
  #main { margin-left: 0; padding: 1.5rem 1.2rem; margin-top: var(--top); }
  section { max-width: 100%; }
  table { font-size: 0.8em; display: block; overflow-x: auto; }
  h1 { font-size: 1.4em; }
  #totop { bottom: 1rem; right: 1rem; }
}
"""

# ── JS ────────────────────────────────────────────────────────────────────────

JS = """
// ── Sidebar open/close ──────────────────────────────────────────────────────
const sb = document.getElementById('sidebar');
const ov = document.getElementById('overlay');
const openSb  = () => { sb.classList.add('open');  ov.classList.add('show'); };
const closeSb = () => { sb.classList.remove('open'); ov.classList.remove('show'); };
document.getElementById('hbtn').addEventListener('click', openSb);
document.getElementById('sbclose').addEventListener('click', closeSb);
ov.addEventListener('click', closeSb);
document.querySelectorAll('.nt, .ns2, .ns3').forEach(a =>
  a.addEventListener('click', () => { if (window.innerWidth <= 860) closeSb(); })
);

// ── Chapter expand/collapse ──────────────────────────────────────────────────
document.querySelectorAll('.nt').forEach(a => {
  a.addEventListener('click', () => {
    const nc = a.closest('.nc');
    const wasOpen = nc.classList.contains('open');
    document.querySelectorAll('.nc.open').forEach(n => n.classList.remove('open'));
    if (!wasOpen) nc.classList.add('open');
  });
});

// ── H2 expand/collapse for H3 subs ──────────────────────────────────────────
document.querySelectorAll('.ns2.has-children').forEach(a => {
  a.addEventListener('click', e => {
    e.preventDefault();
    a.closest('.nc2').classList.toggle('open2');
  });
});

// ── Font size toggle ─────────────────────────────────────────────────────────
const fsSizes  = ['', 'fs-large', 'fs-xlarge'];
const fsLabels = ['A', 'A+', 'A++'];
let fsIdx = parseInt(localStorage.getItem('fsIdx') || '0');

function applyFs() {
  document.body.classList.remove(...fsSizes.filter(Boolean));
  if (fsSizes[fsIdx]) document.body.classList.add(fsSizes[fsIdx]);
  document.querySelectorAll('.fs-btn').forEach(b => b.textContent = fsLabels[fsIdx]);
  localStorage.setItem('fsIdx', fsIdx);
}
applyFs();
document.querySelectorAll('.fs-btn').forEach(b =>
  b.addEventListener('click', () => { fsIdx = (fsIdx + 1) % 3; applyFs(); })
);

// ── Back to top ──────────────────────────────────────────────────────────────
const totop = document.getElementById('totop');
window.addEventListener('scroll', () => {
  totop.classList.toggle('visible', window.scrollY > 400);
}, { passive: true });
totop.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));

// ── Copy-to-clipboard for code cells ─────────────────────────────────────────
// Mark cells that look like procedure codes (uppercase, no spaces, 3-12 chars)
document.querySelectorAll('td').forEach(td => {
  const t = td.textContent.trim();
  if (/^[A-Z][A-Z0-9]{2,11}$/.test(t)) td.classList.add('code-cell');
});
document.getElementById('main').addEventListener('click', e => {
  const td = e.target.closest('td.code-cell');
  if (!td) return;
  navigator.clipboard.writeText(td.textContent.trim()).then(() => {
    td.classList.add('copied');
    setTimeout(() => td.classList.remove('copied'), 800);
  });
});

// ── Search ───────────────────────────────────────────────────────────────────
const searchInput = document.getElementById('search-input');
const searchCount = document.getElementById('search-count');
const searchNav   = document.getElementById('search-nav');
const mainEl      = document.getElementById('main');
let marks = [], markIdx = 0;

function clearSearch() {
  document.querySelectorAll('mark.srch').forEach(m => {
    m.parentNode.replaceChild(document.createTextNode(m.textContent), m);
    m.parentNode.normalize();
  });
  marks = []; markIdx = 0;
  searchCount.textContent = '';
  searchNav.style.display = 'none';
}

function doSearch(q) {
  clearSearch();
  if (q.length < 2) return;
  const re = new RegExp(q.replace(/[.*+?^${}()|[\\]\\\\]/g, '\\\\$&'), 'gi');
  const walker = document.createTreeWalker(mainEl, NodeFilter.SHOW_TEXT, {
    acceptNode: n => n.parentNode.nodeName === 'MARK' ? NodeFilter.FILTER_REJECT : NodeFilter.FILTER_ACCEPT
  });
  const nodes = [];
  let node;
  while ((node = walker.nextNode())) { if (re.test(node.textContent)) { nodes.push(node); re.lastIndex = 0; } }

  nodes.forEach(node => {
    re.lastIndex = 0;
    const text = node.textContent;
    const frag = document.createDocumentFragment();
    let last = 0, m;
    while ((m = re.exec(text))) {
      if (last < m.index) frag.appendChild(document.createTextNode(text.slice(last, m.index)));
      const mark = document.createElement('mark');
      mark.className = 'srch';
      mark.textContent = m[0];
      frag.appendChild(mark);
      marks.push(mark);
      last = m.index + m[0].length;
    }
    if (last < text.length) frag.appendChild(document.createTextNode(text.slice(last)));
    node.parentNode.replaceChild(frag, node);
  });

  if (marks.length) { searchNav.style.display = 'flex'; goToMark(0); }
  else searchCount.textContent = 'Ingen resultater';
}

function goToMark(i) {
  marks.forEach(m => m.classList.remove('current'));
  if (!marks.length) return;
  markIdx = ((i % marks.length) + marks.length) % marks.length;
  marks[markIdx].classList.add('current');
  marks[markIdx].scrollIntoView({ behavior: 'smooth', block: 'center' });
  searchCount.textContent = `${markIdx + 1} / ${marks.length}`;
}

let searchTimer;
searchInput.addEventListener('input', () => {
  clearTimeout(searchTimer);
  searchTimer = setTimeout(() => doSearch(searchInput.value.trim()), 250);
});
searchInput.addEventListener('keydown', e => {
  if (e.key === 'Escape') { searchInput.value = ''; clearSearch(); }
  if (e.key === 'Enter')  goToMark(markIdx + 1);
});
document.getElementById('search-prev').addEventListener('click', () => goToMark(markIdx - 1));
document.getElementById('search-next').addEventListener('click', () => goToMark(markIdx + 1));

// ── Active section / heading highlight ───────────────────────────────────────
// Chapter level: observe <section> elements
const ioChapter = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (!entry.isIntersecting) return;
    const id = entry.target.id;
    document.querySelectorAll('.nt').forEach(a => {
      const on = a.getAttribute('href') === '#' + id;
      a.classList.toggle('active', on);
      if (on) a.closest('.nc').classList.add('open');
    });
  });
}, { rootMargin: '-10% 0px -80% 0px' });
document.querySelectorAll('section[id]').forEach(s => ioChapter.observe(s));

// Sub-section level: observe H2 and H3 headings
const ioSub = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (!entry.isIntersecting) return;
    const id = entry.target.id;
    document.querySelectorAll('.ns2, .ns3').forEach(a => {
      const on = a.getAttribute('href') === '#' + id;
      a.classList.toggle('active', on);
      if (on) {
        const nc2 = a.closest('.nc2');
        if (nc2) nc2.classList.add('open2');
      }
    });
  });
}, { rootMargin: '-10% 0px -80% 0px' });
document.querySelectorAll('h2[id], h3[id]').forEach(h => ioSub.observe(h));
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
  <span id="topbar-title">DCCG-LPR Databasemanual</span>
  <button class="sb-btn fs-btn" title="Skriftstørrelse">A</button>
</header>

<div id="overlay"></div>

<nav id="sidebar">
  <div id="sb-head">
    <span id="sb-title">DCCG&#8209;LPR Manual</span>
    <div id="sb-tools">
      <button class="sb-btn fs-btn" title="Skriftstørrelse">A</button>
      <button class="sb-btn" id="sbclose" aria-label="Luk">&#10005;</button>
    </div>
  </div>
  <div id="sb-search">
    <input id="search-input" type="search" placeholder="&#128269; Søg i manualen…" autocomplete="off">
    <div id="search-info">
      <span id="search-count"></span>
      <div id="search-nav">
        <button id="search-prev" title="Forrige">&#8679;</button>
        <button id="search-next" title="Næste">&#8681;</button>
      </div>
    </div>
  </div>
  <div id="sb-nav">
{NAV}
  </div>
  <div id="sb-footer">
    <strong>[P]</strong> = pseudo-procedurekode &nbsp;|&nbsp; klik procedurekode for at kopiere
  </div>
</nav>

<main id="main">
{CONTENT}
</main>

<button id="totop" title="Til toppen">&#8679;</button>

<script>{JS}</script>
</body>
</html>"""

OUT.write_text(PAGE)
print(f"✓  {OUT}  ({len(PAGE):,} bytes, {len(chapters)} chapters)")
