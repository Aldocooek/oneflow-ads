# OneFlow Ads — MAXX design brief

Repo pro Filipa. Úkol: vytvořit **5 nových statických reklam OneFlow** (1080×1350, česky, bez CTA) — lepší design než reference, **stejná designová DNA**.

## Co kde je
- **[`PROMPT-CZ.md`](PROMPT-CZ.md)** — kompletní zadání. **Přečti první.** Design dělej na **Fable 5**.
- `reference/`
  - `oneflow-funds-ad-v1.png` — baseline render (ten máš překonat).
  - `ad-funds.html` — zdrojový kód baseline (barvy, fonty, váhy, **inline logo SVG**).
  - `oneflow-brand-manual-v2026.html` — **HTML brand manuál OneFlow** (otevři v prohlížeči).
- `render-all.py` — vyrenderuje každý `*.html` v kořeni složky na stejnojmenné `.png` (Playwright).

## Postup
1. Přečti `PROMPT-CZ.md` + otevři brand manuál.
2. Vytvoř `oneflow-fund-1.html` … `oneflow-fund-5.html` v kořeni.
3. `pip install playwright && playwright install chromium`
4. `python3 render-all.py`
5. Ověř výsledné pixely (otevři každý PNG).

**Výstup = 5 PNG (1080×1350) v kořeni složky.**
