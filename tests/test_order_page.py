import pytest

from locators.order_page_locators import OrderPageLocators


class TestOrderPage:
    @pytest.mark.parametrize(
        "button_order, rental, checkbox, text", [
            (OrderPageLocators.BUTTON_ORDER_UP, OrderPageLocators.RENTAL_VAR1,
             OrderPageLocators.CHECKBOX_BLACK, 'No comments'),
            (OrderPageLocators.BUTTON_ORDER_DOWN, OrderPageLocators.RENTAL_VAR2,
             OrderPageLocators.CHECKBOX_GREY, 'Live fast, die young')
        ])
    def test_pop_up_window(self, main_page, order_page, button_order, rental, checkbox, text):
        order_page.skrooll_to_element(button_order)
        order_page.click_element(button_order)
        order_page.set_order_form(rental, checkbox, text)
        assert main_page.find_element_with_wait(OrderPageLocators.BUTTON_TO_CHECK_ORDER)

