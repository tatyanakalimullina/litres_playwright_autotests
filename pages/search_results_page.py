import re

from playwright.sync_api import Locator, expect
from pages.base_page import BasePage

class SearchResultsPage(BasePage):

    #locators
    @property
    def results_title(self) -> Locator:
         return self.page.get_by_role("heading", level=1)

    @property
    def books(self) -> Locator:
        return self.page.get_by_test_id("art__wrapper")

    @property
    def russian_filtr(self) -> Locator:
        # кликабельна подпись фильтра: настоящий input скрыт и перекрыт label
        return self.page.locator("label[for='languages-ru']")

    @property
    def russian_filtr_checkbox(self) -> Locator:
        return self.page.locator("#languages-ru")

    @property
    def subscription_switch(self) -> Locator:
        return self.page.locator('[role="switch"][aria-description*="Подпиской"]')

    #методы
    def results_heading(self, text) -> Locator:
        return self.page.get_by_role("heading", name=f'Результаты поиска «{text}»')

    #проверки
    def expect_search_url(self, text) -> None:
        expect(self.page).to_have_url(f"https://www.litres.ru/search/?q={text}")

    def expect_russian_filter_in_url(self) -> None:
        expect(self.page).to_have_url(re.compile(r"languages=ru"))

    def expect_subscription_switch(self, on: bool) -> None:
        expect(self.subscription_switch).to_have_attribute("aria-checked", "true" if on else "false")

    def expect_russian_filter_checked(self) -> None:
        expect(self.russian_filtr_checkbox).to_be_checked()

    def expect_results_heading(self, text, timeout: int = 15000) -> None:
        expect(self.results_heading(text)).to_be_visible(timeout=timeout)

    def expect_title_contains(self, text) -> None:
        expect(self.results_title).to_contain_text(text)

    def expect_books_count(self, count: int, timeout: int = 10000) -> None:
        expect(self.books).to_have_count(count, timeout=timeout)
