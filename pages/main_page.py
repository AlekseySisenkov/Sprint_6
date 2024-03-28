import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Раскрываем ответ на вопрос')
    def click_question_get_answer(self, num):
        self.click_element(self.set_number_to_locator(MainPageLocators.QUESTION, num))
        return self.get_text(self.set_number_to_locator(MainPageLocators.ANSWER, num))

    @allure.step('Закрываем всплывающее окно про куки')
    def close_cookie(self):
        self.click_element(MainPageLocators.COOKIE)

    @allure.step('Прокручиваем вниз страницы')
    def skrooll_to_down(self):
        self.skrooll_to_element(MainPageLocators.DOWN_MAIN_PAGE)

    @staticmethod
    @allure.step('Проверяем ответ')
    def check_answer(result, expected):
        return result == expected
