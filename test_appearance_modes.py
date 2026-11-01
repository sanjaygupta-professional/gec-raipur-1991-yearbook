import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

WORKSPACE = Path("/home/sanjayg4/gec-raipur-1991-yearbook")
BASE_URL = "http://localhost:8089"

async def test_appearance():
    async with async_playwright() as p:
        browser = await p.chromium.launch(args=["--no-sandbox"])
        try:
            page = await browser.new_page(viewport={"width": 1440, "height": 900})
            
            console_errors = []
            page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)
            
            # Clear local storage first
            await page.goto(f"{BASE_URL}/landing.html", wait_until="networkidle")
            await page.evaluate("() => localStorage.clear()")
            await page.reload(wait_until="networkidle")
            
            # 1. Verify default theme mode is blueprint
            mode = await page.get_attribute("html", "data-theme-mode")
            assert mode == "blueprint", f"Expected blueprint mode by default, got {mode}"
            print("✓ Default theme mode on landing.html is blueprint.")
            await page.screenshot(path=str(WORKSPACE / "assets/screenshot_blueprint_landing.png"))
            print("✓ Saved screenshot_blueprint_landing.png")
            
            # 2. Switch to Heritage
            heritage_btn = page.locator('.appearance-switcher button[data-mode="heritage"]').first
            await heritage_btn.click()
            await page.wait_for_timeout(250)
            mode = await page.get_attribute("html", "data-theme-mode")
            assert mode == "heritage", f"Expected heritage mode, got {mode}"
            print("✓ Switched to Forged Heritage mode successfully.")
            await page.screenshot(path=str(WORKSPACE / "assets/screenshot_heritage_landing.png"))
            print("✓ Saved screenshot_heritage_landing.png")

            # 3. Switch to Flow & Connection
            flow_btn = page.locator('.appearance-switcher button[data-mode="flow"]').first
            await flow_btn.click()
            await page.wait_for_timeout(250)
            mode = await page.get_attribute("html", "data-theme-mode")
            assert mode == "flow", f"Expected flow mode, got {mode}"
            print("✓ Switched to Flow & Connection mode successfully.")
            await page.screenshot(path=str(WORKSPACE / "assets/screenshot_flow_landing.png"))
            print("✓ Saved screenshot_flow_landing.png")

            # 4. Switch to Linen (Archival Warm Off-White)
            linen_btn = page.locator('.appearance-switcher button[data-mode="linen"]').first
            await linen_btn.click()
            await page.wait_for_timeout(300)
            mode = await page.get_attribute("html", "data-theme-mode")
            assert mode == "linen", f"Expected linen mode, got {mode}"
            print("✓ Switched to Archival Linen mode successfully.")
            
            # Verify name visibility on landing.html hero photo in linen mode
            # Check computed color and background of face-label
            await page.wait_for_selector(".face-tag.is-on .face-label", state="visible", timeout=5000)
            label_styles = await page.evaluate("""() => {
                const label = document.querySelector('.face-tag.is-on .face-label');
                if (!label) return null;
                const cs = window.getComputedStyle(label);
                return {
                    color: cs.color,
                    bgColor: cs.backgroundColor,
                    border: cs.border
                };
            }""")
            print("✓ Landing face-label computed styles in Linen mode:", label_styles)
            assert label_styles is not None, "Face label element not found"
            # Color should be dark text (rgb(29, 25, 20)), background should be white (rgb(255, 255, 255))
            assert "rgb(255, 255, 255)" in label_styles["bgColor"], f"Expected white background in linen, got {label_styles['bgColor']}"
            assert "rgb(29, 25, 20)" in label_styles["color"], f"Expected dark text in linen, got {label_styles['color']}"
            print("✓ VERIFIED: Face names in Linen mode on landing photo have dark high-contrast text on white background!")

            # Dimension dividers check
            dividers_count = await page.locator(".dimension-divider").count()
            print(f"✓ Found {dividers_count} engineering dimension dividers on landing page.")
            assert dividers_count >= 5, f"Expected at least 5 dimension dividers, found {dividers_count}"

            await page.screenshot(path=str(WORKSPACE / "assets/screenshot_linen_landing.png"))
            print("✓ Saved screenshot_linen_landing.png")

            # 5. Switch to Dark
            dark_btn = page.locator('.appearance-switcher button[data-mode="dark"]').first
            await dark_btn.click()
            await page.wait_for_timeout(250)
            mode = await page.get_attribute("html", "data-theme-mode")
            assert mode == "dark", f"Expected dark mode, got {mode}"
            print("✓ Switched to Obsidian Dark mode successfully.")
            
            # 6. Test index.html with theme persistence and name toggle
            await page.goto(f"{BASE_URL}/index.html", wait_until="networkidle")
            mode = await page.get_attribute("html", "data-theme-mode")
            assert mode == "dark", f"Expected persisted dark mode on index.html, got {mode}"
            print("✓ Index.html inherited persisted theme mode: dark")

            # Switch to Linen on index.html
            viewer_linen = page.locator('.appearance-switcher button[data-mode="linen"]').first
            await viewer_linen.click()
            await page.wait_for_timeout(300)
            mode = await page.get_attribute("html", "data-theme-mode")
            assert mode == "linen", f"Expected linen mode on viewer, got {mode}"
            print("✓ Switched index.html to Linen mode.")

            # Test Toggle Names button (#toggleNamesBtn)
            toggle_names_btn = page.locator("#toggleNamesBtn")
            await toggle_names_btn.click()
            await page.wait_for_timeout(300)

            # Canvas should have class show-all-names
            canvas_classes = await page.locator("#canvas").get_attribute("class")
            assert "show-all-names" in canvas_classes, f"Canvas missing show-all-names class: {canvas_classes}"
            print("✓ #toggleNamesBtn activated: canvas has 'show-all-names' class.")

            # Check tooltip styles in Linen mode with show-all-names active
            tooltip_styles = await page.evaluate("""() => {
                const tooltip = document.querySelector('.face-pin .face-tooltip');
                const nameEl = document.querySelector('.face-pin .tooltip-name');
                if (!tooltip || !nameEl) return null;
                const csTooltip = window.getComputedStyle(tooltip);
                const csName = window.getComputedStyle(nameEl);
                return {
                    tooltipBg: csTooltip.backgroundColor,
                    tooltipOpacity: csTooltip.opacity,
                    nameColor: csName.color,
                    border: csTooltip.border
                };
            }""")
            print("✓ Viewer face-tooltip computed styles in Linen mode:", tooltip_styles)
            assert tooltip_styles is not None, "Tooltip element not found"
            assert float(tooltip_styles["tooltipOpacity"]) >= 0.9, f"Tooltip should be visible, got opacity {tooltip_styles['tooltipOpacity']}"
            assert "rgb(255, 255, 255)" in tooltip_styles["tooltipBg"], f"Expected white tooltip bg in linen, got {tooltip_styles['tooltipBg']}"
            assert "rgb(29, 25, 20)" in tooltip_styles["nameColor"], f"Expected dark text in linen, got {tooltip_styles['nameColor']}"
            print("✓ VERIFIED: All names over photo in Linen mode are crisp dark text on white cards!")

            await page.screenshot(path=str(WORKSPACE / "assets/screenshot_linen_viewer_all_names.png"))
            print("✓ Saved screenshot_linen_viewer_all_names.png")

            # Switch to Blueprint on index.html
            viewer_bp = page.locator('.appearance-switcher button[data-mode="blueprint"]').first
            await viewer_bp.click()
            await page.wait_for_timeout(300)
            await page.screenshot(path=str(WORKSPACE / "assets/screenshot_blueprint_viewer.png"))
            print("✓ Saved screenshot_blueprint_viewer.png")

            # Click a face to open profile modal and verify
            first_pin = page.locator(".face-pin").first
            await first_pin.click()
            await page.wait_for_timeout(400)
            modal = page.locator("#profileModalOverlay")
            modal_class = await modal.get_attribute("class")
            assert "open" in modal_class, f"Expected modal to be open, got {modal_class}"
            print("✓ Clicked face pin: Profile modal opened cleanly.")

            # Close modal
            await page.locator("#closeModalBtn").click()
            await page.wait_for_timeout(200)
            modal_class_after = await modal.get_attribute("class")
            assert "open" not in modal_class_after, "Modal should be closed"
            print("✓ Closed profile modal successfully.")

            print(f"Total console errors: {len(console_errors)}")
            assert len(console_errors) == 0, f"Errors: {console_errors}"
            print("ALL 5 THEMES, NAME VISIBILITY DEFECT FIX, AND TOGGLE NAMES TESTS PASSED!")
            
        finally:
            await browser.close()
            print("Browser closed cleanly.")

if __name__ == "__main__":
    asyncio.run(test_appearance())
