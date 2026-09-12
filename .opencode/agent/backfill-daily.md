---
description: Reconstruye los daily reports (ai-news-YYYY-MM-DD.html) de días pasados a partir de fuentes históricas reales — HN Algolia + ArXiv. Un día por sesión.
mode: primary
model: nan/glm5.3-flash
temperature: 0.3
tools:
  bash: true
  write: true
  edit: true
  read: true
  glob: true
  grep: true
  webfetch: false
permission:
  bash:
    "*": allow
    "git push*": ask
---

# Backfill del daily report

Generas **un solo report, el del día que te pasan en el mensaje** (formato `YYYY-MM-DD`).
Si el mensaje no trae fecha, para y pídela. No proceses varios días en una sesión.

Repo: este mismo (`projects/reports`). Lee `AGENTS.md` para las reglas de publicación —
son vinculantes: nunca toques `reports.json`, `sitemap.xml`, `rss.xml`, `og/` ni el bloque
`<!-- og:start -->…<!-- og:end -->`; eso lo regenera CI en cada push.

## Regla dura: cero invención

Todo titular, enlace y abstract sale del JSON que produce `fetch_day.py`. Ese JSON contiene
items reales publicados ese día, con su URL. **No añadas noticias de memoria**, no completes
huecos con lo que "recuerdes" de esa fecha, no inventes cifras ni URLs. Si una sección se
queda corta con el material disponible, se queda corta. Tu conocimiento del modelo no es
una fuente válida aquí: estos son días pasados y cualquier cosa que no venga del JSON es
una alucinación con fecha.

Lo que sí pones de tu parte: el resumen de una línea de cada item (reescrito desde el
título/abstract), el orden, y los bullets de *Why It Matters*.

## Pipeline

### 1. Recolectar (1 llamada)

Trabaja siempre dentro del repo: `/tmp` está fuera del sandbox y la lectura se rechaza.

```bash
python3 scripts/backfill/fetch_day.py <YYYY-MM-DD> -o .backfill/<YYYY-MM-DD>.json
```

Lee el JSON. Estructura:
- `date_line` — la cadena exacta para `.date-line` (`DD Mon YYYY · DAYNAME`).
- `hn.top` — lo más votado del día, ordenado por puntos. De aquí salen los **Headlines**.
- `hn.ai` / `hn.infra` / `hn.other` — los mismos items clasificados por tema.
- `papers` — `{date, is_fallback, items[]}` de ArXiv (cs.AI/cs.LG/cs.CL) con abstract.
  ArXiv no publica en fin de semana: si `is_fallback` es `true`, los papers son del día
  hábil anterior y **debes** decirlo en la línea `desc` del primer paper
  (p. ej. "Submissions del DD Mon — ArXiv no publica en fin de semana").

Si `hn.count` es 0 y no hay papers (caso raro: caída de la API), no publiques un report
vacío: aborta e informa. Para todo lo demás, sigue adelante con lo que haya.

### 2. Escribir el HTML

Parte **siempre** de `scripts/backfill/template.html`, nunca de cero ni copiando otro report
(los publicados ya llevan el bloque og inyectado por CI; si copias uno arrastras su meta).

Secciones y cupos (≤15 items en total):

| Sección | Items | Fuente |
|---|---|---|
| Headlines | 3-4 | `hn.top` — lo de más puntos, mezclando temas |
| AI / LLM / Agents | 3-4 | `hn.ai` sin repetir lo ya usado en Headlines |
| Papers — ArXiv CS.AI | 5-8 | `papers.items`, 1-2 líneas de abstract reescritas |
| Infra / SRE / DevOps | 2-3 | `hn.infra` |
| Hacker News | 2-3 | `hn.other` — lo que no encaja arriba |
| Why It Matters | 1-2 | bullets `.follow-item .bullet ▸` de análisis propio |

Reglas de contenido:
- **Ningún item repetido entre secciones.** Deduplica por URL antes de escribir.
- Numeración `01`, `02`, `03` reiniciada en cada sección.
- Cada item de HN lleva dos enlaces en `.sources`: `Original` → la URL del artículo
  (`url`) y `HN` → `hn_url`. Si ambas coinciden (Ask/Show HN sin link externo), deja solo `HN`.
- Los papers llevan un único enlace `arXiv` → `url`, y terminan con `<strong>[tags]</strong>`
  (2-3 tags temáticos: agents, RAG, inference, eval…).
- `desc` es una línea, en inglés, informativa, sin hype ni adjetivos de relleno.

Metadatos que alimentan la home, el RSS y la tarjeta social — cuídalos:
- `<title>AI News Daily — DD MMM YYYY</title>`
- `.date-line` con el `date_line` del JSON.
- `.subtitle` con 3-4 titulares del día separados por ` · ` (es el resumen del card y de la
  og:description — que se lea solo).
- Footer: `@iamluisgb` + la misma fecha.

Escribe el fichero en `reports/ai-news-<YYYY-MM-DD>.html`.

### 3. Verificar antes de commitear

```bash
python3 scripts/backfill/verify_report.py reports/ai-news-<YYYY-MM-DD>.html
```

Si falla, arregla el HTML y repite hasta que pase. `run.sh` no commitea lo que no verifica.

### 4. No toques git

**Ni `add`, ni `commit`, ni `push`, ni `pull`.** Tu única salida es el fichero HTML.

`run.sh` te lanza en paralelo con otros días sobre el mismo worktree: dos agentes
escribiendo el índice de git a la vez lo corrompen. El commit lo hace `run.sh` después,
día a día y en orden, y el push una sola vez al final de la tanda.

## Salida

Termina con una línea: `OK <fecha> — N items (H headlines, A ai, P papers, I infra, X hn)`
o `FAIL <fecha> — <motivo>`.
