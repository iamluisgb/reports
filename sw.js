/* Service worker for AI Reports — https://luisgonzalezbernal.com/reports/
 *
 * Two jobs:
 *
 * 1. **Stay current.** Documents (the homepage, every report) and data
 *    (reports.json, RSS, sitemap) are network-first and revalidated on every
 *    request. GitHub Pages pins everything to `Cache-Control: max-age=600` and its
 *    headers cannot be changed, so a plain fetch may answer from a ten-minute-old
 *    HTTP cache entry; a conditional request revalidates it against the ETag
 *    instead. The cache is only the fallback, never the answer while online.
 *
 * 2. **Work offline.** The shell (styles, scripts, fonts, icons) is cached, and
 *    so is every page you open. Audio is cached only when asked for: the
 *    briefings are 256 MB and do not belong on a phone uninvited.
 *
 * Strategies: network-first for documents and data, stale-while-revalidate for
 * the shell, cache-first with an LRU cap for media.
 */

const VERSION = 'v1';
const SHELL_CACHE = `ai-reports-shell-${VERSION}`;
const PAGE_CACHE = `ai-reports-pages-${VERSION}`;
// Audio the reader asked to keep is their own download, not cached content: it
// survives a version bump, and only the LRU cap evicts it.
const MEDIA_CACHE = 'ai-reports-media';
const KEEP = [SHELL_CACHE, PAGE_CACHE, MEDIA_CACHE];

const BASE = '/reports/';
const OFFLINE_URL = BASE + 'offline.html';
const MEDIA_LIMIT = 45 * 1024 * 1024;   // audio kept offline, oldest evicted first
const TIMEOUT = 4000;                   // how long the network gets before the cache answers

const SHELL = [
  BASE,
  BASE + 'index.html',
  BASE + 'offline.html',
  BASE + 'manifest.json',
  BASE + 'styles.css',
  BASE + 'home.css',
  BASE + 'site.js',
  BASE + 'report.js',
  BASE + 'pwa.js',
  BASE + 'assets/icons/favicon-32.png',
  BASE + 'assets/icons/icon-192.png',
  ...['InstrumentSerif-normal.woff2', 'InstrumentSerif-italic.woff2',
      'Geist-normal.woff2', 'GeistMono-normal.woff2']
    .map(f => `${BASE}assets/fonts/web/${f}`),
];

const isMedia = p => /\/audio\/[\w.-]+\.(mp3|json)$/.test(p);
const isDocument = p => p.endsWith('/') || p.endsWith('.html');
const isData = p => p.endsWith('/reports.json') || p.endsWith('/rss.xml')
  || p.endsWith('/sitemap.xml') || p.endsWith('.md');
const isStatic = p => /\.(css|js|mjs|woff2?|png|svg|ico|webmanifest|json)$/.test(p);

/* ---------- helpers ---------- */

function timedFetch(input, ms = TIMEOUT) {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), ms);
  return fetch(input, { signal: controller.signal }).finally(() => clearTimeout(timer));
}

async function trim(cache, limit) {
  let keys = await cache.keys();
  if (!keys.length) return;
  const sizes = [];
  let total = 0;
  for (const key of keys) {
    const res = await cache.match(key);
    if (!res) continue;
    const len = Number(res.headers.get('content-length')) || (await res.clone().blob()).size;
    sizes.push({ key, len });
    total += len;
  }
  if (total <= limit) return;
  for (const { key, len } of sizes) {           // insertion order: oldest first
    if (total <= limit) break;
    await cache.delete(key);
    total -= len;
  }
}

/* Network-first: fresh if the network answers, cached if it does not. */
async function networkFirst(request, cacheName, navigation) {
  const cache = await caches.open(cacheName);
  try {
    // A navigation request cannot be rebuilt with `new Request(...)` — `mode:
    // "navigate"` is not constructible — so fetch the URL as a plain GET with
    // no-cache. For a static document that is the same response.
    const fresh = navigation
      ? await timedFetch(new Request(request.url, { cache: 'no-cache', credentials: 'same-origin', redirect: 'follow' }))
      : await timedFetch(new Request(request, { cache: 'no-cache' }));
    if (fresh && fresh.status === 200) {
      cache.put(request, fresh.clone());
      return fresh;
    }
    if (fresh) return fresh;                      // 404 and friends: let the page see it
  } catch (err) {
    /* offline, blocked, or slower than TIMEOUT: fall through to the cache */
  }
  const cached = await cache.match(request, { ignoreSearch: true });
  if (cached) return cached;
  if (navigation) {
    const offline = await caches.match(OFFLINE_URL);
    if (offline) return offline;
  }
  return Response.error();
}

