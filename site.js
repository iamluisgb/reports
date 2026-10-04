// Shared behaviour for every page: theme, the audio player, and the small
// helpers the index and the reports both need. Loaded before report.js and
// before the index's own script. Exposes window.Site.
(function () {
  const MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
  const MONTHS_LONG = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
  const WEEKDAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
  const RATES = [1, 1.25, 1.5, 2];
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

  const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const parseDate = s => { const [y, m, d] = s.split('-').map(Number); return new Date(y, m - 1, d); };
  const fmtDate = s => { const d = parseDate(s); return `${d.getDate()} ${MONTHS[d.getMonth()]} ${d.getFullYear()}`; };
  const store = {
    get: k => { try { return localStorage.getItem(k); } catch (e) { return null; } },
    set: (k, v) => { try { localStorage.setItem(k, v); } catch (e) {} },
  };

  /* ---------- Reports from the manifest ---------- */
  const isBroken = r => !r.summary || /\{\w+\}/.test(r.summary);
  // A daily is titled by its first story; a special by its own title.
  const headline = r => r.type === 'daily'
    ? (isBroken(r) ? 'AI News Daily' : r.summary.split(' · ')[0])
    : r.title.replace(/\s+/g, ' ');

  /* ---------- Theme: follows the system until the reader picks one ('ai-reports-theme') ---------- */
  const systemLight = matchMedia('(prefers-color-scheme: light)');
  function labelToggles() {
    const light = document.documentElement.getAttribute('data-theme') === 'light';
    document.querySelectorAll('.theme-toggle, [data-theme-toggle]').forEach(b => {
      b.textContent = '◐';
      b.setAttribute('aria-label', light ? 'Switch to dark theme' : 'Switch to light theme');
    });
  }
  function applyTheme(theme) {
    if (theme !== 'light' && theme !== 'dark') theme = systemLight.matches ? 'light' : 'dark';
    if (theme === 'light') document.documentElement.setAttribute('data-theme', 'light');
    else document.documentElement.removeAttribute('data-theme');
    labelToggles();
  }
  function toggleTheme() {
    const next = document.documentElement.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
    const flip = () => applyTheme(next);
    document.startViewTransition && !reduce ? document.startViewTransition(flip) : flip();
    store.set('ai-reports-theme', next);
  }

  /* ---------- Audio player ----------
     Markup (make_audio.py writes it; the index builds the same):
     .audio-player > audio, button.play-btn, .player-body > .player-meta >
     (.player-title, .player-time) + input[type=range]. */
  const mmss = s => { s = Math.max(0, Math.round(s)); return Math.floor(s / 60) + ':' + String(s % 60).padStart(2, '0'); };

  function waveHeights(peaks) {
    const lo = Math.min(...peaks), hi = Math.max(...peaks), span = (hi - lo) || 1;
    return peaks.map(v => Math.round((0.18 + 0.82 * Math.pow((v - lo) / span, 1.6)) * 100));
  }

  function initPlayer(player) {
    if (!player || player.dataset.ready) return;
    const audio = player.querySelector('audio');
    const btn = player.querySelector('.play-btn');
    const time = player.querySelector('.player-time');
    const seek = player.querySelector('input[type="range"]');
    if (!audio || !btn || !seek) return;
    player.dataset.ready = '1';

    // Fallback length from the "0:00 / 4:59" the markup ships with.
    const shipped = (time && time.textContent.match(/(\d+):(\d\d)\s*$/)) || null;
    let total = shipped ? (+shipped[1]) * 60 + (+shipped[2]) : 0;
    const dur = () => audio.duration || total;
    const src = (audio.querySelector('source') || audio).getAttribute('src') || '';

    // Seek bar: the range input stays for keyboard and screen readers; the wave is drawn under it.
    const wrap = document.createElement('div');
    wrap.className = 'seek';
    seek.parentNode.insertBefore(wrap, seek);
    wrap.append(seek);
    let bars = [];
    fetch(src.replace(/\.mp3$/, '.json')).then(r => r.ok ? r.json() : null).then(data => {
      if (!data || !Array.isArray(data.peaks) || !data.peaks.length) return;
      if (!total && data.duration) { total = data.duration; paint(); }
      const wave = document.createElement('div');
      wave.className = 'wave';
      wave.setAttribute('aria-hidden', 'true');
      wave.innerHTML = waveHeights(data.peaks).map(h => `<i style="height:${h}%"></i>`).join('');
      wrap.prepend(wave);
      bars = [...wave.children];
      paint();
    }).catch(() => {});

    // Playback speed, remembered across the index and every report.
    const rate = document.createElement('button');
    rate.type = 'button';
    rate.className = 'btn btn-xs';
    const setRate = (r, save) => {
      audio.defaultPlaybackRate = r;   // survives the reload the first play triggers
      audio.playbackRate = r;
      rate.textContent = r + '×';
      rate.setAttribute('aria-label', `Playback speed ${r}×, change`);
      if (save) store.set('ai-reports-rate', String(r));
    };
    rate.addEventListener('click', () => setRate(RATES[(RATES.indexOf(audio.playbackRate) + 1) % RATES.length], true));
    const saved = parseFloat(store.get('ai-reports-rate'));
    setRate(RATES.includes(saved) ? saved : 1, false);
    time ? time.parentNode.insertBefore(rate, time) : player.append(rate);

    function paint() {
      const d = dur(), f = d ? audio.currentTime / d : 0;
      seek.value = f * 100;
      if (time) time.textContent = d ? `${mmss(audio.currentTime)} / ${mmss(d)}` : '';
      bars.forEach((b, i) => b.classList.toggle('on', (i + 0.5) / bars.length <= f));
    }
    const sync = () => {
      player.classList.toggle('playing', !audio.paused);
      btn.setAttribute('aria-label', audio.paused ? 'Play audio briefing' : 'Pause audio briefing');
    };
    btn.addEventListener('click', () => { audio.paused ? audio.play().catch(() => {}) : audio.pause(); });
    ['play', 'pause', 'ended'].forEach(ev => audio.addEventListener(ev, sync));
    audio.addEventListener('timeupdate', paint);
    audio.addEventListener('loadedmetadata', paint);
    seek.addEventListener('input', () => {
      const go = () => { audio.currentTime = (seek.value / 100) * dur(); };
      if (audio.readyState) go();
      else { audio.preload = 'metadata'; audio.addEventListener('loadedmetadata', go, { once: true }); audio.load(); }
    });
    paint();
  }

  window.Site = {
    MONTHS, MONTHS_LONG, WEEKDAYS, esc, parseDate, fmtDate, store,
    isBroken, headline, waveHeights, initPlayer, applyTheme, toggleTheme, reduce,
  };
  // Older report markup calls these from inline onclick handlers.
  window.toggleTheme = toggleTheme;
  window.applyTheme = applyTheme;

  /* ---------- Start ---------- */
  applyTheme(store.get('ai-reports-theme'));
  systemLight.addEventListener('change', () => { if (!store.get('ai-reports-theme')) applyTheme(null); });
  document.querySelectorAll('[data-theme-toggle]').forEach(b => {
    if (!b.hasAttribute('onclick')) b.addEventListener('click', toggleTheme);
  });
  document.querySelectorAll('.audio-player').forEach(initPlayer);
})();
