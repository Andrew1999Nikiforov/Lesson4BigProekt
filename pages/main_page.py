from .base_page import BasePage
from .locators import MainPageLocators
from .basket_page import BasketPage

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
