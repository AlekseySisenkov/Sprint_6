from locators.header_page_locators import HeaderPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from pages.order_page import OrderPage


class HeaderPage(OrderPage):
    def make_order(self):
        self.click_element(OrderPageLocators.BUTTON_ORDER_UP)
        self.set_order_form(OrderPageLocators.RENTAL_VAR1, OrderPageLocators.CHECKBOX_GREY, '')
        self.click_element(OrderPageLocators.BUTTON_TO_CHECK_ORDER)


class DzenPage(BasePage):
    def close_window(self):
        self.click_element(HeaderPageLocators.BUTTON_CLOSE)
