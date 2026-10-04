// Report pages: top bar with reading progress, section index on wide screens,
// a mini audio control and previous/next links. Needs site.js (loaded first).
// Everything is additive: if an older report lacks a piece, that feature is skipped.
(function () {
  const page = document.querySelector('.page');
  if (!page || !window.Site) return;
  const { esc, fmtDate, headline, toggleTheme } = window.Site;

  const file = location.pathname.split('/').pop() || '';
  const type = /^ai-news-/.test(file) ? 'daily' : 'special';
  const header = document.querySelector('.header, .special-header');
  const el = (tag, cls, html) => { const n = document.createElement(tag); if (cls) n.className = cls; if (html != null) n.innerHTML = html; return n; };
  const slug = s => s.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');

  /* ---------- Top bar + reading progress ---------- */
  const PLAY = '<svg viewBox="0 0 16 16"><path d="M4 2v12l10-6z"/></svg>';
  const PAUSE = '<svg viewBox="0 0 16 16"><path d="M4 2h3v12H4zM9 2h3v12H9z"/></svg>';
  const bar = el('div', 'topbar',
    '<div class="topbar-in">' +
      '<a class="topbar-brand" href="../" tabindex="-1">AI <em>Reports</em></a>' +
      '<span class="topbar-where"></span>' +
      '<button class="btn btn-sm topbar-audio" type="button" tabindex="-1" hidden aria-label="Play audio briefing"></button>' +
      '<button class="btn btn-sm" type="button" tabindex="-1" data-theme-toggle>◐</button>' +
    '</div><div class="topbar-progress"></div>');
  bar.setAttribute('aria-hidden', 'true');
  document.body.prepend(bar);
  const where = bar.querySelector('.topbar-where');
  const progress = bar.querySelector('.topbar-progress');
  bar.querySelector('[data-theme-toggle]').addEventListener('click', toggleTheme);
  window.Site.applyTheme(document.documentElement.getAttribute('data-theme'));   // label the new toggle

  const setBar = on => {
    bar.classList.toggle('on', on);
    bar.setAttribute('aria-hidden', String(!on));
    bar.querySelectorAll('a, button').forEach(b => { b.tabIndex = on ? 0 : -1; });
  };
  if (header) new IntersectionObserver(([e]) => setBar(!e.isIntersecting && e.boundingClientRect.top < 0)).observe(header);

  let ticking = false;
  const paintProgress = () => {
    ticking = false;
    const max = document.documentElement.scrollHeight - innerHeight;
    progress.style.transform = `scaleX(${max > 0 ? Math.min(1, scrollY / max) : 0})`;
  };
  addEventListener('scroll', () => { if (!ticking) { ticking = true; requestAnimationFrame(paintProgress); } }, { passive: true });
  paintProgress();

  /* ---------- Section index ---------- */
  let heads = [...document.querySelectorAll('.section-label')].filter(h => !/audio briefing/i.test(h.textContent));
  if (heads.length < 3) heads = [...document.querySelectorAll('.special-content > h2')];
  const sections = heads.map(h => {
    let label = h.textContent.replace(/\s+/g, ' ').trim();
    // Specials label sections "Part II"; the heading that follows says what it is about.
    const sub = /^(part|section|chapter)\b/i.test(label) && h.parentElement.querySelector('h2');
    if (sub && sub !== h) label = sub.textContent.replace(/\s+/g, ' ').trim();
    if (!h.id) h.id = slug(label) || 'section';
    return { h, label };
  }).filter(s => s.label);

  if (sections.length >= 3) {
    const toc = el('nav', 'page-toc',
      '<div class="eyebrow">On this page</div>' + sections.map(s => `<a href="#${s.h.id}">${esc(s.label)}</a>`).join(''));
    toc.setAttribute('aria-label', 'Sections');
    document.body.append(toc);
    const links = [...toc.querySelectorAll('a')];
    const mark = () => {
      // Current section: the last heading that has scrolled above 40% of the screen.
      let cur = 0;
      sections.forEach((s, i) => { if (s.h.getBoundingClientRect().top < innerHeight * 0.4) cur = i; });
      links.forEach((a, i) => a.setAttribute('aria-current', String(i === cur)));
      where.textContent = scrollY > 200 ? sections[cur].label : '';
    };
    addEventListener('scroll', () => requestAnimationFrame(mark), { passive: true });
    mark();
  }

  /* ---------- Mini audio control in the top bar ---------- */
  const audio = document.querySelector('.audio-player audio');
  const mini = bar.querySelector('.topbar-audio');
  if (audio) {
    const sync = () => {
      mini.hidden = audio.paused && audio.currentTime === 0;
      mini.innerHTML = (audio.paused ? PLAY : PAUSE) + '<span>Audio</span>';
      mini.setAttribute('aria-label', audio.paused ? 'Play audio briefing' : 'Pause audio briefing');
    };
    mini.addEventListener('click', () => { audio.paused ? audio.play().catch(() => {}) : audio.pause(); });
    ['play', 'pause', 'ended'].forEach(ev => audio.addEventListener(ev, sync));
    sync();
  }

  /* ---------- Reading analytics (Umami events) ---------- */
  // "read-complete" fires once when the end of the report scrolls into view; with
  // pageviews it tells which reports are read through, not just opened.
  const track = (name, data) => { try { window.umami && window.umami.track(name, data); } catch (e) {} };
  const end = page.querySelector('.footer') || page.lastElementChild;
  if (end) {
    const io = new IntersectionObserver(([e]) => {
      if (!e.isIntersecting) return;
      io.disconnect();
      track('read-complete', { report: file, type });
    });
    io.observe(end);
  }
  if (audio) audio.addEventListener('play', () => track('audio-play', { report: file }), { once: true });

  /* ---------- Previous / next ---------- */
  fetch('../reports.json').then(r => r.ok ? r.json() : null).then(data => {
    if (!data || !Array.isArray(data.reports)) return;
    const list = data.reports.filter(r => r.type === type)
      .sort((a, b) => a.date.localeCompare(b.date) || a.file.localeCompare(b.file));
    const i = list.findIndex(r => r.file === file);
    if (i < 0) return;
    const prev = list[i - 1], next = list[i + 1];
    if (!prev && !next) return;
    const day = s => fmtDate(s).replace(` ${new Date().getFullYear()}`, '');
    const link = (r, cls, k) => r ? `<a class="${cls}" href="${encodeURI(r.file)}"><span class="eyebrow">${k} · ${day(r.date)}</span><span class="t">${esc(headline(r))}</span></a>` : '';
    const nav = el('nav', 'pager', link(prev, 'prev', '← Previous') + link(next, 'next', 'Next →'));
    nav.setAttribute('aria-label', type === 'daily' ? 'Other briefings' : 'Other special reports');
    const footer = page.querySelector('.footer');
    footer ? page.insertBefore(nav, footer) : page.append(nav);
  }).catch(() => {});
})();
