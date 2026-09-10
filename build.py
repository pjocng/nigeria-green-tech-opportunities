# -*- coding: utf-8 -*-
"""Render docs/green-tech-open-data-opportunities-nigeria.md into an interactive
single-page web report (index.html): sticky-nav table of contents,
scrollspy, collapsible sections, section filter, click-to-sort tables,
dark/light, print-to-PDF. Self-contained, no external dependencies."""
import re, html, io, os, datetime, markdown

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "green-tech-open-data-opportunities-nigeria.md")
OUT = os.path.join(HERE, "index.html")

md_text = io.open(SRC, encoding="utf-8").read()

md = markdown.Markdown(
    extensions=["tables", "fenced_code", "attr_list", "sane_lists", "toc"],
    extension_configs={"toc": {"toc_depth": "1-3", "permalink": False}},
)
body = md.convert(md_text)


def strip_tags(s):
    return re.sub(r"<[^>]+>", "", s).strip()


def nav_label(s):
    return html.escape(html.unescape(strip_tags(s)))


parts = re.split(r"(?=<h1 )", body)
front = parts[1] if parts and parts[0].strip() == "" else parts[0]
real = parts[2:] if parts and parts[0].strip() == "" else parts[1:]


def h1_meta(chunk):
    m = re.search(r'<h1 id="([^"]+)">(.*?)</h1>', chunk, re.S)
    return m.group(1), strip_tags(m.group(2))


title_m = re.search(r'<h1 id="([^"]+)">(.*?)</h1>', front, re.S)
doc_title = html.unescape(strip_tags(title_m.group(2))) if title_m else "Green-Tech Opportunities — Nigeria"

# nav: front-matter h2s (skip the subtitle h2) + section h1s
nav = []
for hid, htxt in re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', front, re.S)[1:]:
    nav.append((hid, nav_label(htxt), "top"))

wrapped = ['<div class="doc-front" id="doc-front">' + front + "</div>"]
for chunk in real:
    hid, htxt = h1_meta(chunk)
    nav.append((hid, nav_label(htxt), "sec"))
    chunk = re.sub(
        r'(<h1 id="[^"]+">.*?</h1>)',
        lambda m: '<button class="sec-toggle" aria-expanded="true">'
        + m.group(1)
        + '<span class="chev">›</span></button><div class="sec-body">',
        chunk,
        count=1,
        flags=re.S,
    )
    wrapped.append(f'<section class="doc-sec" id="wrap-{hid}">' + chunk + "</div></section>")

body = "".join(wrapped)

# wrap tables for horizontal scroll + mark them sortable
body = body.replace("<table>", '<div class="tbl-scroll"><table class="sortable">').replace(
    "</table>", "</table></div>"
)

navhtml = "\n".join(
    f'<a href="#{hid}" data-target="{hid}" class="nav-{kind}">{txt}</a>'
    for hid, txt, kind in nav
)

GEN_DATE = datetime.date.today().strftime("%d %B %Y")

PAGE = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(doc_title)}</title>
<meta name="description" content="Research study: green, climate-tech and sustainability products that can be built in Nigeria on free/open data — data inventory, 26 product concepts, scoring, green-funding and carbon-credit assessment, and a build-first recommendation. Prepared by Pjoc.">
<style>
:root{{
  --bg:#f6f8f6;--panel:#fff;--ink:#15201a;--muted:#5b6b62;--line:#e2e8e3;
  --brand:#127a4b;--brand-2:#0c5c39;--accent:#2fbf71;--warn:#b5541f;
  --shadow:0 1px 3px rgba(20,40,30,.08),0 8px 24px rgba(20,40,30,.06);--radius:12px;--sbw:300px;
}}
@media (prefers-color-scheme:dark){{:root:not([data-theme=light]){{
  --bg:#0e1512;--panel:#151d19;--ink:#e8efe9;--muted:#9db0a5;--line:#25302a;
  --brand:#3fce88;--brand-2:#2fbf71;--accent:#3fce88;--warn:#f0975e;
  --shadow:0 1px 3px rgba(0,0,0,.4),0 10px 30px rgba(0,0,0,.35);
}}}}
:root[data-theme=dark]{{
  --bg:#0e1512;--panel:#151d19;--ink:#e8efe9;--muted:#9db0a5;--line:#25302a;
  --brand:#3fce88;--brand-2:#2fbf71;--accent:#3fce88;--warn:#f0975e;
  --shadow:0 1px 3px rgba(0,0,0,.4),0 10px 30px rgba(0,0,0,.35);
}}
*{{box-sizing:border-box}}
html{{scroll-behavior:smooth}}
body{{margin:0;background:var(--bg);color:var(--ink);
  font:16px/1.62 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;-webkit-font-smoothing:antialiased}}
