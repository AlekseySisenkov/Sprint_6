import random

from data import NAME_AND_FAMILY, ADDRESS
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    def set_order_form(self, rental, checkbox, text):
        self.set_text_to_field(OrderPageLocators.NAME, NAME_AND_FAMILY)
        self.set_text_to_field(OrderPageLocators.FAMILY, NAME_AND_FAMILY)
        self.set_text_to_field(OrderPageLocators.ADDRESS, ADDRESS)
        self.select_drop_down_menu_item(OrderPageLocators.METRO,
                                        self.set_number_to_locator(OrderPageLocators.STATION_METRO,
                                                                   random.randint(0, 224)))
        self.set_text_to_field(OrderPageLocators.TELEPHONE, random.randint(10000000000, 99999999999))
        self.click_element(OrderPageLocators.BUTTON_TO_RENT)
        self.set_text_to_field(OrderPageLocators.DATE, random.randint(1, 99999))
        self.click_element(OrderPageLocators.ACCEPT_DATE)
        self.select_drop_down_menu_item(OrderPageLocators.RENTAL_PERIOD, rental)
        self.click_element(checkbox)
        self.set_text_to_field(OrderPageLocators.COMMENT, text)
        self.click_element(OrderPageLocators.BUTTON_TO_BACK)
        self.click_element(OrderPageLocators.BUTTON_TO_RENT)
        self.click_element(OrderPageLocators.BUTTON_TO_FINALLY_ORDER)
        self.click_element(OrderPageLocators.BUTTON_NO)
        self.click_element(OrderPageLocators.BUTTON_TO_FINALLY_ORDER)
        self.click_element(OrderPageLocators.BUTTON_YES)


