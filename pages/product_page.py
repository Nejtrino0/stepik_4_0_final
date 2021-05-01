from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def success_add_to_basket(self):
        self.name_of_product_in_success_message_is_present()
        self.price_of_product_is_correct()

    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def name_of_product_in_success_message_is_present(self):
        name_of_product_in_success_message = self.browser.find_element(
            *ProductPageLocators.NAME_OF_PRODUCT_IN_SUCCESS_MESSAGE).text
        product_name = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT_AFTER_ADD_TO_BASKET).text
        assert name_of_product_in_success_message == product_name

    def price_of_product_is_correct(self):
        price_in_message = self.browser.find_element(*ProductPageLocators.PRICE_OF_PRODUCT_IN_MESSAGE).text
        price = self.browser.find_element(*ProductPageLocators.PRICE_OF_PRODUCT).text
        assert price == price_in_message

    def message_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.NAME_OF_PRODUCT_IN_SUCCESS_MESSAGE), \
            "Есть сообщение об успехе"

    def user_cant_see_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.NAME_OF_PRODUCT_IN_SUCCESS_MESSAGE), \
            "Есть сообщение об успехе"
