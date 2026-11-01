import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

WORKSPACE = Path("/home/sanjayg4/gec-raipur-1991-yearbook")

async def test_themes():
    async with async_playwright() as p:
        # Bundled browser only, no executablePath
        browser = await p.chromium.launch(args=["--no-sandbox"])
        try:
            page = await browser.new_page(viewport={"width": 1440, "height": 950})
            
            console_errors = []
            page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)
            
            # 1. Test index.html with themes
            await page.goto(f"file://{WORKSPACE}/index.html", wait_until="networkidle")
            print("Loaded index.html successfully.")
            
            # Test switching to Blueprint
            await page.click('button[data-theme="blueprint"]')
            await page.wait_for_timeout(300)
            overlay_src = await page.get_attribute("#themeFrameOverlay", "src")
            assert "theme_blueprint.svg" in overlay_src, f"Expected theme_blueprint.svg, got {overlay_src}"
            print("✓ Blueprint theme activated successfully.")
            
            # Capture Blueprint screenshot
            await page.screenshot(path=str(WORKSPACE / "assets/screenshot_theme_blueprint.png"))
            print("✓ Saved screenshot_theme_blueprint.png")
            
            # Test switching to 1991 Cinema
            await page.click('button[data-theme="cinema"]')
            await page.wait_for_timeout(300)
            overlay_src = await page.get_attribute("#themeFrameOverlay", "src")
            assert "theme_cinema.svg" in overlay_src, f"Expected theme_cinema.svg, got {overlay_src}"
            print("✓ Bollywood Cinema theme activated successfully.")
            
            # Capture Cinema screenshot
            await page.screenshot(path=str(WORKSPACE / "assets/screenshot_theme_cinema.png"))
            print("✓ Saved screenshot_theme_cinema.png")
            
            # Test face spotlight under a theme (Sanjay Gupta)
            await page.fill("#searchInput", "Sanjay Gupta")
            await page.wait_for_timeout(300)
            await page.click(".alumni-card")
            await page.wait_for_timeout(500)
            overlay_class = await page.get_attribute("#profileModalOverlay", "class")
            assert "open" in overlay_class, f"Expected modal overlay to have class open, got {overlay_class}"
            print("✓ Profile modal opened for Sanjay Gupta.")
            
            # Close modal
            await page.click("#closeModalBtn")
            await page.wait_for_timeout(200)
            
            # 2. Test landing.html with Apple Bento Grid & 35th Jubilee Special section
            await page.goto(f"file://{WORKSPACE}/landing.html", wait_until="networkidle")
            
            # Verify Apple Bento Grid
            bento_count = await page.locator(".bento-card").count()
            print(f"✓ Found {bento_count} Apple Bento cards on landing.html (expected 4).")
            assert bento_count == 4, f"Expected 4 bento cards, got {bento_count}"
            
            await page.wait_for_selector("#styles", timeout=4000)
            cards_count = await page.locator(".style-card").count()
            print(f"✓ Found {cards_count} style cards on landing.html (expected 5).")
            assert cards_count == 5, f"Expected 5 style cards, got {cards_count}"
            
            # Capture landing page styles section screenshot
            styles_sec = page.locator("#styles")
            await styles_sec.screenshot(path=str(WORKSPACE / "assets/screenshot_landing_styles.png"))
            print("✓ Saved screenshot_landing_styles.png")
            
            print(f"Total console errors: {len(console_errors)}")
            assert len(console_errors) == 0, f"Errors: {console_errors}"
            print("ALL THEME TESTS PASSED PERFECTLY!")
            
        finally:
            await browser.close()
            print("Browser closed cleanly.")

if __name__ == "__main__":
    asyncio.run(test_themes())
