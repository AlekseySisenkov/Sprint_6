import random

import allure

from data import NAME_AND_FAMILY, ADDRESS
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step('Заполняем форму заказа')
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

    @allure.step('Проверяем успешность заказа')
    def check_order(self):
        return self.find_element_with_wait(OrderPageLocators.BUTTON_TO_CHECK_ORDER)

    @allure.step('Передаем различные параметры в параметризацию')
    def set_parameter(self, parameter):
        if parameter == 'up':
            return OrderPageLocators.BUTTON_ORDER_UP
        if parameter == 'down':
            return OrderPageLocators.BUTTON_ORDER_DOWN
        if parameter == 2:
            return OrderPageLocators.RENTAL_VAR1
        if parameter == 4:
            return OrderPageLocators.RENTAL_VAR2
        if parameter == 'black':
            return OrderPageLocators.CHECKBOX_BLACK
        if parameter =='grey':
            return OrderPageLocators.CHECKBOX_GREY




