import pyodbc
import pandas as pd
import difflib
import importlib.util

from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from importlib.machinery import SourceFileLoader

class BasePage(object):
    def __init__ (self,driver):
        self.driver = driver

class MainPage(BasePage):
    def click_button_pre_order(self):
        mainPage = SourceFileLoader("locator","script/MEGAZIP/CONFIG/CONFIG_PAGE/locator.py").load_module() 
        mainPage = mainPage.MainPageLocator()
        try:
            element = self.driver.find_element(*mainPage.BUTTON_PRE_ORDER)
            element.click()
        except:
            pass
    
class SearchResultPage(BasePage):
    def is_results_found(self):
        return "No result found." not in self.driver.page_source