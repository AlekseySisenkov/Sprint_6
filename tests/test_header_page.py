import allure


class TestHeaderPage:
    @allure.title('Проверка перехода на главную страницу «Самоката» при нажатии на логотип «Самоката»')
    def test_logo_scooter(self, main_page, header_page):
        header_page.make_order()
        header_page.click_to_scooter()
        assert header_page.check_scooter()

    @allure.title('Проверка перехода на главную страницу Дзена при нажатии на логотип Яндекса')
    def test_logo_yandex(self, main_page, header_page, dzen_page):
        header_page.make_order()
        header_page.click_to_yandex()
        dzen_page.switch_to_dzen()
        assert 'dzen' in dzen_page.get_dzen() and 'redirect=true' in dzen_page.url_dzen()
