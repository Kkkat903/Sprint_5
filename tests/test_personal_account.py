from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Data as d
from locators import Locators as ls


class TestPersonalAccount:
    def test_personal_account_transition(self,login):
        login.find_element(*ls.PERSONAL_ACCOUNT).click()
        WebDriverWait(login, 10).until( EC.url_to_be("https://stellarburgers.education-services.ru/account/profile"))

        assert login.current_url.endswith("/account/profile")

    def test_switching_to_constructor(self,login):
        login.find_element(*ls.PERSONAL_ACCOUNT).click()
        login.find_element(*ls.CONSTRUCTOR_BUTTON).click()

        assert login.find_element(*ls.PLACE_AN_ORDER_BUTTON).is_displayed()

    def test_logout_from_account(self,login):
        login.find_element(*ls.PERSONAL_ACCOUNT).click()
        WebDriverWait(login, 10).until(EC.url_to_be("https://stellarburgers.education-services.ru/account/profile"))
        login.find_element(*ls.LOGOUT_BUTTON).click()
        WebDriverWait(login,10).until(EC.url_to_be(d.LOGIN_URL))

        assert login.current_url.endswith("/login")

    def test_click_logo(self,login):
        login.find_element(*ls.PERSONAL_ACCOUNT).click()
        WebDriverWait(login, 10).until(EC.url_to_be("https://stellarburgers.education-services.ru/account/profile"))
        login.find_element(*ls.LOGO_BUTTON).click()
        WebDriverWait(login, 10).until(EC.url_to_be(d.MAIN_PAGE_URL))

        assert login.find_element(*ls.PLACE_AN_ORDER_BUTTON).is_displayed()