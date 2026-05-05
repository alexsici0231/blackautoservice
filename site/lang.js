const langStorage = 'blackautoservice_lang';
function setLang(l) {
  const isRo = l === 'ro';
  document.body.classList.toggle('ro', isRo);
  localStorage.setItem(langStorage, isRo ? 'ro' : 'ru');
  document.querySelectorAll('.lb button').forEach((btn, idx) => {
    btn.classList.toggle('on', idx === (isRo ? 1 : 0));
  });
  const ta = document.getElementById('ta');
  if (ta) ta.placeholder = isRo ? 'Descrieți problema sau întrebarea...' : 'Опишите проблему или вопрос...';
}

document.addEventListener('DOMContentLoaded', () => {
  const saved = localStorage.getItem(langStorage);
  setLang(saved === 'ro' ? 'ro' : 'ru');
});