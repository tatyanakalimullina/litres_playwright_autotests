import re

from playwright.sync_api import Page, expect

def test_main_actions(page: Page):
    page.wait_for_load_state("networkidle")
    page.get_by_test_id("search__input").fill("python")
    page.keyboard.press("Enter")
    expect(page).to_have_url("https://www.litres.ru/search/?q=python")

    sub = page.locator('[role="switch"][aria-description*="Подпиской"]')
    sub.click()
    expect(sub).to_have_attribute("aria-checked", "true")  # само дождётся асинхронного обновления

    sub.click()
    expect(sub).to_have_attribute("aria-checked", "false")  # вернули в исходное состояние

    page.locator('label[for="languages-ru"]').click()
    expect(page.locator("#languages-ru")).to_be_checked()  # input стал checked
    expect(page).to_have_url(re.compile(r"languages=ru"))


