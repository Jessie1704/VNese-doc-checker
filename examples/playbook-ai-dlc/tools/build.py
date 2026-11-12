import re, html, sys, os
import markdown

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # thư mục chứa md/
SAMPLE = sys.argv[1]
OUT = sys.argv[2]

sample = open(SAMPLE, encoding='utf-8').read()
styles = re.findall(r'<style>(.*?)</style>', sample, re.S)
css = styles[1]  # the page's own stylesheet (first one is the viewer wrapper)
script = re.findall(r'<script>(.*?)</script>', sample, re.S)[-1]

extra_css = """
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){color-scheme:dark}}
:root[data-theme="dark"]{color-scheme:dark}
nav .part{margin:16px 8px 2px;font-size:11px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}
.part-title{margin:36px 0 12px;font-size:13px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
.cover{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:8px 32px 24px;margin-bottom:28px}
.cover .lead{font-size:18px;color:var(--muted);margin:4px 0 16px}
td.mx{text-align:center;font-size:14px;padding:4px 6px}
td.mx.on{color:var(--accent);font-weight:700}
td.mx.off{color:var(--muted)}
.tbl table.matrix th{font-size:12.5px;padding:6px 6px}
pre{white-space:pre}
:not(pre)>code{overflow-wrap:anywhere}
.tbl table.matrix code{overflow-wrap:normal;white-space:nowrap}
blockquote.call p+p{margin-top:8px}
@media (max-width:860px){.cover{padding:4px 16px 16px}}
"""

files = ['00','01','02','03','04','05','06','07','11','12','13','13b','14','15','16','17','18','19',
         'a1','a2','a3','a4','a5','a6','a7','a8','b1','b2']

def slug_id(fid):
    return 'c-' + fid

md = markdown.Markdown(extensions=['tables', 'fenced_code', 'attr_list', 'sane_lists'])

toc = []      # (kind, text, href)
sections = []

for fid in files:
    src = open(os.path.join(BASE, 'md', fid + '.md'), encoding='utf-8').read()
    part = None
    m = re.match(r'<!-- part: (.*?) -->\n', src)
    if m:
        part = m.group(1)
        src = src[m.end():]
    # chapter title
    first = src.split('\n', 1)[0]
    title = re.sub(r'\s*\{#[^}]+\}\s*$', '', first[2:]).strip()
    body_md = src.split('\n', 1)[1]
    md.reset()
    body = md.convert(body_md)
    cid = slug_id(fid)
    # h2 ids + toc
    n = [0]
    sub = []
    def h2(mo):
        attrs, inner = mo.group(1), mo.group(2)
        idm = re.search(r'id="([^"]+)"', attrs)
        if idm:
            hid = idm.group(1)
        else:
            n[0] += 1
            hid = f's-{fid}-{n[0]}'
        sub.append((re.sub('<[^>]+>', '', inner), hid))
        return f'<h2 id="{hid}">{inner}</h2>'
    body = re.sub(r'<h2([^>]*)>(.*?)</h2>', h2, body)
    # callouts
    def bq(mo):
        inner = mo.group(1)
        cls = 'call'
        if re.search(r'^\s*<p><strong>(Lưu ý|Cảnh báo)', inner):
            cls = 'call warn'
        elif re.search(r'^\s*<p><strong>(Ghi chú|Gợi ý)', inner):
            cls = 'call note'
        return f'<blockquote class="{cls}">{inner}</blockquote>'
    body = re.sub(r'<blockquote>(.*?)</blockquote>', bq, body, flags=re.S)
    # task lists
    def task(mo):
        return '<ul class="contains-task-list">' + re.sub(r'<li>\[ \]\s*', '<li class="task-list-item"><input disabled type="checkbox"> ', mo.group(1)) + '</ul>'
    body = re.sub(r'<ul>((?:\s*<li>\[ \].*?</li>)+\s*)</ul>', task, body, flags=re.S)
    # tables
    body = body.replace('<table>', '<div class="tbl"><table>').replace('</table>', '</table></div>')
    body = re.sub(r'<td>●</td>', '<td class="mx on" title="trên route">●</td>', body)
    body = re.sub(r'<td>·</td>', '<td class="mx off" title="ngoài route">·</td>', body)
    if fid == 'a1':
        body = body.replace('<div class="tbl"><table>', '<div class="tbl"><table class="matrix">', 2)
    if part:
        toc.append(('part', part, None))
        sections.append(f'<div class="part-title">{html.escape(part)}</div>')
    toc.append(('l1', title, '#s-' + fid))
    for t, hid in sub:
        toc.append(('l2', t, '#' + hid))
    sections.append(f'<section class="chap" id="{cid}"><h1 id="s-{fid}">{html.escape(title)}</h1>\n{body}\n</section>')

