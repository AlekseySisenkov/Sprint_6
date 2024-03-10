from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 15).until(expected_conditions.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    def skrooll_to_element(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.find_element_with_wait(locator))

    def click_element(self, locator):
        self.find_element_with_wait(locator).click()

    def get_text(self, locator):
        return self.find_element_with_wait(locator).text

    def set_text_to_field(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def select_drop_down_menu_item(self, locator_menu, locator_item):
        self.click_element(locator_menu)
        self.skrooll_to_element(locator_item)
        self.click_element(locator_item)

    @staticmethod
    def set_number_to_locator(locator_num, num):
        method, locator = locator_num
        locator = locator.format(num)
        return method, locator
