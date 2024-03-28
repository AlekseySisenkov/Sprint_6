import pytest
from selenium import webdriver

from data import MAIN_PAGE_REF
from pages.header_page import HeaderPage, DzenPage
from pages.main_page import MainPage
from pages.order_page import OrderPage


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()

    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def main_page(driver):
    driver.get(MAIN_PAGE_REF)
    return MainPage(driver)


@pytest.fixture(scope='function')
def order_page(driver):
    return OrderPage(driver)


@pytest.fixture(scope='function')
def header_page(driver):
    return HeaderPage(driver)


@pytest.fixture(scope='function')
def dzen_page(driver):
    return DzenPage(driver)
