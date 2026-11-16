from pathlib import Path
from shutil import rmtree

import allure
import pytest
from playwright.sync_api import Page

from pages.base_page import BASE_URL
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage


@pytest.fixture(autouse=True, scope="session")
def _clean_screenshots():
    """Скриншоты — только текущего запуска.
    allure-results чистится флагом --clean-alluredir (сам плагин владеет папкой)."""
    rmtree("screenshot", ignore_errors=True)
    yield


@pytest.fixture(autouse=True)
def open_litres(page: Page):
    page.goto(BASE_URL)
    yield page


@pytest.fixture
def home(page: Page) -> HomePage:
    return HomePage(page)


@pytest.fixture
def results(page: Page) -> SearchResultsPage:
    return SearchResultsPage(page)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Кладём отчёт pytest в атрибуты теста — фикстуры ниже читают rep_call."""
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)


@pytest.fixture(autouse=True)
def screenshot_on_failure(page, request):
    """При падении: скриншот в файл (для быстрой диагностики) и вложением в Allure."""
    yield

    rep = getattr(request.node, "rep_call", None)
    if rep and rep.failed:
        png = page.screenshot(full_page=True)

        path = Path("screenshot") / f"{request.node.name}.png"
        path.parent.mkdir(exist_ok=True)
        path.write_bytes(png)

        allure.attach(png, name="Screenshot on failure", attachment_type=allure.attachment_type.PNG)