a{{color:var(--brand)}}
.topbar{{position:sticky;top:0;z-index:40;display:flex;align-items:center;gap:12px;
  padding:10px 16px;background:color-mix(in srgb,var(--bg) 90%,transparent);backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}}
.topbar .brand{{font-weight:750;font-size:14px;letter-spacing:-.01em}}
.topbar .brand small{{color:var(--muted);font-weight:500}}
.topbar .sp{{flex:1}}
.btn{{font:inherit;font-size:12.5px;font-weight:650;padding:6px 11px;border-radius:8px;border:1px solid var(--line);
  background:var(--panel);color:var(--ink);cursor:pointer}}
.btn:hover{{border-color:var(--brand);color:var(--brand)}}
#menuBtn{{display:none}}
.progress{{position:sticky;top:53px;z-index:39;height:3px;background:transparent}}
.progress i{{display:block;height:100%;width:0;background:var(--brand);transition:width .1s linear}}
.layout{{display:grid;grid-template-columns:var(--sbw) 1fr;gap:0;max-width:1320px;margin:0 auto}}
aside{{border-right:1px solid var(--line);padding:18px 10px 60px;position:sticky;top:56px;align-self:start;
  height:calc(100vh - 56px);overflow-y:auto}}
aside .filter{{width:100%;padding:8px 10px;border:1px solid var(--line);border-radius:9px;background:var(--panel);
  color:var(--ink);font:inherit;font-size:13px;margin-bottom:10px}}
aside nav{{display:flex;flex-direction:column;gap:1px}}
aside a{{text-decoration:none;color:var(--muted);font-size:13px;font-weight:600;padding:6px 10px;border-radius:7px;
  border-left:2px solid transparent;line-height:1.35}}
