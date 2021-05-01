from .base_page import BasePage
from .locators import LoginPageLocators
import time
from random import randint
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON)

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISRATION_BUTTON)

    def register_new_user(self, email, password):
        email_address = self.browser.find_element(*LoginPageLocators.EMAIL_ADDRESS)
        email_address.send_keys(email)
        password_input = self.browser.find_element(*LoginPageLocators.PASSWORD)
        password_input.send_keys(password)
        confirm_password = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD)
        confirm_password.send_keys(password)
        reg_button = self.browser.find_element(*LoginPageLocators.REGISRATION_BUTTON)
        reg_button.click()
