from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators
from .base_page import BasePage

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Link is not correct"

    def should_be_login_form(self):
        try:
            self.browser.find_element(*LoginPageLocators.ID_LOGIN_USERNAME)
            self.browser.find_element(*LoginPageLocators.ID_LOGIN_PASSWORD)
            self.browser.find_element(*LoginPageLocators.ID_LOGIN_BUTTON)
        except NoSuchElementException:
            assert False, "The site does not have a login form."

    def should_be_register_form(self):
        try:
            self.browser.find_element(*LoginPageLocators.ID_REGISTRATION_EMAIL)
            self.browser.find_element(*LoginPageLocators.ID_REGISTRATION_PASSWORD1)
            self.browser.find_element(*LoginPageLocators.ID_REGISTRATION_PASSWORD2)
            self.browser.find_element(*LoginPageLocators.ID_REGISTRATION_BUTTON)
        except NoSuchElementException:
            assert False, "The site does not have a registration form."

    def register_new_user(self, EMAIL, PASSWORD):
        self.browser.find_element(*LoginPageLocators.ID_REGISTRATION_EMAIL).send_keys(EMAIL)
        self.browser.find_element(*LoginPageLocators.ID_REGISTRATION_PASSWORD1).send_keys(PASSWORD)
        self.browser.find_element(*LoginPageLocators.ID_REGISTRATION_PASSWORD2).send_keys(PASSWORD)
        self.browser.find_element(*LoginPageLocators.ID_REGISTRATION_BUTTON).click()

    def check_user_in_autorizared(self):
        try:
            WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "alertinner")))
        except TimeoutException:
            assert False, "Authorization failed"