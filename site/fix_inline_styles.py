from pathlib import Path

replacement_map = [
    ('style="color:var(--red);font-size:28px"', 'class="mobile-phone"'),
    ('style="display:flex;justify-content:space-between;flex-wrap:wrap;gap:20px;align-items:center"', 'class="footer-top"'),
    ('style="font-family:var(--fh);font-size:20px;letter-spacing:.06em"', 'class="footer-brand"'),
    ('style="color:var(--red)"', 'class="text-red"'),
    ('style="font-size:12px;color:var(--gray2);margin-top:6px"', 'class="footer-copy"'),
    ('style="display:flex;gap:20px;flex-wrap:wrap"', 'class="footer-nav"'),
    ('style="font-size:13px;color:var(--gray2)"', 'class="footer-link"'),
    ('style="padding:60px 0 20px"', 'class="blog-main"'),
    ('style="font-size:11px;font-weight:700;letter-spacing:.22em;text-transform:uppercase;color:var(--red);margin-bottom:12px"', 'class="section-label"'),
    ('style="font-family:var(--fh);font-size:clamp(40px,6vw,72px);line-height:1.05;margin-bottom:14px"', 'class="page-title"'),
    ('style="font-size:16px;color:var(--gray);max-width:560px;margin-bottom:52px;line-height:1.7"', 'class="page-description"'),
    ('style="text-decoration:none;display:block;background:var(--bg3);border:1px solid var(--bdr);border-radius:14px;overflow:hidden;transition:border-color .22s,transform .22s" onmouseover="this.style.borderColor=\'var(--red)\';this.style.transform=\'translateY(-5px)\'" onmouseout="this.style.borderColor=\'var(--bdr)\';this.style.transform=\'\'"', 'class="blog-card"'),
    ('style="font-size:30px"', 'class="card-icon"'),
    ('style="font-size:10px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:var(--red);margin-top:10px"', 'class="card-label"'),
    ('style="padding:18px 20px"', 'class="card-body"'),
    ('style="font-family:var(--fh);font-size:19px;margin-bottom:8px;line-height:1.25;color:var(--white)"', 'class="card-title"'),
    ('style="font-size:13px;color:var(--gray);line-height:1.55;margin-bottom:14px"', 'class="card-desc"'),
    ('style="display:flex;justify-content:space-between;align-items:center"', 'class="card-footer"'),
    ('style="color:var(--red);font-size:12px;font-weight:700;letter-spacing:.06em"', 'class="read-link"'),
    ('style="font-size:11px;color:var(--gray2)"', 'class="card-meta"'),
    ('style="border-top:1px solid var(--bdr);padding-top:28px;margin-top:16px"', 'class="footer-section"'),
    ('style="font-size:40px;margin-bottom:16px"', 'class="article-icon"'),
    ('style="background:transparent;border:1px solid var(--red)"', 'class="btn-cta btn-cta-alt"'),
]

files = sorted(Path('site').rglob('*.html'))
files.append(Path('../index.html') if Path('../index.html').exists() else Path('index.html'))
summary = {}
for path in files:
    if not path.exists():
        continue
    text = path.read_text(encoding='utf-8')
    original = text
    for old, new in replacement_map:
        if old in text:
            text = text.replace(old, new)
            summary[old] = summary.get(old, 0) + original.count(old)
    if path.name == 'index.html' and 'meta name="viewport"' not in text:
        text = text.replace('<meta charset="UTF-8">\n  <meta http-equiv="refresh" content="0; URL=site/">',
                            '<meta charset="UTF-8">\n  <meta name="viewport" content="width=device-width, initial-scale=1">\n  <meta http-equiv="refresh" content="0; URL=site/">')
    if text != original:
        path.write_text(text, encoding='utf-8')
        print(f'Updated {path}')
print('Processed files:', len(files))
for k, v in summary.items():
    print(f'Replaced {v}x: {k}')
