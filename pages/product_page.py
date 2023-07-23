from .base_page import BasePage
from .locators import ProductAddBusketPageLocators
from .locators import CheckProductNamePageLocators
from .locators import PriceProductPageLocators

class ProductPage(BasePage):
    def click_to_button_add_busket(self):
        self.browser.find_element(*ProductAddBusketPageLocators.BUTTON_ADD_BUSKET).click()

    def check_before_add_name_product(self):
        get_name_product = self.browser.find_element(*CheckProductNamePageLocators.XPATH_GET_NAME_BEFORE_PRODUCT)
        self.Product_name_before_adding = get_name_product.text

    def check_after_add_name_product(self):
        get_name_product = self.browser.find_element(*CheckProductNamePageLocators.XPATH_GET_NAME_AFTER_PRODUCT)
        self.Product_name_after_adding = get_name_product.text
        assert self.Product_name_before_adding == self.Product_name_after_adding, "Название товара в каталоге и в корзине отличаются"

    def check_price_before_and_after_add_basket(self):
        price_before_click_add = self.browser.find_element(*PriceProductPageLocators.CLASS_PRODUCT_BEFORE_ADD_BASKET)
        price_after_click_add = self.browser.find_element(*PriceProductPageLocators.XPATH_PRODUCT_AFTER_ADD_BASKET)
        assert price_after_click_add.text in price_before_click_add.text, "Цена товара в каталоге и в корзине отличаются"
       