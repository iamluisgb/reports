// Shared behaviour for every report page, injected by build_social.py.
// Adds the sticky bar with reading progress, the section index on wide screens,
// the waveform over the audio seek bar and previous/next links. Everything is
// additive: if a piece is missing from an older report, that feature is skipped.
(function () {
  const page = document.querySelector('.page');
  if (!page) return;

  const file = location.pathname.split('/').pop() || '';
  const type = /^ai-news-/.test(file) ? 'daily' : 'special';
  const header = document.querySelector('.header, .special-header');

  const el = (tag, attrs, html) => {
    const n = document.createElement(tag);
    for (const k in attrs || {}) n.setAttribute(k, attrs[k]);
    if (html != null) n.innerHTML = html;
    return n;
  };
  const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const slug = s => s.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');

  /* ---------- Sticky bar + reading progress ---------- */
  const PLAY = '<svg viewBox="0 0 16 16"><path d="M4 2v12l10-6z"/></svg>';
  const PAUSE = '<svg viewBox="0 0 16 16"><path d="M4 2h3v12H4zM9 2h3v12H9z"/></svg>';
  const bar = el('div', { class: 'rb-bar', 'aria-hidden': 'true' },
    '<div class="rb-bar-in">' +
      '<a class="rb-brand" href="../" tabindex="-1">AI <em>Reports</em></a>' +
      '<span class="rb-where"></span>' +
      '<button class="rb-btn rb-audio" type="button" tabindex="-1" hidden aria-label="Play audio briefing"></button>' +
      '<button class="rb-btn rb-theme" type="button" tabindex="-1" aria-label="Toggle theme">◐</button>' +
    '</div><div class="rb-progress"></div>');
  document.body.prepend(bar);
  const where = bar.querySelector('.rb-where');
  const progress = bar.querySelector('.rb-progress');

  bar.querySelector('.rb-theme').addEventListener('click', () => {
    if (typeof window.toggleTheme === 'function') window.toggleTheme();
  });

  function setBar(on) {
    bar.classList.toggle('on', on);
    bar.setAttribute('aria-hidden', String(!on));
    bar.querySelectorAll('a, button').forEach(b => { b.tabIndex = on ? 0 : -1; });
  }
  if (header && 'IntersectionObserver' in window) {
    new IntersectionObserver(([e]) => setBar(!e.isIntersecting && e.boundingClientRect.top < 0)).observe(header);
  }

  let ticking = false;
  function paintProgress() {
    ticking = false;
    const max = document.documentElement.scrollHeight - innerHeight;
    progress.style.transform = `scaleX(${max > 0 ? Math.min(1, scrollY / max) : 0})`;
  }
  addEventListener('scroll', () => { if (!ticking) { ticking = true; requestAnimationFrame(paintProgress); } }, { passive: true });
  paintProgress();

  /* ---------- Section index ---------- */
  let heads = [...document.querySelectorAll('.section-label')]
    .filter(h => !/audio briefing/i.test(h.textContent));
  if (heads.length < 3) heads = [...document.querySelectorAll('.special-section h2, .special-content > h2')];
  const sections = heads.map(h => {
    let label = h.textContent.replace(/\s+/g, ' ').trim();
    // Specials label sections "Part II"; the heading that follows says what it is about.
    const sub = /^(part|section|chapter)\b/i.test(label) && h.parentElement.querySelector('h2');
    if (sub && sub !== h) label = sub.textContent.replace(/\s+/g, ' ').trim();
    if (!h.id) h.id = slug(label) || 'section';
    return { h, label };
  }).filter(s => s.label);

  if (sections.length >= 3) {
    const toc = el('nav', { class: 'rb-toc', 'aria-label': 'Sections' },
      '<div class="rb-toc-h">On this page</div>' +
      sections.map(s => `<a href="#${s.h.id}">${esc(s.label)}</a>`).join(''));
    document.body.append(toc);
    const links = [...toc.querySelectorAll('a')];
    const mark = () => {
      // Current section: the last heading that has scrolled above the middle of the screen.
      let cur = 0;
      sections.forEach((s, i) => { if (s.h.getBoundingClientRect().top < innerHeight * 0.4) cur = i; });
      links.forEach((a, i) => a.setAttribute('aria-current', String(i === cur)));
      where.textContent = scrollY > 200 ? sections[cur].label : '';
    };
    addEventListener('scroll', () => requestAnimationFrame(mark), { passive: true });
    mark();
  }

  /* ---------- Waveform over the audio seek bar ---------- */
  const player = document.getElementById('audioPlayer');
  const audio = document.getElementById('audioEl');
  const seek = document.getElementById('playerSeek');
  const miniBtn = bar.querySelector('.rb-audio');
  if (player && audio && seek) {
    const src = (audio.querySelector('source') || audio).getAttribute('src') || '';
    const wrap = el('div', { class: 'rb-seek' });
    seek.parentNode.insertBefore(wrap, seek);
    wrap.append(seek);

    fetch(src.replace(/\.mp3$/, '.json')).then(r => r.ok ? r.json() : null).then(data => {
      if (!data || !Array.isArray(data.peaks) || !data.peaks.length) return;
      const lo = Math.min(...data.peaks), hi = Math.max(...data.peaks), span = (hi - lo) || 1;
      const wave = el('div', { class: 'rb-wave', 'aria-hidden': 'true' },
        data.peaks.map(v => `<i style="height:${Math.round((0.18 + 0.82 * Math.pow((v - lo) / span, 1.6)) * 100)}%"></i>`).join(''));
      wrap.prepend(wave);
      player.classList.add('has-wave');
      const bars = [...wave.children];
      const paint = () => {
        const f = seek.value / 100;
        bars.forEach((b, i) => b.classList.toggle('on', (i + 0.5) / bars.length <= f));
      };
      audio.addEventListener('timeupdate', paint);
      seek.addEventListener('input', paint);
      paint();
    }).catch(() => {});

    // Playback speed, remembered across the index and every report.
    const RATES = [1, 1.25, 1.5, 2];
    const rateBtn = el('button', { class: 'rb-rate', type: 'button' });
    const setRate = (r, save) => {
      audio.defaultPlaybackRate = r;   // survives the reload the first play triggers
      audio.playbackRate = r;
      rateBtn.textContent = r + '×';
      rateBtn.setAttribute('aria-label', `Playback speed ${r}×, change`);
      if (save) try { localStorage.setItem('ai-reports-rate', String(r)); } catch (e) {}
    };
    rateBtn.addEventListener('click', () => setRate(RATES[(RATES.indexOf(audio.playbackRate) + 1) % RATES.length], true));
    let savedRate = 1;
    try { savedRate = parseFloat(localStorage.getItem('ai-reports-rate')) || 1; } catch (e) {}
    setRate(RATES.includes(savedRate) ? savedRate : 1, false);
    const timeEl = player.querySelector('.player-time');
    timeEl ? timeEl.parentNode.insertBefore(rateBtn, timeEl) : player.append(rateBtn);

    // Mini control in the sticky bar once the briefing has started.
    const syncMini = () => {
      miniBtn.hidden = audio.paused && audio.currentTime === 0;
      miniBtn.innerHTML = (audio.paused ? PLAY : PAUSE) + '<span>Audio</span>';
      miniBtn.setAttribute('aria-label', audio.paused ? 'Play audio briefing' : 'Pause audio briefing');
    };
    miniBtn.addEventListener('click', () => { audio.paused ? audio.play() : audio.pause(); });
    ['play', 'pause', 'ended'].forEach(ev => audio.addEventListener(ev, syncMini));
    syncMini();
  }

  /* ---------- Previous / next ---------- */
  fetch('../reports.json').then(r => r.ok ? r.json() : null).then(data => {
    if (!data || !Array.isArray(data.reports)) return;
    const list = data.reports.filter(r => r.type === type)
      .sort((a, b) => a.date.localeCompare(b.date) || a.file.localeCompare(b.file));
    const i = list.findIndex(r => r.file === file);
    if (i < 0) return;
    const prev = list[i - 1], next = list[i + 1];
    if (!prev && !next) return;
    const MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
    const day = s => { const [y, m, d] = s.split('-').map(Number); return `${d} ${MONTHS[m - 1]}${y !== new Date().getFullYear() ? ' ' + y : ''}`; };
    const label = r => {
      if (r.type !== 'daily') return r.title;
      const lead = (r.summary || '').split(' · ')[0];
      return lead && !/\{\w+\}/.test(lead) ? lead : 'AI News Daily';
    };
    const link = (r, cls, k) => r ? `<a class="${cls}" href="${encodeURI(r.file)}"><span class="k">${k} · ${day(r.date)}</span><span class="t">${esc(label(r))}</span></a>` : '';
    const nav = el('nav', { class: 'rb-pager', 'aria-label': type === 'daily' ? 'Other briefings' : 'Other special reports' },
      link(prev, 'prev', '← Previous') + link(next, 'next', 'Next →'));
    const footer = page.querySelector('.footer');
    footer ? page.insertBefore(nav, footer) : page.append(nav);
  }).catch(() => {});

})();
