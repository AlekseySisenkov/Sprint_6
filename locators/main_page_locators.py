from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTION = By.ID, 'accordion__heading-{}'
    ANSWER = By.XPATH, '//div[@id="accordion__panel-{}"]/p'
    COOKIE = By.ID, 'rcc-confirm-button'
    DOWN_MAIN_PAGE = By.ID, 'accordion__heading-7'
