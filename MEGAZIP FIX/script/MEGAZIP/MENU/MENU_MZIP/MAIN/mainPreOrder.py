import unittest
import pyodbc
import difflib
import importlib.util
import sys
import csv
import os
from datetime import datetime
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

class PythonOrgSearchTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path='C:\driverfirefox\geckodriver.exe')
        self.driver.get("http://uatmegazip.megafinance.co.id/index.php/site/login")
        
    def test_search_python (self):
        mainPage = SourceFileLoader("page","script/MEGAZIP/CONFIG/CONFIG_PAGE/page.py").load_module() 
        mainPage = mainPage.MainPage(self.driver)
    
        dbCon =   SourceFileLoader("configPmf","script/MEGAZIP/CONFIG/CONFIG_DB/configPmf.py").load_module()
        query = dbCon.DbPMF(query = "UPDATE TU_USER SET is_login_mzip = 0 WHERE NIK = '202100317'")
        query.commit()

        array_input = SourceFileLoader("var_login","script/MEGAZIP/CONFIG/CONFIG_PAGE/array_login.py").load_module()
        array = array_input.var_login_novis(self)  
        
        #login
        pageLogin =  SourceFileLoader("login","script/MEGAZIP/CONFIG/CONFIG_PAGE/login.py").load_module()  
        pageLogin.MainPage.username(self,array)
        pageLogin.MainPage.password(self,array)
        pageLogin.MainPage.click_go_button(self)
        sleep(2)

        pageListMenu =  SourceFileLoader("menu","script/MEGAZIP/MENU/MENU_MZIP/LIST_MENU/listMenu.py").load_module()  
        pageListMenu.MainPage.preOrderEntry(self)
        sleep(2)

        mainPage.click_button_pre_order()
        sleep(1)

        # create =  SourceFileLoader("menu","script/MEGAZIP/MENU/MENU_MZIP/MENU/menuProgramRate.py").load_module()  
        # create.MainPage.createRateProgram(self)
        # sleep(2)

        # create =  SourceFileLoader("menu","script/MEGAZIP/MENU/MENU_MZIP/MENU/menuProgramRate.py").load_module()  
        # create.MainPage.program(self,vara)
        # sleep(2)

if __name__ == "__main__":
    unittest.main()

        