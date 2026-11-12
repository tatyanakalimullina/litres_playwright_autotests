import pytest


@pytest.mark.parametrize("text", ["python"])
def test_main_actions(page, home, results, text):
    home.search(text, submit_with_enter=True)
    results.expect_search_url(text)

    results.subscription_switch.click()
    results.expect_subscription_switch(True)    # само дождётся асинхронного обновления

    results.subscription_switch.click()
    results.expect_subscription_switch(False)    # вернули в исходное состояние

    results.russian_filtr.click()
    results.expect_russian_filter_checked()      # input стал checked
    results.expect_russian_filter_in_url()


@pytest.mark.parametrize("text", ["Самоучитель python"])
def test_waiting(page, home, results, text):
    home.search(text)

    results.expect_results_heading(text)
    results.expect_title_contains(text)
    results.expect_books_count(24)
