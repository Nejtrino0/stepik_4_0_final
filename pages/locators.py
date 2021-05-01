from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators():
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[name="login_submit"]')
    REGISRATION_BUTTON = (By.CSS_SELECTOR, 'button[name="registration_submit"]')
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    EMAIL_ADDRESS = (By.CSS_SELECTOR, 'input[type="email"]#id_registration-email')
    PASSWORD = (By.CSS_SELECTOR, 'input[type="password"]#id_registration-password1')
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, 'input[type="password"]#id_registration-password2')


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, 'button[value = "Add to basket"]')
    NAME_OF_PRODUCT_IN_SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages > :nth-child(1) > .alertinner strong')
    NAME_OF_PRODUCT_AFTER_ADD_TO_BASKET = (By.CSS_SELECTOR, '.product_main > h1')
    PRICE_OF_PRODUCT = (By.CSS_SELECTOR, '.product_main > p:nth-child(2)')
    PRICE_OF_PRODUCT_IN_MESSAGE = (By.CSS_SELECTOR, '#messages > :last-child >  :nth-child(2)  strong')


class BasketPageLocators():
    SELECT_COUNT_PRODUCT = (By.CSS_SELECTOR, '.row  input[type="number"]')
    TEXT_EMPTY_BASKET = (By.CSS_SELECTOR, 'div#content_inner')
