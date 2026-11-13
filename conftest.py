from pathlib import Path
from shutil import rmtree

import pytest
from playwright.sync_api import Page

from pages.base_page import BASE_URL
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage


@pytest.fixture(autouse=True, scope="session")
def _clean_screenshots():
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
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            path = Path("screenshot") / f"{item.name}.png"
            path.parent.mkdir(exist_ok=True)
            page.screenshot(path=str(path))
