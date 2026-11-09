from playwright.sync_api import Page, expect


def test_main_page_title(page: Page):
    assert page.title()=="Литрес – сервис электронных и аудиокниг, скачать в fb2 и mp3, читать и слушать онлайн на Litres"


def test_audiobook_page_titke(page: Page):
    page.locator("xpath=/html/body/div[4]/header/div[3]/nav/div/a[7]").click()
    expect(page).to_have_title("Аудиокниги – слушать онлайн или скачаgit ть в mp3 на Литрес")
    page.keyboard.press("Enter")