from playwright.sync_api import Locator
from pages.base_page import BasePage

class HomePage(BasePage):

    #locators
    @property
    def search_input(self) -> Locator:
         return self.page.get_by_test_id("search__input")


    @property
    def search_button(self) -> Locator:
         return self.page.get_by_test_id("search__button")

    #действия
    def search(self, text, submit_with_enter: bool = False)->None:
        self.page.wait_for_load_state("networkidle")
        self.search_input.fill(text)
        if submit_with_enter:
            self.page.keyboard.press("Enter")
        else:
            self.search_button.click()
