from .base_page import BasePage
from .locators import BasePageLocators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class BasketPage(BasePage):
    
    def check_basket_is_empty(self):
        try:
            self.browser.find_element(*BasePageLocators.BASKET_IS_EMPTY)
        except NoSuchElementException:
            return True
        
        return False

    def should_not_be_success_message(self):
        assert self.check_basket_is_empty(), "В корзине имеется какой то товар check_basket_is_empty"

    def check_basket_is_empty_message(self):
        try:
            assert self.browser.find_element(*BasePageLocators.BASKET_IS_EMPTY_MESSAGE).text in BasePageLocators.BASKET_IS_EMPTY_MESSAGE_TEXT, "В корзине имеются какие то товары check_basket_is_empty_message"
        except:
            return True

        return False

    def should_not_be_success_message_text(self):
        assert self.check_basket_is_empty_message(), "В корзине имеется какой то товар check_basket_is_empty_message"