aside a:hover{{color:var(--ink);background:var(--panel)}}
aside a.active{{color:var(--brand);background:color-mix(in srgb,var(--brand) 10%,transparent);border-left-color:var(--brand)}}
aside a.nav-top{{margin-top:2px;color:var(--brand)}}
main{{padding:26px clamp(18px,4vw,54px) 120px;min-width:0}}
.doc-front{{border-bottom:1px solid var(--line);padding-bottom:8px;margin-bottom:6px}}
.doc-front h1{{font-size:clamp(24px,3.6vw,38px);line-height:1.18;letter-spacing:-.015em;margin:.1em 0 .15em;scroll-margin-top:70px}}
.doc-front > h2:first-of-type{{font-size:clamp(15px,2vw,18px);color:var(--muted);font-weight:600;margin:.1em 0 1em}}
.doc-front h2{{font-size:16px;scroll-margin-top:70px}}
.doc-front em{{color:var(--muted)}}
.doc-sec{{scroll-margin-top:70px;border-top:1px solid var(--line);margin-top:26px}}
.doc-sec:first-of-type{{border-top:0}}
.sec-toggle{{all:unset;display:flex;align-items:center;gap:10px;width:100%;cursor:pointer;padding:14px 0}}
.sec-toggle h1{{font-size:clamp(19px,2.6vw,26px);letter-spacing:-.01em;margin:0;flex:1}}
.sec-toggle .chev{{font-size:22px;color:var(--muted);transition:transform .18s;transform:rotate(90deg)}}
.sec-toggle[aria-expanded=false] .chev{{transform:rotate(0deg)}}
.sec-body{{overflow:hidden}}
.sec-body[hidden]{{display:none}}
main h2{{font-size:17px;margin:1.6em 0 .5em;padding-top:4px;letter-spacing:-.005em;scroll-margin-top:70px}}
main h3{{font-size:15px;margin:1.3em 0 .4em;color:var(--brand-2);scroll-margin-top:70px}}
main p{{margin:.7em 0}}
main ul,main ol{{margin:.6em 0;padding-left:1.35em}}
main li{{margin:.3em 0}}
main blockquote{{margin:1em 0;padding:.4em 1em;border-left:3px solid var(--brand);background:color-mix(in srgb,var(--brand) 7%,transparent);border-radius:0 8px 8px 0;color:var(--ink)}}
main code{{background:color-mix(in srgb,var(--muted) 16%,transparent);padding:.1em .35em;border-radius:5px;font-size:.9em}}
main pre{{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:14px;overflow-x:auto;font-size:12.5px;line-height:1.5}}
main pre code{{background:none;padding:0}}
hr{{border:0;border-top:1px solid var(--line);margin:1.6em 0}}
.tbl-scroll{{overflow-x:auto;border:1px solid var(--line);border-radius:10px;margin:1em 0}}
table{{width:100%;border-collapse:collapse;font-size:13px}}
th,td{{text-align:left;padding:9px 12px;border-bottom:1px solid var(--line);vertical-align:top}}
thead th{{background:color-mix(in srgb,var(--brand) 9%,transparent);font-size:11px;text-transform:uppercase;letter-spacing:.05em;color:var(--muted);position:sticky;top:0;white-space:nowrap}}
table.sortable thead th{{cursor:pointer;user-select:none}}
table.sortable thead th:hover{{color:var(--brand)}}
table.sortable thead th.sort-asc::after{{content:" \\2191";color:var(--brand)}}
table.sortable thead th.sort-desc::after{{content:" \\2193";color:var(--brand)}}
tbody tr:last-child td{{border-bottom:0}}
tbody tr:hover{{background:color-mix(in srgb,var(--muted) 7%,transparent)}}
.doc-front .card,main .card{{background:var(--panel);border:1px solid var(--line);border-radius:var(--radius);padding:16px;box-shadow:var(--shadow)}}
#toTop{{position:fixed;right:18px;bottom:18px;z-index:30;opacity:0;pointer-events:none;transition:opacity .2s}}
#toTop.show{{opacity:1;pointer-events:auto}}
@media (max-width:960px){{
  .layout{{grid-template-columns:1fr}}
  aside{{position:fixed;left:0;top:56px;z-index:35;width:min(86vw,320px);background:var(--bg);
    transform:translateX(-102%);transition:transform .22s;box-shadow:var(--shadow)}}
  aside.open{{transform:none}}
  #menuBtn{{display:inline-block}}
  .scrim{{position:fixed;inset:56px 0 0;background:rgba(0,0,0,.35);z-index:34;opacity:0;pointer-events:none;transition:opacity .2s}}
  .scrim.show{{opacity:1;pointer-events:auto}}
}}
@media print{{
  .topbar,aside,.progress,#toTop,.scrim{{display:none!important}}
  .layout{{grid-template-columns:1fr}}
  .sec-body[hidden]{{display:block!important}}
  .sec-toggle .chev{{display:none}}
  main{{padding:0}}
  a{{color:inherit;text-decoration:none}}
}}
</style>
</head>
<body>
<div class="topbar">
  <button class="btn" id="menuBtn" aria-label="Contents">&#9776;</button>
  <span class="brand">Nigeria Green-Tech <small>&nbsp;/ Open-Data Opportunity Study</small></span>
  <span class="sp"></span>
  <button class="btn" id="expandBtn">Collapse all</button>
  <button class="btn" id="themeBtn" aria-label="Toggle theme">Theme</button>
  <button class="btn" onclick="window.print()">Print / PDF</button>
</div>
<div class="progress"><i id="progBar"></i></div>

<div class="layout">
  <aside id="sidebar">
    <input class="filter" id="navFilter" type="search" placeholder="Filter sections&hellip;" aria-label="Filter sections">
    <nav id="toc">
      {navhtml}
    </nav>
  </aside>
  <div class="scrim" id="scrim"></div>

  <main id="content">
    {body}
    <hr>
    <p style="font-size:11px;color:var(--muted)">Interactive study generated {GEN_DATE} from
    <code>green-tech-open-data-opportunities-nigeria.md</code>. Prepared by Pjoc. Dataset,
    funding-programme and policy facts checked September 2026 &mdash; re-verify before relying on any of
    them. Scores are the author's assessment. Not investment advice.</p>
  </main>
</div>
<button class="btn" id="toTop">&#8593; Top</button>

