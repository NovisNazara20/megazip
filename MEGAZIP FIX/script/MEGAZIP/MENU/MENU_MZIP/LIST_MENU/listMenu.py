import unittest
import random
import string
#
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

class BasePage(object):
    def __init__ (self,driver):
        self.driver = driver

class MainPage(BasePage): 
    def programRate(self): 
        self.driver.get('http://uatmegazip.megafinance.co.id/index.php/base/rateProgram/admin')
    
    def deskCall(self): 
        self.driver.get('http://uatmegazip.megafinance.co.id/index.php/acquisition/survey/list')
    
    def surveyEntry(self): 
        self.driver.get('http://uatmegazip.megafinance.co.id/index.php/acquisition/ApplAnalisaKredit/admin')
    
    def salesSlip(self): 
        self.driver.get('http://uatmegazip.megafinance.co.id/index.php/acquisition/po/listSaleSlip')
    
    def tandaTerimaTagihan(self): 
        self.driver.get('http://uatmegazip.megafinance.co.id/index.php/acquisition/receipt/print')
    
    def preOrderEntry(self): 
        self.driver.get('http://uatmegazip.megafinance.co.id/index.php/acquisition/application/preOrder')

    def POBE(self): 
        self.driver.get('http://uatmegazip.megafinance.co.id/index.php/acquisition/application/updateAdminEntryPages/appl_id/2022100195/page/1')  
    
