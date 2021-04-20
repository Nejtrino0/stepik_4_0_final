from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")



class LoginPageLocators():
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[name="login_submit"]')
    REGISRATION_BUTTON = (By.CSS_SELECTOR, 'button[name="registration_submit"]')
    LOGIN_FROM = (By.CSS_SELECTOR, '#login_form')