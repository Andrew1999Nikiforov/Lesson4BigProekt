from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage):
    def go_to_login_page(self):
        self.browser.find_element(*MainPageLocators.REGISTRATION_LINK).click()
