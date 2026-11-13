import re

from playwright.sync_api import Page, expect

from pages.base_page import BASE_URL


def test_locator_role(page: Page):
    page.get_by_role(role="link", name="С чего начать").click()
    # заголовок SPA-страницы обновляется с задержкой — проверяем по фрагменту, а не точной строке
    expect(page).to_have_title(re.compile(r"Рекомендации для вас"))


def test_locator_placeholder(page: Page):
    page.wait_for_load_state("networkidle")  # даём React завершить гидрацию input
    page.get_by_placeholder("Искать на Литрес").fill("Игра престолов")
    page.keyboard.press("Enter")
    expect(
        page.get_by_role("heading", name="Результаты поиска «Игра престолов»")
    ).to_be_visible(timeout=15000)


def test_locator_datatestid(page: Page):
    page.get_by_test_id("tab-login").click()
    expect(page.get_by_text("Почта или логин")).to_be_visible()


def test_locator_alttext(page: Page):
    page.goto(f"{BASE_URL}/audiobooks/")
    page.get_by_alt_text("Логотип Литрес").click()
    expect(page).to_have_url(f"{BASE_URL}/")


def test_locator_title(page: Page):
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")  # футер лениво догружается
    expect(page.get_by_title("YouTube")).to_be_visible(timeout=15000)
