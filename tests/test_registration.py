from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Data as d
from locators import Locators as ls
from generators import generate_email, generate_name, generate_password

class TestRegistration:
    def test_successful_registration(self, driver):
        driver.get(d.REGISTER)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(ls.NAME_INPUT))
        
        name = generate_name()
        email = generate_email()
        password = generate_password()

        driver.find_element(*ls.NAME_INPUT).send_keys(name)
        driver.find_element(*ls.EMAIL_INPUT).send_keys(email)
        driver.find_element(*ls.PASSWORD_INPUT).send_keys(password)

        driver.find_element(*ls.REGISTRATION).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(ls.LOGIN_BUTTON))
        
        assert driver.current_url.endswith("/login")

    def test_invalid_password_error(self, driver):
        driver.get(d.REGISTER)

        name = generate_name()
        email = generate_email()

        driver.find_element(*ls.NAME_INPUT).send_keys(name)
        driver.find_element(*ls.EMAIL_INPUT).send_keys(email)
        driver.find_element(*ls.PASSWORD_INPUT).send_keys("12345")

        driver.find_element(*ls.REGISTRATION).click()

        error = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(ls.ERROR_TEXT))
        assert error.is_displayed()
        assert "Некорректный пароль" in error.text