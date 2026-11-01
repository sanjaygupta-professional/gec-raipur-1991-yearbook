import asyncio
import os
from playwright.async_api import async_playwright

async def verify():
    workspace = "/home/sanjayg4/gec-raipur-1991-yearbook"
    landing_url = f"file://{workspace}/landing.html"
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(args=["--no-sandbox"])
        try:
            # 1. Desktop Test (1440x900)
            page = await browser.new_page(viewport={"width": 1440, "height": 900})
            
            console_errors = []
            page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)
            
            await page.goto(landing_url, wait_until="networkidle")
            
            title = await page.title()
            print(f"[Desktop] Page title: {title}")
            
            # Scroll to trigger IntersectionObservers
            await page.evaluate("window.scrollTo(0, 800)")
            await page.wait_for_timeout(400)
            await page.evaluate("window.scrollTo(0, 1600)")
            await page.wait_for_timeout(400)
            await page.evaluate("window.scrollTo(0, 2400)")
            await page.wait_for_timeout(400)
            await page.evaluate("window.scrollTo(0, 0)")
            await page.wait_for_timeout(400)
            
            # Full page screenshot
            desktop_shot = f"{workspace}/assets/landing_preview_desktop.png"
            await page.screenshot(path=desktop_shot, full_page=True)
            print(f"[Desktop] Full page screenshot saved: {desktop_shot}")
            
            # Total face cards initially
            all_cards = await page.locator(".face-card").count()
            print(f"[Desktop] Initial face cards rendered: {all_cards} (expected 67)")
            assert all_cards == 67, f"Expected 67 faces, got {all_cards}"
            
            # Test face tab switching
            seated_tab = page.locator('.row-tabs button[data-row="Sitting (Front Row)"]')
            await seated_tab.click()
            await page.wait_for_timeout(200)
            seated_cards = await page.locator(".face-card").count()
            print(f"[Desktop] Cards after 'Seated faculty' click: {seated_cards} (expected 15)")
            assert seated_cards == 15, f"Expected 15 seated, got {seated_cards}"
            
            # Test search form submit with "Sanjay Gupta"
            search_input = page.locator('[data-find-form] input[name="name"]').first
            await search_input.fill("Sanjay Gupta")
            await page.wait_for_timeout(200)
            
            submit_btn = page.locator('[data-find-form] button[type="submit"]').first
            await submit_btn.click()
            await page.wait_for_timeout(1000)
            
            current_url = page.url
            print(f"[Desktop] URL after search submit: {current_url}")
            
            # Verify deep-link navigation
            assert "index.html" in current_url
            assert "person=std1-16" in current_url or "q=Sanjay" in current_url
            
            # Wait for index.html initialization & active pin / toast
            await page.wait_for_selector(".toast-msg.show, .face-pin.active-selected", timeout=6000)
            print("[Index] Hotspot spotlight / toast successfully triggered on deep-linked face!")
            
            # Screenshot of the active deep-linked state on index.html
            index_shot = f"{workspace}/assets/index_deeplink_test.png"
            await page.screenshot(path=index_shot)
            print(f"[Index] Screenshot saved: {index_shot}")
            
            await page.close()
            
            # 2. Mobile Test (390x844)
            mobile_page = await browser.new_page(viewport={"width": 390, "height": 844})
            mobile_page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)
            
            await mobile_page.goto(landing_url, wait_until="networkidle")
            
            # Test mobile nav open
            hamburger = mobile_page.locator(".menu-toggle")
            await hamburger.click()
            await mobile_page.wait_for_timeout(400)
            
            mobile_shot_nav = f"{workspace}/assets/landing_preview_mobile_nav.png"
            await mobile_page.screenshot(path=mobile_shot_nav)
            print(f"[Mobile] Nav screenshot saved: {mobile_shot_nav}")
            
            # Close nav
            await hamburger.click()
            await mobile_page.wait_for_timeout(300)
            
            # Mobile full page screenshot
            mobile_shot = f"{workspace}/assets/landing_preview_mobile.png"
            await mobile_page.screenshot(path=mobile_shot, full_page=True)
            print(f"[Mobile] Full page screenshot saved: {mobile_shot}")
            
            await mobile_page.close()
            
            print(f"Total console errors encountered: {len(console_errors)}")
            if console_errors:
                print("Errors:", console_errors)
            assert len(console_errors) == 0, f"Encountered console errors: {console_errors}"
            print("ALL VERIFICATION CHECKS PASSED PERFECTLY!")
                
        finally:
            await browser.close()
            print("Browser closed successfully.")

if __name__ == "__main__":
    asyncio.run(verify())
