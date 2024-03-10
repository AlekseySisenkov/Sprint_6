import pytest

from data import Answer
from locators.main_page_locators import MainPageLocators


class TestMainPage:
    @pytest.mark.parametrize(
        "num, expected", [
            (0, Answer.TO_QUESTION_0),
            (1, Answer.TO_QUESTION_1),
            (2, Answer.TO_QUESTION_2),
            (3, Answer.TO_QUESTION_3),
            (4, Answer.TO_QUESTION_4),
            (5, Answer.TO_QUESTION_5),
            (6, Answer.TO_QUESTION_6),
            (7, Answer.TO_QUESTION_7)
        ])
    def test_questions(self, main_page, num, expected):
        main_page.click_element(MainPageLocators.COOKIE)
        main_page.skrooll_to_element(MainPageLocators.DOWN_MAIN_PAGE)
        result = main_page.click_question_get_answer(MainPageLocators.QUESTION, MainPageLocators.ANSWER, num)
        assert main_page.check_answer(result, expected)
