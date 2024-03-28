import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    @allure.step('Инициализация драйвера')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Поиск элемента с ожиданием')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 15).until(expected_conditions.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Прокрутка до элемента')
    def skrooll_to_element(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.find_element_with_wait(locator))

    @allure.step('Нажатие на элемент')
    def click_element(self, locator):
        self.find_element_with_wait(locator).click()

    @allure.step('Получение текста элемента')
    def get_text(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step('Ввод текста в поле')
    def set_text_to_field(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step('Выбор пункта в выпадающем меню')
    def select_drop_down_menu_item(self, locator_menu, locator_item):
        self.click_element(locator_menu)
        self.skrooll_to_element(locator_item)
        self.click_element(locator_item)

    @staticmethod
    @allure.step('Добавление номера в метку')
    def set_number_to_locator(locator_num, num):
        method, locator = locator_num
        locator = locator.format(num)
        return method, locator

    @allure.step('Просмотр текущего URL')
    def get_url(self):
        return self.driver.current_url
