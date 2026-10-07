import pytest
from selenium import webdriver
from data import Data as d
from locators import Locators as ls

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture()
def login(driver):
    driver.get(d.LOGIN_URL)

    driver.find_element(*ls.EMAIL_INPUT).send_keys(d.EMAIL)
    driver.find_element(*ls.PASSWORD_INPUT).send_keys(d.PASSWORD)
    driver.find_element(*ls.LOGIN_BUTTON).click()

    return driver
