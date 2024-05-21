import pyodbc
import pandas as pd
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
#
from selenium.webdriver.common.action_chains import ActionChains

class BasePageElementUsername(object):
    try:
        USERNAME = (By.NAME, "LoginForm[username]")
    except:      
        pass

class BasePageElementPass(object):
    try:
        PASSWORD = (By.NAME, "LoginForm[password]")
    except:      
        pass

class MainPageLocator(object):
    try:
        GO_BUTTON = (By.ID, "sbm")
        BUTTON_PRE_ORDER = (By.ID, "btn-pre-order-entry")
    except:      
        pass
class SearchResultPageLocators(object):
    pass

