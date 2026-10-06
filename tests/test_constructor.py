from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Data as d
from locators import Locators as ls


class TestConstructor:
    def test_constructor_sauces(self, login):
        WebDriverWait(login, 10).until(EC.visibility_of_element_located(ls.BUNS_TAB_ACTIVE))
        login.find_element(*ls.SAUCES_BUTTON).click()
        WebDriverWait(login, 5).until(EC.visibility_of_element_located(ls.SAUCES_TAB_ACTIVE))
        
        assert login.find_element(*ls.SAUCES_TAB_ACTIVE).is_displayed()

    def test_constructor_buns(self,login):
        WebDriverWait(login, 10).until(EC.visibility_of_element_located(ls.BUNS_TAB_ACTIVE))
        login.find_element(*ls.SAUCES_BUTTON).click()
        WebDriverWait(login, 5).until(EC.visibility_of_element_located(ls.SAUCES_TAB_ACTIVE))
        login.find_element(*ls.BUNS_BUTTON).click()

        assert login.find_element(*ls.BUNS_TAB_ACTIVE).is_displayed()

    def test_constructor_fillings(self, login):
        WebDriverWait(login, 10).until(EC.visibility_of_element_located(ls.BUNS_TAB_ACTIVE))
        login.find_element(*ls.FILLINGS_BUTTON).click()
        WebDriverWait(login, 5).until(EC.visibility_of_element_located(ls.FILLINGS_TAB_ACTIVE))
        
        assert login.find_element(*ls.FILLINGS_TAB_ACTIVE).is_displayed()