from .pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"


def test_guest_can_go_to_login_page(browser):
    login_page = LoginPage(browser, link)
    login_page.open()
    login_page.should_be_login_page()
