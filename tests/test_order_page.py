import allure
import pytest

from locators.order_page_locators import OrderPageLocators


class TestOrderPage:
    @pytest.mark.parametrize(
        "button_order, rental, checkbox, text", [
            ('up', 2, 'black', 'No comments'),
            ('down', 4, 'grey', 'Live fast, die young')
        ])
    @allure.title('Проверка заказа самоката')
    def test_pop_up_window(self, main_page, order_page, button_order, rental, checkbox, text):
        order_page.skrooll_to_element(order_page.set_parameter(button_order))
        order_page.click_element(order_page.set_parameter(button_order))
        order_page.set_order_form(order_page.set_parameter(rental), order_page.set_parameter(checkbox), text)
        assert order_page.check_order()

