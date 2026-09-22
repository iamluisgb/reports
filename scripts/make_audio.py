#!/usr/bin/env python3
"""Turn a day's briefing script into the report's audio player.

Synthesises the script with Kokoro (NaN's OpenAI-compatible /v1/audio/speech),
concatenates the per-speaker segments, writes audio/ai-news-<day>.mp3 and
injects the "Audio Briefing" section plus its player JS into the report.

The script file is plain text with speaker tags, one segment per paragraph:

    [FENRIR] Good morning. Here are the four stories that mattered.
    [SARAH] Alibaba released Qwen 3.8 27B in FP8 on Hugging Face...

Both the section and the JS are injected idempotently: re-running replaces
them rather than stacking copies.

Usage:
  make_audio.py 2026-08-20 --script audio/ai-news-2026-08-20.txt
  make_audio.py 2026-08-20 --check          # report state, synthesise nothing
"""
import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
API = os.environ.get("NAN_BASE_URL", "https://api.nan.builders/v1") + "/audio/speech"
# The quirón skill `media/long-audio` writes dialogue as [HOST_A]/[HOST_B];
# both spellings map to the same English dialogue pair it standardises on.
VOICES = {
    "HOST_A": "am_fenrir", "A": "am_fenrir", "FENRIR": "am_fenrir",
    "HOST_B": "af_sarah", "B": "af_sarah", "SARAH": "af_sarah",
}
# media/long-audio asks for >= 3 minutes; the briefings deliberately sit in a
# tighter four-to-five minute window so the read never overstays.
MIN_SECONDS = 240
MAX_SECONDS = 300
# MP3 frame granularity and container-duration rounding differ between ffprobe
# versions, and an atempo fit that lands on the boundary measures a hair past
# it. Treat the window as inclusive with a second of slack, and aim the fit
# just inside it so the next measurement cannot tip out again.
WINDOW_SLACK = 1.0
# Same loudness target as that skill, so a briefing sits level with the rest.
LOUDNORM = "I=-16:TP=-1.5:LRA=11"
# Kokoro is capped at 15 RPM; stay under it without making a 12-segment
# briefing take a minute to build.
MIN_INTERVAL = 4.5
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36")

SECTION = """    <div class="section">
      <div class="section-label">Audio Briefing</div>

      <div class="audio-player" id="audioPlayer">
        <audio id="audioEl" preload="none">
          <source src="../audio/ai-news-{day}.mp3" type="audio/mpeg">
          Your browser does not support the audio element.
        </audio>
        <button class="play-btn" aria-label="Play audio briefing">
          <svg class="icon-play" viewBox="0 0 16 16"><path d="M4 2l10 6-10 6V2z"/></svg>
          <svg class="icon-pause" viewBox="0 0 16 16"><path d="M3 2h3.5v12H3zM9.5 2H13v12H9.5z"/></svg>
        </button>
        <div class="player-body">
          <div class="player-meta">
            <span class="player-title">AI NEWS DAILY · {pretty} · EN</span>
            <span class="player-time" id="playerTime">0:00 / {mmss}</span>
          </div>
          <input type="range" id="playerSeek" min="0" max="100" value="0" step="0.1" aria-label="Seek">
        </div>
      </div>

    </div>
"""

PLAYER_JS = """  (function() {{
    const player = document.getElementById('audioPlayer');
    if (!player) return;
    const audio = document.getElementById('audioEl');
    const btn = player.querySelector('.play-btn');
    const time = document.getElementById('playerTime');
    const seek = document.getElementById('playerSeek');
    const total = {seconds};

    function fmt(s) {{
      s = Math.max(0, Math.round(s));
      return Math.floor(s / 60) + ':' + String(s % 60).padStart(2, '0');
    }}

    btn.addEventListener('click', () => {{
      if (audio.paused) {{ audio.play(); }} else {{ audio.pause(); }}
    }});

    audio.addEventListener('play', () => player.classList.add('playing'));
    audio.addEventListener('pause', () => player.classList.remove('playing'));
    audio.addEventListener('ended', () => player.classList.remove('playing'));

    audio.addEventListener('loadedmetadata', () => {{
      time.textContent = '0:00 / ' + fmt(audio.duration || total);
    }});

    audio.addEventListener('timeupdate', () => {{
      const dur = audio.duration || total;
      seek.value = (audio.currentTime / dur) * 100;
      time.textContent = fmt(audio.currentTime) + ' / ' + fmt(dur);
    }});

    seek.addEventListener('input', () => {{
      const dur = audio.duration || total;
      audio.currentTime = (seek.value / 100) * dur;
    }});
  }})();
"""


