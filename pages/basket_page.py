from selenium.common.exceptions import NoSuchElementException
from .locators import BasePageLocators
from .base_page import BasePage

class BasketPage(BasePage):
    def check_basket_is_empty(self):
        try:
            self.browser.find_element(*BasePageLocators.BASKET_IS_EMPTY)
        except NoSuchElementException:
            return True
        return False

    def check_basket_is_empty_message(self):
        try:
           BasePageLocators.BASKET_IS_EMPTY_MESSAGE_TEXT in self.browser.find_element(*BasePageLocators.BASKET_IS_EMPTY_MESSAGE).text # Проверка только англоязычного сайта на данный момент
        except:
            return False
        return True

    def should_not_be_success_message(self):
        assert self.check_basket_is_empty(), "There is some product in the basket (check by html tag)"

    def should_not_be_success_message_text(self):
        assert self.check_basket_is_empty_message(), "There is some product in the basket (check by message)"