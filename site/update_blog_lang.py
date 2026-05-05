from pathlib import Path
import re
base = Path('blog')
count = 0
for path in sorted(base.glob('*.html')):
    text = path.read_text(encoding='utf-8')
    modified = False
    if 'href="../lang.css"' not in text:
        text = text.replace(
            '"https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">',
            '"https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">\n<link rel="stylesheet" href="../lang.css">')
        modified = True
    if '<div class="lb">' not in text:
        pattern = re.compile(
            r'(<div class="nr">\s*<a href="tel:\+37368078078" class="nc">📞 068 078 078</a>\s*<button class="bb" onclick="document\.getElementById\(\'mm\'\)\.classList\.toggle\(\'open\'\)" aria-label="Menu"><span></span><span></span><span></span></button>\s*</div>)',
            re.S)
        repl = (
            '  <div class="nr">\n'
            '    <div class="lb">\n'
            '      <button class="on" onclick="setLang(\'ru\')" type="button">RU</button>\n'
            '      <button onclick="setLang(\'ro\')" type="button">RO</button>\n'
            '    </div>\n'
            '    <a href="tel:+37368078078" class="nc">📞 068 078 078</a>\n'
            '    <button class="bb" onclick="document.getElementById(\'mm\').classList.toggle(\'open\')" aria-label="Menu"><span></span><span></span><span></span></button>\n'
            '  </div>'
        )
        new_text, n = pattern.subn(repl, text)
        if n:
            text = new_text
            modified = True
    if '<script src="../lang.js"></script>' not in text:
        text = text.replace('</body>', '<script src="../lang.js"></script>\n</body>')
        modified = True
    if modified:
        path.write_text(text, encoding='utf-8')
        count += 1
print(f'Updated {count} files')