def parse_script(path):
    segments, speaker, buf = [], None, []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        m = re.match(r"\s*\[(\w+)\]\s*(.*)", line)
        if m:
            if speaker and buf:
                segments.append((speaker, " ".join(buf).strip()))
            speaker, buf = m.group(1).upper(), [m.group(2)]
        elif line.strip():
            buf.append(line.strip())
    if speaker and buf:
        segments.append((speaker, " ".join(buf).strip()))

    bad = {s for s, _ in segments} - set(VOICES)
    if bad:
        raise SystemExit(f"unknown speaker tag(s): {sorted(bad)}; known: {sorted(VOICES)}")
    return [(s, t) for s, t in segments if t]


def speak(text, voice, out, key):
    body = json.dumps({"model": "kokoro", "voice": voice,
                       "input": text, "response_format": "mp3"}).encode()
    req = urllib.request.Request(API, data=body, method="POST", headers={
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json",
        # NaN's edge rejects non-browser user agents with 403/1010, and
        # urllib announces itself as Python-urllib by default.
        "User-Agent": UA,
    })
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                data = r.read()
            if len(data) < 500:
                raise RuntimeError(f"suspiciously small audio ({len(data)} bytes)")
            Path(out).write_bytes(data)
            return
        except Exception as exc:
            if attempt == 3:
                raise SystemExit(f"TTS failed for a {voice} segment: {exc}")
            # 15 RPM: a 429 needs real time, not a token retry.
            time.sleep(10 * (attempt + 1))


def have(tool):
    return subprocess.run(["which", tool], capture_output=True).returncode == 0


def concat(parts, out):
    """ffmpeg when it is there; otherwise append the frames.

    The cron host is not guaranteed to have ffmpeg, and MP3 is a frame stream:
    appending files of the same codec and sample rate plays correctly in every
    browser. Kokoro returns a constant 128 kbps 24 kHz mono, so this holds.
    """
    if have("ffmpeg"):
        with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False) as fh:
            for p in parts:
                fh.write(f"file '{p}'\n")
            listing = fh.name
        subprocess.run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", listing,
                        "-c", "copy", str(out)], check=True, capture_output=True)
        os.unlink(listing)
        return
    with open(out, "wb") as dst:
        for p in parts:
            dst.write(Path(p).read_bytes())


def normalise(path):
    """Bring the briefing to the standard loudness target.

    Skipped without ffmpeg — a briefing that is merely un-normalised still
    plays, and the alternative is publishing no audio at all."""
    if not have("ffmpeg"):
        return False
    tmp = Path(str(path) + ".norm.mp3")
    r = subprocess.run(["ffmpeg", "-y", "-i", str(path), "-af", f"loudnorm={LOUDNORM}",
                        "-b:a", "128k", "-ar", "24000", "-ac", "1", str(tmp)],
                       capture_output=True)
    if r.returncode != 0 or not tmp.exists() or tmp.stat().st_size < 500:
        tmp.unlink(missing_ok=True)
        return False
    tmp.replace(path)
    return True


def duration(path):
    """Real duration when ffprobe is available, else estimated from the bitrate.

    The estimate only seeds the player's fallback `total`; the browser replaces
    it with the true duration on loadedmetadata."""
    if have("ffprobe"):
        out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                              "-of", "csv=p=0", str(path)], capture_output=True, text=True, check=True)
        return float(out.stdout.strip())
    return Path(path).stat().st_size * 8 / 128_000


def in_window(seconds):
    return MIN_SECONDS - WINDOW_SLACK <= seconds <= MAX_SECONDS + WINDOW_SLACK


def fit(seconds, path):
    """Pull the briefing into the four-to-five minute window with atempo.

    The script is written to land there on its own; this only catches the day
    Kokoro reads faster or slower than usual. atempo shifts pacing without
    touching pitch, and the correction is small (0.8-1.4x) because the word
    target is already right. Without ffmpeg there is nothing to do but report
    the real duration and let the caller decide.
    """
    if in_window(seconds) or not have("ffmpeg"):
        return seconds
    # Aim a second inside the bound so the re-measure cannot land just past it.
    target = (MIN_SECONDS + WINDOW_SLACK if seconds < MIN_SECONDS
              else MAX_SECONDS - WINDOW_SLACK)
    factor = min(2.0, max(0.5, seconds / target))
    tmp = Path(str(path) + ".fit.mp3")
    r = subprocess.run(["ffmpeg", "-y", "-i", str(path), "-filter:a", f"atempo={factor:.4f}",
                        "-b:a", "128k", "-ar", "24000", "-ac", "1", str(tmp)],
                       capture_output=True)
    if r.returncode != 0 or not tmp.exists() or tmp.stat().st_size < 500:
        tmp.unlink(missing_ok=True)
        return seconds
    tmp.replace(path)
    return duration(path)


