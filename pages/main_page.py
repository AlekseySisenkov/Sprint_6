from pages.base_page import BasePage


class MainPage(BasePage):

    def click_question_get_answer(self, question, answer, num):
        self.click_element(self.set_number_to_locator(question, num))
        return self.get_text(self.set_number_to_locator(answer, num))

    @staticmethod
    def check_answer(result, expected):
        return result == expected
