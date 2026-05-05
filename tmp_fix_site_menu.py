from pathlib import Path

patterns = {
    '<a href="index.html#services">Услуги / Servicii</a>': '<a href="index.html#services"><span data-ru>Услуги</span><span data-ro>Servicii</span></a>',
    '<a href="index.html#why">О нас / Despre noi</a>': '<a href="index.html#why"><span data-ru>О нас</span><span data-ro>Despre noi</span></a>',
    '<a href="blog.html">Блог / Blog</a>': '<a href="blog.html"><span data-ru>Блог</span><span data-ro>Blog</span></a>',
    '<a href="index.html#map">Контакты / Contacte</a>': '<a href="index.html#map"><span data-ru>Контакты</span><span data-ro>Contacte</span></a>',
    '<a href="index.html#services" onclick="document.getElementById(\'mm\').classList.remove(\'open\')">Услуги / Servicii</a>': '<a href="index.html#services" onclick="document.getElementById(\'mm\').classList.remove(\'open\')"><span data-ru>Услуги</span><span data-ro>Servicii</span></a>',
    '<a href="blog.html" onclick="document.getElementById(\'mm\').classList.remove(\'open\')">Блог / Blog</a>': '<a href="blog.html" onclick="document.getElementById(\'mm\').classList.remove(\'open\')"><span data-ru>Блог</span><span data-ro>Blog</span></a>',
    '<a href="index.html#map" onclick="document.getElementById(\'mm\').classList.remove(\'open\')">Контакты / Contacte</a>': '<a href="index.html#map" onclick="document.getElementById(\'mm\').classList.remove(\'open\')"><span data-ru>Контакты</span><span data-ro>Contacte</span></a>'
}
paths = list(Path('site').glob('*.html')) + list(Path('site/blog').glob('*.html'))
for path in paths:
    text = path.read_text(encoding='utf-8')
    updated = text
    for old, new in patterns.items():
        updated = updated.replace(old, new)
    if updated != text:
        path.write_text(updated, encoding='utf-8')
        print('Updated', path)
