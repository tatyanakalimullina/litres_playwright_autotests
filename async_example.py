from playwright.async_api import async_playwright
import asyncio

async def main():
    async with async_playwright() as p:
        browser = await  p.chromium.launch(headless=False)
        page= await browser.new_page()
        await page.goto("https://hh.ru/resume/dd010804ff0071eac30039ed1f736563726574")
        await page.screenshot(path="screenshot/resume.png")
        await browser.close()

asyncio.run(main())