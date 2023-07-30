from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasePageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Ссылка не корректна"

    def should_be_login_form(self):
        try:
            self.browser.find_element(*LoginPageLocators.ID_LOGIN_USERNAME)
            self.browser.find_element(*LoginPageLocators.ID_LOGIN_PASSWORD)
            self.browser.find_element(*LoginPageLocators.ID_LOGIN_BUTTON)
        except NoSuchElementException:
            assert False, "На сайте не имеется форма для логина "

    def should_be_register_form(self):
        try:
            self.browser.find_element(*LoginPageLocators.ID_REGISTRATION_EMAIL)
            self.browser.find_element(*LoginPageLocators.ID_REGISTRATION_PASSWORD1)
            self.browser.find_element(*LoginPageLocators.ID_REGISTRATION_PASSWORD2)
            self.browser.find_element(*LoginPageLocators.ID_REGISTRATION_BUTTON)
        except NoSuchElementException:
            assert False, "На сайте не имеется форма для регистрации "

    def register_new_user(self, EMAIL, PASSWORD):
        self.browser.find_element(*LoginPageLocators.ID_REGISTRATION_EMAIL).send_keys(EMAIL)
        self.browser.find_element(*LoginPageLocators.ID_REGISTRATION_PASSWORD1).send_keys(PASSWORD)
        self.browser.find_element(*LoginPageLocators.ID_REGISTRATION_PASSWORD2).send_keys(PASSWORD)
        self.browser.find_element(*LoginPageLocators.ID_REGISTRATION_BUTTON).click()

    def check_user_in_autorizared(self):
        try:
            WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "alertinner")))
        except TimeoutException:
            assert False, "Вы не смогли авторизоваться"