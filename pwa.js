// Installed-web-app behaviour: register the service worker, tell the reader when
// there is something new, and let them keep a briefing for the commute.
//
// Loaded on every page, after site.js. Everything here is additive: without
// service-worker support the site is exactly what it was before.
(function () {
  const BASE = '/reports/';
  const SW_URL = BASE + 'sw.js';
  const MANIFEST = BASE + 'reports.json';
  const SEEN_GEN = 'ai-reports-seen-gen';     // reports.json "generated" when the reader last looked
  const SEEN_DATE = 'ai-reports-seen-date';   // newest report date at that moment
  const CHECK_EVERY = 60 * 1000;              // throttle: never re-check more often than this

  const store = {
    get: k => { try { return localStorage.getItem(k); } catch (e) { return null; } },
    set: (k, v) => { try { localStorage.setItem(k, String(v)); } catch (e) {} },
  };
  const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));

  /* ---------- Toast: one transient line over the page ---------- */

  let toastEl = null;
  let hideTimer = 0;

  function toast(message, opts) {
    const o = opts || {};
    if (!toastEl) {
      toastEl = document.createElement('div');
      toastEl.className = 'toast';
      toastEl.setAttribute('role', 'status');
      toastEl.setAttribute('aria-live', 'polite');
      document.body.append(toastEl);
    }
    toastEl.innerHTML =
      '<span class="toast-msg">' + message + '</span>' +
      (o.label ? '<button class="btn btn-xs" type="button" data-toast-action></button>' : '') +
      '<button class="toast-x" type="button" data-toast-close aria-label="Dismiss">✕</button>';

    const action = toastEl.querySelector('[data-toast-action]');
    if (action) {
      action.textContent = o.label;
      action.addEventListener('click', () => { hide(); if (o.run) o.run(); });
    }
    toastEl.querySelector('[data-toast-close]').addEventListener('click', hide);

    requestAnimationFrame(() => toastEl.classList.add('on'));
    clearTimeout(hideTimer);
    if (o.ms !== 0) hideTimer = setTimeout(hide, o.ms || 9000);
  }

  function hide() {
    clearTimeout(hideTimer);
    if (toastEl) toastEl.classList.remove('on');
  }

  /* ---------- Theme colour follows the reader's theme, not only the system's
       (the head ships two media-scoped meta tags; from here on we own the tag) ---------- */
  const CHROME = { dark: '#0c0f0e', light: '#f4f5f2' };
  function paintChrome() {
    const light = document.documentElement.getAttribute('data-theme') === 'light';
    document.querySelectorAll('meta[name="theme-color"]').forEach(m => m.remove());
    const meta = document.createElement('meta');
    meta.name = 'theme-color';
    meta.content = light ? CHROME.light : CHROME.dark;
    document.head.append(meta);
  }

  /* ---------- Badge: how many reports the reader has not seen ---------- */

  function badge(n) {
    if (!navigator.setAppBadge) return;
    Promise.resolve(n > 0 ? navigator.setAppBadge(n) : navigator.clearAppBadge()).catch(() => {});
  }

  /* ---------- Freshness ---------- */

  let checking = false;
  let lastCheck = 0;

  function remember(data, latest) {
    store.set(SEEN_GEN, data.generated || '');
    if (latest) store.set(SEEN_DATE, latest.date || '');
  }

  async function checkFresh() {
    if (checking || Date.now() - lastCheck < CHECK_EVERY) return;
    checking = true;
    lastCheck = Date.now();
    let data;
    try {
      // `_` busts the HTTP cache; the service worker matches ignoring the query.
      const res = await fetch(MANIFEST + '?_=' + Date.now(), { cache: 'no-cache' });
      if (!res.ok) return;
      data = await res.json();
    } catch (err) {
      return;                       // offline: whatever the service worker served is what we have
    } finally {
      checking = false;
    }

    const reports = data.reports || [];
    const latest = reports[0];
    if (!latest) return;

    const seenGen = store.get(SEEN_GEN);
    const seenDate = store.get(SEEN_DATE) || '';
    const onLatest = location.pathname.endsWith(latest.file);

    if (onLatest) {                 // reading the newest report counts as seen
      remember(data, latest);
      badge(0);
      return;
    }
    if (seenGen === null) { remember(data, latest); return; }   // first visit: introduce nothing
    if (seenGen === String(data.generated || '')) return;       // nothing changed since the last look

    const fresh = reports.filter(r => r.date > seenDate);
    if (fresh.length) {
      const head = latest.type === 'daily' ? latest.summary.split(' · ')[0] : latest.title;
      toast(fresh.length > 1
        ? `<b>${fresh.length} new reports</b> since your last visit`
        : `New ${latest.type === 'daily' ? 'briefing' : 'special report'}: <b>${esc(head)}</b>`,
        {
          label: fresh.length > 1 ? 'See them' : 'Read it',
          ms: 15000,
          run: () => { remember(data, latest); badge(0); location.href = BASE + 'reports/' + latest.file; },
        });
      badge(fresh.length);
    }
    remember(data, latest);
  }

  /* ---------- "Keep this briefing" on the audio player ---------- */

  function ask(worker, message) {
    return new Promise(resolve => {
      const channel = new MessageChannel();
      const timer = setTimeout(() => resolve({ ok: false, error: 'timeout' }), 30000);
      channel.port1.onmessage = e => { clearTimeout(timer); resolve(e.data); };
      worker.postMessage(message, [channel.port2]);
    });
  }

  function addOfflineButton(player, worker) {
    if (player.dataset.offlineReady) return;
    const audio = player.querySelector('audio');
    const src = audio && ((audio.querySelector('source') || audio).getAttribute('src') || '');
    if (!src || !/\.mp3$/.test(src)) return;
    player.dataset.offlineReady = '1';

    const url = new URL(src, location.href).href;
    const btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'btn btn-xs';
    btn.textContent = 'Keep';
    btn.setAttribute('aria-label', 'Keep this briefing for offline listening');
    const meta = player.querySelector('.player-meta');
    (meta || player).append(btn);

    ask(worker, { type: 'HAS_AUDIO', url }).then(res => {
      if (res && res.cached) { btn.textContent = 'Kept ✓'; btn.disabled = true; }
    });

    btn.addEventListener('click', async () => {
      btn.disabled = true;
      btn.textContent = 'Saving…';
      const res = await ask(worker, { type: 'SAVE_AUDIO', url });
      if (res && res.ok) {
        btn.textContent = 'Kept ✓';
        toast(`Briefing kept offline · ${(res.bytes / 1048576).toFixed(1)} MB`, { ms: 6000 });
      } else {
        btn.disabled = false;
        btn.textContent = 'Keep';
        toast('Could not save the briefing — check the connection.', { ms: 8000 });
      }
    });
  }

  /* ---------- Start ---------- */

  paintChrome();
  new MutationObserver(paintChrome)
    .observe(document.documentElement, { attributes: true, attributeFilter: ['data-theme'] });

  // Loopback is a secure context too: keep it working so the app can be tested
  // locally before it ships.
  const loopback = /^(localhost|127\.0\.0\.1|\[::1\])$/.test(location.hostname);
  if (!('serviceWorker' in navigator) || (location.protocol !== 'https:' && !loopback)) return;

  let reloading = false;
  navigator.serviceWorker.addEventListener('controllerchange', () => {
    if (reloading) location.reload();
  });

  navigator.serviceWorker.register(SW_URL, { scope: BASE, updateViaCache: 'none' })
    .then(reg => {
      // A new build is waiting: say so, and swap when the reader says go.
      reg.addEventListener('updatefound', () => {
        const next = reg.installing;
        if (!next) return;
        next.addEventListener('statechange', () => {
          if (next.state !== 'installed' || !navigator.serviceWorker.controller) return;
          toast('A new version of the site is ready.', {
            label: 'Reload',
            ms: 0,
            run: () => { reloading = true; next.postMessage({ type: 'SKIP_WAITING' }); },
          });
        });
      });
    })
    .catch(() => {});      // no service worker (private mode, blocked): the site still works

  navigator.serviceWorker.ready.then(reg => {
    addOfflineButtonToPlayers(reg);
    checkFresh();
    reg.update().catch(() => {});
  });

  function addOfflineButtonToPlayers(reg) {
    const worker = reg.active;
    if (!worker) return;
    document.querySelectorAll('.audio-player').forEach(p => addOfflineButton(p, worker));
  }

  // Coming back to the app is the one moment a reader expects today's report:
  // iOS has no background sync, so this is where freshness is checked.
  document.addEventListener('visibilitychange', () => {
    if (document.visibilityState === 'visible') checkFresh();
  });

  addEventListener('online', () => checkFresh());
  addEventListener('offline', () => toast('You are offline. Everything you have opened is still here.', { ms: 8000 }));
})();
