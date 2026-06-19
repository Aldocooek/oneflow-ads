"""Vyrenderuje KAŽDÝ *.html v této složce do stejnojmenného .png (1080x1350 @2x).
Spuštění:  python3 render-all.py
Reference/ se ignoruje (renderuje se jen kořen složky)."""
from playwright.sync_api import sync_playwright
import pathlib

HERE = pathlib.Path(__file__).parent
htmls = sorted(p for p in HERE.glob("*.html"))

if not htmls:
    print("Žádné .html v kořeni složky. Vytvoř oneflow-fund-1.html ... oneflow-fund-5.html a spusť znovu.")
else:
    with sync_playwright() as p:
        b = p.chromium.launch()
        for html in htmls:
            out = html.with_suffix(".png")
            page = b.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=2)
            page.goto(html.as_uri(), wait_until="networkidle")
            page.evaluate("document.fonts.ready")
            page.wait_for_timeout(600)
            page.screenshot(path=str(out), clip={"x": 0, "y": 0, "width": 1080, "height": 1350})
            page.close()
            print("WROTE", out.name)
        b.close()