<script>
(function(){{
  var d=document, root=d.documentElement;
  try{{var t=localStorage.getItem('gi-theme'); if(t) root.setAttribute('data-theme',t);}}catch(e){{}}
  d.getElementById('themeBtn').onclick=function(){{
    var cur=root.getAttribute('data-theme');
    var next = cur==='dark' ? 'light' : cur==='light' ? 'dark'
      : (matchMedia('(prefers-color-scheme:dark)').matches?'light':'dark');
    root.setAttribute('data-theme',next);
    try{{localStorage.setItem('gi-theme',next);}}catch(e){{}}
  }};
  var sb=d.getElementById('sidebar'), scrim=d.getElementById('scrim');
  function closeMenu(){{sb.classList.remove('open');scrim.classList.remove('show');}}
  d.getElementById('menuBtn').onclick=function(){{sb.classList.toggle('open');scrim.classList.toggle('show');}};
  scrim.onclick=closeMenu;
  var toggles=[].slice.call(d.querySelectorAll('.sec-toggle'));
  function setAll(exp){{toggles.forEach(function(t){{t.setAttribute('aria-expanded',exp);
    t.nextElementSibling.hidden=!exp;}});
    d.getElementById('expandBtn').textContent=exp?'Collapse all':'Expand all';}}
  toggles.forEach(function(t){{t.addEventListener('click',function(e){{
    if(e.target.tagName==='A')return;
    var exp=t.getAttribute('aria-expanded')==='true';
    t.setAttribute('aria-expanded',!exp); t.nextElementSibling.hidden=exp;
  }});}});
  var allExp=true;
  d.getElementById('expandBtn').onclick=function(){{allExp=!allExp;setAll(allExp);}};

  var links=[].slice.call(d.querySelectorAll('#toc a[data-target]'));
  var map={{}}; links.forEach(function(l){{map[l.dataset.target]=l;}});
  var heads=[].slice.call(d.querySelectorAll('main h1[id], main h2[id]')).filter(function(h){{return map[h.id];}});
  var io=new IntersectionObserver(function(ents){{
    ents.forEach(function(en){{
      if(en.isIntersecting){{
        links.forEach(function(l){{l.classList.remove('active');}});
        var l=map[en.target.id]; if(l){{l.classList.add('active'); l.scrollIntoView({{block:'nearest'}});}}
      }}
    }});
  }},{{rootMargin:'-64px 0px -70% 0px',threshold:0}});
  heads.forEach(function(h){{io.observe(h);}});
  links.forEach(function(l){{l.addEventListener('click',function(){{
    var host=d.getElementById(l.dataset.target);
    if(host){{var bdy=host.closest('.sec-body'); if(bdy&&bdy.hidden){{
      bdy.hidden=false; bdy.previousElementSibling.setAttribute('aria-expanded','true');}}}}
    if(innerWidth<=960) closeMenu();
  }});}});

  var bar=d.getElementById('progBar'), top=d.getElementById('toTop');
  top.onclick=function(){{scrollTo({{top:0,behavior:'smooth'}});}};
  addEventListener('scroll',function(){{
    var h=d.documentElement, sc=h.scrollTop, mx=h.scrollHeight-h.clientHeight;
    bar.style.width=(mx>0?100*sc/mx:0)+'%';
    top.classList.toggle('show',sc>600);
  }},{{passive:true}});

  d.getElementById('navFilter').addEventListener('input',function(e){{
    var q=e.target.value.trim().toLowerCase();
    d.querySelectorAll('#toc a[data-target]').forEach(function(l){{
      l.style.display = !q||l.textContent.toLowerCase().indexOf(q)>-1 ? '' : 'none';
    }});
    d.querySelectorAll('.doc-sec').forEach(function(s){{
      var txt=s.textContent.toLowerCase();
      s.style.display = !q||txt.indexOf(q)>-1 ? '' : 'none';
    }});
  }});

  // click-to-sort tables
  function cellVal(td){{
    var s=(td.textContent||'').trim().replace(/[,%$\\u20a6]/g,'');
    var m=s.match(/-?\\d+(\\.\\d+)?/);
    return m ? parseFloat(m[0]) : (td.textContent||'').trim().toLowerCase();
  }}
  d.querySelectorAll('table.sortable').forEach(function(tb){{
    var ths=tb.querySelectorAll('thead th'); if(!ths.length) return;
    ths.forEach(function(th,ci){{
      th.addEventListener('click',function(){{
        var body=tb.tBodies[0]; if(!body) return;
        var rows=[].slice.call(body.rows);
        var asc=!th.classList.contains('sort-asc');
        ths.forEach(function(x){{x.classList.remove('sort-asc','sort-desc');}});
        th.classList.add(asc?'sort-asc':'sort-desc');
        rows.sort(function(a,b){{
          var x=cellVal(a.cells[ci]), y=cellVal(b.cells[ci]);
          if(typeof x==='number'&&typeof y==='number') return asc?x-y:y-x;
          return asc ? String(x).localeCompare(String(y)) : String(y).localeCompare(String(x));
        }});
        rows.forEach(function(r){{body.appendChild(r);}});
      }});
    }});
  }});
}})();
</script>
</body>
</html>
"""

io.open(OUT, "w", encoding="utf-8").write(PAGE)
print("wrote", OUT, len(PAGE), "bytes;", len(nav), "nav entries")
