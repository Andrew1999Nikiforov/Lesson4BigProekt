from .base_page import BasePage
from .locators import ProductAddBusketPageLocatort


class ProductPage(BasePage):
    def click_to_button_add_busket(self):
        self.browser.find_element(*ProductAddBusketPageLocatort.BUTTON_ADD_BUSKET).click()
