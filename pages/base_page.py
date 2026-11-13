from playwright.sync_api import Page

BASE_URL = "https://www.litres.ru"


class BasePage:

    def __init__(self, page: Page):
        self.page = page
