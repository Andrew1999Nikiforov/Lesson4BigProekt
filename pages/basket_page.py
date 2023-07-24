from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By

class BasketPage(BasePage):
    
    def check_basket_is_empty(self):
        assert self.browser.find_element(By.ID, "content_inner").text in "Ваша корзина пуста", "В корзине имеются какие то товары"

