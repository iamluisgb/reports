"""NaN (api.nan.builders) for the research pipeline: chat, embeddings, rerank.

Chat reuses write_report.post(): streaming (Cloudflare cuts non-streamed answers at
100 s), a browser User-Agent (the edge answers 403/1010 to Python's default), and
parse_json() that survives fenced or chatty replies. NaN rejects concurrent calls
on one key, so everything here is serial.
"""
from __future__ import annotations

import json
import math
import os
import sys
import time
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from write_report import UA, parse_json, post  # noqa: E402

BASE = os.environ.get("NAN_BASE_URL", "https://api.nan.builders/v1")
# Extraction is many small, single-document jobs: the fast model first, the strong one
# as fallback. Low reasoning effort keeps the budget for the answer.
EXTRACT_MODELS = os.environ.get("RESEARCH_MODELS", "deepseek-v4-flash,glm5.3-flash").split(",")


def key() -> str:
    k = os.environ.get("NAN_API_KEY", "").strip()
    if not k:
        raise SystemExit("NAN_API_KEY not set")
    return k


def chat_json(prompt: str, label: str, effort: str = "low", tries: int = 2) -> tuple[dict, str]:
    """Ask each model in turn until one returns parseable JSON."""
    for model in EXTRACT_MODELS:
        for _ in range(tries):
            started = time.time()
            try:
                payload = {"model": model, "temperature": 0.2, "max_tokens": 16000,
                           "messages": [{"role": "user", "content": prompt}]}
                if effort:
                    payload["reasoning_effort"] = effort
                data = post(payload, key())
                text = (data["choices"][0]["message"].get("content") or "").strip()
                result = parse_json(text)
                print(f"  {label}: {model} {time.time() - started:.0f}s", file=sys.stderr)
                return result, model
            except Exception as exc:   # network, 524, truncated or unparseable JSON
                print(f"  ! {label}: {model} failed ({str(exc)[:120]})", file=sys.stderr)
                time.sleep(3)
    raise RuntimeError(f"{label}: every model failed")


def _post_json(endpoint: str, body: dict, timeout: int = 120) -> dict:
    req = urllib.request.Request(f"{BASE}/{endpoint}", data=json.dumps(body).encode(), method="POST",
                                 headers={"Authorization": f"Bearer {key()}", "Content-Type": "application/json",
                                          "User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.load(r)


def embed(texts: list[str], batch: int = 32) -> list[list[float]]:
    out: list[list[float]] = []
    for i in range(0, len(texts), batch):
        data = _post_json("embeddings", {"model": "qwen3-embedding", "input": texts[i:i + batch]})
        out.extend(d["embedding"] for d in sorted(data["data"], key=lambda d: d["index"]))
    return out


def rerank(query: str, documents: list[str]) -> list[float]:
    """Relevance of each document to the query, in the documents' order (0–1)."""
    if not documents:
        return []
    data = _post_json("rerank", {"model": "rerank", "query": query, "documents": documents})
    scores = [0.0] * len(documents)
    for r in data.get("results", []):
        scores[r["index"]] = float(r["relevance_score"])
    return scores


def cosine(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    na, nb = math.sqrt(sum(x * x for x in a)), math.sqrt(sum(y * y for y in b))
    return dot / (na * nb) if na and nb else 0.0
