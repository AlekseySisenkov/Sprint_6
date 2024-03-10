from locators.header_page_locators import HeaderPageLocators


class TestHeaderPage:
    def test_logo_scooter(self, main_page, header_page):
        header_page.make_order()
        header_page.click_element(HeaderPageLocators.LOGO_SCOOTER)
        assert header_page.find_element_with_wait(HeaderPageLocators.IMG_SCOOTER)

    def test_logo_yandex(self, main_page, header_page, dzen_page):
        header_page.make_order()
        header_page.click_element(HeaderPageLocators.LOGO_YANDEX)
        dzen_page.close_window()
        assert dzen_page.find_element_with_wait(HeaderPageLocators.LOGO_DZEN)
