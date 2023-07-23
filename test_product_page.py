from .pages.product_page import ProductPage
import time
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.check_before_add_name_product()
    page.click_to_button_add_busket()
    page.solve_quiz_and_get_code()
    page.check_after_add_name_product()
    page.check_price_before_and_after_add_basket()
    time.sleep(10)