/* Stale-while-revalidate: instant from the cache, corrected in the background. */
async function staleWhileRevalidate(request) {
  const cache = await caches.open(SHELL_CACHE);
  const cached = await cache.match(request, { ignoreSearch: true });
  const network = fetch(request).then(res => {
    if (res && res.status === 200) cache.put(request, res.clone());
    return res;
  }).catch(() => null);
  return cached || (await network) || Response.error();
}

/* Cache-first, for media the reader asked to keep. */
async function cacheFirst(request, cacheName, { capped = false } = {}) {
  const cache = await caches.open(cacheName);
  const cached = await cache.match(request, { ignoreSearch: true });
  if (cached) return cached;
  const res = await fetch(request);
  // 206 (a range request) and opaque responses are never worth storing.
  if (res && res.status === 200) {
    await cache.put(request, res.clone());
    if (capped) await trim(cache, MEDIA_LIMIT);
  }
  return res;
}

/* ---------- lifecycle ---------- */

self.addEventListener('install', event => {
  event.waitUntil((async () => {
    const cache = await caches.open(SHELL_CACHE);
    // Individually: one missing file must not fail the whole install.
    await Promise.all(SHELL.map(url =>
      cache.add(new Request(url, { cache: 'no-cache' })).catch(() => {})));
  })());
});

self.addEventListener('activate', event => {
  event.waitUntil((async () => {
    const names = await caches.keys();
    await Promise.all(names
      .filter(n => n.startsWith('ai-reports-') && !KEEP.includes(n))
      .map(n => caches.delete(n)));
    await self.clients.claim();
  })());
});

self.addEventListener('fetch', event => {
  const request = event.request;
  if (request.method !== 'GET') return;

  let url;
  try { url = new URL(request.url); } catch (e) { return; }
  if (url.origin !== self.location.origin) return;      // Umami and everything else
  if (!url.pathname.startsWith(BASE)) return;           // outside the scope we own

  // Seeks send a Range header: let the network answer, those responses are 206
  // and must never be stored.
  if (request.headers.has('range')) return;

  if (isMedia(url.pathname)) {
    // The peaks JSON is small and always wanted with the audio.
    event.respondWith(cacheFirst(request, MEDIA_CACHE, { capped: true }));
    return;
  }
  if (request.mode === 'navigate' || isDocument(url.pathname)) {
    event.respondWith(networkFirst(request, PAGE_CACHE, true));
    return;
  }
  if (isData(url.pathname)) {
    event.respondWith(networkFirst(request, PAGE_CACHE, false));
    return;
  }
  if (isStatic(url.pathname)) {
    event.respondWith(staleWhileRevalidate(request));
  }
});

/* ---------- messages from pwa.js ---------- */

async function saveAudio(url) {
  const cache = await caches.open(MEDIA_CACHE);
  const audio = new URL(url, self.location.origin).href;
  const res = await fetch(new Request(audio, { cache: 'no-cache' }));
  if (!res.ok) throw new Error(`audio ${res.status}`);
  await cache.put(audio, res.clone());
  const bytes = Number(res.headers.get('content-length')) || (await res.clone().blob()).size;
  // The waveform comes from a small JSON beside the mp3; without it the player
  // draws an empty bar offline.
  const peaks = audio.replace(/\.mp3$/, '.json');
  try {
    const p = await fetch(new Request(peaks, { cache: 'no-cache' }));
    if (p.ok) await cache.put(peaks, p.clone());
  } catch (e) { /* the mp3 is what matters */ }
  await trim(cache, MEDIA_LIMIT);
  return bytes;
}

async function cacheSize(cacheName) {
  const cache = await caches.open(cacheName);
  let total = 0;
  for (const key of await cache.keys()) {
    const res = await cache.match(key);
    if (res) total += Number(res.headers.get('content-length')) || (await res.clone().blob()).size;
  }
  return total;
}

self.addEventListener('message', event => {
  const data = event.data || {};
  const reply = payload => { if (event.ports && event.ports[0]) event.ports[0].postMessage(payload); };

  if (data.type === 'SKIP_WAITING') { self.skipWaiting(); return; }

  if (data.type === 'SAVE_AUDIO') {
    event.waitUntil((async () => {
      try {
        const bytes = await saveAudio(data.url);
        reply({ ok: true, bytes, total: await cacheSize(MEDIA_CACHE) });
      } catch (err) {
        reply({ ok: false, error: String(err && err.message || err) });
      }
    })());
    return;
  }

  if (data.type === 'HAS_AUDIO') {
    event.waitUntil((async () => {
      const cache = await caches.open(MEDIA_CACHE);
      reply({ ok: true, cached: !!(await cache.match(new URL(data.url, self.location.origin).href)) });
    })());
    return;
  }

  if (data.type === 'CACHE_SIZE') {
    event.waitUntil((async () => reply({
      ok: true,
      shell: await cacheSize(SHELL_CACHE),
      pages: await cacheSize(PAGE_CACHE),
      media: await cacheSize(MEDIA_CACHE),
    }))());
  }
});
