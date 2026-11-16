import re
import allure
from urllib.parse import quote

from playwright.sync_api import Locator, expect

from pages.base_page import BASE_URL, BasePage


class SearchResultsPage(BasePage):

    #locators
    @property
    def results_title(self) -> Locator:
         return self.page.get_by_role("heading", level=1)

    @property
    def books(self) -> Locator:
        return self.page.get_by_test_id("art__wrapper")

    @property
    def russian_filter(self) -> Locator:
        # кликабельна подпись фильтра: настоящий input скрыт и перекрыт label
        return self.page.locator("label[for='languages-ru']")

    @property
    def russian_filter_checkbox(self) -> Locator:
        return self.page.locator("#languages-ru")

    @property
    def subscription_switch(self) -> Locator:
        return self.page.locator('[role="switch"][aria-description*="Подпиской"]')

    #actions
    def results_heading(self, text) -> Locator:
        return self.page.get_by_role("heading", name=f'Результаты поиска «{text}»')

    #проверки
    @allure.step("Проверка url")
    def expect_search_url(self, text, timeout: int = 15000) -> None:
        # page.url отдаёт кириллицу в percent-кодировке — кодируем ожидание так же;
        # SPA-переход медленный, дефолтных 5 с под нагрузкой не хватает
        expect(self.page).to_have_url(f"{BASE_URL}/search/?q={quote(text)}", timeout=timeout)

    @allure.step("Проверка русского фильтра в url")
    def expect_russian_filter_in_url(self) -> None:
        expect(self.page).to_have_url(re.compile(r"languages=ru"))

    @allure.step("Проверка тоггла Доступно по подписке")
    def expect_subscription_switch(self, on: bool) -> None:
        expect(self.subscription_switch).to_have_attribute("aria-checked", "true" if on else "false")

    @allure.step("Проверка русского фильтра")
    def expect_russian_filter_checked(self) -> None:
        expect(self.russian_filter_checkbox).to_be_checked()

    @allure.step("Проверка заголовка страницы результатов")
    def expect_results_heading(self, text, timeout: int = 15000) -> None:
        expect(self.results_heading(text)).to_be_visible(timeout=timeout)

    @allure.step("Проверка текста в заголовке")
    def expect_title_contains(self, text) -> None:
        expect(self.results_title).to_contain_text(text)

    @allure.step("Проверка числа найденных книг")
    def expect_books_count(self, count: int, timeout: int = 10000) -> None:
        expect(self.books).to_have_count(count, timeout=timeout)
