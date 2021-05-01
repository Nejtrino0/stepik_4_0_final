from .pages.product_page import ProductPage
from .pages.basket_page import BasePage
from .pages.login_page import LoginPage
import pytest
from .pages.locators import ProductPageLocators
from .pages.basket_page import BasketPage
import time
from random import randint

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_cant_see_success_message(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    assert product_page.is_not_element_present(*ProductPageLocators.NAME_OF_PRODUCT_IN_SUCCESS_MESSAGE), \
        "Есть сообщение об успехе"


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.success_add_to_basket()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    assert product_page.is_not_element_present(*ProductPageLocators.NAME_OF_PRODUCT_IN_SUCCESS_MESSAGE), \
        "Есть сообщение об успехе"


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.message_disappeared_after_adding_product_to_basket()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_is_empty_select_count_product_is_empty()
    basket_page.text_empty_basket_is_present()


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function")
    def setup(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        email = str(time.time()) + "@fakemail.org"
        password = randint(40000000000, 900000000000)
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser, setup):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.user_cant_see_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser, setup):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_to_basket()
        product_page.success_add_to_basket()
