from playwright.sync_api import Page, expect

def test_waiting(page: Page):
    page.wait_for_load_state("networkidle")
    page.get_by_test_id("search__input").fill("Самоучитель python")
    page.get_by_test_id("search__button").click()

    expect(
        page.get_by_role("heading", name="Результаты поиска «Самоучитель python»")
    ).to_be_visible(timeout=15000)