def toc_html():
    out = []
    for kind, text, href in toc:
        if kind == 'part':
            out.append(f'<div class="part">{html.escape(text)}</div>')
        else:
            out.append(f'<a class="{kind}" href="{href}">{html.escape(text)}</a>')
    return '\n'.join(out)

# cover: contents table by part
rows = []
curpart = ''
for kind, text, href in toc:
    if kind == 'part':
        curpart = text
    elif kind == 'l1':
        rows.append(f'<tr><td>{html.escape(curpart)}</td><td><a class="xref" href="{href}">{html.escape(text)}</a></td></tr>')

cover = f'''<section class="cover" id="c-cover">
<h1 id="s-cover">Playbook AWS AI-DLC</h1>
<p class="lead">Hướng dẫn tuần tự cho dự án mới và code base sẵn có, viết cho đội nhiều người làm song song.</p>
<div class="tbl"><table><thead><tr><th>Mục</th><th>Nội dung</th></tr></thead><tbody>
<tr><td>Công cụ</td><td><code>aidlc-workflows</code> phiên bản 2.9.0 (xem <a class="xref" href="#c-a8">A.8</a>)</td></tr>
<tr><td>Ngôn ngữ</td><td>Tiếng Việt; thuật ngữ của AI-DLC giữ nguyên tiếng Anh (xem <a class="xref" href="#c-00">00</a>)</td></tr>
<tr><td>Phiên bản trang này</td><td>Bản chỉnh sửa văn phong, cập nhật 12/11/2026</td></tr>
</tbody></table></div>
<h2 id="s-cover-1">Mục lục</h2>
<div class="tbl"><table><thead><tr><th>Phần</th><th>Chương</th></tr></thead><tbody>
{''.join(rows)}
</tbody></table></div>
<blockquote class="call note"><p><strong>Ghi chú:</strong> Số chương giữ theo bản gốc nên không có chương 08 đến 10. Chương 13b nói về chạy song song theo Unit, đọc sau chương 13.</p></blockquote>
</section>'''

page = f'''<title>Playbook AWS AI-DLC</title>
<meta name="claude:viewport-fit-sides" content="cover">
<style>{css}{extra_css}</style>
<button class="menu-btn" onclick="document.body.classList.toggle('nav-open')">☰ Mục lục</button>
<div class="layout">
<nav>
<div class="brand">Playbook AWS AI-DLC</div>
<div class="sub">aidlc-workflows 2.9.0 · bản chỉnh sửa 12/11/2026</div>
<div class="tools"><button id="bTheme">Sáng / tối</button></div>
<div class="search"><input id="q" type="search" placeholder="Tìm trong tài liệu (Ctrl+K)" autocomplete="off" aria-label="Tìm trong tài liệu"><div id="qinfo" class="qinfo"></div><div id="qres" class="qres"></div></div>
<div id="toc">
<a class="l1" href="#s-cover">Giới thiệu và mục lục</a>
{toc_html()}
</div>
</nav>
<main>
{cover}
{''.join(sections)}
</main>
</div>
<script>{script}</script>
'''
open(OUT, 'w', encoding='utf-8').write(page)
print('ok', len(page))
