from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://playwright.dev/python/docs/intro")
    page.screenshot(path="screenshot/homepage.png")
    browser.close()