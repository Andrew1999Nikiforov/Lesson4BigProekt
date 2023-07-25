from selenium.webdriver.common.by import By

class MainPageLocators():
    pass

class LoginPageLocators():
    ID_LOGIN_USERNAME = (By.ID, "id_login-username")
    ID_LOGIN_PASSWORD = (By.ID, "id_login-password")
    ID_LOGIN_BUTTON = (By.NAME, "login_submit")

    ID_REGISTRATION_EMAIL = (By.ID, "id_registration-email")
    ID_REGISTRATION_PASSWORD1 = (By.ID, "id_registration-password1")
    ID_REGISTRATION_PASSWORD2 = (By.ID, "id_registration-password2")
    ID_REGISTRATION_BUTTON = (By.NAME, "registration_submit")

class ProductAddBusketPageLocators():
    BUTTON_ADD_BUSKET = (By.CLASS_NAME, "btn-add-to-basket")

class CheckProductNamePageLocators():
    XPATH_GET_NAME_BEFORE_PRODUCT = (By.XPATH, "//div[@class='col-sm-6 product_main']/h1")
    XPATH_GET_NAME_AFTER_PRODUCT = (By.XPATH, "//div[@class='alertinner ']/strong")
    Product_name_before_adding = ""
    Product_name_after_adding = ""

class PriceProductPageLocators():
    CSS_SELECTOR_PRODUCT_BEFORE_ADD_BASKET = (By.CSS_SELECTOR, ".product_main .price_color")
    CSS_SELECTOR_PRODUCT_AFTER_ADD_BASKET = (By.CSS_SELECTOR, ".alert-info .alertinner strong")

class SuccessMesasages():
    CSS_SELECTOR_PRODUCT_SUCCESS_ADDING_PRODUCT_TO_BASKET = (By.CSS_SELECTOR, ".alert-success .alertinner strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, 'span.btn-group a.btn.btn-default')
    BASKET_IS_EMPTY = (By.CLASS_NAME, "basket-title")
    BASKET_IS_EMPTY_MESSAGE = (By.ID, "content_inner")
    BASKET_IS_EMPTY_MESSAGE_TEXT = "Your basket is empty."