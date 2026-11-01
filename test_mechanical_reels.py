import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

WORKSPACE = Path("/home/sanjayg4/gec-raipur-1991-yearbook")
BASE_URL = "http://localhost:8089"

async def test_reels_and_milestones():
    async with async_playwright() as p:
        browser = await p.chromium.launch(args=["--no-sandbox"])
        try:
            page = await browser.new_page(viewport={"width": 1440, "height": 900})
            
            console_errors = []
            page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)
            
            # 1. Test index.html with ambient side reels
            print("--- Testing index.html with 35-Year Ambient Reels ---")
            await page.goto(f"{BASE_URL}/index.html", wait_until="networkidle")
            
            # Wait for milestone cards to render
            await page.wait_for_selector(".ambient-reel-left .milestone-card", timeout=5000)
            await page.wait_for_selector(".ambient-reel-right .milestone-card", timeout=5000)
            
            left_cards_count = await page.locator(".ambient-reel-left .milestone-card").count()
            right_cards_count = await page.locator(".ambient-reel-right .milestone-card").count()
            print(f"✓ Left reel rendered {left_cards_count} cards (Foundations).")
            print(f"✓ Right reel rendered {right_cards_count} cards (Modern & Robotics).")
            assert left_cards_count >= 10, f"Expected at least 10 left cards, found {left_cards_count}"
            assert right_cards_count >= 10, f"Expected at least 10 right cards, found {right_cards_count}"
            
            # Take desktop screenshot with reels active flanking the 1991 photo
            await page.screenshot(path=str(WORKSPACE / "assets/screenshot_reels_active_desktop.png"))
            print("✓ Saved screenshot_reels_active_desktop.png")
            
            # Click a milestone card (e.g., Carnot Cycle) to open the Engineering Memory Modal
            first_card = page.locator(".ambient-reel-left .milestone-card").first
            await first_card.click(force=True)
            await page.wait_for_timeout(350)
            
            modal = page.locator("#milestoneModalOverlay")
            modal_class = await modal.get_attribute("class")
            assert "open" in modal_class, "Milestone modal should be open"
            
            modal_title = await page.locator("#milestoneModalTitle").inner_text()
            modal_formula = await page.locator("#milestoneModalFormula").inner_text()
            modal_memory = await page.locator("#milestoneModalMemory").inner_text()
            print(f"✓ Milestone modal opened cleanly for: '{modal_title}'")
            print(f"✓ Governing formula displayed: '{modal_formula}'")
            print(f"✓ Nostalgic memory: {modal_memory[:60]}...")
            assert len(modal_formula) > 5, "Formula should be populated"
            assert len(modal_memory) > 10, "Nostalgic batch memory should be populated"
            
            await page.screenshot(path=str(WORKSPACE / "assets/screenshot_milestone_modal.png"))
            print("✓ Saved screenshot_milestone_modal.png")
            
            # Close milestone modal
            await page.locator("#closeMilestoneModalBtn").click()
            await page.wait_for_timeout(250)
            modal_class_after = await modal.get_attribute("class")
            assert "open" not in modal_class_after, "Milestone modal should be closed"
            print("✓ Milestone modal closed cleanly.")
            
            # Test HUD toggle button (#toggleReelsBtn) to collapse side reels
            toggle_reels_btn = page.locator("#toggleReelsBtn")
            await toggle_reels_btn.click()
            await page.wait_for_timeout(300)
            stage_classes = await page.locator("#stageMainArea").get_attribute("class")
            assert "reels-collapsed" in stage_classes, "Stage should have 'reels-collapsed' class"
            print("✓ #toggleReelsBtn toggled reels off (collapsed).")
            
            await toggle_reels_btn.click()
            await page.wait_for_timeout(300)
            stage_classes_restored = await page.locator("#stageMainArea").get_attribute("class")
            assert "reels-collapsed" not in stage_classes_restored, "Stage should restore reels"
            print("✓ #toggleReelsBtn toggled reels back on.")

            # 2. Test landing.html 35-Year Timeline Section
            print("--- Testing landing.html 35-Year Timeline Section ---")
            await page.goto(f"{BASE_URL}/landing.html#milestones", wait_until="networkidle")
            await page.wait_for_selector("#milestonesGrid .milestone-card", timeout=5000)
            
            total_grid_cards = await page.locator("#milestonesGrid .milestone-card").count()
            print(f"✓ Landing page rendered {total_grid_cards} total milestones.")
            assert total_grid_cards == 20, f"Expected 20 milestones on landing, got {total_grid_cards}"
            
            # Filter by Classroom Roots (1987-1991)
            foundations_tab = page.locator('.timeline-tabs button[data-era="foundations"]')
            await foundations_tab.click()
            await page.wait_for_timeout(250)
            foundation_cards = await page.locator("#milestonesGrid .milestone-card").count()
            print(f"✓ Filtered to Classroom Foundations: {foundation_cards} cards.")
            assert foundation_cards == 10, f"Expected 10 foundation cards, got {foundation_cards}"
            
            # Filter by Modern Era (1991-2026)
            modern_tab = page.locator('.timeline-tabs button[data-era="modern"]')
            await modern_tab.click()
            await page.wait_for_timeout(250)
            modern_cards = await page.locator("#milestonesGrid .milestone-card").count()
            print(f"✓ Filtered to Modern Era & Robotics: {modern_cards} cards.")
            assert modern_cards == 10, f"Expected 10 modern cards, got {modern_cards}"

            # Filter back to All
            await page.locator('.timeline-tabs button[data-era="all"]').click()
            await page.wait_for_timeout(250)
            await page.screenshot(path=str(WORKSPACE / "assets/screenshot_landing_milestones_section.png"))
            print("✓ Saved screenshot_landing_milestones_section.png")

            # 3. Test responsive mobile view (<1100px)
            print("--- Testing mobile viewport responsiveness ---")
            await page.set_viewport_size({"width": 768, "height": 900})
            await page.goto(f"{BASE_URL}/index.html", wait_until="networkidle")
            
            left_reel_visible = await page.locator("#ambientReelLeft").is_visible()
            print(f"✓ On tablet (768px), ambient reel left is_visible: {left_reel_visible}")
            assert not left_reel_visible, "Ambient reels should be hidden on mobile/tablet to give photo 100% width"

            print(f"Total console errors: {len(console_errors)}")
            assert len(console_errors) == 0, f"Console errors detected: {console_errors}"
            print("ALL REELS, MILESTONES, AND TIMELINE TESTS PASSED WITH 0 ERRORS!")

        finally:
            await browser.close()
            print("Browser closed cleanly.")

if __name__ == "__main__":
    asyncio.run(test_reels_and_milestones())
