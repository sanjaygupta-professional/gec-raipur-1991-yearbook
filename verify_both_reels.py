import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

WORKSPACE = Path("/home/sanjayg4/gec-raipur-1991-yearbook")
BASE_HTTP = "http://localhost:8089"
BASE_FILE = f"file://{WORKSPACE}"

async def verify_all():
    async with async_playwright() as p:
        browser = await p.chromium.launch(args=["--no-sandbox"])
        try:
            page = await browser.new_page(viewport={"width": 1440, "height": 900})
            
            console_errors = []
            page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)
            
            # --- TEST 1: landing.html (HTTP) ---
            print("1. Testing landing.html over HTTP...")
            await page.goto(f"{BASE_HTTP}/landing.html", wait_until="networkidle")
            await page.wait_for_selector("#landingReelLeft .milestone-card", timeout=5000)
            await page.wait_for_selector("#landingReelRight .milestone-card", timeout=5000)
            
            left_hero_cards = await page.locator("#landingReelLeft .milestone-card").count()
            right_hero_cards = await page.locator("#landingReelRight .milestone-card").count()
            print(f"✓ landing.html Hero Left Reel: {left_hero_cards} cards")
            print(f"✓ landing.html Hero Right Reel: {right_hero_cards} cards")
            assert left_hero_cards == 20, f"Expected 20 left cards, got {left_hero_cards}"
            assert right_hero_cards == 20, f"Expected 20 right cards, got {right_hero_cards}"
            
            # Take screenshot of landing page with moving side reels
            await page.screenshot(path=str(WORKSPACE / "assets/screenshot_landing_hero_reels.png"))
            print("✓ Saved screenshot_landing_hero_reels.png")
            
            # Click card on landing reel
            await page.locator("#landingReelLeft .milestone-card").first.click(force=True)
            await page.wait_for_timeout(350)
            landing_modal = page.locator("#landingMilestoneModal")
            modal_class = await landing_modal.get_attribute("class")
            assert "open" in modal_class, "Landing milestone modal should be open"
            print("✓ Clicked landing reel card: Milestone modal opened.")
            await page.locator("#closeLandingMilestoneBtn").click()
            await page.wait_for_timeout(200)

            # --- TEST 2: index.html (HTTP) ---
            print("2. Testing index.html over HTTP...")
            await page.goto(f"{BASE_HTTP}/index.html", wait_until="networkidle")
            await page.wait_for_selector("#ambientReelLeft .milestone-card", timeout=5000)
            await page.wait_for_selector("#ambientReelRight .milestone-card", timeout=5000)
            
            viewer_left = await page.locator("#ambientReelLeft .milestone-card").count()
            viewer_right = await page.locator("#ambientReelRight .milestone-card").count()
            print(f"✓ index.html Left Reel: {viewer_left} cards")
            print(f"✓ index.html Right Reel: {viewer_right} cards")
            assert viewer_left == 20, f"Expected 20 left cards on viewer, got {viewer_left}"
            assert viewer_right == 20, f"Expected 20 right cards on viewer, got {viewer_right}"
            
            await page.screenshot(path=str(WORKSPACE / "assets/screenshot_viewer_reels.png"))
            print("✓ Saved screenshot_viewer_reels.png")

            # --- TEST 3: file:/// protocol check (Crucial for offline opening) ---
            print("3. Testing file:/// protocol directly (no server)...")
            await page.goto(f"{BASE_FILE}/landing.html", wait_until="load")
            await page.wait_for_timeout(600)
            file_landing_left = await page.locator("#landingReelLeft .milestone-card").count()
            print(f"✓ file:/// landing.html Left Reel: {file_landing_left} cards")
            assert file_landing_left == 20, f"Expected 20 cards on file:// landing, got {file_landing_left}"

            await page.goto(f"{BASE_FILE}/index.html", wait_until="load")
            await page.wait_for_timeout(600)
            file_viewer_left = await page.locator("#ambientReelLeft .milestone-card").count()
            print(f"✓ file:/// index.html Left Reel: {file_viewer_left} cards")
            assert file_viewer_left == 20, f"Expected 20 cards on file:// index, got {file_viewer_left}"

            # --- TEST 4: Tiled / Half-screen viewport (960px width on 1920x1080) ---
            print("4. Testing 960px tiled window width...")
            await page.set_viewport_size({"width": 960, "height": 900})
            await page.goto(f"{BASE_HTTP}/index.html", wait_until="networkidle")
            reel_is_visible = await page.locator("#ambientReelLeft").is_visible()
            print(f"✓ At 960px width, #ambientReelLeft is visible: {reel_is_visible}")
            assert reel_is_visible, "Reels MUST be visible at 960px width on a 1920x1080 display"
            await page.screenshot(path=str(WORKSPACE / "assets/screenshot_960px_tiled_reels.png"))
            print("✓ Saved screenshot_960px_tiled_reels.png")

            print(f"Total console errors: {len(console_errors)}")
            assert len(console_errors) == 0, f"Errors: {console_errors}"
            print("ALL REELS VERIFICATION TESTS PASSED WITH ZERO CONSOLE ERRORS!")

        finally:
            await browser.close()
            print("Browser closed cleanly.")

if __name__ == "__main__":
    asyncio.run(verify_all())