def inject(report, day, seconds):
    html = report.read_text(encoding="utf-8")
    mmss = f"{int(seconds // 60)}:{int(seconds % 60):02d}"
    m = re.search(r'class="date-line">(.*?)</div>', html, re.S)
    pretty = " ".join(re.sub(r"<[^>]+>", "", m.group(1)).split()).split(" · ")[0].upper() if m else day

    section = SECTION.format(day=day, pretty=pretty, mmss=mmss)
    existing = re.search(
        r'[ \t]*<div class="section">\s*<div class="section-label">Audio Briefing</div>.*?</div>\s*\n(?=[ \t]*<div class="section">)',
        html, re.S)
    if existing:
        html = html[:existing.start()] + section + html[existing.end():]
    else:
        first = re.search(r'[ \t]*<div class="section">', html)
        if not first:
            raise SystemExit("no <div class=\"section\"> to anchor the audio player to")
        html = html[:first.start()] + section + html[first.start():]

    js = PLAYER_JS.format(seconds=int(round(seconds)))
    old_js = re.search(r"[ \t]*\(function\(\) \{\s*const player = document\.getElementById\('audioPlayer'\);.*?\}\)\(\);\n", html, re.S)
    if old_js:
        html = html[:old_js.start()] + js + html[old_js.end():]
    else:
        anchor = html.find("  function toggleTheme()")
        if anchor == -1:
            raise SystemExit("no toggleTheme() to anchor the player script to")
        html = html[:anchor] + js + "\n" + html[anchor:]

    report.write_text(html, encoding="utf-8")
    return mmss


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("day")
    ap.add_argument("--script", help="briefing script (default: audio/ai-news-<day>.txt)")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--allow-short", action="store_true",
                    help=f"do not fail when the briefing falls outside "
                         f"{MIN_SECONDS}-{MAX_SECONDS}s")
    args = ap.parse_args()

    report = ROOT / "reports" / f"ai-news-{args.day}.html"
    mp3 = ROOT / "audio" / f"ai-news-{args.day}.mp3"
    script = Path(args.script) if args.script else ROOT / "audio" / f"ai-news-{args.day}.txt"

    if not report.exists():
        raise SystemExit(f"no report: {report}")

    if args.check:
        html = report.read_text(encoding="utf-8")
        secs = duration(mp3) if mp3.exists() else 0
        print(f"{args.day}: mp3={'yes' if mp3.exists() else 'NO':3} "
              f"section={'yes' if 'Audio Briefing' in html else 'NO':3} "
              f"script={'yes' if script.exists() else 'NO':3} "
              f"duration={int(secs // 60)}:{int(secs % 60):02d}"
              f"{'' if in_window(secs) else f'  ⚠ outside {MIN_SECONDS}-{MAX_SECONDS}s'}")
        return

    key = os.environ.get("NAN_API_KEY", "").strip()
    if not key:
        raise SystemExit("NAN_API_KEY not set")
    if not script.exists():
        raise SystemExit(f"no briefing script at {script} — write it first")

    segments = parse_script(script)
    if not segments:
        raise SystemExit("briefing script has no speaker segments")

    mp3.parent.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        parts = []
        for i, (speaker, text) in enumerate(segments):
            part = Path(tmp) / f"{i:03d}.mp3"
            speak(text, VOICES[speaker], part, key)
            parts.append(part)
            if i < len(segments) - 1:
                time.sleep(MIN_INTERVAL)
        concat(parts, mp3)

    normalised = normalise(mp3)
    secs = fit(duration(mp3), mp3)
    mmss = inject(report, args.day, secs)
    words = sum(len(t.split()) for _, t in segments)
    in_range = in_window(secs)
    flag = ("" if in_range
            else f"  ⚠ {mmss} is outside the {MIN_SECONDS}-{MAX_SECONDS}s window "
                 f"— {'expand' if secs < MIN_SECONDS else 'cut'} the script")
    print(f"{args.day}: {len(segments)} segments, {words} words, {mmss}, "
          f"{mp3.stat().st_size // 1024} KB, loudnorm={'yes' if normalised else 'SKIPPED'}"
          f" -> {mp3.relative_to(ROOT)}{flag}")
    if not in_range and not args.allow_short:
        sys.exit(2)


if __name__ == "__main__":
    main()
