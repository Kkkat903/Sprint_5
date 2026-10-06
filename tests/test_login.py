from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Data as d
from locators import Locators as ls
from generators import generate_email, generate_name, generate_password


def login(driver):
    driver.find_element(*ls.EMAIL_INPUT).send_keys(d.EMAIL)
    driver.find_element(*ls.PASSWORD_INPUT).send_keys(d.PASSWORD)
    driver.find_element(*ls.LOGIN_BUTTON).click()


class TestLogin:
    def test_login_from_main_page(self, driver):
        driver.get(d.MAIN_PAGE_URL)
        driver.find_element(*ls.SING_IN_BUTTON).click()

        login(driver)

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(ls.PLACE_AN_ORDER_BUTTON))

        assert driver.find_element(*ls.PLACE_AN_ORDER_BUTTON).is_displayed()

    def test_login_from_personal_account(self, driver):
        driver.get(d.MAIN_PAGE_URL)
        driver.find_element(*ls.PERSONAL_ACCOUNT).click()

        login(driver)

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(ls.PLACE_AN_ORDER_BUTTON))

        assert driver.find_element(*ls.PLACE_AN_ORDER_BUTTON).is_displayed()

    def test_login_from_registration_form(self, driver):
        driver.get(d.REGISTER)
        driver.find_element(*ls.SING_IN_BUTTON_REGFORM).click()

        login(driver)

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(ls.PLACE_AN_ORDER_BUTTON))

        assert driver.find_element(*ls.PLACE_AN_ORDER_BUTTON).is_displayed()

    def test_login_from_password_recovery_form(self, driver):
        driver.get(d.PASSWORD_RECOVERY_FORM_URL)
        driver.find_element(*ls.SING_IN_BUTTON_REGFORM).click()

        login(driver)
        
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(ls.PLACE_AN_ORDER_BUTTON))

        assert driver.find_element(*ls.PLACE_AN_ORDER_BUTTON).is_displayed()
