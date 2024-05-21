from array import array
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from importlib.machinery import SourceFileLoader

class BasePage(object):
    def __init__ (self,driver):
        self.driver = driver

class VariablePage1(BasePage):
    array = {}
    array["NamaLengkap"]              = "ANANDA CITRA ISLAMI"
