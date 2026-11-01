import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

WORKSPACE = Path("/home/sanjayg4/gec-raipur-1991-yearbook")
THEMES_DIR = WORKSPACE / "assets/themes"

THEMES = [
    ("archival", "theme_archival.svg", "composite_archival.jpg"),
    ("blueprint", "theme_blueprint.svg", "composite_blueprint.jpg"),
    ("contactsheet", "theme_contactsheet.svg", "composite_contactsheet.jpg"),
    ("cinema", "theme_cinema.svg", "composite_cinema.jpg"),
    ("cad", "theme_cad.svg", "composite_cad.jpg"),
]

async def render_composites():
    async with async_playwright() as p:
        browser = await p.chromium.launch(args=["--no-sandbox"])
        try:
            page = await browser.new_page(viewport={"width": 1520, "height": 1212})
            
            for theme_id, svg_file, out_file in THEMES:
                html_content = f"""<!DOCTYPE html>
<html>
<head>
  <style>
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    body {{ width: 1520px; height: 1212px; background: #000; overflow: hidden; position: relative; }}
    .photo {{ position: absolute; left: 160px; top: 160px; width: 1200px; height: 892px; object-fit: cover; z-index: 1; }}
    .frame {{ position: absolute; left: 0; top: 0; width: 1520px; height: 1212px; z-index: 2; pointer-events: none; }}
  </style>
</head>
<body>
  <img class="photo" src="{WORKSPACE / 'assets/photo_deskewed.jpg'}">
  <img class="frame" src="{THEMES_DIR / svg_file}">
</body>
</html>"""
                
                temp_html = THEMES_DIR / f"_temp_{theme_id}.html"
                temp_html.write_text(html_content)
                
                await page.goto(f"file://{temp_html}", wait_until="networkidle")
                await page.wait_for_timeout(300)
                
                out_path = THEMES_DIR / out_file
                await page.screenshot(path=str(out_path), quality=95, type="jpeg")
                print(f"✓ Rendered {out_file} (1520x1212)")
                
                if temp_html.exists():
                    temp_html.unlink()
                    
        finally:
            await browser.close()
            print("Finished rendering all 5 composite theme images.")

if __name__ == "__main__":
    asyncio.run(render_composites())
