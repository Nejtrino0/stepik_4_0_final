from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def basket_is_empty_select_count_product_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.SELECT_COUNT_PRODUCT)

    def text_empty_basket_is_present(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_EMPTY_BASKET)
