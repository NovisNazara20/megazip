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
    global nameRep  
    global header 
    
    nameRep = f"Log/{datetime.today().strftime('%Y')}/{datetime.today().strftime('%m')}/{datetime.today().strftime('%d')}/LogReportNMC.txt"
    if not os.path.exists(os.path.dirname(nameRep)):
        os.makedirs(os.path.dirname(nameRep))

    with open(nameRep, 'a', encoding='UTF8', newline='') as f:
            writer = csv.writer(f,delimiter=';')
            headers = ['Scenario type','Scenario information','Result',"Ekspetasi Value","Actual Value","Process Date"]
            writer.writerow(headers)

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path='C:\driverfirefox\geckodriver.exe')
        self.driver.get("http://uatmegazip.megafinance.co.id/index.php/site/login")
        
    def test_search_python (self):
        mainPage = SourceFileLoader("page","script/MEGAZIP/MENU/page.py").load_module() 
        mainPage = mainPage.MainPage(self.driver)
        dbCon =   SourceFileLoader("configPmf","config/configPmf.py").load_module()
        print('saya')
        query = dbCon.DbPMF(query = "UPDATE TU_USER SET is_login_mzip = 0 WHERE NIK = '202100317'")
        query.commit()

        vara = SourceFileLoader("variable","script/MEGAZIP/MENU/MENU_MZIP/MENU/variable.py").load_module() 
        vara = vara.VariableCreateProgram(self)
        print(vara)
        
        mainPage.username()
        sleep(1)

        mainPage.password()
        sleep(1)

        #Button Login
        mainPage.click_go_button()
        sleep(2)
        
        pageMenu =  SourceFileLoader("menu","script/MEGAZIP/MENU/MENU_MZIP/MENU/LIST_MENU/listMenu.py").load_module()  
        pageMenu.MainPage.programRate(self)
        sleep(2)

        create =  SourceFileLoader("menu","script/MEGAZIP/MENU/MENU_MZIP/MENU/menuProgramRate.py").load_module()  
        create.MainPage.createRateProgram(self)
        sleep(2)

        create =  SourceFileLoader("menu","script/MEGAZIP/MENU/MENU_MZIP/MENU/menuProgramRate.py").load_module()  
        create.MainPage.program(self,vara)
        sleep(2)

        

if __name__ == "__main__":
    unittest.main()

        