from selenium.webdriver.common.by import By


class OrderPageLocators:
    BUTTON_ORDER_UP = By.XPATH, '//div[@class="Header_Nav__AGCXC"]/button[text()="Заказать"]'
    BUTTON_ORDER_DOWN = By.XPATH, '//div[@class="Home_FinishButton__1_cWm"]/button[text()="Заказать"]'
    NAME = By.XPATH, '//input[@placeholder="* Имя"]'
    FAMILY = By.XPATH, '//input[@placeholder="* Фамилия"]'
    ADDRESS = By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]'
    METRO = By.XPATH, '//div[@class="select-search__value"]'
    STATION_METRO = By.XPATH, '//div[@class="select-search__select"]/ul/li[@data-index="{}"]'
    TELEPHONE = By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]'
    BUTTON_TO_RENT = By.XPATH, '//button[text()="Далее"]'
    DATE = By.XPATH, '//input[@placeholder="* Когда привезти самокат"]'
    ACCEPT_DATE = By.XPATH, '//div[@class="Order_Header__BZXOb" and text()="Про аренду"]'
    RENTAL_PERIOD = By.XPATH, '//div[@class="Dropdown-root"]'
    RENTAL_VAR1 = By.XPATH, '//div[@class="Dropdown-option" and text()="двое суток"]'
    RENTAL_VAR2 = By.XPATH, '//div[@class="Dropdown-option" and text()="четверо суток"]'
    CHECKBOX_BLACK = By.XPATH, '//input[@id="black"]'
    CHECKBOX_GREY = By.XPATH, '//input[@id="grey"]'
    COMMENT = By.XPATH, '//input[@placeholder="Комментарий для курьера"]'
    BUTTON_TO_BACK = By.XPATH, '//button[text()="Назад"]'
    BUTTON_TO_FINALLY_ORDER = By.XPATH, '//div[@class="Order_Buttons__1xGrp"]/button[text()="Заказать"]'
    BUTTON_NO = By.XPATH, '//button[text()="Нет"]'
    BUTTON_YES = By.XPATH, '//button[text()="Да"]'
    BUTTON_TO_CHECK_ORDER = By.XPATH, '//button[text()="Посмотреть статус"]'

