import allure

from locators.header_page_locators import HeaderPageLocators, DzenPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.order_page import OrderPage


class HeaderPage(OrderPage):
    @allure.step('Переходим на страницу после заказа')
    def make_order(self):
        self.click_element(OrderPageLocators.BUTTON_ORDER_UP)
        self.set_order_form(OrderPageLocators.RENTAL_VAR1, OrderPageLocators.CHECKBOX_GREY, '')
        self.click_element(OrderPageLocators.BUTTON_TO_CHECK_ORDER)

    @allure.step('Нажимаем на логотип "Самоката"')
    def click_to_scooter(self):
        self.click_element(HeaderPageLocators.LOGO_SCOOTER)

    @allure.step('Проверка перехода на главную страницу "Самоката"')
    def check_scooter(self):
        return self.find_element_with_wait(HeaderPageLocators.IMG_SCOOTER)

    @allure.step('Нажимаем на логотип Яндекса')
    def click_to_yandex(self):
        self.click_element(HeaderPageLocators.LOGO_YANDEX)


class DzenPage(OrderPage):

    @allure.step('Переключение на новую вкладку')
    def switch_to_dzen(self):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])

    @allure.step('Проверка перехода на страницу Дзен')
    def get_dzen(self):
        return self.find_element_with_wait(DzenPageLocators.DZEN).get_attribute('class')

    @allure.step('Просмотр URL Дзена')
    def url_dzen(self):
        self.find_element_with_wait(DzenPageLocators.DZEN)
        return self.get_url()
