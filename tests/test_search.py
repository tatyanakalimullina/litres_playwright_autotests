import pytest

from test_data.loader import load_search_data


@pytest.mark.parametrize("td", load_search_data(ids=["python_books", "game_of_thrones"]))
def test_search_url(home, results, td):
    home.search(td.query, submit_with_enter=True)
    results.expect_search_url(td.query)


@pytest.mark.parametrize("td", load_search_data(ids=["python_books", "game_of_thrones"]))
def test_subscription_toggle(home, results, td):
    home.search(td.query, submit_with_enter=True)

    results.subscription_switch.click()
    results.expect_subscription_switch(True)     # само дождётся асинхронного обновления

    results.subscription_switch.click()
    results.expect_subscription_switch(False)    # вернули в исходное состояние


@pytest.mark.parametrize("td", load_search_data(ids=["python_books", "game_of_thrones"]))
def test_russian_filter(home, results, td):
    home.search(td.query, submit_with_enter=True)

    results.russian_filter.click()
    results.expect_russian_filter_checked()      # input стал checked
    results.expect_russian_filter_in_url()


@pytest.mark.parametrize("td", load_search_data(ids=["self_edu_python"]))
def test_results_count(home, results, td):
    home.search(td.query)

    results.expect_results_heading(td.query)
    results.expect_title_contains(td.query)
    results.expect_books_count(td.expected_count)
